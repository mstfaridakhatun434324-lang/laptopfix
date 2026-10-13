---
title: "\"This PC Can't Run Windows 11\"? Make It Compatible"
slug: how-to-fix-this-pc-can-t-run-windows-11
date: 2026-09-12
categories: ["windows-errors"]
tags: ["this pc can't run windows 11", "tpm 2.0", "secure boot", "compatibility"]
description: "Blocked by 'This PC can't run Windows 11'? Enable TPM 2.0, Secure Boot, and fix every compatibility check step by step."
thumbnail: "/images/thumbs/how-to-fix-this-pc-can-t-run-windows-11.webp"
faqs:
  - q: "Why does my PC fail the Windows 11 compatibility check?"
    a: "The PC Health Check tests CPU generation, TPM 2.0, Secure Boot, RAM (4GB+), storage (64GB+), and UEFI firmware. The overwhelmingly common failures are TPM 2.0 disabled in BIOS and Secure Boot turned off — both are settings, not hardware limits, on most laptops made after 2016. Enable them and re-run the check."
  - q: "How do I enable TPM 2.0 on my laptop?"
    a: "Restart into BIOS/UEFI (F2, Del, or Esc at the logo), find the Security tab, and enable TPM, PTT (Intel), or fTPM (AMD) — the name varies by manufacturer. Save and exit, then verify in Windows with Win+R > tpm.msc, which should report 'TPM is ready for use' with specification version 2.0."
  - q: "Can I install Windows 11 without TPM 2.0?"
    a: "Microsoft documents registry bypasses for clean installs on unsupported hardware, but the PC won't receive full update support and some features (like certain security protections) won't work. The supported path is enabling TPM 2.0 and Secure Boot in BIOS. Only consider bypasses on hardware that genuinely lacks TPM 2.0, understanding the trade-offs."
  - q: "My CPU isn't on the supported list — what now?"
    a: "If the CPU genuinely predates Microsoft's supported generations (generally 8th-gen Intel / Ryzen 2000 and newer), the official upgrade path is blocked. You can continue on Windows 10 (note its support lifecycle), or perform an unsupported install accepting reduced update guarantees. Don't buy a new laptop until you've confirmed TPM and Secure Boot, though — many 'CPU failures' are actually misreported."
---

**"This PC can't run Windows 11"** is the PC Health Check app's verdict, and on laptops it's wrong — or at least fixable — more often than you'd expect. The check tests six things: CPU generation, **TPM 2.0**, **Secure Boot**, 4GB+ RAM, 64GB+ storage, and UEFI firmware. On the vast majority of laptops from 2016 onward, the hardware is fine and the failures are **BIOS settings**: TPM disabled, Secure Boot off, or legacy (CSM) boot mode enabled. Those are ten-minute fixes, not hardware upgrades.

Work the checks in order below, re-running the PC Health Check after each change so you know exactly which fix cleared which requirement. Genuine hardware blocks (too-old CPU, no TPM chip at all) are the last resort conclusion, not the first. For model-specific walkthroughs, see [this PC can't run Windows 11 step by step](/articles/how-to-fix-this-pc-can-t-run-windows-11-step-by-step/) and the [Dell-specific guide](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-dell-laptop/).

## Why this happens

- **TPM 2.0 disabled in BIOS**: The most common failure — the chip exists but is switched off (labeled TPM, PTT, or fTPM).
- **Secure Boot disabled**: Required by Windows 11, often off on machines that shipped with Windows 10 in legacy mode.
- **Legacy/CSM boot mode**: BIOS-mode booting instead of UEFI — Secure Boot can't work without UEFI.
- **CPU below the supported generation**: Genuine block on pre-2017-era processors.
- **Insufficient RAM or storage**: Less than 4GB RAM or 64GB storage fails the check.
- **Outdated PC Health Check app**: Old versions misreport; update the app itself.
- **GPT vs MBR partition style**: MBR disks can't boot UEFI/Secure Boot — conversion may be needed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Update PC Health Check and get the exact failure list

Don't fix blindly — get the itemized report.

1. Download the latest **PC Health Check** app from [Microsoft](https://www.microsoft.com/en-us/software-download/windows11) — old versions misreport TPM and CPU status.
2. Run it and click **Check now**. Expand the results to see exactly which requirements fail.
3. Write down the failing items. TPM and Secure Boot failures = BIOS settings (Fixes 2–3). CPU failure = verify carefully (Fix 5). Storage/RAM = hardware facts.
4. Re-run the check after every fix below to confirm progress.

### Fix 2: Enable TPM 2.0 in BIOS

The fix for the most common failure.

1. Restart and enter **BIOS/UEFI** (**F2**, **Del**, or **Esc** at the logo).
2. Open the **Security** tab and look for **TPM**, **Intel PTT** (Intel laptops), or **AMD fTPM** (AMD laptops). Set it to **Enabled**.
3. Save and exit. In Windows, press **Win + R**, type `tpm.msc`, and confirm it reports "TPM is ready for use" with **Specification Version 2.0**.
4. Re-run PC Health Check. If TPM now passes, you've cleared the biggest hurdle.

### Fix 3: Enable Secure Boot (and UEFI mode)

The second most common failure, often paired with TPM.

1. In **BIOS/UEFI**, find **Secure Boot** (usually under Security or Boot) and set it to **Enabled**.
2. If Secure Boot is greyed out, check **Boot Mode**: it must be **UEFI**, not **Legacy** or **CSM**. Change it to UEFI.
3. Warning: switching Legacy → UEFI on an MBR-partitioned drive will prevent booting until the disk is converted. Check your partition style first: **Disk Management** > right-click the system disk > **Properties** > **Volumes** tab > **Partition style**. If MBR, run `mbr2gpt /convert` from an admin prompt (back up first).
4. Save, exit, and re-run PC Health Check.

### Fix 4: Update the BIOS firmware

Old firmware hides TPM or reports it incorrectly.

1. Find your exact laptop model and download the latest BIOS from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or Lenovo's support site.
2. Run the update on **AC power** with all programs closed. Don't interrupt it.
3. After the update, re-enter BIOS and verify TPM and Secure Boot are still enabled — updates sometimes reset them.
4. Re-run PC Health Check. Firmware updates have cleared "unsupported CPU" misreports on several laptop lines.

### Fix 5: Verify the CPU against the real supported list

Confirm whether the CPU block is genuine.

1. Find your exact CPU: **Settings** > **System** > **About** > **Processor**.
2. Check it against Microsoft's official supported CPU lists on Microsoft's support site — don't trust third-party summaries.
3. If the CPU is genuinely unsupported (pre-8th-gen Intel / pre-Ryzen-2000 era), the official upgrade is blocked. Your options: stay on Windows 10 within its support lifecycle, or do an unsupported install accepting that updates and support aren't guaranteed.
4. If the CPU *is* on the list but the check fails, the failure is a BIOS/firmware reporting issue — update the BIOS (Fix 4) and re-check.

### Fix 6: Free storage and check RAM

The straightforward hardware requirements.

1. Windows 11 needs **64GB+** of storage. Free space: **Settings** > **System** > **Storage** > **Temporary files** > remove what you don't need. Uninstall unused apps.
2. RAM must be **4GB+**. Check **Task Manager** > **Performance** > **Memory** for installed RAM.
3. On laptops with upgradeable RAM/storage, these are cheap fixes — but verify the other requirements first, since there's no point upgrading RAM on a CPU-blocked machine.
4. Re-run PC Health Check after changes.

### Fix 7: Perform the upgrade once all checks pass

Don't let a stale check block you.

1. With PC Health Check fully green, download the **Windows 11 Installation Assistant** from Microsoft's official download page.
2. Run it and follow the prompts — your files and apps carry over.
3. If the assistant still complains after green checks, restart once more (firmware settings sometimes need a full power cycle to register) and retry.
4. After upgrading, verify **Settings** > **Windows Update** works normally — a properly compatible install updates like any other.

## Closing

"This PC can't run Windows 11" is a settings problem far more often than a hardware problem — TPM off, Secure Boot off, legacy boot mode. The ten minutes spent in BIOS resolves the overwhelming majority of laptop failures. Only after TPM 2.0 is confirmed ready, Secure Boot is on, UEFI is active, the BIOS is current, and the check still fails on CPU should you accept the verdict and plan around it rather than through it.
