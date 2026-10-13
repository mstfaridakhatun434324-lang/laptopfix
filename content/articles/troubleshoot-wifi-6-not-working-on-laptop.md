---
title: "Troubleshoot WiFi 6 That Won't Work on Your Laptop"
slug: troubleshoot-wifi-6-not-working-on-laptop
date: 2026-10-10
categories: ["drivers"]
tags: ["wifi 6", "802.11ax", "wireless driver", "intel ax201", "troubleshooting"]
description: "WiFi 6 not working on your laptop? Troubleshoot 802.11ax negotiation, driver issues, and router settings that block Wi-Fi 6 connections."
thumbnail: "/images/thumbs/troubleshoot-wifi-6-not-working-on-laptop.webp"
faqs:
  - q: "Why won't my laptop connect to WiFi 6?"
    a: "The usual causes are a wireless driver that doesn't properly support 802.11ax, the 802.11ax mode disabled in the adapter's advanced settings, or a router running incompatible firmware. All three are fixable without new hardware, and the driver is the culprit in most cases."
  - q: "How do I know if my laptop supports WiFi 6?"
    a: "Check Device Manager under Network adapters for your wireless card model — Intel AX200, AX201, AX210, MediaTek MT7921/MT7922, and Qualcomm WCN685x all support WiFi 6. Then confirm 802.11ax is enabled in the adapter's Advanced properties tab. The laptop's original spec sheet also lists the wireless card model and its WiFi 6 support explicitly."
  - q: "Why is my WiFi 6 slower than expected?"
    a: "The laptop may be connecting on 802.11ac instead of ax due to driver or router settings, or it may be stuck on the congested 2.4 GHz band. Check the link speed in Settings > Network > WiFi > Hardware properties — a WiFi 6 connection on 5 GHz typically negotiates well above 1 Gbps."
  - q: "Can a router setting block WiFi 6?"
    a: "Yes. Routers with 802.11ax disabled, outdated firmware, or aggressive band-steering can prevent WiFi 6 negotiation. Some routers also need their WPA3 or protected-management-frame settings adjusted, since certain laptop drivers fail ax negotiation when those are misconfigured. When in doubt, update the router firmware first — vendors regularly fix ax interoperability bugs that mimic laptop problems."
---

WiFi 6 (802.11ax) promises faster speeds, better congestion handling, and improved battery life — but only when the laptop and router successfully negotiate it. When they don't, you get one of several frustrating outcomes: the laptop connects but only at Wi-Fi 5 speeds, it refuses to join the 5 GHz network at all, or the connection drops whenever ax features engage. The laptop's card almost certainly supports WiFi 6; the negotiation is what's failing.

Troubleshoot the negotiation chain: driver, adapter settings, then the router.

To understand why the chain matters, consider what 802.11ax negotiation actually involves. Unlike earlier WiFi generations, WiFi 6 isn't just "faster" — it introduces fundamentally new airtime mechanics like OFDMA, target wake time, and BSS coloring that both ends must agree on during the handshake. If the laptop's driver has a buggy ax implementation, it may fail that handshake while falling back to 802.11ac flawlessly, which is exactly why "WiFi works but WiFi 6 doesn't" is such a common complaint. The router's side is equally capable of breaking things: a firmware bug in its ax scheduler can reject perfectly good clients. This is why the fixes below address both ends — updating the laptop driver alone can't fix a router that refuses to negotiate, and vice versa.

## Why this happens

- **802.11ax disabled in adapter settings:** The driver exposes an 802.11a/b/g/n/ac/ax mode selector that can be set to exclude ax.
- **Outdated wireless driver:** Early driver versions for Wi-Fi 6 cards had broken or incomplete ax implementations.
- **Router firmware bugs:** The router's ax implementation may conflict with the laptop's driver version.
- **WPA3/PMF incompatibility:** Certain driver builds fail negotiation when the router requires protected management frames.
- **Band steering pushing 2.4 GHz:** The router parks the laptop on 2.4 GHz where ax benefits are minimal.
- **Channel width misconfiguration:** The adapter set to 20 MHz only can't use ax's wide-channel throughput.
- **Power management disabling ax features:** Target wake time and other ax power features conflict with aggressive adapter sleeping.
- **Windows Update driver regression:** A newer generic driver breaks ax while older OEM drivers worked.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm what you're actually connected with

1. Go to **Settings → Network & internet → Wi-Fi**, click your network, and check **Hardware properties** for the protocol and link speed.
2. If it shows **802.11ac** instead of ax, negotiation failed — the hardware works, the handshake doesn't.
3. Note the band (2.4 vs 5 GHz) and channel width while you're there.
4. This baseline tells you whether you're fixing a total failure or a fallback-to-ac problem.

### Fix 2: Enable 802.11ax in the adapter settings

1. Open **Device Manager → Network adapters**, right-click your wireless card → **Properties → Advanced**.
2. Find **802.11a/b/g Wireless Mode** or **VHT/HE mode** entries and ensure ax/HE options are enabled (often listed as "802.11ax" or value entries).
3. Set **Preferred Band** to **5 GHz** to keep the laptop off the congested 2.4 GHz band.
4. Set **Channel Width** for 5 GHz to **Auto** (allows 80/160 MHz) rather than 20 MHz only.

### Fix 3: Update to the right wireless driver

1. Check your card model — Intel AX201/AX210 owners should get drivers from the laptop maker first, then Intel as fallback via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. Avoid the newest generic driver reflexively: for ax issues, the **OEM-validated** driver is usually more stable than the bleeding-edge generic.
3. Uninstall the old driver with driver deletion checked before installing the replacement.
4. Re-check the negotiated protocol after the update. Our [Intel AX201 guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) covers card-specific quirks.

### Fix 4: Update the router firmware

1. Log into your router's admin page and check for **firmware updates**.
2. Router-side ax bugs are common, and vendors fix interoperability issues in firmware updates regularly.
3. After updating, **forget the network** on the laptop and reconnect fresh to force renegotiation.
4. If your router has an explicit **802.11ax mode** toggle, make sure it's enabled (some ship with it off for compatibility).

### Fix 5: Adjust router wireless security

1. In the router settings, try **WPA2/WPA3 transitional** mode rather than WPA3-only if negotiation fails.
2. Check for a **Protected Management Frames (PMF)** setting — set it to **optional/capable** rather than required if the laptop won't connect.
3. Disable any **"ax only"** or Wi-Fi 6-exclusive modes during testing; re-enable after a stable connection.
4. These security settings are a known friction point between certain driver builds and router firmware.

### Fix 6: Tame power management

1. In the adapter's **Power Management** tab, uncheck **Allow the computer to turn off this device to save power**.
2. In **Advanced**, set power-saving modes to **Maximum Performance** while testing.
3. Wi-Fi 6's target wake time features interact badly with aggressive adapter sleeping on some driver versions.
4. Once stable, you can experiment with re-enabling moderate power saving. For the vanished-adapter variant, see [WiFi 6 not working in Windows 11](/articles/how-to-fix-wifi-6-not-working-on-laptop-in-windows-11-24h2/).

### Fix 7: Test against a different ax router

1. Connect to a **different Wi-Fi 6 network** — a friend's router, office, or phone hotspot with ax.
2. If ax works there, your router's configuration or firmware is the problem, not the laptop.
3. If ax fails everywhere, the laptop's driver or card is at fault.
4. This isolation test saves hours of tweaking the wrong end of the connection.

### Fix 8: Reset and rebuild as a last resort

1. **Forget** the network on the laptop, then run a **network reset** (Settings → Network → Advanced → Network reset).
2. Reconnect and reconfigure from scratch.
3. As a final check, boot a **Linux live USB** — Linux's ax support will tell you definitively whether the card's ax hardware works.
4. Check Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) for wireless known issues. If the card never appears at all, our [vanished WiFi guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) applies.

## Closing

WiFi 6 failures are negotiation failures, and negotiations have two sides. Get the laptop's side right — ax enabled, correct OEM driver, sane power settings — then fix the router's side with firmware and security tweaks. When both ends speak clean 802.11ax, the speed and stability improvements are immediately obvious. One last tip: once ax is working, resist the urge to chase the absolute latest generic driver — WiFi 6 stability comes from the driver and router firmware agreeing with each other, and a validated pair that works beats a newer pair that hasn't been tested together.
