---
title: "How to Fix Wi-Fi 6 Not Working on Your Laptop (Connection Drops & Slow Speeds)"
slug: how-do-i-fix-wifi-6-not-working-on-laptop
date: 2026-10-11
categories: ["drivers"]
tags: ["wi-fi 6 fix", "802.11ax drops", "wifi slow", "wireless disconnects", "ax wifi issues"]
description: "Wi-Fi 6 connected but slow, dropping, or unstable? Practical fixes for 802.11ax reliability problems — driver versions, router compatibility, and band settings."
thumbnail: "/images/thumbs/how-do-i-fix-wifi-6-not-working-on-laptop.webp"
faqs:
  - q: "Why is my Wi-Fi 6 connection slower than my old Wi-Fi 5 was?"
    a: "Counterintuitive but common: early 802.11ax implementations had interoperability bugs, and some router-laptop combinations negotiate poorly, falling back to inefficient modes. A too-new or too-old driver, 20 MHz channel widths, or a congested band can all make ax slower than ac in practice. The fixes in this guide address each — and sometimes the answer is pinning the adapter to Wi-Fi 5 until the ecosystem matures."
  - q: "Why does my Wi-Fi 6 connection keep disconnecting?"
    a: "Drops usually come from power management putting the adapter to sleep, driver instability in ax mode, or the router's band-steering kicking the client between bands. Disabling adapter power management and updating to a stable (not necessarily newest) driver version resolves most drop patterns. If drops correlate with distance, it's a signal issue, not an ax issue."
  - q: "Should I disable Wi-Fi 6 and use Wi-Fi 5 instead?"
    a: "As a diagnostic step, absolutely — and as a permanent setting, sometimes. If Wi-Fi 5 (802.11ac) is rock-solid while ax drops or crawls, the ax implementation on your router or adapter is the problem. There's no shame in running stable ac while waiting for firmware maturity; real-world ac speeds handle everything short of multi-gigabit LAN transfers."
  - q: "Do mesh Wi-Fi systems cause Wi-Fi 6 problems?"
    a: "They can. Mesh nodes hand clients between access points, and some mesh systems' roaming logic interacts badly with certain laptop adapters in ax mode — causing drops during handoffs. If drops happen when moving around the house but not when stationary near one node, mesh roaming is the suspect. Check the mesh app for client-steering or roaming settings."
---

This is the companion to our [Wi-Fi 6 setup guide](/articles/what-to-do-if-wifi-6-not-working-on-laptop/): that one gets 802.11ax working at all; this one fixes it when it's connected but misbehaving — slow speeds, random disconnects, high latency, or speeds worse than the Wi-Fi 5 you upgraded from. These are the problems that appear after the "connected with Wi-Fi 6" victory screen.

Wi-Fi 6 reliability issues cluster around three causes: driver versions (ax support matured unevenly), router interoperability (early ax firmware was buggy), and power management (which hits ax harder than older standards). The fixes below address each in turn.

## Why this happens

- **Immature ax driver versions.** 802.11ax support improved dramatically across driver generations; early versions drop and stall.
- **Router firmware interoperability bugs.** Early Wi-Fi 6 routers mishandle certain client adapters.
- **Aggressive adapter power management.** Power-saving hits ax throughput and stability harder than ac.
- **Band steering and mesh roaming conflicts.** Network-directed roaming fights the adapter's own logic.
- **Congested or narrow channels.** ax on a crowded 20 MHz channel performs worse than ac on clean 80 MHz.
- **OFDMA/MU-MIMO misbehavior.** ax's headline features can malfunction with mixed client types, hurting more than helping.
- **Weak signal.** ax's higher-order modulation needs stronger signal; at the edge of range, it underperforms ac.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find a stable driver version (not necessarily the newest)

For ax reliability, driver version matters more than driver newness.

1. Note your current wireless driver version (**Device Manager > Network adapters > Properties > Driver**).
2. Check your laptop manufacturer's support site and Intel's release notes for versions known-stable for ax.
3. If problems started after a driver update, roll back immediately — ax regressions in new drivers are documented.
4. If you're on an old driver, update via [Intel's driver tool](https://www.intel.com/content/www/us/en/support/detect.html) — but test thoroughly; newer isn't automatically better for ax.

Keep a log: version number, date installed, symptoms. Ax driver quality varies enough version-to-version that "the March driver was fine, the June driver drops" is actionable intelligence. Once you find a stable version, [block automatic driver updates](/articles/how-can-i-disable-automatic-driver-updates/) to keep it.

### Fix 2: Disable adapter power management

The single most effective fix for ax disconnects.

1. In **Device Manager > Network adapters**, right-click your Wi-Fi adapter > **Properties > Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. Go to the **Advanced** tab and set **Power Saving Mode** / **Transmit Power** to **Maximum Performance** / **5. Highest**.
4. Set Windows **Power mode** to **Best performance** while testing.

Ax power-save mechanisms (TWT — Target Wake Time) are more aggressive than ac's, and buggy implementations drop connections instead of sleeping gracefully. Maximum-performance settings disable these paths. The battery cost is real but modest; stability is worth it.

### Fix 3: Tune the router's ax settings

The router side of interoperability — where early firmware bugs live.

1. Update the router's firmware to the latest — ax interoperability fixes are a staple of router changelogs.
2. In the router's wireless settings, try disabling **OFDMA** and **MU-MIMO** temporarily — if speeds jump, the router's implementation of these features is buggy.
3. Set the 5 GHz channel width to **80 MHz** explicitly rather than Auto.
4. Try a different 5 GHz channel — use a Wi-Fi analyzer app to find the least congested one.

The OFDMA/MU-MIMO toggle test is revealing: these are ax's signature features, and when they're broken in firmware they hurt more than help. A router with broken OFDMA performs worse than a Wi-Fi 5 router — disabling the broken feature is a genuine fix, not a surrender.

### Fix 4: Pin the adapter to Wi-Fi 5 as a diagnostic (and possibly permanent) step

Isolate whether ax itself is the problem.

1. In the adapter's **Advanced** properties, find the wireless mode setting and select a value without ax (e.g., **802.11a/b/g/n/ac**).
2. Reconnect and test for a day: speed, drops, latency.
3. If ac is stable and fast while ax wasn't, the ax implementation (router or adapter) is at fault.
4. Decide: keep ac pinned for stability, or use the finding to justify a router firmware push / router replacement.

There's no prize for running a broken ax connection. A stable 866 Mbps ac link beats a dropping "2400 Mbps" ax link in every real-world measure. Revisit ax after the next router firmware update — the ecosystem is still maturing.

### Fix 5: Fix band steering and roaming behavior

For drops that happen when moving around or at specific locations:

1. In the router settings, try disabling **band steering** temporarily and use separate SSIDs for 2.4 and 5 GHz.
2. Connect to the 5 GHz SSID manually and set the adapter's **Preferred Band** to **5 GHz**.
3. In the adapter's Advanced properties, look for **Roaming Aggressiveness** and set it to **Lowest** if drops happen during mesh handoffs.
4. If your mesh system has client-steering options, experiment with them — or pin the laptop to the nearest node if the app allows.

The roaming-aggressiveness setting is the key insight: the laptop and the mesh system both try to manage roaming, and when they disagree, the connection drops. Setting the laptop to least-aggressive lets the mesh system drive — or vice versa. One driver, not two.

### Fix 6: Check signal strength and placement

ax's speed depends on signal quality more steeply than older standards.

1. In Command Prompt, run `netsh wlan show interfaces` and check the **Signal** percentage — below 60% means ax can't use its fast modulation.
2. Move closer to the router temporarily: if problems vanish, it's signal, not configuration.
3. Reposition the router: elevated, central, away from metal and mirrors.
4. Consider that the laptop's own antenna placement matters — metal laptop stands and docks can shadow the antennas.

The `netsh` signal reading is the objective truth — don't troubleshoot configuration when the signal is 40%. At weak signal, even perfect settings underperform, and the fix is placement or a mesh node, not a driver.

### Fix 7: Reset and rebuild as a last resort

When the configuration is a tangle of tried settings, start clean.

1. Run **Settings > Network & internet > Advanced network settings > Network reset** and restart.
2. Install your known-stable wireless driver version afterward (Fix 1's finding).
3. Reconfigure from scratch: 5 GHz preference, power management off, then test before touching advanced settings.
4. Add back customizations one at a time, testing after each — you'll find the one that breaks it.

The one-at-a-time rebuild is slow but definitive. Most "I've tried everything" situations are actually "I've tried everything simultaneously and something in the combination is wrong." The clean rebuild with incremental changes finds the culprit that shotgun troubleshooting misses. For the underlying driver management, our [missing drivers guide](/articles/how-to-find-missing-drivers-on-windows-11/) covers keeping the stack healthy long-term.

## Closing

Wi-Fi 6 reliability problems are interoperability problems: a maturing standard, uneven driver quality, and early router firmware. The pragmatic approach is version discipline (find a stable driver and keep it), power management off, and honest testing of whether ax is actually helping — pinning to ac is a valid engineering decision, not a defeat. When the ecosystem matures on your hardware, ax will be there waiting.
