---
title: "MediaTek Wi-Fi Not Working on ASUS Laptop? Complete Fix"
slug: "how-to-fix-mediatek-wifi-not-working-on-asus-laptop"
date: 2026-09-14
categories: ["drivers"]
tags: ["mediatek wifi", "asus laptop", "wifi dropping", "wireless driver", "wifi not working"]
description: "Wi-Fi dropping or missing on your ASUS laptop with MediaTek wireless? Fix it with ASUS driver reinstalls, power tweaks, and connection tuning."
thumbnail: "/images/thumbs/how-to-fix-mediatek-wifi-not-working-on-asus-laptop.webp"
faqs:
  - q: "How do I know if my ASUS laptop has a MediaTek Wi-Fi card?"
    a: "Open Device Manager, expand Network adapters, and read the wireless adapter name. MediaTek cards appear as MediaTek Wi-Fi 6 or MT7921 and similar names. ASUS also lists the wireless card in the specifications on the support page for your exact model. Knowing the card vendor matters because the fix uses the MediaTek-specific driver package from ASUS."
  - q: "Why does my ASUS Wi-Fi disconnect when the laptop sleeps?"
    a: "Sleep-related disconnects happen when the MediaTek card fails to resume cleanly or when Windows powers it down aggressively. Disable power management for the adapter in Device Manager, turn off USB-style selective suspend equivalents, and update to the latest ASUS MediaTek driver, which contains resume fixes. Disabling Fast Startup also helps when the bad state survives across boots."
  - q: "Should I install the MediaTek driver from ASUS or from Windows Update?"
    a: "Install it from ASUS. ASUS validates the MediaTek driver against the specific card and antenna configuration in your model, while Windows Update may deliver a generic version that causes drops or Code 10 errors. Download the WLAN driver from the ASUS support page for your exact model number after fully removing the old driver."
  - q: "My Wi-Fi is slow on the ASUS laptop but fast on my phone. Why?"
    a: "That comparison isolates the problem to the laptop, usually the driver, band selection, or power settings. Make sure the adapter prefers the 5GHz band near the router, disable power-saving features on the adapter, and update the ASUS MediaTek driver. Also check that the laptop is not falling back to 2.4GHz on a congested channel while the phone uses 5GHz."
---

ASUS pairs MediaTek wireless cards with many VivoBook, ZenBook, and TUF models, and the complaints follow a pattern: connections that drop every few minutes, speeds far below what other devices get, adapters that vanish after sleep, and the occasional Code 10 in Device Manager. The MediaTek hardware itself is capable; the driver and power configuration around it are usually what need fixing.

The core issue is version sensitivity. MediaTek drivers interact closely with Windows power management, and a mismatched or generic driver produces exactly the instability users report. ASUS publishes validated MediaTek packages per model, and a clean install of the right one is the highest-yield fix.

This guide covers diagnosis, the clean reinstall, and the tuning that keeps the connection stable. Dell owners with the same card should see the [Dell MediaTek guide](/articles/how-to-fix-mediatek-wifi-not-working-on-dell-laptop/), and [Code 10 errors](/articles/how-to-fix-wifi-driver-code-10-error-on-asus-laptop/) have their own dedicated walkthrough.

## Why this happens

- **Generic driver from Windows Update:** a non-ASUS MediaTek driver mismatches the card firmware and causes drops.
- **Aggressive power management:** the card is suspended during idle and fails to resume cleanly.
- **Fast Startup stale state:** hybrid shutdown preserves broken wireless state across boots.
- **Band steering conflicts:** the card flaps between 2.4GHz and 5GHz on mesh networks.
- **Outdated ASUS driver:** older ASUS MediaTek releases contain known disconnect bugs fixed in later versions.
- **Router channel congestion:** crowded 2.4GHz channels degrade the connection regardless of driver.
- **Antenna or card seating:** rare on new machines, but possible after service or drops.
- **Conflicting VPN filters:** network filter drivers interfere with adapter initialization.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Identify the card and check its state

Confirming the MediaTek card model and its Device Manager state focuses the repair. An error code here changes which steps matter most.

1. Open Device Manager and expand Network adapters.
2. Confirm the adapter name contains MediaTek or MT7921.
3. Note any warning icon and error code such as Code 10.
4. Check the Driver tab for the provider and version.
5. Run the network troubleshooter for a baseline.

### Fix 2: Cold-boot to reset the card

MediaTek cards that vanish or error after sleep often need a full power drain to reinitialize. A cold boot clears card state that restarts preserve.

1. Shut down fully rather than restarting.
2. Unplug the charger and all peripherals.
3. Hold the power button for 20 seconds.
4. Wait one minute, reconnect the charger, and power on.
5. Check whether the adapter now appears and connects.

### Fix 3: Clean-reinstall the ASUS MediaTek driver

The central fix. Remove the mismatched driver entirely and install the WLAN package ASUS validated for your exact model.

1. In Device Manager, uninstall the MediaTek adapter with driver removal checked.
2. Restart the laptop.
3. Download the WLAN driver from the ASUS support page for your exact model.
4. Install the package and restart again.
5. Connect to your network and monitor stability for 30 minutes.

### Fix 4: Disable power management for the adapter

Power-saving features are the top cause of drops and slow resumes on MediaTek cards. Turning them off trades a little battery for a stable connection.

1. In the adapter Properties, uncheck Allow the computer to turn off this device.
2. On the Advanced tab, disable power-saving and selective suspend properties.
3. In Power Options, set Wireless Adapter Settings to Maximum Performance.
4. Disable Fast Startup in the power button settings.
5. Test stability on battery to confirm the fix holds.

### Fix 5: Tune bands and roaming

Default band and roaming behavior can keep the card on a congested or distant signal. Sensible preferences stabilize throughput and reduce drops.

1. In the adapter Advanced tab, set Preferred Band to 5GHz when near the router.
2. Set Roaming Aggressiveness to a middle value like 3.
3. Forget the network in Windows and reconnect fresh.
4. On the router, set a fixed 5GHz channel such as 36 or 44.
5. Test speed with a speed test site before and after.

### Fix 6: Reset the network stack

Corrupted profiles and stack settings survive driver changes. Resetting the stack gives the new driver a clean networking foundation.

1. Open Command Prompt as administrator.
2. Run netsh winsock reset.
3. Run netsh int ip reset.
4. Run ipconfig /flushdns.
5. Restart and reconnect to Wi-Fi from scratch.

### Fix 7: Update BIOS and verify the hardware

ASUS BIOS updates occasionally fix wireless power sequencing, and a final hardware check rules out the card itself.

1. Check your BIOS version against the latest on the ASUS support page.
2. Install any update mentioning wireless or device fixes with the charger connected.
3. Test with a Linux live USB to see if the card works outside Windows.
4. If it fails everywhere, the card or antenna needs service.
5. A USB Wi-Fi adapter works as an interim fix.

## Closing

MediaTek Wi-Fi on ASUS laptops stabilizes with the right formula: cold boot, clean ASUS driver install, power management off, and sensible band preferences. Apply those and the drops stop. Keep the ASUS driver installed and resist generic driver updaters afterward. Long-term stability for MediaTek Wi-Fi comes down to resisting two temptations: third-party driver updater tools, which love replacing the ASUS-validated driver with a generic one, and the urge to tweak every advanced adapter setting at once. Change one setting at a time and test for a day so you know what actually helped. If your router gets a firmware update and the drops return, recheck the band and channel settings first, since router updates sometimes reset those to defaults that the MediaTek card handled poorly in the first place. For Microsoft's official take on wireless adapter errors, see the [Windows support hub](https://support.microsoft.com/en-us/windows), which documents the network reset and driver rollback steps referenced above. Keeping a copy of the working ASUS driver installer also means the next failure takes minutes to fix instead of an evening.
