---
title: "Laptop Speakers Not Working? Step-by-Step Fix Guide"
slug: how-to-fix-laptop-speakers-not-working-step-by-step
date: 2026-09-02
categories: ["drivers"]
tags: ["laptop speakers", "no sound", "audio driver", "realtek", "troubleshooting"]
description: "Fix laptop speakers not working step by step: check output routing, restart audio services, and reinstall the audio driver on any Windows laptop."
thumbnail: "/images/thumbs/how-to-fix-laptop-speakers-not-working-step-by-step.webp"
faqs:
  - q: "Why are my laptop speakers not working but headphones are?"
    a: "The speaker hardware or its specific driver endpoint binding is at fault while the codec itself works. Reinstall the audio driver from your laptop maker's site, check the speaker balance settings, and if it persists across a Linux live USB test, the internal speakers likely need service."
  - q: "How do I reinstall my laptop's audio driver?"
    a: "In Device Manager, under Sound, video and game controllers, uninstall the audio device with the 'remove driver' option checked, then use Action > Scan for hardware changes and reboot. For best results, install the Audio driver package from your laptop manufacturer's support site instead of the generic Windows driver."
  - q: "Why is there a red X on my speaker icon?"
    a: "Windows found no working audio output — the driver failed or the audio service stopped. Restart the Windows Audio services in services.msc first, then check Device Manager for a warning on the audio device and reinstall the driver if needed."
  - q: "Can Windows Update break my laptop speakers?"
    a: "Yes — it is one of the most common triggers for speaker silence. Windows Update replaces the manufacturer's tuned audio driver with a generic one that may not drive your speakers correctly. Reinstall the maker's audio package, then set Device Installation Settings to not auto-install drivers to prevent repeats."
---

Laptop speakers that produce no sound are a routing problem until proven otherwise. Windows maintains a surprisingly complex audio path — default device selection, per-app volumes, enhancement pipelines, driver bindings, services — and a break at any point produces identical silence. The step-by-step approach below checks each point in signal order, so you find the break instead of guessing.

This guide is brand-neutral and works on Dell, HP, Lenovo, Acer, and ASUS laptops running Windows 10 or 11. You'll need no tools and no disassembly — just Settings, Device Manager, and ten focused minutes.

Follow the steps in order. Step 1 alone catches the most common cause.

As you work through the steps, keep one diagnostic distinction in mind: silence from all sources — system sounds, browser, media player — points to the driver or service layer, while silence from one app points to per-app routing or mixer settings. That distinction tells you within seconds whether you are fixing Windows or fixing an app.

## Why this happens

- **Wrong default output device:** Audio routed to a disconnected HDMI monitor, USB headset, or Bluetooth device while speakers sit idle.
- **Muted or zeroed volume layers:** Master mute, per-app mixer mute, or the physical mute key — three independent mutes that all produce silence.
- **Windows Audio service stopped:** Dead audio services = no sound regardless of driver health.
- **Broken audio driver binding:** Post-update driver failures leaving the device in an error state.
- **Enhancement pipeline crash:** OEM audio APOs (MaxxAudio, Dolby, DTS) crashing and muting the chain.
- **BIOS audio disabled:** Firmware-level audio toggle flipped off.
- **Speaker hardware failure:** Blown speakers or loose internal connectors — least common, tested last.
- **App-specific output routing:** Individual apps pinned to a disconnected device in the advanced volume mixer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify output device and all mute layers

Signal routing first — the most common cause lives here.

1. Click the taskbar speaker icon: confirm output is **Speakers** (your laptop's), not HDMI/USB/Bluetooth, and volume is up.
2. Press the laptop's physical **mute key** (often F1/F4 with a speaker icon) — toggle it twice and watch the on-screen indicator.
3. Right-click speaker icon → **Volume mixer**: check the master and per-app sliders — a muted browser is not a broken speaker.
4. **Settings → System → Sound**: confirm the Output device dropdown shows the internal speakers.

### Fix 2: Restart the Windows audio services

Clear a stalled audio engine.

1. **Win + R → services.msc**: set **Windows Audio** and **Windows Audio Endpoint Builder** to **Automatic**, then **Restart** both.
2. Test sound immediately after the restart.
3. If sound returns then dies again later, a third-party app is crashing the service — note what you launched in between.

### Fix 3: Run the built-in audio troubleshooter

Let Windows check its own configuration.

1. **Settings → System → Sound → Troubleshoot** (Windows 11) or **Settings → Update & Security → Troubleshoot → Playing Audio** (Windows 10).
2. Apply whatever it recommends, then retest.
3. It commonly catches disabled devices and wrong defaults you'd otherwise hunt manually.

### Fix 4: Reinstall the audio driver

The core repair for driver-level silence.

1. **Device Manager → Sound, video and game controllers** → right-click your audio device (**Realtek(R) Audio** or similar) → **Uninstall device** (check **Attempt to remove the driver**).
2. **Action → Scan for hardware changes**; reboot.
3. If Windows installs a generic driver that still fails, get the **Audio** driver from your laptop maker's support site (Dell: [Dell support](https://www.dell.com/support); HP: [HP support](https://support.hp.com/us-en); Lenovo: [Lenovo support](https://support.lenovo.com/us/en/)) and install that instead.
4. Retest with the built-in speakers as the output device.

### Fix 5: Disable enhancements and test the raw path

Bypass the enhancement pipeline to isolate APO crashes.

1. **Sound settings → More sound settings** → double-click **Speakers → Enhancements** → check **Disable all enhancements**.
2. If sound returns, an OEM enhancer (MaxxAudio/Dolby/DTS) was crashing the chain — reinstall the maker's full audio package to re-register it cleanly.
3. **Advanced** tab: set **24 bit, 48000 Hz**; test again.
4. See our [MaxxAudio repair guide](/articles/how-to-fix-waves-maxxaudio-not-working-in-windows-11-24h2/) if that APO is your culprit.

### Fix 6: Check BIOS audio and test headphones

Separate firmware, speakers, and codec.

1. Reboot into BIOS/UEFI and confirm **Integrated Audio** is **Enabled**.
2. Plug in wired headphones: sound in headphones = speaker hardware or speaker-endpoint binding; silence in both = driver/codec level.
3. Boot a Linux live USB: sound there = Windows problem; silence there too = hardware.

### Fix 7: Prevent recurrence

Lock in the working state.

1. **Device Installation Settings → No** so Windows Update doesn't swap your working audio driver for a generic one.
2. Save the working audio installer from your maker's site.
3. After major Windows updates, verify speaker output before assuming everything survived.

### Fix 8: Check per-app routing and spatial sound

When most apps have sound but one is silent — or vice versa — the fault is in Windows' per-app routing, not the driver.

1. Open **Settings → System → Sound → Volume mixer** and check each app's **Output device** — an app pinned to a disconnected device stays silent while everything else works.
2. Set any misrouted app back to **Default**.
3. In speaker **Properties**, check the **Spatial sound** tab and set it to **Off** — broken spatial processing can mute output on some drivers.
4. Turn off **Mono audio** (Settings → Accessibility → Audio) unless you need it; it can interact badly with certain enhancement pipelines.

## Closing

Speaker silence is a signal-path problem, and signal paths are debugged in order: routing, mutes, services, driver, enhancements, firmware, hardware. Most cases end at Step 1 (wrong output device) or Step 4 (driver reinstall) — the exotic causes are exotic precisely because they're rare. The headphone test is your circuit breaker: it tells you whether to keep working software or start thinking about speaker hardware. For crackling rather than silence, see [speakers crackling on laptop](/articles/how-to-fix-speakers-crackling-on-laptop-in-windows-11-24h2/).
