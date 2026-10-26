---
title: "TPM Attestation Error on Your ARM Laptop? How to Fix It"
slug: tpm-attestation-arm-error
date: 2026-10-26
categories: ["ai-pc"]
tags: [tpm-attestation, tpm, arm-laptop, windows-hello, security, troubleshooting]
description: "TPM attestation error on your ARM laptop? Fix failed attestation, TPM not ready, and device health errors on Snapdragon Windows 11 PCs with this guide."
thumbnail: "/images/thumbs/tpm-attestation-arm-error.webp"
faqs:
  - q: "What is TPM attestation and why does it fail?"
    a: >
      Attestation is the process where the TPM proves to Windows that the device's boot state is trustworthy. It fails when firmware, TPM measurements, or attestation services are out of sync, often after updates or hardware changes.
  - q: "Can I use Windows Hello without TPM attestation?"
    a: >
      Some features work without attestation, but Windows Hello, BitLocker, and device health checks rely on it for full security. Fixing attestation is better than working around it, since the underlying trust problem affects several features.
  - q: "Does clearing the TPM delete my files?"
    a: >
      No, clearing the TPM does not delete files on your drive. It does remove keys stored in the TPM, which can trigger a BitLocker recovery prompt, so back up your recovery key before clearing it.
  - q: "Is a TPM attestation error a hardware failure?"
    a: >
      Rarely. Most attestation errors are firmware, driver, or service problems. A genuine TPM hardware failure is uncommon and usually shows as the TPM missing entirely from Device Manager and the BIOS.
---
You open Device Security, or try to set up Windows Hello, and Windows reports a TPM attestation error — the device cannot prove its own trustworthiness. Everything else seems fine: the laptop boots, apps run, the internet works. But security features quietly refuse to cooperate, and the error message offers no obvious next step.

Attestation is the TPM's way of vouching for the machine. During boot, the TPM measures firmware and boot components, and Windows compares those measurements against what it trusts. When the measurements, the firmware, or the attestation service disagree, Windows declares the device unattested — and features that depend on that trust, from Windows Hello to BitLocker to device health attestation, start failing in confusing ways.

On ARM laptops, attestation errors most often follow firmware updates, TPM driver changes, or interrupted updates that leave the TPM's stored state inconsistent. The fixes below restore that consistency step by step. If you also use creative apps on the same machine, [Adobe Premiere AI issues](/articles/adobe-premiere-ai-arm-issues/) covers the app side of ARM compatibility, and display-side platform quirks are covered in [Adaptive dimming not working](/articles/adaptive-dimming-not-working-ai/).

## Why this happens

- **Firmware update changed measurements:** New firmware produces different boot measurements, and Windows has not yet recorded them as trusted.
- **TPM driver fault:** A corrupt or outdated TPM driver prevents Windows from communicating with the chip.
- **Attestation service out of sync:** The Windows attestation service holds stale data after an interrupted update.
- **Secure Boot disabled or misconfigured:** Attestation depends on Secure Boot, and disabling it breaks the trust chain.
- **TPM cleared without re-provisioning:** Clearing the TPM without letting Windows re-provision it leaves attestation incomplete.
- **Time and date wrong:** Attestation certificates are time-sensitive, and a badly wrong system clock invalidates them.
- **TPM firmware outdated:** Old TPM firmware may not support the attestation protocols current Windows builds expect.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the TPM is present and ready
Before fixing attestation, confirm the TPM itself is alive. A TPM that is disabled in firmware or missing from Windows produces the same error messages as an attestation failure, but the fix is completely different. This check takes a minute and prevents wasted effort on services when the chip itself is the problem.
1. Press Win + R, type tpm.msc, and press Enter to open the TPM Management console.
2. Check the Status section: it should say "The TPM is ready for use."
3. If the console reports no TPM found, restart into the BIOS and confirm the TPM is enabled.
4. Note the TPM specification version and manufacturer version shown in the console.
5. If the TPM is ready but attestation still fails, continue to the next fixes.
6. If the TPM is missing entirely, update the laptop firmware from the manufacturer's support site.

### Fix 2: Correct the system time and restart attestation services
Attestation certificates expire, and a system clock set months or years wrong makes every certificate look invalid. This is an easy fix that is easy to overlook, because the clock is rarely suspected when security features fail. Syncing the time and restarting the attestation-related services clears a whole class of errors at once.
1. Open Settings, go to Time and language, then Date and time, and enable Set time automatically.
2. Click Sync now to force an immediate time synchronization.
3. Open the Services app and restart the TPM Base Services and related security services.
4. Restart the laptop and check whether the attestation error persists.
5. If the clock keeps drifting after restart, the CMOS battery or firmware time source may need attention.
6. For display features that also depend on platform services, see [Adaptive dimming not working](/articles/adaptive-dimming-not-working-ai/) for the related service checks.

### Fix 3: Update the TPM driver and laptop firmware
The TPM driver translates between Windows and the chip, and an outdated or generic driver can break attestation even when the TPM reports ready. Laptop makers ship firmware updates that include TPM firmware fixes, and these updates are the single most effective remedy for persistent attestation errors on ARM machines.
1. Open Device Manager, expand Security devices, and find the Trusted Platform Module entry.
2. Right-click it, choose Update driver, and let Windows search automatically first.
3. If no update is found, visit the laptop maker's support site for the latest firmware package.
4. Install the firmware update with the laptop plugged in, and do not interrupt the process.
5. After the update, boot into Windows and open tpm.msc to confirm the TPM is still ready.
6. Check the attestation error again — firmware updates resolve the majority of persistent cases.

### Fix 4: Clear and re-provision the TPM
When the TPM's stored state is inconsistent — after an interrupted update or a failed provisioning — clearing it and letting Windows rebuild the keys from scratch is the cleanest fix. The risk is a BitLocker recovery prompt, so back up the recovery key first. Windows re-provisions the TPM automatically on the next boot.
1. Back up your BitLocker recovery key to your Microsoft account and a printed copy.
2. Open Settings, go to System, Recovery, and restart into Advanced startup.
3. Choose Troubleshoot, then UEFI Firmware Settings, and enter the BIOS setup.
4. In the Security section, find the TPM options and choose Clear TPM, then save and exit.
5. At the next boot, enter the BitLocker recovery key if prompted, then sign in normally.
6. Open tpm.msc and confirm the TPM reports ready, then check the attestation error.

### Fix 5: Re-enable Secure Boot and restore firmware defaults
Attestation chains through Secure Boot: if Secure Boot is off, or its keys are in a custom state, the TPM's measurements cannot be trusted. Restoring Secure Boot to its factory state rebuilds the chain from the firmware up, and it is a safe operation on a stock Windows installation.
1. Restart into the BIOS using Advanced startup, as in the previous fix.
2. Find the Secure Boot setting in the Boot or Security section and set it to Enabled.
3. If keys are listed as custom, choose Restore Factory Keys or Reset to default.
4. Save and exit, then boot into Windows and check the attestation status.
5. If Windows fails to boot after changing Secure Boot, return to the BIOS and restore the previous setting.
6. Creative apps that depend on platform security may also recover; if Premiere's AI tools still fail, see [Adobe Premiere AI issues](/articles/adobe-premiere-ai-arm-issues/).

### Fix 6: Reset the attestation and device health state in Windows
If the hardware chain is healthy but Windows still reports an attestation error, the stored attestation state in Windows itself may be stale. Re-registering the device health components and running a system file check repairs corrupted attestation data without touching firmware, and it is the right last step before considering a repair install.
1. Open an elevated Command Prompt and run sfc /scannow to repair system files.
2. Run DISM /Online /Cleanup-Image /RestoreHealth and wait for it to complete.
3. Restart the laptop and sign in, then check Device Security for the attestation status.
4. If the error persists, check Windows Update for pending security updates and install them.
5. As a final software step, use the Reset this PC option keeping your files, which rebuilds Windows state.
6. If on-screen helper features broke at the same time, their fix is separate — see [Click to Do snipping tool not working](/articles/click-to-do-snipping-tool-not-working/).

## Closing

A TPM attestation error sounds severe, but it is usually a mismatch between firmware, drivers, and Windows' stored trust state — not a dying chip. Work through the checks in order: confirm the TPM is ready, fix the clock, update firmware, and clear the TPM only with your BitLocker key in hand. If every software fix fails and the TPM is missing from both Windows and the BIOS, contact the manufacturer, since that points to a hardware fault. Microsoft's TPM documentation is available at the [Windows support hub](https://support.microsoft.com/en-us/windows).
