---
title: "Network Adapter Missing in Device Manager? How to Get It Back"
slug: how-to-fix-network-adapter-missing-youtube
date: "2026-09-15"
categories: ["drivers"]
tags: ["network adapter missing", "device manager", "wifi adapter gone", "ethernet missing", "network fix"]
description: "Network adapter missing from Device Manager? Learn how to bring back disappeared WiFi and Ethernet adapters with driver repair, BIOS checks, and hardware tests."
thumbnail: "/images/thumbs/how-to-fix-network-adapter-missing-youtube.webp"
faqs:
- q: "What does it mean when the network adapter is missing from Device Manager?"
  a: "It means Windows is not detecting the networking hardware at all — not merely disabled or driverless, but absent from the hardware enumeration. The causes range from a hidden-but-present adapter (revealed by Show hidden devices) through corrupted drivers and BIOS-level disables, to a genuinely failed card. The recovery sequence in this guide distinguishes these cases step by step, from the five-second view toggle to hardware verification."
- q: "Can both WiFi and Ethernet adapters disappear at once?"
  a: "Yes, and when they do, the cause is usually system-wide rather than card-specific: a failed Windows update, a corrupted network stack, a BIOS reset that disabled onboard networking, or aggressive power settings. Simultaneous disappearance actually simplifies diagnosis — it points away from individual card failure and toward the shared causes covered in the middle fixes of this guide."
- q: "Will a network reset bring back a missing adapter?"
  a: "Often, yes. The network reset reinstalls all network adapters and rebuilds the network configuration from defaults, which recovers adapters hidden by corruption or bad configuration. It cannot fix BIOS-level disables or dead hardware, but as a software repair it is one of the strongest available. Remember it deletes saved WiFi passwords, so note them before resetting."
- q: "How do I know if my network card is physically dead?"
  a: "The card is likely dead when it is absent from Device Manager even with hidden devices shown, absent from BIOS device lists, invisible to a Linux live USB, and no driver will install to it. A USB network adapter working perfectly in the same laptop further confirms the internal card is the fault. Until all those tests fail, assume software — drivers and settings cause the large majority of missing-adapter cases."
---

Open Device Manager, expand Network adapters, and your WiFi card — or Ethernet controller, or both — is simply not there. No warning icon, no unknown device, no grayed-out entry. The hardware Windows used to see every day has vanished from the enumeration entirely, and with it, any way to get online from that adapter.

A missing adapter is different from a broken connection. Connection problems mean the hardware is present but misconfigured; a missing adapter means Windows cannot see the hardware at all. The causes form a ladder: hidden from view, driver-corrupted, BIOS-disabled, power-parked, or genuinely failed. Each rung has its own test, and you climb until the adapter reappears.

This guide covers both WiFi and Ethernet adapters, since the recovery sequence is the same. Work in order — most adapters return well before the hardware checks.

## Why this happens

- **Hidden by Device Manager's default view**: Deactivated adapters are invisible until "Show hidden devices" is enabled.
- **Corrupted driver hiding the device**: Windows conceals adapters whose drivers fail to load rather than showing them broken.
- **BIOS-level disable**: Firmware toggles for WLAN or onboard LAN remove the hardware from enumeration.
- **Deep power-state parking**: Aggressive link-state power management can drop the card off the bus.
- **Failed Windows update**: Interrupted updates leave network drivers half-installed and hidden.
- **Stale phantom entries conflicting**: Ghost adapters from old installs block the real hardware from enumerating.
- **Dead network card**: The least common cause — the chip itself has failed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Show hidden devices and scan for hardware changes

Device Manager hides deactivated devices by default, which makes a merely disabled adapter look like a missing one. This two-click check changes the picture instantly: grayed-out adapters reappear and can be re-enabled directly. Follow it with a hardware rescan, which forces Windows to re-enumerate the bus and pick up anything it missed.

1. Open Device Manager (Win + X).
2. Click View in the menu and select "Show hidden devices."
3. Expand "Network adapters" and look for grayed-out WiFi or Ethernet entries.
4. If found, right-click and choose "Enable device."
5. Then click Action, "Scan for hardware changes," and watch for the adapter to appear.

### Fix 2: Perform a full power cycle

Modern shutdowns are not full power-offs — fast startup keeps hardware in low-power states across reboots, and a network card wedged on the PCI bus stays wedged. Draining residual power forces every chip to cold-boot and re-enumerate. This genuinely revives adapters that vanish after sleep, hibernation, or power events.

1. Shut down fully: hold Shift while clicking Shut down.
2. Unplug the charger and remove the battery if it is removable.
3. Hold the power button for 30 seconds to drain residual charge.
4. Reconnect power and boot up.
5. Open Device Manager and check Network adapters for the returned device.

### Fix 3: Reinstall the network drivers from the manufacturer

When the adapter appears with a warning, as an [unknown device](/articles/how-to-fix-unknown-device-in-device-manager/), or not at all, the driver is corrupt or absent. Installing the manufacturer's WiFi and LAN drivers for your exact model gives Windows working drivers to bind. Download both packages before uninstalling anything, since you may have no working connection afterward.

1. On another device if needed, download the WiFi and Ethernet drivers from your maker's support page.
2. In Device Manager, uninstall any network adapter entries, ticking "Attempt to remove the driver."
3. Restart the laptop.
4. Install the downloaded drivers — [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) auto-detects the right ones for Intel networking.
5. Restart once more and verify the adapters appear without warnings.

### Fix 4: Reset the network configuration

Corrupted network configuration — damaged profiles, broken virtual adapters, poisoned stack state — can suppress adapter enumeration. The network reset reinstalls all network adapters and returns every setting to defaults, clearing configuration damage that driver reinstalls cannot reach. Note your WiFi passwords first; the reset deletes saved networks.

1. Go to Settings, Network and internet, Advanced network settings.
2. Click "Network reset," then "Reset now," and let the PC restart.
3. After reboot, open Device Manager and check for the adapters.
4. Reinstall the manufacturer drivers (Fix 3) after the reset for the cleanest state.
5. Reconnect to your networks, re-entering passwords.

### Fix 5: Check BIOS for network toggles

A firmware-level disable removes the adapter from enumeration entirely — no driver, no hidden device, nothing for Windows to find. BIOS updates sometimes reset these toggles, which explains adapters that vanish overnight. The check is definitive and takes two minutes: if the toggle is off, you have found the cause.

1. Restart and enter BIOS/UEFI setup (F2 or Del).
2. Look for wireless/WLAN and onboard LAN/Ethernet settings (under Advanced, Devices, or Security).
3. Set both to Enabled.
4. Save and exit, then boot into Windows.
5. Check Device Manager — the adapters should now enumerate.

### Fix 6: Clear stale phantom adapters

Ghost entries from old driver installs — grayed-out duplicates visible only with hidden devices shown — can block the real adapter from enumerating correctly. Removing every phantom network entry and letting Windows rediscover the hardware cleanly resolves these conflicts. Be careful to remove only grayed-out phantoms, not active devices.

1. In Device Manager, enable View, "Show hidden devices."
2. Under Network adapters, identify grayed-out duplicate or old entries.
3. Right-click each phantom and choose "Uninstall device."
4. Also remove stale VPN virtual adapters you no longer use.
5. Click Action, "Scan for hardware changes," and restart.

### Fix 7: Verify the hardware below the OS

If the adapter is absent everywhere — Device Manager with hidden devices, BIOS device lists — test beneath Windows. A Linux live USB enumerates hardware independently of every Windows driver and setting. No adapter there either means the card is dead or unseated. A USB WiFi or USB Ethernet adapter then serves as both diagnosis and permanent workaround. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document software-side network recovery that complements this hardware check.

1. Boot a Linux live USB and check for network interfaces (WiFi and Ethernet).
2. Absent in Linux too means hardware — reseat the M.2 WiFi card if comfortable (one screw, two antenna wires).
3. For Ethernet, a dead controller usually means board-level repair — weigh cost vs. a USB adapter.
4. Plug in a USB network adapter: working immediately confirms the internal card is the fault.
5. Keep using the USB adapter or replace the internal card — both are valid permanent fixes.

When only the WiFi side vanished from the interface but the adapter exists, the [WiFi disappeared guide](/articles/what-to-do-if-wifi-disappeared-from-laptop/) addresses that UI-level variant. For the full driver replacement procedure, see [reinstalling the WiFi driver on Windows 10](/articles/how-to-reinstall-wifi-driver-on-windows-10/).

## Closing

A missing network adapter is usually hiding, not dead — concealed by Device Manager's view settings, orphaned by a corrupt driver, parked by power management, or switched off in BIOS. Reveal hidden devices, power-cycle fully, reinstall the manufacturer's drivers, reset the network, and check BIOS before blaming hardware. The Linux live USB test is the final arbiter: invisible there too, and only then, is the card itself at fault.
