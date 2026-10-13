---
title: "Troubleshooting 'This PC Can't Run Windows 11'"
slug: this-pc-can-t-run-windows-11-troubleshooting
date: 2026-09-08
categories: ["windows-errors"]
tags: ["windows 11", "compatibility", "TPM"]
description: "Blocked by 'This PC can't run Windows 11'? Find out exactly which requirement fails and how to fix it — TPM, Secure Boot, CPU, and more."
thumbnail: "/images/thumbs/this-pc-can-t-run-windows-11-troubleshooting.webp"
faqs:
  - q: "What are the actual Windows 11 requirements?"
    a: "A 64-bit 1GHz+ dual-core CPU on Microsoft's supported list, 4GB RAM, 64GB storage, UEFI firmware with Secure Boot, TPM 2.0, DirectX 12 graphics, and a 720p display. The PC Health Check app tells you exactly which of these your machine fails."
  - q: "My PC meets the specs but still fails. Why?"
    a: "Almost always TPM 2.0 or Secure Boot disabled in the BIOS. Many compatible machines ship with TPM off or in 1.2 mode, and Secure Boot off. Enabling both in the BIOS firmware settings resolves the large majority of false failures."
  - q: "Can I install Windows 11 on an unsupported CPU?"
    a: "Microsoft offers registry bypasses for clean installs on unsupported CPUs, but the PC will not receive feature updates reliably and Microsoft warns about potential issues. For a daily-use laptop, staying on supported hardware — or on Windows 10 — is the safer choice."
  - q: "Does enabling TPM erase my data?"
    a: "No. Enabling TPM or Secure Boot in the BIOS does not touch your files. The one caution: if you use BitLocker, have your recovery key handy, because firmware security changes can trigger a BitLocker recovery prompt on the next boot."
---
**"This PC can't run Windows 11"** is one of the more frustrating messages in computing, because it often appears on machines that are perfectly capable. The PC Health Check app flags a failure without always explaining it clearly, leaving you staring at a red X and no path forward.

The message is almost always about one of four things: TPM 2.0, Secure Boot, the CPU support list, or disk partitioning. Each has a concrete fix. Here is how to find your specific failure and resolve it.

## Why this happens

- **TPM 2.0 disabled or absent:** The most common cause. The TPM chip exists but is turned off in BIOS, or set to TPM 1.2 mode.
- **Secure Boot disabled:** Required by Windows 11; often off on machines that shipped with Windows 10 or were custom-built.
- **CPU not on the supported list:** Microsoft requires 8th-gen Intel / Ryzen 2000 or newer (with a few exceptions). Older CPUs fail even if fast enough.
- **Legacy BIOS / MBR disk:** Windows 11 requires UEFI boot mode and a GPT-partitioned system disk.
- **Insufficient RAM or storage:** Less than 4GB RAM or 64GB disk fails the check outright.
- **Outdated PC Health Check app:** Early versions of the checker gave vague or wrong results; the current version names the exact failure.
- **Virtualization-based check quirks:** On some machines the checker misreads firmware settings until the BIOS is updated.
- **A pending BIOS administrator password requirement:** Some firmware refuses to persist TPM/Secure Boot changes until an admin password is set, silently reverting your fix.

## How to fix it

Work through these in order. Most people are done by Fix 3.

### Fix 1: Run the current PC Health Check and read the exact failure

Do not guess — get the precise failing requirement.

1. Download the latest **PC Health Check** app from [Microsoft's Windows 11 page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it and click **Check now**. Expand the result — the current version names the specific failed requirement (e.g., "TPM 2.0 must be supported and enabled").
3. Write down exactly what failed. Everything below targets a specific failure, so this step directs the rest of your work.

### Fix 2: Enable TPM 2.0 in the BIOS

The number-one fix. The TPM is usually present but sleeping.

1. Restart and enter the BIOS/UEFI (**F2**, **F10**, **Del**, or **Esc** depending on manufacturer).
2. Look under **Security**, **Advanced**, or **Trusted Computing** for **TPM**, **TPM Device**, **fTPM** (AMD), or **PTT** (Intel Platform Trust Technology — this is Intel's firmware TPM and counts).
3. Set it to **Enabled** and make sure the version is **2.0**, not 1.2.
4. Save and exit, then re-run PC Health Check. If you use BitLocker, keep your recovery key accessible before changing firmware security settings.

### Fix 3: Enable Secure Boot and UEFI mode

The second most common blocker, often paired with the TPM issue.

1. In the BIOS, find **Secure Boot** (usually under **Security** or **Boot**) and set it to **Enabled**.
2. Confirm the boot mode is **UEFI**, not **Legacy/CSM**. If your disk is MBR-partitioned, Windows 11 setup will still refuse — convert it first: boot into Windows 10, open an elevated Command Prompt, and run `mbr2gpt /validate /disk:0` then `mbr2gpt /convert /disk:0`.
3. Save, exit, and re-run the checker. Model-specific BIOS walkthroughs exist for major brands — for example, our [Lenovo-specific guide](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-lenovo-laptop/) and [HP-specific guide](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-hp-laptop/).

### Fix 4: Update the BIOS

On some machines the checker misreads firmware capabilities until the BIOS is current.

1. Check your BIOS version with `msinfo32` and compare it to the latest on your manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), Lenovo).
2. Install the update with AC power connected. Newer BIOS versions often add proper TPM 2.0 and Secure Boot reporting that the checker needs.

### Fix 5: Verify CPU, RAM, and storage

If TPM and Secure Boot are fine, check the remaining requirements.

1. Press **Win + R**, type `msinfo32`, and confirm your CPU model. Compare it against Microsoft's supported processor list on the Microsoft Support site.
2. Check **Installed Physical Memory** in the same window — you need 4GB minimum.
3. Confirm at least 64GB of free-able disk space. These are hard requirements with no legitimate bypass for upgrades.

### Fix 6: Understand the unsupported-CPU situation

If your CPU genuinely is not on the list but everything else passes, know your options honestly.

1. Microsoft documents a registry method (`AllowUpgradesWithUnsupportedTPMOrCPU`) that permits clean installs on unsupported CPUs — but not in-place upgrades through Windows Update.
2. Expect no guaranteed feature updates and heed Microsoft's warning that issues may occur. For a primary laptop, this is a compromise, not a fix.
3. The clean alternative: stay on Windows 10 (supported with security updates through its lifecycle) or plan a hardware upgrade.

### Fix 7: Re-run the check after each change

Firmware settings sometimes need a full power cycle — not just a reboot — to register.

1. After enabling TPM/Secure Boot, shut the laptop down completely, wait 10 seconds, and power on.
2. Re-run PC Health Check. If it still fails on TPM, re-enter the BIOS and confirm the setting actually saved — some BIOSes revert security changes unless you set an administrator password first.

## Closing

"This PC can't run Windows 11" is usually a firmware configuration problem, not a hardware problem: TPM 2.0 and Secure Boot are sitting disabled in the BIOS on millions of capable machines. Enable them, confirm UEFI/GPT, update the BIOS, and the checker turns green — no new laptop required. Take a photo of your BIOS settings before changing anything; if a setting does not stick, the photo proves what you changed and makes manufacturer support calls dramatically shorter. Keep the photo until the checker passes.
