---
title: "Black Screen After a Windows Update? Here's How to Fix It"
slug: black-screen-after-windows-update-troubleshooting
date: 2026-10-09
categories: ["windows-errors"]
tags: ["black screen", "windows update", "display"]
description: "Windows updated and now your screen stays black? Work through these fixes to get your display back — from driver rollbacks to Startup Repair."
thumbnail: "/images/thumbs/black-screen-after-windows-update-troubleshooting.webp"
faqs:
  - q: "My screen is black but I can hear Windows sounds — what does that mean?"
    a: "Windows booted successfully; only the display output is wrong. It's almost certainly the graphics driver, a wrong display mode, or output routed to a nonexistent external monitor. The Win + Ctrl + Shift + B graphics reset and Win + P display cycling in Fix 1 are made for exactly this situation."
  - q: "How do I boot to Safe Mode if I can't see anything?"
    a: "Use the forced recovery method: hold the power button to force off during the Windows logo, twice in a row. The third boot opens the recovery environment, where you can reach Startup Settings blind — the menus are in fixed positions, or ask someone to read the screen if you have any display at all on an external monitor."
  - q: "Will System Restore delete my files?"
    a: "No. System Restore only reverses system files, drivers, updates, and settings to the restore point's state. Documents, photos, downloads, and other personal files are not affected — though programs installed after the restore point will need reinstalling."
  - q: "Should I turn off Windows Update to prevent this happening again?"
    a: "Don't turn it off entirely — you'd miss security patches. Instead, pause updates for a week or two after major releases, and consider blocking driver updates via Group Policy or the 'do not include drivers' setting so Windows Update can't replace your working graphics driver."
---

The update finished, the laptop restarted, and now... black. The power light is on, you might even hear the fans, but there's no login screen. Before you assume the worst, know this: a black screen after an update is usually a display driver problem, not a dead laptop.

The key question is whether Windows is actually running behind that black screen. Our [black screen reference](/articles/best-way-to-fix-black-screen-after-windows-update/) covers the variants; the steps below are ordered to answer that question first, then fix it. Start at Fix 1.

## Why this happens

- The update replaced your graphics driver with an incompatible version.

- Windows is booting to the wrong display output (common with external monitors or docks).

- The update changed the display refresh rate or resolution to something your panel can't show.

- Fast startup resuming from a corrupted hibernation state created during the update.

- A failed update leaving the boot process hanging before the login screen loads.

- BitLocker or Secure Boot prompts rendering on a display output you can't see.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Check whether Windows is actually running

A black screen with a running Windows needs a very different fix than a laptop that isn't booting. This quick test tells you which.

1. Press **Caps Lock** — if the keyboard light toggles, Windows is running behind the black screen.

2. Press **Win + Ctrl + Shift + B** to restart the graphics driver; the screen may flicker back to life.

3. Try **Win + P** then **Enter** to cycle display modes in case output went to a phantom monitor.

4. If the laptop is truly unresponsive (no lights, no sounds), skip to Fix 5.

### Fix 2: Boot into Safe Mode

Safe Mode uses a basic display driver. If your screen works there, the normal graphics driver is confirmed as the problem.

1. Force-power-off twice during boot to open the recovery environment.

2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.

3. Press **4** for Safe Mode.

4. If you get a picture in Safe Mode, continue with Fix 3. If not, jump to Fix 5.

### Fix 3: Roll back or reinstall the graphics driver

This is the fix for the majority of post-update black screens. The update's driver has to go.

1. In Safe Mode, open **Device Manager** and expand **Display adapters**.

2. Right-click your GPU, open **Properties > Driver**, and click **Roll Back Driver** if available.

3. Otherwise choose **Uninstall device**, tick **Attempt to remove the driver**, and restart.

4. Install the correct driver from the manufacturer — NVIDIA users should use the [official NVIDIA driver page](https://www.nvidia.com/Download/index.aspx), AMD users the [AMD driver download page](https://www.amd.com/en/support/download/drivers.html).

### Fix 4: Uninstall the update that caused it

If the black screen appeared immediately after a specific update and the driver looks fine, remove the update itself.

1. In Safe Mode, open **Settings > Windows Update > Update history**.

2. Click **Uninstall updates** and remove the most recent cumulative update.

3. Restart normally and confirm the display returns.

4. Then pause updates for two weeks via **Settings > Windows Update > Pause updates**.

### Fix 5: Run Startup Repair

When you can't reach Safe Mode either, the boot files themselves may be damaged. Startup Repair fixes them automatically.

1. From the recovery environment, choose **Troubleshoot > Advanced options > Startup Repair**.

2. Select your account and enter your password if prompted.

3. Let the tool run — it can take 10-20 minutes.

4. If it reports it couldn't repair, note the log path and continue to Fix 6. Our [Startup Repair guide](/articles/best-way-to-use-startup-repair-windows-11/) explains the failure cases.

### Fix 6: Disable fast startup from recovery

A corrupted fast-startup hibernation file can black-screen every boot. Disabling it forces a true cold boot.

1. In the recovery environment, go to **Troubleshoot > Advanced options > Command Prompt**.

2. Run `powercfg /h off` to disable hibernation (which also disables fast startup).

3. Type `exit` and choose **Continue** to boot Windows.

4. If the screen returns, leave hibernation off or re-enable it later with `powercfg /h on` after a week of stable boots.

### Fix 7: Use System Restore

When all else fails, rolling the whole system back to before the update is the reliable escape hatch.

1. In the recovery environment, choose **Troubleshoot > Advanced options > System Restore**.

2. Select a restore point from before the update.

3. Complete the wizard and let the laptop restart.

4. Your files are untouched. See our [full System Restore walkthrough](/articles/best-way-to-use-system-restore-on-windows-11/) for the details.

### Fix 8: Test with an external monitor

This two-minute test separates a Windows/driver problem from a dead laptop panel. If an external display works, your laptop is fine and the issue is the built-in screen or its driver path.

1. Connect a TV or monitor via **HDMI** or **DisplayPort**.

2. Power on the laptop and wait a minute for Windows to load.

3. Press **Win + P**, then tap the **Down arrow** once and press **Enter** — repeat a few times, waiting between presses, to cycle display modes.

4. If the external screen shows Windows, the laptop panel, its cable, or backlight is the problem.

5. Check the BIOS screen too: if setup screens show on the laptop panel but Windows doesn't, it's the Windows driver — return to Fix 3.

6. If nothing displays anywhere, continue with the recovery-environment fixes.

## Closing

A black screen after an update is scary but very rarely fatal — in most cases Windows is fine and it's just the display driver or a hung boot state. The Caps Lock test plus Win + Ctrl + Shift + B resolves a surprising number of cases in seconds, and the driver rollback handles most of the rest. Once you're back, consider disabling automatic driver updates through Windows Update so a bad graphics driver can't ambush you again. If the external monitor works but the laptop screen stays black even in the BIOS, that's a panel, cable, or backlight hardware issue — no Windows fix will reach it, and it's a repair-shop job. But if the BIOS shows fine and only Windows is black, the display itself is proven working and the software fixes above are the right track.
