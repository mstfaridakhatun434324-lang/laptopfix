---
title: "Fixing the 'This PC Can't Run Windows 11' Error"
slug: how-to-fix-this-pc-can-t-run-windows-11-youtube
date: 2026-10-12
categories: ["windows-errors"]
tags: ["windows 11 compatibility", "tpm", "secure boot"]
description: "Seeing 'This PC can't run Windows 11' during setup? Enable TPM, Secure Boot, and meet the requirements with this step-by-step fix guide."
thumbnail: "/images/thumbs/how-to-fix-this-pc-can-t-run-windows-11-youtube.webp"
faqs:
  - q: "What are the actual Windows 11 requirements?"
    a: "A 64-bit 1 GHz+ CPU with 2+ cores on Microsoft's supported list, 4 GB RAM, 64 GB storage, UEFI firmware with Secure Boot, TPM 2.0, and DirectX 12 graphics. The PC Health Check app tells you exactly which requirement your machine fails."
  - q: "How do I enable TPM 2.0?"
    a: "Restart into the BIOS/UEFI (F2, Del, or F10 during boot), find the security settings, and enable TPM — labeled TPM 2.0, Intel PTT, or AMD fTPM depending on your system. Save and exit, then re-run the compatibility check."
  - q: "How do I enable Secure Boot?"
    a: "In the BIOS, go to the Boot or Security tab and set Secure Boot to Enabled. Your disk must use GPT partitioning (not MBR) and Windows must be installed in UEFI mode — Secure Boot cannot enable on legacy BIOS/MBR installations."
  - q: "My CPU isn't on the supported list — can I still install Windows 11?"
    a: "Technically possible via workarounds, but not recommended: Microsoft blocks updates on unsupported hardware and you lose security patch guarantees. If the laptop is otherwise capable, the safe path is staying on Windows 10 (supported with extended updates) or upgrading the hardware."
---
"This PC can't run Windows 11" is frustrating because it's often wrong — or at least, fixable. Most laptops that show this message fail on one of two settings that are simply turned off: TPM 2.0 or Secure Boot. The hardware is usually fine; the configuration isn't.

This guide walks you from diagnosis (what exactly is failing) through each fix in order. Ten minutes in the BIOS resolves the large majority of these errors.

## Why this happens

- **TPM 2.0 is disabled in the BIOS.** The most common cause — the chip exists but is switched off.
- **Secure Boot is disabled.** Often off because the laptop shipped in legacy BIOS mode or someone disabled it.
- **Disk uses MBR instead of GPT.** Secure Boot and UEFI require GPT partitioning; older installs use MBR.
- **CPU not on Microsoft's supported list.** 7th-gen Intel and older, and pre-Ryzen AMD, are officially excluded.
- **Insufficient RAM or storage.** Less than 4 GB RAM or 64 GB disk fails the check legitimately.
- **Outdated BIOS.** Old firmware may not expose TPM 2.0 even when the hardware supports it.

## How to fix it

Work through these in order — check what's failing first, then fix that specific thing.

### Fix 1: Run PC Health Check to identify the failure

Don't guess — Microsoft's tool names the exact failing requirement.

1. Download the **PC Health Check** app from Microsoft and run it.
2. Click **Check now** under "Introducing Windows 11."
3. Read the results carefully — it lists each requirement as passed or failed.
4. Write down exactly which items fail. TPM and Secure Boot failures are settings fixes; CPU failures are hardware limits.

### Fix 2: Enable TPM 2.0 in the BIOS

The single most common fix for this error.

1. Restart and enter the BIOS/UEFI (**F2**, **Del**, or **F10** during boot — varies by maker).
2. Look under **Security** or **Advanced** for **TPM**, **TPM 2.0**, **Intel PTT** (Intel), or **AMD fTPM** (AMD).
3. Set it to **Enabled** — on some systems you must also set it to version **2.0** specifically if 1.2 is selected.
4. Save and exit (**F10** usually), then re-run PC Health Check. Also verify in Windows with `tpm.msc` — it should report "The TPM is ready for use."

### Fix 3: Enable Secure Boot

The second most common fix, with one prerequisite to check first.

1. In the BIOS, find **Secure Boot** under the **Boot** or **Security** tab and set it to **Enabled**.
2. If the option is greyed out, check whether the BIOS is in **UEFI mode** (not Legacy/CSM) — switch to UEFI first.
3. Also confirm your system disk uses **GPT**: open **Disk Management**, right-click the disk, choose **Properties > Volumes**, and check the partition style.
4. If the disk is MBR, convert it without data loss: boot to recovery Command Prompt and run `mbr2gpt /convert /allowfullos`, then enable Secure Boot. MBR-to-GPT issues also cause [INACCESSIBLE_BOOT_DEVICE](/articles/how-to-fix-blue-screen-of-death-windows-11/)-type errors, so this conversion pulls double duty.

### Fix 4: Update the BIOS

Old firmware may hide TPM 2.0 or lack proper Windows 11 support flags.

1. Note your BIOS version with `msinfo32`.
2. Check your laptop maker's support page for a newer BIOS — release notes often mention "Windows 11 support" explicitly.
3. Flash the update with the charger connected.
4. Re-enter the BIOS after updating and re-check TPM and Secure Boot settings — updates sometimes reset them to defaults.

### Fix 5: Verify RAM, storage, and CPU

Confirm the remaining requirements are genuinely met.

1. Check RAM: **Settings > System > About** should show at least 4 GB installed.
2. Check storage: **File Explorer > This PC** should show 64 GB+ total on the system drive.
3. Check the CPU against Microsoft's supported processor list — search Microsoft's site for "Windows 11 supported Intel/AMD processors."
4. If the CPU is unsupported but everything else passes, you're at a decision point, not a fix point — see the FAQ on unsupported installs.

### Fix 6: Do a clean install from Windows 11 media

If the checker passes but setup still complains, bypass the buggy check.

1. Download the **Windows 11 Installation Assistant** or **Media Creation Tool** from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Create installation media on a USB drive (8 GB+).
3. Boot from the USB and run setup — the media-based installer re-evaluates requirements itself.
4. Choose **Upgrade** to keep files and apps, or **Custom** for a clean install (back up first).

### Fix 7: Decide honestly about unsupported hardware

If the CPU is the blocker, make an informed choice rather than fighting the check.

1. Understand the trade-off: workarounds exist, but Microsoft withholds updates and support on unsupported CPUs.
2. For a daily-driver laptop, the responsible options are staying on Windows 10 with extended security updates or replacing the laptop.
3. Only consider bypass methods on a secondary machine where you accept the risk — never on the laptop holding your important data.
4. Whatever you decide, keep backups current; an unsupported install that misses a critical security update is a liability. For general Windows recovery knowledge either way, Microsoft's [support pages](https://support.microsoft.com/en-us/windows) document the official paths.

### Fix 8: Check for a failing drive underneath the installer complaints

Occasionally the compatibility check fails because the disk itself is unhealthy, not because requirements aren't met.

1. Run CrystalDiskInfo and confirm the system drive reports "Good" health — a failing drive can cause the installer to misreport requirements.
2. Run `chkdsk C: /f` from an elevated Command Prompt to fix file-system errors before attempting setup.
3. Ensure at least 20 GB of free space beyond the 64 GB requirement — cramped disks cause setup failures that masquerade as compatibility errors.

## Closing

"This PC can't run Windows 11" is a configuration error far more often than a hardware verdict. Enable TPM 2.0, enable Secure Boot (converting MBR to GPT if needed), update the BIOS, and re-run the check — that sequence clears the error on the large majority of laptops. Only a genuinely unsupported CPU is a hard stop, and that's a decision, not a bug. Once Windows 11 is running, keep drivers and firmware current so the next feature update doesn't bring its own surprises, like the [blue screens after updates](/articles/how-do-i-fix-blue-screen-after-windows-11-update/) some users hit.
