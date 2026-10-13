---
title: "How to Fix a Missing Network Adapter in Windows"
slug: how-do-i-fix-network-adapter-missing
date: 2026-09-23
categories: ["drivers"]
tags: ["network adapter", "missing", "wifi", "ethernet"]
description: "Network adapter disappeared from Windows? Follow this fix guide covering BIOS, power states, drivers, and hardware isolation."
thumbnail: "/images/thumbs/how-do-i-fix-network-adapter-missing.webp"
faqs:
  - q: "Where did my network adapter go in Device Manager?"
    a: "It hasn't gone anywhere physically — Windows has simply stopped enumerating it. The usual reasons are a BIOS toggle disabling the device, a deep power state hiding it, a corrupted driver failing enumeration, or a stuck airplane mode state. Each has a distinct fix, which is why the troubleshooting order matters: check BIOS and power states before assuming the hardware failed."
  - q: "Why is my Ethernet adapter missing but Wi-Fi works?"
    a: "The two adapters are independent devices with independent drivers and BIOS toggles. A missing Ethernet adapter while Wi-Fi works points at the Ethernet-specific driver, its BIOS toggle, or the physical port — not a system-wide network failure. Reinstall the Ethernet driver from the laptop manufacturer's support page and check the BIOS for a LAN toggle."
  - q: "Can I get online at all with no network adapter?"
    a: "Yes — a USB Wi-Fi or USB Ethernet adapter bypasses the internal hardware entirely and gets you online in minutes. This is also a valuable diagnostic: if the USB adapter works, your Windows network stack is healthy and the problem is isolated to the internal adapter's driver, firmware, or hardware."
  - q: "How do I know if the missing adapter is a hardware failure?"
    a: "The strongest test is the BIOS: if the adapter (or its wireless/LAN toggle) doesn't appear in the BIOS either, and a full power drain plus BIOS defaults don't bring it back, hardware failure becomes likely. A second strong test is a USB adapter working fine — that proves Windows networking is healthy and isolates the fault to the internal device."
---

A network adapter that has vanished from Device Manager is Windows' way of saying it cannot see the hardware — and the causes split neatly into firmware, power, driver, and hardware layers. This guide is the practical companion to the broader troubleshooting walkthrough: same diagnostic logic, but organized as direct fix actions you can work through in one sitting. If you have not yet confirmed the adapter is truly missing (versus error-flagged), start with our [network adapter missing troubleshooting guide](/articles/troubleshoot-network-adapter-missing/) for the diagnostic framing.

One clarification before you begin: "network adapter" covers both Wi-Fi and Ethernet, and they fail independently. Note which one is missing — or whether both are gone, which points at a system-level cause like a BIOS setting or a power state rather than a single device driver. For Wi-Fi-specific disappearance, the [Wi-Fi adapter not showing up guide](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/) has model-specific steps.

## Why this happens

- **Disabled in BIOS/UEFI.** Wireless and LAN toggles in firmware override everything in Windows.
- **Deep power state lockup.** Fast Startup and hibernate can hide the adapter across reboots.
- **Corrupted driver blocking enumeration.** A badly broken driver can fail before Windows ever lists the device.
- **Stuck airplane mode.** A wedged radio state can suppress the Wi-Fi adapter's appearance.
- **Windows Update driver mismatch.** An incompatible driver that cannot initialize the hardware.
- **Physical switch or Fn key.** Hardware wireless switches electrically disconnect the radio.
- **Failed adapter hardware.** The M.2 Wi-Fi card or Ethernet controller can fail electrically.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices and check the physical switches

Start with visibility.

1. Open Device Manager, click **View > Show hidden devices**, and expand **Network adapters**. A greyed-out adapter is known-but-disconnected — uninstall it and restart.
2. Check for a physical Wi-Fi switch on the laptop's edges and an **Fn + F-key** wireless toggle — flip both and recheck.
3. Open **Settings > Network & internet** and verify **Airplane mode** is off and stays off. A stuck toggle needs our [airplane mode stuck guide](/articles/how-to-fix-airplane-mode-stuck-on-in-windows-11-24h2/).
4. For missing Ethernet specifically, inspect the port for bent pins or debris, and try a different cable.

### Fix 2: Do a complete power drain

Clear the hidden power states.

1. Shut down fully — not sleep, not hibernate.
2. Unplug the charger and all USB devices; remove the battery if removable.
3. Hold the power button for **30 seconds** to drain residual charge.
4. Reconnect only the charger and boot. Check Device Manager immediately — adapters freed from stuck power states reappear here.

### Fix 3: Enable the adapter in BIOS

Firmware toggles beat Windows every time.

1. Enter the BIOS (**F2**, **F10**, **Delete**, or **Esc**).
2. Find **Wireless/WLAN** and **LAN/Ethernet** toggles under Advanced, Security, or Device Configuration — set the missing one to **Enabled**.
3. If you changed nothing (it was already enabled), choose **Load Optimized Defaults** or **Reset to Default** — a corrupted BIOS setting can hide a device even when the toggle looks right.
4. Save, exit, and recheck Device Manager.

### Fix 4: Force redetection and clean-install the driver

Make Windows see the hardware again.

1. In Device Manager, click **Action > Scan for hardware changes**.
2. If the adapter appears with an error, right-click it, **Uninstall device** with **Attempt to remove the driver** checked, then restart.
3. Install the driver from the laptop manufacturer's support page for your exact model — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/). For Intel Wi-Fi, [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) works too.
4. After installation, verify the adapter appears under Network adapters without warnings and that networks are visible.

### Fix 5: Reset the network stack completely

Clear corrupted network state.

1. Open an elevated terminal and run: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /flushdns` — one at a time.
2. Go to **Settings > Network & internet > Advanced network settings > Network reset** and click **Reset now**.
3. Let the laptop restart, then reinstall the manufacturer's adapter driver before letting Windows Update choose one.
4. Recheck Device Manager and test connectivity before changing anything else.

### Fix 6: Disable Fast Startup and adapter power management

Prevent the hiding from recurring.

1. **Control Panel > Power Options > Choose what the power buttons do** — uncheck **Turn on fast startup** (after clicking **Change settings that are currently unavailable**).
2. In Device Manager, open the adapter's **Properties > Power Management** and uncheck **Allow the computer to turn off this device to save power**.
3. Set **Wireless Adapter Settings > Power Saving Mode** to **Maximum Performance** in the advanced power plan settings.
4. Shut down fully, wait 30 seconds, power on, and confirm the adapter survives the cold boot.

### Fix 7: Isolate the hardware with a USB adapter

The final verdict.

1. Connect a USB Wi-Fi or USB Ethernet adapter. If it works immediately, Windows networking is healthy and the internal adapter is the isolated fault.
2. If comfortable and out of warranty, reseat the M.2 Wi-Fi card (noting antenna wire positions) — loose cards cause exactly this symptom.
3. Check for a BIOS update from the manufacturer; some updates fix adapter enumeration on specific models.
4. If the internal adapter stays invisible across BIOS defaults, power drains, and driver purges, it has likely failed electrically — the USB adapter is a legitimate permanent fix, far cheaper than a motherboard repair.

## Closing

Missing adapters are found, not fixed, in the early steps: the hidden-devices view, the power drain, and the BIOS check recover a large share before any driver work begins. That ordering is deliberate — drivers cannot fix a device the firmware has hidden or a power state has trapped. When the adapter does reappear, note which step did it, because that step named your cause: a BIOS toggle means firmware, a power drain means a stuck state, a driver purge means software. And when nothing brings it back, the USB adapter test gives you both a diagnosis and a working internet connection in the same five minutes.
