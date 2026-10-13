---
title: "How to Fix a Black Screen After a Windows Update"
slug: how-to-fix-black-screen-after-windows-update
date: 2026-09-10
categories: ["windows-errors"]
tags: ["black screen", "windows update", "display issue"]
description: "Stuck on a black screen after updating Windows? Work through these proven fixes — from display driver resets to update rollbacks."
thumbnail: "/images/thumbs/how-to-fix-black-screen-after-windows-update.webp"
faqs:
  - q: "Why is my screen black after a Windows update?"
    a: "Usually a display driver conflict: the update installed a new graphics driver that fails on your hardware, or the update process left the display stack in a broken state. Less often it is a stalled update, a corrupt user profile, or an external display routing problem."
  - q: "How long should I wait on a black screen before acting?"
    a: "After an update, give it 30 to 60 minutes — large updates do real work with no display output, especially on slower drives. If the drive activity light is flashing, it is still working. Only intervene when the drive goes quiet and the screen stays black."
  - q: "Will I lose my files fixing this?"
    a: "No. Every fix here — driver resets, Safe Mode repairs, update rollbacks, even System Restore — preserves your personal files. Only a clean install wipes data, and that is not on this list."
  - q: "What if the black screen has a cursor?"
    a: "A cursor means Windows is running but Explorer (the desktop shell) failed to start. That is actually good news — press Ctrl+Shift+Esc to open Task Manager, run a new task for explorer.exe, and you will often get your desktop back immediately."
---
Few things are as disheartening as restarting for a Windows update and getting... nothing. Just black. The machine sounds alive — fans spinning, lights on — but the screen stays dark. Before panic sets in: this is one of the most fixable post-update problems there is, and your files are almost certainly fine.

A black screen after an update is usually a display driver that the update broke, or Explorer failing to launch. The fixes below start with the 10-second trick that resolves a surprising number of cases and escalate from there.

## Why this happens

- **Broken display driver:** The update installed a graphics driver incompatible with your GPU or laptop, so nothing renders.
- **Stalled or incomplete update:** The update process hung mid-install, leaving the system in a half-updated state.
- **Explorer failing to start:** The desktop shell crashes on login, leaving a black screen (sometimes with a cursor).
- **External display routing:** The update reset display output to a port with nothing attached, or to a disconnected monitor.
- **Fast Startup conflicts:** The hybrid shutdown state conflicts with the newly updated drivers.
- **Corrupt user profile:** The update damaged your profile, so login completes into nothing.
- **Third-party software interference:** Antivirus or "tweaking" utilities blocking updated system components.

## How to fix it

Work through these in order. Try each fully before moving on.

### Fix 1: Wake the display driver (the 10-second fix)

Windows has a built-in keystroke that restarts the graphics driver without rebooting.

1. Press **Win + Ctrl + Shift + B** simultaneously. You should hear a beep and see the screen flicker as the driver restarts.
2. If the desktop appears, the driver had simply stalled. Update your graphics driver afterward (Fix 4) so it does not recur.
3. If nothing happens, press **Win + P**, then the **Down arrow**, then **Enter** — this cycles display modes and can reroute output stuck on a phantom external monitor.

### Fix 2: Check the physical display path

Rule out the embarrassingly simple causes first.

1. If you use an external monitor, check its cable and input selection, and try the laptop's own screen alone (unplug the external display).
2. On the laptop, press the brightness-up key (**Fn** + brightness key) several times — updates occasionally reset brightness to zero.
3. Try **Win + P** followed by **Enter** to force "PC screen only" mode.

### Fix 3: Restart Explorer from Task Manager

If you see a cursor on the black screen, Explorer likely failed to launch.

1. Press **Ctrl + Shift + Esc** to open Task Manager (it works even on a black screen).
2. Click **File > Run new task**, type `explorer.exe`, and press **Enter**.
3. If the desktop appears, the shell was the problem. To prevent recurrence, run `sfc /scannow` from an elevated prompt afterward. If Task Manager will not open, move to Safe Mode in the next fix.

### Fix 4: Boot into Safe Mode and fix the display driver

Safe Mode uses a basic display driver, bypassing the broken one.

1. Force the recovery environment: hold the power button to interrupt boot three times. Then **Troubleshoot > Advanced options > Startup Settings > Restart**, and press **4** for Safe Mode.
2. In Safe Mode, open **Device Manager** (**Win + X**), expand **Display adapters**, right-click your GPU, and choose **Uninstall device** with **Attempt to remove the driver** ticked.
3. Reboot normally — Windows will use a basic driver and you should see your desktop.
4. Install the correct driver from your manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) or directly from NVIDIA / AMD.

### Fix 5: Roll back the problematic update

If the black screen started immediately after a specific update, remove it.

1. In Safe Mode, go to **Settings > Windows Update > Update history > Uninstall updates**.
2. Uninstall the most recent quality or feature update, then reboot.
3. Pause updates for a week or two (**Settings > Windows Update > Pause updates**) to avoid immediate reinstallation while Microsoft or the manufacturer fixes the conflict. For update-specific black screen variants, see [how-to-fix-black-screen-after-windows-update-in-windows-11-24h2](/articles/how-to-fix-black-screen-after-windows-update-in-windows-11-24h2/).

### Fix 6: Use System Restore

If you cannot identify the update, roll the system state back.

1. From the recovery environment: **Troubleshoot > Advanced options > System Restore**.
2. Pick a restore point dated before the update.
3. Let it complete — this reverses system changes without touching your personal files.

### Fix 7: Disable Fast Startup and clean-boot

Fast Startup's hybrid hibernation state frequently conflicts with updated drivers.

1. In Safe Mode or normal mode, open **Control Panel > Power Options > Choose what the power buttons do > Change settings that are currently unavailable**, and uncheck **Turn on fast startup**.
2. Then do a clean boot: **Win + R** > `msconfig` > **Services** tab > **Hide all Microsoft services** > **Disable all**; in **Task Manager > Startup apps**, disable everything non-essential. Reboot and re-enable items in groups to find conflicts.

### Fix 8: Repair system files and the update components

For stubborn cases, repair the underlying OS and update machinery.

1. In Safe Mode with an elevated Command Prompt: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Reset Windows Update components: run `net stop wuauserv`, `net stop bits`, rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`, then `net start wuauserv` and `net start bits`.
3. Reboot and check for updates again — a clean update stack often succeeds where the broken one stalled.

## Closing

A black screen after a Windows update is frightening but rarely serious: it is a stalled display driver, a confused Explorer, or a bad update — all reversible. Start with the Win+Ctrl+Shift+B driver reset, work through Safe Mode driver repair and update rollback, and your desktop will be back without losing a file. If your machine instead gets stuck endlessly on the "Restarting" screen rather than going black, that is a different failure mode covered in our [stuck on restarting screen guide](/articles/windows-11-stuck-on-restarting-screen-fix/).
