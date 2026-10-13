---
title: "'We Couldn't Complete the Updates, Undoing Changes': Full Repair Guide"
slug: how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-after-windows-11-upd
date: 2026-10-09
categories: ["windows-update"]
tags: ["we couldn't complete the updates", "undoing changes", "windows 11 update failed", "update error", "windows update"]
description: "Seeing 'We couldn\\'t complete the updates, undoing changes' after a Windows 11 update? Full repair guide with error-code fixes."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-after-windows-11-upd.webp"
faqs:
  - q: "What is the difference between this message and 'Undoing changes made to your computer'?"
    a: "They describe the same event from two moments: 'We could not complete the updates' appears when the install fails, and 'Undoing changes' appears during the rollback that follows. Same cause, same fixes. Guides use the phrases interchangeably because Windows shows them back-to-back in every failed update."
  - q: "Where do I find the error code for the failed update?"
    a: "Settings → Windows Update → Update history → click the failed update to expand it — the code (like 0x800F0922 or 0xC1900101) appears there. That code is the single most useful diagnostic you have: it tells you whether the failure was driver migration, disk space, servicing corruption, or download corruption, and each family has a different fix."
  - q: "How many times should I retry a failed update before troubleshooting?"
    a: "Once. A single retry rules out transient glitches. If the second attempt fails identically, stop retrying — repeated identical failures never self-heal and each attempt costs you another rollback wait. Switch to diagnosis: read the error code, fix its cause, then retry exactly once more."
  - q: "Can I skip a problematic update and stay secure?"
    a: "Temporarily, yes: you can pause updates for a few weeks while you fix the underlying cause, and Defender still gets its own updates separately. But do not skip permanently — cumulative updates are how security patches arrive. The goal is always to fix the blocker and install, not to avoid updates forever."
---

The update reached some percentage, stalled, and then came the dreaded sentence: **"We could not complete the updates, undoing changes."** Your laptop then spends an age rolling back, boots to the desktop, and the whole thing is queued to fail again next time. It is frustrating precisely because Windows tells you what happened but not why.

The "why" is in the error code, and this guide is built around reading it. You will find the code, match it to its failure family — drivers, space, servicing corruption, or bad download — and apply the fix for that family. Generic retrying is replaced with targeted repair.

Do not retry the update again until you have worked the matching fix below; each blind retry just schedules another rollback. For the 24H2-specific variant of this failure, the [24H2 undoing-changes guide](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-in-windows-11-24h2/) covers that release quirks.

## Why this happens

- **Driver migration failure (0xC1900101 family):** A driver that cannot migrate to the new build aborts the install.
- **Servicing stack corruption (0x800F0922/0x80073712):** Damaged component store failing integrity checks mid-install.
- **Insufficient disk space (0x80070070):** Not enough room for the install plus rollback data.
- **Corrupted download (0x80070002/0x80070003):** Damaged update files failing hash checks.
- **Third-party software interference:** Antivirus, encryption, or disk tools blocking install operations.
- **Incompatible hardware/firmware checks:** Failed compatibility gates for BIOS, TPM, or secure boot state.
- **Stuck update services:** Windows Update or BITS services in a bad state, failing every attempt identically.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the error code and classify the failure

Open Settings → Windows Update → Update history, expand the failed update, and write down the full code. Then classify: 0xC1900101-xx = driver migration (update drivers); 0x800F0922/0x80073712 = servicing corruption (DISM/SFC); 0x80070070 = disk space; 0x80070002/03 = bad download (clear cache); anything else = note it and search the exact string. This two-minute step chooses your fix family — skip it and you are guessing.

1. Open Update history and expand the failed update.
2. Write down the complete error code.
3. Classify into driver / servicing / space / download.
4. Jump to the matching fix below.

### Fix 2: Driver family: update the migration blockers

For 0xC1900101 codes, update chipset, storage (AHCI/NVMe/Intel RST), display, network, and biometric drivers from your laptop maker support page — generic Windows drivers for these are the classic migration failures. If the code names a driver, uninstall it temporarily, install the update, then reinstall fresh. Disconnect non-essential USB devices during the retry; external hardware with bad drivers also triggers this family.

1. Update chipset, storage, display, network, biometric drivers from the maker.
2. Uninstall any driver named in the error; reinstall after.
3. Disconnect external USB devices for the retry.
4. Retry the update exactly once.

### Fix 3: Servicing family: repair the component store

For 0x800F0922/0x80073712, the component store is damaged: elevated `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart. If DISM fails, point it at a known-good source with `/Source` or run it from Windows Recovery. Only retry the update after both tools report clean — retrying on a still-corrupt store just schedules another rollback. Microsoft documents these repairs in [Windows support](https://support.microsoft.com/en-us/windows).

1. Run elevated DISM restore-health until it completes.
2. Follow with `sfc /scannow`.
3. Restart; confirm both reported no unfixable errors.
4. Retry the update once.

### Fix 4: Space and download families: free space, clear cache

For 0x80070070: free 20 GB+ with Disk Cleanup as administrator (include system files — old Windows installations are the big win). For 0x80070002/03: stop the Windows Update and BITS services, delete `C:\Windows\SoftwareDistribution\Download` contents, restart the services, and check for updates to force a clean re-download. These two are the quickest fixes in the guide when the code matches.

1. Free 20 GB+ via elevated Disk Cleanup.
2. Stop Windows Update + BITS; clear the Download cache.
3. Restart services; check for updates.
4. Retry once with space and clean downloads.

### Fix 5: Eliminate third-party interference

Regardless of code family, if the targeted fix did not work, remove the usual interferers: temporarily disable or uninstall third-party antivirus, pause disk encryption, and disable VPN clients. Then retry. Interference failures often masquerade as other codes because the block happens at file-operation level. If the update succeeds with protection off, update the security product before re-enabling — an outdated AV will block the next update too.

1. Disable/uninstall third-party antivirus temporarily.
2. Pause disk encryption and disable VPN clients.
3. Retry the update in this clean state.
4. Success: update the security product, then re-enable.

### Fix 6: Install manually from the Update Catalog

With the KB number from update history, download the package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install the .msu directly. Manual installation bypasses the automatic delivery pipeline — a frequent failure point — and produces clearer errors. If the manual install fails with the same code, your system state is definitively the problem; if it succeeds, the automatic pipeline was at fault and future updates may behave.

1. Get the KB number from the failed entry.
2. Download the .msu from the Update Catalog.
3. Install manually; record the exact result.
4. Same code: system-state repair next; success: pipeline was faulty.

### Fix 7: In-place upgrade repair for chronic failures

When the same update fails after every targeted fix, rebuild the OS around your data: run the Windows 11 installer from [Microsoft software download](https://www.microsoft.com/en-us/software-download/windows11), Upgrade → keep files and apps. This reinstalls the update engine, servicing stack, and driver base cleanly. Chronic "could not complete" loops essentially never survive this — it is the definitive answer when diagnosis is exhausted.

1. Back up personal files.
2. Run the installer → Upgrade → keep files and apps (plugged in).
3. After completion, install the previously failing update.
4. Verify it completes without rollback.

## Closing

We could not complete the updates" is a failure with a code, and the code is the map: classify it, fix its family — drivers, servicing, space, or download — clear interference, install manually, and repair in place when nothing else works. One retry to confirm a fluke, then diagnosis; the rollback loop ends when the cause does. For the rollback phase specifically, the [undoing changes stuck guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update/) covers what to do while the screen is still up.
