---
title: "KMODE_EXCEPTION_NOT_HANDLED: The Best Way to Fix It"
slug: best-way-to-fix-kmode-exception-not-handled
date: 2026-09-08
categories: ["windows-errors"]
tags: ["kmode-exception-not-handled", "bsod", "driver"]
description: "The best way to fix KMODE_EXCEPTION_NOT_HANDLED: read the dump, fix the named driver, then test RAM. Ranked carefully by what works most often."
thumbnail: "/images/thumbs/best-way-to-fix-kmode-exception-not-handled.webp"
faqs:
  - q: "What is the fastest fix for KMODE_EXCEPTION_NOT_HANDLED?"
    a: "Updating the driver named on the blue screen or in the minidump. When the same .sys file appears across crashes, a driver update or rollback resolves it more often than everything else combined — and takes about fifteen minutes. Always start with the named file."
  - q: "Should I update all my drivers or just the named one?"
    a: "Just the named one first. Mass-updating every driver introduces new variables and occasionally new bugs. If the named driver is current or updating it fails, then broaden to graphics, chipset, and storage drivers — the categories most likely to throw kernel exceptions."
  - q: "Can this error be caused by Windows itself?"
    a: "Yes — corrupted Windows system files make even correct drivers throw exceptions, which is why SFC and DISM are in the fix order. But genuine Microsoft-driver bugs are rare; when a Windows .sys file is named, file corruption is far more likely than a Microsoft bug."
  - q: "How many minidumps should I check before acting?"
    a: "At least two or three. One dump can implicate a bystander driver that happened to be running when memory corruption struck. Two or three dumps agreeing on the same driver is a solid diagnosis; dumps disagreeing with each other point at RAM instead."
---
KMODE_EXCEPTION_NOT_HANDLED (stop code 0x1E) means a kernel-mode driver hit an error it could not handle, and Windows stopped everything rather than continue in an unknown state. The blue screen usually names the driver — which makes this one of the most directly fixable blue screens there is. KMODE_EXCEPTION_NOT_HANDLED (stop code 0x1E) means a kernel-mode driver hit an error it could not handle, and Windows stopped everything rather than continue in an unknown state. The blue screen usually names the driver — which makes this one of the most directly fixable blue screens there is.

The best way to fix it is ranked, not random: trust the named driver first, verify with dumps, fix that driver, then rule out RAM and system corruption. Here is the order. The best way to fix it is ranked, not random: trust the named driver first, verify with dumps, fix that driver, then rule out RAM and system corruption. Here is the order that wastes the least time.

## Why this happens

- **An outdated or buggy driver.** The named file on the screen is the cause more often than not.
- **A driver broken by a Windows update.** Updates change kernel interfaces; lagging drivers throw exceptions.
- **Corrupted driver files.** Disk damage makes a good driver throw on load.
- **Faulty RAM.** Corrupts drivers in memory so innocent ones throw — dumps name different files each time.
- **Antivirus filter drivers.** Deep kernel hooks plus update lag equals exceptions.
- **Overclocking instability.** Corrupts execution state so drivers fault randomly.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Fix the named driver first

Highest success rate, least effort — the screen already told you the answer. Highest success rate, least effort — the screen already told you the answer, so act on it before anything else.

1. Write down the exact `.sys` filename from the blue screen.
2. Search it online to identify the product (e.g., `netwtw10.sys` is Intel Wi-Fi).
3. Download the latest version from the manufacturer's site and install it — or roll back in **Device Manager > Properties > Driver > Roll Back Driver** if the trouble started after an update.
4. Restart and reproduce the crash scenario. If the same file was named across multiple crashes, this resolves it most of the time.

### Fix 2: Confirm across multiple dumps

One dump can lie; three rarely do. One dump can lie; three rarely do — agreement across dumps is what turns a hint into a diagnosis worth acting on.

1. Open the two or three newest dumps in `C:\Windows\Minidump` with WinDbg Preview, running `!analyze -v` on each.
2. If all agree on the same IMAGE_NAME, your diagnosis is solid — proceed with that driver.
3. If they disagree, skip ahead to the RAM test (Fix 4) — chasing drivers on disagreeing dumps wastes days. Our [KMODE troubleshooting guide](/articles/kmode-exception-not-handled-troubleshooting/) covers the full diagnostic method.

### Fix 3: Broaden the driver update if needed

For when the named driver is already current or the screen named a Windows file. For when the named driver is already current or the screen named a Windows file — broaden systematically, not randomly.

1. Update graphics, chipset, network, and storage drivers from your laptop maker's support site.
2. If a Windows file like `ntoskrnl.exe` is named, that usually means corruption or RAM — run the SFC/DISM step next rather than hunting a Microsoft bug.
3. Uninstall recently added hardware and its drivers as a test — new devices bring new kernel drivers.

### Fix 4: Test the RAM

The definitive check for the disagreeing-dumps pattern. The definitive check for the disagreeing-dumps pattern — errors mean hardware, clean plus consistent dumps means trust the driver diagnosis.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Errors mean reseat or replace the RAM. Clean plus consistent dumps means the driver diagnosis stands — do not second-guess it.

### Fix 5: Repair system files

Catches the corruption case, especially when Windows files are named. Catches the corruption case, especially when Windows files are named — SFC repairs what the dumps implicate.

1. In an elevated **Command Prompt**, run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` and restart.
3. If SFC repaired files and the named driver was a Windows .sys file, retest for several days — this is frequently the whole fix.

### Fix 6: Clean-boot and remove filter drivers

Isolates the antivirus, VPN, and utility drivers that cause a disproportionate share of 0x1E crashes. Isolates the antivirus, VPN, and utility drivers that cause a disproportionate share of 0x1E crashes — the clean boot finds them by elimination.

1. Run `msconfig`, hide Microsoft services, **Disable all**; disable all startup items in Task Manager; restart.
2. If stable, re-enable in halves to find the culprit.
3. Pay special attention to antivirus and VPN products — clean-reinstall or replace the one that triggers it. For related driver-fault crashes, see our [IRQL guide](/articles/irql-not-less-or-equal-windows-11-fix/).

### Fix 7: Reset tuning and consider a repair install

The last steps when everything else is clean. The last steps when everything else is clean — stock tuning first, then the in-place upgrade, then professional diagnostics.

1. Load BIOS defaults, remove undervolts/overclocks, disable XMP.
2. If crashes persist with a confirmed driver fix, clean RAM, and repaired files, do an in-place upgrade from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) keeping files and apps.
3. Still crashing after that points at motherboard or CPU — professional diagnostics.

### Fix 8: Check for conflicting driver versions

Two versions of the same driver — one from Windows Update, one from the vendor installer — can conflict and throw exceptions that neither version causes alone.

1. In **Device Manager**, check the **Driver** tab version for the suspect device and compare it against the version on the vendor's site.
2. If they differ unexpectedly, do a full uninstall with **Attempt to remove the driver** ticked, then install exactly one known version.
3. Use the **Show hidden devices** view (**View > Show hidden devices**) to spot ghosted duplicate devices from old installs and uninstall those too.
4. One driver, one version, one source — that is the configuration that does not throw.

## Closing

The best way to fix KMODE_EXCEPTION_NOT_HANDLED is to believe the blue screen: it names the driver, and that driver is guilty until the dumps say otherwise. Fix it, verify with a second dump, and only broaden the search if the evidence disagrees. Ranked fixing beats random fixing every time. Ranked fixing is a discipline: resist the urge to 'just update everything' and you will fix this faster — and actually know what fixed it.
