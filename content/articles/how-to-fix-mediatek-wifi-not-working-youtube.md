---
title: "MediaTek WiFi Not Working? How to Fix It on Your Laptop"
slug: how-to-fix-mediatek-wifi-not-working-youtube
date: 2026-10-12
categories: ["drivers"]
tags: ["mediatek wifi not working", "mediatek wireless driver", "mt7921 wifi issues", "mediatek wifi disconnecting", "amd laptop wifi fix"]
description: "MediaTek WiFi card (MT7921/MT7922) dropping, slow, or not detected? These cards need specific driver handling — here's the fix sequence that works."
thumbnail: "/images/thumbs/how-to-fix-mediatek-wifi-not-working-youtube.webp"
faqs:
  - q: "Why is my MediaTek WiFi so unstable compared to Intel?"
    a: "MediaTek's MT7921 and MT7922 cards — common in AMD-based laptops — have had rockier driver maturity than Intel's wireless chips. The typical symptoms are random disconnects, failure to see 5GHz/6GHz networks, and Bluetooth interference. The situation improves dramatically with the right driver: either your laptop maker's validated package or a recent driver direct from MediaTek's support channels. Most 'MediaTek WiFi is bad' stories are really 'MediaTek WiFi with a two-year-old driver' stories."
  - q: "Which driver should I use for my MediaTek WiFi card?"
    a: "Start with your laptop manufacturer's support site — their package is validated for your model's antenna design and power configuration. If their driver is ancient and problems persist, try a newer driver from MediaTek's official driver resources or your laptop maker's newer model pages using the same card. Avoid generic Windows Update drivers for MediaTek cards; they're the most common source of the disconnect and band-detection bugs people report."
  - q: "Why does my MediaTek WiFi drop when Bluetooth is on?"
    a: "The MT7921/MT7922 are combo cards sharing antennas and spectrum between WiFi and Bluetooth, and early drivers handled the coexistence badly — Bluetooth activity would starve or interrupt WiFi. Updated drivers substantially improved coexistence management. As a workaround, switching WiFi to the 5GHz band reduces contention since Bluetooth lives on 2.4GHz. If drops persist on current drivers, disabling Bluetooth when you need stable WiFi confirms the coexistence diagnosis."
  - q: "My MediaTek card isn't detected at all. Is it dead?"
    a: "Probably not — check Device Manager with Show hidden devices enabled first, since MediaTek cards ghost frequently after failed driver installs. Also check the BIOS for a disabled wireless LAN, and try the full power drain (shutdown, unplug, hold power 30 seconds). MediaTek cards are also sensitive to fast startup states; disabling Fast Startup resolves enumeration failures that look exactly like dead hardware."
---

MediaTek WiFi cards — the MT7921 (Wi-Fi 6) and MT7922 (Wi-Fi 6E) found in most AMD-powered laptops — have a reputation for flaky wireless that video tutorials address with random driver swaps. The reality is more specific: these cards are sensitive to driver versions in ways Intel cards aren't, and the fix is almost always getting the *right* driver rather than just the *newest* one. This guide gives you the MediaTek-specific sequence.

First, confirm you actually have a MediaTek card: Device Manager > Network adapters, look for "MediaTek" or "MT7921/MT7922" in the name. If you have Intel or Realtek, use the general WiFi guides instead — the steps below are tuned for MediaTek's quirks.

A bit of context on why these cards behave differently: the MT7921 and MT7922 are combo chips handling WiFi and Bluetooth on shared antennas and shared spectrum, which makes their driver responsible for a delicate balancing act that Intel's separate-radio designs handle more gracefully. Early driver builds got that balancing act wrong — hence the reputation for disconnects and Bluetooth interference. Later builds improved substantially, which is why "update the driver" is genuinely the fix here rather than generic advice. The card in your laptop is probably fine; it is almost certainly just running a driver from the era when the balancing act was broken. Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) is worth knowing about too, in case you ever swap to an Intel card.

## Why this happens

- **Outdated or generic driver** — MediaTek cards degrade badly on old or Windows Update drivers.
- **Bluetooth/WiFi coexistence bugs** in older driver versions (combo card sharing antennas).
- **5GHz/6GHz band detection failures** specific to MediaTek driver builds.
- **Aggressive power management** putting the card to sleep mid-connection.
- **Fast Startup** carrying broken MediaTek driver state across boots.
- **Router features** (band steering, WPA3, 6GHz) that older MediaTek drivers mishandle.
- **Card not enumerating** after sleep — a known MediaTek resume bug fixed in later drivers.
- **Antenna connection issues** — less common, but the shared antenna design makes seating matter.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the right MediaTek driver

The fix that matters most for these cards.

1. Note your exact card model (MT7921, MT7921K, MT7922) from Device Manager.
2. Go to your laptop maker's support site and download their WiFi driver for your exact model — install it first.
3. If problems persist, look for a newer MediaTek driver: check the support pages for newer laptop models using the same card, or MediaTek's official driver resources.
4. In Device Manager, uninstall the current WiFi adapter with driver deletion, then install the chosen package and restart.
5. Verify the driver date in the Driver tab — if Windows Update immediately replaces it, block the offering with the show/hide updates troubleshooter.

### Fix 2: Disable power management on the card

MediaTek cards and Windows power saving are a bad combination.

1. In Device Manager, right-click the MediaTek adapter > **Properties** > **Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. In the **Advanced** tab, find power-related properties and set them to **Maximum Performance**.
4. Disable **Fast Startup** (Control Panel > Power Options > Choose what the power buttons do) — MediaTek resume bugs love fast startup states.

### Fix 3: Separate Bluetooth from WiFi contention

Test whether coexistence is your problem.

1. Temporarily turn Bluetooth off and use WiFi for an hour. If drops stop, you've confirmed coexistence issues.
2. Update to the newest MediaTek driver (Fix 1) — coexistence handling improved significantly across driver generations.
3. Move your WiFi to the **5GHz band** (or 6GHz if supported) to get off Bluetooth's 2.4GHz spectrum.
4. In the driver's Advanced tab, look for **Bluetooth Collaboration** or coexistence settings and experiment with them.

### Fix 4: Fix band detection (5GHz/6GHz missing)

MediaTek-specific band quirks.

1. In the driver's **Advanced** tab, check **Preferred Band** — set to **5GHz** or **No Preference** (not 2.4GHz-only).
2. Verify **802.11a/b/g/n/ac/ax** modes are enabled, not restricted.
3. On the router, set the 5GHz channel to 36 or 40 for maximum compatibility during testing.
4. For 6GHz (MT7922): confirm your region supports it and the router's 6GHz SSID is broadcasting — early drivers had region-detection bugs hiding 6GHz.

### Fix 5: Adjust router compatibility settings

Older MediaTek drivers choke on modern router features.

1. In the router settings, try disabling **band steering / Smart Connect** temporarily and use separate SSIDs.
2. If the card won't connect at all, try setting the router's security to **WPA2** (not WPA3-only) as a test.
3. Disable **802.11ax-only / WiFi 6-only** mode on the router if present — let it run mixed mode.
4. Re-enable features one at a time after stabilizing to find the incompatible one.

### Fix 6: Reset the network stack and power-drain

Clears the stuck states MediaTek cards are prone to.

1. Run in elevated terminal: `netsh winsock reset`, `netsh int ip reset`, then restart.
2. For enumeration failures (card missing after sleep): shut down, unplug everything, hold power 30 seconds, then boot.
3. This power drain resets the embedded controller state that MediaTek resume bugs corrupt.

### Fix 7: Consider replacing the card

The permanent exit from MediaTek driver roulette.

1. If you've tried multiple driver versions and the card still drops, an Intel AX210 card is a drop-in M.2 replacement for most laptops (check your model's whitelist — some Lenovos and HPs restrict cards in BIOS).
2. The AX210 costs little, installs in minutes, and ends the driver-version lottery permanently.
3. Keep the MediaTek card as a spare — it works fine in desktops with PCIe adapters where power management isn't a factor.

For general WiFi adapter disappearance, see [the missing adapter guide](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/), and for 5GHz issues, our [5GHz connection guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/).

## Closing

MediaTek WiFi problems are driver-version problems wearing different disguises — disconnects, missing bands, Bluetooth interference, and resume failures all trace back to which driver build is installed. The winning move is deliberate driver selection (manufacturer-validated first, newer MediaTek builds second) plus taming power management, which these cards handle worse than their Intel counterparts. And if you'd rather stop playing driver roulette entirely, the Intel AX210 swap is one of the highest satisfaction-per-dollar upgrades in laptop ownership.
