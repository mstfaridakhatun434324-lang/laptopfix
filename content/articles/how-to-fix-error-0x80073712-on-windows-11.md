---
title: "How to Fix Error 0x80073712 on Windows 11 (Component Store Corrupt)"
slug: how-to-fix-error-0x80073712-on-windows-11
date: 2026-09-19
categories: ["windows-errors"]
tags: ["0x80073712", "windows update error", "component store", "windows 11"]
description: "Error 0x80073712 blocking Windows 11 updates? Repair the corrupted component store with DISM, manual installs, and in-place upgrade."
thumbnail: "/images/thumbs/how-to-fix-error-0x80073712-on-windows-11.webp"
faqs:
  - q: "What does error 0x80073712 mean on Windows 11?"
    a: "The component store (WinSxS) — the master library every Windows 11 update draws from — is corrupted. Updates fail with 'some update files are missing or have problems' because the store they reference is damaged. DISM's RestoreHealth is the primary repair: it rebuilds the store from known-good sources, after which updates install normally."
  - q: "Why do Windows 11 feature updates trigger this more than cumulative updates?"
    a: "Feature updates (like 24H2) touch far more components than monthly cumulative updates, so they stress the component store harder and are more likely to expose existing corruption. If cumulative updates install fine but the feature update fails with 0x80073712, the store has latent damage — repair it with DISM before retrying."
  - q: "How long does DISM RestoreHealth take?"
    a: "Typically 15 to 30 minutes on an SSD, longer on a hard drive or slow connection since it may download clean components from Windows Update. Let it finish uninterrupted — stopping it midway can leave the store in a worse state. Run it from Terminal (Admin) and do something else while it works."
  - q: "Can I prevent component store corruption?"
    a: "Mostly yes: never force-shutdown during updates, don't let 'cleaner' tools touch the WinSxS folder, keep your drive healthy with periodic chkdsk scans, and maintain adequate free space. The store corrupts when writes to it are interrupted or when the underlying disk is failing."
---
Error 0x80073712 on Windows 11 means the component store is damaged — the WinSxS library that every update depends on has corrupted entries, so updates fail with "some update files are missing or have problems." No amount of retrying the update helps, because the problem isn't the download; it's the library the installer reads from. The repair targets the store directly with DISM.

Windows 11's version of this fix is nearly identical to Windows 10's (see the [Windows 10 guide](/articles/how-to-fix-error-0x80073712-on-windows-10/) for that), with updated navigation and Terminal commands. Nothing here touches your personal files — DISM only repairs Windows' own components. Most people are done by Fix 2; the later steps cover the stubborn cases where DISM needs a local source or the disk itself is contributing.

## Why this happens

- **Interrupted updates.** Power loss or forced shutdown during an update leaves the store half-written.
- **Disk errors.** Bad sectors in the WinSxS area corrupt stored components.
- **Cleaner tools deleting WinSxS files.** Some utilities remove "unnecessary" store files, breaking it.
- **Failed feature updates.** A 24H2-style upgrade that rolled back can leave the store inconsistent.
- **Aging Windows installations.** Systems upgraded across multiple feature updates accumulate store wear; the in-place upgrade in Fix 7 is the periodic deep clean for this.
- **Malware damage.** Some malware damages update components to block security patches.
- **Long update history.** Years of cumulative updates increase the odds of gradual store corruption.
- **Interrupted 24H2-style feature updates.** Large feature updates stress the store hardest; a failed one is the most common origin of this error on Windows 11.

## How to fix it

Work through these in order.

### Fix 1: Run the Windows Update troubleshooter

Clear simple service issues first.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply its fixes.
3. Restart and retry the update.
4. If 0x80073712 returns, the store itself needs repair — continue.

### Fix 2: Repair the component store with DISM

The core fix.

1. Open **Terminal (Admin)** from **Win + X**.
2. Run `DISM /Online /Cleanup-Image /ScanHealth` to confirm the corruption.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` — allow 15–30 minutes uninterrupted.
4. On success, run `sfc /scannow` to fix files damaged while the store was broken, then restart and retry the update.
5. If RestoreHealth stalls at the same percentage repeatedly, your connection may be dropping the component download — try a stable network, or skip to Fix 3's local ISO source, which doesn't need the network at all.

### Fix 3: Point DISM at a local repair source

When RestoreHealth can't fetch clean files from Windows Update.

1. Download the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) matching your installed build.
2. Double-click the ISO to mount it and note its drive letter (e.g., E:).
3. Run: `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:E:\sources\install.wim:1 /LimitAccess`
4. For ESD-based ISOs, use `/Source:ESD:E:\sources\install.esd:1` instead.
5. Follow with `sfc /scannow`, restart, and retry the update.

### Fix 4: Reset the update cache

Give the repaired store a clean pipeline.

1. In **Terminal (Admin)**:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
2. Then:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
3. Restart the four services with `net start`, reboot, and check for updates.
4. Don't rename the folders while any service is still stopping — wait for each `net stop` to confirm success first.
5. After the reboot, the first update check takes longer than usual because Windows rebuilds its entire update metadata from scratch.

### Fix 5: Install the update manually

Bypass the automatic downloader.

1. Find the failing KB number in **Settings > Windows Update > Update history**.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) (x64 for most laptops).
3. Run the `.msu` manually and restart.
4. For feature updates specifically, the Installation Assistant from Microsoft's download page uses a separate engine that sometimes succeeds where Windows Update fails.
5. When downloading from the Update Catalog, match the build number to your installed Windows (check with `winver`) — grabbing the wrong build's package wastes time and fails confusingly.

### Fix 6: Check drive health

Recurring store corruption signals disk trouble.

1. Run `chkdsk C: /f /r` from **Terminal (Admin)** and restart for the full scan.
2. Check SMART data with your SSD maker's health tool.
3. Keep at least 20GB free on C: — cramped drives cause update staging failures.
4. Replace a failing drive before it corrupts the freshly repaired store again.
5. Also confirm at least 20GB free on C: — DISM stages repaired components on the system drive, and low space makes RestoreHealth fail with misleading errors.

### Fix 7: In-place upgrade repair

Rebuild the entire store when DISM can't.

1. Mount the Windows 11 ISO and run setup, choosing **Keep personal files and apps**.
2. The in-place upgrade reinstalls Windows over itself with a pristine component store.
3. After completion, run Windows Update — it should proceed cleanly.
4. Related code: [0x80070057 on Windows 11](/articles/error-code-0x80070057-fix/) covers the sibling parameter error.
5. After the in-place upgrade, run Windows Update immediately and let it install everything before reinstalling third-party software — a clean update stack is the whole point, so verify it works first.

## Closing

Error 0x80073712 is one of the most satisfying to fix because the repair path is so direct: DISM rebuilds the store, SFC fixes the files, updates flow again. The step that saves the most frustration is Fix 3 — when DISM stalls reaching Windows Update, a mounted ISO as a local source turns failure into success.

Afterwards, treat WinSxS as untouchable: no cleaner tool, no manual deletions, no forced shutdowns during updates. Consider running `DISM /Online /Cleanup-Image /ScanHealth` every few months as a preventive check — it takes minutes and catches store corruption before it starts blocking updates. A healthy component store is invisible; a little maintenance keeps it that way.
