---
title: "The Best Way to Fix \"This PC Can't Run Windows 11\""
slug: best-way-to-fix-this-pc-can-t-run-windows-11
date: 2026-10-08
categories: ["windows-errors"]
tags: ["Windows 11 requirements", "TPM", "installation"]
description: "Fix the \"This PC can't run Windows 11\" error: enable TPM and Secure Boot in BIOS, check CPU compatibility, and upgrade without losing your files."
thumbnail: "/images/thumbs/best-way-to-fix-this-pc-can-t-run-windows-11.webp"
faqs:
  - q: "Why does my laptop say it can't run Windows 11 when it seems fast enough?"
    a: "Windows 11 enforces hardware requirements beyond raw speed: TPM 2.0, Secure Boot capability, and a CPU on Microsoft's supported list. Many capable laptops fail the check simply because TPM or Secure Boot is disabled in the BIOS — enabling both fixes it in minutes without any hardware changes."
  - q: "How do I check which requirement my PC is failing?"
    a: "Download Microsoft's PC Health Check app — it lists exactly which requirements pass and fail. The usual failures are TPM 2.0 (often just disabled in BIOS), Secure Boot (also usually just disabled), or an unsupported CPU generation. The app's report tells you precisely what to fix."
  - q: "Is it safe to bypass the Windows 11 requirements?"
    a: "Microsoft officially discourages it: bypassed installs don't receive guaranteed updates and may break with future builds. For a daily-driver laptop, meeting the real requirements (TPM, Secure Boot, supported CPU) is the safe path. Bypasses are a last resort for secondary or lab machines, not your main computer."
  - q: "Will enabling TPM or Secure Boot delete my files?"
    a: "No. Enabling TPM 2.0 and Secure Boot in the BIOS doesn't touch your files, apps, or Windows installation. The only caveat: if your drive uses BitLocker, have your recovery key handy before changing Secure Boot settings, just in case Windows asks for it on the next boot."
---

"This PC can't run Windows 11" is frustrating precisely because the laptop in front of you often *can* — the check fails on a BIOS toggle, not on actual capability. Before you assume your hardware is too old, work through the real requirements: most failures are TPM or Secure Boot sitting disabled in firmware.

This guide covers the legitimate fixes in order of likelihood, plus how to verify each one. If your goal is a fresh install rather than an upgrade, our [Windows 11 installation failure guide](/articles/what-to-do-if-windows-11-installation-failed/) covers the setup side; Dell owners have a [brand-specific version](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-dell-laptop/) of this check.

## Why this happens

- TPM 2.0 is present but disabled in the BIOS — the single most common cause.
- Secure Boot is disabled or set to a legacy/custom mode.
- The CPU isn't on Microsoft's supported processor list (common on pre-2018 chips).
- The system disk uses MBR partitioning instead of GPT (Secure Boot requires UEFI+GPT).
- Insufficient RAM (under 4 GB) or storage (under 64 GB).
- An outdated BIOS that doesn't expose TPM 2.0 even though the hardware supports it.

## How to fix it

Work through these in order — most people are done by Fix 3.

### Fix 1: Run PC Health Check to identify the failure

Don't guess; get the exact failing requirement first.

1. Download **PC Health Check** from [Microsoft's Windows 11 page](https://www.microsoft.com/en-us/software-download/windows11).
2. Install it, open the app, and click **Check now**.
3. Click **See all results** to expand the full requirement list.
4. Note exactly which items fail — TPM, Secure Boot, CPU, or disk space.
5. Every fix below maps to one of these results, so keep the report open.

### Fix 2: Enable TPM 2.0 in the BIOS

This one toggle fixes the majority of "can't run" reports on otherwise capable laptops.

1. Restart and enter the BIOS/UEFI (usually **F2**, **Del**, or **F10** — varies by brand).
2. Look under **Security**, **Advanced**, or **Trusted Computing** for **TPM**, **PTT** (Intel), or **fTPM** (AMD).
3. Set it to **Enabled** and make sure the version is **2.0**, not 1.2.
4. Save and exit (**F10**), then re-run PC Health Check.
5. If no TPM option exists, update the BIOS (Fix 4) — newer firmware often adds it.

### Fix 3: Enable Secure Boot and switch to UEFI/GPT

Secure Boot requires UEFI mode and a GPT-partitioned system disk.

1. In the BIOS, find **Boot** options and set **Boot Mode** to **UEFI** (not Legacy/CSM).
2. Enable **Secure Boot** under the **Security** or **Boot** tab.
3. In Windows, press **Win + R**, type `msinfo32`, and confirm **BIOS Mode** reads **UEFI**.
4. Check partition style: open **Disk Management**, right-click the system disk, choose **Properties > Volumes** — it must say **GPT**.
5. If it says MBR, convert without data loss using `mbr2gpt /validate` then `mbr2gpt /convert` from an elevated Command Prompt (back up first anyway).

### Fix 4: Update the BIOS firmware

Old BIOS versions may hide TPM 2.0 or lack Windows 11-ready firmware.

1. Note your current BIOS version from `msinfo32` (**BIOS Version/Date**).
2. Visit your laptop maker's support site and check for a newer BIOS for your exact model.
3. Read the release notes for TPM, Secure Boot, or Windows 11 mentions.
4. Install with the charger connected; don't interrupt the process.
5. Re-enter the BIOS after updating and re-enable TPM and Secure Boot if the update reset them.

### Fix 5: Verify CPU compatibility

If TPM and Secure Boot pass but the CPU fails, check Microsoft's list before giving up.

1. Find your exact CPU: **Settings > System > About** shows the processor name.
2. Compare it against Microsoft's [Windows 11 supported processors](https://support.microsoft.com/en-us/windows) list for Intel or AMD.
3. Note that some 7th-gen Intel and 1st-gen Ryzen chips are excluded despite being capable.
4. If your CPU is genuinely unsupported, weigh staying on Windows 10 (supported with ESU options) against new hardware.
5. Don't trust third-party "compatibility" tools — Microsoft's list is the only authority.

### Fix 6: Free up disk space and check RAM

The simplest requirements are the easiest to overlook.

1. Windows 11 needs **64 GB** of free storage for installation — check in **Settings > System > Storage**.
2. Free space with **Disk Cleanup** (`cleanmgr`) and by moving large files to external storage.
3. Confirm at least **4 GB** of RAM in **Settings > System > About**.
4. Laptops with soldered 4 GB RAM meet the minimum but will feel slow — consider whether the upgrade is worth it.
5. Re-run PC Health Check after freeing space.

### Fix 7: Do a clean compatibility re-check

After all BIOS changes, make Windows re-evaluate from scratch.

1. Restart the laptop after every BIOS change — checks read firmware state at boot.
2. Re-run **PC Health Check** and confirm all items pass.
3. Open **Settings > Windows Update** — the Windows 11 upgrade offer should appear within a day.
4. If it doesn't, use the **Installation Assistant** from Microsoft's download page.
5. Back up your files before upgrading, even though the upgrade preserves them.

### Fix 8: Use the Installation Assistant as the final path

Once PC Health Check passes fully, Microsoft's own tool handles the upgrade cleanly.

1. Return to [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Under **Windows 11 Installation Assistant**, click **Download now**.
3. Run the tool and accept the license terms.
4. It re-verifies compatibility, downloads Windows 11, and walks you through the upgrade.
5. After installation, confirm activation in **Settings > System > Activation** and enjoy the new OS.

## Closing

"This PC can't run Windows 11" is usually a configuration problem, not a hardware verdict: enable TPM 2.0, switch on Secure Boot with UEFI/GPT, update the BIOS, and most "incompatible" laptops pass the check immediately. Only the CPU list is non-negotiable — everything else is a toggle waiting to be flipped. Run PC Health Check, fix what's actually failing, and upgrade with confidence.
