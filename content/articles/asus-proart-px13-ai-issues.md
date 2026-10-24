---
title: "How to Fix ASUS ProArt PX13 AI Issues on Windows 11"
slug: asus-proart-px13-ai-issues
date: 2026-10-24
categories: ["ai-pc"]
tags: ["proart-px13", "asus", "creator-laptop", "ryzen-ai", "troubleshooting"]
description: "ASUS ProArt PX13 AI features keep failing on Windows 11? Fix Ryzen AI NPU drivers, Studio Effects, color accuracy, and creator app issues step by step."
thumbnail: "/images/thumbs/asus-proart-px13-ai-issues.webp"
faqs:
  - q: "Why are AI features missing on my ProArt PX13?"
    a: >
      The AMD Ryzen AI NPU driver is usually missing or outdated. Check Device Manager under Neural processors, install the latest chipset driver from ASUS, and let Windows Update download the AI model components.
  - q: "Why do colors look wrong on my ProArt PX13?"
    a: >
      Wrong colors usually mean the color profile got reset by a Windows update, or HDR is mishandling SDR content. Restore the factory calibrated profile in Color Management and check HDR settings.
  - q: "Why is my ProArt PX13 slow in creative apps?"
    a: >
      Slowness in creative apps often comes from the wrong GPU being used, outdated Studio drivers, or thermal throttling. Check per-app GPU assignment and update to NVIDIA Studio drivers.
  - q: "Does the ProArt PX13 support Copilot+ features?"
    a: >
      Ryzen AI 300 series configurations with 16GB+ RAM meet the Copilot+ spec. If features are missing despite qualifying hardware, the NPU driver or AI components need attention.
---

The ProArt PX13 is ASUS's creator convertible — Ryzen AI inside, NVIDIA graphics, a color-accurate OLED, and AI features sprinkled across the creative workflow. It's a machine with two brains (NPU for AI, GPU for rendering) and a display that has to be perfect. When the AI features vanish, colors shift, or creative apps stumble, it hits right where this laptop is supposed to excel.

PX13 issues cluster around three systems: the Ryzen AI NPU stack that powers Copilot+ features, the dual-GPU dance between integrated Radeon and discrete NVIDIA graphics, and the color pipeline that the OLED panel depends on. Each has its own driver chain, and they fail independently — which is why one fix rarely solves everything.

This guide works through the six most common PX13 AI issues in technician order: NPU and AI components first, then GPU assignment, then color accuracy, then thermals under creative load, then ASUS's driver stack, and finally the app-specific quirks. The same layered logic applies across AI PCs — our [USB-C Ethernet adapter guide](/articles/usb-c-ethernet-adapter-not-working/) covers the shared peripheral stack, and [GTA V Enhanced on ARM](/articles/gta-v-enhanced-arm-laptop-issues/) shows the same driver-maturity pattern — while [Copilot being disabled on managed devices](/articles/copilot-managed-device-disabled/) is worth checking on work machines.

## Why this happens

- **Ryzen AI NPU driver missing:** ASUS's factory image doesn't always include the AMD NPU driver, and Windows Update doesn't reliably fetch it — Copilot+ features silently stay off.
- **Wrong GPU assigned to creative apps:** Windows' auto GPU selection sometimes parks DaVinci or Premiere on the integrated GPU, crippling render performance for no reason.
- **Color profile reset by updates:** Windows updates periodically reset the ICC profile, undoing the factory calibration that the ProArt line is sold on.
- **Game Ready vs. Studio drivers:** NVIDIA's Game Ready drivers prioritize frame rates; creators need Studio drivers for stability in creative apps — the wrong branch causes crashes.
- **Thermal throttling under sustained load:** The 13-inch chassis can't sustain full CPU+GPU indefinitely; dust or old thermal paste turns throttling from occasional to constant.
- **Conflicting ASUS utilities:** ProArt Creator Hub, Armoury Crate remnants, and MyASUS can fight over fan curves and GPU modes.
- **Windows AI components pending:** Even with a healthy NPU, the on-device models are separate downloads — features stay grayed out until they arrive.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the Ryzen AI NPU driver and AI components

Every Copilot+ feature on the PX13 gates on AMD's NPU driver — and it's the component most likely missing from the factory image. Fix this first; half the AI symptoms resolve together.

1. Open **Device Manager > Neural processors** and look for the AMD Ryzen AI NPU — no warning icons allowed.
2. If missing or flagged, download the latest chipset driver from ASUS's support site for the ProArt PX13 — AMD's NPU driver ships inside the chipset package.
3. Open **Settings > Windows Update**, install everything including optional updates — the Copilot+ AI models are separate downloads.
4. Leave the laptop plugged in on Wi-Fi for 30-60 minutes so the on-device models finish downloading.
5. Verify in **Settings > Bluetooth & devices > Cameras** (Studio Effects) and **Privacy & security > Recall & snapshots** that features are now live.

### Fix 2: Assign the right GPU to creative apps

The PX13 has two GPUs and Windows doesn't always choose wisely. Forcing creative apps onto the NVIDIA GPU is the single biggest performance fix for rendering and timeline work.

1. Open **Settings > System > Display > Graphics**, find your creative app (or add it via **Browse**), and set it to **High performance** (NVIDIA GPU).
2. In the **NVIDIA Control Panel > Manage 3D Settings > Program Settings**, confirm the app uses the **High-performance NVIDIA processor**.
3. Install **NVIDIA Studio drivers** (not Game Ready) from [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx) — Studio drivers are validated for creative app stability.
4. In your creative app's own preferences, confirm GPU acceleration is enabled and pointing at the NVIDIA card.
5. Test a render — if times drop dramatically, the iGPU was the bottleneck all along.

### Fix 3: Restore color accuracy

A ProArt with wrong colors is a broken promise. The fix is restoring the factory calibration profile and stopping Windows from undoing it — plus checking HDR behavior on the OLED.

1. Open **Color Management** (search it in Start), select the PX13's display, and confirm the ASUS factory profile is set as default.
2. Remove any third-party or "vivid" ICC profiles — they're calibrated for other panels and look wrong here.
3. Check **Settings > System > Display > HDR** — toggle it off for SDR creative work; HDR tone-mapping shifts colors in non-HDR apps.
4. In your creative app, confirm the working color space matches your delivery target (sRGB for web, Rec.709 for video).
5. For critical work, consider a hardware calibrator — factory profiles drift as OLED panels age, and recalibration every 6-12 months keeps the ProArt promise.

### Fix 4: Fix thermals under creative load

The PX13 will thermal-throttle under sustained CPU+GPU rendering — that's physics in a 13-inch chassis. The fix is managing the heat path so throttling stays occasional, not constant.

1. Clean the vents with compressed air — dust is the most common reason a previously-fine machine starts throttling.
2. Use a cooling stand or at least a hard flat surface — the bottom intakes need airflow during renders.
3. In **ProArt Creator Hub** or MyASUS, set the fan profile to **Performance** (not Silent) before long renders — silent modes trade thermals for noise.
4. Monitor with HWiNFO during a render — if the CPU sits at 95°C+ constantly, consider a repaste (or a service center if under warranty).
5. For very long renders, cap the app's thread count slightly — 90% speed at sustainable thermals beats 100% speed with throttling stutter.

### Fix 5: Clean up ASUS's utility conflicts

Multiple ASUS utilities fighting over fan curves, GPU modes, and power plans is a real PX13 issue — pick one control plane and disable the others.

1. Decide your primary: **ProArt Creator Hub** for creator workflows is the natural choice on this machine.
2. Uninstall or disable Armoury Crate if present — it's a gaming utility that conflicts with Creator Hub's profiles.
3. In MyASUS, turn off any overlapping features (fan control, GPU mode) that Creator Hub also manages.
4. After consolidating, set your power plan once and verify it sticks across reboots — flip-flopping plans indicate two utilities still fighting.
5. Keep MyASUS for updates only — it's the reliable source for ASUS driver packages even when you control everything else elsewhere.

### Fix 6: Fix app-specific AI and creative quirks

With the platform healthy, remaining issues are usually per-app: AI features inside creative apps need their own updates, and plugin conflicts are common in this ecosystem.

1. Update your creative apps — AI features in Photoshop, Premiere, and DaVinci arrive via app updates, not Windows updates.
2. Check each app's AI/GPU preferences — some disable GPU or NPU acceleration by default after updates.
3. Disable third-party plugins one by one if an app crashes on AI operations — plugin conflicts are the top crash cause.
4. For Adobe apps specifically, confirm you're on the Studio-driver-compatible version — Adobe validates against Studio drivers.
5. Check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) for Windows AI feature issues that span apps — some "app bugs" are platform bugs.

## Closing

The ProArt PX13's AI issues are a three-stack problem: get AMD's NPU driver and the Windows AI components right, pin creative apps to the NVIDIA GPU with Studio drivers, and protect the factory color calibration from Windows updates. Manage thermals honestly for the 13-inch chassis, pick one ASUS utility as your control plane, and update creative apps for their own AI features. Do that, and the convertible does what creators bought it for — accurate color, fast renders, and AI that actually assists.
