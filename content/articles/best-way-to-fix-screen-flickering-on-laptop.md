---
title: "Best Way to Fix Screen Flickering on a Laptop (Step-by-Step)"
slug: "best-way-to-fix-screen-flickering-on-laptop"
date: "2026-09-12"
categories: ["drivers"]
tags: ["screen flickering", "display issue", "gpu driver", "windows 11"]
description: "Laptop screen flickering, flashing, or strobing? Follow this technician-tested sequence — from refresh-rate checks to driver reinstalls — to find and fix the cause fast."
thumbnail: "/images/thumbs/best-way-to-fix-screen-flickering-on-laptop.webp"
faqs:
  - q: "Why is my laptop screen flickering after a Windows update?"
    a: "Windows updates frequently replace or reset the graphics driver and can change the refresh rate to an unsupported value. Reinstalling the latest driver from Intel, NVIDIA, or AMD with a clean install, and resetting the refresh rate to your panel's native value, resolves most post-update flicker."
  - q: "How do I know if screen flicker is hardware or software?"
    a: "Take a screenshot during the flicker: if the screenshot shows it, the GPU or driver is at fault (software). If the screenshot is clean but you see flicker, the panel, cable, or backlight is failing (hardware). Flicker visible in the BIOS screen also points to hardware."
  - q: "Can a loose display cable cause flickering?"
    a: "Yes — it is the most common hardware cause. The display cable flexes through the hinge every time you open the lid, and years of flexing loosen the connector or crack internal traces. If flicker changes as you move the lid, the cable is almost certainly the culprit."
  - q: "Does screen flickering mean my GPU is dying?"
    a: "Rarely. A dying GPU usually produces artifacts, crashes, or a dead display rather than simple flicker. Flicker is far more often a driver, refresh-rate, cable, or panel issue. If an external monitor shows a perfect image, your GPU is healthy and the laptop's panel assembly is the problem."
---

Screen flickering ranges from mildly annoying to completely unusable: the display strobes, flashes black briefly, or shows tearing lines. The first diagnostic question is whether the flicker appears in screenshots and in the BIOS screen. Flicker in a screenshot means software — the GPU is rendering bad frames. Flicker visible only to your eyes means the panel, display cable, or refresh-rate negotiation.

That test divides every flicker fix into two tracks. Software flicker — far more common — is usually a graphics driver or refresh-rate issue, fixable in minutes. Hardware flicker needs a cable reseat or panel replacement.

Most flicker follows a driver or Windows feature update, making the graphics driver the prime suspect. Our [post-update flicker guide](/articles/how-to-fix-screen-flickering-on-laptop-after-windows-11-update/) covers that angle; here is the complete general-purpose sequence.

## Why this happens

- ****Corrupted or incompatible graphics driver**:** A bad update or partial install makes the driver output unstable frames, which you see as flicker.
- ****Wrong refresh rate**:** If Windows sets the panel to a refresh rate it does not support — 60 Hz on a 144 Hz panel after a driver reset, for example — the display strobes or tears.
- ****Loose or damaged display cable**:** The hinge-routed ribbon cable flexes every time you open the lid; years of flexing loosen the connector or crack traces, causing intermittent flicker.
- ****Failing backlight or panel**:** An aging panel or a failing backlight inverter circuit produces flicker that worsens with brightness changes and never appears in screenshots.
- ****Conflicting apps or overlays**:** Screen recording tools, third-party overlays, and some antivirus products hook the display pipeline and can cause flashing, especially in fullscreen apps.
- ****Dynamic refresh rate bugs**:** Windows 11's dynamic refresh rate feature switches between 60 Hz and 120 Hz+ to save battery. On some panels the switching itself is visible as flicker.
- ****Electromagnetic interference or bad power**:** A failing charger or a damaged power brick can inject electrical noise that shows up as faint shimmering, particularly at low brightness.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Screenshot and BIOS Test

Take a screenshot while the flicker is happening (Windows key + Shift + S) and view it on another device or zoom in. If the flicker is visible in the screenshot, your GPU or its driver is producing bad frames — a software problem. If the screenshot is clean but your eyes see flicker, the panel, cable, or backlight is at fault — a hardware problem.

Then restart into the BIOS setup screen: flicker there, with no Windows driver loaded, confirms hardware; no flicker points at Windows or the driver.

1. 1. Capture the flicker with Windows key + Shift + S.
2. 2. View the screenshot on another device and zoom in.
3. 3. Restart and enter the BIOS setup screen.
4. 4. Observe whether the flicker appears in the BIOS.
5. 5. Software track if screenshots show it; hardware track if only your eyes do.

### Fix 2: Set the Correct Refresh Rate

Right-click the desktop, choose Display settings, then Advanced display. Check the refresh rate dropdown — it should match your panel's native rate (60 Hz, 120 Hz, 144 Hz, or 165 Hz depending on the model). Driver updates sometimes reset this to the wrong value, and the mismatch causes visible strobing.

If your laptop offers dynamic refresh rate, turn it off and lock a fixed rate — on several panels the switching itself is the flicker. Watch the screen for a full minute after applying the change.

1. 1. Right-click the desktop and open Display settings.
2. 2. Click Advanced display and check the refresh rate.
3. 3. Set it to your panel's native rate (check the laptop's specs).
4. 4. Turn off dynamic refresh rate if the option exists.
5. 5. Observe the screen for a full minute to confirm the fix.

### Fix 3: Reinstall the Graphics Driver Cleanly

In Device Manager, uninstall the display adapter with driver deletion, restart, then install the latest driver from Intel, NVIDIA, AMD, or your laptop maker (choose clean install for NVIDIA).

This removes the corrupted driver state updates leave behind — Microsoft documents it as a core display step in its [Windows support hub](https://support.microsoft.com/en-us/windows).

1. 1. In Device Manager, uninstall the display adapter including its driver.
2. 2. Restart the laptop and let Windows install a basic driver.
3. 3. Download the latest driver from the GPU or laptop maker.
4. 4. Install it, choosing clean install if the option exists.
5. 5. Restart once more and check for flicker.

### Fix 4: Disable Hardware Acceleration in Apps

If flicker happens only in a browser or specific app, the app's hardware acceleration is the likely trigger. Turn it off in the app's settings (Chrome/Edge: Settings, System) and relaunch.

This only fixes app-specific flashing, but it also tells you the GPU driver is struggling with that app's acceleration path — useful diagnostic information.

1. 1. Open the flickering app's settings.
2. 2. Find the hardware acceleration or GPU rendering option.
3. 3. Turn it off and fully relaunch the app.
4. 4. Confirm the flicker is gone in that app.
5. 5. Repeat for any other affected apps.

### Fix 5: Check the Display Cable and Hinges

For hardware-track flicker, the display cable is suspect number one. Open and close the lid slowly through its full range — if flicker changes with lid angle, the cable or connector is the problem.

Reseating the cable means removing the bottom panel and display bezel per your service manual — or visit a repair shop, where a cable reseat is a quick, inexpensive job.

1. 1. Slowly open and close the lid while watching the flicker.
2. 2. Note whether flicker intensity changes with lid angle.
3. 3. If it does, the display cable or connector is at fault.
4. 4. Reseat the cable following your model's service manual, or take it to a shop.
5. 5. Replace the cable if reseating does not resolve it.

### Fix 6: Test With an External Monitor

Connect an external monitor via HDMI or USB-C. If the external display is solid while the laptop panel flickers, the panel, cable, or backlight is at fault — the GPU is fine. Identical flicker on both means a GPU or driver problem.

This test doubles as a workaround while you arrange a panel repair. For detection problems, see our [external monitor guide](/articles/what-to-do-if-external-monitor-not-detected/).

1. 1. Connect an external monitor via HDMI or USB-C.
2. 2. Duplicate or extend the display.
3. 3. Compare flicker on both screens for several minutes.
4. 4. External clean plus internal flicker means panel or cable failure.
5. 5. Both flickering means a GPU or driver problem — return to Fix 3.

### Fix 7: Adjust Brightness and Power Settings

Some panels flicker only at specific brightness levels due to pulse-width modulation (PWM) dimming. Raise brightness above 50 percent — if flicker stops, low-brightness PWM dimming is the cause. Also compare charger-plugged versus battery behavior.

If the flicker only happens on battery, the GPU power-saving states are likely dropping the panel clock too aggressively. In your power plan's advanced settings, set the graphics power settings to Maximum Performance and retest.

1. 1. Raise screen brightness above 50 percent and observe.
2. 2. Test with the charger plugged in, then on battery only.
3. 3. In advanced power settings, set graphics to Maximum Performance.
4. 4. Disable panel self-refresh if your Intel graphics panel offers it.
5. 5. Keep the brightness level that eliminates the flicker.

## Closing

Flickering feels alarming, but the diagnosis is logical: screenshots and the BIOS test classify it in two minutes, and the fix is usually a refresh-rate correction or clean driver reinstall. Only lid-angle-tracking flicker that survives every software fix warrants budgeting for a cable or panel replacement.
