---
title: "Intel WiFi 6 AX201 Not Working? Proven Fixes for Your Laptop"
slug: what-to-do-if-intel-wifi-6-ax201-not-working
date: 2026-10-06
categories: ["drivers"]
tags: ["intel ax201", "wifi 6", "wireless driver", "code 10", "windows 11"]
description: "Intel WiFi 6 AX201 not working on your laptop? Fix Code 10 errors, disappearances, and slow speeds with these proven driver and settings fixes."
thumbnail: "/images/thumbs/what-to-do-if-intel-wifi-6-ax201-not-working.webp"
faqs:
  - q: "Why does my Intel AX201 show Code 10 in Device Manager?"
    a: "Code 10 ('device cannot start') on the AX201 almost always means a driver problem — either a corrupted installation or a Windows Update-supplied driver that doesn't match the card's firmware. The reliable fix is downloading the Intel WiFi driver package directly from Intel (not Windows Update) and doing a clean install. In rarer cases, Code 10 indicates the card's firmware region got corrupted, which a driver reinstall also typically repairs."
  - q: "Should I use Intel's driver or my laptop maker's driver for the AX201?"
    a: "Intel's generic driver is usually the better choice for the AX201 because laptop makers update their customized packages infrequently, while Intel ships fixes monthly. The exception is laptops with custom regulatory or antenna configurations (some Lenovo and Dell models) — if Intel's driver causes odd behavior, fall back to the OEM package for your exact model."
  - q: "Why does my AX201 keep disconnecting on Windows 11?"
    a: "Frequent culprits are Windows' power management turning the adapter off to save battery, outdated drivers with 802.11ax handshake bugs, and router incompatibilities with WiFi 6 features like OFDMA or 160MHz channels. Disabling 'allow the computer to turn off this device' in the adapter's Power Management tab and updating to Intel's latest driver resolves most disconnect cycles."
  - q: "Can a BIOS update fix AX201 problems?"
    a: "Yes — the AX201 is a CNVio2 card, meaning part of its logic lives in the Intel chipset/CPU rather than on the card itself, so BIOS/firmware compatibility matters more than with standard cards. Several laptop makers have released BIOS updates specifically fixing AX201 detection and Code 10 issues. Check your maker's support page for BIOS changelogs mentioning WiFi or the AX201."
---

The Intel WiFi 6 AX201 is in millions of laptops — and it has a reputation. Code 10 errors in Device Manager, the adapter vanishing after sleep, disconnect loops on WiFi 6 routers: AX201 owners know these symptoms by heart. The card's CNVio2 design (part of its brains live in the chipset, not on the card) makes it pickier about driver and BIOS versions than ordinary WiFi cards.
The good news is that nearly all AX201 problems are software. Intel updates this driver constantly, and most 'dead card' scares resolve with the right driver package installed the right way. This guide covers the AX201-specific fixes in the order that works — and if your card has vanished entirely, our [WiFi disappeared guide](/articles/wifi-disappeared-from-laptop-troubleshooting/) covers the general case.
One critical note: because of the CNVio2 architecture, you cannot swap an AX201 for a standard card like the AX210 — they're electrically incompatible. Don't buy a replacement card until you've exhausted the software fixes here; also see our [AX201-specific troubleshooting](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) for additional OS-version details.

## Why this happens

- **Corrupted driver after Windows Update.** The top cause — Windows replaces Intel's driver with a mismatched version and the card throws Code 10.
- **CNVio2 firmware mismatch.** The card's chipset-side logic and driver must agree; mismatched pairs fail to start.
- **Power management disabling the adapter.** Windows powers down the AX201 to save battery and it doesn't wake cleanly.
- **Outdated BIOS.** Older BIOS revisions mishandle CNVio2 initialization, especially after sleep/resume cycles.
- **WiFi 6 router incompatibilities.** OFDMA, 160MHz channels, or WPA3 transition modes trigger disconnect loops with older AX201 drivers.
- **Bluetooth coexistence interference.** The AX201's Bluetooth shares the card; aggressive Bluetooth activity can destabilize WiFi.
- **Antenna connection issues.** The tiny MHF4 antenna connectors work loose, causing weak signal misdiagnosed as driver failure.
- **Fast Startup driver state corruption.** Windows' hybrid shutdown saves a bad driver state that persists across 'restarts' that aren't really restarts.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install Intel's latest driver cleanly

The single most effective AX201 fix: Intel's current driver package, installed over a fully removed old one.

1. Download the latest 'Intel Wireless WiFi driver' for Windows 11 from Intel's site — or let the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) detect it automatically.
2. In Device Manager, right-click the Intel WiFi 6 AX201 → Uninstall device, checking 'Attempt to remove the driver for this device.'
3. Restart, then install the downloaded Intel driver package (it covers both WiFi and Bluetooth).
4. Reboot once more and verify in Device Manager that the driver date is current and no warning icon appears.
5. If Code 10 persists, repeat the uninstall but also delete the driver files manually via Device Manager's 'Delete the driver software' path.

### Fix 2: Disable Fast Startup

Fast Startup's hybrid shutdown preserves driver state across boots — including broken driver state. Disabling it forces true clean boots.

1. Open Control Panel → Power Options → 'Choose what the power buttons do.'
2. Click 'Change settings that are currently unavailable.'
3. Uncheck 'Turn on fast startup (recommended).'
4. Save changes, then do a full Shutdown (not Restart) and power back on.
5. Retest the AX201 — many 'dead after sleep' cases are actually Fast Startup preserving a wedged state.

### Fix 3: Turn off adapter power management

Windows' eagerness to power down the AX201 is a leading cause of disconnects and post-sleep disappearances.

1. In Device Manager, open the AX201's Properties → Power Management tab.
2. Uncheck 'Allow the computer to turn off this device to save power.'
3. Go to the Advanced tab → find 'Power Saving Mode' and set it to 'Maximum Performance.'
4. Set 'Roaming Aggressiveness' to '1. Lowest' as a test — aggressive roaming causes disconnect loops on some networks.
5. In Windows power plan advanced settings, set 'Wireless Adapter Settings → Power Saving Mode' to Maximum Performance for both battery and plugged in.

### Fix 4: Update the BIOS

For CNVio2 cards, BIOS updates aren't optional maintenance — several vendors shipped AX201 fixes exclusively via BIOS.

1. Find your exact laptop model on the maker's support site and check the BIOS changelog for WiFi/AX201/CNVio2 mentions.
2. Download the latest BIOS and install it on AC power with a charged battery — never interrupt a BIOS flash.
3. After flashing, enter BIOS setup and 'Load Optimized Defaults' to clear any stale CNVio2 configuration.
4. Boot into Windows and verify the AX201 enumerates cleanly in Device Manager.
5. If the changelog doesn't mention WiFi, still consider it — chipset initialization fixes are sometimes listed generically.

### Fix 5: Tune WiFi 6 settings for router compatibility

When the AX201 connects but loops disconnects on a WiFi 6 router, the 802.11ax features are usually the friction point.

1. In the AX201's Advanced tab, set '802.11a/b/g Wireless Mode' or 'VHT Mode' to test without ax features temporarily.
2. Disable 'OFDMA' or set 'MU-MIMO' off as a diagnostic step (re-enable after testing).
3. On your router, try disabling 160MHz channel width on the 5GHz band — the AX201 is happier at 80MHz on some firmware.
4. Set the router's WPA mode to WPA2 (not WPA3-transition) temporarily to rule out handshake issues.
5. If stability returns, update the router firmware — the incompatibility is often on the router side.

### Fix 6: Fix Bluetooth coexistence issues

The AX201's Bluetooth radio shares antennas and bus time with WiFi; when Bluetooth misbehaves, WiFi suffers.

1. If disconnects correlate with Bluetooth headset/mouse use, update the Intel Bluetooth driver (it ships in the same Intel package).
2. In the AX201 Advanced tab, look for 'Bluetooth Collaboration' or coexistence settings and try alternate values.
3. Test with Bluetooth fully disabled (Settings → Bluetooth & devices → off) to confirm the correlation.
4. Move Bluetooth audio devices closer to reduce retransmissions that steal airtime.
5. As a workaround for persistent conflicts, a USB Bluetooth dongle offloads Bluetooth from the AX201 entirely.

### Fix 7: Reseat the card and antennas (advanced)

When software is exhausted and signal is inexplicably weak, the physical MHF4 antenna connectors are suspect.

1. Power off, unplug, and remove the bottom panel following a guide for your exact model.
2. Locate the M.2 WiFi card — two hair-thin antenna wires (black and white/gray) snap onto tiny round connectors.
3. Gently pry each connector straight up with a plastic tool, then press firmly straight down until it clicks.
4. Check the card's retaining screw is snug — a loose card loses contact intermittently.
5. Reassemble and test; if the card is truly dead (absent in BIOS), replace it with another CNVio2 card like the AX201 or AX211 — never a standard AX210. See our [adapter-not-showing guide](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/) for the full hardware diagnosis.

## Closing

The AX201's bad reputation is mostly undeserved — it's a capable card that just demands current drivers, a compatible BIOS, and sane power settings. Work through this guide in order and you'll either fix it or prove it's hardware, which is the next best thing to a fix.
