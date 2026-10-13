---
title: "Laptop Won't Connect to 5GHz WiFi? How to Fix It"
slug: how-to-fix-laptop-not-connecting-to-wifi-5ghz
date: 2026-09-27
categories: ["drivers"]
tags: ["5ghz wifi not connecting", "laptop only sees 2.4ghz", "5g wifi missing", "wifi band issue", "wireless adapter 5ghz"]
description: "Your laptop sees the 2.4GHz network but not the 5GHz one, or it refuses to connect. Here's how to check band support and fix 5GHz WiFi on Windows laptops."
thumbnail: "/images/thumbs/how-to-fix-laptop-not-connecting-to-wifi-5ghz.webp"
faqs:
  - q: "Why can my phone see the 5GHz network but my laptop can't?"
    a: "This almost always means the laptop's WiFi adapter doesn't support 5GHz, or the driver has the 5GHz band disabled. Older and budget laptops shipped with single-band 2.4GHz-only adapters, while phones from the same era often had dual-band chips. Check the adapter's specifications in Device Manager under the Advanced tab — look for a Preferred Band or VHT Mode setting. If no 5GHz options exist, the hardware itself is single-band."
  - q: "My laptop connected to 5GHz before but stopped. What changed?"
    a: "A driver update is the most likely culprit — new drivers sometimes reset the preferred band to 2.4GHz or disable 802.11a/n/ac modes. Router changes matter too: if someone renamed the 5GHz SSID, enabled band steering, or changed the channel to one your adapter's region doesn't support, the network vanishes. Check both the driver settings and any recent router configuration changes."
  - q: "Which WiFi channels should I use for 5GHz?"
    a: "For maximum compatibility, use channels 36, 40, 44, or 48 — these are universally supported across regions and adapter generations. Higher channels like 149-165 work on most modern adapters but can be invisible to older ones, and DFS channels (52-144) cause adapters to hesitate or drop. If your laptop can't see the 5GHz network, switching the router to channel 36 or 40 is one of the most effective fixes."
  - q: "Is 5GHz always better than 2.4GHz for a laptop?"
    a: "Not always. 5GHz is faster at close range but has shorter range and worse wall penetration than 2.4GHz. If your laptop is far from the router or separated by thick walls, 2.4GHz may actually give you a more stable connection despite lower peak speed. The ideal setup lets the laptop use 5GHz when close and fall back to 2.4GHz at distance — which is exactly what a properly configured dual-band connection does."
---

The 5GHz band is where WiFi speed lives — but it's also where a specific class of connection problems lives. Your laptop connects fine to the 2.4GHz network, your phone happily uses the 5GHz one, and the laptop either can't see the 5GHz SSID at all or sees it and refuses to connect. This is one of the most common WiFi complaints on Windows laptops, and it has a short list of causes.

The key insight: 5GHz problems are almost always about capability negotiation — the adapter, the driver, or the router disagreeing about what the 5GHz band should look like. The fixes below go from checking what your hardware can actually do, through driver settings, to router-side changes.

Before diving in, it is worth understanding why 5GHz is fussier than 2.4GHz in the first place. The 5GHz band is split into many more channels, some of which require the router to check for radar before transmitting (DFS channels), and different countries allow different subsets — so the adapter, driver, and router all have to agree on region, channel, and mode before a connection happens. The 2.4GHz band has fewer moving parts, which is why it "just works" while 5GHz fails. Every fix below removes one of those moving parts from the equation.

## Why this happens

- **The WiFi adapter is 2.4GHz-only.** Budget and older laptops shipped with single-band adapters that physically cannot see 5GHz.
- **The driver has the 5GHz band disabled** or the preferred band set to 2.4GHz, often after a driver update reset.
- **The router is on an incompatible channel.** DFS channels or high-band channels can be invisible to some adapters.
- **The 5GHz SSID is hidden or band-steering merged it** with the 2.4GHz network under one name.
- **Outdated driver** lacking proper 802.11ac/ax support for the router's mode.
- **Power management** throttling the adapter so it won't attempt 5GHz association.
- **Regional regulatory mismatch** — the adapter's country setting doesn't allow the router's channel.
- **Weak 5GHz signal** at distance causing the laptop to prefer (or only hold) 2.4GHz.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your adapter actually supports 5GHz

Don't troubleshoot a hardware limitation.

1. Press **Win + X**, open **Device Manager**, and expand **Network adapters**.
2. Note the exact model of your wireless adapter (Intel, Realtek, MediaTek, Qualcomm).
3. Look up the model online — check for "dual band" or "802.11a/n/ac/ax" support. 802.11b/g/n-only means 2.4GHz only.
4. Alternatively, open an elevated terminal and run `netsh wlan show drivers`. Look at **Radio types supported** — if it lists only 802.11b/g/n without 802.11a, the card is single-band.
5. If the card is single-band, the fix is a USB WiFi adapter or an internal card upgrade — no setting will conjure 5GHz support.

### Fix 2: Check the Preferred Band setting in the driver

The driver may be steering you to 2.4GHz.

1. In Device Manager, right-click the wireless adapter and choose **Properties**.
2. Open the **Advanced** tab and look for **Preferred Band** — set it to **Prefer 5GHz band** or **5GHz**.
3. Look for **802.11a/b/g Wireless Mode** or **VHT Mode** and make sure 5GHz modes (802.11a/n/ac) are enabled, not disabled.
4. Click OK and restart the laptop. Check whether the 5GHz SSID appears now.

### Fix 3: Update or reinstall the WiFi driver

Stale drivers mishandle modern 5GHz configurations.

1. Download the latest wireless driver from your laptop maker's support site (or Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel cards).
2. In Device Manager, uninstall the wireless adapter with driver deletion.
3. Install the fresh driver and restart.
4. Recheck the Advanced tab settings from Fix 2 — new drivers sometimes reset them.

### Fix 4: Change the router's 5GHz channel

Channel incompatibility is a silent killer.

1. Log into your router's admin page (usually 192.168.1.1 or 192.168.0.1).
2. Find the 5GHz wireless settings and change the channel to **36** or **40** — the most universally compatible channels.
3. Avoid DFS channels (52–144) during testing; they cause detection delays and dropouts on many adapters.
4. Save, wait for the router to apply, and rescan networks on the laptop.

### Fix 5: Check SSID broadcast and band steering

The network might be there but hidden by router features.

1. In the router settings, confirm the 5GHz SSID is broadcasting (not hidden).
2. If the router merges 2.4GHz and 5GHz under one SSID (band steering / Smart Connect), try temporarily giving the 5GHz band its own distinct SSID name to test.
3. On the laptop, click the WiFi icon and check **all** available networks — the 5GHz network may appear as a separate entry.

### Fix 6: Disable power saving on the wireless adapter

Power management can prevent 5GHz association.

1. In Device Manager, open the wireless adapter's **Properties > Power Management** and uncheck **Allow the computer to turn off this device to save power**.
2. In the **Advanced** tab, set **Power Saving Mode** or **Roaming Aggressiveness** to **Maximum Performance** while testing.
3. In **Settings > System > Power & battery**, use **Best performance** mode temporarily.

### Fix 7: Reset the network stack

Clears corrupted wireless profiles that block 5GHz specifically.

1. Open **Terminal (Admin)** and run:
   `netsh winsock reset`
   `netsh int ip reset`
   `netsh wlan delete profile name=* i=*`
2. Restart and reconnect to the 5GHz network fresh, re-entering the password.

If your adapter problems go deeper than band selection, see [what to do when the WiFi adapter vanishes entirely](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/).

## Closing

5GHz connection failures are a negotiation problem, and the fix is making sure both sides speak the same language: a capable adapter, a driver that prefers the 5GHz band, and a router on a friendly channel. The channel change to 36 or 40 is the unsung hero here — it resolves a remarkable number of "laptop can't see 5GHz" cases with one router setting. If your WiFi troubles extend to the laptop's own hotspot feature, our [mobile hotspot troubleshooting guide](/articles/how-to-fix-hotspot-not-working-on-laptop-in-windows-11-24h2/) covers the reverse direction of the same radio.
