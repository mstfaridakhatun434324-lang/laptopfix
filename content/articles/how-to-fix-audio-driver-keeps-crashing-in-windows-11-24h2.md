---
title: "How to Stop Your Audio Driver From Crashing on Windows 11 24H2"
slug: how-to-fix-audio-driver-keeps-crashing-in-windows-11-24h2
date: 2026-10-08
categories: ["drivers"]
tags: ["audio driver crashing", "realtek crash windows 11", "sound driver fix 24h2"]
description: "Audio driver keeps crashing on Windows 11 24H2? Fix looping Realtek and Waves crashes, restarts, and silent audio with these proven driver repairs."
thumbnail: "/images/thumbs/how-to-fix-audio-driver-keeps-crashing-in-windows-11-24h2.webp"
faqs:
  - q: "Why does my audio driver crash repeatedly on Windows 11 24H2?"
    a: "The 24H2 update changed how Windows handles audio driver power management, which clashes with older Realtek, Conexant, and Waves drivers. Enhancements like Waves MaxxAudio add another failure point. The crash loop usually ends once you install a 24H2-certified driver from your laptop maker."
  - q: "Will disabling audio enhancements stop the crashes?"
    a: "Often, yes. Enhancements run extra processing inside the audio driver, and unstable enhancement packs are the single most common crash trigger. Turn off all enhancements in the device properties first — it takes a minute and resolves a surprising number of recurring crashes."
  - q: "Is it safe to roll back the audio driver?"
    a: "Yes. Rolling back simply reinstalls the previous driver version Windows kept on disk. Your files and settings are untouched, and you can re-update later once a stable release exists. Use Device Manager's rollback option, which is built exactly for this situation."
  - q: "Does a clean driver reinstall delete my sound settings?"
    a: "It resets per-device settings like volume levels and enhancement toggles to defaults, but your files are safe. Take a screenshot of any custom equalizer settings first if you rely on them, then reinstall — the fresh driver state is worth the minor reconfiguration."
---

Your sound cuts out mid-call, the volume icon shows a red X, and a few seconds later audio returns — until the next crash ten minutes later. On Windows 11 24H2, this looping audio driver crash has become one of the most reported driver problems on laptops, especially machines running Realtek audio with Waves MaxxAudio or similar enhancement packs on top.

The crashes look like a hardware fault, but they are almost always a software conflict: the driver fights with 24H2's new power handling, an enhancement layer glitches, or a partial update leaves mismatched driver files. Work through the fixes below in order — most people stop the crashing permanently at Fix 2 or Fix 3.

## Why this happens

- **24H2 power-management changes:** Windows 11 24H2 altered how audio drivers enter low-power states, and older drivers crash when the system suspends and resumes them.
- **Unstable audio enhancements:** Waves MaxxAudio, Dolby, and vendor EQ packs inject processing into the driver stream; a buggy version crashes the whole stack.
- **Mismatched driver files:** A Windows Update that replaces some Realtek files but not others leaves a hybrid driver that faults under load.
- **Driver conflicts with Bluetooth audio:** The system audio driver and Bluetooth audio services can collide when switching output devices, triggering a crash.
- **Over-aggressive USB power saving:** For USB headsets and docks, selective suspend cuts power to the audio device mid-stream.
- **Corrupted driver cache:** Repeated failed updates accumulate bad entries in the driver store that resurface after every reinstall attempt.
- **Third-party audio software hooks:** VoIP apps, game overlays, and recording tools that hook the audio pipeline can destabilize an already fragile driver.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable all audio enhancements

Enhancements are the number-one crash trigger, and disabling them is instant and reversible.

1. Right-click the speaker icon in the taskbar and choose **Sound settings**.
2. Scroll to **Advanced** and click **More sound settings**.
3. In the **Playback** tab, double-click your default output device (usually **Speakers / Realtek Audio**).
4. Open the **Enhancements** tab and check **Disable all enhancements**. On some drivers this appears as a toggle on the **Advanced** tab.
5. Click **Apply**, then use the laptop normally for an hour.

If the crashes stop, the enhancement pack was the culprit. You can live without enhancements or reinstall a newer Waves/MaxxAudio package from your laptop maker's site later.

### Fix 2: Roll back to the pre-24H2 driver

If the crashes started right after the 24H2 update, the previous driver was working fine — go back to it.

1. Open **Device Manager** and expand **Sound, video and game controllers**.
2. Right-click your audio device and choose **Properties**, then the **Driver** tab.
3. Click **Roll Back Driver** and select a reason (for example, "previous version worked better").
4. Restart the laptop when prompted.

This restores the driver Windows kept before 24H2 replaced it. If the button is grayed out, move on to Fix 3 — Windows only keeps one rollback generation. After rolling back, consider pausing driver updates with our guide to [disabling automatic driver updates](/articles/best-way-to-disable-automatic-driver-updates/) so 24H2 does not reinstall the crashing version overnight.

### Fix 3: Clean-reinstall the audio driver from the manufacturer

A full wipe removes the mismatched files that cause repeat crashes.

1. Download the latest audio driver for your exact model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/) — vendor drivers, not the generic Realtek download.
2. In Device Manager, right-click the audio device and choose **Uninstall device**. Check **Attempt to remove the driver for this device**.
3. Restart the laptop. Windows will install a basic driver — that is fine for now.
4. Run the manufacturer's installer you downloaded and restart again.

Vendor packages include the correct enhancement integration for your machine, which is why they crash less than generic downloads. This is the fix that permanently resolves most 24H2 audio crash loops.

### Fix 4: Reinstall or repair the Waves MaxxAudio component

On Dell, HP, and many gaming laptops, Waves MaxxAudio is a separate app that hooks into the audio driver — and a broken one crashes constantly.

1. Open **Settings > Apps > Installed apps** and look for **Waves MaxxAudio** or **MaxxAudio Pro**.
2. If present, uninstall it, restart, and test your audio for a day without it.
3. If you want it back, download the newest MaxxAudio package from your laptop maker's driver page — not from Waves directly — and install it.

If crashes vanish after removing MaxxAudio, keep it off or stay on the vendor's version. Related: our walkthrough for [fixing Waves MaxxAudio when it stops working](/articles/best-way-to-fix-waves-maxxaudio-not-working/) covers the companion symptoms.

### Fix 5: Turn off USB selective suspend for external audio

For USB headsets, USB speakers, and docking-station audio, power saving is a classic crash source.

1. Open **Control Panel > Power Options** and click **Change plan settings** next to your active plan, then **Change advanced power settings**.
2. Expand **USB settings > USB selective suspend setting** and set both **On battery** and **Plugged in** to **Disabled**.
3. Click **Apply** and **OK**.

This stops Windows from cutting power to USB audio devices mid-stream, which the driver often misinterprets as a device failure and crashes trying to recover.

### Fix 6: Update the driver through Windows Update's optional updates

Sometimes the stable driver exists but only as an optional update Microsoft never installed automatically.

1. Go to **Settings > Windows Update > Advanced options > Optional updates**.
2. Expand **Driver updates** and look for anything audio-related (Realtek, Conexant, Waves, Intel Smart Sound).
3. Check the boxes, click **Download & install**, and restart.

Microsoft's Windows Update catalog also hosts these drivers directly if you prefer to search by hardware ID. Install one driver package at a time so you can tell which one fixed the crashes.

### Fix 7: Disable fast startup to stabilize driver loading

Fast startup keeps driver state cached between sessions, which can preserve a corrupted audio driver state across reboots.

1. Open **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
4. Shut down fully, then power on.

With fast startup off, every boot loads the audio driver fresh. If your [sound crackles or pops](/articles/best-way-to-fix-crackling-sound-on-laptop/) alongside the crashes, this fix often helps both symptoms since they share the same loading instability.

## Closing

Recurring audio driver crashes on 24H2 are frustrating because they interrupt everything, but they are rarely hardware failures. Disable enhancements first for immediate relief, then do a clean reinstall of the manufacturer's audio driver for the permanent fix — that combination resolves the crash loop on the vast majority of laptops.
