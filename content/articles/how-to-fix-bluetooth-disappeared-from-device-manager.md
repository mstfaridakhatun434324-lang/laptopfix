---
title: "Bluetooth Disappeared From Device Manager? Get It Back Fast"
slug: "how-to-fix-bluetooth-disappeared-from-device-manager"
date: "2026-09-22"
categories: ["drivers"]
tags: ["bluetooth", "device manager", "wireless", "drivers", "windows"]
description: "Bluetooth vanished from Device Manager and Settings? Learn why the Bluetooth adapter disappears and follow proven steps to restore it on your laptop."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-disappeared-from-device-manager.webp"
faqs:
  - q: "Why did Bluetooth disappear from Device Manager completely?"
    a: "The Bluetooth radio usually shares a physical card with WiFi, so when its driver corrupts, gets replaced by Windows Update, or is disabled in BIOS, the entire Bluetooth section vanishes from Device Manager. Airplane mode or a function-key toggle can also hide it, and on some laptops the Bluetooth device only appears when the supporting USB or UART bus driver loads correctly during boot."
  - q: "How do I make Bluetooth show up again in Settings?"
    a: "Start in Device Manager with hidden devices shown, then scan for hardware changes and reinstall the Bluetooth driver from your laptop maker's support page. Check that airplane mode is off and that Bluetooth is enabled in BIOS. Once the driver loads, the Bluetooth toggle reappears in Settings automatically — the Settings page only shows when Windows detects a working radio."
  - q: "Can a Windows update remove Bluetooth from my laptop?"
    a: "It can appear that way. Updates sometimes replace the manufacturer's Bluetooth driver with a generic version that fails to start, or reset BIOS-adjacent radio settings, which removes the device from Device Manager. The hardware is unaffected. Reinstalling the OEM Bluetooth driver package and re-enabling the radio restores everything the update disrupted."
  - q: "Is my Bluetooth broken if WiFi still works?"
    a: "Usually not. WiFi and Bluetooth share one card but use separate drivers and firmware paths, so one can fail while the other works fine. If WiFi works, the card has power and is seated correctly, which strongly points to a Bluetooth driver or service problem rather than dead hardware. Focus on driver reinstallation and the Bluetooth Support Service before suspecting the card."
---

You open Settings to pair your headphones and the Bluetooth toggle is simply gone. Device Manager shows no Bluetooth section at all — not even an error, just absence. This is one of the more disorienting Windows problems because there is nothing to click, nothing to troubleshoot, just a missing feature.

Here is the reassuring part: on virtually every modern laptop, Bluetooth lives on the same physical card as WiFi. If your WiFi still works, the card is powered and seated, which means the Bluetooth disappearance is a software problem — a driver, a service, or a disabled radio — and software problems have reliable fixes. The steps below recover the Bluetooth stack in the order a technician would try them.

## Why this happens

- **Corrupted or replaced Bluetooth driver:** Windows Update swaps the OEM Bluetooth driver for a generic one that fails to initialize the radio.
- **Bluetooth disabled in BIOS:** Firmware toggles for the wireless radios can turn Bluetooth off independently of WiFi.
- **Airplane mode or function-key toggle:** A stuck airplane mode or Fn-key radio switch disables Bluetooth at a level Settings cannot see.
- **Bluetooth Support Service stopped:** If this background service is disabled, Windows hides Bluetooth even with a working driver.
- **Driver hidden after repeated failures:** Device Manager hides devices whose drivers fail to start, making the section vanish.
- **Fast startup skipping device init:** Hybrid boot can skip proper initialization of the Bluetooth bus after updates.
- **Failing combo card:** Rare, but the Bluetooth portion of a WiFi/Bluetooth card can die while WiFi keeps working.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices and rescan
Open Device Manager, click View, and select "Show hidden devices." Look for a greyed-out Bluetooth section. If you find it, right-click each entry, uninstall with driver deletion, then click Action and "Scan for hardware changes." If no Bluetooth section appears even hidden, move on — the driver is not loading at all. This step takes thirty seconds and resolves cases where a failed driver load simply hid the device. Our companion guide on [enabling hidden devices](/articles/how-to-enable-hidden-devices-in-device-manager-on-windows-11/) covers this technique in detail.

### Fix 2: Check airplane mode and the wireless function key
Open quick settings (Windows key + A) and make sure airplane mode is off. Then press your laptop's wireless toggle — usually Fn plus a key with a tower icon — and watch for an indicator change. Some laptops tie Bluetooth to this hardware switch independently of the Windows airplane mode setting. Toggle it, wait ten seconds, and rescan in Device Manager. If the Bluetooth section appears, the radio was simply switched off at the hardware level.

### Fix 3: Start the Bluetooth Support Service
Press Windows key + R, type `services.msc`, and locate "Bluetooth Support Service." Set its Startup type to Automatic and start it if it is stopped. Also check "Bluetooth Audio Gateway Service" and "Bluetooth User Support Service" on newer Windows builds. Without these services, Windows will not surface Bluetooth in Settings even when the driver is perfect. Restart the laptop after changing them and check Settings again.

### Fix 4: Reinstall the OEM Bluetooth driver
Download the Bluetooth driver for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). In Device Manager (with hidden devices shown), uninstall any Bluetooth entries with driver deletion, then install the downloaded package and reboot. The OEM package includes the correct firmware loader for your specific combo card — generic Windows drivers frequently fail to initialize the Bluetooth side. Intel card owners can cross-check with the Intel Driver & Support Assistant.

### Fix 5: Enable Bluetooth in BIOS/UEFI
Restart into firmware setup and look under Advanced, Devices, or Wireless for Bluetooth or WLAN/Bluetooth toggles. Ensure Bluetooth is enabled, save, and exit. BIOS updates sometimes reset these to disabled, which removes the device before Windows ever sees it. While you are there, disable "Fast Boot" if present, since aggressive fast boot can skip initializing secondary buses that Bluetooth depends on.

### Fix 6: Disable fast startup and power-cycle
Go to Control Panel, Power Options, "Choose what the power buttons do," click "Change settings that are currently unavailable," and uncheck fast startup. Shut down fully (not restart), unplug AC power, hold the power button for 30 seconds, then boot. Fast startup's hybrid hibernation is a notorious cause of Bluetooth failing to initialize after updates, and a true cold boot with drained residual power clears the stuck state. Related radio issues like [airplane mode stuck on](/articles/how-to-fix-airplane-mode-stuck-on-step-by-step/) respond to the same treatment.

### Fix 7: Run the Bluetooth troubleshooter and test the hardware
Go to Settings, System, Troubleshoot, Other troubleshooters, and run the Bluetooth troubleshooter — it can repair service registrations and stack corruption automatically. If Bluetooth is still absent, boot a Linux live USB: if Bluetooth works there, your Windows install needs a repair install; if it is missing in Linux too, the combo card's Bluetooth side has likely failed. Replacement WiFi/Bluetooth cards are inexpensive, though some laptops require professional service to access them.

## Closing
Bluetooth does not really "disappear" — it gets hidden by a failed driver, a stopped service, a disabled radio, or a boot shortcut that skipped its initialization. Revealing hidden devices, restarting the support services, reinstalling the OEM driver, and forcing a true cold boot brings it back in the overwhelming majority of cases, with hardware failure a distant last resort. Keeping Bluetooth visible is mostly about not letting the stack regress: after each Windows feature update, open Settings and confirm the Bluetooth toggle is present before you need it — discovering it missing right before a flight is the worst timing. Keep the OEM Bluetooth driver installer saved with your other drivers so a reinstall never depends on a working internet connection. If your laptop has a physical wireless switch, make its position part of your mental checklist whenever radios misbehave; it is astonishing how often a switch nudged in a bag is the whole story. For users who pair many devices, note that Windows 11 handles Bluetooth LE Audio and classic Bluetooth through the same stack, so a single driver fix restores headsets, mice, and keyboards together. And if Bluetooth ever vanishes alongside WiFi simultaneously, suspect the shared combo card or its BIOS toggle rather than either driver — the two radios failing together is a hardware-level signal, not a coincidence.
