---
title: "Windows Update Stuck on Restarting Screen? Fix It Fast"
slug: how-to-fix-windows-update-stuck-on-restarting-screen
date: 2026-09-29
categories: ["windows-update"]
tags: ["windows update stuck on restarting", "restarting screen stuck", "update stuck at restart", "windows 11 restarting loop"]
description: "Stuck on the Restarting screen during a Windows update? Learn when to wait, when to force a shutdown, and how to recover safely."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-screen.webp"
faqs:
  - q: "How long should I wait on the Restarting screen?"
    a: "For a major update, up to two hours can be legitimate, especially on slower drives. If the spinner is still animating, the system is likely still working. Only intervene when the screen is completely frozen with no animation for over an hour."
  - q: "Is it safe to force-shutdown during Restarting?"
    a: "It carries risk, but a truly stuck restart will not resolve itself. Hold the power button for 10 seconds only after the screen has shown zero activity for well over an hour. Windows is designed to roll back incomplete updates on the next boot."
  - q: "Why does my laptop get stuck on Restarting during updates?"
    a: "It carries risk, but a truly stuck restart will not resolve itself. Hold the power button for 10 seconds only after the screen has shown zero activity for well over an hour. Windows is designed to roll back incomplete updates safely on the next boot."
  - q: "What if it gets stuck on Restarting every update?"
    a: "Recurring stuck restarts point at a systematic cause: disable Fast Startup, update chipset and storage drivers, disconnect peripherals during updates, and check for a specific update that always triggers it in your update history. Fix the pattern once and every future update benefits."
---

Few sights inspire as much dread as the Restarting screen that never ends. The update reached its reboot phase, the spinner started, and then... nothing. Minutes become an hour, the dots keep circling or freeze entirely, and you are left wondering whether touching the power button will brick the machine.

Here is the technician's perspective: a stuck Restarting screen is usually a shutdown that cannot finish, not an update that cannot install. Some driver or service is refusing to unload, and Windows is waiting politely for something that will never comply. The update itself is typically staged and safe; it is the handoff that is wedged.

The strategy is patience first, then decisive action. The steps below tell you exactly how long to wait, how to force the issue safely when waiting fails, and how to prevent the encore.

Patience is a diagnostic tool. A restart that is merely slow and a restart that is truly stuck demand opposite responses — waiting versus force-shutdown — and telling them apart is the skill this guide teaches first. The disk activity light is your oracle: flickering means work, dark means wedged. Everything below builds on that single distinction.

## Why this happens

- **Hanging driver during shutdown.** A driver, often storage, network, or USB, refuses to unload and blocks the restart sequence.

- **Fast Startup conflict.** Hybrid shutdown state confuses the update's restart, leaving the boot wedged.

- **External devices blocking shutdown.** USB devices and docks whose drivers will not release keep the shutdown phase alive indefinitely.

- **Stuck servicing operation.** A pending update transaction that cannot complete holds the restart hostage.

- **Corrupt update payload.** A damaged staged update can hang the phase that applies it during reboot.

- **Third-party services refusing to stop.** Antivirus and system utilities that ignore the shutdown request stall the sequence.

- **Disk errors.** Failing storage slows the write phase of the restart to a crawl that looks like a hang.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Wait it out, properly

The hardest fix is doing nothing, but premature force-shutdowns cause the very corruption you fear. Big updates on hard drives legitimately take a long time, and the spinner is evidence of life. Mechanical hard drives are the slowest legitimate case; an update restart on a 5400 RPM drive can genuinely take over an hour while the SSD next to it finishes in minutes.

1. Give it at least 60 to 90 minutes if the animation is still moving.
2. Watch for disk activity: a flickering drive LED or faint drive sounds mean work is happening.
3. Only proceed to force-shutdown if the animation is fully frozen for over an hour with no disk activity.

### Fix 2: Fix 2: Force shutdown and power-drain

When the screen is truly dead, cut the power decisively. A full power drain clears the wedged hardware state that a normal forced shutdown can leave behind. The 15-second power-button hold with everything disconnected drains residual charge from capacitors, clearing hardware states a simple force-off leaves behind.

1. Hold the power button for a full 10 seconds until the laptop turns off.
2. Unplug the charger and all USB devices. If the battery is removable, remove it.
3. Hold the power button for 15 seconds with everything disconnected, then reconnect only the charger and boot.

### Fix 3: Fix 3: Boot into Windows Recovery and run Startup Repair

If the boot after the force-shutdown is abnormal, WinRE's Startup Repair fixes the boot files the interrupted restart may have damaged. Startup Repair logs to the SrtTrail.txt file under the LogFiles folder; if it reports it could not repair, that log names what it tried.

1. Force-shutdown during boot twice in a row to trigger Automatic Repair, or boot holding Shift while clicking Restart if you can reach Windows.
2. In WinRE, choose Troubleshoot, then Advanced options, then Startup Repair.
3. Let it run and reboot normally.

### Fix 4: Fix 4: Uninstall the problematic update in Safe Mode

If the same update triggers the stuck restart every time, remove it. Safe Mode loads a minimal driver set that sidesteps the hanging driver. In Safe Mode, also pause updates for a week from Settings so the offending update does not reinstall itself before you have diagnosed it.

1. Boot into Safe Mode via WinRE, then Troubleshoot, then Advanced options, then Startup Settings.
2. Open Settings, then Windows Update, then Update history, then Uninstall updates, and remove the latest update.
3. Restart normally and pause updates for a week while you investigate.

### Fix 5: Fix 5: Disconnect peripherals before updating

USB devices are a leading cause of shutdown hangs. Updating with a bare laptop removes the entire category. USB-C docks with power delivery are the worst offenders; their drivers span power, display, and USB subsystems, any of which can hang a shutdown.

1. Unplug all USB devices, docks, SD cards, and external displays.
2. Run the update with only the charger connected.
3. Reconnect peripherals after the update completes and the system is stable.

### Fix 6: Fix 6: Disable Fast Startup

Fast Startup's hybrid shutdown is a known conflict with update restarts. Disabling it makes every shutdown and restart a clean one. Disabling Fast Startup also makes the Shift+Shutdown full-shutdown shortcut unnecessary, since every shutdown becomes a full one.

1. Open Control Panel, then Power Options, then Choose what the power buttons do.
2. Click Change settings that are currently unavailable and uncheck Turn on fast startup.
3. Save changes and retry the update cycle.

### Fix 7: Fix 7: Update chipset and storage drivers

The drivers most likely to hang during shutdown are the chipset and storage drivers. Current versions from the manufacturer unload cleanly. Storage drivers deserve priority in the update order; the storahci and Intel RST drivers are the ones managing the disk the restart is writing to.

1. Download the latest chipset and storage drivers from your manufacturer's support page.
2. Install them, restart, and run the next update.
3. If updates still hang at restart, the [undoing-changes recovery guide](/articles/best-way-to-fix-windows-update-undoing-changes-stuck/) covers the rollback scenario, and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the recovery options.

## Closing

A stuck Restarting screen is almost always a shutdown that cannot finish rather than an update that cannot install: wait patiently first, force-shutdown decisively when truly frozen, then remove the hanging driver or Fast Startup conflict so it does not recur. If the machine rolls back instead of hanging, our [undoing-changes stuck guide](/articles/best-way-to-fix-windows-update-undoing-changes-stuck/) is the next read, and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) covers the official recovery tools. If you are on Windows 11 24H2 specifically, note that its restart phase has its own wrinkles — our [24H2 restarting-screen guide](/articles/how-to-fix-windows-update-stuck-on-restarting-in-windows-11-24h2/) covers the checkpoint-servicing and driver-model quirks that can wedge this build.
