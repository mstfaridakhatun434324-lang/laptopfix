---
title: "Fix DRIVER_IRQL_NOT_LESS_OR_EQUAL After a Windows 11 Update"
slug: how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update
date: 2026-10-11
categories: ["windows-errors"]
tags: ["bsod", "stop code 0xd1", "windows 11 update", "drivers"]
description: "Fix the DRIVER_IRQL_NOT_LESS_OR_EQUAL blue screen that appeared after a Windows 11 update — find the driver and roll it back."
thumbnail: "/images/thumbs/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update.webp"
faqs:
  - q: "What does DRIVER_IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "Stop code 0x000000D1 means a driver tried to access memory at an improper interrupt level — essentially a driver reaching for memory it wasn't allowed to touch right then. After a Windows 11 update, this almost always means the update replaced a working driver with an incompatible version."
  - q: "Which drivers cause this after an update?"
    a: "Network drivers (Wi-Fi and Ethernet) are the number one offender, followed by graphics drivers and storage controller drivers. The minidump almost always names the exact .sys file, so check it before updating drivers blindly."
  - q: "Will uninstalling the Windows update fix it?"
    a: "Often yes, if the crashes started within days of the update. Uninstalling the cumulative update removes both the update and the driver version it pushed. But the better long-term fix is replacing just the bad driver, then letting the update reinstall cleanly."
  - q: "Is my hardware failing?"
    a: "Unlikely when the timing lines up with an update. Hardware failure doesn't schedule itself around Patch Tuesday. If the crashes started right after an update, treat it as a driver problem until proven otherwise — run the fixes below before suspecting RAM or the SSD."
---
DRIVER_IRQL_NOT_LESS_OR_EQUAL (stop code 0x000000D1) right after a Windows 11 update is one of the most diagnosable blue screens there is, because the timeline does half the detective work for you. The error means a kernel-mode driver tried to touch pageable memory while running at a raised interrupt level — in plain terms, a driver grabbed memory it had no business grabbing at that moment. When that driver worked fine last week and the only thing that changed is a Windows update, the update almost certainly delivered a driver version your hardware doesn't like.

The fix is targeted: identify the driver from the crash dump, replace it with the right version, and stop Windows Update from putting the bad one back. Here's the order that gets you there fastest.

## Why this happens

- **Windows Update replaced a stable driver.** Cumulative and feature updates bundle driver updates. The new network, graphics, or storage driver has a bug on your specific hardware.
- **A driver incompatible with the new kernel build.** Feature updates change kernel internals; older drivers that bent the rules can break outright on the new build.
- **Corrupted driver installation during the update.** If the update was interrupted or the download was damaged, the driver installed half-broken.
- **Two drivers fighting over the same device.** The update installs a new driver while the old one's remnants remain, and they conflict at interrupt level.
- **Overlapping filter drivers.** VPN clients, third-party firewalls, and network utilities install filter drivers that break when the underlying network driver changes underneath them.
- **Actual hardware failure.** The least likely when timing matches an update, but a failing Wi-Fi card or RAM can produce the identical stop code.

## How to fix it

Work through these in order. The dump comes first because it names the driver and saves you from updating everything blindly.

### Fix 1: Read the minidump to identify the driver

This takes five minutes and aims every fix after it.

1. Boot into Safe Mode if the loop is bad: interrupt boot three times to reach **Automatic Repair** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > press **4**.
2. Open `C:\Windows\Minidump`, install **WinDbg Preview** from the Microsoft Store, and open the newest dump.
3. Run `!analyze -v` and read **IMAGE_NAME**. Common post-update culprits: `Netwtw10.sys`/`Netwtw12.sys` (Intel Wi-Fi), `rtwlanu.sys` (Realtek), `nvlddmkm.sys` (NVIDIA), `storahci.sys` (storage).
4. Note the name. If you've never read a dump before, our [WinDbg guide](/articles/best-way-to-read-dump-files-with-windbg/) walks through it with screenshots.

### Fix 2: Roll back the driver Windows Update changed

The fastest fix when the timeline is clear: put the old driver back.

1. Open **Device Manager** (`devmgmt.msc`) and find the device matching the dumped driver.
2. Right-click > **Properties** > **Driver** tab > **Roll Back Driver**. Select a reason and confirm.
3. Reboot and test. If rollback is greyed out, Windows didn't keep the old driver — move to Fix 3.
4. This is also the core technique in the general [IRQL_NOT_LESS_OR_EQUAL fix guide](/articles/irql-not-less-or-equal-windows-11-fix/), which covers the non-update variants of this crash.

### Fix 3: Install the manufacturer's driver cleanly

Replace the bad driver with the version your laptop maker actually validated.

1. In **Device Manager**, right-click the device > **Uninstall device**, ticking **Attempt to remove the driver for this device**.
2. Reboot — Windows falls back to a basic inbox driver.
3. Download the driver for your exact model from your manufacturer's support site (Dell, HP, Lenovo, Acer, ASUS).
4. Install it, reboot, and test for a day. For Intel Wi-Fi specifically, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) usually has the newest stable build.

### Fix 4: Uninstall the Windows update itself

When multiple drivers seem affected or the dump is inconclusive, remove the update that started it.

1. Go to **Settings** > **Windows Update** > **Update history** > **Uninstall updates**.
2. Uninstall the cumulative or feature update matching your crash timeline, then reboot.
3. Test for 24–48 hours. Stable? Pause updates (**Settings** > **Windows Update** > **Pause updates**) for two weeks to give the vendor time to fix the driver.
4. Microsoft documents this flow on [Microsoft Support](https://support.microsoft.com/en-us/windows) if you need the official steps.

### Fix 5: Block Windows Update from reinstalling the bad driver

Otherwise the bad driver comes right back with the next update cycle.

1. After installing the good driver, go to **Settings** > **Windows Update** > **Advanced options** and turn off **Receive updates for other Microsoft products** temporarily — no, the real control: set **Device Installation Settings** to **No**: search Start for **Device installation settings**, choose **No (your device might not work as expected)**.
2. Alternatively, use the official **Show or hide updates** troubleshooter to hide the specific driver update.
3. Re-enable normal driver updates after a month, once the vendor has shipped a fixed version.

### Fix 6: Repair system files damaged by the crash loop

Repeated blue screens can corrupt Windows files, creating secondary crashes.

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
3. Reboot and confirm stability. If SFC keeps finding corruption it can't fix, the update itself damaged the component store — consider the repair install in Fix 7.

### Fix 7: Test RAM and storage to rule out hardware

Only now, with drivers addressed, spend time on hardware.

1. **Win + R** > `mdsched.exe` > **Restart now and check for problems**, Extended mode, two passes.
2. In **Terminal (Admin)**, run `chkdsk C: /f /r` and reboot to let it scan.
3. Clean on both? Hardware is fine — the driver was guilty. Errors on either need addressing before anything else will be stable.

### Fix 8: Do an in-place repair install

The last resort that preserves everything.

1. Download the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, and run **setup.exe**.
2. Choose **Keep personal files and apps** and let it reinstall Windows over itself.
3. After setup, install your manufacturer's drivers first, then run Windows Update — this order prevents the bad driver from landing before the good one.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL after a Windows 11 update is the rare blue screen that practically diagnoses itself: check the timeline, read the dump, and the offending driver is staring at you. Roll it back or replace it with the manufacturer's version, block the bad one from returning, and you're done. The whole job is usually under an hour — most of it waiting for reboots — and it beats the alternative of living in fear of every Patch Tuesday.
