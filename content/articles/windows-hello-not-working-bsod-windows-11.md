---
title: "Windows Hello Not Working After a Blue Screen on Windows 11"
slug: windows-hello-not-working-bsod-windows-11
date: 2026-09-23
categories: ["windows-errors"]
tags: ["windows-hello", "bsod", "biometric-driver"]
description: "Windows Hello stopped working after a blue screen? Repair the biometric driver and sign-in stack with these steps."
thumbnail: "/images/thumbs/windows-hello-not-working-bsod-windows-11.webp"
faqs:
  - q: "Why did a blue screen break Windows Hello?"
    a: "The crash likely corrupted the biometric driver, the Windows Biometric Service state, or the TPM data Hello depends on. It can also leave the sign-in database in an inconsistent state, so Hello's PIN or facial data no longer validates."
  - q: "Will I lose my saved face or fingerprint data?"
    a: "Possibly. Reinstalling the biometric driver or resetting Hello usually requires re-enrolling your face or fingerprint. Your Microsoft account and files are unaffected — only the local biometric templates need recreating."
  - q: "Is my TPM damaged?"
    a: "Rarely. More often the TPM driver or its stored keys are in a bad state after the crash. Clearing the TPM (with your BitLocker recovery key handy) and letting Windows re-provision it fixes most cases."
  - q: "Can I just use a password instead?"
    a: "Yes — your password and PIN (once reset) still work even when Hello's biometrics fail. But since Hello failing after a BSOD often signals driver corruption, it's worth fixing properly rather than ignoring it."
---
# Windows Hello Not Working After a Blue Screen on Windows 11

You reboot after a blue screen, and suddenly **Windows Hello** — your face, fingerprint, or PIN — refuses to work. The timing isn't a coincidence: the crash corrupted something in the biometric or sign-in stack, and Hello is picky about its dependencies.

The fix sequence here is specific to post-crash Hello failures: repair the underlying system damage first, then rebuild Hello's credentials. Don't skip the early system-repair steps — re-enrolling your fingerprint on top of corrupted files just produces a new, confusing failure a day later.

For Hello problems that appear without any crash, start with [Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) to rule out third-party interference, then work through driver and service checks.

## Why this happens

- **Corrupted biometric driver:** The crash damaged the fingerprint sensor or IR camera driver while it was loaded.
- **Broken Windows Biometric Service:** The service that brokers Hello requests can get stuck in a failed state after an unexpected shutdown.
- **TPM data corruption:** Hello's keys live in the TPM; a crash during a write can leave them unusable.
- **Damaged sign-in database:** The NGC folder holding PIN data can be left inconsistent by the crash.
- **Corrupted system files:** Kernel or credential-manager files damaged by the BSOD break the Hello chain.
- **Failed Windows update:** If the blue screen happened mid-update, half-installed biometric components are a common result.

## How to fix it

Work through these in order. Fix the crash damage first (Fixes 1–3), then rebuild Hello itself (Fixes 4–7).

### Fix 1: Repair system files first

Never rebuild Hello on top of corrupted system files — fix the foundation.

1. Open **Terminal (Admin)** from the **Win + X** menu.
2. Run `sfc /scannow` and wait for completion.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and check whether Hello works before continuing — sometimes this alone is enough.

### Fix 2: Reinstall the biometric drivers

The fingerprint reader and IR camera drivers are the most crash-sensitive part of the Hello chain.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Biometric devices**; right-click your fingerprint sensor and choose **Uninstall device**, ticking **Attempt to remove the driver for this device**.
3. Do the same under **Cameras** or **Imaging devices** for the IR camera if you use facial recognition.
4. Restart — Windows will reinstall fresh drivers automatically.
5. If it doesn't, download the drivers from your laptop maker's support site (for example [HP support](https://support.hp.com/us-en)) rather than a generic driver tool.
6. After reinstalling, check **Settings > Bluetooth & devices > Cameras > Privacy** to confirm Windows is allowed to access the camera — a crash can occasionally flip privacy toggles that silently block facial recognition.

### Fix 3: Restart the Windows Biometric Service

A service wedged in a failed state blocks every Hello attempt.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **Windows Biometric Service**, right-click it, and choose **Restart**.
3. Double-click it and set **Startup type** to **Automatic** if it isn't already.
4. Also check the **Dependencies** tab — the service relies on Remote Procedure Call (RPC), and if RPC is stuck, Hello fails with it. Restart RPC from the same services list if needed.
5. Try signing in with Hello again.

### Fix 4: Clear the TPM

If Hello still fails, the TPM's stored keys are probably damaged. Warning: if you use BitLocker, have your recovery key ready first.

1. Open **Windows Security > Device security > Security processor details**.
2. Click **Security processor troubleshooting**, then **Clear TPM**.
3. Restart when prompted; Windows will re-provision the TPM automatically.
4. You'll need to set up your PIN and biometrics again afterward.

### Fix 5: Reset the PIN via the NGC folder

A corrupted PIN database blocks Hello even when biometrics are fine.

1. Sign in with your password.
2. Open File Explorer and navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC`.
3. Take ownership of the folder if prompted, then delete its contents (not the folder itself).
4. Go to **Settings > Accounts > Sign-in options > PIN (Windows Hello)** and set up a new PIN.
5. Re-enroll your face or fingerprint under the same settings page.
6. If the NGC folder refuses to delete because of permissions, boot into Safe Mode and retry — fewer processes hold locks on it there.

### Fix 6: Re-enroll biometrics cleanly

After the repairs above, Hello needs fresh biometric templates.

1. Go to **Settings > Accounts > Sign-in options**.
2. Remove existing **Facial recognition** and **Fingerprint recognition** entries.
3. Add them again, following the on-screen capture carefully — good lighting for face, full finger coverage for fingerprint.
4. Sign out and test each Hello method at the lock screen.
5. Microsoft documents the whole Hello setup flow on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Check for the update that caused the crash

If the blue screen came from a bad update, the underlying cause may still be installed.

1. Go to **Settings > Windows Update > Update history** and note recent driver or cumulative updates.
2. Uninstall the suspect update via **Uninstall updates**.
3. Pause updates for a week (**Settings > Windows Update > Pause updates**) to avoid immediate reinstallation.
4. If blue screens persist, investigate the stop code itself — start with our [blue screen of death fix guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) to stop the crashes at their source.

## Closing

A blue screen breaks Windows Hello by damaging its drivers, service state, or TPM keys — so repair the system damage first, then rebuild the PIN and biometrics on a clean foundation. Once Hello is re-enrolled after these fixes, it stays working, and future sign-ins will be just as fast as before the crash. And if the blue screens keep coming back, fix the crash itself rather than just its casualties: a laptop that blue-screens weekly will eventually corrupt something that a driver reinstall can't undo, so treat recurring crashes as the real problem and Hello as the symptom.
