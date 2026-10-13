---
title: "Fix Servicing Stack Update Failed on Windows 10 (SSU Install Errors)"
slug: how-to-fix-servicing-stack-update-failed-on-windows-10
date: 2026-09-15
categories: ["windows-update"]
tags: ["servicing stack", "ssu", "windows update", "windows 10", "install failed"]
description: "A servicing stack update (SSU) failing on Windows 10 blocks everything behind it. Here are 7 fixes to get the SSU installed so your updates can flow again."
thumbnail: "/images/thumbs/how-to-fix-servicing-stack-update-failed-on-windows-10.webp"
faqs:
  - q: "What is a servicing stack update and why does it matter?"
    a: "The servicing stack is the Windows component that installs other updates — think of it as the machinery that delivers the packages. A servicing stack update (SSU) upgrades that machinery itself. Microsoft requires the latest SSU before newer cumulative updates will install, so a failed SSU silently blocks every update behind it, even though the real problem is the installer, not the updates."
  - q: "Why does the servicing stack update keep failing?"
    a: "The most common causes are a corrupted component store (the very machinery being updated is damaged), pending operations from a previous interrupted update, third-party antivirus locking the files being replaced, or a missing prerequisite update. SSUs touch deep system files, so anything that locks or damages those files can block them."
  - q: "Can I just skip the servicing stack update?"
    a: "No — skipping it is a dead end. Cumulative updates check for the required SSU version and will refuse to install without it, often with a misleading error. The SSU is small and quick once the underlying issue is fixed, so repairing it is always faster than working around it."
  - q: "How do I know which servicing stack update I need?"
    a: "Check your installed SSU version in Settings > System > About (look at the OS build number), then compare with the latest SSU for your Windows 10 version on the Microsoft Update Catalog. The catalog lists SSUs per build — download the one matching your version and install it manually if Windows Update will not."
---

Few update failures are as quietly destructive as a failed servicing stack update. Your Windows 10 laptop tries to install its monthly updates, one of them fails with a cryptic code, and behind the scenes the real culprit is the servicing stack update — the small, unglamorous package that upgrades Windows' own update machinery. Until that SSU lands, every cumulative update behind it will keep failing, no matter how many times you retry. It feels like Windows Update itself is broken, when really the delivery truck just needs its engine fixed.

The servicing stack is the component that unpacks, verifies, and installs every other update. Microsoft ships SSUs separately because the installer sometimes needs to be newer than the packages it installs. The failure modes are distinctive: the SSU fails with errors like 0x800f081f, 0x80073701, or simply hangs at a percentage, and afterward all other updates fail too. The fixes below repair the machinery in order, starting with the simplest prerequisite checks and ending with a manual SSU install from the catalog.

## Why this happens

- **Corrupted component store.** The servicing stack being updated is itself damaged, so its own replacement cannot apply.
- **Pending operations from an interrupted update.** A previous update that was force-rebooted leaves the stack in a half-finished state.
- **Third-party antivirus file locks.** Security software locking the exact files the SSU needs to replace.
- **Missing prerequisite updates.** Some SSUs require a specific earlier update to already be present.
- **Corrupted update cache.** Damaged metadata in SoftwareDistribution causing the SSU download to be incomplete.
- **Insufficient disk space for staging.** The SSU needs room to stage and back up files before replacing them.
- **System file corruption.** Broader damage that interferes with the deep file operations an SSU performs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check what is actually failing

Do not fight the wrong battle. Confirm the SSU is the blocker before repairing anything.

1. Open **Settings > Update & Security > Windows Update > View update history**.
2. Find the failed update — if the failed entry is a "Servicing Stack Update" (often labeled KB50xxxx with SSU in the details), that is your blocker.
3. Note the exact KB number and error code; you will need the KB number for the manual install in Fix 7.
4. If instead a cumulative update is failing and no SSU appears in history, the SSU may have failed silently — check whether your installed SSU is current (see Fix 7) before assuming otherwise.

### Fix 2: Free disk space and clear temporary staging files

SSUs stage backups of the files they replace. A nearly full drive blocks this silently.

1. Check free space on C: — you want at least **20 GB free** for comfortable update staging.
2. Open **Settings > System > Storage > Temporary files**, select **Windows update cleanup**, **Temporary files**, and **Delivery Optimization Files**, then remove them.
3. Empty the Recycle Bin and restart.
4. Retry the update. Disk-space blocks are common on laptops with small SSDs, and this fix takes five minutes.

### Fix 3: Run the Windows Update troubleshooter and SFC

Clear the easy blockers: cached corruption and damaged system files that interfere with the SSU.

1. Run the troubleshooter at **Settings > Update & Security > Troubleshoot > Additional troubleshooters > Windows Update**.
2. Then open Command Prompt as administrator and run `sfc /scannow` to 100%.
3. Restart the laptop.
4. Check for updates. If the SSU still fails, the component store itself likely needs the deeper DISM repair in Fix 4 — see our guide to [fixing the update troubleshooter when it cannot help](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-windows-10/) for related infrastructure repairs.

### Fix 4: Repair the component store with DISM

The SSU replaces servicing-stack files, and it cannot do that if the component store it reads from is damaged. This is the most important repair in this guide.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` — allow 15–30 minutes; do not interrupt it.
3. If DISM reports it cannot find source files, you need an ISO source: download the Windows 10 ISO from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11) (choose the Windows 10 media tool option), mount it, and rerun DISM with `/Source:` pointing at the mounted `install.wim`.
4. After DISM completes successfully, run `sfc /scannow` once more, restart, and retry the update check.

### Fix 5: Temporarily disable third-party antivirus

Antivirus products sometimes lock the servicing binaries mid-replacement, which is fatal to an SSU install.

1. Open your third-party antivirus and disable **real-time protection** (temporarily — re-enable it afterward).
2. If the antivirus has a "tamper protection" or "self-defense" feature, you may need to disable that too for the SSU to replace protected system files.
3. Run the update check and let the SSU install.
4. Immediately re-enable your antivirus protection. If the SSU only installs with protection off, consider adding the Windows servicing paths to your antivirus exclusions — or switching to Windows Security, which never conflicts with updates.

### Fix 6: Reset the update cache manually

A damaged download or corrupted metadata can make the SSU fail identically every retry. Rebuild the cache.

1. Open Command Prompt as administrator and stop the services:
   ```
   net stop wuauserv
   net stop bits
   net stop cryptsvc
   ```
2. Rename the cache folders:
   ```
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   ren C:\Windows\System32\catroot2 catroot2.old
   ```
3. Restart the services with `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Check for updates. If the SSU now downloads fresh and installs, the old cache was the problem. For the broader picture on stuck downloads, see our guide to updates [stuck downloading on Windows 11](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/) — the same cache mechanics apply on Windows 10.

### Fix 7: Install the SSU manually from the Microsoft Update Catalog

When Windows Update cannot install the SSU by itself, do its job for it — download the exact package and run it.

1. Find the KB number of the SSU from your update history (Fix 1) or look up the latest SSU for your Windows 10 build on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Search the catalog for that KB number, download the version matching your system (x64 for most laptops), and save the `.msu` file.
3. Double-click the `.msu` to install it — run it as administrator and let it finish, even if it sits at a percentage for a while.
4. Restart when prompted, then run Windows Update again. The previously failing cumulative updates should now install, since their SSU prerequisite is satisfied. If the manual install also fails, the component store is still damaged — revisit Fix 4 with an ISO source.

## Closing

A failed servicing stack update is a machinery problem, not a package problem: the installer that delivers your updates is broken, so everything behind it fails too. The DISM repair in Fix 4 and the manual catalog install in Fix 7 resolve nearly every case — repair the store, then hand-install the SSU, and the backlog of cumulative updates will clear on its own. Keep an eye on update history afterward: a healthy SSU line is the quiet sign that your update pipeline is working again.
