---
title: "How to Fix the Windows 11 24H2 Update Stuck at 75% on an ASUS Laptop"
slug: how-to-fix-24h2-update-stuck-at-75-percent-on-asus-laptop
date: 2026-10-10
categories: ["windows-update"]
tags: ["windows 11 24h2", "update stuck at 75", "asus laptop", "feature update stuck"]
description: "Windows 11 24H2 stuck at 75% on your ASUS laptop? Learn why it stalls there and the exact steps to push the update through safely."
thumbnail: "/images/thumbs/how-to-fix-24h2-update-stuck-at-75-percent-on-asus-laptop.webp"
faqs:
  - q: "Why does the Windows 11 24H2 update always stall at 75%?"
    a: "The 75% mark is typically where Windows migrates drivers and finalizes system files, so a stuck third-party driver, a peripheral holding a device handle, or corrupted temporary files can pause it. It usually resumes once the blocking driver is removed or the update cache is cleared, which is why the first fixes focus on drivers and connected devices."
  - q: "Is it safe to force shut down a stuck update at 75%?"
    a: "If the progress bar has not moved for several hours and the disk activity light is dark, a forced shutdown is reasonably safe because 75% is past the critical early phase. Hold the power button for ten seconds, wait thirty seconds, then power on and let Windows resume or roll back. Do not force a shutdown during the first hour of apparent stalling."
  - q: "How long should I wait before assuming the update is stuck?"
    a: "Give it at least two to three hours on a single percentage if the disk light shows activity. SSDs can still sit at 75% for an hour during driver migration on a loaded system. If there is no disk activity at all for over an hour and the percentage never changes, treat it as stuck and start with the peripheral and driver fixes."
  - q: "Can ASUS Armoury Crate interfere with the 24H2 update?"
    a: "Yes. Armoury Crate hooks into system services and its background components have been known to hold handles that block driver migration at exactly this stage. Updating Armoury Crate to the latest version, or temporarily stopping its services before retrying the update, resolves many ASUS-specific stalls at 75%."
---

If your ASUS laptop has been sitting at 75% on the Windows 11 24H2 update for hours, you are looking at one of the most common stall points in the entire update process. The percentage does not move, the fans may be quiet, and it is impossible to tell whether anything is happening at all. The good news is that 75% is not a random number: it is the stage where Windows migrates device drivers and finalizes the new system image, which means the blockage is almost always a driver, a connected device, or a corrupted update cache rather than a dead system.

On ASUS machines specifically, a few brand traits show up repeatedly in these stalls. Armoury Crate and its background services can hold device handles that block driver migration, older ASUS system drivers sometimes conflict with 24H2's expectations, and ASUS laptops with secondary drives or unusual partition layouts can trip the installer. The fixes below are ordered so you diagnose first: quick checks that identify the blocker, then the actions that clear it.

ASUS's gaming and creator laptops add another wrinkle: many ship with two drives or Intel RST configurations that the 24H2 installer must re-enumerate at exactly this stage, and a stale RST driver is a documented stall trigger. There is also the human factor — 75% looks broken, so people force reboots at the worst moment and convert a slow update into a corrupted one. The checks below take ten minutes and tell you whether the installer is working, blocked, or genuinely dead, so every action after that is aimed at the real problem instead of guesswork.

## Why this happens

- **Driver migration deadlock at 75%.** This stage migrates every device driver to the new OS build; a single incompatible or unsigned driver can pause the whole process indefinitely.
- **A connected peripheral holding a device handle.** USB drives, docks, printers, and especially external GPUs can block the installer from releasing a device it needs to migrate.
- **Armoury Crate or MyASUS background services** interfering with system services during the migration phase.
- **Corrupted temporary update files** in the SoftwareDistribution cache that the installer keeps retrying.
- **Insufficient free space on the system partition.** 24H2 needs a working margin during migration, and a nearly full drive stalls it silently.
- **Outdated ASUS system drivers or BIOS** that conflict with what 24H2 expects during hardware re-enumeration.
- **Antivirus real-time protection locking system files** the installer needs to replace at this stage.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out a slow-but-working update

1. Watch the disk activity light (or open Task Manager with **Ctrl + Shift + Esc** if you have a second screen) for at least 60–90 minutes before doing anything.
2. If the drive light blinks or Task Manager shows disk activity from the update process, the update is still working — driver migration at 75% is genuinely slow on HDDs and crowded systems. Let it finish.
3. Only move to the next fixes if there has been zero disk activity for over an hour. Rushing past this check is how good updates get broken.

### Fix 2: Disconnect every peripheral and restart the update

1. If the update is truly stuck, hold the **power button** for ten seconds to force the laptop off, then wait thirty seconds.
2. Unplug everything: USB drives, docks, external monitors, printers, SD cards, and especially external GPUs.
3. Power on with only the charger connected and let Windows resume, roll back, or boot normally.
4. Once you are back in Windows, retry the update with peripherals still disconnected. This alone clears a large share of 75% stalls.

### Fix 3: Update ASUS system drivers before retrying

1. Open **MyASUS** (preinstalled on ASUS laptops) and install any pending driver or BIOS updates it lists.
2. Run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to update chipset and storage drivers, which matter most during migration.
3. In **Device Manager**, expand **Display adapters** and **Network adapters**, and update any driver dated before 2024.
4. Retry the 24H2 update from **Settings** > **Windows Update** after the driver refresh.

### Fix 4: Temporarily stop Armoury Crate services

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Find services starting with **Armoury Crate** or **ASUS**, right-click each, and choose **Stop**.
3. Also open Task Manager (**Ctrl + Shift + Esc**), go to the **Startup apps** tab, and disable Armoury Crate and MyASUS entries.
4. Restart the laptop and retry the update. You can re-enable these services after 24H2 installs successfully.

### Fix 5: Clear the update cache

1. Press **Windows key + R**, type `services.msc`, and stop the **Windows Update** service.
2. Open File Explorer and navigate to `C:\Windows\SoftwareDistribution\Download`, then delete everything inside (these are only temporary files).
3. Restart the **Windows Update** service.
4. Go to **Settings** > **Windows Update** and click **Check for updates** to download a fresh copy of the 24H2 files. For more on cache problems, see [how to fix Windows Update stuck downloading](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/).

### Fix 6: Free up system drive space

1. Open **Settings** > **System** > **Storage** and check free space on C:. You want at least 20 GB free for a feature update.
2. Run **Disk Cleanup** (search for it in Start), select the C: drive, and check **Windows Update Cleanup**, **Temporary files**, and **Delivery Optimization Files**.
3. Uninstall large programs you no longer use, or move personal files to an external drive temporarily.
4. Retry the update once you have comfortable free space.

### Fix 7: Run the Windows Update troubleshooter and retry

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** and run **Windows Update**.
2. Apply any fixes it recommends, then restart the laptop.
3. Return to **Settings** > **Windows Update** and click **Retry** or **Check for updates**.
4. If the troubleshooter itself fails, the official [Windows Update support page](https://support.microsoft.com/en-us/windows) documents additional recovery steps. Related reading: [fixing undoing-changes loops](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-in-windows-11-24h2/).

### Fix 8: Run an in-place upgrade repair

If the update will not complete no matter what, repair the Windows installation underneath it with an in-place upgrade, which reinstalls 24H2's files while keeping your programs and data.

1. Download the Windows 11 ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and copy it to the ASUS via USB.
2. Double-click the ISO to mount it, then run `setup.exe`.
3. Choose **Keep personal files and apps** when asked what to keep.
4. Let the repair install complete — it rebuilds the servicing stack that the stuck update was fighting, and your files stay put.

## Closing

A 24H2 update frozen at 75% on an ASUS laptop is frustrating precisely because it looks dead while often being one blocked driver away from finishing. Work the list in order — verify it is genuinely stuck, remove peripherals, refresh ASUS drivers, quiet Armoury Crate, clear the cache — and the installer almost always pushes through on the next attempt. If the in-place repair also stalls at the same point, suspect hardware: run a full drive health check and memory diagnostic before trying again, because no software fix overcomes failing storage. And once 24H2 is finally in, update Armoury Crate and your ASUS drivers immediately — the combination that stalled this time will stall the next feature update too unless the drivers are current.
