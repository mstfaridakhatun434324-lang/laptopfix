---
title: "HDMI Not Working on Your Laptop? Complete Troubleshooting Guide"
slug: hdmi-not-working-on-laptop-troubleshooting
date: "2026-09-07"
categories: ["drivers"]
tags: ["hdmi no signal", "external display", "hdmi port", "laptop to tv", "second monitor"]
description: "Laptop HDMI port not working with your TV or monitor? Follow this complete troubleshooting guide — input checks, projection modes, drivers, and cable fixes."
thumbnail: "/images/thumbs/hdmi-not-working-on-laptop-troubleshooting.webp"
faqs:
- q: "Why does my TV say no signal when I connect my laptop via HDMI?"
  a: "The most common reasons are the TV being set to the wrong HDMI input, the laptop's projection mode set to PC screen only, or a faulty cable. HDMI handshake failures between the laptop's GPU and the TV also cause no-signal, especially with older TVs. Checking the input source first, then the projection mode with Win + P, resolves the issue in most cases without touching drivers."
- q: "Do I need to change a setting for HDMI to work on a laptop?"
  a: "Usually just the projection mode: press Win + P and choose Duplicate or Extend rather than PC screen only. Beyond that, HDMI is designed to work automatically once the cable connects a working port to the correct TV input. If Win + P shows no second display, the problem is the cable, the input selection, or the GPU driver — not a hidden setting you missed."
- q: "Can a Windows update break HDMI output?"
  a: "Yes. Updates sometimes replace the GPU driver with a version that mishandles HDMI handshake, or they reset display settings to PC screen only. If HDMI worked before an update and stopped after, reinstalling the GPU driver from your laptop manufacturer or the GPU vendor is the most reliable fix. Also recheck Win + P, since updates occasionally reset the projection mode."
- q: "Why does HDMI work for video but not audio?"
  a: "HDMI carries both, but Windows treats the TV as a separate audio device that must be selected as the output. Right-click the speaker icon, open Sound settings, and set the TV or monitor as the output device. If the TV does not appear in the output list, the GPU's audio driver component may need reinstalling — it installs alongside the graphics driver, so a GPU driver reinstall fixes both."
---

You connect the HDMI cable, the TV flickers, and then — "No Signal." Or the laptop screen goes black while the TV stays dark. Or everything works except the sound. HDMI is supposed to be plug-and-play, and when it is not, the failure gives you almost nothing to work with: a cable, two ports, and silence.

Most HDMI problems fall into three buckets: the display is listening on the wrong input, Windows is not sending anything (projection mode), or the handshake between the GPU and the display fails (cable, driver, or port). Each bucket has a quick test, and running them in order finds the fault fast — no guesswork, no random setting changes.

This guide covers laptop-to-TV and laptop-to-monitor HDMI equally, since the troubleshooting is identical. Work through the fixes in order.

## Why this happens

- **TV/monitor on the wrong input**: The display is listening on HDMI 2 while the laptop feeds HDMI 1.
- **Projection mode set to PC screen only**: Windows sends nothing to the external display by design.
- **Faulty or incompatible cable**: Damaged cables and very long runs fail the HDMI handshake.
- **GPU driver handshake failure**: A corrupted driver cannot complete HDCP and EDID negotiation.
- **Stale display configuration**: Windows caches a broken configuration for the display.
- **Port hardware fault**: Worn HDMI ports lose contact; some laptops disable HDMI in certain power states.
- **TV firmware quirks**: Older TVs mishandle handshake with newer laptop GPUs until power-cycled.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the input source and reseat the cable

Start at the display end, because it is the cause most often. TVs and monitors do not reliably auto-switch inputs, and "No Signal" on HDMI 1 while the laptop feeds HDMI 2 is indistinguishable from a dead port. Manually selecting the input and reseating the cable eliminates the two most common faults in under a minute.

1. Use the TV/monitor remote to open the input/source menu and select the exact HDMI port the cable uses.
2. Unplug the HDMI cable at both ends and plug it back in firmly until seated.
3. Try a different HDMI port on the TV — some ports (ARC, specifically) behave differently.
4. If the TV has multiple HDMI inputs, cycle through each one slowly, waiting five seconds per input.
5. Watch for any flicker or handshake attempt, which indicates the cable is at least partially working.

### Fix 2: Set the projection mode with Win + P

Windows may simply not be sending a picture. The projection mode controls this: "PC screen only" keeps everything on the laptop, while "Duplicate" and "Extend" activate the external display. Updates and Fn-key presses change this silently. Win + P is the fastest check and fix in one keystroke.

1. With the cable connected, press Win + P.
2. Choose "Duplicate" to mirror your laptop screen on the TV.
3. If Duplicate shows nothing, try "Extend" — then look for the display in Settings, System, Display.
4. Avoid "Second screen only" until the connection works; it blacks the laptop screen if the TV fails.
5. If Win + P shows only one display, the handshake is failing — continue below.

### Fix 3: Force Windows to detect the display

When the TV is on the right input and projection is set but Windows still sees no second display, force re-detection. Windows caches display identities (EDID data), and a corrupted cache entry makes it ignore a display it previously knew. Clearing the cached entry and rescanning forces a fresh handshake.

1. Open Settings, System, Display, and click "Detect" next to the display diagram.
2. In Device Manager, expand "Monitors" and uninstall any entry for the TV/monitor.
3. Click Action, "Scan for hardware changes."
4. Disconnect and reconnect the HDMI cable after the rescan.
5. Return to Display settings and check whether the second display appears.

### Fix 4: Update or reinstall the GPU driver

The GPU driver performs the HDMI handshake — resolution negotiation, HDCP content protection, and audio transport. A corrupted driver fails this silently, producing no-signal on a healthy cable and TV. Reinstalling the driver from the GPU vendor or laptop manufacturer rebuilds the handshake path. This is the fix when HDMI died after an update.

1. Open Device Manager and expand "Display adapters" to identify your GPU.
2. Download the latest driver from your laptop maker, or the GPU vendor directly.
3. Run the installer (choose clean install if offered) and restart.
4. Reconnect the HDMI cable after Windows has fully loaded.
5. Press Win + P, choose Duplicate, and check the TV. For Intel graphics, [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) automates the update.

### Fix 5: Try a different cable and rule out the port

Cables fail more often than ports — internal breaks from bending, chewed shielding, or simply a cable that never met spec. Long cables (over 5 meters) are especially suspect without active boosting. Swapping in a known-good, preferably short, high-speed cable isolates the cable definitively.

1. Replace the cable with a different one, ideally under 2 meters and rated High Speed or Ultra High Speed.
2. Test the original cable between two other devices to confirm whether it is faulty.
3. Try the laptop's HDMI with a different TV or monitor to isolate the laptop side.
4. Inspect the laptop's HDMI port for bent pins or debris with a flashlight.
5. If the port is physically damaged, a USB-C to HDMI adapter (on video-capable USB-C ports) bypasses it.

### Fix 6: Power-cycle both devices completely

HDMI handshake state can wedge on either end — the TV remembers a failed negotiation, the laptop's GPU holds a stale link. Standby does not clear it; only a full power drain does. This sounds too simple to matter, but it resolves a genuine share of stubborn no-signal cases, especially with older TVs.

1. Turn off the TV and unplug its power cable for a full 60 seconds.
2. Shut down the laptop completely (Shift + Shut down to bypass fast startup).
3. Unplug the HDMI cable from both ends during the wait.
4. Plug the TV back in, power it on, and set the correct HDMI input.
5. Boot the laptop, then connect the HDMI cable once Windows loads.

### Fix 7: Check firmware, BIOS, and audio routing

For the last stubborn cases, look at firmware: TV firmware updates fix handshake bugs with newer GPUs, and some laptops gate HDMI behind BIOS graphics settings. Separately, if video works but audio does not, the fix is routing, not hardware — the TV must be selected as the Windows output device. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document display and sound routing in detail.

1. Check the TV manufacturer's site for firmware updates addressing HDMI compatibility.
2. Enter the laptop BIOS and look for graphics mode settings (Hybrid/Discrete) — try toggling.
3. For missing HDMI audio: right-click the speaker icon, Sound settings, and set the TV as output.
4. If the TV is absent from the output list, reinstall the GPU driver (its audio component comes bundled).
5. As a final hardware test, try a USB-C to HDMI adapter to bypass the built-in port entirely.

DisplayPort connections follow the same diagnostic logic — see [fixing DisplayPort not working](/articles/how-to-fix-displayport-not-working-youtube/) for the DP-specific details. When Windows will not detect the external display at all, continue with [external monitor not detected](/articles/troubleshoot-external-monitor-not-detected/).

## Closing

HDMI failures are almost always one of three things: the wrong input selected, Windows not projecting, or a failed handshake from cable or driver. Check the input, press Win + P, swap the cable, refresh the GPU driver — in that order. The port hardware itself is the last suspect, and a USB-C adapter bypasses it when it truly fails.
