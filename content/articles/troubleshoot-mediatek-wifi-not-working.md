---
title: "MediaTek Wi-Fi Not Working: Complete Driver Troubleshooting"
slug: troubleshoot-mediatek-wifi-not-working
date: 2026-10-11
categories: ["drivers"]
tags: ["mediatek wifi", "wifi not working", "mt7921", "wireless driver"]
description: "MediaTek Wi-Fi dead on your laptop? Diagnose MT7921/MT7922 adapter failures and restore wireless with this driver-focused troubleshooting guide."
thumbnail: "/images/thumbs/troubleshoot-mediatek-wifi-not-working.webp"
faqs:
  - q: "Why does my MediaTek Wi-Fi disappear after a Windows update?"
    a: "Windows Update sometimes installs a generic or mismatched driver for the MT7921 or MT7922 card, or the update resets the adapter's power-management settings. The Wi-Fi icon may vanish entirely or show no networks. Reinstalling the laptop maker's MediaTek driver package and disabling adapter power saving usually brings the radio back online."
  - q: "Is the MediaTek MT7921 a bad Wi-Fi card?"
    a: "The card itself is capable hardware, but its early Windows drivers were notoriously unstable, giving it a poor reputation. Modern driver versions are substantially better. Most current MT7921 problems are driver or power-management issues, not defective silicon, so work through software fixes thoroughly before considering a card replacement."
  - q: "Should I replace my MediaTek card with an Intel AX210?"
    a: "If driver troubleshooting repeatedly fails and the card drops connections constantly, swapping to an Intel AX210 is a popular and effective upgrade — but only if your laptop's BIOS doesn't whitelist Wi-Fi cards. Check your model's service manual first. Also note that opening the laptop may void warranty on some brands."
  - q: "Why is my MediaTek Wi-Fi slow but connected?"
    a: "Slow-but-connected usually means the adapter negotiated a poor link: wrong band, crowded channel, or the driver throttling to save power. Forget the network and reconnect to force renegotiation, set the preferred band to 5GHz in the adapter's advanced properties, and update the driver. Router-side channel changes can also help significantly."
---

MediaTek Wi-Fi adapters — the MT7921 and MT7922 found in a huge number of AMD-based laptops — have earned a reputation for flaky wireless. Dropped connections, vanished adapters, and no-networks-found errors are the classic symptoms. The hardware is generally capable; the pain almost always comes from immature drivers, aggressive power management, or Windows swapping in the wrong driver package.

This guide focuses on the driver and configuration layer, which is where MediaTek problems live. You will learn to confirm the adapter is present, install a known-good driver, tame power management, and optimize the radio settings. If you own an Intel card instead, the companion guide on [Intel Wi-Fi 6 AX201 issues](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) covers that hardware specifically.

## Why this happens

- **Immature or buggy MediaTek drivers:** Early MT7921/MT7922 drivers had genuine stability bugs; outdated installs still carry them.
- **Windows Update driver swaps:** A generic driver replaces the tuned package, breaking band steering and power behavior.
- **Aggressive power saving:** Windows powers down the adapter to save battery and the MediaTek firmware fails to wake cleanly.
- **Bluetooth/Wi-Fi coexistence bugs:** The combo card's shared antenna arbitration mishandles simultaneous Bluetooth and Wi-Fi traffic.
- **Wrong band or channel negotiation:** The adapter latches onto a congested 2.4GHz channel or a weak 5GHz signal and never roams.
- **Corrupted driver installation:** Interrupted updates leave the driver half-installed, producing Code 10 or Code 43 in Device Manager.
- **Router-side incompatibilities:** Certain WPA3, OFDMA, or 802.11ax settings on the router confuse older MediaTek firmware.
- **Antenna or card seating issues:** Loose antenna leads inside the chassis cause weak signal that looks like a driver problem.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the adapter exists in Device Manager

Press Win + X, open Device Manager, and expand Network adapters. You should see "MediaTek Wi-Fi 6 MT7921 Wireless LAN Card" or similar. A missing entry with an unknown device listed instead means the driver isn't installed at all. A yellow warning icon with Code 10 or Code 43 means the driver is present but failing to start — note the code, since it changes the fix path. If Bluetooth also died at the same time, suspect the combo card as a unit.

1. Open Device Manager with Win + X, then M.
2. Expand Network adapters and locate the MediaTek entry.
3. Note any yellow icons and read the Device status error code.
4. Check whether Bluetooth died simultaneously.
5. Use the findings to pick the right fix below.

### Fix 2: Install the laptop maker's MediaTek driver

Download the wireless driver package for your exact model from the manufacturer — [Lenovo's support site](https://support.lenovo.com/us/en/) carries per-model MediaTek packages, as do Dell and HP. In Device Manager, uninstall the MediaTek adapter with "Attempt to remove the driver for this device" ticked, reboot, then install the downloaded package. Avoid the generic driver Windows offers during this process; let the maker's installer finish first, then reboot once more.

1. Download the Wi-Fi driver for your exact laptop model.
2. Uninstall the MediaTek adapter with driver software removed.
3. Restart the laptop.
4. Run the manufacturer's driver installer.
5. Restart again and verify the adapter starts cleanly.

### Fix 3: Disable power management on the adapter

This single setting resolves a large share of MediaTek dropouts. In Device Manager, open the MediaTek adapter's Properties, go to the Power Management tab, and uncheck "Allow the computer to turn off this device to save power." Then open the Advanced tab and set "Power Saving Mode" to Maximum Performance if the option exists. In Power Options, set Wireless Adapter Settings to Maximum Performance on both battery and plugged in. Test for a full day before declaring victory.

1. Open the MediaTek adapter Properties in Device Manager.
2. Uncheck power-saving on the Power Management tab.
3. Set Power Saving Mode to Maximum Performance on the Advanced tab.
4. In Power Options, set wireless adapter performance to Maximum.
5. Monitor stability for 24 hours.

### Fix 4: Tune the advanced radio properties

In the adapter's Advanced tab, several properties materially affect MediaTek stability. Set "Preferred Band" to 5GHz if your router supports it (5GHz is faster and less congested). Try disabling "802.11a/b/g Wireless Mode" legacy fallbacks only if you never need them. Set "Roaming Aggressiveness" to a middle value — too aggressive causes constant hopping, too passive causes sticky weak connections. Change one setting at a time and test, so you know which change helped. [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents how to reach these adapter properties.

1. Open the adapter's Advanced tab in Device Manager.
2. Set Preferred Band to 5GHz (or 5G first).
3. Set Roaming Aggressiveness to the middle setting.
4. Disable legacy wireless modes only if unnecessary.
5. Change one property at a time and retest.

### Fix 5: Fix Bluetooth/Wi-Fi coexistence

Because the MT7921/MT7922 is a combo card, Bluetooth traffic can starve Wi-Fi. In the Advanced tab, look for "Bluetooth Collaboration" or "BT-AMP" settings and experiment with toggling them. As a diagnostic, turn Bluetooth off entirely in Windows Settings for a day — if Wi-Fi stabilizes, coexistence is your problem. Updating the Bluetooth driver from the same manufacturer package often improves arbitration. If your Bluetooth has vanished too, see [Bluetooth missing from Device Manager](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-after-windows-11-update/).

1. Toggle Bluetooth Collaboration in the Advanced tab.
2. Test with Bluetooth fully disabled for a day.
3. Update the Bluetooth driver from the maker package.
4. Keep Bluetooth and Wi-Fi drivers version-matched.
5. Consider a USB Bluetooth dongle if coexistence stays broken.

### Fix 6: Adjust router-side settings

Log into your router and try targeted changes: switch the 5GHz channel to a less congested one (36, 40, 44, or 48 are usually safe), disable WPA3 or set WPA2/WPA3 transitional mode if the MediaTek firmware chokes on pure WPA3, and turn off OFDMA or 802.11ax-specific features as a test. Also try forgetting the network on the laptop and reconnecting fresh, which forces a clean security and channel negotiation. If other devices are fine and only the laptop struggles, the router is probably innocent — but these tests are cheap.

1. Log into the router admin page.
2. Try a cleaner 5GHz channel (36, 40, 44, 48).
3. Set WPA2/WPA3 transitional instead of WPA3-only.
4. Forget and rejoin the network on the laptop.
5. Test with 802.11ax features toggled off.

### Fix 7: Consider a card replacement

If every driver version fails and the card drops under load regardless of settings, the hardware may genuinely be at fault. The Intel AX210 is the standard replacement: stable drivers, Wi-Fi 6E support, and wide compatibility. Check your laptop's service manual for the card location and whether the BIOS whitelists Wi-Fi cards (many Lenovos historically do). Reseat the antenna leads carefully — black to MAIN, white to AUX — and test thoroughly before closing the chassis. This is also the moment to confirm the [5GHz connection basics](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/) are solid.

1. Confirm the BIOS doesn't whitelist Wi-Fi cards.
2. Buy an Intel AX210 (or AX211 if the platform supports it).
3. Open the chassis and swap the M.2 card.
4. Reconnect antenna leads: black to MAIN, white to AUX.
5. Install Intel drivers and verify stability.

## Closing

MediaTek Wi-Fi problems feel random but they follow patterns: power management, driver versions, and coexistence. Work the list in order, change one variable at a time, and keep notes on what each change did. Most MT7921 and MT7922 cards settle down with the right driver and power settings — and when they don't, an Intel card swap is a well-trodden, reliable escape hatch.
