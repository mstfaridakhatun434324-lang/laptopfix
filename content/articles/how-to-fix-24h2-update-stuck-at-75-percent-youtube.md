---
title: "24H2 Update Stuck at 75%? Video-Style Fixes to Push It Through"
slug: how-to-fix-24h2-update-stuck-at-75-percent-youtube
date: 2026-09-15
categories: ["windows-update"]
tags: ["24h2", "stuck at 75", "feature update stuck", "windows 11", "installation frozen"]
description: "The 24H2 update has been sitting at 75% for hours. Here's what that percentage means and the visual, step-by-step fixes to get it moving."
thumbnail: "/images/thumbs/how-to-fix-24h2-update-stuck-at-75-percent-youtube.webp"
faqs:
  - q: "What does 75% mean during the 24H2 update?"
    a: "Around 75%, the installer is typically in the driver migration and second-boot phases — moving your drivers into the new OS image and finalizing system configuration. Stalls here usually mean a driver is hanging during migration or the disk is struggling with the heavy write workload. It is a phase problem, not a percentage problem."
  - q: "How long should I wait at 75% before acting?"
    a: "Give it at least three hours of genuine inactivity before intervening. Feature updates do enormous disk I/O at this stage, and slow SSDs or hard drives can look frozen while working. Check Task Manager's disk activity from another angle if you can — sustained activity means progress, even without percentage movement."
  - q: "Is it safe to force restart at 75%?"
    a: "It is reasonably safe. At 75% the new OS is staged but your old system is preserved for rollback. A forced shutdown triggers the automatic rollback to your previous build, which is the designed recovery path. The riskier interruption point is much later, during the final boot configuration."
  - q: "Why does it always stall at the same percentage?"
    a: "Consistent stalls at one percentage point to a deterministic blocker: the same driver hanging, the same disk sector failing, or the same corrupted payload. Random stalls suggest flaky hardware; repeatable stalls suggest a specific component you can identify and fix."
---

Seventy-five percent is where 24H2 updates go to contemplate their existence. The progress bar freezes, the spinner keeps its brave face, and hours pass. Video tutorials love this problem because it is visual and dramatic — but the fixes are methodical, not magical. This text walkthrough gives you the same steps at your own pace.

At 75%, the installer is migrating drivers and finalizing the new system image. A stall here means something in that migration is wedged. The plan: confirm the stall, recover safely, remove the blocker, and reinstall.


The most important tool for this problem is patience with measurement: note the exact time the percentage froze and check back at defined intervals rather than staring at the screen. A watched progress bar never moves, but a checked one tells you the truth. The steps below assume you have confirmed a genuine stall, not just a slow phase.
## Why this happens

- **Driver hanging during migration:** A single bad driver stalls the entire driver migration phase.
- **Slow or failing disk:** The heavy write workload at 75% exposes marginal storage.
- **Low disk space:** The migration needs working room it does not have.
- **Corrupted install payload:** A damaged staged image fails at the same point every time.
- **Peripheral interference:** External devices confusing the hardware migration.
- **Antivirus hooks:** Security software intercepting the migration's file operations.
- **Overheating:** Sustained high load on a dusty laptop triggering thermal throttling or shutdown.
- **Memory pressure:** The migration's RAM demands exceeding available memory on 8 GB machines.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall with disk activity

1. Wait a full **three hours** from when the percentage last moved.
2. Watch the drive activity light; sustained blinking means the installer is still working.
3. Listen for disk sounds on laptops with hard drives — silence for an hour means stuck.
4. Only proceed when you are confident it is frozen, not slow. Patience prevents unnecessary rollbacks.
5. Check the laptop's temperature — an ice-cold machine doing 'heavy work' is suspicious.
6. If you can access Task Manager via Ctrl+Shift+Esc, check disk throughput directly.

### Fix 2: Force shutdown and let it roll back

1. Hold the power button for **10 seconds** until the laptop powers off.
2. Unplug the charger, wait 30 seconds, then power on.
3. Windows will detect the interrupted upgrade and roll back to your previous build — let it finish uninterrupted.
4. Verify the desktop returns normally. The rollback is the designed safety net; trust it. If the rollback itself has issues, see our guide on [updates that undo their changes](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-windows-11/).
5. If the machine boots straight back into the installer, force shutdown again and choose Safe Mode.
6. Never pull the battery mid-rollback on older laptops — wait for a safe moment.

### Fix 3: Free space and cool the machine

1. Once back in Windows, free **30 GB** on C: — the stall may have been a space crisis.
2. Clean dust from vents and ensure the laptop sits on a hard, flat surface.
3. Run the update with the laptop plugged in and well-ventilated; thermal throttling under sustained load causes exactly these freezes.
4. Consider elevating the rear of the laptop slightly for airflow during the retry.
5. Uninstall large games or applications temporarily if space is the blocker — reinstall after.
6. Disable hibernation with powercfg /hibernate off to reclaim gigabytes quickly.

### Fix 4: Update drivers and firmware before retrying

1. Update **chipset, storage, and graphics drivers** from the manufacturer's support site.
2. Install any pending **BIOS/UEFI update** — firmware fixes for upgrade hangs are common.
3. Temporarily uninstall third-party antivirus and virtual drive software.
4. Disconnect all non-essential USB devices. For the driver-error family specifically, see our guide on [the 0xc1900101 error](/articles/how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update/).
5. Pay special attention to storage controller drivers — they govern the migration's disk access.
6. If a driver has no newer version, try the previous version instead of the latest.

### Fix 5: Clear the staged payload and repair

1. In an elevated Command Prompt: `net stop wuauserv`, `net stop bits`, empty `C:\Windows\SoftwareDistribution\Download`, restart services.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`.
3. Run Disk Cleanup with **Windows Update Cleanup** to remove the failed staging.
4. This ensures the retry downloads and stages a completely fresh copy.
5. Delete the $Windows.~BT folder after the rollback to remove the failed staging completely.
6. Verify the deletion freed significant space before retrying.

### Fix 6: Retry via the Installation Assistant

1. Download the **Windows 11 Installation Assistant** from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it with peripherals disconnected and antivirus paused.
3. The Assistant's delivery path differs from Windows Update and often sails past the stall point.
4. Monitor progress; if it stalls at 75% again, the blocker is hardware or driver-level — proceed to Fix 7.
5. Run the Assistant from an administrator account explicitly.
6. If the Assistant also stalls, capture its log file before rolling back — it names the phase.

### Fix 7: Isolate the hanging driver

1. Check **C:\$Windows.~BT\Sources\Panther\setuperr.log** after a failed attempt for named drivers.
2. Update or uninstall the implicated driver before retrying.
3. Run `chkdsk C: /f` to rule out disk errors contributing to the stall.
4. As a final option, clean-install 24H2 from USB media — a fresh install skips the migration phase entirely. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) cover clean installation.
5. Search the log for the word 'failed' and read the surrounding lines for context.
6. Address log findings one at a time, retrying between changes to isolate the fix.

## Closing

A 75% stall is the installer telling you exactly where it struggles: driver migration under heavy disk load. Confirm, roll back, clear space, refresh drivers, and retry through the Assistant. Repeatable stalls are diagnostic gold — the setup logs will name the culprit. Once past 75%, the rest of the upgrade is usually smooth sailing. The 75% stall looks dramatic but follows rules: confirm, recover, remove the blocker, retry smarter. Log-reading turns the next stall from a mystery into a ten-minute fix.
