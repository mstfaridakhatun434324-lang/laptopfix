---
title: "Windows Update Undoing Changes Stuck: Troubleshooting Guide"
slug: windows-update-undoing-changes-stuck-troubleshooting
date: 2026-10-01
categories: ["windows-update"]
tags: ["undoing changes troubleshooting", "update rollback diagnosis", "windows update failure analysis", "cbs log troubleshooting"]
description: "Troubleshoot a stuck Undoing changes rollback like a technician: read the logs, find the failing update, and fix the root cause."
thumbnail: "/images/thumbs/windows-update-undoing-changes-stuck-troubleshooting.webp"
faqs:
  - q: "Where do I find why the update failed?"
    a: "Start with Settings, then Windows Update, then Update history, which shows the failed update and its error code. For depth, check C:\\Windows\\Logs\\CBS\\CBS.log for servicing failures and the Event Viewer under Windows Logs, then System and Setup for the exact failure."
  - q: "What is SetupDiag and when should I use it?"
    a: "SetupDiag is Microsoft's free log analyzer for failed feature updates. After a rollback, run it against the logs in the hidden $Windows.~BT folder and it produces a readable report naming the failure phase and often the responsible driver. Save its report alongside your troubleshooting notes."
  - q: "How do I read the CBS log without getting lost?"
    a: "Open CBS.log and search for the word Failed or your error code near the end of the file, which corresponds to the most recent attempt. The lines around the match name the package that failed and why, which is usually enough to direct the fix."
  - q: "Should I disable automatic updates after a stuck rollback?"
    a: "Pause them, not disable them. Pausing for one to two weeks gives you time to fix drivers, free space, and repair the component store without the failed update retrying. Disabling updates entirely leaves dangerous security holes open. Stay paused, stay protected, and unpause when the fix is verified."
---

This guide is the diagnostic companion to the recovery walkthrough: instead of just escaping the stuck Undoing changes screen, you will find out why the update failed and fix the root cause so the next attempt succeeds. Technicians do not guess at update failures; they read the evidence Windows leaves behind.

Every failed update writes a trail. The update history names the KB and the error code. The CBS log records the servicing engine's blow-by-blow. The Event Viewer timestamps the failure. SetupDiag translates the whole mess into plain language for feature updates. Together they almost always name the culprit.

The troubleshooting sequence below follows that evidence trail from the easy reads to the deep logs, and each finding maps to a specific fix.

Technicians do not guess; they read. Windows writes down almost everything about a failed update, in the history, the event logs, and the servicing logs — but the information is scattered across four locations in three formats. This guide assembles the evidence in the order a professional would read it, so each finding points directly at its fix instead of sending you in circles.

## Why this happens

- **Driver conflict during install.** An incompatible driver fails migration, aborting the update and triggering the rollback.

- **Insufficient disk space.** The install cannot stage its files, fails partway, and the rollback inherits the cramped conditions.

- **Corrupt update payload.** A damaged download fails validation mid-install, forcing the reversal.

- **Third-party antivirus interference.** Security software blocking install operations causes the failure the rollback then has to undo.

- **Component store corruption.** A damaged servicing foundation makes the install fail at the staging phase.

- **Pending servicing transaction.** A wedged previous transaction blocks the new install from completing.

- **Failing hardware.** Bad RAM or disk sectors corrupt the install as it writes, failing unpredictably.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Read the update history for the error code

Every diagnosis starts with the code. The history entry for the failed update names the KB number and the hex code, which tells you which repair family you are in. Screenshot or note the exact KB number and code; you will need them for every subsequent step, from log searches to catalog downloads.

1. Open Settings, then Windows Update, then Update history.
2. Find the failed update, note its KB number and error code.
3. Match the code to its fix: 0x800f codes mean store repair, 0x8024 codes mean network or download issues, 0xC1900101 means driver trouble.

### Fix 2: Fix 2: Check the Event Viewer timeline

The System and Setup logs timestamp exactly when the install failed and what the system was doing. Look for the red error entries clustered around the failure time. Custom views in Event Viewer can filter the System log to the update window; create one spanning the hour of the failure to cut through the noise.

1. Press Win + X and open Event Viewer.
2. Open Windows Logs, then System, and filter for Error around the update attempt time.
3. Also check Windows Logs, then Setup for setup-phase failures. Note any driver or service names mentioned.

### Fix 3: Fix 3: Inspect the CBS log

The CBS log is the servicing engine's diary. Searching for the failure near the end of the log reveals which package or manifest broke the install. The CBS log rolls over to CbsPersist cab files; if CBS.log itself starts after your failure, the evidence is in the most recent persist archive.

1. Open C:\Windows\Logs\CBS\CBS.log in Notepad.
2. Search for Failed or your error code, starting from the bottom of the file.
3. Read the surrounding lines for the package name; language packs, drivers, and .NET packages each point at different fixes.

### Fix 4: Fix 4: Run SetupDiag for feature update failures

For the big feature updates, Microsoft's SetupDiag automates the log analysis and often names the exact driver or phase. It is the closest thing to asking the installer what went wrong. SetupDiag needs to run on the machine that failed, since it reads local logs; copy the tool over rather than trying to analyze exported logs elsewhere.

1. Download SetupDiag from Microsoft and run it after a failed upgrade attempt.
2. Open its output log and read the identified failure.
3. Update or remove the named driver before retrying.

### Fix 5: Fix 5: Verify disk space and drive health

Space and storage health are the two physical prerequisites. Confirm both before blaming software. Free space matters twice: once for the install and once for the rollback, so budget headroom for both when sizing the requirement.

1. Ensure at least 20 GB free on C: for cumulative updates, more for feature updates.
2. Run `chkdsk C: /f` from an admin Terminal and schedule the scan.
3. Check SMART health; replace a failing drive before retrying large updates.

### Fix 6: Fix 6: Repair the component store

If the logs point at servicing or manifest failures, repair the foundation before anything else. A corrupt store fails installs deterministically. If DISM repairs the store, re-examine the CBS log afterward; the repaired entries confirm your diagnosis and teach you the failure's signature for next time.

1. In an admin Terminal, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Follow with `sfc /scannow`, restart, and only then retry the update.

### Fix 7: Fix 7: Clean-boot and retry with monitoring

The final diagnostic is a controlled retry: minimal drivers, no third-party interference, watching the logs live. If it succeeds clean-booted, re-enable startup items in halves to find the interferer. During the controlled retry, keep a log of what you re-enable and when; the binary search only works if you track which half contained the culprit.

1. Clean-boot via `msconfig`, hiding Microsoft services and disabling the rest plus all startup items.
2. Run the update and watch for success.
3. Re-enable in halves to identify the culprit. For the recovery-first version of this scenario, see our [best way to fix undoing-changes stuck](/articles/best-way-to-fix-windows-update-undoing-changes-stuck/), and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the log locations.

## Closing

Troubleshooting a stuck rollback is detective work, and Windows leaves generous evidence: the history gives you the code, the Event Viewer gives you the timeline, the CBS log gives you the package, and SetupDiag gives you the verdict. Follow the evidence to the root cause — driver, space, corruption, or interference — fix it once, and the update succeeds. For escaping the stuck screen itself, our [recovery walkthrough](/articles/best-way-to-fix-windows-update-undoing-changes-stuck/) covers that side, and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official tools. Once the stuck screen finally releases you, the sibling symptom — Windows booting back to 'We couldn't complete the updates' — gets its own diagnostic in our ['We couldn't complete the updates' guide](/articles/we-couldn-t-complete-the-updates-undoing-changes-troubleshooting/); that's where you go to make the next attempt stick.
