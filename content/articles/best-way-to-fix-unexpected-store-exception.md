---
title: "The Best Way to Fix UNEXPECTED_STORE_EXCEPTION on Windows 11"
slug: best-way-to-fix-unexpected-store-exception
date: 2026-10-10
categories: ["windows-errors"]
tags: ["unexpected store exception", "bsod", "ssd", "windows 11"]
description: "UNEXPECTED_STORE_EXCEPTION blue screen on your laptop? Here's the technician-approved order of fixes — from antivirus conflicts to failing SSDs."
thumbnail: "/images/thumbs/best-way-to-fix-unexpected-store-exception.webp"
faqs:
  - q: "What causes UNEXPECTED_STORE_EXCEPTION?"
    a: "The memory manager's 'store' component — which handles the paging file and compressed memory — hit an unexpected condition. Common triggers are antivirus drivers interfering with paging, corrupted system files, a failing SSD, or sleep/hibernation drivers mishandling power transitions. The error often appears during sleep, wake, or heavy memory use, which is a strong diagnostic clue."
  - q: "Is UNEXPECTED_STORE_EXCEPTION always a hardware problem?"
    a: "No — software causes are actually more common. Third-party antivirus kernel drivers are the classic trigger, followed by corrupted system files. Hardware enters the picture when the error persists after a clean driver set and a repaired system image, or when your SSD's SMART data shows warnings. Always exhaust software fixes before suspecting the drive."
  - q: "Can I fix it without reinstalling Windows?"
    a: "Usually yes. Removing conflicting antivirus drivers, running SFC and DISM, disabling Fast Startup, and updating storage drivers resolve most cases. Reinstallation or a reset is the last resort — this error's root causes are almost always addressable in place, unlike a physically dead drive."
  - q: "Why does this error happen when my laptop wakes from sleep?"
    a: "Sleep and hibernation rely heavily on the store component to page memory in and out. If a storage or chipset driver handles the power transition badly, or the paging file is corrupt, the crash fires exactly at wake. Disabling Fast Startup and updating your storage drivers are the two fixes that most often stop sleep-triggered crashes."
---
UNEXPECTED_STORE_EXCEPTION is one of those blue screens that almost always shows up at the worst moment — right as your laptop wakes from sleep, or in the middle of heavy work when the system is juggling memory. The name refers to Windows' memory "store" manager, the part of the OS that handles the paging file and memory compression. When something interferes with that machinery, Windows crashes deliberately.

The encouraging part: this error is overwhelmingly a software problem. Third-party antivirus drivers, corrupt system files, and sleep-state driver bugs account for the vast majority of cases. Work the list below in order and you'll find the cause without guessing.

## Why this happens

- **Third-party antivirus kernel drivers.** AV products hook deep into memory management; a bug in their filter driver collides with the store manager. This is the single most common cause.
- **Corrupted system files or paging file.** A damaged pagefile.sys or broken core files make the store manager trip over its own data.
- **Fast Startup conflicts.** The hybrid shutdown keeps kernel state on disk; if that state gets corrupted, the error appears on the next boot.
- **Outdated storage or chipset drivers.** The drivers that move memory pages to and from the SSD must handle power transitions perfectly — older ones don't.
- **Failing SSD.** Bad flash cells in the paging area cause read errors that surface as store exceptions, especially under memory pressure.
- **Faulty RAM.** Corrupted memory contents get written to the page file and read back as garbage, which the store manager flags.

## How to fix it

Work through these in order — the first few fix most cases.

### Fix 1: Temporarily remove third-party antivirus

If you run anything other than Windows Security, this is step one — AV filter drivers are the classic trigger.

1. Open **Settings > Apps > Installed apps** and uninstall your third-party antivirus completely (not just disable it — the kernel driver stays loaded otherwise).
2. Restart and use the laptop for a day with just **Windows Security** active.
3. If the crashes stop, you've found the cause. Either keep Windows Security or reinstall the latest version of your AV, since vendors do fix these bugs.
4. If crashes continue, the AV wasn't the cause — move to Fix 2.

### Fix 2: Disable Fast Startup

Fast Startup's hybrid shutdown is a known source of stale kernel state.

1. Open **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
4. Shut down fully (not restart), wait ten seconds, and power on. Sleep/wake-triggered crashes often disappear immediately.

### Fix 3: Repair system files and rebuild the paging file

Clean core files and a fresh pagefile remove the two most common corrupt-data causes.

1. Open **Terminal (Admin)** and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Go to **Settings > System > About > Advanced system settings > Performance > Settings > Advanced > Virtual memory > Change**.
3. Uncheck **Automatically manage paging file size**, select **No paging file**, click Set, and restart.
4. Go back to the same dialog, re-enable **Automatically manage paging file size**, click Set, and restart again. This rebuilds pagefile.sys from scratch.

### Fix 4: Update storage and chipset drivers

The drivers handling memory paging need to be current.

1. Open **Device Manager** and expand **IDE ATA/ATAPI controllers** and **Storage controllers**.
2. Note your storage controller model, then download the latest chipset and storage drivers from your laptop maker's site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Install the chipset driver first, restart, then the storage driver, and restart again.
4. If you have an Intel platform, [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can verify nothing was missed.

### Fix 5: Run check disk and test the SSD's health

Rule out the drive itself feeding bad data to the store manager.

1. In **Terminal (Admin)**, run `chkdsk C: /f /r`, type Y, and restart to scan for bad sectors.
2. Install your SSD maker's health tool (Samsung Magician, Crucial Storage Executive, WD Dashboard) and check the SMART status and wear level.
3. If SMART shows warnings, reallocated sectors, or a "failing" status, back up immediately — no software fix will save a dying drive.
4. If the drive is healthy, continue to the memory test.

### Fix 6: Test the RAM

Bad memory corrupts the data the store manager pages in and out.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. If errors are reported, power off, reseat the RAM, and test again.
3. Still failing? Test one stick at a time to isolate the bad module and replace it.
4. Memory-caused store exceptions typically vanish the moment the faulty stick is out.

### Fix 7: Reset Windows with a fresh image

If software fixes all fail but hardware tests pass, the Windows installation itself is damaged beyond targeted repair.

1. Back up your files, then go to **Settings > System > Recovery > Reset PC**.
2. Choose **Keep my files** and then **Cloud download** to pull a clean image from Microsoft.
3. After the reset completes, install chipset and storage drivers first, test for a day, then reinstall your antivirus last.
4. If crashes return even on a clean reset, the motherboard or SSD is failing — time for the repair shop with your diagnostic notes.

## Closing

UNEXPECTED_STORE_EXCEPTION follows a clear hierarchy: antivirus drivers first, then Fast Startup, then system files, then drivers, then hardware. Most people never get past Fix 3. The wake-from-sleep pattern is your best diagnostic friend — if crashes happen only on wake, focus on Fast Startup and storage drivers. For companion blue-screen guides, see how to [fix memory management stop codes](/articles/how-to-fix-stop-code-memory-management-after-windows-11-update/) and how to [troubleshoot Driver IRQL errors](/articles/how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2/).
