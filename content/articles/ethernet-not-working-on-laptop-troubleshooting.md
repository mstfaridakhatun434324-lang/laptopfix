---
title: "Ethernet Not Working on Laptop: Troubleshooting Guide"
slug: ethernet-not-working-on-laptop-troubleshooting
date: 2026-10-04
categories: ["drivers"]
tags: ["ethernet not working", "wired network", "lan driver", "no ethernet", "realtek lan"]
description: "Ethernet not working on your laptop? Fix the wired network adapter with driver reinstalls, cable tests, and BIOS checks step by step."
thumbnail: "/images/thumbs/ethernet-not-working-on-laptop-troubleshooting.webp"
faqs:
  - q: "Why is my Ethernet port not working but Wi-Fi is fine?"
    a: "When Wi-Fi works but Ethernet doesn't, the problem is isolated to the wired path: the Ethernet adapter driver, the cable, the port, or the router's LAN side. Check Device Manager for the Ethernet adapter's status first, then test with a different cable. A driver reinstall fixes most cases where the adapter shows a warning."
  - q: "My laptop has no Ethernet port — what are my options?"
    a: "Use a USB-to-Ethernet adapter, which works immediately with built-in Windows drivers on most models, or a USB-C docking station with Ethernet. These adapters are inexpensive and reliable. If the adapter isn't recognized, try a different USB port and check Device Manager for unknown USB devices."
  - q: "Why does my Ethernet say 'Unidentified network'?"
    a: "Unidentified network means the adapter has link (the cable is electrically fine) but can't get a valid IP configuration from the router. Release and renew the IP with ipconfig commands, reset the network stack, and check whether the router's DHCP server is working. A static IP conflict with another device causes the same message."
  - q: "Can a Windows update break Ethernet?"
    a: "Yes. Updates sometimes replace the manufacturer's Ethernet driver with a generic version that misbehaves, or corrupt the driver installation. If wired networking died right after an update, reinstall the LAN driver from your laptop maker's support page and check that the adapter isn't disabled in Device Manager."
---

Wired Ethernet failing while Wi-Fi hums along is a particularly annoying split — you bought the cable and the dock for reliability, and now the "reliable" connection is the dead one. The good news: Ethernet problems are highly diagnosable because the chain is short and every link is testable: adapter driver, cable, port, and router LAN side.

Work the isolation in order: confirm the adapter exists in software, verify the physical link (LEDs don't lie), then fix the driver and network configuration layers.

## Why this happens

- **Ethernet adapter driver failed:** Updates corrupt or replace the LAN driver; the adapter shows a warning or vanishes from Device Manager.
- **Adapter disabled:** The Ethernet adapter gets disabled in Device Manager or Network Connections and forgotten.
- **Bad cable:** Damaged, kinked, or incorrect cables (a phone cord in an Ethernet jack happens) break the link silently.
- **Router/switch port issue:** A dead LAN port on the router or a switch that needs rebooting looks exactly like a laptop problem.
- **IP configuration failure:** DHCP failures leave the adapter with a 169.254 APIPA address and "Unidentified network."
- **Power management disabling the adapter:** The OS powers down the Ethernet controller to save battery, and it doesn't wake properly.
- **BIOS LAN toggle:** Some laptops have a BIOS LAN/WLAN switching feature that disables wired when wireless is active.
- **USB adapter driver issues:** For USB-to-Ethernet dongles, the USB network driver or the dongle itself can fail.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical link — LEDs and cable

1. Plug in the Ethernet cable and look at the port's LEDs: solid/blinking **link light** means electrical connection; **activity light** flickers with traffic.
2. No lights at all = no electrical link. Try a different cable first — cables fail more often than ports.
3. Try a different port on the router or switch, and power-cycle the router (unplug 30 seconds).
4. Inspect the laptop's port for bent pins or debris; inspect the cable's connector for a broken locking tab (a loose connector causes intermittent link).
5. If another device works on the same cable and router port, the laptop side is the problem — continue below. LED behavior is the fastest isolation in wired networking.

### Fix 2: Verify the adapter in Device Manager

1. Press **Win + X** → **Device Manager** → expand **Network adapters**.
2. Look for your Ethernet controller (Realtek PCIe GbE, Intel Ethernet, Killer E-series, or a USB adapter entry).
3. A yellow warning: note the error code, then proceed to the driver reinstall (Fix 3).
4. A down arrow: right-click → **Enable device**.
5. Missing entirely: enable **View → Show hidden devices** — a greyed-out ghost means the driver is present but the hardware isn't enumerating, which points to BIOS or hardware. The [missing adapter diagnostics](/articles/how-to-fix-wifi-adapter-not-showing-up-youtube/) apply the same logic to wired adapters.

### Fix 3: Reinstall the Ethernet driver from the manufacturer

1. Download the **LAN/Ethernet driver** for your exact model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
2. In Device Manager, right-click the Ethernet adapter → **Uninstall device**, checking **Attempt to remove the driver for this device**.
3. Install the downloaded driver and restart.
4. Verify the adapter appears cleanly in Device Manager with no warnings.
5. For USB-to-Ethernet adapters, get the driver from the adapter maker's site (Realtek, ASIX) if Windows doesn't handle it automatically — and test the dongle on another computer to rule out dongle failure.

### Fix 4: Fix the IP configuration

1. Open an elevated Command Prompt and run: `ipconfig /release`, then `ipconfig /renew`.
2. Check the output: a **169.254.x.x** address means DHCP failed — the router isn't assigning addresses.
3. Run `netsh winsock reset` and `netsh int ip reset`, then restart.
4. As a test, assign a static IP in the router's subnet (e.g., 192.168.1.50 with the router as gateway) — if static works but DHCP doesn't, the router's DHCP server is the problem.
5. If the adapter shows **Unidentified network** with a valid-looking IP, check for IP conflicts: another device may be squatting on the same address.

### Fix 5: Disable power management on the adapter

1. In Device Manager, open the Ethernet adapter's **Properties → Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. In the **Advanced** tab, look for **Energy Efficient Ethernet** or **Green Ethernet** and disable it as a test — these features cause link instability on some switches.
4. Set **Speed & Duplex** to **Auto Negotiation** (forced speeds cause mismatches with modern switches).
5. Restart and test. Power-gated Ethernet controllers that die after sleep are a classic laptop issue.

### Fix 6: Check BIOS LAN settings

1. Enter BIOS/UEFI setup and look for **LAN**, **Onboard LAN**, or **LAN/WLAN Switching** options.
2. Ensure the onboard LAN is **enabled**. If **LAN/WLAN Switching** is on, the BIOS disables wired when Wi-Fi connects — turn it off if you want both active.
3. Save and exit, then check Device Manager for the adapter.
4. If the adapter was missing from Device Manager entirely, a BIOS toggle is a strong suspect — especially after a BIOS update.
5. Some docks need **MAC address passthrough** or dock LAN settings configured in BIOS; check your dock's documentation.

### Fix 7: Reset the network stack completely

1. **Settings → Network & internet → Advanced network settings → Network reset** → **Reset now**.
2. The laptop restarts with all network adapters reinstalled and all configurations cleared.
3. Reconnect and retest Ethernet before reinstalling VPNs or custom network software.
4. This clears corrupted adapter bindings and filter drivers that survive ordinary driver reinstalls.
5. If you use a VPN, reinstall it after the reset and test Ethernet both with and without the VPN active — VPN filter drivers are a known Ethernet breaker.

### Fix 8: Update the chipset driver and test hardware

1. Install the latest **chipset driver** from your laptop maker — the Ethernet controller hangs off chipset-managed PCIe lanes, and chipset issues can present as LAN failure. The [chipset install guide](/articles/best-way-to-install-chipset-drivers/) covers the process.
2. Test with a Linux live USB: working Ethernet in Linux = Windows driver/config problem; dead in Linux too = hardware.
3. For built-in ports that fail electrically (no LEDs with known-good cable and router), the port or its PHY chip has failed — motherboard-level repair.
4. For USB adapters that fail everywhere, replace the dongle — they're cheap and they do wear out.
5. Document the working driver version once fixed; Ethernet drivers are among the most frequently regressed by Windows Update, so knowing your good version saves future headaches.

## Closing

Ethernet diagnosis is refreshingly physical: LEDs and cable swaps isolate the problem in minutes, and the remaining cases are driver or IP configuration issues with well-worn fixes. The pattern to remember is Wi-Fi-works-but-Ethernet-doesn't, which always means the fault is in the wired-specific chain — adapter, cable, port, or router LAN side — never in your internet connection itself.
