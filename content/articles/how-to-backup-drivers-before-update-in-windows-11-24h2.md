---
title: "How to Back Up Drivers Before Updating in Windows 11 24H2"
slug: how-to-backup-drivers-before-update-in-windows-11-24h2
date: 2026-09-04
categories: ["drivers"]
tags: ["backup drivers", "windows 11 24h2", "driver backup", "dism"]
description: "About to update Windows 11 24H2? Back up all your drivers first with DISM or PowerShell so you can restore working versions anytime."
thumbnail: "/images/thumbs/how-to-backup-drivers-before-update-in-windows-11-24h2.webp"
faqs:
  - q: "Why should I back up drivers before a Windows 11 24H2 update?"
    a: "Feature updates routinely replace working manufacturer drivers with generic versions that break WiFi, audio, brightness, or touchpads. A driver backup gives you the exact working versions to reinstall in minutes, instead of hunting down each driver from manufacturer sites after something breaks. It is the cheapest insurance in Windows maintenance."
  - q: "How much space does a full driver backup need?"
    a: "A complete third-party driver backup for a typical laptop runs 500 MB to 2 GB, depending on how many devices you have. Graphics and chipset packages are the largest contributors. Any USB drive or spare partition handles it easily — size is never a practical obstacle."
  - q: "Can I restore a driver backup after a clean Windows install?"
    a: "Yes, with one caveat: the backup restores the driver files themselves, but a clean install sometimes also needs the manufacturer's installer packages for the utilities and control panels that ride along with drivers. The DISM backup covers the drivers perfectly; keep the maker's installer executables too for full-featured components like audio suites and graphics control panels."
  - q: "Does the backup include Windows' own built-in drivers?"
    a: "DISM's driver export captures third-party (OEM) drivers — exactly the ones Windows Update likes to replace and the ones hardest to find again after a bad update. Built-in Microsoft drivers reinstall automatically with Windows itself, so excluding them is correct behavior, not a gap. The backup covers precisely the drivers you'd otherwise spend hours hunting down individually."
---

Every Windows 11 24H2 feature update carries the same risk: it replaces your carefully working manufacturer drivers with generic versions, and something — WiFi, audio, the touchpad, brightness — stops working. The recovery is always the same: reinstall the OEM driver. And the fastest source for that driver is a backup you made before the update, sitting on a USB drive, ready in two minutes.

Driver backup takes about five minutes with built-in Windows tools — no third-party software needed. This guide covers the DISM method (simplest and most reliable), the PowerShell alternative, what to do with the backup, and how to restore when an update breaks something.
Think of a driver backup as a save point for your hardware. Windows updates are the boss fights — usually fine, occasionally devastating — and a save point lets you retry from safety instead of replaying the whole game. Unlike System Restore, which Windows updates can interfere with, a DISM driver export is just files in a folder: simple, portable, and impossible for an update to silently invalidate.

## Why this happens

- **Feature updates replace OEM drivers:** 24H2's update process installs its catalog drivers over manufacturer-tuned ones as a matter of policy.
- **Driver versions are hard to re-find:** Maker support pages reorganize, old versions get pulled, and exact-match hunting wastes hours.
- **Rollback windows expire:** Windows keeps old drivers briefly, but the rollback option disappears — a backup does not expire.
- **Clean installs need drivers:** Fresh Windows has no OEM drivers at all; a backup provisions the machine offline.
- **Multiple machines benefit:** One backup per model can provision every identical laptop you own.
- **Update failures corrupt drivers:** Interrupted updates leave half-written drivers; a backup restores the last known good set.
- **Peace of mind is cheap:** Five minutes and a gigabyte of USB space versus hours of post-update troubleshooting.
- **Documentation value:** The backup folder itself inventories exactly which drivers your system uses.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Export drivers with DISM (recommended)

1. Create a folder for the backup, e.g. `D:\DriverBackup\24H2-pre` on a USB drive.
2. Open **Terminal (Admin)** and run: `dism /online /export-driver /destination:D:\DriverBackup\24H2-pre`
3. Wait for the export to complete — it typically takes 2–5 minutes and reports each driver as it goes.
4. Verify the folder contains subfolders per driver; an empty or tiny export means the command ran without elevation — retry as administrator.
5. Microsoft documents the DISM driver-servicing commands in its [Windows support documentation](https://support.microsoft.com/en-us/windows) if you want the full option reference beyond export and add.

### Fix 2: Export with PowerShell (alternative)

1. Open **PowerShell as administrator**.
2. Run: `Export-WindowsDriver -Online -Destination D:\DriverBackup\24H2-pre`
3. This achieves the same result as DISM through a different cmdlet — useful if DISM is unavailable.
4. Compare the output folder size against expectations (hundreds of MB minimum); investigate if suspiciously small.

### Fix 3: Back up the driver list for documentation

1. In an admin terminal, run `driverquery /v > D:\DriverBackup\driver-list.txt` to save a human-readable inventory.
2. In Device Manager, note any devices with custom or manually installed drivers — these are your highest-priority restores.
3. Save copies of the manufacturer installer executables you originally used (graphics, audio, chipset) alongside the DISM backup.
4. Label the backup with the date and Windows build (`winver`) so future you knows what it matches.
5. Also export a backup right after a fresh laptop setup, before installing anything else — that "factory driver set" is the cleanest restore point you'll ever have, capturing every OEM driver exactly as the manufacturer intended them.

### Fix 4: Store the backup safely

1. Copy the backup folder to two locations: a USB drive and cloud storage or a second disk.
2. Keep it outside the system drive — a backup on C: is useless if C: gets wiped.
3. For multiple laptops, create one folder per model with the model name in the path.
4. Refresh the backup every six months or before each feature update; drivers drift over time.

### Fix 5: Restore a single broken driver after an update

1. When an update breaks a device, open **Device Manager**, right-click the device → **Update driver → Browse my computer**.
2. Point it at your backup folder and tick **Include subfolders** — Windows finds the matching driver automatically.
3. Alternatively use the Have Disk path to force a specific INF from the backup, as described in our [manual OEM driver installation guide](/articles/how-to-install-oem-drivers-manually-in-windows-11-24h2/).
4. Restart and verify the device works, then block Windows Update from replacing it again.
5. The same backup-and-restore discipline protects [battery driver updates](/articles/how-to-update-battery-drivers-on-windows-11/) too — export before any driver change, not just Windows updates.

### Fix 6: Bulk-restore all drivers

1. For widespread post-update breakage, open **Terminal (Admin)**.
2. Run: `dism /online /add-driver /driver:D:\DriverBackup\24H2-pre /recurse`
3. Restart the laptop — Windows binds the backed-up drivers across all devices.
4. Check Device Manager afterward for any remaining warning icons and handle stragglers individually.
5. After a bulk restore, reboot twice — some drivers only bind correctly on the second boot when their dependencies settle. If a device still shows a warning after two reboots, it needs the individual Have Disk treatment, not another bulk pass.

### Fix 7: Use the backup during clean installs

1. During or after a clean Windows install, connect the USB drive with the backup.
2. In Device Manager, update each unknown device by browsing to the backup folder with subfolders included.
3. Install the saved manufacturer executables for graphics and audio to restore their control panels and utilities.
4. Run Windows Update only after the OEM drivers are in place, and decline its driver replacements to preserve your working set.

## Closing

Driver backup is the five-minute habit that turns every future update disaster into a two-minute restore. Run the DISM export before each feature update, store it off the system drive, and pair it with the manual installation technique for forcing specific versions. The guides on this site fix broken drivers constantly — this is the one that prevents the breakage from costing you an afternoon in the first place.
