---
title: "Qualcomm Hexagon NPU Driver for Windows: Install & Fix Guide"
slug: qualcomm-hexagon-npu-driver-windows
date: 2026-10-19
categories: ["ai-pc"]
tags: ["qualcomm hexagon", "npu driver", "snapdragon", "windows 11", "arm"]
description: "Qualcomm Hexagon NPU driver for Windows explained: where to get it, how to install it, and fixes for common Hexagon driver problems."
thumbnail: "/images/thumbs/qualcomm-hexagon-npu-driver-windows.webp"
faqs:
  - q: "What is the Qualcomm Hexagon NPU?"
    a: "Hexagon is Qualcomm's NPU architecture inside Snapdragon X Plus and Elite chips, delivering 45 TOPS for on-device AI. On Windows it appears as the NPU device that powers Recall, Studio Effects, and Live Captions."
  - q: "Can I download the Hexagon driver directly from Qualcomm?"
    a: "No consumer download exists. Qualcomm distributes through OEMs and Windows Update. Your laptop maker's support page is the official source for the Hexagon NPU package."
  - q: "How do I know my Hexagon driver version?"
    a: "Device Manager, Neural processors, right-click the Hexagon/NPU entry, Properties, Driver tab. Compare the version against your OEM's support page to see if you are current."
  - q: "Does the Hexagon driver affect non-AI apps?"
    a: "No. It only drives the NPU. General app compatibility on Snapdragon laptops is a separate x86-emulation matter — see our [ARM app guide](/articles/app-not-working-snapdragon-x-laptop/)."
---

The Hexagon NPU is the AI heart of every Snapdragon X laptop, but unlike Intel or AMD, Qualcomm offers no direct driver download. You get Hexagon drivers through your laptop maker or Windows Update — which means version lag, occasional mismatches, and confusion about where the driver even lives. This guide maps the whole picture: what the Hexagon driver is, where to get it, and how to fix it when it breaks.

If you are fighting general [Snapdragon X NPU issues](/articles/snapdragon-x-elite-npu-driver-issues/), start there for the ARM-specific playbook; this article goes deep on the Hexagon driver itself.

## Why this happens (driver problems)

- **No direct Qualcomm download:** Users hunt Qualcomm's site, find nothing, and install wrong packages from shady sources.
- **OEM validation lag:** Makers validate Qualcomm drops slowly; your Hexagon driver may be many months old.
- **Windows Update desync:** OS AI components update faster than the Hexagon driver, breaking the interface between them.
- **Firmware pairing:** Hexagon drivers expect matching Snapdragon UEFI firmware; mismatches cause silent failures.
- **Clean-install gaps:** Recovery media sometimes omits the Hexagon package, leaving the NPU driverless.
- **Conflicting manual installs:** Forcing x86 NPU drivers onto ARM64 corrupts the stack.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Get the driver from the right source

Stop hunting Qualcomm's website — it is not there.

1. Go to your maker's support page: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/), Samsung, or Microsoft (Surface).
2. Enter your exact Snapdragon model and find the NPU/AI/Hexagon driver entry.
3. Download the ARM64 package — verify the filename or description mentions ARM64.
4. Never install x86/x64 NPU drivers from Intel/AMD pages; they cannot work and may corrupt detection.
5. Save the installer — you will need it again after major Windows updates.

### Fix 2: Check your current Hexagon version

Know what you have before changing it.

1. Device Manager, Neural processors, right-click the Hexagon/NPU entry, Properties, Driver tab.
2. Note driver version and date; compare with your OEM's latest listing.
3. If Device Manager shows no NPU entry at all, skip to Fix 4 — this is a detection problem.
4. An ancient driver (a year+) with broken AI features is your cue to update via Fix 3.

### Fix 3: Install or update the Hexagon driver

The core procedure.

1. Close all apps and plug in the charger.
2. Run the OEM Hexagon installer as administrator.
3. Reboot when prompted — do not skip the reboot.
4. Verify in Device Manager: clean entry, no warnings, plausible new version/date.
5. Test an AI feature (Windows Studio Effects on camera) to confirm functionality, not just presence.

### Fix 4: Recover a missing Hexagon NPU

When the NPU entry is gone entirely.

1. First check [general NPU detection](/articles/npu-not-detected-windows-11/) steps — BIOS visibility applies on ARM too.
2. Device Manager, Action, "Scan for hardware changes" — look under Neural processors and Other devices.
3. Install the OEM Hexagon package from Fix 1 even if no device is visible; the installer often triggers detection.
4. Check for Snapdragon UEFI firmware updates — on ARM, firmware leads drivers.
5. If still missing after firmware + driver, check Windows Update optional updates for Qualcomm entries.

### Fix 5: Keep firmware, driver, and OS in sync

The ARM trinity. When one moves alone, things break.

1. Note your UEFI version (`msinfo32`), Hexagon driver version, and Windows build.
2. Update in order: UEFI firmware first, then Hexagon driver, then Windows updates.
3. After each step, verify the NPU still works before proceeding — isolate which step breaks it.
4. If a Windows update breaks a working trio, roll back the update or the driver, not all three.
5. Bookmark your maker's driver page and check quarterly — Hexagon updates are infrequent but important.

### Fix 6: Understand NPU vs GPU for AI tasks

Set expectations correctly — the Hexagon is efficient, not omnipotent.

1. The 45-TOPS Hexagon excels at sustained, efficient inference: background blur, live captions, Recall indexing.
2. Heavy generative AI (large local LLMs, image generation) may still prefer the GPU — that is by design.
3. If an app ignores the Hexagon, check its settings for NPU selection; many default to GPU.
4. Our [NPU vs GPU guide](/articles/npu-vs-gpu-which-runs-ai-tasks/) details which workloads belong where.
5. Do not judge the Hexagon by GPU benchmarks — judge it by battery life during AI work, where it dominates.

## Closing

The Qualcomm Hexagon driver is simple once you accept its distribution model: OEM or Windows Update, never Qualcomm direct, and always paired with matching firmware. Keep that trio in sync and the 45-TOPS NPU quietly powers your Copilot+ features for years. When AI features misbehave on Snapdragon, check the Hexagon driver version first — it is the single most common root cause on this platform, ahead of app bugs and Windows settings. New to NPU concepts entirely? Start with [how to check if your laptop has an NPU](/articles/check-if-laptop-has-npu/) to ground the basics before troubleshooting drivers.
