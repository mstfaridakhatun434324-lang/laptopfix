---
title: "How to Fix Screen Flickering on a Windows Laptop"
slug: "how-to-fix-screen-flickering-on-laptop"
date: "2026-09-22"
categories: ["drivers"]
tags: ["screen flickering", "display", "graphics driver", "windows 11", "troubleshooting"]
description: "Laptop screen flickering nonstop? Identify whether it's a driver, app, or hardware issue and apply the right fix with this detailed guide."
thumbnail: "/images/thumbs/how-to-fix-screen-flickering-on-laptop.webp"
faqs:
  - q: "Why is my laptop screen flickering?"
    a: "Screen flickering is usually caused by a faulty display driver, an incompatible app, or a loose display cable. Open Task Manager: if Task Manager flickers too, the cause is the display driver or hardware. If Task Manager is steady while everything else flickers, an application is the culprit."
  - q: "Can a Windows update cause screen flickering?"
    a: "Yes. Display driver updates delivered through Windows Update are a classic trigger. If flickering started right after an update, roll back the display driver in Device Manager or reinstall the manufacturer's graphics driver. Blocking the problematic driver version prevents it from reinstalling."
  - q: "How do I know if flickering is hardware or software?"
    a: "Use the Task Manager test: press Ctrl + Shift + Esc and watch. Flicker in Task Manager points to the driver or the panel hardware. Boot into the BIOS setup screen; if the flicker appears there too, it is almost certainly a hardware issue with the panel, cable, or GPU."
  - q: "Can an app really make my whole screen flicker?"
    a: "Yes. Antivirus overlays, screen recorders, and some older utilities hook into the display pipeline and can cause system-wide flicker. If the Task Manager test points to software, uninstall recently added apps one by one, starting with anything that draws overlays or modifies the display."
---

A flickering laptop screen is uniquely maddening. It is not broken enough to stop you working, but it is impossible to ignore: the constant shimmer strains your eyes, and every flicker carries the worry that the display is dying.

Before you panic about hardware, know this: most laptop screen flicker is software. Display drivers cause the lion's share, followed by misbehaving apps. There is a simple thirty-second test, using Task Manager, that tells you which camp you are in. Display-side repairs like [fixing display driver crashes](/articles/how-to-fix-display-driver-stopped-responding-on-windows-11/) overlap heavily with this guide.

Run the diagnostic test first, then follow the fixes for your category. Hardware checks come last because they are the least likely and the hardest.

## Why this happens

- **A corrupted display driver:** The GPU driver renders every frame; a bad one produces flicker across the whole screen.
- **An incompatible application:** Overlay and hook-based apps can interfere with the desktop compositor.
- **Wrong refresh rate:** A refresh rate the panel does not truly support causes visible shimmer.
- **A loose internal display cable:** The ribbon cable through the hinge loosens over years of opening and closing.
- **Failing backlight or panel:** Aging panels and backlight circuits flicker, often worse at low brightness.
- **External interference or a bad charger:** Poorly shielded chargers can inject electrical noise into the display.
- **Dynamic refresh rate conflicts:** Variable refresh features can clash with certain panels and drivers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Task Manager flicker test

This single test splits the problem in half and tells you exactly which fixes to pursue. It takes thirty seconds and prevents wasted effort.

1. Press Ctrl + Shift + Esc to open Task Manager.
2. Watch the Task Manager window carefully for ten to twenty seconds.
3. If Task Manager flickers along with everything else, the cause is the display driver or hardware.
4. If Task Manager stays perfectly steady while the rest flickers, an application is causing it.
5. Note your result; the fixes below are grouped by which outcome you saw.

### Fix 2: Update or roll back the display driver

For driver-side flicker, the fix is a driver change: update if the driver is old, roll back if flicker started after an update. A clean reinstall covers both directions.

1. Open Device Manager and expand Display adapters.
2. If flicker started after an update, open Properties, go to the Driver tab, and click Roll Back Driver.
3. Otherwise, right-click the adapter and choose Update driver.
4. For a thorough fix, uninstall the device with driver deletion, restart, and install the maker's latest driver.
5. Test for several minutes at your normal brightness and resolution.

### Fix 3: Set the correct refresh rate

Panels have one native refresh rate where they are happiest. Running at an odd rate the panel merely tolerates can produce a visible shimmer, especially on budget displays.

1. Open Settings, then System, then Display, then Advanced display.
2. Note the current refresh rate and try the panel's native rate, usually 60 Hz.
3. If a higher rate is selected, drop to 60 Hz and observe for a few minutes.
4. Disable dynamic or variable refresh rate options as a test.
5. Keep the rate that is completely stable; smoothness is worthless if it flickers.

### Fix 4: Remove the offending application

For app-side flicker, the culprit is usually something installed recently that hooks the display: antivirus with overlays, screen recording tools, or desktop customization utilities.

1. Think back to what you installed around the time flicker started.
2. Open Settings, then Apps, and sort by install date.
3. Uninstall suspects one at a time, starting with overlay and recording software.
4. Restart after each uninstall and retest before removing the next.
5. Check the app maker's site for an updated version before giving up on software you need.

### Fix 5: Test with an external monitor

An external monitor tells you whether the GPU or the internal panel is at fault. If the external image is perfect, your GPU and driver are fine and the problem lives in the laptop's display assembly.

1. Connect an external monitor via HDMI or USB-C.
2. Press Windows + P and choose Duplicate.
3. Observe both screens for several minutes.
4. If only the laptop screen flickers, suspect the panel, cable, or backlight.
5. If both flicker, the GPU or its driver is the problem; revisit the driver fixes.

### Fix 6: Check the charger and power source

It sounds odd, but bad power can flicker screens. Aftermarket chargers with poor shielding inject electrical noise, and the effect often changes with brightness level.

1. Unplug the charger and run on battery for ten minutes.
2. If the flicker stops on battery, the charger is the prime suspect.
3. Test with the original manufacturer charger if you have it.
4. Try a different wall outlet, avoiding power strips full of other devices.
5. Replace third-party chargers that cause the issue; they can damage more than the display.

### Fix 7: Adjust the hinge and check for cable issues

If flicker changes when you move the lid, the internal display cable is loose or worn where it passes through the hinge. This is the classic hardware signature.

1. Slowly open and close the lid through its full range while watching the screen.
2. Note any angle where flicker worsens or disappears; that implicates the cable.
3. Do not attempt to reseat the cable yourself unless you are comfortable disassembling the laptop.
4. Back up your data before any hardware service.
5. If the BIOS screen flickers too, contact the manufacturer's repair service, since the panel or cable needs professional attention. Guidance on [brightness controls](/articles/how-to-fix-display-brightness-not-working-in-windows-11-24h2/) will not help a hardware fault, so do not delay the repair.

## Closing

Screen flicker feels like a dying display, but the Task Manager test usually reveals a driver or an app instead. Fix the software causes first, because they are free and fast. Only when the flicker follows the lid angle or appears in the BIOS should you accept that the panel hardware needs professional repair.
