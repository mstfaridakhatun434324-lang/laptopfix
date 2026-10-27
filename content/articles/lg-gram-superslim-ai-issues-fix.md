---
title: "How to Fix LG Gram SuperSlim AI Issues on Windows 11"
slug: lg-gram-superslim-ai-issues-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["lg gram superslim", "ai laptop", "ultralight laptop", "windows 11", "npu", "troubleshooting"]
description: "Fix LG Gram SuperSlim AI issues: ultralight NPU throttling, Copilot failures, Studio Effects glitches, and battery profiles that stall AI features quickly."
thumbnail: "/images/thumbs/lg-gram-superslim-ai-issues-fix.webp"
faqs:
  - q: "Why do AI features slow down on the Gram SuperSlim?"
    a: >
      Heat is the usual suspect: the ultralight chassis throttles the NPU under sustained AI load. Keep vents clear and test with the laptop cool.
  - q: "Does the Gram SuperSlim need a BIOS update for AI?"
    a: >
      Early BIOS versions did not fully expose the NPU, so updating the BIOS is required when the NPU is missing or flagged in Device Manager.
  - q: "Why did AI features stop after a Windows update?"
    a: >
      Feature updates can replace the validated NPU driver or reset AI permissions. Reinstall the LG driver and re-grant camera and microphone access.
  - q: "Should I use battery-saver mode on an AI laptop?"
    a: >
      Not during AI work. Battery profiles can park the NPU, which defeats the purpose of the AI hardware. Use Balanced instead.
---

The Gram SuperSlim is one of the lightest AI laptops you can buy, and that featherweight design is both its charm and its AI challenge: a tiny chassis heats up fast, and power profiles tuned for battery life can park the NPU just when AI work needs it.

On the Gram SuperSlim, AI faults come from thermal throttling, LG power profiles that prioritize battery over acceleration, Intel AI Boost drivers that lag Windows updates, or permissions reset by a feature update.

These six fixes run in technician order, with the ultralight-specific heat and power checks included. Test after each step.

## Why this happens

- **Thermal throttling in an ultralight chassis:** Sustained AI workloads heat a SuperSlim quickly, and the NPU clocks down to protect itself.
- **LG power profiles parking the NPU:** Battery-first profiles in LG software can throttle the NPU enough that AI workloads time out.
- **Outdated Intel AI Boost driver:** The factory NPU driver lags behind Windows AI runtime updates, so Copilot+ features fail.
- **BIOS lagging AI firmware:** Early Gram SuperSlim BIOS versions did not fully expose the NPU to Windows.
- **Windows update resetting permissions:** Feature updates can revoke camera, microphone, and activity permissions that AI features need.
- **Corrupted Copilot Runtime files:** A damaged shared runtime breaks Copilot, Recall, and Studio Effects simultaneously.
- **LG Smart Assistant interference:** LG Smart Assistant can override Windows power settings for AI workloads, reapplying battery-first limits after you set a balanced profile.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check NPU detection, heat, and airflow together

On an ultralight, heat and driver faults look identical. Check all three variables before changing software.

1. Open Task Manager and confirm an NPU entry under Performance.
2. If it is missing, check Device Manager for Intel AI Boost and note any warning icon.
3. Confirm the laptop sits on a hard surface with vents unblocked.
4. Let a hot machine cool, then retest the failing AI feature.
5. Restart into the BIOS and confirm NPU options are enabled if detection fails.

### Fix 2: Update BIOS and Intel AI Boost driver

LG pairs BIOS and NPU driver updates. Installing both together is the reliable way to expose the NPU fully. Use only official sources for drivers and update help, such as [Microsoft Windows support](https://support.microsoft.com/en-us/windows) [Intel support](https://www.intel.com/content/www/us/en/support/detect.html).

1. Find your exact Gram SuperSlim model in Settings, then open the LG support page.
2. Download the latest BIOS and Intel AI Boost driver for Windows 11.
3. Install the BIOS update on AC power and allow the automatic restart.
4. Install the NPU driver, restart, and verify the NPU in Task Manager.
5. Test a Copilot+ feature immediately.

### Fix 3: Switch LG power settings to Balanced

The Gram line chases battery records, and its default profile can park the NPU. Balanced restores AI performance at a modest battery cost.

1. Open LG software or Windows Settings and choose Balanced.
2. Set Windows Power mode to Best performance while testing.
3. Disable any setting that limits background acceleration on battery.
4. Test AI features on AC power to isolate power as the variable.
5. Keep the balanced profile for daily use once confirmed.

### Fix 4: Re-grant AI permissions

Updates can silently revoke the camera and microphone permissions AI features need. Re-granting them is quick and often decisive. The same permission reset also helps with the related fault covered in [AI PC BIOS update failures](/articles/ai-pc-bios-update-failed/).

1. Open Settings, then Privacy and security, and check Camera and Microphone access.
2. Re-enable any app that lost permission after the last update.
3. Toggle each Studio Effect off and on in Quick Settings.
4. Test with the Camera app to isolate the pipeline from meeting software.
5. If effects stay greyed out, continue to the runtime repair.

### Fix 5: Repair the Windows Copilot Runtime

When several AI features fail together, the shared runtime is the prime suspect. Repairing it fixes the group, not just one app.

1. Run the Windows Update troubleshooter from Settings, System, Recovery.
2. In elevated PowerShell, run the system file checker to repair Windows files.
3. Install all pending Windows updates and restart.
4. Confirm AI features are listed in Settings after the restart.
5. Move to the final sweep if problems persist.

### Fix 6: Clean-reinstall drivers and manage thermals

A stale driver stack can survive normal updates, and a hot ultralight chassis can throttle even a healthy NPU. Address both here. Related guides on the same platform include [Razer Blade 14 AI fixes](/articles/razer-blade-14-ai-laptop-issues-fix/) and [USB4 device not recognized](/articles/usb4-device-not-recognized-ai-laptop-fix/).

1. Uninstall Intel AI Boost and the graphics adapter in Device Manager, removing driver software.
2. Restart and install the latest LG graphics and NPU drivers from the support site.
3. Use the laptop on a hard surface, keep vents clear, and avoid heavy AI sessions on soft bedding.
4. Apply Windows updates, restart, and retest every broken AI feature.
5. If throttling persists, a small laptop stand improves airflow noticeably.

### Fix 7: Reset LG Gram power and fan controls

LG power software can fight Windows power settings: you set Balanced in Windows, and LG Smart Assistant quietly reapplies its own battery-first profile afterward. Resetting LG power and fan controls to defaults and then setting a single source of truth for power management ends the tug-of-war that keeps parking the NPU.

1. Open LG Smart Assistant or LG software power settings.
2. Reset power and fan controls to factory defaults.
3. Set Windows Power mode to Balanced as the single power authority.
4. Disable any LG setting that overrides Windows power plans.
5. Test AI features on AC power and confirm the NPU stays active.

## Closing

Gram SuperSlim AI issues are usually heat, power profiles, or drivers — not a dead NPU. Update the BIOS and driver together, keep power balanced, keep airflow clear, and re-check permissions after updates. Once the NPU shows healthy and cool, AI features should run as lightly and quietly as the laptop itself.
