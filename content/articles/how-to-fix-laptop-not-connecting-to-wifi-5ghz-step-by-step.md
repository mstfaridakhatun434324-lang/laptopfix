---
title: "Laptop Not Connecting to 5 GHz Wi-Fi? A Step-by-Step Fix"
slug: how-to-fix-laptop-not-connecting-to-wifi-5ghz-step-by-step
date: 2026-10-01
categories: ["drivers"]
tags: ["5ghz wifi", "wifi band", "wireless", "step by step"]
description: "Fix a laptop that will not connect to 5 GHz Wi-Fi: enable the 5 GHz band on the adapter, fix router settings, and solve authentication failures step by step."
thumbnail: "/images/thumbs/how-to-fix-laptop-not-connecting-to-wifi-5ghz-step-by-step.webp"
faqs:
  - q: "Why does my laptop see the 2.4 GHz network but not 5 GHz?"
    a: "The most common reason is the wireless adapter's band preference set to 2.4 GHz only, or an older adapter that lacks 5 GHz support entirely. Less commonly, the router's 5 GHz radio is disabled or the laptop is just out of the 5 GHz band's shorter range. Checking the adapter's preferred band setting resolves the first case in seconds."
  - q: "How do I know if my laptop supports 5 GHz Wi-Fi?"
    a: "Open Command Prompt and run netsh wlan show drivers. Look at the Radio types supported line — if it lists 802.11a or 802.11ac/ax, the adapter supports 5 GHz. If it shows only 802.11b/g/n, the hardware is 2.4 GHz only and no setting will add 5 GHz."
  - q: "Why does 5 GHz connect but keep dropping?"
    a: "The 5 GHz band has shorter range and poorer wall penetration than 2.4 GHz. Drops at distance are physics, not a fault — the signal is simply too weak. Move closer to test: if the connection stabilizes nearby, the issue is range, and the fix is router placement, not laptop settings."
  - q: "Should I use separate network names for 2.4 and 5 GHz?"
    a: "For troubleshooting, yes — separate SSIDs let you choose the band explicitly instead of trusting the router's band-steering algorithm. Once everything works, you can re-merge them if you prefer. During diagnosis, explicit control beats automation and removes one more variable from an already tricky problem."
---

The router broadcasts two networks, the phone happily uses the fast 5 GHz one, and the laptop either cannot see it at all or refuses to connect to it. The 2.4 GHz network works, so the wireless card is clearly functional — it is specifically the 5 GHz band that fails. This is a configuration problem far more often than a hardware limitation, and it yields to a methodical check of the adapter, the router, and the space between them.

The 5 GHz band differs from 2.4 GHz in ways that matter for diagnosis: shorter range, worse wall penetration, wider channels, and a separate radio in the router that can be disabled independently. A laptop parked one room too far away, an adapter preference set to 2.4 GHz only, or a router with its 5 GHz radio quietly off all produce the same symptom — and each has a different fix.

The steps below are deliberately sequential. Each one rules out a layer before you touch the next, so by the end you will know exactly which layer was at fault instead of having changed six settings and hoping.

## Why this happens

- **Adapter band preference set to 2.4 GHz:** The wireless adapter's preferred band setting can lock it to 2.4 GHz. The 5 GHz network is invisible to the laptop until this changes.
- **Adapter lacks 5 GHz hardware support:** Older 2.4 GHz-only cards cannot see 5 GHz networks at all. No software setting overcomes missing radio hardware.
- **Router's 5 GHz radio disabled:** Routers allow each band's radio to be toggled independently. A disabled 5 GHz radio is invisible to every device, but phones on mobile data mask the outage.
- **Out of 5 GHz range:** The 5 GHz signal fades faster through walls and distance. A laptop that connects near the router but not in the bedroom is range-limited, not broken.
- **Wrong Wi-Fi password cached for the 5 GHz SSID:** Separate SSIDs can have separate passwords. A stale cached credential produces repeated authentication failures that look like a band problem.
- **Outdated wireless driver:** Old drivers mishandle 5 GHz authentication and channel widths, failing connections that newer drivers complete effortlessly.
- **Router channel set to DFS range:** Some 5 GHz channels require radar-avoidance behavior that certain laptop cards handle poorly, causing failures on specific channels only.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the adapter supports 5 GHz

No setting fixes missing hardware. Verify capability first so the rest of the steps are meaningful.

1. Open Command Prompt and run netsh wlan show drivers.
1. Check Radio types supported for 802.11a, ac, or ax — any of these means 5 GHz capable.
1. If only b/g/n appear, the adapter is 2.4 GHz only; a USB Wi-Fi adapter is the practical upgrade path.

### Fix 2: Set the preferred band to 5 GHz

The most common software cause is a single dropdown in the adapter's advanced properties.

1. Open Device Manager, expand Network adapters, and open your Wi-Fi adapter's Properties.
1. On the Advanced tab, find Preferred Band and set it to Prefer 5GHz band.
1. Click OK, then disconnect and reconnect to the network. Check whether the 5 GHz SSID now appears.

### Fix 3: Verify the router's 5 GHz radio is on

Check the other end of the link. A disabled 5 GHz radio defeats every laptop-side fix.

1. Log into the router's admin page and open the wireless settings.
1. Confirm the 5 GHz radio is enabled and broadcasting its SSID.
1. While there, note the channel: if it is in the DFS range (52-144), try a non-DFS channel like 36 or 149 to rule out radar-avoidance issues.

### Fix 4: Forget the network and reconnect cleanly

Stale credentials and corrupted profiles cause authentication failures that masquerade as band problems.

1. Open Settings, then Network and internet, then Wi-Fi, then Manage known networks.
1. Forget the 5 GHz network, then reconnect and carefully re-enter the password.
1. If it connects now, the profile was the problem all along.

### Fix 5: Update the wireless driver

Driver age matters disproportionately for 5 GHz, where authentication and wide channels stress older implementations.

1. Identify your wireless card in Device Manager.
1. Install the newest driver from the laptop vendor or the chipmaker — Intel cards via Intel's [Driver and Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
1. Restart and retest the 5 GHz connection. If the whole Wi-Fi option vanished rather than just the band, see [Wi-Fi disappeared](/articles/wifi-disappeared-windows-11-no-wifi-option/).

### Fix 6: Test range and interference

Separate physics from configuration with a simple proximity test.

1. Move the laptop within a few meters of the router with line of sight and try connecting.
1. If it connects nearby but not at distance, the issue is range — reposition the router centrally and elevated, or add an access point.
1. Check for interference from USB 3.0 devices and microwaves near the laptop, which disproportionately affect 5 GHz. For the 24H2-specific band quirks, see [5 GHz on 24H2](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/).

### Fix 7: Reset the network stack as a final step

When everything is configured correctly but connections still fail, corrupted network configuration is the remaining suspect.

1. In an elevated Command Prompt, run netsh winsock reset and netsh int ip reset.
1. Restart the laptop and reconnect to the 5 GHz network from scratch.
1. If it still fails after all of this, the adapter's 5 GHz radio may be faulty — test with a USB Wi-Fi adapter to confirm before concluding hardware failure. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the wireless troubleshooting flow.

## Closing

A laptop that ignores the 5 GHz band is almost always a settings story: the adapter's band preference, the router's radio state, a stale network profile, or an old driver. The proximity test is your truth serum — it separates range physics from configuration in sixty seconds. Work the steps in order, and the fast band that the phone enjoyed all along will show up on the laptop too.
