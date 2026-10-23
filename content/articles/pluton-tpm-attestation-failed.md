---
title: "How to Fix Pluton TPM Attestation Failures on Windows 11 AI PCs"
slug: pluton-tpm-attestation-failed
date: 2026-10-23
categories: ["ai-pc"]
tags: ["pluton", "tpm", "attestation", "windows hello", "copilot+ pc", "security"]
description: "Fix Pluton TPM attestation failures on Windows 11 AI PCs with step-by-step fixes for TPM provisioning, Windows Hello, BitLocker, and firmware updates."
thumbnail: "/images/thumbs/pluton-tpm-attestation-failed.webp"
faqs:
  - q: "What does 'attestation failed' mean on a Pluton TPM?"
    a: "It means Windows asked the Pluton security chip to cryptographically prove the device's boot integrity, and the proof failed. The TPM may be unprovisioned, its endorsement key may not match what the health service expects, or firmware may be stale."
  - q: "Can a Pluton attestation failure break Windows Hello?"
    a: "Yes. Windows Hello PINs and biometric credentials are backed by the TPM on Copilot+ PCs, so an unprovisioned or corrupted TPM blocks new credential creation and can prevent sign-in with existing ones until it is fixed."
  - q: "Does clearing the TPM delete my files?"
    a: "Clearing the TPM deletes keys stored inside it, not your documents — but it invalidates BitLocker-protected drives and Windows Hello credentials. Back up your BitLocker recovery key and remove the TPM-based protection before clearing."
  - q: "Will a BIOS update fix attestation failures?"
    a: "Often. Pluton firmware ships inside the laptop's BIOS/UEFI updates, and several vendors have fixed attestation bugs through firmware alone. If attestation started failing after a platform update, a BIOS update is one of the first things to check."
---

You open Windows Security and see a yellow warning — "Attestation is not supported" or a health-attestation report that says the device failed to attest. Windows Hello stops accepting your PIN, BitLocker wants a recovery key it never asked for before, and Conditional Access at work refuses your login. Everything still boots, but the trust layer underneath Windows 11 is broken.

On Copilot+ PCs and modern AI laptops, Microsoft's Pluton security processor is built directly into the Snapdragon, Intel Core Ultra, or AMD Ryzen AI silicon instead of living as a separate TPM chip. Attestation — the process where the TPM cryptographically vouches that the machine booted untampered — depends on Pluton being provisioned correctly, its endorsement keys being intact, and the firmware matching what Microsoft's attestation service expects.

This guide walks you through the attestation chain in the right order: checking the TPM's state first, re-provisioning it safely, repairing Windows Hello and BitLocker fallout, and updating Pluton firmware when the hardware itself is the problem.

## Why this happens

- **TPM never provisioned after a reset or board replacement:** A Windows reset, motherboard replacement, or firmware flash can leave Pluton in a factory-fresh, unprovisioned state that cannot attest until it is initialized.
- **Corrupted endorsement or attestation keys:** The Endorsement Key (EK) and Attestation Identity Key (AIK) can become invalid after a failed firmware update or a partial TPM clear, causing every attestation request to fail signature checks.
- **Outdated Pluton firmware:** Vendors ship Pluton firmware inside BIOS/UEFI updates; running an old version against newer Windows attestation requirements produces a mismatch failure.
- **Secure Boot disabled or tampered boot chain:** Attestation measures the boot path — if Secure Boot is off or a boot component changed, the TPM's measurements will not match the expected values.
- **Conflicting third-party security software:** Some disk-encryption or endpoint agents fight Windows over TPM ownership, breaking the provisioning state mid-flight.
- **Windows Hello credential corruption:** Sometimes the TPM itself is healthy but the Hello key containers are damaged, which surfaces as an attestation-style failure in Windows Security.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the TPM's actual state before doing anything

Pluton problems look like Windows problems, and Windows problems look like Pluton problems. Two built-in tools tell you exactly which one you have in under a minute.

1. Press **Win + R**, type `tpm.msc`, and press Enter — this is the definitive TPM status screen.
2. Under **Status**, a healthy TPM reads "The TPM is ready for use." Note anything else: "not ready," "not provisioned," or a red error.
3. Under **TPM Manufacturer Information**, confirm Pluton shows as the manufacturer (or your SoC vendor) — if the TPM is missing entirely, skip to Fix 5 (firmware).
4. Open **Windows Security > Device security > Security processor details** and read the **Attestation** line — it will say Ready, Not ready, or Not supported.
5. Run `Get-Tpm` in an elevated PowerShell to cross-check: `TpmReady` and `TpmPresent` should both be True. If the processor info is confusing, [checking system info for what your NPU and security hardware actually report](/articles/msinfo32-npu-not-listed/) is the same diagnostic habit applied to the rest of the platform.

### Fix 2: Re-provision the TPM without clearing it

If the TPM is present but "not ready," it usually just needs Windows to complete provisioning — the EK certificate and storage root key hierarchy get set up without destroying existing keys.

1. In `tpm.msc`, open the **Action** menu and choose **Prepare the TPM** — this restarts provisioning against the Pluton chip.
2. Restart the laptop when prompted; Pluton completes provisioning during early boot.
3. After sign-in, reopen `tpm.msc` and confirm the status now reads "The TPM is ready for use."
4. Recheck **Windows Security > Device security** — the attestation warning should clear within a few minutes as Windows re-registers with the attestation service.
5. If status is still not ready after the reboot, do not repeat blindly — move to Fix 3, because a failed prepare usually means the keys themselves are corrupt.

### Fix 3: Clear the TPM safely and re-provision from scratch

When provisioning fails or keys are corrupt, the TPM must be cleared. This deletes keys inside the TPM — so protect BitLocker and Hello first, or you will lock yourself out of your own drive.

1. Back up your BitLocker recovery key: open an elevated Command Prompt and run `manage-bde -protectors -get C:`, then save the 48-digit key somewhere off this machine.
2. Suspend BitLocker temporarily with `manage-bde -protectors -disable C:` so the clear does not trigger recovery mode.
3. Go to **Settings > Accounts > Sign-in options** and note your Windows Hello PIN — you will recreate it after the clear, the same recovery flow you would use when [a Hello PIN stops working for Recall](/articles/recall-pin-windows-hello-required/).
4. In `tpm.msc`, choose **Action > Clear TPM**, confirm, and let the machine restart into the UEFI confirmation screen — accept the clear there.
5. After Windows boots, the TPM provisions automatically; re-enable BitLocker protectors (`manage-bde -protectors -enable C:`) and recreate your Hello PIN.
6. Verify attestation reads Ready in Windows Security and `Get-Tpm` shows `TpmReady: True`.

### Fix 4: Repair Secure Boot and the measured boot chain

Attestation measures every link of the boot chain, so a disabled or misconfigured Secure Boot makes a healthy TPM report failure. This fix restores the measurements attestation expects.

1. Open `msinfo32` and check the **Secure Boot State** line — it must read **On**, not Off or Unsupported.
2. If it is Off, restart into UEFI firmware settings (Settings > Recovery > Advanced startup > Troubleshoot > UEFI Firmware Settings).
3. Set **Secure Boot** to Enabled and **TPM Device / Pluton** to Enabled if either is off; do not change the Secure Boot mode from Standard unless you know why.
4. Save, boot into Windows, and run `Confirm-SecureBootUEFI` in elevated PowerShell — it should return True.
5. Recheck the attestation status in Windows Security; with the boot chain intact, the TPM's measurements should now validate.

### Fix 5: Update the BIOS/UEFI to refresh Pluton firmware

Pluton firmware is bundled with the system BIOS, and vendors have shipped attestation fixes through BIOS updates on all three Copilot+ platforms — this is the hardware-side repair when software provisioning keeps failing.

1. Identify your exact model in **Settings > System > About**.
2. Download the newest BIOS/UEFI from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support — read the release notes for any mention of Pluton, TPM, or attestation.
3. Connect AC power and close all apps, then run the updater — do not interrupt it for any reason.
4. After the update and reboot, Pluton re-initializes; open `tpm.msc` and confirm it is ready and provisioned.
5. Check Windows Security again — post-update, a previously failing attestation typically flips to Ready, the same way stale firmware explains [odd hardware reporting elsewhere on AI PCs](/articles/npu-tops-explained-real-world/).

### Fix 6: Remove the conflicting security agent and re-register attestation

If attestation fails only on corporate or school networks — Conditional Access or Intune compliance reports "device not healthy" — a third-party agent may be fighting Windows for TPM ownership.

1. Check **Settings > Apps > Installed apps** for third-party disk encryption, DLP, or endpoint agents installed alongside the company portal.
2. If you manage the machine yourself, temporarily uninstall the suspect agent and reboot.
3. In `tpm.msc`, run **Action > Prepare the TPM** again so Windows regains clean ownership.
4. Re-enroll in Intune/Company Portal and recheck compliance — attestation-dependent policies should pass.
5. Reinstall the agent only after confirming attestation is green, and if it breaks again, that agent is the culprit — escalate to its vendor with [Microsoft's Windows security documentation](https://support.microsoft.com/en-us/windows) in hand.

## Closing

Pluton attestation failures are a provisioning problem far more often than a hardware problem — check the TPM state, prepare or safely clear it, fix Secure Boot, and update the BIOS before assuming the chip is dead. A green attestation line in Windows Security is what Windows Hello, BitLocker, and Conditional Access all quietly depend on.
