---
title: "ASUS VivoBook S NPU Not Detected? Fix It Now"
slug: asus-vivobook-s-npu-not-detected
date: 2026-10-19
categories: ["ai-pc"]
tags: ["asus", "vivobook s", "npu not detected", "ai boost", "troubleshooting"]
description: "ASUS VivoBook S NPU not detected? Fix missing Neural processors, Intel AI Boost driver failures, and AI feature issues on all VivoBook S models today."
thumbnail: "/images/thumbs/asus-vivobook-s-npu-not-detected.webp"
faqs:
  - q: "How do I know if my VivoBook S has an NPU?"
    a: >
      Check Settings > System > About for the processor: VivoBook S 14/15/16 models with Intel Core Ultra Series 2 (e.g., 258V/268V) or AMD Ryzen AI 300 series include NPUs. Older VivoBook S models with 13th-gen Intel or Ryzen 7000 (non-AI) lack a qualifying NPU — verify before troubleshooting.
  - q: "Where are ASUS's NPU drivers?"
    a: >
      On the ASUS support site: enter your exact VivoBook S model, select Windows 11, and download the chipset/MEI and graphics drivers — the NPU driver (Intel AI Boost) ships inside these packages. MyASUS's update scan is the easier path and usually finds the right ones.
  - q: "Why did the NPU disappear after a Windows update?"
    a: >
      Windows Update sometimes replaces ASUS's matched NPU driver with a generic version that doesn't initialize on VivoBook hardware, or the update corrupts the driver stack. Rolling back the driver or reinstalling ASUS's package (Fix 3) resolves most post-update disappearances.
  - q: "Does MyASUS interfere with the NPU?"
    a: >
      Rarely directly, but MyASUS power profiles can throttle the NPU, and its updates occasionally install mismatched drivers. Keep MyASUS for updates, but check its power/fan profiles if AI features underperform.
---

The ASUS VivoBook S lineup — S 14, S 15, S 16 in Intel Core Ultra and AMD Ryzen AI flavors — brings Copilot+ AI to ASUS's mainstream thin-and-lights. But "NPU not detected" is a recurring VivoBook S complaint: Device Manager shows no Neural processors, Intel AI Boost fails to install, or AI features that worked yesterday are gone today.

ASUS's wrinkle is driver packaging: the NPU driver hides inside chipset/MEI and graphics packages rather than shipping as a standalone "NPU driver," so owners don't know what to download. Add MyASUS vs Windows Update version fights, and the NPU becomes the casualty. This guide follows the ASUS-specific trail — MyASUS first, correct package identification second, clean reinstall third. For Acer's AI laptop with similar symptoms, see [Acer Swift 14 AI Copilot problems](/articles/acer-swift-14-ai-copilot-problems/); for Dell's, [Dell XPS 13 Snapdragon problems](/articles/dell-xps-13-snapdragon-problems/); for Samsung's, [Samsung Galaxy Book5 NPU driver](/articles/samsung-galaxy-book5-npu-driver/).

If heat comes with the NPU trouble, [AI PC running hot fix](/articles/ai-pc-running-hot-fix/) covers cooling alongside.

## Why this happens

- **NPU driver hidden in chipset packages:** Owners download "graphics drivers" and miss that the NPU driver ships in the chipset/MEI package — so it never gets installed.
- **MyASUS vs Windows Update conflicts:** The two channels overwrite each other's NPU driver versions, breaking initialization.
- **BIOS too old:** Early VivoBook S BIOS versions had NPU enumeration bugs; later releases fix detection.
- **Interrupted driver installs:** The multi-part Intel AI Boost install is fragile — a reboot mid-install corrupts it.
- **NPU fused off or BIOS-disabled:** Rare, but some SKUs or BIOS resets leave the NPU disabled in firmware.
- **Windows feature update regressions:** 24H2-era updates broke NPU detection on several VivoBook configurations pending matched drivers.

## How to fix it

Work through these in order — ASUS's channels first.

### Fix 1: Update via MyASUS and Windows Update

Let ASUS's updater run before anything manual — it knows which packages your exact VivoBook S needs.

1. Open MyASUS (preinstalled; Microsoft Store if missing) > System Update.
2. Install all critical updates, especially BIOS, chipset/MEI, and graphics.
3. Keep the laptop on AC power throughout — BIOS updates must not be interrupted.
4. Then run Windows Update to full clear, including optional drivers.
5. Reboot and check Device Manager for the Neural processors category.

### Fix 2: Identify the correct NPU driver package

Downloading the wrong package is the classic VivoBook S mistake. Get the right one from ASUS's site.

1. Go to ASUS support, enter your exact VivoBook S model (e.g., S5507QA vs S5606MA — they differ!).
2. Select Windows 11 and open the Chipset and Graphics/VGA sections.
3. For Intel models: the NPU (Intel AI Boost) driver is in the Intel Chipset/MEI package and/or the graphics driver — download both.
4. For AMD Ryzen AI models: the NPU driver ships with the AMD chipset driver from ASUS (or [AMD's driver page](https://www.amd.com/en/support/download/drivers.html)).
5. Note the version numbers — you'll compare after installation.

### Fix 3: Clean-reinstall the NPU driver stack

When versions have fought each other, only a clean reinstall untangles the stack. Order matters: chipset first, then graphics.

1. In Device Manager, uninstall the NPU device if present (check "delete the driver software").
2. Also uninstall the related chipset/MEI entries showing warnings.
3. Reboot into a clean state — don't let Windows auto-install yet (pause Windows Update temporarily if needed).
4. Install ASUS's chipset/MEI package first, reboot, then the graphics package, reboot.
5. Verify: Device Manager shows Neural processors without warnings; Task Manager > Performance shows the NPU graph.

### Fix 4: Check BIOS for NPU settings

If Device Manager shows no Neural processors category at all, firmware may be the gate.

1. Reboot into BIOS (F2 or Del on ASUS, tapped during boot).
2. Look through Advanced settings for NPU, AI Boost, or neural processor toggles.
3. Ensure any such option is Enabled; also check that the iGPU isn't disabled (the NPU stack can depend on it).
4. Save and exit, boot to Windows, re-check Device Manager.
5. If no NPU options exist in BIOS, that's normal on many VivoBooks — the NPU should simply enumerate with correct drivers.

### Fix 5: Fix MyASUS power profile throttling

Sometimes the NPU is detected but AI features crawl — MyASUS power profiles may be starving it.

1. Open MyASUS > Customization > Power & Performance (or Fan profile).
2. Switch from Whisper/Battery saver to Standard or Performance temporarily.
3. Test the AI feature (Studio Effects, Recall) under the higher profile.
4. If it works, keep Standard for daily use — Whisper mode's savings aren't worth broken AI.
5. Also check Windows power mode (Settings > System > Power) isn't on extreme saver.

### Fix 6: Escalate to ASUS with model precision

ASUS support is model-number-driven — precision gets you past the scripts.

1. Document your exact model (e.g., VivoBook S 15 S5507QA), BIOS version, and driver versions installed.
2. Run MyASUS's System Diagnostics and save any failure reports.
3. Screenshot Device Manager showing the missing Neural processors category.
4. Contact ASUS support with the package — mention the clean reinstall already attempted.
5. For NPU absence surviving BIOS updates and clean driver stacks, request hardware diagnosis; the NPU is part of the SoC.

## Closing

VivoBook S "NPU not detected" is usually a driver-packaging problem, not a dead chip: the NPU driver hides in chipset/MEI packages, MyASUS and Windows Update fight over versions, and old BIOS versions fail to enumerate it. Work MyASUS → correct package → clean reinstall → BIOS check, and the Neural processors category appears in the large majority of cases. What doesn't appear after all of that — with current BIOS and clean ASUS drivers — is a firmware or silicon issue, and ASUS service is the right destination with your documentation in hand.
