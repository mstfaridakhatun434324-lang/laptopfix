---
title: "WiFi 6 Not Working on Your Laptop? Troubleshooting Guide"
slug: wifi-6-not-working-on-laptop-troubleshooting
date: 2026-09-17
categories: ["drivers"]
tags: ["wifi 6", "802.11ax", "wifi 6 not working", "wireless adapter"]
description: "WiFi 6 not working on your laptop? Troubleshoot 802.11ax connection failures with driver, router, and adapter settings that restore fast wireless."
thumbnail: "/images/thumbs/wifi-6-not-working-on-laptop-troubleshooting.webp"
faqs:
  - q: "Why is WiFi 6 not working on my laptop?"
    a: "The most common causes are an outdated wireless driver that predates proper 802.11ax support, the router's AX mode being disabled or misconfigured, and the adapter's advanced settings forcing an incompatible mode. Less often the laptop's card is not actually WiFi 6 capable. Because WiFi 6 needs matching support on both ends, troubleshooting must check the laptop and the router."
  - q: "How do I know if my laptop supports WiFi 6?"
    a: "Check the wireless adapter model in Device Manager: Intel AX200, AX201, AX210, and AX211 are WiFi 6; MediaTek MT7921/MT7922 and Qualcomm FastConnect 6800/6900 are also WiFi 6. Older AC9560, 9260, and 8265 cards are WiFi 5 only and cannot do 802.11ax no matter the driver. If your card is WiFi 5, the fix is a card upgrade, not software."
  - q: "Can a driver update break WiFi 6?"
    a: "Yes. Wireless drivers carry the 802.11ax feature tables, and a bad update can disable AX mode, break WPA3 handshakes, or introduce the Code 10 start failure. If WiFi 6 worked and stopped after an update, rolling back the wireless driver is the first step. Intel's wireless drivers are particularly update-sensitive, which is why the laptop maker's validated version matters."
  - q: "Does WiFi 6 require a WiFi 6 router?"
    a: "For 802.11ax speeds and features, yes — both the laptop and the router must support WiFi 6, or the connection falls back to the best common standard (usually WiFi 5/ac). A WiFi 6 laptop on a WiFi 5 router works fine but never shows AX rates. If you expect WiFi 6 and see 802.11ac in the connection status, check the router's capabilities first."
---

WiFi 6 (802.11ax) promises faster speeds, better congestion handling, and lower latency — when it works. When it does not, the symptoms vary: the laptop connects but only at WiFi 5 rates, it refuses to join the 6GHz-capable network, connections drop under load, or the adapter fails outright. Because WiFi 6 is a negotiation between the laptop's card, its driver, and the router, the fault can sit on either end.

Effective troubleshooting checks both ends in order: confirm the hardware is actually WiFi 6 capable, fix the driver (the most common failure point), then align the router's AX settings and the adapter's advanced options. Skip the capability check and you may chase a software fix for hardware that cannot do AX at all.

## Why this happens

- **Wireless driver outdated** or corrupted, lacking proper 802.11ax support.
- **Router's AX/802.11ax mode disabled** or set to an incompatible configuration.
- **Adapter's advanced settings** forcing 802.11a/b/g or VHT mode instead of AX.
- **Laptop's card is WiFi 5 only** — no software enables 802.11ax on it.
- **WPA3/OWE handshake failures** between mismatched implementations.
- **Router firmware bugs** in early WiFi 6 implementations.
- **Channel width forced to 20MHz**, capping AX throughput.
- **Power management throttling** the adapter below AX rates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the card is actually WiFi 6 capable

Open Device Manager > Network adapters and read the wireless card's exact model. Intel AX200, AX201, AX210, AX211, Killer AX1650/1675, MediaTek MT7921/MT7922, and Qualcomm FastConnect 6800/6900 are WiFi 6. Intel AC9560, 9260, 8265 and older are WiFi 5 — they will never do 802.11ax. If your card is WiFi 5, stop troubleshooting software: the answer is a card upgrade (a $20 M.2 module on most laptops) or accepting WiFi 5. This check prevents hours of futile driver work.

1. Open Device Manager > Network adapters.
2. Read the exact wireless card model.
3. Check it against the WiFi 6 model list above.
4. If WiFi 5 only, plan a card upgrade instead.

### Fix 2: Update the wireless driver from the right source

The wireless driver carries the 802.11ax feature tables, so it is the prime suspect. Download the WiFi driver from the laptop maker's support page for your exact model first; if that version is old, use Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel cards, which installs the current AX-aware build. Uninstall the old driver completely (deleting the driver software) before installing the new one — in-place upgrades sometimes leave stale AX tables behind. The [AX201-specific guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) covers Intel's most common card.

1. Download the WiFi driver from the laptop maker or Intel.
2. Uninstall the old wireless driver, deleting the driver software.
3. Install the fresh driver and reboot.
4. Check the connection status for the 802.11ax protocol.

### Fix 3: Check the router's WiFi 6 settings

Log into the router and verify 802.11ax mode is enabled — on some routers it hides under 'Wireless Mode', 'AX Mode', or per-band advanced settings. Enable WPA2/WPA3 transitional mode rather than WPA3-only if devices fail to connect, and set the 5GHz channel width to 80MHz (or 160MHz if both ends support it) — a 20MHz width strangles AX throughput. Update the router firmware too; early WiFi 6 firmware was notoriously buggy. If the laptop shows 802.11ax after these changes, the router was the bottleneck.

1. Log into the router's admin page.
2. Enable 802.11ax mode on the 5GHz band.
3. Set WPA2/WPA3 transitional security and 80MHz channel width.
4. Update the router firmware and retest.

### Fix 4: Align the adapter's advanced settings

In Device Manager, open the wireless adapter's Properties > Advanced tab. Set '802.11a/b/g Wireless Mode' or 'VHT Mode' to allow AX/802.11ax (the exact property name varies by vendor — look for 802.11ax, HE, or 'WiFi 6' in the property list). Set 'Preferred Band' to 5GHz if the router's AX lives there, and 'Channel Width' to Auto or 80MHz+. Disable 'Power Saving Mode' on the adapter. Wrong advanced settings silently cap the connection below AX even with perfect drivers. Microsoft's wireless baseline is in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open the adapter's Properties > Advanced tab.
2. Enable 802.11ax/HE mode in the wireless mode property.
3. Set preferred band to 5GHz and channel width to Auto/80MHz+.
4. Disable adapter power saving and retest.

### Fix 5: Fix the power-management throttle

WiFi 6's high rates demand full adapter power, but Windows' power plans throttle wireless aggressively. In the advanced power plan settings, set Wireless Adapter Settings to Maximum Performance on both battery and AC. In the adapter's Power Management tab, untick 'Allow the computer to turn off this device'. Then retest throughput — adapters stuck in power-save show AX in name only, with real speeds far below. This fix particularly helps the 'connects at AX but slow' complaint.

1. Set Wireless Adapter Settings to Maximum Performance.
2. Untick power saving on the adapter's Power Management tab.
3. Retest speed on AC power first.
4. Compare battery vs AC to confirm the throttle is gone.

### Fix 6: Reset the network stack and rejoin

If settings are right but connections drop or fail, reset the stack: run `netsh winsock reset` and `netsh int ip reset` in an elevated Command Prompt, then Settings > Network & internet > Advanced network settings > Network reset. Reboot, forget the WiFi network, and rejoin fresh — this clears corrupted profiles with stale security settings that block AX negotiation. The [in-depth WiFi 6 guide](/articles/how-to-fix-wifi-6-not-working-on-laptop-in-windows-11-24h2/) covers profile corruption in detail.

1. Run `netsh winsock reset` and `netsh int ip reset` as admin.
2. Use Settings' Network reset and reboot.
3. Forget the WiFi network and rejoin it fresh.
4. Verify 802.11ax in the connection status.

### Fix 7: Replace the card or reposition the router

If the card is WiFi 6 capable, the driver is current, and the router is configured, yet AX will not engage — test the laptop against a different WiFi 6 router (a phone hotspot with AX, a friend's router). AX on another network exonerates the laptop and convicts the router; failure everywhere points at the card. Replacement AX210 cards are cheap and fit the same M.2 2230 slot — just match CNVi vs non-CNVi for Intel platforms. Also try moving closer to the router: AX features degrade first at range, and 'WiFi 6 not working' at the far bedroom is often just physics.

1. Test the laptop on a different WiFi 6 network.
2. Test close to the router to rule out range.
3. Replace the card with a compatible AX model if needed.
4. Match CNVi type when buying Intel replacement cards.

## Closing

WiFi 6 failures are negotiation failures, and negotiations need both parties capable and correctly configured. The capability check comes first because no driver enables AX on a WiFi 5 card; the driver comes second because it carries the AX feature tables; the router comes third because its AX mode, security, and channel width all gate what the laptop can use. Work that order and the fault reveals itself quickly — usually as a stale driver or a router setting, occasionally as a card that was never AX to begin with. Once AX engages, leave the driver alone: wireless drivers are the most update-fragile in the machine, and a working AX connection is worth protecting from the next silent update.
