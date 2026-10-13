---
title: "How to Fix Cortana High CPU in Windows 11: Step-by-Step"
slug: "how-to-fix-cortana-high-cpu-windows-11-step-by-step"
date: "2026-10-07"
categories: ["performance"]
tags: ["cortana high cpu fix", "disable cortana step by step", "cortana background process", "windows 11 cortana cpu", "remove cortana"]
description: "Step-by-step instructions to stop Cortana’s background CPU usage in Windows 11 — from quick settings changes to complete removal."
thumbnail: "/images/thumbs/how-to-fix-cortana-high-cpu-windows-11-step-by-step.webp"
faqs:
  - q: "Which step should most people stop at?"
    a: "Steps 1–3 (background permission, speech recognition, scheduled tasks) solve the problem for most users while keeping Cortana technically available. Go to Step 4–5 if processes still appear at boot or return after updates. Reserve Step 6 (uninstall) for when you are certain you will never use Cortana — though even that is reversible via the Microsoft Store."
  - q: "Can I reinstall Cortana after removing it?"
    a: "Yes. The Cortana app remains available in the Microsoft Store, so uninstalling via PowerShell is reversible — search for Cortana in the Store and reinstall. The policy/registry disable (Step 5) should be reverted first if you used it, since it blocks the app from running even when installed."
  - q: "Does this affect voice typing (Win + H)?"
    a: "Potentially, if you disabled online speech recognition in Step 2 — voice typing uses those speech services. If you dictate regularly, skip Step 2 and rely on Steps 1, 3, and 4 instead; they target Cortana specifically without touching the shared speech stack that voice typing needs."
  - q: "Why do I still see SearchHost.exe after removing Cortana?"
    a: "That is expected and fine. SearchHost.exe is the Windows Search interface process, not Cortana — it powers the Start-menu search box and is supposed to be there. Removing Cortana does not remove Windows Search, and SearchHost using brief CPU when you actively search is normal behavior, not a leftover problem."
---

Cortana may be retired as a consumer assistant, but its processes can still consume CPU on Windows 11 machines — background tasks firing on schedules, the app pre-launching at boot, speech services idling expensively. If Task Manager shows Cortana-related activity you never asked for, this step-by-step guide eliminates it in escalating stages.

Each step is independent and safe to stop at: Step 1–3 calm it down while keeping it available; Steps 4–6 shut it down firmly. Pick the depth that matches how done you are with Cortana.

## Why this happens

- **Background app permission granted:** Lets Cortana run and consume CPU when not in use.
- **Scheduled maintenance tasks:** Periodic wake-ups for updates and telemetry.
- **Startup pre-launch:** Registered to start with Windows on many OEM images.
- **Online speech recognition active:** Keeps speech services processing in the background.
- **Microsoft account sync attempts:** Background sync work for an unused assistant.
- **Corrupted app package:** Damaged Store package looping its background host.
- **Update re-enablement:** Feature updates restoring Cortana components.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Step 1: Revoke background app permission

The fastest win. Cutting background permission stops Cortana from running when you are not using it — which, for most people, is always.

1. Open Settings > Apps > Installed apps.
2. Find Cortana, click ... > Advanced options.
3. Set Background apps permissions to Never.
4. Close Settings; check Task Manager in 10 minutes for improvement.

### Fix 2: Step 2: Disable online speech recognition

Cortana leans on Windows speech services. If you do not dictate or use voice typing, disabling online speech recognition removes a whole background subsystem Cortana was exercising.

1. Go to Settings > Privacy & security > Speech.
2. Turn off Online speech recognition.
3. If prompted, also turn off ‘Let apps access speech services’ for apps you do not need.
4. Restart and observe background CPU.

### Fix 3: Step 3: Disable Cortana's scheduled tasks

Background spikes on a schedule — every hour, at logon — come from Task Scheduler. Disabling Cortana's tasks there is precise and reversible.

1. Open Task Scheduler (search in Start).
2. Navigate Task Scheduler Library > Microsoft > Windows.
3. Locate Cortana / SpeechRuntime-related tasks; right-click each > Disable.
4. Watch for 24 hours: scheduled spikes should stop.

### Fix 4: Step 4: Remove Cortana from startup

If a Cortana process appears at every boot, it is registered somewhere in the startup chain. Clearing those registrations stops boot-time activity. Combine with [broader startup cleanup](/articles/how-to-disable-startup-programs-windows-11/) for a fully lean boot.

1. Open Task Manager > Startup apps; disable any Cortana entry.
2. Press Win + R, type shell:startup, and remove Cortana shortcuts.
3. Also check shell:common startup for machine-wide entries.
4. Restart and confirm no Cortana process auto-starts.

### Fix 5: Step 5: Policy-disable Cortana (persistent)

Settings and scheduler changes can be undone by updates. The policy/registry disable is the enterprise-grade method that persists — use it when you want Cortana gone and staying gone.

1. Windows Pro: gpedit.msc > Computer Configuration > Administrative Templates > Windows Components > Search > set ‘Allow Cortana’ to Disabled.
2. Windows Home: open regedit, go to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search (create keys as needed), add DWORD AllowCortana = 0.
3. Restart the PC.
4. Verify in Task Manager that Cortana processes no longer launch.

### Fix 6: Step 6: Uninstall the Cortana package

The final stage: remove the app entirely. Safe on Windows 11 — Search keeps working, nothing else depends on it. [Microsoft's support documentation](https://support.microsoft.com/en-us/windows) notes Cortana's deprecation, so removal aligns with where Windows is headed anyway.

1. Open PowerShell as administrator.
2. Run: Get-AppxPackage -allusers Microsoft.549981C3F5F10 | Remove-AppxPackage -AllUsers
3. If the package name differs on your build, list with Get-AppxPackage *Cortana* first.
4. Restart; confirm no Cortana processes exist and Search still works.

### Fix 7: Step 7: Verify and guard against return

Close the loop: verify the fix held across a couple of days and one update cycle, so you are not revisiting this in a month.

1. Monitor Task Manager for 48 hours.
2. After the next Patch Tuesday updates, re-check.
3. If anything returned, the policy/registry step is the one to re-apply.
4. Done — enjoy the reclaimed CPU and quieter fans.

### Fix 8: Clean up related speech and telemetry services

Cortana does not work alone: Windows speech runtime, telemetry, and ‘connected user experiences’ services all feed it and can generate their own background CPU even after Cortana itself is quiet. Calming this supporting cast finishes the job. This pairs well with [startup cleanup](/articles/how-to-disable-startup-programs-windows-11/) since several of these services register background triggers.

1. Open services.msc and review: Connected User Experiences and Telemetry (DiagTrack), Speech-related services.
2. If you do not use dictation or Timeline features, set DiagTrack to Manual.
3. In Settings > Privacy & security > Diagnostics & feedback, set diagnostic data to Required only.
4. Turn off ‘Tailored experiences’ and ‘Improve inking and typing’ in the same page.
5. In Task Scheduler > Microsoft > Windows > Customer Experience Improvement Program, disable its tasks.
6. Restart and monitor background CPU for 48 hours to confirm lasting quiet.

If you'd rather work from a condensed checklist than this full staircase, our [Cortana high-CPU walkthrough](/articles/best-way-to-fix-cortana-high-cpu-windows-11/) covers the same ground with just the steps that matter.

## Closing

Fixing Cortana high CPU is a staircase: revoke background permission, disable speech services and scheduled tasks, clear startup, policy-disable, and finally uninstall. Stop at whatever step solves it for you — most users never need past Step 4. The key point is that every stage is safe and reversible until the final uninstall, and Windows Search never depends on Cortana at any stage. Make a habit of checking Task Manager's Startup tab quarterly — Windows updates and new software gradually re-register background tasks, and catching them early keeps idle CPU near zero. If Cortana ever returns despite the policy disable, repeat Step 5 before anything else: it is the most persistent control in this guide. Done in this order, the whole process takes under thirty minutes and the silence lasts.
