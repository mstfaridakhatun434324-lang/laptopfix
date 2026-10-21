---
title: "How to Fix Windows Recall Not Working with Dual Monitors"
slug: recall-not-working-dual-monitor
date: 2026-10-21
categories: ["ai-pc"]
tags: ["recall dual monitor", "windows recall", "recall second monitor", "ai pc", "recall troubleshooting", "multi display recall"]
description: "Fix Windows Recall failing on dual monitors with six methods: display settings, capture scope, GPU drivers, and per-monitor exclusions that actually stick."
thumbnail: "/images/thumbs/recall-not-working-dual-monitor.webp"
faqs:
  - q: "Does Windows Recall support multiple monitors?"
    a: >
      Yes — Recall is designed to capture all connected displays. When it fails on dual monitors, the cause is almost always configuration, drivers, or capture-scope settings, not a missing feature.
  - q: "Why does Recall only capture my main display?"
    a: >
      Usually a capture-scope setting limited to the primary display, a display driver misreporting the second monitor, or a stale multi-display configuration from before the second monitor was connected.
  - q: "Can different refresh rates break Recall on dual monitors?"
    a: >
      They can contribute. Mismatched refresh rates or scaling between monitors sometimes confuse the capture pipeline, producing black frames or skipped captures on the secondary display.
  - q: "Will disconnecting my second monitor fix Recall?"
    a: >
      As a diagnostic step, yes — it isolates whether the problem is multi-display-specific. But it is not a solution; the fixes here keep both monitors working with Recall.
---

Recall works fine on your laptop screen — and then you plug in the second monitor and everything gets weird. Maybe the external display never appears in snapshots, maybe captures come out black on one screen, maybe Recall stops capturing entirely the moment the second display connects. Single-display Recall is healthy; dual-monitor Recall is not.

Multi-display capture is genuinely harder than single-display: the pipeline composites frames from two different adapters, refresh rates, and scaling settings into one coherent snapshot. When any link misreports itself, Recall degrades — often silently, capturing only what it can.

This guide gives you six fixes in technician order: verify the display setup, correct the capture scope, fix the driver layer, and handle per-display quirks. Work through them in sequence.

## Why this happens

- **Capture scope limited to the primary display:** A setting or stale configuration can restrict Recall to the main display, so the second monitor is never included in captures.
- **Display driver misreporting the second monitor:** If the GPU driver reports wrong topology — resolution, position, or even existence — the capture pipeline cannot frame the second display correctly.
- **Mismatched scaling or refresh rates:** Different DPI scaling or refresh rates between monitors can produce black frames, tearing, or skipped captures on the secondary display.
- **Stale configuration from before the monitor was connected:** Recall caches display topology at setup. A monitor connected later — especially through a dock — may never get registered in that cached layout.
- **Dock or adapter interference:** USB-C docks and display adapters insert themselves into the display chain, and buggy dock firmware can make the second monitor appear and disappear from Windows' perspective.
- **GPU switching confusion on hybrid graphics:** Laptops with both integrated and discrete GPUs sometimes route each display through a different GPU, and the capture pipeline may only hook one of them.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify Windows sees both displays correctly

Recall can only capture what Windows itself recognizes. If the OS-level display setup is wrong, no Recall setting will fix it — so start at the foundation.

1. Open **Settings > System > Display** and confirm both monitors appear, with the correct one marked as the main display.
2. Click **Identify** and check the numbering matches physical reality — swapped identities confuse capture mapping.
3. Confirm the second monitor is set to **Extend these displays**, not Duplicate or Show only on 1/2; duplication and single-display modes change what there is to capture.
4. Note each display's resolution, scaling, and refresh rate — you will need these numbers in Fix 3.
5. If Windows itself does not see the second monitor reliably, fix that first (cable, dock, input source) before touching Recall.

### Fix 2: Re-register the display topology with Recall

Recall caches your display layout, and that cache goes stale when monitors change. Forcing Recall to re-learn the topology fixes the "second monitor connected later" class of failures.

1. In **Settings > Privacy & security > Recall & snapshots**, turn Recall off.
2. Disconnect the second monitor, wait 10 seconds, and reconnect it — let Windows fully settle (no flickering) before continuing.
3. Turn Recall back on and use the PC across both monitors for at least 30 minutes.
4. Open the timeline and verify that snapshots now include content from both displays.
5. If only the primary display appears, check whether a capture-scope option limits Recall to one display and broaden it — and if Recall is broadly misbehaving beyond monitors, the general [Windows Recall not working guide](/articles/windows-recall-not-working/) covers the wider fault set.

### Fix 3: Harmonize scaling, resolution, and refresh rate

The capture pipeline composites per-display frames, and wildly mismatched display parameters are a known source of black frames and skipped secondary captures. You do not need identical monitors — just a sane, supported combination.

1. In **Settings > System > Display**, select each monitor and set scaling to the recommended value Windows suggests for it.
2. Set both displays to their native resolutions — non-native resolutions force GPU scaling that complicates capture.
3. Under **Advanced display**, check refresh rates; if one monitor is at 144Hz and the other at 60Hz, try lowering the faster one temporarily as a test.
4. Restart Recall's capture (toggle off and on) after changing display parameters so it re-initializes against the new topology.
5. If the secondary display now captures correctly, you can experiment with raising the refresh rate back — change one variable at a time.

### Fix 4: Update the GPU and dock drivers

Display topology is reported by the GPU driver, and dock firmware sits in the chain for external monitors. Outdated drivers on either end produce exactly the phantom-monitor and black-frame symptoms in this guide.

1. Identify your GPU in Device Manager (**Display adapters**) and download the latest driver for your exact laptop model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support.
2. If you connect through a USB-C dock, check the dock manufacturer's support page for firmware updates — dock firmware bugs are a notorious cause of disappearing second monitors.
3. Install the GPU driver with a clean install option if offered, update dock firmware per the manufacturer's instructions, then restart.
4. Reconnect the second monitor, let the topology settle, and re-test Recall capture across both screens.
5. Peripheral-side faults on Snapdragon machines follow similar driver-first logic — see the [scanner not working on Snapdragon laptops](/articles/scanner-not-working-snapdragon-laptop/) guide for the pattern.

### Fix 5: Test with a direct connection to isolate the chain

If everything above fails, the fault may sit in the connection chain itself — a specific cable, adapter, or dock port — rather than in Recall or Windows. Isolating it keeps you from chasing software ghosts.

1. Connect the second monitor directly to the laptop (HDMI or USB-C) bypassing any dock or adapter.
2. Restart Recall capture and test for 30 minutes on the direct connection.
3. If Recall works directly but fails through the dock, the dock or its firmware is the fault — replace or update it rather than reconfiguring Recall.
4. If it fails even on a direct connection with current drivers, capture the exact symptom (black frames? missing display? total capture halt?) for Feedback Hub under Privacy > Recall.
5. Model-level speech and media faults follow the same isolate-the-chain discipline — the [live captions speech model error](/articles/live-captions-speech-model-error/) guide demonstrates it for a different component.

## Closing

Dual-monitor Recall failures are topology problems: Windows, the driver, or Recall disagrees about what the second display is. Verify the OS-level setup, force Recall to re-learn the layout, harmonize display parameters, and keep GPU and dock drivers current. Both screens end up in your timeline — the whole point of the second monitor.
