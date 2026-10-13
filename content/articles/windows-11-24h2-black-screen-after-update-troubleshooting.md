---
title: "Windows 11 24H2 Black Screen After Update: Troubleshooting Guide"
slug: windows-11-24h2-black-screen-after-update-troubleshooting
date: 2026-09-02
categories: ["windows-update"]
tags: ["24h2 black screen", "black screen after update", "windows 11", "display driver"]
description: "Black screen after the Windows 11 24H2 update? Diagnose whether Windows is running behind it, then fix the display driver or roll back the update."
thumbnail: "/images/thumbs/windows-11-24h2-black-screen-after-update-troubleshooting.webp"
faqs:
  - q: "How do I know if my laptop is on when the screen is black?"
    a: "Press Caps Lock and watch for its indicator light, listen for fan noise, and check the power LED. If Caps Lock toggles, Windows is running and only the display output is broken — a much easier fix. If nothing responds at all, the system may be hung during boot, which points to a deeper update or driver problem."
  - q: "Can a black screen after an update fix itself?"
    a: "Sometimes, if you give it time. The 24H2 update can sit on a black screen for 30 to 60 minutes while it migrates drivers in the background, especially on slower drives. Wait at least an hour with the charger connected before forcing anything off — interrupting a working update is worse than the black screen."
  - q: "Will I lose my files if I roll back the 24H2 update?"
    a: "No. Rolling back a feature update restores the previous Windows build but keeps your personal files, installed programs, and most settings intact. It is designed as a safe undo. The only things you lose are the changes the update itself made, which is exactly what you want when the update broke your display."
  - q: "Why does 24H2 cause black screens on some laptops?"
    a: "Feature updates replace the entire display driver stack, and 24H2's driver migration is aggressive about swapping in newer drivers. On laptops with hybrid graphics, custom OEM display drivers, or unusual panel configurations, the migrated driver can fail to initialize the screen while Windows itself boots fine behind it."
---

You ran the Windows 11 24H2 update, the laptop restarted, and now the screen is black. No logo, no login, maybe a lonely cursor blinking in the corner. This is one of the scarier update failures because it looks like a dead machine — but in most cases Windows is alive behind that black screen and only the display pipeline broke. The 24H2 feature update is particularly prone to this because it aggressively migrates display drivers during installation.

Your first job is diagnosis: is Windows running, or is the machine hung? The Caps Lock test answers that in five seconds. Everything after that follows from the answer — display driver fixes if Windows is alive, boot repair if it is not. Work through the steps below before you assume the hardware died; it almost certainly did not.

A word about what not to do: do not start reinstalling Windows, do not flash the BIOS, and do not assume the GPU died. Post-update black screens are software problems with software fixes, and the drastic measures people reach for in a panic cause far more damage than the black screen itself. The display pipeline has exactly three layers — the panel, the driver, and Windows' output routing — and the fixes below test them in that order, cheapest first.

## Why this happens

- **Faulty migrated display driver.** 24H2 swapped in a graphics driver that cannot initialize your specific panel or GPU combination.
- **Hybrid graphics handoff failure.** On laptops with integrated plus discrete GPUs, the update can break the switching logic the display depends on.
- **External display confusion.** The update set a disconnected monitor or dock output as the primary display.
- **Half-finished driver migration.** The update stalled mid-migration, leaving the display stack in a broken intermediate state.
- **Fast Startup state mismatch.** The saved hybrid-shutdown state no longer matches the updated system, confusing the boot display.
- **Changed refresh rate or resolution** that the panel cannot show, set silently during the update.
- **Corrupted boot files** in the rare case where the machine is genuinely not booting.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Windows is alive and wake the display

1. Press **Caps Lock** — if the indicator light toggles, Windows is running and this is a display-output problem. Continue with the fixes below.
2. Press **Windows key + Ctrl + Shift + B**. You should hear a beep as the graphics driver restarts.
3. Press **Windows key + P**, then **Down arrow**, then **Enter** to cycle projection modes — this recovers output sent to a phantom external display.
4. Disconnect all external monitors, docks, and adapters, then press a key. If the laptop panel wakes up, the update had misrouted your display. Related: [undoing-changes boot loops](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-in-windows-11-24h2/).

### Fix 2: Wait it out if the update may still be working

1. If the black screen appeared during the update's restart phase, give it at least 60 minutes with the charger connected.
2. Watch and listen for disk activity — blinking drive light or fan changes mean migration is still running.
3. Do not force a shutdown during this window; interrupting driver migration is what turns a slow update into a broken one.
4. If there is zero activity for over an hour, move on — the update is genuinely stuck.

### Fix 3: Force a restart into the recovery environment

1. Hold the **power button** for ten seconds to force the laptop off. Wait thirty seconds.
2. Power on, and as soon as the manufacturer's logo appears, force it off again. Repeat twice more.
3. On the third boot, Windows should enter the recovery environment automatically.
4. Go to **Troubleshoot** > **Advanced options**. From here you can access Safe Mode, System Restore, and update rollback.

### Fix 4: Boot into Safe Mode to confirm the driver theory

1. In recovery, go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **4** for Safe Mode.
2. Safe Mode uses a basic display driver. If your desktop appears, the normal display driver is confirmed as the culprit.
3. If Safe Mode is also black, skip to Fix 6 (System Restore) — the problem is deeper than the display driver — see also [fixing updates stuck on the restarting screen](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/).
4. While in Safe Mode, continue to the next fix to replace the driver.

### Fix 5: Roll back or reinstall the display driver

1. In Safe Mode, open **Device Manager** and expand **Display adapters**.
2. Right-click your GPU, choose **Properties** > **Driver** tab, and click **Roll Back Driver** if available — this undoes exactly what 24H2 did.
3. If rollback is unavailable, choose **Uninstall device**, check **Attempt to remove the driver for this device**, and restart normally.
4. Then install a known-good driver: use your laptop maker's support site, or the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx) for your GPU.

### Fix 6: Use System Restore to undo the update

1. In the recovery environment, go to **Troubleshoot** > **Advanced options** > **System Restore**.
2. Pick a restore point dated before the 24H2 update and follow the prompts.
3. System Restore reverts system files and drivers but leaves your personal files alone.
4. After the restore completes and the desktop returns, pause Windows updates for a week before retrying 24H2, and update your display driver first.

### Fix 7: Uninstall the 24H2 update from recovery

1. In recovery, go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Choose **Uninstall latest feature update** and confirm.
3. This rolls the system back to the previous Windows build — your files stay intact.
4. Once back in Windows, check the [official Windows Update support page](https://support.microsoft.com/en-us/windows) for known 24H2 issues with your hardware before attempting the update again.

### Fix 8: Rebuild the boot configuration data

If the machine is genuinely not booting (no Caps Lock response, no disk activity), the update may have damaged the boot files rather than the display driver.

1. Boot into the recovery environment (force off at the logo twice, as in Fix 3).
2. Go to **Troubleshoot** > **Advanced options** > **Command Prompt**.
3. Run these commands in order:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /rebuildbcd`
4. Type `exit`, choose **Continue** to restart, and watch for the login screen. If the BCD was the problem, Windows boots normally now.

## Closing

A black screen after 24H2 is almost never a dead laptop — it is a display driver or migration problem with Windows running blind behind it. Diagnose with the Caps Lock test, restart the graphics driver, confirm in Safe Mode, then roll back the driver or the update itself. Your files are safe through all of it. If the boot rebuild and every earlier fix leave you with a black screen on a demonstrably dead machine — no lights, no sounds, no Caps Lock — then and only then consider hardware service. But that outcome is rare: the overwhelming majority of 24H2 black screens end at Fix 1, Fix 5, or Fix 7, with everything intact.
