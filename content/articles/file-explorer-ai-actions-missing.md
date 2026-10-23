---
title: "How to Restore Missing AI Actions in File Explorer on Windows 11"
slug: file-explorer-ai-actions-missing
date: 2026-10-23
categories: ["ai-pc"]
tags: ["file explorer", "ai actions", "windows 11", "copilot+ pc", "context menu"]
description: "AI Actions missing from File Explorer's right-click menu? Step-by-step fixes for Windows builds, NPU drivers, Microsoft account sign-in, and model downloads."
thumbnail: "/images/thumbs/file-explorer-ai-actions-missing.webp"
faqs:
  - q: "What are AI Actions in File Explorer?"
    a: >
      AI Actions are Copilot+ PC-exclusive right-click options in File Explorer, such as summarizing documents, removing image backgrounds, erasing objects from photos, and visual search. They run on the PC's NPU using on-device AI models.
  - q: "Why don't I see AI Actions when I right-click a file?"
    a: >
      The most common reasons are an outdated Windows 11 build, a missing or broken NPU driver, not being signed in with a Microsoft account, or the on-device AI models not having downloaded yet. All four must be in place.
  - q: "Do AI Actions work on non-Copilot+ PCs?"
    a: >
      No. AI Actions are exclusive to Copilot+ PCs with a qualifying NPU (40+ TOPS). They do not appear on standard Windows 11 PCs, even with the latest updates, because the on-device models they depend on cannot run there.
  - q: "Do AI Actions need an internet connection?"
    a: >
      Mostly no — once the on-device models are downloaded, actions like background removal and summarization run locally on the NPU. Visual search with Bing is the exception and needs internet because it queries the web.
---

You right-click a photo in File Explorer expecting the AI Actions menu — summarize, remove background, erase objects — and it is not there. No error, no grayed-out entry, just the ordinary context menu. On a Copilot+ PC that advertised these features, the absence feels like a broken promise.

AI Actions are a headline Copilot+ PC feature: right-click options powered by on-device AI models running on the NPU. They depend on a whole stack — a new-enough Windows 11 build, a working NPU driver, a Microsoft account sign-in, and downloaded AI models — and any single broken layer hides the entire menu, with no error pointing at the culprit.

This guide gives you six fixes in order: build and eligibility checks, the NPU driver, sign-in, model downloads, and a shell reset. Right-click a test file after each step.

## Why this happens

- **Windows 11 build too old:** AI Actions shipped with Windows 11 24H2 and newer. An older build — or a 24H2 install missing cumulative updates — never renders the menu.
- **Broken or generic NPU driver:** The actions run on the NPU. A missing, outdated, or generic driver means the AI runtime cannot initialize, so Explorer hides the entries entirely.
- **Not signed in with a Microsoft account:** AI Actions check your Microsoft identity before appearing. A local account, or a signed-out profile, keeps the menu hidden.
- **On-device AI models not downloaded:** The models arrive as separate downloads after setup. On a fresh PC, or right after a feature update, the menu stays absent until they finish.
- **Group Policy or registry block on AI features:** Workplace-managed PCs often disable consumer AI experiences via policy. On such machines the menu is suppressed by design, not by bug.
- **Explorer shell state corruption:** A stuck Explorer process or corrupted shell cache can fail to load the AI Actions extension even when every requirement is satisfied.
- **Wrong file type selected:** AI Actions are contextual — image actions for photos, document actions for text files. Right-clicking an unsupported file type shows nothing, which mimics a missing feature.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your PC is a Copilot+ PC on a supported build

AI Actions are exclusive to Copilot+ PCs — no tweak brings them to a standard laptop, so confirm eligibility before troubleshooting anything else. This two-minute check saves you from chasing a feature your hardware cannot run.

1. Open **Settings > System > About** and look for Copilot+ branding and an NPU entry (40+ TOPS) in the processor details.
2. Press **Win + R**, type **winver**, and confirm Windows 11 **24H2** (build 26100) or newer — AI Actions do not exist on 23H2 or older.
3. If you are on 23H2, open **Settings > Windows Update** and install the 24H2 feature update; AI Actions only appear after it.
4. After any feature update, install all pending cumulative updates — the AI Actions extension has been patched several times since launch.
5. Restart the PC after updating and right-click a JPG photo to check for the AI Actions entry. If your machine is not Copilot+ class, stop here — the menu is unavailable on this hardware. NPU confusion after major updates is covered in the [missing NPU after the 25H2 update](/articles/npu-missing-after-25h2-update/) guide.

### Fix 2: Repair the NPU driver

The AI Actions menu is rendered by a shell extension that queries the NPU at load time. If the NPU driver is broken, missing, or generic, the extension silently unloads itself — no error, just a normal-looking context menu.

1. Open **Device Manager > Neural processors** and check for your NPU — a yellow warning icon or a missing category means the driver is at fault.
2. Download the latest NPU/chipset driver for your exact model from your laptop maker's support page: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Install the driver package as administrator, then restart when prompted — the AI runtime binds at startup.
4. After rebooting, confirm in Device Manager that the NPU shows with no warnings.
5. Right-click a photo in File Explorer and check for AI Actions. If the NPU is still flagged, a deeper clean-install of the driver is the next step before continuing.

### Fix 3: Sign in with a Microsoft account

AI Actions verify your Microsoft identity before the menu renders — a local account, or one that signed itself out after an update, keeps the entries hidden with no explanation. This is the quietest of all the gates.

1. Open **Settings > Accounts > Your info** and confirm you are signed in with a Microsoft account, not a local account.
2. If it shows a local account, click **Sign in with a Microsoft account instead** and complete it.
3. Open the Microsoft Store, click the profile icon, and confirm the same account is signed in there — Store and Windows identities can drift apart.
4. Sign out and back in to Windows so the identity change propagates to shell extensions.
5. Right-click a JPG (image actions) or TXT (summarize) and check the menu. Identity drift on ARM causes the same silent failures seen in [Dev Home issues on Windows 11 ARM](/articles/dev-home-windows-11-arm-issues/).

### Fix 4: Let the on-device AI models finish downloading

Even with the right build, driver, and sign-in, AI Actions need their model packages — which download separately, in the background, after setup or a feature update. On a new PC the menu can stay absent for an hour with zero indication anything is pending.

1. Connect to unmetered Wi-Fi and plug in the charger — model downloads pause on metered connections and on battery.
2. Open **Settings > Windows Update** and install everything pending, including optional updates — model packages sometimes ride along.
3. Leave the PC idle and plugged in for 30–60 minutes; background downloads only run when the machine is idle.
4. After the wait, restart and right-click a photo — background removal appearing means the models landed. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) note Copilot+ model downloads need an active connection and idle time.

### Fix 5: Check for policy blocks and restart the Explorer shell

If every requirement is met and the menu is still missing, suspect a workplace policy suppressing AI features or a stuck Explorer process failing to load the extension. Both are fixable without touching your files.

1. On a work-managed PC, ask your IT admin whether AI experiences are disabled by policy — if so, no local fix overrides it.
2. On a personal PC, open **Settings > Privacy & security** and confirm no "turn off AI features" style toggles are enabled.
3. Press **Ctrl + Shift + Esc** to open Task Manager, find **Windows Explorer**, right-click it, and choose **Restart**.
4. Wait for the taskbar and desktop to reload, then right-click a JPG and a TXT file to test both image and document actions.
5. If the restart helps temporarily but the menu vanishes again, a shell extension conflict is likely — the same stale-state pattern that skews [SleepStudy battery reports](/articles/sleepstudy-report-arm-laptop-battery/) on ARM laptops.

### Fix 6: Re-register the AI shell components with an in-place repair

When nothing above restores the menu, the AI Actions shell extension itself may be damaged — a state that survives driver reinstalls because it lives in the Windows component store. An in-place repair reinstalls those components while keeping your files and apps.

1. Back up anything critical first — the repair is non-destructive, but backups are cheap insurance.
2. Download the Windows 11 installation media for your build from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Run setup from the mounted ISO and choose **Keep personal files and apps** — this reinstalls Windows components including the AI extension.
4. Let the repair complete (30–60 minutes), then install all Windows Updates again.
5. Sign in, wait for model downloads as in Fix 4, and test AI Actions on a photo and a document. If the menu still does not appear on confirmed Copilot+ hardware, contact your laptop maker's support — the NPU may need firmware attention.

## Closing

Missing AI Actions are never a single bug — they are a stack of four gates (build, NPU driver, sign-in, downloaded models) plus policy and shell state. Confirm Copilot+ eligibility first, repair the NPU driver second, and give the model downloads idle time before assuming anything is broken.
