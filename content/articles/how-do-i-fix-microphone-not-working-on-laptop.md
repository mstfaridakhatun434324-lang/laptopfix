---
title: "Microphone Not Working on Your Laptop? Here's the Fix"
slug: how-do-i-fix-microphone-not-working-on-laptop
date: 2026-09-05
categories: ["drivers"]
tags: ["microphone", "mic not working", "audio input", "privacy settings"]
description: "Laptop microphone not picking up sound? Diagnose and fix mic failures from privacy settings to drivers, step by step."
thumbnail: "/images/thumbs/how-do-i-fix-microphone-not-working-on-laptop.webp"
faqs:
  - q: "Why is my laptop mic not working in Zoom or Teams but works elsewhere?"
    a: "That's an app-permission or app-settings issue, not a broken mic. The conferencing app may have the wrong input device selected, or Windows granted it mic access while the in-app device picker points at a disconnected headset. Check the app's audio settings first, then Windows' per-app microphone permissions — the system-level mic is usually fine."
  - q: "Windows privacy settings keep blocking my microphone. How do I fix it permanently?"
    a: "Go to Settings > Privacy & security > Microphone and turn on both the master 'Microphone access' toggle and 'Let apps access your microphone.' Windows feature updates sometimes reset these. Also check 'Let desktop apps access your microphone' at the bottom — classic Win32 apps like older conferencing tools need that separate toggle, and it's easy to miss."
  - q: "My mic is detected but the volume is extremely low. What helps?"
    a: "Open Sound settings > Input > your microphone > and raise the input volume, then check the Levels tab in the legacy Sound control panel for the Microphone Boost slider — +10 to +20 dB usually fixes faint mics. Also disable 'audio enhancements' for the input device, which can suppress quiet speech, and make sure you're speaking toward the mic holes near the webcam."
  - q: "Could a driver update have killed my microphone?"
    a: "Yes — audio driver updates are a classic mic killer because the input path depends on the same Realtek or Intel audio driver as the speakers. If the mic died right after an update, roll the audio driver back in Device Manager or reinstall the manufacturer's audio package, which restores the full input chain including the mic array processing."
---

Nobody notices the microphone until the meeting starts. Then it's "we can't hear you," the frantic unmute-checking, and the slow realization that the laptop's mic has quietly stopped working — in every app, or just one, or only since yesterday's update. Microphone failures are disorienting because the causes span three unrelated systems: Windows privacy permissions, the app's own device selection, and the audio driver.

The diagnostic shortcut is the input level meter in **Settings > System > Sound > Input**: speak and watch. If the meter moves, Windows hears you and the problem is the app or its permissions. If it doesn't move, the problem is system-level — privacy, driver, or hardware. That one observation cuts the troubleshooting in half, so start there before changing anything.

This guide works from the meter outward: permissions and app settings first (the most common causes), then the driver layer, then hardware. For update-specific input failures, see the [microphone fix for Windows 11 24H2](/articles/how-to-fix-microphone-not-working-on-laptop-in-windows-11-24h2/).

## Why this happens

- **Microphone privacy access got turned off.** Windows updates and "privacy debloat" tools disable mic access globally or per-app — the mic is healthy, just gagged.
- **The wrong input device is selected.** With a headset, dock, or monitor connected, Windows or the app may be listening to a disconnected device while the built-in mic sits idle.
- **The audio driver broke the input path.** The microphone array rides the same Realtek/Intel audio driver as the speakers; a bad driver update kills input while output keeps working.
- **The app has its own device picker.** Zoom, Teams, and Discord each select an input independently of Windows' default — the system mic can be perfect while the app listens to nothing.
- **Microphone boost or levels got zeroed.** Driver reinstalls and updates sometimes reset input volume to near-zero — technically "working," practically silent.
- **The mic is muted at a hardware or function-key level.** Some laptops have a mic-mute **Fn key** or a physical shutter/kill switch; easy to trigger, easy to miss.
- **The mic array hardware failed.** Least common — usually after liquid damage or a screen replacement that disturbed the mic cable near the webcam.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Watch the input meter and check the physical mute

Establish the baseline before touching software.

1. Go to **Settings > System > Sound**, scroll to **Input**, select your microphone, and speak normally. If the blue level bar moves, Windows hears you — skip to Fix 3 (app-level). If not, continue here.
2. Check for a **mic-mute Fn key** (microphone icon on the function row) — press **Fn + that key** and watch for an on-screen mute indicator.
3. Some laptops (notably ThinkPads and HPs) have a **physical mic shutter or kill switch** — check the sides and the webcam area.
4. In the same Sound settings page, confirm the correct device is chosen under **Choose a device for speaking** — select the internal **Microphone Array** explicitly rather than leaving it on Default.

### Fix 2: Fix Windows microphone privacy permissions

The most common system-level cause, and the most overlooked.

1. Go to **Settings > Privacy & security > Microphone**.
2. Turn **Microphone access** ON (master toggle), then **Let apps access your microphone** ON.
3. Scroll down and enable access for the specific app that's failing (Teams, Zoom, browser, etc.).
4. Scroll further to **Let desktop apps access your microphone** and turn it ON — classic desktop apps need this separate toggle, and it's off by default after some updates. Microsoft documents the current permission layout on the [official Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 3: Set the right device in the app itself

When the Windows meter moves but the app hears nothing.

1. Open the app's audio settings (Zoom: Settings > Audio; Teams: Settings > Devices; Discord: Voice & Video).
2. Set the **input/microphone** explicitly to your internal mic or headset — never leave it on "Same as System" or "Default" while troubleshooting.
3. Use the app's **Test Mic** feature and speak — adjust until the app's own meter moves.
4. In browser-based apps (Google Meet), click the **lock/camera icon** in the address bar and confirm microphone permission is **Allowed** for the site — browser permission is separate from Windows permission.

### Fix 4: Raise input volume and microphone boost

For mics that are "working" but inaudible.

1. **Settings > System > Sound > Input** > select the mic > set **Volume** to 80–100 and speak — watch the meter.
2. For finer control: **More sound settings** > **Recording** tab > double-click the mic > **Levels** tab > set **Microphone** to 100 and **Microphone Boost** to **+10 dB** (try +20 dB if still faint).
3. On the **Enhancements** tab for the recording device, **disable all enhancements** — noise suppression can gate quiet speech into silence.
4. Speak toward the top bezel near the webcam — laptop mic holes are tiny and directional; talking at the keyboard halves your volume.

### Fix 5: Reinstall the audio driver package

When the meter doesn't move anywhere and permissions are correct, the driver is suspect.

1. In **Device Manager > Sound, video and game controllers**, right-click the audio device (Realtek/Intel) > **Uninstall device**, checking *Attempt to remove the driver*.
2. Install the **audio driver** for your exact model from the laptop maker's support site — the full OEM package, which includes the mic-array processing. This mirrors the approach in our [Realtek audio driver guide](/articles/realtek-audio-driver-not-working-windows-11/).
3. Reboot, then recheck the input meter in Sound settings before opening any app.
4. If a recent update caused it, use **Roll Back Driver** on the audio device first — faster than a full reinstall when the previous version is still on disk.

### Fix 6: Remove conflicting audio software

Something else may be holding the input device hostage.

1. **Device Manager > View > Show hidden devices** — uninstall ghost microphone entries from previously used headsets, docks, or virtual audio software (Voicemeeter, virtual cables).
2. Temporarily disable third-party "audio enhancer," noise-cancellation, or antivirus web-protection tools that hook the mic — test the meter with each disabled.
3. Check **Sound settings > Input** again after each removal; conflicting drivers often release the device the moment they're gone.
4. If you use a USB dock with audio, test the built-in mic with the dock disconnected — dock audio drivers are a frequent source of input conflicts.

### Fix 7: Verify hardware with an outside-OS test

The final verdict on the mic array itself.

1. Boot a **Linux live USB** and open its sound settings — if the input meter moves there, the hardware is fine and the fault is Windows software (revisit Fixes 2–5 knowing that).
2. If it's dead in Linux too, and there's no physical mute engaged, the mic array or its cable (routed through the display assembly on most laptops) has likely failed.
3. Check whether the failure followed a **screen replacement or drop** — the mic cable runs through the hinge area and is easily pinched during display service.
4. Practical workaround: a $15 USB headset or clip-on mic bypasses the internal array entirely and usually sounds better anyway — a reasonable permanent answer for an out-of-warranty machine.

## Closing

Microphone troubleshooting is really permission troubleshooting plus driver troubleshooting wearing a trench coat: the privacy toggles gag more mics than any hardware failure, and the audio driver carries the input path whether the speakers work or not. Watch the input meter, open the permissions, reinstall the OEM audio package — and the next meeting will hear you just fine.
