---
title: "What to Do If Bluetooth Disappeared From Device Manager"
slug: what-to-do-if-bluetooth-disappeared-from-device-manager
date: 2026-10-01
categories: ["drivers"]
tags: ["bluetooth", "device manager", "bluetooth missing", "wireless"]
description: "Bluetooth vanished from Device Manager? Diagnose driver, BIOS, and hardware causes and restore Bluetooth on your Windows laptop."
thumbnail: "/images/thumbs/what-to-do-if-bluetooth-disappeared-from-device-manager.webp"
faqs:
  - q: "Why is there no Bluetooth section at all in my Device Manager?"
    a: "When the entire Bluetooth category is missing, Windows cannot see the Bluetooth radio hardware. The usual causes are a failed Bluetooth driver, the radio disabled in BIOS or by a hardware switch, power management trapping the device, or the wireless card itself failing. Showing hidden devices first tells you whether it is disabled or truly undetected."
  - q: "Can a Windows update delete my Bluetooth adapter?"
    a: "It cannot delete hardware, but it can install a broken Bluetooth driver that fails to start, which makes the adapter disappear from the normal Device Manager view. Rolling back the driver or installing the manufacturer's version restores it. This pattern is extremely common after major Windows updates."
  - q: "Is Bluetooth on the same card as WiFi in laptops?"
    a: "On most modern laptops, yes — Bluetooth and WiFi share one M.2 wireless card, typically from Intel, Realtek, or MediaTek. If WiFi works but Bluetooth is missing, the card is probably fine and the Bluetooth USB interface or its driver is the problem. If both are gone, suspect the card, its slot, or BIOS."
  - q: "Should I buy a USB Bluetooth adapter?"
    a: "A USB Bluetooth 5.x adapter is a cheap, reliable workaround and a useful diagnostic tool: if it works, your OS Bluetooth stack is fine and the internal radio is the problem. But try the driver and BIOS fixes first — most missing-Bluetooth cases are software and take minutes to fix."
---

Bluetooth disappearing from Device Manager entirely — not disabled, not error-flagged, just gone, with no Bluetooth category and no Bluetooth toggle in Settings — is disorienting because there is nothing obvious to right-click and fix. But the absence itself is diagnostic information. It means Windows cannot enumerate the Bluetooth radio, and the reasons for that form a short, testable list.

The most useful first question is whether WiFi still works. On nearly all current laptops, Bluetooth rides on the same physical wireless card as WiFi. WiFi working plus Bluetooth missing narrows the fault to the Bluetooth driver or its USB interface; both missing points at the card, BIOS, or a hardware switch. Keep that split in mind as you work through the fixes.
Here's the detail that makes Bluetooth disappearance diagnosable: on nearly all modern laptops, Bluetooth and WiFi share one physical M.2 card, with Bluetooth carried over an internal USB connection while WiFi uses PCIe. That split is why WiFi can work perfectly while Bluetooth vanishes — the USB side of the card, its driver, or its power state failed independently. Every fix below exploits that split to narrow the fault.

## Why this happens

- **Broken Bluetooth driver after an update:** A mismatched or corrupted Bluetooth driver fails to start, and Windows hides the non-starting device from the default view.
- **Radio disabled in BIOS:** Some BIOS setups have a separate Bluetooth toggle; updates can reset it to disabled.
- **Airplane mode or hardware switch latched:** A stuck Fn airplane-mode key or physical wireless switch can gate the Bluetooth radio off below the OS.
- **Power management trapping the USB interface:** Bluetooth typically connects via internal USB, and selective suspend can leave it in an unrecoverable sleep state.
- **Wireless card partially failed:** The WiFi side can survive while the Bluetooth USB interface on the same card dies.
- **Card loose in its slot:** A shifted M.2 card can lose the USB lines Bluetooth needs while keeping the PCIe lines WiFi uses.
- **Bluetooth Support Service disabled:** If the service is stopped and set to manual or disabled, the stack never initializes even with good hardware.
- **Corrupt Bluetooth pairing database:** Rare as a cause of total disappearance, but a damaged device database can block enumeration on some stacks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices and check WiFi status

1. Open **Device Manager → View → Show hidden devices** and look for a **Bluetooth** category or grayed-out Bluetooth entries.
2. A grayed-out entry means the device is present but disabled — right-click → **Enable device** may end the whole saga.
3. Note whether WiFi works. WiFi fine plus Bluetooth missing means driver/USB-interface trouble; both missing means card/BIOS trouble. The WiFi side has its own recovery path in our [missing WiFi adapter guide](/articles/how-to-fix-wifi-adapter-not-showing-up-on-lenovo-laptop/).
4. Check **Settings → Bluetooth & devices** — if the Bluetooth toggle itself is absent, that confirms the radio is not enumerating.

### Fix 2: Toggle airplane mode and check hardware switches

1. Press the airplane-mode Fn key (often **Fn + F2** or a dedicated key) twice — on, wait five seconds, off — to unlatch a stuck radio state.
2. Check for a physical wireless switch on the laptop's side or front edge and make sure it is on.
3. In **Settings → Network & internet → Airplane mode**, toggle it off and on once more from software.
4. Recheck Device Manager with hidden devices shown. A latched radio is the simplest cause and the most embarrassing to miss.

### Fix 3: Restart the Bluetooth services

1. Press **Win + R**, type `services.msc`, and open the Services console.
2. Find **Bluetooth Audio Gateway Service**, **Bluetooth Support Service**, and **Bluetooth User Support Service**.
3. Set each to **Automatic** startup, then right-click → **Restart** (or **Start** if stopped).
4. Also confirm **Device Association Service** is running — Bluetooth pairing depends on it.

### Fix 4: Reinstall the Bluetooth driver from the manufacturer

1. Download the Bluetooth driver for your exact model from your laptop maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. In Device Manager (hidden devices shown), uninstall any grayed-out Bluetooth entries, ticking driver removal if offered.
3. Install the manufacturer's package and restart.
4. If no Bluetooth entry exists even hidden, install the maker's full wireless/WiFi driver package instead — on combo cards, the Bluetooth driver often ships inside it.
5. When Bluetooth audio specifically stutters after the radio returns, the broader [Bluetooth troubleshooting guide](/articles/bluetooth-not-working-on-windows-11-laptop-fix/) covers audio-profile issues that live above the driver layer.

### Fix 5: Disable power management on the Bluetooth radio and USB hubs

1. If the Bluetooth entry reappears, open its **Properties → Power Management** and uncheck **Allow the computer to turn off this device to save power**.
2. Expand **Universal Serial Bus controllers**, and for each **USB Root Hub**, uncheck the same power-saving option.
3. In **Power Options → Advanced → USB settings**, disable **USB selective suspend**.
4. Restart and confirm Bluetooth survives sleep-wake cycles.
5. If the radio vanishes only on battery power, your power plan is the culprit rather than the driver — create a custom plan with USB selective suspend disabled and wireless adapter power at maximum performance, and use it as your battery plan.

### Fix 6: Check the BIOS Bluetooth setting

1. Enter the BIOS on restart and look under **Security → I/O Port Access**, **Advanced → Wireless**, or similar for a **Bluetooth** toggle.
2. Make sure it is **Enabled** — some BIOS updates reset it.
3. Save, exit, and recheck Windows. A BIOS-disabled radio is invisible to every software fix, so verify this before opening the chassis.
4. While in the BIOS, confirm the wireless LAN setting is enabled too, since the combo card needs both.

### Fix 7: Reseat the wireless card or use a USB adapter

1. If both WiFi and Bluetooth are missing, power off, open the back panel, and reseat the M.2 wireless card, checking both antenna wires.
2. If only Bluetooth is missing and everything software has failed, the card's Bluetooth interface is likely dead — replace the card with an identical model.
3. As a workaround or permanent fix, a USB Bluetooth 5.x adapter restores full Bluetooth functionality for a few dollars with no disassembly.
4. After any hardware change, reinstall the manufacturer's wireless driver package to bind both radios cleanly.

## Closing

Bluetooth that vanishes from Device Manager is a driver, service, or BIOS problem in the great majority of cases — the radio hardware is usually fine. Work the list in order: reveal hidden devices, unlatch airplane mode, restart services, reinstall the maker's driver, fix power management, and check the BIOS. The hardware steps at the end are there for the stubborn remainder, and a USB adapter is always a valid exit ramp.
