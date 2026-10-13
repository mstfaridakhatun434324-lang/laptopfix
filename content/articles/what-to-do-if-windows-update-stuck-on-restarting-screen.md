---
title: "Windows Update Stuck on the Restarting Screen: What to Do Right Now"
slug: what-to-do-if-windows-update-stuck-on-restarting-screen
date: 2026-10-11
categories: ["windows-update"]
tags: ["stuck on restarting", "windows update stuck", "restart loop", "windows 11", "windows 10"]
description: "Your laptop is stuck on the 'Restarting' screen during Windows Update. Learn when to wait, when to intervene, and how to recover without corrupting the update."
thumbnail: "/images/thumbs/what-to-do-if-windows-update-stuck-on-restarting-screen.webp"
faqs:
  - q: "How long should I wait on the Restarting screen before doing anything?"
    a: "Wait at least 60 to 90 minutes on a spinning Restarting screen before intervening, longer for major feature updates. Updates genuinely need this time on slower drives. Intervening too early is the most common way a stuck update becomes a corrupted one."
  - q: "Is it safe to force shutdown during a stuck update?"
    a: "It carries risk but is sometimes necessary. After 90+ minutes with zero progress indicators, a forced shutdown is the standard recovery step, and Windows is designed to roll back gracefully. The danger is interrupting an update that was actually still working, which is why the waiting period matters."
  - q: "Why does my laptop get stuck on Restarting after every update?"
    a: "Recurring stuck restarts usually point to a driver that hangs during shutdown — often display, storage, or network drivers — or to fast startup conflicting with the update's restart sequence. Updating drivers and disabling fast startup, as covered below, typically breaks the pattern."
  - q: "What if it is stuck on Restarting with no spinning dots?"
    a: "A frozen screen with no animation for more than 30 minutes almost certainly means the system has truly hung rather than working slowly. The dots stopping is your signal that waiting longer will not help, and you can move to the forced shutdown step sooner."
---

The "Restarting" screen with its spinning dots is supposed to last a minute or two. When it stretches past half an hour, every instinct says to hold the power button — and every instinct is fighting the one piece of knowledge that matters: interrupting a working update can corrupt it. So the real skill here is telling a slow update from a stuck one, and this guide gives you that judgment call plus the full recovery ladder if the update has genuinely hung.

First, the waiting rule: give it 60 to 90 minutes if the dots are still animating. Major updates on older hard drives legitimately take that long. Only when the animation freezes, or the wait stretches far beyond reason, do you intervene. If the stuck restart eventually resolves into a rollback, the [guide to undoing-changes boot loops](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck/) picks up that story.

There is also a useful distinction between the restart hanging and the update failing. A hang at the Restarting screen means the shutdown-and-restart sequence stalled \u2014 often a driver refusing to shut down \u2014 while the update itself may be perfectly fine and simply waiting for the restart to complete. That is why the fixes below target the restart mechanism (drivers, fast startup, shutdown blockers) as much as the update. If the underlying update is itself broken and fails every time it runs, the [cumulative update failure guide](/articles/how-to-fix-cumulative-update-fails-every-time-on-laptop/) addresses that separate problem.

## Why this happens

- **Slow drive, big update:** Feature updates on spinning hard drives or nearly full SSDs genuinely need an hour or more at the Restarting stage — many "stuck" updates are just slow ones.
- **Hanging shutdown driver:** A display, storage, or network driver that fails to respond to the shutdown request stalls the entire restart sequence.
- **Fast startup conflicts:** Windows fast startup saves a kernel hibernation state that can conflict with the update's expected clean restart, hanging the handoff.
- **Pending file operations queue:** A huge backlog of pending file renames and replacements makes the restart phase take far longer than the screen suggests.
- **Third-party software blocking shutdown:** Antivirus, backup tools, or system utilities that refuse to terminate hold the shutdown hostage.
- **Corrupt update payload:** A damaged update that passed initial checks can hang when the installer actually tries to apply it during restart.
- **Failing drive sectors:** The restart phase does heavy disk I/O; marginal sectors that were fine at idle start erroring under load and stall progress.
- **Windows Update service in a bad state:** A wedged update service can leave the restart orchestrator waiting for a signal that never comes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait properly — and watch the dots

Do not skip this; most premature interventions happen here.

1. Note the time and confirm the dots are still animating. Animating dots mean the system is alive.
2. Wait a full 60–90 minutes from when the screen appeared (longer for feature updates).
3. Listen for drive activity and check for heat from vents — both suggest real work is happening.
4. Only proceed to Fix 2 if the dots have frozen for 30+ minutes or the wait has clearly exceeded reason.

### Fix 2: Force a shutdown and let Windows recover

1. Press and hold the power button for 10 seconds until the laptop powers off completely.
2. Unplug the AC adapter and, if the battery is removable, remove it for 30 seconds (skip this on sealed laptops).
3. Reconnect power and turn the laptop on.
4. Windows will typically resume the update or roll it back automatically. Let whichever process starts run to completion without interrupting it.

### Fix 3: Boot into Safe Mode if normal boot hangs

1. Force shutdown twice in a row during the Windows logo to trigger Automatic Repair.
2. Go to Troubleshoot, Advanced options, Startup Settings, Restart, then press 4 for Safe Mode.
3. In Safe Mode, open Settings, Windows Update, and check the update status.
4. If the update shows as failed, note the error code; if it shows pending, try installing it from Safe Mode with Networking.

### Fix 4: Disable fast startup

Fast startup is a frequent repeat offender for restart hangs.

1. Boot normally (or into Safe Mode), open Control Panel, Power Options.
2. Click "Choose what the power buttons do", then "Change settings that are currently unavailable".
3. Untick "Turn on fast startup" and save changes.
4. Restart normally and retry the update. If restarts now complete cleanly, leave fast startup off — the boot-time cost is a few seconds.

### Fix 5: Update the drivers that hang shutdowns

1. In Device Manager, update display, storage controller, and network adapter drivers — use the manufacturer's site for the exact model.
2. Pay special attention to the display driver: use [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx) or [AMD's driver page](https://www.amd.com/en/support/download/drivers.html) for discrete GPUs rather than relying on Windows Update's older copies.
3. Restart and confirm shutdowns complete promptly before running the next update.

### Fix 6: Clear the update cache and reset components

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Delete the contents of C:\Windows\SoftwareDistribution.
4. Restart the services, reboot, and check for updates. If the previously hanging update was corrupt, the fresh download often sails through.

### Fix 7: Run system repairs and check the drive

1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated Command Prompt.
2. Run `chkdsk C: /f` and schedule it for restart if prompted.
3. After these complete, retry the update. If restarts still hang at this point, the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) documents deeper recovery options including startup repair from installation media.

### Fix 8: Repair startup from installation media

If the laptop cannot boot cleanly after the forced shutdown, repair it externally.

1. Create Windows installation media on another PC using Microsoft's Media Creation Tool.
2. Boot the stuck laptop from the USB drive and choose Repair your computer.
3. Go to Troubleshoot, Advanced options, Startup Repair, and let it run.
4. If Startup Repair does not resolve it, use System Restore from the same menu to return to a pre-update restore point.

## Closing

A stuck Restarting screen is a patience test first and a technical problem second. The waiting period protects you from turning a slow update into a broken one, and the recovery ladder \u2014 forced shutdown, Safe Mode, fast startup off, driver updates, and if needed, media-based startup repair \u2014 resolves the genuine hangs. If this happens after every update rather than once, treat it as the driver or fast-startup pattern it almost certainly is, and fix the pattern instead of dreading each Patch Tuesday.
