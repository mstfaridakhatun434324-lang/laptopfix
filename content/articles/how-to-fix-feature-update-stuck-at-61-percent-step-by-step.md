---
title: "Feature Update Stuck at 61 Percent? Step-by-Step Fix"
slug: how-to-fix-feature-update-stuck-at-61-percent-step-by-step
date: 2026-09-22
categories: ["windows-update"]
tags: ["feature update stuck", "61 percent", "windows 11", "update stuck"]
description: "Feature update frozen at 61%? That percentage usually means the driver migration phase. Follow this step-by-step to unstick it safely without breaking Windows."
thumbnail: "/images/thumbs/how-to-fix-feature-update-stuck-at-61-percent-step-by-step.webp"
faqs:
  - q: "Why do feature updates always seem to stall at 61 percent?"
    a: "Because 61% falls in the driver and feature migration phase, where Windows moves your drivers and settings into the new build. If one driver resists migration, the whole phase waits on it — the percentage freezes while the installer retries in the background."
  - q: "How long should I wait at 61 percent before acting?"
    a: "Give it at least two hours on an SSD, three to four on a hard drive, with the laptop plugged in and idle. Migration is disk-heavy and genuinely slow. Only treat it as stuck after hours of zero progress with idle disk activity."
  - q: "Is it safe to force-restart a feature update stuck at 61%?"
    a: "It is safer than at most other percentages, because 61% is still in the pre-reboot migration phase — Windows has not yet committed to the new build. Hold the power button only after the waiting period above, and expect an automatic rollback on reboot."
  - q: "Will I have to download the whole feature update again?"
    a: "Possibly. After a forced restart and rollback, Windows Update usually resumes or restarts the download. The migration-phase work is discarded, but that is preferable to a half-migrated system. Delivery Optimization may reuse validated chunks, so the re-download is sometimes faster than the first attempt."
---

Feature updates have a tell: they sail through the download, climb steadily through the install percentages, and then park at 61 percent. Hours pass. The circle spins. The percentage does not move. If this sounds familiar, you are experiencing the most-reported stall point in Windows feature updates — the migration phase, where Windows transfers your drivers, apps, and settings into the new build.

The good news about 61 percent specifically is where it sits in the process: before the point of no return. The update has not committed to the new Windows build yet, which gives you safer recovery options than a stall at 90 percent would. This step-by-step guide starts with the waiting game (done correctly), moves through safe intervention, and ends with the driver cleanup that prevents the next attempt from stalling in the same place.

The percentages tell a story if you know the phases. The early percentages cover download and staging; the 40-to-75 range is migration, where drivers and settings move into the new build; beyond that comes the second-boot phase that actually commits the new Windows. Sixty-one percent sits squarely in migration — before the point of no return. That is why the forced restart is safe here and reckless at 90 percent. The installer has not committed anything yet; it is still packing boxes, and you are allowed to stop the movers.

## Why this happens

- **A driver refusing migration.** One incompatible driver — often storage, display, or a third-party filter — blocks the entire migration phase.
- **Antivirus filter drivers hooking the migration.** Security products with deep system hooks resist the driver's handoff to the new build.
- **Corrupted migration state from a previous attempt.** A prior interrupted feature update left partial migration data that confuses the new attempt.
- **Insufficient disk space for the migration scratch area.** The migration needs gigabytes of working room beyond the download itself.
- **External devices complicating driver migration.** USB drives, docks, and peripherals add drivers the migrator must handle.
- **A damaged component store.** Store corruption fails the file operations the migration phase performs.
- **Pending operations from monthly updates.** Unfinished cumulative-update transactions hold locks the feature update needs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait it out properly — on AC power, idle

Step one is genuine patience, because migration is slow, not necessarily stuck.

1. Plug into AC power — migration throttles on battery.
1. Close all apps and leave the machine alone for 2 to 4 hours.
1. Check disk activity in Task Manager periodically; activity means progress.
1. If the percentage moves even slightly, keep waiting — it is working. A related but distinct stall is the [Update Assistant stuck at 99 percent](/articles/how-to-fix-update-assistant-stuck-at-99-percent-on-lenovo-laptop/) during manual upgrades.

### Fix 2: Remove external devices

Every attached device is migration work the installer must complete.

1. Unplug USB drives, docks, printers, and external monitors.
1. Remove SD cards and disconnect Bluetooth peripherals.
1. Leave only the power adapter connected.
1. Wait another hour — simplified hardware often unblocks the migration.

### Fix 3: Force a restart only after the waiting period

The safe intervention when the stall is confirmed.

1. Hold the power button for 10 seconds to force off.
1. Power on — Windows should detect the incomplete update and roll back automatically.
1. The rollback can take 30 to 60 minutes; let it finish.
1. Log in and verify you are back on the previous build in **Settings** > **System** > **About**.

### Fix 4: Clear the update cache and pending operations

Remove the failed attempt's leftovers before retrying.

1. In an elevated Command Prompt, stop wuauserv, cryptSvc, bits, and msiserver.
1. Rename `C:\Windows\SoftwareDistribution` and `C:\Windows\System32\catroot2`.
1. Restart the services.
1. This wipes the stalled 61% attempt so the retry starts clean. If the retry stalls identically, the cause is a driver — continue.

### Fix 5: Update or remove the blocking driver

The 61% stall is a driver problem until proven otherwise.

1. Open **Device Manager** and update storage controllers, display adapters, and network adapters.
1. Get drivers from your maker: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
1. Temporarily uninstall third-party antivirus and any disk-encryption filter drivers.
1. Also disconnect from VPNs — virtual network adapters complicate migration.

### Fix 6: Free space and run the update troubleshooter

Cover the environmental causes before the final retry.

1. Ensure 30 GB free on C: — feature updates need more room than cumulative ones.
1. Run **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update**.
1. Run `DISM /Online /Cleanup-Image /RestoreHealth` and `sfc /scannow`.
1. Restart and attempt the feature update again, on AC power, idle.

### Fix 7: Use the Installation Assistant as an alternative path

When Windows Update's feature-update path keeps stalling at the same point.

1. Download the Windows 11 Installation Assistant from Microsoft's official Windows 11 download site.
1. Run it with external devices unplugged and antivirus temporarily disabled.
1. The Assistant uses a different orchestration that sometimes sails past WU-specific stalls.
1. If it also stalls at the same phase, the blocking driver still needs identifying — check `C:\$Windows.~BT\Sources\Panther\setupact.log` for the failing component. Brand-specific 61% notes: [61% stuck on HP](/articles/how-to-fix-feature-update-stuck-at-61-percent-on-hp-laptop/).

### Fix 8: Identify the stalling driver in setupact.log

When the stall repeats, let the logs name the driver.

1. Open `C:\$Windows.~BT\Sources\Panther\setupact.log` after a failed attempt.
1. Search for `Failed` or `0x` error entries near the end of the log.
1. The failing driver's .inf or .sys name appears in the migration error lines.
1. Update or uninstall that specific driver before the next attempt — targeted beats generic.

## Closing

A feature update parked at 61 percent is waiting on driver migration, and the fix is to simplify what it has to migrate: unplug everything, update or remove the blocking driver, clear the failed attempt, and retry on AC power with room to work. Because 61% sits before the point of no return, even the forced restart is safe — but with the driver cause addressed, you should not need it.
