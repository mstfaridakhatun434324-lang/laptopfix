---
title: "How to Fix \"This PC Can't Run Windows 11\" Error"
slug: how-do-i-fix-this-pc-can-t-run-windows-11
date: 2026-09-22
categories: ["windows-errors"]
tags: ["Windows 11 requirements", "TPM 2.0", "compatibility"]
description: "Blocked by \"This PC can't run Windows 11\"? Check which requirement fails and enable TPM, Secure Boot, or fix the real compatibility issue."
thumbnail: "/images/thumbs/how-do-i-fix-this-pc-can-t-run-windows-11.webp"
faqs:
  - q: "Why does my PC fail the Windows 11 compatibility check?"
    a: "The PC Health Check app tests CPU generation, 4 GB RAM, 64 GB storage, UEFI firmware, Secure Boot capability, and TPM 2.0. On most laptops that fail, the hardware is actually fine — TPM or Secure Boot is simply disabled in the BIOS. The checker tells you which requirement failed; start there before assuming the machine is too old."
  - q: "How do I enable TPM 2.0 for Windows 11?"
    a: "Restart into the BIOS (F2 or Del during boot), find the security or advanced section, and enable TPM — it may be labeled TPM, PTT (Intel), or fTPM (AMD). Save and exit, then verify with tpm.msc in Windows, which should report TPM 2.0 ready. Most laptops from 2017 onward have the hardware; it is just switched off."
  - q: "My CPU isn't on the supported list. Can I still install Windows 11?"
    a: "There are registry workarounds that bypass the CPU check, but Microsoft does not support or recommend them — such installs may not receive updates and can have stability problems. If your CPU is genuinely unsupported, the supported options are staying on Windows 10 (with its end-of-support implications) or upgrading the hardware."
  - q: "Does enabling Secure Boot delete my files?"
    a: "No. Enabling Secure Boot in the BIOS does not touch your files or installed programs. One caveat: if your Windows installation is in Legacy/CSM boot mode rather than UEFI, flipping to UEFI + Secure Boot can prevent booting until the disk is converted from MBR to GPT with the mbr2gpt tool. Check your boot mode first in System Information."
---

"This PC can't run Windows 11" is the gatekeeper message that stops the upgrade before it starts. The PC Health Check app runs through Microsoft's requirement list — CPU, RAM, storage, UEFI, Secure Boot, TPM 2.0 — and if anything fails, you get this message, sometimes with specifics and sometimes infuriatingly vague.

Here is what most people discover: their laptop is perfectly capable, but TPM or Secure Boot is simply turned off in the BIOS. Manufacturers shipped millions of machines with these features disabled by default. The fixes below walk through identifying the actual failed check and enabling what is missing, which resolves the large majority of these blocks.

## Why this happens

- **TPM disabled in BIOS.** The hardware exists but is switched off — the number one cause.
- **Secure Boot disabled or unsupported boot mode.** Legacy/CSM boot instead of UEFI.
- **CPU not on Microsoft's supported list.** Older processors fail the check regardless of capability.
- **Insufficient RAM or storage.** Under 4 GB RAM or 64 GB storage fails outright.
- **Outdated PC Health Check results.** The app sometimes caches old results; re-running after BIOS changes matters.
- **MBR-partitioned system disk.** Legacy partition style incompatible with UEFI/Secure Boot requirements.

## How to fix it

Work through these in order, re-running the compatibility check after each change.

### Fix 1: See exactly which check failed

Do not guess — the checker tells you.

1. Download the **PC Health Check** app from Microsoft's website (linked via [Microsoft Support](https://support.microsoft.com/en-us/windows)) if you do not have it.
2. Run it and click **Check now**.
3. Click **See all results** to expand the full list — note precisely which items show red.
4. The fix for each red item is below; green items need no action.

### Fix 2: Enable TPM 2.0 in the BIOS

The most common fix.

1. Restart and enter the BIOS (**F2** or **Del** during boot; **F10** on many HPs, **F1** or **Enter** then **F1** on Lenovos).
2. Look under **Security** or **Advanced** for **TPM**, **Intel PTT**, or **AMD fTPM** and set it to **Enabled**.
3. Save and exit.
4. In Windows, press `Win + R`, type `tpm.msc`, and confirm **Status** reads "The TPM is ready for use" with specification version 2.0.

### Fix 3: Enable Secure Boot (and UEFI mode)

The second most common fix.

1. In the BIOS, find **Secure Boot** (usually under **Security** or **Boot**) and set it to **Enabled**.
2. Make sure the boot mode is **UEFI**, not **Legacy** or **CSM**.
3. Before switching boot modes, check your current setup: open **System Information** (`msinfo32`) and look at **BIOS Mode** and the disk's partition style in **Disk Management** (GPT vs MBR).
4. If the disk is MBR, convert it first from an admin Command Prompt: `mbr2gpt /validate` then `mbr2gpt /convert` — back up first, as with any disk operation.
5. Save BIOS changes, exit, and re-run the check.

### Fix 4: Update the BIOS

Newer firmware sometimes adds or fixes TPM/Secure Boot support.

1. Check your current BIOS version in **System Information**.
2. Compare with the latest on the manufacturer's site: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
3. Install the update with the charger plugged in; do not interrupt it.
4. Re-enter the BIOS afterward — updates sometimes reset TPM/Secure Boot to defaults — and re-enable as needed.

### Fix 5: Free storage and verify RAM

If the check flags storage or memory:

1. Ensure at least 64 GB total storage with ample free space; run **Disk Cleanup** with system files.
2. Confirm installed RAM in **Settings > System > About** — under 4 GB fails the check.
3. On laptops with upgradeable RAM, adding a stick is cheap and easy.

### Fix 6: Bypass checks only as an informed last resort

For genuinely unsupported CPUs where you accept the risks:

1. Understand the tradeoff: Microsoft may withhold updates and does not support these installs.
2. The documented workaround involves creating the `AllowUpgradesWithUnsupportedTPMOrCPU` registry value — research the current, exact procedure from reputable sources before attempting it.
3. Back up everything first; unsupported installs are harder to recover when they break.

Brand-specific walkthroughs: [can't run Windows 11 on Lenovo](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-lenovo-laptop/), [on Dell](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-dell-laptop/), and the full [step-by-step compatibility guide](/articles/how-to-fix-this-pc-can-t-run-windows-11-step-by-step/). Our [troubleshooting overview](/articles/this-pc-can-t-run-windows-11-troubleshooting/) covers edge cases.

### Fix 7: Check for firmware-level blocks and re-run the checker cleanly

Sometimes the checker itself is the problem, or a firmware quirk hides the TPM.

1. In the BIOS, look for a **TPM Device Selection** option — on some boards it toggles between discrete TPM and firmware TPM, and only one is visible to Windows.
2. If TPM was already enabled but `tpm.msc` shows nothing, try switching between **PTT**/**fTPM** options and rebooting between changes.
3. Uninstall the PC Health Check app, download the latest version fresh, and re-run the check — older builds had bugs that misreported results on some laptops.
4. Run the check while plugged into AC power; a few firmware features report differently on battery.

## Closing

"This PC can't run Windows 11" is usually "this PC *can* run Windows 11 but a BIOS setting says otherwise." Check exactly what failed, enable TPM 2.0 and Secure Boot in UEFI mode, update the BIOS if needed, and re-run the checker — that sequence clears the block for the overwhelming majority of laptops. Only when the CPU itself is genuinely unsupported do you face a real hardware decision, and even then it is worth weighing your options calmly rather than forcing an unsupported install you will regret. When in doubt, the manufacturer's support page for your exact model is the authoritative word on what the board supports.
