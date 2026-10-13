---
title: "Bluetooth Not Working on an HP Laptop? Fix It Here"
slug: how-to-fix-bluetooth-not-working-on-hp-laptop
date: 2026-09-12
categories: ["drivers"]
tags: ["bluetooth", "hp laptop", "wireless", "device manager"]
description: "Bluetooth dead or missing on your HP laptop? HP-specific fixes from the wireless toggle to the driver stack."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why is Bluetooth missing entirely from my HP laptop's settings?"
    a: "When Bluetooth vanishes from Settings, the radio is usually disabled below Windows or its driver failed to load. On HPs the prime suspects are the airplane-mode/Fn wireless toggle, the BIOS wireless setting, and a Windows update that replaced HP's Bluetooth driver. Check Device Manager for the Bluetooth section — its presence or absence tells you which layer failed."
  - q: "My HP Bluetooth turns on but won't find any devices. What's wrong?"
    a: "The radio works but discovery is blocked — usually because the target device isn't in pairing mode (the most common real cause), Windows' Bluetooth Support Service is stuck, or a corrupted pairing cache is interfering. Put the accessory in pairing mode first, restart the Bluetooth services, and remove old pairings before assuming a driver problem."
  - q: "Should I download Bluetooth drivers from HP or Intel/Realtek?"
    a: "From HP for your exact model. HP validates the Bluetooth driver against the specific wireless card and antenna configuration in your laptop, and bundles it correctly with the Wi-Fi driver (they're usually one package). The chip vendor's generic driver sometimes works but can break HP-specific features like the wireless toggle integration."
  - q: "Does airplane mode on HP laptops disable Bluetooth separately?"
    a: "Airplane mode disables all radios including Bluetooth, and on some HP models the Fn wireless key toggles a hardware-level radio kill that persists until pressed again. If Bluetooth died after you hit the airplane-mode key accidentally, press it again and then verify in Settings that Bluetooth is actually back on — the two states can desync."
---

HP laptops have their own particular Bluetooth personality: the wireless toggle key, HP's BIOS wireless settings, and the combined Wi-Fi/Bluetooth driver packages all interact in ways that produce HP-specific failure modes. The generic Bluetooth advice still applies, but the HP layer on top is where most HP Bluetooth deaths actually happen — a radio killed by the Fn key, a BIOS toggle flipped by a firmware update, or HP's driver replaced by Windows' generic one.

This guide works the HP stack specifically: the physical and firmware radio controls first (because they're instant to check), then Windows' Bluetooth services and pairing state, then the driver layer with HP's own packages, and finally the hardware verdict. For Bluetooth that vanished from Device Manager entirely after an update, the [Bluetooth disappearance walkthrough](/articles/bluetooth-disappeared-from-device-manager-troubleshooting/) goes deeper on that specific symptom.

## Why this happens

- **The wireless radio is killed at the Fn key or airplane mode.** HP's wireless toggle (often **Fn + F12** or a dedicated key) cuts Bluetooth at a level Windows can't override — and it's easy to hit accidentally.
- **Bluetooth is disabled in BIOS.** HP BIOS/UEFI exposes wireless device toggles; firmware updates can flip Bluetooth off while leaving Wi-Fi on.
- **Windows Update replaced HP's Bluetooth driver.** The generic driver may load but fail to operate HP's specific wireless card correctly — present in Device Manager, dead in practice.
- **The Bluetooth Support Service is stuck.** Windows' Bluetooth stack depends on background services; when they wedge, the toggle spins forever or devices won't pair.
- **The pairing cache corrupted.** Stale or conflicting pairings block new connections and can make the whole Bluetooth UI misbehave.
- **Power management suspended the radio.** The Bluetooth module shares the wireless card; aggressive power saving kills it after sleep.
- **The wireless card itself failed.** Wi-Fi and Bluetooth usually share one card — if Wi-Fi also died simultaneously, suspect the card or its antenna connections.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the HP wireless toggle and airplane mode

The instant HP-specific check. Do this before anything else.

1. Look for the **wireless/airplane-mode key** on your HP — usually **Fn + F12** or a dedicated key with an antenna icon. Press it once and watch for the on-screen indicator.
2. Check the LED if your model has one (amber = radios off, white/blue = on). Toggle until it shows radios on.
3. Open **Settings > Network & internet** and confirm **Airplane mode** is **Off**, then check **Settings > Bluetooth & devices** for the Bluetooth toggle.
4. If the Fn key does nothing, HP's hotkey software may be broken — the software toggles in Settings still work independently, so continue with those.

### Fix 2: Verify Bluetooth is enabled in BIOS

When the radio is dead at every software level.

1. Restart and press **Esc** (then **F10**) at the HP logo to enter BIOS setup.
2. Navigate to **Advanced > Built-in Device Options** (path varies by model) and find the **Bluetooth** or **Wireless** device toggles.
3. Ensure Bluetooth is **Enabled** — some HP BIOSes have separate toggles for WLAN and Bluetooth, and updates can flip just one.
4. Save and exit, boot into Windows, and check **Device Manager** for the reappearance of the **Bluetooth** section.

### Fix 3: Restart the Bluetooth services

For toggles that won't stay on and pairing that hangs.

1. Press **Win + R**, type `services.msc`, and find **Bluetooth Audio Gateway Service**, **Bluetooth Support Service**, and **Bluetooth User Support Service**.
2. Right-click each > **Restart**; set **Startup type** to **Automatic** (or **Manual** for the user service, per its default — just ensure it's running).
3. Toggle Bluetooth off and on in **Settings > Bluetooth & devices** after the restart.
4. Try pairing again. If services were the issue, discovery and pairing now proceed normally.

### Fix 4: Clear the pairing cache and re-pair cleanly

Stale pairings are a notorious source of "won't connect" on HPs.

1. Go to **Settings > Bluetooth & devices > Devices** — remove (trash icon) every Bluetooth device, especially the one failing to connect.
2. Put the accessory into **pairing mode** properly — most need a long-press until an LED blinks rapidly; "turned on" is not "pairing mode," and this distinction resolves a huge share of discovery failures.
3. Click **Add device > Bluetooth** in Windows and select the accessory when it appears. Keep the devices within a meter during pairing.
4. If pairing fails repeatedly, restart the laptop with all Bluetooth devices removed, then pair exactly one device first — a corrupted multi-device cache sometimes needs the clean slate.

### Fix 5: Reinstall HP's wireless driver package

The anchor fix — HP's validated Wi-Fi/Bluetooth combo driver.

1. Go to [HP Support](https://support.hp.com/us-en), enter your model or serial number, and download the **Wireless/Bluetooth driver** for Windows 10/11 — on most HPs this is a single Intel, Realtek, or MediaTek package covering both radios.
2. In **Device Manager**, expand **Bluetooth** — right-click the Bluetooth adapter (e.g., *Intel Wireless Bluetooth*) > **Uninstall device**, checking *Attempt to remove the driver*.
3. Also check **Network adapters** for the Wi-Fi card — uninstall its driver too, since the combo package replaces both.
4. Run HP's installer as administrator, reboot, and verify: Bluetooth section present in Device Manager, toggle responsive in Settings, and the wireless Fn key working again.

### Fix 6: Disable power management on the wireless card

For Bluetooth that dies after sleep or on battery.

1. In **Device Manager > Network adapters**, right-click the Wi-Fi/Bluetooth combo card > **Properties > Power Management** > uncheck *Allow the computer to turn off this device to save power*.
2. In **Settings > System > Power & battery**, avoid the most aggressive battery-saver modes while testing — they throttle the radio regardless of the Device Manager setting.
3. Test specifically across sleep/wake cycles: pair a device, sleep the laptop, wake it, and confirm the connection resumes.
4. If Bluetooth and Wi-Fi both die together after sleep, the whole wireless card is being powered down — the same power-management fix covers both, which is a useful diagnostic confirmation in itself. Our general [Bluetooth fix guide](/articles/bluetooth-not-working-on-windows-11-laptop-fix/) covers additional radio-level steps.

### Fix 7: Test the wireless card hardware

The final verdict when software is exhausted.

1. Note the failure pattern: **Bluetooth dead + Wi-Fi dead** simultaneously = the combo wireless card, its slot, or its antenna leads. **Bluetooth dead + Wi-Fi fine** = more likely driver/software, since the card's radio section is shared.
2. Boot a **Linux live USB** — if Bluetooth works there, the hardware is fine and the problem is Windows software (revisit Fix 5 with a driver-store cleanup).
3. Reseating the wireless card (usually under a bottom-panel hatch, two antenna wires + one screw) fixes connection-related failures — but only attempt this if you're comfortable inside the laptop; the antenna connectors are fragile.
4. Replacement wireless cards are $15–25 and a straightforward DIY on most HPs — or a USB Bluetooth adapter ($10–15) bypasses the internal radio entirely with zero disassembly. HP's [official support site](https://support.hp.com/us-en) has the service manual for your model if you go the replacement route.

## Closing

HP Bluetooth failures live in the HP layer more often than not: the wireless toggle key, the BIOS radio setting, and HP's combo driver package. Check the radio controls first — they're instant — then restart the Bluetooth services, clear the pairing cache, and reinstall HP's driver as the anchor fix. The radio you thought was dead was usually just switched off, stuck, or mis-driven.
