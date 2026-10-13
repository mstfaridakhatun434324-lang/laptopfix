---
title: "SYSTEM_LICENSE_VIOLATION Blue Screen: A Step-by-Step Repair Guide"
slug: how-to-fix-system-license-violation-bsod-step-by-step
date: 2026-10-13
categories: ["windows-errors"]
tags: ["blue screen", "system license violation", "windows 11", "activation", "stop code 0x9a"]
description: "Step-by-step repair guide for the SYSTEM_LICENSE_VIOLATION blue screen: rebuild the license store, fix edition mismatches, and reactivate Windows."
thumbnail: "/images/thumbs/how-to-fix-system-license-violation-bsod-step-by-step.webp"
faqs:
  - q: "What is stop code 0x9A SYSTEM_LICENSE_VIOLATION?"
    a: "Windows' licensing subsystem detected an inconsistency serious enough to crash the system — usually a corrupted license store, a wrong Windows edition for the embedded OEM key, or hardware changes that invalidated the digital license. Your files and license are typically intact."
  - q: "Do I need to buy Windows again after this error?"
    a: "Almost certainly not. The error means verification failed, not that the license vanished. OEM laptops carry the key in firmware, so reinstalling the correct edition reactivates automatically. Retail digital licenses linked to your Microsoft account reactivate via the troubleshooter."
  - q: "Can I fix this without reinstalling Windows?"
    a: "Yes, in most cases. The activation troubleshooter, rebuilding the tokens.dat store, and correcting the edition via an in-place upgrade all work without a clean install. Reinstallation is only the last resort."
  - q: "Why did this happen after a motherboard replacement?"
    a: "The digital license is tied to a hardware hash that includes the motherboard. A new board means a new hash, so the old license doesn't match. If the replacement was done under warranty, the service center should have handled reactivation — contact them or Microsoft support with your proof of repair."
---

Of all the blue screens, SYSTEM_LICENSE_VIOLATION (0x9A) is the one that makes people panic about money — it sounds like Windows is accusing you of piracy. It isn't. It's a verification failure: something in the licensing chain doesn't add up, and Windows crashes rather than run in an indeterminate licensed state. Your files are safe, and in nearly every case your license is still valid too.

This guide is the full step-by-step repair sequence, from the two-minute troubleshooter to the last-resort reinstall. Follow it in order.

## Why this happens

- **Corrupted license token store.** The `tokens.dat` file holding activation data corrupts after disk errors or interrupted updates.
- **Wrong Windows edition installed.** A Home license with Pro installed (or vice versa) fails the firmware-key match on OEM machines.
- **Hardware changes.** Motherboard replacement, or even a BIOS update that changes reported hardware IDs, invalidates the hardware hash.
- **KMS/volume licensing remnants.** Leftover corporate activation on a personal machine conflicts with the OEM digital license.
- **Cloned installations.** Disk images carried from another PC bring licensing data that doesn't match the current hardware.
- **Software Protection service failures.** If `sppsvc` can't start or crashes, licensing checks fail catastrophically instead of gracefully.

## How to fix it

Work through these in order — start with Fix 1 and stop when the blue screens stop.

### Fix 1: Boot to Safe Mode and run the Activation troubleshooter

Start with the built-in repair.

1. If the blue screen blocks normal boot, interrupt startup three times to reach **Automatic Repair**, then **Troubleshoot > Advanced options > Startup Settings > Restart** and press **4** for Safe Mode.
2. Open **Settings > System > Activation**.
3. Click **Troubleshoot** and follow the prompts — accept reactivation with your digital license if offered.
4. Restart normally and verify **Settings > System > Activation** shows **Windows is activated**.
5. If the troubleshooter fails, note the exact error code for later steps.

Brand-specific walkthroughs exist too — for example, our [SYSTEM_LICENSE_VIOLATION guide for HP laptops](/articles/how-to-fix-system-license-violation-bsod-on-hp-laptop/) covers OEM firmware-key recovery in detail.

### Fix 2: Verify and correct the Windows edition

Edition mismatch is the most common root cause.

1. Open **Settings > System > About** and check **Edition**.
2. Compare with what the PC shipped with (check the manufacturer's specs or your purchase receipt — most consumer laptops ship Home).
3. If it doesn't match, download the correct edition from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
4. Run setup and choose **Keep personal files and apps** — this changes the edition without a full wipe in most cases.
5. After the upgrade, check activation; the firmware-embedded OEM key should activate the correct edition automatically.

### Fix 3: Rebuild the licensing token store

Corrupted tokens trigger this exact stop code.

1. Open **Command Prompt as administrator**.
2. Run `net stop sppsvc` to stop the Software Protection service.
3. Go to `C:\Windows\System32\spp\store\2.0` and rename `tokens.dat` to `tokens.old`.
4. Run `net start sppsvc` to restart the service.
5. Run `slmgr /ato` to attempt online activation, then restart.

Windows regenerates the token store. If activation now fails with a specific error (like 0xC004C003), that code identifies the real problem — look it up on the [Windows support site](https://support.microsoft.com/en-us/windows). The update-related variant is covered in our [SYSTEM_LICENSE_VIOLATION after Windows 11 update guide](/articles/how-to-fix-system-license-violation-bsod-after-windows-11-update/).

### Fix 4: Clear KMS and volume-license remnants

Corporate activation leftovers are a classic cause on secondhand machines.

1. Open **Command Prompt as administrator**.
2. Run `slmgr /dlv` and check whether the description mentions **KMS**, **Volume**, or a corporate server.
3. If so, run `slmgr /upk` to uninstall the product key, then `slmgr /cpky` to clear it from the registry.
4. Restart and run `slmgr /ato` to attempt proper OEM or retail activation.
5. Confirm **Settings > System > Activation** shows the correct license type.

### Fix 5: Repair the Software Protection service

If `sppsvc` itself is broken, licensing can't function.

1. Press **Windows + R**, type `services.msc`, and press Enter.
2. Find **Software Protection**, double-click it, and set **Startup type** to **Automatic (Delayed Start)**.
3. Click **Start** if it's stopped.
4. Open an admin terminal and run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth` to repair any corrupted service files.
5. Restart and check activation.

### Fix 6: Use the Microsoft account digital license link

For retail licenses tied to your account.

1. Open **Settings > System > Activation > Troubleshoot**.
2. When the troubleshooter finishes, click **I changed hardware on this device recently** if that option appears.
3. Sign in with the Microsoft account holding your digital license.
4. Select your device from the list and click **Activate**.
5. This transfers the digital license to the current hardware hash — Microsoft's intended path for legitimate hardware changes.

### Fix 7: Clean-install the correct edition (last resort)

When the licensing state is beyond repair, start fresh.

1. Back up all personal files.
2. Download the correct Windows 11 edition from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Create bootable media, boot from it, and install — delete old partitions for a truly clean state.
4. Skip the product key prompt during setup.
5. Connect to the internet afterward; OEM firmware keys and Microsoft-account digital licenses activate automatically.

## Closing

SYSTEM_LICENSE_VIOLATION is a verification problem, not a lost license — and the step-by-step sequence above resolves it without spending money in the vast majority of cases. Match the edition, rebuild the token store, clear any KMS remnants, and let the legitimate license reassert itself. Keep a record of your product key or Microsoft account link once you're activated again, so any future hardware change is a five-minute troubleshooter run instead of another full investigation. The only scenario that genuinely needs human help is a motherboard replacement, where Microsoft support (with your repair documentation) is the right call rather than another reinstall.
