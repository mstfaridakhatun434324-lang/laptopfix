---
title: "MediaTek WiFi Not Working on Your Laptop? Community-Tested Fixes"
slug: how-to-fix-mediatek-wifi-not-working-reddit
date: 2026-10-09
categories: ["drivers"]
tags: ["mediatek wifi", "mt7921", "wireless driver", "wifi fix", "windows 11"]
description: "MediaTek WiFi not working on your laptop? These community-tested fixes cover the MT7921/MT7922 drops, Code 10 errors, and driver issues users actually solved."
thumbnail: "/images/thumbs/how-to-fix-mediatek-wifi-not-working-reddit.webp"
faqs:
  - q: "Why is MediaTek WiFi so problematic on Windows laptops?"
    a: "MediaTek's MT7921/MT7922 cards shipped in huge numbers during the chip shortage as substitutes for Intel cards, often with immature drivers and less OEM tuning. Common complaints include random disconnects, Code 10 errors, and the adapter vanishing after sleep. The good news: driver maturity has improved significantly, and current drivers resolve most issues that plagued early units."
  - q: "Which driver should I use for the MediaTek MT7921?"
    a: "Get the latest driver from your laptop maker's support site first — makers like ASUS and Lenovo validate MediaTek packages for their specific antenna designs. If the OEM package is old, MediaTek's own driver downloads or Windows Update's optional driver updates are the next best source. Avoid random third-party driver sites; mismatched MediaTek drivers are a leading cause of Code 10 errors."
  - q: "Does the MediaTek WiFi card disappear after sleep?"
    a: "This is the MT7921's signature bug on older drivers: the card fails to reinitialize after modern standby, vanishing from Device Manager until a full shutdown. Updating to a 2023-or-newer driver largely fixes it, and disabling Fast Startup plus turning off the adapter's power management covers the remaining cases. A full shutdown (not restart) temporarily recovers the card when it happens."
  - q: "Should I replace my MediaTek card with an Intel AX210?"
    a: "It's the most recommended community upgrade: the Intel AX210 is inexpensive, broadly compatible, and dramatically more reliable. Check that your laptop doesn't have a BIOS whitelist blocking non-approved cards (most modern laptops don't), and confirm the card is a removable M.2 module rather than soldered. If you're not comfortable opening the laptop, the driver fixes in this guide get most MediaTek cards working acceptably."
---

If your laptop came with a MediaTek WiFi card — usually the MT7921 or MT7922 — you've probably visited the forums. Random disconnects, the adapter vanishing after sleep, Code 10 errors out of nowhere: these cards earned their reputation during the chip-shortage years when they shipped as last-minute Intel substitutes with half-baked drivers. The threads are full of frustration, but also full of fixes that actually worked.
This guide collects the community-tested solutions that kept coming up as 'this fixed it for me' — updated drivers, power-management tweaks, Fast Startup changes — in the order worth trying. If your adapter has vanished entirely rather than misbehaving, start with our [WiFi disappeared guide](/articles/wifi-disappeared-from-laptop-troubleshooting/) for the general missing-adapter diagnostics.
Fair warning and fair credit: MediaTek's newer drivers are much better than the ones these cards shipped with. A lot of 'MediaTek is garbage' sentiment dates to 2021-era drivers. Before judging the hardware, get the current driver on there — and if it still misbehaves, our [WiFi adapter troubleshooting](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/) covers the deeper hardware checks.

## Why this happens

- **Immature launch-era drivers.** Early MT7921/MT7922 drivers had sleep-resume and handshake bugs that newer releases fixed.
- **Windows Update driver mismatch.** Windows installs a generic MediaTek driver that doesn't match the card's firmware revision.
- **Modern Standby resume failure.** The card's signature bug: failing to reinitialize after sleep on older drivers.
- **Aggressive power management.** Windows powers down the MediaTek card and it doesn't wake cleanly — the most reported trigger.
- **Fast Startup preserving bad state.** Hybrid shutdown carries a wedged driver state across boots.
- **Router WiFi 6 incompatibilities.** Older MediaTek firmware chokes on certain 802.11ax features like OFDMA or 160MHz channels.
- **Bluetooth coexistence.** The combo card's Bluetooth activity destabilizes WiFi on marginal drivers.
- **Loose MHF4 antenna connectors.** Weak-signal complaints that look like driver bugs but are physical.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Update to the newest MediaTek driver

The fix behind most success stories: the current driver is generations ahead of what these laptops shipped with.

1. Find your exact laptop model on the maker's support site and download their latest WiFi driver package.
2. If the OEM package is outdated, check Windows Update → Advanced options → Optional updates for a newer MediaTek driver.
3. Install with the old driver fully removed first: Device Manager → Uninstall device (check 'delete the driver software') → reboot → install.
4. Verify the driver date in Device Manager — you want something recent, not the 2021 original.
5. Test sleep/resume cycles specifically, since that's where old drivers failed most visibly.

### Fix 2: Disable Fast Startup and do a true shutdown

The community's favorite quick fix for the vanishing-after-sleep bug — it forces genuine clean boots.

1. Control Panel → Power Options → 'Choose what the power buttons do' → 'Change settings that are currently unavailable.'
2. Uncheck 'Turn on fast startup (recommended)' and save.
3. Do a full Shutdown, wait 10 seconds, and power on — this clears any wedged card state.
4. Test several sleep/wake cycles to confirm the card survives them.
5. If the card ever vanishes again, a full shutdown (not restart) remains the fastest recovery.

### Fix 3: Turn off all adapter power saving

The single most upvoted tweak across every MediaTek thread: stop Windows from powering down the card.

1. Device Manager → MediaTek WiFi adapter → Properties → Power Management tab → uncheck 'Allow the computer to turn off this device to save power.'
2. Advanced tab → 'Power Saving Mode' → set to 'Maximum Performance.'
3. Windows power plan → advanced settings → 'Wireless Adapter Settings' → Maximum Performance on battery and plugged in.
4. In BIOS, disable any 'deep sleep' or aggressive ASPM power settings for the WLAN if present.
5. Retest under your normal usage for a full day — disconnects often take hours to manifest.

### Fix 4: Tune wireless mode for stability

When disconnects persist with current drivers, the 802.11ax features are the usual friction point with MediaTek firmware.

1. In the adapter's Advanced tab, find 'Wireless Mode' or '802.11ax' settings.
2. Try disabling 802.11ax (WiFi 6) mode temporarily — if stability returns, you've found the incompatibility.
3. Set 'Preferred Band' to 5GHz if your router's 2.4GHz band is congested, or 2.4GHz for better range through walls.
4. On the router side, disable 160MHz channel width and try WPA2 instead of WPA3-transition mode.
5. Update the router firmware too — many 'MediaTek bugs' were actually router-side ax implementation bugs.

### Fix 5: Fix the Bluetooth coexistence

MediaTek combo cards share the radio between WiFi and Bluetooth; stabilizing one often stabilizes the other.

1. Update the MediaTek Bluetooth driver from the same OEM package as the WiFi driver.
2. Test with Bluetooth disabled for a day — if WiFi stabilizes, coexistence is your issue.
3. In the WiFi adapter's Advanced tab, look for coexistence or 'Bluetooth Collaboration' settings and experiment.
4. Keep Bluetooth audio devices close to reduce retransmissions.
5. If problems persist only with Bluetooth active, a cheap USB Bluetooth dongle offloads it from the combo card.

### Fix 6: Reset the network stack

When the driver is current but behavior is still erratic, corrupted network state may be compounding the problem.

1. Settings → System → Troubleshoot → Other troubleshooters → run 'Network and Internet.'
2. In an elevated Command Prompt: netsh winsock reset and netsh int ip reset, then reboot.
3. Forget the WiFi network (Settings → Network → WiFi → Manage known networks → Forget) and reconnect fresh.
4. If it still misbehaves, use Network Reset (Settings → Network → Advanced → Network reset) for a full wipe.
5. Re-enter WiFi passwords and VPN settings afterward — the reset clears them.

### Fix 7: Consider the Intel AX210 swap

The community's nuclear option — and the most universally praised one for truly stubborn cards.

1. Verify your laptop's card is a removable M.2 2230 module (check a teardown guide for your model).
2. Confirm no BIOS whitelist blocks third-party cards (rare on 2020+ laptops, but check forums for your model).
3. Buy an Intel AX210 (under $25 typically) — it's the drop-in community favorite.
4. Swap the card, reconnect the two antenna wires (note which goes where), and install Intel's driver via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
5. If you'd rather not open the laptop, a USB WiFi adapter is the zero-disassembly alternative — see Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for adapter setup basics.

## Closing

MediaTek WiFi's forum reputation was earned by old drivers, not necessarily bad hardware. Update the driver, kill Fast Startup and power management, tune the ax settings — and if the card still won't behave, the AX210 swap is the best twenty-five dollars in laptop repair.
