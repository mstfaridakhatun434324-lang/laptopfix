---
title: "How to Fix Intel Wi-Fi 6 AX201 Not Working on an HP Laptop"
slug: "how-to-fix-intel-wifi-6-ax201-not-working-on-hp-laptop"
date: "2026-09-08"
categories: ["drivers"]
tags: ["intel ax201", "wifi 6", "hp laptop", "wireless driver", "network adapter"]
description: "Intel Wi-Fi 6 AX201 not working on your HP laptop? This step-by-step guide covers driver reinstalls, power management, BIOS settings, and hardware checks to restore your wireless connection."
thumbnail: "/images/thumbs/how-to-fix-intel-wifi-6-ax201-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why did my Intel Wi-Fi 6 AX201 stop working after a Windows update?"
    a: "Windows Update sometimes installs a generic or mismatched wireless driver that conflicts with the AX201 hardware, causing the adapter to fail with Code 10 or disappear entirely. The update may also reset power management settings or disable the device. Rolling back the driver or installing the latest Intel Wi-Fi driver package from HP or Intel usually resolves this conflict within minutes."
  - q: "Should I download the Wi-Fi driver from HP or Intel?"
    a: "Start with HP's official support site, since HP customizes drivers for your exact model and may include required Bluetooth or platform dependencies. If HP's driver is outdated or does not fix the problem, try Intel's generic Wi-Fi driver package using the Intel Driver & Support Assistant. Both sources are safe, but HP's version is tuned for your laptop's BIOS and power states."
  - q: "How do I know if my AX201 failure is a driver problem or a dead card?"
    a: "If the adapter appears in Device Manager with a yellow warning, shows under hidden devices, or worked recently, it is almost certainly a driver or configuration problem. A likely hardware failure shows as the adapter being completely absent even after showing hidden devices, a clean OS reinstall, and a BIOS reset. The Intel card is replaceable on some HP models but soldered on others."
  - q: "Can a BIOS update fix Intel AX201 Wi-Fi problems?"
    a: "Yes, an outdated BIOS can cause AX201 issues, especially power-state errors or the adapter not being enumerated at boot. HP periodically releases BIOS updates that improve wireless card compatibility and fix PCIe link training. Check HP's support page for your model, follow the update instructions carefully, and never interrupt the process. Keep the laptop on AC power during the update."
---

The Intel Wi-Fi 6 AX201 is one of the most common wireless cards shipped inside modern HP laptops, from Pavilion and Envy models to ProBook and EliteBook business machines. When it fails, the symptoms are unmistakable: no networks appear in the taskbar, the adapter vanishes from Device Manager, or it sits there with a yellow warning triangle and an error code.

The good news is that a genuinely dead AX201 card is rare. In the vast majority of cases, the problem is a corrupt, mismatched, or outdated driver, a power-management conflict, or a Windows setting that got flipped during an update. The fixes below are ordered from the quickest software checks to deeper driver and firmware work, so start at the top and stop as soon as your connection returns.

## Why this happens

- **Corrupted driver after a Windows Update:** Windows Update frequently pushes its own version of the Intel wireless driver, which can clash with HP's customized build and break the adapter.
- **Mismatched driver version:** Installing a generic Intel package on a system that expects HP's OEM-tuned driver — or vice versa — can produce Code 10 errors.
- **Power management turning the card off:** Windows may cut power to the AX201 to save battery, and on some HP firmware builds it never wakes back up properly.
- **Disabled in Device Manager or BIOS:** The wireless adapter can be disabled by a Windows policy, a previous troubleshoot, or the BIOS wireless toggle.
- **Bluetooth coexistence conflict:** The AX201 handles both Wi-Fi and Bluetooth on one card; a Bluetooth stack crash can drag the Wi-Fi side down with it.
- **Outdated BIOS firmware:** Older HP BIOS versions have known PCIe enumeration quirks that leave the AX201 invisible after sleep or a fast startup.
- **Fast Startup corrupting device state:** Windows Fast Startup saves a hibernation snapshot that can lock the wireless card into a bad power state across reboots.
- **Physical hardware failure:** A loose M.2 connector, a damaged antenna lead, or a failing card — uncommon, but possible after drops or repairs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the basics and the hardware switch

Make sure the problem is really the AX201 before you touch drivers. Some HP laptops have a dedicated wireless function key (often F12 with a small antenna icon) that toggles the radio — press Fn + F12 and watch for the indicator light. Then open Settings > Network & internet and confirm Wi-Fi is switched on.

1. Run Settings > System > Troubleshoot > Other troubleshooters > Network and Internet, and apply its suggestions.
2. If a red X or airplane icon persists, continue to the driver checks below.

### Fix 2: Inspect the adapter in Device Manager

Device Manager tells you exactly what state the AX201 is in, which shapes everything you do next.

1. Press Win + X and choose Device Manager.
2. Expand Network adapters and look for "Intel(R) Wi-Fi 6 AX201 160MHz" — click View > Show hidden devices if it is missing.
3. A yellow warning icon means a driver problem: double-click it and note the error code (10, 43, and 45 are common).
4. A greyed-out entry means disabled: right-click it and choose Enable device.
5. Record what you find — it tells you whether to re-enable, reinstall, or roll back.

### Fix 3: Roll back or reinstall the driver

This single step resolves most AX201 failures. If the problem started after a recent update, roll back first; otherwise do a clean reinstall.

1. In Device Manager, right-click the Intel Wi-Fi 6 AX201 and choose Properties.
2. On the Driver tab, click Roll Back Driver if the button is available, and explain why.
3. If rollback is not available, choose Uninstall device instead.
4. In the uninstall dialog, tick "Attempt to remove the driver for this device" so Windows cannot reinstall the broken version.
5. Click Uninstall, then restart the laptop.
6. Windows will usually detect the card on boot and install a working inbox driver — test your Wi-Fi before doing anything else.
7. If Windows does not reinstall automatically, go to Action > Scan for hardware changes.

### Fix 4: Install the latest driver from HP or Intel

If the clean reinstall did not help, get the newest driver directly from the source. HP customizes wireless drivers for its hardware, so start there. If you have no internet on the laptop, see [installing drivers without internet](/articles/how-to-install-drivers-without-internet-on-windows-11/) first.

1. On another device, visit [HP's official support page](https://support.hp.com/us-en), enter your exact model, and download the latest Intel wireless driver.
2. Transfer it to the laptop with a USB stick and run the installer, choosing a clean install if offered.
3. If HP's driver is older than six months or did not fix the issue, use Intel's official [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to scan and install the newest generic package.
4. Restart after the install and test Wi-Fi before and after connecting to power.
5. Note that Intel generic drivers sometimes drop HP-specific tweaks, so if the generic driver behaves worse, revert to the HP build.

### Fix 5: Stop Windows from powering off the adapter

Windows power management is a classic cause of AX201 dropouts, especially on battery.

1. In Device Manager, right-click the AX201 and choose Properties.
2. Go to the Power Management tab and uncheck "Allow the computer to turn off this device to save power".
3. Click OK, then open Control Panel > Power Options > Change plan settings > Change advanced power settings.
4. Expand Wireless Adapter Settings > Power Saving Mode and set both On battery and Plugged in to Maximum Performance.
5. While you are there, expand USB settings and disable USB selective suspend if your Bluetooth side is also flaky.
6. Restart the laptop and test on battery and on AC power.

### Fix 6: Disable Fast Startup and reset the network stack

Fast Startup can trap the AX201 in a corrupted power state that survives normal reboots.

1. Open Control Panel > Power Options > Choose what the power buttons do.
2. Click "Change settings that are currently unavailable".
3. Uncheck "Turn on fast startup" and save changes.
4. Shut the laptop down completely (do not just restart), wait 30 seconds, then power it on.
5. If Wi-Fi is still broken, open Command Prompt as administrator and run `netsh winsock reset` followed by `netsh int ip reset`.
6. Restart once more and check the adapter.

### Fix 7: Update the BIOS and reset it to defaults

HP BIOS updates frequently include wireless compatibility fixes for the AX201 platform.

1. Find your exact model on HP's support site and check the BIOS section for updates newer than what you have.
2. Download the BIOS update, keep the laptop plugged into AC power, and run it without interrupting.
3. After the update, enter the BIOS (usually F10 during boot).
4. Use the option to load setup defaults, then confirm the wireless adapter is enabled in the BIOS settings.
5. Save, exit, and boot into Windows to test the adapter again.

### Fix 8: Reseat the card or rule out hardware failure

If the AX201 never appears in Device Manager even with hidden devices shown, and a BIOS default reset changed nothing, suspect hardware.

1. Power off the laptop, unplug it, and remove the battery if it is removable.
2. Open the bottom cover (check HP's service manual for your model first — this can void warranty on some units).
3. Locate the M.2 wireless card, reseat it firmly, and confirm both antenna leads are snapped on.
4. Reassemble, power on, and check Device Manager. If the card is still invisible, it has likely failed — contact HP support, since some HP models solder the wireless card.

## Closing

Intel Wi-Fi 6 AX201 failures on HP laptops almost always trace back to drivers or power management, and the sequence above covers the full spectrum — from a flipped function key to a genuine hardware fault. Once your Wi-Fi is back, prevent repeats by disabling Windows' automatic [driver updates](/articles/how-to-disable-automatic-driver-updates-on-windows-11/) for the wireless adapter, keeping your BIOS current, and downloading new wireless drivers only from HP or Intel rather than third-party driver tools.
