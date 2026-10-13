---
title: "Windows Hello Not Working? Complete Troubleshooting Guide"
slug: windows-hello-not-working-troubleshooting
date: 2026-10-13
categories: ["windows-errors"]
tags: ["windows-hello", "troubleshooting", "sign-in"]
description: "Complete Windows Hello troubleshooting: fix face, fingerprint, and PIN failures with this systematic guide."
thumbnail: "/images/thumbs/windows-hello-not-working-troubleshooting.webp"
faqs:
  - q: "Windows Hello was working and suddenly stopped. What first?"
    a: "Check the two fastest causes first: camera privacy settings (Settings > Privacy & security > Camera) and recent Windows updates that may have replaced your biometric driver. Those two account for the majority of sudden Hello failures."
  - q: "My fingerprint sensor isn't even detected. Is it dead?"
    a: "Not necessarily — check Device Manager for the biometric device first. If it's missing or has a warning, reinstall the driver from your laptop maker's site. If it's absent entirely, check the BIOS to confirm the sensor is enabled."
  - q: "Face recognition fails in the dark. Normal?"
    a: "Somewhat — Windows Hello face recognition uses an IR camera that works in low light, but total darkness or strong backlight can still defeat it. If it fails in normal lighting too, clean the camera and re-enroll your face."
  - q: "Should I remove and re-add all Hello methods?"
    a: "As a troubleshooting step, yes — removing face, fingerprint, and PIN, then setting them up fresh, clears corrupted templates and is often the fastest path when individual fixes fail. Set up the PIN first, then biometrics."
---
# Windows Hello Not Working? Complete Troubleshooting Guide

This is the systematic, no-stone-unturned **Windows Hello troubleshooting** guide: face recognition failing, fingerprint sensor not detected, PIN greyed out, or Hello options missing entirely. Instead of trying random fixes, you'll work through Hello's dependency chain in order — hardware, drivers, services, privacy, credentials — so the first fix that sticks is the right one.

If your Hello broke specifically after a blue screen, stabilize the crashes first with our [blue screen of death guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) — crash damage needs its own sequence. For a quick isolation test, try Hello in [Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) — if it works there, third-party software is interfering.

## Why this happens

- **Driver replaced by Windows Update:** The most common cause — a working biometric driver swapped for a broken one.
- **Camera privacy toggles:** Silent killer of facial recognition after updates reset permissions.
- **Windows Biometric Service stopped:** Every Hello method depends on this service.
- **Corrupted PIN/credential data:** The NGC folder damage that breaks PIN and everything built on it.
- **TPM unprovisioned or disabled:** Hello's cryptographic foundation missing.
- **Hardware disabled in BIOS:** Fingerprint sensor or camera turned off at the firmware level.
- **Missing Windows components:** Biometric framework pieces lost in a major update.

## How to fix it

Work through these in order — each layer depends on the one above it.

### Fix 1: Verify the hardware exists and is enabled

No software fix helps if the hardware is off or missing.

1. Open **Device Manager** and confirm your fingerprint sensor appears under **Biometric devices** and the IR camera under **Cameras** — no yellow warnings, no missing entries.
2. If a device is missing, restart into the BIOS/UEFI and verify the fingerprint sensor and camera are **Enabled** (often under **Security** or **Advanced**).
3. If the device appears with a warning, note the error code — Code 10 or Code 43 usually means driver trouble (Fix 2); Code 45 means Windows thinks it's disconnected (check BIOS and physical connections).
4. On some laptops a physical camera shutter or **Fn** key combination disables the camera — check for a shutter slider above the screen or a camera kill-switch key before assuming a driver problem.

### Fix 2: Reinstall biometric drivers cleanly

The most common actual fix — do it properly, not just "update."

1. In Device Manager, right-click each biometric device and choose **Uninstall device**, ticking **Attempt to remove the driver for this device**.
2. Restart and let Windows reinstall.
3. If Windows installs a non-working generic driver, download the exact driver from your laptop maker's support site — [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), or Lenovo support — using your model number.
4. After installing, check **Optional updates** under Windows Update for a newer biometric driver — the best version is sometimes staged there rather than installed automatically.

### Fix 3: Check privacy and app permissions

Facial recognition dies silently when permissions change.

1. Go to **Settings > Privacy & security > Camera** and ensure camera access is on.
2. Check **Settings > Accounts > Sign-in options** — if Hello options are greyed out with "something went wrong," the issue is deeper (continue to Fix 4).
3. Verify no third-party "privacy" app is blocking the camera at a lower level than Windows settings.

### Fix 4: Restart the Windows Biometric Service

One stuck service breaks all Hello methods simultaneously.

1. Press **Win + R**, type `services.msc`, and open **Windows Biometric Service**.
2. Set **Startup type** to **Automatic**; **Start** it if stopped, **Restart** it if running.
3. Check its **Dependencies** tab and make sure **Remote Procedure Call (RPC)** is running.
4. Test Hello at the lock screen (**Win + L**). If it works here but fails after a full reboot, a startup program is interfering — disable startup apps in Task Manager and re-enable them one at a time.

### Fix 5: Rebuild the PIN and credential store

The foundation layer — fix it before touching biometrics.

1. Sign in with your password.
2. Delete the contents of `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC` (take ownership if prompted).
3. Go to **Settings > Accounts > Sign-in options > PIN (Windows Hello)** and set up a fresh PIN.
4. Confirm the PIN works at the lock screen before proceeding.

### Fix 6: Remove and re-enroll all biometrics

With the foundation solid, rebuild the biometric templates from scratch.

1. In **Sign-in options**, remove existing **Facial recognition** and **Fingerprint recognition**.
2. Re-add facial recognition in even lighting, looking directly at the camera — and improve recognition afterward with the "Improve recognition" option if offered.
3. Re-add fingerprints, enrolling the same finger at multiple angles.
4. Clean the sensor and camera lens with a microfiber cloth — smudges cause more failures than people expect.
5. Test each method at the lock screen.

### Fix 7: Check the TPM and system integrity

The deepest layers — TPM state and OS health.

1. Run `tpm.msc` — status should read "The TPM is ready for use." Clear and re-provision it if not (keep your BitLocker recovery key handy).
2. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an admin Terminal.
3. Install all pending Windows updates — Microsoft ships Hello fixes in cumulative updates regularly.
4. If Hello works in a new local user account but not yours, your profile's credential store is corrupted — migrate to the new profile. Microsoft's full Hello documentation lives on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Windows Hello is a chain — hardware, driver, service, privacy, PIN, biometrics, TPM — and it breaks at the weakest link. Work the chain top to bottom instead of guessing, and you'll find the break quickly. Most of the time it's the driver Windows Update just replaced or a privacy toggle it just flipped; the full rebuild in Fixes 5–6 handles everything else. Once every link is verified, Hello just works — which is how it should have been all along, letting you sign in with a glance or a touch.
