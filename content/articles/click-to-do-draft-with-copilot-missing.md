---
title: "How to Fix Click to Do Draft with Copilot Missing on Windows 11"
slug: click-to-do-draft-with-copilot-missing
date: 2026-10-21
categories: ["ai-pc"]
tags: ["draft with copilot", "click to do missing", "copilot+ pc", "ai writing", "windows 11", "copilot features"]
description: "Fix Click to Do Draft with Copilot missing on your AI PC with six step-by-step methods covering feature rollout, Microsoft 365, NPU checks, and settings."
thumbnail: "/images/thumbs/click-to-do-draft-with-copilot-missing.webp"
faqs:
  - q: "What is Draft with Copilot in Click to Do?"
    a: "It is the Click to Do text action that rewrites or drafts text with Copilot — select a sentence and ask Copilot to rewrite it, expand it, or change its tone. When it is missing, the rest of the menu can still work fine."
  - q: "Does Draft with Copilot need a Microsoft 365 subscription?"
    a: "Some Copilot writing features are tied to Microsoft 365 Copilot licensing, while the basic on-device rewrite runs locally. If the action is missing only in Office apps, licensing is the first thing to check."
  - q: "Why do other Click to Do actions work but not Draft with Copilot?"
    a: "Draft with Copilot depends on the Copilot service connection and sometimes cloud features, while actions like copy or search run fully on-device. A sign-in or service problem removes just the Copilot actions."
  - q: "Is Draft with Copilot available in every region?"
    a: "No. Copilot features roll out by region and Microsoft account market. If your account region or Windows display language is set to an unsupported market, Copilot-powered actions may not appear."
---

Click to Do's menu should include **Draft with Copilot** — the action that rewrites selected text, changes its tone, or drafts new wording with AI help. When every other action (summarize, search, copy) shows up but Draft with Copilot is nowhere to be seen, the feature is not broken so much as ungated: something between your PC and the Copilot service is not satisfied.

Unlike on-device actions, Draft with Copilot needs the Copilot service, account sign-in, licensing, and regional availability too. Any gap — unsigned-in account, unsupported region, outdated app, unmet NPU bar — removes just this action.

This guide walks through six fixes in order: confirming the action should exist on your build, fixing sign-in and region, updating the Copilot app, checking licensing, verifying the NPU, and repairing the feature.

## Why this happens

- **Copilot app is outdated or missing:** Draft with Copilot calls into the Copilot app/service. If the app is old — or was uninstalled as "bloat" — the action has nothing to call and disappears.
- **Not signed into a Microsoft account:** Copilot-powered actions need a signed-in Microsoft account. On a local account, on-device actions work but every Copilot action is withheld.
- **Region or language not supported:** Copilot features are gated by account region and display language. A mismatch hides Copilot actions — like [driver-gated features](/articles/studio-effects-driver-update-required/) vanishing when prerequisites are unmet.
- **Microsoft 365 licensing gap in Office apps:** Inside Word or Outlook, Draft with Copilot may require a Microsoft 365 Copilot license. It can appear in Notepad but be missing in Office on the same PC.
- **NPU below the Copilot+ bar:** The rewrite assistance expects Copilot+ class hardware. If your NPU does not qualify, Copilot actions stay hidden — [check your NPU's TOPS rating](/articles/how-to-check-npu-tops-windows-11/).
- **Feature rollout has not reached you:** Microsoft rolls Click to Do actions out gradually. Two identical laptops on different update rings can show different menus — the same per-ring gating behind [Zoom's virtual background](/articles/zoom-virtual-background-arm-laptop/) availability.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the action should exist on your Windows build

First make sure your build actually ships Draft with Copilot. It arrived in a specific Windows 11 feature update — machines behind on updates simply do not have it.

1. Press **Win + R**, type **winver**, and note your Windows 11 version and build.
2. Go to **Settings > Windows Update**, install everything pending including optional updates, and restart.
3. If you are on an older build (e.g., 23H2), the action may need 24H2 or later — see the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
4. After updating, select text in Notepad, **Win + click** it, and check the menu again.
5. If the action appears after the update, you were simply behind the rollout.

### Fix 2: Sign into a Microsoft account and check your region

Copilot actions are account-bound. A local account gets the on-device actions but not the Copilot ones, and a region mismatch can gate them even when signed in.

1. Go to **Settings > Accounts > Your info** and confirm a **Microsoft account** sign-in (not local).
2. If local, click **Sign in with a Microsoft account instead** and complete sign-in.
3. Go to **Settings > Time & language > Language & region** and set **Country or region** to a Copilot-supported market matching your account.
4. Set **Windows display language** to English (United States) while testing.
5. Restart, then retest Draft with Copilot in Notepad.

### Fix 3: Update or reinstall the Microsoft Copilot app

Draft with Copilot leans on the Copilot app package. An outdated, corrupted, or missing Copilot app removes the action while leaving on-device actions untouched.

1. Open the **Microsoft Store**, search **Microsoft Copilot**, and install or update it.
2. Open the Copilot app once and sign in with the same Microsoft account as Windows.
3. Ask Copilot a test question inside the app to confirm the service connection works.
4. If already installed, go to **Settings > Apps > Installed apps > Copilot > Advanced options** and click **Repair**, then **Reset** if needed.
5. Retest: select text in Notepad and **Win + click** — Draft with Copilot should now be listed.

### Fix 4: Check Microsoft 365 Copilot licensing for Office apps

If Draft with Copilot appears in Notepad but is missing in Word or Outlook, you are hitting the licensing boundary: in-Office Copilot writing features require a Microsoft 365 Copilot license.

1. Test in **Notepad** first — if it works there, your Windows-side setup is fine.
2. In Word, check **File > Account** and confirm your subscription includes Copilot.
3. Without the license, use Draft with Copilot in non-Office apps where no extra subscription is needed.
4. If you should have the license but Office does not see it, sign out in **File > Account > Sign out**, restart the apps, and sign back in.
5. Run **File > Account > Update Options > Update Now**, then retest.

### Fix 5: Verify the NPU meets the Copilot+ requirement

Draft with Copilot expects Copilot+ hardware — a 40+ TOPS NPU. On machines that fall short, or where the NPU driver is broken, Copilot-class actions stay hidden.

1. [Check your NPU's TOPS rating](/articles/how-to-check-npu-tops-windows-11/) in Task Manager or via that guide's method.
2. In Device Manager, confirm the NPU has no warning icon — reinstall the driver from your laptop maker's support page if it does.
3. Trigger any NPU workload (live captions, background blur) and watch Task Manager's NPU graph for activity.
4. If the NPU is missing from Task Manager entirely, resolve that first — no Copilot+ hardware means no Copilot actions.
5. On qualifying hardware, sign out and back in, then retest the menu.

### Fix 6: Reset Click to Do and repair Windows AI components

When account, region, app, license, and hardware all check out but the action is still missing, the Click to Do feature state itself is likely corrupt. Resetting it and repairing system files clears the stale state.

1. In **Settings > Privacy & security > Click to Do**, turn the feature off, restart, and turn it back on.
2. In an elevated Command Prompt, run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Check the [Windows support hub](https://support.microsoft.com/en-us/windows) for known-issue notices about missing Copilot actions on your build.
4. Restart once more and test in Notepad with a simple selected sentence.
5. If it remains missing, an in-place upgrade repair install (keeping files and apps) refreshes the AI feature stack.

## Closing

Draft with Copilot goes missing for gating reasons: build version, sign-in, region, the Copilot app, Office licensing, or the NPU bar. Working on-device actions prove the local pipeline is fine and point at the Copilot service side.
