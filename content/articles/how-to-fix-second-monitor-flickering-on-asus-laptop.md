---
title: "Fix Second Monitor Flickering on an ASUS Laptop for Good"
slug: how-to-fix-second-monitor-flickering-on-asus-laptop
date: 2026-09-22
categories: ["drivers"]
tags: ["asus laptop", "second monitor", "flickering", "display driver", "hdmi"]
description: "Fix a flickering second monitor on an ASUS laptop: diagnose refresh-rate mismatches, GPU driver faults, and cable issues with this technician's step-by-step guide."
thumbnail: "/images/thumbs/how-to-fix-second-monitor-flickering-on-asus-laptop.webp"
faqs:
  - q: "Why does my second monitor flicker only on my ASUS laptop?"
    a: "Because the laptop's GPU driver negotiates the signal. Windows Update often replaces the ASUS-tuned driver with a generic one that mishandles refresh rates or adaptive sync on external panels. Reinstalling the exact driver build from ASUS support for your model resolves this in the majority of cases we see."
  - q: "Can a bad HDMI cable cause monitor flickering?"
    a: "Yes, and it is one of the most common causes. A cable rated below your resolution and refresh rate drops packets, which shows as intermittent flicker or sparkles. Always test with a short, certified Ultra High Speed HDMI or DisplayPort 1.4 cable before assuming a driver problem."
  - q: "Does refresh rate mismatch cause flicker on external monitors?"
    a: "Absolutely. If Windows sets 59 Hz on a panel expecting 60 Hz, or enables a mode the monitor barely supports, you get visible shimmer. Open Advanced display settings and lock the monitor to its native resolution and refresh rate, and disable HDR while testing."
  - q: "Should I disable G-Sync or FreeSync to stop flicker?"
    a: "If the flicker looks like brightness pulsing during games or video, yes. Adaptive sync on mismatched laptop-monitor pairs is a classic cause. Turn it off in the monitor's OSD menu first, then in NVIDIA Control Panel or AMD Software, and retest for several minutes."
---

A flickering second monitor turns productive work into a headache, literally. On ASUS laptops the problem almost always traces back to one of three things: the refresh rate the laptop negotiated with the monitor, a GPU driver that Windows replaced during an update, or a cable that cannot carry the signal cleanly. Pin down which one you have before changing anything else.

ASUS machines complicate this slightly because they ship with extra display tooling — Armoury Crate on ROG/TUF models, MyASUS on consumer lines, and Splendid color profiles — any of which can inject their own refresh-rate or color behavior. Start with the monitor itself: does the flicker appear only when the laptop drives it, or also when another device does? That one test splits the problem in half. You will also want to rule out [second monitor detection issues](/articles/how-to-fix-second-monitor-not-detected-windows-11-on-asus-laptop/) first if the display drops out entirely between flickers.

Work through the fixes below in order. Each one is a concrete test with a visible result, so you will know exactly which layer was broken.

## Why this happens

- **Refresh-rate mismatch:** The laptop may push 59 Hz while the monitor expects 60 Hz, or HDR may force a mode the panel handles badly. Even a 1 Hz disagreement can produce visible shimmer.
- **GPU driver replaced by Windows Update:** Windows loves to swap your ASUS-tuned NVIDIA/AMD/Intel driver for a generic one. The generic driver often lacks the OEM display quirks that keep external monitors stable.
- **Faulty or underspecified cable:** A cheap HDMI cable rated for 1080p will struggle at 1440p 144 Hz. The signal degrades into intermittent flicker, especially over longer runs.
- **Variable refresh rate confusion:** FreeSync/G-Sync enabled on a monitor paired with a laptop that negotiates it poorly causes brightness flicker during frame-rate changes.
- **Armoury Crate or Splendid interference:** ASUS display utilities can force game-visual modes or color profiles that clash with the monitor's own processing.
- **Power-plan GPU switching:** On models with switchable graphics, aggressive power saving can toggle between iGPU and dGPU mid-session, producing brief flicker each switch.
- **Faulty monitor overdrive setting:** The monitor's own overdrive/response-time setting at its maximum can overshoot pixels and shimmer, which looks like a laptop problem but is not.
- **Windows HDR and night-light conflicts:** HDR on Windows plus Night Light or f.lux-style filters can fight over the color pipeline and produce periodic flicker on secondary displays.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test the monitor and cable on another device

Before touching any driver, confirm the monitor itself is innocent. If it flickers on a second computer too, the fault is the monitor or its cable — not your ASUS laptop.

1. Connect the monitor to a different computer or a game console with the same cable. Watch for two full minutes.
2. If it flickers there too, swap to a different, shorter, certified cable (Ultra High Speed HDMI or DP 1.4 rated).
3. If the flicker survives a known-good cable on a second device, the monitor panel or its power supply is failing — service or replace it.
4. If the monitor is clean elsewhere, the problem lives in your laptop. Continue to the next fix.

### Fix 2: Set the correct refresh rate and resolution manually

Windows does not always pick the best mode. Locking it yourself eliminates negotiation flicker immediately.

1. Right-click the desktop, choose **Display settings**, select the external monitor, then **Advanced display**.
2. Set the refresh rate to the monitor's native value (usually **60 Hz** or the panel's advertised max) and the resolution to its native resolution.
3. Disable **HDR** on the external display if it is on, and turn off **Night light** temporarily as a test.
4. Watch for five minutes. If the flicker stops, you found it — leave these settings locked in.

### Fix 3: Turn off adaptive sync on the monitor

Adaptive-sync flicker is distinctive: brightness pulsing when content changes, especially in games or video. If that matches, the monitor's FreeSync/G-Sync implementation is fighting the laptop.

1. Open the monitor's on-screen menu and find **FreeSync**, **Adaptive Sync**, or **G-Sync Compatible** — set it to **Off**.
2. In the NVIDIA Control Panel (if present), go to **Set up G-SYNC** and uncheck the external monitor, or in AMD Software disable **FreeSync** for that display.
3. Restart the laptop and retest with video playback and a game.
4. If flicker is gone, keep adaptive sync off for this pairing — stability beats the feature here.

### Fix 4: Clean-install the GPU driver from ASUS, not Windows

This is the fix that resolves most ASUS cases. Windows Update's generic driver is the usual culprit; the ASUS-specific build contains display fixes for your exact model.

1. Download **DDU (Display Driver Uninstaller)** and the latest GPU driver for your exact model from the ASUS support site (search your model, e.g. at [ASUS-adjacent vendor pages](https://www.nvidia.com/Download/index.aspx) for NVIDIA chips if ASUS's build lags).
2. Boot into **Safe Mode**, run DDU to remove the current GPU driver completely.
3. Install the driver you downloaded, choosing **Custom → Clean installation** if using NVIDIA's installer.
4. Reboot normally and retest the external monitor for at least ten minutes of mixed use.

### Fix 5: Disable ASUS display utilities temporarily

Armoury Crate game-visual profiles and Splendid color modes can override the signal in ways that shimmer on external panels.

1. Open **Armoury Crate → Game Visual** and set it to **Default** (not Racing/Cinema/FPS).
2. Open **MyASUS → Customization → Splendid** and set it to **Normal** or turn it off.
3. In **Armoury Crate → System → GPU Power Saving**, set it to **Standard** so the dGPU is not aggressively toggling.
4. Retest. If the flicker is gone, re-enable features one at a time to find the offender. A related [screen flickering guide](/articles/how-to-fix-screen-flickering-on-laptop-after-windows-11-update/) covers the built-in-display variant.

### Fix 6: Fix USB-C/Thunderbolt display output if you use it

If your monitor connects through USB-C or Thunderbolt, the alternate-mode handshake adds another failure layer: bandwidth sharing with USB data can starve the display signal.

1. Use the cable that came with the monitor, plugged directly into the laptop — no hubs or dongles for this test.
2. In **Device Manager → Universal Serial Bus controllers**, confirm no **USB Billboard Device** warnings appear (that means alt-mode negotiation failed).
3. Update the **Thunderbolt/USB4** driver from ASUS support, then the Intel graphics driver.
4. If hubs are involved, power the hub from its own adapter — unpowered hubs are a classic flicker source.

### Fix 7: Rule out electromagnetic interference and power

Flicker that pulses at regular intervals can be interference, not software. This is quick to rule out.

1. Move phone chargers, desk lamps, and especially cheap LED power bricks away from the video cable.
2. Plug the monitor into a different wall outlet, ideally on a different circuit from the laptop charger.
3. Try the laptop on battery power with the charger unplugged — if flicker stops, the charger is injecting noise and should be replaced.

## Closing

Second-monitor flicker on ASUS laptops is almost never a dying GPU — it is a handshake problem between laptop, cable, driver, and panel. The systematic order matters: prove the monitor innocent, lock the mode, kill adaptive sync, then clean-install the ASUS GPU driver. Most people never get past Fix 4.