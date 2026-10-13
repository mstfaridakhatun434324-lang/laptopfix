---
title: "What to Do If Your Wi-Fi Adapter Isn't Showing Up"
slug: what-to-do-if-wifi-adapter-not-showing-up
date: 2026-10-05
categories: ["drivers"]
tags: ["wifi adapter missing", "network adapter", "device manager", "wireless card", "no wifi"]
description: "No Wi-Fi adapter in Device Manager and no wireless option in Windows? Systematic fixes from hidden-device checks to BIOS toggles and hardware diagnosis."
thumbnail: "/images/thumbs/what-to-do-if-wifi-adapter-not-showing-up.webp"
faqs:
  - q: "Why did my Wi-Fi adapter disappear from Device Manager?"
    a: "The adapter disappears when Windows can't enumerate it: the card is disabled in BIOS, its driver failed catastrophically, the M.2 card worked loose, or the hardware died. Unlike a driver problem — which shows the device with a warning — a missing device means the OS sees nothing on the bus, so the fixes target enumeration: BIOS, reseating, and driver stack rebuilds."
  - q: "Can a Windows update make the Wi-Fi adapter vanish?"
    a: "Yes. Updates can install an incompatible wireless driver that fails to load, leaving no adapter visible. They can also reset BIOS-adjacent settings on some machines. If the adapter vanished right after an update, boot into BIOS first to confirm the card is enabled there — then roll back or reinstall the driver from the manufacturer's site."
  - q: "Is a missing Wi-Fi adapter always a hardware failure?"
    a: "No — most cases are software or configuration. BIOS toggles, corrupted drivers, and Windows power management account for the majority. Hardware failure is the diagnosis of exclusion: it applies only after BIOS confirms the card is enabled, drivers are cleanly reinstalled, and the card still doesn't enumerate. A USB Wi-Fi adapter is the quick confirmatory test."
  - q: "Will a USB Wi-Fi adapter work if the internal one is missing?"
    a: "Yes, and it's both a workaround and a diagnostic. A USB adapter uses a completely independent driver and hardware path, so it works regardless of what happened to the internal card. If the USB adapter works perfectly, the laptop's USB subsystem is fine and the fault is isolated to the internal wireless card or its driver."
---

A missing Wi-Fi adapter is different from broken Wi-Fi. Broken Wi-Fi shows an adapter with an error; a missing adapter shows nothing — no wireless section in Settings, no adapter in Device Manager's Network adapters, sometimes not even a hidden device. Windows behaves as if the laptop never had wireless hardware.

This is an enumeration failure, and the fixes run from "Windows is hiding it" through "the BIOS disabled it" to "the card is dead." If your adapter appears but won't connect or performs badly, our [Dell Wi-Fi guide](/articles/how-to-fix-wifi-not-working-on-dell-laptop/) and [Wi-Fi 6 guide](/articles/what-to-do-if-wifi-6-not-working-on-laptop/) cover those adjacent problems.

## Why this happens

- **The card is disabled in BIOS/UEFI.** The firmware hides it from the OS entirely.
- **A failed driver update.** An incompatible driver that won't load can leave no visible adapter.
- **Windows is hiding non-present devices.** Device Manager's default view omits disconnected devices.
- **Power management shut it down hard.** Aggressive power policies can leave the card unenumerated after sleep.
- **The M.2 card worked loose.** Thermal cycling and movement can unseat the card over years.
- **Antenna or card hardware failure.** Dead cards don't enumerate, period.
- **Airplane-mode / radio kill stuck.** A stuck radio kill switch can suppress enumeration on some models.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Show hidden devices and scan

Windows may be hiding the adapter rather than missing it.

1. Open **Device Manager** and click **View > Show hidden devices**.
2. Expand **Network adapters** and look for grayed-out entries — a grayed adapter is present-but-disconnected.
3. Click **Action > Scan for hardware changes** and watch for the adapter to appear.
4. Check **Other devices** for unknown entries that might be the wireless card without a driver.

A grayed-out adapter that reappears on scan is a driver or power-state issue, not hardware death. Note exactly what appears — the device name tells you whether Windows recognizes the card but can't start it (driver problem) or sees only a generic device (missing driver).

### Fix 2: Check BIOS for the wireless toggle

The firmware can hide the card from Windows completely — and it does so silently.

1. Restart and enter BIOS/UEFI (F2, F12, or Del at the boot logo).
2. Find **Wireless**, **WLAN**, or **Network** settings — location varies by manufacturer.
3. Ensure the wireless card is **Enabled**; save and exit.
4. Boot into Windows and re-check Device Manager.

Also verify there's no **Wireless Switch** behavior configured oddly — some BIOSes tie enumeration to the physical switch position. If the card was disabled in BIOS, consider how it got that way: IT policy, an accidental change, or a BIOS reset all leave this signature.

### Fix 3: Power-drain reset

A card stuck in a bad power state may not enumerate until fully power-cycled.

1. Shut down completely and disconnect the charger.
2. If the battery is removable, remove it; otherwise, hold the power button for 30 seconds.
3. Wait a full minute, reconnect power, and boot.
4. Check Device Manager for the adapter before opening any network settings.

This drains the auxiliary power that keeps the wireless card's state machine alive across normal reboots. It's the same principle as the EC reset technicians perform — you're forcing every chip to cold-boot from zero.

### Fix 4: Reinstall the wireless driver from the manufacturer

A catastrophically failed driver can suppress enumeration. Replace it from a clean state.

1. On another device if needed, download the wireless driver for your exact model from the manufacturer — [Dell](https://www.dell.com/support) or [HP](https://support.hp.com/us-en).
2. In Device Manager (with hidden devices shown), uninstall any wireless-related entries, ticking **Attempt to remove the driver**.
3. Install the manufacturer's package and restart.
4. If the adapter still doesn't appear, try the chip vendor's driver ([Intel's tool](https://www.intel.com/content/www/us/en/support/detect.html)) as an alternative.

Transfer the installer via USB if the laptop has no connectivity — our [offline driver guide](/articles/how-can-i-install-drivers-without-internet/) details the bridge process. Install the driver before concluding hardware failure; you'd be surprised how often "dead card" is "dead driver."

### Fix 5: Reset network and power settings

Corrupted network configuration and aggressive power policies can both suppress the adapter.

1. Run **Settings > Network & internet > Advanced network settings > Network reset**, then restart.
2. In **Device Manager**, if the adapter appears, open its **Properties > Power Management** and uncheck **Allow the computer to turn off this device**.
3. In **Power Options > Advanced**, disable **USB selective suspend** (some wireless cards are USB-connected internally).
4. Check the manufacturer's power utility for adapter-specific power policies and set them to maximum performance while testing.

Do the network reset before the driver reinstall if you haven't reinstalled yet — the reset can disturb driver bindings, and you want the fresh driver laid onto the clean configuration, not the other way around.

### Fix 6: Test with a USB Wi-Fi adapter

The definitive split test between internal-card fault and system fault.

1. Plug in any USB Wi-Fi adapter — even a cheap one.
2. If it works immediately, your USB subsystem and Windows network stack are fine; the fault is the internal card, its driver, or its slot.
3. If the USB adapter also fails to enumerate, the problem is system-wide — consider a Windows repair install.
4. A working USB adapter is also a perfectly good permanent workaround while you decide on repair.

This test costs almost nothing and answers the biggest question in the guide. Technicians do exactly this before opening a laptop — there's no reason you shouldn't too.

### Fix 7: Reseat or replace the internal card

When software is exhausted, it's hardware: reseat, then replace.

1. Run the manufacturer's built-in diagnostics first (F12 boot menu on Dell, UEFI diagnostics on HP/Lenovo) for a wireless card test.
2. If comfortable opening the machine: power off, disconnect battery, remove the bottom panel, and reseat the M.2 wireless card — release the screw, lift, reinsert firmly, re-screw.
3. Check the antenna leads (usually black/white wires) are snapped onto the card's terminals.
4. If reseating fails, replacement M.2 wireless cards are inexpensive and model-standard (Intel AX210 is a common upgrade) — but verify your laptop's BIOS doesn't whitelist cards.

The whitelist warning is real on some business laptops: certain BIOSes refuse to boot with non-approved wireless cards. Check your model's documentation before buying a replacement. And if the machine is under warranty, stop at the diagnostic step — opening it yourself can void coverage.

## Closing

A missing Wi-Fi adapter is an enumeration problem, and enumeration problems have a short list of causes: hidden by Windows, disabled in BIOS, stuck in a power state, driverless, or dead. The fixes above walk that list in order of likelihood and cost — most adapters reappear by Fix 4. If yours doesn't, the USB adapter test gives you both a diagnosis and a workaround in one move, which is more than most troubleshooting sequences offer.
