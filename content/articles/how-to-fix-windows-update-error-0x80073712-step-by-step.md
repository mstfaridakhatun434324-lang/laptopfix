---
title: "How to Fix Windows Update Error 0x80073712 Step by Step"
slug: how-to-fix-windows-update-error-0x80073712-step-by-step
date: 2026-09-02
categories: ["windows-update"]
tags: ["windows update", "0x80073712", "component store", "windows 11"]
description: "Error 0x80073712 means the Windows component store is corrupted. Follow this step-by-step guide — DISM repair, SFC verify, and in-place upgrade."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80073712-step-by-step.webp"
faqs:
  - q: "What does Windows Update error 0x80073712 mean?"
    a: "It is ERROR_SXS_COMPONENT_STORE_CORRUPT: the WinSxS component store, Windows' master library of system file versions, is damaged. Every update is assembled from parts in this store, so a corrupted store blocks all updates. Common causes are interrupted updates, aggressive cleaner utilities deleting store files, disk errors, and failed driver installations writing conflicting data."
  - q: "In what order should I run DISM and SFC?"
    a: "Run DISM first, then SFC. SFC repairs protected system files using the component store as its source, so running SFC against a corrupted store is futile — it would pull damaged replacements. DISM rebuilds the store itself; once the store is healthy, SFC can do its job properly. The sequence is CheckHealth, RestoreHealth, then sfc /scannow."
  - q: "How long does DISM RestoreHealth take?"
    a: "Anywhere from fifteen minutes to over an hour, depending on the extent of corruption, disk speed, and internet bandwidth, since it downloads clean components. Let it reach one hundred percent without closing the window, sleeping the laptop, or losing power. Interrupting DISM mid-repair can leave the store worse than before, so start it when you can leave the machine alone."
  - q: "Will an in-place upgrade delete my programs?"
    a: "Not if you choose Keep personal files and apps during setup. The in-place upgrade reinstalls Windows over itself while preserving your data, installed programs, and most settings. It is the heaviest repair here but also the most thorough, replacing the entire component store. Back up irreplaceable files first anyway, as insurance against power loss during the upgrade."
---

Error 0x80073712 reports ERROR_SXS_COMPONENT_STORE_CORRUPT — the Windows component store is damaged. Think of WinSxS as the parts warehouse every update draws from: when the warehouse itself is compromised, nothing built from its parts can be trusted, and Windows refuses to install any of it. Every update, large or small, fails with the same code until the store is repaired.

This sounds catastrophic, but the repair tooling is purpose-built for exactly this scenario. DISM exists largely to rebuild damaged component stores, and it succeeds in the great majority of cases. The sequence below escalates deliberately: assess the damage, repair online, repair from ISO media if needed, verify with SFC, rule out disk problems, and only then rebuild Windows itself. A practical note on patience: DISM's RestoreHealth is doing genuinely heavy work — comparing thousands of components against clean copies and downloading replacements — so a run that looks stuck at 20 percent for twenty minutes is usually working normally. Judge progress by disk and network activity in Task Manager rather than the percentage counter, and only consider a run failed if it reports an actual error code or makes zero progress for over an hour.

## Why this happens

- **Updates interrupted mid-install.** Power failures and forced reboots leave the store half-written.
- **Cleaner utilities.** Third-party tools deleting WinSxS content they don't understand.
- **Disk-level corruption.** Bad sectors damaging store files over time.
- **Failed driver installs.** Conflicting component manifests from botched driver packages.
- **Malware.** Infections damaging system components before being cleaned.
- **Interrupted past repairs.** A DISM or SFC run killed halfway through.
- **Storage wear.** Aging SSDs corrupting rarely-read files.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the store's health

A quick assessment before committing to the long repair.

1. Open an administrator Command Prompt and run `DISM /Online /Cleanup-Image /CheckHealth` for the fast verdict.
2. If corruption is reported, run `DISM /Online /Cleanup-Image /ScanHealth` for the full picture.
3. Use the result to set expectations: detected-but-bounded corruption is a standard RestoreHealth case.
4. Hold off on SFC for now — it needs the repaired store as its source.

### Fix 2: Run DISM RestoreHealth

The main event: rebuild the damaged store from clean components.

1. In the elevated prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Keep the machine awake, plugged in, and connected — it fetches clean files from Windows Update.
3. Do not interrupt it; allow up to an hour on badly damaged stores.
4. On successful completion, move to verification — resist testing the update until SFC confirms the repair.

### Fix 3: Repair from an ISO source when online repair fails

If the store is too far gone for self-repair, supply clean files externally.

1. Download the Windows 11 ISO from [Microsoft's official software download page](https://www.microsoft.com/en-us/software-download/windows11) and mount it; note the drive letter.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth /Source:wim:E:\sources\install.wim:1 /LimitAccess` with your letter in place of `E:`.
3. Check the image index with `DISM /Get-WimInfo /WimFile:E:\sources\install.wim` if the default index fails.
4. Let the sourced repair complete fully before moving on.

### Fix 4: Verify with SFC and reset the cache

Confirm the repair, then clear stale metadata.

1. Run `sfc /scannow` in the administrator Command Prompt and restart afterward.
2. Reset the update cache: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, then `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`, then restart the services.
3. Retry **Settings > Windows Update > Check for updates**.
4. A healthy store plus fresh metadata is the combination that clears this error.

### Fix 5: Rule out disk damage

Recurring corruption points below the software layer.

1. Run `chkdsk C: /f /r` from an administrator Command Prompt and reboot for the scan.
2. Examine the report for bad sectors and file-system errors.
3. Check SMART status via your drive maker's utility for early failure warnings.
4. Replace a failing drive before continuing — software repairs can't outlast bad hardware.

### Fix 6: Install the update manually

Test whether the repaired store handles a real package.

1. Note the failing KB from Update history.
2. Download its x64 `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Run the standalone installer and restart as prompted.
4. Success here confirms the store repair; failure sends you to the final fix.

### Fix 7: In-place upgrade as the definitive repair

Replace the entire store when targeted repair can't.

1. Run `setup.exe` from the mounted Windows 11 ISO.
2. Choose **Keep personal files and apps** when asked.
3. Allow 30–90 minutes, several restarts, charger connected, no interruptions.
4. Afterward, updates install against a pristine store. Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents this repair path for the truly stubborn cases.

### Fix 8: Roll back with System Restore to a healthy store

If the corruption is recent, a restore point may predate it entirely.

1. Press **Windows key + R**, type `rstrui.exe`, and press Enter to open System Restore.
2. Choose a restore point dated before the 0x80073712 errors began — the older, the better, within reason.
3. Let the restore complete and reboot; your personal files are untouched, though recently installed programs may need reinstalling.
4. Retry the update. If no restore point exists or the error persists, proceed to the in-place upgrade in Fix 7 — and enable System Protection afterward so you have restore points next time.

## Closing

Error 0x80073712 is the component store asking for reconstruction, and the DISM-to-upgrade ladder above handles every severity of it. For HP-specific context like driver-install conflicts, see the [HP laptop version](/articles/how-to-fix-windows-update-error-0x80073712-on-hp-laptop/), and if your error is a missing prerequisite rather than store corruption, the [0x800F0831 step-by-step guide](/articles/how-to-fix-windows-update-error-0x800f0831-step-by-step/) is the right companion.
