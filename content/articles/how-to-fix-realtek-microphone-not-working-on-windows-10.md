---
title: "Realtek Microphone Not Working on Windows 10? Try These Fixes"
slug: how-to-fix-realtek-microphone-not-working-on-windows-10
date: 2026-09-24
categories: ["drivers"]
tags: ["realtek microphone", "windows 10", "mic not working", "audio driver"]
description: "Realtek mic silent on Windows 10? Work through privacy settings, recording-device checks, and driver repairs to restore microphone input."
thumbnail: "/images/thumbs/how-to-fix-realtek-microphone-not-working-on-windows-10.webp"
faqs:
  - q: "Why does my mic not work in apps but tests fine in Windows?"
    a: "That split means the signal reaches Windows but apps are blocked — almost always the microphone privacy settings. Go to Settings, then Privacy, then Microphone, and confirm both the master toggle and the per-app permissions are on. Windows 10 updates reset these regularly, so a mic that worked last week can go app-silent overnight with no driver problem at all."
  - q: "How do I make the internal mic the default recording device?"
    a: "Right-click the speaker icon, choose Sounds, open the Recording tab, right-click the Realtek microphone or mic array, and choose Set as Default Device (and Default Communication Device). Windows 10 sometimes leaves a disconnected headset as the default, so every app listens to a device that is not there."
  - q: "What should the microphone level be set to?"
    a: "In the Recording tab, open the mic's Properties, then Levels: set the main level to 70-90 and the Microphone Boost to +10 or +20 dB if the input is quiet. Levels near zero or a muted speaker icon are a common post-update state. Adjust while watching the green level bar — you want it peaking in the upper-middle when speaking normally."
  - q: "Do I need the manufacturer's Realtek driver on Windows 10?"
    a: "For reliable microphone capture, yes. The vendor's Realtek package includes the matched capture components and the audio console for jack and array configuration. Generic Windows drivers often handle playback fine while the mic input misbehaves — the classic speakers-work-mic-doesn't split is frequently a generic-driver symptom."
---

Nobody can hear you. The mic level bar in the Recording tab barely twitches, Teams shows no input, and the voice recorder produces silence — while the speakers play perfectly and Device Manager reports everything healthy.

On Windows 10, mic diagnosis starts in the classic **Sound** control panel's **Recording** tab: the green level bar next to the Realtek mic is the ground truth. Bar moves but apps hear nothing — privacy problem. Bar flat — device, mute, or driver problem. That one observation aims the whole repair. (Windows 11 moved these screens around — see our [Windows 11 mic guide](/articles/how-to-fix-realtek-microphone-not-working-on-windows-11/) for that layout.)

## Why this happens

- **Privacy permissions reset by an update.** Apps are blocked while Windows itself hears the mic.
- **Wrong default recording device.** A disconnected headset remains the default input.
- **Mic muted or level at zero.** Post-update state with no visible error.
- **Realtek capture path corrupted.** Driver update broke input while output survived.
- **Enhancements blocking the signal.** Broken noise-suppression APO gates the mic.
- **Exclusive mode held by an app.** One program seizes the mic and starves the rest.
- **Jack misdetected.** The Realtek console classified a plugged mic as line-in or headphones.
- **Stereo Mix or disabled device confusion.** The wrong capture endpoint is active.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set the right default in the Recording tab

Right-click the speaker icon in the taskbar and choose **Sounds**, then open the **Recording** tab. Right-click in the empty area and check **Show Disabled Devices** and **Show Disconnected Devices**. Find your **Microphone (Realtek)** or mic array, right-click it, choose **Enable** if needed, then **Set as Default Device** and **Set as Default Communication Device**. Speak and watch the green bar — it should bounce. If the bar moves here, Windows hears the mic; any remaining problem is permissions or app settings (Fix 3).

### Fix 2: Fix levels and unmute

With the mic selected in the Recording tab, click **Properties**, open the **Levels** tab, and drag **Microphone** to 80 and **Microphone Boost** to **+20 dB** if input is faint. Make sure the speaker icon next to the level is not muted (no red circle). Click **Apply** and speak — the green bar should now peak healthily. Updates routinely reset levels to near-zero or muted with no notification, and this silent reset is behind a remarkable number of "mic suddenly dead" reports.

### Fix 3: Check Windows 10 microphone privacy

Go to **Settings > Privacy > Microphone**. Turn on **Allow apps to access your microphone**, and scroll the app list to allow your specific apps (Teams, Zoom, browsers). Also check **Allow desktop apps to access your microphone** at the bottom — classic Win32 conferencing apps need this separate toggle. This is the fix for the "bar moves in Recording tab, apps hear nothing" pattern. Toggle the master switch off and on once to force Windows to re-register permissions.

### Fix 4: Disable enhancements and exclusive mode

In the mic's **Properties** (Recording tab), open the **Enhancements** tab and check **Disable all sound effects**. On the **Advanced** tab, uncheck **Allow applications to take exclusive control of this device** and set the default format to **2 channel, 16 bit, 44100 Hz (CD Quality)** — exotic sample rates from a broken driver can silence capture. Click Apply and retest. Enhancement APOs damaged by driver updates are a genuine cause of gated mic signals, and exclusive-mode conflicts produce the "works in one app, dead in all others" symptom.

### Fix 5: Reinstall the Realtek driver

Open **Device Manager**, expand **Sound, video and game controllers**, right-click the Realtek device, choose **Uninstall device**, and check **Delete the driver software for this device** if offered. Also check **Audio inputs and outputs** for the mic entry. Restart — Windows reinstalls on boot. Then install the vendor's **Realtek audio driver** for your exact model from [Lenovo support](https://support.lenovo.com/us/en/), [Dell support](https://www.dell.com/support), or [HP support](https://support.hp.com/us-en) for the matched capture components. Restart again, re-verify the default device and levels, since a fresh driver can reset them.

### Fix 6: Configure the Realtek HD Audio Manager

Open **Realtek HD Audio Manager** (or Realtek Audio Console) from the Control Panel or Start menu. For a plugged-in mic, confirm the front/rear jack is classified as **Mic In** — reassign it if the manager guessed wrong. Check the **Microphone** tab for array-vs-jack selection and any noise-suppression toggles that might be gating input. On some Lenovo and Dell models this manager is the actual authority over which physical input is live, and its settings persist across driver reinstalls — a stale misconfiguration here survives every driver fix until corrected.

### Fix 7: Rule out hardware with a cross-test

Plug in a USB headset or basic earbud mic and test: if the external mic works but the internal array never does — across driver versions and with correct settings — the array's cable or the codec's capture path is faulty. Test the internal mic in the BIOS diagnostics if your brand offers them. If no microphone works on any input including USB, and a Linux live USB also hears nothing, the audio codec hardware needs service. But exhaust the software side first — genuine mic hardware failure is uncommon compared to privacy and driver causes.

## Closing

Windows 10 mic repair is a two-question diagnosis: does the Recording tab's green bar move, and do apps have permission? Answer those, fix the matching half — levels and drivers for a flat bar, privacy toggles for a moving one — and the mic comes back. If the speakers are crackling, cutting out, or the driver itself keeps crashing, our [Realtek audio driver guide](/articles/realtek-audio-driver-not-working-windows-11/) addresses the broader playback-side driver problem in detail. Make the Recording tab check a habit after updates; it takes ten seconds and catches most mic regressions immediately. Future you will be genuinely grateful.
