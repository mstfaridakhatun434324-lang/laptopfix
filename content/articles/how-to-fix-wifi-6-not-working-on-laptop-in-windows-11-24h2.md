---
title: "Wi-Fi 6 Not Working on Windows 11 24H2? Unlock AX Speeds"
slug: how-to-fix-wifi-6-not-working-on-laptop-in-windows-11-24h2
date: 2026-09-20
categories: ["drivers"]
tags: ["wifi 6", "802.11ax", "windows 11 24h2", "wireless speed"]
description: "Fix Wi-Fi 6 not working on Windows 11 24H2: enable 802.11ax mode on the adapter, update wireless drivers, and fix router and band settings."
thumbnail: "/images/thumbs/how-to-fix-wifi-6-not-working-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "How do I know if my laptop is actually using Wi-Fi 6?"
    a: "Open Settings, then Network and internet, then Wi-Fi, and click your connected network. The Properties page shows the protocol — look for Wi-Fi 6 (802.11ax). You can also check the link speed: Wi-Fi 6 connections on a clean 5 GHz or 6 GHz channel typically negotiate well above the 866 Mbps ceiling of Wi-Fi 5."
  - q: "Why does my Wi-Fi 6 laptop only connect at Wi-Fi 5 speeds?"
    a: "The usual culprits are the router broadcasting with AX mode disabled, the laptop connecting on the 2.4 GHz band instead of 5 GHz, or the adapter's 802.11ax setting turned off in its advanced properties. Any single one of these silently caps you at Wi-Fi 5 rates while everything claims to be working."
  - q: "Do I need a new router to use Wi-Fi 6?"
    a: "Yes, both ends must support it. A Wi-Fi 6 laptop talking to a Wi-Fi 5 router negotiates Wi-Fi 5 — the standard only applies when both sides speak it. If your router is older, no laptop setting will conjure AX speeds; the upgrade has to happen on the router side."
  - q: "Can a driver update really change my Wi-Fi speed?"
    a: "Absolutely. Early Wi-Fi 6 drivers had broken or disabled AX implementations, and vendors fixed them in later releases. Users commonly report their protocol flipping from Wi-Fi 5 to Wi-Fi 6 immediately after installing the current Intel, MediaTek, or Realtek driver — same hardware, same router, different driver."
---

Your laptop has a Wi-Fi 6 card, your router says AX on the box, and yet the connection stubbornly reports Wi-Fi 5 with speeds to match. Wi-Fi 6 failures are rarely total — the wireless works, it is just slower than the hardware promises. That makes the problem easy to ignore and surprisingly tricky to pin down, because the bottleneck can sit in the laptop's driver, its adapter settings, the router's configuration, or the band you happened to join.

Wi-Fi 6 (802.11ax) requires agreement at every layer: the adapter must have AX mode enabled, the driver must implement it correctly, the router must broadcast an AX-capable network, and the client must join the right band. Windows 11 24H2 complicates this with driver migrations that can silently disable AX mode in the adapter's advanced properties, resetting months of correct operation overnight.

The approach below verifies each layer in turn, starting with confirming what protocol you are actually getting, then fixing the laptop side — driver and adapter settings — before moving to router configuration and band selection.

## Why this happens

- **802.11ax disabled in adapter properties:** The 24H2 update can reset the adapter's advanced 802.11a/b/g wireless mode setting to a value that excludes AX, silently downgrading every connection.
- **Outdated wireless driver:** Early Wi-Fi 6 drivers shipped with broken or incomplete AX support. The driver version matters more for Wi-Fi 6 than for any previous standard.
- **Router not broadcasting AX:** Many routers ship with AX mode off by default, or an update resets the wireless mode. A Wi-Fi 6 client cannot use what the router does not offer.
- **Connected on 2.4 GHz instead of 5 GHz:** Wi-Fi 6's headline speeds need 5 GHz or 6 GHz channels. A client parked on 2.4 GHz gets Wi-Fi 6's efficiency but none of its speed.
- **Router firmware too old:** Early AX router firmware had interoperability bugs with certain laptop cards. Both ends need current firmware to negotiate AX reliably.
- **Channel width restricted:** AX speed gains depend on wide channels (80 or 160 MHz). A router set to 20 or 40 MHz channels caps throughput regardless of the AX label.
- **Power saving throttling the radio:** Aggressive adapter power settings can prevent the card from using its fastest modulation, dragging negotiated rates down.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the actual negotiated protocol

You cannot fix what you have not measured. Check whether the laptop is really on Wi-Fi 5 or just slow Wi-Fi 6.

1. In Settings, open Network and internet, then Wi-Fi, and click your network to view Properties.
1. Read the Protocol field: Wi-Fi 6 (802.11ax) versus Wi-Fi 5 (802.11ac).
1. Note the link speed as well — it is your baseline for measuring improvement.

### Fix 2: Enable 802.11ax in the adapter's advanced properties

This single setting is the most common laptop-side cause. The 24H2 migration loves to reset it.

1. Open Device Manager, expand Network adapters, and open your Wi-Fi adapter's Properties.
1. Go to the Advanced tab and find the 802.11a/b/g Wireless Mode or VHT Mode entry.
1. Set it to a value that includes AX (often labeled 802.11a/b/g/n/ac/ax) and click OK.
1. Disconnect and reconnect to your network, then recheck the protocol.

### Fix 3: Update the wireless driver to a current release

Driver age is the second most common cause. Wi-Fi 6 support matured significantly in drivers released well after the first AX cards shipped.

1. Identify your wireless card model in Device Manager.
1. Download the newest driver from the laptop vendor or the chipmaker — Intel's [Driver and Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) handles Intel cards directly.
1. Install, restart, and verify the protocol field again. A jump from AC to AX here is the classic driver-fix signature.

### Fix 4: Fix the router side: AX mode, band, and channel width

With the laptop correct, the router gets its turn. Log into the router's admin page for these checks.

1. Confirm the wireless mode is set to AX or Wi-Fi 6 rather than N/AC mixed.
1. Give the 5 GHz network a distinct SSID if the router merges bands, so you can join it deliberately.
1. Set 5 GHz channel width to 80 MHz (or 160 MHz if the environment is clean) and update the router firmware.

### Fix 5: Force the 5 GHz band with a separate SSID

Band steering sometimes parks AX-capable laptops on 2.4 GHz for stability. A dedicated 5 GHz SSID takes the decision away from the algorithm.

1. In the router settings, split the bands into separate network names.
1. Forget the 2.4 GHz network on the laptop or set it to not auto-connect.
1. Join the 5 GHz SSID and confirm the protocol and link speed improve. If 5 GHz specifically refuses to connect, see [5 GHz connection fixes](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/).

### Fix 6: Disable adapter power saving

Power-saving modes can keep the radio from reaching its top rates even when everything else is configured correctly.

1. In the adapter's Advanced properties, set Power Saving Mode to Maximum Performance.
1. On the Power Management tab, uncheck Allow the computer to turn off this device to save power.
1. Retest speeds near the router to isolate configuration from range issues.

### Fix 7: Reset and retest methodically

If speeds are still wrong, eliminate variables one at a time rather than changing everything at once.

1. Test with the laptop within a few meters of the router to rule out range.
1. Temporarily disable VPNs and third-party firewalls, which can bottleneck throughput measurements.
1. If the adapter itself keeps disappearing rather than just underperforming, the [vanished Wi-Fi guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) addresses that separate failure. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the built-in wireless diagnostics.

## Closing

Wi-Fi 6 is a negotiation, and it fails silently at the weakest link — usually the adapter's AX setting after a 24H2 update, an old driver, or a router that never had AX enabled. Verify the protocol, fix the laptop side first, then the router, and measure at each step. When every layer agrees on 802.11ax, the speed difference is immediately obvious — and it stays that way as long as updates are not allowed to reset the settings behind your back.
