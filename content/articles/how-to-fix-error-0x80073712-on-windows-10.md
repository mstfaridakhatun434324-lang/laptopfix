---
title: "How to Fix Error 0x80073712 on Windows 10 (Component Store Corrupt)"
slug: how-to-fix-error-0x80073712-on-windows-10
date: 2026-09-10
categories: ["windows-errors"]
tags: ["0x80073712", "windows update error", "component store", "windows 10"]
description: "Error 0x80073712 means Windows' component store is damaged. Fix it with DISM, manual update installs, and in-place repair on Windows 10."
thumbnail: "/images/thumbs/how-to-fix-error-0x80073712-on-windows-10.webp"
faqs:
  - q: "What does error 0x80073712 mean?"
    a: "It means the Windows component store (WinSxS) — the master library Windows Update draws from — is corrupted. The full message is usually 'Some update files are missing or have problems.' Updates can't install because the store they need to reference is damaged. The primary fix is DISM's RestoreHealth, which rebuilds the store from known-good sources."
  - q: "What's the difference between SFC and DISM for this error?"
    a: "SFC repairs individual system files using the component store as its source; DISM repairs the component store itself. For 0x80073712, the store is the problem, so DISM is the primary tool — run it first. After DISM succeeds, run SFC to fix any files that were damaged while the store was broken."
  - q: "Will DISM RestoreHealth delete my files or programs?"
    a: "No. DISM's RestoreHealth only repairs Windows system components — it doesn't touch personal files, installed programs, or settings. It's safe to run and is the officially supported repair path for component store corruption."
  - q: "What if DISM fails with its own error?"
    a: "DISM needs a healthy source to rebuild from. If it fails, provide one explicitly: mount a Windows 10 ISO matching your version and use the /Source flag pointing at its install.wim, or /LimitAccess with a local source. As a fallback, an in-place upgrade reinstalls the entire component store cleanly."
---
Error 0x80073712 is Windows Update telling you its parts warehouse is damaged. The component store (the WinSxS folder) is the master library of system files that every update draws from — when it corrupts, updates fail with "some update files are missing or have problems," and no amount of retrying helps. The fix targets the store directly: DISM rebuilds it, and then updates flow again.

This is a very fixable error, and nothing here risks your personal files. Work the steps in order and don't skip the DISM source tricks in Fix 3 — they're what separate a quick fix from a frustrating loop. Most people are done by Fix 2; the later steps exist for the stubborn cases where DISM can't reach its repair sources or the disk itself is contributing to the corruption.

## Why this happens

- **Interrupted updates.** A power loss or forced shutdown mid-update leaves the component store half-written.
- **Disk errors.** Bad sectors in the WinSxS area corrupt stored components.
- **Aggressive cleaning tools.** Some "system cleaners" delete WinSxS files they deem unnecessary, breaking the store.
- **Failed feature updates.** A feature update that rolled back midway can leave the store inconsistent.
- **Malware damage.** Some malware deliberately damages system components to prevent updates from patching vulnerabilities.
- **Aging installations.** Years of updates, partial installs, and rollbacks gradually increase the chance of store corruption.
- **Multiple interrupted feature updates.** Each failed upgrade attempt compounds store damage, which is why this error often appears after two or three bad upgrade tries in a row.

## How to fix it

Work through these in order.

### Fix 1: Run the Windows Update troubleshooter

Clear any simple service-level issues first.

1. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply its fixes.
3. Restart and retry the update.
4. If 0x80073712 returns, the store itself is damaged — continue to DISM.

### Fix 2: Repair the component store with DISM

The core fix for this error.

1. Open **Command Prompt as administrator**.
2. Run `DISM /Online /Cleanup-Image /ScanHealth` to confirm corruption.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait — this downloads clean components from Windows Update and can take 15–30 minutes.
4. When it completes successfully, run `sfc /scannow` to fix any files damaged while the store was broken, then restart and retry the update.
5. If RestoreHealth completes but reports it couldn't repair everything, run it once more — the second pass often finishes what the first started, since the first pass repaired the download pipeline itself.

### Fix 3: Give DISM an explicit repair source

If RestoreHealth fails or can't reach Windows Update, point it at a local source.

1. Download the Windows 10 ISO matching your installed version and mount it (double-click the ISO).
2. Note the drive letter of the mounted ISO (e.g., E:).
3. Run: `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:E:\sources\install.wim:1 /LimitAccess`
4. If your ISO uses install.esd instead, convert it or use `/Source:ESD:E:\sources\install.esd:1`.
5. After success, run `sfc /scannow`, restart, and retry the update.

### Fix 4: Reset the Windows Update components

Clear the cache so the repaired store gets a clean pipeline.

1. In an elevated Command Prompt, stop the services:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
2. Rename the caches:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
3. Restart the services with `net start` for each, then restart the laptop.
4. Check for updates — the combination of a repaired store and fresh cache resolves most persistent cases.
5. After the cache reset, don't retry the same update ten times in a row — check once, and if it fails again, move to the manual install in Fix 5 instead of deepening the corruption with repeated attempts.

### Fix 5: Install the update manually from the catalog

Bypass the automatic pipeline while the store heals.

1. Find the failing update's KB number in **Settings > Update & Security > Windows Update > View update history**.
2. Search it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and download the x64 package.
3. Run the `.msu` file manually.
4. This sometimes succeeds even when automatic update fails, buying time while you complete the deeper repairs.

### Fix 6: Check the drive for errors

Recurring store corruption points at the disk.

1. Run `chkdsk C: /f /r` from an elevated Command Prompt and restart to allow the scan.
2. Check SMART health with your SSD/HDD maker's tool.
3. If the drive shows warnings, back up and replace it — a failing drive will keep corrupting the store no matter how often you repair it.
4. On a healthy drive, the DISM repair should now hold.
5. While you're at it, verify the system drive has at least 20GB free — DISM needs working space to stage repaired components, and a cramped drive can make RestoreHealth fail for no other reason.

### Fix 7: In-place upgrade to rebuild everything

The definitive fix when DISM can't repair the store.

1. Download the Windows 10 Media Creation Tool and choose **Upgrade this PC now**.
2. Select **Keep personal files and apps**.
3. The upgrade reinstalls Windows over itself, building a brand-new component store.
4. Afterward, updates install cleanly. Related error-code guides: [0x80070003](/articles/how-to-fix-error-0x80070003-on-windows-10/) and [0x80070057](/articles/error-code-0x80070057-fix/).

## Closing

Error 0x80073712 looks intimidating but has a clear repair path: DISM rebuilds the store, SFC fixes the files, and the update cache gets reset. The step people miss is Fix 3 — when DISM can't reach Windows Update for clean files, giving it a local ISO source turns a failure into a success.

Once fixed, protect the store: never let "cleaner" tools touch WinSxS, and don't force-shutdown during updates. It's also worth running `DISM /Online /Cleanup-Image /ScanHealth` every few months as a preventive check — it takes a couple of minutes and catches store corruption early, before it starts blocking updates. A healthy component store is one of those invisible things you only notice when it breaks; a tiny bit of maintenance keeps it invisible.
