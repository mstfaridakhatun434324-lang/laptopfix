---
title: "How to Fix Wi-Fi 6 Not Working on a Laptop (Video Walkthrough)"
slug: how-to-fix-wifi-6-not-working-on-laptop-youtube
date: 2026-09-20
categories: ["drivers"]
tags: ["wifi 6 not working", "802.11ax", "intel ax201", "wifi speed slow", "wireless fix"]
description: "Wi-Fi 6 not working on your laptop — slow speeds or no 802.11ax connection? Fix driver, router, and band settings to unlock full Wi-Fi 6 performance."
thumbnail: "/images/thumbs/how-to-fix-wifi-6-not-working-on-laptop-youtube.webp"
faqs:
  - q: "How do I know if my laptop is actually using Wi-Fi 6?"
    a: "Open Settings > Network & internet > Wi-Fi, click your connected network, and read the Protocol field — it will say Wi-Fi 6 (802.11ax) when active. You can also run `netsh wlan show interfaces` in Command Prompt and check the 'Radio type' line. If it says 802.11ac or 802.11n despite Wi-Fi 6 hardware on both ends, work through the driver and router settings in this guide."
  - q: "Why is my Wi-Fi 6 slower than expected?"
    a: "Link rate is not throughput: real-world ax speeds depend on channel width (use 80/160MHz), distance, congestion, and the router's backhaul. Also verify you are on the 5GHz band — many 'slow Wi-Fi 6' complaints are laptops camped on 2.4GHz. Update both the laptop Wi-Fi driver and router firmware, disable adapter power saving, and test close to the router to isolate the bottleneck."
  - q: "Do I need a Wi-Fi 6 router to benefit from a Wi-Fi 6 laptop?"
    a: "For 802.11ax speeds, yes — both ends must support ax, otherwise they negotiate the best common standard (usually Wi-Fi 5/ac). However, a Wi-Fi 6 laptop on a Wi-Fi 5 router still benefits from the newer card's better drivers, power efficiency, and MU-MIMO client behavior. If you are buying a router, Wi-Fi 6 models are now the sensible default."
  - q: "What is the difference between Wi-Fi 6 and Wi-Fi 6E?"
    a: "Wi-Fi 6E extends Wi-Fi 6 into the 6GHz band, adding fresh uncongested spectrum with very high throughput at short range. It requires a 6E-capable card (Intel AX210/AX211, not the older AX200/AX201) and a 6E router. Standard Wi-Fi 6 operates on 2.4GHz and 5GHz. For most homes, 5GHz Wi-Fi 6 delivers the meaningful upgrade; 6E matters most in dense apartments and for multi-gigabit internet plans."
---

Wi-Fi 6 (802.11ax) promises faster speeds, better congestion handling, and lower latency — but many laptops with Wi-Fi 6 hardware never actually connect at 802.11ax rates. Instead they limp along on Wi-Fi 5 (802.11ac) or 2.4GHz-only connections, and owners assume the 'Wi-Fi 6 not working' problem is a broken adapter. Usually it is a configuration mismatch between the laptop, the driver, and the router.

The three sides must agree: the laptop needs a Wi-Fi 6-capable card (Intel AX200/AX201/AX210/AX211, MediaTek MT7921/7922, Qualcomm FastConnect), the driver must have 802.11ax mode enabled, and the router must broadcast Wi-Fi 6 on a band the laptop can use. A failure on any side silently downgrades the connection.

Start by confirming what you actually have: check the adapter model in Device Manager. Intel AX201 owners with outright failures should also read the [Intel Wi-Fi 6 AX201 repair guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/); if Wi-Fi is gone entirely, the [missing Wi-Fi guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) comes first.

## Why this happens

- **802.11ax mode disabled in driver settings** — The adapter's Advanced properties can have 802.11a/b/g or VHT mode forced, capping the connection below ax.
- **Router not broadcasting Wi-Fi 6** — The router's ax mode may be off, or the laptop connects to a 2.4GHz/legacy SSID.
- **Outdated Wi-Fi driver** — Early AX200/AX201 drivers had broken or incomplete 802.11ax support.
- **Router firmware bugs with ax clients** — Some routers mishandle ax handshakes and the laptop falls back to ac.
- **5GHz/6GHz band issues** — Wi-Fi 6E's 6GHz band needs specific driver and Windows support; region settings can disable it.
- **Power saving throttling the radio** — Aggressive power management disables ax features like MU-MIMO and 160MHz channels.
- **Channel width forced narrow** — A 20MHz-only channel width setting caps throughput regardless of the ax link.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the hardware and current link rate

Know what you have before changing anything. This baseline tells you whether ax is even possible.

1. In Device Manager > Network adapters, confirm the adapter model (AX200/AX201/AX210/AX211, MT7921/7922, etc.).
2. Connect to Wi-Fi, then open Settings > Network & internet > Wi-Fi > your network > Properties.
3. Check **Protocol** — it should read Wi-Fi 6 (802.11ax). Note the link speed.
4. In Command Prompt, `netsh wlan show interfaces` shows the radio type and channel — record these as your baseline.

### Fix 2: Enable 802.11ax in the adapter's Advanced settings

The driver can silently restrict the wireless mode. Forcing ax-capable modes unlocks the standard.

1. In Device Manager, right-click the Wi-Fi adapter > Properties > **Advanced** tab.
2. Find **802.11a/b/g Wireless Mode** or **Wireless Mode** and set it to **802.11ax** (or the highest ax-inclusive option).
3. Set **Preferred Band** to **5GHz** (or 6GHz for Wi-Fi 6E cards).
4. Set **Channel Width** (VHT/HT mode) to **Auto** or 160MHz/80MHz — not 20MHz only. Click OK and reconnect.

### Fix 3: Update the Wi-Fi driver

Wi-Fi 6 support matured enormously across driver generations; old drivers are a top cause of ax failures.

1. Download the latest driver for your exact laptop model from the maker's support site.
2. Intel card owners can use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for the newest generic driver.
3. In Device Manager, uninstall the old Wi-Fi driver (tick 'delete driver'), then install the fresh package.
4. Restart, reconnect, and recheck the protocol in Wi-Fi properties.

### Fix 4: Configure the router for Wi-Fi 6

The laptop cannot use ax if the router does not offer it properly. Check the other side of the link.

1. Log into the router admin page and confirm **802.11ax / Wi-Fi 6 mode** is enabled on the 5GHz band.
2. Set 5GHz channel width to **80MHz or 160MHz** (not 20/40MHz).
3. Update the router firmware — ax handshake bugs are frequently fixed in updates.
4. Disable 'smart connect' band-steering temporarily to test a dedicated 5GHz SSID.

### Fix 5: Disable power saving on the adapter

Power-saving features can disable the very ax enhancements (MU-MIMO, 160MHz) you are trying to use.

1. In Device Manager > Wi-Fi adapter > Properties > Power Management, uncheck power-saving.
2. On the Advanced tab, set **Power Saving Mode** to **Maximum Performance** and **MIMO Power Save Mode** to **No SMPS** (static).
3. In Windows power settings, set Wireless Adapter Settings to Maximum Performance.
4. Retest link rate and speed.

### Fix 6: Forget and rejoin the network cleanly

Stale network profiles can pin old capability negotiations. A fresh join renegotiates everything.

1. In Settings > Network & internet > Wi-Fi > Manage known networks, **Forget** the network.
2. Restart the laptop.
3. Reconnect from scratch, entering the password fresh.
4. Verify the protocol now reads Wi-Fi 6 and test throughput with a speed test near the router.

### Fix 7: Check 6GHz / Wi-Fi 6E specifics

For 6E cards, the 6GHz band has extra requirements that silently fail.

1. Confirm your card is actually 6E-capable (AX210/AX211, MT7922) — AX200/AX201 are Wi-Fi 6, not 6E.
2. Ensure Windows is fully updated; 6GHz support requires recent builds.
3. Check the router broadcasts a 6GHz SSID and that your region settings permit 6GHz (some regions restrict it).
4. If 6GHz will not come up, 5GHz ax still delivers the vast majority of Wi-Fi 6's real-world benefit.

## Closing

Wi-Fi 6 'not working' is almost always a negotiation failure, not broken hardware: the driver mode, the router's ax settings, or power management silently downgrading the link. Verify the protocol in Wi-Fi properties after each change — the moment it reads 802.11ax, you have found your fix, and the settings to protect are the driver's wireless mode and the router's channel width.
