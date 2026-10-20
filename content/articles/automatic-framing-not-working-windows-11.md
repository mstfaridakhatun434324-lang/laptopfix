---
title: "Automatic Framing Not Working in Windows 11? Fix Studio Effects"
slug: automatic-framing-not-working-windows-11
date: 2026-10-20
categories: ["ai-pc"]
tags: ["automatic framing", "studio effects", "webcam", "troubleshooting", "ai pc", "windows 11"]
description: "Automatic framing not keeping you centered on video calls? Learn why this NPU camera effect fails on Copilot+ PCs and how to restore smooth auto-framing."
thumbnail: "/images/thumbs/automatic-framing-not-working-windows-11.webp"
faqs:
  - q: "Why is automatic framing greyed out in Windows 11?"
    a: "Greyed-out framing usually means the NPU is not available to the effects pipeline — the driver may be missing, disabled, or crashed. It can also mean the app you are using does not support Studio Effects. Confirm the NPU is visible in Task Manager under Performance before troubleshooting further."
  - q: "Does automatic framing work in Zoom and Teams?"
    a: "Yes, both support Windows Studio Effects on Copilot+ PCs, but each app has its own camera pipeline. Framing can work in the Windows Camera app yet fail in Zoom if Zoom is using a virtual camera or an incompatible capture mode. Test in the Camera app first to isolate the problem."
  - q: "Does automatic framing need an internet connection?"
    a: "No. Automatic framing runs entirely on the NPU inside your laptop, which is the point of Copilot+ AI features — local, private processing. If framing fails offline, the problem is the driver or the app, not your connection."
  - q: "Why does automatic framing make my video laggy?"
    a: "Lag means the effect is falling back to the CPU or GPU instead of the NPU, usually because the NPU driver stalled. Updating the NPU driver and restarting the effects pipeline restores smooth NPU processing. If the NPU is missing entirely, see our guide on the [NPU not being detected](/articles/npu-not-detected-windows-11/)."
---

Automatic framing is supposed to keep you centered as you move around on a call — instead, the toggle is greyed out, the camera stays stubbornly fixed, or the framing stutters so badly you turn it off. On Copilot+ PCs this feature runs on the NPU, so when it breaks, the root cause is usually the AI pipeline rather than the camera itself.

The good news is that framing failures follow a predictable pattern. Either the NPU is not handing the effect to Windows, the app is bypassing Studio Effects, or the driver crashed mid-call. Each has a distinct fix, and this guide takes them in order so you find yours fast. If the whole Studio Effects panel misbehaves in calls, also see our guide on [Studio Effects not working in Microsoft Teams](/articles/studio-effects-not-working-teams/) — the two issues share the same pipeline.

Three paragraphs in, here is the plan: verify the NPU, verify the app path, then repair the driver. Let us start.

## Why this happens

- **NPU driver missing or crashed:** Automatic framing needs a live NPU. If the driver failed, the toggle greys out. Check whether your AI hardware shows up properly — our guide on [AI Boost greyed out in Task Manager](/articles/ai-boost-greyed-out-task-manager/) covers the same detection problem.
- **App bypasses Studio Effects:** Some apps use their own camera stack or a virtual camera, which skips Windows effects entirely.
- **Effects toggled off for that camera:** Windows stores Studio Effects per camera device; the setting can be off for your built-in camera while on for another.
- **Camera driver conflict:** A generic camera driver may not expose the frames the NPU effects need.
- **Windows version too old:** Studio Effects requires a recent Windows 11 build; older installs lack the plumbing.
- **Effect crashed mid-call:** The framing process can die silently, leaving the toggle on but the video unframed.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Confirm the NPU is alive in Task Manager

Automatic framing cannot run without the NPU. If the AI hardware is not visible to Windows, no effects toggle will ever work.

1. Open Task Manager (Ctrl + Shift + Esc) and go to the Performance tab.
2. Look for an "NPU" entry (it may be labeled "NPU 0" or "Intel AI Boost").
3. If it is missing, follow our NPU detection guide before continuing — the camera is not the problem.
4. If the NPU shows 0% during a call with framing on, the effect is not reaching the hardware — continue to Fix 3.

### Fix 2: Enable framing for the right camera in Settings

Windows stores Studio Effects per camera device. The toggle can be on for a disconnected USB camera and off for your built-in one.

1. Open Settings > Bluetooth & devices > Cameras and select your built-in camera.
2. Make sure the "Automatic framing" toggle is on for this specific camera.
3. Close and reopen your video app so it picks up the new setting.
4. Test in the built-in Camera app first — it is the cleanest test of the Windows effects path.

### Fix 3: Restart the effects pipeline

The framing process can crash silently while the toggle stays on. A pipeline reset clears the dead state without a full reboot.

1. Turn off all Studio Effects for the camera in Settings, then close every video app.
2. Open Task Manager and end any "Windows Camera Frame Server" process.
3. Reopen the Camera app, re-enable automatic framing, and move side to side to test tracking.
4. If framing works in the Camera app, the Windows side is healthy — the issue is your call app's camera path (Fix 4).

### Fix 4: Point your call app at the physical camera

Call apps sometimes latch onto a virtual camera or a stale device entry that bypasses Studio Effects. Pointing the app at the real hardware restores the effects path.

1. In Teams or Zoom, open video/device settings and check which camera is selected.
2. Choose the built-in camera by its real name (for example "Integrated Camera"), not "Virtual Camera" or "OBS."
3. Disable any virtual camera software you are not actively using.
4. Restart the call app and verify the framing toggle is now active.

### Fix 5: Update the NPU and camera drivers

Framing depends on both drivers cooperating. Update them as a pair from your manufacturer's support page rather than relying on Windows Update alone.

1. Download the latest NPU driver (Intel AI Boost, AMD Ryzen AI, or Qualcomm) from your maker's support site.
2. Download the latest camera driver for your exact model from the same page.
3. Install the NPU driver first, restart, then install the camera driver and restart again.
4. Microsoft documents driver update basics on the [Windows support hub](https://support.microsoft.com/en-us/windows) if you need the general procedure.

### Fix 6: Update Windows and reset the camera stack

Studio Effects plumbing improves with every Windows 11 build. If you are behind, the framing feature may be missing pieces it needs.

1. Go to Settings > Windows Update and install all pending updates, then restart.
2. If framing still fails, reset the Camera app via Settings > Apps > Installed apps > Camera > Advanced options > Reset.
3. As a last resort, uninstall the camera in Device Manager (tick "remove driver"), restart, and let Windows reinstall it.
4. Re-enable automatic framing in Settings and test with a real call.

## Closing

Automatic framing fails for one of three reasons: a dead NPU, the wrong camera path, or a broken driver — and the fixes above address them in that order. Verify the NPU in Task Manager, enable framing per camera, reset the pipeline, aim your app at the physical camera, and update the driver pair. Once framing tracks you smoothly again, it should stay that way; if it keeps dying, the NPU driver needs the deeper reinstall treatment. If connectivity is also flaky on your AI laptop, see [Wi-Fi 7 not working on AI laptops](/articles/wifi-7-not-working-ai-laptop/).
