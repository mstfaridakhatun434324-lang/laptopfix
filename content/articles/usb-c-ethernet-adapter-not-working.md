---
title: "How to Fix USB-C Ethernet Adapter Not Working on AI Laptops"
slug: usb-c-ethernet-adapter-not-working
date: 2026-10-24
categories: ["ai-pc"]
tags: ["usb-c", "ethernet", "adapter", "networking", "windows 11", "troubleshooting"]
description: "USB-C Ethernet adapter not detected or stuck offline on your AI laptop? Follow these step-by-step fixes for drivers, ports, cables, DHCP, and settings."
thumbnail: "/images/thumbs/usb-c-ethernet-adapter-not-working.webp"
faqs:
  - q: "Why is my USB-C Ethernet adapter not detected at all?"
    a: >
      The most common reasons are a charge-only USB-C port or cable, a missing driver for the adapter's chipset, or the adapter being plugged into a port that does not support data. Try a different USB-C port and install the chipset driver.
  - q: "The adapter is detected but shows 'no internet'. What now?"
    a: >
      Detection without connectivity is usually DHCP, cable, or network-policy related. Check the Ethernet cable, confirm DHCP is enabled, and test whether the network requires 802.1X authentication or a captive portal.
  - q: "My adapter only gets 100 Mbps instead of gigabit. Why?"
    a: >
      A 100 Mbps ceiling means the link negotiated down — usually a damaged cable, a bad port on the switch, or the adapter's speed/duplex forced wrong. Swap the cable first; it is the cause most of the time.
  - q: "Do USB-C Ethernet adapters need drivers on Windows 11?"
    a: >
      Many work plug-and-play with inbox drivers (especially Realtek chipsets), but some ASIX and exotic chipsets need a manufacturer driver. If Device Manager shows an unknown device, download the driver from the adapter maker's site.
---

You plug a USB-C Ethernet adapter into your AI laptop for a stable wired connection — and Windows shows nothing, or shows the adapter with "no internet," or connects at a miserable 100 Mbps. The adapter worked on your old laptop, so the new machine gets the blame.

USB-C Ethernet adapters are simple devices with a surprising number of failure points: the USB-C port must carry data (not all do), the cable between adapter and laptop matters on some designs, the adapter's chipset needs a driver, and then the entire Ethernet stack (cable, DHCP, network policy) must cooperate. AI laptops add one wrinkle — port capabilities vary, and some USB-C ports are wired for charging first. The same port-capability check fixes [USB-C dock dual-monitor issues](/articles/usb-c-dock-dual-monitor-ai-laptop/) and [HDMI 2.1 problems](/articles/hdmi-2-1-not-working-ai-laptop/) — verify the port before anything else. Model-specific port behavior is documented for machines like the [Dell Inspiron 14 Plus AI](/articles/dell-inspiron-14-plus-ai-problems/); similar verify-first discipline helps with [Edge crashing on ARM64](/articles/edge-arm64-crashing-windows-11/) and reading [SleepStudy battery reports](/articles/sleepstudy-report-arm-laptop-battery/).

This guide gives you six fixes in order: verify port and adapter basics, install the chipset driver, fix detection issues, fix no-internet issues, fix speed negotiation, and handle power and sleep behavior.

## Why this happens

- **USB-C port without data:** Some laptop USB-C ports are charge-only. An Ethernet adapter on a charge-only port is invisible to Windows.
- **Missing chipset driver:** Realtek adapters usually work inbox; ASIX AX88179/AX88772 and other chipsets often need a manufacturer driver, especially on fresh installs.
- **Faulty or wrong cable (adapter to laptop):** On adapters with a detachable USB-C cable, a charge-only cable passes power but no data — the adapter never enumerates.
- **Bad Ethernet cable or switch port:** Detection works but the link fails — damaged Ethernet cables and dead switch ports produce "no internet" or 100 Mbps ceilings.
- **DHCP or network policy:** Corporate networks may require 802.1X authentication or MAC registration; without it you get "no internet" despite a perfect local link.
- **Power management suspending the adapter:** Windows may power down the USB adapter to save battery, causing disconnects and failure to reconnect after sleep.
- **Speed/duplex forced wrong:** A manually forced speed in the adapter's Advanced settings that mismatches the switch produces a dead or degraded link.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the port, cable, and adapter basics

Rule out the physical layer completely before touching software.

1. Plug the adapter into a **different USB-C port** on the laptop — try every port; note which ones detect the adapter.
2. If the adapter has a detachable USB-C cable, swap it for a known-good **data-capable** USB-C cable (charge-only cables are the silent killer here).
3. Check the adapter's LED: link/activity lights that stay dark suggest no USB enumeration or no Ethernet link — note which.
4. Plug the adapter into a **different computer** if available — if it works there, the laptop's port or driver is the issue.
5. Confirm the laptop's USB-C port supports data by plugging in another USB data device (a flash drive) into the same port.

### Fix 2: Install the adapter's chipset driver

Device Manager shows an unknown device or a warning on the adapter — it needs its driver.

1. Open **Device Manager** and look under **Network adapters** and **Other devices** for the adapter or an unknown USB device.
2. Note the chipset if visible (Realtek RTL8153/8156, ASIX AX88179A are common) — right-click > **Properties > Details > Hardware Ids** to identify it.
3. Download the driver from the **adapter maker's** support page (or the chipset vendor: Realtek, ASIX) — match your Windows 11 build.
4. Install the driver and restart, then recheck Device Manager — the adapter should now appear cleanly under Network adapters.
5. If Windows Update offers a newer driver under **Optional updates**, install it after the manufacturer driver as a second pass.

### Fix 3: Fix "detected but no internet"

Windows sees the adapter but there is no connectivity — work the Ethernet link layer.

1. Check the Ethernet cable: swap it for a known-good Cat5e or better cable, and try a different switch/router port.
2. Look at the adapter's link LED — solid link light means the physical connection is up; no light means cable or switch-port failure.
3. Open **Settings > Network & internet > Ethernet** and confirm the adapter shows **Connected** — then check whether it has a valid IP (not 169.254.x.x).
4. A 169.254 address means DHCP failed: in an elevated Terminal run `ipconfig /release` then `ipconfig /renew` for the adapter.
5. If DHCP keeps failing, ask your network admin whether the network needs **802.1X authentication** or MAC registration — common on corporate and campus networks.

### Fix 4: Fix slow speeds (100 Mbps ceiling)

Connected but slow — the link negotiated down. Find out why.

1. Open **Settings > Network & internet > Ethernet**, click the adapter, and check the **Link speed** — 100/100 means negotiated Fast Ethernet.
2. Swap the Ethernet cable first — damaged cables are the #1 cause of gigabit falling back to 100 Mbps.
3. Try a different switch/router port — a bad switch port negotiates down identically.
4. In Device Manager, open the adapter's **Advanced** tab and check **Speed & Duplex** — set it to **Auto Negotiation**, not a forced 100 Mbps.
5. Test with a USB-A Ethernet adapter or a different USB-C adapter if available — a failing adapter chipset degrades exactly this way.

### Fix 5: Fix power management and sleep behavior

The adapter works until the laptop sleeps, then never reconnects — or randomly disconnects on battery.

1. In Device Manager, open the adapter's **Power Management** tab and **uncheck** "Allow the computer to turn off this device to save power."
2. Also check the USB root hub the adapter hangs off: **Device Manager > Universal Serial Bus controllers > USB Root Hub > Power Management** — uncheck the same box.
3. Set **Settings > System > Power & battery > Power mode** to **Best performance** while testing plugged in.
4. Disable **USB selective suspend**: **Control Panel > Power Options > Change plan settings > Change advanced power settings > USB settings**.
5. Test a full sleep/wake cycle — if the adapter reconnects cleanly now, power management was the culprit.

### Fix 6: Reset the network stack and reconfigure

Everything checks out but it still will not work — clear corrupted network state.

1. In an elevated Terminal, run `netsh winsock reset` and `netsh int ip reset`, then restart.
2. Go to **Settings > Network & internet > Advanced network settings > Network reset** — this reinstalls all network adapters including the USB one.
3. After reboot, reinstall the chipset driver from Fix 2 (the reset can revert to a generic driver).
4. Reconnect the adapter and re-run `ipconfig /renew` if DHCP is in play.
5. If it still fails identically, test the adapter on another machine one final time — a consistent failure across machines means the adapter itself is dead, and no software fix will revive it.

## Closing

USB-C Ethernet adapters fail at the physical and driver layers far more than the network layer: data-capable port, good USB-C cable, correct chipset driver — then cable, DHCP, and network policy. Work the list in order and the failure reveals itself quickly, usually by Fix 3. The honest end state: a dead adapter is a dead adapter — the cross-machine test in Fix 6 is the definitive verdict, and these adapters are cheap enough that replacement beats prolonged surgery. For driver downloads, the adapter maker's page first, then the chipset vendor, then Windows Update optional updates.
