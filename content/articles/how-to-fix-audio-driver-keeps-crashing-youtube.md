---
title: "How to Fix an Audio Driver That Keeps Crashing"
slug: how-to-fix-audio-driver-keeps-crashing-youtube
date: 2026-09-21
categories: ["drivers"]
tags: ["audio driver", "sound crashing", "realtek audio", "no sound", "driver crash"]
description: "Audio driver keeps crashing or sound cuts out? Fix Realtek and Windows audio driver crashes with clean reinstalls, enhancement tweaks, and service resets."
thumbnail: "/images/thumbs/how-to-fix-audio-driver-keeps-crashing-youtube.webp"
faqs:
  - q: "Why does my audio driver crash randomly?"
    a: "Random audio crashes usually come from a corrupted driver installation, conflicting audio enhancements, or a Windows update that installed an incompatible driver version. Power management suspending the audio device and third-party audio software fighting for exclusive control are the other common triggers. A clean driver reinstall fixes the majority of cases."
  - q: "Should I disable audio enhancements to stop crashes?"
    a: "Yes, this is one of the highest-yield troubleshooting steps. Enhancements like bass boost, virtual surround, and loudness equalization run inside the driver, and buggy enhancement modules are a classic crash source. Disabling all enhancements in the device properties stabilizes the driver immediately for many users."
  - q: "Can Windows Update break my audio driver?"
    a: "Frequently. Windows Update routinely replaces manufacturer-tuned audio drivers with generic versions that crash on specific hardware, particularly Realtek codecs with custom laptop configurations. If crashes started right after an update, roll back the driver or reinstall the manufacturer's version and block the update from replacing it."
  - q: "What does restarting Windows Audio services actually fix?"
    a: "Restarting the Windows Audio and Windows Audio Endpoint Builder services clears corrupted audio session state and hung audio graphs without touching drivers. It fixes crashes caused by stuck exclusive-mode streams and failed device transitions, like unplugging headphones mid-playback. It is a quick, safe first step worth trying before driver surgery."
---

An audio driver that keeps crashing announces itself unmistakably: sound cuts out mid-video, the speaker icon shows a red X, applications freeze when they touch audio, or the dreaded "audio device has crashed" state where nothing plays until a reboot. The underlying cause is almost always in the driver layer — corrupted installs, bad updates, or enhancement modules misbehaving — rather than in your speakers.

The repair order here matters. Quick service-level resets come first because they're instant and safe, then enhancement and format tweaks, then the clean driver reinstall that resolves the stubborn cases. Keep your laptop maker's audio driver downloaded before you start uninstalling anything.

## Why this happens

- **Corrupted driver installation:** Partial updates and interrupted installs leave the audio driver in a half-working state that crashes under load.
- **Windows Update driver swap:** Updates replace tuned manufacturer audio drivers with generic versions that crash on specific Realtek/Conexant codec configurations.
- **Buggy audio enhancements:** Bass boost, virtual surround, and "smart" volume features run as driver modules; a buggy one crashes the whole driver.
- **Exclusive mode conflicts:** Apps grabbing exclusive audio control (games, DAWs, conferencing tools) can crash drivers that handle the handoff poorly.
- **Power management suspending audio:** The OS suspending the audio device to save power can crash drivers that don't resume cleanly.
- **Sample rate/format mismatches:** Forcing an unsupported bit depth or sample rate can destabilize marginal drivers, especially over Bluetooth and HDMI.
- **Conflicting third-party audio software:** Virtual audio cables, old equalizer apps, and uninstalled-but-lingering audio tools fight the real driver.
- **Failing audio hardware:** Rare, but a dying codec chip produces crashes that no driver reinstall fixes — distinguishable because crashes happen in Safe Mode and Linux live USBs too.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the Windows Audio services

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Audio**, right-click, and choose **Restart**.
3. Find **Windows Audio Endpoint Builder**, right-click, and choose **Restart**.
4. Test playback immediately. If sound returns, the crash was session state, not a broken driver.
5. If the services refuse to restart or crash again instantly, continue to driver fixes — but this two-minute step resolves a real share of "audio died" reports, the same quick reset used in [general audio crash troubleshooting](/articles/audio-driver-keeps-crashing-troubleshooting/).

### Fix 2: Disable all audio enhancements

1. Right-click the speaker icon → **Sound settings**, then click your output device and open **Properties** (or **More sound settings → Playback → Properties**).
2. Go to the **Enhancements** tab and check **Disable all enhancements** (on some systems it's labeled "Disable all sound effects").
3. Click Apply and test with a video or music for several minutes.
4. If crashes stop, re-enable enhancements one at a time to identify the culprit — then leave that one off permanently.
5. Realtek's control panel has its own separate effects section; disable those too if the Windows toggle doesn't cover them.

### Fix 3: Change the default format to a safe baseline

1. In the output device **Properties → Advanced** tab, look at **Default Format**.
2. Set it to **16 bit, 44100 Hz (CD Quality)** or **16 bit, 48000 Hz (DVD Quality)** — the most universally stable settings.
3. Uncheck both **Exclusive Mode** options ("Allow applications to take exclusive control" and "Give exclusive mode applications priority").
4. Apply and test. Exclusive mode handoffs crash fragile drivers; disabling them costs nothing for normal playback.
5. Only raise the format back up after stability is confirmed — and if crashes return at 24-bit/192kHz, your driver simply can't handle it reliably.

### Fix 4: Reinstall the audio driver from the manufacturer

1. Download the audio driver for your exact model from [Dell Support](https://www.dell.com/support) or [HP Support](https://support.hp.com/us-en).
2. In Device Manager, expand **Sound, video and game controllers**, right-click your audio device (Realtek Audio, Conexant, etc.), and choose **Uninstall device**, checking **Attempt to remove the driver for this device**.
3. Restart — Windows will load a basic driver — then install the manufacturer's package.
4. Restart again and test thoroughly, including sleep/wake cycles, which is when marginal drivers most often crash.
5. Manufacturer audio drivers include codec customizations the generic Windows driver lacks; this is why the [dedicated audio crash fix](/articles/best-way-to-fix-audio-driver-keeps-crashing/) leads with the same step.

### Fix 5: Roll back a driver broken by Windows Update

1. In Device Manager, open the audio device **Properties → Driver** tab.
2. If **Roll Back Driver** is available, click it and select a reason — this restores the pre-update driver that was working.
3. Restart and verify stability over a day of normal use.
4. To prevent recurrence, use **Device Installation Settings** (System Properties → Hardware) to stop automatic driver downloads, or hide the specific update.
5. If rollback is greyed out, the old driver wasn't preserved — do the clean manufacturer reinstall from Fix 4 instead.

### Fix 6: Disable power management on the audio device

1. In Device Manager, find your audio device under **Sound, video and game controllers** and open **Properties → Power Management** (if the tab exists).
2. Uncheck **Allow the computer to turn off this device to save power**.
3. Also check **System devices** for **High Definition Audio Controller** entries and disable power management there.
4. In **Power Options → Advanced**, look for any audio or PCI Express power settings set to aggressive saving and relax them.
5. Test with sleep/wake cycles. Drivers that crash specifically after the laptop sleeps are almost always victims of bad power-state handling.

### Fix 7: Remove conflicting third-party audio software

1. Open **Settings → Apps** and uninstall old equalizers, virtual audio devices, and audio "boosters" you no longer use.
2. In Device Manager with hidden devices shown, remove greyed-out ghosts of uninstalled audio devices.
3. Check **Startup** apps (Task Manager) for audio utilities launching at boot and disable the ones you don't need.
4. Restart and test. Lingering filter drivers from uninstalled audio software are a notorious hidden crash cause.
5. Reinstall only the audio tools you actively use, one at a time, testing stability between each.

### Fix 8: Test in a clean state to rule out hardware

1. Boot into **Safe Mode** and test audio (basic Windows audio works in Safe Mode).
2. If audio is stable in Safe Mode but crashes in normal mode, a third-party driver or startup program is the cause — use **msconfig** to do a clean boot and bisect the culprit.
3. As a stronger test, boot a Linux live USB and play audio there. Stable audio in Linux with crashes in Windows confirms a Windows driver problem, not hardware.
4. If audio crashes in Safe Mode AND Linux, the codec hardware is likely failing — that's a motherboard-level repair.
5. For persistent Windows-only crashes after all fixes, consider the [Microsoft support resources](https://support.microsoft.com/en-us/windows) for the audio troubleshooter as a final automated pass before concluding hardware failure.

## Closing

Audio driver crashes are a driver-hygiene problem: corrupt installs, bad updates, crashing enhancement modules, and power management that the driver can't handle. The service restart and enhancement disable are your fast wins; the clean manufacturer reinstall is your definitive fix. When crashes survive Safe Mode and a Linux live test, stop reinstalling drivers — the hardware itself is telling you something.
