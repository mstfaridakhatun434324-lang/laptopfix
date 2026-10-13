---
title: "\"This PC Can't Run Windows 11\" on a Dell Laptop? Fix It Here"
slug: how-to-fix-this-pc-can-t-run-windows-11-on-dell-laptop
date: 2026-10-06
categories: ["windows-errors"]
tags: ["windows 11", "tpm", "dell", "upgrade", "compatibility"]
description: "PC Health Check says your Dell can't run Windows 11? It's usually TPM or Secure Boot disabled in BIOS. Here's how to enable both."
thumbnail: "/images/thumbs/how-to-fix-this-pc-can-t-run-windows-11-on-dell-laptop.webp"
faqs:
  - q: "My Dell is only a few years old. Why does it say it can't run Windows 11?"
    a: "Because TPM 2.0 or Secure Boot is disabled in BIOS — not because the hardware is incapable. Most Dells from 2018 onward have TPM 2.0 built in; it's just switched off by default on some models. Enabling it takes two minutes in BIOS."
  - q: "What are the actual Windows 11 requirements?"
    a: "64-bit 1GHz+ dual-core CPU (8th-gen Intel / Ryzen 2000 or newer), 4GB RAM, 64GB storage, UEFI with Secure Boot, TPM 2.0, and DirectX 12 graphics. The CPU generation cutoff is the only truly hard requirement — everything else is usually just a BIOS setting."
  - q: "Is it safe to enable TPM and Secure Boot?"
    a: "Yes. They're security features your hardware already supports. Enabling them doesn't delete anything or change how Windows 10 runs. The only caveat: if you dual-boot Linux, check your distro supports Secure Boot first."
  - q: "What if my Dell's CPU is too old for Windows 11?"
    a: "If the CPU predates the cutoff (7th-gen Intel or older), Microsoft doesn't officially support the upgrade. The laptop still runs Windows 10 fine until its end of support, and community workarounds exist — but for a daily driver, staying on a supported OS is the safer choice."
---

Seeing "This PC can't run Windows 11" on a perfectly good Dell is annoying, but in most cases it's a configuration message, not a hardware verdict. Microsoft's PC Health Check flags three things on Dells more than anything else: TPM 2.0 disabled, Secure Boot disabled, or an unsupported CPU. The first two are BIOS toggles. Only the third is a real wall.

Here's how to check which one you're hitting and fix the fixable ones.

## Why this happens

- **TPM 2.0 disabled in BIOS**: The most common Dell-specific cause. The chip is there; the BIOS just has it switched off (often labeled "TPM On," "PTT," or "fTPM").
- **Secure Boot disabled**: Required by Windows 11 and frequently off on machines that shipped with Windows 10 in legacy configurations.
- **BIOS in Legacy/CSM mode instead of UEFI**: Secure Boot requires UEFI boot mode. Some Dells shipped with Legacy ROMs enabled, which blocks it.
- **CPU below the support cutoff**: 7th-gen Intel Core and older (and pre-Ryzen-2000 AMD) aren't on Microsoft's list regardless of settings.
- **Outdated BIOS**: Very old BIOS versions may not expose TPM 2.0 options at all, or report them incorrectly to the Health Check tool.
- **PC Health Check misreading**: Early versions of the tool were notoriously vague; an outdated checker can report failure without saying why.

## How to fix it

Work through these in order — check, enable, update, verify.

### Fix 1: Get the real reason from PC Health Check

Don't guess — the tool tells you exactly what's failing if you look.

1. Download the latest **PC Health Check** app from [Microsoft's Windows 11 page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it and click **Check now**.
3. Click **See all results** — it lists each requirement with a pass/fail. Note exactly which items fail: TPM 2.0, Secure Boot, processor, or something else.
4. Everything below targets the specific failures. Don't change BIOS settings blind.

### Fix 2: Enable TPM 2.0 in Dell BIOS

The fix for the most common failure.

1. Restart and press **F2** repeatedly at the Dell logo to enter BIOS setup.
2. Go to **Security** > **TPM 2.0 Security** (on some models: **Security** > **PTT Security** for Intel Platform Trust Technology).
3. Check **TPM On** and make sure it's set to **TPM 2.0** (not 1.2).
4. On newer Dell BIOS layouts, look under **Security** > **TPM 2.0 Security On** — the exact path varies by model year.
5. **Apply**, then **Exit** (saving changes). The laptop reboots.
6. Back in Windows, verify: press **Win + R**, type `tpm.msc`, press Enter. It should say "TPM is ready for use" with specification version 2.0.

### Fix 3: Enable Secure Boot (and UEFI mode if needed)

The second most common failure, often paired with the first.

1. Enter BIOS with **F2** at the Dell logo.
2. Go to **Secure Boot** > **Secure Boot Enable** and check **Secure Boot Enable**.
3. If the option is grayed out, check **General** > **Boot Sequence** (or **Advanced Boot Options**): set **Boot List Option** to **UEFI**, and uncheck **Enable Legacy Option ROMs**.
4. **Warning**: switching from Legacy to UEFI on a Windows 10 installed in Legacy mode can prevent it booting. If your current Windows was installed in Legacy mode, convert it first with `mbr2gpt /convert /allowfullos` from an elevated command prompt *before* flipping the BIOS setting.
5. Apply, exit, and re-run PC Health Check.

### Fix 4: Update the Dell BIOS

Old BIOS versions hide TPM options or misreport them.

1. Find your Service Tag (sticker on the bottom, or **Win + R** > `cmd` > `wmic bios get serialnumber`).
2. Go to [Dell's support site](https://www.dell.com/support), enter the Service Tag, and check **Drivers & Downloads** > **BIOS**.
3. If a newer BIOS is available, download and run the updater — on AC power, all programs closed, **do not interrupt it**.
4. After the update, re-enter BIOS and verify the TPM and Secure Boot settings from Fixes 2–3 (updates sometimes reset them).
5. Re-run PC Health Check.

### Fix 5: Verify the CPU is actually supported

If the processor is the failing item, settings won't help — but verify before giving up.

1. In PC Health Check's results, confirm the CPU is genuinely the failure (not a misread).
2. Check your CPU model: **Settings** > **System** > **About** > **Processor**.
3. Compare against Microsoft's supported lists on the [Windows support site](https://support.microsoft.com/en-us/windows) — 8th-gen Intel Core (i3/i5/i7/i9-8xxx) and up, AMD Ryzen 2000 and up.
4. Note: some 7th-gen Intel chips (like the i7-7820HQ) got exceptions for specific business laptops — check the list rather than assuming.

### Fix 6: Meet the remaining requirements

RAM, storage, and display are rarely the issue on Dells, but check them.

1. **RAM**: 4GB minimum — **Settings** > **System** > **About** > **Installed RAM**. Most Dells qualify easily.
2. **Storage**: 64GB minimum free-ish space. If you're tight, run **Disk Cleanup** (**Win + S** > `cleanmgr`).
3. If an install fails later with error codes rather than compatibility messages, the [0x80070002 install error guide for Dell](/articles/how-to-fix-windows-11-install-error-0x80070002-on-dell-laptop/) covers those specifically.

For Lenovo models hitting the same message, there's a parallel [install error guide for Lenovo](/articles/how-to-fix-windows-11-install-error-0x80070002-on-lenovo-laptop/).

### Fix 7: Run the upgrade once everything passes

With all checks green, do the upgrade properly.

1. Re-run PC Health Check and confirm every item passes.
2. Back up important files (the upgrade is safe, but backups are free insurance).
3. Go to **Settings** > **Update & Security** > **Windows Update** and look for the Windows 11 offer — or download the Installation Assistant from [Microsoft's Windows 11 page](https://www.microsoft.com/en-us/software-download/windows11).
4. Keep the laptop on AC power throughout the upgrade and don't interrupt it.

## Closing

"This PC can't run Windows 11" on a Dell is a BIOS configuration message about 80% of the time — TPM off, Secure Boot off, or both. Ten minutes in the BIOS setup fixes what the Health Check was complaining about, and the `tpm.msc` verification proves it. Check the CPU honestly, update the BIOS if the options aren't there, and you'll know definitively whether your Dell is upgrading or staying put — no more guessing from a vague error message.
