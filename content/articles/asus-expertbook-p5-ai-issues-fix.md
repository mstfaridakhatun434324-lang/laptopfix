---
title: "How to Fix Asus ExpertBook P5 AI Issues on Windows 11"
slug: asus-expertbook-p5-ai-issues-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["asus expertbook p5", "ai laptop", "windows 11", "copilot pc", "npu", "troubleshooting"]
description: "Fix Asus ExpertBook P5 AI issues with proven steps: NPU driver repair, Copilot restore, Studio Effects fixes, and power settings that keep AI working."
thumbnail: "/images/thumbs/asus-expertbook-p5-ai-issues-fix.webp"
faqs:
  - q: "Why is the NPU missing from Task Manager on my ExpertBook P5?"
    a: >
      The usual reason is an old BIOS that does not expose the NPU, or an outdated Intel AI Boost driver. Update both from the Asus support page and the NPU should appear.
  - q: "Does MyASUS really block AI features?"
    a: >
      Yes. MyASUS battery-saving profiles can park the NPU, which makes AI workloads time out or fall back to the slow CPU path. Switch to Balanced or Performance while testing.
  - q: "Why did AI features break after a Windows update?"
    a: >
      Feature updates can replace the validated NPU driver or reset AI privacy permissions. Reinstalling the Asus driver and re-granting permissions fixes most post-update failures.
  - q: "Should I update the BIOS just for AI features?"
    a: >
      If your BIOS predates the AI firmware updates, yes. The BIOS controls whether Windows can see and use the NPU at all, so it is a prerequisite, not an optional extra.
---

The Asus ExpertBook P5 is built for business AI workloads, with an Intel Core Ultra chip and a dedicated NPU that powers Copilot+ features, live captions, and background effects. When those features stutter, vanish, or refuse to start, the business case for the machine evaporates with them.

On the ExpertBook P5, AI failures usually come from MyASUS power profiles, an Intel AI Boost driver that lags behind Windows updates, or a BIOS that needs updating before the NPU is fully exposed. A fourth cause, less obvious, is Asus system utilities conflicting with Windows AI services after an update.

This guide gives you six fixes in technician order. Work through them one at a time and test after each step — most ExpertBook P5 owners find the answer in the first three.

## Why this happens

- **MyASUS power profile throttling the NPU:** MyASUS battery-saving modes can park the NPU, so AI features time out or run on the CPU at a crawl.
- **Outdated Intel AI Boost driver:** The factory NPU driver predates current Windows AI runtime updates, which causes Copilot+ features to fail on launch.
- **BIOS version lagging AI firmware:** Early ExpertBook P5 BIOS releases did not fully hand the NPU to Windows, leaving it hidden or error-flagged.
- **Windows update resetting AI permissions:** Feature updates can revoke camera, microphone, and activity permissions that Studio Effects and Recall depend on.
- **Conflicting Asus utilities:** Older versions of Asus camera or audio utilities can hook the same pipeline that Windows Studio Effects needs.
- **Corrupted Windows AI runtime files:** The shared Copilot Runtime can corrupt during a failed update, breaking every AI feature at once.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the NPU is visible in Task Manager

Before changing anything, confirm Windows can see the NPU. This single check splits the problem into hardware exposure versus software failure.

1. Press Ctrl + Shift + Esc, open the Performance tab, and look for an NPU entry.
2. If it is missing, open Device Manager and check System devices for Intel AI Boost.
3. Note any warning icon and error code shown on the Intel AI Boost device.
4. Restart into the BIOS with F2 and confirm NPU or AI acceleration options are enabled.
5. Return to Windows and recheck Task Manager before continuing.

### Fix 2: Update the BIOS and NPU driver together

Asus releases BIOS and NPU driver updates as matched pairs. Installing one without the other leaves the NPU half-configured, which is why AI features break after partial updates. Use only official sources for drivers and update help, such as [Microsoft Windows support](https://support.microsoft.com/en-us/windows) [Intel support](https://www.intel.com/content/www/us/en/support/detect.html).

1. Find your exact ExpertBook P5 model in Settings, then visit the Asus support page for that model.
2. Download the latest BIOS and the Intel AI Boost driver for Windows 11.
3. Install the BIOS update with the charger connected and let the machine restart by itself.
4. Install the NPU driver package, restart again, and confirm the NPU appears healthy in Task Manager.
5. Test a Copilot+ feature immediately to confirm the pairing worked.

### Fix 3: Set MyASUS to a performance-friendly profile

MyASUS can override Windows power settings in ways that are invisible in the Settings app. A battery profile that parks the NPU is a classic ExpertBook trap.

1. Open MyASUS and switch the power profile to Performance or Balanced.
2. In Windows Settings, set Power mode to Best performance while you test.
3. Turn off any MyASUS option that limits AI or background acceleration on battery.
4. Plug in the charger and retest the failing feature to isolate power as the cause.
5. Once confirmed, settle on a balanced profile for daily use.

### Fix 4: Re-grant AI privacy permissions

After a Windows feature update, camera and microphone permissions can reset without warning. AI features then fail silently because they are blocked, not broken. The same permission reset also helps with the related fault covered in [AI laptop microphone problems](/articles/ai-laptop-microphone-not-working/).

1. Open Settings, then Privacy and security, and check Camera and Microphone permissions.
2. Allow the apps that use AI features, toggling any that were reset back on.
3. Open Quick Settings and toggle each Windows Studio Effect off and on again.
4. Test the Camera app, which exercises the same pipeline without a meeting app involved.
5. If effects remain greyed out, move to the runtime repair in the next fix.

### Fix 5: Repair the Windows Copilot Runtime

When Copilot, Recall, and Studio Effects fail together, the shared runtime is the common thread. Repairing it fixes all of them at once.

1. Open Settings, then System, then Recovery, and run the Windows Update troubleshooter.
2. In an elevated PowerShell window, run the system file checker to repair damaged Windows files.
3. Install all pending Windows updates, since runtime fixes arrive through cumulative updates.
4. Restart and confirm AI features reappear in Settings.
5. If the problem persists, the driver sweep in the final fix is the next step.

### Fix 6: Clean-reinstall the driver stack and cross-check

A stale driver stack can survive normal updates and keep AI features broken. A full sweep with fresh Asus drivers clears it, and related guides catch shared causes. Related guides on the same platform include [Asus ZenBook 14 OLED AI fixes](/articles/asus-zenbook-14-oled-ai-issues-fix/) and [Recall after an account switch](/articles/recall-not-working-after-account-switch-fix/).

1. In Device Manager, uninstall Intel AI Boost and the graphics adapter, removing driver software.
2. Restart, then install the latest Asus graphics and NPU drivers from the support site.
3. Apply pending Windows updates, restart again, and retest every broken AI feature.
4. Compare notes with the companion guide for the next Asus model in this series, which shares the same Intel platform.
5. Also check the guide on restoring AI features after an account change, since identity and permission faults often appear together.

## Closing

ExpertBook P5 AI trouble is rarely a hardware fault. Keep the BIOS and NPU driver updated as a pair, keep MyASUS out of aggressive battery modes while AI work runs, and re-check permissions after every Windows feature update. With the NPU visible and healthy in Task Manager, the AI features this laptop was sold on should work the way they were meant to.
