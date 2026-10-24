---
title: "How to Fix Paint Generative Fill Not Working on Windows 11"
slug: paint-generative-fill-not-working
date: 2026-10-24
categories: ["ai-pc"]
tags: ["paint", "generative-fill", "ai-editing", "copilot-plus", "troubleshooting"]
description: "Paint Generative Fill grayed out or failing on Windows 11? Fix Copilot+ eligibility, NPU drivers, Paint updates, AI model downloads, and region settings."
thumbnail: "/images/thumbs/paint-generative-fill-not-working.webp"
faqs:
  - q: "What is Generative Fill in Paint?"
    a: >
      Generative Fill lets you select an area of your canvas and describe what should appear there — the AI generates matching content. It's a Copilot+ exclusive running on the NPU.
  - q: "Why is Generative Fill grayed out in Paint?"
    a: >
      The top causes are non-qualifying hardware, a stale Paint version, or missing AI models. All three gates must be open — check eligibility first, then update Paint.
  - q: "Does Generative Fill need internet?"
    a: >
      Only for the initial model download. Fill generation itself runs on the NPU offline once models are downloaded.
  - q: "Why does Generative Fill produce weird results?"
    a: >
      Vague prompts produce vague fills — describe the desired content specifically, keep selections reasonably sized, and give the AI clear surrounding context to blend with.
---

Generative Fill is Paint's most magical trick: lasso an empty patch of your image, type "a wooden fence," and the NPU paints one in, matched to the style and lighting. When it works, it feels like Photoshop's headline feature living in a free app. When the button is grayed out or every fill fails — it just feels broken.

Like Cocreator, Generative Fill is a Copilot+ exclusive running a diffusion model on the NPU. The gates are the same: qualifying hardware, healthy NPU driver, current Paint from the Store, downloaded AI models, and region settings. The failure signature is also the same — silent absence or grayed-out controls rather than useful errors.

This guide fixes Generative Fill in technician order: eligibility, NPU driver, Paint app, model downloads, technique, region, and app repair. The same NPU-first logic applies across AI PCs — our [Windows Sandbox on ARM guide](/articles/windows-sandbox-arm-laptop-not-working/) covers the shared platform stack, and [WireGuard on ARM](/articles/wireguard-arm-windows-issues/) shows the same driver-maturity pattern — while [Intel NPU driver update failures](/articles/intel-npu-driver-update-failed/) are worth reading if the driver itself won't install.

## Why this happens

- **Not a Copilot+ PC:** Generative Fill requires a qualifying NPU — non-qualifying hardware never gets it, by design.
- **NPU driver missing or broken:** On qualifying hardware, a bad NPU driver keeps the AI runtime from initializing.
- **Outdated Paint app:** Generative Fill arrived via Store updates — old Paint builds lack it.
- **AI models not downloaded:** The fill models are separate downloads; the tool grays out until they arrive.
- **Poor prompt or selection technique:** Vague prompts ("something nice") and huge selections produce bad fills that look like failures.
- **Region or language gating:** Availability is gated on region and display language.
- **Corrupted Paint data:** Damaged app state breaks the AI path while basic tools work.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify Copilot+ eligibility honestly

Generative Fill cannot be enabled on non-Copilot+ hardware — no setting, update, or workaround changes this. Verify before troubleshooting. This gate is absolute: the feature's diffusion model only runs on a qualifying NPU, so an ineligible PC will never show the option no matter what you update. Confirming this first keeps you from wasting an afternoon on fixes that can't work.

1. Check **Settings > System > About** for Copilot+ PC branding.
2. Confirm the NPU in **Device Manager > Neural processors** — present, no warnings.
3. Verify 16GB+ RAM in Task Manager's **Performance** tab.
4. If hardware doesn't qualify, stop — browser-based generative fill tools are the alternative.
5. If it qualifies and Fill is grayed out, continue — it's drivers, app, models, or region.

### Fix 2: Fix the NPU driver

The NPU driver gates every Paint AI feature. Source it from your laptop maker, and don't trust a "working" status blindly — reinstall if Fill stays gray. Device Manager can report a driver as working while its AI runtime components are actually broken, because the status reflects basic enumeration rather than the NPU's compute path. A clean reinstall from your laptop maker's package is the only way to be sure.

1. Check **Device Manager > Neural processors** for warning icons.
2. Download the NPU/chipset driver from your laptop maker's support site for your exact model.
3. Uninstall the existing driver (check **"Delete the driver software"**) and reinstall fresh to clear silent corruption.
4. Restart and verify clean NPU enumeration.
5. Run **Windows Update** with optional updates for AI runtime components.

### Fix 3: Update Paint from the Microsoft Store

Generative Fill is Store-delivered — the inbox Paint predates it, and stalled updates are the most common fixable cause of the grayed-out tool. Microsoft ships Paint's AI features exclusively through the Store, so the version bundled with Windows will never gain Generative Fill on its own. Store updates also stall silently in the background, so run a manual update check even if you believe updates are automatic.

1. Open **Microsoft Store > Library > Get updates**; wait for **Paint** to finish.
2. Open Paint and check for the **Generative Fill** option in the selection tools.
3. Confirm a recent Paint build in the app's settings — Fill needs 2024+ versions.
4. Close Paint fully and reopen — new tools sometimes need a fresh launch.
5. If no update appears, check **Settings > Windows Update** for OS-build gating.

### Fix 4: Download the AI models and master the technique

Two things live here: the model downloads that ungray the button, and the prompting technique that makes fills actually good. Both matter — a working button with bad technique still looks broken. The diffusion models are several gigabytes and arrive through Windows Update's AI components channel, which respects metered connections and low-disk conditions by simply not downloading. On the technique side, the model blends your prompt with the surrounding pixels, so the quality of that surrounding context matters as much as your words.

1. In **Settings > Windows Update**, install everything and watch for AI component downloads.
2. Use unmetered Wi-Fi with several GB free — model downloads stall otherwise.
3. Leave the PC plugged in and idle 1-2 hours for background downloads to finish.
4. When prompting, be specific: "a red brick wall in soft daylight" beats "wall" every time.
5. Keep selections moderate — fills work best on areas under a third of the canvas with clear surrounding context.

### Fix 5: Check region, language, and account

With everything else correct, gating hides the tool silently. This check takes a minute and resolves the "everything looks right but it's gray" cases. Microsoft rolls Copilot+ features out by region and language, and the gating is evaluated at sign-in — which is why a region change only takes effect after you sign out and back in. There's no in-app message explaining any of this, so gating is the classic invisible cause.

1. Set **Windows display language** to **English (United States)**.
2. Set **Country or region** to **United States** (or another supported region).
3. Sign out and back in, then reopen Paint.
4. Sign into the Store with your Microsoft account if prompted.
5. Check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) for current availability by region.

### Fix 6: Repair or reset Paint

The last resort for cases where every gate is open but Fill stays gray — corrupt app data breaking just the AI path. Corruption tends to strike the newest features first, because the AI code paths depend on cached model metadata that older features never touch. Repair preserves your settings and is quick; reset is more thorough and still leaves your image files alone.

1. Go to **Settings > Apps > Installed apps > Paint > Advanced options**.
2. Click **Repair**, wait for the checkmark, retest Fill.
3. If repair fails, click **Reset** — saved images are files on disk and are safe.
4. Reopen Paint and check the selection tools for Generative Fill.
5. Final measure: uninstall and reinstall Paint from the Microsoft Store.

## Closing

Paint Generative Fill is gated the same five ways as its sibling AI tools: Copilot+ hardware, NPU driver, Paint version, AI models, and region — plus technique as the human factor. Verify eligibility first, work the list in order, and prompt specifically once the tool is live. The NPU does remarkable fill work when you give it a clear selection and a clear description.
