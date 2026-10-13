---
title: "How to Fix a Black Screen After a Windows Update (Blue Screen Fix Guide)"
slug: black-screen-after-windows-update-blue-screen-error-fix
date: 2026-09-13
categories: ["windows-errors"]
tags: ["black screen", "windows-update", "bsod", "windows-11"]
description: "Black screen after a Windows update? Diagnose whether it's a display driver, boot failure, or bad update, and fix it step by step."
thumbnail: "/images/thumbs/black-screen-after-windows-update-blue-screen-error-fix.webp"
faqs:
  - q: "Why do I get a black screen after a Windows update?"
    a: "The update usually broke the display driver, changed the display output, or left the boot process hanging. A black screen with a cursor is different from a fully dead screen: the cursor means Windows loaded but the shell or driver failed, while no signal at all points to a driver or firmware problem."
  - q: "How do I know if it's a black screen or a failed boot?"
    a: "Listen and look. If you hear the startup sound, see the drive light working, or can move a mouse cursor, Windows booted and the problem is display-related. If nothing happens at all, not even backlight, the boot itself failed and you should work from the recovery environment instead."
  - q: "Can I fix a black screen without losing data?"
    a: "Yes. Display driver rollbacks, Safe Mode repairs, SFC scans, and update uninstalls do not touch personal files. Only a clean install deletes data, and that is the last resort. If you can reach the recovery environment, your files are almost certainly intact."
  - q: "What if the black screen happens on every boot now?"
    a: "Then the update installed a persistently broken driver or damaged the boot files. Boot into Safe Mode or the recovery environment, roll back the display driver or uninstall the update, and the normal boot should return. The fixes below cover both paths."
---

You install a Windows update, the laptop restarts, and instead of your desktop you get... nothing. A black screen. Maybe a lonely mouse cursor. Maybe not even that. Black screens after Windows updates are frightening because they give you so little information, but they are also very fixable once you determine which of the three usual causes you are dealing with: a broken display driver, a stalled boot, or a bad update.

This guide helps you diagnose first and fix second, in an order that gets most people back to a desktop within half an hour.

## Why this happens

- **The update installed an incompatible display driver.** The number one cause: a new GPU driver that does not work with your hardware or the new build.
- **The display output changed.** Updates can reset display settings, sending output to a nonexistent external monitor.
- **The boot process stalls.** A bad update can hang Windows before the login screen appears.
- **Corrupted system files.** A damaged update breaks components needed to render the desktop.
- **Fast startup conflicts.** The hybrid shutdown state can conflict with the updated drivers.
- **Third-party software interference.** Antivirus or disk tools can block updated components from loading.
- **BIOS/firmware mismatch.** Rare, but a major update can expose firmware incompatibilities.

## How to fix it

Work through these in order, testing for stability after each fix before moving on.

### Fix 1: Wake the display and check the obvious

Rule out the trivial before the technical.

1. Press **Windows key + Ctrl + Shift + B** to restart the graphics driver; you will hear a beep and the screen may flash.
2. If you have a cursor, press **Ctrl + Alt + Del** and see whether the security screen appears.
3. Disconnect all external monitors and docks, then restart.
4. Try **Win + P** and press **Enter** a few times to cycle display modes in case output went to a phantom monitor.
5. If any of this works, update the display driver properly in Fix 2.

### Fix 2: Boot into Safe Mode and roll back the display driver

Safe Mode uses a basic driver, bypassing the broken one.

1. Force recovery: hold the power button to shut down, power on, and interrupt boot three times until **Automatic Repair** appears.
2. Go to **Advanced options** then **Startup Settings** then **Restart**, and press **4** for Safe Mode.
3. Open **Device Manager** (**Win + X**), expand **Display adapters**, right-click your GPU, and choose **Properties**.
4. On the **Driver** tab, click **Roll Back Driver** if available.
5. If rollback is grayed out, choose **Uninstall device** (do not delete the driver), restart, and let Windows install its basic driver, then install the vendor driver fresh.

### Fix 3: Install the correct graphics driver

Replace the broken update driver with a known-good vendor version.

1. In Safe Mode with networking (or normal mode if the display works now), download the driver: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html).
2. Choose a clean installation to wipe the broken driver completely.
3. Restart normally and verify the desktop appears.
4. If the vendor driver also fails, use the driver from your laptop maker's support site, which is tested against your exact model.

### Fix 4: Uninstall the problematic update

If the black screen started with a specific update, remove it.

1. From Safe Mode or recovery, open **Settings** then **Windows Update** then **Update history** then **Uninstall updates**.
2. Remove the most recent update and restart.
3. If the desktop returns, pause updates for a couple of weeks from **Windows Update** then **Advanced options**.
4. Reinstall the update later after updating drivers first.

### Fix 5: Run startup repair and system file checks

Fix boot and file damage from the recovery environment.

1. Boot to **Advanced options** then **Troubleshoot** then **Advanced options**.
2. Run **Startup Repair** first and let it attempt an automatic fix.
3. If that fails, open **Command Prompt** and run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.
4. Follow with `DISM /Image:C:\ /Cleanup-Image /RestoreHealth` if SFC cannot repair everything.
5. Type `exit` and choose **Continue** to restart.

### Fix 6: Disable fast startup and clean-boot

Eliminate startup-state conflicts.

1. Once you can boot, open **Control Panel** then **Power Options** then **Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Press **Win + R**, type `msconfig`, and on the **Services** tab check **Hide all Microsoft services** and click **Disable all**.
4. Restart. If the black screen is gone, re-enable services in halves to find the conflicting program.
5. Uninstall or update whatever you find.

### Fix 7: Use System Restore

Roll the system back to before the update.

1. Boot to **Advanced options** and choose **System Restore**.
2. Pick a restore point dated before the update.
3. Let it complete and restart.
4. If no restore points exist, enable System Protection afterward for next time: search **Create a restore point** in **Start** and turn on protection for C:.

### Fix 8: Reset Windows as a final option

When the update damaged the installation beyond repair.

1. From recovery, choose **Troubleshoot** then **Reset this PC**.
2. Try **Keep my files** first.
3. If that fails, back up via the recovery command prompt or another PC, then choose **Remove everything**.
4. After reinstalling, get drivers from the vendor before letting Windows Update run wild.

For the looping variant of this problem, see our [SrtTrail.txt blue screen guide](/articles/how-to-fix-srttrail-txt-blue-screen-error-on-windows-11/), and for general post-update crashes, the [blue screen after Windows 11 update](/articles/how-to-fix-blue-screen-after-windows-11-update-on-lenovo-laptop/) walkthrough overlaps usefully.

## Closing

A black screen after a Windows update is Windows failing to show you the desktop, not Windows being destroyed. The display driver is guilty more often than not, and Safe Mode plus a clean vendor driver install resolves the majority of cases. Diagnose with the cursor test, fix with the driver rollback, and keep a restore point handy for the next update, because there will always be a next update.
