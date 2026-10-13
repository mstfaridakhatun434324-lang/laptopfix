---
title: "How to Fix Wi-Fi 6 Not Working on a Laptop Running Windows 10"
slug: "how-to-fix-wifi-6-not-working-on-laptop-on-windows-10"
date: "2026-09-21"
categories: ["drivers"]
tags: ["wifi 6", "802.11ax", "windows 10", "wireless driver", "slow wifi"]
description: "Wi-Fi 6 not working or slow on Windows 10? Fix driver support for 802.11ax, router compatibility settings, and band configuration step by step."
thumbnail: "/images/thumbs/how-to-fix-wifi-6-not-working-on-laptop-on-windows-10.webp"
faqs:
  - q: "Does Windows 10 fully support Wi-Fi 6?"
    a: "Windows 10 supports Wi-Fi 6 (802.11ax) starting from version 2004, but only with a compatible wireless driver — the OS support means nothing if the driver does not implement 802.11ax properly. Many early Wi-Fi 6 driver releases for Windows 10 were buggy, causing slow speeds or disconnects. Updating to the latest driver from your laptop maker or Intel is the single most important step for Windows 10 Wi-Fi 6 reliability."
  - q: "My laptop connects but Wi-Fi 6 speeds are slow on Windows 10. Why?"
    a: "Slow Wi-Fi 6 on Windows 10 is usually a driver or configuration issue: an outdated driver negotiating a lower standard, the adapter's 802.11ax mode disabled in Advanced settings, the router using incompatible settings like WPA3-only or 160 MHz channels the card handles poorly, or Windows power management throttling the adapter. Checking the actual connection standard in the Wi-Fi status window tells you what the laptop negotiated."
  - q: "How do I check if my laptop is actually using Wi-Fi 6?"
    a: "Open Settings > Network & Internet > Wi-Fi, click your connected network, and look at the protocol or standard field — it should say Wi-Fi 6 (802.11ax). Alternatively, open Command Prompt and run netsh wlan show interfaces, which lists the radio type. If it shows 802.11n or 802.11ac instead of ax, the laptop fell back to an older standard, and the fixes in this guide address exactly that."
  - q: "Should I upgrade to Windows 11 for better Wi-Fi 6 support?"
    a: "Windows 11 has more mature Wi-Fi 6 and 6E support, including better WPA3 handling and newer inbox drivers, so an upgrade can help if your hardware qualifies. But most Windows 10 Wi-Fi 6 problems are fixed by a driver update alone, without reinstalling the OS. Try the driver and router fixes here first — upgrade to Windows 11 only if problems persist or you want Wi-Fi 6E's 6 GHz band, which Windows 10 barely supports."
---

Wi-Fi 6 (802.11ax) promises faster speeds, better crowded-network performance, and lower latency — but on Windows 10 laptops it often arrives as a disappointment: the laptop connects to a Wi-Fi 6 router yet negotiates an older standard, crawls at a fraction of expected speed, or disconnects under load. The hardware is usually fine. Windows 10's Wi-Fi 6 support depends heavily on having a mature driver, and early or generic drivers are where most of these problems live.

This guide focuses on the Windows 10-specific side of Wi-Fi 6 trouble: driver support for 802.11ax, adapter settings, and the router compatibility quirks that trip up older driver builds. If your Wi-Fi is missing entirely rather than misbehaving, start with our [general Wi-Fi disappeared guide](/articles/how-to-fix-wifi-disappeared-from-laptop-on-windows-11/) instead.

## Why this happens

- **Outdated wireless driver:** Early Wi-Fi 6 drivers for Windows 10 had immature 802.11ax implementations with speed and stability bugs.
- **802.11ax mode disabled:** The adapter's Advanced settings may have the ax/HE mode switched off, forcing fallback to 802.11ac.
- **Router settings the driver dislikes:** WPA3-only security, 160 MHz channel width, or OFDMA features can break older Windows 10 drivers.
- **Windows 10 version too old:** Builds before version 2004 lack proper Wi-Fi 6 framework support regardless of driver.
- **Power management throttling:** The adapter dropping to low-power states kills the throughput Wi-Fi 6 is supposed to deliver.
- **Generic Windows driver:** The inbox driver may connect fine but never enable the full ax feature set.
- **Band steering confusion:** The laptop bouncing between 2.4 GHz and 5 GHz produces the classic fast-then-slow pattern.
- **Failing back due to interference:** In noisy environments the card drops to older standards for stability — sometimes permanently until reset.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm what standard you are actually getting

Measure before you fix — you need a baseline.

1. Connect to your Wi-Fi 6 network, then open Command Prompt and run `netsh wlan show interfaces`.
2. Note the "Radio type" — 802.11ax means Wi-Fi 6 is active; 802.11ac or n means fallback.
3. Note the receive/transmit rates — Wi-Fi 6 on an 80 MHz channel should show well above 500 Mbps link rate.
4. Run an internet speed test and compare against what the same network delivers to a phone or another device.
5. If the radio type is already ax but speeds are slow, the issue is configuration or interference, not standard negotiation.

### Fix 2: Update Windows 10 to a supported build

Wi-Fi 6 needs a new enough Windows 10 underneath the driver.

1. Open Settings > System > About and check your Windows 10 version — you need 2004 or later, ideally 22H2.
2. Go to Settings > Update & Security > Windows Update and install all available updates.
3. After updating, recheck `netsh wlan show interfaces` — the framework update alone sometimes unlocks ax negotiation.
4. If Windows Update offers a newer wireless driver during this process, let it install, then test before replacing it with the manufacturer's version.

### Fix 3: Install the latest manufacturer wireless driver

This is the fix that resolves most Windows 10 Wi-Fi 6 problems.

1. In Device Manager, note your exact wireless adapter model under Network adapters.
2. Download the newest Windows 10 driver for your laptop model from the manufacturer's support site.
3. In Device Manager, uninstall the current wireless driver with "Attempt to remove the driver" ticked.
4. Install the downloaded package, restart, and recheck the radio type with `netsh wlan show interfaces`.
5. Intel adapter owners can also use the official [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to pull the latest Wi-Fi 6 driver directly.
6. Avoid letting Windows Update immediately replace your new driver — consider [disabling automatic driver updates](/articles/how-to-disable-automatic-driver-updates-on-windows-10/) afterward.

### Fix 4: Enable 802.11ax in the adapter's Advanced settings

Some drivers ship with the ax mode switched off or set to a compatibility value.

1. In Device Manager, right-click the wireless adapter, choose Properties, and go to the Advanced tab.
2. Look for "802.11ax", "HE Mode", "VHT Mode", or "Wireless Mode" in the property list.
3. Set any ax/HE-related property to Enabled, and set Wireless Mode to a value including ax (such as "802.11a/b/g/n/ac/ax").
4. Find "Preferred Band" and set it to 5 GHz if your Wi-Fi 6 network is on 5 GHz — 2.4 GHz ax exists but is less common.
5. Click OK, disconnect and reconnect to your network, then verify the radio type again.

### Fix 5: Adjust router settings for older drivers

Sometimes the router needs to meet the driver halfway.

1. Log into your router's admin page and check the wireless security mode — if it is WPA3-only, try WPA2/WPA3 transitional mode.
2. Set the 5 GHz channel width to 80 MHz instead of 160 MHz as a test; some early ax drivers are unstable on 160 MHz.
3. Try disabling OFDMA or MU-MIMO temporarily to see if stability improves — if it does, the driver is the weak link.
4. Make sure the router's firmware is current; early Wi-Fi 6 router firmware had interoperability bugs too.
5. After each router change, forget the network on the laptop and reconnect fresh.

### Fix 6: Disable power saving on the wireless adapter

Power management is the enemy of sustained Wi-Fi 6 throughput.

1. In Device Manager, open the wireless adapter's Properties > Power Management tab.
2. Uncheck "Allow the computer to turn off this device to save power".
3. On the Advanced tab, set "Power Saving Mode" or "Transmit Power" to Maximum Performance / Highest.
4. Go to Control Panel > Power Options > Change advanced power settings > Wireless Adapter Settings > Power Saving Mode > Maximum Performance.
5. Retest speeds on AC power — if Wi-Fi 6 performance is fine plugged in but poor on battery, power management was throttling it.
6. A [Code 10 on the wireless driver](/articles/how-to-fix-wifi-driver-code-10-error-on-lenovo-laptop/) can also masquerade as poor performance, so check Device Manager for warnings.

### Fix 7: Reset the network stack and Wi-Fi profile

Stale profiles and corrupted stack data can lock the adapter into fallback behavior.

1. Open Command Prompt as administrator and run `netsh winsock reset` and `netsh int ip reset`.
2. In Settings > Network & Internet > Wi-Fi > Manage known networks, forget your Wi-Fi 6 network.
3. Restart the laptop, reconnect to the network fresh, and re-enter the password.
4. Recheck the radio type — a fresh profile sometimes negotiates ax where the old one would not.
5. Microsoft documents the network reset options at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 8: Test with a controlled setup to isolate the fault

If nothing has helped, determine whether the laptop, the router, or the environment is at fault.

1. Test the laptop's Wi-Fi 6 against a different ax router or a phone hotspot that supports Wi-Fi 6.
2. Test a different Wi-Fi 6 device against your router to see if the router is the problem.
3. Move the laptop within a few meters of the router with line of sight and retest — this rules out interference.
4. If the laptop fails against every ax network but works on ac, the adapter's ax implementation may be faulty — a USB Wi-Fi 6 adapter is a cheap workaround.
5. Document your findings (radio types, speeds, conditions) before contacting support — it dramatically speeds up warranty claims.

## Closing

Wi-Fi 6 on Windows 10 is a driver-maturity story: the standard works, but only when the driver properly implements it. Update Windows, install the manufacturer's latest wireless driver, verify ax is enabled in Advanced settings, and tune the router to meet older drivers halfway. Do those four things and the overwhelming majority of Windows 10 Wi-Fi 6 problems — slow speeds, fallback to ac, random drops — resolve without any hardware changes.
