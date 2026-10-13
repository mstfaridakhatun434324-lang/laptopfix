---
title: "How to Run DISM RestoreHealth on Windows 10"
slug: how-to-run-dism-restore-health-on-windows-10
date: 2026-09-19
categories: ["windows-errors"]
tags: ["DISM", "system repair", "windows 10"]
description: "DISM RestoreHealth repairs the Windows 10 component store that SFC depends on. Here's the exact command sequence, explained."
thumbnail: "/images/thumbs/how-to-run-dism-restore-health-on-windows-10.webp"
faqs:
  - q: "What does DISM RestoreHealth actually do?"
    a: "DISM (Deployment Image Servicing and Management) checks the Windows component store — the repository of system files SFC draws from — against known-good copies and repairs corruption. If SFC reports it cannot fix files, the component store itself is usually damaged, and RestoreHealth fixes that underlying layer."
  - q: "Should I run SFC or DISM first?"
    a: "Run SFC first: sfc /scannow. If it reports corrupt files it could not repair, run DISM RestoreHealth, then run SFC again. DISM repairs the source; the second SFC pass then succeeds because it finally has clean files to copy from."
  - q: "How long does RestoreHealth take on Windows 10?"
    a: "Typically 10 to 30 minutes on an SSD, longer on a hard drive. The progress bar often appears stuck at 20% or 40% for long stretches — that is normal. Do not close the window; let it finish."
  - q: "Does DISM need an internet connection?"
    a: "Usually yes — RestoreHealth downloads clean files from Windows Update by default. If it fails with a source error, you can point it at a Windows 10 installation ISO instead, which works fully offline."
---
**DISM** with the **RestoreHealth** option is the heavy artillery of Windows 10 system repair. When `sfc /scannow` reports "found corrupt files but was unable to fix some of them," the problem is usually not the files themselves — it is the component store SFC copies replacements from. RestoreHealth repairs that store, and then SFC can do its job.

This guide covers the exact commands for Windows 10, what each one does, how long to wait, and what to do when the online repair cannot find clean files.

## Why this happens

You reach for DISM when the component store is damaged — and it gets damaged by:

- **Interrupted Windows updates:** Updates that fail midway leave the store inconsistent.
- **Disk errors:** Bad sectors corrupting stored component files.
- **Forced shutdowns during servicing:** Power loss while Windows is installing updates.
- **Malware damage:** Infections that modify or replace system components.
- **Failed upgrades:** Windows 10 feature updates that partially applied.
- **Third-party "cleaners":** Aggressive utilities deleting servicing components to "save space."
- **Dual-boot time conflicts:** On dual-boot machines, the other OS resetting the hardware clock can corrupt servicing timestamps.

## How to fix it

Work through these in order. Each step builds on the last.

### Fix 1: Open an elevated Command Prompt

DISM requires administrator rights — without them, every command fails.

1. Click **Start**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Click **Yes** on the UAC prompt. The title bar should say "Administrator: Command Prompt."
3. Keep this window open for the whole process. Do not run these commands in a regular Command Prompt or from a limited account.

### Fix 2: Check the component store health first

Before repairing, see what state the store is in.

1. Run: `DISM /Online /Cleanup-Image /CheckHealth`
2. This is a quick read-only check — it tells you whether corruption is detected, but not whether it is repairable.
3. For a deeper (but slower) scan: `DISM /Online /Cleanup-Image /ScanHealth`. This can take 10+ minutes and actually examines the store contents. Either way, proceed to the repair step — these checks just tell you what to expect.

### Fix 3: Run RestoreHealth (the main repair)

The core command. This is the one that fixes the store. Before running it, close unnecessary programs — DISM competes for disk and CPU, and while it will not damage anything by running alongside your work, it finishes noticeably faster on a quiet system. Laptops on battery should be plugged in; a shutdown mid-repair from a dead battery is one of the few ways to make component-store corruption worse.

1. Run: `DISM /Online /Cleanup-Image /RestoreHealth`
2. Wait. The progress bar will stall — often at 20%, 40%, or 62% — for many minutes. This is normal; DISM is downloading and verifying files. Typical time: 10-30 minutes on SSD, up to an hour on HDD.
3. When it reports "The restore operation completed successfully," the store is repaired. If it reports failure or error `0x800f081f` (source files not found), continue to Fix 4.

### Fix 4: Provide an offline source when online repair fails

If Windows Update cannot supply clean files, point DISM at a Windows 10 ISO.

1. Download the Windows 10 ISO via the [Microsoft Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11) page (select Windows 10) and mount it by double-clicking — note the drive letter (e.g., `E:`).
2. Find the image index: `DISM /Get-WimInfo /WimFile:E:\sources\install.wim` (use `install.esd` if that is what the ISO contains).
3. Run: `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:E:\sources\install.wim:1 /LimitAccess` (replace `1` with the correct index for your edition).
4. This performs the repair fully offline from known-good installation files.

### Fix 5: Follow up with SFC

DISM repaired the store; now let SFC use it. This ordering matters and is the most common mistake people make with these tools — running SFC repeatedly without fixing the store first just produces the same "unable to fix" message. The second SFC pass after a successful RestoreHealth is where the actual file replacement happens.

1. Run: `sfc /scannow` and wait for completion.
2. This time it should report that corrupt files were found and repaired — the clean store gives it good copies to work with.
3. Reboot. Test whatever was broken: blue screens, update failures, or malfunctioning features. For persistent driver-related crashes after file repair, our [driver IRQL troubleshooting guide](/articles/driver-irql-not-less-or-equal-troubleshooting/) picks up where DISM leaves off.

### Fix 6: Verify the repair stuck

Confirm the component store is actually healthy now.

1. Run `DISM /Online /Cleanup-Image /CheckHealth` again — it should report no corruption detected.
2. Check **Settings > Update & Security > Windows Update** and install any pending updates; a repaired store lets previously failing updates install cleanly.
3. If corruption returns quickly, suspect the drive: run `chkdsk C: /f /r` and check SMART health. A failing drive re-corrupts the store as fast as you repair it.

### Fix 7: Run DISM from recovery when Windows will not boot

The offline variant works from the recovery environment too.

1. Boot into recovery (**Troubleshoot > Advanced options > Command Prompt**) from installation media or the automatic repair screen.
2. Identify your Windows drive letter (it may not be C: here — use `diskpart`, then `list volume`).
3. Run: `DISM /Image:C:\ /Cleanup-Image /RestoreHealth /Source:WIM:E:\sources\install.wim:1` with the correct letters for your Windows partition and mounted ISO.
4. Follow with the offline SFC: `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.

## Closing

DISM RestoreHealth on Windows 10 is a three-act repair: check the store, restore it (online, or from an ISO when online fails), then run SFC to propagate the clean files. It looks intimidating, but it is three commands — and it fixes the class of corruption that nothing else touches. If your original symptom was Windows Update failing with cryptic error codes, our [0x80070057 fix guide](/articles/error-code-0x80070057-fix/) covers the update-specific side once the store itself is healthy.
