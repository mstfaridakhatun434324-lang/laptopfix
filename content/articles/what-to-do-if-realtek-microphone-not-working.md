---
title: "Realtek Microphone Not Working on Your Laptop? Here's What to Do"
slug: what-to-do-if-realtek-microphone-not-working
date: 2026-10-02
categories: ["drivers"]
tags: ["realtek microphone", "mic not working", "audio input", "windows 11", "microphone driver"]
description: "Realtek microphone not working on your laptop? Fix muted inputs, privacy settings, driver issues, and jack detection with this step-by-step guide."
thumbnail: "/images/thumbs/what-to-do-if-realtek-microphone-not-working.webp"
faqs:
  - q: "Why is my Realtek microphone not picking up any sound?"
    a: "The usual causes are the microphone being muted or disabled in Sound settings, Windows privacy settings blocking microphone access, or a corrupted Realtek driver after a Windows update. Less commonly, the wrong default input is selected (e.g., a webcam mic instead of the headset mic). Checking the input device selection and privacy toggles resolves most cases in minutes."
  - q: "How do I enable my Realtek microphone in Windows 11?"
    a: "Go to Settings → System → Sound → Input, and make sure the correct microphone is selected with its volume slider up. Then open Settings → Privacy & security → Microphone and confirm 'Microphone access' is on plus per-app access for the apps you use. Finally, in the classic Sound panel's Recording tab, right-click and enable 'Show Disabled Devices' in case the mic is hidden."
  - q: "Can Windows Update break the Realtek microphone?"
    a: "Yes — it's a classic trigger. Windows Update often replaces the laptop maker's Realtek driver package with a generic one that mishandles microphone arrays or jack detection. Reinstalling the audio driver from your laptop manufacturer's support site restores the correct behavior, and you can then manage driver updates to prevent recurrence."
  - q: "What if my microphone works in one app but not another?"
    a: "That's an app-permission or app-settings issue, not a driver problem. Check Windows Settings → Privacy & security → Microphone and make sure the specific app is allowed. Then open the app's own audio settings (Zoom, Teams, Discord all have them) and verify the correct input device is selected there — apps often default to the wrong mic after updates."
---

Your Realtek microphone was working yesterday. Today, Zoom hears silence, the voice recorder shows a flat line, and Windows insists everything is fine. Microphone failures are uniquely frustrating because the mic can be broken at four different layers — privacy settings, the app, Windows' sound stack, or the driver — and each layer happily reports 'working properly' while you get silence.
The fix order matters here more than most audio problems. Start with the two-minute checks (is the right input selected? is access allowed?), because a surprising number of 'dead mic' cases are just Windows' privacy toggle doing its job a little too well. If you also have headphone jack trouble, our [headphone detection guide](/articles/troubleshoot-laptop-not-detecting-headphones/) covers the shared Realtek plumbing.
Realtek drivers deserve special attention because Windows Update loves replacing them. If your mic died right after Patch Tuesday, skip straight to the driver reinstall — and afterward, our guide to [microphone issues on Windows 11](/articles/how-to-fix-microphone-not-working-on-laptop-in-windows-11-24h2/) has extra steps for the OS-level settings that trip people up.

## Why this happens

- **Microphone access blocked by privacy settings.** Windows 11's privacy toggles can silently deny every app access to the mic.
- **Wrong input device selected.** The laptop's mic array, a webcam mic, and a headset mic compete — Windows picks wrong, especially after updates.
- **Microphone muted or volume at zero.** The input volume slider can be dragged to zero by updates or audio utilities without any visible warning.
- **Microphone disabled in Sound settings.** Disabled recording devices are hidden by default, making the mic look absent rather than off.
- **Corrupted or replaced Realtek driver.** Windows Update swaps the OEM Realtek package for a generic driver that breaks mic array or jack detection.
- **App-level wrong device.** Zoom/Teams/Discord keep their own input selection and don't follow Windows' default.
- **Front jack detection failure.** For headset mics, the same jack-sensing logic that handles headphones must detect the mic pin — if it fails, the mic never appears.
- **Enhancement software interference.** Nahimic, Waves MaxxAudio, or Discord's noise suppression can mute or hijack the input stream.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify privacy settings and app permissions

Windows 11 blocks microphone access at the OS level by default in many configurations — no app can hear anything until you allow it.

1. Open Settings → Privacy & security → Microphone.
2. Turn ON 'Microphone access' (the master switch) and 'Let apps access your microphone.'
3. Scroll through the app list and enable access for each app you need (Zoom, Teams, browser, etc.).
4. Also enable 'Let desktop apps access your microphone' for traditional Win32 programs.
5. Retest with Windows' built-in Voice Recorder app — if it records, the OS layer is fine and the problem is app-specific.

### Fix 2: Select the correct input and unmute it

With multiple mics present, Windows routinely defaults to the wrong one — and the volume slider loves to reset itself to zero.

1. Open Settings → System → Sound → scroll to Input and select the microphone you actually want to use.
2. Drag the input volume slider up to at least 75 and speak — watch the 'Test your microphone' bar for movement.
3. Click the arrow next to the input device and confirm the format (e.g., 2 channel, 16 bit, 48000 Hz) is set.
4. In the classic Sound panel (More sound settings → Recording tab), right-click your mic → Properties → Levels, and make sure nothing is muted there either.
5. If the mic you want isn't listed, right-click → 'Show Disabled Devices' and enable it.

### Fix 3: Fix the app's own audio settings

When the mic works in Voice Recorder but not in Zoom, the app is overriding Windows' choice — this is app configuration, not a driver bug.

1. Open the problematic app's audio/voice settings (in Zoom: Settings → Audio; in Discord: User Settings → Voice & Video).
2. Change the input device from 'Default' to your specific microphone by name.
3. Disable the app's automatic input-volume adjustment and noise suppression temporarily for testing.
4. In Teams, check Settings → Devices and confirm the right mic is chosen — Teams is notorious for switching after updates.
5. Restart the app after changing settings; many apps only enumerate devices at launch.

### Fix 4: Reinstall the Realtek audio driver cleanly

The definitive fix for driver-level mic failures: remove the corrupted or generic driver and install the OEM package.

1. Open Device Manager (Windows + X) → 'Sound, video and game controllers.'
2. Right-click the Realtek device → Uninstall device, checking 'Attempt to remove the driver for this device.'
3. Also expand 'Audio inputs and outputs' and uninstall the microphone entries the same way.
4. Restart — Windows installs a basic driver on boot.
5. Download the audio driver for your exact model from your laptop maker's support site and install it; Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the generic audio troubleshooter as a supplement.

### Fix 5: Restore jack detection for headset microphones

Headset mics depend on the same jack-sensing as headphones — if the laptop doesn't know a headset is plugged in, the mic never appears.

1. Open Realtek Audio Console from the Start menu.
2. Verify the insertion popup is enabled and the jack is configured for 'Headset' (not 'Headphone') when you plug in.
3. Test with the headset fully seated — a partially inserted TRRS plug gives you audio out but no mic in.
4. Try a different headset to rule out a broken mic wire (the thinnest wire in the cable, and the first to snap).
5. Check our [headphone detection troubleshooting](/articles/troubleshoot-laptop-not-detecting-headphones/) if the jack itself seems dead — the fixes overlap heavily.

### Fix 6: Disable audio enhancements and third-party effects

Enhancement suites process the mic stream in real time; when they glitch, they output silence while reporting success.

1. In the mic's Properties → Enhancements tab (classic Sound panel), check 'Disable all enhancements.'
2. Open any installed audio utilities (Nahimic, Waves MaxxAudio, Realtek Audio Console effects) and turn off noise suppression and voice effects.
3. In Discord/Teams, disable Krisp or built-in noise suppression temporarily.
4. Retest with Voice Recorder — if the mic springs to life, re-enable effects one by one to find the offender.
5. Keep enhancements off permanently if you value reliability over processing; raw mic input is what most apps expect.

### Fix 7: Check for BIOS and chipset updates

On some laptops the mic array connects through the chipset or an Intel Smart Sound Technology bus that needs its own driver.

1. In Device Manager, expand 'System devices' and look for 'Intel Smart Sound Technology' entries with warning icons.
2. Update these via right-click → Update driver, or from your laptop maker's driver page.
3. Install the latest chipset driver for your model — audio DSP issues often ride along with chipset updates.
4. Check for a BIOS update mentioning audio or microphone fixes in its changelog.
5. As a final software step, run the built-in troubleshooter: Settings → System → Troubleshoot → Other troubleshooters → Recording Audio.

## Closing

Realtek microphone problems are almost always a settings or driver issue, not dead hardware. Work top-down — privacy, input selection, app settings, then the driver — and you'll have your voice back long before you start worrying about the microphone itself.
