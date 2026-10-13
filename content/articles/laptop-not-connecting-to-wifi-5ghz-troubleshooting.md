---
title: "Laptop Not Connecting to 5GHz WiFi? Troubleshooting Guide"
slug: laptop-not-connecting-to-wifi-5ghz-troubleshooting
date: 2026-09-26
categories: ["drivers"]
tags: ["5ghz wifi", "wifi band", "wireless adapter", "windows 11"]
description: "Laptop won't connect to 5GHz WiFi but 2.4GHz works? Troubleshoot band detection, adapter settings, and driver issues with these 7 fixes."
thumbnail: "/images/thumbs/laptop-not-connecting-to-wifi-5ghz-troubleshooting.webp"
faqs:
  - q: "Why can't my laptop see the 5GHz WiFi network?"
    a: "The most common reasons: the WiFi adapter is set to 2.4GHz-only in its Advanced properties, the adapter's driver doesn't properly support 5GHz on your card revision, the router's 5GHz band uses a channel the laptop can't see (especially DFS channels), or the laptop is too far from the router — 5GHz has shorter range than 2.4GHz. Check the adapter's Preferred Band setting in Device Manager first; it's the fastest fix."
  - q: "How do I force my laptop to use 5GHz WiFi?"
    a: "In Device Manager, open the WiFi adapter's Properties, go to the Advanced tab, find Preferred Band or Band, and set it to 5GHz (or Prefer 5GHz). Also set Roaming Aggressiveness to a middle value so the laptop doesn't cling to a weak 2.4GHz signal. On the router side, give the 5GHz network a distinct SSID name so you can connect to it explicitly rather than relying on band steering."
  - q: "Is my WiFi card too old for 5GHz?"
    a: "Possibly. 5GHz requires an 802.11n (dual-band), 802.11ac, or 802.11ax card — old 802.11b/g-only cards are 2.4GHz-only. Check your adapter's properties in Device Manager or run netsh wlan show drivers in Command Prompt and look at Radio types supported: you want to see 802.11a, 802.11ac, or 802.11ax listed (the 'a' indicates 5GHz capability). Single-band cards can be replaced with an inexpensive dual-band M.2 card."
  - q: "Why does 5GHz work on my phone but not my laptop?"
    a: "That isolates the problem to the laptop — the router's 5GHz band is fine. Focus on the laptop's adapter settings (Preferred Band), its driver (update from the manufacturer's site), and the channels in use: phones handle DFS channels better than many laptop cards. Try setting the router's 5GHz channel to 36-48 (non-DFS) as a test. For MediaTek-specific adapter issues, see the [MediaTek WiFi guide](/articles/best-way-to-fix-mediatek-wifi-not-working/)."
---

Your phone happily connects to the fast 5GHz network, but your laptop either can't see it or refuses to connect — stuck on the slower, congested 2.4GHz band. Since the router is proven working (the phone proves it), the problem is entirely on the laptop side: its adapter settings, its driver, or its hardware capability.

This is a driver-and-settings problem in nearly every case. The fixes below move from the adapter's band settings through driver repair to router-side channel tweaks, and each one takes only a few minutes.

## Why this happens

- **Adapter set to 2.4GHz-only:** The Preferred Band property locked to 2.4GHz.
- **Outdated WiFi driver:** Old driver with broken 5GHz support on current Windows.
- **Router on DFS channels:** Channels 52–144 that many laptop cards can't use.
- **Single-band WiFi card:** Old 802.11b/g/n (2.4GHz-only) hardware.
- **Weak 5GHz signal:** 5GHz's shorter range — the laptop clings to 2.4GHz at distance.
- **Band steering confusion:** Router's single SSID steering the laptop to 2.4GHz.
- **Corrupt wireless profile:** A damaged saved network profile blocking 5GHz connection.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set the adapter's Preferred Band to 5GHz

The fastest fix — the adapter may simply be told to prefer 2.4GHz.

1. Open Device Manager (**Win + X**), expand **Network adapters**.
2. Right-click the WiFi adapter, choose **Properties**, and go to the **Advanced** tab.
3. Find **Preferred Band** (may be called **Band**) and set it to **Prefer 5GHz band** or **5GHz**.
4. Find **Roaming Aggressiveness** and set it to **3. Medium** — this stops the laptop clinging to weak 2.4GHz.
5. Click OK, then disconnect and reconnect to WiFi.

If there's no Preferred Band property, the driver doesn't expose it — update the driver (Fix 3), which often adds the property.

### Fix 2: Verify the card supports 5GHz

Don't fight hardware — confirm capability first.

1. Open Command Prompt and run `netsh wlan show drivers`.
2. Look at **Radio types supported** — you need **802.11a**, **802.11ac**, or **802.11ax** listed (the "a" family is 5GHz).
3. If only 802.11b/g/n appear with no "a", the card is 2.4GHz-only.
4. Check the card model in Device Manager against its specs online.

A 2.4GHz-only card needs replacing — an Intel AX210 M.2 card costs around $20 and adds WiFi 6 with 5GHz. It's a ten-minute swap on laptops with accessible M.2 slots. The [5GHz-specific guide](/articles/best-way-to-fix-laptop-not-connecting-to-wifi-5ghz/) covers card upgrades.

### Fix 3: Update the WiFi driver from the manufacturer

Old drivers are the top fixable cause of 5GHz blindness.

1. Note your exact WiFi adapter model in Device Manager.
2. Download the latest WiFi driver from your laptop maker's support site — or from [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel cards.
3. Install it, restart, and recheck the Preferred Band property (it may now appear).
4. Test 5GHz connection.

Manufacturer drivers include the correct regulatory and band tables for your region — generic drivers sometimes get these wrong, hiding 5GHz channels.

### Fix 4: Change the router's 5GHz channel

DFS channels are invisible to many laptop cards.

1. Log into your router's admin page (usually 192.168.1.1 or 192.168.0.1).
2. Find the **5GHz wireless settings** and check the current **channel**.
3. If it's on a DFS channel (52–144), change it to **36**, **40**, **44**, or **48** — the universally supported non-DFS channels.
4. Set **channel width** to **80MHz** (or Auto) for good speed without compatibility issues.
5. Save, let the router restart its radio, and check the laptop.

Also give the 5GHz band its own SSID (like `Home-5G`) if it shares one with 2.4GHz — separate names let you connect explicitly instead of trusting band steering.

### Fix 5: Delete and recreate the wireless profile

A corrupt saved profile can block 5GHz specifically.

1. Go to **Settings > Network & internet > WiFi > Manage known networks**.
2. **Forget** your network.
3. Open Command Prompt as administrator and run `netsh wlan delete profile name="YourNetworkName"` for good measure.
4. Reconnect fresh: select the 5GHz SSID and enter the password.
5. If it connects now, the old profile was corrupt.

This is quick and fixes the maddening case where the laptop sees 5GHz but fails to connect to it.

### Fix 6: Disable power saving on the WiFi adapter

Power management can disable 5GHz radios to save power.

1. In Device Manager, open the WiFi adapter's **Properties > Power Management** tab and untick **Allow the computer to turn off this device**.
2. On the **Advanced** tab, set **Power Saving Mode** to **Maximum Performance** and **Transmit Power** to **Highest**.
3. In **Settings > System > Power & battery**, set **Power mode** to **Best performance** while testing.
4. Test 5GHz on both AC and battery.

If 5GHz works on AC but not battery, power saving is throttling the radio — keep the adapter at maximum performance.

### Fix 7: Reset the network stack and check distance

Final steps: clean state and physics.

1. Run **Settings > Network & internet > Advanced network settings > Network reset**, then restart.
2. After reboot, set Preferred Band to 5GHz again (reset clears it).
3. Test close to the router — within 5 meters, line of sight. 5GHz attenuates fast through walls; if it works nearby but not in your room, it's a range problem, not a driver problem.
4. For range issues: reposition the router centrally and elevated, or add an access point — no driver fix overcomes physics.

If 5GHz works near the router but nowhere else, consider whether your environment needs a mesh node rather than more troubleshooting. For general WiFi disappearance issues, see the [WiFi vanished guide](/articles/best-way-to-fix-wifi-disappeared-from-laptop/).

## Closing

5GHz connection failures are almost always settings or drivers: Preferred Band locked wrong, an outdated driver, or DFS channels the card can't see. The phone test is your compass — if the phone connects, the router is fine and the laptop is the project. Get the band setting right and the driver current, and 5GHz connects as reliably as 2.4GHz.
