---
title: "How to Fix the KMODE_EXCEPTION_NOT_HANDLED Blue Screen"
slug: kmode-exception-not-handled-blue-screen-error-fix
date: 2026-10-10
categories: ["windows-errors"]
tags: ["blue screen", "driver error", "bsod fix"]
description: "KMODE_EXCEPTION_NOT_HANDLED crashing your laptop? This guide shows how to identify the faulty driver and fix the blue screen step by step."
thumbnail: "/images/thumbs/kmode-exception-not-handled-blue-screen-error-fix.webp"
faqs:
  - q: "What does KMODE_EXCEPTION_NOT_HANDLED mean in simple terms?"
    a: "A program running in kernel mode — the privileged part of Windows where drivers live — caused an exception (error) that the error handler couldn't deal with. Windows stops everything with a blue screen rather than let a privileged crash corrupt your data. The stop code is 0x0000001E."
  - q: "Why does it name a different file each time?"
    a: "When the named file keeps changing, no single driver is at fault — something systemic is corrupting kernel memory. Failing RAM and unstable overclocks are the two big causes. Test the memory and reset the BIOS to stock speeds before chasing individual drivers."
  - q: "Is Driver Verifier safe to use?"
    a: "Mostly, yes — but it intentionally crashes your system when it catches the bad driver, so save your work first and know how to boot into Safe Mode to run verifier /reset. Only verify unsigned or suspect drivers rather than everything, to keep the system usable during testing."
  - q: "Can Windows Update cause this blue screen?"
    a: "Absolutely — it's one of the most common triggers. Updates frequently replace working drivers with newer-but-buggier ones, especially network and storage drivers. If crashes started right after Patch Tuesday, rolling back the suspect driver is Fix 1 for a reason."
---

KMODE_EXCEPTION_NOT_HANDLED is Windows-speak for 'a kernel-mode program did something illegal and I had to stop it.' In plain terms: a driver crashed in a way Windows couldn't recover from. It's one of the most common blue screens on laptops, and it's very fixable.

The stop code sometimes names the guilty file right on the blue screen (like ntfs.sys or ndis.sys), which makes your job much easier. For more on reading these screens, see our [KMODE reference](/articles/best-way-to-fix-kmode-exception-not-handled/). The fixes below start with identifying the driver, then fixing it.

## Why this happens

- A corrupted or outdated driver — network, storage, and graphics drivers are the usual suspects.

- Two drivers conflicting, often after a Windows update replaces one but not the other.

- Overclocked CPU or RAM making kernel operations unstable.

- Corrupted system files that kernel-mode components depend on.

- Failing RAM corrupting kernel data structures.

- Third-party antivirus or firewall drivers hooking deep into the kernel.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Identify the failing driver

The blue screen or the crash dump usually names the file. Finding it turns a generic crash into a specific target.

1. Photograph the blue screen if it names a **.sys** file under the stop code.

2. After rebooting, open **Event Viewer > Windows Logs > System** and find the **BugCheck** entry for details.

3. For a definitive answer, analyze the dump file — our [dump analysis guide](/articles/best-way-to-read-dump-files-with-windbg/) shows how with WinDbg.

4. Common ones: **ntoskrnl.exe** (often RAM or drivers generally), **ndis.sys** (network driver), **ntfs.sys** (storage driver).

### Fix 2: Update or reinstall the suspect driver

Once you know the driver, replace it with a clean, current version from the manufacturer — not whatever Windows Update guessed.

1. Open **Device Manager**, find the device, right-click, and choose **Uninstall device**, ticking **Attempt to remove the driver**.

2. Restart the laptop.

3. Download the latest driver from the manufacturer's support site.

4. Install, restart again, and stress-test with normal use for a day or two.

### Fix 3: Run Driver Verifier carefully

If no driver is named, Driver Verifier stresses drivers until the bad one crashes — which sounds scary but is exactly the point: it names the culprit.

1. Press **Win + R**, type `verifier`, and press **Enter**.

2. Choose **Create standard settings**, then **Automatically select unsigned drivers** (safer) or select specific suspects.

3. Restart — the laptop will run slower, and the bad driver should trigger a blue screen naming it.

4. After identifying it, boot into Safe Mode, run `verifier /reset`, and fix the named driver. Read our [Driver Verifier guide](/articles/best-way-to-fix-driver-verifier-iomanager-violation/) before starting.

### Fix 4: Test the RAM

When the named file is ntoskrnl.exe or the culprit keeps changing, suspect the memory itself rather than any single driver.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.

2. For thorough testing, run **MemTest86** from a USB drive for at least 2 passes.

3. Check results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.

4. Replace any stick that shows errors — no software fix overcomes bad RAM.

### Fix 5: Repair system files

Kernel crashes can stem from corrupted Windows files rather than third-party drivers. Repair them before going deeper.

1. Open **Terminal (Admin)** from the **Win + X** menu.

2. Run `sfc /scannow`.

3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to finish.

4. Restart and monitor. Details for both tools are on [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 6: Remove overclocking and reset BIOS to defaults

Overclocks destabilize kernel operations first — Windows crashes in kernel mode long before apps show problems.

1. Enter BIOS/UEFI setup during boot (**F2**, **Del**, or **Esc**).

2. Disable any CPU overclock, **XMP/EXPO** memory profiles, or 'performance enhancement' presets.

3. Choose **Load Optimized Defaults** if available, then **Save & Exit**.

4. Test stability at stock settings for a few days.

### Fix 7: Temporarily remove third-party antivirus

Kernel-hooking security drivers are a classic KMODE cause. Testing without them is quick and reversible.

1. Download the vendor's official **removal tool** — normal uninstall often leaves the kernel driver behind.

2. Run the removal tool and restart.

3. Windows Security activates automatically, so you're still protected.

4. If crashes stop, reinstall the latest version of the antivirus or switch products.

### Fix 8: Update the BIOS and firmware

The kernel talks to hardware through firmware. Buggy BIOS/UEFI firmware and outdated CPU microcode cause kernel-mode crashes that look exactly like driver faults — and a firmware update fixes them at the source.

1. Press **Win + R**, type `msinfo32`, and note your current **BIOS Version/Date**.

2. Visit your laptop maker's support site and compare with the latest BIOS for your exact model.

3. Download it and apply the update with the laptop on AC power — don't interrupt it.

4. After updating, enter the BIOS and **Load Optimized Defaults** to clear any stale settings.

5. Save, boot normally, and monitor for crashes over the next few days.

## Closing

KMODE_EXCEPTION_NOT_HANDLED is Windows catching a driver red-handed — your whole job is identifying which one and replacing it. The .sys name on the blue screen or in the dump file is the shortcut; Driver Verifier is the fallback when there's no name. Work the list in order, and remember that a culprit that keeps changing names is really a RAM or overclocking problem wearing a driver costume. After the crashes stop, keep a simple log for a week: date, what you were doing, and the stop code if anything recurs. Patterns — 'always during video calls,' 'only on battery' — turn a fixed problem into a diagnosed one, and they're exactly what support asks for if you ever need to escalate.
