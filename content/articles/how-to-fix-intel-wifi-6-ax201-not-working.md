---
title: "Intel WiFi 6 AX201 Not Working? Here's the Fix"
slug: how-to-fix-intel-wifi-6-ax201-not-working
date: 2026-09-10
categories: ["drivers"]
tags: ["intel ax201", "wifi 6", "wireless driver", "troubleshooting", "device manager"]
description: "Intel AX201 WiFi dead, dropping, or showing Code 10? Fix the most common laptop WiFi card with this Intel-specific troubleshooting sequence."
thumbnail: "/images/thumbs/how-to-fix-intel-wifi-6-ax201-not-working.webp"
faqs:
  - q: "Why is the Intel AX201 such a common problem card?"
    a: "It's not that the card is bad — it's that it's everywhere. The AX201 shipped in millions of laptops, so its issues are the most reported. Most problems come from Windows Update replacing Intel's driver with an older inbox version, or power management settings that the card's firmware doesn't handle gracefully."
  - q: "What does Code 10 mean on the Intel AX201?"
    a: "Code 10 means 'this device cannot start' — Windows loaded the driver but the hardware failed to initialize. On the AX201 this usually indicates a driver/firmware mismatch, the card wedged in a bad power state, or occasionally a loose card. The full power-cycle in Fix 1 clears the wedged state."
  - q: "Should I use Intel's driver or my laptop maker's driver?"
    a: "Intel's own drivers (via the Driver & Support Assistant) are usually newer and fix more bugs, and Intel explicitly supports using them on most laptops. The exception: some laptop makers customize the driver for antenna or regulatory reasons — if Intel's driver misbehaves, fall back to the manufacturer's version."
  - q: "My AX201 works on 2.4GHz but not 5GHz. What's wrong?"
    a: "That's typically a band or channel issue rather than a dead card: the router's 5GHz settings (DFS channels, channel width) may be incompatible, or the driver's band preference is misconfigured. Try locking the router's 5GHz to a non-DFS channel like 36-48 and setting the adapter's preferred band explicitly."
---

The Intel Wi-Fi 6 AX201 is the most common wireless card in modern Windows laptops — which makes it the most commonly *troubleshot* card too. The symptoms are familiar: WiFi vanishes after sleep, the adapter shows Code 10 in Device Manager, connections drop every few minutes, or 5GHz/6GHz bands misbehave while 2.4GHz limps along. Nearly all of it is driver and power-state issues, and Intel's own driver releases fix most of them.

This is the AX201-specific sequence — the general WiFi steps adapted to this card's actual quirks.

## Why this happens

- **Windows Update driver downgrade.** The number-one AX201 issue. Windows replaces Intel's current driver with an older inbox version, resurrecting fixed bugs.
- **Wedged power state after sleep.** The AX201's firmware sometimes fails to reinitialize after modern standby, leaving the adapter dead until a full power cycle.
- **Code 10 from driver/firmware mismatch.** When the driver's expected firmware interface doesn't match what's loaded, the device can't start.
- **Aggressive power saving.** PCIe power management and the adapter's own power-saving mode can starve the card, causing drops and disconnects.
- **Band and channel incompatibilities.** DFS channels, 160MHz widths, and WiFi 6E 6GHz quirks can make specific bands unusable with certain routers. Compare [MediaTek's similar band issues](/articles/how-to-fix-mediatek-wifi-not-working-in-windows-11-24h2/).
- **Antenna or card seating problems.** The AX201's tiny antenna connectors can work loose, producing weak signal and drops that look like driver faults.
- **Bluetooth coexistence bugs.** The AX201 handles WiFi and Bluetooth together; certain driver versions let heavy Bluetooth use degrade WiFi throughput.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Full power-cycle the card's firmware

Clears wedged states that survive reboots — do this first for Code 10 and vanished adapters.

1. Shut down completely (not restart — full shutdown). Unplug the charger and all peripherals.
2. Hold the power button for **30 seconds** to drain residual power.
3. Boot up and open **Device Manager** > **Network adapters**. Check whether the AX201 is present and error-free.
4. If it shows Code 10 still, right-click > **Disable device**, wait 10 seconds, then **Enable device** — this forces a clean reinitialization.
5. If the adapter is missing entirely, use **Action** > **Scan for hardware changes**.

### Fix 2: Install Intel's current driver

The highest-yield permanent fix for this card.

1. Go to [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) and let it detect your system — it will offer the correct current WiFi driver for the AX201.
2. Alternatively, download the **Intel Wi-Fi 6 AX201 driver package** manually from Intel's download center.
3. Before installing: in Device Manager, right-click the AX201 > **Uninstall device**, checking "Attempt to remove the driver" to clear the old version.
4. Install Intel's driver as administrator and restart.
5. Verify the version in the Driver tab and note it — you'll compare against this if Windows Update later replaces it.

### Fix 3: Disable power management thoroughly

The AX201 is sensitive to power-state transitions.

1. In Device Manager, right-click the AX201 > **Properties** > **Power Management** tab. Uncheck "Allow the computer to turn off this device to save power."
2. On the **Advanced** tab, set **Power Saving Mode** to **Maximum Performance**.
3. Set **Preferred Band** to **Prefer 5GHz band** (or 2.4GHz if your 5GHz is the problem band) to stop band-hopping drops.
4. Set **Roaming Aggressiveness** to **1. Lowest** for home networks.
5. In **Control Panel** > **Power Options** > advanced settings > **Wireless Adapter Settings** > **Power Saving Mode**, set both states to **Maximum Performance**.

### Fix 4: Fix Code 10 specifically

When the device can't start.

1. In Device Manager, double-click the AX201 and read the **Device status** on the General tab. Confirm it's Code 10 and note any additional details.
2. Try the **driver rollback** first if the problem started after an update: Driver tab > **Roll Back Driver**.
3. If no rollback is available, do the full uninstall/reinstall from Fix 2 — Code 10 is most often a corrupted driver load.
4. Check **BIOS** for the wireless card: make sure WiFi is enabled and, if there's a **Wireless** toggle, it's on. Some BIOS updates flip it.
5. If Code 10 persists across multiple driver versions and a Linux live USB also fails to initialize the card, the hardware is suspect — check card seating (Fix 7).

### Fix 5: Stabilize the connection (drops and band issues)

For cards that work but won't stay working.

1. Log into your router and set the **5GHz channel** to a non-DFS channel (36, 40, 44, or 48) with **80MHz** width as a stability baseline.
2. In the AX201's **Advanced** tab, try setting **802.11a/b/g Wireless Mode** to exclude ax temporarily — if drops stop, update to the newest Intel driver which fixes ax-mode stability.
3. Disable **Wake on Magic Packet** unless you use Wake-on-LAN.
4. **Forget** the network in Windows and reconnect fresh to clear corrupted profiles: Settings > Network & internet > Wi-Fi > Manage known networks.
5. If [airplane mode sticks on](/articles/how-to-fix-airplane-mode-stuck-on-after-windows-11-update/) during these tests, treat it as a separate radio-control issue.

### Fix 6: Protect the working driver from Windows Update

The fix that keeps working.

1. Once stable, open **Device Installation Settings** (System > About > Advanced system settings > Hardware tab) and choose **No**.
2. Use Microsoft's **Show or hide updates** troubleshooter to hide WiFi driver updates.
3. After each Windows feature update, check the AX201's driver version in Device Manager — feature updates are the most common downgrade vector.
4. Keep the Intel installer you used saved locally for quick reinstallation.

### Fix 7: Check the hardware

The last resort for persistent failures.

1. Boot a **Linux live USB** — Linux's iwlwifi driver for the AX201 is excellent. Stable in Linux = Windows driver issue; failing in Linux = hardware.
2. If comfortable opening the laptop, check the card's seating in its M.2 slot and gently press the two antenna connectors (black and white wires) to ensure they're snapped on.
3. Look for a swollen battery pressing on the card area — replace swollen batteries immediately for safety.
4. Replacement AX201 cards are inexpensive if the card itself is dead — but verify the failure in Linux first so you don't replace a driver problem with hardware.

The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) is useful for finding specific Intel driver versions when you need to pin one.

## Closing

The AX201's problems are almost never the card — they're the driver Windows chose for it and the power states Windows puts it in. Full power-cycle to unwedge it, install Intel's current driver, disable every power-saving feature touching it, tune the band settings, then lock Windows Update out of replacing your working driver. That sequence turns the most-troubleshot WiFi card in laptops into the reliable one it was designed to be.
