---
title: "How to Fix \"This PC Can't Run Windows 11\" on an Acer Laptop"
slug: fix-this-pc-can-t-run-windows-11-on-acer-laptop
date: 2026-09-10
categories: ["windows-errors"]
tags: ["windows 11 upgrade", "tpm", "secure boot", "acer laptop"]
description: "Fix the \"This PC can't run Windows 11\" error on your Acer laptop — enable TPM 2.0 and Secure Boot in the BIOS with this step-by-step guide."
thumbnail: "/images/thumbs/fix-this-pc-can-t-run-windows-11-on-acer-laptop.webp"
faqs:
  - q: "My Acer laptop is only a few years old. Why does it say it can't run Windows 11?"
    a: "Because one of Windows 11's hard requirements — TPM 2.0, Secure Boot, or a supported CPU — is disabled or missing in the firmware, not because the hardware is too slow. On Acer laptops the fix is usually flipping two settings in the BIOS, which takes about five minutes."
  - q: "What is TPM and does my Acer have it?"
    a: "TPM (Trusted Platform Module) is a security chip that Windows 11 requires. Virtually every Acer laptop sold since 2016 has TPM 2.0 built in — it is just disabled in the BIOS by default on many models. You enable it; you do not buy anything."
  - q: "Will enabling Secure Boot delete my files?"
    a: "No. Enabling Secure Boot and TPM changes firmware settings only; your files, programs, and Windows installation are untouched. The only setting to be careful with is switching the disk from Legacy/CSM to UEFI boot mode on an old MBR-partitioned drive — check your partition style first."
  - q: "What if my Acer's CPU is not on Microsoft's supported list?"
    a: "Then the official upgrade path is blocked and you should stay on Windows 10 (supported with security updates) or consider a newer machine. Unofficial bypasses exist but leave you without guaranteed updates — not worth it on a daily-use laptop."
---

You ran the PC Health Check app (or the Windows 11 installer), and it told you **"This PC can't run Windows 11"** — even though your Acer laptop feels perfectly fast. Do not take that message at face value. In the large majority of cases it does not mean your hardware is too old; it means a firmware setting is switched off. Windows 11 requires TPM 2.0, Secure Boot, and a supported 64-bit CPU, and Acer ships many laptops with the first two disabled in the BIOS.

The fix is a short trip into the BIOS to flip those settings on. This guide walks you through it step by step for Acer machines. If your actual goal is troubleshooting a different upgrade failure, like [error 0x80070002 during the 24H2 update](/articles/how-to-fix-error-0x80070002-in-windows-11-24h2/), see that guide instead.

A word of reassurance before you touch the BIOS: changing TPM, Secure Boot, and boot mode settings does not affect your files, your installed programs, or your current Windows installation in any way. These are firmware-level security and boot settings — Windows reads them at startup and carries on. The one operation that needs care is the MBR-to-GPT conversion in Fix 3, and even that is a Microsoft-supported, non-destructive process. Millions of people have done exactly this to qualify for Windows 11, and the failure rate is essentially zero when the steps are followed in order.

## Why this happens

- **TPM 2.0 is disabled in the BIOS.** The most common cause on Acer laptops. The chip is there; the firmware just has it switched off.
- **Secure Boot is disabled.** Often disabled alongside TPM, sometimes because a previous owner turned it off for Linux or an older OS.
- **CSM/Legacy boot mode is enabled.** Secure Boot only works in UEFI mode. If the BIOS is set to Legacy/CSM, Secure Boot cannot be enabled.
- **Unsupported CPU.** 8th-gen Intel and Ryzen 2000-series (roughly) and newer are on the list; older CPUs are a hard block no setting can fix.
- **MBR-partitioned system drive.** Switching to UEFI boot requires a GPT-partitioned drive. Older Acer laptops upgraded through the years may still be on MBR.
- **Outdated BIOS.** Early BIOS versions on some Acer models did not expose the TPM toggle properly; a BIOS update adds it.

## How to fix it

Work through these in order — check what is actually missing before changing anything.

### Fix 1: Run PC Health Check to see exactly what failed

1. Download the **PC Health Check** app from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it and click **Check now**.
3. Read the specific failure — it will name TPM, Secure Boot, the processor, or RAM. Fix only what it flags.

### Fix 2: Enable TPM 2.0 in the Acer BIOS

1. Shut down fully, power on, and tap **F2** repeatedly to enter the BIOS/UEFI setup.
2. Go to the **Security** tab and look for **TPM Device**, **TPM Support**, or **Trusted Platform Module**.
3. Set it to **Enabled** (on some models you may need to set a supervisor password first before the option becomes changeable — set one, change the setting, and you can remove the password after).
4. Verify it shows **TPM 2.0** specifically, not 1.2.
5. Press **F10** to save and exit.

### Fix 3: Enable Secure Boot

1. Re-enter the BIOS with **F2**.
2. Go to the **Boot** tab (sometimes under **Security > Secure Boot**).
3. If you see **Boot Mode** set to **Legacy** or **CSM**, change it to **UEFI** first. **Important:** only do this if your system drive is GPT-partitioned. Check in Windows first: open **Disk Management**, right-click the system disk, choose **Properties > Volumes**, and confirm **Partition style** says **GPT**. If it says MBR, convert it first with `mbr2gpt /validate` then `mbr2gpt /convert` from an admin Command Prompt.
4. Set **Secure Boot** to **Enabled**.
5. Press **F10** to save and exit.

### Fix 4: Confirm TPM is active in Windows

1. After rebooting, press **Win + R**, type `tpm.msc`, and press Enter.
2. The TPM Management console should say **"The TPM is ready for use"** and show specification version **2.0**.
3. If it says no TPM found, go back to the BIOS — the setting did not stick, or you enabled the wrong item.

### Fix 5: Update the Acer BIOS

1. If the TPM toggle is missing entirely, your BIOS may predate proper TPM 2.0 support.
2. Open **Acer Care Center** and check for a BIOS update, or look up your exact model on Acer's support site.
3. Run the BIOS update with the charger plugged in and **do not interrupt it**.
4. Re-enter the BIOS afterward — the TPM option often appears after the update.

### Fix 6: Re-run the compatibility check

1. Open PC Health Check again and click **Check now**.
2. If TPM and Secure Boot now pass but the CPU is flagged, your processor genuinely is not on Microsoft's supported list — see the FAQ above for your options.
3. If everything passes, go to **Settings > Windows Update** and the Windows 11 upgrade should be offered, or use the Installation Assistant from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

### Fix 7: Check RAM and storage requirements

1. Windows 11 needs **4 GB RAM** and **64 GB storage** minimum — PC Health Check flags these too.
2. If RAM is the issue on an older Acer, a memory upgrade is cheap and easy on models with accessible slots.
3. If storage is the issue, free up space or clone to a larger SSD.

Note that passing the compatibility check is only half the battle — the upgrade itself can still hit errors like [0x80070057 during installation](/articles/error-code-0x80070057-fix/), so keep this guide handy if the installer throws a code at you.

## Closing

**"This PC can't run Windows 11"** on an Acer laptop is a firmware configuration message far more often than a hardware verdict. Enable TPM 2.0, switch to UEFI, enable Secure Boot, and re-run the check — that five-minute BIOS trip resolves it for most machines sold in the last eight years. Only a genuinely unsupported CPU is a true dead end, and even then, your Windows 10 laptop is not suddenly useless. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the full requirement list if you want to verify anything here.
