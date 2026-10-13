---
title: "Troubleshoot Update Assistant Stuck at 99 Percent: Recovery Guide"
slug: troubleshoot-update-assistant-stuck-at-99-percent
date: 2026-09-02
categories: ["windows-update"]
tags: ["99 percent", "update assistant", "recovery", "windows 11"]
description: "Update Assistant frozen at 99%? A technician's recovery checklist: confirm the stall, protect your data, clear the blockage, and finish the upgrade."
thumbnail: "/images/thumbs/troubleshoot-update-assistant-stuck-at-99-percent.webp"
faqs:
  - q: "What exactly is happening at 99 percent?"
    a: "At 99 percent the assistant is in the finalization stage: copying the last system files, migrating drivers, registering components, and verifying package integrity. It's the most write-intensive phase of the upgrade, which is why a corrupted download, a locked file, or a disk error surfaces here rather than earlier. The work is nearly done — the blockage is in the last stretch, not the whole upgrade."
  - q: "How do I safely recover without losing data?"
    a: "Don't force a shutdown first. End the assistant process in Task Manager, restart the update services, and clear the download cache — none of these touch your files. Your data is only at risk if you cut power during the post-reboot installation phases. At 99 percent in the assistant window, you're still in the pre-reboot phase, which is the safest possible place to intervene."
  - q: "Why does it always stop at exactly 99 and not 98 or 100?"
    a: "The percentage is a coarse estimate mapped to installer phases, and 99 percent corresponds to the final verification gate. The installer won't report 100 percent until every package verifies cleanly, so any single failing file parks the progress at 99. It's not a coincidence or a bug in the progress bar — it's the installer honestly refusing to declare success with an unverified package."
  - q: "After recovering, how do I prevent this next time?"
    a: "Before your next feature update: free 30 GB on C:, update your chipset and storage drivers, temporarily uninstall third-party antivirus, disconnect USB peripherals, and run the update with the laptop plugged in and sleep disabled. Most 99-percent stalls are preventable with this pre-flight checklist, which takes ten minutes and saves hours."
---

Ninety-nine percent. One percent from done, and the progress bar hasn't moved in hours. Before you do anything drastic, understand this: at 99 percent you're in the safest possible place for an intervention. The download is complete, the heavy installation hasn't started its reboot phases, and your files are untouched. This guide is a recovery checklist — confirm, protect, clear, and finish — designed for exactly this moment.

If you haven't yet confirmed the stall is real (versus just slow), start with the two-hour rule below. And if your update services themselves seem broken rather than merely stalled, check our [update service repair guide](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/) alongside this checklist.

## Why this happens

- **Final verification failure** — One corrupted file in the payload fails the integrity gate, and the installer waits instead of proceeding.
- **Locked system files** — Antivirus filters or utilities holding exclusive locks on files the finalizer needs to replace.
- **Disk space pinch** — The last phase needs scratch space; a nearly full drive stalls the final copy silently.
- **Driver migration snag** — A single driver that won't migrate parks the whole finalization phase.
- **Hung update services** — wuauserv or BITS exhausted after hours of work, freezing the pipeline at the finish line.
- **Metered connection pause** — Windows quietly pausing background transfers mid-finalization.
- **Storage errors** — Bad sectors encountered during the write-heavy final phase.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall with the two-hour rule

Never intervene on a hunch at 99 percent — the final phase is legitimately slow on older hardware.

1. Record the exact time and percentage, then leave the laptop plugged in with the lid open.
2. Set sleep to **Never** temporarily (Settings > System > Power & battery) so the laptop can't doze during finalization.
3. Open Task Manager and watch Disk activity: periodic writes mean the finalizer is working.
4. Wait two full hours. Any percentage movement or disk activity means it's alive — be patient.
5. Only proceed when there's been zero movement and zero disk activity for the entire two hours.

### Fix 2: End the assistant safely and restart services

The safe intervention: stop the stuck process without touching the reboot phases.

1. In Task Manager, end **Windows Update Assistant** (Windows10UpgraderApp.exe) and any **SetupHost** processes.
2. Open `services.msc` and restart **Windows Update**, **Background Intelligent Transfer Service**, and **Cryptographic Services**.
3. Confirm your files are intact — browse a few folders; nothing should have changed.
4. Check that C: still has ample free space; note the number for Fix 4.
5. Do NOT force a shutdown or hold the power button — at this stage a graceful process-end is all that's needed.

### Fix 3: Clear the corrupted payload

A bad download is the top cause of 99-percent stalls; purge it and fetch a clean copy.

1. Open an elevated Command Prompt and run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
2. Delete the contents of `C:\Windows\SoftwareDistribution\Download`.
3. Rename `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the services with matching `net start` commands and reboot.
5. Re-run the assistant — the download restarts fresh, and finalization usually completes on the clean payload.

### Fix 4: Free space and remove locks

Tight disks and locked files are the next most common blockers at the finish line.

1. Free at least 25–30 GB on C: via Disk Cleanup (as administrator) with **Windows Update Cleanup** selected.
2. Temporarily uninstall third-party antivirus — its file filter is the classic finalization blocker.
3. Disconnect USB devices, docks, and external drives that complicate the driver migration step.
4. Check whether your connection is marked metered (Settings > Network & Internet) — a [metered connection silently throttling the transfer](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/) can freeze the assistant at the very end.
5. Retry the assistant in this clean state.

### Fix 5: Install the pending update manually

If the assistant's payload keeps failing verification, bypass the assistant with a manual install.

1. Check Settings > Windows Update > Update history for the exact KB number involved.
2. Download that KB from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) as an x64 `.msu`.
3. Run the installer directly and reboot when prompted.
4. The manual path skips the assistant's staging and verification pipeline entirely.
5. Verify the install in the update history — a clean manual install confirms the assistant's payload was the problem.

### Fix 6: Repair system files before the next attempt

When the blockage is in the OS rather than the payload, repair the foundation.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated prompt (keep the laptop online).
2. Follow with `sfc /scannow` and reboot.
3. Retry the assistant or the manual install from Fix 5.
4. If DISM reports unfixable corruption, the component store needs deeper repair — but try the retry first.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents these repair tools if you want the official reference.

### Fix 7: Finish with the Media Creation Tool

The guaranteed finisher: a different engine for the same upgrade.

1. Download the Media Creation Tool from Microsoft's official Windows 11 download page.
2. Choose **Upgrade this PC now**, keeping files and apps.
3. Its independent download and verification engine sidesteps whatever corrupted the assistant's payload.
4. Let it run to completion with the laptop plugged in and awake.
5. Afterward, run Windows Update once more to confirm everything is current — then run through the prevention checklist in the FAQ so the next feature update doesn't repeat this drama.

## Closing

A 99-percent stall is the update equivalent of tripping at the finish line — infuriating, but recoverable, and you're intervening at the safest possible point. Confirm the stall, end the process gracefully, clear the bad payload, and finish with a clean run or the Media Creation Tool. And next time, spend ten minutes on the pre-flight checklist: free space, updated drivers, no conflicting software. Future you will be grateful.
