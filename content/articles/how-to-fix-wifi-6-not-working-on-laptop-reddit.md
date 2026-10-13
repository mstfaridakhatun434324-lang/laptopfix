---
title: "How to Fix Wi-Fi 6 Not Working on a Laptop"
slug: how-to-fix-wifi-6-not-working-on-laptop-reddit
date: 2026-10-01
categories: ["drivers"]
tags: ["wifi 6", "802.11ax", "slow wifi", "intel ax200", "wireless driver"]
description: "Wi-Fi 6 not working or slow on your laptop? Fix 802.11ax negotiation, update the wireless driver, and unlock full Wi-Fi 6 speeds."
thumbnail: "/images/thumbs/how-to-fix-wifi-6-not-working-on-laptop-reddit.webp"
faqs:
  - q: "Why is my Wi-Fi 6 laptop only getting Wi-Fi 5 speeds?"
    a: "The usual reasons are an outdated wireless driver that doesn't properly support 802.11ax, the router's AX mode disabled, or the laptop connecting on the 2.4GHz band instead of 5GHz. Check your link speed in Wi-Fi status — anything at or below 866 Mbps suggests you're on Wi-Fi 5 rates. Update the driver and prefer the 5GHz band."
  - q: "How do I know if I'm actually connected with Wi-Fi 6?"
    a: "In Windows, go to Settings, Network and internet, Wi-Fi, your network properties, and check the Protocol — it should say Wi-Fi 6 (802.11ax). You can also run netsh wlan show interfaces in Command Prompt and look at the Radio type line. If it says 802.11n or 802.11ac, you're not on Wi-Fi 6."
  - q: "Can an old driver prevent Wi-Fi 6 from working?"
    a: "Absolutely — this is the most common cause. Early drivers for AX200, AX201, and similar cards had broken or incomplete 802.11ax support, connecting at AC rates or dropping constantly. Intel fixed 802.11ax behavior across multiple driver generations, so running the latest driver from Intel or your laptop maker is essential for stable Wi-Fi 6."
  - q: "Does Wi-Fi 6 require a special router setting?"
    a: "Yes, the router must have 802.11ax mode enabled, which it is by default on Wi-Fi 6 routers but can be disabled in settings. Some routers also have AX-specific options like OFDMA and MU-MIMO toggles. If your laptop supports Wi-Fi 6 but never negotiates it, log into the router and confirm the wireless mode includes AX rather than being limited to AC or N."
---

Wi-Fi 6 (802.11ax) promises faster speeds, better congestion handling, and lower latency — but plenty of laptop owners with Wi-Fi 6 hardware never actually get a Wi-Fi 6 connection. The laptop connects, the internet works, but speeds match the old Wi-Fi 5 era, or the connection drops under load. The gap between "Wi-Fi 6 capable" and "Wi-Fi 6 connected" is almost always a driver or configuration issue, not hardware.

The fix sequence: verify what you're actually connected with, update the wireless driver to an AX-mature version, then align the router and adapter settings so 802.11ax negotiates properly.

## Why this happens

- **Outdated wireless driver:** Early AX drivers had incomplete 802.11ax support — the card connects but at Wi-Fi 5 rates or unstably.
- **Router AX mode disabled:** The access point isn't offering 802.11ax, so even perfect clients fall back.
- **Connected on 2.4GHz:** Many routers only offer AX on 5GHz; a 2.4GHz connection caps at older rates.
- **Driver configured to prefer older modes:** Adapter advanced settings can restrict the wireless mode below AX.
- **Channel width too narrow:** 20MHz channels cripple AX throughput; AX needs 80MHz (or 160MHz) to shine.
- **Roaming aggressiveness causing drops:** Overly aggressive roaming on AX networks causes disconnect loops mistaken for "Wi-Fi 6 not working."
- **Firmware mismatch between card and router:** Specific card/router combinations have known AX negotiation bugs fixed in later firmware on either side.
- **Power saving throttling the radio:** Aggressive power management prevents the card from sustaining AX rates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify your actual connection type

1. Open **Settings → Network & internet → Wi-Fi**, click your network, and check **Protocol** — you want **Wi-Fi 6 (802.11ax)**.
2. For detail, open Command Prompt and run `netsh wlan show interfaces` — check the **Radio type** line.
3. Note the **Receive/Transmit rate**: AX connections on 80MHz channels typically show 1200 Mbps+ link rates.
4. If Protocol says Wi-Fi 5 (802.11ac) or lower, you're not on Wi-Fi 6 despite the hardware — continue with the fixes.
5. This baseline matters: many "Wi-Fi 6 not working" complaints are actually "connected but at AC rates," a driver/negotiation issue rather than a dead radio. The same verification applies to [Intel AX201-specific problems](/articles/best-way-to-fix-intel-wifi-6-ax201-not-working/).

### Fix 2: Update the wireless driver to an AX-mature version

1. Identify your card in Device Manager → **Network adapters** (Intel AX200/AX201/AX210, MediaTek MT7921, Qualcomm, Realtek).
2. For Intel cards, run [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) and install the latest wireless driver — Intel's AX support matured significantly across driver generations.
3. For other cards, get the driver from your laptop maker's support page ([Dell](https://www.dell.com/support)).
4. Restart and recheck the Protocol — a proper AX driver is the single biggest factor in negotiating 802.11ax.
5. If Windows Update keeps downgrading you to an older driver, block driver updates for the wireless device so your working version sticks. The [Wi-Fi driver reinstall guide](/articles/best-way-to-reinstall-wifi-driver/) covers the clean-install method when a simple update isn't enough.

### Fix 3: Confirm the router offers 802.11ax

1. Log into your router's admin page and open the wireless settings.
2. Verify the **Wireless Mode** includes **AX** (settings like "AX/AC/N mixed" or "Wi-Fi 6 mode enabled").
3. Check for AX-specific features (**OFDMA**, **MU-MIMO**, **TWT**) and leave them enabled unless troubleshooting a specific incompatibility.
4. If your router is Wi-Fi 5 only, no laptop setting will create a Wi-Fi 6 connection — the access point defines the ceiling.
5. Update the router's firmware; vendors have fixed numerous AX negotiation bugs in updates.

### Fix 4: Force the 5GHz band

1. In Device Manager, open your Wi-Fi adapter's **Properties → Advanced** tab.
2. Set **Preferred Band** to **5GHz** (or "Prefer 5GHz band").
3. Alternatively, in the router, give the 5GHz network a distinct SSID and connect the laptop to it directly.
4. Recheck the Protocol — AX on most consumer routers is a 5GHz-only affair, and band steering sometimes parks clients on 2.4GHz.
5. If 5GHz signal is weak where you work, consider router placement or a mesh node rather than accepting 2.4GHz fallback.

### Fix 5: Set channel width to Auto or 80MHz

1. In the adapter's **Advanced** tab, find **802.11a/b/g Wireless Mode** or **VHT Mode** / **Channel Width for 5GHz**.
2. Set channel width to **Auto** (which allows 80MHz) rather than a fixed 20MHz.
3. In the router, set the 5GHz channel width to **80MHz** (or Auto including 80MHz).
4. Retest speed — narrow channels are a silent AX killer, capping throughput at a fraction of the card's capability.
5. Only use 160MHz if both the card and router support it stably; 160MHz is more interference-prone and can reduce reliability.

### Fix 6: Tune roaming and power settings

1. In the adapter's **Advanced** tab, set **Roaming Aggressiveness** to **3. Medium** — the highest setting causes disconnect loops on some AX access points.
2. In **Power Management**, uncheck **Allow the computer to turn off this device to save power**.
3. In **Power Options → Wireless Adapter Settings → Power Saving Mode**, set **Maximum Performance** for both profiles.
4. Set **Transmit Power** to **Highest** in the Advanced tab if available.
5. Retest stability over an hour of use. AX disconnect loops that look like driver bugs are frequently just hyperactive roaming plus power saving.

### Fix 7: Reset the network stack and retest

1. Run in an elevated Command Prompt: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /flushdns`, then restart.
2. Forget the Wi-Fi network (**Settings → Network & internet → Wi-Fi → Manage known networks**) and reconnect fresh, re-entering the password.
3. This clears corrupted wireless profiles that can force fallback to older protocols.
4. After reconnecting, verify the Protocol shows Wi-Fi 6 again.
5. If the fresh profile negotiates AX but the old one didn't, a corrupted profile was the culprit all along.

### Fix 8: Isolate card vs. router with a second network

1. Test the laptop against a different Wi-Fi 6 router or a phone hotspot (note: hotspots are usually AC, so this tests general wireless health, not AX).
2. Test a different Wi-Fi 6 device against your router — if it also fails to negotiate AX, the router is the problem.
3. Check vendor forums for your specific card+router combination; some pairings (particular Intel cards with particular router chipsets) have documented AX bugs with documented firmware fixes.
4. Update both sides' firmware before concluding incompatibility.
5. As a last resort, a USB Wi-Fi 6 adapter with a different chipset sidesteps a fundamentally incompatible built-in card — inelegant but effective.

## Closing

Wi-Fi 6 failures are negotiation failures: the driver, the router, and the band have to agree on 802.11ax, and any weak link drops you to older rates or unstable connections. Update the wireless driver to an AX-mature version, confirm the router offers AX on 5GHz with wide channels, and tame roaming and power settings. Verify with the Protocol readout — "Wi-Fi 6 (802.11ax)" is the receipt that proves the fix worked.
