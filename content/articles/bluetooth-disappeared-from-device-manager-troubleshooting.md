---
title: "Bluetooth Disappeared From Device Manager: Full Troubleshooting"
slug: bluetooth-disappeared-from-device-manager-troubleshooting
date: 2026-09-13
categories: ["drivers"]
tags: ["bluetooth disappeared", "bluetooth troubleshooting", "bluetooth driver reinstall"]
description: "Bluetooth disappeared from Device Manager and won't come back? Full troubleshooting — services, drivers, BIOS, power states, and hardware isolation."
thumbnail: "/images/thumbs/bluetooth-disappeared-from-device-manager-troubleshooting.webp"
faqs:
  - q: "What is the difference between Bluetooth not working and Bluetooth disappeared?"
    a: "Not working means the adapter is visible but fails to connect or pair — a stack or configuration issue. Disappeared means Device Manager shows no Bluetooth section at all, which points to driver-loading failure, BIOS disablement, or hardware enumeration problems. The fixes differ, so identifying which you have matters."
  - q: "Why do Bluetooth and Wi-Fi break at the same time?"
    a: "Most laptops use a single M.2 combo card for both radios with separate drivers. A bad wireless driver update, BIOS toggle, or power state affects the shared hardware, taking both radios down together. Fixing the combo card's drivers often restores both at once."
  - q: "Should I reset Windows to fix missing Bluetooth?"
    a: "No — a full reset is disproportionate. Driver reinstallation, service restarts, and BIOS checks resolve the software causes without wiping your system. Only consider a Windows repair install if several unrelated subsystems broke simultaneously. A repair install keeps your apps and files while refreshing system components, making it far less drastic than a full reset."
  - q: "How can I tell if the Bluetooth hardware is actually dead?"
    a: "If Bluetooth is absent from Device Manager (with hidden devices shown), absent from the BIOS, and a USB Bluetooth dongle works fine, the internal combo card or its connection is the likely failure. Reseating or replacing the M.2 card is the remaining fix."
---

When Bluetooth disappears from Device Manager entirely — no section, no hidden grayed-out entry, no error code — you are dealing with an enumeration failure: Windows cannot see the Bluetooth radio at all. This is different from Bluetooth that is present but will not pair, and it needs its own troubleshooting path focused on drivers, services, firmware toggles, and the shared Wi-Fi/Bluetooth hardware underneath.

This guide is the deep-dive companion to the quick fixes: full diagnostics for every layer, from the Bluetooth Support Service to the M.2 combo card. Follow the sequence — each step eliminates a layer, and the adapter reappears the moment you clear the blocked one.

## Why this happens

- **Bluetooth driver failed after update:** The new driver cannot initialize the radio, so the device never enumerates.
- **Bluetooth Support Service disabled:** Without this service running, the Bluetooth stack does not start.
- **BIOS wireless/Bluetooth toggle off:** Firmware hides the radio from the OS completely.
- **Stuck airplane mode:** A locked radio state suppresses Bluetooth alongside Wi-Fi.
- **USB power management:** The internal USB interface of the Bluetooth radio gets suspended permanently.
- **Combo-card driver mismatch:** Wi-Fi and Bluetooth drivers for the shared card fall out of sync.
- **Corrupted driver store:** Failed installations leave broken entries that block clean reinstallation.
- **Fast startup preserving bad state:** Hibernation-based boot restores a failed enumeration every time.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the disappearance and check services

Establish exactly what "disappeared" means on your machine.

1. Open Device Manager, click **View > Show hidden devices**, and search all sections for Bluetooth entries.
2. Open **Services** (`services.msc`): set **Bluetooth Support Service** to **Automatic** and start it.
3. Check **Settings > Bluetooth & devices** — if the toggle is missing, the stack truly is not loading.
4. Note whether Wi-Fi also misbehaves; joint failure points at the combo card.

If the service starts and Bluetooth appears, you are done. If the service stops again immediately, the driver beneath it is broken — continue.

### Fix 2: Reinstall Bluetooth and Wi-Fi drivers as a pair

Combo cards need matched drivers.

1. Identify the card (Intel AX201/AX210, MediaTek MT7921/7922, Realtek, Qualcomm) from specs or the hidden Device Manager entry.
2. Download both the **Bluetooth** and **Wi-Fi** drivers for your exact model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), [Lenovo Support](https://support.lenovo.com/us/en/), or the Intel Driver & Support Assistant.
3. In Device Manager, uninstall all Bluetooth and wireless entries, checking driver removal.
4. Install the Wi-Fi driver first, then the Bluetooth driver, then restart.

Installing as a pair prevents the version mismatch that causes one radio to enumerate while the other vanishes. For the quick-reference version of this fix, see our [Bluetooth disappeared quick guide](/articles/best-way-to-fix-bluetooth-disappeared-from-device-manager/).

### Fix 3: Clear the driver store of broken Bluetooth entries

Corrupted remnants can block every reinstall attempt.

1. In Device Manager with hidden devices shown, uninstall every Bluetooth-related entry, checking **Attempt to remove the driver for this device** each time.
2. Open an elevated Command Prompt and run `pnputil /enum-drivers`, looking for Bluetooth driver packages from the problematic vendor.
3. Remove broken ones with `pnputil /delete-driver oemXX.inf /uninstall` (use the exact published name shown).
4. Restart and install the fresh manufacturer driver from Fix 2.

Be careful with `pnputil` — only remove drivers you have identified as Bluetooth-related. When in doubt, skip the manual deletion; the uninstall-with-removal in Device Manager handles most cases.

### Fix 4: Reset radio and power states

Stuck states hide radios at multiple levels.

1. Turn **Airplane mode** off in Settings and toggle any physical wireless switch or **Fn** radio key.
2. In **Power Options > advanced settings**, disable **USB selective suspend**.
3. In Device Manager, uncheck power-saving on **USB Root Hub** entries.
4. Disable **fast startup** (Power Options > Choose what the power buttons do), then shut down fully and cold-boot.

If Bluetooth returns after the cold boot but vanishes again after sleep, you have isolated a power-management bug — keep selective suspend off permanently. For Wi-Fi-side symptoms, our [Wi-Fi adapter troubleshooting](/articles/best-way-to-fix-wifi-adapter-not-showing-up/) covers the shared hardware from the wireless angle.

### Fix 5: Verify BIOS toggles and firmware

Check what the firmware reports about the radio.

1. Reboot into BIOS/UEFI setup and look for **Bluetooth**, **BT**, or **Wireless** toggles — enable them.
2. If the BIOS shows no Bluetooth device or option, the firmware cannot see the hardware: note this for the hardware step.
3. Check for a BIOS update on the manufacturer's support page — BIOS updates regularly fix device enumeration bugs.
4. Apply the update with the charger connected and never interrupt it.

A BIOS update that mentions "wireless," "BT," or "device enumeration" in its changelog is a strong candidate fix for disappearance issues.

### Fix 6: Test with a USB Bluetooth dongle

Isolate hardware from software definitively.

1. Plug in any USB Bluetooth adapter. If Windows immediately shows Bluetooth settings, the OS stack is healthy and the internal radio is the problem.
2. If the dongle also fails, run `sfc /scannow` and consider a Windows in-place repair install — the stack itself is damaged.
3. A working dongle is also your immediate workaround: sub-$15 adapters provide fully functional Bluetooth while you decide on internal repair.

This single test answers the hardware-vs-software question more reliably than any amount of driver reinstallation.

### Fix 7: Reseat or replace the M.2 combo card

The physical layer, for when software is exhausted.

1. If comfortable and warranty allows: power off, open the bottom panel, locate the M.2 wireless card, reseat it, and reattach the antenna leads.
2. If reseating fails, replace the card — Intel AX210 cards are inexpensive, widely compatible, and a common upgrade.
3. Match the form factor (2230 vs 2280) and keying when buying a replacement.
4. After replacement, install the driver for the new card and verify both Wi-Fi and Bluetooth.

Also lock in the working drivers afterward with our [automatic driver update guide](/articles/best-way-to-disable-automatic-driver-updates/) so a bad update does not recreate the problem.

## Closing

Bluetooth that vanishes from Device Manager is an enumeration failure, and the fix is a layer-by-layer elimination: services, paired driver reinstall, radio and power states, BIOS, and finally the hardware itself. The USB dongle test is your decisive fork — it tells you in sixty seconds whether to keep fighting software or start planning a card replacement.
