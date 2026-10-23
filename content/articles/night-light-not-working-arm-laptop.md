---
title: "How to Fix Night Light Not Working on Your ARM Laptop"
slug: night-light-not-working-arm-laptop
date: 2026-10-23
categories: ["ai-pc"]
tags: ["night light", "blue light filter", "display", "arm laptop", "windows 11", "troubleshooting"]
description: "Fix Night Light not working on your ARM laptop with step-by-step solutions for display drivers, registry keys, schedules, HDR conflicts, and color profiles."
thumbnail: "/images/thumbs/night-light-not-working-arm-laptop.webp"
faqs:
  - q: "Why is Night Light greyed out on my ARM laptop?"
    a: "A greyed-out Night Light almost always means the display driver isn't exposing color-temperature control to Windows — typically a generic or corrupted ARM graphics driver. Reinstalling the OEM Adreno driver usually brings the toggle back immediately."
  - q: "Can I fix Night Light with a registry edit?"
    a: "Sometimes. If the toggle is on but nothing changes visually, the schedule or state keys under the CloudStore registry hive may be stuck — deleting those keys and toggling Night Light off and back on resets its state. Back up the key before editing."
  - q: "Does HDR break Night Light?"
    a: "Yes, on some ARM panels enabling HDR overrides or conflicts with Night Light's color-temperature filter, so the warm tint never appears. Turning HDR off in Settings > System > Display is a quick way to test this conflict."
  - q: "Will Night Light work over an external monitor?"
    a: "Usually yes, but some external monitors and docks apply their own color profiles that fight the filter, and certain display drivers only apply Night Light to the internal panel. Test with the internal display alone to isolate the cause."
---

You flip on Night Light at 9 PM and… nothing. The screen stays icy blue, the toggle greys out, or the schedule you set never fires. On x86 machines this is usually a driver hiccup; on Windows 11 on ARM Copilot+ PCs, the color-temperature pipeline runs through the Adreno display driver in ways that make Night Light more fragile than it looks.

Night Light works by asking the display driver to shift the color temperature of the rendered frame. When the ARM graphics driver is generic, corrupted, or fighting a custom color profile, Windows silently fails — the toggle may even stay "on" while the screen never warms. This is the same driver-exposure problem that breaks other display-stack features on the platform.

This guide gives you six fixes in technician order: quick toggles and schedule checks first, then driver repair, then registry and profile-level repair. Work through them in sequence and test the filter after each step.

## Why this happens

- **Generic or corrupted ARM display driver:** The most common cause — Night Light needs the driver to expose color-temperature control, and a generic Microsoft Basic Display Adapter driver or a half-installed Adreno package simply doesn't.
- **Stuck Night Light state in the registry:** The schedule and on/off state live in the CloudStore registry hive; when those values corrupt, the toggle can show "on" while the filter never applies.
- **HDR overriding the filter:** On some ARM panels, enabling HDR takes over the color pipeline and Night Light's warm shift is silently discarded — the two features conflict at the driver level.
- **Conflicting color profile:** A custom ICC color profile from the laptop maker or a calibration tool can override Night Light's temperature shift, so the filter applies and then gets overwritten.
- **Schedule misconfiguration:** Night Light set to "sunset to sunrise" depends on location services; if location is off or the timezone is wrong, the schedule fires at the wrong times or never.
- **External monitor or dock in the chain:** Some docks and external displays apply their own color processing, and the ARM driver may only apply Night Light to the internal panel.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle it cleanly and check the schedule

Before assuming driver trouble, verify Night Light isn't just misconfigured. A surprising number of "not working" reports are a schedule that never fires or a toggle stuck in a half-state.

1. Open **Settings > System > Display > Night light** and turn the toggle **Off**, wait ten seconds, then turn it **On** — watch for any color shift.
2. Drag the **Strength** slider to 100 temporarily; at low strength the effect is subtle enough to miss, especially on already-warm OLED panels.
3. Set the schedule to **Set hours** with a test window covering the current time (e.g., 8 AM to 11 PM) to see if it engages on a manual schedule.
4. If you prefer sunset-to-sunrise, confirm **Settings > Privacy & security > Location > Location services** is on — the schedule needs your location to compute sunset.
5. Restart the Settings app and recheck; if the toggle is greyed out entirely, skip ahead to the driver fixes — no schedule tweak will help a greyed toggle.

### Fix 2: Reinstall the OEM ARM display driver

A greyed-out or dead Night Light toggle on an ARM laptop points at the display driver nine times out of ten. This is the same class of driver-exposure failure that breaks hardware features across the platform — [NPU features fail the same way](/articles/ollama-npu-not-working-windows/) when the wrong driver stack is in place.

1. Open **Device Manager > Display adapters** and check the listed device — "Microsoft Basic Display Adapter" means no real driver is loaded and Night Light cannot work.
2. Note your exact model from **Settings > System > About**, then download the latest Windows 11 on ARM graphics driver from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Run the installer as administrator, let it finish without sleep or interruption, and restart when prompted.
4. After reboot, recheck the Night Light toggle — it typically returns to full function the moment the proper Adreno driver loads.
5. If Windows Update later replaces the driver with a generic one, use the "show or hide updates" approach documented on [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) to block that specific driver.

### Fix 3: Disable HDR and remove conflicting color profiles

If the driver is correct but the warm tint still never appears, something downstream is overriding it. HDR and custom ICC profiles are the two usual suspects, and both are easy to test.

1. Open **Settings > System > Display > HDR** and toggle it **Off**, then test Night Light again immediately.
2. If the filter now works, you have the HDR conflict — keep HDR off for evening use or accept the tradeoff, since the two fight at the driver level on affected panels.
3. Open **Settings > System > Display > Advanced display > Display adapter properties**, go to the **Color Management** tab, and check the **ICC profiles** assigned to the display.
4. Remove or disable any third-party calibrated profile and revert to the system default (sRGB) profile, then test Night Light.
5. Some OEM utilities (including [audio-tuning apps with their own display hooks](/articles/myasus-ai-noise-cancellation-problems/)) install display "enhancement" profiles — disable those enhancements and retest.

### Fix 4: Reset Night Light's registry state

When the toggle is on but the screen never warms, the CloudStore state can be stuck. Deleting the Night Light keys forces Windows to rebuild them cleanly on the next toggle.

1. Press **Win + R**, type `regedit`, and navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Current`.
2. Look for subkeys starting with `$$windows.data.bluelightreduction` — there are usually two (settings and state).
3. Right-click each and **Export** it as a backup, then **Delete** both keys.
4. Sign out and back in (or restart), then open **Settings > System > Display > Night light** and toggle it on — Windows rebuilds the keys fresh.
5. If the filter now engages, reconfigure your preferred strength and schedule; the corruption is gone.

### Fix 5: Rule out the external monitor and dock

Night Light applies per display, and the ARM graphics driver doesn't always apply it to external outputs — especially through docks that do their own color processing.

1. Disconnect all external monitors and docks, then test Night Light on the internal panel alone.
2. If it works internally but not on the external display, the limitation is the dock/monitor chain — check the monitor's own menu for a built-in blue-light or "eye care" mode as a substitute.
3. Reconnect the dock and check whether the monitor appears in **Settings > System > Display** with its own Night Light behavior; some configurations need the filter toggled per display.
4. Update the dock's firmware if the maker provides one — display-output firmware affects color-pipeline features.
5. As a workaround for a stubborn external display, use the monitor's hardware low-blue-light preset in the evenings — similar per-app display quirks affect [creative tools on ARM](/articles/unity-editor-arm-windows-issues/) and are handled the same pragmatic way.

### Fix 6: Repair Windows' display components

If nothing above works on the internal panel with a correct driver, the OS-side display stack itself may be damaged — rare, but it happens after interrupted updates.

1. Open an elevated Terminal (**Win + X > Terminal (Admin)**) and run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, and restart.
2. After reboot, toggle Night Light off and on once more and test with the strength slider at maximum.
3. Check **Settings > Windows Update** for any pending optional driver updates for the display and install them.
4. Create a fresh local user account temporarily and test Night Light there — if it works in the new profile, your main profile's settings store is damaged and migrating to a new profile is the clean fix.
5. As a last resort, use **Settings > System > Recovery > Reset this PC** with **Keep my files** — this rebuilds the display stack while preserving your data.

## Closing

Night Light failing on an ARM laptop is almost always the display driver not exposing color-temperature control, or HDR and color profiles fighting the filter downstream. Reinstall the OEM Adreno driver first, kill HDR and custom profiles second, and reset the registry state third — one of those three restores the warm glow in nearly every case.
