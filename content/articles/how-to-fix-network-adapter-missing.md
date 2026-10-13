---
title: "How to Fix Network Adapter Missing from Device Manager"
slug: how-to-fix-network-adapter-missing
date: 2026-09-05
categories: ["drivers"]
tags: ["network adapter", "missing", "wifi adapter", "ethernet", "device manager"]
description: "Network adapter missing from Device Manager? Recover vanished Wi-Fi and Ethernet adapters with detection scans, driver repair, BIOS checks, and resets."
thumbnail: "/images/thumbs/how-to-fix-network-adapter-missing.webp"
faqs:
  - q: "Why is my network adapter completely missing from Device Manager?"
    a: "Windows cannot enumerate the adapter: its driver failed to load, the device is disabled, a Windows update broke the driver, or the adapter is switched off in BIOS. Hardware failure is possible but less common. The missing entry means Windows sees no working device to list, not necessarily that the hardware is gone."
  - q: "My Wi-Fi adapter is missing but Ethernet works. What does that tell me?"
    a: "The networking stack is healthy and the fault is specific to the wireless hardware or its driver. Focus on the Wi-Fi adapter: check for a physical wireless switch, reinstall the Wi-Fi driver, and verify the BIOS wireless setting. Ethernet working is actually good news — it gives you a connection to download the Wi-Fi driver."
  - q: "Can I fix a missing network adapter without internet access?"
    a: "Partially. Device Manager rescans, BIOS checks, and driver reinstalls from locally stored files all work offline. But downloading the manufacturer's driver needs a connection — use a phone USB tether, another computer plus USB stick, or Ethernet if available. Plan the download step before you start."
  - q: "Will a network reset bring back a missing adapter?"
    a: "Often yes. Network reset reinstalls all network adapters and returns networking components to defaults, which clears the corrupted state hiding the adapter. It is one of the most reliable fixes when the adapter is missing due to driver or configuration corruption rather than hardware failure."
---

A missing network adapter is worse than a broken one — there is nothing to configure, no error to read, just an empty Network adapters section and no internet. But "missing from Device Manager" does not mean "missing from the laptop." It means Windows failed to enumerate the device: the driver did not load, the device is disabled, firmware hides it, or the hardware truly died. Those are very different problems with very different fixes.

This guide recovers the adapter layer by layer, and it plans for the cruel constraint of the situation: you may have no internet while fixing the thing that provides internet.

## Why this happens

- **Corrupted network driver:** The driver fails to load at boot, so Windows lists no adapter.
- **Device disabled:** Adapters disabled in Device Manager vanish from the normal view.
- **Windows update driver swap:** Updates replace working network drivers with incompatible builds.
- **BIOS wireless/LAN disable:** Firmware can switch off the Wi-Fi card or Ethernet independently.
- **Physical wireless switch off:** A hardware switch can remove the Wi-Fi adapter from enumeration.
- **Power management deep-disable:** Aggressive power states can park the adapter where Windows cannot wake it.
- **Hardware failure:** A dead Wi-Fi card or failed Ethernet PHY removes the device electrically.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices and scan for hardware changes

Open Device Manager (Win + X), click View, enable Show hidden devices, and expand Network adapters. A greyed-out adapter means disabled — right-click, Enable device, restart. Then click Action, "Scan for hardware changes" to force re-enumeration of the bus. Check under Other devices for unknown entries that may be the unclaimed adapter. If the scan rediscovers the adapter, install its driver immediately (Fix 3) before the next reboot loses it again. This two-minute pass recovers every "disabled or skipped" case without touching drivers. For technique details, see our guide to [hidden devices in Device Manager](/articles/how-to-enable-hidden-devices-in-device-manager-on-windows-11/). If the adapter appears in some views but Wi-Fi specifically is gone, see [fixing a Wi-Fi adapter not showing up](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/).

### Fix 2: Check physical switches and BIOS settings

Inspect the laptop for a physical wireless switch or Fn-key toggle and cycle it — a switch in the off position removes the Wi-Fi adapter from enumeration on many models. Then restart into BIOS/UEFI setup and verify wireless LAN, WLAN, and onboard LAN/Ethernet are enabled; some BIOS updates reset these. Save and exit. If the adapter was firmware-disabled, no Windows procedure could ever find it. While in the BIOS, check for a hardware inventory page listing the network devices — presence there confirms the hardware is electrically alive and the fault is software.

### Fix 3: Reinstall the network driver from the manufacturer

You need the driver file, which needs a connection — plan this: USB-tether your phone, use Ethernet if that adapter works, or download on another machine and transfer by USB stick. Get the Wi-Fi and Ethernet drivers for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). In Device Manager, uninstall any ghosted or unknown network entries with driver deletion, then run the manufacturer's installers — chipset first if you suspect deeper issues, then network — and reboot. The OEM network driver is the one validated against your card's firmware; install it even if Windows' automatic driver seemed to work.

### Fix 4: Perform a network reset

Go to Settings, Network & internet, Advanced network settings, Network reset, and click Reset now. Confirm and let the laptop restart. This reinstalls every network adapter, clears corrupted bindings and configurations, and returns the whole networking subsystem to defaults. It is the heavy fix for adapters missing due to configuration corruption rather than driver files. You will lose saved Wi-Fi networks, so note passwords first — or rather, note them before you start this whole guide, since you may be offline already. After the reset, reinstall the manufacturer's drivers from Fix 3 rather than relying on the generic ones the reset installs.

### Fix 5: Repair the driver store and check services

Open Terminal as administrator and run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`, then restart — a corrupted driver store blocks adapter enumeration across driver versions. Then open `services.msc` and confirm WLAN AutoConfig (for Wi-Fi), Wired AutoConfig (for Ethernet), Network Connections, and Network Location Awareness are running with sensible startup types. A missing adapter with broken underlying services stays missing even with perfect drivers. This step addresses the OS-foundation faults that survive driver reinstalls. Microsoft's Windows support hub documents these repair commands officially.

### Fix 6: Test power states and the Ethernet fallback

Disable Fast Startup (Control Panel, Power Options, "Choose what the power buttons do") and do a full Shift+Shutdown, then cold boot — this clears hibernation-preserved device states that hide adapters. In Device Manager, on any network adapter's Power Management tab, uncheck "Allow the computer to turn off this device to save power." If Ethernet works but Wi-Fi stays missing, use the Ethernet connection to run Windows Update's optional driver updates and the manufacturer's update utility — sometimes the fix arrives as an update once you have any path online. Document which adapter is missing and which works; the pattern guides the hardware verdict.

### Fix 7: Run diagnostics and judge the hardware

Run the manufacturer's bootable diagnostics network tests. If the Wi-Fi card fails or is absent from diagnostics, reseat or replace it — most laptop Wi-Fi cards are small replaceable modules, though antenna leads need care. If Ethernet fails, the PHY is board-level and the practical fix is a USB Ethernet adapter. When both are missing and diagnostics find no network hardware at all, suspect a deeper board or chipset fault and get a professional quote. A USB Wi-Fi or USB Ethernet adapter is a cheap, immediate workaround that restores connectivity while you decide on repair — and it doubles as proof the OS stack is healthy.

## Closing

A missing network adapter is an enumeration failure, and enumeration fails for concrete reasons: disabled, unswitched, undrivered, unconfigured, or dead. Reveal, switch, reinstall, reset, repair, and test — in that order — and the adapter either reappears or earns a hardware verdict with evidence. Plan your driver download path before you start, because the one thing worse than no network adapter is no way to fetch its driver.
