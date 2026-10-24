---
title: "How to Fix Paint Cocreator Not Working on Windows 11"
slug: paint-cocreator-not-working
date: 2026-10-24
categories: ["ai-pc"]
tags: ["paint", "cocreator", "ai-image-generation", "copilot-plus", "troubleshooting"]
description: "Paint Cocreator missing or failing on Windows 11? Fix Copilot+ eligibility, NPU drivers, Paint updates, AI model downloads, and region settings step by step."
thumbnail: "/images/thumbs/paint-cocreator-not-working.webp"
faqs:
  - q: "Why is Cocreator missing from Paint?"
    a: >
      Cocreator in Paint requires a Copilot+ PC, the latest Paint from the Microsoft Store, and downloaded AI models. Missing any one hides the feature — check all three in order.
  - q: "Does Paint Cocreator need internet?"
    a: >
      Only for the initial AI model download. Generation itself runs on the NPU entirely offline once the models are on your device.
  - q: "Why does Paint Cocreator say 'Something went wrong'?"
    a: >
      This usually means the AI models haven't finished downloading or the NPU driver glitched. Check Windows Update for AI components and verify the NPU in Device Manager.
  - q: "Is Paint Cocreator free?"
    a: >
      Yes — on Copilot+ PCs it runs on-device with no credits or subscription. Sketch plus a text prompt generates the image locally on your NPU.
---

Paint's Cocreator is the delightful one — scribble a rough sketch, type what you're imagining, and the NPU paints it into something real. Except your Paint has no Cocreator button. Or it has the button and every generation fails. The feature that was supposed to make Paint fun again is just... not there.

Paint Cocreator is a Copilot+ exclusive: it runs a diffusion model on the NPU, combining your sketch with a text prompt. That means four gates: qualifying hardware, a healthy NPU driver, the latest Paint from the Store, and the downloaded AI models — plus region gating. Miss any one and Cocreator hides or fails, usually without a helpful message.

This guide fixes Paint Cocreator in technician order: eligibility first, then NPU driver, then the Paint app, then model downloads, then region, and finally app repair. The same NPU-first logic applies across AI PCs — our [Docker Desktop on ARM issues guide](/articles/docker-desktop-arm-windows-issues/) covers the shared platform stack, and [ExpressVPN on ARM64](/articles/expressvpn-arm64-windows-not-working/) shows the same driver-maturity pattern — while [HP EliteBook Ultra AI PC problems](/articles/hp-elitebook-ultra-ai-pc-problems/) cover the broader business-laptop picture.

## Why this happens

- **Not a Copilot+ PC:** Paint Cocreator requires a qualifying NPU. Non-qualifying hardware never gets the feature — intentional gating, not a bug.
- **NPU driver missing or broken:** On qualifying hardware, a bad NPU driver prevents the AI runtime from initializing — Cocreator stays hidden.
- **Outdated Paint app:** Cocreator arrived via Microsoft Store updates to Paint. The inbox version lacks it entirely.
- **AI models not downloaded:** The diffusion models are separate Windows Update downloads. Without them, Cocreator fails or hides.
- **Region or language gating:** Cocreator availability is gated on region and display language.
- **Insufficient RAM:** Copilot+ needs 16GB minimum — some qualifying-chip configurations with less RAM miss AI features.
- **Corrupted Paint app data:** Damaged local state can break the AI path while basic painting works fine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify Copilot+ eligibility honestly

Thirty seconds here prevents hours of futile fixing. Paint Cocreator cannot be enabled on non-Copilot+ hardware by any setting, update, or trick.

1. Open **Settings > System > About** and look for Copilot+ PC branding.
2. Open **Device Manager > Neural processors** — the NPU must be present with no warning icon.
3. Check RAM in Task Manager's **Performance** tab — 16GB minimum for Copilot+.
4. If any check fails, stop — the alternative is the Photos app's cloud features or a browser-based image generator.
5. If all pass and Cocreator is missing, continue — it's drivers, app, models, or region.

### Fix 2: Fix the NPU driver

On qualifying hardware, the NPU driver is the gatekeeper. Get it from your laptop maker — generic driver packages miss OEM customizations that the AI runtime depends on.

1. Inspect **Device Manager > Neural processors** for warning icons.
2. Download the NPU/chipset driver from your laptop maker's support site for your exact model.
3. If the driver looks healthy, uninstall it anyway (check **"Delete the driver software"**) and reinstall — silent corruption hides behind clean status.
4. Restart and confirm the NPU enumerates without warnings.
5. Run **Windows Update** with optional updates — AI runtime components frequently arrive this way.

### Fix 3: Update Paint from the Microsoft Store

Cocreator is Store-delivered. The inbox Paint doesn't have it, and stalled Store updates are the most common fixable cause.

1. Open **Microsoft Store > Library > Get updates** and wait for **Paint** to finish updating.
2. Open Paint and look for the **Cocreator** button in the toolbar (brush/sparkle icon) — it appears in recent builds.
3. Check Paint's version via its settings — Cocreator needs the 2024+ Store builds.
4. Fully close Paint and reopen it — new AI tools sometimes need a fresh launch.
5. If no update appears, check **Settings > Windows Update** — some Paint AI features gate on the OS build.

### Fix 4: Download the AI models completely

The diffusion models behind Cocreator are large separate downloads. The button can hide until they arrive — and downloads stall silently on metered connections or full disks.

1. Open **Settings > Windows Update** and install everything, watching for AI component entries.
2. Use unmetered Wi-Fi — Windows won't fetch multi-GB AI models over metered connections.
3. Free several GB of disk space if needed.
4. Leave the PC plugged in, on Wi-Fi, and idle for 1-2 hours for background downloads to complete.
5. Reopen Paint and check the toolbar — Cocreator often appears without needing a restart.

### Fix 5: Check region, language, and account

With hardware, drivers, app, and models all correct, region/language gating is the usual invisibility cause — no error, just a missing button.

1. Set **Windows display language** to **English (United States)** in **Settings > Time & language > Language & region**.
2. Set **Country or region** to **United States** (or another supported region).
3. Sign out and back in, then reopen Paint.
4. Sign into the Store with your Microsoft account if prompted — AI features verify identity.
5. Check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) for current Copilot+ availability by region.

### Fix 6: Repair or reset Paint

When every gate checks out, Paint's local data is corrupt — the last resort for the genuinely puzzling cases where the AI path breaks but painting works.

1. Go to **Settings > Apps > Installed apps > Paint > Advanced options**.
2. Click **Repair**, wait for the checkmark, and recheck for Cocreator.
3. If repair fails, click **Reset** — your saved images are files on disk; only app data clears.
4. Reopen Paint and look for the Cocreator button.
5. Final measure: uninstall Paint and reinstall from the Microsoft Store for a completely clean state.

## Closing

Paint Cocreator is gated five ways: Copilot+ hardware, NPU driver, Paint version, downloaded AI models, and region — with app corruption as the rare sixth. Verify eligibility first so you never chase the impossible, then work the list in order. When the gates open, Cocreator just appears — sketch roughly, describe clearly, and let the NPU do the painting.
