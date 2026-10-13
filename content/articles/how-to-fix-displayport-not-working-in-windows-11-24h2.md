---
title: "DisplayPort Not Working in Windows 11 24H2? 7 Fixes That Work"
slug: how-to-fix-displayport-not-working-in-windows-11-24h2
date: 2026-09-07
categories: ["drivers"]
tags: ["displayport", "monitor", "windows 11", "24h2", "display"]
description: "DisplayPort monitor not working after the Windows 11 24H2 update? 7 fixes — cable and adapter checks, graphics driver repairs, and display settings."
thumbnail: "/images/thumbs/how-to-fix-displayport-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why did DisplayPort stop working after the 24H2 update?"
    a: "The 24H2 update replaces graphics drivers with versions that sometimes mishandle DisplayPort link training — the handshake where the GPU and monitor negotiate resolution and refresh rate. It can also reset display settings or break the driver components specific to DisplayPort output. HDMI often keeps working because it uses a simpler, separate code path in the driver."
  - q: "Is DisplayPort better than HDMI for my laptop monitor?"
    a: "For most uses, yes. DisplayPort supports higher refresh rates at high resolutions (like 4K at 144Hz), handles multi-monitor daisy-chaining, and carries adaptive sync more reliably. HDMI 2.1 has closed much of the gap, but DisplayPort remains the preferred connection for high-refresh gaming and professional multi-display setups."
  - q: "Why does my DisplayPort monitor work in BIOS but go black in Windows?"
    a: "That split behavior is the classic signature of a Windows driver problem. The BIOS uses basic VGA-compatible output that doesn't need the full driver; Windows loads the real graphics driver, which then fails DisplayPort link training. Reinstalling the manufacturer's graphics driver almost always fixes this exact symptom."
  - q: "Can a DisplayPort cable go bad without visible damage?"
    a: "Yes — internal wire fractures and connector wear cause failures invisible from outside. DisplayPort is particularly sensitive because its high-bandwidth link training fails entirely rather than degrading gracefully. If wiggling the connector causes flicker or the monitor drops out intermittently, replace the cable before suspecting anything else."
---

Your DisplayPort monitor worked yesterday. Then 24H2 installed, and now it's black — or Windows doesn't see it at all, while HDMI (if you tried it) works fine. DisplayPort failures after the Windows 11 24H2 update are common enough to be a known pattern: the update's graphics driver mishandles DisplayPort's link-training handshake, the negotiation where your GPU and monitor agree on resolution, refresh rate, and signal parameters.

DisplayPort is fussier than HDMI by design — higher bandwidth, more complex negotiation — which is why updates break it first. The seven fixes below cover the handshake chain: cable, monitor, driver, and Windows settings. If your connection is Thunderbolt-based rather than native DisplayPort, our [Thunderbolt fix guide](/articles/how-to-fix-thunderbolt-not-working-on-laptop-in-windows-11-24h2/) addresses that variant.

## Why this happens

- **24H2's graphics driver fails DisplayPort link training** — the GPU-monitor handshake breaks while HDMI keeps working.
- **The DisplayPort cable is marginal or damaged** — link training is the first thing a weak cable fails.
- **The monitor is on the wrong input** — it's listening on HDMI while DisplayPort carries the signal.
- **An adapter in the chain doesn't convert properly** — passive USB-C to DisplayPort adapters are frequent culprits.
- **Display settings reset to single-display mode** — 24H2 sometimes drops the external display configuration.
- **The monitor's DisplayPort version setting conflicts** — DP 1.2 vs 1.4 negotiation mismatches with the GPU.
- **Multi-stream (daisy-chain) settings interfere** — MST enabled on a single monitor confuses link training.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Power-cycle the DisplayPort handshake

DisplayPort link training is stateful — once it fails, both ends can get stuck refusing to retry properly. Break the stalemate: unplug the DisplayPort cable from both ends, power the monitor fully off (unplug from the wall, not just the button), shut the laptop down completely, wait 60 seconds, then power up the monitor first and reconnect. This forces a fresh handshake from a clean state on both sides.

1. Unplug the DisplayPort cable from both the laptop and the monitor.
2. Unplug the monitor from wall power and shut the laptop down fully.
3. Wait 60 seconds, then plug in and power on the monitor first.
4. Boot the laptop, wait for Windows to load, then connect the DisplayPort cable.

### Fix 2: Verify the monitor input and DisplayPort version

Open the monitor's on-screen menu and confirm it's set to the DisplayPort input your cable uses — then look for a DisplayPort version setting (often under System or Input settings). If it's set to DP 1.4, try forcing DP 1.2, and vice versa. Version mismatches during link training cause exactly this black-screen behavior, and manually pinning the version sidesteps the negotiation failure.

1. Open the monitor's menu and select the correct **DisplayPort** input.
2. Find the **DisplayPort version** setting (DP 1.1 / 1.2 / 1.4) in the menu.
3. Try each version setting, waiting 10 seconds after each change.
4. Disable **DisplayPort MST / daisy-chain** mode if you're using a single monitor.

### Fix 3: Swap the cable and remove adapters

DisplayPort cables fail invisibly, and link training is unforgiving of marginal ones. Replace the cable with a certified DisplayPort cable (look for VESA certification), keep it under 2 meters for high resolutions, and connect directly — no adapters, no docks — for the test. If you're using USB-C to DisplayPort, try a different adapter: the active conversion chips in cheap adapters are a leading failure point. Our [second-monitor detection guide](/articles/how-to-fix-laptop-not-detecting-second-monitor-in-windows-11-24h2/) covers adapter pitfalls in detail.

1. Replace the cable with a VESA-certified DisplayPort cable.
2. Connect directly to the laptop — bypass docks and adapters for this test.
3. If you must use USB-C to DisplayPort, try a different, reputable adapter.
4. Test detection with **Windows + P** after each change.

### Fix 4: Force detection and check display mode

Windows may have the monitor connected at the hardware level but stuck in "PC screen only" mode after the 24H2 update. Press **Windows + P** and try **Extend** explicitly. Then open **Settings > System > Display** and click **Detect**. If the monitor appears here, arrange it and set it as needed — the hardware was fine all along, just ignored by a settings reset.

1. Press **Windows + P** and select **Extend** (not Duplicate).
2. Go to **Settings > System > Display** and click **Detect**.
3. If the monitor appears, drag it to the correct position in the layout.
4. Set **Multiple displays** to **Extend these displays** and apply.

### Fix 5: Clean-reinstall the graphics driver

This is the highest-probability fix for post-24H2 DisplayPort failures. The update's generic graphics driver is what broke link training; your manufacturer's driver restores it. Download the graphics driver for your exact model from Dell, HP, Lenovo, or ASUS support. Use Display Driver Uninstaller (DDU) in Safe Mode for a truly clean wipe if a regular reinstall doesn't work — corrupted driver remnants survive normal uninstalls.

1. Download the graphics driver for your exact model from the manufacturer's site.
2. For stubborn cases, run **Display Driver Uninstaller (DDU)** in Safe Mode first.
3. Install the manufacturer's driver, choosing **Clean install** if offered.
4. Restart with the DisplayPort monitor connected and check detection.

### Fix 6: Lower resolution and refresh rate to establish the link

If link training fails at 4K/144Hz, it may succeed at 1080p/60Hz — proving the chain works but lacks stability at high bandwidth. Once the monitor is detected at low settings, step the resolution and refresh rate up gradually to find the stable ceiling. If the ceiling is lower than the monitor's spec, the cable is the bottleneck: upgrade it and try again.

1. With the monitor connected, open **Settings > System > Display > Advanced display**.
2. Drop to **1920x1080 at 60Hz** and check whether the monitor is detected.
3. If detected, raise resolution and refresh rate one step at a time.
4. Note the highest stable combination — a low ceiling means replace the cable.

### Fix 7: Update the monitor firmware and check GPU output

Some monitors have firmware updates that fix DisplayPort handshake bugs — check the monitor manufacturer's support page for your model. Also verify which GPU drives the DisplayPort output: on laptops with hybrid graphics, the port may be wired to the NVIDIA/AMD discrete GPU, whose driver needs updating separately from Intel's. Update both graphics drivers, and check the discrete GPU control panel for display output settings. Microsoft's display troubleshooting background is at [Windows support](https://support.microsoft.com/en-us/windows).

1. Check the monitor manufacturer's site for firmware updates for your model.
2. In Device Manager, verify both Intel and discrete GPU drivers are current.
3. Update the discrete GPU driver from NVIDIA/AMD or the laptop manufacturer.
4. Test the DisplayPort connection after both drivers are updated.

## Closing

DisplayPort failing after 24H2 is a handshake problem — the update's driver can't complete the link-training negotiation that DisplayPort demands. The power-cycle and cable checks clear the physical side; the clean graphics driver reinstall fixes the software side in most cases. DisplayPort's fussiness is the price of its performance — but once the handshake succeeds, it's the best connection your monitor has.
