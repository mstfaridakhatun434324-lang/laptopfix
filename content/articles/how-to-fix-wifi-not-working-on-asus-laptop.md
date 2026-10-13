---
title: "WiFi Not Working on Your ASUS Laptop? How to Fix It"
slug: how-to-fix-wifi-not-working-on-asus-laptop
date: "2026-09-11"
categories: ["drivers"]
tags: ["asus wifi", "asus drivers", "wireless adapter", "myasus", "wifi fix"]
description: "WiFi not working on your ASUS laptop? This ASUS-specific guide covers the Fn key toggle, MyASUS, ASUS drivers, and proven fixes for ASUS wireless problems."
thumbnail: "/images/thumbs/how-to-fix-wifi-not-working-on-asus-laptop.webp"
faqs:
- q: "Which Fn key enables WiFi on an ASUS laptop?"
  a: "On most ASUS laptops it is Fn + F2, marked with a wireless icon — though ROG and TUF gaming models sometimes use a different key, so check your function row icons. The toggle switches the wireless radio with no confirmation message, making accidental presses a top cause of sudden WiFi loss. If the key combination does nothing, the ASUS hotkey software or ATK package may need reinstalling from ASUS support."
- q: "Where do I download WiFi drivers for my ASUS laptop?"
  a: "From the ASUS support site: enter your model (VivoBook, ZenBook, ROG, TUF, and so on) and download the Wireless driver for your Windows version. The MyASUS app can also check for and install driver updates tailored to your machine. Prefer ASUS's driver over generic versions, since ASUS customizes wireless behavior per model, particularly on gaming laptops with specialized antenna layouts."
- q: "Can Armoury Crate or MyASUS break WiFi?"
  a: "Rarely directly, but these utilities manage power profiles and updates that can indirectly affect wireless — an aggressive power profile may throttle the adapter, and a bad driver pushed through MyASUS can destabilize a working setup. If WiFi broke right after a MyASUS-suggested update, roll back the wireless driver in Device Manager and report the issue through the app rather than reinstalling everything."
- q: "Why does my ASUS laptop disconnect from WiFi during gaming?"
  a: "Gaming laptops push the wireless card hard while generating significant heat, and the combination of thermal stress plus aggressive power saving causes drops. Disable power management on the wireless adapter in Device Manager, set Armoury Crate to a performance profile rather than silent, and prefer the 5GHz band. If drops persist only under load, the card may be overheating — ensure vents are clear."
---

ASUS laptops span VivoBook ultraportables, ZenBook flagships, and ROG/TUF gaming machines — and each line has its own WiFi personality. The Fn + F2 radio toggle is bumped constantly. MyASUS pushes driver updates on its own schedule. Gaming models run hot enough to stress the wireless card. And ASUS's BIOS layouts hide the wireless toggle in places you would not think to look.

This guide targets those ASUS specifics — the keys, the apps, the driver sources, the BIOS — alongside the universal Windows wireless repairs. Whether your ASUS lost WiFi after an update, drops connections hourly, or shows no wireless at all, the fix is in the sequence below.

## Why this happens

- **Fn + F2 radio toggle bumped**: ASUS's wireless key switches the radio silently; accidental presses are extremely common.
- **MyASUS driver update gone wrong**: A pushed wireless driver can destabilize a previously working setup.
- **Aggressive power profiles**: Silent/eco modes in Armoury Crate or MyASUS throttle the wireless adapter.
- **ATK/hotkey package missing**: After clean installs, Fn keys do nothing without ASUS's hotkey software.
- **BIOS wireless toggle**: Some ASUS BIOS versions include a WLAN switch that updates reset.
- **Corrupted wireless driver**: Standard Windows driver corruption, hitting ASUS models like any other.
- **Heat-related card instability**: Gaming laptops' thermals can push marginal wireless cards into dropping.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the ASUS wireless toggle and MyASUS

Start with ASUS's own controls. Fn + F2 toggles the radio with no on-screen confirmation on many models, and MyASUS shows the radio state explicitly. Between the key, Windows airplane mode, and any physical switch, all three must agree for WiFi to work. This thirty-second check resolves a large share of sudden ASUS WiFi losses.

1. Press Fn + F2 (wireless icon key) and wait ten seconds.
2. Open Quick Settings (Win + A) and ensure Airplane mode is off.
3. Open the MyASUS app and check the wireless/radio status there.
4. If Fn + F2 does nothing, install the ASUS ATK Package / hotkey driver from ASUS support.
5. Restart and test the connection.

### Fix 2: Install the ASUS wireless driver for your model

ASUS customizes wireless drivers per model line — antenna tuning on ZenBooks, gaming-optimized settings on ROG — and the generic Windows driver skips all of it. After Windows updates or clean installs, the ASUS Wireless driver package from the support site is the correct foundation. MyASUS can also deliver it, but the support site gives you version control.

1. Find your exact model on the bottom sticker (e.g., VivoBook 15 X515, ROG Strix G15).
2. On the ASUS support site, enter the model and open Drivers & Tools for your Windows version.
3. Download the Wireless driver package and install it, then restart.
4. For Intel-based wireless, [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can provide the latest stable version as an alternative.
5. Reconnect to WiFi and verify the adapter shows no warnings in Device Manager.

### Fix 3: Clean-reinstall the wireless adapter driver

When the driver is present but corrupt — warning icons, connects-then-drops, or identical misbehavior after simple reinstalls — remove it completely before installing ASUS's package. The full removal (including driver software) prevents old corruption from surviving into the fresh install.

1. Open Device Manager (Win + X) and expand "Network adapters."
2. Right-click the wireless adapter, choose "Uninstall device," and tick "Attempt to remove the driver."
3. Restart the laptop.
4. Install the ASUS wireless driver from Fix 2 and restart again.
5. Test stability for at least fifteen minutes, including on battery power.

### Fix 4: Disable power saving on the adapter and in profiles

ASUS power profiles — especially Silent mode in Armoury Crate and battery-saver settings — can starve the wireless card. The adapter-level power management toggle in Device Manager is the direct fix; the profile setting is the indirect one. Disabling both stops the card from sleeping mid-session, which is the classic cause of hourly disconnects.

1. In Device Manager, right-click the wireless adapter, open Properties.
2. On the Power Management tab, untick "Allow the computer to turn off this device to save power."
3. On the Advanced tab, set any power-saving property to "Maximum Performance."
4. In Armoury Crate or MyASUS, switch from Silent to Performance/Balanced profile for testing.
5. Restart and monitor — disconnects should stop if power saving was the cause.

### Fix 5: Check the wireless toggle in ASUS BIOS

ASUS BIOS (UEFI) on many models includes a network stack or WLAN control, sometimes under Advanced, sometimes under Security. BIOS updates occasionally reset it. A disabled radio at firmware level is invisible to Windows — no adapter, no WiFi option — and only a BIOS visit reveals it.

1. Restart and press F2 or Del to enter the ASUS BIOS/UEFI setup.
2. Look under Advanced or Security for wireless/WLAN/network stack options.
3. Ensure wireless is enabled.
4. Save and exit (F10), then boot into Windows.
5. Check Quick Settings for the return of the WiFi tile.

### Fix 6: Reset network settings and flush bad profiles

When the adapter is healthy but connections fail — "Can't connect to this network" on known-good routers — the saved profile or the TCP/IP stack is corrupt. Forgetting the network and resetting the stack clears both layers. This is the right fix when other devices connect fine but the ASUS will not, despite a good driver.

1. Go to Settings, Network and internet, WiFi, "Manage known networks," and Forget the network.
2. Open an admin terminal; run `netsh winsock reset` and `netsh int ip reset`.
3. Alternatively, use Settings, Network and internet, Advanced network settings, "Network reset" (this also deletes saved passwords — note them first).
4. Restart and reconnect, entering the password carefully.
5. If it still fails, check the router for MAC filtering or firmware issues. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) cover additional network diagnostics.

### Fix 7: Test the hardware with a Linux live USB

If no driver version makes the adapter appear or behave, test below Windows. A Linux live USB sees the wireless card independently of every Windows driver and setting: working there means a Windows-side problem (consider a Windows refresh); absent there too means the card is dead or unseated. Most ASUS models use standard M.2 cards, and a USB WiFi adapter is an instant bypass.

1. Boot a Linux live USB and check for available WiFi networks.
2. Working in Linux points at Windows — back up data and consider refreshing the OS.
3. Dead in both means hardware — reseat the M.2 card if comfortable opening the machine.
4. Replacement Intel AX-series cards are inexpensive and widely compatible.
5. Or use a USB WiFi adapter — five minutes, no disassembly.

For the same toggle-and-driver pattern on another brand, see the [Acer laptop WiFi guide](/articles/how-to-fix-wifi-not-working-on-acer-laptop/). If the adapter is missing from Device Manager entirely, the [network adapter missing guide](/articles/how-to-fix-network-adapter-missing-youtube/) covers that deeper case.

## Closing

ASUS WiFi problems orbit a familiar set: the Fn + F2 toggle, MyASUS driver updates, aggressive power profiles, and the standard Windows driver corruption that hits every brand. Check the toggle, install ASUS's wireless driver for your exact model, and disable adapter power saving. That sequence restores wireless on the overwhelming majority of ASUS laptops.
