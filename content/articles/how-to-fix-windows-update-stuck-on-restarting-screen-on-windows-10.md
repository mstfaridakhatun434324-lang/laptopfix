---
title: "How to Fix Windows Update Stuck on the Restarting Screen on Windows 10"
slug: "how-to-fix-windows-update-stuck-on-restarting-screen-on-windows-10"
date: 2026-09-10
categories: ["windows-update"]
tags: ["stuck on restarting", "windows update", "windows 10", "boot hang"]
description: "Windows Update stuck on the Restarting screen on Windows 10? Six fixes tuned for Windows 10 — wait-time rules, WinRE recovery, and Fast Startup fixes."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-screen-on-windows-10.webp"
faqs:
  - q: "How long should Windows 10 sit on Restarting?"
    a: "On Windows 10 with an SSD, allow 60 minutes for cumulative updates and up to 2 hours for feature updates; with a mechanical hard drive, allow 2–4 hours. Windows 10’s restart phase on HDDs is genuinely slow. Judge by activity, not the clock alone: a moving spinner or drive sounds mean work is happening. Intervene only when the spinner is frozen and the drive is silent for 15+ minutes."
  - q: "Is it safe to force-shutdown Windows 10 here?"
    a: "A single forced shutdown on a truly frozen Restarting screen is the accepted recovery step and rarely causes harm — Windows 10 will typically roll back or resume the update at next boot. Do not do it repeatedly, and never interrupt a BIOS update. The real risk is interrupting a healthy-but-slow update, which is why verifying the hang (frozen spinner, silent drive) comes before the power button."
  - q: "Should I unplug everything?"
    a: "Yes. Disconnect USB drives, docks, printers, SD cards, and external displays before retrying the update. During the restart phase, Windows 10 polls hardware, and a sluggish or unresponsive device can stall the handoff. Many users find the update sails through on the second attempt with only the charger attached — the peripheral was the entire problem."
  - q: "How do I disable Fast Startup on Windows 10?"
    a: "On Windows 10, open Control Panel, then Power Options, then “Choose what the power buttons do,” click “Change settings that are currently unavailable,” and uncheck “Turn on fast startup.” Fast Startup’s hibernated kernel session can conflict with driver replacements during the restart phase. Disabling it forces a full clean boot every time, at the cost of a few extra seconds of boot time."
---

Windows 10’s blue “Restarting” screen has ended more evenings than any other update screen. The dots spin, the minutes pass, and the laptop never returns — particularly on the many Windows 10 machines still running mechanical hard drives, where the restart phase is genuinely, painfully slow.

That slowness is the trap: Windows 10 gives you no progress indicator during this phase, so a healthy-but-slow install looks identical to a hung one for the first hour. The Windows 11 version of this hang is covered in the [Windows 11 restarting guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-on-windows-11/) — the recovery steps overlap, but the wait budgets differ significantly by OS and drive type.

## Why this happens

- **Slow mechanical drive stretching the phase:** On Windows 10 laptops still running HDDs, the restart phase’s file work legitimately takes hours — most “hangs” are impatience.
- **Corrupted staged files looping the installer:** Damaged SoftwareDistribution contents make the restart-phase installer retry the same step endlessly.
- **Fast Startup kernel-session conflict:** The hibernated kernel session Fast Startup restores can clash with drivers the update is replacing mid-restart.
- **USB devices stalling the boot handshake:** External drives and docks that do not respond promptly hold the restart handoff open.
- **Antivirus boot drivers deadlocking:** Third-party boot-time security drivers can deadlock with the update’s own boot operations.
- **Pending operations from an earlier update:** Unfinished business from a previous update collides with the new restart phase.
- **Failing drive or full disk:** Bad sectors or under 10 percent free space turn the file-replacement phase into a crawl or a stall.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Set a hardware-appropriate wait budget

Windows 10 on a spinning hard drive is the slowest mainstream update experience still in common use, and most “stuck” reports are simply slow installs. Calibrating your wait to the hardware prevents the number-one cause of update corruption: interrupting a working install.

1. Identify your drive type: SSD (60–120 min budget) or HDD (2–4 hour budget for feature updates).
2. Watch for spinner movement and drive activity as signs of life.
3. Do not judge by the percentage — the restart phase shows no percentage.
4. Only proceed when frozen spinner plus silent drive persists 15+ minutes.

### Fix 2: Force a clean restart with peripherals detached

Once the hang is verified real, the forced restart is the way out. Windows 10 handles this interruption gracefully in the vast majority of cases — the rollback machinery exists precisely for this moment.

1. Hold power 10 seconds for a full shutdown.
2. Disconnect all peripherals except the charger.
3. Power on and observe: normal boot, Automatic Repair, or “Undoing changes”.
4. Let any rollback complete; note the failed update in Update history afterward.

### Fix 3: Remove the offending update in WinRE

WinRE’s uninstall option removes the update that hung the restart without touching personal files. It is the surgical fix when Windows will not boot normally after the forced restart.

1. Interrupt boot twice at the Windows logo to reach Automatic Repair.
2. Choose Troubleshoot > Advanced options > Uninstall Updates.
3. Try “Uninstall latest quality update” first, then the feature update if needed.
4. Restart; pause updates 7 days via Settings > Update & Security > Windows Update > Advanced options.

### Fix 4: Clear the corrupted cache from Safe Mode

Safe Mode gives you the file locks-free environment to delete the corrupted staging. The next update check re-downloads everything cleanly, and the restart phase gets a fresh, uncorrupted payload.

1. From WinRE: Troubleshoot > Advanced options > Startup Settings > Restart, press 4 for Safe Mode.
2. Elevated prompt: net stop wuauserv, then net stop bits.
3. Run: rd /s /q C:\Windows\SoftwareDistribution.
4. Restart normally; for persistent trouble see [Microsoft’s update support](https://support.microsoft.com/en-us/windows).

### Fix 5: Prevent recurrence: Fast Startup, AV hooks, drive health

With the immediate hang resolved, prevent the next one: Fast Startup off removes kernel-session conflicts, and trimming boot-time security hooks removes deadlock partners. Persistent hangs across updates point at the drive itself.

1. Disable Fast Startup: Control Panel > Power Options > “Choose what the power buttons do” > uncheck “Turn on fast startup”.
2. Temporarily disable third-party antivirus boot-time protection.
3. Retry the update with a minimal environment.
4. If hangs persist across updates, run chkdsk C: /f and check SMART health — and compare notes with the [Windows 11 restarting guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-on-windows-11/) for shared causes.

### Fix 6: Use System Restore to return to a known-good state

When a Windows 10 update hangs the restart phase repeatedly and the usual repairs are not sticking, System Restore offers a clean slate: roll the system back to a restore point from before the update attempts began, then approach the update with all the preventive fixes (cache cleared, Fast Startup off, peripherals detached, drivers current) already in place. Restore points capture drivers, registry, and system files — exactly the layers a botched update disturbs — while leaving your personal files untouched. The key is having a restore point at all: Windows 10 sometimes disables System Protection on SSDs to save space, so verify it is on before you need it. After restoring, do not simply retry the same update the same way; apply the full preparation sequence first, because the restore only buys you a second chance — it does not fix whatever caused the hang.

1. Boot to WinRE > Troubleshoot > Advanced options > System Restore.
2. Choose a restore point dated before the update troubles began.
3. Let the restore complete and boot into Windows normally.
4. Immediately apply the preventive fixes: clear the update cache, disable Fast Startup, detach peripherals.
5. Update key drivers from the manufacturer, then retry the Windows update.
6. Afterward, verify System Protection is enabled (System Properties > System Protection) so a restore point exists next time.

## Closing

On Windows 10, the Restarting screen demands one virtue above all: patience calibrated to your hardware. HDDs need hours, SSDs need up to an hour — and only a truly frozen spinner with a silent drive justifies the power button. After that, the recovery path (WinRE, cache clear, environment strip) is the same reliable sequence that has fixed this hang for a decade. The recovery sequence itself is OS-agnostic — our [general restarting-screen guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-on-laptop/) walks through the same wait-budget and recovery logic for any laptop, in case you're fixing one of these for someone on a newer Windows.
