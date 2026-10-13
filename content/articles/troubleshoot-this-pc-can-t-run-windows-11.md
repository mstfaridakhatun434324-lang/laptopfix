---
title: "This PC Can't Run Windows 11? How to Diagnose and Fix Every Blocker"
slug: troubleshoot-this-pc-can-t-run-windows-11
date: 2026-09-28
categories: ["windows-errors"]
tags: ["windows 11", "tpm", "secure boot", "compatibility", "upgrade"]
description: "PC Health Check says 'This PC can't run Windows 11'? Find out exactly which requirement fails — TPM, Secure Boot, CPU, or RAM — and fix each one."
thumbnail: "/images/thumbs/troubleshoot-this-pc-can-t-run-windows-11.webp"
faqs:
  - q: "Why does my PC fail the Windows 11 check when it feels fast enough?"
    a: "Raw speed isn't the issue — Windows 11 requires specific hardware features: TPM 2.0, Secure Boot capability, a supported CPU generation, 4 GB of RAM, and 64 GB of storage. A fast 2017 laptop can fail simply because its TPM is disabled in firmware, which takes thirty seconds to fix."
  - q: "Can I enable TPM 2.0 if my laptop doesn't seem to have it?"
    a: "Most laptops from 2016 onward have firmware TPM (fTPM on AMD, Intel PTT) built into the processor — it just ships disabled. Check your BIOS/UEFI security settings for TPM, PTT, or fTPM and turn it on. Only very old machines genuinely lack TPM 2.0 support."
  - q: "Is it safe to bypass the Windows 11 requirements?"
    a: "Bypasses exist but Microsoft warns that unsupported devices may not receive updates, including security updates, and future feature updates can break the install. For a daily-use laptop, meeting the real requirements or staying on Windows 10 is safer than running an unsupported configuration."
  - q: "My CPU is on the supported list but the check still fails — why?"
    a: "The usual culprits are TPM disabled in BIOS, Secure Boot turned off, or the disk using MBR instead of GPT partition style (Secure Boot needs UEFI mode with GPT). The PC Health Check app names the failing item — fix that specific item rather than guessing."
---

"This PC can't run Windows 11" is one of the more frustrating messages in computing, because it rarely tells you the whole story in plain language. The PC Health Check app lists the failing requirements, but many laptops fail for reasons that are settings, not hardware — a disabled TPM, Secure Boot turned off, or a legacy BIOS mode. Before you assume your laptop is too old, you need to know exactly which requirement is failing, because half of the blockers take minutes to fix in firmware settings.

Windows 11's requirements are specific and non-negotiable from Microsoft's side: a 64-bit processor at 1 GHz or faster with 2+ cores from the supported CPU lists, 4 GB of RAM, 64 GB of storage, UEFI firmware with Secure Boot capability, TPM 2.0, a DirectX 12 compatible GPU, and a 720p display. The two that trip up the most laptops are TPM 2.0 and Secure Boot — both features most 2016-and-newer laptops physically have but ship with disabled.

The good news is that the check is deterministic. Each requirement is a yes/no gate, and the PC Health Check app (or the newer compatibility tools) will name every failing gate. Work through them one at a time. And if you're troubleshooting crashes rather than upgrades, virtualization-based features like memory integrity — a common TPM-adjacent setting — are also implicated in crashes like the [HYPERVISOR_ERROR blue screen](/articles/how-to-fix-hypervisor-error-bsod-youtube/).

## Why this happens

- **TPM 2.0 is disabled in firmware**: The most common blocker. The chip (or firmware TPM in the CPU) exists but is switched off in BIOS/UEFI settings, so Windows can't see it.
- **Secure Boot is turned off**: Required for the Windows 11 upgrade path. Many laptops ship with it off, or users disabled it years ago for dual-booting Linux.
- **CPU not on the supported list**: Microsoft supports 8th-gen Intel and newer (plus select 7th-gen) and AMD Ryzen 2000 and newer. Older CPUs fail even if they're fast.
- **Disk uses MBR instead of GPT**: Secure Boot requires UEFI boot mode, and UEFI mode requires a GPT-partitioned system disk. Laptops upgraded from old Windows installs are often still MBR.
- **Insufficient RAM or storage**: Less than 4 GB RAM or 64 GB storage fails the check outright — common on budget laptops with 32 GB eMMC drives.
- **Outdated PC Health Check results**: Sometimes the app caches an old result. Re-running the check after a firmware change shows the real current status.
- **Virtualization-based security conflicts**: On some machines, enabling the required features conflicts with existing virtualization settings, confusing the checker until firmware is updated.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Get the exact failing requirement

Don't guess — read the actual report.

1. Download and run the **PC Health Check** app from [Microsoft's Windows support page](https://support.microsoft.com/en-us/windows).
2. Click **Check now** and expand the results to see every requirement with a pass/fail mark.
3. Write down each failing item. TPM, Secure Boot, processor, and RAM/storage each need a different fix.
4. If everything passes except the check still says no, click **Check now** again — the app sometimes needs a refresh after firmware changes. Reboot first if you changed any BIOS setting.

### Fix 2: Enable TPM 2.0 in BIOS/UEFI

This single change fixes the majority of failures.

1. Restart and enter BIOS/UEFI setup (**F2**, **Del**, or **Esc** — varies by brand; **F2** is common on Dell, **F10** or **Esc** on HP, **F2** or **Fn+F2** on Lenovo).
2. Look under **Security** settings for **TPM**, **TPM 2.0**, **Intel PTT** (Platform Trust Technology), or **AMD fTPM**.
3. Set it to **Enabled** or **On**. On some systems you must also set the TPM version to 2.0 if a 1.2/2.0 toggle exists.
4. Save and exit (**F10**), boot into Windows, and press **Win + R**, type `tpm.msc`, press Enter — the TPM Management console should now show "TPM is ready for use" with specification version 2.0.
5. Re-run the PC Health Check.

### Fix 3: Enable Secure Boot

The second most common blocker, fixed in the same firmware screen.

1. In BIOS/UEFI, find **Secure Boot** under the **Security** or **Boot** tab.
2. Set it to **Enabled**. If it's greyed out, you may need to set an administrator/supervisor password in BIOS first, or switch from Legacy/CSM boot mode to **UEFI** mode.
3. While there, confirm **Boot Mode** is set to **UEFI**, not **Legacy** or **CSM**. Secure Boot cannot function in Legacy mode.
4. Save, exit, and re-run the compatibility check. If the disk is MBR-partitioned, Secure Boot alone won't be enough — continue to Fix 4.

### Fix 4: Convert the disk from MBR to GPT

Required when the system disk predates UEFI adoption.

1. In Windows, open an elevated Command Prompt and run `mbr2gpt /validate /disk:0` to check the disk can be converted (disk 0 is usually the system disk — verify in Disk Management).
2. If validation passes, run `mbr2gpt /convert /disk:0`. This converts the partition scheme without deleting data, but back up first anyway — partition operations always carry some risk.
3. Reboot into BIOS, set boot mode to **UEFI** (disable CSM/Legacy), and enable **Secure Boot** per Fix 3.
4. Boot Windows and confirm it starts normally, then re-run the health check.
5. If validation fails, the disk layout is too unusual for the tool — in that case a clean install with a GPT disk is the path, which means backing up everything first.

### Fix 5: Check RAM and storage against the minimums

Some failures are genuinely hardware.

1. Press **Ctrl + Shift + Esc** to open Task Manager > **Performance** > **Memory** to see installed RAM. If it's under 4 GB, check whether your laptop supports a RAM upgrade — many do via an access panel.
2. Check storage in **Settings** > **System** > **Storage**. Windows 11 needs 64 GB; 32 GB eMMC laptops common in budget models can't qualify.
3. If RAM is soldered and storage can't be expanded, the laptop genuinely can't run Windows 11 — staying on a supported Windows 10 install or using the machine for lighter duties is the realistic call.
4. Don't buy RAM speculatively — confirm the exact compatible module in your manufacturer's manual first.

### Fix 6: Update the BIOS/UEFI firmware

Old firmware sometimes hides TPM or Secure Boot options, or reports them incorrectly.

1. Visit your manufacturer's support page — Dell, HP, or Lenovo — and find your exact model.
2. Check the BIOS version against what's installed (run `msinfo32` and look at BIOS Version/Date).
3. If an update exists, download it and follow the manufacturer's instructions exactly. Keep the laptop plugged into AC power for the entire flash — a power loss mid-update can brick the board.
4. After updating, re-enter BIOS and re-check for TPM and Secure Boot options; updates frequently expose previously hidden settings. Then re-run the health check.

### Fix 7: Decide the honest path for unsupported hardware

If the CPU itself is the blocker, there's no settings fix.

1. Verify the CPU against Microsoft's official supported-processor lists (linked from the Windows support page). If it's genuinely not listed, no firmware toggle changes that.
2. Weigh your options: stay on supported Windows 10, try a Linux distribution, or retire the laptop from Windows duty.
3. Avoid registry bypasses for a machine you depend on — Microsoft states unsupported installs may miss security updates, and troubleshooting an unsupported install is harder because every guide assumes supported hardware.
4. If you do upgrade hardware, prioritize an SSD and sufficient RAM first — those improve the experience more than chasing the newest OS on marginal hardware. For virtualization-related crashes on machines where you toggled these features, see [troubleshooting UNEXPECTED_KERNEL_MODE_TRAP](/articles/troubleshoot-unexpected-kernel-mode-trap/).

## Closing

Most "can't run Windows 11" verdicts are firmware settings, not hardware obituaries — TPM and Secure Boot fixes resolve the majority of cases in under ten minutes. The discipline is to read the actual failing requirement instead of assuming the worst, change one setting at a time, and re-check after each change. If the CPU is the genuine blocker, that's useful information too: it tells you to plan the machine's next chapter deliberately rather than fighting the checker.
