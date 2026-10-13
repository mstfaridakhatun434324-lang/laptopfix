---
title: "How to Fix MediaTek WiFi Not Working on Windows 11"
slug: how-to-fix-mediatek-wifi-not-working-on-windows-11
date: 2026-10-09
categories: ["drivers"]
tags: ["mediatek wifi", "wifi not working", "windows 11", "mt7921", "wifi driver"]
description: "MediaTek WiFi not working on Windows 11? Fix dead wireless, Code 10 errors, and dropouts on MT7921/MT7922 cards with 7 proven repairs."
thumbnail: "/images/thumbs/how-to-fix-mediatek-wifi-not-working-on-windows-11.webp"
faqs:
  - q: "Why is my MediaTek WiFi adapter not working on Windows 11?"
    a: "MediaTek cards (MT7921, MT7922, MT7961) are notoriously sensitive to driver versions on Windows 11 — a Windows Update driver, a power-management conflict, or the card failing to initialize after sleep leaves it dead or throwing Code 10. The reliable fix is installing the driver from your laptop maker's support site (not Windows Update's), which is validated against your machine's firmware."
  - q: "What does Code 10 mean on a MediaTek WiFi adapter?"
    a: "Code 10 ('This device cannot start') means Windows loaded the driver but the hardware failed to initialize — on MediaTek cards this usually indicates a driver/firmware mismatch rather than dead hardware. Reinstalling the manufacturer's driver package, disabling fast startup, and power-cycling the machine resolve most Code 10 cases. Only suspect the card itself if Code 10 survives a clean driver install and a BIOS update."
  - q: "Should I replace my MediaTek WiFi card with an Intel one?"
    a: "Many technicians do exactly that — the Intel AX210 is a popular, inexpensive upgrade for laptops with a replaceable M.2 WiFi card, and it ends MediaTek driver drama permanently. Check that your laptop's card isn't soldered and that the BIOS doesn't whitelist cards (rare on modern consumer laptops). If the card is soldered, the driver fixes below are your path."
  - q: "Why does MediaTek WiFi die after sleep on Windows 11?"
    a: "The card fails to reinitialize when Windows' power management cuts its power during sleep — a firmware/driver handshake bug specific to certain MediaTek driver builds. Disabling 'Allow the computer to turn off this device' on the adapter and disabling USB-style selective suspend for the wireless card are the standard workarounds, along with installing the laptop maker's latest driver."
---

MediaTek WiFi cards — the MT7921, MT7922, and MT7961 found in countless budget and mid-range Windows 11 laptops — have earned a reputation. They work fine until a Windows update, a sleep cycle, or a driver refresh leaves them dead, throwing Code 10 in Device Manager, or vanishing from the network list entirely. The hardware is usually fine; the driver and firmware dance around it is what's fragile.

This guide is MediaTek-specific: the driver sources that actually work, the power settings that kill these cards, and the Code 10 sequence. If your card is soldered (most thin-and-lights), these software fixes are the whole game.

## Why this happens

- **Windows Update driver mismatch.** Microsoft's MediaTek driver build conflicting with the laptop's firmware.
- **Power management killing the card.** The adapter failing to reinitialize after sleep or idle power-down.
- **Code 10 initialization failure.** Driver loads but the hardware won't start — usually a version mismatch.
- **Fast Startup stale state.** Hybrid boot resuming the card in a wedged state.
- **Corrupt driver installation.** Partial update leaving mixed driver files.
- **BIOS/firmware too old.** The card's firmware expecting a newer platform initialization.
- **Failing M.2 card.** Genuine hardware failure — uncommon but real on these cards.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Power-cycle and check the adapter's state

Start by establishing exactly what state the card is in.

1. Open **Device Manager > Network adapters** — look for **MediaTek Wi-Fi** (MT7921/MT7922/MT7961).
2. Note the symptom precisely: **missing entirely**, **yellow warning (Code 10)**, or **present but no networks**.
3. Do a full shutdown — hold **Shift** while clicking **Shut down** to bypass Fast Startup — wait 30 seconds, power on.
4. If the card reappears after a cold boot but dies after sleep, it's the power-management issue — jump to Fix 4 after completing Fix 3.
5. Check **Settings > Network & internet** — if Wi-Fi is missing as a category, Windows isn't seeing the adapter at all.

### Fix 2: Run the network troubleshooter

The quick automated pass before driver surgery.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters > Network and Internet > Run**.
2. Let it complete — it resets the adapter and the TCP/IP stack, which fixes simple wedged states.
3. Restart after it finishes, even if it claims nothing was wrong.
4. If it reports the adapter has a driver problem, that's confirmation for Fix 3.
5. Microsoft's network troubleshooting reference is on [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 3: Install the laptop maker's MediaTek driver

The central fix — the manufacturer's validated driver, not Windows Update's.

1. Go to your **laptop maker's support site** (ASUS, Acer, Lenovo, MSI) and download the **Wi-Fi/MediaTek driver** for your exact model and Windows 11.
2. In **Device Manager**, right-click the MediaTek adapter, choose **Uninstall device**, and check **Attempt to remove the driver for this device**.
3. Restart — then install the downloaded maker driver **before** reconnecting to the internet if possible (stops Windows grabbing its own first).
4. Restart again after installation and verify the driver date in **Properties > Driver**.
5. If the maker's driver is older than what Windows offered, install the maker's anyway — validated beats newer for MediaTek cards.

### Fix 4: Disable power management on the adapter

The classic MediaTek sleep-death workaround.

1. In **Device Manager**, right-click the MediaTek adapter > **Properties > Power Management** tab.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. Go to **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
4. Expand **Wireless Adapter Settings > Power Saving Mode** and set both **On battery** and **Plugged in** to **Maximum Performance**.
5. Disable **Fast Startup** (Power Options > Choose what the power buttons do) — hybrid boot wedges these cards.

### Fix 5: Reset the network stack

When the driver is fine but Windows' networking is corrupt around it.

1. Open **Command Prompt as administrator**.
2. Run, in order: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
3. Restart the laptop.
4. Alternatively: **Settings > Network & internet > Advanced network settings > Network reset** — this reinstalls all adapters and resets everything to defaults (you'll re-enter Wi-Fi passwords).
5. Test with the laptop close to the router first — rule out signal issues before blaming the stack.

### Fix 6: Update the BIOS and try a newer MediaTek driver

Firmware and newer driver builds for stubborn cases.

1. Check your laptop maker's site for a **BIOS update** — changelogs mentioning Wi-Fi, MT7921, or connectivity are directly relevant.
2. Install on AC power, then retest the card's behavior after sleep specifically.
3. If the maker's driver still misbehaves, try the newer driver from **MediaTek's** or **Microsoft Update Catalog** ([catalog.update.microsoft.com](https://www.catalog.update.microsoft.com/)) — search for your card model (MT7921/MT7922) and pick a recent build.
4. Install via **Device Manager > Update driver > Browse my computer** pointing at the extracted catalog files.
5. If a catalog driver fixes it, consider blocking Windows Update from replacing it (Show or hide updates troubleshooter).

When Wi-Fi disappears from Windows entirely, the broader guide helps: [WiFi disappeared on Windows 11 — no WiFi option](/articles/wifi-disappeared-windows-11-no-wifi-option/).

### Fix 7: Code 10 deep fix and the hardware verdict

For the persistent "device cannot start" case.

1. In **Device Manager**, open the adapter's **Properties > General** and confirm it's **Code 10** (not Code 43 or 45 — different fixes).
2. Uninstall with **driver deletion checked**, shut down fully, unplug AC, hold power 15 seconds, then boot and install the maker driver — the full power-cycle clears wedged firmware state.
3. Try the card in a different OS state: a **Linux live USB** — working Wi-Fi there proves the hardware is fine and it's purely a Windows driver problem.
4. If the card is a replaceable **M.2 module** (check your model's service manual), an **Intel AX210** (~$20) is the popular permanent fix — but verify the card isn't soldered first.
5. For 5GHz-specific connection failures rather than a dead adapter, see [how to fix laptop not connecting to WiFi 5GHz in Windows 11 24H2](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/).

## Closing

MediaTek WiFi on Windows 11 is a driver-management problem more than a hardware problem: get the laptop maker's validated driver installed, stop Windows Update from replacing it, and disable the power-management features that wedge the card after sleep. That trio resolves the overwhelming majority of dead-or-Code-10 MediaTek adapters.
