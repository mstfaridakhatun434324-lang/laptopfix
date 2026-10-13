---
title: "Fix Windows Update With the Troubleshooter: The Best Way"
slug: best-way-to-fix-windows-update-with-troubleshooter
date: 2026-09-17
categories: ["windows-update"]
tags: ["troubleshooter", "windows update", "automatic fix", "windows 11", "diagnostics"]
description: "The built-in Windows Update troubleshooter fixes more than you'd expect — if you run it right. Here's the best way to use it for real results."
thumbnail: "/images/thumbs/best-way-to-fix-windows-update-with-troubleshooter.webp"
faqs:
  - q: "What does the Windows Update troubleshooter actually fix?"
    a: "It checks the update services' configuration, resets stuck services, clears corrupted cache metadata, repairs the BITS queue, and verifies the cryptographic services updates depend on. It handles the common misconfigurations automatically. What it cannot do is repair deep system file corruption or hardware problems — those need the manual steps in the second half of this guide."
  - q: "Where is the Windows Update troubleshooter in Windows 11?"
    a: "Go to Settings, System, Troubleshoot, Other troubleshooters, then click Run next to Windows Update. Microsoft has also moved some troubleshooters into the Get Help app, so if you do not see it in Settings, open Get Help and search for the Windows Update troubleshooter there."
  - q: "How long does the troubleshooter take to run?"
    a: "Usually five to fifteen minutes. It runs a series of checks sequentially, and some involve waiting on service restarts. Let it finish completely — closing it early can leave services in a half-reset state that is worse than where you started."
  - q: "What should I do if the troubleshooter finds nothing?"
    a: "A clean troubleshooter result means the problem is outside its checklist: corrupted system files, a damaged component store, or a network issue. Move on to the manual repairs below — cache clearing, DISM/SFC, and manual installation. The troubleshooter ruling things out is still useful information."
---

The Windows Update troubleshooter has a reputation problem: people run it, it says it fixed something vague, and the update still fails. But used properly — as the first step in a sequence rather than a magic button — it genuinely resolves a large share of update problems. It resets services, clears bad cache metadata, and repairs the BITS queue, all in a few clicks.

The trick is knowing what it can and cannot do, running it correctly, and having the manual follow-ups ready for when it falls short. This guide covers the full arc: the best way to run it, how to interpret its results, and what to do next in every outcome.


Think of the troubleshooter as triage, not surgery: it quickly handles the common, shallow problems so you can focus your effort on whatever remains. Running it first also gives you a documented baseline — if a later manual fix is needed, you know the service layer is already verified. That division of labor is what makes the sequence in this guide effective.
## Why this happens

- **Services in bad states:** The troubleshooter's primary target — stuck or misconfigured update services.
- **Corrupted cache metadata:** The troubleshooter clears the download database Windows Update consults.
- **BITS queue corruption:** Stalled transfer jobs the troubleshooter can purge.
- **Cryptographic service issues:** Signature verification failures it can reset.
- **Problems beyond its scope:** Deep file corruption it detects but cannot repair.
- **Troubleshooter itself broken:** Missing or crashing troubleshooter needing re-registration.
- **Underlying hardware faults:** Disk errors no software troubleshooter can fix.
- **Outdated troubleshooter definitions:** The troubleshooter's own checklists needing refresh via Get Help.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the troubleshooter correctly

1. Close all applications to give the troubleshooter a quiet system.
2. Go to **Settings > System > Troubleshoot > Other troubleshooters** and click **Run** next to **Windows Update**.
3. Let it complete fully — do not click away or close the window early.
4. Apply every fix it offers, even ones that look unrelated, then restart when it finishes.
5. Disconnect from VPN during the run — network checks behave better on a direct connection.
6. Note the exact time you ran it; the event log entries help if you escalate later.

### Fix 2: Interpret the results properly

1. If it reports fixed issues, retry Windows Update immediately after the restart.
2. If it reports it could not identify the problem, note that — it rules out service misconfiguration.
3. Check **Settings > Windows Update > Update history** for whether the error code changed.
4. A changed error code after the troubleshooter means progress; treat the new code as your next lead.
5. Expand the troubleshooter's detailed view to see every check it performed.
6. If it fixed services, verify they show as Running in services.msc afterward.

### Fix 3: Run it from Get Help as an alternative

1. If the Settings version is missing, open the **Get Help** app from the Start menu.
2. Search for "Windows Update troubleshooter" and run the guided version there.
3. This version sometimes includes newer checks than the Settings one.
4. Microsoft is migrating troubleshooters here, so bookmark this path. If neither version runs, see our guide on [troubleshooter failures](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/).
5. The Get Help version may download updated diagnostic packs — allow it network access.
6. If Get Help lacks the troubleshooter, your Windows build may need updating first.

### Fix 4: Follow up with a manual cache clear

1. The troubleshooter clears metadata but sometimes leaves the payload cache; do it manually.
2. In an elevated Command Prompt: `net stop wuauserv`, `net stop bits`, empty `C:\Windows\SoftwareDistribution\Download`, restart both services.
3. Retry the update.
4. This one-two punch — automated metadata repair plus manual payload clear — resolves most stubborn cases.
5. After the manual clear, confirm the update client rebuilds its database on the next check.
6. Run the troubleshooter once more after the manual clear — the combination often succeeds.

### Fix 5: Repair what the troubleshooter cannot

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated Command Prompt.
2. Follow with `sfc /scannow` and restart.
3. These repair the system file and component store damage outside the troubleshooter's scope.
4. Retry Windows Update. Microsoft documents these repairs on its [Windows support pages](https://support.microsoft.com/en-us/windows).
5. Capture DISM's completion message for your records if this becomes a support case.
6. If SFC reports unfixable corruption, the CBS log names the files for targeted repair.

### Fix 6: Install the update manually

1. Find the failing KB number in Update history.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and install the .msu directly.
3. This bypasses the automated pipeline the troubleshooter was trying to heal.
4. If the manual install succeeds, the troubleshooter did its job on the services — only the delivery was broken.
5. Match the Catalog package to your build exactly — architecture and build both matter.
6. After manual success, let the next scheduled update run automatically to confirm recovery.

### Fix 7: Reset components when all else fails

1. Stop `wuauserv`, `bits`, `cryptsvc`, and `msiserver` in an elevated Command Prompt.
2. Rename `SoftwareDistribution` and `catroot2` with `.old` suffixes, then restart the services.
3. Run the troubleshooter once more on the clean slate — it often succeeds now.
4. Check for updates. For recurring monthly failures, our guide on [cumulative update failures](/articles/how-to-fix-monthly-cumulative-update-failed-reddit/) addresses the pattern.
5. Restart each service and verify its status shows Running before proceeding.
6. After the reset, avoid interrupting the first update check — it takes longer than normal.

## Closing

The troubleshooter is the right first move, not the only move: run it properly, read its results, then layer the manual cache clear, the DISM/SFC repair, and the manual install behind it. Used as the opening of a sequence rather than a lone hope, it earns its place in every technician's toolkit. Keep it in mind next Patch Tuesday before reaching for anything drastic. The troubleshooter-plus-manual-followup pattern works beyond Windows Update too — it is a general troubleshooting philosophy. Automate the shallow checks, hand-repair the deep ones, and verify everything at the end.
