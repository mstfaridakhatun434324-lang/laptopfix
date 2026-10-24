---
title: "How to Fix Photos App Cocreator Not Working on Windows 11"
slug: photos-cocreator-not-working
date: 2026-10-24
categories: ["ai-pc"]
tags: ["photos-app", "cocreator", "ai-image-generation", "copilot-plus", "troubleshooting"]
description: "Photos Cocreator missing or failing on Windows 11? Fix NPU drivers, Photos app updates, AI model downloads, and region settings to restore AI image creation."
thumbnail: "/images/thumbs/photos-cocreator-not-working.webp"
faqs:
  - q: "Why is Cocreator missing from my Photos app?"
    a: >
      Cocreator requires a Copilot+ PC with a working NPU, the latest Photos app from the Microsoft Store, and the downloaded AI models. Missing any one of the three hides the feature entirely.
  - q: "Does Cocreator work without internet?"
    a: >
      Yes, on Copilot+ PCs — Cocreator runs on the NPU with on-device models once they've downloaded. The initial model download needs internet, but generation itself works offline.
  - q: "Why does Cocreator say 'Something went wrong'?"
    a: >
      This usually means the AI models haven't finished downloading, the NPU driver glitched, or the app needs an update. Check Windows Update for AI components and update Photos from the Store.
  - q: "Is Cocreator free to use?"
    a: >
      Yes — on Copilot+ PCs, Cocreator uses on-device AI at no cost with no credit system. It's one of the genuinely free AI features, unlike some cloud-based image generators.
---

You open the Photos app, ready to sketch something and watch Cocreator turn it into art — and the Cocreator button isn't there. Or it is there, but clicking it gives you a spinner, an error, or a blank panel. Microsoft's on-device image generation was supposed to be the fun Copilot+ demo, and yours won't even start.

Cocreator is the Photos app's text-to-image and sketch-to-image feature, powered by a diffusion model running on your PC's NPU. That means three things must align: Copilot+ capable hardware with a healthy NPU driver, the latest Photos app from the Store, and the downloaded AI model files. Miss any one and Cocreator silently vanishes or fails — with almost no useful error message.

This guide fixes Cocreator in technician order: hardware eligibility first, then the NPU driver, then the Photos app itself, then the AI model downloads, then region and account issues, and finally the app-repair layer. The same NPU-first logic applies across AI PCs — our [RTX Video Super Resolution guide](/articles/rtx-video-super-resolution-not-working/) covers the shared GPU/AI driver stack, and [Brother printer drivers on ARM](/articles/brother-printer-driver-arm-windows/) show the same driver-maturity pattern — while the [Dell Inspiron 14 Plus AI issues](/articles/dell-inspiron-14-plus-ai-issues/) rundown covers the broader platform health.

## Why this happens

- **Not a Copilot+ PC:** Cocreator's on-device model requires an NPU meeting the Copilot+ spec (40+ TOPS). Older or non-qualifying hardware simply doesn't get the feature — no setting changes this.
- **NPU driver missing or broken:** Even on qualifying hardware, a missing or corrupted NPU driver means the AI runtime can't initialize — Cocreator hides itself rather than erroring.
- **Outdated Photos app:** Cocreator arrived in Photos via Store updates. The inbox version or a stalled update lacks the feature entirely.
- **AI models not downloaded:** The diffusion model files are separate downloads via Windows Update. Without them, Cocreator's button may appear but generation fails.
- **Region or language gating:** Cocreator availability is gated on region and display language — unsupported configurations hide the feature with no explanation.
- **Corrupted Photos app data:** A damaged app cache can break just the AI features while basic photo viewing works fine.
- **Conflicting GPU driver state:** On some configurations, a broken GPU driver interferes with the AI runtime's initialization even though generation runs on the NPU.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Copilot+ eligibility honestly

Before troubleshooting, verify your PC actually qualifies — Cocreator is exclusive to Copilot+ PCs, and no driver update brings it to older hardware. This check takes thirty seconds and prevents hours of futile fixing.

1. Open **Settings > System > About** and look for Copilot+ PC branding or an NPU entry in the processor details.
2. Open **Device Manager > Neural processors** — the NPU must be present with no warning icon.
3. Check your RAM: Copilot+ requires 16GB minimum — some configurations with qualifying chips but 8GB RAM don't get all features.
4. If your PC genuinely isn't Copilot+, stop here — Cocreator isn't available, and the honest alternative is a cloud image generator in your browser.
5. If it IS Copilot+ and Cocreator is missing, continue — it's a driver, app, or components problem.

### Fix 2: Fix the NPU driver

On qualifying hardware with a broken or missing NPU driver, the AI runtime never initializes and Cocreator stays hidden. The driver must come from your laptop maker, not a generic package.

1. In Device Manager, check **Neural processors** for warning icons — a yellow triangle means the driver is broken.
2. Download the NPU/chipset driver from your laptop maker's support site (Dell, HP, Lenovo, ASUS, Samsung, Acer) for your exact model.
3. If the driver looks fine but Cocreator fails, uninstall it from Device Manager (check **"Delete the driver software"**) and reinstall fresh — corruption hides behind "working" status.
4. Restart and re-verify the NPU appears cleanly.
5. Open **Settings > Windows Update** and install optional driver updates — the AI runtime components often arrive this way.

### Fix 3: Update the Photos app from the Microsoft Store

Cocreator lives in the Store version of Photos, not the inbox version — and Store updates stall more often than people realize. This is the most common fix after the NPU driver.

1. Open the **Microsoft Store**, go to **Library**, and click **Get updates** — wait for **Microsoft Photos** to finish updating.
2. Open Photos, click the **Settings** gear, and check the version — Cocreator needs a recent 2024+ build.
3. Look for the **Cocreator** icon in the Photos toolbar (the paintbrush/sparkle icon) — it appears once the app version supports it.
4. If the Store shows no Photos update, check **Settings > Windows Update** — some Photos features gate on OS build versions.
5. Still missing? The AI models (Fix 4) may be the actual blocker — the button sometimes hides until models arrive.

### Fix 4: Let the AI models download completely

Cocreator's diffusion model is a large download that arrives via Windows Update in the background — and it fails silently on metered connections, low disk space, or interrupted downloads. No models, no generation.

1. Open **Settings > Windows Update** and check for a pending **AI components** or model download — install everything offered.
2. Ensure you're on unmetered Wi-Fi — Windows won't download multi-hundred-megabyte AI models over a metered connection.
3. Check free disk space — the models need several GB; clear space if the drive is nearly full.
4. Leave the PC plugged in, on Wi-Fi, and idle for 1-2 hours — model downloads resume in the background but need idle time.
5. Reopen Photos and check for Cocreator — the button often appears mid-session once models land, no restart needed.

### Fix 5: Check region, language, and account

Cocreator is region- and language-gated like other Copilot+ AI features. A non-English display language or unsupported region hides it with zero feedback — maddening, but fixable in a minute.

1. Open **Settings > Time & language > Language & region** — set **Windows display language** to **English (United States)**.
2. Set **Country or region** to **United States** (or another supported region) on the same page.
3. Sign out and back in so the language change fully applies, then reopen Photos.
4. Sign into the Photos app / Microsoft Store with your Microsoft account if prompted — some AI features check identity.
5. Check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) for current Cocreator availability by region — the list expands over time.

### Fix 6: Repair or reset the Photos app

When hardware, drivers, app version, models, and region are all correct, the Photos app's own data is usually corrupt — damaged cache breaks the AI path while photo viewing works fine. Repair is safe; reset is thorough.

1. Open **Settings > Apps > Installed apps**, find **Microsoft Photos**, click the three dots, then **Advanced options**.
2. Click **Repair** and wait for the checkmark, then reopen Photos and check for Cocreator.
3. If repair changes nothing, click **Reset** — this clears the app's data (your photo files are untouched, they're just files on disk).
4. Reopen Photos, let it re-index briefly, and check the toolbar for Cocreator.
5. As a last resort, uninstall Photos from Advanced options and reinstall it from the Microsoft Store — a clean install rules out every local-state cause.

## Closing

Photos Cocreator fails at one of six gates: Copilot+ eligibility, the NPU driver, the Photos app version, the AI model downloads, region/language gating, or corrupt app data. Verify eligibility first so you don't chase the impossible, then work the list in order. When all six gates are open, Cocreator just appears — sketch, describe, and generate, entirely on-device.
