---
title: "How to Fix Ethernet Not Working on a Laptop"
slug: how-to-fix-ethernet-not-working-on-laptop-youtube
date: 2026-09-30
categories: ["drivers"]
tags: ["ethernet not working", "wired network", "network adapter", "no internet"]
description: "Fix Ethernet not working on a laptop: diagnose the wired connection from cable to driver and restore stable wired networking."
thumbnail: "/images/thumbs/how-to-fix-ethernet-not-working-on-laptop-youtube.webp"
faqs:
  - q: "Why does my laptop say 'Unidentified network' on Ethernet?"
    a: "Unidentified network means the Ethernet link is up but the laptop cannot get a valid IP configuration — usually a DHCP failure, a bad cable causing packet loss, or a router issue. Releasing and renewing the IP, trying a different cable and router port, and resetting the network stack resolve most cases."
  - q: "My laptop has no Ethernet port. How do I troubleshoot wired networking?"
    a: "You are using a USB-C or USB-A Ethernet adapter, which adds the adapter and its driver as suspects. Test the adapter on another computer, try different USB ports, reinstall the adapter's driver from the vendor, and confirm the USB port itself works with other devices. The adapter is the most common failure point."
  - q: "Ethernet worked yesterday but not today. What changed?"
    a: "Overnight Windows updates are the prime suspect — they can replace the Ethernet driver or reset network settings. Check Device Manager for driver changes, roll back the network adapter driver if the timing matches, and verify the cable was not disturbed. Router firmware auto-updates overnight are the other common overnight change."
  - q: "Should I disable Wi-Fi when using Ethernet?"
    a: "It is good practice while troubleshooting, and often beneficial permanently. With both active, Windows may route traffic over Wi-Fi anyway due to interface metrics. Disabling Wi-Fi when docked ensures traffic uses the faster, more stable wired connection and removes a variable from diagnosis."
---

Wired Ethernet is supposed to be the reliable option — plug in, get gigabit, forget about it. So when Ethernet stops working on a laptop, it is uniquely annoying: the thing that never breaks just broke. The failure can sit anywhere in a longer chain than people expect: the cable, the wall jack or router port, the laptop's port (or USB adapter), the driver, or Windows' network configuration.

This guide works the chain from the physical layer up. Each test isolates one link, so instead of randomly reinstalling drivers you will know exactly which component failed — and the fix for that component specifically.

Wired networking fails in layers, and naming them keeps the troubleshooting honest. At the bottom is the physical layer: the cable, the port LEDs, and the link negotiation where your laptop and the switch agree on speed. Above that sits the driver, which presents the adapter to Windows. Then comes IP configuration — usually DHCP, where the router assigns your address — and finally the Windows network stack that carries actual traffic. 'Unidentified network' means the bottom two layers work but DHCP failed; no link lights means the problem is purely physical; an adapter missing from Device Manager means the driver layer never came up. Match your symptom to its layer before you start, and most of the steps below will either confirm or eliminate a suspect within minutes.

## Why this happens

- **Bad cable:** Ethernet cables fail from kinks, chewed insulation, or broken clips that cause partial seating.
- **Dead router/switch port:** Individual ports on routers and switches die while the rest work fine.
- **Driver regression:** Windows updates replace the Ethernet driver with a broken version.
- **USB adapter failure:** USB Ethernet dongles are the weakest link in modern thin-and-light setups.
- **DHCP failure:** The laptop cannot obtain an IP address, producing "Unidentified network."
- **Corrupted network stack:** Winsock/TCP-IP corruption breaks connectivity despite a healthy link.
- **Power management:** The adapter gets suspended and fails to resume.
- **Speed/duplex mismatch:** Forced settings that disagree with the switch cause link failure or extreme slowness.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical link

1. Look at the Ethernet port LEDs — link and activity lights should be on/blinking. No lights means no physical link at all.
2. Reseat the cable at both ends; listen/feel for the click of the retaining clip.
3. Try a different cable — Cat5e or Cat6, as short as practical for the test.
4. Try a different port on the router or switch. If the link lights come alive on a new port, the old port was dead.

### Fix 2: Isolate the adapter (USB Ethernet users)

1. Plug the USB Ethernet adapter into a different USB port, preferably directly on the laptop.
2. Test the adapter on another computer with the same cable — working elsewhere clears the adapter.
3. Reinstall the adapter's driver from the vendor's site (Realtek USB Ethernet drivers are the most common).
4. If the adapter is unrecognized, treat it as a USB problem first — see [USB device troubleshooting](/articles/what-to-do-if-usb-device-not-recognized/).

### Fix 3: Verify the adapter in Device Manager

1. Open **Device Manager → Network adapters** and confirm the Ethernet adapter is present and enabled (no down-arrow).
2. Check **Properties → General** for error codes — Code 10 here gets the same treatment as [Wi-Fi Code 10 errors](/articles/wifi-driver-code-10-error-troubleshooting/).
3. On the **Power Management** tab, uncheck **"Allow the computer to turn off this device to save power"**.
4. On the **Advanced** tab, set **Speed & Duplex** to **Auto Negotiation** unless your network specifically requires a forced value.

### Fix 4: Release, renew, and reset the IP stack

1. Open an elevated Command Prompt and run: **ipconfig /release** then **ipconfig /renew**.
2. If that fails, run **ipconfig /flushdns**, **netsh winsock reset**, and **netsh int ip reset**, then restart.
3. Check **ipconfig /all** — a 169.254.x.x address means DHCP failed; a proper 192.168.x.x or 10.x.x.x means the network layer is healthy.
4. For a GUI approach, **Settings → Network & internet → Advanced network settings → Network reset** does the full stack rebuild.

### Fix 5: Reinstall the Ethernet driver

1. In Device Manager, right-click the Ethernet adapter → **Uninstall device** (check driver removal if offered), then restart.
2. Download the latest driver from your laptop maker's support site — for Intel Ethernet, [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) works well.
3. If the problem started after an update, try **Roll Back Driver** first — it is faster.
4. Verify link speed in **Settings → Network & internet → Ethernet** after reinstalling; it should show 1.0 Gbps on a healthy gigabit chain.

### Fix 6: Test the network path

1. Connect the same cable to a different device (another laptop, a game console) — working there clears the cable and router port.
2. Bypass wall jacks and patch panels by plugging directly into the router.
3. Try a different router port even if the current one shows link lights — ports can link yet pass no traffic.
4. If everything local checks out, restart the router/modem — DHCP server hangs are real and a reboot is the fix.

### Fix 7: Check for software interference

1. Temporarily disable third-party firewall, VPN, and security software — then test.
2. Check for proxy settings: **Settings → Network & internet → Proxy** should usually be off on a home network.
3. Disable Wi-Fi while testing Ethernet to remove routing ambiguity.
4. Boot into **Safe Mode with Networking** — working there means a third-party program is blocking traffic.

### Fix 8: BIOS, firmware, and hardware verdict

1. Check the laptop maker's site for **BIOS** updates — Ethernet controller fixes ship in BIOS updates.
2. Update the router's firmware; auto-updates overnight are a classic "worked yesterday" cause.
3. Run the manufacturer's network diagnostics.
4. If the built-in Ethernet port never links with known-good cables on known-good networks, the port or controller has failed — a USB Ethernet adapter is the practical workaround, and Microsoft documents wired troubleshooting at [Microsoft support](https://support.microsoft.com/en-us/windows).

## Closing

Ethernet failures are physical-layer problems more often than Wi-Fi failures are: cables, ports, and adapters. Check the link lights, swap the cable, change the router port, then repair the driver and IP stack — working from the wire inward finds the break fast, and most of the time the break is the cheapest component in the chain.
