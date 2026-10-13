---
title: "UNEXPECTED_STORE_EXCEPTION on Windows 10: How to Fix It"
slug: how-to-fix-unexpected-store-exception-on-windows-10
date: 2026-09-24
categories: ["windows-errors"]
tags: ["bsod", "windows 10", "stop code", "ssd"]
description: "UNEXPECTED_STORE_EXCEPTION blue screen on Windows 10? It's usually your storage or a driver failing the memory manager. Here's the fix order."
thumbnail: "/images/thumbs/how-to-fix-unexpected-store-exception-on-windows-10.webp"
faqs:
  - q: "What does UNEXPECTED_STORE_EXCEPTION mean on Windows 10?"
    a: "The Windows memory manager hit an unexpected exception in the 'store' — the component managing compressed memory pages and the pagefile. In practice, this almost always traces back to storage problems: a failing SSD/HDD, corrupt storage drivers, or disk errors."
  - q: "Is UNEXPECTED_STORE_EXCEPTION a sign my SSD is dying?"
    a: "It's one of the stronger signs, yes. This stop code correlates heavily with failing storage. Check your drive's SMART health immediately — if it shows warnings, back up your data before doing anything else."
  - q: "Can antivirus cause UNEXPECTED_STORE_EXCEPTION?"
    a: "Yes. Third-party antivirus filter drivers sit in the storage stack, and a buggy one can throw exceptions the memory manager doesn't expect. If crashes started after an antivirus update, try disabling or uninstalling it temporarily."
  - q: "Does this error happen on Windows 11 too?"
    a: "Yes, the same stop code exists on Windows 11 with the same causes. The fixes are nearly identical — see our [Windows 11 version of this guide](/articles/unexpected-store-exception-windows-11-fix/) if you've upgraded."
---

`UNEXPECTED_STORE_EXCEPTION` is Windows 10's way of telling you the memory manager tripped over something in the storage layer. The "store" here is the part of Windows that manages memory compression and paging — and when it hits an exception it didn't expect, the prime suspect is whatever lives underneath: your SSD or hard drive, your storage drivers, or software sitting in the storage path.

This stop code has a well-earned reputation as a dying-drive warning. Not every case is hardware — drivers and antivirus cause it too — but you should treat it as guilty-until-proven-innocent for your storage. That means the fix order here leads with drive health, not driver updates.

## Why this happens

- **Failing SSD or hard drive**: The most common cause. Bad sectors, worn flash cells, or a dying controller throw errors the memory manager can't handle, and it crashes with this code.
- **Corrupt or outdated storage drivers**: AHCI, NVMe, or Intel RST drivers with bugs produce storage exceptions that bubble up as this stop code.
- **Third-party antivirus filter drivers**: Antivirus products hook into the storage stack to scan files on access. A buggy filter driver throws exceptions in exactly the path this stop code monitors.
- **Corrupt system files**: Damage to the memory manager or storage stack components themselves.
- **Failing RAM**: Less common for this code than for others, but bad memory can corrupt the data structures the store manager relies on.
- **Disk encryption conflicts**: Third-party encryption tools (or BitLocker glitches) interfering with the storage path.
- **Power issues to the drive**: A failing battery or loose drive connection causing intermittent I/O errors, especially on older laptops.

## How to fix it

Work through these in order — drive health first, because if the drive is dying, everything else is rearranging deck chairs.

### Fix 1: Check your drive's SMART health immediately

Don't skip this. If the drive is failing, back up first and troubleshoot second.

1. Open **Command Prompt** and run `wmic diskdrive get status` — you want "OK" for every drive.
2. For detail, install CrystalDiskInfo (free) and check the health status and reallocated sector count. Anything but "Good" is a warning.
3. SSD owners: also run the manufacturer's tool (Samsung Magician, Crucial Storage Executive, WD Dashboard) and check wear percentage and firmware updates.
4. If health is bad: back up your files NOW to an external drive, then replace the drive. No software fix saves a dying SSD.

### Fix 2: Update your storage drivers

If the drive is healthy, the driver talking to it is the next suspect.

1. Open **Device Manager** (**Win + X**) and expand **IDE ATA/ATAPI controllers** and **Storage controllers**.
2. Right-click each controller and choose **Update driver** > **Search automatically for drivers**.
3. Better: get the exact driver from your laptop maker's support page — Intel RST and NVMe drivers from the manufacturer beat generic Windows ones.
4. Restart and monitor. Storage driver updates fix a large share of non-hardware cases. If you've since upgraded to Windows 11 and see the same crash there, the [Windows 11 version of this guide](/articles/unexpected-store-exception-windows-11-fix/) covers the identical troubleshooting path.

### Fix 3: Run CHKDSK and repair the file system

File system corruption in the paging path triggers this crash.

1. Open **Command Prompt as administrator** (**Win + X** > **Command Prompt (Admin)** or **Windows PowerShell (Admin)**).
2. Run `chkdsk C: /f /r` and type **Y** to schedule the scan at reboot.
3. Restart and let it complete — don't interrupt it, even if it looks stuck at the same percentage for a while.
4. Afterward, run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth` to repair any system files the disk errors damaged.

### Fix 4: Disable Fast Startup

Fast Startup's hibernation-based shutdown can preserve a corrupted kernel/storage state across reboots.

1. Open **Control Panel** > **Power Options** > **Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Untick **Turn on fast startup** and click **Save changes**.
4. Shut down fully (not restart), power back on, and test for a few days.

### Fix 5: Temporarily remove third-party antivirus

Filter drivers are a known trigger for this exact code.

1. Uninstall your third-party antivirus (don't just disable it — disabled filters can still load).
2. Use the vendor's complete removal tool if they offer one.
3. Rely on **Windows Security** (**Win + S**, type `windows security`) during testing — it's a capable antivirus and doesn't install the problematic filter architecture.
4. If crashes stop, try a fresh install of the latest antivirus version, or stick with Defender.

### Fix 6: Test your RAM

Less common for this code, but worth ruling out.

1. Press **Win + R**, type `mdsched.exe`, press Enter, and choose **Restart now and check for problems**.
2. Any errors mean bad RAM. This is a quick check that eliminates a whole category.

### Fix 7: Clean-boot to find software conflicts

Something in the storage path may be third-party software.

1. Press **Win + R**, type `msconfig`, press Enter.
2. On the **Services** tab, tick **Hide all Microsoft services**, then **Disable all**.
3. Disable all **Startup** items in Task Manager, restart, and test.
4. Re-enable in halves to identify the culprit. Disk utilities, backup tools, and encryption software are the usual finds.

### Fix 8: Reinstall Windows 10 on a healthy drive

When the drive is fine but crashes persist, the OS storage stack may be unrecoverable.

1. Back up everything — this is a clean install, not a repair.
2. Create fresh media with the [Windows 10 Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11) (use the Windows 10 version of the download page) on a known-good USB drive.
3. During setup, delete all partitions on the system drive and install clean.
4. Install drivers from the laptop manufacturer first, before letting Windows Update add its own.
5. For the broader blue screen playbook, see [how to fix the blue screen of death on Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/) — the methodology applies to Windows 10 identically.

## Closing

`UNEXPECTED_STORE_EXCEPTION` on Windows 10 is your storage subsystem crying for help — check the drive's health first, update storage drivers second, and work through the software stack after. Most cases resolve at Fix 1, 2, or 5. But take the drive-health warning seriously: this is one stop code where ignoring it can cost you your data, not just your afternoon.
