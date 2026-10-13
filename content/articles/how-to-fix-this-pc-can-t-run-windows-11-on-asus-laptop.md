---
title: "\"This PC Can't Run Windows 11\" on an ASUS Laptop? Fix It Here"
slug: how-to-fix-this-pc-can-t-run-windows-11-on-asus-laptop
date: 2026-09-01
categories: ["windows-errors"]
tags: ["windows 11", "tpm", "asus", "upgrade", "compatibility"]
description: "PC Health Check failing on your ASUS laptop? Usually it's TPM or Secure Boot disabled in BIOS. Here's the ASUS-specific fix."
thumbnail: "/images/thumbs/how-to-fix-this-pc-can-t-run-windows-11-on-asus-laptop.webp"
faqs:
  - q: "Why does my ASUS laptop fail the Windows 11 check?"
    a: "Almost always TPM 2.0 or Secure Boot disabled in BIOS — not incapable hardware. ASUS calls TPM 'PTT' (Intel) or 'fTPM' (AMD) in BIOS, which confuses people searching for the word 'TPM'. Enabling the right toggle fixes it in minutes."
  - q: "Where is the TPM setting in ASUS BIOS?"
    a: "Enter BIOS (F2 or Del), switch to Advanced Mode (F7), then: Intel systems — Advanced > PCH-FW Configuration > PTT > Enable. AMD systems — Advanced > AMD fTPM configuration > TPM Device Select > Firmware TPM. Save and exit."
  - q: "Will enabling TPM delete anything?"
    a: "No. Enabling TPM/fTPM doesn't touch your files, Windows installation, or settings. One caution: if you use BitLocker, suspend it before changing TPM settings to avoid a recovery-key prompt on next boot."
  - q: "What if my ASUS CPU is too old?"
    a: "Pre-8th-gen Intel or pre-Ryzen-2000 AMD CPUs aren't officially supported. Check Microsoft's CPU list to be sure — but if the processor is genuinely below the cutoff, the laptop stays on Windows 10, which remains usable."
---

ASUS laptops fail the Windows 11 compatibility check for the same reasons as everyone else's — but ASUS BIOS labels make it harder than it needs to be. The TPM setting isn't called "TPM" on most ASUS boards: Intel systems call it **PTT**, AMD systems call it **fTPM**, and both hide under Advanced menus. Once you know the names, it's a five-minute fix.

Here's the ASUS-specific path from red X to green checkmark.

## Why this happens

- **PTT/fTPM disabled in BIOS**: The number-one ASUS cause. The firmware TPM exists but is off by default on many models, and the Health Check fails you for it.
- **Secure Boot disabled**: Required alongside TPM; often off on machines that shipped with Windows 10 in legacy configurations.
- **BIOS in CSM/Legacy mode**: Secure Boot needs pure UEFI. ASUS boards with CSM enabled block Secure Boot entirely.
- **Outdated ASUS BIOS**: Old firmware may lack fTPM/PTT options or misreport them to the checker.
- **CPU below Microsoft's cutoff**: 7th-gen Intel and older genuinely don't qualify, regardless of settings.
- **PC Health Check not updated**: Old versions of the checker gave vague failures; the current one from Microsoft reports each requirement individually.

## How to fix it

Work through these in order — identify, enable, update, verify.

### Fix 1: See exactly what's failing

Don't change BIOS settings blind.

1. Download the current **PC Health Check** from [Microsoft's Windows 11 page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it, click **Check now**, then **See all results**.
3. Note each failing item: TPM 2.0, Secure Boot, processor, or other. Your fixes target exactly these.

### Fix 2: Enable PTT (Intel) or fTPM (AMD) in ASUS BIOS

The fix for the most common failure — with the ASUS-specific names.

1. Restart and press **F2** (or **Del**) repeatedly to enter BIOS. If you land in EZ Mode, press **F7** for **Advanced Mode**.
2. **Intel ASUS laptops**: go to **Advanced** > **PCH-FW Configuration** > **PTT** > set to **Enable**. (PTT = Intel Platform Trust Technology = firmware TPM 2.0.)
3. **AMD ASUS laptops**: go to **Advanced** > **AMD fTPM configuration** > **TPM Device Select** > **Firmware TPM**.
4. Press **F10** to save and exit.
5. Back in Windows, verify: **Win + R** > `tpm.msc` — it should report "TPM is ready for use," specification version 2.0.
6. **BitLocker caution**: if your drive is BitLocker-encrypted, suspend BitLocker first (**Control Panel** > **BitLocker Drive Encryption** > **Suspend protection**) to avoid a recovery prompt after the TPM change.

### Fix 3: Enable Secure Boot and pure UEFI mode

The second gate, with the ASUS menu paths.

1. Enter BIOS (**F2**/**Del**), **F7** for Advanced Mode if needed.
2. Go to **Boot** > **Secure Boot** > set **OS Type** to **Windows UEFI mode** (this enables Secure Boot).
3. In the same **Boot** menu, check **CSM (Compatibility Support Module)** — set **Launch CSM** to **Disabled**. Secure Boot won't work with CSM on.
4. **Warning**: if your current Windows 10 was installed in Legacy/CSM mode, disabling CSM will stop it booting. Convert first: from an elevated prompt run `mbr2gpt /convert /allowfullos`, *then* disable CSM.
5. **F10** to save, reboot, and re-run PC Health Check.

### Fix 4: Update the ASUS BIOS

Old firmware hides the options you need.

1. Find your exact model (sticker on the bottom or **MyASUS** app).
2. Download the latest BIOS from ASUS support or via the **MyASUS** app's update section.
3. ASUS offers **EZ Flash** (update from within BIOS using a USB stick) and Windows-based updaters — either works. Use AC power, close everything, **never interrupt a BIOS flash**.
4. After updating, re-enter BIOS and re-verify the PTT/fTPM and Secure Boot settings (updates can reset them).
5. Re-run the compatibility check.

### Fix 5: Confirm the CPU genuinely qualifies

If the processor is the failing item, verify rather than assume.

1. Check your CPU: **Settings** > **System** > **About** > **Processor**.
2. Compare with Microsoft's supported lists on the [Windows support site](https://support.microsoft.com/en-us/windows): 8th-gen Intel Core and newer, AMD Ryzen 2000 and newer.
3. Some ASUS gaming laptops with 7th-gen i7-7700HQ chips fail officially — that's a real cutoff, not a settings issue.

### Fix 6: Handle install errors after passing the check

Passing the check but failing the install is a different problem.

1. If setup throws error codes (like 0x80070002), the [ASUS 0x80070002 guide](/articles/how-to-fix-windows-11-install-error-0x80070002-on-asus-laptop/) covers those step by step.
2. Ensure 20GB+ free space and disconnect USB peripherals during setup.
3. The Acer variant of the same install-error walkthrough is at the [Acer 0x80070002 guide](/articles/how-to-fix-windows-11-install-error-0x80070002-on-acer-laptop/) if you're cross-referencing.

### Fix 7: Run the upgrade

With all checks green:

1. Re-run PC Health Check one final time and confirm everything passes.
2. Back up important files (cheap insurance).
3. Use **Settings** > **Update & Security** > **Windows Update** for the official offer, or the Installation Assistant from [Microsoft's Windows 11 page](https://www.microsoft.com/en-us/software-download/windows11).
4. Stay on AC power and don't interrupt the upgrade.

For Dell laptops hitting the same message, the [Dell 0x80070002 install guide](/articles/how-to-fix-windows-11-install-error-0x80070002-on-dell-laptop/) covers the equivalent ground.

## Closing

On ASUS laptops, "This PC can't run Windows 11" is a translation problem as much as a technical one — the setting you need is called PTT or fTPM, not TPM, and it's buried in Advanced Mode. Enable it, enable Secure Boot with CSM off, update the BIOS if the options are missing, and the Health Check turns green. Five minutes in BIOS beats hours of forum-reading every time. One last tip: after the upgrade completes, re-enter BIOS once and confirm PTT/fTPM and Secure Boot are still enabled — major Windows upgrades have been known to leave them on, but verifying takes thirty seconds and guarantees features like BitLocker and Windows Hello keep working exactly as they should on your ASUS machine.
