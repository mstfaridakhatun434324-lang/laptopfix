---
title: "Laptop Won't Connect to 5GHz Wi-Fi? What to Do First"
slug: what-to-do-if-laptop-not-connecting-to-wifi-5ghz
date: 2026-09-28
categories: ["drivers"]
tags: ["5ghz wifi", "wifi fix", "wireless adapter", "network", "windows 11"]
description: "Your laptop sees 2.4GHz but not 5GHz Wi-Fi? Diagnose band support, router settings, and driver issues with this practical troubleshooting guide."
thumbnail: "/images/thumbs/what-to-do-if-laptop-not-connecting-to-wifi-5ghz.webp"
faqs:
  - q: "Why can my laptop see 2.4GHz but not 5GHz networks?"
    a: "The most common reason is the wireless adapter's band setting or an outdated driver that mishandles 5GHz channels. Older or single-band adapters physically cannot see 5GHz at all. Check your adapter's specifications first, then verify the Preferred Band setting in the driver properties and confirm your router is actually broadcasting the 5GHz network with a distinct name."
  - q: "How do I know if my laptop supports 5GHz Wi-Fi?"
    a: "Open Device Manager, find your Wi-Fi adapter, and check its specifications on the manufacturer's site — look for 802.11a, 802.11ac, or 802.11ax support, all of which include 5GHz. In the driver's Advanced properties tab, a Preferred Band option with a 5GHz choice is a strong hint the hardware supports it. No 5GHz option usually means single-band hardware."
  - q: "Can a Windows update break 5GHz connectivity?"
    a: "Yes. Windows feature updates sometimes replace your wireless driver with a generic version that drops 5GHz support or misconfigures channel scanning. If 5GHz disappeared right after an update, roll the driver back in Device Manager or reinstall the manufacturer's driver. This pattern is documented in the Windows 11 24H2 Wi-Fi guides."
  - q: "Does distance from the router affect 5GHz more than 2.4GHz?"
    a: "Significantly. The 5GHz band is faster but has roughly half the range of 2.4GHz and penetrates walls poorly. If your laptop connects to 5GHz near the router but drops it from another room, that is physics, not a fault. Test within the same room before assuming the adapter or driver is broken."
---

Your phone connects to the 5GHz network just fine, your laptop sits on the slower 2.4GHz band — or worse, the 5GHz network doesn't appear in the list at all. It's maddening, because the laptop is supposedly the more capable device. The 5GHz band is where the speed lives: less congestion, wider channels, and real-world throughput that can be three to four times faster than 2.4GHz.

Before you buy a USB Wi-Fi dongle, understand that this problem is usually a configuration issue, not a hardware death sentence. The causes stack in a predictable order: the router might not be broadcasting properly, the adapter's band preference might be wrong, or the driver might be too old to handle modern 5GHz channels. Work through them in sequence and you'll find the break in the chain.

## Why this happens

- **Single-band adapter:** Some budget laptops ship with 2.4GHz-only wireless cards. No driver update can add a radio the hardware doesn't have.
- **Preferred Band set to 2.4GHz:** The driver's Advanced settings can pin the adapter to the 2.4GHz band, making the 5GHz network invisible even though the hardware supports it.
- **Outdated wireless driver:** Old drivers may not scan DFS channels (52–144) or handle newer 5GHz configurations, so the network never shows up in the list.
- **Router not broadcasting 5GHz:** The router's 5GHz radio can be disabled, set to an incompatible channel, or merged into a single SSID with band steering that parks your laptop on 2.4GHz.
- **Windows power management killing the radio:** Aggressive power saving can drop the 5GHz connection first because it draws more power than 2.4GHz.
- **Channel width mismatch:** If the router uses a channel width the adapter driver doesn't expect, the network may appear but refuse to connect.
- **Corrupted network profile:** A stale saved profile for the 5GHz SSID with an old password or security setting blocks connection even when the signal is strong.
- **Adapter failing at higher frequencies:** A dying wireless card sometimes loses 5GHz while 2.4GHz keeps working — the higher-frequency circuitry fails first.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your adapter supports 5GHz

1. Press **Win+X**, open **Device Manager**, and expand **Network adapters**.
2. Note your Wi-Fi adapter's exact model, then search its specs on the manufacturer's site (Intel, Realtek, MediaTek, or Qualcomm).
3. Look for **802.11ac**, **802.11ax**, or **Wi-Fi 5/6** — all support 5GHz. If it's 802.11b/g/n only, your hardware is 2.4GHz-only and a USB Wi-Fi adapter is the fix.
4. In the adapter's **Properties > Advanced** tab, look for **Preferred Band**. If present, set it to **Prefer 5GHz band**.

### Fix 2: Check the router's 5GHz broadcast

1. Log in to your router's admin page (usually `192.168.1.1` or `192.168.0.1`).
2. Verify the **5GHz radio is enabled** and broadcasting — give it a distinct SSID like `Home-5G` temporarily so you can see it clearly.
3. Set the 5GHz channel to **36, 40, 44, or 48** (non-DFS channels every adapter supports) and channel width to **80MHz** for the test.
4. Save, then check whether the network appears on the laptop. If it does, the router's channel selection was the issue — the detailed [step-by-step 5GHz guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-step-by-step/) covers advanced router tuning.

### Fix 3: Update the wireless driver

1. In Device Manager, right-click your Wi-Fi adapter and choose **Update driver > Search automatically for drivers**.
2. If Windows finds nothing, download the latest driver from your laptop manufacturer's support site (or Intel's driver page) for your exact model.
3. Install it, restart, and check for the 5GHz network again. Use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) if your card is Intel — it detects the exact chip and pulls the right package.

### Fix 4: Delete the stale network profile

1. Open **Settings > Network & internet > Wi-Fi > Manage known networks**.
2. Find your 5GHz network (or its combined SSID) and click **Forget**.
3. Reconnect from scratch, entering the password fresh. This clears corrupted security settings that silently block 5GHz connections.

### Fix 5: Disable power saving on the adapter

1. In Device Manager, right-click the Wi-Fi adapter, choose **Properties > Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power** and click OK.
3. Also go to **Settings > System > Power & battery** and set the power mode to **Best performance** while testing. If the adapter itself has vanished rather than just dropping 5GHz, the [missing network adapter guide](/articles/how-to-fix-network-adapter-missing-in-windows-11-24h2/) is the right next step.

### Fix 6: Reset the wireless stack

1. Open Terminal as administrator (**Win+X > Terminal (Admin)**).
2. Run these commands one by one, pressing Enter after each: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
3. Restart the laptop and try connecting to the 5GHz network again.

### Fix 7: Test with a USB Wi-Fi adapter

1. Borrow or buy an inexpensive dual-band USB Wi-Fi adapter.
2. Plug it in, let Windows install its driver, and connect to the 5GHz network through it.
3. If 5GHz works fine via USB, your internal card is the problem — either failing hardware or an unfixable driver situation — and replacing the internal card or using the USB adapter permanently are both valid solutions.

## Closing

A laptop that won't use 5GHz is almost always suffering from a settings mismatch rather than broken hardware: the wrong preferred band, an outdated driver, or a router broadcasting on channels the adapter can't see. Verify hardware support first so you don't chase a software fix for a physical limitation, then work the list. Once you're on 5GHz, the speed difference is immediate — and you'll wonder how you tolerated 2.4GHz for so long. Keep these settings documented so the next Windows update doesn't silently undo them.
