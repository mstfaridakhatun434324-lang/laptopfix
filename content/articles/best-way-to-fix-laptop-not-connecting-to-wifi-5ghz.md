---
title: "Best Way to Fix Laptop Not Connecting to WiFi 5GHz"
slug: best-way-to-fix-laptop-not-connecting-to-wifi-5ghz
date: 2026-10-11
categories: ["drivers"]
tags: ["wifi 5ghz", "5ghz not connecting", "wifi driver", "wireless adapter", "windows 11"]
description: "Laptop won't connect to WiFi 5GHz? Fix the missing 5GHz network with 7 proven repairs — band settings, drivers, and router tweaks."
thumbnail: "/images/thumbs/best-way-to-fix-laptop-not-connecting-to-wifi-5ghz.webp"
faqs:
  - q: "Why can't my laptop see the 5GHz WiFi network?"
    a: "The most common reasons are the wireless adapter's 5GHz band disabled in its advanced settings, an outdated driver that doesn't handle the band properly, or the router broadcasting 5GHz on a DFS channel the laptop can't use. Some older or budget adapters are 2.4GHz-only — check your adapter's specifications first, because no software fix adds a band the hardware lacks."
  - q: "How do I enable 5GHz on my laptop's WiFi adapter?"
    a: "Open Device Manager, find your WiFi adapter under Network adapters, open Properties, go to the Advanced tab, and set Preferred Band (or Band) to 5GHz or Auto — never 2.4GHz-only. Also check the Wireless Mode / 802.11 setting includes 5GHz modes (a/n/ac/ax). If there's no band option at all, the adapter is likely 2.4GHz-only hardware."
  - q: "Is 5GHz always better than 2.4GHz?"
    a: "Not always. 5GHz is faster with less interference but has shorter range and penetrates walls poorly — at distance, 2.4GHz often gives a more stable connection. Use 5GHz when you're in the same room as the router for maximum speed, and let the laptop fall back to 2.4GHz farther away. The fixes below get both bands working so you can choose."
  - q: "Can a driver update fix 5GHz connection problems?"
    a: "Yes — 5GHz handling is entirely in the wireless driver, and updates regularly fix band-steering bugs, DFS channel support, and WPA3 handshake issues. Install the WiFi driver from your laptop maker's support site rather than Windows Update's generic build. On Intel cards the Intel Driver and Support Assistant finds the newest validated wireless driver reliably."
---

Your laptop sees the 2.4GHz network fine but the 5GHz one is invisible — or it appears, you click connect, and it fails or drops immediately. This is a band-specific problem, which is good news diagnostically: the wireless hardware works (2.4GHz proves it), so the issue is band configuration, driver handling of 5GHz, or the router's 5GHz settings.

These seven fixes run from the adapter's band settings through driver updates to router-side tweaks. One caveat up front: check that your adapter actually supports 5GHz — some budget cards are 2.4GHz-only, and no setting changes physics.

## Why this happens

- **Preferred band set to 2.4GHz.** The adapter's advanced setting locking it off the 5GHz band.
- **Outdated wireless driver.** Old driver mishandling 5GHz association or WPA3 handshakes.
- **Router on a DFS channel.** The laptop's region-locked adapter refusing DFS 5GHz channels.
- **Separate SSIDs confusing band steering.** Router presenting bands badly, or 5GHz SSID hidden.
- **Wireless mode excluding 5GHz protocols.** The 802.11 mode set to b/g/n (2.4GHz-only modes).
- **Weak 5GHz signal.** 5GHz's short range — the laptop sees a faint signal it can't sustain.
- **2.4GHz-only adapter hardware.** The card physically lacks 5GHz — check specs first.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the adapter supports 5GHz

Don't chase a software fix for a hardware limitation.

1. Open **Device Manager > Network adapters** and note your adapter's exact model (e.g., Intel AX201, MediaTek MT7921, Realtek 8852).
2. Search the model online — look for **dual-band** or **802.11ac/ax** in the specs. Single-band 802.11n cards are 2.4GHz-only.
3. In the adapter's **Properties > Advanced** tab, look for **Preferred Band**, **Band**, or **Wireless Mode** — the absence of any band option strongly suggests 2.4GHz-only hardware.
4. If the card is 2.4GHz-only, your options are a **USB WiFi adapter** with 5GHz support ($15–25) or a **card replacement** if it's a removable M.2 module.
5. If the adapter is dual-band, continue — the fix is in settings or drivers.

### Fix 2: Set the preferred band to 5GHz

The direct setting that governs band selection.

1. **Device Manager > Network adapters**, right-click your WiFi adapter > **Properties > Advanced** tab.
2. Find **Preferred Band** (may be called **Band** or **Preferred Frequency Band**) and set it to **5GHz** — or **No Preference/Auto** if you want the laptop to choose.
3. Find **Wireless Mode** (802.11a/b/g/n/ac/ax) and make sure a value including **5GHz modes** is selected (e.g., **802.11a/b/g/n/ac/ax** or **Auto**).
4. Click OK and restart the WiFi: toggle **airplane mode** on and off, or disable/enable the adapter.
5. Check the network list — the 5GHz SSID should now appear if the router broadcasts it.

### Fix 3: Update the wireless driver from the right source

5GHz association bugs get fixed in driver updates constantly.

1. Download the **WiFi driver** from your **laptop maker's support site** for your exact model — this is the validated build.
2. For **Intel** cards, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) is equally good and usually newer.
3. In **Device Manager**, uninstall the old driver (**Attempt to remove the driver** checked), restart, then install the fresh package.
4. After installing, recheck the **Advanced** tab — new drivers sometimes add band options that weren't there before.
5. Avoid Windows Update's wireless driver for this fix — it lags and occasionally ships the very build with the 5GHz bug.

### Fix 4: Forget the network and reconnect cleanly

Stale network profiles cause cryptic 5GHz connection failures.

1. Go to **Settings > Network & internet > WiFi > Manage known networks**.
2. Select the 5GHz network (or the combined SSID) and click **Forget**.
3. Restart the laptop.
4. Reconnect by selecting the network fresh and re-entering the password carefully.
5. If the router uses **separate SSIDs** for 2.4 and 5GHz (e.g., "Home" and "Home_5G"), connect to the 5GHz one explicitly.

### Fix 5: Check the router's 5GHz settings

The router side of the handshake matters as much as the laptop.

1. Log into your router's admin page and check the **5GHz settings**.
2. Make sure the 5GHz radio is **enabled** and broadcasting its SSID (not hidden — some laptops struggle with hidden 5GHz SSIDs).
3. Change the 5GHz **channel** to a non-DFS channel: **36, 40, 44, or 48** — DFS channels (52–144) are refused by many laptop adapters depending on region.
4. Set **channel width** to **80MHz** (or Auto) and security to **WPA2-Personal** during testing — some older drivers choke on WPA3 handshakes.
5. If your router merges bands under one SSID (**band steering**), try temporarily splitting them to test 5GHz directly.

### Fix 6: Reset the network stack

Corrupt wireless profiles and stack state can block one band specifically.

1. Open **Command Prompt as administrator** and run: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /flushdns`.
2. Restart the laptop.
3. Or use **Settings > Network & internet > Advanced network settings > Network reset** — this wipes all adapters and saved networks (you'll re-enter passwords).
4. After the reset, redo Fix 2's band settings — network reset restores driver defaults.
5. Test 5GHz connection **near the router** first — 5GHz range is short, and distance failures masquerade as configuration problems.

For the Intel AX201 specifically, which has its own 5GHz quirks: [how to fix Intel WiFi 6 AX201 not working in Windows 11 24H2](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/).

### Fix 7: Rule out signal and interference

When 5GHz appears but won't stay connected.

1. Stand **in the same room as the router** and test — if 5GHz works close but not far, it's range, not configuration.
2. 5GHz penetrates walls poorly — one wall can halve the usable range versus 2.4GHz.
3. Check for **interference**: neighboring 5GHz networks on the same channel (use a WiFi analyzer app), microwave ovens, and USB 3.0 devices near the laptop (USB 3.0 is a notorious 2.4GHz interferer, but poorly shielded docks affect 5GHz too).
4. In the router, try a different non-DFS channel if neighbors crowd yours.
5. If the laptop connects to 5GHz but gets **no internet**, the issue is DHCP/DNS on that band — set a static DNS (8.8.8.8) as a test.

Microsoft's wireless troubleshooting background is on [Windows support](https://support.microsoft.com/en-us/windows).

## Closing

A laptop that won't use 5GHz is almost always a settings or driver story: the preferred-band option, a fresh manufacturer wireless driver, and a non-DFS router channel resolve the large majority of cases. Verify the hardware supports 5GHz first so you don't chase ghosts — then work the sequence and enjoy the faster band. For the Windows 11 settings path specifically, see [how to fix laptop not connecting to WiFi 5GHz on Windows 11](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-on-windows-11/).
