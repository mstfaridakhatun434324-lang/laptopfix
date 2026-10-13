---
title: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED: Troubleshoot It the Right Way"
slug: troubleshoot-system-thread-exception-not-handled
date: 2026-10-10
categories: ["windows-errors"]
tags: ["bsod", "stop code", "system thread exception", "drivers"]
description: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED blue screen? A driver threw an exception Windows couldn't catch. Here's how to find and fix it."
thumbnail: "/images/thumbs/troubleshoot-system-thread-exception-not-handled.webp"
faqs:
  - q: "What does SYSTEM_THREAD_EXCEPTION_NOT_HANDLED mean?"
    a: "A system thread — code running with kernel privileges, usually a driver — hit an error (exception) that nothing caught and handled. Windows stops the whole system rather than let the unknown error continue. The name of the failing driver often appears in parentheses on the blue screen itself."
  - q: "Which driver causes this error most often?"
    a: "Graphics drivers lead the list, followed by network (Wi-Fi) drivers and storage drivers. But any kernel driver can cause it, including ones installed by VPN software, antivirus products, and USB peripherals. Check the blue screen text or the dump file for the exact .sys file."
  - q: "Can a Windows update trigger this blue screen?"
    a: "Yes — this error frequently appears within days of a Windows feature update or a driver update delivered through Windows Update. If the timing lines up, rolling back the recent update or driver is usually the fastest fix."
  - q: "Is my hard drive failing when I see this error?"
    a: "Not necessarily, but disk problems are one possible cause — a failing drive can corrupt a driver as it loads. If fixes point at the disk, run chkdsk and your manufacturer's drive health tool before assuming the worst."
---

`SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` is the blue screen that appears when a piece of kernel-mode code — almost always a driver — crashes in a way nobody expected. In plain terms: a driver hit an error, nothing caught it, and Windows pulled the emergency brake. The helpful part is that the blue screen often names the failing driver in parentheses, like `(nvlddmkm.sys)` or `(rtwlanu.sys)`. That file name is your single best clue, and everything below starts from it.

If you caught the file name on the blue screen, you're already halfway to a fix. If you didn't — it flashes by fast — don't worry: Fix 1 shows you how to pull it from the log instead. Like many [blue screen errors on Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/), this one rewards patience and punishes guesswork, so work the list in order.

## Why this happens

- **A buggy or outdated graphics driver**: The single most common trigger. NVIDIA, AMD, and Intel graphics drivers all have a history of releases that throw unhandled exceptions under specific conditions — gaming, video playback, or even waking from sleep.
- **Corrupt or incompatible network drivers**: Wi-Fi and Ethernet drivers crash this way surprisingly often, especially Realtek and Intel wireless drivers after a Windows feature update changes the networking stack.
- **A driver installed by third-party software**: VPN clients, antivirus suites, disk utilities, and even some RGB control apps install kernel drivers. One bad update from any of them lands you on this blue screen.
- **Windows Update replaced a manufacturer driver**: Windows Update sometimes swaps your laptop maker's tuned driver for a generic one. The generic driver may mishandle hardware-specific quirks and crash.
- **Corrupted system files or a bad Windows update**: If the crash mentions a Windows system file rather than a third-party driver, the cause is more likely damaged system files or an update that didn't install cleanly.
- **Failing storage corrupting drivers at load time**: A dying SSD or HDD can corrupt driver code as Windows loads it into memory, producing an exception in code that was fine when it was written.
- **BIOS/firmware incompatibilities**: Older firmware on newer Windows builds can mishandle power states or hardware interrupts, surfacing as a thread exception in a driver that depends on that firmware.

## How to fix it

Work through these in order — find the failing driver first, then fix it.

### Fix 1: Identify the failing driver from the crash log

Before changing anything, get the name of the driver. This takes five minutes and saves you from updating the wrong thing.

1. Press **Windows + X** and open **Event Viewer**.
2. Expand **Windows Logs** > **System** and look for entries marked **Critical** with source **Kernel-Power** around the time of the crash — but the real detail is in **BugCheck** events from source **Microsoft-Windows-WER-SystemErrorReporting** or the dump file itself.
3. For the definitive answer, check `C:\Windows\Minidump` for the latest `.dmp` file. Open it with WinDbg (free from the Microsoft Store) and run `!analyze -v` — the `IMAGE_NAME` line names the failing driver. (Our [WinDbg walkthrough](/articles/how-to-read-dump-files-with-windbg-on-windows-11/) covers this step by step.)
4. If the blue screen showed the driver name in parentheses, just use that — `rtwlanu.sys` is Realtek wireless, `nvlddmkm.sys` is NVIDIA, `atikmdag.sys` is AMD, `igdkmd64.sys` is Intel graphics.

Write the driver name down. Every fix below assumes you know it.

### Fix 2: Update the failing driver — cleanly

Once you know the driver, update it properly rather than letting Windows guess.

1. Press **Windows + X** and open **Device Manager**.
2. Find the device matching the failing driver (Display adapters for graphics, Network adapters for Wi-Fi).
3. Right-click it and choose **Update driver** > **Search automatically for drivers** — but treat this as a fallback. The real fix is the driver from your laptop manufacturer's support site or the chip vendor ([NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or Intel's driver support site).
4. For graphics drivers, do a **clean install**: run the vendor installer and choose the "Clean installation" option, which removes the old driver completely instead of layering over it. This resolves the large majority of driver-caused thread exceptions.

If the crash started right after a driver update, do the opposite: in **Device Manager** > device **Properties** > **Driver** tab, click **Roll Back Driver**.

### Fix 3: Remove the driver Windows Update forced on you

If the failing driver arrived via Windows Update and conflicts with your hardware, block it and install the manufacturer's version.

1. Note the driver version in **Device Manager** > **Properties** > **Driver** tab.
2. Uninstall the device (right-click > **Uninstall device**), ticking **Attempt to remove the driver for this device** if the option appears.
3. Install the driver from your laptop manufacturer's support page instead.
4. To stop Windows Update from "helpfully" replacing it again, use Microsoft's **Show or Hide Updates** troubleshooter (available via [Microsoft's support pages](https://support.microsoft.com/en-us/windows)) to hide that specific driver update.

### Fix 4: Uninstall recently added kernel-level software

If the failing driver belongs to third-party software — a VPN's `.sys` file, an antivirus filter driver, a USB dock utility — the software itself has to go or be updated.

1. Open **Settings** > **Apps** > **Installed apps** and sort by date.
2. Remove anything installed in the week before the crashes began: VPN clients, third-party antivirus, disk tools, and peripheral utilities are the usual suspects.
3. Restart after each removal and test. Reinstall only the programs you actually need, from the vendor's site, at their latest version.

### Fix 5: Run SFC and DISM

If the failing file is a Windows component — or if you can't pin down a driver — repair the system files.

1. Open **Terminal (Admin)** from **Windows + X**.
2. Run `sfc /scannow` and let it complete.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` to fix the component store.
4. Run `sfc /scannow` once more, then restart.

### Fix 6: Check the disk

A failing drive corrupting drivers at load time produces exactly this error, and it's the one cause you don't want to miss.

1. Open **Terminal (Admin)** and run `chkdsk C: /f /r`. Type **Y** when asked to schedule it, then restart — the scan runs before Windows loads.
2. Check the drive's health with your manufacturer's tool (Samsung Magician, WD Dashboard, Crucial Storage Executive) or read the SMART data with CrystalDiskInfo.
3. If the drive shows reallocated sectors or fails the manufacturer's test, back up immediately and replace the drive — no software fix will hold on dying storage.

### Fix 7: Update the BIOS and test memory

Two firmware-level checks round out the list.

1. Visit your laptop manufacturer's support site and compare your BIOS version (check with `msinfo32`, look at **BIOS Version/Date**) against the latest. Install it on AC power.
2. Press **Windows + R**, type `mdsched.exe`, choose **Restart now and check for problems**, and let the memory test run. Corrupt RAM can make innocent drivers throw exceptions.
3. If the memory test fails, the RAM needs replacing — a hardware fix, but at least you'll know exactly what's wrong.

## Closing

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED looks intimidating, but the diagnostic path is straightforward: name the driver, then fix that driver. The blue screen or the dump file tells you which one, and in most cases a clean driver update or a rollback ends the story. Save the hardware tests for last — they're the least likely cause, but they're also the ones you can't afford to skip if everything else comes back clean.
