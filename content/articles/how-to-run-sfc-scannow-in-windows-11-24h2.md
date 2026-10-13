---
title: "How to Run SFC Scannow in Windows 11 24H2 (Correctly)"
slug: how-to-run-sfc-scannow-in-windows-11-24h2
date: 2026-09-24
categories: ["windows-errors"]
tags: ["sfc scannow", "system file checker", "DISM"]
description: "SFC scannow repairs corrupted Windows 11 system files. Learn the right command order, what the results mean, and what to do when SFC can't fix it."
thumbnail: "/images/thumbs/how-to-run-sfc-scannow-in-windows-11-24h2.webp"
faqs:
  - q: "What does sfc /scannow actually do?"
    a: "System File Checker scans all protected Windows system files and compares them against known-good copies in the component store. When it finds a corrupted, modified, or missing file, it replaces it with the correct version automatically. It is the first-line repair for blue screens, update failures, and strange system behavior caused by file corruption."
  - q: "How long does sfc /scannow take?"
    a: "Typically 10 to 30 minutes depending on your drive speed — much faster on NVMe SSDs, slower on older SATA SSDs and hard drives. Let it reach 100 percent without interrupting it; closing the window mid-scan can leave repairs incomplete. If it appears stuck at a percentage for a long time, give it at least 30 minutes before concluding it has hung."
  - q: "What should I do if SFC finds corrupt files but can't fix them?"
    a: "Run DISM /Online /Cleanup-Image /RestoreHealth first — SFC draws its replacement files from the component store, and if that store is itself damaged, SFC cannot complete repairs. After DISM finishes, run sfc /scannow again and it will usually succeed. This SFC-then-DISM-then-SFC-again sequence is the standard professional workflow."
  - q: "Do I need to run SFC as administrator?"
    a: "Yes, always. System File Checker needs elevated privileges to scan and replace protected system files. Open Terminal or Command Prompt via Win + X and choose the Admin option; running it in a standard window will fail with an error telling you that you must be an administrator running a console session."
---

SFC — System File Checker — is the single most useful repair command in Windows, and `sfc /scannow` is the version you will reach for whenever system files are suspect: blue screens, updates that will not install, features that broke for no reason. It is simple to run but easy to run *wrong*: wrong order relative to DISM, wrong interpretation of the results, or giving up when the first scan cannot fix everything.

This guide covers the correct way to run it on Windows 11 24H2 — including the offline variant for when Windows will not boot — what each possible result message means, and the exact follow-up steps for each outcome.

## Why this happens

SFC exists because system files get corrupted. The usual ways:

- **Interrupted Windows updates.** Power loss or forced shutdowns mid-update leave files half-written.
- **Disk errors.** Bad sectors damaging files SFC protects.
- **Malware.** Infections modifying or replacing system files.
- **Bad shutdowns.** Repeated hard power-offs corrupting files mid-write.
- **Failed driver or software installs.** Installers overwriting shared system files.
- **Aging component store.** The repair source itself degrading, which is why DISM matters.

## How to fix it

Work through these in order — the sequence matters.

### Fix 1: Run SFC correctly as administrator

The baseline scan, done right.

1. Press `Win + X` and choose **Terminal (Admin)**.
2. Type `sfc /scannow` and press Enter.
3. Wait for it to reach 100% — typically 10 to 30 minutes. Do not close the window.
4. Read the result message carefully (interpretations in Fix 3).
5. Restart the laptop after any repair, even if Windows does not ask.

### Fix 2: Run DISM first if SFC fails or cannot repair

SFC pulls replacement files from the component store — if the store is damaged, SFC fails. DISM repairs the store.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Wait for completion — 15 to 30 minutes, longer on slow connections since it may download files.
3. When DISM finishes successfully, run `sfc /scannow` again.
4. This DISM-then-SFC order is the professional standard; memorize it.

### Fix 3: Interpret the SFC result correctly

SFC reports one of four outcomes — each means something specific:

1. **"Windows Resource Protection did not find any integrity violations."** Your system files are fine; the problem lies elsewhere (drivers, hardware, configuration).
2. **"Found corrupt files and successfully repaired them."** Fixed — restart and retest whatever was broken. Check details in `C:\Windows\Logs\CBS\CBS.log` if curious.
3. **"Found corrupt files but was unable to fix some of them."** Run DISM (Fix 2), then SFC again. If it still cannot fix them, the offline method in Fix 4 or an in-place upgrade is next.
4. **"Could not perform the requested operation."** Usually means SFC was not run as admin, or Windows Modules Installer service is disabled — enable it in `services.msc` and retry elevated.

### Fix 4: Run SFC offline from the recovery environment

When Windows will not boot, run SFC against the offline installation.

1. Boot into WinRE (triple force-shutdown, or USB media > **Repair your computer**).
2. Open **Command Prompt** from **Troubleshoot > Advanced options**.
3. Find your Windows drive letter: `diskpart`, `list vol`, `exit` — it is often D: or E: here, not C:.
4. Run `sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows` using the correct letter.
5. Follow with offline DISM: `DISM /Image:D:\ /Cleanup-Image /RestoreHealth`.
6. Type `exit`, choose **Continue**, and boot normally.

### Fix 5: Point DISM at an ISO when online repair fails

If DISM cannot reach Windows Update for source files:

1. Download the Windows 11 ISO from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and double-click to mount it; note the drive letter.
2. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth /Source:E:\Sources\install.wim:1` (adjust letter; use install.esd if present).
3. Then run `sfc /scannow` again.

### Fix 6: Do an in-place upgrade when repairs cannot finish

If SFC and DISM both fail to produce a clean system:

1. Back up your important files.
2. Run the **Media Creation Tool** from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), choose **Upgrade this PC now**, keep files and apps.
3. The upgrade reinstalls Windows over itself with fresh files.
4. Run `sfc /scannow` afterward to confirm a clean result.

For booting into the recovery environment, see our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/), and for servicing errors SFC cannot touch, our [0x800f0900 repair walkthrough](/articles/how-to-fix-error-0x800f0900-in-windows-11-24h2/) goes deeper on component store damage. Microsoft documents the tool officially on [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 7: Make SFC part of routine maintenance (and know its limits)

SFC is a repair tool, not a monitoring tool — use it deliberately.

1. After every major Windows update, consider a quick `sfc /scannow` to catch update-induced corruption early.
2. If you run SFC monthly "just in case" and it always finds nothing, that is normal and healthy — stop worrying.
3. Know what SFC cannot fix: driver bugs, hardware faults, malware infections, and registry corruption are all outside its scope. If SFC is clean but problems persist, the cause is elsewhere — check drivers, test the RAM, and scan for malware instead of re-running SFC hoping for a different result.
4. Keep a log: if SFC repeatedly finds and repairs the same files, something is actively corrupting them — usually a failing drive. Run `chkdsk C: /f /r` and check SMART health rather than repairing forever.

## Closing

SFC is simple, but the order of operations is what makes it effective: DISM repairs the store, SFC repairs the files, and the offline flags let you do both when Windows will not boot. Learn to read the four result messages instead of just hoping for the best, and keep the ISO-source trick ready for machines with broken update pipelines. Run this sequence before you ever consider reinstalling — it resolves an enormous share of "Windows is acting weird" problems with zero data risk.
