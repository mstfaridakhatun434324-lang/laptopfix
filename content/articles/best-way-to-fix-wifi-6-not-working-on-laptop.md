---
title: "Best Way to Fix WiFi 6 Not Working on a Laptop"
slug: best-way-to-fix-wifi-6-not-working-on-laptop
date: 2026-09-23
categories: ["drivers"]
tags: ["wifi 6", "fix wifi 6", "ax200 ax201", "wireless not working"]
description: "The best way to fix WiFi 6 not working: verify your card, install the right driver, and configure router and adapter settings for 802.11ax."
thumbnail: "/images/thumbs/best-way-to-fix-wifi-6-not-working-on-laptop.webp"
faqs:
  - q: "What is the single best fix for WiFi 6 not working?"
    a: "The highest-yield sequence is: confirm the card is WiFi 6 capable, clean-install the wireless driver from the laptop maker or Intel, then enable 802.11ax mode on the router with 80MHz channel width. That trio resolves the large majority of cases because it addresses capability, the driver tables, and the router negotiation — the three gates every AX connection must pass."
  - q: "Why does my laptop say connected but show 802.11ac instead of ax?"
    a: "The connection negotiated the best standard both ends support, and something in the chain capped it at WiFi 5: the router's AX mode is off, the adapter's advanced settings force VHT mode, the driver is too old for AX, or the router itself is WiFi 5. Check the router's wireless mode first, then the adapter's advanced settings — one of those two is the cap in most cases."
  - q: "Will upgrading my WiFi card enable WiFi 6?"
    a: "Yes, if the laptop has a standard M.2 2230 slot — an Intel AX210 is inexpensive and fits most machines. Match the CNVi type: CNVi cards (AX201/AX211) only work on Intel platforms with CNVi support, while the AX200/AX210 work anywhere. Check your platform before buying. Some thin laptops solder the card, in which case no upgrade is possible."
  - q: "Does WiFi 6 need WPA3 to work?"
    a: "No — WiFi 6 works fine with WPA2. WPA3 is a security standard, not a WiFi 6 requirement, though many WiFi 6 routers default to WPA2/WPA3 transitional mode. If connections fail, try WPA2-only on the router to rule out handshake issues; some older AX drivers negotiate WPA3 poorly. Security mode is a handshake variable, not an AX prerequisite."
---

When WiFi 6 refuses to work, the efficient approach is a fixed best-practice sequence rather than random troubleshooting. WiFi 6 is a three-gate system — the card must be capable, the driver must carry the AX tables, and the router must offer AX — and the best fix walks those gates in order, fixing each before moving on. No gate can be skipped, and the order prevents the classic waste of configuring a router for a card that cannot do AX.

This guide is that sequence, refined to the steps with the highest yield. Follow it top to bottom; most laptops are fixed by the third gate.

## Why this happens

- **Card is WiFi 5 only** — no software enables 802.11ax on it.
- **Wireless driver outdated**, predating stable 802.11ax support.
- **Router's AX mode disabled** or misconfigured.
- **Adapter advanced settings** forcing legacy or VHT-only modes.
- **Channel width capped at 20MHz**, strangling AX throughput.
- **WPA3 handshake failures** with older AX driver builds.
- **Router firmware bugs** in early WiFi 6 implementations.
- **Power management** throttling the adapter below AX rates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the card can do WiFi 6

Open Device Manager > Network adapters and read the exact model. WiFi 6 cards: Intel AX200/AX201/AX210/AX211, Killer AX1650/1675, MediaTek MT7921/MT7922, Qualcomm FastConnect 6800/6900. WiFi 5 cards (AC9560, 9260, 8265) cannot do 802.11ax under any software. This check takes twenty seconds and determines whether you troubleshoot or upgrade — skipping it is how people spend hours fixing hardware that was never capable. If the card is WiFi 5, jump to Fix 7 for the upgrade path.

1. Open Device Manager > Network adapters.
2. Read the exact wireless card model.
3. Match it against the WiFi 6 list above.
4. WiFi 5 only? Go to Fix 7 instead of troubleshooting.

### Fix 2: Clean-install the AX-aware wireless driver

The driver carries the 802.11ax capability tables, making it the best software fix. Download the WiFi driver from the laptop maker's support page for your exact model; for Intel cards, Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) installs the newest AX-aware build when the OEM package lags. Uninstall the existing driver completely — tick 'Delete the driver software' — because stale AX tables survive in-place upgrades. Reboot, then check the connection status: the protocol should read 802.11ax. MediaTek-specific AX issues are covered in the [MediaTek WiFi guide](/articles/how-to-fix-mediatek-wifi-not-working-in-windows-11-24h2/).

1. Download the WiFi driver from the maker or Intel.
2. Uninstall the old driver, deleting the driver software.
3. Install the fresh driver and reboot.
4. Check connection status for the 802.11ax protocol.

### Fix 3: Enable AX properly on the router

Log into the router and enable 802.11ax mode (may be labeled AX Mode, WiFi 6 mode, or 802.11ax under advanced wireless settings) on the 5GHz band. Set security to WPA2/WPA3 transitional — not WPA3-only — while troubleshooting, and set 5GHz channel width to 80MHz. Update the router firmware; early WiFi 6 firmware had negotiation bugs that current builds fixed. Reconnect the laptop and check the protocol. If AX appears now, the router was the gate — the most common single cause after the driver. Microsoft's wireless baseline is in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Enable 802.11ax mode on the router's 5GHz band.
2. Set WPA2/WPA3 transitional security.
3. Set 5GHz channel width to 80MHz.
4. Update router firmware, reconnect, and verify.

### Fix 4: Set the adapter's advanced options for AX

In Device Manager, open the wireless adapter's Properties > Advanced tab. Find the wireless-mode property (named 802.11a/b/g Wireless Mode, VHT Mode, or similar depending on vendor) and set it to allow 802.11ax/HE. Set Preferred Band to 5GHz, Channel Width to Auto or 80MHz+, and disable any power-saving mode on the adapter. These settings silently cap connections when wrong — a driver can be perfect while the adapter is configured to never attempt AX. The [5GHz connection guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/) covers band-specific issues.

1. Open the adapter's Advanced tab in Device Manager.
2. Enable 802.11ax/HE in the wireless mode property.
3. Set preferred band 5GHz, channel width Auto/80MHz+.
4. Disable adapter power saving and retest.

### Fix 5: Remove power throttling

AX speeds need full adapter power. In the advanced power plan, set Wireless Adapter Settings to Maximum Performance for both battery and AC; in the adapter's Power Management tab, untick 'Allow the computer to turn off this device'. Retest on AC power first, then compare with battery — a large gap confirms throttling was active. Adapters in power-save show AX in name only, with throughput far below the standard's promise. This is the best fix for 'says WiFi 6 but feels like WiFi 4' complaints.

1. Set Wireless Adapter Settings to Maximum Performance.
2. Untick power saving on the adapter.
3. Speed-test on AC power.
4. Compare with battery to confirm the throttle is gone.

### Fix 6: Reset the network stack and rejoin clean

Corrupted network profiles with stale security settings block AX negotiation even when everything else is right. Run `netsh winsock reset` and `netsh int ip reset` elevated, then Settings > Network & internet > Advanced network settings > Network reset, and reboot. Forget the WiFi network and rejoin from scratch — the fresh profile negotiates with current settings instead of cached ones. This is the best fix for 'AX worked, then stopped after a settings change' cases where no single setting looks wrong.

1. Run both netsh resets in an elevated Command Prompt.
2. Use Settings' Network reset and reboot.
3. Forget the network and rejoin fresh.
4. Verify 802.11ax in connection status.

### Fix 7: Upgrade the card if it was never AX

If Fix 1 showed a WiFi 5 card, the best fix is hardware: an Intel AX210 (non-CNVi, works on any platform) costs little and fits the standard M.2 2230 slot under the service hatch. Power down, swap the card, reconnect the two antenna leads (main/aux — note which was which), and install the Intel driver. On Intel platforms with CNVi support, AX201/AX211 also work; on AMD platforms, stick with AX200/AX210. If the card is soldered, no upgrade exists — an AX USB adapter is the fallback. The [troubleshooting companion](/articles/wifi-6-not-working-on-laptop-troubleshooting/) details the CNVi matching rules.

1. Buy a compatible AX card (AX210 for universal fit).
2. Power down, open the hatch, and swap the M.2 card.
3. Reconnect both antenna leads correctly.
4. Install the driver and verify 802.11ax.

## Closing

The best way to fix WiFi 6 is the disciplined way: capability, driver, router — in that order, no skipping. Each gate has a definitive test (the model number, the protocol readout, the router's wireless mode page), so you never guess; you check, fix, and move on. Most failures clear at the driver or the router, which is why the sequence puts the thirty-second capability check first — it is the only gate that cannot be fixed in software, and knowing that upfront saves every wasted hour. Once AX is negotiating, protect it: wireless drivers are fragile across updates, so keep the working installer and think twice before letting an update touch a connection that works.
