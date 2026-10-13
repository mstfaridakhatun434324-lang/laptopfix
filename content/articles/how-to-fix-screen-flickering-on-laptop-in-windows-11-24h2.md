---
title: "Screen Flickering on Windows 11 24H2? End the Flicker"
slug: how-to-fix-screen-flickering-on-laptop-in-windows-11-24h2
date: 2026-10-06
categories: ["drivers"]
tags: ["screen flickering", "display flicker", "windows 11 24h2", "refresh rate"]
description: "Fix screen flickering on Windows 11 24H2: identify app vs driver flicker with Task Manager, reinstall graphics drivers, and fix refresh-rate issues."
thumbnail: "/images/thumbs/how-to-fix-screen-flickering-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "How do I tell if the flickering is caused by an app or the display driver?"
    a: "Open Task Manager with Ctrl+Shift+Esc and watch it during the flicker. If Task Manager flickers along with everything else, the display driver is the cause. If Task Manager stays perfectly steady while the rest of the screen flickers, an incompatible application is responsible. This single test splits the diagnosis cleanly."
  - q: "Why did my screen start flickering right after the 24H2 update?"
    a: "The update migrates the graphics driver, and the migrated driver is the most common source of new flickering. It can also reset the refresh rate to a value the panel handles poorly or re-enable variable refresh features that conflict with the driver. Driver-first troubleshooting is the right response to post-update flicker."
  - q: "Can the wrong refresh rate cause flickering?"
    a: "Yes. A refresh rate the panel does not handle cleanly — or a mismatch between the set rate and the panel's native rate — produces visible flicker, especially at low brightness. Setting the display to its native refresh rate in Advanced display settings resolves a surprising number of cases."
  - q: "Is screen flickering a sign my display is dying?"
    a: "Usually not. Flickering that Task Manager shares is a driver issue; flickering isolated to one app is a software conflict; flickering with visible lines, discoloration, or pressure-sensitivity is hardware. The Task Manager test plus an external monitor test distinguish these definitively before you worry about the panel."
---

Screen flickering is uniquely maddening among display problems: the laptop is fully usable, yet the constant shimmer makes your eyes ache within minutes. On Windows 11 24H2, flickering that appears after the update has a prime suspect — the migrated graphics driver — but apps, refresh-rate settings, and panel hardware all produce their own flavors of flicker. The critical first step is a thirty-second test that tells you which of these worlds you are in.

That test is Task Manager. Open it during the flicker and watch: if Task Manager flickers too, the display driver owns the problem. If Task Manager is rock steady while everything behind it shimmers, an incompatible application is drawing badly. This distinction, straight from Microsoft's own troubleshooting guidance, prevents hours of driver work on what turns out to be a single misbehaving program — or vice versa.

The guide below starts with that test, then branches: the driver path for Task-Manager-flickers cases, the app path for steady-Task-Manager cases, and the settings and hardware checks that catch the remainder.

## Why this happens

- **Migrated graphics driver from the 24H2 update:** The update's replacement driver may mishandle the panel's timing, producing flicker that did not exist before the update.
- **Incompatible application:** Apps with broken hardware acceleration or outdated rendering — historically including some antivirus and cloud-storage clients — can make the whole screen flicker while Task Manager stays clean.
- **Wrong refresh rate:** A non-native refresh rate stresses the panel's timing controller. The update can reset this setting silently.
- **Variable refresh rate conflicts:** G-Sync, FreeSync, or adaptive sync negotiating badly with the driver produces rhythmic flicker, especially at low frame rates.
- **Corrupted color profile:** A damaged ICC color profile can cause shimmering and banding that reads as flicker.
- **Loose or damaged display cable:** The internal eDP cable flexes every time the lid moves. Flicker that changes when you adjust the lid angle is the classic cable signature.
- **Failing panel or backlight:** Backlight flicker at low brightness and flicker with discoloration point at the panel hardware itself.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Task Manager flicker test

This test decides the entire diagnostic direction. Do it first, before changing anything.

1. Press Ctrl+Shift+Esc to open Task Manager.
1. Watch it for thirty seconds during active flickering.
1. Task Manager flickering too means a driver problem — follow the driver path below. Task Manager steady means an app problem — skip to the app step.

### Fix 2: Reinstall the graphics driver (driver-path flicker)

For Task-Manager-flickers cases, the migrated driver is the prime suspect. Replace it cleanly.

1. Download the current graphics driver for your GPU — Intel via Intel's [Driver and Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA or AMD from their sites.
1. Use DDU from Safe Mode for a thorough removal, then install fresh.
1. Restart and retest. If the flicker began with 24H2 specifically, the [post-update flicker notes](/articles/how-to-fix-screen-flickering-on-laptop-after-windows-11-update/) cover adjacent cases.

### Fix 3: Remove the incompatible app (app-path flicker)

For steady-Task-Manager cases, find and remove the offending program.

1. Think about what was installed or updated when the flicker started.
1. Uninstall suspect apps one at a time — cloud storage clients, antivirus suites, and screen utilities first — testing after each.
1. Check the app vendor's site for a Windows 11 24H2-compatible version before reinstalling anything.

### Fix 4: Set the native refresh rate

A wrong refresh rate is a quick settings fix that resolves many cases outright.

1. Open Settings, then System, then Display, then Advanced display.
1. Set the refresh rate to the panel's native value — usually the highest listed, commonly 60, 120, or 144 Hz.
1. If variable refresh rate options appear, try disabling them temporarily to test.

### Fix 5: Reset the color profile

A corrupted color profile causes shimmer that mimics driver flicker.

1. Search for Color Management and open it.
1. On the Devices tab, select your display and remove custom profiles, reverting to the system default.
1. Restart and check whether the shimmer is gone.

### Fix 6: Test with an external monitor and the lid

Separate panel hardware from everything else with two physical tests.

1. Connect an external monitor: flicker on both screens means driver or GPU; flicker only on the laptop panel means panel, cable, or backlight.
1. Slowly adjust the lid angle: flicker that changes with angle indicates the internal display cable.
1. If the driver path keeps failing despite clean installs, the [TDR crash guide](/articles/how-to-fix-display-driver-stopped-responding-in-windows-11-24h2/) addresses the deeper driver instability behind some flicker. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the official flicker troubleshooting flow.

### Fix 7: Test in Safe Mode to isolate driver from hardware

Safe Mode loads only the basic display driver, which makes it an excellent flicker discriminator. If the flicker disappears in Safe Mode, the full graphics driver or a startup program is responsible, and your troubleshooting stays in software. If the flicker persists in Safe Mode, the panel, cable, or backlight is suspect, because the basic driver does almost nothing that could flicker on its own. Take a photo of the flicker with your phone before rebooting, since describing shimmer to a repair shop is harder than showing it.

1. Boot into Safe Mode through Settings, then Recovery, then Advanced startup.
1. Observe the screen for several minutes at the same brightness where flicker normally appears.
1. No flicker in Safe Mode means returning to the driver path with confidence; flicker in Safe Mode means focusing on the panel hardware and the lid-cable test.
1. Restart normally afterward. Safe Mode changes nothing permanently.

## Closing

Screen flickering on 24H2 surrenders to methodical diagnosis: the Task Manager test picks the battlefield, and each path — driver, app, refresh rate, or hardware — has a decisive test and fix. Most post-update flicker is the migrated driver and ends with a clean reinstall. The flicker that survives all of this is hardware talking, and the external monitor test will have told you exactly which hardware.
