---
title: "Fix a Laptop That Won't Connect to 5GHz Wi-Fi on Windows 10"
slug: how-to-fix-laptop-not-connecting-to-wifi-5ghz-on-windows-10
date: 2026-10-13
categories: ["drivers"]
tags: ["5ghz wifi", "wifi not connecting", "windows 10", "wireless adapter", "802.11ac"]
description: "Fix Windows 10 laptops that can't see or join 5GHz Wi-Fi networks: band capability checks, adapter driver repair, and router settings."
thumbnail: "/images/thumbs/how-to-fix-laptop-not-connecting-to-wifi-5ghz-on-windows-10.webp"
faqs:
  - q: "Why can't my Windows 10 laptop see 5GHz networks?"
    a: "Either the wireless adapter only supports 2.4GHz (common on older laptops), the driver has the 5GHz band disabled, or the router's 5GHz radio uses a channel or width the adapter cannot use. Check the adapter's supported bands in Device Manager first."
  - q: "How do I know if my Wi-Fi adapter supports 5GHz?"
    a: "Open Device Manager, then Network adapters, then your Wi-Fi adapter Properties, then the Advanced tab. Look for Preferred Band or VHT Mode settings — their presence indicates 5GHz capability. Or run netsh wlan show drivers and check Radio types supported."
  - q: "Can a driver update add 5GHz support?"
    a: "No. 5GHz support is physical hardware — the radio chipset must be built for the 5GHz band. A driver update can only repair a 5GHz-capable adapter whose band was disabled in settings or broken by a bad driver install; it cannot add a radio frequency the hardware does not have."
  - q: "Why does 5GHz connect but keep dropping?"
    a: "Drops on a connected 5GHz network usually mean weak signal at your location — 5GHz has shorter range and poorer wall penetration than 2.4GHz — or DFS channel radar interference forcing channel switches, or aggressive roaming between access points. Move closer to the router, switch the router off DFS channels to 36 through 48, or fall back to 2.4GHz if the laptop sits far away."
---

A Windows 10 laptop that cannot see or join 5GHz networks falls into two buckets: hardware that never supported 5GHz, and hardware that does but is blocked by drivers or settings. The distinction matters because no amount of driver work adds 5GHz to a 2.4GHz-only radio — but a huge share of these cases are actually capable adapters with the band disabled, a broken driver, or a router broadcasting on settings the adapter cannot use.

Start by establishing capability, then work the software chain. The checks below take you from "is 5GHz even possible on this machine" through driver repair to the router-side settings that most often block capable laptops.

## Why this happens

- **Adapter hardware is 2.4GHz-only:** Older or budget laptops ship single-band radios; 5GHz is physically impossible on them.
- **5GHz band disabled in driver settings:** The adapter's Advanced properties can have the band forced to 2.4GHz.
- **Corrupted or outdated wireless driver:** A bad driver can fail to initialize the 5GHz radio while 2.4GHz keeps working.
- **Router using incompatible channel/width:** DFS channels or 160MHz widths the adapter does not support make the network invisible to it.
- **Band steering confusion:** Router band-steering features can push the laptop to 2.4GHz or hide the 5GHz SSID from the scan list.
- **Preferred band set to 2.4GHz:** The driver's Preferred Band setting can be locked to 2.4GHz, ignoring 5GHz networks.
- **Power management disabling the 5GHz radio:** Aggressive power saving can shut down the higher-power 5GHz radio chain.
- **Windows 10 wireless stack corruption:** Damaged WLAN profiles or stack state after updates block 5GHz association specifically.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the adapter actually supports 5GHz

1. Open an elevated Command Prompt and run `netsh wlan show drivers`.
2. Check **Radio types supported** — look for **802.11a**, **802.11ac**, or **802.11ax**. Presence of 802.11a/ac/ax means 5GHz hardware exists; only 802.11b/g/n means 2.4GHz-only.
3. In **Device Manager → Network adapters → Wi-Fi adapter → Properties → Advanced**, look for **Preferred Band**, **VHT Mode**, or **802.11a/b/g Wireless Mode** entries.
4. If the hardware is 2.4GHz-only, the fix is a USB Wi-Fi adapter with 5GHz support — no software step changes the radio. If 5GHz hardware exists, continue.

### Fix 2: Set the preferred band to 5GHz

1. In the adapter's **Advanced** tab, set **Preferred Band** to **Prefer 5GHz band** (or **5G first**).
2. Set **VHT Mode** to **Enabled** if present.
3. Set **802.11a/b/g Wireless Mode** to a value including **a** (e.g., **Dual Band 802.11a/b/g**).
4. Click OK and rescan for networks. A band forced to 2.4GHz is one of the most common causes and takes thirty seconds to fix.

### Fix 3: Reinstall the wireless driver

1. Identify your adapter (Intel, Realtek, Qualcomm) in Device Manager.
2. Download the Wi-Fi driver for your exact model from the laptop vendor — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — or the chip maker ([Intel](https://www.intel.com/content/www/us/en/support/detect.html) for Intel adapters).
3. In Device Manager, right-click the Wi-Fi adapter → **Uninstall device** (check **Attempt to remove the driver**), reboot, then install the downloaded driver.
4. Rescan. Driver corruption that kills only the 5GHz radio is common after Windows updates, and the same repair logic applies to other wireless faults like those in the [Intel AX201 fix guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/).

### Fix 4: Adjust the router's 5GHz settings

1. Log into your router and check the 5GHz radio: ensure it is **enabled** and broadcasting its SSID (or note the SSID if hidden).
2. Set the channel to a non-DFS channel (**36–48** or **149–161**) — some adapters cannot use DFS channels (52–144).
3. Set channel width to **80MHz** or **20/40/80 auto** instead of 160MHz, which older 5GHz adapters do not support.
4. If the router merges bands under one SSID (band steering), temporarily split them into separate 2.4GHz and 5GHz SSIDs to test.

### Fix 5: Disable power management on the wireless adapter

1. **Device Manager → Network adapters → Wi-Fi adapter → Properties → Power Management** → uncheck **Allow the computer to turn off this device to save power**.
2. In the **Advanced** tab, set **Transmit Power** to **Highest** and **Power Saving Mode** to **Maximum Performance**.
3. **Settings → System → Power & sleep →** set the power plan to **Best performance** while testing.
4. Power saving disproportionately affects the 5GHz radio because it draws more power than 2.4GHz.

### Fix 6: Reset the wireless stack and profiles

1. Elevated Command Prompt: `netsh wlan delete profile name="Your5GHzSSID"` to remove a corrupted saved profile, then reconnect fresh.
2. For a full reset: `netsh winsock reset` and `netsh int ip reset`, then reboot.
3. Or **Settings → Network & Internet → Status → Network reset** — this reinstalls adapters and clears all profiles, so reinstall the vendor Wi-Fi driver afterward if needed.
4. Microsoft documents wireless troubleshooting in [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 7: Rule out hardware and consider a USB adapter

1. Boot a Linux live USB and scan for 5GHz networks — visible in Linux but not Windows means a Windows driver problem; invisible in both means hardware or router.
2. Test near the router to rule out range: 5GHz fades fast through walls.
3. If the internal radio is truly 2.4GHz-only or faulty, a USB Wi-Fi 6 adapter ($15–25) adds full 5GHz/6GHz support — disable the internal adapter in Device Manager to avoid conflicts.

## Closing

The 5GHz question always starts with capability: `netsh wlan show drivers` tells you in ten seconds whether the hardware can do it. The Windows 11 version of this problem has its own wrinkles — see the [Windows 11 5GHz guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/) if you support both operating systems. From there it is settings (preferred band, VHT mode), driver health, and router channel/width compatibility — in that order.
