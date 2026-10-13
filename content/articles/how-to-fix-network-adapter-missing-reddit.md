---
title: "How to Fix a Missing Network Adapter on Windows"
slug: how-to-fix-network-adapter-missing-reddit
date: 2026-10-08
categories: ["drivers"]
tags: ["network adapter missing", "no internet", "ethernet adapter", "device manager", "network reset"]
description: "Network adapter gone from Device Manager — no Wi-Fi, no Ethernet? Recovery steps for vanished network adapters on Windows 11 and 10."
thumbnail: "/images/thumbs/how-to-fix-network-adapter-missing-reddit.webp"
faqs:
  - q: "What's the difference between a missing and a disabled network adapter?"
    a: "A disabled adapter appears in Device Manager with a down-arrow icon — right-click and Enable fixes it. A missing adapter doesn't appear at all, even with hidden devices shown. Disabled is a configuration state you reverse in seconds; missing means Windows can't enumerate the hardware, which needs the BIOS, driver, and power-state checks in this guide."
  - q: "Can I still get online with no network adapter showing?"
    a: "Yes, via workarounds: USB tethering from your phone (which presents as a separate network device), a USB Wi-Fi or USB Ethernet adapter, or Bluetooth tethering. These use independent drivers, so they work even when the internal adapters are missing. USB phone tethering is the fastest bridge — most people have the cable already."
  - q: "Why do both Wi-Fi and Ethernet disappear at the same time?"
    a: "Both vanishing together points above the individual adapters: a corrupted network stack, a bad chipset driver (both adapters hang off chipset controllers), a BIOS setting, or a Windows update that damaged shared networking components. Fix the shared layer — network reset, chipset driver, BIOS check — rather than chasing each adapter separately."
  - q: "Will resetting Windows bring back a missing network adapter?"
    a: "A reset fixes software causes — corrupted stacks, broken drivers, damaged system files — but not BIOS-disabled or physically failed hardware. It's the last resort precisely because it's disruptive. Work through this guide first: the BIOS check and driver reinstall resolve most cases without touching your files and apps."
---

When every network adapter vanishes — no Wi-Fi, no Ethernet, Device Manager's Network adapters section empty or absent — the laptop is an island. No internet means no downloading drivers, no Windows Update, no remote help. The urgency is real, but the fix sequence is methodical: this is an enumeration problem, and enumeration problems have a finite list of causes.

This guide covers both adapters together and each separately, plus the offline bridge tactics that get you downloading drivers again. For Wi-Fi-only disappearances, our [Wi-Fi adapter guide](/articles/what-to-do-if-wifi-adapter-not-showing-up/) goes deeper on the wireless-specific causes.

## Why this happens

- **Corrupted network stack.** Winsock/TCP-IP damage can suppress adapter enumeration.
- **Failed chipset driver.** Both adapters depend on chipset controllers; a bad chipset driver takes down all networking.
- **BIOS disabled the adapters.** Firmware toggles for WLAN and LAN hide them from Windows entirely.
- **A Windows update broke the drivers.** Update-delivered network drivers occasionally fail catastrophically.
- **Power-state corruption.** Sleep/hibernate bugs can leave adapters unenumerated until fully power-cycled.
- **Third-party VPN/filter drivers.** Network filter drivers from VPNs or security suites can wedge the stack.
- **Hardware failure.** Dead controllers don't enumerate — the diagnosis of exclusion.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices and check for disabled adapters

First, establish exactly what's missing versus hidden versus disabled.

1. Open **Device Manager**, click **View > Show hidden devices**.
2. Expand **Network adapters** — note grayed-out entries (disconnected) and any with down arrows (disabled; right-click > **Enable device**).
3. Check **Other devices** for unknown entries that may be your adapters without drivers.
4. Click **Action > Scan for hardware changes** and watch for reappearance.

A disabled adapter found here is a thirty-second fix — enable it and move on. The distinction matters because everything below assumes true absence; don't do BIOS surgery for a right-click problem.

### Fix 2: Get online via a bridge device

Before deeper fixes, establish a way to download drivers — you'll likely need it.

1. Connect your phone via USB and enable **USB tethering** — Windows sees it as a new network adapter independent of the missing ones.
2. Alternatively, use a USB Wi-Fi or USB Ethernet adapter if you have one.
3. Confirm the bridge connection works by loading a webpage.
4. Keep the bridge connected through the driver fixes below — you'll fetch packages with it.

USB tethering is the unsung hero of network troubleshooting: it bypasses the entire internal network hardware. With it active, the pressure drops — you can download drivers, search error codes, and work methodically instead of frantically.

### Fix 3: Check BIOS for LAN/WLAN toggles

Firmware can hide network hardware from the OS without any Windows-visible trace.

1. Restart into BIOS/UEFI setup.
2. Look for **Integrated NIC**, **WLAN**, **Wireless**, or **Onboard LAN** settings — enable everything network-related.
3. Check for **Deep Sleep** or power settings that might gate the controllers.
4. Save, exit, and re-check Device Manager after booting.

Some BIOSes have separate toggles for wired and wireless — verify both. If the toggles were already enabled, note that too; it eliminates firmware from the suspect list and moves focus to drivers.

### Fix 4: Reinstall chipset and network drivers

The chipset driver is the foundation; network drivers build on it.

1. Using your bridge connection, download the **chipset** driver for your exact model from the manufacturer — [Dell](https://www.dell.com/support) or [HP](https://support.hp.com/us-en).
2. Download the **wired (Ethernet)** and **wireless** drivers too.
3. In Device Manager (hidden devices shown), uninstall any network-related entries, ticking **Attempt to remove the driver**.
4. Install chipset first, restart, then network drivers, then restart again.

The chipset-first ordering is structural, not ritual: network controllers are PCIe/USB devices managed through chipset logic. Installing network drivers onto a broken chipset foundation reproduces the failure. For machines with no bridge available, our [offline driver guide](/articles/how-can-i-install-drivers-without-internet/) covers the USB transfer method.

### Fix 5: Remove VPN and filter drivers

Third-party network filters can wedge enumeration for all adapters.

1. Uninstall VPN clients temporarily via **Settings > Apps**.
2. In an elevated Command Prompt, run `netsh winsock reset` and `netsh int ip reset`.
3. Open **Network Connections** (ncpa.cpl), right-click any connection > **Properties**, and uninstall non-Microsoft protocol/filter entries you recognize as third-party.
4. Restart and check whether the adapters reappear.

VPN filter drivers operate at a layer below the adapters themselves — when they corrupt, they can take down the whole network device enumeration. The winsock reset clears their hooks. Reinstall the VPN afterward if you need it; a fresh install rarely reproduces the corruption.

### Fix 6: Full power-drain and network reset

Combine the deepest software reset with the deepest power reset.

1. Shut down completely, disconnect all power, and hold the power button 30 seconds (remove the battery if possible).
2. Boot up, then run **Settings > Network & internet > Advanced network settings > Network reset**.
3. After the restart, reinstall the chipset and network drivers from Fix 4 onto the clean configuration.
4. Re-check Device Manager before reconnecting VPNs or custom network software.

The order — power drain, then network reset, then driver reinstall — ensures each layer is clean before the next is built on it. Reversing the order (drivers before reset) is the common mistake that forces a second pass.

### Fix 7: Diagnose hardware failure

When software is exhausted, determine whether the controllers are dead.

1. Boot a Linux live USB and check whether the network adapters appear there — if yes, it's a Windows problem, not hardware.
2. Run the manufacturer's built-in hardware diagnostics (all major vendors include network controller tests).
3. If both adapters fail everywhere and diagnostics confirm it, the fault is likely the chipset or board — professional repair.
4. As a permanent workaround, USB network adapters are cheap and fully functional — many users simply adopt one rather than repairing the board.

The Linux test is decisive: hardware that enumerates in Linux but not Windows is a Windows problem by definition. If it fails in both, you've earned the hardware verdict — and the USB adapter workaround means even that verdict doesn't have to end the laptop's useful life.

## Closing

A missing network adapter is an enumeration failure with a short suspect list: hidden, disabled, BIOS-gated, driverless, stack-corrupted, or dead. The bridge connection (Fix 2) is the tactical key — it converts a no-internet emergency into a routine driver job. Work the list in order, and the adapter reappears; if it doesn't, the Linux test tells you honestly whether you're fighting software or shopping for a USB adapter.
