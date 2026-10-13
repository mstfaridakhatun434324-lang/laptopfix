---
title: "Network Adapter Missing After a Windows 11 Update? Restore Connectivity"
slug: how-to-fix-network-adapter-missing-after-windows-11-update
date: 2026-09-24
categories: ["drivers"]
tags: ["network adapter", "missing adapter", "windows 11 update", "ethernet wifi"]
description: "Fix a missing network adapter after a Windows 11 update: recover vanished Wi-Fi and Ethernet adapters, reinstall network drivers, and repair the stack."
thumbnail: "/images/thumbs/how-to-fix-network-adapter-missing-after-windows-11-update.webp"
faqs:
  - q: "Why did both Wi-Fi and Ethernet disappear after the update?"
    a: "When every network adapter vanishes at once, the cause is usually system-wide rather than per-device: a failed network driver migration, a disabled network stack component, or third-party filter drivers (VPNs, firewalls) that broke during the update and now block all adapters from binding. Fixing the shared layer restores everything together."
  - q: "How is this different from the Wi-Fi option just being hidden?"
    a: "A hidden Wi-Fi option with Ethernet still working is a wireless-specific driver problem. All adapters missing — no Wi-Fi, no Ethernet, sometimes not even a Network adapters category in Device Manager — points to the migration or filter-driver causes in this guide. The distinction decides whether you chase one driver or repair the whole stack."
  - q: "Can I get online at all to download fixed drivers?"
    a: "Yes, usually. USB tethering from a phone presents itself as a separate network device that does not depend on the broken adapters, and it works even when every built-in adapter is missing. That tethered connection lets you download the correct drivers directly onto the laptop."
  - q: "Will resetting the network stack delete my saved Wi-Fi passwords?"
    a: "A network reset removes saved networks and passwords along with the configuration, so you will need to rejoin Wi-Fi afterward. It does not touch personal files. Because of that, treat it as a later step — recover the adapters first, then reset only if connections still misbehave."
---

A Windows 11 update reboots and the laptop is an island: no Wi-Fi icon, no Ethernet adapter, and Device Manager's Network adapters section is either empty or missing entirely. The machine works perfectly otherwise, which makes the total loss of connectivity feel surreal. This is different from a single misbehaving Wi-Fi card — when every network interface vanishes together, the failure is in a shared layer that all adapters depend on.

That shared layer is usually the driver migration that Windows performs during updates, which can complete with network drivers that fail to start, or third-party network filter drivers — VPN clients, firewall components — that break against the new build and prevent every adapter from binding to the TCP/IP stack. In both cases the hardware is fine; the software plumbing between the adapters and Windows is what collapsed.

The repair order below starts with revealing hidden adapters and removing the filter drivers that commonly cause system-wide loss, then reinstalls network drivers cleanly, and finishes with stack repairs. A phone's USB tethering is your lifeline for downloads throughout.

## Why this happens

- **Failed network driver migration:** The update migrates every network driver at once. If the migration corrupts the shared network components, all adapters fail together rather than individually.
- **Broken third-party filter drivers:** VPN and firewall filter drivers bind between adapters and the TCP/IP stack. An incompatible filter after an update can block every adapter from coming up.
- **Network adapters disabled en masse:** The migration can leave adapters in a disabled state. With all of them disabled, Windows shows no network UI at all.
- **Corrupted TCP/IP stack or Winsock:** Damage to the shared Winsock and TCP/IP configuration prevents adapters from binding even when their drivers are healthy.
- **Power management disabling devices:** Aggressive power policies applied during the update can switch adapters off at the device level across the board.
- **BIOS network stack settings:** On some business laptops, the update's bundled firmware changes can alter network stack or LAN/WLAN BIOS settings.
- **Driver store corruption:** Half-migrated driver packages poison reinstallation attempts until they are deleted from the driver store.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Get a lifeline connection via USB tethering

Before anything else, restore some form of internet. You will need it for driver downloads, and tethering bypasses the broken adapters entirely.

1. Connect your phone to the laptop with a USB cable.
1. Enable USB tethering in the phone's hotspot settings.
1. Confirm the laptop shows a new wired-style connection. This uses the phone as the network device, independent of the missing adapters.

### Fix 2: Reveal hidden adapters and check their state

See exactly what Windows knows before changing anything. Grayed-out adapters are a quick fix; truly absent ones need the driver steps.

1. Open Device Manager, click View, then Show hidden devices.
1. Expand Network adapters and note every entry, including grayed-out ones.
1. Right-click any grayed adapter and choose Enable device, then rescan for hardware changes from the Action menu.

### Fix 3: Remove third-party filter drivers

VPN clients and firewall filters are the top cause of all-adapters-missing. Remove them before reinstalling anything else.

1. Uninstall VPN clients and third-party firewall software from Apps.
1. In an elevated Command Prompt, run netsh winsock reset to clear layered providers.
1. Restart and check whether the built-in adapters reappear on their own — they often do once the broken filter is gone.

### Fix 4: Reinstall network drivers cleanly

With filters out of the way, replace the migrated drivers with known-good vendor packages.

1. Download Wi-Fi and Ethernet drivers for your exact model from the vendor's support site over the tethered connection.
1. In Device Manager, uninstall each network adapter, checking Delete the driver software for this device.
1. Install the downloaded packages and restart. Intel wireless cards can use Intel's [Driver and Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for the newest driver. If only the wireless side vanished, the focused [Wi-Fi disappeared guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) goes deeper on that single adapter.

### Fix 5: Reset the TCP/IP stack

When adapters are visible but cannot connect or obtain addresses, the shared stack configuration is the suspect.

1. In an elevated Command Prompt, run netsh int ip reset followed by netsh winsock reset.
1. Run ipconfig /flushdns for good measure.
1. Restart the laptop and test both Wi-Fi and Ethernet connections.

### Fix 6: Use Windows network reset as a final software step

Network reset reinstalls all network components to factory defaults. It is disruptive — saved networks are forgotten — but thorough.

1. Open Settings, then Network and internet, then Advanced network settings.
1. Choose Network reset and confirm, then restart when prompted.
1. Reconnect to your networks afterward. If adapters are still missing even with [hidden devices revealed](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-in-windows-11-24h2/) — the same Device Manager technique applies to network hardware — suspect BIOS settings or hardware, and check the vendor's diagnostics. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the automated network troubleshooters.

### Fix 7: Try an older driver version when the newest one fails

The newest driver is not always the most compatible with your exact hardware revision. When the current vendor driver fails to bring the adapters back, the previous release — or the driver Windows used before the update — may succeed. Version roulette is legitimate troubleshooting when device enumeration is at stake.

1. In Device Manager, open the adapter's Properties and use Roll Back Driver if the option is available.
1. Otherwise download the previous driver release from the vendor's support archive and install it over the current one.
1. Test each version with a restart between attempts, keeping notes on which versions enumerate the adapters.

## Closing

Total network loss after a Windows 11 update looks like a dead machine, but it is a shared-layer software failure far more often than broken hardware: filter drivers, a botched migration, or a corrupted stack. Tether a phone for downloads, strip out the filters, reinstall the vendor drivers cleanly, and reset the stack only if needed. Connectivity almost always returns before the last step — and the laptop that was an island is back on the network.
