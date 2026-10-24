---
title: "How to Fix RTX Video Super Resolution Not Working on a Laptop"
slug: rtx-video-super-resolution-not-working
date: 2026-10-24
categories: ["ai-pc"]
tags: ["rtx video", "super resolution", "nvidia", "video upscaling", "chrome"]
description: "RTX Video Super Resolution not engaging on your laptop? Fix NVIDIA VSR in Chrome and Edge with these proven driver, GPU-selection, and Control Panel checks."
thumbnail: "/images/thumbs/rtx-video-super-resolution-not-working.webp"
faqs:
  - q: "What is RTX Video Super Resolution?"
    a: >
      RTX Video Super Resolution (VSR) is NVIDIA's AI upscaling for video played in Chrome and Edge — it uses the RTX GPU's Tensor cores to sharpen and upscale web video in real time. It requires an NVIDIA RTX GPU (20-series or newer), current drivers, and supported browsers.
  - q: "Does RTX Video Super Resolution work on Snapdragon ARM laptops?"
    a: >
      No. VSR requires an NVIDIA RTX GPU with Tensor cores — Snapdragon laptops use Adreno graphics, which cannot run it. This is a hardware requirement, not a settings issue. ARM laptops have their own OS-level video enhancement features instead.
  - q: "Why is the RTX Video Enhancement option grayed out in NVIDIA Control Panel?"
    a: >
      Grayed-out options mean the driver does not detect a supported configuration: outdated driver, an incompatible GPU, the laptop running on the integrated GPU instead of the NVIDIA GPU, or an external monitor plugged into the iGPU output.
  - q: "Does VSR increase battery drain on laptops?"
    a: >
      Yes, noticeably. VSR runs AI inference on the GPU for every frame of video, which keeps the NVIDIA GPU awake and draws significant power. On battery, consider dropping to quality level 1 or disabling VSR — the battery cost is real.
---

You heard RTX Video Super Resolution makes web video look dramatically better — AI upscaling, right in Chrome. You opened NVIDIA Control Panel, and the option is grayed out. Or you enabled it and nothing changes. The feature that was supposed to be automatic is doing nothing.

First, the critical honesty: RTX Video Super Resolution requires an NVIDIA RTX GPU. If your laptop is a Snapdragon/ARM machine with Adreno graphics, VSR cannot work — there is no setting, driver, or hack that creates Tensor cores. This article is for laptops that actually have NVIDIA RTX graphics (many Intel/AMD AI PCs do), where VSR should work but does not.

For RTX laptops where VSR misbehaves, the causes are: outdated drivers, the browser running on the integrated GPU, the feature disabled in Control Panel, unsupported video conditions, or external-monitor routing issues. Six fixes, in order.

## Why this happens

- **No NVIDIA RTX GPU present:** Snapdragon/ARM laptops and Intel/AMD iGPU-only machines lack the Tensor-core hardware VSR requires — the feature cannot exist there.
- **Outdated NVIDIA driver:** VSR needs recent drivers; old ones lack the feature or its current browser hooks.
- **Browser running on integrated graphics:** On dual-GPU laptops, Chrome/Edge may run on the iGPU — VSR only processes video on the NVIDIA GPU.
- **Feature not enabled in Control Panel:** VSR defaults off and must be enabled per quality level in NVIDIA Control Panel.
- **Unsupported video conditions:** VSR skips DRM-protected content paths it cannot process, very low-resolution sources, and some HDR configurations.
- **External monitor on iGPU output:** If the display pipeline routes through the integrated GPU, VSR cannot engage.
- **Browser hardware acceleration off:** With GPU acceleration disabled in the browser, there is no GPU video path for VSR to enhance.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm you have a supported NVIDIA RTX GPU

Do not troubleshoot a feature your hardware cannot run. Thirty seconds here prevents hours of futile settings-chasing — especially on AI PCs where the "AI" branding invites confusion.

1. Open **Device Manager > Display adapters** and confirm an **NVIDIA GeForce RTX** (20-series or newer) is listed.
2. If you see only Qualcomm Adreno, Intel Iris/UHD, or AMD Radeon integrated graphics — VSR is not available on this machine, full stop. Windows' own video enhancement settings are your alternative.
3. On dual-GPU laptops, confirm the NVIDIA GPU is actually active and not disabled in Device Manager.
4. Check **NVIDIA Control Panel > System Information** for the GPU model and driver version.
5. Only continue if an RTX GPU is present and enabled. Copilot+ Thunderbolt dock users with eGPUs face related GPU-routing issues: [Copilot+ PC Thunderbolt dock not working](/articles/copilot-plus-pc-thunderbolt-dock-not-working/).

### Fix 2: Update the NVIDIA driver

VSR is driver-delivered — its browser hooks, quality levels, and bug fixes all ride the driver package. An old driver is the top cause of "option missing" on supported hardware.

1. Open **GeForce Experience** (or the NVIDIA app) and check for driver updates — install the latest **Game Ready** driver.
2. Alternatively, download the driver manually from [NVIDIA's driver download page](https://www.nvidia.com/Download/index.aspx) — select your exact GPU and Windows 11.
3. Choose **Custom install** and check **Perform a clean installation** to clear old driver state.
4. Restart after installation — driver changes need a reboot.
5. Reopen NVIDIA Control Panel and check whether the RTX Video Enhancement section now appears.

### Fix 3: Enable VSR in NVIDIA Control Panel

The feature defaults off. Enabling it is a Control Panel setting with quality levels — and the setting must stick, which it sometimes does not on laptop driver configurations.

1. Open **NVIDIA Control Panel > Video > Adjust video image settings** (or **RTX Video Enhancement** section on newer drivers).
2. Check **Super resolution** and set the quality level — start at **1** (lowest GPU cost) to verify it engages.
3. Click **Apply** and close the Control Panel.
4. Reopen the Control Panel and confirm the setting persisted — if it reverts, the driver install is damaged (redo Fix 2's clean install).
5. Note the expected behavior: VSR engages automatically on played video — there is no per-video toggle. Narrator's natural voices fail in a similarly "setting won't stick" way: [Narrator natural voices not working](/articles/narrator-natural-voices-not-working/).

### Fix 4: Force the browser onto the NVIDIA GPU

On dual-GPU laptops, browsers default to the power-saving integrated GPU — and VSR only works when the browser's video pipeline runs on the NVIDIA GPU. This is the most common "enabled but nothing happens" cause.

1. Open **Settings > System > Display > Graphics**.
2. Find **Chrome** and **Edge** in the app list (add them via Browse if missing).
3. Set each to **High performance** (the NVIDIA GPU) — not "Let Windows decide."
4. Fully quit the browser (check Task Manager — no lingering processes) and relaunch.
5. Play a 1080p YouTube video and check the NVIDIA GPU activity in Task Manager's **Performance** tab — the GPU should show video-engine/AI load. No load means the browser is still on the iGPU.

### Fix 5: Verify browser requirements and test properly

VSR has specific browser conditions. Testing wrong — wrong content, wrong settings — looks identical to "not working."

1. Use **Chrome** (version 110+) or **Edge** (version 110+) — VSR supports these two browsers.
2. In the browser settings, confirm **hardware acceleration** is enabled (`chrome://settings/system` > **Use graphics acceleration when available**).
3. Test with a standard 720p/1080p YouTube video — VSR upscales sub-native content; it does nothing visible on already-4K video.
4. Toggle VSR quality between 1 and 4 while watching — the sharpness difference should be visible when it engages.
5. Note DRM limits: some protected streams bypass the enhancement path — test with plain YouTube first before judging protected services. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the graphics-preference settings used above.

### Fix 6: Fix external monitor and HDR edge cases

The remaining failures are display-pipeline issues: the video frames never reach the NVIDIA GPU because of how the monitor is connected, or HDR modes VSR does not process.

1. If using an external monitor, connect it to a port wired to the NVIDIA GPU (usually HDMI/DisplayPort directly, not through a dock's iGPU path) — check your laptop manual's port diagram.
2. Test with the laptop's internal display only — if VSR works internally but not externally, the external path bypasses the NVIDIA GPU.
3. Disable HDR in **Settings > System > Display > HDR** as a test — some HDR configurations are not processed by VSR.
4. Close other GPU-heavy apps during testing — VSR needs Tensor-core headroom; a maxed GPU may skip enhancement silently.
5. If VSR works on the internal display with SDR content, you have found your configuration limits — that is the feature working as designed, not a bug. Samsung's Galaxy Book4 Edge (Intel-based) supports VSR properly: [Galaxy Book4 Edge problems](/articles/samsung-galaxy-book4-edge-problems/).

## Closing

RTX Video Super Resolution is a real, visible upgrade on laptops that have the hardware — and a non-starter on those that do not, which is the first thing to verify honestly. On supported RTX laptops, the fix chain is short: current driver, feature enabled, browser forced to the NVIDIA GPU, and sane test content. Once the Tensor cores show load in Task Manager during a YouTube video, VSR is working — enjoy the sharper picture, and remember the battery cost when you unplug.
