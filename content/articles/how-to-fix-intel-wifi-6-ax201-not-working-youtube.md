---
title: "How to Fix Intel Wi-Fi 6 AX201 Not Working on a Laptop"
slug: how-to-fix-intel-wifi-6-ax201-not-working-youtube
date: 2026-10-04
categories: ["drivers"]
tags: ["intel ax201", "wifi 6", "wireless not working", "intel driver"]
description: "Fix Intel Wi-Fi 6 AX201 not working on a laptop: repair the Intel wireless driver, fix disconnects, and restore stable Wi-Fi 6 connectivity."
thumbnail: "/images/thumbs/how-to-fix-intel-wifi-6-ax201-not-working-youtube.webp"
faqs:
  - q: "Why is my Intel AX201 disconnecting randomly?"
    a: "Random disconnects on the AX201 usually come from outdated drivers with roaming bugs, aggressive power management suspending the adapter, or router features like band steering and 802.11ax modes confusing the client. Updating to the latest Intel driver and disabling adapter power saving resolves most intermittent drops."
  - q: "Should I use Intel's driver or my laptop maker's driver for the AX201?"
    a: "Try the laptop maker's driver first — it includes antenna and regulatory tuning for your specific chassis. If the OEM driver is old and disconnects persist, Intel's generic driver from their support site is an excellent second option and often contains newer bug fixes. Either is preferable to whatever Windows Update installs automatically."
  - q: "My AX201 shows Code 10 in Device Manager. What does that mean?"
    a: "Code 10 means the device failed to start — the driver loaded but the adapter would not initialize. For the AX201 this is typically driver corruption or a stuck power state after sleep. Reinstall the driver cleanly, drain residual power with a full shutdown, and verify wireless is enabled in BIOS."
  - q: "Does the AX201 support Wi-Fi 6E?"
    a: "No — the AX201 is Wi-Fi 6 (802.11ax) on 2.4 and 5GHz only; it does not support the 6GHz band. The AX210 is the Wi-Fi 6E variant. If your router broadcasts a 6GHz network, the AX201 simply will not see it, which is normal and not a malfunction."
---

The Intel Wi-Fi 6 AX201 is one of the most common wireless cards in modern laptops, and when it misbehaves the symptoms are familiar: random disconnects, slow speeds, the adapter vanishing after sleep, or Wi-Fi refusing to turn on at all. Intel's drivers for this card matured significantly after launch, which means a large share of AX201 problems are simply old-driver problems — fixable without touching hardware.

This guide covers the AX201's specific failure modes: driver repair with the right package, the power and roaming settings behind disconnects, BIOS and platform issues, and the deeper checks for cards that will not start at all.

The AX201 has an architectural quirk worth knowing: it uses Intel's CNVi (Connectivity Integration) design, which moves part of the Wi-Fi MAC into the Intel chipset itself and keeps only the radio on the M.2 card. This means the AX201 only works on Intel platforms with a compatible chipset — and, more relevantly for troubleshooting, that its behavior depends on chipset drivers and platform firmware as well as its own wireless driver. An outdated chipset driver or BIOS can produce AX201 symptoms that no wireless driver update will fix, because part of the Wi-Fi pipeline lives outside the wireless driver entirely. Keep this in mind if the standard driver fixes stall: the platform underneath the card matters as much as the card's own software.

## Why this happens

- **Outdated driver with known bugs:** Early AX201 drivers had documented disconnect, roaming, and resume defects.
- **Windows Update driver replacement:** Windows swaps the working driver for an older generic one.
- **Power management suspend:** The adapter sleeps and fails to wake — the classic post-sleep disappearance.
- **Roaming aggressiveness:** Over-eager roaming between access points or bands causes drops.
- **Router 802.11ax incompatibilities:** Some routers' Wi-Fi 6 implementations clash with older AX201 firmware.
- **Bluetooth coexistence:** The AX201 shares antennas with Bluetooth; coexistence bugs cause Wi-Fi drops when Bluetooth is active.
- **Corrupted driver state:** Failed updates leave mixed driver files that misbehave unpredictably.
- **Hardware failure:** Rare — the card itself or its antenna connections.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the latest Intel driver

1. Note your current driver version: **Device Manager → Network adapters → Intel Wi-Fi 6 AX201 → Properties → Driver**.
2. Download the latest **Intel Wireless driver** — use [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) or your laptop maker's support site.
3. In Device Manager, right-click the AX201 → **Uninstall device** (check driver removal), restart, then install the fresh driver.
4. Confirm the new version in Properties. Intel's release notes for AX201 drivers explicitly list fixed disconnect bugs — this step alone resolves a huge fraction of cases, the same pattern seen with [other Intel wireless issues](/articles/how-to-fix-intel-wifi-6-ax201-not-working-on-windows-10/).

### Fix 2: Disable power management

1. In the AX201's **Properties → Power Management**, uncheck **"Allow the computer to turn off this device to save power"**.
2. Go to **Power Options → Advanced → Wireless Adapter Settings → Power Saving Mode** → **Maximum Performance** (battery and plugged in).
3. Set Windows **Power mode** to **Best performance** while testing.
4. Retest sleep/wake cycles specifically — AX201 adapters that vanish after sleep are almost always power-management victims.

### Fix 3: Tune roaming and band settings

1. Open the AX201's **Properties → Advanced** tab.
2. Set **Roaming Aggressiveness** to **1. Lowest** if you use one router — stops pointless roaming drops.
3. Set **Preferred Band** to **5GHz** (or 2.4GHz at long range) instead of Auto to prevent band-hopping disconnects.
4. If drops correlate with Bluetooth use, try disabling Bluetooth temporarily to test coexistence — then update Bluetooth drivers too, since Intel ships them together.

### Fix 4: Address router-side issues

1. Test on a phone hotspot — stable there means your router is implicated.
2. In the router settings, try disabling **802.11ax / Wi-Fi 6 mode** temporarily; if drops stop, update the router firmware and re-enable.
3. Disable **band steering** (separate the 2.4GHz and 5GHz network names) as a test.
4. Update the router firmware regardless — client and access-point firmware evolve together, and mismatches cause exactly these symptoms.

### Fix 5: Reset the network stack

1. Run **Settings → Network & internet → Advanced network settings → Network reset → Reset now**, then restart.
2. Or via elevated Command Prompt: **netsh winsock reset** and **netsh int ip reset**, then restart.
3. Reconnect to Wi-Fi and retest for a full day — some fixes only prove themselves over time.
4. If the adapter shows **Code 10** instead of disconnecting, follow the [Code 10 repair sequence](/articles/wifi-driver-code-10-error-troubleshooting/) — the AX201 responds to the same steps.

### Fix 6: Stop Windows Update from regressing the driver

1. Once stable, set **Device Installation Settings** to **No** (**System → About → Advanced system settings → Hardware**).
2. Use the show/hide updates troubleshooter from [Microsoft support](https://support.microsoft.com/en-us/windows) to block the specific bad driver version.
3. Recheck after each Windows feature update — they sometimes reset this protection.
4. Consider pausing updates briefly while stabilizing a previously broken adapter.

### Fix 7: Check BIOS and platform firmware

1. Enter BIOS and confirm wireless/WLAN is enabled; choose **Load Defaults** if anything looks off.
2. Install the latest **BIOS** and **chipset drivers** from your laptop maker — platform firmware affects how the AX201 enumerates and resumes.
3. On Intel platforms, [Intel's assistant](https://www.intel.com/content/www/us/en/support/detect.html) can also update Bluetooth and chipset components that interact with the Wi-Fi card.
4. Cold boot after firmware updates and verify the adapter survives sleep/wake.

### Fix 8: Hardware verification

1. Boot a **Linux live USB** — the AX201 is well supported in Linux; working there clears the hardware.
2. If comfortable opening the machine, check that the two antenna leads (black/white, Main/Aux) are firmly connected to the M.2 card — loose antennas cause weak signal and drops, not total failure.
3. The AX201 is a standard M.2 2230 card and is replaceable (or upgradable to AX210) on many laptops — check your model's service manual.
4. If the card fails everywhere including Linux with BIOS wireless enabled, replace the card.

## Closing

The AX201's reputation for flakiness is mostly a driver-age problem: early drivers were buggy, Windows Update keeps reinstalling old ones, and power management keeps putting the card to sleep. Install Intel's current driver, disable the power saving that breaks resume, calm the roaming logic, and lock the good driver in place — the card that disconnected hourly becomes the card you forget about.
