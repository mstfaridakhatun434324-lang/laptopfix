---
title: "Microsoft Surface Pro NPU Not Detected? Fix It Step by Step"
slug: microsoft-surface-pro-npu-not-detected
date: 2026-10-19
categories: ["ai-pc"]
tags: ["surface pro", "npu not detected", "snapdragon", "copilot plus pc", "troubleshooting"]
description: "Microsoft Surface Pro NPU not detected? Fix missing Neural processors, driver failures, and AI issues on Surface Pro 11th Edition and all later models."
thumbnail: "/images/thumbs/microsoft-surface-pro-npu-not-detected.webp"
faqs:
  - q: "Which Surface Pro models have an NPU?"
    a: >
      The Surface Pro 11th Edition (Snapdragon X Elite/Plus) and later Copilot+ Surface Pros include qualifying NPUs (45 TOPS). Older Surface Pro 9/10 models with Intel 12th/13th-gen or SQ chips lack a Copilot+-grade NPU. Check Settings > System > About — Snapdragon X means you're in the right place.
  - q: "Why did the NPU disappear from Device Manager?"
    a: >
      Common causes: a Windows update replaced the working NPU driver with an incompatible one, the driver stack corrupted during an interrupted update, or (rarely) firmware stopped enumerating the device. The fixes below address each in order of likelihood.
  - q: "Can I download a Surface Pro NPU driver manually?"
    a: >
      Microsoft delivers Surface Pro NPU drivers through Windows Update and the Surface driver MSI packages on Microsoft's support site — there's no standalone "NPU driver" download. If Windows Update's driver fails, the Surface driver pack or a clean reinstall (Fix 3) is the path.
  - q: "Is a missing NPU a hardware failure on Surface Pro?"
    a: >
      Rarely. In our experience, 90%+ of "NPU not detected" cases on Surface Pro are driver or firmware issues fixed by updates and clean reinstalls. Genuine NPU silicon failure is uncommon — but if the device never enumerates after all software fixes, the Surface Diagnostic Toolkit can confirm hardware status.
---

The Surface Pro 11th Edition is Microsoft's flagship detachable Copilot+ PC — Snapdragon X Elite, OLED option, the NPU front and center in every marketing slide. So when Device Manager shows no Neural processors, or Intel AI Boost-style driver errors appear, or every AI feature grays out at once, it's jarring. The reference device shouldn't have reference-device problems.

It does, though — and the causes are familiar: Windows Update driver swaps, interrupted driver installs, firmware enumeration hiccups, and the occasional genuinely confused driver stack. This guide is the Surface Pro-specific path, using Microsoft's own tools (Surface Diagnostic Toolkit, Surface driver packs) before generic fixes. For the Surface Laptop with similar symptoms, see [Surface Laptop AI features not working](/articles/surface-laptop-ai-features-not-working/); for the general NPU diagnosis that applies to all brands, see [NPU not detected in Windows 11](/articles/npu-not-detected-windows-11/) and our [Intel AI Boost driver install guide](/articles/intel-ai-boost-driver-not-installing/).

If the Pro runs hot while the NPU is missing, [AI PC running hot fix](/articles/ai-pc-running-hot-fix/) handles thermals in parallel.

## Why this happens

- **Windows Update driver swaps:** Update replaces Microsoft's matched NPU driver with a generic version that doesn't initialize on Surface hardware.
- **Interrupted driver installations:** The multi-stage NPU driver install corrupts if a reboot or update interrupts it mid-way.
- **Firmware enumeration failures:** The UEFI firmware occasionally fails to expose the NPU to Windows, especially after firmware updates.
- **Surface driver pack version skew:** Manually installed Surface driver MSIs can conflict with Windows Update's newer components.
- **Corrupted AI platform:** The Windows ML runtime or AI model packages corrupt independently of the driver, breaking features while the driver looks fine.
- **Detached keyboard/firmware state:** On a detachable, accessory firmware states can rarely interfere with device enumeration after sleep/wake cycles.

## How to fix it

Work through these in order — Microsoft's tools first.

### Fix 1: Verify the model and run full updates

Confirm Copilot+ eligibility, then let Microsoft's update stack do its work — most cases end here.

1. Check Settings > System > About: confirm Snapdragon X Elite/Plus (11th Edition or later).
2. Run Settings > Windows Update until completely clear, including optional driver updates.
3. Install the Surface app from the Microsoft Store and check for device updates there too.
4. Reboot (full restart, not fast-startup resume) and check Device Manager for Neural processors.
5. If the NPU appears, test an AI feature (Studio Effects in Camera app) to confirm function, not just presence.

### Fix 2: Use the Surface Diagnostic Toolkit

Microsoft's own diagnostic checks Surface-specific hardware and driver health, including the NPU.

1. Install the Surface Diagnostic Toolkit from the Microsoft Store.
2. Run the complete diagnostic — it tests firmware, drivers, and hardware enumeration.
3. Apply every recommended fix and reboot as instructed.
4. Re-check Device Manager: if the toolkit reports NPU hardware failure, stop here — that's a warranty case.
5. If the toolkit reports software issues fixed, verify AI features work before moving on.

### Fix 3: Clean-reinstall the NPU driver stack

When updates have tangled driver versions, a clean reinstall is the reliable untangler.

1. In Device Manager, find the NPU entry (Qualcomm Hexagon / Neural processors) — or note its absence.
2. If present with a warning: right-click > Uninstall device, check "delete the driver software."
3. Download the Surface driver pack for your exact model from Microsoft's [Surface support](https://support.microsoft.com/en-us/windows) downloads.
4. Install the driver pack (it includes the matched NPU driver), reboot.
5. Verify: Neural processors present without warnings; Task Manager > Performance shows the NPU graph.

### Fix 4: Reset firmware enumeration

If software is clean but the NPU still doesn't enumerate, force the firmware to rediscover hardware.

1. Shut down completely (hold Shift while clicking Shut down to bypass fast startup).
2. Wait 30 seconds, then boot into UEFI: hold Volume Up + Power on Surface Pro.
3. In UEFI, check Devices/Security for any NPU/AI-related toggles and ensure they're enabled.
4. Exit UEFI (saving if you changed anything) and boot normally.
5. Two-button reset as a deeper option: hold Power 30 seconds, then Volume Up + Power 15 seconds, release, power on.

### Fix 5: Repair the Windows AI platform

Driver healthy but AI features still dead? The platform layer above the driver is suspect.

1. Run `sfc /scannow` in an elevated terminal, then DISM restore-health.
2. Check for the AI/ML optional components: Settings > Apps > Optional features.
3. Re-register failing AI apps (Copilot: Settings > Apps > Advanced options > Repair/Reset).
4. Create a new local user account and test AI features there — profile corruption is a real (if rare) cause.
5. Keep Windows fully updated throughout — AI platform fixes ship in cumulative updates.

### Fix 6: Escalate to Microsoft with diagnostics in hand

The Surface Pro's advantage: first-party support with first-party diagnostics.

1. Save the Surface Diagnostic Toolkit's full report.
2. Document: exact model (11th Edition, configuration), OS build, driver versions, Device Manager screenshots.
3. Contact Microsoft Surface support with the package — the toolkit report short-circuits triage.
4. Under warranty (or Microsoft Complete), NPU hardware failure means device replacement — push for it with evidence.
5. Out of warranty: Microsoft's out-of-warranty service is the definitive hardware test.

## Closing

Surface Pro "NPU not detected" is a software problem until proven otherwise — Windows Update driver swaps and interrupted installs cause the large majority of cases, fixed by the update → Diagnostic Toolkit → clean driver reinstall sequence. The UEFI enumeration reset catches the firmware-level stragglers. Genuine NPU silicon failure on this device is rare, and the Surface Diagnostic Toolkit will tell you definitively when it's real. Come to support with the toolkit report and your documentation, and even the worst case resolves quickly.
