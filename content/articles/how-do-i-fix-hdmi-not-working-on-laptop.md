---
title: "How to Fix HDMI Not Working on a Windows Laptop"
slug: "how-do-i-fix-hdmi-not-working-on-laptop"
date: "2026-09-13"
categories: ["drivers"]
tags: ["hdmi", "external display", "windows 11", "graphics driver", "troubleshooting"]
description: "No signal on your HDMI monitor? Learn why laptop HDMI ports fail and follow seven technician-tested fixes, from cable checks to driver repairs."
thumbnail: "/images/thumbs/how-do-i-fix-hdmi-not-working-on-laptop.webp"
faqs:
  - q: "Why is my laptop not detecting my monitor over HDMI?"
    a: "The most common reasons are a faulty or loose cable, the monitor set to the wrong input source, a corrupted graphics driver, or display output disabled in Windows. First swap the cable and press Windows + P to cycle projection modes. If nothing appears, check Device Manager for display adapter errors and reinstall the driver from your laptop manufacturer's support page."
  - q: "Can a bad HDMI cable stop a monitor from being detected?"
    a: "Yes. Worn, loose, or low-quality cables are a leading cause of HDMI failures. A cable that works at low resolutions can still fail at 4K or high refresh rates if its bandwidth is insufficient. Always test with a known-good cable, reseat both ends firmly, and try a different port on the monitor. Confirm the cable works between two other devices to rule it out completely."
  - q: "Should I update my graphics driver to fix HDMI problems?"
    a: "Usually yes. HDMI output depends on the GPU driver, and Windows updates or failed installs can corrupt it. Open Device Manager, expand Display adapters, and update the driver. If the problem started right after an update, roll the driver back instead. For NVIDIA or AMD systems, install the latest driver from the official source and choose a clean installation to remove leftover settings."
  - q: "What if HDMI works on another laptop but not mine?"
    a: "Then the cable and monitor are fine, so focus on your laptop. Check that Windows + P is not set to PC screen only, update or reinstall the graphics driver, and look in the BIOS for options that disable external display output. Also try a cold boot with the HDMI cable already connected, since some laptops only negotiate the handshake during startup."
---

You plug in the HDMI cable, the monitor wakes from sleep, and then... nothing. No signal. The laptop screen keeps showing your desktop like the monitor does not exist. Few things are more annoying than an HDMI port that worked fine yesterday and now refuses to acknowledge an external display.

In my experience, HDMI failures on Windows laptops almost always come down to one of a handful of causes: a bad cable, the wrong projection mode, a broken graphics driver, or a handshake issue between the laptop and the monitor. The good news is that most of these are fixable in minutes once you know where to look. Our [second monitor detection guide](/articles/how-to-fix-second-monitor-not-detected-windows-11-step-by-step/) covers related display problems too.

Below you will find the exact diagnostic order a technician would follow: quick physical checks first, then Windows settings, then drivers. Work through the fixes in order and do not skip the cable test. It resolves more cases than anything else.

## Why this happens

- **A damaged or under-specified HDMI cable:** Internal wires break from repeated bending, and cheap cables lack the bandwidth for 4K or 144 Hz signals.
- **The monitor is on the wrong input source:** TVs and monitors with multiple HDMI ports default to HDMI 1, while your cable may sit in HDMI 2.
- **Windows is set to PC screen only:** The projection mode (Windows + P) may have flipped after an update or docking session, hiding the second display.
- **A corrupted or outdated graphics driver:** The GPU driver handles HDMI negotiation; a bad driver can kill output while the built-in screen still works.
- **External display output is disabled in the BIOS:** Some business laptops let administrators disable HDMI output entirely for security reasons.
- **A failed HDMI handshake:** The laptop and monitor exchange resolution and encryption data when connected; if it desyncs, you get a black screen.
- **Conflicting resolution or refresh rate settings:** Windows may push 4K at 60 Hz to a monitor that only supports 4K at 30 Hz over its HDMI version.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reseat and swap the HDMI cable

Before touching any software, rule out the physical layer. HDMI cables fail silently: they will carry a partial signal or nothing at all once a conductor breaks. A five-minute cable test saves hours of driver troubleshooting.

1. Unplug the HDMI cable from both the laptop and the monitor.
2. Inspect both ends for bent pins, cracked housing, or loose connectors.
3. Reconnect firmly. You should feel the plug seat fully with no wiggle.
4. If possible, test with a different HDMI cable, ideally one rated High Speed or Ultra High Speed.
5. Try a different HDMI port on the monitor if one is available.

### Fix 2: Select the correct input and projection mode

Two simple settings block HDMI more often than any hardware fault: the monitor listening on the wrong input and Windows sending the image to the wrong screen. Both take seconds to check.

1. Use the monitor's menu buttons to select the exact HDMI input your cable uses, such as HDMI 1 versus HDMI 2.
2. On the laptop, press Windows + P to open the projection panel.
3. Choose Duplicate or Extend. Never use PC screen only for this test.
4. Wait a few seconds; monitors can take up to ten seconds to lock onto a new signal.
5. If the image appears stretched, open display settings and fix the resolution afterward.

### Fix 3: Power-cycle to force a fresh HDMI handshake

The HDMI handshake, where the laptop and monitor agree on resolution, refresh rate, and HDCP encryption, sometimes desyncs. A full power cycle forces both sides to renegotiate from scratch.

1. Shut down the laptop completely. Sleep and restart are not enough here.
2. Unplug the monitor's power cable and wait thirty seconds.
3. Disconnect the HDMI cable from both ends.
4. Power the monitor back on first, then reconnect the HDMI cable.
5. Boot the laptop and check whether the monitor is now detected.

### Fix 4: Update or reinstall the graphics driver

The GPU driver controls HDMI output. A Windows feature update or a failed driver install can corrupt it while leaving the internal display untouched. Reinstalling a clean driver fixes most persistent HDMI failures. If you also run into [HDMI issues on Windows 11 24H2](/articles/how-to-fix-hdmi-not-working-on-laptop-in-windows-11-24h2/), the same driver repair usually applies.

1. Open Device Manager and expand Display adapters.
2. Right-click your GPU (Intel, NVIDIA, or AMD) and choose Uninstall device, ticking the option to delete the driver software if offered.
3. Restart the laptop; Windows will install a basic fallback driver.
4. Download the latest driver from your laptop maker's support page or the GPU vendor's site.
5. Install it, restart once more, and retest the HDMI connection.

### Fix 5: Check display output settings in the BIOS

Some laptops, especially business models from Dell, HP, and Lenovo, include a BIOS option that disables HDMI or external display output. If every software fix fails, this buried setting is worth checking.

1. Restart the laptop and press the BIOS key (F2, F12, Delete, or Esc depending on the brand).
2. Look under Advanced, Video, or Display settings for options like External Display or HDMI Output.
3. Make sure external output is enabled rather than set to internal display only.
4. Save and exit (usually F10), boot Windows, and test HDMI again.

### Fix 6: Roll back a recent graphics driver or Windows update

If HDMI broke immediately after an update, the new code is the prime suspect. Windows keeps the previous driver version, and rolling back takes about a minute.

1. Open Device Manager, expand Display adapters, and open your GPU's Properties.
2. Go to the Driver tab and click Roll Back Driver if the button is active.
3. Choose a reason, confirm, and restart the laptop.
4. If the culprit was a Windows feature update, check Windows Update history for a rollback option.
5. Pause driver updates temporarily so the bad version does not reinstall overnight.

### Fix 7: Match resolution and refresh rate to the monitor

Windows sometimes remembers a 4K at 60 Hz profile for a monitor whose HDMI 1.4 port tops out at 4K and 30 Hz. The result is a permanent no-signal screen. Dropping to a supported mode often brings the picture back instantly.

1. With HDMI connected, open Settings, then System, then Display, and select the external monitor.
2. Open Advanced display settings and lower the refresh rate to 60 Hz or 30 Hz.
3. Set the resolution to the monitor's native value (check the manual or the label on the back).
4. If the monitor still shows nothing, boot into Safe Mode at low resolution and adjust from there.
5. Consult the monitor maker's documentation if you are unsure which HDMI version each port supports.

## Closing

HDMI problems feel like hardware failures, but they are usually a cable, a setting, or a driver, all of which you can fix yourself in under half an hour. Start with the cable and the Windows + P panel, because those two checks resolve the majority of cases. If you have worked through every fix here and the port is still dead across multiple cables and monitors, the HDMI controller itself may have failed, and that is a job for the manufacturer's repair service.
