---
title: "How to Disable Recall in Windows 11 (3 Methods)"
slug: how-to-disable-recall-windows-11
date: 2026-10-19
categories: ["ai-pc"]
tags: ["disable recall", "windows recall", "privacy", "windows 11", "turn off"]
description: "How to disable Recall in Windows 11? Three reliable methods to turn off Recall snapshots completely, plus how to delete existing data."
thumbnail: "/images/thumbs/how-to-disable-recall-windows-11.webp"
faqs:
  - q: "Is it safe to disable Recall?"
    a: "Yes, completely. Recall is an optional feature; disabling it affects nothing else in Windows. Your PC works exactly as before, minus the snapshot timeline."
  - q: "Does disabling Recall delete my existing snapshots?"
    a: "Not automatically. Turning off saving stops new snapshots, but old ones remain until you explicitly delete them. Always delete snapshots separately if privacy is your concern."
  - q: "Can my employer re-enable Recall after I disable it?"
    a: "On work-managed machines, IT policy overrides local settings. If Recall is policy-controlled, your toggle may be greyed out or reverted — that is intentional enterprise management."
  - q: "Will disabling Recall improve battery life?"
    a: "Yes, noticeably. Recall's constant snapshotting and on-device AI processing is one of the heaviest NPU consumers. Disabling it is among the biggest single battery savers on Copilot+ PCs."
---

Not everyone wants Windows photographing their screen every few seconds — and that is a perfectly valid choice. Whether for privacy, battery life, disk space, or simple preference, disabling Recall is straightforward. What trips people up is doing it incompletely: turning off saving but leaving gigabytes of old snapshots behind, or using one method while another re-enables it.

This guide covers three reliable methods plus the cleanup step everyone forgets. If Recall is broken rather than unwanted, our [Recall not working guide](/articles/windows-recall-not-working/) fixes it instead.

## Why this happens

- **Privacy:** A searchable screenshot database is a sensitive target; some users prefer it never exist. Even stored locally and encrypted, the concept bothers people — and that discomfort is reason enough.
- **Battery life:** Constant snapshotting and NPU processing measurably drain the battery. On travel days, every consumer you can switch off extends runtime.
- **Disk space:** Snapshots and their AI index consume tens of gigabytes — significant on 256GB drives.
- **Performance:** On busy systems, the capture pipeline adds background load that can show up as micro-stutters.
- **Policy/compliance:** Some workplaces and regulated industries forbid screen-capture AI outright.
- **Simplicity:** If you never open the timeline, it is pure overhead with zero benefit to you.

## How to fix it

Use one method — then do the cleanup.

### Method 1: Settings toggle (easiest)

The official off switch.

1. Open Settings, Privacy & security, Recall & snapshots.
2. Toggle "Save snapshots" to Off.
3. Confirm any prompt — new snapshots stop immediately; the system tray icon should reflect the paused state.
4. Verify: use the PC for 10 minutes, open Recall, confirm the timeline shows no new entries.
5. This stops future capture but keeps existing snapshots — do the cleanup in "Delete existing data" below.

### Method 2: Group Policy (Pro/Enterprise, most thorough)

Policy-level disable that survives feature updates better.

1. Press Win + R, type `gpedit.msc`, Enter.
2. Navigate to Computer Configuration, Administrative Templates, Windows Components, Windows AI (or Windows Recall on some builds).
3. Open "Turn off saving snapshots for Windows Recall" (exact name varies by build).
4. Set it to Enabled (Enabled = feature off, confusingly), click OK.
5. Reboot and verify in Settings that the toggle is off or greyed out.

### Method 3: Registry (Home edition)

The Home-edition equivalent of Group Policy.

1. Press Win + R, type `regedit`, Enter (approve the UAC prompt).
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsAI` (create keys if missing).
3. Create a DWORD (32-bit) named `TurnOffSavingSnapshots` set to `1`.
4. Reboot.
5. Verify in Settings — saving should be off. To re-enable later, delete the value or set it to `0`.

### What disabling does NOT turn off

Clear up the common confusion about scope.

1. Disabling Recall stops snapshot capture only — other Copilot+ features (Live Captions, Studio Effects, Click to Do) keep working independently.
2. The NPU itself stays active for those other features; only Recall's workload stops.
3. Windows Search, Timeline, and File Explorer history are separate systems — untouched by Recall settings.
4. If you want all AI features off, that is a bigger job — see our guide on [turning off AI features](/articles/turn-off-ai-features-windows-11/).
5. Copilot (the assistant app) is unrelated to Recall — disabling one does not affect the other.

### Delete existing data (do not skip)

Disabling stops new snapshots; old ones remain until deleted.

1. Settings, Privacy & security, Recall & snapshots — click "Delete snapshots."
2. Choose the time range (or all) and confirm.
3. Check disk space before and after — you should reclaim gigabytes.
4. Our [delete snapshots guide](/articles/delete-recall-snapshots/) covers selective deletion if you want to keep some history.
5. After deletion, spot-check the timeline to confirm it is empty.

### Verify it stays off

Windows updates occasionally reset feature toggles.

1. After each major Windows update, glance at Recall settings to confirm saving is still off.
2. If using Group Policy/registry, the setting normally persists — the Settings toggle alone is the one updates sometimes flip.
3. Watch for new "AI features" prompts after updates that quietly re-enable capture — decline them.
4. If the toggle is greyed out and you did not set a policy, your organization did — check with IT rather than fighting it.
5. Battery and disk improvements should be noticeable within a day of proper disabling.

## Closing

Disabling Recall is a two-part job: stop the capture (any of the three methods), then delete the existing snapshots. Most people do only the first half and wonder why gigabytes remain and the timeline still shows old entries. If disk pressure is your motivation, our [Recall disk usage guide](/articles/recall-using-too-much-disk-space/) covers trimming storage without fully disabling — but done completely, Recall becomes zero-footprint: no snapshots, no NPU drain, no disk usage — while the rest of Windows carries on untouched. If you are disabling because Recall never worked on your machine in the first place, check [why Recall is unavailable on some PCs](/articles/recall-not-available-on-my-pc/) before assuming it is broken. And if you ever change your mind, re-enabling is just the same steps in reverse, though you will be starting the snapshot history from scratch. Either way, the choice is yours and takes effect immediately — no restart required for the Settings method.
