---
title: "Laptop Not Connecting to Wi-Fi 5GHz? 7 Fixes That Work"
slug: how-to-fix-laptop-not-connecting-to-wifi-5ghz-youtube
date: 2026-09-08
categories: ["drivers"]
tags: ["wifi", "5ghz", "wireless", "network", "connection"]
description: "Laptop sees the 2.4GHz network but won't connect to 5GHz Wi-Fi? 7 fixes — band settings, driver updates, and router tweaks that restore 5GHz."
thumbnail: "/images/thumbs/how-to-fix-laptop-not-connecting-to-wifi-5ghz-youtube.webp"
faqs:
  - q: "Why can my laptop see 2.4GHz but not 5GHz networks?"
    a: "Three possibilities: your wireless adapter only supports 2.4GHz (common on older or budget laptops), the adapter's preferred band is locked to 2.4GHz in its driver settings, or the 5GHz signal isn't reaching the laptop — 5GHz has significantly shorter range and worse wall penetration than 2.4GHz. Check the adapter's specifications first to rule out hardware limits."
  - q: "Is 5GHz actually faster than 2.4GHz?"
    a: "Yes, substantially — 5GHz offers more bandwidth and less interference, typically delivering two to five times the real-world speed of 2.4GHz on the same router. The tradeoff is range: 5GHz fades faster through walls and distance. Use 5GHz when you're relatively near the router and 2.4GHz when you're far away or behind multiple walls."
  - q: "Can a driver update fix 5GHz connection problems?"
    a: "Often, yes. Wireless driver updates fix 5GHz band bugs, improve compatibility with newer router firmware, and correct the preferred-band logic that steers connections. If 5GHz worked before and stopped after a Windows update, the driver is the prime suspect — rolling back or reinstalling the manufacturer's wireless driver usually restores it."
  - q: "Why does my laptop connect to 5GHz but keep dropping?"
    a: "Dropping usually means a marginal signal — you're at the edge of the 5GHz range where the connection is unstable. Move closer to the router to test: if drops stop, it's range, not a fault. Other causes include router channel congestion (try a different 5GHz channel), outdated router firmware, or the laptop's power management throttling the wireless adapter."
---

Your phone connects to the 5GHz network fine, but the laptop either doesn't see it at all or refuses to connect — sticking stubbornly to the slower 2.4GHz band. Since 5GHz is where the speed lives, being locked out of it means leaving most of your internet performance on the table. The causes range from a simple driver setting to genuine hardware limits, and they're all diagnosable.

Start by confirming your adapter actually supports 5GHz — not all do. Then work through the settings and driver fixes below. If the 5GHz network doesn't appear in the list at all, the preferred-band setting in Fix 3 is the most common culprit. For the closely related 5GHz issues on newer systems, our [5GHz on Windows 11 guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/) covers the same ground for Windows 11.

## Why this happens

- **The wireless adapter doesn't support 5GHz** — older or budget cards are 2.4GHz-only by hardware design.
- **Preferred band is set to 2.4GHz** — the driver setting steers every connection away from 5GHz.
- **The driver is outdated or corrupted** — 5GHz functionality breaks while 2.4GHz keeps limping along.
- **The 5GHz signal doesn't reach the laptop** — shorter range and poor wall penetration versus 2.4GHz.
- **Router band steering misbehaves** — the router's "smart connect" pushes the laptop to 2.4GHz incorrectly.
- **Wrong wireless mode selected** — the adapter's 802.11 mode excludes the 5GHz-capable standards.
- **Channel compatibility issues** — the router uses a 5GHz channel or width the adapter can't use.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your adapter supports 5GHz

Don't troubleshoot a hardware limit. Open Device Manager, find your wireless adapter under Network adapters, and search its model name online — the specs will state its bands. Or check in Command Prompt: run `netsh wlan show drivers` and look at "Radio types supported." If you see only 802.11b/g/n (without the "a"), the card is 2.4GHz-only and no software fix will change that — a USB 5GHz adapter is the practical upgrade.

1. Open **Command Prompt** and run `netsh wlan show drivers`.
2. Check **Radio types supported** — look for **802.11a**, **ac**, or **ax** (these include 5GHz).
3. If only b/g/n appear, your card is 2.4GHz-only — consider a USB Wi-Fi adapter.
4. If 5GHz is supported, continue with the fixes below.

### Fix 2: Move closer to rule out range

5GHz range is dramatically shorter than 2.4GHz — a laptop two rooms away may see full 2.4GHz bars and zero 5GHz. Before changing anything, carry the laptop within a few meters of the router with clear line of sight and check whether the 5GHz network appears and connects. If it works up close, you have a coverage problem, not a laptop problem — consider router placement or a mesh node.

1. Move the laptop within 3 meters of the router, line of sight.
2. Check whether the 5GHz network now appears in the Wi-Fi list.
3. Try connecting — success here means it's a range issue.
4. If it still fails up close, the problem is settings or drivers — continue.

### Fix 3: Set the preferred band to 5GHz

The wireless adapter's driver has a "Preferred Band" setting that steers connections — and it's sometimes locked to 2.4GHz by default or by an update. Setting it to prefer 5GHz (or 5G first) makes the adapter actively seek the faster band. This single setting resolves the "laptop ignores 5GHz" complaint more often than any other fix.

1. In **Device Manager**, right-click the wireless adapter and choose **Properties**.
2. Open the **Advanced** tab and find **Preferred Band** in the property list.
3. Set its value to **Prefer 5GHz band** (or "5G first" depending on driver).
4. Click **OK**, disconnect from Wi-Fi, and reconnect — check which band it joins.

### Fix 4: Set the wireless mode to include 5GHz standards

The adapter's "Wireless Mode" or "802.11 mode" property controls which Wi-Fi standards it uses — and some settings exclude 5GHz-capable modes. Set it to a dual-band option like **802.11a/b/g/n/ac** or **Auto/Dual Band** rather than a 2.4GHz-only mode like 802.11b/g/n. The exact labels vary by driver (Intel, Realtek, and MediaTek all word it differently), but the dual-band option is always present on 5GHz-capable cards.

1. In the adapter's **Properties > Advanced** tab, find **Wireless Mode** (or 802.11 a/b/g).
2. Set it to the **dual-band** option (a/b/g/n/ac or Auto).
3. Avoid any option listing only b/g/n — those are 2.4GHz-only.
4. Click **OK** and re-scan for the 5GHz network.

### Fix 5: Update the wireless driver

Wireless drivers accumulate 5GHz bugs that get fixed in later releases — band-steering logic, channel compatibility, and handshake issues with newer routers. Download the latest wireless driver for your exact laptop model from the manufacturer's support site, or from Intel's driver assistant for Intel cards. Install it, restart, and retest the 5GHz connection. If 5GHz broke after a Windows update, try rolling back first instead.

1. Download the latest Wi-Fi driver for your exact model from the manufacturer's site.
2. In **Device Manager**, right-click the wireless adapter and choose **Update driver**, or run the installer.
3. Restart the laptop after installation.
4. Check whether the 5GHz network appears and connects reliably. If the adapter itself has vanished from Device Manager rather than just ignoring 5GHz, see our [Wi-Fi disappeared guide](/articles/wifi-disappeared-windows-11-no-wifi-option/).

### Fix 6: Forget the network and rejoin fresh

A corrupted saved network profile can lock the laptop into 2.4GHz behavior — Windows remembers band preferences per network. Forgetting the network wipes that memory. Go to **Settings > Network & Internet > Wi-Fi > Manage known networks**, forget your network, then reconnect by selecting the 5GHz SSID explicitly (if your router broadcasts separate names) and entering the password fresh.

1. Go to **Settings > Network & Internet > Wi-Fi > Manage known networks**.
2. Select your network and click **Forget**.
3. Click the Wi-Fi icon and select the **5GHz** network name explicitly.
4. Enter the password and connect — verify the band in the connection properties.

### Fix 7: Adjust the router's 5GHz settings

Sometimes the laptop is fine and the router is the problem. Log into your router's admin page and check: is the 5GHz radio actually enabled? Try changing the 5GHz channel (36, 40, 44, or 48 are usually safe), set channel width to 40MHz instead of 80/160MHz for compatibility, and disable "Smart Connect" band steering temporarily to test. Also update the router's firmware — manufacturers fix 5GHz client compatibility regularly. General network troubleshooting background is at [Windows support](https://support.microsoft.com/en-us/windows).

1. Log into your router's admin page (usually 192.168.1.1 or 192.168.0.1).
2. Verify the **5GHz radio** is enabled and broadcasting its SSID.
3. Try a different 5GHz **channel** and set width to **40MHz**.
4. Update the router firmware, then retest the laptop's 5GHz connection.

## Closing

Being stuck on 2.4GHz is usually a settings problem — the preferred-band toggle in Fix 3 alone restores 5GHz for most laptops. Verify hardware support first so you don't chase a software fix for a 2.4GHz-only card, then work the driver and router settings. The speed difference is worth the ten minutes: 5GHz is where your internet connection actually gets to stretch its legs.
