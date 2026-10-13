---
title: "This PC Can't Run Windows 11? How to Fix It on Any Laptop"
slug: how-to-fix-this-pc-can-t-run-windows-11-reddit
date: 2026-10-01
categories: ["windows-errors"]
tags: ["windows 11 requirements", "tpm", "secure boot"]
description: "Seeing 'This PC can't run Windows 11' on a capable laptop? It's usually just TPM or Secure Boot turned off. Here's how to check and fix each requirement."
thumbnail: "/images/thumbs/how-to-fix-this-pc-can-t-run-windows-11-reddit.webp"
faqs:
  - q: "Why does my laptop say it can't run Windows 11 when it's fast enough?"
    a: "In most cases the hardware is fine — TPM 2.0 or Secure Boot is simply disabled in the BIOS/UEFI firmware. Microsoft's checker flags the machine even though enabling two settings fixes it. Run the PC Health Check app to see exactly which requirement fails, then enable the missing items in firmware settings."
  - q: "What if my CPU isn't on Microsoft's supported list?"
    a: "If the processor itself is unsupported (typically CPUs older than 8th-gen Intel or 2nd-gen Ryzen), Windows 11 will still often install and run — but Microsoft won't guarantee updates. For a daily-driver laptop, an unsupported CPU is the one blocker worth taking seriously, since future updates could stop arriving."
  - q: "Do I need to convert my disk to GPT for Windows 11?"
    a: "Yes, if your drive still uses the older MBR partition style, you'll need GPT. You can convert without losing data using Microsoft's mbr2gpt tool from the recovery command prompt. Back up first anyway — partition conversions are safe but not risk-free."
  - q: "Can I bypass the Windows 11 requirements?"
    a: "Registry bypasses for TPM and CPU checks exist and are widely discussed, but Microsoft warns such installs may not receive updates. The clean path is always to meet the real requirements: enable TPM 2.0 and Secure Boot, use GPT, and confirm CPU support."
---
Nothing stings quite like Microsoft telling you your perfectly good laptop "can't run Windows 11" when you know it should. Before you believe it, know this: the overwhelming majority of these failures come down to two firmware settings — TPM 2.0 and Secure Boot — that are simply switched off. Ten minutes in your BIOS usually solves it.

This guide walks through each requirement, shows you how to check it, and fixes the common blockers one by one. If your goal is a fresh install rather than an upgrade, make sure your disk layout is right too — an MBR disk will block setup even on fully compatible hardware, similar to how a damaged boot setup causes [inaccessible boot device errors](/articles/how-to-fix-inaccessible-boot-device-in-windows-11-24h2/). And if anything goes sideways during the install itself, our [Safe Mode boot guide](/articles/best-way-to-boot-windows-11-in-safe-mode/) shows how to get into Windows with minimal drivers for repairs.

## Why this happens

- **TPM 2.0 disabled in firmware:** Most laptops from 2016 onward have a TPM chip, but it's often turned off by default in BIOS/UEFI settings.
- **Secure Boot disabled:** Many machines ship with Secure Boot off, or users disabled it years ago for a Linux dual-boot and forgot.
- **Disk uses MBR instead of GPT:** Older Windows 10 installs on MBR-partitioned drives fail the check even when everything else passes.
- **Unsupported CPU:** Processors older than Intel 8th gen or AMD Ryzen 2000 generally fail Microsoft's official list.
- **Insufficient RAM or storage:** Less than 4 GB RAM or 64 GB storage fails the check — rare on modern laptops but common on old budget models.
- **Outdated BIOS:** Some early firmware versions don't expose TPM 2.0 properly even when the hardware supports it.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as the checker passes.

### Fix 1: Run the PC Health Check app to identify the exact blocker

Don't guess — Microsoft's own tool tells you precisely which requirement fails.

1. Download the **PC Health Check** app from Microsoft's Windows support pages or the Windows 11 download page.
2. Install it, open it, and click **Check now** under "Introducing Windows 11."
3. Read the results carefully — it names the specific failing item (TPM, Secure Boot, CPU, disk, RAM).
4. Write down every failing item; you'll fix each one in the steps below.

### Fix 2: Enable TPM 2.0 in BIOS/UEFI

The number-one fix. The setting hides under different names depending on your brand.

1. Restart and enter firmware setup — usually **F2**, **Del**, or **Esc** during the logo screen (Lenovo often uses **F1** or **Fn+F2**, HP uses **Esc** then **F10**).
2. Look under **Security** (or **Advanced** > **Trusted Computing**) for **TPM**, **TPM Device**, **Intel PTT**, or **AMD fTPM**.
3. Set it to **Enabled** or **Available**. Note: Intel PTT and AMD fTPM are firmware TPMs — they fully satisfy the requirement.
4. Save and exit (**F10** on most machines).
5. Back in Windows, press **Win + R**, type `tpm.msc`, and confirm it says "TPM is ready for use" with specification version 2.0.

### Fix 3: Enable Secure Boot

The second most common blocker, fixed in the same firmware screen.

1. Re-enter firmware setup as in Fix 2.
2. Find **Secure Boot** under **Security** or **Boot** options.
3. Set **Secure Boot** to **Enabled**.
4. If the option is greyed out, look for **OS Type** or **Boot Mode** and set it to **UEFI** (not Legacy/CSM) — Secure Boot requires UEFI mode.
5. Save, exit, and re-run the PC Health Check.

### Fix 4: Convert MBR to GPT without losing data

If the checker complains about the disk or setup refuses with a partition error, convert the disk style.

1. Back up your important files first.
2. Open an **administrator Command Prompt**.
3. Run `mbr2gpt /validate /disk:0` to check the conversion is possible (use the correct disk number from Disk Management).
4. If validation passes, boot into the **recovery environment** (Settings > System > Recovery > Advanced startup > Restart now).
5. Open **Command Prompt** in recovery and run `mbr2gpt /convert /disk:0`.
6. Reboot, re-enter firmware setup, and make sure **Boot Mode** is **UEFI**.

### Fix 5: Update your BIOS/UEFI firmware

Old firmware sometimes lacks TPM 2.0 options or reports them incorrectly.

1. Find your exact model on your maker's support site: [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
2. Download the latest **BIOS** update and read the release notes for TPM or Windows 11 mentions.
3. Plug into AC power — never update BIOS on battery.
4. Run the updater and let it finish without touching anything.
5. Re-enter setup afterward and re-check the TPM and Secure Boot options; new options sometimes appear.

### Fix 6: Verify RAM, storage, and CPU

The remaining hard requirements — these you can't toggle, but you should confirm them accurately.

1. Press **Win + R**, type `msinfo32`, and check **Installed Physical Memory** (needs 4 GB+) and **Processor**.
2. Open **Settings** > **System** > **Storage** to confirm 64 GB+ total capacity.
3. Compare your CPU against Microsoft's supported processor list — search your exact model on the support hub.
4. On many laptops RAM and storage are upgradeable; a cheap SSD or RAM stick can turn a failing machine into a passing one.

### Fix 7: Re-run the installer from fresh media

Once every check passes, don't trust the old failed attempt — start the install clean.

1. Download the Media Creation Tool from Microsoft's Windows 11 download page.
2. Create a fresh USB installer.
3. Boot from the USB and run setup — with TPM, Secure Boot, GPT, and a supported CPU in place, it should sail through.
4. If you're upgrading rather than clean-installing, run `setup.exe` from the USB inside Windows 10 and choose **Keep personal files and apps**.

## Closing

"This PC can't run Windows 11" is a scary message for what is usually a five-minute firmware fix. Enable TPM 2.0 (or Intel PTT/AMD fTPM), switch on Secure Boot in UEFI mode, and convert to GPT if needed — that trio clears the check on the vast majority of laptops made since 2017. Only a genuinely unsupported CPU is a hard stop, and even then it's worth weighing your options before giving up on the machine. Once the checker gives you the green light, install from fresh media and enjoy a clean, fully supported Windows 11.
