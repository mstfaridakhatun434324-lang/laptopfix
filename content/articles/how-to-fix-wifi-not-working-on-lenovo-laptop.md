---
title: "WiFi Not Working on Your Lenovo Laptop? How to Fix It"
slug: how-to-fix-wifi-not-working-on-lenovo-laptop
date: 2026-10-09
categories: ["drivers"]
tags: ["lenovo wifi not working", "thinkpad wifi fix", "ideapad wifi problem", "lenovo wireless driver", "wifi keeps disconnecting lenovo"]
description: "WiFi broken on your ThinkPad, IdeaPad, or Legion? Use Lenovo's own tools — Vantage, System Update, and the wireless driver packages — plus these Windows fixes."
thumbnail: "/images/thumbs/how-to-fix-wifi-not-working-on-lenovo-laptop.webp"
faqs:
  - q: "Why does WiFi keep disconnecting on my Lenovo laptop?"
    a: "The most common cause is power management: Lenovo's power plans aggressively sleep the wireless adapter, and it doesn't always wake cleanly. Disable 'Allow the computer to turn off this device to save power' on the WiFi adapter in Device Manager, and set the wireless adapter power saving to Maximum Performance in the advanced power settings. Outdated Intel or Realtek drivers from Windows Update are the second major cause — install Lenovo's own wireless driver package instead."
  - q: "What is Lenovo Vantage and does it help with WiFi problems?"
    a: "Lenovo Vantage is Lenovo's preinstalled management app that handles driver updates, hardware scans, and WiFi security settings for your specific model. Its hardware scan can test the wireless card, and its update section delivers Lenovo-validated drivers — which are preferable to generic Windows Update drivers for ThinkPads and IdeaPads. It's the first place to check for model-specific wireless fixes and known-issue advisories."
  - q: "My Lenovo has a WiFi switch or airplane mode key. Where is it?"
    a: "Most modern Lenovos use the F8 key (with the antenna/airplane icon) often combined with Fn, toggled via Settings > Bluetooth & devices or Win + A. Older ThinkPads had a physical wireless switch on the side or front edge — check there if your model has one. In the BIOS, ThinkPads also have a Security > I/O Port Access toggle for wireless LAN that can disable the radio below the OS level."
  - q: "Should I use Lenovo's drivers or Intel's for WiFi?"
    a: "Start with Lenovo's driver from their support site or Vantage — it's validated for your exact model's antenna configuration and power tables. If Lenovo's driver is very old and you're having issues fixed in newer Intel releases, Intel's generic driver usually works fine on Intel cards, but you may lose Lenovo-specific power optimizations. For Realtek and MediaTek cards in IdeaPads, stick with Lenovo's package; generic drivers for those chips are less reliable."
---

Lenovo's ThinkPad, IdeaPad, Legion, and Yoga lines share Windows' generic WiFi failure modes, but they add Lenovo-specific layers: the Vantage management app, Lenovo System Update, model-specific wireless drivers, function-key radio toggles, and BIOS-level wireless controls on ThinkPads. Knowing which Lenovo tools to use — and when to bypass them for the chip maker's driver — is the difference between a ten-minute fix and an afternoon of frustration.

This guide starts with Lenovo's own utilities (they're genuinely useful here), then moves through the Windows-side fixes that apply to every brand.

Lenovo's lineup matters for WiFi troubleshooting more than most brands, because the wireless experience differs across it. ThinkPads (the business line) tend to use Intel wireless cards with Lenovo-validated drivers and have the BIOS-level wireless toggles; IdeaPads (the consumer line) more often ship with Realtek or MediaTek cards where driver choice matters enormously; Legions (gaming) push high throughput where band and channel settings dominate. The fixes below are ordered to work across all of them, but pay special attention to the driver-source guidance — on IdeaPads with non-Intel cards, installing the wrong vendor's generic driver is the single fastest way to make WiFi worse. When in doubt, Lenovo's package for your exact model is always the safe choice; experiment with chip-maker drivers only after the validated one is working. That conservative order keeps you from trading a known-good setup for an unknown one.

## Why this happens

- **Power management sleeping the adapter** — Lenovo power plans are aggressive about this.
- **Windows Update replaced Lenovo's wireless driver** with a generic one lacking model-specific tuning.
- **Airplane mode / function-key radio toggle** (F8) engaged accidentally.
- **ThinkPad BIOS wireless LAN disabled** under Security > I/O Port Access.
- **Corrupted wireless profile** for the specific network.
- **Lenovo Vantage WiFi security settings** interfering with certain networks.
- **Antenna or card issue** — loose M.2 card after a drop, or failing hardware.
- **Router-side incompatibility** (band, channel, security mode) with the specific card.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the radio toggles

Lenovo's toggles are easy to hit accidentally.

1. Press **Win + A** and confirm **Airplane mode** is off and **WiFi** is on.
2. Try **Fn + F8** (the key with the antenna icon on most Lenovos).
3. On older ThinkPads, check the physical wireless switch on the side or front edge.
4. If the WiFi option is missing entirely from Quick Settings, that's a driver problem — skip to Fix 4.

### Fix 2: Run Lenovo Vantage diagnostics and updates

Lenovo's own tool, genuinely useful for wireless issues.

1. Open **Lenovo Vantage** (install from the Microsoft Store if missing).
2. Run the **hardware scan** — it tests the wireless card independently of Windows networking.
3. Go to **System Update** and install any wireless/WiFi driver updates offered. These are Lenovo-validated for your model.
4. Check Vantage's **WiFi Security** or advisory sections for known issues with your model.

### Fix 3: Disable power management on the wireless adapter

The #1 fix for Lenovo WiFi disconnects.

1. Press **Win + X**, open **Device Manager**, expand **Network adapters**.
2. Right-click the wireless adapter > **Properties** > **Power Management** tab.
3. Uncheck **Allow the computer to turn off this device to save power**.
4. In the **Advanced** tab, set power-saving-related properties (Power Saving Mode, Roaming Aggressiveness) to **Maximum Performance** while testing.
5. In **Settings > System > Power & battery**, avoid the extreme battery-saver modes during testing.

### Fix 4: Install Lenovo's wireless driver package

Replaces the generic driver Windows Update installed.

1. Go to [Lenovo's support site](https://support.lenovo.com/us/en/), enter your serial number or model.
2. Download the **WLAN/WiFi driver** for your exact model and Windows version.
3. In Device Manager, uninstall the wireless adapter, ticking driver deletion.
4. Install Lenovo's package and restart. Verify in the Driver tab that the provider is now Intel/Realtek via Lenovo's package date, not Microsoft's.

### Fix 5: Forget and rejoin the network

Clears corrupted wireless profiles.

1. Go to **Settings > Network & internet > WiFi > Manage known networks**.
2. Select the problem network and click **Forget**.
3. Reconnect fresh, carefully re-entering the password.
4. If it connects but has no internet, run `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns` in an elevated terminal.

### Fix 6: Reset the network stack

For persistent "connected, no internet" or repeated drops.

1. Open **Terminal (Admin)** and run:
   `netsh winsock reset`
   `netsh int ip reset`
2. Restart and reconnect.
3. This is also worth doing after major Windows updates that shuffle network components.

### Fix 7: Check ThinkPad BIOS wireless settings

When the adapter is missing at the system level.

1. Enter BIOS (**F1** on most ThinkPads during boot, or via Settings > Recovery > Advanced startup).
2. Go to **Security > I/O Port Access** and confirm **Wireless LAN** is **Enabled**.
3. Check for a BIOS update on Lenovo's support site mentioning wireless or WLAN fixes.
4. Save and exit.

If the adapter itself has vanished from Device Manager, see [how to fix a missing WiFi adapter](/articles/how-to-fix-wifi-adapter-not-showing-up-on-lenovo-laptop/). For 5GHz-specific connection issues, our [5GHz guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-step-by-step/) covers band and channel fixes.

## Closing

On Lenovo laptops, the fix hierarchy is: radio toggles, Vantage's validated drivers, power management off, then the standard Windows network repairs. The power-management step deserves emphasis — Lenovo's aggressive power plans cause more WiFi grief than any other single factor on these machines, and unchecking one box in Device Manager permanently ends it. If WiFi is stable now but you want to share the connection, our [hotspot troubleshooting guide](/articles/how-to-fix-hotspot-not-working-on-laptop-in-windows-11-24h2/) covers turning the laptop into an access point. Lastly, if disconnects return after a Windows feature update, check the driver provider in Device Manager first — updates replacing Lenovo's validated wireless driver with a generic one is a recurring pattern, and reinstalling Lenovo's package is a two-minute fix once you recognize the signature.
