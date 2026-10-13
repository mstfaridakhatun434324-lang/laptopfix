---
title: "What to Do If Wi-Fi 6 Isn't Working on Your Laptop"
slug: what-to-do-if-wifi-6-not-working-on-laptop
date: 2026-09-21
categories: ["drivers"]
tags: ["wi-fi 6", "802.11ax", "wireless adapter", "wifi driver", "network troubleshooting"]
description: "Your laptop supports Wi-Fi 6 but connects on older standards or won't connect at all? Here's how to get 802.11ax working — drivers, router settings, and band checks."
thumbnail: "/images/thumbs/what-to-do-if-wifi-6-not-working-on-laptop.webp"
faqs:
  - q: "How do I know if I'm actually connected with Wi-Fi 6?"
    a: "In Windows 11, go to Settings > Network & internet > Wi-Fi, click your network, and check the Protocol field — it shows Wi-Fi 6 (802.11ax) when active. In Command Prompt, `netsh wlan show interfaces` lists the radio type. If it says 802.11ac or 802.11n, you're connected on an older standard despite having Wi-Fi 6 hardware."
  - q: "Does Wi-Fi 6 need a special router?"
    a: "Yes. Both ends must support 802.11ax. A Wi-Fi 6 laptop talking to a Wi-Fi 5 router negotiates down to Wi-Fi 5 (802.11ac) — that's normal, not a fault. You also need the router's ax mode enabled; some routers ship with it off or limited to the 5 GHz band only, so check the router's wireless settings."
  - q: "Will a driver update enable Wi-Fi 6 on my laptop?"
    a: "If the hardware supports it, often yes. Early Wi-Fi 6 drivers were buggy, and several adapter models only stabilized on 802.11ax with later driver releases. Update the wireless driver from your laptop maker or Intel's official driver page — but no driver can add Wi-Fi 6 to hardware that only supports Wi-Fi 5."
  - q: "Why is my Wi-Fi 6 connection slower than expected?"
    a: "Wi-Fi 6's headline speeds need a wide channel (80 or 160 MHz), a strong signal, and a compatible router. Congested 2.4 GHz bands, 20 MHz channel widths, or distance from the router all cap real-world throughput far below the theoretical 9.6 Gbps. Check your link speed in the adapter status before assuming something is broken."
---

Wi-Fi 6 (802.11ax) promises faster speeds, better congestion handling, and improved battery life — but only when the whole chain cooperates. Your laptop needs a Wi-Fi 6-capable adapter, a current driver, a Wi-Fi 6 router with ax mode enabled, and a compatible band. Break any link and the connection silently falls back to Wi-Fi 5 or fails outright, leaving you wondering why the shiny new standard isn't working.

The tricky part: Windows rarely tells you plainly what's wrong. It just connects on an older protocol or shows "can't connect to this network." This guide walks the chain from hardware to router, with the driver fixes that resolve most cases. If your Wi-Fi adapter isn't showing up at all, start with our [Wi-Fi adapter missing guide](/articles/what-to-do-if-wifi-adapter-not-showing-up/) instead — that's a different fault.

## Why this happens

- **The router doesn't support Wi-Fi 6 or has ax mode disabled.** The laptop negotiates down to the best standard both ends share.
- **The wireless driver is outdated or generic.** Early 802.11ax drivers were unstable; Windows' inbox driver may not enable ax at all.
- **The adapter is Wi-Fi 5 hardware.** Not every recent laptop shipped with an ax-capable card — some budget models still use 802.11ac.
- **You're on the 2.4 GHz band.** Some routers only offer Wi-Fi 6 on 5 GHz; the 2.4 GHz radio stays on older standards.
- **802.11ax is disabled in the adapter's advanced properties.** A manual or default-off setting can pin the card to ac/n.
- **Channel width is too narrow.** 20 MHz channels cap throughput regardless of the ax label.
- **Router firmware is old.** Early Wi-Fi 6 router firmware had interoperability bugs with certain laptop adapters.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your hardware actually supports Wi-Fi 6

No driver can add 802.11ax to a Wi-Fi 5 card. Verify the hardware first so you don't chase a software fix for a hardware limit.

1. Press **Win + X** > **Device Manager** > **Network adapters** and note your wireless adapter's exact model.
2. Search the model on the manufacturer's site (Intel, Realtek, MediaTek) and check its spec sheet for 802.11ax support.
3. In an elevated Command Prompt, run `netsh wlan show drivers` and look at **Radio types supported** — `802.11ax` must appear.
4. If ax is absent from both, your card is Wi-Fi 5; the practical fix is a USB Wi-Fi 6 adapter or an internal card swap.

Intel AX200, AX201, and AX210 cards are Wi-Fi 6; the older AC9260/AC9560 are Wi-Fi 5. Knowing your exact card saves hours of misdirected troubleshooting.

### Fix 2: Update the wireless driver from the official source

Wi-Fi 6 stability improved dramatically across driver generations. The driver Windows ships is often several generations behind.

1. Identify your adapter model from Fix 1.
2. For Intel cards, use [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to get the latest Wi-Fi driver; for others, use your laptop maker's support page.
3. Install the driver and restart — don't rely on Device Manager's "search automatically," which often reports the old driver as current.
4. Re-run `netsh wlan show drivers` and confirm the driver date is recent.

If a brand-new driver misbehaves, roll back: **Device Manager > adapter Properties > Driver > Roll Back Driver**. And to stop Windows swapping your working driver again, see our guide on [disabling automatic driver updates](/articles/how-can-i-disable-automatic-driver-updates/).

### Fix 3: Enable 802.11ax in the adapter's advanced properties

Some adapters ship with ax mode disabled in their advanced settings, pinning the card to older standards.

1. Open **Device Manager > Network adapters**, right-click your Wi-Fi adapter, and choose **Properties**.
2. Go to the **Advanced** tab and look for properties like **802.11a/b/g Wireless Mode**, **VHT Mode**, or **802.11ax**.
3. Set any ax-related mode to **Enabled** or select a value that includes **ax** (e.g., "6. 802.11a/b/g/n/ac/ax").
4. Click OK, then disconnect and reconnect to your network.

Property names vary by vendor — Realtek, Intel, and MediaTek all label these differently. If no ax option exists, your driver is too old (Fix 2) or the hardware doesn't support it (Fix 1).

### Fix 4: Enable Wi-Fi 6 on the router

The laptop can only use what the router offers. Log into your router and check its wireless settings.

1. Open your router's admin page (usually `192.168.1.1` or `192.168.0.1`) and go to wireless settings.
2. Confirm **802.11ax / Wi-Fi 6 mode** is enabled — on both 2.4 GHz and 5 GHz if you use both bands.
3. Set channel width to **80 MHz** (or **Auto** including 80/160 MHz) on the 5 GHz band.
4. Update the router's firmware while you're there; early ax firmware had laptop-adapter interoperability bugs.

If your router is a Wi-Fi 5 model, no setting will conjure ax from it — that's a hardware upgrade decision. For the general case of Wi-Fi misbehaving on specific brands, our [Dell Wi-Fi fix guide](/articles/how-to-fix-wifi-not-working-on-dell-laptop/) covers vendor-specific quirks.

### Fix 5: Prefer the 5 GHz band and check the negotiated protocol

Even with everything enabled, Windows may camp on 2.4 GHz where ax benefits are minimal.

1. In **Settings > Network & internet > Wi-Fi**, click your network and check the **Protocol** and **Link speed**.
2. If the SSID is band-steered, split the bands in the router settings (separate SSIDs for 2.4 and 5 GHz) and connect to the 5 GHz one.
3. In the adapter's **Advanced** properties, set **Preferred Band** to **5 GHz** if available.
4. Re-check the protocol — you want **Wi-Fi 6 (802.11ax)** with a link speed in the hundreds of Mbps or higher.

Band steering algorithms don't always pick the best band for your location in the house. A manual preference is a legitimate, stable configuration — not a hack.

### Fix 6: Reset the network stack

Corrupted network configuration can prevent ax negotiation even when hardware and drivers are fine.

1. Open **Settings > Network & internet > Advanced network settings > Network reset**.
2. Click **Reset now** and confirm; the laptop will restart.
3. Reconnect to your Wi-Fi network and re-check the protocol.
4. Alternatively, in an elevated Command Prompt: `netsh winsock reset` and `netsh int ip reset`, then restart.

A network reset wipes saved Wi-Fi passwords and VPN configurations, so have your credentials handy. It's a blunt tool, but it clears the obscure corrupted states that targeted fixes miss.

### Fix 7: Test against a known-good Wi-Fi 6 network

Isolate whether the problem is your laptop or your router by testing elsewhere.

1. Connect the laptop to a different Wi-Fi 6 network (a friend's, office, or phone hotspot won't be ax — use a real ax router).
2. Check the negotiated protocol there.
3. If ax works elsewhere, your router's configuration is the problem — revisit Fix 4 or consider replacement.
4. If ax fails everywhere with a capable card and current driver, the adapter itself may be faulty — try a USB Wi-Fi 6 adapter to confirm before servicing the laptop.

This is the definitive split test. Everything before it is educated guessing; this tells you which half of the chain owns the fault.

## Closing

Wi-Fi 6 failures are chain failures: capable card, current driver, ax enabled on both ends, right band, sane channel width. Walk the chain in order and the weak link reveals itself — usually an outdated driver or a router with ax mode off. Once every link is green, the protocol field reads "Wi-Fi 6 (802.11ax)" and stays there, which is the only confirmation that matters.
