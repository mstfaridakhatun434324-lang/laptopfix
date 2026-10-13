---
title: "Fix a Dead Ethernet Port on a Laptop in Windows 11 24H2"
slug: how-to-fix-ethernet-not-working-on-laptop-in-windows-11-24h2
date: 2026-10-07
categories: ["drivers"]
tags: ["ethernet not working", "windows 11 24h2", "network adapter", "realtek ethernet", "wired connection"]
description: "Fix laptop Ethernet that stopped working after Windows 11 24H2: adapter driver repair, cable/port diagnosis, and network stack resets."
thumbnail: "/images/thumbs/how-to-fix-ethernet-not-working-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why did my Ethernet stop working after the 24H2 update?"
    a: "The update frequently replaces the Ethernet adapter driver with an incompatible version or leaves the adapter disabled after migration. The physical port hardware is almost always fine. Reinstalling the laptop vendor's network driver for your exact model, then disabling NIC power management, restores the wired connection in most cases."
  - q: "How do I know if the problem is the cable or the laptop?"
    a: "Check the port LEDs with the cable plugged in — link and activity lights prove the physical layer works. Then test the same cable and router port with another device. If the other device connects, your cable and router are fine and the fault is in the laptop's adapter driver, settings, or port hardware."
  - q: "What does 'network cable unplugged' mean when the cable is plugged in?"
    a: "Windows is not detecting a link signal on the port despite the cable being seated. The causes range from a bad cable or dead switch port to a disabled adapter or a driver that cannot initialize the NIC. Always verify the physical path first — different cable, different port — then move to driver repair."
  - q: "Should I use the vendor driver or Windows Update for Ethernet?"
    a: "Use the vendor driver from Dell, HP, or Lenovo support for your exact model. Realtek and Intel Ethernet chips have laptop-specific power management and firmware quirks that generic Windows drivers mishandle, particularly after feature updates. The vendor package is validated against your machine's specific NIC revision."
---

Ethernet dying after the Windows 11 24H2 update is frustrating precisely because wired connections are supposed to be the reliable fallback. The symptom varies: the adapter vanishes from Network Connections, the status shows "network cable unplugged" with a cable firmly seated, or the link connects but passes no traffic. Before assuming the port is dead, run the physical checks — then accept that 24H2's network driver migration is the likely culprit.

The diagnostic logic is simple: physical layer first (cable, port, LEDs), then driver layer, then Windows network stack. Most cases resolve at the driver layer. Keep this order and you will not waste an hour resetting TCP/IP for a broken cable.

## Why this happens

- **Ethernet driver replaced with incompatible version:** 24H2 installs a generic or wrong-version driver for the Realtek/Intel NIC that cannot initialize the hardware.
- **Adapter disabled during migration:** The update can leave the Ethernet adapter disabled in Network Connections or Device Manager.
- **Power management killing the NIC:** "Allow the computer to turn off this device" lets Windows sleep the adapter and fail to wake it on cable insert.
- **Corrupted network stack:** Winsock and TCP/IP catalog corruption from the update breaks connectivity even with a working driver and link.
- **Speed/duplex forced to wrong value:** A hardcoded speed setting that worked with the old driver fails to negotiate with the new one.
- **USB-C/Thunderbolt dock driver issues:** Many modern laptops get Ethernet through a dock; the dock's Ethernet driver (often a separate USB network driver) breaks in 24H2.
- **Bad cable or switch port (physical):** Updates get blamed for coincidental hardware failures — always verify the physical path.
- **BIOS network stack setting changes:** Some firmware updates reset the onboard LAN or deep-sleep settings.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the physical layer

1. Check the Ethernet port LEDs with the cable plugged in — link/activity lights mean the NIC sees the switch.
2. Try a different cable and a different router/switch port.
3. Test the same cable and port with another device (or your phone via USB tethering to confirm the router side works).
4. If no LEDs light on any cable/port combination, the port or NIC may be dead — but continue with driver checks first, since a driver that cannot initialize the NIC also produces dark LEDs.

### Fix 2: Confirm the adapter is enabled

1. Go to **Settings → Network & internet → Advanced network settings → More network adapter options**.
2. If the Ethernet adapter is grayed, right-click → **Enable**.
3. In **Device Manager → Network adapters**, confirm the Ethernet controller has no warning icon and is not disabled.
4. If the adapter is missing entirely from Device Manager, enable **View → Show hidden devices** — a grayed entry points to an enumeration problem, and the [hidden-device cleanup guide](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/) covers the next steps.

### Fix 3: Reinstall the vendor Ethernet driver

1. Identify your NIC in Device Manager (e.g., Realtek PCIe GbE, Intel Ethernet Controller).
2. Download the LAN driver for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support.
3. In Device Manager, right-click the adapter → **Uninstall device**, checking **Attempt to remove the driver**.
4. Reboot and install the downloaded vendor driver. If you connect through a dock, also update the dock's Ethernet/USB network driver from the dock vendor.

### Fix 4: Disable power management on the adapter

1. In Device Manager, right-click the Ethernet adapter → **Properties → Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. On the **Advanced** tab, disable **Energy Efficient Ethernet** and **Green Ethernet** if present — these power-saving modes cause link negotiation failures on some switches.
4. Set **Speed & Duplex** to **Auto Negotiation** unless your network admin requires a fixed value.

### Fix 5: Reset the Windows network stack

1. Open an elevated Command Prompt.
2. Run, in order: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
3. Reboot.
4. Alternatively use **Settings → Network & internet → Advanced network settings → Network reset** — it reinstalls all adapters and resets everything to defaults. Reinstall the vendor driver afterward if the reset pulls a generic one.

### Fix 6: Check for IP and DHCP problems

1. Run `ipconfig /all` and check whether the Ethernet adapter has a valid IPv4 address or a 169.254.x.x APIPA address.
2. APIPA means DHCP failed — try `ipconfig /release` then `ipconfig /renew`, and reboot the router.
3. Test with a static IP in your LAN's range to isolate DHCP vs. driver issues.
4. If Wi-Fi gets DHCP fine but Ethernet does not, the problem is specific to the Ethernet path — driver or hardware, not the router. Related wireless-side checks live in the [Wi-Fi troubleshooting guides](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/).

### Fix 7: Check BIOS settings and rule out hardware failure

1. Enter BIOS and confirm **Onboard LAN / LAN Controller** is **Enabled**.
2. Disable **Deep Sleep** power options for the NIC if present — they can prevent link establishment.
3. Boot a Linux live USB and test Ethernet there. Working Ethernet in Linux proves the port hardware is fine and the fault is Windows drivers.
4. If Linux also shows no link with known-good cables, the NIC or port is physically faulty — USB Ethernet adapters are an inexpensive workaround.

## Closing

Ethernet failures after 24H2 follow a predictable pattern: the physical port is fine, but the driver migration broke the software path. Verify the cable and LEDs, confirm the adapter is enabled, reinstall the vendor's driver, disable NIC power management, and reset the network stack — in that order. A Linux live-USB test gives you the definitive hardware verdict if everything else fails. Wired networking is simple at its core; the update just tangled the driver, and untangling it is mechanical.
