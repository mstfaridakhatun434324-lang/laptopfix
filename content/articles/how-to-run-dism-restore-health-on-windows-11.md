---
title: "How to Run DISM RestoreHealth on Windows 11"
slug: how-to-run-dism-restore-health-on-windows-11
date: 2026-09-20
categories: ["windows-errors"]
tags: ["DISM", "system repair", "windows 11"]
description: "Repair Windows 11's component store with DISM RestoreHealth — the exact commands, offline ISO method, and verification steps."
thumbnail: "/images/thumbs/how-to-run-dism-restore-health-on-windows-11.webp"
faqs:
  - q: "Is DISM different on Windows 11 than Windows 10?"
    a: "The commands are identical, but Windows 11's servicing stack is newer and the online repair is generally more reliable. The main practical difference: Windows 11 ISOs from Microsoft always work as an offline source, and the Settings paths for reaching recovery tools have moved."
  - q: "How do I know DISM actually fixed anything?"
    a: "Run DISM /Online /Cleanup-Image /CheckHealth afterward — it should report no component store corruption. Then run sfc /scannow, which should complete with no unfixable files. If the original symptom (failed updates, crashes) is gone too, the repair held."
  - q: "Can DISM fix blue screens?"
    a: "It can fix blue screens caused by corrupt system files — which covers a meaningful share of cases. It cannot fix driver bugs, bad RAM, or failing drives. If dumps name a third-party .sys file, fix the driver; DISM is for when Windows' own files are the problem."
  - q: "Is it safe to interrupt DISM if it seems stuck?"
    a: "No — let it finish. The progress bar routinely appears frozen at percentages like 62% while it downloads and verifies files in the background. Interrupting a servicing operation can leave the component store in a worse state than you started with."
---
On Windows 11, **DISM RestoreHealth** does the same vital job it does on Windows 10: it repairs the component store — the master repository of system files — so that SFC and Windows Update have clean files to work with. When SFC says it found corruption it could not fix, or when cumulative updates fail repeatedly with obscure errors, RestoreHealth is the correct next step.

The commands are short; the understanding of what they do and what to do when they fail is what this guide provides.

## Why this happens

The component store gets damaged by the usual suspects:

- **Failed cumulative or feature updates:** Windows 11's frequent updates occasionally fail midway, leaving the store inconsistent.
- **Disk errors and bad sectors:** Corrupting stored component files silently over time.
- **Power loss during servicing:** Shutdowns while updates are installing.
- **Malware or "debloating" scripts:** Removing or modifying servicing components.
- **Interrupted upgrades:** Feature updates (like 24H2) that partially applied.
- **Third-party cleaners:** Tools that aggressively "clean" WinSxS and servicing data.
- **Interrupted servicing stack updates:** Windows 11 updates its servicing stack itself; an interrupted servicing-stack update leaves the repair tools partially broken.

## How to fix it

Work through these in order.

### Fix 1: Open an elevated terminal

Windows 11 pushes you toward Terminal, which works fine for DISM.

1. Right-click **Start** and choose **Terminal (Admin)**. Click **Yes** on the UAC prompt.
2. If Terminal opens PowerShell, that is fine — DISM commands work identically in PowerShell and Command Prompt. (You can switch to a Command Prompt tab with the dropdown if you prefer.)
3. Confirm the title bar says "Administrator" before proceeding.

### Fix 2: Check store health

A quick read-only assessment before the repair. This step takes under a minute for CheckHealth and tells you whether corruption is even present — useful because if the store is clean, your problem lies elsewhere and you should not waste half an hour on a repair you do not need. ScanHealth goes deeper but takes ten minutes or more; run it when CheckHealth is ambiguous or when you want certainty before committing to the full restore.

1. Run: `DISM /Online /Cleanup-Image /CheckHealth`
2. For a thorough scan: `DISM /Online /Cleanup-Image /ScanHealth` — slower (10+ minutes) but actually inspects the store.
3. Note the result, then proceed to repair regardless — the check just sets expectations.

### Fix 3: Run RestoreHealth

The main repair command. Before running it, close unnecessary programs and plug in the charger — DISM is disk- and CPU-intensive, and a mid-repair shutdown from a dead battery can leave the component store worse than you found it. On a quiet system with an SSD, expect 10-30 minutes; the percentage will appear frozen at points, which is normal behavior while files download and verify in the background.

1. Run: `DISM /Online /Cleanup-Image /RestoreHealth`
2. Be patient: 10-30 minutes on an SSD, longer on spinning drives. The progress percentage will appear stuck at points — it is working.
3. Success looks like "The restore operation completed successfully." Failure with `0x800f081f` means it could not reach clean source files — continue to Fix 4.

### Fix 4: Use a Windows 11 ISO as the offline source

When the online repair cannot fetch clean files, supply them yourself.

1. Download the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) and double-click to mount it — note the drive letter.
2. Check available images: `DISM /Get-WimInfo /WimFile:E:\sources\install.wim` (adjust the letter; use `install.esd` if present instead).
3. Run: `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:E:\sources\install.wim:1 /LimitAccess` with the right index for your edition (Home/Pro).
4. The `/LimitAccess` flag prevents it from trying Windows Update, forcing the offline source.

### Fix 5: Complete the repair with SFC

Now that the store is clean, let SFC finish the job. This is the payoff step: SFC scans every protected system file and replaces damaged ones from the freshly repaired store. Run it, let it complete without interruption, and reboot — then retest whatever was originally broken rather than assuming success.

1. Run: `sfc /scannow`
2. It should now repair files it previously could not. Reboot afterward.
3. Retest the original problem — failed updates, crashes, broken features. If blue screens persist and dumps implicate drivers rather than Windows files, move to driver troubleshooting: our [critical process died walkthrough](/articles/how-to-fix-critical-process-died-step-by-step/) covers the driver side of post-repair crashes.

### Fix 6: Verify and update

Confirm the repair and get current. Do not skip the update pass: a freshly repaired component store with months of pending cumulative updates is still vulnerable to the same corruption patterns, and the pending updates often include servicing-stack improvements that make the next repair easier.

1. Re-run `DISM /Online /Cleanup-Image /CheckHealth` — expect a clean report.
2. Go to **Settings > Windows Update** and install everything pending. Previously failing updates should now install.
3. Create a restore point (**Settings > System > About > System protection**) so the next problem has a one-click rollback. Microsoft documents additional servicing guidance on [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 7: Repair from the recovery environment

For systems that will not boot, the same tools work offline.

1. Boot to **Troubleshoot > Advanced options > Command Prompt** from recovery.
2. Find your Windows drive letter with `diskpart` > `list volume` (it is often not C: here).
3. Run: `DISM /Image:C:\ /Cleanup-Image /RestoreHealth /Source:WIM:E:\sources\install.wim:1` (adjust letters), then `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.
4. Type `exit` and choose **Continue** to attempt a normal boot.

## Closing

Windows 11's DISM RestoreHealth is three commands that fix what nothing else can: a corrupt component store. Check health, restore it (from Windows Update or a mounted ISO), verify with SFC, and update. When system-file corruption is the disease, this is the cure — quick, safe, and built into every copy of Windows 11. For the broader blue-screen troubleshooting that file repair fits into, our [general BSOD fix guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) puts DISM in context with driver and hardware steps.
