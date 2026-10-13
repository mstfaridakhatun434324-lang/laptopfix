---
title: "How to Fix Error 0xC1900101 on Windows 11"
slug: how-to-fix-error-0xc1900101-on-windows-11
date: 2026-09-29
categories: ["windows-errors"]
tags: ["error-0xc1900101", "windows-11", "upgrade-error"]
description: "Windows 11 upgrade failing with error 0xC1900101? Fix the driver conflicts and disk issues blocking your upgrade."
thumbnail: "/images/thumbs/how-to-fix-error-0xc1900101-on-windows-11.webp"
faqs:
  - q: "What does error 0xC1900101 mean?"
    a: "It's a generic Windows setup failure code meaning the upgrade rolled back — usually because a driver crashed during installation. The extended code after it (like 0x30018 or 0x40017) narrows down the phase, but the fix approach is the same: remove the blocking driver or condition."
  - q: "What do the extended codes like 0x30018 mean?"
    a: "They indicate which setup phase failed: 0x2000C–0x4001B codes map to phases like driver migration or first boot. They're useful for technicians, but for most users the practical fixes — driver cleanup, disk space, disconnecting peripherals — are identical regardless of the extension."
  - q: "Will I lose my files if the upgrade keeps rolling back?"
    a: "No. A rollback restores your previous Windows installation intact — that's the whole point of the rollback mechanism. Your files and apps survive; you just don't get the new version until the blocker is fixed."
  - q: "How much free space do I need for the upgrade?"
    a: "Microsoft recommends at least 20 GB free on the system drive for 64-bit Windows 11, but 30–40 GB is safer. Setup needs room for the downloaded image, the Windows.old backup, and working space — cramped drives are a top cause of 0xC1900101."
---
# How to Fix Error 0xC1900101 on Windows 11

**Error 0xC1900101** is Windows 11's way of saying "the upgrade failed and I rolled everything back." You'll see it with an extended code like `0x30018` or `0x40017`, and the setup log will blame a driver — because nine times out of ten, a driver is exactly what killed the upgrade.

The maddening part is the rollback: you wait an hour, then you're back where you started. But the fix list is straightforward — free up space, strip out the blocking drivers and peripherals, and give setup a clean runway. If your failures show a different update code, our [stuck on restarting screen fix](/articles/windows-11-stuck-on-restarting-screen-fix/) covers another common upgrade blocker, and the [black screen after update guide](/articles/windows-11-black-screen-after-update-fix/) helps when upgrades leave the system unbootable.

## Why this happens

- **Incompatible or crashing driver:** A driver that bluescreens during the upgrade's driver-migration phase — storage, display, and antivirus filter drivers lead the pack.
- **Insufficient disk space:** Setup needs tens of gigabytes for the image, Windows.old, and working files.
- **Connected peripherals:** USB devices with flaky drivers (printers, docks, external drives) can crash setup.
- **Corrupted system files:** Damage in the current installation carries into the upgrade attempt.
- **Third-party antivirus:** Filter drivers that hook deep into the OS frequently block upgrades.
- **Failing drive sectors:** Bad blocks in the middle of the system partition corrupt the new install as it's written.

## How to fix it

Work through these in order. Most 0xC1900101 failures yield to Fixes 1–3.

### Fix 1: Free up disk space

The simplest cause and the simplest fix — give setup room to breathe.

1. Open **Settings > System > Storage** and run **Cleanup recommendations**; remove temporary files, old downloads, and unused apps.
2. Aim for at least **30–40 GB free** on C: — more is better. Turn on **Storage Sense** while you're here so temporary files get cleaned automatically going forward.
3. Empty the Recycle Bin and move large media files to an external drive temporarily.
4. Run **Disk Cleanup** (`cleanmgr.exe`) as admin and tick **Previous Windows installations** and **Temporary Windows installation files** if present.
5. Retry the upgrade.

### Fix 2: Disconnect all non-essential peripherals

USB devices are a notorious upgrade killer. Strip the laptop down to basics.

1. Unplug everything: printers, USB hubs, docks, external drives, SD cards, and USB headsets.
2. Keep only the charger and, if needed, a basic wired mouse.
3. If you use a docking station for the upgrade, undock and run setup on the bare laptop.
4. Retry the upgrade with the minimal setup — if it succeeds, reconnect peripherals one at a time afterward.

### Fix 3: Update or remove problem drivers

Since a crashing driver is the most common root cause, clean up the driver stack before retrying.

1. Open **Device Manager** (**Win + X**) and look for any device with a yellow warning — update or uninstall it.
2. Update the **storage controller**, **display adapter**, and **network adapter** drivers from your laptop maker's support site.
3. Uninstall third-party antivirus completely (use the vendor's removal tool, not just Add/Remove) and rely on Windows Security during the upgrade.
4. Remove virtual-drive, disk-encryption, and "system optimizer" software — their low-level drivers are frequent blockers.
5. Also update the BIOS from the manufacturer's site; old firmware plus a new OS is a classic 0xC1900101 recipe.
6. If Device Manager shows no warnings but setup still fails, check **Optional updates** under **Settings > Windows Update > Advanced options** — installing those driver updates before the upgrade sometimes resolves hidden incompatibilities.

### Fix 4: Repair system files before upgrading

Upgrading a damaged installation just carries the damage forward.

1. Open an admin Terminal.
2. Run `sfc /scannow` until it's clean.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart, then retry the upgrade — don't skip the restart, since pending repairs only finalize on reboot.

### Fix 5: Run setup from a fresh ISO

The Windows Update–delivered upgrade files may themselves be corrupted.

1. Download the latest Windows 11 ISO from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) — or use the Media Creation Tool there to build a bootable USB as a backup.
2. Mount the ISO (double-click it) and run `setup.exe`.
3. Choose **Keep personal files and apps** when prompted.
4. A fresh ISO also means you're installing the newest build, which may already contain the fix for whatever blocked the older one. Disconnect from the internet during setup if you suspect Windows Update is injecting a bad driver mid-install — you can update afterward on your own terms.

### Fix 6: Check the drive health

Bad sectors can corrupt the new install as setup writes it, producing rollbacks that look driver-related.

1. Open an admin Command Prompt and run `chkdsk C: /f /r`.
2. Schedule at reboot and let the full scan finish.
3. Check the drive's SMART status with the manufacturer's tool or `wmic diskdrive get status`.
4. If the drive is failing, replace it before retrying — no software fix survives bad hardware. Back up your data first.

### Fix 7: Read the setup logs to find the exact blocker

When all else fails, the logs name the culprit — you just have to look.

1. After a failed upgrade, open `C:\$Windows.~BT\Sources\Panther\setuperr.log` in Notepad.
2. Look for driver filenames (`.sys`) or device IDs near the errors at the end of the log.
3. Search the web for the specific filename plus 0xC1900101 — someone has usually identified the offending hardware.
4. Uninstall or disable that device/driver, then retry.
5. For persistent mysteries, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the extended error codes and their meanings.

## Closing

Error 0xC1900101 is setup telling you something in the current system can't survive the upgrade — usually a driver, a peripheral, or a cramped disk. Clear space, unplug everything, clean up the drivers, and retry from a fresh ISO. The rollback mechanism means your data is safe while you iterate, so work the list patiently and the upgrade will eventually go through cleanly.
