---
title: "How to Fix Windows Hello Not Working on Windows 10"
slug: how-to-fix-windows-hello-not-working-on-windows-10
date: 2026-09-18
categories: ["windows-errors"]
tags: ["windows hello", "biometrics", "windows 10"]
description: "Windows Hello broken on Windows 10? Fingerprint or face sign-in failing? Here's the fix sequence that actually works."
thumbnail: "/images/thumbs/how-to-fix-windows-hello-not-working-on-windows-10.webp"
faqs:
  - q: "Why did Windows Hello stop working on Windows 10?"
    a: "The usual cause is a Windows update replacing your manufacturer's biometric driver with a generic one. Corrupted Hello credentials, disabled biometric devices, camera privacy settings, and TPM problems are the other common triggers."
  - q: "I get 'Something went wrong' when setting up Windows Hello. What now?"
    a: "That generic error usually means corrupted credential data or a TPM issue. Remove your PIN and biometric data (Settings > Accounts > Sign-in options), restart, check the TPM with tpm.msc, then set everything up fresh."
  - q: "Does Windows Hello work on Windows 10 without an IR camera?"
    a: "Fingerprint and PIN work without one, but face recognition requires an infrared camera — a standard webcam can't do it. If your laptop only has a regular webcam, fingerprint or PIN are your Hello options."
  - q: "Windows 10 is near end of support. Should I just upgrade?"
    a: "Windows 10's end of support was October 14, 2025, so upgrading to Windows 11 is genuinely worth considering for security. But Hello itself is fully fixable on Windows 10 — don't upgrade just to fix biometrics."
---

Windows Hello on Windows 10 — fingerprint, face, or PIN sign-in — tends to break in one of two ways: it vanishes after an update ("Windows Hello isn't available on this device"), or enrollment fails with a cryptic error. Both are fixable, and the culprit is usually the biometric driver or corrupted credential data rather than the hardware itself.

One note before starting: Windows 10 reached end of support in October 2025. These fixes work fine, but if your laptop supports it, planning a Windows 11 upgrade is smart for security reasons — not required for Hello, just good hygiene.

## Why this happens

- **Update replaced the OEM biometric driver**: Windows Update swaps manufacturer drivers for generics that lack Hello support.
- **Biometric device disabled**: The fingerprint reader or IR camera got disabled in Device Manager.
- **Corrupted Hello credential store**: Damaged PIN or biometric templates.
- **TPM malfunction**: Hello PIN is TPM-backed; TPM errors break enrollment.
- **Camera access disabled**: Privacy settings blocking the camera break face setup.
- **Windows Biometric Service stopped**: The background service Hello depends on isn't running.

## How to fix it

Work through these in order — hardware check, drivers, credentials, TPM.

### Fix 1: Confirm the biometric device is present and enabled

Start with Device Manager, not guesswork.

1. Press **Win + X** > **Device Manager**.
2. Expand **Biometric devices** — your fingerprint reader should be listed without warnings. Check **Imaging devices** for the camera/IR camera.
3. Yellow icon? Right-click > **Update driver**. Down arrow (disabled)? Right-click > **Enable device**.
4. Missing entirely? Check **View** > **Show hidden devices** — a greyed-out entry means Windows sees the hardware but can't start it (driver problem, Fix 2).
5. Truly absent on a laptop that never had a reader? Then Hello biometrics were never available — PIN is your option.

### Fix 2: Reinstall the manufacturer's biometric driver

The single most effective fix for post-update Hello breakage.

1. Identify your laptop's exact model (**Win + R** > `msinfo32` > **System Model**).
2. Download the fingerprint reader and camera drivers from your manufacturer's official support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). Use only the manufacturer's site.
3. In **Device Manager**, uninstall the biometric device, checking **Delete the driver software for this device**.
4. Install the downloaded driver and restart.
5. Check **Settings** > **Accounts** > **Sign-in options** — the Hello options should be available again.
6. Prevent Windows Update from swapping it back with the **Show or hide updates** troubleshooter.

### Fix 3: Remove and re-add PIN and biometrics

Corrupted credential data is fixed by starting over.

1. Go to **Settings** > **Accounts** > **Sign-in options**.
2. Under **Windows Hello PIN**, click **Remove**, then set up a new PIN.
3. Remove **Windows Hello Fingerprint** / **Face** entries, then re-enroll.
4. Enroll fingerprints twice at different angles; for face, ensure even lighting without glare.
5. If you see error `0x80090016` or similar during PIN setup, that's a TPM/container issue — continue to Fix 6.
6. Microsoft's Hello troubleshooting is documented on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 4: Check camera privacy settings

Face recognition needs camera access at the OS level.

1. **Settings** > **Privacy** > **Camera** — ensure **Allow apps to access your camera** is on.
2. On Windows 10, also check **Settings** > **Privacy** > **Camera** > **Allow desktop apps to access your camera**.
3. If your laptop has a physical camera shutter or **Fn** key camera kill-switch, verify it's open — on many models the IR camera shares the shutter.
4. Test the regular webcam in the Camera app — if it doesn't work either, it's a camera driver problem, not Hello-specific.

### Fix 5: Restart the Windows Biometric Service

A stuck service silently disables all biometrics.

1. **Win + R** > `services.msc` > find **Windows Biometric Service**.
2. Set **Startup type** to **Automatic**, and click **Start** if it's stopped. If running, **Restart** it.
3. Also verify **Credential Manager** is running.
4. Retry Hello enrollment.
5. If the service crashes on start, run `sfc /scannow` from an elevated prompt — corrupted system files are the usual cause.

### Fix 6: Fix TPM issues

Hello PIN requires a healthy TPM.

1. **Win + R** > `tpm.msc` — it should say "The TPM is ready for use."
2. If not, enter BIOS and enable TPM (Intel **PTT** / AMD **fTPM**).
3. For persistent TPM errors, back up BitLocker recovery keys first, then **Clear TPM** in `tpm.msc` and re-enroll Hello.
4. After TPM is healthy, redo Fix 3 — old credentials enrolled against a broken TPM won't work.
5. Some older laptops need a BIOS update for TPM 2.0 reliability — check the manufacturer's site.

### Fix 7: Reset Hello via registry (advanced)

When the UI options are greyed out and nothing else works, stale policy/registry state may be blocking Hello.

1. **Win + R** > `regedit`. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System`.
2. If `AllowDomainPINLogon` exists and is 0, set it to 1 (relevant mainly on domain-joined PCs).
3. Check `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI` for corruption — don't delete keys blindly; export the branch first as backup.
4. Alternatively, run an in-place upgrade: mount a Windows 10 ISO (from Microsoft's official software download site) and run setup keeping files and apps. This refreshes the entire Hello stack.
5. Related guides: [Windows Hello on Acer laptops](/articles/how-to-fix-windows-hello-not-working-on-acer-laptop/) and [booting into Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) for driver work.
6. If Hello broke immediately after a specific Windows update, you can also uninstall that update (**Settings** > **Update & Security** > **Windows Update** > **View update history** > **Uninstall updates**) and pause updates while you install the manufacturer's driver — this stops Windows from re-breaking Hello before you've fixed the driver side.

## Closing

Windows Hello on Windows 10 breaks for mundane reasons — a swapped driver, corrupted credentials, a grumpy TPM — and each has a direct fix. Verify the hardware, reinstall the manufacturer's driver, re-enroll from scratch, and check the TPM. It's a 20-minute job in most cases, and you'll be back to one-touch sign-in without typing a password ever again.
