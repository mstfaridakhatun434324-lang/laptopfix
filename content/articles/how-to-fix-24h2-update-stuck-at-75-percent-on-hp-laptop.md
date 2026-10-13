---
title: "Windows 11 24H2 Stuck at 75% on HP Laptop: How to Get It Moving"
slug: how-to-fix-24h2-update-stuck-at-75-percent-on-hp-laptop
date: 2026-09-09
categories: ["windows-update"]
tags:
  - "windows 11 24h2"
  - "stuck at 75"
  - "hp laptop"
  - "feature update"
description: "The 24H2 update freezing at 75% on HP laptops is usually a driver migration hang. Learn how to tell a real stall from slow progress, and the steps that get the install moving again."
thumbnail: "/images/thumbs/how-to-fix-24h2-update-stuck-at-75-percent-on-hp-laptop.webp"
faqs:
  - q: "Is my HP laptop actually stuck at 75%, or just slow?"
    a: "The 70-80 percent range is the driver migration phase, which is legitimately slow — two to four hours on some HP models is normal. It is only stuck if the percentage and the disk activity light are both frozen for over four hours, or the same percentage survives a full restart cycle."
  - q: "Can I turn off my HP laptop while 24H2 is stuck at 75%?"
    a: "Avoid it if at all possible. Powering off mid-migration is the top cause of corrupted installs that then need the full rollback-and-repair sequence. Only force a shutdown after you have confirmed a genuine stall (no disk activity for hours), and expect a rollback afterward."
  - q: "Why does 24H2 always seem to stall at 75% on HP laptops?"
    a: "Seventy-five percent is roughly where the installer migrates third-party drivers to the new build. HP laptops carry a lot of custom drivers — audio, fingerprint readers, printers, docks — and one misbehaving driver package can pause the whole migration while the installer waits on a timeout."
  - q: "Will I lose files if the 24H2 install fails at 75%?"
    a: "No. A failed feature update rolls back to your previous Windows build with files and programs intact. The undoing changes screen looks alarming, but it is Windows restoring the working state. Still, keep a current backup — it is cheap insurance."
---

Watching the Windows 11 24H2 progress bar freeze at 75 percent on your HP laptop is a special kind of suspense. An hour passes. Two hours. The percentage does not move, the fan drones on, and you start wondering whether touching anything will brick the machine. Take a breath — this exact stall is one of the best-understood 24H2 behaviors on HP hardware.

The 75 percent mark is not random. It is deep in the driver migration phase, where the installer moves your third-party drivers onto the new build. HP laptops, with their extensive custom driver stacks, spend longer here than most — and when a single driver package misbehaves, the whole phase can appear frozen while the installer waits out long timeouts.

This guide teaches you to distinguish slow from stuck, then walks the HP-specific fixes in order: driver cleanup, peripheral removal, cache repair, and the bypass methods. For the broader 24H2 problem set on HP, see our [complete HP 24H2 guide](/articles/how-to-fix-windows-11-24h2-update-problems-on-hp-laptop/).

## Why this happens

- **Driver migration timeouts:** the installer waits on each third-party driver package, and one bad HP driver can stall the phase for hours.

- **Conflicting HP custom drivers:** outdated Conexant/Bang and Olufsen audio, fingerprint, or chipset drivers from HP resist migration to the new build.

- **Connected peripherals:** USB docks, printers, and external drives inject their drivers into the migration and multiply the chances of a hang.

- **HP Wolf Security hooks:** security drivers that hook the kernel can block the migration steps that touch protected processes.

- **Corrupted staged files:** a damaged 24H2 download means the installer retries and re-verifies endlessly at the same percentage.

- **Low disk space:** migration needs working room for both builds at once; tight drives stall when the scratch space runs out.

- **Pending prior updates:** an uninstalled-but-staged cumulative update can deadlock the feature update behind it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: First, determine whether it is really stuck

Most 75 percent stalls are just slow. Acting on a healthy-but-slow install by force-rebooting is how good updates become corrupted ones, so verify before you intervene.

1. Note the exact time and percentage, then leave the laptop completely alone for two hours.
2. Watch the disk activity light (or Task Manager's disk graph via Ctrl+Shift+Esc on a second check).
3. If the percentage moves even slightly, or disk activity continues, it is working — wait.
4. Only treat it as stuck after 4+ hours with zero movement and zero disk activity.
5. If it is genuinely stuck, continue below; if it finished, run Windows Update to catch up.

### Fix 2: Force a safe restart and let it roll back

When the stall is confirmed genuine, a single forced restart triggers Windows' rollback machinery, which restores your working build. One clean rollback is far better than a corrupted half-install.

1. Hold the power button until the HP laptop fully powers off.
2. Wait 30 seconds, then power on with only the charger connected.
3. Let the Attempting to recover installation or Undoing changes screen finish — this can take an hour.
4. Do not interrupt the rollback for any reason.
5. Once back in Windows, do not immediately retry 24H2 — work the fixes below first.

### Fix 3: Disconnect everything and update HP drivers

Peripherals and stale HP drivers are the two biggest stall causes. Removing the peripherals and refreshing HP's driver stack before retrying addresses both at once.

1. Shut down fully, disconnect all USB devices, docks, SD cards, and external displays.
2. Boot up and open [HP's support site](https://support.hp.com/us-en) to check for newer drivers for your exact model.
3. Install the latest chipset, audio, and BIOS updates HP offers, with the charger connected.
4. In Device Manager, uninstall ghost or duplicate devices under USB and Human Interface Devices.
5. Restart and confirm Device Manager shows no warning icons before retrying 24H2.

### Fix 4: Clear the update cache for a fresh 24H2 download

The staged 24H2 files from the failed attempt are suspect. Clearing them forces a complete fresh download, eliminating corrupted staged data as a stall cause.

1. Open Terminal (Admin) from the Start right-click menu.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services with `net start` commands and reboot.
5. Start the 24H2 update fresh and monitor — with clean files, the 75 percent phase should progress.

### Fix 5: Temporarily pause HP security software

HP Wolf Security's kernel hooks can deadlock the driver migration phase. Pausing them for the install window is standard practice and safe as long as you re-enable immediately after.

1. Open HP Wolf Security and pause Sure Sense and related threat protections.
2. If you run a third-party antivirus alongside, pause its real-time protection too.
3. Disconnect from untrusted networks during the window if that concerns you.
4. Run the 24H2 update to completion, including all restarts.
5. Re-enable every protection layer and verify the security dashboard is green.

### Fix 6: Install 24H2 with the Installation Assistant

The standalone [Windows 11 Installation Assistant](https://www.microsoft.com/en-us/software-download/windows11) uses a different download and staging path than Windows Update, which bypasses whatever is poisoned in the automatic pipeline.

1. Back up important files first — the assistant is safe, but backups are mandatory.
2. Download the Installation Assistant from Microsoft's Windows 11 download page.
3. Run it with only the charger connected and no peripherals attached.
4. Let it download, install, and restart the laptop as many times as needed.
5. After success, run Windows Update to install any remaining cumulative updates.

### Fix 7: Free space and retry with room to breathe

Driver migration needs scratch space for both the old and new driver stores simultaneously. HP laptops with 128-256 GB drives stall here when free space is marginal.

1. Check free space: Settings, System, Storage — you want 30 GB free for 24H2.
2. Run Disk Cleanup with Clean up system files, selecting Windows Update Cleanup.
3. Uninstall large unused programs and move media off C:.
4. Empty the Recycle Bin and confirm the free-space number.
5. Retry 24H2 only after the space target is met.

## Closing

A 24H2 stall at 75 percent on an HP laptop is almost always the driver migration phase struggling with a stale HP driver, a peripheral, or corrupted staged files — not a dying machine. Verify it is truly stuck before intervening, roll back cleanly if needed, refresh HP's drivers, clear the cache, and retry with peripherals disconnected. Patience at 75 percent is a feature, not a bug. For the related stall where the machine hangs on the restarting screen instead, see our [restarting-screen fix guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/).
