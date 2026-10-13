---
title: "What to Do If You Get a Black Screen After a Windows Update"
slug: what-to-do-if-black-screen-after-windows-update
date: 2026-09-14
categories: ["windows-errors"]
tags: ["black screen", "windows update", "display driver", "troubleshooting"]
description: "Black screen after a Windows update? Don't panic — work through these 8 steps from quick checks to driver rollbacks and update uninstalls."
thumbnail: "/images/thumbs/what-to-do-if-black-screen-after-windows-update.webp"
faqs:
  - q: "My screen is black after updating Windows. Is my laptop broken?"
    a: "Almost certainly not. A black screen after an update is usually a display driver problem or a stuck update process, not hardware failure. The machine is typically running fine behind the black screen — it just is not showing you anything."
  - q: "How long should I wait on a black screen after an update?"
    a: "Give it at least 30–60 minutes on the first boot after a major update, especially on slower drives. Windows sometimes sits at a black screen while finishing driver migrations in the background. Only start troubleshooting after a full hour of no change."
  - q: "Can I hear sound but see nothing?"
    a: "That is actually good news — it means Windows booted successfully and only the display pipeline is broken. The graphics driver reset shortcut (Win + Ctrl + Shift + B) often fixes this instantly."
  - q: "Will I lose my files fixing a black screen?"
    a: "No. Every fix in this guide — driver rollbacks, update uninstalls, even Startup Repair — preserves your files. A black screen is a display problem, and your data is sitting safely on the drive behind it."
---

You installed a Windows update, the laptop restarted, and now... blackness. Maybe a cursor blinks at you; maybe there is not even that. Before you panic: this is one of the most common post-update problems in Windows, and it is a *display* problem far more often than a *Windows* problem. Your files are fine. The operating system usually booted just fine. It simply is not drawing anything on the screen.

The trick is figuring out which layer broke: the graphics driver, the update itself, or the boot process. This guide goes from the 10-second fixes to the deeper repairs in order. If your screen is black *during* normal use rather than after an update, the driver steps still apply — but the update-specific steps are what make this guide different from a general display troubleshooting article. For the related scenario where Windows will not boot at all, see our guide to the [SrtTrail.txt blue screen error](/articles/srttrail-txt-blue-screen-error-bsod-windows-11/).

## Why this happens

- **New graphics driver conflicts with the old one.** Windows Update sometimes installs a display driver that fights with the manufacturer's version already on the system.
- **Update stuck mid-installation.** The screen goes black while Windows finishes configuring in the background — and sometimes it genuinely gets stuck there.
- **Corrupted display driver.** A partially applied driver update leaves the graphics stack in a broken state.
- **Fast Startup + new kernel.** The hibernated kernel session from before the update does not match the new system files.
- **External display confusion.** The update can reset display settings, sending the image to a phantom second monitor.
- **BitLocker or credential prompt hidden.** Occasionally the black screen is actually a BitLocker recovery or login prompt that is not rendering — the system is waiting for input you cannot see.

## How to fix it

Work through these in order. Do not skip the early ones just because they sound too simple.

### Fix 1: Wait, then wake the display properly

1. Wait a full **30–60 minutes** if this is the first boot after a feature update. Seriously — go make tea.
2. Press **Win + Ctrl + Shift + B**. You will hear a beep as the graphics driver restarts. This alone fixes a huge number of post-update black screens.
3. Try **Win + P**, then press the **Down arrow** and **Enter** — this cycles display modes and can pull the image back from a phantom external monitor.
4. If you have an external monitor or TV plugged in, unplug it and press **Win + Ctrl + Shift + B** again.

### Fix 2: Force a proper shutdown and cold boot

1. Hold the power button for 10 seconds until the laptop fully powers off.
2. Unplug the charger and all USB devices, external monitors, and docks.
3. Wait 30 seconds, plug in only the charger, and power on.
4. This clears Fast Startup's hibernated state, which is a common cause of the black screen persisting across restarts.

### Fix 3: Boot into Safe Mode

If the normal boot stays black, Safe Mode loads a basic display driver that almost always works.

1. Force-interrupt the boot **three times** (hold power during the Windows logo) to reach **Automatic Repair**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode (or **5** for Safe Mode with Networking).
3. If Safe Mode displays fine, the problem is your graphics driver or a startup program — continue to Fix 4.
4. If Safe Mode is *also* black, skip to Fix 6 — the problem is deeper than the display driver.

### Fix 4: Roll back or reinstall the graphics driver

1. In Safe Mode, press **Win + X** and open **Device Manager**.
2. Expand **Display adapters**, right-click your GPU, and choose **Properties > Driver**.
3. If **Roll Back Driver** is available, click it — this restores the pre-update driver.
4. If rollback is not available, choose **Uninstall device** (check **Attempt to remove the driver**), restart, and let Windows install its basic driver. Then install the proper driver: NVIDIA from [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx), AMD from AMD's driver download page, Intel from [Intel's driver tool](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 5: Uninstall the problematic update

1. In Safe Mode, go to **Settings > Windows Update > Update history > Uninstall updates**.
2. Remove the most recent update (note its KB number) and restart normally.
3. If the screen works now, pause updates for a couple of weeks: **Settings > Windows Update > Pause updates**. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) usually documents known bad updates within days.
4. You can also hide the specific bad update so it does not reinstall immediately.

### Fix 6: Run Startup Repair and system file checks

1. From **Automatic Repair**, go to **Troubleshoot > Advanced options > Startup Repair** and let it run.
2. If that does not help, open **Command Prompt** from Advanced options and run:
   - `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`
   - `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`
3. Type `exit`, choose **Continue** to reboot, and test.

### Fix 7: Check for a hidden BitLocker prompt

1. On the black screen, try typing your BitLocker recovery key followed by Enter — if the system was waiting at a recovery prompt, this unlocks it.
2. If that is not it, boot into the BIOS and check whether the boot order changed — some updates flip the boot device, and the "black screen" is the laptop trying to boot from an empty USB stick. Remove all USB drives and re-check.

### Fix 8: System Restore to before the update

1. From **Troubleshoot > Advanced options**, choose **System Restore**.
2. Pick a restore point dated before the update and follow the prompts.
3. System Restore does not touch your personal files — it only rolls back system files, drivers, and registry settings.
4. After restoring, pause updates and install them one at a time to identify the culprit.

## Closing

A black screen after a Windows update is frightening but overwhelmingly fixable — and your data was never at risk. The graphics driver restart shortcut and a proper cold boot resolve the quick cases; Safe Mode plus a driver rollback or update uninstall handles the stubborn ones. For the variant where the screen stays black on every boot rather than just after updates, see our [Windows 11 black screen after update guide](/articles/windows-11-black-screen-after-update-fix/). And next time a major update lands, give that first reboot a full hour before you decide anything is wrong — Windows does a lot of invisible work behind a black screen.
