---
title: "How to Fix MediaTek Wi-Fi Not Working"
slug: how-to-fix-mediatek-wifi-not-working
date: 2026-09-17
categories: ["drivers"]
tags: ["mediatek", "wifi", "mt7921", "driver"]
description: "MediaTek Wi-Fi dropping or not working on your laptop? Fix the MT7921/MT7922 driver issues with this targeted troubleshooting guide."
thumbnail: "/images/thumbs/how-to-fix-mediatek-wifi-not-working.webp"
faqs:
  - q: "Why is MediaTek Wi-Fi so problematic on Windows laptops?"
    a: "MediaTek Wi-Fi cards (especially the MT7921) have a history of driver immaturity on Windows compared to Intel's offerings. Common issues include connections dropping under load, the adapter vanishing after sleep, and Bluetooth interference. The good news is that recent driver versions from laptop manufacturers have fixed most of these problems — updating to the latest manufacturer driver is the single most effective step."
  - q: "Should I replace my MediaTek Wi-Fi card with an Intel one?"
    a: "It is a valid option on laptops where the card is a replaceable M.2 module and not whitelisted in the BIOS. An Intel AX210 costs relatively little and is famously stable. But try the driver fixes first — most MediaTek issues are software, and a $0 driver update beats a hardware swap. Check your warranty terms before opening the machine."
  - q: "Why does my MediaTek Wi-Fi disconnect when Bluetooth is on?"
    a: "MediaTek combo cards share the 2.4GHz radio between Wi-Fi and Bluetooth, and older drivers handled the coexistence poorly — Bluetooth activity could starve the Wi-Fi connection. Updating to the latest driver, which contains improved coexistence algorithms, usually fixes this. As a workaround, using 5GHz Wi-Fi avoids the shared 2.4GHz band entirely."
  - q: "My MediaTek adapter disappears after sleep — how do I fix it?"
    a: "This is the classic MT7921 power management bug. Disable 'Allow the computer to turn off this device to save power' on the adapter's Power Management tab in Device Manager, disable USB/PCIe selective suspend equivalents, and update to the latest driver. If it persists, disabling Fast Startup prevents the deep sleep states that trigger the disappearance."
---

MediaTek Wi-Fi cards — the MT7921 and MT7922 found in countless AMD-powered laptops — have a reputation. Dropped connections, vanishing adapters after sleep, Bluetooth interference, and speeds that never match the spec sheet. Some of this reputation is earned: early drivers were genuinely rough. But the situation today is much better than the horror stories suggest, and most MediaTek Wi-Fi problems yield to the same disciplined approach: update the driver properly, fix power management, and separate the 2.4GHz coexistence issues.

The critical detail with MediaTek cards is where you get the driver. Windows Update's generic MediaTek driver is the source of a large share of problems — the laptop manufacturer's version, tuned for your specific machine, is almost always better. This guide is MediaTek-specific throughout. For Intel Wi-Fi issues, see our [Intel AX201 fix guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/), and for adapters that vanish entirely, the [missing network adapter guide](/articles/troubleshoot-network-adapter-missing/).

## Why this happens

- **Immature or generic driver.** Windows Update installs a basic MediaTek driver lacking the manufacturer's stability fixes.
- **Aggressive power management.** The MT7921 is notorious for failing to wake from low-power states after sleep.
- **Bluetooth/Wi-Fi coexistence bugs.** The shared 2.4GHz radio gets starved by Bluetooth traffic on older drivers.
- **Roaming aggressiveness.** Overly eager roaming between access points causes drops on some networks.
- **Outdated card firmware.** The Wi-Fi card's own firmware (delivered via driver packages) can have bugs fixed in later releases.
- **Antenna connection issues.** The tiny M.2 antenna wires can loosen, devastating signal quality.
- **Router incompatibilities.** Certain router features (band steering, WPA3 transition modes) interact badly with MediaTek drivers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the manufacturer's MediaTek driver

The single highest-value step — do this first.

1. Identify your exact card in Device Manager (**Network adapters** — look for **MediaTek Wi-Fi 6 MT7921** or similar).
2. Go to your **laptop manufacturer's** support page and download the latest Wi-Fi driver for your exact model — for Dell, HP, or Lenovo machines start at [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/). Avoid MediaTek's generic package and Windows Update's version for this step.
3. In Device Manager, right-click the MediaTek adapter, choose **Uninstall device**, and check **Attempt to remove the driver** to purge the generic one.
4. Restart, then install the manufacturer's driver package. Test for a full day before judging — MediaTek issues are often intermittent.

### Fix 2: Disable power management on the adapter

Fix the classic disappear-after-sleep bug.

1. In Device Manager, right-click the MediaTek adapter, choose **Properties**, and open the **Power Management** tab.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. Open the **Advanced** tab and look for power-related properties (**Power Saving Mode**, **Sleep on WoWLAN Disconnect**) — set them to **Maximum Performance** or disabled.
4. Go to **Control Panel > Power Options > Change plan settings > Change advanced power settings**, expand **Wireless Adapter Settings > Power Saving Mode**, and set it to **Maximum Performance** on both battery and AC.

### Fix 3: Disable Fast Startup

Fast Startup's hybrid shutdown triggers the MT7921's worst behaviors.

1. Open **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**, then uncheck **Turn on fast startup**.
3. Shut down fully (not restart) and power back on. Test sleep/wake cycles over the next day.
4. If the adapter now survives sleep reliably, Fast Startup was contributing — leave it off; the boot-time cost on modern SSDs is negligible.

### Fix 4: Fix Bluetooth coexistence

For drops that coincide with Bluetooth use.

1. In the adapter's **Advanced** tab in Device Manager, look for **Bluetooth Collaboration**, **BT-AMP**, or coexistence settings and experiment with the available values.
2. The most reliable workaround: connect to your router's **5GHz** network instead of 2.4GHz, removing the shared-band contention entirely. Our [5GHz connection guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/) helps if the 5GHz network is not visible.
3. Update the **Bluetooth** driver from the laptop manufacturer as well — the combo card's Bluetooth driver participates in coexistence.
4. As a test, turn Bluetooth off completely for a day. If Wi-Fi stabilizes, coexistence is confirmed as the issue and the driver update is the real fix.

### Fix 5: Tune roaming and band preferences

Stop the card from hunting networks unnecessarily.

1. In the adapter's **Advanced** tab, find **Roaming Aggressiveness** and set it to **1. Lowest** if you stay near one access point — this stops drops caused by the card jumping between APs.
2. Find **Preferred Band** and set it to **5GHz** (or **6GHz** if your card and router support it) to keep the card off the congested 2.4GHz band.
3. Set **802.11a/b/g Wireless Mode** or **VHT Mode** according to your router's capabilities — forcing an incompatible mode causes exactly these symptoms.
4. After changing advanced settings, disable and re-enable the adapter for the changes to take effect.

### Fix 6: Address router-side incompatibilities

Sometimes the router and the card simply disagree.

1. Log into your router and try disabling **band steering** temporarily — some MediaTek drivers handle steering poorly.
2. If your router uses **WPA3** or WPA2/WPA3 transition mode, try pure **WPA2-AES** as a test. Revert if it makes no difference.
3. Try a different Wi-Fi channel, particularly on 2.4GHz — set it manually to 1, 6, or 11 rather than Auto.
4. Test the laptop on a completely different network (phone hotspot). If it is stable there, the issue is the specific router-card interaction, not the card alone.

### Fix 7: Consider the hardware options

When software is exhausted.

1. Check the antenna wires if you are comfortable opening the laptop — the MAIN and AUX wires on the M.2 card must be firmly connected. (Note their positions before touching anything.)
2. A BIOS update from the laptop manufacturer sometimes includes fixes for the M.2 slot's power delivery to the Wi-Fi card.
3. Replacing the MediaTek card with an Intel AX210 is a well-trodden upgrade path — verify your laptop does not BIOS-whitelist Wi-Fi cards (most modern consumer laptops do not) and that the card is socketed, not soldered.
4. A USB Wi-Fi adapter is the zero-disassembly fallback that bypasses the internal card entirely.

## Closing

MediaTek Wi-Fi on Windows is a driver story first and a hardware story distant second. The manufacturer's driver — not Windows Update's — plus tamed power management resolves the large majority of drops, disappearances, and Bluetooth conflicts. The MT7921's early reputation was earned by early drivers, but the current ones are substantially better, which means a card that misbehaves today is usually just running yesterday's software. Update it properly, calm the power settings, and give it a day of real-world testing before declaring the hardware guilty.
