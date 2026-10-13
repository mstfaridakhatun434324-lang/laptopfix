---
title: "KB5058411 Not Installing on Windows 11 24H2? Diagnose and Fix It"
slug: how-to-fix-kb5058411-not-installing-in-windows-11-24h2
date: 2026-09-12
categories: ["windows-update"]
tags: ["kb5058411", "cumulative update", "install failed", "windows 11 24h2", "servicing"]
description: "Fix KB5058411 failing on Windows 11 24H2: trace the servicing chain, repair broken links, and get the cumulative update installed."
thumbnail: "/images/thumbs/how-to-fix-kb5058411-not-installing-in-windows-11-24h2.webp"
faqs:
  - q: "KB5058411 fails but last month's update installed fine. Why?"
    a: "Each cumulative update makes new assumptions about the component store. Last month's success does not guarantee this month's, because the new package touches different files and expects different prerequisites. A servicing-stack update or a driver change since last month is the usual new variable."
  - q: "What does error 0x800f0988 mean?"
    a: "Error 0x800f0988 indicates the servicing stack could not process the update package, often because of a corrupted manifest or a component-store inconsistency introduced by an earlier incomplete operation. DISM repair followed by a cache reset is the standard fix."
  - q: "Do I need to uninstall the previous cumulative update first?"
    a: "No — cumulative updates are designed to install on top of each other, and uninstalling the previous one is unnecessary and sometimes harmful. Only uninstall a prior update if it is itself corrupted and blocking the new one, which the CBS log will indicate."
  - q: "How do I know if a driver is blocking this update?"
    a: "Check Device Manager for warning icons and review the Setup event log around the failure time for driver names. Updates that fail above 90% with a rollback are the classic driver-block signature, while early failures point at the cache or servicing stack."
---

KB5058411 is a mid-year cumulative update, and its failures follow the mid-year pattern: the machine has absorbed six months of patches, driver revisions, and software installs since the last build upgrade, and somewhere in that accumulated state is the thing this particular update trips over. The update is fine — the machine's servicing history is the suspect. Your job is to find which link in the chain broke and repair it.

This guide works the servicing chain methodically: verify prerequisites, inspect the failure signature, repair the store, clear the pipeline, and install through the channel that works.

Mid-year machines carry something January machines do not: six months of small compromises. A driver installed from a forum link in March. A servicing hiccup in April that "fixed itself." A disk that has been 95 percent full since May. None of these broke anything at the time, but each one narrowed the margin — and KB5058411 is the update that finally needs the margin. This guide restores it.

## Why this happens

- **Servicing-chain inconsistency:** Six months of patches leave small inconsistencies that compound until one update cannot reconcile them.
- **Missing prerequisite SSU:** The update expects a servicing stack version that failed to install in a prior month.
- **Corrupted manifests:** Damaged update manifests (0x800f0988) mislead the installer about package contents.
- **Driver blocking late install:** A driver updated since last month now holds a lock the installer needs.
- **Pending transaction residue:** An incompletely committed prior update blocks the new transaction.
- **Cache corruption:** Damaged payload chunks failing verification at install time.
- **Antivirus definition conflicts:** Security software updated aggressively can newly conflict with servicing operations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the failure signature carefully

1. Record the error code from **Update history** and the progress percentage at failure.
2. Open **Event Viewer > Windows Logs > Setup** and read the events in the failure minute.
3. Compare against last month: what changed since the successful update — new drivers, new software, a missed SSU?
4. The signature plus the "what changed" list focuses every step below.

### Fix 2: Verify and install the prerequisite servicing stack

1. Check Update history for the most recent Servicing Stack Update and its status.
2. Download any missing SSU from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and install it standalone.
3. SSUs are prerequisites, not optionals — the cumulative update's installer assumes the SSU's fixes are present.
4. Retry KB5058411 only after the SSU shows successfully installed.

### Fix 3: Repair the component store deeply

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated prompt and let it fully complete.
2. If it reports unfixable corruption, rerun with a mounted ISO as `/Source`.
3. Follow with `sfc /scannow` and a restart.
4. The 0x800f0988 manifest errors live here; a deep repair is the direct treatment. When DISM needs an ISO source to complete, that tells you the local store was damaged beyond self-repair — take it as a warning to run these health checks more than once a year.

### Fix 4: Reset the pipeline and pull fresh

1. Stop wuauserv, bits, cryptSvc, msiserver; rename SoftwareDistribution and Catroot2; restart the services.
2. Check for updates to download a pristine KB5058411.
3. This eliminates both corrupted payloads and jammed pending transactions in one move.
4. If the [update troubleshooter is broken](/articles/best-way-to-fix-windows-update-troubleshooter-not-working/), this manual reset does its job better anyway.

### Fix 5: Hunt the driver blocker

1. In **Device Manager**, scrutinize every device — update anything with a warning from the vendor first.
2. For late-failure rollbacks, suspect storage and display drivers; update them from the maker ([Intel](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA, AMD).
3. Temporarily disable third-party antivirus during the install attempt.
4. If [driver updates fail independently](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/), resolve that in parallel — the two problems share causes. Pay special attention to drivers updated in the last 60 days; the "what changed since last month" question from Fix 1 usually answers itself right here.

### Fix 6: Check space and disk health

1. Ensure 15–20 GB free on C:; mid-year machines accumulate surprising cruft.
2. Run `chkdsk C: /f` scheduled at reboot to catch file-system damage.
3. Review SMART status for early drive-failure signs.
4. Servicing operations are disk-intensive; marginal disks fail updates before they fail anything else. If chkdsk finds bad sectors, replace the drive before trusting the machine with important work — update failures are often the first symptom of a dying disk, not the last.

### Fix 7: Manual install from the Catalog

1. Download the KB5058411 x64 package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Install standalone with the machine idle on AC power.
3. The manual path bypasses the pipeline where most repeat failures live.
4. Verify in Update history and re-run **Check for updates** to sync state.

### Fix 8: Audit the servicing chain for next month

1. After success, review the full Update history for any other failed entries and resolve them — each is a future chain-break waiting to happen.
2. Note what fixed this one (SSU? driver? cache?) in a text file; next month's failure will rhyme.
3. Consider the [in-place upgrade path](/articles/best-way-to-fix-windows-update-says-undoing-changes-made-to-your-computer/) if servicing repairs are becoming a monthly ritual — a rebuilt stack beats monthly triage.
4. Monthly maintenance — install promptly, restart when asked, keep space free — is what keeps the chain unbroken.

## Closing

KB5058411 fails on accumulated servicing history, and the fix is accumulated diligence: prerequisites first, store repair second, pipeline reset third, driver hunt fourth, manual install as the closer. Each month's update builds on the last — keep the chain clean and the failures stop compounding. The next cumulative update will test whether the lesson stuck: a machine that installs promptly, restarts when asked, and keeps its component store healthy never gives a monthly update a reason to fail.
