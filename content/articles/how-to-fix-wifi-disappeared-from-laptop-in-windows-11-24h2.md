---
title: "Wi-Fi Disappeared on Windows 11 24H2? Bring the Adapter Back"
slug: how-to-fix-wifi-disappeared-from-laptop-in-windows-11-24h2
date: 2026-09-15
categories: ["drivers"]
tags: ["wifi disappeared", "windows 11 24h2", "network adapter", "no wifi option"]
description: "Fix Wi-Fi disappearing on Windows 11 24H2: recover a missing wireless adapter in Device Manager, reinstall the Wi-Fi driver, and stop 24H2 from breaking it again."
thumbnail: "/images/thumbs/how-to-fix-wifi-disappeared-from-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why did the Wi-Fi option completely vanish after the 24H2 update?"
    a: "The 24H2 update migrates network drivers during installation, and on some systems it completes the migration with a driver the adapter cannot start. The result is an adapter that is either missing from Device Manager or flagged with an error, so Windows removes the Wi-Fi quick setting entirely. Reinstalling the vendor's driver for your exact model restores it."
  - q: "What is the difference between no Wi-Fi networks and no Wi-Fi option?"
    a: "No networks with a visible Wi-Fi icon means the adapter works but cannot see or join anything — usually a router or configuration issue. No Wi-Fi option at all, with only airplane mode or Ethernet shown, means Windows cannot see a working adapter — a driver or hardware-enumeration problem. This guide targets the second case."
  - q: "Will a network reset bring back a missing Wi-Fi adapter?"
    a: "Rarely on its own. Network reset clears configuration, but a vanished adapter is a driver or enumeration failure, not a configuration problem. Run the driver steps in this guide first; use network reset afterward only if the adapter returns but connections still misbehave."
  - q: "How do I prevent 24H2 from breaking my Wi-Fi again?"
    a: "Install the newest Wi-Fi driver from your laptop vendor before major updates, and consider pausing automatic driver updates once a known-good driver is in place. Keeping a copy of the working driver installer on a USB stick means you can reinstall offline if a future update breaks the adapter again."
---

After the Windows 11 24H2 update, some laptops boot up to a nasty surprise: the Wi-Fi icon is gone, the network quick setting shows only airplane mode, and Settings lists no wireless adapter at all. The laptop is not broken — Windows simply cannot see a working Wi-Fi adapter anymore, so it hides every trace of wireless from the interface. Ethernet over USB-C still works, which makes the situation even more confusing.

The 24H2 update performs a driver migration during installation, and wireless drivers are among the most fragile pieces it touches. If the migration finishes with a mismatched or half-installed driver, the adapter fails to start and Windows treats it as absent. In rarer cases the update exposes a latent BIOS or power-management issue that the old driver happened to tolerate. Either way, the adapter is usually recoverable without new hardware.

This guide is ordered to bring the adapter back with minimum risk: confirm what Windows sees, force re-enumeration, reinstall the correct driver, fix the power settings that kill adapters after sleep, and only then touch the BIOS and network stack.

## Why this happens

- **Failed driver migration during 24H2 setup:** The update replaces the working Wi-Fi driver with a version the adapter cannot start. Device Manager shows the adapter with a warning or hides it under unknown devices.
- **Adapter disabled at the device level:** The migration can leave the adapter in a disabled state. Windows then removes the Wi-Fi UI completely instead of showing a disabled adapter.
- **Power management killing the card:** 24H2's power policies can shut the wireless card down and fail to reinitialize it. The adapter vanishes after sleep and never comes back until a reboot — or not even then.
- **Airplane mode stuck on:** The update can leave the radio in a software airplane-mode state that the quick-settings toggle cannot clear, especially on laptops with a hardware radio key.
- **BIOS wireless setting flipped:** Some systems come out of the 24H2 update plus its bundled firmware updates with the WLAN device disabled in BIOS.
- **Corrupted driver store entries:** A half-written driver package from the failed migration poisons every automatic reinstall until it is deleted from the driver store.
- **Third-party VPN or filter drivers:** VPN clients and network filters that are incompatible with 24H2 can block the adapter from binding to TCP/IP, which Windows reports by hiding the adapter.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm what Windows actually sees

Diagnosis first. Whether the adapter is missing, disabled, or error-flagged determines which fix applies, and guessing wastes time.

1. Open Device Manager, expand Network adapters, and note exactly what is listed.
1. Click View, then Show hidden devices, and look for grayed-out wireless entries.
1. Check Settings, then Network and internet, and see whether Wi-Fi appears at all. A grayed-out adapter needs re-enabling; a missing one needs the driver steps below.

### Fix 2: Re-enable and rescan for the adapter

If the adapter is present but grayed out or flagged, a clean re-enumeration often restores it without any downloads.

1. Right-click the wireless adapter and choose Enable device if available.
1. If it shows a warning, choose Uninstall device without deleting the driver, then click Action and Scan for hardware changes.
1. Restart and check whether the Wi-Fi icon returns. If the adapter is still missing, continue.

### Fix 3: Perform a full power-cycle reset of the radio

Wireless cards can wedge in a low-power state that survives warm reboots. A full shutdown with the power drained forces the card to cold-start.

1. Shut the laptop down completely — not sleep, not hibernate.
1. Unplug the charger, hold the power button for fifteen seconds, then reconnect power.
1. Boot up and check for the Wi-Fi option. This also clears stuck airplane-mode states on many models.

### Fix 4: Reinstall the Wi-Fi driver from the vendor

This is the definitive fix for migration-broken drivers. The vendor's package is validated against your exact model and the 24H2 build, which is what the migrated driver was not.

1. On another device, download the Wi-Fi driver for your exact model from the vendor's support site and copy it over on USB.
1. In Device Manager, uninstall the wireless adapter and check Delete the driver software for this device.
1. Install the downloaded package and restart. Intel-based cards can also use Intel's [Driver and Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for the newest generic driver.

### Fix 5: Disable adapter power management

Once the adapter is back, stop Windows from killing it again. 24H2 is aggressive about powering down wireless cards, and some drivers never recover cleanly.

1. In the adapter's Properties, open the Power Management tab.
1. Uncheck Allow the computer to turn off this device to save power.
1. In the Advanced tab, set any power-saving or sleep-related properties to Maximum Performance while you verify stability over several sleep cycles.

### Fix 6: Check BIOS and the physical radio switch

If the adapter will not appear no matter what driver you install, look below the operating system. These checks take minutes and rule out hardware-level disables.

1. Enter the BIOS and confirm the WLAN or wireless device is Enabled.
1. Press the laptop's wireless Fn key and confirm the radio indicator responds.
1. Boot a live Linux USB if available: if Wi-Fi works there, the hardware is fine and the problem is strictly Windows-side.

### Fix 7: Reset the network stack and remove filter drivers

With the adapter visible again, clear any corrupted configuration or incompatible filters left behind by the update.

1. Temporarily uninstall third-party VPN clients, then reinstall them from 24H2-compatible versions afterward.
1. In an elevated Command Prompt, run netsh winsock reset and netsh int ip reset, then restart.
1. If the adapter shows but cannot see 5 GHz networks specifically, follow [5 GHz troubleshooting](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/). For a single Intel card with its own error code, see the [AX201 fix guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-on-lenovo-laptop/).

## Closing

A vanished Wi-Fi adapter after 24H2 looks catastrophic but is almost always a driver migration casualty, not dead hardware. Confirm the adapter's state, reinstall the vendor's driver cleanly, and lock down power management so it cannot happen again. Keep that driver installer on a USB stick — the next feature update will be a lot less stressful when you are prepared for it.
