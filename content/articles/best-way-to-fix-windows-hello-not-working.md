---
title: "Best Way to Fix Windows Hello Not Working"
slug: best-way-to-fix-windows-hello-not-working
date: 2026-10-02
categories: ["windows-errors"]
tags: ["windows-hello", "biometric", "sign-in"]
description: "Windows Hello face, fingerprint, or PIN not working? Fix it fast with this ordered driver and sign-in repair guide."
thumbnail: "/images/thumbs/best-way-to-fix-windows-hello-not-working.webp"
faqs:
  - q: "Why did Windows Hello suddenly stop working?"
    a: "The most common reasons are a broken biometric driver after a Windows update, the Windows Biometric Service failing to start, camera privacy settings blocking the IR camera, or corrupted PIN data. Less often, a TPM issue or a failed update component is responsible."
  - q: "Do I need to re-enroll my face or fingerprint after fixing it?"
    a: "Often yes. Reinstalling biometric drivers or resetting the PIN usually wipes the stored templates, so you'll set up face or fingerprint recognition again afterward. It takes two minutes and your Microsoft account is unaffected."
  - q: "Windows Hello says it's unavailable on this device. What does that mean?"
    a: "It means Windows can't find compatible biometric hardware or its driver. Check Device Manager for missing or warning-marked biometric devices, reinstall the driver from your laptop maker's site, and confirm the hardware is enabled in the BIOS."
  - q: "Can I use Windows Hello without a PIN?"
    a: "No — Windows requires a PIN as the fallback before you can set up face or fingerprint recognition. If the PIN option itself is broken, fix that first (usually by clearing the NGC folder), then add biometrics."
---
# Best Way to Fix Windows Hello Not Working

When **Windows Hello** stops working — face recognition failing, fingerprint sensor dead, or the PIN option greyed out — the cause is almost always one of a handful of things: a driver that broke during an update, a stopped service, a privacy toggle, or corrupted sign-in data. This guide orders the fixes from most to least likely so you're not guessing.

One important note: a PIN is the foundation Hello builds on. If the PIN is broken, face and fingerprint won't work either — so we fix the foundation first, even if the PIN isn't the thing you personally use. Skipping straight to the fingerprint sensor when the PIN database is corrupted is the most common reason these fixes seem to "not work."

If your Hello problems started right after a blue screen, stabilize the crashes first with our [blue screen of death guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) — Hello can't stay fixed on a system that keeps crashing.

## Why this happens

- **Broken biometric driver:** Windows updates frequently replace working fingerprint or IR camera drivers with incompatible ones.
- **Windows Biometric Service not running:** If this service fails to start, every Hello method fails with it.
- **Camera privacy settings:** A toggled-off camera permission silently kills facial recognition.
- **Corrupted PIN data:** The NGC folder holding PIN credentials gets damaged, blocking PIN and everything built on it.
- **TPM problems:** Hello's keys live in the TPM; if it's unprovisioned or its driver is broken, Hello can't initialize.
- **Missing optional features:** The biometric framework components can go missing after major updates.

## How to fix it

Work through these in order — each fix targets the next most likely cause.

### Fix 1: Check camera privacy settings

The quickest win of all, and embarrassingly common after updates that reset permissions.

1. Go to **Settings > Privacy & security > Camera**.
2. Make sure **Camera access** and **Let apps access your camera** are both on.
3. If you use facial recognition, also verify the IR camera isn't disabled in **Device Manager** under **Cameras** or **Imaging devices**.
4. Try Hello again — if it was a privacy toggle, you're done in under a minute.

### Fix 2: Reinstall the biometric drivers

Driver breakage from Windows Update is the single most common cause.

1. Open **Device Manager** (**Win + X**).
2. Expand **Biometric devices**, right-click your fingerprint sensor, and choose **Uninstall device** (tick **Attempt to remove the driver for this device**).
3. Under **Cameras** or **System devices**, do the same for the IR camera if facial recognition is broken.
4. Restart — Windows reinstalls the drivers automatically.
5. If Windows installs a generic driver that doesn't work, download the proper one from your laptop maker's support site, such as [HP support](https://support.hp.com/us-en) or [Lenovo support](https://support.lenovo.com/us/en/), using your exact model number.
6. After reinstalling, check **Settings > Windows Update > Advanced options > Optional updates** — the correct biometric driver is sometimes hiding there rather than in the automatic queue.

### Fix 3: Restart the Windows Biometric Service

A stuck service blocks all Hello methods at once.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **Windows Biometric Service** and double-click it.
3. Set **Startup type** to **Automatic** and click **Start** if it's stopped (or **Restart** if it's running but wedged).
4. Click **OK** and test Hello at the lock screen (**Win + L**) — give the service a few seconds to fully initialize before testing.

### Fix 4: Reset the PIN

Since everything Hello builds on the PIN, a corrupted PIN database breaks all of it.

1. Sign in with your password.
2. Navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC` in File Explorer.
3. Delete the contents of the folder (take ownership if Windows prompts you).
4. Go to **Settings > Accounts > Sign-in options > PIN (Windows Hello)** and click **Set up** to create a fresh PIN.
5. Test the PIN at the lock screen before re-adding biometrics.

### Fix 5: Re-enroll face and fingerprint

With the foundation repaired, rebuild the biometric templates.

1. Go to **Settings > Accounts > Sign-in options**.
2. Remove any existing **Facial recognition** and **Fingerprint recognition** entries first — stale templates conflict with new ones.
3. Set up facial recognition in good, even lighting; look directly at the camera during capture.
4. For fingerprints, enroll the same finger twice at slightly different angles for better recognition.
5. Sign out (**Win + L**) and verify each method works.

### Fix 6: Check the TPM

If Hello still says it's unavailable, the TPM may need attention.

1. Press **Win + R**, type `tpm.msc`, and press **Enter**.
2. The status should read "The TPM is ready for use." If it says otherwise, click **Clear TPM** in the Actions pane (have your BitLocker recovery key ready if you use BitLocker).
3. Restart and let Windows re-provision the TPM.
4. Also check the BIOS/UEFI (**F2**, **F10**, or **Del** at boot depending on brand) to confirm TPM/Security Device is **Enabled**.

### Fix 7: Repair system files and reinstall Hello components

For stubborn cases, repair the OS components Hello depends on.

1. Open an admin Terminal and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Go to **Settings > System > Optional features > View features** and confirm biometric-related features are installed.
3. Check **Settings > Windows Update** for pending updates — Microsoft regularly ships Hello fixes in cumulative updates.
4. As a last resort, create a new local user account and test Hello there; if it works, your original profile's credential store is corrupted and migrating to the new profile is the pragmatic fix.
5. Test Hello in [Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) — if it works there but not in normal mode, a third-party startup program is interfering; disable startup apps in Task Manager to find it. Microsoft documents the full Hello troubleshooting flow on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Windows Hello failures look mysterious but they're almost always mundane: a driver Windows Update broke, a service that didn't start, a privacy toggle, or a corrupted PIN file. Work the list from Fix 1 down and you'll find the culprit quickly — and once Hello is rebuilt on a clean foundation, it tends to stay fixed for good.
