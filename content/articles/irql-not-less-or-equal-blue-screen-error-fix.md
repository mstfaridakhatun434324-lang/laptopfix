---
title: "IRQL_NOT_LESS_OR_EQUAL Blue Screen: How to Fix It"
slug: irql-not-less-or-equal-blue-screen-error-fix
date: 2026-10-06
categories: ["windows-errors"]
tags: ["IRQL_NOT_LESS_OR_EQUAL", "driver errors", "BSOD fixes"]
description: "Fix the IRQL_NOT_LESS_OR_EQUAL blue screen on Windows: identify the bad driver from the dump, update or roll back drivers, and test your RAM."
thumbnail: "/images/thumbs/irql-not-less-or-equal-blue-screen-error-fix.webp"
faqs:
  - q: "What does IRQL_NOT_LESS_OR_EQUAL mean in plain English?"
    a: "It means a driver tried to access memory it wasn't allowed to touch at its current privilege level. Windows organizes kernel work into priority levels (IRQLs), and drivers must follow strict rules about which memory they can access at each level. Stop code 0xA fires when a driver breaks those rules — almost always a driver bug, not broken hardware."
  - q: "Which driver usually causes IRQL_NOT_LESS_OR_EQUAL?"
    a: "Network drivers (Wi-Fi and Ethernet), graphics drivers, and storage drivers top the list. Antivirus filter drivers are frequent offenders too. The crash dump's IMAGE_NAME line usually names the exact file — commonly Netwtw10.sys (Intel Wi-Fi), nvlddmkm.sys (NVIDIA), or rtwlanu.sys (Realtek). Update or roll back whichever one the dump names."
  - q: "Can bad RAM cause IRQL_NOT_LESS_OR_EQUAL?"
    a: "Yes, though it's less common than driver bugs. Faulty RAM can corrupt the memory a driver is legitimately accessing, producing the same stop code. If every crash dump blames a different driver, test your RAM — inconsistent blame is the classic signature of a hardware memory problem rather than one bad driver."
  - q: "Why does this error happen after a Windows update?"
    a: "Updates change kernel timing and memory layout, which can expose latent bugs in older drivers that previously got lucky. Windows Update also sometimes replaces a manufacturer's tuned driver with a generic one. If the error started within days of an update, rolling back the driver or the update itself is the fastest diagnostic test."
---

IRQL_NOT_LESS_OR_EQUAL (stop code `0xA`) is the most famous blue screen in Windows, and the most fixable: in the overwhelming majority of cases, one driver accessed memory it shouldn't have, and replacing that driver ends the crashes. The trick is identifying *which* driver instead of updating everything blindly.

This guide shows you how to read the dump, name the driver, and fix it — plus what to do when the dumps disagree with each other. It's the single most efficient path through this particular blue screen. Lenovo owners should also check our [brand-specific IRQL guide](/articles/fix-irql-not-less-or-equal-on-lenovo-laptop/); the steps below work on every brand.

## Why this happens

- A buggy network driver (Wi-Fi/Ethernet) accessing paged memory at high IRQL.
- Outdated or corrupt graphics drivers mishandling memory under load.
- Antivirus or VPN filter drivers breaking kernel memory rules.
- Faulty RAM corrupting legitimately accessed memory regions.
- A Windows update exposing latent bugs in previously "working" drivers.
- Overclocked hardware (CPU/RAM) causing timing violations the driver can't survive.
- Corrupted driver installations where mismatched old and new driver files load side by side.

## How to fix it

Work through these in order — Fix 1 identifies the target, the rest fix it.

### Fix 1: Read the dump to name the driver

Five minutes here saves hours of blind driver updates.

1. Open the newest `.dmp` in `C:\Windows\Minidump` with **WinDbg Preview** (free, Microsoft Store).
2. Configure symbols once, then run `!analyze -v` in the command box.
3. Read the **IMAGE_NAME** line — that's your prime suspect (e.g. `Netwtw10.sys`).
4. Run `lmvm <drivername>` (without `.sys`) to see the vendor and timestamp.
5. Every fix below targets this specific driver first, everything else second.

### Fix 2: Update the named driver from the vendor

Get the driver from the people who wrote the hardware, not from Windows Update's generic pool.

1. For Intel Wi-Fi: use [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. For NVIDIA graphics: download from [NVIDIA's official page](https://www.nvidia.com/Download/index.aspx).
3. For Realtek or MediaTek, get the driver from your laptop maker's support site.
4. Install, restart, and test with the workload that crashed before.
5. If the newest driver still crashes, try the *previous* stable version — newest isn't always best.

### Fix 3: Roll back the driver

When the crash started right after a driver update, the old version was fine — go back to it.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Find the device, right-click, choose **Properties > Driver** tab.
3. Click **Roll Back Driver** and pick the reason; restart when done.
4. If the button is greyed out, download the older driver manually from the maker's archive.
5. Use Microsoft's **Show or Hide Updates** troubleshooter to block Windows from reinstalling the bad version.

### Fix 4: Remove antivirus and VPN filter drivers

These sit in the kernel's hottest paths and break IRQL rules more than any other software category.

1. Uninstall third-party antivirus and VPN clients via **Settings > Apps > Installed apps**.
2. Restart — Windows Security takes over automatically.
3. Test for a few days; stability here is a definitive diagnosis.
4. Reinstall only the latest versions, one product at a time.
5. If you need always-on VPN, prefer the vendor's newest client or Windows' built-in VPN.

### Fix 5: Test the RAM when dumps disagree

One driver blamed every time = driver problem. A different driver every crash = test the memory.

1. Press **Win + R**, type `mdsched.exe`, and run **Windows Memory Diagnostic**.
2. For certainty, run **MemTest86** from a bootable USB for 4 full passes.
3. Test sticks individually if you have two.
4. Reseat modules before replacing — loose contacts cause intermittent faults.
5. Our [memory diagnostic walkthrough](/articles/how-to-run-memory-diagnostic-tool-on-laptop/) covers thorough testing step by step.

### Fix 6: Repair system files and check the disk

Rule out OS corruption that makes good drivers look guilty.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow` and restart.
3. Run `chkdsk C: /f` to verify file-system integrity.
4. Microsoft documents these utilities on its [Windows support hub](https://support.microsoft.com/en-us/windows).
5. Persistent corruption after repairs suggests a failing drive — check SMART health.

### Fix 7: Undo overclocks and update the BIOS

Unstable clocks cause timing violations that surface as IRQL errors under load.

1. Reset any CPU/RAM overclocks in **Intel XTU**, **Throttlestop**, or the BIOS.
2. Load BIOS **Setup Defaults** and disable XMP profiles.
3. Check your laptop maker's support site for a BIOS update and install it with the charger connected.
4. Clean cooling vents — thermal throttling under load produces the same signature.
5. Retest with the heaviest workload you run.

### Fix 8: Do a clean boot to catch the hidden culprit

When dumps are inconclusive, a clean boot isolates whether any third-party software is involved at all.

1. Press **Win + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, check **Hide all Microsoft services**, then click **Disable all**.
3. Open **Task Manager > Startup apps** and disable every non-Microsoft entry.
4. Restart and use the laptop normally — stability here proves third-party software is involved.
5. Re-enable services in halves to narrow it down to the exact program, then update or remove it permanently.

## Closing

IRQL_NOT_LESS_OR_EQUAL is Windows telling you exactly what's wrong — a driver broke the memory rules — and the dump tells you which one. Read it, replace that driver with the right version from the right source, and the most famous blue screen in Windows becomes a solved problem instead of a recurring one. Keep the working driver version written down; future updates will try to "improve" it, and you'll want to know exactly which version was stable. That note is the difference between a five-minute rollback and another full weekend of investigation.
