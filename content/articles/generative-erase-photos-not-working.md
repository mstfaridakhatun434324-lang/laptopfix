---
title: "How to Fix Generative Erase Not Working in Windows Photos"
slug: generative-erase-photos-not-working
date: 2026-10-20
categories: ["ai-pc"]
tags: ["generative erase", "photos app", "troubleshooting", "ai pc", "generative erase not working", "windows 11"]
description: "Generative Erase missing or grayed out in the Windows Photos app? This guide covers the Copilot+ PC, NPU, and app-update requirements, plus step-by-step fixes."
thumbnail: "/images/thumbs/generative-erase-photos-not-working.webp"
faqs:
  - q: "Why is Generative Erase grayed out in the Photos app?"
    a: "Generative Erase is usually grayed out because your PC does not meet the Copilot+ PC hardware bar — a 40+ TOPS NPU, recent Windows 11 build, and current Photos app. An outdated NPU driver can also disable it. Work through the checks below to find which requirement is failing."
  - q: "Does Generative Erase require a Copilot+ PC?"
    a: "Yes. Microsoft gates Generative Erase behind Copilot+ PC hardware because the feature runs its inpainting model on the NPU. PCs without a qualifying NPU will not see the option at all. If your laptop has an NPU but the feature is still missing, the driver or Photos app is the likely culprit, not the hardware."
  - q: "Can I use Generative Erase without an internet connection?"
    a: "Yes. Generative Erase runs entirely on-device using your laptop's NPU, so it works offline once it is enabled. If the tool only works while you are online, something else is wrong — most likely the Photos app fell back to an older cloud-assisted edit path. Updating the app normally restores the on-device NPU version."
  - q: "Generative Erase worked before but stopped after an update. What happened?"
    a: "Windows or driver updates occasionally break the NPU stack that Photos depends on. A driver rollback, a reinstalled NPU driver, or repairing the Photos app usually brings it back. Check your NPU status in Task Manager before reinstalling anything."
---

Generative Erase is the AI-powered object remover inside the Microsoft Photos app. You brush over an unwanted person, sign, or photobomber, and the NPU fills the area with a plausible background in seconds. It only runs on Copilot+ PCs with a qualifying NPU.

When it stops working, the symptoms are vague. The option may be grayed out, missing entirely, or it may throw an error the moment you apply a brush stroke. Because Generative Erase sits at the intersection of the Photos app, Windows 11, and your NPU driver, any one of those layers can silently break it.

This guide walks you through the full diagnosis. You will confirm your PC actually qualifies, bring the app and OS up to date, repair the NPU driver stack, and fix the app itself — in that order, so you stop as soon as the feature comes back.

## Why this happens

- **Your PC is not a Copilot+ PC:** Generative Erase requires a 40+ TOPS NPU, and PCs below that bar never get the option.
- **The Photos app is outdated:** the feature only appears in recent Photos releases delivered through the Microsoft Store.
- **Windows 11 is behind:** older builds lack the NPU runtime components Photos depends on.
- **The NPU driver is broken or missing:** if Device Manager or Task Manager cannot see the NPU, Photos cannot use it either.
- **App data is corrupted:** a damaged Photos installation can hide or disable editing features after an update.
- **Region or account restrictions:** some AI features roll out by region or require a signed-in Microsoft account.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your PC meets the Copilot+ requirements

Before changing anything, verify the hardware bar, because no software fix can add an NPU your laptop does not have. Open Task Manager, switch to the Performance tab, and look for an NPU entry alongside CPU, GPU, and memory. Clicking it should show TOPS numbers and driver details. If there is no NPU tile at all, start by ruling out [NPU detection problems](/articles/npu-not-detected-windows-11/) before continuing with this guide. Also confirm you are running Windows 11 on a supported build by checking Settings, then System, then About.

1. Press Ctrl + Shift + Esc to open Task Manager.
2. Switch to the Performance tab and look for an NPU tile.
3. Click the NPU tile and note the driver version and TOPS figure.
4. Open Settings, then System, then About to confirm Windows 11.
5. If no NPU appears, follow an NPU detection guide first.

### Fix 2: Update the Photos app from the Microsoft Store

Generative Erase ships inside the Photos app itself, not inside Windows, so an old app version is the single most common cause of a missing button. Microsoft updates Photos through the Store independently of Windows Update, which means your OS can be current while Photos lags months behind. Open the Microsoft Store, check your library for pending updates, and install the latest Photos release. Restart the app afterward and reopen the editor to check whether the Erase tool has appeared.

1. Open the Microsoft Store from the Start menu.
2. Click Library in the lower-left corner of the Store window.
3. Click Get updates and wait for the scan to finish.
4. Install the Microsoft Photos update if one is listed.
5. Reopen Photos and check the editing toolbar for Generative Erase.

### Fix 3: Install the latest Windows 11 updates

The NPU runtime that Photos calls into is part of Windows 11, and older builds simply do not expose the interfaces newer Photos versions expect. Feature updates in particular add the DirectML and NPU execution plumbing that AI editing tools need, and the same class of problem shows up when [DirectML is not using the NPU](/articles/directml-not-using-npu-windows-11/). Go to Settings, then Windows Update, and install everything offered, including optional driver updates. Reboot when prompted and retest Generative Erase afterward.

1. Open Settings and go to Windows Update.
2. Click Check for updates and install all available updates.
3. Expand Advanced options and install any optional driver updates.
4. Restart your laptop when Windows prompts you to.
5. Open Photos and test Generative Erase again.

### Fix 4: Update or reinstall the NPU driver

A corrupted or outdated NPU driver breaks every AI feature that touches it. This is worth checking even when Task Manager shows the NPU, because a driver can be present yet fail to serve inference requests. Get the latest driver from your laptop maker's support page or the chip vendor's site — [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) handles Intel AI Boost systems automatically. If the newest driver does not help, uninstall the NPU device in Device Manager and let Windows reinstall it cleanly.

1. Open Device Manager and expand the Neural processors section.
2. Right-click your NPU and choose Update driver, then search automatically.
3. If that fails, download the latest driver from your vendor's support site.
4. As a last resort, uninstall the device and restart to reinstall it.
5. Open Task Manager and confirm the NPU tile is healthy again.

### Fix 5: Repair or reset the Photos app

When the OS and drivers are healthy but the button is still missing or crashes on use, the Photos installation itself is suspect. Windows lets you repair Store apps without losing data, which fixes most corrupted-app cases in under a minute. If repair does not work, a reset clears the app's local data and restores its defaults — you will keep your photos, which live in your Pictures folder, not inside the app. Similar on-device AI tools can fail the same way, so if photo enhancement is broken more broadly, compare with our guide to [Super Resolution not working in Photos](/articles/super-resolution-photos-not-working/).

1. Open Settings, then Apps, then Installed apps.
2. Find Microsoft Photos in the list and click the three-dot menu.
3. Choose Advanced options to open the app's settings page.
4. Click Repair, wait for the checkmark, and retest the feature.
5. If it still fails, return and click Reset, then reopen Photos.

## Closing

Generative Erase fails for boring, fixable reasons far more often than for broken hardware: an old Photos build, a stale NPU driver, or a Windows release that predates the feature. Work the list from the top, and in most cases the tool reappears by Fix 3 or Fix 4 without any drastic measures.
