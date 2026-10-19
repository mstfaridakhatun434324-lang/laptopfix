---
title: "Windows Recall Not Working? Fix It Step by Step"
slug: windows-recall-not-working
date: 2026-10-19
categories: ["ai-pc"]
tags: ["windows recall", "recall not working", "copilot plus pc", "windows 11", "npu"]
description: "Windows Recall not working on your Copilot+ PC? Diagnose why Recall fails to open, search, or save — and fix it with these proven steps."
thumbnail: "/images/thumbs/windows-recall-not-working.webp"
faqs:
  - q: "Why won't Recall open at all?"
    a: "The usual suspects: your PC does not meet Copilot+ requirements, Recall is disabled in settings, or the NPU driver is broken. Recall also requires Windows Hello sign-in — without it, the app refuses to launch for security reasons."
  - q: "Does Recall need an NPU to work?"
    a: "Yes. Recall's on-device AI processing requires a Copilot+ certified NPU (40+ TOPS). Without a working NPU driver, Recall cannot function even if everything else is correct."
  - q: "Can I use Recall without Windows Hello?"
    a: "No. Microsoft requires Windows Hello (face, fingerprint, or PIN) as a security gate for Recall's snapshot database. Set up Windows Hello first, then enable Recall."
  - q: "Is Recall available in all regions?"
    a: "Recall rolled out gradually and was initially limited in some regions (notably the EU/EEA at launch). If your region blocks it, the feature may simply not appear regardless of hardware."
---

Recall promises a photographic memory for your PC — every app, document, and website, searchable by describing it. When it works, it feels like magic. When it does not open, does not search, or sits stuck "setting up," it is just another broken Windows feature. The fixes depend on which flavor of broken you have, so start by identifying your symptom.

Recall has hard requirements: Copilot+ PC (40+ TOPS NPU, 16GB RAM, 256GB storage), Windows Hello enabled, and a working NPU driver. If your machine does not qualify, see [why Recall is not available on your PC](/articles/recall-not-available-on-my-pc/) — no troubleshooting overcomes missing hardware.

## Why this happens

- **Not a Copilot+ PC:** The most common root cause — the hardware bar is real and non-negotiable.
- **Windows Hello not set up:** Recall's security model requires Hello; without it, Recall will not launch.
- **NPU driver broken or missing:** Recall's AI engine needs the NPU; a bad driver kills the whole feature.
- **Recall disabled in settings:** It can be toggled off by policy, by debloat tools, or by the user long ago.
- **Corrupted snapshot database:** A damaged local database makes Recall crash or hang on launch.
- **Insufficient disk space:** Recall needs room for snapshots and its AI index — a full drive stops it cold.
- **Region restrictions:** Some regions had delayed or limited Recall availability.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the requirements

Do not troubleshoot hardware you do not have.

1. Confirm Copilot+ status: 40+ TOPS NPU, 16GB+ RAM, 256GB+ storage — see our [requirements guide](/articles/windows-recall-system-requirements/).
2. Settings, Accounts, Sign-in options — set up Windows Hello (PIN minimum; face/fingerprint better).
3. Confirm the NPU works: Task Manager, Performance tab, NPU entry present and active.
4. If any requirement fails, stop here — Recall cannot run until it is met.
5. If all pass and Recall still fails, continue — this is now a software problem.

### Fix 2: Check that Recall is actually enabled

It is off more often than people think.

1. Settings, Privacy & security, Recall & snapshots.
2. Verify "Save snapshots" is toggled on.
3. Check for group policy or registry disables — especially on work machines or after running debloat scripts.
4. If you previously followed a [disable-Recall guide](/articles/how-to-disable-recall-windows-11/), reverse those exact steps.
5. Toggle it off and back on once — this restarts the snapshot service cleanly.

### Fix 3: Fix the NPU driver

Recall without a working NPU is a non-starter.

1. Device Manager: verify Neural processors shows a clean NPU entry, no warnings.
2. If broken, reinstall the OEM NPU/chipset driver ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
3. Reboot and confirm Task Manager's NPU graph is live.
4. Retry Recall — NPU driver fixes resolve a large share of "won't open" cases.
5. Keep the driver current; Recall updates often need matching driver capabilities.

### Fix 4: Repair the snapshot database

A corrupted database hangs or crashes Recall.

1. Settings, Privacy & security, Recall & snapshots — note your current snapshot settings first.
2. Choose "Delete snapshots" to wipe the database (you lose history, but a corrupt database is useless anyway).
3. Toggle "Save snapshots" off, reboot, toggle it back on.
4. Give Recall 10-15 minutes to rebuild its index before testing search.
5. If [snapshots still will not save](/articles/recall-snapshots-not-saving/) after a clean database, the problem is deeper — continue.

### Fix 5: Free disk space and check storage health

Recall is storage-hungry and fails silently when starved.

1. Check free space: Settings, System, Storage — Recall wants tens of GB free.
2. Free space: empty Recycle Bin, run Disk Cleanup, move large files off the system drive.
3. In Recall settings, reduce the maximum snapshot storage allocation.
4. Run `chkdsk C: /scan` in admin Command Prompt to rule out filesystem issues corrupting the database.
5. Our [disk space guide](/articles/recall-using-too-much-disk-space/) covers Recall storage tuning in depth.

### Fix 6: Reset Recall via Windows features

When settings-level fixes fail, reset the component.

1. Check for Windows updates — install everything; Recall fixes ship in cumulative updates.
2. If Recall broke after an update, consider [rolling back](/articles/recall-not-working-after-update/) that update.
3. As a last resort: disable Recall fully, reboot twice, re-enable from scratch with fresh settings.
4. Re-run Windows Hello setup after the reset — the security binding sometimes needs refreshing.
5. If Recall still fails on qualifying hardware with a clean database and good drivers, file Feedback Hub feedback and watch for the next cumulative update.

## Closing

Recall failures sort neatly into three buckets: missing requirements, broken NPU driver, or corrupted snapshot database. Check requirements first — no software fix overcomes absent hardware — then work the driver and database angles. Most "not working" cases resolve at Fix 2 or Fix 3. And if you decide Recall is more trouble than it is worth, disabling it cleanly is a valid choice too — it is your PC, after all.
