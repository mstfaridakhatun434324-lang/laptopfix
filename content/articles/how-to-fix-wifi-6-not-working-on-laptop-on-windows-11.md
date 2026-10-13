---
title: "Wi-Fi 6 Not Working on a Laptop on Windows 11? 7 Fixes That Work"
slug: how-to-fix-wifi-6-not-working-on-laptop-on-windows-11
date: 2026-09-09
categories: ["drivers"]
tags: ["wifi 6", "802.11ax", "windows 11", "wireless", "intel"]
description: "Wi-Fi 6 (802.11ax) not working on your Windows 11 laptop? 7 fixes — driver updates, AX mode settings, and router tweaks for full Wi-Fi 6 speeds."
thumbnail: "/images/thumbs/how-to-fix-wifi-6-not-working-on-laptop-on-windows-11.webp"
faqs:
  - q: "How do I know if my laptop actually supports Wi-Fi 6?"
    a: "Check your wireless adapter model in Device Manager — Intel AX200, AX201, AX210, and Killer AX cards support Wi-Fi 6, while older AC8265 or AC9560 cards top out at Wi-Fi 5. Run 'netsh wlan show drivers' in Command Prompt and look for 802.11ax in the radio types. If ax isn't listed, your hardware caps at Wi-Fi 5 and no setting will change that."
  - q: "Why is my Wi-Fi 6 laptop only connecting at Wi-Fi 5 speeds?"
    a: "The connection negotiates down to the lowest common capability. If the router isn't Wi-Fi 6, if the laptop's 802.11ax mode is disabled in the driver, or if the router's AX features are turned off, you get Wi-Fi 5 speeds on Wi-Fi 6 hardware. Both ends must have AX enabled and compatible for the faster standard to engage."
  - q: "Do I need a Wi-Fi 6 router to benefit from a Wi-Fi 6 laptop?"
    a: "Yes, for Wi-Fi 6 speeds specifically — the standard only applies to the laptop-router link, and both sides must support 802.11ax. A Wi-Fi 6 laptop on a Wi-Fi 5 router connects at Wi-Fi 5 speeds (still fast, just not AX). The laptop's AX capability also improves efficiency slightly on older routers, but the headline speeds need an AX router."
  - q: "Can Windows 11 updates break Wi-Fi 6 functionality?"
    a: "They can. Updates sometimes replace the Intel wireless driver with a version that has 802.11ax disabled by default or contains AX handshake bugs with certain routers. If Wi-Fi 6 worked and stopped after an update, check the driver's 802.11a/b/g wireless mode setting first, then consider rolling back or reinstalling Intel's driver."
---

Your laptop has a Wi-Fi 6 card, your router broadcasts Wi-Fi 6, but the connection stubbornly runs at Wi-Fi 5 speeds — or the 802.11ax mode won't engage at all. Wi-Fi 6 (802.11ax) promises faster throughput, better congestion handling, and improved battery life, but it only works when the laptop's driver, the router, and Windows 11 all agree to use it. One weak link and you silently drop to older standards.

The tricky part: nothing looks broken. You connect, the internet works, speeds are merely... fine. You have to check the link speed and radio type to even notice you're not on AX. The seven fixes below verify your hardware, enable AX mode properly, and fix the driver issues that keep Wi-Fi 6 switched off. For Intel AX201-specific problems, our [Intel AX201 guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) goes deeper on that card.

## Why this happens

- **802.11ax mode is disabled in the driver** — the adapter's wireless mode setting excludes the AX standard.
- **The wireless driver is outdated** — old drivers have AX handshake bugs or lack AX features entirely.
- **The router's Wi-Fi 6 features are off** — AX disabled on the router, or incompatible settings like WPA3-only.
- **A Windows update replaced the Intel driver** — the new driver defaults AX off or breaks AX negotiation.
- **Channel width is too narrow** — 20/40MHz widths cap throughput well below Wi-Fi 6 potential.
- **OFDMA or MU-MIMO disabled on the router** — the headline AX features are switched off router-side.
- **Power management throttles the adapter** — aggressive saving prevents the card from sustaining AX rates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify Wi-Fi 6 hardware on both ends

Confirm the laptop actually has an AX-capable card: run `netsh wlan show drivers` and look for **802.11ax** in radio types. Intel AX200/AX201/AX210 and Killer AX-series cards qualify. Then confirm the router is Wi-Fi 6 — check its model specs or admin page. If either end lacks AX, you're done diagnosing: the connection correctly runs at the lower standard, and no laptop setting changes physics.

1. Run `netsh wlan show drivers` in **Command Prompt**.
2. Look for **802.11ax** in **Radio types supported**.
3. Check your router's model specifications for Wi-Fi 6 / 802.11ax support.
4. If both support AX, continue — the problem is configuration.

### Fix 2: Enable 802.11ax in the adapter's wireless mode

The adapter's driver has a wireless mode property that gates which standards it uses — and AX is sometimes excluded by default or after updates. In Device Manager, open the wireless adapter's Properties > Advanced tab, find **802.11a/b/g Wireless Mode** (Intel's label) or **Wireless Mode**, and set it to the option including **ax** (e.g., "802.11a/b/g/n/ac/ax" or "6. Dual Band 802.11a/b/g/n/ac/ax"). This is the single most common fix.

1. In **Device Manager**, open the wireless adapter's **Properties > Advanced** tab.
2. Find **802.11a/b/g Wireless Mode** (or Wireless Mode) in the property list.
3. Set the value to the option that includes **ax** (dual-band a/b/g/n/ac/ax).
4. Click **OK**, disconnect, and reconnect to Wi-Fi.

### Fix 3: Check the actual connection radio type

Don't guess — measure. After connecting, run `netsh wlan show interfaces` and check the **Radio type** field: it should say **802.11ax** when Wi-Fi 6 is active. Also note the **Receive/Transmit rate** — AX connections on 80MHz channels typically show 1200 Mbps or higher link rates. If it says 802.11ac, AX isn't engaging, and you know the remaining fixes are still needed. Our [5GHz guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/) covers band-specific issues that overlap here.

1. Connect to your Wi-Fi 6 network.
2. Run `netsh wlan show interfaces` in **Command Prompt**.
3. Check **Radio type** — you want **802.11ax**, not 802.11ac.
4. Note the link rate — healthy AX shows 1200+ Mbps on 80MHz channels.

### Fix 4: Update the Intel wireless driver

Intel's wireless drivers get regular AX fixes — handshake compatibility, OFDMA behavior, and power management tuning. Download the latest Wi-Fi driver for your card from Intel's driver support page or use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to detect and install it automatically. Restart after installing and re-check the radio type. If AX broke after a Windows update, roll back first, then install Intel's version.

1. Run the Intel Driver & Support Assistant or download the Wi-Fi driver manually.
2. Install the latest driver for your AX card and restart.
3. Re-check the adapter's wireless mode setting — updates sometimes reset it.
4. Run `netsh wlan show interfaces` again to verify 802.11ax.

### Fix 5: Set channel width to Auto or 80MHz

The adapter's "HT Mode" or "Channel Width" setting caps throughput: 20MHz-only means Wi-Fi 6 speeds are impossible regardless of AX mode. In the adapter's Advanced properties, set **802.11n/ac/ax channel width** (or VHT Mode / HT Mode) to **Auto** — this lets the card negotiate the widest channel the router offers. On the router side, set the 5GHz channel width to 80MHz (or 160MHz if both devices support it cleanly).

1. In the adapter's **Properties > Advanced**, find the channel width / HT Mode setting.
2. Set it to **Auto** (not 20MHz only).
3. On the router admin page, set 5GHz channel width to **80MHz**.
4. Reconnect and verify the link rate improved.

### Fix 6: Tune the router's Wi-Fi 6 settings

Log into the router and verify its AX features are actually on: **802.11ax mode** enabled, **OFDMA** enabled, **MU-MIMO** enabled, and security set to **WPA2/WPA3 mixed** (WPA3-only breaks some older AX handshakes; WEP/WPA break AX entirely). Update the router firmware — vendors fix AX client compatibility constantly. After changes, restart the router and reconnect the laptop fresh.

1. Log into the router admin page and find the wireless/AX settings.
2. Enable **802.11ax mode**, **OFDMA**, and **MU-MIMO** if present.
3. Set security to **WPA2/WPA3** (not WEP, not WPA-only, not WPA3-only for testing).
4. Update router firmware, restart the router, and reconnect the laptop.

### Fix 7: Disable power saving on the wireless adapter

Windows' power management can prevent the AX card from sustaining Wi-Fi 6 rates — the card drops to lower modes to save power. In the adapter's Properties > Power Management tab, uncheck "allow the computer to turn off this device." Also set the wireless adapter's **Power Saving Mode** (in Advanced properties) to **Maximum Performance**. Test on AC power first to isolate battery-related throttling.

1. In the adapter's **Properties > Power Management**, uncheck the power-off option.
2. In **Advanced**, set **Power Saving Mode** to **Maximum Performance**.
3. Test on AC power with `netsh wlan show interfaces` to check the radio type.
4. If AX engages on AC but not battery, adjust the power plan's wireless settings.

## Closing

Wi-Fi 6 not engaging is a negotiation failure — the AX mode setting, the driver version, and the router's AX features all have to line up. The wireless-mode toggle in Fix 2 is the culprit most of the time; the driver update and router tuning cover the rest. Verify with `netsh wlan show interfaces` rather than trusting vibes — when it says 802.11ax, you're actually getting what you paid for.
