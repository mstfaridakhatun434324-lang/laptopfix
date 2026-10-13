---
title: "How to Back Up Your Drivers Before Updating on a Laptop"
slug: how-to-backup-drivers-before-update-on-laptop
date: 2026-10-02
categories: ["drivers"]
tags: ["backup drivers windows", "driver backup before update", "export drivers dism", "restore drivers", "driver rollback safety"]
description: "About to update drivers? Back them up first with built-in Windows tools so you can roll back in minutes if the new driver breaks something."
thumbnail: "/images/thumbs/how-to-backup-drivers-before-update-on-laptop.webp"
faqs:
  - q: "Why should I back up drivers before updating them?"
    a: "Because driver updates sometimes make things worse — a new graphics driver can break games, a new WiFi driver can kill connectivity, and Windows doesn't always keep a working copy to roll back to. A backup taken before the update gives you a guaranteed restore path that doesn't depend on the internet or the manufacturer's site still hosting the old version. It takes five minutes and has saved countless reinstall headaches."
  - q: "Does Windows have a built-in way to back up drivers?"
    a: "Yes — the DISM command can export all third-party drivers from the driver store with a single command: dism /online /export-driver /destination:C:\\DriverBackup. It copies the .inf packages for every installed third-party driver into a folder you choose. No extra software needed, and the export works on any Windows 10 or 11 machine. It's the method Microsoft's own documentation recommends."
  - q: "How do I restore drivers from a backup?"
    a: "Open Device Manager, right-click the device, choose Update driver, then Browse my computer for drivers and point it at your backup folder — Windows finds the matching .inf automatically. For a bulk restore, use pnputil /add-driver with the /subdirs /install switches against the backup folder. Restore only the specific driver that broke; there's no need to roll back everything."
  - q: "How often should I back up my drivers?"
    a: "Take a fresh backup before any major driver update round — especially graphics, chipset, and BIOS-adjacent updates — and before Windows feature updates, which are notorious for replacing working drivers. A quarterly backup is plenty for routine maintenance. Keep the backup on an external drive or a separate partition so it survives even if Windows itself needs reinstalling."
---

Every experienced technician has a driver horror story: the "routine" update that killed WiFi, broke the touchscreen, or left the machine booting to a black screen — with no way back because the old driver was gone and the internet was down. The five-minute habit that prevents all of it is backing up your working drivers before you update. Windows includes the tools to do it; no third-party software required.

This guide shows you how to export your drivers with built-in commands, how to restore them when an update goes wrong, and how to build the habit into your update routine. Do the backup once now, and every future driver update becomes risk-free.

The tool behind this is DISM (Deployment Image Servicing and Management), the same utility IT departments use to service Windows images — and Microsoft documents the driver export capability at the [Windows support hub](https://support.microsoft.com/en-us/windows). What it does is copy the driver packages Windows has staged in its driver store: the .inf files plus their associated binaries, exactly as installed. That matters because a backup of the staged package reinstalls cleanly with full signatures intact, unlike copying files out of System32 by hand. One command, one folder, every third-party driver on the machine preserved.

## Why this happens

Backup habits matter because driver updates go wrong in predictable ways:

- **New drivers introduce regressions** — fixed one bug, broke something else. Version numbers don't guarantee quality.
- **Windows Update replaces manufacturer drivers** with generic ones and doesn't keep the old package.
- **Rollback isn't always available** — the Roll Back Driver button is grayed out if Windows cleaned up the old driver.
- **Manufacturer sites remove old versions**, leaving you no download path for the working driver.
- **No internet after a bad network driver update** means you can't download anything to fix it.
- **Clean installs wipe the driver store**, and a backup on external media restores hardware support fast.
- **Laptop-specific drivers** (hotkeys, touchpad, power management) are hard to find individually later.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Export all third-party drivers with DISM

The one-command backup. Do this before any update round.

1. Create a folder for the backup, e.g., `C:\DriverBackup` (or better, a folder on an external drive).
2. Open **Terminal (Admin)**.
3. Run: `dism /online /export-driver /destination:C:\DriverBackup`
4. Wait for it to complete — it exports every third-party driver package (.inf) from the driver store.
5. Verify the folder contains subfolders (one per driver). Note the date in the folder name, e.g., `DriverBackup-2026-10-02`, so you know which backup is which.

### Fix 2: Back up a single critical driver with PowerShell

When you only care about one device (WiFi before a risky update, for example).

1. First, [check the exact driver version](/articles/how-to-check-driver-version-in-device-manager/) so you know what you're preserving.
2. In an elevated PowerShell, list the driver: `Get-WindowsDriver -Online | Where-Object {$_.ProviderName -like "*Intel*"}`
3. Note the **OriginalFileName** — that's the .inf in the driver store.
4. Copy the whole driver package folder from `C:\Windows\System32\DriverStore\FileRepository\` to your backup location.
5. This preserves the exact signed package, which is what Windows needs for reinstall.

### Fix 3: Create a system restore point as a companion safety net

Driver backup plus restore point covers both files and system state.

1. Search for **Create a restore point** and open it.
2. Select your system drive, click **Create**, and name it "Before driver updates."
3. Restore points capture registry and system file state — they complement (not replace) the driver file backup.
4. If a driver update causes boot problems, you can roll back from the recovery environment even without the file backup.

### Fix 4: Restore a single driver from your backup

The payoff — rolling back in minutes.

1. Open **Device Manager**, right-click the misbehaving device, and choose **Update driver**.
2. Select **Browse my computer for drivers** and point it at your backup folder (tick **Include subfolders**).
3. Windows matches the device to the backed-up .inf and reinstalls the old version.
4. Restart and verify the version is back to the pre-update number.

### Fix 5: Bulk-restore drivers with pnputil

For reinstalling many drivers at once (after a clean Windows install, for example).

1. Open **Terminal (Admin)**.
2. Run: `pnputil /add-driver "C:\DriverBackup\*.inf" /subdirs /install`
3. Windows stages and installs every matching driver from the backup.
4. Restart and check Device Manager for any remaining unknown devices.

### Fix 6: Store backups where they survive disasters

A backup on the system drive dies with the system drive.

1. Copy the backup folder to a USB drive or external hard disk after exporting.
2. Keep at least two generations (e.g., last quarter and today) in case the most recent backup captured an already-broken driver.
3. Label folders with dates and machine model: `DriverBackup-HP-Pavilion15-2026-10-02`.
4. Consider keeping a copy in cloud storage for the critical network driver alone — it's the one you need when you have no internet.

### Fix 7: Make it a habit — the pre-update checklist

Build the routine so you never skip it.

1. Before any driver update round: export with DISM (Fix 1) + create a restore point (Fix 3).
2. Before Windows feature updates: same, since they replace drivers aggressively.
3. Before graphics driver updates specifically, also note your current version — graphics rollbacks are the most common need.
4. After confirming the new drivers work for a few days, you can delete the oldest backup generation.

## Closing

Driver backup is the cheapest insurance in PC maintenance: one command, five minutes, and every future update becomes reversible. The DISM export plus a restore point covers you against bad updates, Windows Update overwrites, and even clean installs — as long as the backup lives on external media. If you're about to update graphics drivers specifically, pair this habit with our [clean NVIDIA driver install guide](/articles/how-can-i-update-nvidia-drivers-clean-install/) for the safest possible update path. And if an update already went wrong before you had a backup, our [driver version checking guide](/articles/how-to-check-driver-version-in-device-manager/) helps you identify exactly what changed.
