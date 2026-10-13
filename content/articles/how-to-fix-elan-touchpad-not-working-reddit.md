---
title: "ELAN Touchpad Not Working? Fixes That Actually Solve It"
slug: "how-to-fix-elan-touchpad-not-working-reddit"
date: "2026-09-15"
categories: ["drivers"]
tags: ["elan touchpad", "touchpad not working", "elan driver", "windows 11"]
description: "ELAN touchpad dead after a Windows update? These fixes — from unhiding the device to reinstalling the ELAN driver — get your touchpad working again."
thumbnail: "/images/thumbs/how-to-fix-elan-touchpad-not-working-reddit.webp"
faqs:
  - q: "Why did my ELAN touchpad stop working after a Windows update?"
    a: "Windows feature updates frequently replace the vendor's ELAN driver with a generic PS/2 mouse driver that cannot operate the touchpad properly. Uninstalling the current driver and installing the ELAN package from your laptop manufacturer's support site restores full functionality for good."
  - q: "What is the ETDService and does my touchpad need it?"
    a: "ETDService is the ELAN background service that handles the touchpad's advanced features and communication with Windows. If it is disabled or missing, the touchpad may be detected but unresponsive. Set it to Automatic in services.msc, or reinstall the ELAN driver if the service is absent."
  - q: "How do I know if my touchpad is ELAN or Synaptics?"
    a: "Open Device Manager and expand Mice and other pointing devices or Human Interface Devices — the entry will say ELAN or Synaptics. You can also check the driver provider on the device's Driver tab. The fix paths differ, so identifying the hardware first saves time."
  - q: "Can a Windows update disable my touchpad in the BIOS?"
    a: "A Windows update cannot change BIOS settings directly, but BIOS updates delivered through Windows Update sometimes reset settings to defaults — which can disable the internal pointing device. If the touchpad vanished after a firmware update, check the BIOS touchpad option first."
---

ELAN touchpads ship on Acer, Asus, Lenovo, MSI, and many HP laptops. When one stops working, the pattern is consistent — it almost always follows a Windows feature update that replaces the ELAN driver with a generic one, or an ELAN driver update that fails halfway.

Telltale signs: the touchpad is missing from the Touchpad settings page, Device Manager shows an ELAN device with a yellow warning, or the ELAN tab vanished from Mouse properties. If the cursor moves but gestures fail, check the Touchpad settings page first — that is a simpler settings issue.

These fixes run quickest-first and reflect what works in repair shops. For Synaptics hardware, see our [Synaptics touchpad fix guide](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/).

## Why this happens

- ****Windows Update replaced the ELAN driver**:** Feature updates routinely swap the vendor ELAN driver for a generic PS/2 mouse driver. Basic movement may survive, but the touchpad device itself stops being recognized.
- ****Corrupted ELAN driver installation**:** A failed ELAN driver update leaves a partially installed driver, and the device shows a Code 10 or Code 43 error.
- ****Touchpad disabled in BIOS or by function key**:** Many laptops have a BIOS toggle for the internal pointing device, plus an Fn-key combination (often Fn+F7 or Fn+F9) that disables the touchpad. Either can be triggered accidentally.
- ****Conflicting precision touchpad settings**:** Windows 11 prefers Precision touchpad drivers. If the system tries to force Precision mode on ELAN hardware without the right driver, the touchpad goes dead.
- ****ELAN service not running**:** The ELAN service (ETDService) handles advanced touchpad features. If it is disabled, the touchpad may work minimally or not at all.
- ****Fast Startup driver staleness**:** Fast Startup hibernates driver state between boots. A stale ELAN driver state can survive normal restarts indefinitely until a full shutdown clears it.
- ****Physical ribbon cable issue**:** The touchpad connects via a small ribbon cable that can work loose, especially after a drop or a bottom-panel removal. No software fix helps if the cable is disconnected.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the Touchpad Toggle and Settings First

Press the touchpad toggle function key (commonly Fn+F7 or Fn+F9) and watch for an on-screen indicator. Then confirm the touchpad switch is on in Settings, Bluetooth and devices, Touchpad. Accidental Fn-key presses account for a real share of 'dead touchpad' reports.

While in the Touchpad settings, verify the touchpad is not set to turn off when a mouse is connected if you are testing without one. Rule out the simple causes before touching drivers.

1. 1. Press the Fn touchpad toggle key and look for an indicator.
2. 2. Open Settings, Bluetooth and devices, Touchpad.
3. 3. Make sure the main Touchpad switch is turned on.
4. 4. Uncheck 'Leave touchpad on when a mouse is connected' temporarily as a test.
5. 5. Test the touchpad before moving to driver fixes.

### Fix 2: Enable the ELAN Device in BIOS

Enter the BIOS/UEFI setup and look under Advanced or Devices for 'Internal Pointing Device,' 'Touchpad,' or 'ELAN' — make sure it is enabled, then save and exit. A BIOS update can silently disable this, and no Windows fix overrides it.

If the option is already enabled, try toggling it off, saving, rebooting, then toggling it back on — this forces the firmware to re-enumerate the device.

1. 1. Restart and enter BIOS/UEFI setup.
2. 2. Find the internal pointing device or touchpad option.
3. 3. Set it to Enabled, save, and exit.
4. 4. If already enabled, toggle it off and on across two reboots.
5. 5. Check whether Windows now detects the touchpad.

### Fix 3: Reinstall the ELAN Driver From Your Laptop Maker

In Device Manager, expand Mice and other pointing devices (or Human Interface Devices), right-click the ELAN entry, and choose Uninstall device with driver deletion ticked. Restart, then install the ELAN driver package from your laptop maker's support site for your exact model.

Do not rely on Windows Update for this driver — it caused the problem. The vendor package includes the ELAN control panel and filter driver as a matched set; find it under Mouse/Touchpad drivers, such as on [Lenovo's support site](https://support.lenovo.com/us/en/).

1. 1. In Device Manager, uninstall the ELAN device including its driver.
2. 2. Restart the laptop.
3. 3. Download the ELAN/touchpad driver for your exact model from the maker.
4. 4. Install the package and restart again.
5. 5. Verify the touchpad appears in Settings under Touchpad.

### Fix 4: Start the ELAN Service

In services.msc, find ETDService or ELAN Service, set its startup type to Automatic, and start it. Without this background service, the touchpad may be detected but unresponsive.

If the service is missing entirely, the ELAN driver package did not install correctly — return to Fix 3 and reinstall, making sure to run the installer as administrator.

1. 1. Press Windows key + R, type services.msc, and press Enter.
2. 2. Locate ETDService or ELAN Service in the list.
3. 3. Set its startup type to Automatic.
4. 4. Click Start to run the service now.
5. 5. Test the touchpad immediately.

### Fix 5: Do a Full Shutdown to Clear Fast Startup State

Fast Startup saves driver state to disk, so a corrupted ELAN driver state can survive every normal restart. Hold Shift while clicking Shut down for a full shutdown, wait ten seconds, then power on.

For a permanent change, disable Fast Startup in Power Options under 'Choose what the power buttons do.' The slightly longer boot time is a fair trade for eliminating an entire category of driver glitches.

1. 1. Hold Shift and click Shut down for a full shutdown.
2. 2. Wait ten seconds, then power the laptop on.
3. 3. Test the touchpad.
4. 4. Optionally disable Fast Startup in Power Options.
5. 5. If the touchpad works now, stale driver state was the cause.

### Fix 6: Roll Back a Bad Driver Update

In Device Manager, open the ELAN device's properties and check the Driver tab. If 'Roll Back Driver' is clickable, use it to restore the previously working version, then restart.

Use this when the touchpad died right after a driver update. Then block the bad version with the 'Show or hide updates' troubleshooter so Windows does not re-apply it.

1. 1. In Device Manager, open the ELAN device properties.
2. 2. Go to the Driver tab and click Roll Back Driver.
3. 3. Choose a reason and confirm, then restart.
4. 4. Test the touchpad thoroughly.
5. 5. Block the bad driver version from reinstalling via Windows Update.

### Fix 7: Check the Ribbon Cable

If Device Manager shows no ELAN device at all — not even with hidden devices shown — and the BIOS toggle did nothing, the touchpad's ribbon cable may be loose. It is a thin flat ribbon near the front edge, secured by a flip-lock connector.

Reseat it carefully: flip the lock open, slide the ribbon fully in, and close the lock — or have a repair shop do it in minutes. Related input issues are covered in our [touchscreen fix guide](/articles/how-to-fix-touchscreen-not-working-on-laptop-in-windows-11-24h2/).

1. 1. Power off completely and remove the bottom panel.
2. 2. Locate the touchpad ribbon cable near the front edge.
3. 3. Open the connector lock, reseat the ribbon fully, and close the lock.
4. 4. Reassemble and boot.
5. 5. Check Device Manager for the ELAN device.

## Closing

ELAN touchpad failures look dramatic but resolve to a short list: the Fn toggle, the BIOS setting, or a driver that Windows Update mangled. Reinstall the vendor's ELAN package as a matched set rather than letting Windows pick the driver, and the touchpad almost always comes back to life.
