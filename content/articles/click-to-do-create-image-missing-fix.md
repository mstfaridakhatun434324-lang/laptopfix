---
title: "How to Fix the Missing Create Image Action in Click to Do"
slug: click-to-do-create-image-missing-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["click to do", "create image", "image generation", "copilot+ pc", "windows 11", "npu"]
description: "Bring back the missing Create image action in Click to Do with fixes for NPU drivers, image model downloads, feature settings, and Windows update repair."
thumbnail: "/images/thumbs/click-to-do-create-image-missing-fix.webp"
faqs:
  - q: "Why is Create image missing but Rewrite and Summarize still work?"
    a: "Create image is the only Click to Do action that needs the on-device image model and full NPU support. Text actions can run without it, so when the image model or NPU driver fails, Create image vanishes while text actions keep working."
  - q: "Does Create image need an internet connection?"
    a: "No, on a Copilot+ PC the image generation runs on-device using the NPU. A missing model download or a disabled NPU blocks it even with a perfect internet connection, so connectivity is rarely the fix."
  - q: "Can I get Create image on a non-Copilot+ PC?"
    a: "No. Create image in Click to Do requires the Copilot+ PC NPU and the downloaded image model. On other PCs the action simply does not appear, which is expected behaviour rather than a fault."
  - q: "Will resetting Click to Do delete my generated images?"
    a: "No, images you already saved stay in your Pictures folder or wherever you saved them. Resetting the feature or reinstalling its components only affects the menu and models, not your saved files."
---

Click to Do opens fine, Rewrite and Summarize are right where they should be — but Create image is gone. You select text, the menu appears, and the one action you actually wanted is simply not listed.

Create image is the most demanding Click to Do action: it needs your NPU, a downloaded image model, free disk space, and power headroom. Text actions can survive a broken NPU driver; image generation cannot, so it disappears first and returns last.

This guide targets the image pipeline specifically: settings, drivers, the model itself, and the power and storage conditions that gate it. Work through the fixes in order and check the Click to Do menu after each one.

## Why this happens

- **Image model not downloaded or corrupted:** The on-device image model downloads separately after setup or an update; if that download failed or was interrupted, Create image cannot appear.
- **NPU driver replaced or outdated:** A generic or old NPU driver may still handle text actions while failing the image workload, which hides Create image first.
- **Click to Do image actions disabled:** Feature settings, privacy settings, or a device policy can disable image generation while leaving text actions untouched.
- **Battery saver or low-power mode active:** Image generation is power-gated on many Copilot+ PCs, so battery saver or a low battery can suppress Create image until the PC is plugged in.
- **Low disk space blocking the model:** The image model needs free space to download and run; a nearly full drive can stall the download silently.
- **Windows update left the AI components mismatched:** A major update can leave the Click to Do menu on a newer build than its image model, and the mismatched action simply does not load.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Plug in, charge up, and check the basics

Image generation is the first feature power management sacrifices, so rule out the power and storage gates before any driver work.

1. Plug in the charger and wait until the battery is above 20 percent — do not test on a nearly dead battery.
2. Open **Settings > System > Power & battery** and turn off **Battery saver**, setting **Power mode** to **Best performance** or **Balanced**.
3. Check free space in **Settings > System > Storage**; free up at least 10 GB if the drive is nearly full.
4. Restart the PC on AC power, open Notepad, type a sentence, select it, and open Click to Do to look for Create image.
5. If the action returns on AC power, power gating was the cause — keep the charger connected when generating images. A similar power-sensitive disappearance affects other menus, as in [Click to Do image actions not working](/articles/click-to-do-image-actions-not-working/), where the whole image set fails together.

### Fix 2: Confirm image actions are enabled in settings

Before assuming the model is broken, confirm Windows is actually allowed to show image actions. A toggled setting or a reverted privacy default after an update can hide Create image with no other symptom at all.

1. Open **Settings > System > Click to Do** and confirm the feature is **On** and that image-related options, if listed separately, are enabled.
2. Open **Settings > Privacy & security** and review the AI-feature and app-permission settings for your device.
3. Make sure you are signed in with your Microsoft account, since some AI features check sign-in state before loading.
4. Toggle Click to Do off, restart the PC, toggle it back on, and test again — the toggle forces the menu and its actions to re-register.
5. If other actions appear but Create image still does not, the menu is fine and the image model or NPU is the fault — continue below. The next action in the chain, [Click to Do Ask Copilot missing](/articles/click-to-do-ask-copilot-missing-fix/), fails in a similar selective way when its own backend does not load.

### Fix 3: Restore the NPU driver from your PC maker

Text actions can limp along on a generic driver, but image generation cannot. If Windows Update swapped your NPU driver, restoring the PC maker's validated driver is the fix most likely to bring Create image back.

1. Open **Device Manager > Neural processors** and note the driver name, version, and date.
2. Download the latest NPU and chipset drivers for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Install the NPU driver, restart when prompted, and do not interrupt the install or let the PC sleep mid-way.
4. After the restart, open Click to Do on selected text and check for Create image — give it up to a minute on first load while the model initialises.
5. If the driver installer refuses, saying a newer driver is already installed, uninstall the Neural processor device in Device Manager first (without deleting files if asked), restart, and then run the maker's installer.

### Fix 4: Force the image model to re-download

If the driver is correct but Create image is still missing, the model itself is the suspect. Windows does not always retry a failed model download on its own, so you need to trigger the conditions that make it try again.

1. Confirm at least 10 GB of free disk space and a stable internet connection, then plug in the charger.
2. Open **Settings > Windows Update** and install any pending updates, including optional AI-component updates.
3. Toggle Click to Do off, restart, toggle it on again, and leave the PC idle on AC power for thirty minutes so background downloads can run.
4. Test Click to Do again. If Create image appears but generation fails, the model may be partly downloaded — leave the PC idle longer and test again later.
5. If nothing changes after a full day of idle time, run the system repair in Fix 6 before concluding the model is unrecoverable — a damaged Windows component can block the download silently.

### Fix 5: Test image generation in a second app

Create image can be missing from one app's menu while working elsewhere. Testing a second app tells you whether the image pipeline is broken everywhere or only in one place.

1. Test Click to Do in Notepad first, then in a screenshot: press **Windows + Shift + S**, capture a region, and open Click to Do on the screenshot.
2. If Create image appears on the screenshot but not on selected text, the text path is the problem — update the app where it fails and test again.
3. If Create image is missing in both places, the problem is system-wide: return to the driver and model fixes above rather than reinstalling apps.
4. Try a different user profile on the same PC: sign in as another user, open Notepad, and test Click to Do there to rule out profile corruption.
5. If it works under the new profile, your original profile's Click to Do state is damaged — migrate to a fresh profile. See also [Grammarly issues on ARM Windows](/articles/grammarly-arm-windows-issues-fix/).

### Fix 6: Repair Windows AI components with system tools

When the driver, model, and settings are all correct but Create image still refuses to appear, the Windows AI components themselves need repair. The built-in tools rebuild damaged files without removing your documents or apps.

1. Right-click **Start**, choose **Terminal (Admin)**, and run `DISM /Online /Cleanup-Image /RestoreHealth`, waiting for it to complete.
2. When DISM finishes, run `sfc /scannow` in the same window and restart afterwards.
3. After the restart, install any pending Windows updates and restart once more.
4. Leave the PC idle on AC power for thirty minutes to let any model download complete, then test Click to Do.
5. If Create image is still missing, an in-place repair install of Windows 11, choosing **Keep personal files and apps**, is the final step.

## Closing

Create image vanishes first because it is the hardest-working Click to Do action — it needs the NPU, the model, power, and disk space all at once. Plug in, restore the maker's NPU driver, give the model time to download, and repair Windows if needed, and the action should return to the menu.
