---
title: "How to Fix Smart App Control Blocking Your ARM Apps on Windows 11"
slug: smart-app-control-blocking-arm-apps
date: 2026-10-23
categories: ["ai-pc"]
tags: ["smart app control", "arm apps", "app blocked", "windows security", "sac", "windows 11"]
description: "Fix Smart App Control blocking trusted ARM apps on Copilot+ PCs — understand evaluation mode, signing failures, and safe workarounds that keep protection on."
thumbnail: "/images/thumbs/smart-app-control-blocking-arm-apps.webp"
faqs:
  - q: "Why does Smart App Control block apps that worked fine before?"
    a: "Smart App Control blocks any unsigned or low-reputation executable, and many ARM-native or niche utilities lack the signing or reputation history it requires. The app is usually legitimate — it simply has not earned SAC's trust signals yet."
  - q: "Can I unblock a single app without turning off Smart App Control?"
    a: "Not directly — SAC has no per-app allowlist. Your options are running the app's signed installer version, using the Microsoft Store edition, or switching SAC to evaluation mode. Disabling it entirely is permanent for that Windows install."
  - q: "Does turning off Smart App Control require reinstalling Windows to re-enable?"
    a: "Yes. Once Smart App Control is fully turned off, turning it back on requires a clean reinstall or reset of Windows. That is why evaluation-mode and workaround fixes are preferable to disabling it."
  - q: "Is Smart App Control stricter on ARM laptops?"
    a: "It feels stricter because the ARM software ecosystem has more unsigned indie tools, sideloaded utilities, and x64-emulated apps with unusual signatures — all categories SAC treats cautiously. Store and well-known signed apps behave the same as on x64."
---

You download a trusted utility — a developer tool, a niche ARM-native app, something you have run for years — and Windows refuses to launch it: "Smart App Control blocked this app." There is no "run anyway" button that sticks, and the publisher looks legitimate. The laptop is protecting you from software you actually want.

On Copilot+ PCs and Windows on ARM, Smart App Control (SAC) blocks every executable that is not signed by a trusted publisher or recognized by Microsoft's cloud reputation service. The ARM ecosystem skews heavily toward exactly the software SAC distrusts: small indie tools, open-source utilities, sideloaded apps, and x64 binaries running under emulation with unfamiliar signatures. The block is usually a trust-signal problem, not a malware verdict.

This guide gives you six fixes in technician order: confirm what SAC is actually blocking, find a trusted path to run the app, and use evaluation mode correctly — without permanently killing a protection you cannot re-enable without reinstalling Windows.

## Why this happens

- **Unsigned or self-signed executables:** SAC's core rule is simple — no trusted signature, no launch. Many ARM utilities from small developers ship unsigned.
- **Low cloud reputation:** Even signed apps get blocked if Microsoft's reputation service has seen them too rarely; new releases and niche tools start at zero reputation.
- **x64 emulation changes the signature picture:** Some x64 apps under Prism emulation present loader or packaging characteristics that SAC scores lower than their native x64 counterparts.
- **Repackaged or portable builds:** Portable ZIP distributions and community repacks strip the installer signatures SAC relies on, so the same app works from its official installer but not as a portable.
- **Scripts and unsigned installers chained together:** An installer that downloads and launches unsigned helper executables gets the whole chain blocked, even when the top-level installer is signed.
- **Evaluation mode expired into enforcement:** SAC starts in evaluation mode and silently switches to full enforcement if it decides it can run without breaking your workflow — the blocks then appear "suddenly" weeks after setup.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Smart App Control is the actual blocker

Other protections produce similar-looking blocks. Verify SAC is the cause before working around it, or you will fix the wrong thing.

1. Open **Windows Security > App & browser control > Smart App Control settings** and note the current state: On, Evaluation, or Off.
2. Reproduce the block and read the exact dialog text — a genuine SAC block names Smart App Control explicitly.
3. Check **Windows Security > Protection history** for the blocked file's entry; it records the filename, path, and the SAC verdict.
4. If Protection history blames SmartScreen instead, the fix is different (SmartScreen has its own per-app bypass) — do not follow SAC workarounds for a SmartScreen block.
5. Note whether the block hits the installer, the installed executable, or a helper process — the trusted-path fix in Fix 2 depends on which stage fails.

### Fix 2: Get the app through a trusted path

SAC trusts signatures and reputation, so the cleanest fix is giving it something it already trusts: the signed installer, the Store edition, or the vendor's official build.

1. Download the app again from the developer's official site — not a mirror or portable repack — and prefer an `.msix` or signed `.exe` installer over a ZIP.
2. Check the Microsoft Store for an official edition of the app; Store apps carry the trust signals SAC wants and install cleanly on ARM.
3. Right-click the installer > **Properties** and look for a **Digital Signatures** tab — a valid signature from the known publisher is what SAC checks.
4. If the vendor offers separate ARM64 and x64 builds, take the ARM64 one; native builds from established vendors accumulate reputation faster and dodge emulation-related scoring quirks.
5. Install from the trusted package and launch — if SAC stays silent, the problem was the distribution format, not the app. This is also why [NPUs vanish inside virtual machines](/articles/npu-not-available-virtual-machine/) for some users: the VM path changes what the platform trusts and exposes.

### Fix 3: Use evaluation mode deliberately

Evaluation mode lets SAC learn your workflow and only enforce when it is confident — it is the sanctioned middle ground between full enforcement and the irreversible off switch.

1. In **Smart App Control settings**, if the option is available, set it to **Evaluation** rather than On.
2. Understand the deal: during evaluation SAC monitors without blocking; if it concludes your usage is compatible, it flips itself to On automatically.
3. Run your normal apps — including the blocked one — during the evaluation period so SAC builds an accurate picture of your legitimate software.
4. Do not mistake evaluation for a permanent bypass: if SAC decides your workflow needs the blocked app category, it stays permissive, but a future reset can re-trigger enforcement.
5. Check the setting monthly; a silent flip from Evaluation to On is the classic cause of "it worked for weeks, then blocked."

### Fix 4: Handle developer tools, scripts, and unsigned utilities

Developers and power users hit SAC hardest: compilers, script runtimes, and self-built tools are unsigned by nature. There are legitimate paths that do not require disabling protection.

1. Prefer tools distributed with proper signatures — most mainstream ARM64 dev tools (signed terminals, editors, runtimes) pass SAC without issue.
2. For your own builds, sign them with a self-generated certificate and add that certificate to the local Trusted Publishers store — SAC honors locally trusted publishers.
3. Run unsigned scripts through signed hosts (e.g., the signed Python or PowerShell executable) rather than as standalone unsigned `.exe` wrappers.
4. Keep a separate record of which tools you had to work around — if you later benchmark the machine, use a recognized [NPU benchmark guide for Windows 11](/articles/how-to-benchmark-npu-windows-11/) rather than an obscure unsigned binary that SAC will fight.
5. Never disable SAC just to run one unsigned tool — the per-tool workarounds above take minutes and preserve the protection permanently.

### Fix 5: Check for system-level confusion behind repeated blocks

When SAC blocks apps that are clearly signed and reputable, the trust pipeline itself may be malfunctioning — cloud connectivity, corrupted reputation cache, or system file damage.

1. Confirm the laptop has normal internet access — SAC consults cloud reputation, and a broken connection can turn "unknown" verdicts into blocks.
2. Run `sfc /scannow` in an elevated Command Prompt to repair corrupted system files that the trust stack depends on.
3. Check **Settings > Windows Update** and install all pending updates; SAC's intelligence components update through the normal channel.
4. Review **Reliability Monitor** (`perfmon /rel`) for patterns — if [Reliability Monitor shows AI PC crashes](/articles/reliability-monitor-ai-pc-crashes/) clustered around the same timeframe as the blocks, a crashing security or platform component may be corrupting verdicts.
5. As a diagnostic, create a new local user account and test the blocked app there — a profile-specific reputation cache issue will not follow you to the fresh profile.

### Fix 6: Make the final call — and understand the off switch

If none of the above yields a workable path, you face SAC's hard design decision: it can be turned off, but never turned back on without reinstalling Windows. Make this choice with full information.

1. Re-read the **Smart App Control settings** page warning: "Off" is permanent for this Windows installation — re-enabling requires **Settings > System > Recovery > Reset this PC** or a clean install.
2. Before flipping it, exhaust Fix 2's trusted paths once more — contact the app vendor and ask for a signed ARM64 build; vendors add signing when users ask.
3. If you do turn it off, compensate deliberately: keep SmartScreen on, keep Memory Integrity on, and be stricter about download sources.
4. Document the date and reason — six months later, "why is SAC off on this machine" is a question you will want answered.
5. Check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for any SAC policy changes before a future reinstall; Microsoft continues to tune enforcement, and a clean install a year from now may behave better than today's.

## Closing

Smart App Control blocks on trust signals, not on malice — and the ARM software world is full of legitimate apps with weak signals. Route around it with signed installers and Store editions, use evaluation mode as the sanctioned middle ground, and treat the off switch as the one-way door it is. The protection is worth keeping; the workaround is usually one trusted download away.
