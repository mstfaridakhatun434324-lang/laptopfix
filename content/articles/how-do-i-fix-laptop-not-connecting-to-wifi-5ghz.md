---
title: "How Do I Fix a Laptop Not Connecting to Wi-Fi 5GHz?"
slug: how-do-i-fix-laptop-not-connecting-to-wifi-5ghz
date: 2026-09-30
categories: ["drivers"]
tags: ["wifi 5ghz not connecting", "5ghz wifi missing", "dual band wifi", "wireless fix", "wifi driver"]
description: "Laptop not connecting to Wi-Fi 5GHz — only seeing 2.4GHz? Fix band settings, driver preferred-band options, and router configuration step by step."
thumbnail: "/images/thumbs/how-do-i-fix-laptop-not-connecting-to-wifi-5ghz.webp"
faqs:
  - q: "Why can my phone see 5GHz but my laptop cannot?"
    a: "Phones have newer, more tolerant Wi-Fi chips and aggressive band preference. Laptops fail where phones succeed usually because the laptop's driver has Preferred Band set to 2.4GHz, the driver is too old to handle the router's DFS channel or 160MHz width, or power saving has parked the 5GHz radio. The phone working proves the router's 5GHz is fine — the fix is entirely laptop-side."
  - q: "Is 5GHz always better than 2.4GHz?"
    a: "For speed, yes — 5GHz offers far more throughput and less congestion. For range and wall penetration, no — 2.4GHz reaches farther. Use 5GHz when within good range of the router (same room or adjacent), and let the laptop fall back to 2.4GHz at distance. That is exactly what the 'Prefer 5GHz' driver setting does: prefer the fast band, tolerate the far one."
  - q: "What are DFS channels and why do they break 5GHz?"
    a: "DFS (Dynamic Frequency Selection) channels are 5GHz frequencies shared with weather radar; routers must vacate them if radar is detected. Some laptop Wi-Fi drivers handle DFS poorly — failing to connect, dropping, or never seeing the SSID. If your router auto-selected a DFS channel (52–144), switching to a non-DFS channel (36–48) often fixes stubborn laptop 5GHz problems instantly."
  - q: "Will a USB Wi-Fi adapter fix 5GHz problems?"
    a: "It bypasses them: a modern USB Wi-Fi 6 adapter with its own current driver sidesteps the internal card's driver and band issues entirely. It is a pragmatic fix for older laptops whose makers stopped updating Wi-Fi drivers. Downsides: it occupies a USB port, sticks out of the machine, and cannot match a good internal card's antenna performance — but for reviving 5GHz on an old laptop, it works reliably."
---

When a laptop sees the 2.4GHz network fine but the 5GHz band is missing or refuses to connect, the cause is almost never the router being broken — your phone probably sees 5GHz without trouble. The fault lies in the laptop's wireless configuration: the driver preferring 2.4GHz, the 5GHz radio effectively disabled in settings, an outdated driver, or the router's 5GHz settings using parameters the laptop's card cannot handle.

Note the important distinction: 5GHz is a frequency band, not a speed tier — and it is not '5G' cellular. A laptop connecting only to 2.4GHz gets longer range but much lower throughput and worse congestion. Fixing 5GHz is usually worth it for any laptop used within normal home range of the router.

Start with the laptop side (this guide), then check the router. If Wi-Fi is missing entirely, see [missing Wi-Fi](/articles/wifi-disappeared-windows-11-no-wifi-option/); for the 24H2-specific [5GHz connection guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/), that companion covers OS-version quirks.

## Why this happens

- **Driver preferred band set to 2.4GHz** — The adapter's Advanced setting pins the card to 2.4GHz, hiding 5GHz networks.
- **Outdated Wi-Fi driver** — Old drivers mishandle 5GHz channels, especially DFS channels routers auto-select.
- **Router 5GHz using incompatible channel/width** — DFS channels or 160MHz width on routers can exceed what the laptop card supports.
- **Separate SSIDs with 5GHz hidden** — The 5GHz SSID may be hidden, renamed, or on a 'smart connect' band the laptop avoids.
- **5GHz radio disabled in router** — Some routers ship with 5GHz off or it gets disabled in 'eco' modes.
- **Weak 5GHz signal / too far** — 5GHz attenuates faster through walls; the laptop may see the SSID but fail to hold it.
- **Power saving disabling 5GHz features** — Aggressive power management can shut down the 5GHz radio paths.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set the preferred band to 5GHz

The most common laptop-side cause. One dropdown fixes it.

While you are in the Advanced tab, also check 'Roaming Aggressiveness' — set it to Medium or higher. An overly sticky roam setting can glue the laptop to a distant 2.4GHz access point even when a strong 5GHz signal is available, producing the confusing symptom of '5GHz works, but the laptop will not stay on it.'

1. Open Device Manager > Network adapters > right-click Wi-Fi adapter > Properties > **Advanced** tab.
2. Find **Preferred Band** and set it to **5GHz** (or 'Prefer 5GHz').
3. Find **Wireless Mode / 802.11a/b/g** and ensure 5GHz-capable modes (a/n/ac/ax) are enabled — not b/g only.
4. Click OK, then scan for networks — the 5GHz SSID should now appear.

### Fix 2: Update the Wi-Fi driver

Old drivers are the top cause of 5GHz failures on DFS channels and newer routers.

1. Download the latest Wi-Fi driver for your exact laptop model from the maker's support site.
2. Intel owners can use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
3. In Device Manager, uninstall the Wi-Fi adapter (tick 'delete driver'), then install the fresh package.
4. Restart and recheck for the 5GHz network.

### Fix 3: Check the router's 5GHz settings

The router side: confirm 5GHz is actually on and sanely configured.

If your router combines both bands under one SSID with no way to split them, most routers still let you temporarily disable the 2.4GHz radio for testing. Connect the laptop while only 5GHz is broadcasting to prove the laptop side works, then re-enable 2.4GHz. This isolates router steering behavior from laptop configuration in one test.

1. Log into the router admin page and verify the **5GHz radio is enabled** with its SSID broadcasting.
2. Set the 5GHz channel to a non-DFS channel (36, 40, 44, or 48) for testing — some laptop cards struggle with DFS channels.
3. Set channel width to **80MHz** (not 160MHz) initially; widen later once stable.
4. Update router firmware — 5GHz client-compatibility fixes are common in updates.

### Fix 4: Forget the network and rejoin on 5GHz

Stale profiles can pin the connection to 2.4GHz parameters.

1. Settings > Network & internet > Wi-Fi > Manage known networks > **Forget** the network.
2. Move within 5 meters / clear line-of-sight to the router for testing.
3. Reconnect, explicitly selecting the 5GHz SSID if the router uses separate names.
4. Verify in Wi-Fi properties: Network band should read **5GHz**.

### Fix 5: Disable band-steering temporarily

'Smart connect' single-SSID setups sometimes steer the laptop to 2.4GHz and keep it there.

1. In the router admin, temporarily disable band steering / smart connect.
2. Give the 5GHz band a distinct SSID (e.g., HomeWiFi-5G) for testing.
3. Connect the laptop to the 5GHz SSID directly.
4. If it works, the steering algorithm was the problem — keep separate SSIDs or tune steering thresholds.

### Fix 6: Disable Wi-Fi power saving

Power management can disable the 5GHz radio chains while leaving 2.4GHz alive.

1. Device Manager > Wi-Fi adapter > Power Management: uncheck power-saving.
2. Advanced tab: set **Transmit Power** to Highest and power-saving modes to Maximum Performance.
3. Windows power plan: Wireless Adapter Settings > **Maximum Performance**.
4. Retest 5GHz discovery and connection stability.

### Fix 7: Check range and interference

Physics matters: 5GHz does not penetrate like 2.4GHz.

1. Test next to the router — if 5GHz works there but not in your room, it is range, not configuration.
2. Use a Wi-Fi analyzer app to check 5GHz congestion on your channel; switch to the emptiest non-DFS channel.
3. Consider router placement (elevated, central) or a mesh node for dead zones.
4. USB Wi-Fi adapters with external antennas are a cheap fix for laptops with weak internal 5GHz. See Microsoft's [Wi-Fi support](https://support.microsoft.com/en-us/windows) for signal diagnostics.

## Closing

A laptop ignoring 5GHz is a configuration mismatch, not broken Wi-Fi: the driver's preferred-band setting, an outdated driver, or the router's channel choices. Set the preferred band to 5GHz, update the driver, and put the router on a friendly non-DFS channel — that trio resolves nearly every case, and the fix is permanent.
