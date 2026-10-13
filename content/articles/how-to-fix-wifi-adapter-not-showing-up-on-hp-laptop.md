---
title: "Wi-Fi Adapter Not Showing Up on HP Laptop? How to Bring It Back"
slug: "how-to-fix-wifi-adapter-not-showing-up-on-hp-laptop"
date: 2026-09-16
categories: ["drivers"]
tags: ["wifi adapter missing", "hp laptop", "device manager", "wireless not showing", "wifi disappeared"]
description: "Wireless adapter missing from Device Manager on your HP laptop? Restore it with BIOS checks, cold boots, driver reinstalls, and HP diagnostics."
thumbnail: "/images/thumbs/how-to-fix-wifi-adapter-not-showing-up-on-hp-laptop.webp"
faqs:
  - q: "Why did my Wi-Fi adapter disappear from Device Manager?"
    a: "The adapter usually disappears because it failed to enumerate at boot, often after sleep, hibernation, or a failed driver update. The card may also be disabled in the BIOS or blocked by airplane mode. A full cold boot with power drained brings back most missing adapters. If it stays missing across cold boots, check the BIOS wireless setting and reinstall the driver from HP support."
  - q: "How do I check if Wi-Fi is disabled in the HP BIOS?"
    a: "Restart and press F10 to enter the BIOS setup. Navigate to the Advanced or Built-in Device Options section and look for the WLAN or wireless device setting. Make sure it is enabled, then save and exit. Some HP models also have a wireless button or key combination that toggles the radio at a firmware level, so check that as well."
  - q: "Can a Windows update make the Wi-Fi adapter vanish?"
    a: "Yes. Updates can install an incompatible driver that fails to start the card, after which Windows may hide the device entirely. They can also corrupt the driver stack during installation. If the adapter vanished right after an update, boot into Safe Mode, uninstall the wireless driver, and install the HP-validated driver from HP support for your model."
  - q: "Is a missing Wi-Fi adapter always a hardware failure?"
    a: "No, and hardware failure is actually the least common cause. Enumeration failures, BIOS settings, and driver corruption account for the vast majority. Only suspect hardware after the adapter stays missing through cold boots, BIOS confirmation, driver reinstalls, and a Linux live USB test. HP's pre-boot diagnostics can also test the wireless card directly."
---

A Wi-Fi adapter that vanishes from Device Manager is more alarming than one with an error, because there is nothing to troubleshoot directly. No networks list, no adapter entry, sometimes not even an unknown device. On HP laptops this almost always traces to enumeration failure at boot, a BIOS setting, or a driver problem rather than a dead card.

The key insight is that missing usually means not started rather than not present. The card is soldered or seated in the machine; Windows simply failed to bring it up. Cold boots, BIOS checks, and driver reinstalls bring it back in the large majority of cases.

Work through this guide from the least invasive step to the deepest. If the adapter appears but shows [Code 10](/articles/how-to-fix-wifi-driver-code-10-error-on-acer-laptop/) instead of vanishing, that guide is the right one.

## Why this happens

- **Failed enumeration after sleep:** the card does not come back up after sleep or hibernation and stays hidden.
- **Disabled in BIOS:** the WLAN device option in BIOS is off, so the OS never sees the card.
- **Airplane mode stuck on:** a firmware-level radio kill persists across boots.
- **Corrupted driver stack:** a failed update leaves the driver unable to start the card, and Windows hides it.
- **Fast Startup stale state:** hybrid shutdown preserves the failed enumeration across boots.
- **Hidden device:** the adapter is present but marked hidden after a failed start.
- **Loose card or antenna:** on models with socketed cards, reseating can be needed after drops.
- **Failed wireless module:** hardware failure, uncommon but possible, confirmed by diagnostics.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Show hidden devices in Device Manager

Windows hides devices that failed to start. Revealing hidden devices often shows the adapter sitting there with an error, which is far more actionable than nothing.

1. Open Device Manager.
2. Click View, then Show hidden devices.
3. Expand Network adapters and look for greyed-out wireless entries.
4. If it appears greyed out, right-click and choose Uninstall device.
5. Click Action, then Scan for hardware changes.

### Fix 2: Cold-boot with full power drain

A wireless card stuck in a bad state needs complete power removal to reset. This is the highest-yield single step for vanished adapters.

1. Shut the laptop down fully.
2. Unplug the charger and all USB devices.
3. Hold the power button for 20 seconds.
4. Wait one full minute before reconnecting power.
5. Power on and check Device Manager for the adapter.

### Fix 3: Check airplane mode and the wireless key

HP laptops have airplane mode toggles and sometimes dedicated wireless keys that kill the radio below the OS level. A stuck toggle hides the adapter completely.

1. Press Windows + A and make sure Airplane mode is off.
2. Look for a wireless or airplane key on the function row and toggle it.
3. Check the wireless LED indicator on the laptop if present.
4. In Settings, confirm Wi-Fi appears as an option at all.
5. Restart after toggling to let the radio reinitialize.

### Fix 4: Enable the WLAN device in BIOS

If the BIOS has the wireless device disabled, no Windows step can bring it back. Checking this takes two minutes and rules out the firmware layer.

1. Restart and press F10 to enter BIOS setup.
2. Find Built-in Device Options or the Advanced tab.
3. Locate the WLAN or wireless device setting.
4. Set it to Enabled.
5. Save changes, exit, and boot into Windows.

### Fix 5: Reinstall the HP wireless driver

With the card visible again, or even if it is not, removing the corrupted driver and installing HP's validated package repairs the software side completely.

1. In Device Manager, uninstall any wireless adapter entries with driver removal.
2. Restart the laptop.
3. Go to HP support, enter your model or serial number.
4. Download and install the latest Wi-Fi driver.
5. Restart and verify the adapter appears and connects.

### Fix 6: Reset BIOS to defaults

Misconfigured BIOS settings beyond the WLAN toggle can also suppress the card. Loading defaults restores sane values across the board.

1. Enter the BIOS setup with F10.
2. Choose the option to load setup defaults or optimized defaults.
3. Confirm the WLAN device is still enabled afterward.
4. Save and exit.
5. Cold-boot once more and check Device Manager.

### Fix 7: Run HP diagnostics and test hardware

HP's pre-boot diagnostics test the wireless card directly, independent of Windows. This gives a definitive hardware verdict when software steps fail.

1. Restart and press F2 to open HP PC Hardware Diagnostics.
2. Run the wireless or network component test.
3. Boot a Linux live USB as a second independent test.
4. If the card fails diagnostics, contact HP support for service.
5. Check [HP support](https://support.hp.com/us-en) for warranty status with your serial number.

## Closing

A missing Wi-Fi adapter on an HP laptop is usually a boot enumeration problem, not a dead card. Show hidden devices, cold-boot with a power drain, check the BIOS, and reinstall HP's driver. The adapter comes back in the large majority of cases. For related symptoms, see our guide on [finding missing drivers](/articles/how-to-find-missing-drivers-on-windows-11-on-laptop/). Preventing the next disappearance is mostly about shutdown hygiene: use full shutdowns periodically instead of endless sleep cycles, since sleep is where enumeration failures breed. Keep the HP-validated wireless driver installed and be cautious with driver updaters that promise newer versions; newer is not better when it has not been validated for your card. Finally, save the HP support driver page for your model as a bookmark and keep a USB Wi-Fi adapter in your bag as insurance; with both, a vanished adapter is an inconvenience rather than a crisis. One more preventive step: in Windows Update advanced options, consider pausing driver updates for a week after getting stable, since surprise driver swaps are a leading cause of repeat disappearances.
