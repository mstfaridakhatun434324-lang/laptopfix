---
title: "Microsoft Teams Keeps Crashing on Snapdragon Laptops: 6 Fixes"
slug: teams-crashing-snapdragon-laptop
date: 2026-10-21
categories: ["ai-pc"]
tags: ["teams crashing", "snapdragon laptop", "teams arm64", "windows 11 arm", "video calls", "troubleshooting"]
description: "Microsoft Teams keeps crashing on your Snapdragon laptop? Six fixes for Teams on Windows 11 on ARM: the native ARM64 build, cache clearing, and crash fixes."
thumbnail: "/images/thumbs/teams-crashing-snapdragon-laptop.webp"
faqs:
  - q: "How do I know if my Teams is the ARM64 version?"
    a: >
      Open Task Manager, go to the Details tab, right-click the column headers, and enable the Architecture column. If Teams shows ARM64, you have the native build; if it shows x86, it is running under emulation and should be replaced with the native installer from the Microsoft Store.
  - q: "Will clearing the Teams cache delete my chats and files?"
    a: >
      No. Your chats, files, and meeting history live in Microsoft's cloud, not in the local cache. Clearing the cache only removes temporary files, thumbnails, and GPU shader blobs — Teams rebuilds them on the next launch, and everything re-syncs when you sign in.
  - q: "Why does Teams crash only when I share my screen?"
    a: >
      Screen sharing is the heaviest real-time workload Teams performs, and under x86 emulation the capture pipeline misses its timing deadlines and crashes. The native ARM64 build plus a current graphics driver fixes this in most cases — see Fix 1 and Fix 6 below.
  - q: "Can I just use Teams in the browser instead?"
    a: >
      Yes, as a stopgap. Edge on ARM handles Teams calls well, including screen sharing. But the browser cannot match the native app's background effects and notification integration, so treat it as a fallback while you fix the desktop client, not the permanent answer.
---

Teams freezing mid-call, crashing to the desktop the moment you share your screen, or refusing to open at all is a familiar headache on Snapdragon X laptops. The cause is almost always the same: an x86 build of Teams running under Prism emulation instead of the native ARM64 build — and emulation plus real-time video is a reliable recipe for crashes.

Copilot+ PCs ship with the new Teams client, but upgrades, old installers, and enterprise Microsoft 365 deployments can quietly leave the emulated build behind. Add a stale cache from a previous crash, camera and microphone permission tangles with NPU-powered Studio Effects, and you get the classic symptom set: launch crashes, mid-call drops, and screen-share freezes.

This guide gives you six fixes in technician order: get the native ARM64 build first, clear the corrupted state, then fix permissions and drivers. Work through them in sequence and test a call after each step.

## Why this happens

- **x86 Teams under emulation:** The Intel build runs through Prism translation, and real-time audio/video threads miss their deadlines under translation — the app crashes instead of stuttering.
- **Corrupted Teams cache:** Stale cache files and GPU shader blobs from a crashed session poison the next launch, which is why "Teams won't open at all" usually follows one bad crash.
- **Camera and microphone permission conflicts:** Windows Studio Effects (NPU background blur, eye contact) can fight Teams' own media processing for control of the camera pipeline, crashing it.
- **Outdated Teams client:** Older builds lack the ARM64 stability fixes Microsoft shipped across 2025 and 2026 — the Store version moves faster than enterprise deployments.
- **Graphics driver mismatch:** The Adreno GPU driver on Snapdragon X must match the Windows build; a mismatch crashes hardware-accelerated rendering exactly when screen sharing starts.
- **Legacy add-ins loading into the new client:** Old COM add-ins from the classic Teams and Skype for Business era can load into the new client and take it down on launch.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the native ARM64 build of the new Teams

This is the fix that resolves the majority of Teams crashes on Snapdragon laptops. The native ARM64 build runs directly on the processor with no translation layer, which eliminates the timing failures that kill the emulated build during calls.

1. Open **Settings > Apps > Installed apps**, find Microsoft Teams, and uninstall it completely.
2. Restart the laptop — this clears any locked files the uninstaller leaves behind.
3. Open the Microsoft Store, search for Microsoft Teams, and install it fresh; the Store serves the ARM64 build automatically on Snapdragon machines.
4. Verify the build: open Task Manager > Details tab, enable the **Architecture** column, and confirm Teams shows **ARM64**, not x86.
5. Sign in and place a test call before changing any settings — if it is stable now, the emulated build was your whole problem.

### Fix 2: Clear the Teams cache completely

If Teams crashes on launch or freezes within seconds, a corrupted cache from a previous crash is the likely culprit. A full cache wipe forces Teams to rebuild its temporary state from scratch, and your chats re-sync from the cloud afterward.

1. Quit Teams fully: right-click its system-tray icon and choose **Quit** (closing the window is not enough).
2. Press Win+R, type `%appdata%\Microsoft\Teams`, and delete everything inside the folder.
3. Also clear `%localappdata%\Microsoft\Teams` and any `GPUCache` folders you find there.
4. Relaunch Teams, sign in, and let it sit for a minute while it re-syncs.
5. If the rest of Microsoft 365 feels sluggish too, the [Office performance guide for Snapdragon laptops](/articles/microsoft-office-slow-snapdragon-laptop/) covers the shared causes behind slow Microsoft apps on ARM.

### Fix 3: Update Teams and Windows together

Teams and Windows 11 on ARM evolve in lockstep — media pipeline fixes land in both. Running a new Teams against an old Windows build (or vice versa) recreates the exact crashes the updates were meant to fix.

1. In Teams, click your profile picture > **About Teams** and check for updates; install any it finds.
2. Open **Settings > Windows Update** and install all pending updates, including optional driver updates.
3. Restart even if Windows does not ask — media components only reload on a full boot.
4. Re-test the exact scenario that crashed before (screen share is the best stress test).
5. Turn on automatic Store app updates so Teams does not silently fall behind again.

### Fix 4: Fix camera and microphone permissions and effect conflicts

When Teams crashes the moment video starts, the camera pipeline is usually where it dies — either a denied permission or a fight between Teams' effects and Windows Studio Effects for control of the NPU-processed feed.

1. Open **Settings > Privacy & security > Camera** and confirm **Let apps access your camera** is on and Microsoft Teams is allowed.
2. Do the same under **Microphone** — a denied mic can crash call setup just as hard as a denied camera.
3. In Teams, go to **Settings > General** and turn off Teams' own background effects if you also use Windows Studio Effects; running both processors on the same feed is a classic crash trigger.
4. Alternatively, disable Studio Effects for your camera under **Settings > Bluetooth & devices > Cameras** and let Teams handle effects alone — pick one, not both.
5. Start a test meeting and toggle video on and off; the pipeline should now survive the transition.

### Fix 5: Repair or reset the Teams app

When the installation itself is damaged — a half-applied update, a broken registration — Windows' built-in repair fixes it without touching your account data. Reset goes further, wiping local state while keeping the app installed.

1. Open **Settings > Apps > Installed apps**, click the three dots next to Microsoft Teams, and choose **Advanced options**.
2. Click **Repair** first and wait for the checkmark, then launch Teams and test.
3. If crashes continue, return to the same page and click **Reset** — you will need to sign in again, but chats and files re-sync.
4. Test a call with screen sharing, since that is the heaviest path through the repaired code.
5. Only if both fail should you uninstall and reinstall again — repeated reinstalls without the repair step rarely add anything.

### Fix 6: Update the graphics driver, and know when it is hardware

If Teams crashes specifically when sharing screens or using video effects, the Adreno GPU driver is the remaining suspect — hardware-accelerated capture and effects run through it. And if crashes spread beyond Teams to other apps, the problem may sit below the software entirely.

1. Find your exact model under **Settings > System > About**, then get the latest graphics/Adreno driver from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support — OEM drivers are validated against your firmware.
2. Install with the charger connected, restart, and re-test screen sharing in Teams.
3. Check Microsoft's guidance on [Windows app troubleshooting](https://support.microsoft.com/en-us/windows) if a specific error code appears alongside the crash.
4. If other apps crash or freeze too — browsers, Office, even File Explorer — and [Recall snapshots keep pausing](/articles/recall-snapshots-paused-fix/) as well, suspect system-level instability rather than Teams.
5. When crashes survive a native build, clean cache, current updates, and fresh drivers, read the [AI laptop warranty and NPU repair guide](/articles/ai-laptop-warranty-npu-repair/) — at that point a hardware check is the rational next step, and the guide covers what to document before the call.

## Closing

Teams crashes on Snapdragon laptops trace back to emulation in nearly every case: get the native ARM64 build, keep its cache clean, give it one effects pipeline instead of two, and keep the GPU driver current. Do those four things and Teams on a Snapdragon X machine is as boring and reliable as it is on any other laptop — which is exactly what you want from a work app.
