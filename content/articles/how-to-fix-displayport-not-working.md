---
title: "How to Fix DisplayPort Not Working on a Windows Laptop"
slug: how-to-fix-displayport-not-working
date: 2026-09-01
categories: ["drivers"]
tags: ["displayport", "external monitor", "no signal", "usb-c", "graphics driver"]
description: "DisplayPort not working on your laptop? Fix no-signal issues with cable checks, driver repair, USB-C alt-mode troubleshooting, and monitor settings."
thumbnail: "/images/thumbs/how-to-fix-displayport-not-working.webp"
faqs:
  - q: "Why does my monitor say no signal on DisplayPort but works on HDMI?"
    a: "The DisplayPort link negotiation is failing while HDMI's simpler handshake succeeds. Common causes are a marginal cable, the monitor's DisplayPort version setting, or a graphics driver that mishandles the DP link training. Trying a certified cable and toggling the monitor's DP version setting resolves most of these cases."
  - q: "Does every USB-C port support DisplayPort video output?"
    a: "No. Only USB-C ports with DisplayPort Alt Mode — or Thunderbolt — carry video. Many laptops have USB-C ports that are data-only. Check your laptop's specifications for the DP Alt Mode or Thunderbolt marking; a data-only port will never output video no matter what adapter you use."
  - q: "Can a graphics driver update break DisplayPort output?"
    a: "Yes. DisplayPort link training is driver-managed, and buggy releases can fail negotiation with specific monitors. If DisplayPort broke right after a driver update, roll the graphics driver back to the previous version. This is a well-documented pattern with certain driver and monitor combinations."
  - q: "My DisplayPort worked, then stopped after the laptop slept. Why?"
    a: "The GPU failed to re-train the DisplayPort link on wake — a driver or firmware resume bug. Updating the graphics driver and the BIOS usually fixes it. As a workaround, unplugging and replugging the cable after wake forces a fresh link negotiation."
---

DisplayPort failures have a signature symptom: "No Signal" on a monitor that works fine over HDMI, with a cable that worked yesterday. DisplayPort uses an active link negotiation — the GPU and monitor handshake over lane speeds before any image appears — and that handshake is where things break. Cable quality, monitor settings, driver bugs, and USB-C alt-mode confusion are the usual suspects.

Troubleshooting DisplayPort means testing the physical link first, then the negotiation settings, then the driver. Skip the driver reinstall until you have ruled out the cable — technicians replace more "broken" DisplayPort setups with a $15 certified cable than with any software fix.

## Why this happens

- **Marginal or over-long cable:** DisplayPort is sensitive to cable quality; a cable that works at lower resolutions fails link training at higher ones.
- **Monitor's DisplayPort version mismatch:** A monitor set to DP 1.2 talking to a GPU expecting DP 1.4 can fail negotiation.
- **USB-C port without Alt Mode:** Data-only USB-C ports cannot output video regardless of adapter.
- **Graphics driver link-training bug:** Buggy drivers fail the handshake with specific monitor firmware.
- **Sleep/wake resume failure:** The GPU does not re-train the link after resume, leaving "no signal" until replug.
- **Wrong input selected:** Monitors with multiple inputs sometimes auto-switch away from DisplayPort.
- **Dock or adapter incompatibility:** Cheap USB-C to DP adapters and docks fail with certain GPU/monitor pairs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out the cable and the monitor input

Unplug the DisplayPort cable at both ends and reconnect firmly — DisplayPort connectors have a latch that must click. On the monitor's on-screen menu, manually select the DisplayPort input rather than relying on auto-detect. Then test with a different, preferably VESA-certified, DisplayPort cable under 2 meters; long or cheap cables are the number one cause of link-training failure. If possible, test the laptop on a different DisplayPort monitor. If a new cable fixes it, the old cable was marginal — keep the certified one and stop troubleshooting. This physical pass resolves the plurality of cases.

### Fix 2: Check the monitor's DisplayPort version setting

Open the monitor's OSD menu and look for a DisplayPort version or DP standard option — often under Input or System settings. If it is set to 1.2, try 1.4 (or vice versa). Some monitors ship at DP 1.1 for compatibility and never negotiate up; others at 1.4 confuse older laptop GPUs. Match the setting to what both devices support, then power-cycle the monitor. Also disable any monitor "deep sleep" or aggressive power-saving mode during testing, since those can drop the link entirely. These OSD settings are invisible to Windows, which is why driver fixes never touch them.

### Fix 3: Verify USB-C Alt Mode if you are using USB-C

If your DisplayPort connection runs through USB-C (directly or via an adapter/dock), confirm the port supports DisplayPort Alt Mode or Thunderbolt — check the laptop's specs or the port markings. A data-only USB-C port will never carry video. Try a different USB-C port on the laptop; manufacturers often enable Alt Mode on only one. If using a dock or adapter, test with a direct USB-C to DisplayPort cable instead to isolate the dock as the suspect. For broader external-display issues, our guide to [external monitors not detected](/articles/how-to-fix-external-monitor-not-detected-in-windows-11-24h2/) covers the Windows-side detection steps.

### Fix 4: Update or roll back the graphics driver

DisplayPort link training lives in the graphics driver. If the failure started after a driver update, roll back: Device Manager, Display adapters, Properties, Driver tab, Roll Back Driver. If the driver is old, update to your laptop manufacturer's latest graphics package from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — OEM graphics drivers carry validated DisplayPort behavior for the laptop's specific ports. For Intel graphics, Intel's Driver & Support Assistant is a reliable source. Reboot after any graphics driver change and test the DisplayPort connection cold, not from sleep.

### Fix 5: Adjust Windows display settings and detection

Press Win + P and cycle to "Extend" or "Duplicate" — sometimes Windows parks the external display in "PC screen only" after a driver change. Then go to Settings, System, Display, and click Detect under the display diagram; also try "Advanced display" to confirm Windows sees the monitor's capabilities. If Windows detects the monitor but shows no image, lower the refresh rate temporarily (Advanced display settings) — an over-ambitious refresh rate can fail link training on marginal cables. Set it back up once a stable connection is established. These settings cost nothing to try and catch the configuration-class failures.

### Fix 6: Update the BIOS and test sleep behavior

GPU firmware and link-training fixes ship in BIOS updates. Check your BIOS version against the manufacturer's latest and update on AC power if behind. Then test the specific failure pattern: connect DisplayPort, put the laptop to sleep, wake it, and observe. If the signal dies only across sleep, you have a resume bug — the BIOS update is the real fix, and unplug/replug after wake is the workaround until then. Also test with the laptop lid open vs. closed, since some firmware handles the DP link differently per lid state. Microsoft's Windows support hub documents display troubleshooting that complements these steps.

### Fix 7: Isolate dock, adapter, and monitor firmware

If a dock or adapter is in the chain, check the dock manufacturer's site for firmware updates — dock firmware bugs are a documented source of DisplayPort failures. Test the monitor on another computer's DisplayPort to confirm the monitor's port works. Try the laptop's HDMI port: if HDMI works but DisplayPort never does across cables and monitors, the laptop's DP output circuitry may be faulty — a hardware fault needing manufacturer service. For HDMI-specific failures, see our guide to [HDMI not working on laptops](/articles/how-to-fix-hdmi-not-working-on-laptop-in-windows-11-24h2/). Document your isolation results (cable swapped, monitor swapped, dock bypassed) before contacting support; a clean test log gets you past first-line scripts immediately.

## Closing

DisplayPort is a negotiation, and negotiations fail at the weakest participant — usually the cable, sometimes the monitor's settings, occasionally the driver. Test physical, test settings, test driver, in that order, and the "No Signal" message becomes a solved handshake instead of a mystery. Keep a certified cable in your bag; it is the cheapest DisplayPort insurance there is.
