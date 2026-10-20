---
title: "How to Fix Auto Super Resolution Not Working in Games"
slug: auto-super-resolution-games-not-working
date: 2026-10-20
categories: ["ai-pc"]
tags: ["auto super resolution", "gaming", "troubleshooting", "ai pc", "auto sr", "windows 11"]
description: "Auto SR not boosting your games on a Copilot+ PC? This guide explains the NPU, game-support, and graphics requirements, then walks through every fix in order."
thumbnail: "/images/thumbs/auto-super-resolution-games-not-working.webp"
faqs:
  - q: "Why is Auto SR grayed out in Windows Settings?"
    a: "Auto SR is grayed out when your PC lacks a qualifying Copilot+ NPU or when your graphics driver is too old. It also stays unavailable if Windows 11 is not on a recent build. Updating your GPU driver and installing all Windows updates resolves the grayed-out toggle in most cases."
  - q: "Does Auto Super Resolution work with every game?"
    a: "No. Auto SR only enhances games that render at supported resolutions and use compatible graphics APIs. Older titles, games running in exclusive fullscreen at native resolution, and some anti-cheat-protected games may not engage it. Microsoft maintains a list of verified titles, so check whether your game is officially supported."
  - q: "Auto SR worked yesterday but stopped today. What should I check first?"
    a: "A recent graphics driver or Windows update is the usual suspect, since either can break the Auto SR handshake. Roll the GPU driver back or reinstall it cleanly, and confirm the per-game toggle is still on, because major updates sometimes reset graphics settings."
  - q: "Is Auto SR the same as DLSS or FSR?"
    a: "No. DLSS and FSR are built into individual games by their developers, while Auto SR is applied by Windows itself to supported titles without any game changes. Auto SR runs on the NPU of Copilot+ PCs, which is why it needs different hardware than GPU-based upscalers."
---

Auto Super Resolution, or Auto SR, is Windows 11's system-level AI upscaler for games. Instead of waiting for each developer to add DLSS or FSR, Windows applies its own NPU-powered upscaling to supported titles, rendering them at a lower internal resolution and reconstructing a sharper image for smoother frame rates.

When it does not work, the signs are easy to miss. The toggle in Settings may be grayed out, the feature may simply never engage in a supported game, or you might see stuttering and visual glitches where the upscale should be helping. Because Auto SR depends on the NPU, the GPU driver, and per-game compatibility all at once, the cause is rarely obvious.

This guide sorts it out step by step: confirm the hardware and game requirements, fix drivers and settings, and verify the feature engages — stopping once frame rates improve.

## Why this happens

- **No qualifying NPU:** Auto SR needs a Copilot+ PC with a 40+ TOPS NPU to run its model.
- **Outdated graphics driver:** the GPU driver mediates between the game, Windows, and the NPU upscaler.
- **Windows build too old:** Auto SR arrived in recent Windows 11 releases and needs current servicing updates.
- **Unsupported game:** not every title or graphics API is compatible with system-level upscaling.
- **Per-game toggle off:** Auto SR can be disabled globally or for individual games in Settings.
- **Conflicting overlays or upscalers:** a game's own DLSS/FSR setting or a third-party overlay can fight Auto SR.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your PC and game qualify

Auto SR is gated on Copilot+ hardware, so verify the NPU first: open Task Manager, check the Performance tab for the NPU tile, and confirm its TOPS rating. If the NPU is missing from Task Manager, treat that as the real problem — our guide to [Ryzen AI NPUs not showing up](/articles/amd-ryzen-ai-npu-not-showing-up/) covers the AMD side, and the same detection logic applies to other vendors. Next, check that your game is on Microsoft's supported list and is not running at native resolution in exclusive fullscreen, which bypasses the upscaler.

1. Open Task Manager and confirm the NPU tile on the Performance tab.
2. Verify the NPU meets the 40+ TOPS Copilot+ requirement.
3. Check Microsoft's documentation for whether your game supports Auto SR.
4. Set the game to a below-native render resolution, not native fullscreen.
5. Disable any in-game DLSS or FSR option so it does not conflict.

### Fix 2: Update Windows 11 completely

Auto SR's system components ship with Windows itself, and partial or outdated installs are a classic cause of a dead toggle. Go to Settings, then Windows Update, and install every available update including optional ones. Feature updates matter most here, since they carry the graphics and NPU stack changes Auto SR depends on. Restart afterward and recheck the toggle in Settings, then System, then Display, then Graphics.

1. Open Settings and go to Windows Update.
2. Click Check for updates and install everything offered.
3. Include optional updates under Advanced options.
4. Restart your laptop.
5. Reopen Settings, then System, then Display, then Graphics to check Auto SR.

### Fix 3: Update or clean-install the graphics driver

The GPU driver sits in the middle of the Auto SR pipeline, handing frames between the game and the NPU upscaler. A stale or corrupted driver is the most common reason Auto SR engages inconsistently or produces artifacts. Download the latest driver from your GPU vendor — NVIDIA users can use [NVIDIA's driver download page](https://www.nvidia.com/Download/index.aspx) — and choose a clean installation.

1. Identify your GPU in Task Manager or Device Manager.
2. Download the latest driver from the GPU vendor's official site.
3. Run the installer and choose the clean installation option.
4. Restart the laptop after installation completes.
5. Launch the game and check whether Auto SR now engages.

### Fix 4: Enable Auto SR globally and per game

Auto SR has two switches: a system-wide default and a per-game override, and either one can silently be off. Open Settings, then System, then Display, then Graphics, and turn on Auto Super Resolution at the top of the page. Then scroll to your specific game in the app list and make sure it is set to use the system default or is explicitly enabled.

1. Open Settings, then System, then Display, then Graphics.
2. Turn on the main Auto Super Resolution toggle.
3. Find your game in the per-app list below.
4. Open its options and set Auto SR to on or system default.
5. Restart the game for the change to take effect.

### Fix 5: Update NPU firmware and drivers

Auto SR leans on the NPU more heavily than most people expect, so NPU-side problems can break it even when the GPU driver is perfect. Update the NPU driver through Device Manager or your laptop maker's support page, and check for firmware updates in your manufacturer's update utility — a [failed NPU firmware update](/articles/npu-firmware-update-failed-laptop/) is a known way for AI features to degrade silently. After updating, verify the NPU tile in Task Manager shows a healthy driver version before retesting the game.

1. Open Device Manager and expand Neural processors.
2. Update the NPU driver to the latest vendor release.
3. Check your laptop maker's utility for NPU firmware updates.
4. Restart and confirm the NPU looks healthy in Task Manager.
5. Retest Auto SR in the supported game.

### Fix 6: Disable conflicting overlays and capture tools

Third-party overlays and screen recorders hook into the same graphics pipeline Auto SR uses, and the two can interfere. Temporarily disable overlays from game launchers and GPU utilities, then test the game clean. If Auto SR engages with overlays off, re-enable them one at a time to find the culprit. This kind of interference also slows other AI-accelerated background work, which is why a [slow AI search index](/articles/windows-search-ai-indexing-slow/) sometimes shares the same overloaded-system root cause.

1. Disable overlays in your game launcher and GPU utility.
2. Turn off third-party screen recording for the test.
3. Launch the game and check whether Auto SR engages.
4. Re-enable tools one by one to identify the conflict.
5. Keep the conflicting tool disabled while gaming.

## Closing

Auto SR fails most often at the seams — between the NPU, the GPU driver, and the game's settings — rather than from any single broken part. Confirm the hardware, update both drivers, flip both toggles, and the upscaler will kick in on supported titles.
