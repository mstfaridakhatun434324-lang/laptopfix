---
title: "The Best Way to Fix a Black Screen After a Windows Update"
slug: best-way-to-fix-black-screen-after-windows-update
date: 2026-09-29
categories: ["windows-errors"]
tags: ["black screen", "windows update", "windows 11"]
description: "Black screen after a Windows update? Here's the best order to fix it: from quick display checks to rolling back the bad update."
thumbnail: "/images/thumbs/best-way-to-fix-black-screen-after-windows-update.webp"
faqs:
  - q: "Why is my screen black after a Windows update?"
    a: "The update likely installed a faulty display driver, left the update half-finished, or changed a display setting your hardware does not like. The system is usually running fine behind the black screen, which is why the fixes focus on the display pipeline and the update itself."
  - q: "How do I know if the laptop is actually on?"
    a: "Listen for fans, check for keyboard backlight or power LEDs, and try Caps Lock. If the Caps Lock light toggles, Windows is running and only the display output is broken, which is a much easier problem."
  - q: "Should I force shut down a black-screened laptop?"
    a: "If it has been black for more than thirty minutes with no disk activity, yes. Hold the power button for ten seconds. The risk of interrupting an update is real but small after that long, and you cannot fix the problem while it sits there."
  - q: "Will rolling back the update delete my files?"
    a: "No. Uninstalling a Windows update removes only the update's changes. Your files, programs, and settings stay exactly where they were."
---

You installed a Windows update, the laptop restarted, and now the screen is black. Maybe the cursor blinks in the corner, maybe there is nothing at all, but Windows clearly is not showing you a desktop. Before you panic, check whether the machine is actually alive: toggle Caps Lock and watch for the light, listen for the fans. If the laptop is running behind that black screen, the problem is almost certainly the display driver or the update itself, and both are fixable.

This guide gives you the best order of operations, ranked by speed and effectiveness. Start at the top and stop when your desktop returns. Most black screens after updates resolve within the first three fixes.

## Why this happens

- **Faulty display driver from the update.** Windows Update installed a graphics driver that does not work with your hardware.
- **Half-finished update.** The update stalled partway, leaving the display stack in a broken intermediate state.
- **Changed display settings.** The update altered the refresh rate, resolution, or display output in a way your screen cannot handle.
- **External display confusion.** The update switched the primary display to an external monitor or projector output that is not connected.
- **Corrupted system files.** Damage during the update breaks components the display pipeline needs.
- **Fast Startup conflict.** The hybrid shutdown state saved before the update no longer matches the updated system.
- **Failing update services.** The update components themselves are corrupted, blocking both the display fix and future updates.

## How to fix it

Work through these in order, starting with the quickest fixes first.

### Fix 1: Wake the display and check the basics

Rule out the trivial before anything else.

1. Press **Windows key + Ctrl + Shift + B**. This restarts the graphics driver with an audible beep. It is the single fastest fix for a black screen.
2. If nothing happens, press **Windows key + P**, then the **Down arrow**, then **Enter**. This cycles the projection mode and can restore output sent to a phantom external display.
3. Disconnect any external monitors, docks, and projectors, then restart.
4. Check the laptop's brightness keys. It sounds silly, but updates have been known to drop brightness to zero on some models.

### Fix 2: Force a restart and boot into Safe Mode

1. Hold the **power button** for ten seconds to force the laptop off. Wait thirty seconds.
2. Power on. If the screen stays black, force it off again during the Windows logo twice more to trigger the recovery environment.
3. In recovery, go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **4** for Safe Mode.
4. Safe Mode uses a basic display driver. If the desktop appears, the problem is the normal display driver, and the next fixes will resolve it.

### Fix 3: Roll back or reinstall the display driver

1. In Safe Mode, open **Device Manager** and expand **Display adapters**.
2. Right-click your GPU, choose **Properties** > **Driver**, and click **Roll Back Driver** if it is available. This undoes exactly what the update did.
3. If rollback is unavailable, choose **Uninstall device**, check **Attempt to remove the driver for this device**, and restart. Windows will load a basic driver that at least gives you a screen.
4. Then install a known-good driver from the manufacturer: [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx), [AMD drivers](https://www.amd.com/en/support/download/drivers.html), or the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 4: Uninstall the problematic Windows update

1. In Safe Mode, open **Settings** > **Windows Update** > **Update history** > **Uninstall updates**.
2. Remove the most recent update, the one that preceded the black screen.
3. Restart normally. If the desktop returns, pause updates for a week while Microsoft ships a corrected version: **Settings** > **Windows Update** > **Pause updates**.

### Fix 5: Disable Fast Startup

1. In Safe Mode, press **Windows key + R**, type `powercfg.cpl`, and press Enter.
2. Click **Choose what the power buttons do**, then **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and save.
4. Shut down fully, then power on. Fast Startup saves a system state that can be incompatible with the updated display stack.

### Fix 6: Run Startup Repair and system file checks

1. From the recovery environment, choose **Troubleshoot** > **Advanced options** > **Startup Repair** and let it run.
2. Then open **Command Prompt** from **Advanced options** and run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`, adjusting the drive letter if needed.
3. Follow with `DISM /Image:C:\ /Cleanup-Image /RestoreHealth` for deeper repair.
4. Restart and test.

### Fix 7: System Restore to before the update

1. In recovery, go to **Troubleshoot** > **Advanced options** > **System Restore**.
2. Choose a restore point from before the update installed.
3. Let it complete. System Restore reverts drivers and system files without touching your personal files, making it ideal for update-caused black screens.
4. Afterward, install the update again only when you are ready, or hide the problematic driver update.

### Fix 8: Reset Windows as a last resort

1. In recovery, choose **Troubleshoot** > **Reset this PC** > **Keep my files**.
2. This reinstalls Windows cleanly while preserving your data.
3. After the reset, install drivers from your laptop maker's support site before letting Windows Update touch the display driver.
4. Related display failures: [black screen after update on Windows 11](/articles/how-to-fix-black-screen-after-windows-update-on-windows-11/) and the general [black screen after update fix](/articles/windows-11-black-screen-after-update-fix/). Microsoft's recovery help is on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

### Fix 9: Block the bad driver from coming back

The most frustrating version of this problem is fixing the black screen, only for Windows Update to reinstall the same bad driver overnight.

1. Once your screen works, open **Settings** > **System** > **About** > **Advanced system settings**, go to the **Hardware** tab, and open **Device Installation Settings**.
2. Choose **No** so Windows Update stops replacing your working graphics driver with its own versions.
3. Install your graphics driver directly from the laptop maker or the GPU vendor, using their clean-install option.
4. As insurance, create a restore point right now: search **Create a restore point**, click **Create**, and name it "display working". If a future update black-screens you again, restoring takes ten minutes instead of an afternoon.

## Closing

A black screen after a Windows update is frightening because you cannot see what is happening, but the laptop is usually fine underneath. The graphics driver restart shortcut, Safe Mode, and the update rollback resolve the overwhelming majority of cases. Keep the habit of creating a restore point before major updates, and the next bad update becomes a ten-minute rollback instead of a black-screen emergency. Your future self will thank you.
