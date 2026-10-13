---
title: "HDMI Not Working on Laptop in Windows 11? Fix It in Minutes"
slug: "how-to-fix-hdmi-not-working-on-laptop-on-windows-11"
date: 2026-09-15
categories: ["drivers"]
tags: ["hdmi not working", "windows 11", "external monitor", "no signal", "display settings"]
description: "TV or monitor not detected over HDMI on Windows 11? Run through these quick fixes for cables, display settings, and graphics drivers."
thumbnail: "/images/thumbs/how-to-fix-hdmi-not-working-on-laptop-on-windows-11.webp"
faqs:
  - q: "Why is HDMI not working after upgrading to Windows 11?"
    a: "Upgrades can carry over an older graphics driver that Windows 11 handles differently, or install a new inbox driver that mismatches the HDMI hardware. The fix is a clean install of the Windows 11 graphics driver from the laptop or GPU manufacturer. Also press Windows plus P to check the projection mode, since upgrades sometimes reset it to PC screen only."
  - q: "How do I get Windows 11 to detect my HDMI TV?"
    a: "Connect the cable, turn the TV on first, then open Settings, System, Display, and click Detect. Press Windows plus Ctrl plus Shift plus B to restart the graphics driver if detection fails. Make sure the TV is set to the correct HDMI input manually, since auto-switching often misses the signal."
  - q: "HDMI worked yesterday but not today. What changed?"
    a: "Overnight Windows updates are the usual suspect, especially driver updates that replace the working graphics driver. Check Device Manager for the display adapter driver date; if it changed overnight, roll it back. Sleep and hibernation glitches are the other common cause, fixed by a full shutdown rather than a restart."
  - q: "Does the HDMI cable version matter for Windows 11 laptops?"
    a: "For basic 1080p output almost any intact cable works, but 4K at 60Hz needs a high-speed cable rated for 18Gbps, and 4K at 120Hz needs an ultra high-speed 48Gbps cable. If the display is detected but shows no image at high resolutions, the cable is the first suspect. Try 1080p at 60Hz as a baseline test before blaming the laptop."
---

HDMI on Windows 11 should be plug-and-play, and when it is not, the usual suspects are the cable, the TV input, the projection mode, or the graphics driver. Windows 11's driver model changed enough from Windows 10 that HDMI failures cluster around updates and upgrades, which actually makes diagnosis easier: if it broke overnight, check what updated.

The physical chain is identical to Windows 10, so the same two-minute cable and input checks apply. Where Windows 11 differs is in display settings layout and in how aggressively Windows Update manages graphics drivers. This guide accounts for both.

Start physical, then move into settings and drivers. The [Windows 10 HDMI guide](/articles/how-to-fix-hdmi-not-working-on-laptop-on-windows-10/) covers the older OS, and the [second-monitor guide](/articles/how-do-i-fix-second-monitor-not-detected-windows-11/) goes deeper on detection.

## Why this happens

- **Loose or faulty cable:** the most common physical cause; cables fail silently from bending and wear.
- **TV on wrong input:** auto input switching misses the laptop signal frequently.
- **Projection mode reset:** upgrades and updates can revert the mode to PC screen only.
- **Graphics driver replaced:** Windows Update swaps the manufacturer driver for an inbox version.
- **Sleep resume glitch:** the GPU fails to re-enumerate HDMI after sleep or hibernation.
- **Resolution mismatch:** an unsupported mode produces a detected-but-black display.
- **HDCP handshake failure:** copy-protection negotiation fails through adapters or older TVs.
- **Port or cable bandwidth limit:** an old cable cannot carry the 4K mode the laptop tries to send.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Reseat the cable and confirm the TV input

Two minutes of physical checks resolve a large fraction of HDMI failures. Do this first every time, even if the cable looks fine.

1. Unplug the HDMI cable at both ends and plug it back in firmly.
2. Turn the TV on before connecting the laptop.
3. Use the TV remote to select the exact HDMI input manually.
4. Try a different HDMI port on the TV.
5. Swap in a known-good high-speed cable for the test.

### Fix 2: Set the projection mode with Windows + P

Windows 11 keeps the Windows 10 project panel. If the mode is PC screen only, the TV stays dark regardless of the connection.

1. Press Windows + P with the cable connected.
2. Choose Duplicate to test basic output.
3. Switch to Extend for a proper second-display setup.
4. Wait a few seconds after each selection.
5. Repeat after any reconnection of the cable.

### Fix 3: Force detection and restart the graphics driver

Windows 11 sometimes needs a manual push to enumerate the HDMI display. The Detect button plus the graphics driver restart shortcut covers both the OS and driver layers.

1. Open Settings, System, Display, and click Detect.
2. Press Windows + Ctrl + Shift + B; the screen will flash as the driver restarts.
3. Click Detect again after the blink.
4. If the TV appears, choose Extend these displays.
5. Set the TV to its native resolution.

### Fix 4: Do a full shutdown to clear sleep state

Sleep-resume glitches leave the GPU in a state where HDMI will not enumerate until fully reset. A shutdown clears what a restart preserves under Fast Startup.

1. Save your work and shut the laptop down completely.
2. Unplug the HDMI cable.
3. Wait 30 seconds, then power the laptop on.
4. Once at the desktop, plug the HDMI cable back in.
5. Check detection in display settings.

### Fix 5: Clean-install the Windows 11 graphics driver

The graphics driver owns HDMI negotiation. A clean install of the manufacturer's Windows 11 driver fixes update-caused breakage and corrupted installs alike.

1. Download the latest Windows 11 graphics driver for your GPU.
2. Run the installer with the clean installation option.
3. Restart the laptop with the HDMI cable connected.
4. Verify the driver version in Device Manager afterward.
5. Test detection and resolution switching on the TV.

### Fix 6: Test at 1080p to rule out bandwidth

If the TV is detected but black at 4K, the cable or port may lack the bandwidth. Dropping to 1080p proves the link and identifies the bottleneck.

1. In Display settings, select the TV display.
2. Open Advanced display settings.
3. Set resolution to 1920 x 1080 and refresh to 60Hz.
4. If the image appears, the cable is the 4K bottleneck.
5. Upgrade to an ultra high-speed cable for 4K modes.

### Fix 7: Check for Windows updates and official guidance

Microsoft occasionally ships fixes for HDMI and display enumeration in cumulative updates. A final check ensures the OS side is current.

1. Run Windows Update and install all pending updates.
2. Check optional updates for newer display drivers.
3. Restart after updates and retest HDMI.
4. Review display troubleshooting at the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).
5. If two TVs and two cables both fail, suspect the laptop HDMI port.

## Closing

HDMI on Windows 11 fails in predictable places: cable, input, projection mode, driver. Check them in that order and the TV lights up. After an update breaks it once, you will know to check the graphics driver first next time. A detail that saves future headaches: Windows 11 remembers display arrangements per monitor, so once the TV works, set it as you like it and Windows will restore that layout automatically next time it detects the same display. If you frequently connect to different TVs, such as in meeting rooms, carry a short certified high-speed cable of your own; venue cables are the most abused cables in existence and the leading cause of works-on-my-laptop-not-on-theirs embarrassment. And after any future feature update, give HDMI a quick test before the important presentation rather than discovering a driver swap five minutes before it starts. Finally, if the TV has multiple HDMI ports with different capabilities, note which one worked; some TVs only enable full bandwidth or ARC on specific ports, and using the same port every time avoids repeat confusion.
