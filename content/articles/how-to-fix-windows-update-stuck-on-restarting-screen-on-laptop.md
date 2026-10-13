---
title: "Fix Windows Update Stuck on the Restarting Screen on a Laptop"
slug: how-to-fix-windows-update-stuck-on-restarting-screen-on-laptop
date: 2026-09-05
categories: ["windows-update"]
tags: ["windows update stuck restarting", "laptop restart loop", "update stuck fix"]
description: "Windows Update stuck on the 'Restarting' screen? Learn how long to wait, how to force a safe reboot, and how to clear the update cache so the install completes."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-screen-on-laptop.webp"
faqs:
  - q: "How long should I wait on the Restarting screen before doing anything?"
    a: "On an SSD, give it at least 60 minutes before concluding it is stuck; on a spinning hard drive, allow up to two hours for a major feature update. Updates write large amounts of data, and interrupting them too early is the most common way a simple delay turns into a broken install. Watch the drive activity light if your laptop has one."
  - q: "Is it safe to force-shut-down a laptop stuck on Restarting?"
    a: "It is a last resort, but generally safe once you have waited long enough. Hold the power button for ten seconds, disconnect the charger, and remove USB devices. Modern Windows Update is transactional, meaning a failed install rolls back rather than corrupting the system. Always try waiting first, and never force a shutdown repeatedly in a row."
  - q: "Why does the Restarting screen show no percentage?"
    a: "During the restart phase, Windows is in the offline servicing portion of the update, where the progress UI is deliberately minimal. The lack of a percentage does not indicate a failure by itself. The screen is only suspicious after an hour or more of zero visible activity on an SSD-equipped laptop."
  - q: "Can a stuck Restarting screen damage my laptop?"
    a: "Almost never. The hardware is unaffected, and Windows protects itself with rollback. The real risk is interrupting the update while it writes system files, which is why patience and a proper forced reboot sequence matter more than speed. Data loss from this screen alone is extremely rare."
---

A laptop that sits on the "Restarting" screen with the spinning dots for an hour feels broken, but it usually is not. During the restart phase, Windows is deep inside the offline portion of the update — replacing locked system files, migrating drivers, and running the final commit of everything it downloaded. There is no percentage counter by design, so you cannot tell the difference between "working slowly" and "stuck" by looking at the screen.

The technician's rule is simple: time is your diagnostic tool. A feature update on a mechanical hard drive can legitimately spend 60–90 minutes on this screen. On an SSD, 20–40 minutes is normal for a big update and under 10 for a cumulative one. If you have exceeded those numbers with zero drive activity, you are dealing with a genuinely stuck restart, and the fixes below will get you out of it. This guide works on any brand — the mechanics are identical, since [the restarting-screen hang in Windows 11 24H2](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/) follows the same pattern.

## Why this happens

- **A driver install stalls mid-restart:** Graphics, storage, and network drivers install during the offline phase. A mismatched driver can hang the whole sequence silently.
- **Pending file operations never complete:** The update queues thousands of file replacements. One locked or corrupted file blocks the entire commit, like a single car stalling in a tunnel.
- **Corrupted update cache:** Partially downloaded packages in the SoftwareDistribution folder make Windows retry operations that can never succeed.
- **Slow or failing storage:** An aging hard drive with bad sectors takes far longer than expected, and a dying drive can stall reads indefinitely.
- **Low disk space on the system drive:** The offline phase needs several gigabytes of scratch space. Below roughly 10 GB free, the install can freeze partway through.
- **USB peripherals blocking the restart:** External drives, docks, printers, and even some phones can confuse the boot sequence during a restart-heavy update.
- **Third-party antivirus or disk encryption fighting the update:** Kernel-level security software can intercept file operations the update needs, causing a deadlock.
- **Interrupted previous update:** A laptop that was force-shut-down during an earlier update may have left the servicing stack in an inconsistent state that now blocks every restart.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give it the right amount of time, then confirm it is truly stuck

1. Note the exact time and leave the laptop alone for **60 minutes** (SSD) or **up to 2 hours** (hard drive, feature update).
2. Listen and watch: a churning hard drive or a blinking drive-activity LED means work is happening — keep waiting.
3. If there is zero activity and the screen has not changed after those windows, you can safely conclude it is stuck and move to Fix 2.
4. Do not press keys or click anything during this period; input does nothing useful and can occasionally interfere.

### Fix 2: Perform a clean forced reboot

1. Disconnect **all USB devices** — external drives, docks, printers, dongles, phones. Keep only the charger.
2. Hold the power button for **10 full seconds** until the laptop powers off completely.
3. Unplug the charger for 30 seconds (on models with removable batteries, remove the battery too).
4. Reconnect the charger and power on. Windows will usually resume the update or begin rolling back automatically.
5. If the screen shows "Undoing changes made to your computer," let it finish — it can take 30–60 minutes. Forcing another shutdown here causes real damage. If the rollback itself hangs, see the guide on [Windows Update undoing changes stuck](/articles/how-to-fix-windows-update-undoing-changes-stuck-on-dell-laptop/).

### Fix 3: Boot into the Recovery Environment and run Startup Repair

1. Power on the laptop and force it off **three times in a row** while the Windows logo shows (hold power 10 seconds each time). On the third boot, WinRE loads automatically.
2. Go to **Troubleshoot → Advanced options → Startup Repair**.
3. Let it run — it fixes boot files the interrupted update may have damaged.
4. Restart normally when it finishes and check whether the update completes.

### Fix 4: Clear the update cache from Safe Mode

1. In WinRE (from Fix 3), go to **Troubleshoot → Advanced options → Startup Settings → Restart**, then press **5** for Safe Mode with Networking.
2. Open an elevated Command Prompt (right-click Start → Terminal (Admin)).
3. Stop the update services: `net stop wuauserv` and `net stop bits`.
4. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
5. Restart the services: `net start wuauserv` and `net start bits`.
6. Reboot normally and check **Settings → Windows Update** — the update will re-download fresh.

### Fix 5: Repair system files from the recovery command prompt

1. In WinRE, open **Troubleshoot → Advanced options → Command Prompt**.
2. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` to scan the offline Windows installation.
3. Then run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth` to repair the component store (needs internet via Wi-Fi in WinRE on most models, or a Windows USB).
4. Restart and retry the update. Corrupt system files are a frequent hidden cause of restart hangs.

### Fix 6: Use System Restore to roll back cleanly

1. In WinRE, go to **Troubleshoot → Advanced options → System Restore**.
2. Pick the restore point created just before the update (Windows normally makes one automatically).
3. Complete the restore and boot normally — your files are untouched, only system state rolls back.
4. Before retrying the update, free up disk space and disconnect peripherals (see Fixes 2 and 7).

### Fix 7: Free disk space and retry the update on your terms

1. Once booted normally, open **Settings → System → Storage** and ensure at least **15 GB free** on C:.
2. Run Disk Cleanup as administrator and select "Windows Update Cleanup" to remove gigabytes of stale update files.
3. Update drivers from your manufacturer's site before retrying — outdated storage and graphics drivers are the top trigger.
4. Retry the update manually from **Settings → Windows Update**, with only the charger connected. A manual retry after cleanup succeeds in the majority of stuck-restart cases. If a specific package keeps failing, search for its KB number on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it standalone.

## Closing

A stuck Restarting screen is almost always a software logistics problem, not a dying laptop. The winning sequence is patience first, then a clean forced reboot, then cache-clearing and file repair — in that order. If you have walked through all seven fixes and the update still hangs at restart, the nuclear option is an in-place repair install using the Media Creation Tool, which reinstalls Windows while keeping your files and apps. That fixes virtually every servicing-stack issue, and it beats a clean reinstall every time.
