---
title: "WiFi Adapter Not Showing Up in Device Manager? How to Fix It"
slug: wifi-adapter-not-showing-up-troubleshooting
date: "2026-10-10"
categories: ["drivers"]
tags: ["wifi adapter", "network adapter missing", "device manager", "wireless not detected"]
description: "WiFi adapter missing from Device Manager on your laptop? Learn how to reveal hidden adapters, reinstall the wireless driver, and restore your WiFi connection."
thumbnail: "/images/thumbs/wifi-adapter-not-showing-up-troubleshooting.webp"
faqs:
- q: "Why is my WiFi adapter not showing up in Device Manager?"
  a: "The usual reasons are a corrupted or missing wireless driver, the adapter being disabled in BIOS, Windows hiding the device after a failed update, or power settings that switched the card off. Less commonly, the WiFi card itself has failed or worked loose from its slot. Checking hidden devices first, then the driver, then BIOS settings identifies which of these applies in a few minutes."
- q: "How do I unhide my WiFi adapter in Device Manager?"
  a: "Open Device Manager, click the View menu, and select Show hidden devices. Adapters that Windows has deactivated appear grayed out under Network adapters. Right-click the grayed-out WiFi adapter and choose Enable device. If the adapter appears with a warning icon instead, the driver is the problem and needs reinstalling rather than simply enabling."
- q: "Can airplane mode hide the WiFi adapter completely?"
  a: "Airplane mode normally just disables the radios rather than hiding the adapter, but on some laptops a stuck airplane mode or a faulty Fn-key toggle can make the adapter vanish from the active device list. Toggle airplane mode off in Quick Settings, check the physical WiFi switch or Fn key combination on your laptop, and restart — the adapter frequently reappears after the radio state resets."
- q: "Is a missing WiFi adapter a sign of hardware failure?"
  a: "Not usually. Driver corruption and BIOS toggles account for the large majority of cases, and both are fixable in software. Hardware failure becomes likely only when the adapter is absent even with hidden devices shown, no driver will install to it, and a Linux live USB also sees no wireless card. At that point the M.2 WiFi card may need reseating or replacement, which is a simple repair on most laptops."
---

There is a special kind of panic when the WiFi icon vanishes from the taskbar, you open Device Manager to investigate, and the wireless adapter is simply not there. No warning triangle, no disabled entry — the Network adapters section shows Ethernet and Bluetooth and nothing else, as if your laptop never had WiFi at all.

Before assuming the worst, know this: a missing adapter is a software problem far more often than a hardware one. Windows hides devices it cannot bind a driver to, BIOS settings can switch the radio off at a level Windows cannot see, and power management occasionally parks the card so aggressively it drops off the bus. All of these are reversible, and the checks are quick.

This guide works from the least invasive step to the most — revealing hidden devices, resetting the radio state, reinstalling the driver, checking BIOS, and finally verifying the hardware. Follow in order; most people find their adapter long before the last fix.

## Why this happens

- **Corrupted or missing wireless driver**: Without a working driver, Windows may hide the adapter instead of showing it with an error.
- **Adapter disabled in BIOS/UEFI**: A firmware-level toggle switches the radio off where Windows cannot see or override it.
- **Stuck airplane mode or Fn-key radio toggle**: A latched radio-off state can remove the adapter from the active device list.
- **Aggressive power management**: Link-state power saving can park the card so deeply it drops off the PCI bus until reset.
- **Failed Windows update**: Interrupted updates leave the driver half-installed, and Windows hides the resulting broken device.
- **Loose or failed M.2 WiFi card**: The card can work loose from its slot over years of heat cycles, or simply die.
- **Hidden by Device Manager's default view**: Deactivated devices are invisible until you enable "Show hidden devices."

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices in Device Manager

Device Manager hides deactivated devices by default, which makes a merely disabled adapter look like a missing one. This one menu toggle changes the picture completely: grayed-out adapters reappear, and you can see whether Windows knows about the hardware but has parked it. Always start here — it takes five seconds.

1. Press Win + X and open Device Manager.
2. Click View in the menu bar and select "Show hidden devices."
3. Expand "Network adapters" and look for a grayed-out WiFi or wireless entry.
4. If you find it, right-click and choose "Enable device."
5. If it shows a warning icon instead, the driver needs reinstalling — continue to Fix 4.

### Fix 2: Reset the radio state — airplane mode, switches, and Fn keys

Laptops control the wireless radio through several overlapping switches: Windows airplane mode, a physical slider on some models, and an Fn-key combination on most. When these disagree — say the Fn toggle is off while Windows thinks it is on — the adapter can vanish. Cycling every switch forces them back into agreement.

1. Open Quick Settings (Win + A) and make sure Airplane mode is off.
2. Check your laptop for a physical WiFi switch or slider and set it to on.
3. Press the Fn + wireless key combination (often Fn + F2 or a key with an antenna icon).
4. Restart the laptop and recheck Device Manager with hidden devices shown.
5. If the adapter reappears, connect to your network and confirm stability.

### Fix 3: Perform a full power cycle to reset the hardware bus

A normal restart does not fully power down modern laptops — fast startup keeps hardware in a low-power state across reboots. If the WiFi card has wedged itself on the PCI bus, only a complete power drain resets it. This sounds like folk wisdom, but it genuinely revives adapters that vanish after sleep or hibernation.

1. Shut the laptop down completely (hold Shift while clicking Shut down to bypass fast startup).
2. Unplug the charger and, if the battery is removable, take it out.
3. Hold the power button for 30 seconds to drain residual charge.
4. Reconnect power, boot up, and open Device Manager.
5. Check whether the WiFi adapter has reappeared under Network adapters.

### Fix 4: Reinstall the wireless driver from the manufacturer

When the adapter appears with a warning, shows as an [unknown device](/articles/how-to-fix-unknown-device-in-device-manager/), or appears only as hidden and will not enable, the driver is corrupt. Downloading the wireless driver for your exact model from the manufacturer and installing it clean gives Windows a working driver to bind. [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can auto-detect the right package for Intel-based cards.

1. On another device if needed, download the WiFi driver from your laptop maker's support page.
2. In Device Manager, right-click the WiFi adapter (or unknown device), choose "Uninstall device," and tick "Attempt to remove the driver."
3. Run the downloaded driver installer and restart when prompted.
4. Open Device Manager and confirm the adapter appears without warnings.
5. Connect to your WiFi network to verify full functionality.

### Fix 5: Reset Windows network settings

If the adapter is present but nonfunctional, or if it appears and disappears, corrupted network configuration may be the culprit. The built-in network reset reinstalls all network adapters and returns every network setting to defaults. It is a blunt instrument — you will need to re-enter WiFi passwords — but it clears configuration damage that driver reinstalls cannot.

1. Open Settings, go to Network and internet, then Advanced network settings.
2. Click "Network reset" and then "Reset now."
3. Confirm and let the laptop restart automatically.
4. After reboot, check Device Manager for the WiFi adapter.
5. Reconnect to your WiFi network with the password.

### Fix 6: Check the wireless toggle in BIOS/UEFI

A BIOS-level wireless disable is invisible to Windows: no driver, no hidden device, nothing. It happens after BIOS updates that reset settings to defaults, or when someone toggles it while troubleshooting something else. Entering setup and re-enabling the radio takes two minutes and explains the cases where absolutely nothing appears in Device Manager.

1. Restart and enter BIOS/UEFI setup (usually F2 or Del during boot).
2. Look under Advanced, Devices, or Security for "Wireless," "WLAN," or "WiFi."
3. Make sure it is set to Enabled.
4. Save and exit, then boot into Windows.
5. Open Device Manager — the adapter should now be detected.

### Fix 7: Reseat or replace the M.2 WiFi card

If the adapter is absent everywhere — not in Device Manager even with hidden devices shown, not in BIOS, and not visible to a Linux live USB — the card itself is suspect. Most laptop WiFi cards are standard M.2 modules held by one screw, and reseating takes minutes. Replacement cards cost little and are a straightforward upgrade path to WiFi 6.

1. Boot a Linux live USB first: if Linux also sees no wireless card, hardware is confirmed as the issue.
2. Power down, unplug, and remove the bottom panel (check a teardown guide for your model).
3. Locate the M.2 WiFi card, remove its screw, and reseat it firmly in the slot.
4. Reconnect the two tiny antenna wires (black and white) to the matching terminals.
5. Reassemble, boot, and install the driver — or replace the card if reseating fails. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) cover the software-side network troubleshooting that complements this hardware check.

If WiFi vanished from the taskbar but the adapter is still present, the companion guide on [what to do if WiFi disappeared from your laptop](/articles/what-to-do-if-wifi-disappeared-from-laptop/) addresses that variant. For a full clean driver replacement procedure, see [how to reinstall the WiFi driver on Windows 11](/articles/how-to-reinstall-wifi-driver-on-windows-11/).

## Closing

A WiFi adapter that does not show up is usually hiding, not dead — concealed by Device Manager's default view, parked by power management, or orphaned by a broken driver. Reveal hidden devices, reset the radio state, reinstall the manufacturer's driver, and check BIOS before suspecting hardware. The card itself is the last thing to blame, not the first.
