---
title: "The Best Way to Backup Drivers Before a Windows Update"
slug: best-way-to-backup-drivers-before-update
date: 2026-09-09
categories: ["drivers"]
tags: ["backup drivers", "driver backup", "windows update", "dism", "restore drivers"]
description: "Before a Windows update breaks your drivers, back them all up in minutes with DISM or PowerShell. Restore in seconds if anything goes wrong."
thumbnail: "/images/thumbs/best-way-to-backup-drivers-before-update.webp"
faqs:
  - q: "Why should I backup drivers before a Windows update?"
    a: "Windows updates routinely replace working OEM drivers with generic versions that break WiFi, audio, touchpads, and graphics. A driver backup lets you restore the exact working set in minutes instead of hunting down each driver from manufacturer websites afterward. It is cheap insurance against the most common post-update breakage."
  - q: "Does Windows backup my drivers automatically?"
    a: "No. Windows keeps a DriverStore of installed drivers, but updates can overwrite it, and a clean reinstall wipes it entirely. System Restore points sometimes include drivers but are unreliable for this purpose. An explicit backup to a folder or external drive is the only dependable method."
  - q: "How much space does a driver backup need?"
    a: "A typical laptop driver backup is 500 MB to 2 GB. Graphics drivers are the largest single component. Any USB flash drive or a folder on a secondary partition is plenty. The backup is a plain folder of INF files, so it compresses well if you zip it."
  - q: "Can I restore drivers on a different laptop?"
    a: "Sometimes, but it is unreliable. Drivers are tied to specific hardware IDs, and a mismatched driver can cause worse problems than the original issue. Always restore to the same machine the backup came from. For a new machine, download fresh drivers from the manufacturer instead."
---

Every experienced Windows user has a story about an update that killed their WiFi, their audio, or their touchpad overnight. The update itself is fine — the problem is that Windows replaces your manufacturer's carefully matched drivers with its own generic versions. The fix after the fact is tedious: identify each broken device, find the right driver on the OEM site, install, reboot, repeat.

The smart move is a driver backup before the update. It takes about five minutes, needs no third-party software, and gives you a one-command restore if anything breaks. Think of it as a seatbelt: you hope you never need it, but you always want it on.

## Why this happens

- **Windows Update overwrites OEM drivers:** Microsoft pushes its own driver versions that may lack OEM customizations for audio, touchpads, and hotkeys.
- **Feature updates reset the driver stack:** Major updates rebuild driver bindings, and devices that worked yesterday can vanish or misbehave today.
- **DriverStore gets pruned:** Windows removes older driver versions to save space, eliminating your rollback options.
- **Clean installs start from zero:** If an update goes badly enough to require reinstallation, you lose every driver at once.
- **OEM sites reorganize:** Finding the exact driver for a three-year-old laptop model gets harder over time as support pages change.
- **Third-party driver tools are unreliable:** Many "driver backup" utilities bundle adware or fail to capture the full driver package.
- **INF-only backups are fragile:** Copying files by hand misses the driver store metadata Windows needs for a proper reinstall.
- **Rollback windows expire:** Windows only keeps the previous driver for a short time; after that, Device Manager's "Roll Back Driver" button goes gray.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Create a DISM driver backup (the best method)

1. Create a folder for the backup, for example `D:\DriverBackup` or a USB drive folder. Avoid the system drive if you might reinstall Windows.
2. Open **Terminal as Administrator**.
3. Run: `dism /online /export-driver /destination:D:\DriverBackup`
4. Wait for the export to complete — DISM walks the entire driver store and copies every third-party driver package. This is the official, Microsoft-supported method, and it captures everything Windows needs for a clean restore.

### Fix 2: Verify the backup is complete

1. Open the backup folder and confirm it contains many subfolders, each with `.inf` files inside.
2. Check the total size — a healthy backup is typically hundreds of megabytes to a couple of gigabytes. A tiny backup means the export missed packages.
3. Look specifically for your critical drivers: wireless (Intel/Realtek/MediaTek), graphics (NVIDIA/AMD/Intel), audio (Realtek), and chipset folders should all be present.
4. Copy the folder to a second location (external drive or cloud storage). A backup that lives only on the drive it protects is half a backup.

### Fix 3: Create a matching system restore point

1. Open **Control Panel → System → System Protection**.
2. Select your system drive, click **Create**, and name it something like "Before 24H2 update."
3. This gives you a second safety net: driver backup for surgical restores, restore point for whole-system rollback.
4. Confirm System Protection is actually enabled for the drive — it is off by default on many fresh installs.

### Fix 4: Document your current driver versions

1. Open **Device Manager** and, for each critical device (display adapter, network adapter, audio), right-click → **Properties → Driver tab** and note the version and date.
2. Save this list in a text file inside the backup folder. After the update, you can compare versions at a glance and spot which drivers Windows changed.
3. Pay special attention to the [Intel WiFi driver version](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) and your GPU driver, since these break most often.

### Fix 5: Pause updates until you are ready

1. Go to **Settings → Windows Update** and use **Pause updates** for one to two weeks.
2. Install the update manually when you have an hour free and your backup is verified — never right before a deadline or a trip.
3. Keep the laptop plugged in during the update. Power loss mid-update is one of the few things a driver backup cannot fix.

### Fix 6: Restore drivers after a bad update

1. After the update, check Device Manager for yellow warnings or missing devices.
2. For each broken device, right-click → **Update driver → Browse my computer for drivers** and point it at your backup folder. Check **"Include subfolders."**
3. Windows will find the matching INF and reinstall your original driver.
4. If several devices broke at once, this per-device method still beats downloading everything again — and it is exactly the skill that also fixes [missing network adapters](/articles/how-to-fix-network-adapter-missing-after-windows-11-update/).

### Fix 7: Use pnputil for bulk restore of many drivers

1. Open **Terminal as Administrator**.
2. Run: `pnputil /add-driver "D:\DriverBackup\*.inf" /subdirs /install`
3. This installs every driver package in the backup at once — useful when an update broke five things simultaneously.
4. Reboot and verify in Device Manager. For authoritative background on driver management, the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) documents these tools in detail.

### Fix 8: Automate driver backups so you never forget

1. Open **Notepad** and save a file called `backup-drivers.bat` containing: `dism /online /export-driver /destination:D:\DriverBackup\%date:~10,4%-%date:~4,2%-%date:~7,2%`
2. Right-click the batch file → **Run as administrator** whenever you want a timestamped backup — each run creates a dated folder.
3. For full automation, open **Task Scheduler**, create a basic task running monthly, pointing at the batch file with **"Run with highest privileges"** checked.
4. Monthly automated backups mean you always have a recent known-good driver set, not one from two years ago. Pair this habit with the OEM-first reinstall approach used for [WiFi adapter repairs](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) and driver problems become minor inconveniences.

## Closing

Five minutes with DISM before an update saves hours of driver archaeology after one. Make the backup, verify it, and update with confidence — the worst case is now a two-minute restore instead of a ruined evening.
