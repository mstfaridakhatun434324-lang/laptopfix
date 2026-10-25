---
title: "Recall Not Working on External Monitor? Fix It Step by Step"
slug: recall-external-monitor-not-working
date: 2026-10-25
categories: ["ai-pc"]
tags: ["Recall", "Copilot+ PC", "Windows 11", "external monitor", "display"]
description: "Recall not capturing your external monitor? Learn why snapshots skip second screens and how to get full multi-monitor Recall coverage on your Copilot+ PC."
thumbnail: "/images/thumbs/recall-external-monitor-not-working.webp"
faqs:
  - q: "Does Recall capture external monitors?"
    a: >
      Yes, Recall is designed to capture all connected displays, including
      external monitors. If only your laptop screen appears in the timeline,
      a display, driver, or scaling issue is preventing capture of the second
      screen rather than a Recall limitation.
  - q: "Why does Recall ignore my second monitor?"
    a: >
      Common causes are a monitor that Windows sees as disconnected, a
      graphics driver problem, mixed-DPI scaling conflicts, or the monitor
      being in a power-saving state when snapshots are taken.
  - q: "Do I need to change settings for multi-monitor Recall?"
    a: >
      Usually not. Recall captures all active displays by default. The fixes
      in this guide focus on making Windows treat the external monitor as a
      healthy, active display, which is normally all Recall needs.
  - q: "Will docking and undocking break Recall capture?"
    a: >
      Docking changes can temporarily confuse display detection, but Recall
      recovers once Windows re-detects the monitor. Persistent gaps after
      docking point to a driver or detection problem worth fixing properly.
---

You dock your Copilot+ laptop, spread your work across two screens, and later discover Recall only remembers what happened on the laptop display. Everything you did on the external monitor is missing from the timeline, as if that screen never existed. For multi-monitor users, that gap can swallow half a workday.

Recall is supposed to capture every active display, so a missing monitor is a detection problem, not a feature limit. The usual suspects are Windows not fully recognising the monitor, a graphics driver that mishandles the second screen, scaling mismatches, or the monitor sleeping while you work. Each has a distinct fix, and working through them in order will identify yours.

Multi-monitor trouble often travels with other display and NPU issues, so check the wider picture too. If your NPU is not detected in creative apps, see our guide to [NPU not detected in DaVinci](/articles/npu-not-detected-davinci/), and Dell users should check [Dell Pro 14 AI problems](/articles/dell-pro-14-ai-problems/). If you also use Click to Do across monitors, our guide to [Click to Do summarize PDF not working](/articles/click-to-do-summarize-pdf-not-working/) covers related capture quirks.

## Why this happens

- **Monitor not fully detected:** Windows may show the monitor as connected but not treat it as an active display for capture.
- **Graphics driver bug:** A driver that mishandles multi-monitor output can leave the second screen invisible to Recall.
- **Monitor in power-saving state:** A sleeping or dimmed external monitor produces no capturable content.
- **Mixed-DPI scaling conflict:** Very different scaling values between displays can break capture on one of them.
- **Dock or cable issue:** A loose connection, faulty dock, or low-quality cable can cause intermittent detection.
- **Display mode set to single screen:** If Windows is set to show only one display, the other screen is not captured by design.
- **Snapshot service glitch after display changes:** Rapid docking and undocking can leave the snapshot service tracking a stale display layout.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Windows is extending to the external monitor

The simplest explanation is also the most common: Windows is set to duplicate or show only one display. Switching to Extend mode makes the external monitor a real, independent display that Recall can capture.

1. Press Windows + P to open the project menu.
2. Select Extend.
3. Open Settings, go to System, then Display.
4. Confirm both monitors appear and are arranged correctly.
5. Click Identify to confirm which number is the external monitor.
6. Use the external monitor actively for 10 minutes, then check Recall.

### Fix 2: Re-detect the monitor cleanly

If the monitor appears but Recall still skips it, force Windows to re-detect displays. This clears stale display records left over from docking changes and gives Recall a clean layout to capture.

1. Open Settings, go to System, then Display.
2. Click Detect if the monitor is missing or greyed out.
3. If that fails, disconnect and reconnect the monitor cable.
4. Try a different port on the dock or laptop if available.
5. Restart the PC with the monitor connected.
6. Confirm both displays are active, then test Recall capture.

### Fix 3: Update the graphics driver

Multi-monitor capture depends heavily on the graphics driver, and an outdated driver is a prime suspect when one screen is skipped. Update through Windows Update first, then the manufacturer's tool if needed.

1. Open Settings, go to Windows Update, and install pending updates.
2. Open Device Manager and expand Display adapters.
3. Right-click your graphics adapter and choose Update driver.
4. If Windows finds nothing, check Intel, AMD, or NVIDIA support tools.
5. Restart after installing.
6. Verify Recall now captures the external monitor.

### Fix 4: Match scaling and resolution across displays

Wildly different scaling between a high-DPI laptop screen and a standard external monitor can break capture on one display. Setting each to its recommended values usually restores capture on both.

1. Open Settings, go to System, then Display.
2. Select the laptop display and set its recommended scale.
3. Select the external monitor and set its recommended scale.
4. Set each display to its native resolution.
5. Sign out and back in if prompted.
6. Test Recall on both screens for 15 minutes.

### Fix 5: Keep the external monitor awake

A monitor that sleeps, dims, or powers down while you work produces nothing to capture. Check the monitor's own power settings and Windows power settings so the external screen stays active during your work sessions.

1. Open the monitor's on-screen menu and check its power-saving options.
2. Set the monitor to stay on during use, not auto-sleep quickly.
3. In Windows, open Settings, go to System, then Power.
4. Set the display timeout generously for plugged-in use.
5. Move the mouse on the external monitor periodically during tests.
6. Confirm Recall captures the external screen consistently.

### Fix 6: Restart the snapshot service after display changes

Docking and undocking can leave the snapshot service tracking an old display layout. Restarting it after the display setup is stable forces it to re-read the current monitors and resume full capture.

1. Set up your monitors and confirm both are active.
2. Press Windows + R, type `services.msc`, and press Enter.
3. Restart the Recall snapshot service.
4. Use both monitors actively for 15 minutes.
5. Open Recall and check for snapshots from each display.
6. If capture is still single-screen, restart the PC with the dock connected.

### Fix 7: Test the dock and cable

Intermittent detection often comes from hardware: a marginal cable or dock port can make the monitor flicker in and out of Windows' view, and Recall cannot capture a display that keeps vanishing. A direct connection test isolates the hardware from the software.

1. Connect the monitor directly to the laptop, bypassing the dock.
2. Check whether Recall captures it reliably.
3. If yes, the dock or its cable is suspect — try another dock port.
4. Swap in a known-good cable.
5. Update the dock firmware if the manufacturer provides it.
6. For ongoing display issues, see the official [Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

An external monitor missing from Recall is a display detection problem in almost every case, and the fixes are practical: extend mode, clean detection, driver updates, and matched scaling. Once both screens are captured, your timeline finally reflects how you actually work — across every display, not just the laptop's own.
