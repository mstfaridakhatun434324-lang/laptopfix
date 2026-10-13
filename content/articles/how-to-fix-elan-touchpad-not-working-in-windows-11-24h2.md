---
title: "ELAN Touchpad Not Working After the Windows 11 24H2 Update? Here's How to Fix It"
slug: how-to-fix-elan-touchpad-not-working-in-windows-11-24h2
date: 2026-09-01
categories: ["drivers"]
tags: ["elan touchpad", "windows 11 24h2", "touchpad driver", "device manager"]
description: "Your ELAN touchpad died after the Windows 11 24H2 update? This guide walks you through every proven fix, from driver rollback to a clean ELAN reinstall."
thumbnail: "/images/thumbs/how-to-fix-elan-touchpad-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why did my ELAN touchpad stop working after the 24H2 update?"
    a: "The 24H2 feature update often replaces the ELAN I2C driver with a generic Microsoft version that cannot talk to the touchpad hardware. Your touchpad vanishes from Device Manager or shows a yellow warning icon. Rolling back the driver or installing the manufacturer's ELAN package restores the correct driver and brings the touchpad back."
  - q: "How do I know if my touchpad is ELAN or Synaptics?"
    a: "Open Device Manager, expand Human Interface Devices, and look for entries like ELAN Input Device or ELAN I2C Filter Driver. If you see Synaptics instead, your laptop uses a different touchpad and the fixes here may not apply. Most Lenovo, ASUS, and Acer laptops in recent years shipped with ELAN touchpads."
  - q: "Will reinstalling the ELAN driver delete my settings?"
    a: "A basic driver reinstall preserves your Windows touchpad settings like tap sensitivity and scroll direction. Only a full ELAN utility reinstall — where you also remove the ELAN control panel software — resets custom gesture settings. Windows reapplies sensible defaults afterward, and you can reconfigure gestures in Settings."
  - q: "What if the touchpad is missing from Device Manager entirely?"
    a: "When the touchpad is completely absent, the driver is either uninstalled or disabled at a lower level. Click Action, then Scan for hardware changes, and check for unknown devices. If it still does not appear, check the BIOS — some laptops have a touchpad enable or disable toggle — and consider a full power drain to reset the embedded controller."
---

You close the lid, install the Windows 11 24H2 update, reopen it — and the cursor is gone. The ELAN touchpad that worked yesterday now does nothing: no movement, no taps, no scroll. The keyboard still works, USB mice still work, but the built-in touchpad is completely dead.

This is one of the most reported laptop issues after major Windows feature updates, and it is almost never a hardware failure. The 24H2 update routinely swaps the ELAN I2C driver for a generic Microsoft driver that cannot communicate with the touchpad, or it corrupts the existing driver mid-install. The fix is to get the correct driver back on the machine — and in nearly every case, the touchpad springs back to life. If your laptop actually uses a Synaptics touchpad instead, see our guide on [Synaptics touchpad problems on Windows 11](/articles/how-to-fix-synaptics-touchpad-not-working-on-windows-11/) — the steps differ.

## Why this happens

- **24H2 replaced the ELAN driver.** Windows Update installs a generic PS/2 or I2C driver over the vendor's ELAN package.
- **Corrupted driver from a mid-update crash.** An interrupted update can leave the ELAN driver half-installed.
- **ELAN I2C filter driver disabled.** The update disables the filter driver the touchpad needs to report gestures.
- **Touchpad disabled in Settings.** The update can flip the touchpad toggle off under Bluetooth & devices.
- **BIOS touchpad setting changed.** Some firmware updates bundled with 24H2 reset the internal pointing device to off.
- **Conflicting old ELAN utility.** Leftover ELAN control-panel software from the old Windows install blocks the new driver.
- **I2C bus error after sleep/wake.** The 24H2 power management changes can wedge the I2C bus the touchpad talks on.
- **Embedded controller wedged.** The EC that bridges the touchpad to the CPU is stuck in a bad state after the update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the touchpad toggle in Settings

Start with the simplest cause. Press **Windows + I**, go to **Bluetooth & devices > Touchpad**, and confirm the toggle is on. The 24H2 update has been known to flip this off during the migration. While you are here, make sure **Touchpad sensitivity** is not set to something extreme. If the toggle was off and turning it on brings the cursor back, you are done — no driver work needed. Also try the function-key shortcut: many laptops use **Fn + F5**, **Fn + F7**, or **Fn + F9** to toggle the touchpad, and 24H2 can change the default state of that key combination.

### Fix 2: Roll back the touchpad driver in Device Manager

If the toggle did not help, the driver is the likely culprit. Open **Device Manager** (right-click Start), expand **Human Interface Devices**, and look for **ELAN Input Device** or **ELAN I2C Filter Driver** — you may also find the touchpad under **Mice and other pointing devices**. Right-click it, choose **Properties**, open the **Driver** tab, and click **Roll Back Driver** if it is available. Select "a previous version of the driver seemed more reliable" and confirm. Restart the laptop. Rollback restores the pre-24H2 ELAN driver in about a minute and fixes most cases where the update pushed a bad driver. On Lenovo machines specifically, our [ELAN touchpad guide for Lenovo laptops](/articles/how-to-fix-elan-touchpad-not-working-on-lenovo-laptop/) covers model-specific driver quirks.

### Fix 3: Uninstall the ELAN device and scan for hardware changes

When rollback is greyed out, do a clean reinstall. In Device Manager, right-click the ELAN entry and choose **Uninstall device**. If you see a checkbox for **Attempt to remove the driver for this device**, check it — this deletes the broken 24H2 driver package from the driver store. Then click **Action > Scan for hardware changes** at the top of the window. Windows will redetect the touchpad and install a driver. Restart afterward. If Windows reinstalls the same broken generic driver, move on to Fix 4 for a vendor-specific package.

### Fix 4: Install the manufacturer's ELAN driver package

This is the most reliable long-term fix. Go to your laptop manufacturer's support site — [Lenovo support](https://support.lenovo.com/us/en/), [Dell support](https://www.dell.com/support), or [HP support](https://support.hp.com/us-en) depending on your brand — enter your exact model, and download the **touchpad / ELAN driver** listed for Windows 11. Run the installer, accept the defaults, and restart. Vendor packages include the correct ELAN I2C filter driver plus the gesture software, and they register with Windows Update so future updates do not overwrite them as aggressively.

### Fix 5: Remove the old ELAN utility software

Leftover ELAN control-panel apps from before the update can conflict with the new driver. Open **Settings > Apps > Installed apps**, search for **ELAN** or **ETD**, and uninstall anything ELAN-branded. Restart, then reinstall the vendor driver from Fix 4. This two-step — remove old software, install fresh package — clears the registry keys and startup services that commonly wedge after a feature update. After reinstalling, reconfigure your gestures under **Settings > Bluetooth & devices > Touchpad** since removing the utility resets custom settings to defaults.

### Fix 6: Check the BIOS touchpad setting

Some 24H2-era firmware updates reset the internal pointing device to disabled. Restart and press **F2**, **Del**, or your brand's BIOS key during boot. Look under **Advanced** or **Devices** for **Internal Pointing Device** or **Touchpad** and make sure it is **Enabled**, then save and exit. If the touchpad was disabled here, no Windows driver would ever see it — which is exactly why it also disappears from Device Manager. While in the BIOS, consider updating to the latest version from the manufacturer, since touchpad-related EC firmware fixes ship regularly.

### Fix 7: Drain residual power to reset the embedded controller

If nothing in software works, the embedded controller may be wedged. Shut down completely, unplug the charger, and if the battery is removable, take it out. Hold the power button for **30 seconds** to drain residual charge. Reconnect everything and boot. This resets the EC that bridges the touchpad's I2C bus to the CPU, and it revives touchpads that survived every driver fix. If the touchpad works in the BIOS menus or the Windows recovery environment but not in Windows, that points squarely at drivers — repeat Fix 4. If it works nowhere, a service visit is warranted.

## Closing

ELAN touchpad failures after the Windows 11 24H2 update are a driver problem in the overwhelming majority of cases, not a hardware one. The reliable path is: check the toggle, roll back or clean-reinstall the driver, and finish with the manufacturer's ELAN package. Keep a cheap USB mouse handy during troubleshooting, and once the touchpad is back, check for driver updates on the vendor site every few months to stay ahead of the next feature update.
