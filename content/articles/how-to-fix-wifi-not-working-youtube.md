---
title: "How to Fix Wi-Fi Not Working: Video Walkthrough Companion Guide"
slug: how-to-fix-wifi-not-working-youtube
date: 2026-10-04
categories: ["drivers"]
tags: ["wifi not working", "wireless fix", "video guide", "network adapter", "windows 11"]
description: "Follow along with video-style Wi-Fi repair steps: a written companion that mirrors what tutorials show, so you can fix dead Wi-Fi even while offline."
thumbnail: "/images/thumbs/how-to-fix-wifi-not-working-youtube.webp"
faqs:
  - q: "I cannot watch a video tutorial because my Wi-Fi is down. What do I do?"
    a: "That is exactly why this written guide exists — every step is described in text so you can follow it on the broken laptop itself or on your phone. Start with the physical checks and work down the list. If you have mobile data, you can also download the manufacturer's Wi-Fi driver to your phone and transfer it by USB."
  - q: "Why do video tutorials always start with restarting the router?"
    a: "Because it genuinely fixes a large share of Wi-Fi problems. Routers run for months and their firmware gets into bad states; a power cycle clears stuck DHCP leases and hung radios. It is the highest-probability, lowest-effort step, so every competent tutorial — and this guide — puts it first."
  - q: "The tutorial I watched says to reset the network stack. Is that safe?"
    a: "Yes. Commands like netsh winsock reset and netsh int ip reset only clear network configuration back to defaults; they do not delete files or programs. You will need to re-enter Wi-Fi passwords afterward, so have them handy. It is one of the safest advanced steps in Wi-Fi troubleshooting."
  - q: "What if none of the video steps bring my Wi-Fi back?"
    a: "Then the fault is likely the wireless card or its antenna connections. Run the manufacturer's hardware diagnostics wireless test, check that the Wi-Fi adapter appears in Device Manager, and inspect the BIOS wireless setting. A USB Wi-Fi adapter is a cheap workaround while you arrange a card replacement."
---

Video tutorials are great for Wi-Fi repair — you can see exactly which menus to open. But there is a cruel irony: the people who need them most cannot get online to watch them. This guide is the written companion to those walkthroughs. It follows the same sequence a good video tutorial would — router, toggles, adapter, drivers, stack reset — with every click described in text so you can work through it on the dead laptop or from your phone's screen.

Keep this page open on your phone if the laptop is fully offline. Each section tells you what a tutorial would show you, in the order it would show it.

## Why this happens

- **Router in a bad state:** Home routers accumulate stuck sessions and DHCP glitches over weeks of uptime; a power cycle clears them.
- **Airplane mode or wireless switch:** A stuck airplane mode or a physical switch kills the radio before Windows networking is even involved.
- **Corrupted Wi-Fi driver:** Updates can replace the working wireless driver with a generic or mismatched one that fails to connect.
- **Wrong network profile:** A changed router password or security mode leaves Windows retrying with stale credentials forever.
- **TCP/IP stack corruption:** Malware, VPN clients, and bad updates can corrupt the Winsock and IP stack so no network works.
- **Power management disabling the adapter:** Aggressive power saving can shut the Wi-Fi card down and fail to wake it.
- **Failing wireless card or antennas:** Loose antenna leads or a dying card produce the classic "works for five minutes then drops" pattern.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Power-cycle the router and modem

Unplug the power from both your modem and router. Wait a full 60 seconds — this matters, because capacitors keep the hardware half-alive for shorter gaps. Plug the modem back in first, wait for its lights to stabilize (two to three minutes), then plug in the router and wait another two minutes. Meanwhile, restart your laptop. When everything is back, try connecting. This resolves a remarkable share of "Wi-Fi stopped working" cases because it clears the router's stuck state rather than anything on your laptop. If other devices connect fine but yours does not, the router is innocent — continue down the list.

### Fix 2: Check airplane mode, Wi-Fi toggle, and physical switches

Press Win + A to open Quick Settings and verify airplane mode is off and Wi-Fi is on. If airplane mode is stuck and will not turn off, follow our dedicated guide for [fixing airplane mode stuck on](/articles/how-do-i-fix-airplane-mode-stuck-on/). Check your laptop for a physical wireless switch on the side or an Fn-key wireless toggle — cycle it once. Then go to Settings, Network & internet, Wi-Fi, and confirm Wi-Fi is enabled there too. These checks take a minute and eliminate the entire class of "radio is simply off" problems that no driver reinstall will fix.

### Fix 3: Forget the network and reconnect fresh

If Wi-Fi is on but your network will not connect, the saved profile may hold a stale password or security setting. Go to Settings, Network & internet, Wi-Fi, Manage known networks, select your network, and choose Forget. Restart the laptop, then reconnect by selecting the network and typing the current password carefully. This clears corrupted profile data that causes endless "can't connect to this network" loops after a router password change or security-mode switch. If you manage the router, confirm its security is set to WPA2 or WPA3 — ancient WEP or WPA modes can refuse modern Windows clients outright.

### Fix 4: Restart the WLAN AutoConfig service

Press Win + R, type `services.msc`, and find WLAN AutoConfig. If it is stopped, right-click and start it; set its Startup type to Automatic. This service is the engine behind Wi-Fi scanning and connecting — without it, the network list is empty no matter what the driver does. VPN clients and "optimizer" utilities sometimes disable it. While you are in Services, also confirm the Network Connections and Network Location Awareness services are running. A quick service restart here fixes the otherwise baffling symptom of Wi-Fi hardware that looks fine but shows no networks at all.

### Fix 5: Reinstall the Wi-Fi adapter driver

Open Device Manager (Win + X), expand Network adapters, right-click your Wi-Fi adapter, and choose Uninstall device — check "delete the driver software" if offered. Restart; Windows will redetect the adapter and install a driver. If the adapter is missing from the list, enable Show hidden devices under View and look for it greyed out or under Other devices. After reinstalling, test the connection before updating anything else. If the adapter never appears, our guide to [fixing a missing network adapter](/articles/how-to-fix-network-adapter-missing/) covers the deeper recovery. For the proper long-term driver, grab the OEM Wi-Fi package from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) once you have any connection — even phone-tethered — available.

### Fix 6: Reset the TCP/IP stack and Winsock

Open Terminal or Command Prompt as administrator (right-click Start, Terminal (Admin)) and run these commands in order, pressing Enter after each: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`. Then restart the laptop. This rebuilds the network stack from defaults, clearing corruption from VPN clients, malware, or failed updates that leaves the adapter "connected" with no actual traffic. You will need to re-enter Wi-Fi passwords afterward, so have them ready. This is the step most video tutorials demonstrate around the middle, and it is safe — it touches network configuration only.

### Fix 7: Disable power management and test the hardware

In Device Manager, right-click the Wi-Fi adapter, open Properties, and on the Power Management tab uncheck "Allow the computer to turn off this device to save power." Test on mains power with the power mode set to Best performance. If Wi-Fi now stays up, power management was the culprit. If it still drops, run the manufacturer's hardware diagnostics wireless test and check the BIOS for a wireless enable option. A card that fails diagnostics needs reseating or replacement — and as a stopgap, a USB Wi-Fi adapter costs little and gets you online immediately. Microsoft's Windows support hub documents additional wireless diagnostics if you want the official reference steps.

## Closing

Every good Wi-Fi tutorial follows the same arc — router, radio, profile, service, driver, stack, hardware — because that is the order of probability. Work it in text form right here, and you will fix the same problems the videos fix, no streaming required. And once you are back online, install the manufacturer's Wi-Fi driver so the next update does not knock you offline again.
