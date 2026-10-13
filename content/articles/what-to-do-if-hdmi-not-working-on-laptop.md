---
title: "HDMI Not Working on Your Laptop? What to Do First"
slug: what-to-do-if-hdmi-not-working-on-laptop
date: 2026-09-13
categories: ["drivers"]
tags: ["hdmi not working", "external monitor", "no signal", "display output", "second screen"]
description: "Laptop HDMI port gives no signal to your TV or monitor? Diagnose cable, port, driver, and display settings issues with this practical guide."
thumbnail: "/images/thumbs/what-to-do-if-hdmi-not-working-on-laptop.webp"
faqs:
  - q: "Why does my laptop not detect the HDMI monitor?"
    a: "The most common reasons are a faulty cable, the monitor set to the wrong input, an outdated or corrupted graphics driver, or Windows projecting to the wrong display mode. Less often, the HDMI port itself is damaged or the laptop's USB-C port you are using does not support video output. Testing with a known-good cable eliminates the most likely cause first."
  - q: "Do I need a special cable for laptop to TV HDMI?"
    a: "No — any standard High Speed HDMI cable works for 1080p and most 4K use. Cable quality only matters for 4K at 120Hz or 8K, where an Ultra High Speed cable is required. If your cable is very old or very long (over 5 meters), try a shorter modern cable before suspecting the laptop."
  - q: "Why does HDMI work on one monitor but not another?"
    a: "Different displays negotiate different resolutions and refresh rates through EDID handshaking. A monitor requesting a mode your laptop's GPU cannot output — or a TV with HDMI-CEC quirks — can fail the handshake. Lowering the output resolution in Windows Display settings often gets the stubborn display working."
  - q: "Can a driver update break HDMI output?"
    a: "Yes. Graphics driver updates occasionally break HDMI handshake or multi-display handling, especially on laptops with hybrid graphics (Intel + NVIDIA). If HDMI stopped working right after a driver update, rolling back the graphics driver is the fastest and most reliable fix."
---

HDMI failures follow a frustrating pattern: everything looks connected, the TV says "No Signal," and Windows acts like nothing is plugged in. The fix is almost always in one of four places — the cable, the display's input selection, Windows' projection settings, or the graphics driver. The key is testing them in an order that isolates the fault instead of changing everything at once.

Start with the physical layer and work upward. Each step below either fixes the problem or eliminates a suspect, so by the end you know exactly which component failed.

## Why this happens

- **Bad or loose HDMI cable:** The number one cause. Cables fail internally, and even slightly loose connectors break the digital handshake.
- **Monitor/TV on the wrong input:** The display is listening on HDMI 1 while the laptop is plugged into HDMI 2.
- **Windows projection mode wrong:** The display is set to "PC screen only" instead of Duplicate or Extend, so nothing is sent out.
- **Corrupted graphics driver:** The GPU driver handles HDMI handshaking; a broken install means no signal negotiation.
- **Hybrid graphics confusion:** On Intel + NVIDIA laptops, the wrong GPU may be assigned to external display duty.
- **Resolution/refresh rate mismatch:** The laptop outputs a mode the display cannot accept, and the handshake fails silently.
- **USB-C port without DisplayPort Alt Mode:** Not every USB-C port carries video. An adapter on a data-only port will never work.
- **Damaged HDMI port:** Bent pins or a cracked solder joint from cable strain, common on laptops used with heavy HDMI cables.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the cable and the display input

1. Unplug the HDMI cable at both ends and firmly reseat it — push until it is fully seated with no wiggle.
2. Use the TV/monitor remote to cycle through inputs and confirm you are on the exact HDMI port the cable uses.
3. Swap in a different HDMI cable, ideally a short known-good one. If the new cable works, the old one was the problem — replace it.
4. Test the same cable and display with another device (a console or streaming stick) to confirm the display's HDMI port itself works.

### Fix 2: Force Windows to detect the display

1. Press **Win + P** and choose **Duplicate** or **Extend** — never "PC screen only" when troubleshooting.
2. Go to **Settings → System → Display** and click **Detect** next to the display diagram.
3. If a second display appears grayed out, click it and choose **"Extend desktop to this display"** from the Multiple displays dropdown.
4. Scroll to **Advanced display** and try lowering the refresh rate to 60 Hz, which fixes handshake failures on picky TVs.

### Fix 3: Reinstall the graphics driver cleanly

1. Open **Device Manager → Display adapters**, right-click your GPU → **Uninstall device** (check "delete the driver software" if offered).
2. Restart and let Windows reinstall, or better, download the current driver from Intel, NVIDIA, or AMD directly.
3. For NVIDIA laptops, use the [official NVIDIA driver page](https://www.nvidia.com/Download/index.aspx) and choose **Custom → Clean installation**.
4. Retest HDMI. Driver corruption is the most common software cause, and a clean install resolves it — the same principle behind fixing [screen flickering](/articles/how-to-fix-screen-flickering-on-laptop-in-windows-11-24h2/).

### Fix 4: Check which GPU drives the HDMI port

1. On hybrid-graphics laptops, the HDMI port is usually wired to either the integrated or the discrete GPU — check your manual.
2. Open **NVIDIA Control Panel → Manage 3D settings → Preferred graphics processor** and try **High-performance NVIDIA processor**.
3. Alternatively, in **Settings → System → Display → Graphics**, set your apps to the high-performance GPU.
4. Some laptops need the discrete GPU active for HDMI to work at all; forcing it on eliminates the switching ambiguity.

### Fix 5: Lower the output resolution and disable HDR

1. In **Settings → System → Display**, select the external display and drop the resolution to **1920×1080**.
2. Turn off **HDR** for the external display if it is on — HDR handshakes fail on many older TVs and adapters.
3. If the display appears now, raise the resolution step by step to find the highest stable mode.
4. This also helps when the second monitor [flickers rather than staying black](/articles/how-to-fix-second-monitor-flickering-after-windows-11-update/).

### Fix 6: Verify USB-C video capability if using an adapter

1. Check your laptop's specifications for **DisplayPort Alt Mode** or **Thunderbolt** on the USB-C port you are using.
2. If the port is data-only, no adapter will ever produce video — use the native HDMI port instead.
3. For adapters, prefer active adapters from reputable brands; passive cheap adapters are a common failure point.
4. Update the Thunderbolt/USB4 driver from your laptop maker's support page if the port should support video but doesn't.

### Fix 7: Test the port hardware and check for damage

1. Shine a light into the HDMI port and look for bent pins or debris.
2. Try the laptop on a different display with a different cable — if no display ever works, the port is likely damaged.
3. Wiggle the cable gently while watching for flickers of signal; intermittent contact confirms a physical port problem.
4. Port repair means motherboard-level soldering — check warranty status first, and see the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) for display troubleshooting documentation before paying for a repair.

### Fix 8: Tame HDMI-CEC and TV-side settings

1. On the TV, turn **off HDMI-CEC** (called Anynet+, Bravia Sync, or Simplink depending on brand) as a test — CEC negotiation failures can block the video handshake entirely.
2. Try different HDMI ports on the TV — many TVs only support full bandwidth on specific ports (often labeled HDMI 1 or ARC/eARC).
3. In the TV's picture settings, look for **HDMI mode** or **input signal** options and set them to **Standard** rather than Enhanced/4K modes while troubleshooting.
4. If the laptop works on a monitor but never on this TV, try booting the laptop with the TV already on and set to the right input — some TVs only handshake during their own power-on sequence.

## Closing

HDMI diagnosis is a process of elimination: cable, input, projection mode, driver, GPU assignment. Work it in that order and you will find the fault quickly — most of the time it is the cable or the driver, and both are cheap to fix.
