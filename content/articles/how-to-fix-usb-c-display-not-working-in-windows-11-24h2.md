---
title: "USB-C Display Not Working on Windows 11 24H2? Here's What to Do"
slug: how-to-fix-usb-c-display-not-working-in-windows-11-24h2
date: 2026-09-06
categories: ["drivers"]
tags: ["usb-c display", "windows 11 24h2", "displayport alt mode", "external monitor"]
description: "Your USB-C monitor stopped working after Windows 11 24H2? Diagnose whether it's the cable, port, or driver — then fix it with these step-by-step solutions."
thumbnail: "/images/thumbs/how-to-fix-usb-c-display-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why did my USB-C monitor stop working after 24H2?"
    a: "The 24H2 update can break USB-C display output in several ways: it may replace the graphics or USB4/Thunderbolt driver with an incompatible version, reset display detection, or change power delivery behavior so the monitor never wakes. The cable and port are usually fine — driver and detection issues cause the vast majority of post-update USB-C display failures."
  - q: "Does every USB-C port support video output?"
    a: "No, and this is the most common confusion. Only USB-C ports with DisplayPort Alt Mode, USB4, or Thunderbolt carry video. Many laptops have one video-capable port and one charging/data-only port. Check your laptop's manual or the port markings — a DisplayPort or lightning symbol means video is supported, while a plain USB or battery symbol often means it is not."
  - q: "Can the cable be the problem even if it charges the laptop?"
    a: "Yes. Charging only needs the power wires, while video needs the high-speed data lanes. A cheap or damaged cable can deliver power perfectly and carry zero video. For USB-C display output you need a cable rated for DisplayPort Alt Mode or Thunderbolt — if in doubt, test with the cable that came with the monitor."
  - q: "Should I update the graphics driver or the Thunderbolt driver?"
    a: "Both, in order. Update the graphics driver first (Intel, NVIDIA, or AMD for your GPU), then the Thunderbolt/USB4 driver from your laptop maker. USB-C video is a chain: the GPU renders, the Thunderbolt/USB4 controller packetizes, and the cable carries it. A break anywhere in the chain produces the same black screen."
---

You plug the USB-C cable into your laptop, the monitor stays black, and Windows shows nothing in display settings. It worked last week — then the Windows 11 24H2 update landed, and now the second screen is dead. The same cable charges the laptop fine, which makes the whole thing feel broken in a way that defies logic.

USB-C display output is a chain with several links: the port must support video, the cable must carry video lanes, the Thunderbolt/USB4 controller must negotiate the connection, and the graphics driver must drive the display. The 24H2 update tends to break the software links — graphics or Thunderbolt drivers — while the cable and port are innocent. Diagnose in the right order and most cases resolve without buying anything. If the monitor is detected but misbehaves, our guide on [second monitor flickering](/articles/how-to-fix-second-monitor-flickering-in-windows-11-24h2/) picks up where this one leaves off.

## Why this happens

- **24H2 replaced the graphics driver.** The update installed a display driver that breaks DisplayPort Alt Mode negotiation.
- **Thunderbolt/USB4 driver broken or outdated.** The controller driver cannot establish the video tunnel after the update.
- **Wrong USB-C port used.** The laptop has multiple USB-C ports but only one carries video.
- **Cable lacks video capability.** A charge-only or USB 2.0-spec cable cannot carry display signals.
- **Display detection stuck.** Windows cached the old display topology and never re-detects the monitor.
- **Monitor input not set to USB-C.** The monitor is waiting on HDMI or DisplayPort while the signal arrives on USB-C.
- **Power delivery negotiation failed.** The monitor never wakes because PD negotiation stalls after the update changed USB power behavior.
- **BIOS Thunderbolt security blocking.** Firmware security settings can block the display tunnel until authorized.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the port, cable, and monitor input

Check your laptop's manual or the port icons: use the USB-C port marked with a DisplayPort or Thunderbolt symbol, not the charge-only port. Swap to the cable that came with the monitor, or a cable explicitly rated for video/Thunderbolt. On the monitor itself, open the input menu and select **USB-C** manually — auto-input detection fails more often than people expect. Also try unplugging the monitor's power for 30 seconds to reset its input logic. If the monitor springs to life, the problem was never Windows — it was the physical chain.

### Fix 2: Force Windows to detect the display

Press **Windows + P** and choose **Extend** or **Duplicate** explicitly — 24H2 sometimes leaves the projection mode on "PC screen only" after an update. Then go to **Settings > System > Display**, scroll down, and click **Detect** next to the display diagram, then click **Detect** again under Multiple displays. If Windows finds the monitor but shows it greyed out, select it and choose **Extend desktop to this display**. Detection failures after updates are usually just stale display topology cache, and a forced detect clears it.

### Fix 3: Update the graphics driver from the GPU maker

USB-C video starts at the GPU, so fix it there first. Identify your graphics (Intel integrated, NVIDIA, or AMD) and install the latest driver: Intel users can use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA users should go to the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx), and AMD users to the [AMD driver support page](https://www.amd.com/en/support/download/drivers.html). Do a clean install if the installer offers it. Restart and retest the USB-C monitor. Graphics driver updates fix the Alt Mode negotiation handshake that 24H2 broke.

### Fix 4: Update the Thunderbolt/USB4 driver and firmware

Go to your laptop maker's official support site and download the latest **Thunderbolt driver** and any **Thunderbolt firmware** update for your exact model. Install the driver first, then the firmware (firmware updates require the charger connected and a restart). The Thunderbolt controller negotiates the video tunnel over USB-C, and 24H2-era driver/firmware mismatches are a leading cause of dead USB-C displays. Check the Thunderbolt Control Center app afterward to confirm the controller reports healthy.

### Fix 5: Roll back the recent driver update

If the monitor died immediately after 24H2 and the port/cable are verified, roll back. In **Device Manager**, check **Display adapters** (graphics driver) and **System devices** (Thunderbolt/USB4 controller) — open **Properties > Driver** on each and use **Roll Back Driver** where available. Restart and test after each rollback so you know which one mattered. Rollback is the fastest fix when you can pinpoint the failure to the update window, and it buys time while you wait for the vendor to release a properly fixed driver.

### Fix 6: Check BIOS Thunderbolt settings

Restart into the BIOS (F2, Del, or your brand's key) and look for **Thunderbolt**, **USB4**, or **Type-C** settings. Make sure Thunderbolt pre-boot and device support are enabled, and check the security level — **No Security** or **User Authorization** are the practical choices for docks and monitors; overly strict settings can block the display tunnel. Save and exit. While you are there, check for a **BIOS update** on the manufacturer's site — USB-C/Thunderbolt initialization fixes ship in firmware regularly, and 24H2-era BIOS updates specifically addressed display tunneling.

### Fix 7: Reset the USB and display stack

As a final software step, open **Device Manager**, expand **Universal Serial Bus controllers**, and uninstall each **USB Root Hub** and the Thunderbolt controller entries (do not check driver deletion — keep the drivers). Restart; Windows rebuilds the USB stack from scratch. Then open an elevated Command Prompt and run `netsh winsock reset` for good measure if you use a USB-C dock with Ethernet. If the monitor works on another computer with the same cable but never on this laptop through any driver version, the USB-C port's video lanes may have failed physically — try a dock or adapter on a different port, or have the port inspected.

## Closing

USB-C display failures after 24H2 are a chain problem — verify the physical chain first (right port, video-rated cable, correct monitor input), then rebuild the software chain (graphics driver, Thunderbolt driver and firmware). Work port-to-cable-to-driver and you will find the broken link quickly. If the monitor is detected but the handshake fails on a specific brand, our [ASUS external monitor guide](/articles/how-to-fix-external-monitor-not-detected-on-asus-laptop/) covers brand-specific detection quirks.
