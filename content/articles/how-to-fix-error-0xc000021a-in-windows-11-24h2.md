---
title: "How to Fix Error 0xc000021a in Windows 11 24H2"
slug: how-to-fix-error-0xc000021a-in-windows-11-24h2
date: 2026-09-22
categories: ["windows-errors"]
tags: ["0xc000021a", "blue screen", "winlogon", "windows 11 24h2"]
description: "Fix the 0xc000021a blue screen in Windows 11 24H2 — repair winlogon/csrss failures, rebuild the BCD, run SFC offline, and restore boot."
thumbnail: "/images/thumbs/how-to-fix-error-0xc000021a-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0xc000021a mean?"
    a: "It means a critical user-mode process — winlogon.exe or csrss.exe — terminated unexpectedly. Windows cannot run without these, so it blue-screens. The usual causes are corrupted system files, a bad update, or a driver that crashes during the login phase."
  - q: "Why does 0xc000021a happen after the 24H2 update?"
    a: "Feature updates replace thousands of system files, and if the update is interrupted or a driver conflicts with the new build, winlogon or csrss can fail to start. The recovery environment tools below — offline SFC, DISM, and BCD rebuild — are designed for exactly this."
  - q: "Can I fix 0xc000021a without reinstalling Windows?"
    a: "Usually yes. The offline SFC/DISM repairs and BCD rebuild fix the majority of cases without touching your files or apps. Reinstallation is the last resort, and even then an in-place repair keeps everything."
  - q: "Is 0xc000021a a virus?"
    a: "No. It is a system integrity failure, not malware — though running a Defender Offline scan is still a sensible step since malware can damage the same processes. Do not download '0xc000021a fixer' tools from random sites; they are the actual malware risk here."
---

**0xc000021a** is the blue screen you get when Windows' login machinery dies. Specifically, it means **winlogon.exe** or **csrss.exe** — two processes Windows absolutely cannot run without — terminated unexpectedly. Since there is no recovering from that, Windows stops everything and shows you the error. It often appears right after a feature update like 24H2, because that is when thousands of system files get replaced and the login components are most vulnerable.

The defining trait of this error: you usually cannot boot into Windows at all, so every fix happens from the **recovery environment** (WinRE). That sounds intimidating, but the steps are just typed commands. If you *can* boot, the same commands work from an admin Terminal — but most 0xc000021a victims will be doing this from the blue **Choose an option** screen. For the closely related boot-failure cousin, see our [SrtTrail.txt guide](/articles/srttrail-txt-blue-screen-error-bsod-windows-11/).

A practical note on drive letters before you begin: in the recovery environment, your Windows drive is frequently **not** C:. WinRE boots from its own hidden partition and assigns letters differently, so Windows usually lands on D: or E:. Every command below that references a drive letter includes a reminder to verify first with `diskpart` → `list volume`. Getting the letter wrong does not damage anything — the commands just fail — but verifying first saves you a round of confusion. When in doubt, look for the largest NTFS volume; that is almost always your Windows drive.

## Why this happens

- **Corrupted winlogon.exe or csrss.exe.** Disk errors or an interrupted 24H2 update damage these critical files.
- **Mismatched system files after an update.** New kernel files paired with old user-mode components (or vice versa) after a partial update.
- **Corrupt Boot Configuration Data (BCD).** If the boot loader points at the wrong Windows installation or a damaged one, the login processes fail to initialize.
- **A driver crashing at login.** Graphics and credential-provider drivers load during the login phase; a bad one can take winlogon down with it.
- **Malware damage.** Some malware targets winlogon specifically; even after removal, the damage remains.
- **Failing drive.** Bad sectors on the exact files Windows needs at login produce this error with maddening consistency.

## How to fix it

Work through these in order from the recovery environment. To get there: interrupt the boot three times, or boot from Windows installation media and choose **Repair your computer**.

### Fix 1: Run Startup Repair

1. On the **Choose an option** screen, go to **Troubleshoot > Advanced options > Startup Repair**.
2. Select your Windows installation and let it run. It fixes common boot-loader and BCD issues automatically.
3. If it reports it could not repair, continue — Startup Repair is the quick attempt, not the thorough one.

### Fix 2: Run SFC and DISM offline

This is the core repair for 0xc000021a — it fixes the damaged login components directly.

1. Go to **Troubleshoot > Advanced options > Command Prompt**.
2. First, confirm your Windows drive letter — in WinRE it is often **D:** instead of C:. Type `diskpart`, then `list volume`, then `exit` to check.
3. Run SFC against the offline installation (adjust the letter if needed):
   `sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows`
4. Then run DISM offline:
   `DISM /Image:D:\ /Cleanup-Image /RestoreHealth`
5. Run the SFC command once more, type `exit`, and choose **Continue** to reboot.

### Fix 3: Rebuild the BCD and boot files

If the boot configuration is corrupt, Windows may be loading the wrong or damaged installation.

1. Open **Command Prompt** from Advanced options.
2. Run these commands one at a time:
   - `bootrec /fixmbr`
   - `bootrec /fixboot` (if this gives "Access denied," use the next approach instead)
   - `bootrec /rebuildbcd`
3. If fixboot fails, rebuild the EFI partition manually:
   - `diskpart`, then `list vol`, identify the EFI partition (FAT32, ~100MB), `sel vol <number>`, `assign letter=Z:`, `exit`
   - `bcdboot D:\Windows /s Z: /f UEFI` (adjust D: to your Windows drive)
4. Type `exit` and reboot.

### Fix 4: Uninstall the latest update from WinRE

1. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Choose **Uninstall the latest quality update** first; if the problem started after 24H2 itself, choose **Uninstall the latest feature update**.
3. Reboot and test. If Windows boots, pause updates (**Settings > Windows Update > Pause updates**) and check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known 24H2 issues before retrying.

### Fix 5: Disable driver signature enforcement and test

If a bad driver is killing winlogon at login:

1. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **7** (Disable driver signature enforcement).
2. If Windows boots, a third-party driver is the culprit. Open **Device Manager** and look for recently updated drivers — roll back the graphics driver first (**Properties > Driver > Roll Back Driver**).
3. Also try Safe Mode (option **4**): if Safe Mode boots but normal mode does not, that confirms a driver or startup program.

### Fix 6: Check disk health and run a malware scan

1. From the WinRE Command Prompt, run `chkdsk D: /f /r` (your Windows drive letter) and let it complete — this can take a while.
2. For malware: boot into Safe Mode if possible, then run a **Microsoft Defender Offline scan** from **Windows Security > Virus & threat protection > Scan options**.
3. If chkdsk finds extensive bad sectors, prioritize data recovery — clone the drive before it deteriorates further.

### Fix 7: System Restore, then in-place repair

1. Go to **Troubleshoot > Advanced options > System Restore** and pick a restore point from before the problem started. Your files are not affected.
2. If no restore point exists or it fails, do an in-place repair: boot from Windows 11 installation media (created on another PC from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11)), but instead of clean-installing, run setup from within the media while booted into Safe Mode if possible — or use the media's repair options first.
3. As a final measure, **Reset this PC** from **Troubleshoot > Reset this PC** with **Keep my files**.

## Closing

**0xc000021a** in 24H2 is Windows telling you its login processes are damaged — and the offline SFC/DISM repair plus a BCD rebuild fix that damage in most cases without costing you a single file. If your machine instead gets stuck in the Automatic Repair loop without ever showing this code, our [SrtTrail.txt guide](/articles/srttrail-txt-blue-screen-error-bsod-windows-11/) covers that sibling scenario. If the same 0xc000021a code appears on an earlier Windows 11 build rather than 24H2, our [0xc000021a guide for Windows 11](/articles/how-to-fix-error-0xc000021a-on-windows-11/) covers the non-24H2 behavior. The recovery environment looks stark, but it gives you everything you need: the commands are the same ones technicians use. Work the list patiently, and only reach for the reset option once the repairs have had their fair shot.
