---
title: "How to Fix Windows Update Stuck on the Restarting Screen on Windows 11"
slug: "how-to-fix-windows-update-stuck-on-restarting-screen-on-windows-11"
date: 2026-09-09
categories: ["windows-update"]
tags: ["stuck on restarting", "windows update", "windows 11", "boot hang"]
description: "Windows Update stuck on the Restarting screen on Windows 11? Six fixes — from safe waiting to WinRE repairs — that get your laptop booting again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-screen-on-windows-11.webp"
faqs:
  - q: "How long is too long on the Restarting screen?"
    a: "On an SSD, allow 60 minutes for a cumulative update and up to 2 hours for a feature update; on a hard drive, double both. The key test is activity: a moving spinner or blinking drive light means progress. Only consider the system hung when the spinner is completely frozen and there is no drive activity for 15 minutes or more. Most “stuck” updates are simply slow ones."
  - q: "Will force-restarting damage Windows 11?"
    a: "One forced shutdown to escape a genuinely frozen Restarting screen is safe and is the standard recovery step — Windows will usually roll back or resume the update on the next boot. The danger is repeated forced shutdowns, especially during BIOS updates (never interrupt those). Avoid making a habit of it, but do not fear the single power-button hold when the system is truly hung."
  - q: "Should I unplug USB devices?"
    a: "Yes — unplug everything: USB drives, docks, SD cards, external displays, even the mouse receiver. During the restart phase, Windows polls boot devices, and an unresponsive peripheral can stall the handoff indefinitely. Retrying the update with only the charger connected eliminates the most common environmental cause in one step."
  - q: "What does Fast Startup have to do with this?"
    a: "Fast Startup saves a hibernated kernel session to speed up booting, but that saved session can conflict with the driver versions a restart-phase update is installing. Disabling it (Control Panel, then Power Options, then “Choose what the power buttons do”) forces a clean kernel initialization on every boot, removing a whole class of restart hangs. The boot-time cost is a few seconds."
---

The blue “Restarting” screen, the spinning dots, and then… nothing. Ten minutes, thirty, an hour — the dots keep spinning (or freeze entirely) and your Windows 11 laptop never comes back. It is the most visually alarming update failure because the machine looks alive while doing nothing.

Two very different situations hide behind that screen: an update that is genuinely still working, and one that is truly hung. Telling them apart is the entire skill, because interrupting the first causes damage while waiting on the second wastes hours. Dell owners should also check the [Dell-specific restarting guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-on-dell-laptop/), which covers firmware handoff issues unique to Dell hardware.

## Why this happens

- **Update installer waiting on a hung driver swap:** The restart phase swaps drivers; a misbehaving storage or display driver can stall the handoff with the spinner running.
- **Corrupted staged update files:** Damaged files in SoftwareDistribution make the restart-phase installer retry the same broken step in a loop.
- **Fast Startup preserving a bad kernel session:** Fast Startup’s hibernated kernel state can conflict with the driver versions the update is installing, freezing the restart.
- **Peripheral devices stalling boot:** USB drives, docks, and some external displays hold the boot handshake while Windows polls unresponsive devices.
- **Insufficient disk space for the second phase:** The restart phase needs working space; a nearly full drive slows it to a crawl that looks like a hang.
- **Antivirus or encryption software intercepting boot:** Third-party boot-time drivers (AV, disk encryption) can deadlock with the update’s own boot-time operations.
- **Failing drive retrying bad sectors:** A drive repeatedly retrying marginal sectors during the file-replacement phase stretches minutes into hours.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Verify it is actually stuck before intervening

Most “stuck on Restarting” cases are slow, not stuck. The restart phase does heavy file work with minimal screen feedback, so patience is a legitimate technical step — and interrupting a healthy install creates the corruption you are trying to avoid.

1. Note the time; allow 60 minutes (SSD) or 120 minutes (HDD) for cumulative updates, double for feature updates.
2. Watch the spinner: movement means the process is alive.
3. Check the drive activity LED or listen for disk sounds.
4. Only act when the spinner is frozen AND there is no drive activity for 15+ minutes.

### Fix 2: Force a restart and let Windows recover

For a genuinely frozen system, the forced restart is the correct recovery. Windows Update is designed to handle interruption here — expect Automatic Repair or a rollback, both of which are the system protecting itself.

1. Hold the power button 10 seconds until fully off.
2. Wait 30 seconds, then power on with only the charger connected.
3. If Windows boots, check Update history for the failed entry.
4. If it boots to “Undoing changes,” let that rollback finish — see the [undoing-changes guide](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-reddit/) for what to expect.

### Fix 3: Strip peripherals and disable Fast Startup

This strips the two biggest environmental causes in one pass. Peripheral polling stalls and Fast Startup kernel conflicts account for a large share of restart-phase hangs, and both are eliminated without touching system files.

1. Unplug all USB devices, docks, cards, and external displays.
2. Power on and boot normally.
3. Open Control Panel > Power Options > “Choose what the power buttons do”.
4. Click “Change settings that are currently unavailable” and uncheck “Turn on fast startup”, then retry the update.

### Fix 4: Uninstall the stuck update from WinRE

If Windows will not boot after the forced restart, WinRE lets you surgically remove the update that caused the hang. Your files are untouched — only the offending update is uninstalled.

1. Trigger WinRE: interrupt boot twice at the logo, or hold Shift while clicking Restart.
2. Go to Troubleshoot > Advanced options > Uninstall Updates.
3. Remove the latest quality update (or feature update if that fails).
4. Restart and pause updates for 7 days while you apply the remaining fixes.

### Fix 5: Clear the update cache in Safe Mode

Corrupted staged files make the restart installer loop on the same broken step. Clearing the cache in Safe Mode (where nothing holds the files locked) forces a clean re-download and a clean restart phase.

1. Boot to Safe Mode via WinRE > Startup Settings.
2. Elevated Command Prompt: net stop wuauserv, then net stop bits.
3. Delete the cache: rd /s /q C:\Windows\SoftwareDistribution.
4. Restart normally and retry the update; if problems persist, check [Microsoft’s update support](https://support.microsoft.com/en-us/windows).

### Fix 6: Check drive health and free space

When hangs recur across different updates, suspect the storage. A drive retrying bad sectors during the file-replacement phase looks exactly like a software hang, and no cache trick fixes hardware.

1. Run chkdsk C: /f from an elevated prompt (restart if scheduled).
2. Check SMART health via your laptop maker’s diagnostics.
3. Free space to at least 20 percent of the drive.
4. If the drive is failing, replace it before retrying large updates — a dying drive turns every update into a hang.

### Fix 7: Turn off automatic restart to see hidden error screens

Some restart-phase failures flash a blue error screen for a fraction of a second before the spinner returns — too fast to read, but containing the real diagnostic. Disabling automatic restart on system failure freezes those screens so you can photograph the stop code. Combined with the setup logs in C:\$WINDOWS.~BT\Sources\Panther, this turns an opaque hang into a named problem with a documented fix.

1. Boot to WinRE > Troubleshoot > Advanced options > Startup Settings > Restart.
2. Press 9 to “Disable automatic restart after failure”.
3. Retry the update and photograph any stop screen that appears instead of the spinner.
4. Look up the stop code — it usually names a driver file, which you then update from the manufacturer.
5. Re-enable normal behavior afterward; the setting resets on its own after a successful boot.

## Closing

A Windows 11 laptop stuck on the Restarting screen is usually either still working (give it time) or tripped on something environmental — a peripheral, Fast Startup, a bad cache, or a failing drive. Verify the hang is real, restart cleanly, strip the environment to basics, and repair the staging. The spinner almost always gives way.
