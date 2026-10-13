---
title: "Fix 'This PC Can't Run Windows 11' on Your HP Laptop"
slug: how-to-fix-this-pc-can-t-run-windows-11-on-hp-laptop
date: 2026-10-13
categories: ["windows-errors"]
tags: ["windows 11", "tpm", "secure boot", "hp laptop", "upgrade error"]
description: "HP laptop says 'This PC can't run Windows 11'? Enable TPM 2.0 and Secure Boot in the BIOS, check CPU support, and upgrade without the error."
thumbnail: "/images/thumbs/how-to-fix-this-pc-can-t-run-windows-11-on-hp-laptop.webp"
faqs:
  - q: "Why does my HP laptop say it can't run Windows 11?"
    a: "Almost always because TPM 2.0 or Secure Boot is disabled in the BIOS — not because the hardware is actually too old. HP ships many laptops with TPM present but switched off. The PC Health Check app flags the missing requirement without telling you it's just a BIOS toggle. Enabling both usually clears the error immediately."
  - q: "How do I check if my HP laptop has TPM 2.0?"
    a: "Press **Win + R**, type `tpm.msc`, and press Enter. The TPM Management console shows the specification version — you need 2.0. If it says no TPM found, check the BIOS: on HP laptops it's under **Security > TPM Device** or **TPM State**. Some very old models genuinely lack TPM 2.0, but anything sold after 2016 usually has it."
  - q: "Is it safe to enable Secure Boot on my HP laptop?"
    a: "Yes, for standard Windows installations. Secure Boot is a Microsoft requirement for Windows 11 and doesn't affect normal use. The only exception is if you dual-boot Linux distributions without Secure Boot support — in that case you'd need to manage keys manually. For a Windows-only HP laptop, enabling it is safe and recommended."
  - q: "My CPU isn't on Microsoft's supported list. Can I still upgrade?"
    a: "Officially, no — the installer will block you, and workarounds leave you without guaranteed updates. If your CPU is genuinely unsupported (generally pre-2017 Intel or pre-Zen AMD), the honest answer is that the laptop has reached the end of its Windows 11 road. Focus on keeping Windows 10 secure instead of fighting the installer."
---

Nothing is more frustrating than a laptop that's clearly capable being told "This PC can't run Windows 11." On HP laptops, this message is wrong more often than it's right — the hardware usually qualifies, but a BIOS setting or two is blocking the check.

Windows 11 requires TPM 2.0, Secure Boot, 4GB of RAM, 64GB of storage, and a supported 64-bit CPU. HP laptops from the last several years meet all of these on paper; they just need the right toggles flipped. Here's how to find and fix whatever is actually failing the check.

## Why this happens

- **TPM 2.0 is disabled in the BIOS.** The most common cause on HP laptops — the chip is there, just switched off.
- **Secure Boot is disabled.** Often turned off for a past Linux install or troubleshooting session and never re-enabled.
- **BIOS is in Legacy/CSM mode instead of UEFI.** Windows 11 requires UEFI boot; Secure Boot can't even be enabled in Legacy mode.
- **CPU genuinely unsupported.** Pre-8th-gen Intel and pre-Ryzen AMD chips don't make Microsoft's list, and no setting changes that.
- **Outdated BIOS misreporting capabilities.** Old firmware sometimes fails to expose TPM 2.0 to Windows even when the hardware supports it.
- **PC Health Check app misreading the system.** The checker occasionally flags systems incorrectly, especially right after a BIOS update.
- **Insufficient RAM or storage on paper.** Rare on HP laptops, but 4GB RAM / 64GB storage are hard minimums the installer enforces.

## How to fix it

Work through these in order — the first two fixes resolve the overwhelming majority of HP cases.

### Fix 1: Enable TPM 2.0 in the HP BIOS

This alone fixes most "can't run Windows 11" errors on HP hardware.

1. Restart and press **Esc** repeatedly at the HP logo, then press **F10** to enter BIOS Setup.
2. Go to the **Security** tab and look for **TPM Device**, **TPM State**, or **TPM 2.0**.
3. Set it to **Available** or **On**. On some models it's under **Security > TPM Embedded Security**.
4. Press **F10** to save and exit. Back in Windows, run `tpm.msc` to confirm it now reports specification version 2.0.

### Fix 2: Enable Secure Boot (and UEFI mode)

Secure Boot requires UEFI — both need to be right.

1. Enter BIOS Setup again (**Esc** then **F10**).
2. Go to **Advanced > Boot Options** and make sure **UEFI Boot Mode** is selected (not Legacy).
3. Go to **Security > Secure Boot Configuration** and set **Secure Boot** to **Enable**.
4. If the option is greyed out, you may need to set a BIOS administrator password first — HP locks Secure Boot changes behind one on some models.
5. Save and exit, then re-run the PC Health Check.

### Fix 3: Verify with PC Health Check and the registry

Confirm what Windows actually sees now.

1. Download the PC Health Check app from [Microsoft's Windows support page](https://support.microsoft.com/en-us/windows) and run it.
2. If it still fails, open **System Information** (`msinfo32`) and check **Secure Boot State** and **BIOS Mode** — BIOS Mode must say **UEFI**.
3. If BIOS Mode says Legacy, your Windows installation itself is in Legacy mode. Converting requires `mbr2gpt` — back up first, then run `mbr2gpt /convert /allowfullos` in an elevated prompt before retrying.

### Fix 4: Update the HP BIOS

Old firmware can hide TPM 2.0 from Windows.

1. Check your BIOS version with `msinfo32` under **BIOS Version/Date**.
2. Go to [HP support](https://support.hp.com/us-en), enter your exact model or serial number, and download the latest BIOS.
3. Install it with the charger plugged in, following HP's instructions exactly.
4. After the update, re-enter the BIOS — updates sometimes reset TPM and Secure Boot to defaults, so re-enable them.

### Fix 5: Confirm CPU support

If TPM and Secure Boot are on and it still fails, check the processor.

1. Open **Settings > System > About** and note the processor name.
2. Compare it against Microsoft's official Windows 11 supported-CPU lists (linked from Microsoft's Windows 11 software download page).
3. Intel needs 8th generation or newer; AMD needs Ryzen 2000-series or newer (with a few exceptions). If your CPU is older, the block is legitimate.

### Fix  6: Free up disk space and check RAM

The installer enforces the minimums strictly.

1. Make sure C: has at least 64GB total capacity with 20GB+ free — use **Settings > System > Storage > Cleanup recommendations**.
2. Confirm 4GB+ RAM in **Settings > System > About**.
3. If storage is the only blocker, the real fix is a larger SSD, not settings tweaks.

### Fix 7: Re-run the compatibility check cleanly

Stale results and cached checks cause false failures.

1. Uninstall the PC Health Check app and reinstall the latest version.
2. Restart the laptop (full shutdown, not Fast Startup resume) and run the check again.
3. If it passes now, proceed with the upgrade via **Settings > Windows Update** or the Installation Assistant.

### Fix 8: Use the Installation Assistant as the final test

The assistant performs its own check and is the authority that matters.

1. Download the Windows 11 Installation Assistant from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it — if your fixes worked, it will proceed instead of blocking.
3. If it still blocks on CPU, accept the verdict: that laptop stays on Windows 10, which remains usable with proper security practices.

For HP-specific upgrade paths on other models, see our [Dell variant](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-dell-laptop/) and [Lenovo variant](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-lenovo-laptop/) of this same fix, plus the [step-by-step walkthrough](/articles/how-to-fix-this-pc-can-t-run-windows-11-step-by-step/) for the general case.

## Closing

"This PC can't run Windows 11" on an HP laptop is usually a two-minute BIOS job, not a hardware obituary. Enable TPM 2.0, enable Secure Boot under UEFI, update the BIOS if needed — and if the CPU is genuinely too old, that's useful information too, because it tells you to stop fighting and plan the laptop's next chapter instead.
