---
title: "How to Fix the 'This PC Can't Run Windows 11' Error Step by Step"
slug: how-to-fix-this-pc-can-t-run-windows-11-step-by-step
date: 2026-09-28
categories: ["windows-errors"]
tags: ["windows-11-requirements", "tpm", "secure-boot"]
description: "Seeing 'This PC can't run Windows 11'? Check TPM, Secure Boot, and CPU compatibility step by step and fix each blocker."
thumbnail: "/images/thumbs/how-to-fix-this-pc-can-t-run-windows-11-step-by-step.webp"
faqs:
  - q: "My laptop is only a few years old. Why does it fail the Windows 11 check?"
    a: "Almost always because TPM 2.0 or Secure Boot is disabled in BIOS — not because the hardware is actually incompatible. Most laptops from 2017 onward have TPM 2.0 built in; it's just switched off by default on some models. Enabling it in BIOS clears the check in the majority of cases."
  - q: "What is TPM and why does Windows 11 require it?"
    a: "TPM (Trusted Platform Module) is a security chip — or firmware feature on modern CPUs — that stores encryption keys and verifies boot integrity. Windows 11 requires TPM 2.0 to enable features like BitLocker, Windows Hello, and measured boot. On Intel laptops it appears as Intel PTT; on AMD as fTPM."
  - q: "Can I install Windows 11 without TPM 2.0?"
    a: "There are registry workarounds that bypass the check, but Microsoft doesn't support them: such installs may not receive updates and can break on future upgrades. The supported path is enabling TPM 2.0 in BIOS. Only consider bypasses on hardware that genuinely lacks TPM, and understand the trade-offs."
  - q: "Does enabling Secure Boot erase my data?"
    a: "No. Enabling Secure Boot changes only the boot verification policy; your files, apps, and Windows installation are untouched. The one precaution: if your disk uses legacy MBR partitioning, you may need to convert to GPT first — check that before toggling UEFI/Secure Boot settings."
---
"This PC can't run Windows 11" is the message the PC Health Check app and Windows Update show when your laptop fails Microsoft's compatibility requirements. Before you assume your laptop is too old, know this: most failures are configuration problems, not hardware problems. TPM 2.0 disabled in BIOS and Secure Boot turned off account for the vast majority of failed checks on laptops that are perfectly capable of running Windows 11.

This guide walks through each requirement in order, showing you how to check it and fix it. For brand-specific BIOS paths, see [the Lenovo variant](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-lenovo-laptop/) or [the Dell version](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-dell-laptop/).

## Why this happens

- **TPM 2.0 disabled in BIOS.** The single most common cause — the chip exists but is switched off (Intel PTT / AMD fTPM).
- **Secure Boot disabled.** Required by Windows 11; often off on laptops that shipped with Windows 10 in legacy mode.
- **Legacy BIOS / CSM mode instead of UEFI.** Secure Boot requires UEFI; CSM/legacy mode blocks it.
- **MBR-partitioned disk.** Secure Boot and UEFI need GPT partitioning; MBR disks fail the chain.
- **Unsupported CPU.** Microsoft's CPU list excludes processors older than 8th-gen Intel / Ryzen 2000 (with narrow exceptions).
- **Less than 4GB RAM or 64GB storage.** Rare on modern laptops, but the check enforces it.

## How to fix it

Work through these in order — each step clears one requirement.

### Fix 1: Run the PC Health Check to identify the exact blocker

Don't guess; get the specific failure.

1. Download the **PC Health Check** app from Microsoft's [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Install it, open it, and click **Check now** in the Windows 11 section.
3. Click **See all results** to list exactly which requirements fail — TPM, Secure Boot, processor, RAM, or storage.
4. Write down the failures; the fixes below address each one.

### Fix 2: Enable TPM 2.0 in BIOS

The fix for the most common failure.

1. Restart and enter BIOS/UEFI setup — usually **F2**, **Del**, or **Esc** at the logo (HP: **F10**, Lenovo: **F2** or Novo button, Dell: **F2**).
2. Find the security section and look for **TPM**, **Intel PTT** (Intel CPUs), **AMD fTPM** (AMD CPUs), or **Trusted Computing**.
3. Set it to **Enabled** (not just "Available" — on some BIOSes TPM shows as present but disabled).
4. Save with **F10** and exit.
5. Back in Windows, verify: press **Win + R**, type `tpm.msc`, press **Enter** — it should report TPM 2.0 ready for use.

### Fix 3: Enable Secure Boot

The second most common blocker.

1. Re-enter BIOS setup.
2. Find **Secure Boot** (usually under **Security** or **Boot** tabs) and set it to **Enabled**.
3. If Secure Boot is greyed out, first disable **CSM / Legacy Boot** and ensure **Boot Mode** is set to **UEFI** (not Legacy).
4. Save and exit, then re-run the PC Health Check.
5. Note: switching from Legacy to UEFI won't boot an MBR-partitioned Windows — check Fix 4 first if your disk is MBR.

### Fix 4: Convert MBR to GPT if needed

Required when the disk uses the old MBR layout.

1. In Windows, open an admin **Terminal** and run: `diskpart`, then `list disk`. If your system disk shows no asterisk under **GPT**, it's MBR.
2. Exit diskpart (`exit`), then run Microsoft's converter:
   `mbr2gpt /validate /disk:0 /allowFullOS`
   (Replace 0 with your system disk number if different.)
3. If validation succeeds, run: `mbr2gpt /convert /disk:0 /allowFullOS`
4. Restart, enter BIOS, set boot mode to **UEFI**, enable **Secure Boot**, and boot — Windows should start normally on the converted disk.

### Fix 5: Check your CPU against Microsoft's list

The one requirement you can't change with settings.

1. Find your exact CPU: **Settings > System > About** shows the processor name.
2. Compare it against Microsoft's supported processor lists on the [Windows support hub](https://support.microsoft.com/en-us/windows).
3. 8th-generation Intel Core and AMD Ryzen 2000-series (and newer) are supported; older chips officially aren't.
4. If your CPU is on the list but the check still fails, the issue is TPM/Secure Boot configuration — revisit Fixes 2 and 3.

### Fix 6: Verify RAM and storage meet minimums

Quick to check, occasionally the blocker on budget models.

1. **Settings > System > About** shows installed RAM — you need 4GB minimum (8GB+ recommended for actual usability).
2. Open **File Explorer > This PC** and confirm the system drive has 64GB+ total capacity.
3. If RAM is the issue on an upgradeable laptop, adding a stick is cheap — but most laptops failing here fail on TPM instead, so double-check Fix 2.

### Fix 7: Update the BIOS

Old BIOS versions sometimes hide TPM options or misreport readiness.

1. Visit your laptop maker's support page for your exact model and check for a newer BIOS.
2. Install it with AC power connected and all apps closed — do not interrupt.
3. Re-enter BIOS afterward: TPM and Secure Boot options sometimes appear only after the update.
4. Re-run the PC Health Check to confirm everything passes.

### Fix 8: Re-run the check and start the upgrade

Confirm all green, then proceed.

1. Open **PC Health Check** and click **Check now** again — every item should pass.
2. Go to **Settings > Windows Update** — the Windows 11 upgrade offer should now appear.
3. Back up important files before upgrading (an external drive or cloud backup), then start the installation.
4. The upgrade keeps your files and apps; allow 1–2 hours for it to complete.

## Closing

"This PC can't run Windows 11" is a configuration checklist, not a verdict on your laptop — TPM 2.0 and Secure Boot toggles in BIOS resolve it for the vast majority of machines. Work the requirements one at a time with the PC Health Check confirming each fix, and only the CPU requirement is truly non-negotiable. Once every check is green, the upgrade itself is the easy part.
