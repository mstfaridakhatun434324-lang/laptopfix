---
title: "HDMI Not Working on Your Laptop? Fix It With This Guide"
slug: how-to-fix-hdmi-not-working-on-laptop-youtube
date: 2026-09-14
categories: ["drivers"]
tags: ["hdmi", "external display", "no signal", "display driver"]
description: "Laptop HDMI output dead? Fix no-signal HDMI from cable checks to graphics driver repairs, step by step."
thumbnail: "/images/thumbs/how-to-fix-hdmi-not-working-on-laptop-youtube.webp"
faqs:
  - q: "Why does my laptop not detect the HDMI display at all?"
    a: "Detection happens through the HDMI handshake — the display's EDID data must reach the laptop's graphics driver. A faulty cable, a display stuck on the wrong input, or a graphics driver that can't enumerate external outputs all break detection silently. The fastest triage: try a known-good cable and confirm the display's input is set to the right HDMI port before touching any software."
  - q: "My HDMI worked yesterday and stopped overnight. What happened?"
    a: "Overnight failures are usually a Windows update that replaced the graphics driver, or the display/display-driver state wedged during sleep. Restarting the graphics driver with Win + Ctrl + Shift + B often revives it instantly. If that fails, roll back or reinstall the graphics driver — the update is guilty until proven innocent."
  - q: "The TV shows 'no signal' but the laptop thinks a display is connected. Why?"
    a: "The laptop is outputting, but the signal isn't surviving the trip — or it's a format the display rejects. Causes include a marginal cable that passes detection but drops the video signal, an unsupported refresh rate or resolution, or HDCP handshake failure on protected content. Lower the output to 1080p/60Hz as a test; if the picture appears, it's a bandwidth or format issue."
  - q: "Do I need a special HDMI cable for 4K from my laptop?"
    a: "For 4K at 60Hz you need a High Speed (or better, Ultra High Speed) cable — old or cheap cables top out at lower bandwidths and produce no signal or flicker at 4K. The cable should be marked accordingly. Also confirm your laptop's HDMI port version supports 4K60; some laptops only do 4K at 30Hz, which looks broken on 60Hz-expecting displays."
---

You plug in the HDMI cable and… nothing. The TV says "no signal," the monitor stays asleep, or Windows insists no second display exists. HDMI failures are uniquely annoying because the chain has so many links — port, cable, display input, graphics driver, display settings, HDCP — and any single one fails silently while the rest look fine.

The good news: HDMI problems are almost always in the first three links, and they're fast to test. This guide works the chain in the order a technician would: the physical handshake first (cable, input, port), then the graphics driver restart trick that fixes a huge share of cases instantly, then display settings and driver repair, ending with the port-hardware verdict. Most people find their answer before the halfway mark.

## Why this happens

- **The display is on the wrong input.** The most common "failure" of all — the TV or monitor is set to HDMI 2 while the cable is in HDMI 1. Always verify first.
- **The cable is faulty or under-spec.** Marginal cables pass enough signal for detection but not for video, or lack the bandwidth for the selected resolution — producing no-signal or flicker.
- **The graphics driver crashed or wedged.** The driver that manages external outputs can hang while the internal display keeps working — the classic "worked until sleep" failure.
- **A Windows update replaced the graphics driver.** The new driver may mishandle external output enumeration or HDMI audio, breaking a previously working setup.
- **The output resolution/refresh rate is unsupported.** A setting the display can't handle produces a persistent no-signal that looks like a dead port.
- **HDCP handshake failed.** Protected content paths (streaming apps, Blu-ray) need an unbroken HDCP chain — adapters and docks in the path commonly break it.
- **The HDMI port hardware failed.** Least common — usually after physical stress on the port, like tripping over the cable while plugged in.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the display input and cable

The two-minute physical audit that resolves most HDMI "failures."

1. On the TV/monitor, open the **input/source menu** and select the exact HDMI port the cable is plugged into (HDMI 1 vs HDMI 2 matters). Cycle through inputs once if unsure.
2. Unplug the HDMI cable at **both ends** and reconnect firmly — a partially seated connector is a classic no-signal cause.
3. Try a **different, known-good HDMI cable** — ideally one currently working on another device. If the picture appears, the old cable was the entire problem.
4. If the display has multiple HDMI ports, try another one — individual ports fail, and this ten-second test rules that out.

### Fix 2: Restart the graphics driver (the instant fix)

The keyboard shortcut that revives wedged display output without a reboot.

1. Press **Win + Ctrl + Shift + B** — the screen will blink black for a second as Windows restarts the graphics driver.
2. Wait a few seconds and check the external display. This single shortcut resolves a large share of "stopped working after sleep" HDMI failures.
3. If it worked, the driver had wedged — consider updating the graphics driver (Fix 5) to reduce recurrence, since repeated wedging suggests a driver bug.
4. If nothing changed, the problem is deeper than a wedged driver — continue.

### Fix 3: Force detection and configure the display

When the hardware is fine but Windows isn't managing the output.

1. Press **Win + P** and select **Duplicate** or **Extend** — don't leave it on **PC screen only**, which is exactly what it sounds like.
2. Go to **Settings > System > Display** — click **Detect** (Windows 10) or check whether the second display appears (Windows 11 shows it automatically when detected).
3. If the display appears but shows no image: select it, lower the **Display resolution** to **1920 × 1080** and the refresh rate to **60 Hz** as a test — an unsupported mode is a common silent killer.
4. Try **Duplicate** mode specifically for testing — it forces output at a compatible mode and confirms the signal path works before you fine-tune Extend settings.

### Fix 4: Test the port, cable, and display independently

Isolate which link is broken before changing software.

1. Connect the laptop to a **different display** (another TV/monitor) with the same cable — works = your original display or its settings are the issue.
2. Connect a **different source** (streaming stick, another laptop) to the original display with the same cable — works = your laptop's output is the issue.
3. If your laptop has **USB-C with DisplayPort**, test external video through that port with an adapter — working USB-C video with dead HDMI points at the HDMI port or its specific driver path. Related port-level issues are covered in our [Thunderbolt troubleshooting guide](/articles/how-do-i-fix-thunderbolt-not-working-on-laptop/).
4. Inspect the laptop's HDMI port with a flashlight — bent pins or debris inside the port cause intermittent or total failure, especially after cable trips.

### Fix 5: Reinstall the graphics driver cleanly

The anchor software fix for persistent HDMI failures.

1. Identify your graphics: **Device Manager > Display adapters** (Intel, NVIDIA, AMD — laptops often have two; the integrated one usually drives HDMI).
2. Download the driver from the right source: **Intel** cards via the [Intel driver support page](https://www.intel.com/content/www/us/en/support/detect.html), **NVIDIA** from the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx), **AMD** from the [AMD driver download page](https://www.amd.com/en/support/download/drivers.html) — or your laptop maker's site for the validated OEM build.
3. For a truly clean install, use **DDU (Display Driver Uninstaller)** in Safe Mode to strip the old driver completely, then install the fresh package and reboot. If the driver was crashing rather than just misbehaving, our [display driver crash guide](/articles/how-to-fix-display-driver-stopped-responding-in-windows-11-24h2/) covers that specific failure mode.
4. Retest HDMI before reinstalling any graphics utilities or overlays — confirm the base driver works first.

### Fix 6: Check HDMI audio and HDCP path issues

When video works but something adjacent is broken — or protected content won't play.

1. For **no sound over HDMI**: right-click the speaker icon > **Sound settings** > set the **output device** to the HDMI/TV device explicitly — Windows doesn't always switch automatically.
2. For **streaming apps showing black** on the external display while the desktop mirrors fine: that's **HDCP** — remove adapters, docks, and capture devices from the path and connect laptop-to-display directly.
3. Try a shorter, higher-quality cable for HDCP issues — marginal cables fail the handshake even when they carry unprotected video.
4. As a test, play unprotected local video — if local files display but streaming doesn't, HDCP is confirmed as the layer, not your port or driver.

### Fix 7: Rule out a dead port

The final verdict when everything else checks out.

1. If HDMI fails with multiple known-good cables on multiple displays, while USB-C video works, the HDMI port or its motherboard connection is the likely fault.
2. Check for physical damage history — tripping over a plugged-in HDMI cable is the number-one port killer; the solder joints crack while the port looks fine externally.
3. Boot a **Linux live USB** and test HDMI there — working in Linux means a Windows driver issue (revisit Fix 5 aggressively); dead in Linux too means hardware.
4. Workarounds: a **USB-C to HDMI adapter** ($15–20) gives you external video through the working USB-C port — a fine permanent solution. In-warranty port failure = manufacturer repair.

## Closing

HDMI troubleshooting is chain troubleshooting: display input, cable, driver, settings — in that order. Check the physical handshake first (it takes two minutes and it's the cause most of the time), restart the graphics driver with the keyboard shortcut for the instant wins, and reinstall the graphics driver cleanly for the stubborn cases. The port itself is guilty last, not first.
