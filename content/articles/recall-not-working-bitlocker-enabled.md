---
title: "Recall Not Working With BitLocker Enabled? How to Fix It"
slug: recall-not-working-bitlocker-enabled
date: 2026-10-20
categories: ["ai-pc"]
tags: ["recall bitlocker", "recall not working", "troubleshooting", "ai pc", "device encryption"]
description: "Recall refuses to run even though BitLocker is on? Learn why BitLocker configuration blocks Recall and how to set encryption up correctly on your Copilot+ PC."
thumbnail: "/images/thumbs/recall-not-working-bitlocker-enabled.webp"
faqs:
  - q: "Does Recall really require BitLocker?"
    a: "Yes. Recall requires device encryption as a security prerequisite, because it stores sensitive snapshots of your screen locally. On most Copilot+ PCs this means BitLocker with the OS drive encrypted."
  - q: "BitLocker is on but Recall still won't start. Why?"
    a: "Having BitLocker installed is not the same as having it actively encrypting your OS drive. Common gaps include encryption being suspended, only a data drive being encrypted instead of the OS drive, or device encryption being managed by your organization with conflicting settings."
  - q: "Will turning on BitLocker slow down my laptop?"
    a: "On modern Copilot+ PCs with hardware-accelerated encryption, the performance impact is negligible. Most users notice no difference in app speed or battery life once encryption is active."
  - q: "Can I use Recall without any encryption at all?"
    a: "No. Microsoft made device encryption a hard requirement for Recall, and there is no supported way to bypass it. This protects your snapshot history if the laptop is lost or stolen."
---

Recall's most misunderstood requirement is encryption. Many users enable BitLocker, see it listed as active, and are baffled when Recall still refuses to start — or worse, Recall works for a while and then stops with no explanation. The confusion comes from a simple fact: "BitLocker is installed" and "the OS drive is actively encrypted right now" are two different things, and Recall checks the second one.

This matters because Recall stores screenshots of nearly everything you do, so Microsoft made device encryption a non-negotiable prerequisite. Fixing this problem is really about getting encryption into the exact state Recall demands. This guide walks you through the setup step by step.

Before you start, note that encryption issues are just one family of Recall failures. If your snapshots are intact but the app behaves oddly, you might be looking at a different problem, such as a [corrupted Recall database](/articles/recall-database-corrupted-fix/). But if Recall's error or settings page mentions encryption, device encryption, or BitLocker at all, you are in the right place.

## Why this happens

- **Encryption is suspended:** BitLocker can be installed and even "on" while protection is temporarily suspended, which fails Recall's check.
- **Wrong drive encrypted:** Encrypting a data or external drive does not count — Recall requires the OS (system) drive to be encrypted.
- **Device encryption vs. BitLocker mismatch:** Some PCs use the simpler "device encryption" toggle instead of full BitLocker; the toggle must actually be on.
- **Encryption paused mid-process:** If encryption was interrupted at, say, 40 percent, the drive is not fully protected and Recall stays blocked.
- **Group Policy conflicts:** Organization-managed PCs may have policies that disable BitLocker or Recall independently, creating a contradictory state.
- **TPM issues:** BitLocker depends on the TPM chip; if the TPM is disabled in BIOS or malfunctioning, encryption cannot activate.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the OS drive is actually encrypted

The single most common finding is that BitLocker is "on" somewhere that doesn't count. Check the real encryption status of your system drive before anything else.

1. Open File Explorer, right-click the C: drive, and look for a BitLocker status indicator or "Turn on BitLocker" option.
2. If you see "Turn on BitLocker," encryption is not active — click it to begin setup.
3. Alternatively, open an elevated Command Prompt and run `manage-bde -status C:` to see the exact protection status.
4. Confirm the output shows "Protection Status: Protection On" and "Encryption Method" listed, not "Fully Decrypted."
5. If protection shows as suspended, resume it with `manage-bde -protectors -enable C:` and let encryption complete.

### Fix 2: Let encryption finish to 100 percent

Recall checks for complete encryption, not partial. If your drive is stuck partway through encrypting, Recall will keep refusing until progress reaches 100 percent.

1. Check the current encryption percentage with `manage-bde -status C:` in an elevated Command Prompt.
2. If it shows anything below 100 percent encrypted, keep the PC plugged in and powered on.
3. Let the process run — large drives can take one to several hours.
5. Re-run `manage-bde -status C:` to confirm "Percentage Encrypted: 100%," then open Recall.

### Fix 3: Enable device encryption from Settings

On many Copilot+ PCs, the consumer-friendly path is the Device encryption toggle rather than the full BitLocker control panel. If this toggle is off, Recall's requirement is unmet no matter what the BitLocker tools say. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the official steps for turning it on.

1. Open Settings and go to Privacy & security, then Device encryption.
2. If the toggle is off, turn it on and wait for the confirmation that encryption is enabled.
3. If the Device encryption page is missing, your PC may not support it — use the BitLocker control panel path instead.
4. Restart the PC after enabling encryption to ensure all services pick up the new state.
5. Open Recall and check whether it now allows setup.

### Fix 4: Check TPM status in BIOS

BitLocker needs a working TPM to seal its encryption keys. If the TPM was disabled — sometimes after a BIOS update or a manual settings change — BitLocker cannot protect the drive and Recall stays blocked. This is closely related to firmware-level requirements like [Secure Boot errors blocking Recall](/articles/recall-secure-boot-requirement-error/).

1. Restart the PC and enter BIOS/UEFI setup (usually F2, Del, or Esc during boot).
2. Find the security section and look for TPM, PTT (Intel), or fTPM (AMD) settings.
3. Make sure the TPM is enabled, then save and exit.
4. In Windows, run `tpm.msc` to confirm the TPM is ready for use.
5. Re-run BitLocker setup or resume protection, then test Recall again.

### Fix 5: Resolve Group Policy or MDM conflicts

On work or school PCs, an administrator policy may disable BitLocker, device encryption, or Recall itself — and these can contradict each other. You cannot override these as a standard user, but you can identify the conflict and take the right next step.

1. Press Win + R, type `gpedit.msc`, and check Computer Configuration, Administrative Templates for BitLocker and Recall-related policies.
2. Look for any policy set to Disabled for BitLocker Drive Encryption or device encryption.
3. Check Settings, Accounts, Access work or school to see if an MDM policy manages encryption.
4. If you manage the PC yourself, set conflicting policies to Not Configured and restart.
5. If the PC is organization-owned, contact your IT administrator — Recall may be intentionally blocked.

### Fix 6: Back up the recovery key and re-enable cleanly

When BitLocker is in a confused state — partially on, protectors missing, or reporting errors — the cleanest path is to decrypt fully and re-encrypt from scratch. With the recovery key safely stored, this eliminates every ambiguous state at once. Some users chase this problem into unrelated areas, like [Copilot widgets not working](/articles/copilot-widgets-not-working/), but encryption state is almost always the real cause when Recall cites it.

1. In an elevated Command Prompt, run `manage-bde -protectors -get C:` and save the recovery key somewhere safe — not on the same PC.
2. Decrypt the drive with `manage-bde -off C:` and wait for full decryption.
3. Restart the PC, then turn BitLocker back on from the Control Panel BitLocker page.
4. Choose to back up the new recovery key to your Microsoft account or a USB drive.
5. Let encryption reach 100 percent with the PC plugged in.
6. Open Recall and complete setup — it should now pass the encryption check.

## Closing

BitLocker problems with Recall almost always come down to one thing: the OS drive is not fully, actively encrypted at the moment Recall checks. Work through the status verification, finish any partial encryption, confirm the TPM, and clear policy conflicts before assuming anything exotic. Once encryption is genuinely complete, Recall's requirement is satisfied permanently. If your Recall issues persist after encryption is confirmed healthy, the companion guide on [NPU driver error code 43](/articles/npu-driver-error-code-43/) covers the next most common hardware-level blocker on Copilot+ PCs.
