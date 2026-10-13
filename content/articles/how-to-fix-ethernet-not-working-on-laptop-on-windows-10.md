---
title: "How to Fix Ethernet Not Working on a Laptop in Windows 10"
slug: how-to-fix-ethernet-not-working-on-laptop-on-windows-10
date: 2026-10-03
categories: ["drivers"]
tags: ["ethernet", "windows 10", "wired network", "lan driver"]
description: "Wired Ethernet dead on your Windows 10 laptop? Fix adapter, driver, cable, and network stack issues to restore your wired connection."
thumbnail: "/images/thumbs/how-to-fix-ethernet-not-working-on-laptop-on-windows-10.webp"
faqs:
  - q: "Why does my laptop say Ethernet is unplugged when the cable is connected?"
    a: "That message means the network adapter sees no electrical link, which points to the cable, the port, the switch or router end, or a dead adapter. Try a different cable and a different router port first. If the link lights stay dark across cables and ports, the laptop's Ethernet controller or its driver is the problem."
  - q: "Can a Windows 10 update break the Ethernet adapter?"
    a: "Yes. Updates frequently replace the Ethernet driver with a generic version that misbehaves on Realtek, Intel, or Killer controllers — causing no-link, Code 10 errors, or connections that drop under load. Reinstalling the manufacturer's driver is the standard fix and takes only a few minutes."
  - q: "Do USB-C Ethernet adapters need drivers on Windows 10?"
    a: "Most modern USB Ethernet adapters work with Windows 10's built-in drivers, but Realtek-based dongles often perform better with the manufacturer's driver installed. If a dongle is flaky, install its specific driver rather than relying on the generic one Windows assigns."
  - q: "Ethernet works but is very slow — is that a driver problem?"
    a: "It can be. Forced duplex or speed mismatches, outdated drivers, and damaged cables that still link at 100 Mbps instead of 1 Gbps all cause slowness. Check the adapter's Speed & Duplex setting and the link speed in Status — a healthy wired connection should negotiate 1.0 Gbps on a gigabit network."
---

Ethernet that stops working on a Windows 10 laptop presents differently from WiFi trouble: there is usually a cable, port LEDs, and a very specific error message to work with. "Network cable unplugged" when the cable is plainly plugged in, a yellow triangle on the adapter, or a connection that identifies the network but gives no internet — each points at a different layer, and reading the symptom correctly cuts the fix time dramatically.

Work from the physical layer up. Ethernet is beautifully diagnosable: link lights tell you about the cable and port before you ever open Device Manager, and the adapter's reported link speed tells you about driver and duplex problems. Software fixes come after the hardware baseline is confirmed.
Windows 10's networking stack is mature, which cuts both ways: it's stable, but years of VPN clients, security suites, and feature updates can leave it in a tangled state where the adapter links fine and no traffic flows. The other Windows 10 wrinkle is driver age — the OS happily runs Ethernet drivers from 2016 that predate your router's firmware by a decade. The steps below handle both the cruft and the age.

## Why this happens

- **Damaged or wrong-category cable:** A broken pair inside the cable kills the link entirely; an old Cat5 cable may link but cap speed at 100 Mbps.
- **Dead router/switch port:** The far end of the connection fails as often as the laptop end, and it is the easiest thing to test.
- **Corrupted Ethernet driver:** Driver corruption or a bad Windows Update replacement produces Code 10 errors or phantom "unplugged" states.
- **Power management disabling the adapter:** Windows turning off the NIC to save power leaves it unable to re-establish link after sleep.
- **Speed/duplex mismatch:** A manually forced speed setting that disagrees with the switch causes no-link or severe slowness.
- **TCP/IP stack corruption:** Malware, VPN clients, or failed updates can corrupt the stack so the adapter links fine but passes no traffic.
- **Disabled adapter:** The Ethernet adapter is simply disabled in Network Connections — common after troubleshooting WiFi issues.
- **Failing Ethernet controller:** Rare, but onboard NICs do die, usually after power surges through the cable.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check link lights, cable, and port

1. Look at the Ethernet port LEDs with the cable plugged in — solid or blinking lights mean electrical link; dark LEDs mean no link at all.
2. Swap the cable for a known-good Cat5e or Cat6 cable, even if the current one "looks fine" — internal breaks are invisible.
3. Plug into a different port on the router or switch, and power-cycle the router.
4. If link lights come alive on a different port, the router port was dead; if they stay dark everywhere, the laptop side is the suspect.
5. While testing, look at the LED colors and blink patterns — many adapters use green for gigabit link and amber for 100 Mbps, so an amber light with a good cable immediately tells you the negotiation is degraded, pointing at the cable or switch port rather than the laptop.

### Fix 2: Confirm the adapter is enabled

1. Press **Win + R**, type `ncpa.cpl`, and open Network Connections.
2. If the Ethernet adapter shows **Disabled**, right-click → **Enable**.
3. If it shows **Network cable unplugged** despite a good cable and port, continue to driver fixes.
4. Note the adapter name (Realtek, Intel, Killer) — you will need it to fetch the right driver.

### Fix 3: Reinstall the Ethernet driver cleanly

1. Download the LAN driver for your model from the laptop maker's support site using WiFi or another computer.
2. In **Device Manager → Network adapters**, right-click the Ethernet controller → **Uninstall device**, ticking driver removal if offered.
3. Restart and install the manufacturer's driver package — avoid letting Windows Update pick a generic one first.
4. Verify in Device Manager that the adapter shows no warning icon. The same clean-reinstall discipline fixes [vanishing wireless adapters](/articles/wifi-adapter-not-showing-up-troubleshooting/).
5. For the deeper step-by-step variant of this repair, our [ordered Ethernet checklist](/articles/ethernet-not-working-on-laptop-troubleshooting/) covers the same ground as a strict sequence you can follow without skipping steps.

### Fix 4: Disable power management for the NIC

1. In Device Manager, right-click the Ethernet adapter → **Properties → Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. On the **Advanced** tab, disable **Energy Efficient Ethernet** and **Green Ethernet** if present — these power-saving modes cause link flaps on some switches.
4. Restart and test sleep-wake cycles to confirm the link re-establishes.

### Fix 5: Set speed and duplex correctly

1. In the adapter's **Properties → Advanced** tab, find **Speed & Duplex**.
2. Set it to **Auto Negotiation** first — manual settings cause more problems than they solve on modern networks.
3. Check **Status** on the connection: it should read **1.0 Gbps** on a gigabit network. If it reads 100 Mbps with a good cable, the cable or a switch port is limiting you.
4. Only force **1.0 Gbps Full Duplex** manually if auto-negotiation demonstrably fails with specific enterprise switches.
5. Document the working combination — adapter driver version, speed setting, and cable category — in a note. Ethernet issues recur across Windows updates, and knowing the exact working setup turns the next repair into a five-minute restore instead of a fresh investigation.

### Fix 6: Reset the TCP/IP stack

1. Open **Command Prompt as administrator**.
2. Run `netsh winsock reset` and then `netsh int ip reset`, pressing Enter after each.
3. Run `ipconfig /release` followed by `ipconfig /renew` and `ipconfig /flushdns`.
4. Restart the laptop. This clears corrupted stack state that lets the adapter link while passing zero traffic — the classic "connected, no internet" on wired.
5. If problems persist after the reset, check [Microsoft's Windows networking guidance](https://support.microsoft.com/en-us/windows) for any known-issue patches affecting wired adapters on your Windows 10 build.

### Fix 7: Test with a USB Ethernet adapter

1. Borrow or buy a USB 3.0 Ethernet dongle and connect through it.
2. If the dongle works perfectly, the onboard NIC is faulty or its driver is unfixable — the dongle is a fine permanent replacement.
3. If the dongle fails identically, the problem is in Windows networking itself — consider a network reset (**Settings → Network & Internet → Advanced network settings → Network reset**).
4. After a network reset, reinstall VPN clients and re-enter WiFi passwords, since the reset clears all network profiles.

## Closing

Ethernet failures on Windows 10 laptops reward methodical layer-by-layer diagnosis: link lights and cables first, then the adapter state, then drivers, then the TCP/IP stack. Most cases end at Fix 3 or Fix 4 — a clean manufacturer driver with power management disabled. Keep a spare known-good cable in your bag; it is the fastest diagnostic tool in wired networking.
