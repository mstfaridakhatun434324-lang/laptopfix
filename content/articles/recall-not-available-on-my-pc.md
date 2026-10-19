---
title: "Recall Not Available on My PC? Why & What to Do"
slug: recall-not-available-on-my-pc
date: 2026-10-19
categories: ["ai-pc"]
tags: ["recall not available", "copilot plus pc", "requirements", "windows 11", "npu"]
description: "Recall not available on your PC? Learn the exact hardware and software requirements and what to do when your laptop doesn't make the cut."
thumbnail: "/images/thumbs/recall-not-available-on-my-pc.webp"
faqs:
  - q: "What are the exact Recall requirements?"
    a: "A Copilot+ PC: 40+ TOPS NPU, 16GB RAM, 256GB storage, Windows 11, and Windows Hello sign-in. All five must be met — missing any one blocks Recall entirely."
  - q: "Can I enable Recall on an unsupported PC with tweaks?"
    a: "Registry tricks exist online, but they do not work reliably — Recall's AI models require the NPU hardware, and forcing it on unsupported machines produces a broken, slow experience. We do not recommend it."
  - q: "My laptop has an NPU but Recall is unavailable. Why?"
    a: "Likely the NPU is under 40 TOPS (first-gen Intel Core Ultra has only 11), or RAM/storage falls short, or Windows Hello is not set up. Check each requirement individually — the failing one is usually obvious."
  - q: "Will my current laptop ever get Recall?"
    a: "Only if it already meets the hardware bar and is blocked by software (region, update, driver). If the NPU, RAM, or storage is insufficient, no update will ever enable it — that requires new hardware."
---

You open Settings looking for Recall and it is simply not there — no toggle, no timeline, nothing. Or worse, it appears but says your PC is not supported. Before frustration sets in, understand this: Recall has the strictest hardware requirements of any Windows feature ever shipped. "Not available" is usually Windows telling the truth about your hardware, and the checklist below will prove it either way in about ten minutes.

This guide maps every requirement precisely and tells you what to do in each failure case. If Recall is present but broken, our [Recall not working guide](/articles/windows-recall-not-working/) is the right path instead.

## Why this happens

- **40+ TOPS NPU:** The headline bar. Snapdragon X (45), Ryzen AI 300 (50), Intel Core Ultra Series 2 (48) qualify; Core Ultra Series 1 (11) does not.
- **16GB RAM minimum:** Non-negotiable — Recall's models need the memory headroom.
- **256GB storage minimum:** For the snapshot database and AI index.
- **Windows 11 (current build):** Recall needs recent Windows 11 builds with the AI components.
- **Windows Hello sign-in:** Face, fingerprint, or PIN — required as Recall's security gate.

## How to fix it

Work through these in order — diagnose first, then act.

### Check 1: Verify your NPU's TOPS

The most common failure point — start here.

1. Identify your processor (`msinfo32`) and look up its NPU TOPS on the vendor spec page.
2. 40+? You clear the bar — move to the next check.
3. Under 40 (e.g., 11-TOPS Core Ultra Series 1)? No software change will ever qualify this chip.
4. No NPU at all? Same verdict — Recall needs the silicon.
5. Our [system requirements deep-dive](/articles/windows-recall-system-requirements/) lists qualifying chips by name — cross-check yours there.

### Check 2: Verify RAM and storage

The quiet disqualifiers — easy to overlook, impossible to work around.

1. Settings, System, About — confirm 16GB+ RAM installed.
2. Settings, System, Storage — confirm 256GB+ total drive capacity (not free space — total).
3. 8GB RAM machines fail even with a great NPU — and RAM is rarely upgradeable on thin AI laptops.
4. 128GB storage models fail the bar regardless of everything else; the snapshot database needs room.
5. If either falls short, the answer is definitive: new hardware is the only path.

### Check 3: Set up Windows Hello

The fixable blocker — and the most commonly missed one.

1. Settings, Accounts, Sign-in options — set up PIN at minimum.
2. Add face or fingerprint if your hardware supports it; biometrics are the smoothest Hello experience.
3. Sign out and back in with Hello to activate the security binding Recall depends on.
4. Recheck Recall settings — on qualifying hardware, it often appears immediately after Hello setup.
5. This is the number-one "it was available all along" fix — many users skip Hello and assume hardware failure.

### Check 4: Update Windows and drivers

Software gates that lift with updates — check these before concluding hardware failure.

1. Install all Windows updates — Recall availability expanded across builds and regions.
2. Update the NPU driver from your OEM — Recall checks driver capabilities, not just hardware.
3. Check your region: early Recall availability excluded some regions; updates have widened it.
4. After updates, reboot and recheck Settings, Privacy & security for the Recall section.
5. If it appears but [snapshots are missing](/articles/recall-snapshots-missing/), that is a separate (fixable) problem.

### Check 5: Accept the verdict gracefully

When hardware truly falls short, acceptance beats endless workarounds.

1. If the NPU, RAM, or storage fails the bar, no tweak, registry hack, or reinstall will enable Recall — the models physically need the resources.
2. Do not install "Recall enabler" tools from the internet — they produce broken experiences and security risks.
3. Your laptop remains a fine machine — everything except Recall's exclusives works normally.
4. When you next buy, the [Copilot+ requirements](/articles/copilot-plus-pc-requirements/) are now a known checklist to shop against.
5. In the meantime, Windows' regular Timeline and search cover much of Recall's use case, minus the AI magic.

## Closing

"Recall not available" is Windows enforcing a real hardware bar, not a bug to fix — except when the blocker is Windows Hello, an old driver, or a pending update, which are all fixable in minutes. Check the five requirements in order, fix what is fixable, and accept what is not. Note that availability is only the first gate: once Recall appears, review the [privacy settings](/articles/windows-recall-privacy-settings-fix/) to control what it captures — many users enable it and immediately want to tune its behavior. Chasing registry hacks for a hardware-gated feature wastes the time you could spend using the laptop you have. Run the checklist, keep the printout of your specs, and move on with confidence either way. And if you are shopping for your next machine, run through this same five-point checklist before buying — it is the fastest way to guarantee Recall will be there on day one.
