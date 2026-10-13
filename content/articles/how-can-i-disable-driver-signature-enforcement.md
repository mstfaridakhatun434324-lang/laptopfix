---
title: "How to Disable Driver Signature Enforcement (and When You Should)"
slug: how-can-i-disable-driver-signature-enforcement
date: 2026-09-02
categories: ["windows-errors"]
tags: ["driver signature", "unsigned drivers", "windows 11"]
description: "Need to install an unsigned driver? Here's how to disable driver signature enforcement safely — temporary vs permanent methods, plus the risks."
thumbnail: "/images/thumbs/how-can-i-disable-driver-signature-enforcement.webp"
faqs:
  - q: "What is driver signature enforcement?"
    a: "It's a Windows security feature that blocks installation of drivers not digitally signed by Microsoft or a trusted publisher. It prevents malware and unstable drivers from loading at the kernel level. Disabling it lets unsigned drivers install — useful for old hardware or development, but it removes an important protection."
  - q: "Is it safe to disable driver signature enforcement?"
    a: "Temporarily, for installing a specific trusted driver, the risk is manageable. Permanently disabling it (via test mode) leaves you exposed to malicious drivers indefinitely and shows a watermark on your desktop. The safest approach: disable it once, install your driver, and reboot — enforcement comes back automatically."
  - q: "Why does Windows say 'Windows requires a digitally signed driver'?"
    a: "You're trying to install a driver whose signature is missing, expired, or from an untrusted publisher. Common with very old peripherals, community-made drivers, and some development hardware. First check the manufacturer's site for an updated signed driver before disabling enforcement."
  - q: "Does disabling it require turning off Secure Boot?"
    a: "For the temporary method (Startup Settings option 7), no. For permanent methods using bcdedit (test signing mode), Secure Boot must be off, since Secure Boot blocks test-signed drivers. Most users should stick with the temporary method."
---
Driver Signature Enforcement is the bouncer at Windows' kernel door: no valid digital signature, no entry. Usually that's exactly what you want — until you need to install a legitimate unsigned driver for old hardware, a development board, or a niche device whose maker never got their driver signed. Then you need to get past the bouncer without firing him permanently.

This guide covers the safe temporary method first (recommended for nearly everyone), then the persistent methods with their trade-offs. For the closely related per-laptop walkthrough, see [disabling driver signature enforcement on laptops](/articles/how-to-disable-driver-signature-enforcement-on-laptop/). If you're disabling enforcement to troubleshoot a flagged driver, our [Driver Verifier IOManager violation guide](/articles/how-to-fix-driver-verifier-iomanager-violation-step-by-step/) explains how Verifier catches bad drivers.

## Why this happens

- **Old hardware, unsigned drivers:** Perfectly good printers, scanners, and lab equipment from the 2000s whose vendors never signed modern drivers.
- **Community or open-source drivers:** Hobbyist drivers that work fine but lack paid code-signing certificates.
- **Development and test hardware:** Custom boards and prototypes during driver development.
- **Expired certificates:** Old-but-legitimate drivers whose signatures Windows no longer trusts.
- **Corrupted driver signature:** Disk corruption damaging a signed driver's catalog file, making it appear unsigned.
- **Stricter policies in recent Windows 11 builds:** Newer releases tightened signature requirements, so drivers that installed fine years ago can suddenly get blocked after an upgrade.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as your driver installs.

### Fix 1: Temporarily disable enforcement via Startup Settings (recommended)

Disables enforcement for one boot only — the safest method. Enforcement returns on the next restart.

1. Open **Settings** > **System** > **Recovery**.
2. Under **Advanced startup**, click **Restart now** and confirm.
3. Choose **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
4. When the menu appears, press **7** (or **F7**) for **Disable driver signature enforcement**.
5. Windows boots with enforcement off — install your unsigned driver now. If the installer needs multiple reboots, you'll have to repeat this each time, so prefer installers that finish in one pass.
6. Restart normally afterward; enforcement is automatically back on, while your installed driver keeps working.
7. Verify: open **Device Manager**, find the device, and confirm it's working without a warning icon.

### Fix 2: Disable enforcement from an admin Command Prompt (one boot)

A quicker route to the same temporary disablement.

1. Open an **administrator Command Prompt**.
2. Run `shutdown /r /o /f /t 0` — this reboots straight into the Advanced Startup menu.
3. Choose **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **7**/**F7**.
4. Install your driver, then restart normally to restore enforcement.

### Fix 3: Check for a signed driver first

Before disabling anything, make sure you actually need to.

1. Visit the hardware manufacturer's website and look for a newer driver — many "unsigned" problems are just outdated downloads.
2. In **Device Manager**, try **Update driver** > **Search automatically for drivers**; Windows Update sometimes carries signed versions.
3. Check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for driver-signing policy changes affecting your device.
4. Only proceed with disabling enforcement if no signed driver exists anywhere.

### Fix 4: Enable Test Mode for development (persistent, with watermark)

For developers who need enforcement off across reboots. Requires Secure Boot to be off.

1. Enter BIOS/UEFI and disable **Secure Boot** (test-signed drivers won't load with it on).
2. Open an **administrator Command Prompt**.
3. Run `bcdedit /set testsigning on`.
4. Restart — you'll see a **Test Mode** watermark on the desktop confirming the state.
5. Install and test your drivers freely across reboots.
6. When done, run `bcdedit /set testsigning off`, re-enable Secure Boot, and restart to return to full protection.

### Fix 5: Disable integrity checks (advanced, not recommended)

An older, blunter method — included for completeness, but Test Mode (Fix 4) is cleaner.

1. With Secure Boot off, open an **administrator Command Prompt**.
2. Run `bcdedit /set nointegritychecks on`.
3. Restart. Enforcement stays off until you run `bcdedit /set nointegritychecks off`.
4. Note: on recent Windows 11 builds this is less reliable than Test Mode and may not work with Secure Boot-adjacent features — prefer Fix 4.

### Fix 6: Sign the driver yourself (best long-term solution)

If you maintain the driver, signing it properly beats disabling enforcement forever.

1. Obtain a code-signing certificate from a trusted Certificate Authority.
2. Sign the driver package with `signtool` from the Windows SDK.
3. For internal/lab use, you can self-sign and deploy your certificate to the machine's Trusted Publishers store via `certmgr.msc`.
4. This is the only approach that's both permanent and secure — worth it if you deploy the driver to multiple machines.

### Fix 7: Check Memory Integrity (HVCI) blocking

Even with signature enforcement off, Memory Integrity can refuse to load unsigned drivers — check it if the install still fails.

1. Open **Settings** > **Privacy & Security** > **Windows Security** > **Device security**.
2. Click **Core isolation details**.
3. If **Memory integrity** is on, toggle it **Off** and restart — then retry the driver install (with enforcement disabled per Fix 1).
4. After the driver is working, turn Memory Integrity back **On** if the driver tolerates it; some unsigned drivers simply can't run under HVCI, in which case leaving it off is the trade-off for using that hardware.
5. Understand the cost: Memory Integrity is a meaningful security boundary, so only leave it off if the device is worth it.

## Closing

Disabling Driver Signature Enforcement is a means to an end, not a lifestyle. For installing one unsigned driver, the temporary Startup Settings method (Fix 1) is all you need: enforcement lapses for a single boot, your driver installs, and protection returns on restart. Reserve Test Mode for genuine development work, and always re-enable Secure Boot when you're done. If Memory Integrity also stood in the way, weigh the device against the protection before leaving it off. And before reaching for any of these, spend five minutes hunting for a signed driver — the safest unsigned driver is the one you never had to install. Enforcement exists because kernel malware is real; borrow the bouncer's keys briefly, then give them back.
