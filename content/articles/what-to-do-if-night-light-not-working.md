---
title: "Night Light Not Working on Windows 11? Fix the Grayed-Out Toggle"
slug: what-to-do-if-night-light-not-working
date: 2026-09-30
categories: ["drivers"]
tags: ["night light not working", "night light greyed out", "blue light filter", "display driver", "windows 11"]
description: "Night Light not working or grayed out on Windows 11? Fix it with registry repairs, driver updates, location settings, and schedule troubleshooting."
thumbnail: "/images/thumbs/what-to-do-if-night-light-not-working.webp"
faqs:
  - q: "Why is Night Light grayed out in Windows 11 settings?"
    a: "A grayed-out Night Light toggle almost always means the display driver isn't exposing color-temperature control to Windows — usually a generic or corrupted GPU driver. Reinstalling the proper display driver from your laptop maker's site or the GPU manufacturer restores the toggle. Corrupted Night Light registry data from a bad update is the second most common cause."
  - q: "Why won't Night Light turn on at sunset?"
    a: "Sunset scheduling depends on location services — if Windows doesn't know where you are, it can't compute sunset. Enable location under Privacy and security, Location, and set your default location. Alternatively, switch the schedule to fixed hours instead of sunset-to-sunrise, which removes location from the equation entirely."
  - q: "Can a graphics driver update break Night Light?"
    a: "Yes. Display driver updates — from Windows Update or manual installs — can reset or corrupt the color-profile pipeline Night Light depends on. If Night Light broke immediately after a driver update, rolling back the display driver in Device Manager is the fastest fix, followed by a clean reinstall if rollback isn't available."
  - q: "Is there a registry fix for Night Light?"
    a: "Yes, for the specific case where the toggle is stuck or schedules don't apply. Deleting the corrupted state under the CloudStore registry key forces Windows to rebuild Night Light's configuration on next boot. It is safe when done exactly as documented, but back up the registry first — and only use it after driver fixes fail."
---

Night Light is a small feature with an outsized annoyance factor when it breaks: the toggle grays out, the schedule silently stops applying, or the screen just never warms no matter what the settings say. Because Night Light sits at the intersection of the display driver, the color-profile pipeline, location services, and a famously fragile registry state, the failure modes are varied — but they cluster into a few well-understood patterns. This guide matches each pattern to its fix, starting with the driver layer (the most common culprit) and ending with the registry reset that fixes the truly stubborn cases.

First, name your symptom: toggle grayed out, toggle works but nothing happens, or schedule doesn't trigger. Each points somewhere different below.

## Why this happens

- **Generic or corrupted display driver.** The driver not exposing color-temperature control — the top cause of grayed-out toggles.
- **Corrupted Night Light registry state.** Bad update leaving the CloudStore configuration in a stuck state.
- **Location services disabled.** Sunset scheduling with no location data to compute sunset from.
- **Conflicting color management.** Third-party calibration tools or GPU control panels overriding Night Light.
- **Fast startup preserving bad state.** Hibernation-based shutdowns carrying corrupted display state across reboots.
- **Organization policy disabling it.** Managed devices with Night Light blocked by group policy.
- **Display driver update resetting the pipeline.** Fresh driver, broken color-profile handshake.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reinstall the display driver

The core fix for grayed-out or non-functional Night Light.

1. **Device Manager > Display adapters** → right-click your GPU → **Uninstall device** → check "delete the driver software" if offered.
2. Restart — Windows installs a baseline driver; check whether the Night Light toggle is active again.
3. Install the proper driver: from your laptop maker's support page first, or Intel/NVIDIA/AMD directly — the vendor driver exposes the full color pipeline.
4. If Night Light broke right after a driver update, use **Roll Back Driver** on the Driver tab instead of a full reinstall.
5. Test the toggle after each step — Night Light depends on the driver's color-temperature interface, so the toggle state is your diagnostic readout.

The deeper GPU-driver method is covered in [how to fix the display driver stopped responding](/articles/how-to-fix-display-driver-stopped-responding-in-windows-11-24h2/).

### Fix 2: Reset the corrupted Night Light registry state

For stuck toggles and schedules that won't apply.

1. Press **Windows + R**, type `regedit`, press Enter (approve the UAC prompt).
2. Navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Cloud`.
3. Find the key named `default$windows.data.bluelightreduction.bluelightreductionstate` — right-click → **Delete**.
4. Also delete `default$windows.data.bluelightreduction.settings` if present.
5. **Restart** the laptop — Windows rebuilds Night Light's configuration from defaults on boot.
6. Reconfigure your Night Light schedule fresh afterward; the old corrupted schedule is gone with the deleted keys.

### Fix 3: Fix location services for sunset scheduling

When manual toggle works but the sunset schedule doesn't.

1. **Settings > Privacy & security > Location** → turn **Location services** on.
2. Set a **default location** (same page) — Windows needs this to compute sunset times.
3. As an alternative that skips location entirely: **Settings > System > Display > Night light** → **Schedule night light** → choose **Set hours** instead of "Sunset to sunrise."
4. Verify your **time zone** is correct (**Settings > Time & language**) — a wrong zone shifts the computed sunset.
5. Toggle the schedule off and back on after making these changes to force a recalculation.

### Fix 4: Remove color-management conflicts

Third-party tools that fight Night Light.

1. Check for calibration software (DisplayCAL, vendor calibration tools) — their loaded ICC profiles can override Night Light's color adjustments.
2. Open **Color Management** (`colorcpl.exe`) → **Advanced** → ensure the device profile is the system default, not a custom profile fighting the pipeline.
3. In your GPU control panel (Intel Graphics Command Center, NVIDIA Control Panel), reset **color settings** to defaults — custom digital vibrance or hue shifts stack badly with Night Light.
4. Disable **HDR** temporarily as a test — Night Light and HDR have a historically uneasy relationship on some panels. Related: [how to fix HDR not working on a laptop](/articles/how-to-fix-hdr-not-working-on-laptop-in-windows-11-24h2/).
5. Third-party "f.lux"-style apps conflict directly — use Night Light **or** f.lux, never both.

### Fix 5: Disable fast startup and reset display state

For Night Light that works after restart but breaks later.

1. Control Panel → Power Options → **Choose what the power buttons do** → **Change settings currently unavailable** → uncheck **Turn on fast startup**.
2. Shut down fully (not restart), wait 10 seconds, power on — this clears the hibernation-carried display state.
3. After booting, toggle Night Light off and on once to re-seat its state.
4. If the problem recurs after sleep/wake specifically, update the **BIOS** — display power-state bugs live in firmware.
5. Also check **Settings > System > Display** for the brightness slider behaving oddly — related driver issues often travel together; see [how to fix display brightness not working](/articles/how-to-fix-display-brightness-not-working-in-windows-11-24h2/).

### Fix 6: Check policy and system corruption

For managed devices and deep corruption.

1. Press **Windows + R**, type `gpedit.msc` (Pro editions) → check for policies disabling Night Light or display features.
2. **Terminal (Admin)**: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart.
3. Install all pending **Windows updates** — Night Light framework fixes ship in cumulative updates.
4. Create a fresh Windows user profile and test Night Light there — per-user CloudStore corruption is exactly what Fix 2 addresses, but a new profile confirms it.
5. Check [Microsoft Support for Windows](https://support.microsoft.com/en-us/windows) for known Night Light issues on your build.

### Fix 7: Use a reliable alternative

When Night Light itself won't cooperate.

1. **f.lux** (free) replicates Night Light's functionality independently of the Windows pipeline — install it and disable Night Light to avoid conflicts.
2. Many laptop makers include their own blue-light filter (Lenovo Vantage Eye Care, ASUS Eye Care) — try the vendor's version.
3. Your monitor's on-screen menu may have a **low blue light** mode that works regardless of Windows.
4. These alternatives are legitimate long-term solutions, not just workarounds — f.lux predates Night Light and is arguably more configurable.
5. Revisit Night Light after the next major Windows update; pipeline bugs do get fixed eventually.

## Closing

Night Light breaks in patterns, and the pattern is the diagnosis: grayed-out toggle means the display driver, stuck toggle means the CloudStore registry state, dead sunset schedule means location services, and works-until-sleep means fast startup or firmware. The registry reset in Fix 2 looks intimidating but is the documented cure for the most stubborn variant — back up, delete the two keys, reboot, and the feature rebuilds itself clean. And if you'd rather not fight the pipeline at all, f.lux has been doing this job reliably for over a decade.
