---
title: "How to Fix Photos Restyle Image Missing on Windows 11"
slug: photos-restyle-image-missing
date: 2026-10-24
categories: ["ai-pc"]
tags: ["photos-app", "restyle-image", "ai-styles", "copilot-plus", "troubleshooting"]
description: "Photos Restyle Image option missing on Windows 11? Fix Copilot+ eligibility, NPU drivers, app updates, and AI model downloads to bring back art styles."
thumbnail: "/images/thumbs/photos-restyle-image-missing.webp"
faqs:
  - q: "What is Restyle Image in the Photos app?"
    a: >
      Restyle Image applies AI art styles (anime, watercolor, pixel art, and more) to your photos using an on-device diffusion model. It's exclusive to Copilot+ PCs with a working NPU.
  - q: "Why is Restyle Image missing from my Photos app?"
    a: >
      The top causes are: not on a Copilot+ PC, an outdated Photos app, or the AI style models not yet downloaded. All three must be true for the option to appear.
  - q: "Does Restyle Image need internet?"
    a: >
      Only for the initial model download. Once the style models are on your device, restyling runs entirely on the NPU offline.
  - q: "Why does Restyle Image fail after I select a style?"
    a: >
      Mid-process failures usually mean the model download was interrupted or the NPU driver glitched. Check Windows Update for pending AI components and verify the NPU in Device Manager.
---

Restyle Image is the fun one — turn a photo into watercolor, anime, or pixel art with one click, all processed on your PC's NPU. Except on your machine, the option simply isn't there. No error, no grayed-out button, just... absent. You know it exists because you've seen the demos.

Here's the hard truth first: Restyle Image is exclusive to Copilot+ PCs. It runs a diffusion model on the NPU, and Microsoft gates it on qualifying hardware. If your PC isn't Copilot+, the option will never appear — that's by design, not a bug. But if your PC IS Copilot+ and it's still missing, it's one of four fixable things: NPU driver, Photos app version, AI model downloads, or region gating.

This guide works through Restyle Image in technician order: eligibility first (so you don't chase the impossible), then NPU driver, then Photos app, then model downloads, then region, and finally app repair. The same NPU-first logic runs through all AI PCs — our [WSL on Snapdragon guide](/articles/wsl-not-working-snapdragon-laptop/) covers the shared platform stack, and [NordVPN on ARM](/articles/nordvpn-arm-windows-issues/) shows the same driver-maturity pattern — while [HDR issues on ARM laptops](/articles/hdr-not-working-arm-laptop/) are worth checking if the restyled output looks wrong.

## Why this happens

- **Not a Copilot+ PC:** Restyle Image requires a qualifying NPU (40+ TOPS). Non-qualifying hardware never gets the option — this is intentional gating, not a malfunction.
- **NPU driver missing or broken:** On qualifying hardware, a bad NPU driver hides all NPU-gated Photos features including Restyle.
- **Outdated Photos app:** Restyle Image arrived in Photos via Store updates — old versions lack it entirely.
- **Style models not downloaded:** The art-style models are separate downloads. The option may hide until they arrive.
- **Region or language gating:** Restyle availability is gated on region and display language like other Copilot+ AI features.
- **Insufficient RAM:** Copilot+ requires 16GB minimum — qualifying chips with less RAM may miss some AI features.
- **Corrupted Photos app data:** Damaged cache can hide individual AI tools while the rest of Photos works.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify Copilot+ eligibility honestly

Check this first — thirty seconds now saves hours of futile troubleshooting if your hardware simply doesn't qualify. Restyle Image cannot be enabled on non-Copilot+ PCs by any setting.

1. Open **Settings > System > About** and look for Copilot+ PC branding.
2. Open **Device Manager > Neural processors** — confirm the NPU is present with no warning icon.
3. Check installed RAM in Task Manager's **Performance** tab — Copilot+ needs 16GB minimum.
4. If any check fails, stop here — use a cloud-based style transfer tool in your browser as the alternative.
5. If all checks pass and Restyle is still missing, continue — it's drivers, app, models, or region.

### Fix 2: Fix the NPU driver

A broken NPU driver on qualifying hardware hides every NPU-gated feature. The driver must come from your laptop maker — generic packages miss OEM customizations.

1. In Device Manager, inspect **Neural processors** for warning icons.
2. Download the NPU/chipset driver from your laptop maker's support site for your exact model.
3. If the driver claims to be fine, uninstall it (check **"Delete the driver software"**) and reinstall fresh — silent corruption is real.
4. Restart and confirm the NPU enumerates cleanly.
5. Run **Windows Update** including optional updates — AI runtime components often arrive this way.

### Fix 3: Update the Photos app

Restyle Image is Store-delivered. The inbox Photos version doesn't have it, and stalled Store updates are the most common fixable cause of the missing option.

1. Open the **Microsoft Store > Library > Get updates** and wait for **Microsoft Photos** to finish.
2. Open Photos **Settings** (gear icon) and confirm a recent build — Restyle needs a 2024+ version.
3. Open a photo, click **Edit**, and look for the **Restyle** or style options in the toolbar.
4. Fully close and reopen Photos — new AI tools sometimes need a fresh launch after updating.
5. If no Store update appears, check **Settings > Windows Update** — some Photos AI features gate on OS build.

### Fix 4: Download the style models completely

The art-style diffusion models are large separate downloads via Windows Update. The Restyle option can stay hidden until they land — and they fail silently on metered connections or full disks.

1. Open **Settings > Windows Update** and install everything, watching for AI component entries.
2. Switch to unmetered Wi-Fi — Windows won't pull multi-GB AI models over metered connections.
3. Free up several GB of disk space if the drive is nearly full.
4. Leave the PC plugged in, on Wi-Fi, and idle for 1-2 hours — model downloads need idle background time.
5. Reopen Photos and check Edit tools — Restyle often appears mid-session once models arrive.

### Fix 5: Check region, language, and account

Restyle Image is region- and language-gated. With hardware, drivers, app, and models all correct, gating is the usual reason the option stays invisible.

1. Set **Windows display language** to **English (United States)** in **Settings > Time & language > Language & region**.
2. Set **Country or region** to **United States** (or another supported region).
3. Sign out and back in, then reopen Photos and check for Restyle.
4. Sign into the Store/Photos with your Microsoft account if prompted — AI features verify identity.
5. Check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) for current Copilot+ feature availability by region.

### Fix 6: Repair or reset the Photos app

When every gate checks out but Restyle stays missing, the Photos app's local data is corrupt — the last resort that fixes the genuinely puzzling cases.

1. Go to **Settings > Apps > Installed apps > Microsoft Photos > Advanced options**.
2. Click **Repair**, wait for the checkmark, and recheck for Restyle.
3. If repair fails, click **Reset** — your photos are safe; only app data clears.
4. Reopen Photos, let it re-index, and check the Edit toolbar.
5. Final measure: uninstall Photos and reinstall from the Microsoft Store for a fully clean state.

## Closing

Photos Restyle Image is gated four ways: Copilot+ hardware, NPU driver, Photos app version, and downloaded style models — plus region gating on top. Verify eligibility first so you never chase the impossible, then work the list in order. When all gates open, the option just appears — pick a style and watch the NPU repaint your photo entirely on-device.
