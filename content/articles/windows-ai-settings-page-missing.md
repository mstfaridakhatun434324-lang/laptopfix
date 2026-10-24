---
title: "How to Fix the Missing AI Settings Page on Windows 11"
slug: windows-ai-settings-page-missing
date: 2026-10-24
categories: ["ai-pc"]
tags: ["ai settings", "windows 11", "copilot+ pc", "generative ai", "settings missing", "troubleshooting"]
description: "AI settings page missing from Windows 11? Learn why the page hides itself — Copilot+ hardware gates, broken feature packs, policies — and restore it fully."
thumbnail: "/images/thumbs/windows-ai-settings-page-missing.webp"
faqs:
  - q: "Where is the AI settings page supposed to be in Windows 11?"
    a: >
      On a qualifying Copilot+ PC it appears in Settings as its own section covering generative AI features such as Recall and Click to Do. If the hardware gate fails or the AI component pack is missing, the page hides itself instead of showing an error.
  - q: "Does every Windows 11 laptop get the AI settings page?"
    a: >
      No. Microsoft gates it to Copilot+ PCs — machines with a 40+ TOPS NPU running a current Windows 11 build. A regular Windows 11 laptop without that hardware never shows the page, and no setting legitimately changes that.
  - q: "Can a Windows update remove the AI settings page?"
    a: >
      It can hide it temporarily. Feature updates sometimes replace the AI component pack or reset the eligibility check, and the page vanishes until the components reinstall. Updating fully and repairing the pack, as described below, brings it back.
  - q: "Will reinstalling Windows bring the page back?"
    a: >
      Only if the cause was software corruption. If your laptop is not a Copilot+ PC, a clean install changes nothing — the hardware gate still fails. Confirm your NPU meets the 40 TOPS requirement before the nuclear option.
---

You open Settings expecting the AI section — the page controlling generative AI features, Recall, and Click to Do — and it simply is not there. No error, no warning, just a Settings app carrying on like the page never existed. It is an irritating kind of bug because there is nothing to click, and every guide online assumes the page is already open. You start wondering whether your laptop was ever supposed to have it, or whether an update quietly removed it.

The page does not appear for everyone by design. Microsoft gates it behind a Copilot+ PC check: a 40+ TOPS NPU, a current Windows 11 build, and the AI component pack delivered through the Microsoft Store. If any of those three fails, the page hides itself instead of showing an error. Group policies, registry edits from debloating tools, and region restrictions give a capable machine even more ways to hide a page it should show.

The fixes below run from simplest to most involved: confirm the hardware qualifies, update Windows fully, repair the AI components, check the NPU driver, then inspect hiding policies. A quick triage helps — if [Click to Do is missing entirely](/articles/click-to-do-missing/) too, the same broken component pack is the likely culprit, and the middle fixes here cover both. If other AI features misfire as well, like the [Snipping Tool's text extractor not working](/articles/snipping-tool-text-extractor-not-working/), that points to the same root cause. And if the missing page is one of several surprises on a new machine — say [League of Legends misbehaving on ARM Windows](/articles/league-of-legends-arm-windows-issues/) — the update and driver steps below apply there too.

## Why this happens

- **Copilot+ PC hardware gate:** The page only renders on machines with a 40+ TOPS NPU, checked at every boot. Weaker NPUs never show the page, regardless of software.
- **Windows build is too old:** The section arrived with specific Windows 11 feature builds. Paused or stuck updates mean the Settings app lacks the page definition entirely.
- **AI component pack missing or corrupt:** Store-delivered AI components feed the page. If the pack failed to install, was removed by a debloater, or corrupted during an update, the page hides itself.
- **Group policy or registry blocks:** Enterprise policies and privacy scripts can disable the AI settings surface. A single registry value can suppress the page machine-wide.
- **NPU driver missing or disabled:** A warning-flagged NPU in Device Manager, or one disabled in BIOS, fails the eligibility check — Windows then treats the machine as a non-AI PC.
- **Region or language restrictions:** The page and its features are withheld in some regions, or when the system language is not on the supported list.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your laptop is actually a Copilot+ PC

Verify the hardware qualifies before touching software — half of all "missing page" reports end here, and no fix conjures a missing NPU.

1. Check your laptop's spec sheet for "Copilot+ PC" branding and an NPU rated at 40 TOPS or higher.
2. Open Task Manager's Performance tab and look for an NPU tile; no tile usually means the required hardware is absent.
3. In Device Manager, confirm the NPU entry under Neural processors shows no warning icon.
4. If the hardware does not qualify, stop here — the page is hidden by design and nothing below changes that.

### Fix 2: Bring Windows fully up to date

The page definition ships with current Windows 11 builds, so an outdated machine may simply predate it. Microsoft's [Windows 11 support hub](https://support.microsoft.com/en-us/windows) covers the update process if anything below misbehaves.

1. Open **Settings > Windows Update**, click **Check for updates**, and install everything offered, including optional driver updates.
2. Restart when prompted, then check again — repeat until Windows reports you are fully up to date.
3. Open the Microsoft Store, go to Library, and update all apps, since the AI component pack arrives through the Store.
4. Reopen Settings and check for the AI section; updates alone resolve a large share of these cases.

### Fix 3: Repair or reinstall the AI components

If updates did not help, the component pack itself is the likely culprit — these steps force Windows to fetch a clean copy.

1. Open **Settings > Apps > Installed apps**, search for AI, Copilot, or Recall entries, and use the three-dot menu to repair them.
2. In the Microsoft Store, search for AI component updates for your device and install any that appear.
3. If repair is not offered, uninstall the broken component and reinstall it from the Store for a clean package.
4. Restart the laptop and check Settings again — the page often reappears one boot after the components land.

### Fix 4: Verify the NPU driver is healthy

A warning-flagged or generic NPU driver fails the eligibility check silently. Your laptop maker's support site carries the validated package; on Intel machines the [Intel driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) confirms what you need.

1. In Device Manager, expand Neural processors and look for warning icons on the NPU entry.
2. If flagged, update the driver using the package from your manufacturer's support page.
3. If no NPU entry exists, check the BIOS for an NPU or AI accelerator toggle and enable it.
4. After a clean install with no warnings, restart and recheck Settings for the AI page.

### Fix 5: Check policies, region settings, and the Settings app itself

Debloating scripts, enterprise policies, and region mismatches are the quiet culprits. Inspect first, and back up anything you change.

1. Press Win + R, type `gpedit.msc`, and check the Windows AI and Recall policy nodes for anything explicitly disabled.
2. In Registry Editor, inspect AI-related keys under the Windows policies hive; export a backup (File > Export) before changing any value.
3. Open **Settings > System > Region** and confirm your region and language match a region where AI features are supported.
4. Create a fresh local user account and check for the AI page there — if it appears, your main profile is the problem, not the system.
5. As a last resort, use **Settings > System > Recovery** to reinstall Windows while keeping files, but only after Fix 1 confirmed the hardware qualifies.

## Closing

A missing AI settings page feels like a mystery, but it is almost always one of three things: hardware that never qualified, an update or component pack that did not finish, or a policy quietly suppressing the surface. Work the list in order and you will find which one applies within an hour — and if the hardware simply is not a Copilot+ PC, at least you will know for certain instead of chasing a page that was never meant to appear.
