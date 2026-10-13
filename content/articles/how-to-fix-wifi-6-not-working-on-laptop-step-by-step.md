---
title: "WiFi 6 Not Working on Your Laptop? A Step-by-Step Fix Guide"
slug: "how-to-fix-wifi-6-not-working-on-laptop-step-by-step"
date: "2026-09-20"
categories: ["drivers"]
tags: ["wifi 6", "802.11ax", "wireless", "router", "drivers"]
description: "Stuck on slow WiFi despite a WiFi 6 router? Learn why 802.11ax won't engage on your laptop and follow step-by-step fixes to unlock full WiFi 6 speeds."
thumbnail: "/images/thumbs/how-to-fix-wifi-6-not-working-on-laptop-step-by-step.webp"
faqs:
  - q: "How do I know if my laptop is actually using WiFi 6?"
    a: "In Windows, go to Settings, Network and internet, WiFi, then click your connected network and check the Protocol line — it should say Wi-Fi 6 (802.11ax). You can also run netsh wlan show interfaces in Command Prompt and read the Radio type field. If it shows 802.11ac or 802.11n instead, the connection has fallen back to an older standard."
  - q: "Why is my WiFi 6 laptop only connecting at WiFi 5 speeds?"
    a: "The usual causes are an outdated wireless driver that cannot negotiate 802.11ax properly, the router's 802.11ax mode being disabled, connecting on the 2.4GHz band where WiFi 6 benefits are minimal, or the adapter's VHT/HE mode settings forcing older protocols. Interference and distance can also make the driver silently drop to WiFi 5 rates for stability."
  - q: "Does my router need a firmware update for WiFi 6 to work?"
    a: "Often yes. Early WiFi 6 router firmware had buggy 802.11ax implementations that failed handshakes with certain laptop cards, particularly Intel AX200 and AX201 models. Router makers released fixes over time, so updating to the latest firmware resolves a meaningful share of negotiation failures. Check your router maker's support page for the newest release."
  - q: "Can a VPN or security software block WiFi 6?"
    a: "It cannot block the 802.11ax protocol itself, since that negotiation happens between the wireless card and router below the OS network stack. However, VPNs, firewalls, and antivirus suites can throttle throughput so badly that your speed tests look like WiFi 5 or worse. Temporarily disable them when benchmarking to measure the raw wireless link speed."
---

You bought the WiFi 6 router, your laptop's spec sheet says 802.11ax, yet speed tests stubbornly show the same numbers as your old setup — or the connection properties reveal the laptop has quietly fallen back to WiFi 5. WiFi 6 problems are uniquely frustrating because everything "works," just never at the speed you paid for.

The 802.11ax standard demands cooperation between three things: the laptop's wireless card, its driver, and the router's firmware. If any one of them mishandles the handshake, the connection silently degrades to 802.11ac without telling you. The good news is that the failure points are well mapped, and the fixes below address them in the order that restores WiFi 6 fastest.

## Why this happens

- **Outdated wireless driver:** Early AX200/AX201 drivers had broken 802.11ax negotiation that only later releases fixed.
- **802.11ax disabled on the router:** Some routers ship with WiFi 6 mode off, or a firmware bug disables it after an update.
- **Connected on 2.4GHz:** WiFi 6's headline gains need the 5GHz band; the 2.4GHz band shows little improvement.
- **VHT/HE mode forced off in driver settings:** The adapter's advanced properties may disable the high-efficiency modes WiFi 6 requires.
- **Router firmware bugs:** Early WiFi 6 firmware failed handshakes with specific laptop cards.
- **WPA3 transition issues:** Mixed WPA2/WPA3 modes confuse some drivers into falling back to older protocols.
- **Signal too weak for ax rates:** At the edge of coverage, the driver drops to WiFi 5 rates to hold the connection.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Verify what protocol you are actually using
Open Settings, Network and internet, WiFi, click your network, and read the Protocol field. If it says Wi-Fi 5 (802.11ac), you have confirmed the fallback. Also note the link speed and band. This baseline matters: after each fix below, recheck this screen to see whether 802.11ax engaged. Do all testing on the 5GHz band close to the router, since distance alone can mask your progress. For general wireless troubleshooting technique, our [step-by-step WiFi repair guide](/articles/how-to-fix-wifi-not-working-step-by-step/) covers the fundamentals.

### Fix 2: Update the wireless driver to a WiFi 6-aware release
Download the latest driver for your card from your laptop maker's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). Intel AX200/AX201/AX210 owners should also check the Intel Driver & Support Assistant, since Intel fixed several 802.11ax handshake bugs in later releases. Uninstall the old driver with driver deletion first, then install the new package and reboot. Driver age is the number one cause of failed WiFi 6 negotiation.

### Fix 3: Enable 802.11ax mode in the adapter's advanced settings
In Device Manager, open your wireless adapter's Properties and go to the Advanced tab. Look for entries like "802.11a/b/g Wireless Mode," "VHT Mode," or "HE Mode" and make sure they are set to allow ax/HE operation rather than being capped at ac/VHT. Set "Preferred Band" to 5GHz so the card negotiates WiFi 6 on the band where it matters. Click OK, then disable and re-enable the adapter to force a fresh handshake with the router.

### Fix 4: Check the router's WiFi 6 settings and firmware
Log in to your router and confirm 802.11ax mode is enabled on the 5GHz band — on some models it hides under "WiFi 6 mode," "AX mode," or "High Efficiency." Update the router firmware to the latest release, since early WiFi 6 firmware is notoriously buggy. If the router offers separate SSIDs per band, connect the laptop to the 5GHz SSID directly. Reboot the router after changes and recheck the protocol on the laptop. Our guide on [5GHz connection problems](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-step-by-step/) pairs well with this step.

### Fix 5: Simplify the router's security and channel settings
Set the 5GHz security to WPA2-AES only (temporarily avoiding WPA3 or mixed modes) to rule out handshake confusion. Set the channel width to 80 MHz and pick a fixed non-DFS channel such as 36 or 44. Some drivers fail 802.11ax negotiation on 160 MHz widths or DFS channels and silently fall back to ac. If WiFi 6 engages after this change, you can experiment with re-enabling the advanced options one at a time.

### Fix 6: Test at close range and rule out interference
Move the laptop within a few meters of the router with line of sight and recheck the protocol. If 802.11ax engages nearby but not across the house, signal quality — not configuration — is the limiter. Reduce interference by moving the router away from microwaves and thick walls, and consider that neighboring networks on the same channel can force rate fallback. A mesh node or access point closer to your workspace may be the real fix for distant rooms.

### Fix 7: Reset the wireless stack and confirm with clean benchmarks
Run `netsh winsock reset` and `netsh int ip reset` in an elevated Command Prompt, reboot, and reconnect. Then benchmark properly: disable any VPN, close background downloads, and run a speed test plus a local file transfer to a wired device. Compare against the router's rated ax throughput. If the protocol shows 802.11ax but speeds still disappoint, the bottleneck is likely your internet plan or the router's CPU, not the laptop. Microsoft's wireless diagnostics at Windows support offer further checks.

## Closing
WiFi 6 failures are negotiation failures, and negotiations fail for specific, fixable reasons: old drivers, disabled ax modes, buggy router firmware, or hostile radio settings. Updating the driver, enabling 802.11ax on both ends, and testing on a clean 5GHz channel restores the standard in most cases — and the jump in real-world throughput is immediately noticeable once it locks in. Once 802.11ax is negotiating properly, protect the setup: note your router's working channel, width, and security settings somewhere, because a future firmware update may reset them and you will want the known-good values. On the laptop, avoid "driver updater" utilities that promise newer wireless drivers — they frequently install mismatched versions that break 802.11ax negotiation, undoing everything you fixed. If you add a mesh system or extender later, verify that the new nodes actually support WiFi 6; a WiFi 5 mesh node in the path silently caps everything behind it at ac speeds no matter what the main router does. When benchmarking, always test close to the router with a VPN disabled and no background downloads, or you will chase ghosts. And remember that real-world WiFi 6 gains show most in crowded airspace and multi-device homes — if you live alone next to no neighbors, the jump over WiFi 5 is modest, and that is normal.
