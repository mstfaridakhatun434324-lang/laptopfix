---
title: "How to Fix Windows Update Stuck on ‘Restarting’ on an ASUS Laptop"
slug: how-to-fix-windows-update-stuck-on-restarting-on-asus-laptop
date: 2026-09-05
categories: ["windows-update"]
tags: ["windows update stuck on restarting", "asus laptop restarting loop", "restarting screen frozen", "fast startup fix"]
description: "ASUS laptop hanging on the Restarting screen during updates? Force a safe shutdown, disable Fast Startup, clear MyASUS holds, and fix the hanging driver."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-on-asus-laptop.webp"
faqs:
  - q: "Is it safe to force shutdown on the Restarting screen?"
    a: "Yes, at this specific screen. The Restarting phase is still shutdown — the update install has not begun — so you are interrupting a shutdown, not an install. Windows handles this gracefully and will resume or roll back. Do not force shutdown during an install-phase percentage screen, which is riskier."
  - q: "How long should I wait before forcing it?"
    a: "Sixty minutes with zero change is the threshold. Normal update restarts take 5 to 15 minutes (up to 30 on a hard drive). Past an hour with frozen dots and no drive activity, it is hung and will not resolve itself."
  - q: "Why does this only happen during updates?"
    a: "Because updates force the restart that exposes an existing shutdown problem. The hanging driver or service was there all along — you just never noticed because normal restarts may have been fast startups (which do not fully shut down) or you rarely restarted."
  - q: "Can a USB device really block a restart?"
    a: "Yes. If a device's driver refuses the shutdown request, Windows waits for it. Docks, external drives, and some USB audio devices are the usual suspects. The one-minute test — restart with everything unplugged — identifies this instantly. Windows waits rather than forcing the issue, so the hang can last indefinitely."
---

A Asus laptop that sits on the 'Restarting' screen with the spinning dots for an hour is stuck in the shutdown phase of an update — Windows is trying to stop services and drivers so it can reboot into the install phase, and something will not let go. The usual hangers-on: a driver that refuses to unload, a Asus background service stuck mid-task, or Fast Startup's hybrid state confusing the shutdown sequence. [the generic stuck-on-restarting fix](/articles/windows-11-stuck-on-restarting-screen-fix/)

The key question is how long to wait. A normal update restart takes 5 to 15 minutes; on a hard drive, up to 30. Past 60 minutes with no change, it is hung — and the longer you wait beyond that, the less likely it is to resolve itself. The fixes below start with the safe forced shutdown (which is safer than it sounds at this stage) and work toward the driver causes.

## Why this happens

- **Driver refusing to unload.** Network, storage, or audio drivers hanging the shutdown sequence. Update network, storage, and audio drivers from Asus support first.
- **MyASUS background service stuck.** Asus's service holding a shutdown-blocking handle. End Asus background processes in Task Manager before updating.
- **Fast Startup hybrid state.** The hibernation-based shutdown confusing the restart. powercfg /h off disables hybrid shutdown as an alternative test.
- **Windows Update service mid-transaction.** The update engine itself wedged during shutdown. The troubleshooter resets the wedged update transaction.
- **External device blocking shutdown.** A USB device whose driver will not release. Docks and external drives are the most common device blockers.
- **Corrupted shutdown transaction.** Damaged servicing state that cannot complete the handoff. Partial servicing transactions also block clean shutdowns.
- **Third-party antivirus hook.** Security software intercepting shutdown calls. Pause protection rather than uninstalling when testing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait a reasonable time, then force shutdown

Confirm the hang, then do the safe forced shutdown — at the Restarting screen the install has not begun. The Restarting screen is the shutdown phase, not the install phase — Windows is waiting for services and drivers to stop, which is why a forced shutdown here is safer than during a percentage screen.

1. Wait a full 60 minutes from when the dots froze (30 on an SSD is generous).
2. Check for drive activity — blinking LED or sounds mean it is still working.
3. If truly frozen, hold the power button for 10 seconds until it powers off.
4. Wait 30 seconds, then power on normally.
5. Windows will usually resume the update or roll back cleanly.
6. Test a normal restart (not update-related) to confirm shutdown works again.

### Fix 2: Boot and check what happened

See whether the update completed, rolled back, or is pending. Sixty minutes with frozen dots and no drive activity is the threshold; normal update restarts take 5-15 minutes, up to 30 on a hard drive.

1. After the forced shutdown, let Windows boot normally.
2. Open Settings > Windows Update > Update history.
3. If the update shows as failed, note the error code.
4. If it shows as successful, the restart was the only problem.
5. If it is pending again, do not retry yet — continue with the fixes.
6. Check Settings > Windows Update > Update history to see whether the update completed or rolled back.

### Fix 3: Disconnect peripherals

Remove the device-driver suspects in one move. Drivers that refuse the shutdown request are the classic cause — network, storage, and audio drivers top the list on Asus laptops.

1. Unplug all USB devices, docks, and external drives.
2. Remove SD cards.
3. Retry the update restart with only the charger connected. [the undoing-changes loop](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update/)
4. If restarts now work, reconnect devices one at a time to find the culprit.
5. Update that device's driver before the next update cycle.
6. If it rolled back, note the error code before retrying anything.

### Fix 4: Disable Fast Startup

The hybrid shutdown is a classic cause of restart hangs. MyASUS background services sometimes hold shutdown-blocking handles, especially if MyASUS was mid-driver-install when the restart began.

1. Open Control Panel > Power Options > 'Choose what the power buttons do'.
2. Click 'Change settings that are currently unavailable'.
3. Uncheck 'Turn on fast startup'.
4. Save and test with a normal restart.
5. Leave it off — it causes more problems than the seconds it saves.
6. Reconnect peripherals one at a time, restarting between each, to identify the blocking device.

### Fix 5: Check MyASUS for stuck operations

Clear any Asus service holding the shutdown. Fast Startup's hybrid shutdown is implicated in a large share of restart hangs; disabling it is both a fix and a diagnostic step.

1. Open MyASUS and look for in-progress driver or BIOS operations.
2. Let them finish or cancel stuck ones.
3. In Task Manager, end Asus-branded background processes before the next update restart.
4. Consider setting MyASUS updates to manual during update cycles.
5. Restart normally to confirm shutdown works.
6. Confirm Fast Startup stays off across reboots — some updates re-enable it.

### Fix 6: Update drivers from Asus support

Replace the drivers most likely to hang shutdown. USB devices whose drivers will not release can block shutdown indefinitely — the unplug-everything test identifies this in one reboot.

1. Go to [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) and download the latest chipset, storage, and network drivers.
2. Install them with the charger connected.
3. Restart after each major driver.
4. Also update the BIOS if a newer version is available.
5. Current drivers unload cleanly; old ones are the hangers-on.
6. Verify MyASUS shows no stuck operations before the next update attempt.

### Fix 7: Run the shutdown troubleshooter path

Use the update troubleshooter to clear the wedged update state. The update engine itself can wedge mid-transaction during shutdown; the update troubleshooter clears that specific state.

1. Go to Settings > System > Troubleshoot > Other troubleshooters.
2. Run the Windows Update troubleshooter.
3. Apply all fixes and restart.
4. Then retry the update from a clean boot state.
5. This clears the half-transacted update that may be re-hanging shutdown.
6. Run the update again from the clean state and time the restart phase.

## Closing

The Restarting screen is the shutdown phase, not the install phase — which is why the forced shutdown is safe here and why drivers that will not unload are the usual cause. Disable Fast Startup, clear the Asus service holds, and updates restart cleanly again. For updates that hang at other stages, [an update stuck on restarting on other brands](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-lenovo-laptop/) covers those.
