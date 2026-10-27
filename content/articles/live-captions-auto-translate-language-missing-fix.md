---
title: "How to Fix a Missing Language in Live Captions Auto Translate on Windows 11"
slug: live-captions-auto-translate-language-missing-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["live captions", "auto translate", "language pack", "windows 11", "accessibility", "troubleshooting"]
description: "Fix a missing language in Windows Live Captions auto translate by adding language packs, speech components, and the correct translation settings today."
thumbnail: "/images/thumbs/live-captions-auto-translate-language-missing-fix.webp"
faqs:
  - q: "Why is my language missing from Live Captions translation?"
    a: "Auto translate only lists languages whose language pack and speech components are installed. If the pack is missing or incomplete, the language simply does not appear in the list."
  - q: "Does auto translate need an internet connection?"
    a: "Translation itself can run on-device once the language components are installed, but downloading a new language pack requires internet. Install the pack first, then translation works offline."
  - q: "Can Live Captions translate any spoken language?"
    a: "No. Translation supports a limited set of source and target languages, and both must be installed. A language outside that set will not appear, even with all packs installed."
  - q: "Will adding a language change my Windows display language?"
    a: "No. You can add a language for captions and translation without changing the Windows display language. The caption language is a separate setting."
---

You open Live Captions, turn on translation, and look for your language in the list — but it is not there. The captions themselves may work in the original language, yet the translate dropdown offers only a handful of options, and the one you need is missing entirely.

This is almost always a language-pack problem, not a captions problem. Windows Live Captions auto translate can only offer languages whose packs and speech components are actually installed on your PC. If a pack was never downloaded, downloaded incompletely, or belongs to a language outside the supported translation set, Windows silently leaves it out of the list.

This guide fixes the list in order: confirming the language is supported, installing its pack correctly, and checking the caption settings that filter what you see. Add one language at a time and reopen the translate dropdown after each step.

## Why this happens

- **Language pack not installed:** Translation lists only installed languages. A language you speak but never added to Windows will not appear, no matter how correct the caption settings are.
- **Speech components missing from the pack:** Installing a language for display does not always install its speech recognition components, which Live Captions translation needs.
- **Language outside the supported translation set:** Auto translate supports a limited set of languages. A language outside that set cannot be added to the translate list at all.
- **Caption language and translation language confused:** The spoken-language setting and the translate-to language are separate dropdowns. Setting the wrong one makes it look as if the target language is missing.
- **Incomplete download after an update:** A Windows update can interrupt or roll back a language pack, leaving a partial install that Windows hides from the translate list.
- **Region or account restriction on language downloads:** A restricted network, work-managed device, or region setting can block the language-pack download without a clear error.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check that your language is in the supported set

Before installing anything, confirm the language can appear at all. Chasing a download for an unsupported language wastes time, and knowing the supported set tells you whether to look for a pack or choose the nearest supported alternative.

1. Open **Settings > Accessibility > Captions** and open the translation language dropdown to see exactly which languages are listed.
2. Note both the spoken language (what is being said) and the translate-to language (what you want to read) — they are different lists.
3. Check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for the current Live Captions translation language list.
4. If your language is not in the supported set, pick the closest supported language as a workaround and stop here.
5. If it is supported but missing from your dropdown, continue — the pack is the problem, not the feature.

### Fix 2: Add the language with its speech components

The most common fix is also the most fiddly: Windows offers a language in several forms, and only the full install — with speech — unlocks translation. Add the language deliberately, ticking every component option it offers.

1. Open **Settings > Time & language > Language & region** and click **Add a language**.
2. Search for your language, select the correct regional variant, and click **Next**.
3. Tick every available option: language pack, text-to-speech, and speech recognition, if offered.
4. Click **Install** and wait for the download to complete fully — do not close Settings or sleep the PC mid-download.
5. Restart the PC, open Live Captions, and check the translate dropdown again for your language.

### Fix 3: Repair or reinstall a partial language pack

A pack that downloaded halfway — interrupted by sleep, a network drop, or an update — can look installed in Settings while Live Captions refuses to list it. Removing and reinstalling it cleanly is more reliable than trying to patch it.

1. In **Settings > Time & language > Language & region**, find the language under **Preferred languages**.
2. Click the three dots beside it and choose **Remove**, then restart the PC.
3. Re-add the language exactly as in Fix 2, with all speech components ticked.
4. Confirm the download finishes and the language shows as fully installed, not pending.
5. Open Live Captions and check the translate list; a clean reinstall resolves most "installed but missing" cases. The same clean-reinstall principle fixes other missing-component issues, such as [live captions with an external microphone](/articles/live-captions-external-microphone-fix/), where a partial driver install hides the device.

### Fix 4: Set the spoken language correctly before translating

Translation needs to know what language it is hearing. If the spoken-language setting is wrong — say, English when the audio is Spanish — the translate dropdown may filter oddly or produce nonsense, making it look as if the target language is the problem. Similar settings confusion also affects [Copilot memory personalization](/articles/copilot-memory-personalization-not-working/), where the wrong toggle hides a feature that is actually installed.

1. Open **Settings > Accessibility > Captions** and check the **Caption language** (spoken language) setting.
2. Set it to the language actually spoken in the audio or meeting.
3. Then open the translation option and set the **Translate to** language to the one you want to read.
4. Play audio in the correct spoken language and confirm captions appear before translation.
5. If captions work but translation still lacks your language, return to Fix 2 — the target pack, not the spoken setting, is missing.

### Fix 5: Update Windows and clear a stuck component state

Windows updates deliver new translation languages and repair broken caption components. A PC that has skipped updates may simply predate support for your language, or hold a stuck component that hides newly installed packs.

1. Open **Settings > Windows Update** and install all pending updates, including optional updates, then restart.
2. After the restart, reopen **Settings > Accessibility > Captions** and toggle Live Captions off and back on.
3. Check the translate dropdown again — new languages sometimes appear only after this toggle forces a refresh.
4. If the language is still missing, run Windows Update once more; language components sometimes arrive in a second, smaller update.
5. As a final local step, download the latest Windows 11 build from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11) only if your update channel is stuck — otherwise stay on Windows Update. A stalled component download is also what breaks some ARM app installs, as seen with [Claude Desktop on ARM Windows](/articles/claude-desktop-app-arm-windows-fix/).

### Fix 6: Work around a managed-device or network block

On a work or school PC, or a restricted network, language downloads can be blocked silently by policy. If every install attempt stalls or vanishes, the block — not your technique — is the cause, and the workaround is to confirm it and plan around it.

1. Try the language download on a different network, such as a phone hotspot, to rule out a network filter.
2. Check **Settings > Windows Update** for any "managed by your organisation" notice that might also govern language packs.
3. If the device is managed, ask your IT administrator to approve the language pack or push it through device management.
4. While waiting, use a supported alternative language for translation, or use the untranslated captions with a separate translation tool for key passages.
5. Once the pack is approved and installed, verify it in the Live Captions translate dropdown before relying on it in a live meeting.

## Closing

A missing translation language in Live Captions is rarely a mystery once you know the rule: only fully installed, supported languages appear. Confirm support, install the pack with its speech components, and set the spoken language correctly — and the dropdown usually fills in exactly as expected.
