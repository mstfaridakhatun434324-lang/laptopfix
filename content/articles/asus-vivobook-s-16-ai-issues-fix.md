---
title: "How to Fix Asus VivoBook S 16 AI Issues on Windows 11"
slug: asus-vivobook-s-16-ai-issues-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["asus vivobook s 16", "ai laptop", "windows 11", "copilot pc", "npu", "troubleshooting"]
description: "Fix Asus VivoBook S 16 AI issues step by step: NPU driver updates, Copilot restore, Studio Effects repair, and power settings that keep AI features alive."
thumbnail: "/images/thumbs/asus-vivobook-s-16-ai-issues-fix.webp"
faqs:
  - q: "Why is Copilot slow on my VivoBook S 16?"
    a: >
      The usual cause is a parked NPU: either a battery-saving MyASUS profile or an outdated Intel AI Boost driver forcing AI work onto the CPU. Fix the profile and driver first.
  - q: "Does the VivoBook S 16 need a BIOS update for AI?"
    a: >
      Early BIOS versions did not fully expose the NPU, so yes — updating the BIOS is a required step if the NPU is missing or error-flagged in Device Manager.
  - q: "Why did AI features break after a Windows update?"
    a: >
      Feature updates can swap in a generic NPU driver or reset AI permissions. Reinstall the Asus driver and re-grant camera and microphone access.
  - q: "Can too many startup apps break AI features?"
    a: >
      They can make AI features look broken by starving them of CPU and memory headroom. Trimming startup apps is a quick, harmless diagnostic step.
---

The VivoBook S 16 brings Copilot+ AI to a big-screen, budget-friendly chassis, but its value depends on the NPU actually doing its job. When Copilot stalls, live captions drop out, or Studio Effects refuse to engage, the laptop still works — it just stops being an AI PC.

VivoBook S 16 AI faults usually come from the same family of causes as its pricier Asus siblings: an outdated Intel AI Boost driver, MyASUS power profiles that park the NPU, or a Windows update that quietly reset AI permissions. The fixes are the same too, which is good news.

Follow these six fixes in order, testing after each one. Most VivoBook S 16 owners resolve the problem before reaching the final driver sweep.

## Why this happens

- **Outdated Intel AI Boost driver:** The factory NPU driver lags behind Windows AI runtime updates, so Copilot+ features fail on launch or run unbearably slowly.
- **MyASUS battery profiles parking the NPU:** Aggressive power saving on this value model can throttle the NPU hard enough that AI workloads time out.
- **BIOS lagging AI firmware:** Early VivoBook S 16 BIOS versions did not fully expose the NPU to Windows.
- **Windows update resetting permissions:** Feature updates can revoke camera, microphone, and activity permissions that AI features depend on.
- **Background app overload on a value CPU:** Too many startup apps competing with AI workloads can make the NPU look broken when it is simply starved of resources.
- **Corrupted Copilot Runtime files:** A damaged shared runtime breaks Copilot, Recall, and Studio Effects at the same time.
- **Missing VivoBook AI software bundle:** The value VivoBook bundle sometimes ships without the AI utilities installed, leaving Copilot+ features partially functional despite healthy drivers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the NPU is detected

Start with the same check a technician would: is Windows even seeing the NPU? The answer decides whether you need BIOS work or software repair.

1. Open Task Manager, go to Performance, and look for an NPU entry.
2. If absent, open Device Manager and check System devices for Intel AI Boost.
3. Note any warning icon or error code on the device.
4. Restart into the BIOS with F2 and confirm NPU options are enabled.
5. Recheck Task Manager after booting back into Windows.

### Fix 2: Update BIOS and NPU driver together

Asus ships BIOS and NPU driver updates as a pair. Installing one without the other is a reliable way to keep AI features broken. Use only official sources for drivers and update help, such as [Microsoft Windows support](https://support.microsoft.com/en-us/windows) [Intel support](https://www.intel.com/content/www/us/en/support/detect.html).

1. Find your exact VivoBook S 16 model in Settings, then visit the Asus support page.
2. Download the latest BIOS and Intel AI Boost driver for Windows 11.
3. Install the BIOS update on AC power and let it restart automatically.
4. Install the NPU driver, restart, and confirm the NPU in Task Manager.
5. Test a Copilot+ feature immediately.

### Fix 3: Switch MyASUS to a balanced power profile

The VivoBook line leans hard into battery life, and its default profile can park the NPU. A balanced profile restores AI performance with a modest battery tradeoff.

1. Open MyASUS and select Balanced or Performance, not Battery Saving.
2. Set Windows Power mode to Best performance while testing.
3. Disable any MyASUS option that limits background AI acceleration.
4. Test on AC power first to isolate power as the variable.
5. Keep the balanced profile for daily use once AI features work.

### Fix 4: Trim startup load and re-grant permissions

Two quick wins in one fix: fewer competing startup apps, and permissions restored after an update reset them. The same permission reset also helps with the related fault covered in [AI laptop speaker crackling](/articles/ai-laptop-speakers-crackling-fix/).

1. Open Task Manager, go to Startup apps, and disable anything you do not need at boot.
2. Open Settings, then Privacy and security, and re-enable Camera and Microphone access for AI apps.
3. Toggle each Studio Effect off and on in Quick Settings.
4. Restart and test the previously failing AI feature.
5. If it still fails, the runtime repair in the next fix is the likely answer.

### Fix 5: Repair the Windows Copilot Runtime

When several AI features fail together, the shared runtime is the prime suspect. Repairing it fixes the group, not just one app.

1. Run the Windows Update troubleshooter from Settings, System, Recovery.
2. In elevated PowerShell, run the system file checker to repair Windows files.
3. Install all pending Windows updates and restart.
4. Verify AI features are listed in Settings after the restart.
5. Continue to the driver sweep if problems persist.

### Fix 6: Clean-reinstall drivers and cross-check guides

A stale driver stack can survive ordinary updates. A full sweep with fresh Asus drivers clears it, and sibling-model guides confirm platform-wide causes. Related guides on the same platform include [Acer TravelMate P6 AI fixes](/articles/acer-travelmate-p6-ai-issues-fix/) and [Recall snapshot viewer zoom](/articles/recall-snapshot-viewer-zoom-fix/).

1. Uninstall Intel AI Boost and the graphics adapter in Device Manager, removing driver software.
2. Restart, then install the latest Asus graphics and NPU drivers from the support site.
3. Apply Windows updates, restart, and retest every broken AI feature.
4. Compare with the companion guide for the next model in this Asus series, which shares the same platform.
5. Also check the guide on zooming AI snapshot viewers, since viewer and permission issues often travel together.

### Fix 7: Reinstall the VivoBook AI software bundle

The VivoBook AI software bundle contains the utilities and services that Copilot+ features depend on, and a missing or partial install can leave features half-working in confusing ways. Reinstalling the bundle from Asus support restores the complete set in one pass, which is faster than chasing individual missing components.

1. Download the latest VivoBook S 16 software bundle from the Asus support page.
2. Uninstall any existing Asus AI utilities first to avoid version conflicts.
3. Run the bundle installer and restart when prompted.
4. Open Settings and confirm AI features are listed after the reinstall.
5. Test each previously broken AI feature in turn to confirm the bundle fixed it.

## Closing

VivoBook S 16 AI issues are almost never a reason to return the laptop. Pair the BIOS and NPU driver updates, keep MyASUS on a balanced profile, trim startup clutter, and re-check permissions after Windows updates. Once Task Manager shows a healthy NPU, the AI features that define this machine should stay reliable.
