---
title: "How to Fix Windows Hello When It Stops Working"
slug: how-to-fix-windows-hello-not-working-youtube
date: 2026-09-15
categories: ["windows-errors"]
tags: ["windows hello", "biometrics", "sign-in"]
description: "Windows Hello face or fingerprint login failing? These fixes cover drivers, camera issues, PIN resets, and corrupted biometric data."
thumbnail: "/images/thumbs/how-to-fix-windows-hello-not-working-youtube.webp"
faqs:
  - q: "Why does Windows Hello say it's unavailable?"
    a: "Usually the biometric driver failed to load, the camera or fingerprint sensor is disabled in BIOS or Device Manager, or a Windows update broke the biometric stack. Less often, the stored biometric data itself is corrupt and needs to be re-enrolled."
  - q: "Do I need a PIN to use Windows Hello?"
    a: "Yes — Windows requires a PIN as the fallback and foundation for Hello. If your PIN is broken or was removed, Hello biometrics will not work until the PIN is set up again. Many 'Hello not working' cases are actually PIN problems."
  - q: "Can a Windows update break Windows Hello?"
    a: "Yes, it happens regularly. Updates replace biometric and camera drivers with generic versions, or change the biometric service configuration. Rolling back the biometric driver or re-enrolling your face/fingerprint after an update fixes most cases."
  - q: "Is it safe to delete my biometric data and start over?"
    a: "Yes. Your face and fingerprint templates are stored locally in a secure enclave on your device, not in the cloud. Deleting them just means re-enrolling — nothing is lost that you cannot recreate in two minutes at the login screen."
---
Windows Hello is one of those features you do not appreciate until it breaks — and then every login becomes an exercise in typing a password you barely remember. Face recognition failing, the fingerprint reader ignoring you, or Settings bluntly stating "Windows Hello isn't available on this device" all have concrete causes, and most are fixable in minutes.

The fixes below cover the full chain: the PIN foundation, the biometric drivers, the camera and sensor hardware, and the stored biometric data itself.

## Why this happens

- **Broken or missing PIN:** Hello biometrics sit on top of the PIN; a damaged PIN breaks everything above it.
- **Biometric driver failure:** Fingerprint sensor or IR camera drivers that fail to load after updates.
- **Camera/sensor disabled:** Disabled in Device Manager, blocked by a privacy shutter, or turned off in BIOS.
- **Corrupt biometric enrollment data:** Damaged templates that no longer match, requiring re-enrollment.
- **Windows Update driver replacement:** Generic drivers overwriting manufacturer biometric drivers.
- **Biometric service problems:** The Windows Biometric Service stalled or misconfigured.
- **Lighting or hardware changes:** For face recognition — new glasses, major lighting changes, or a dirty IR camera.
- **Domain or work-account policy changes:** On work laptops, an IT policy update can disable biometrics remotely without any local error explaining why — if nothing local helps, check with your administrator.

## How to fix it

Work through these in order.

### Fix 1: Fix the PIN first

Most Hello failures are PIN failures in disguise.

1. Go to **Settings > Accounts > Sign-in options** and look at the **PIN** section.
2. If the PIN shows an error or Hello options are greyed out, click **Remove** on the PIN (you will need your Microsoft account password), then **Add** to create a fresh one.
3. Sign out and back in with the new PIN. In many cases, face and fingerprint immediately start working again once the PIN foundation is healthy.

### Fix 2: Re-enroll your biometrics

Corrupt enrollment data is common after updates. Before re-enrolling, make sure the sensor or camera actually works: open the Camera app and check the IR camera shows an image, and confirm the fingerprint reader appears in Device Manager without warnings. Re-enrolling onto broken hardware just wastes time — Fix 3 covers the hardware checks if enrollment fails.

1. In **Settings > Accounts > Sign-in options**, remove your existing **Facial recognition** and **Fingerprint recognition** enrollments.
2. Re-add them: for face, sit in normal room lighting facing the camera; for fingerprint, use the finger you naturally unlock with and press firmly through the full scan animation.
3. Test on the lock screen (**Win + L**). If enrollment itself fails with an error, the driver or hardware is the problem — continue below.

### Fix 3: Check the camera and sensor in Device Manager

A disabled or driverless device cannot do biometrics.

1. Open **Device Manager** (**Win + X**) and expand **Biometric devices** — your fingerprint reader should appear with no warning icon.
2. Expand **Cameras** (or **Imaging devices**) and confirm the IR camera is present and enabled. Right-click anything disabled and choose **Enable device**.
3. If a device shows a yellow warning, right-click it and choose **Update driver > Search automatically for drivers**. For brand-specific Hello problems, see our [Lenovo guide](/articles/how-to-fix-windows-hello-not-working-on-lenovo-laptop/) or [Dell guide](/articles/how-to-fix-windows-hello-not-working-on-dell-laptop/).

### Fix 4: Install the manufacturer's biometric drivers

Generic Windows drivers frequently break Hello.

1. Go to [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/), enter your serial number, and download the **fingerprint**, **camera/IR camera**, and **chipset** drivers.
2. Install them and reboot. If Hello broke right after a Windows update, check **Device Manager > Biometric devices > Properties > Driver** and use **Roll Back Driver** instead.

### Fix 5: Check BIOS settings and physical shutters

Hardware-level disables override everything in Windows. This is the step people skip because it feels unlikely — but privacy shutters and BIOS toggles are exactly the kind of thing that gets flipped during travel, cleaning, or a "helpful" tweak by someone else using the laptop, and then forgotten.

1. Enter the BIOS at boot and look for **fingerprint reader**, **biometric device**, or **camera** toggles — make sure they are enabled.
2. Check for a physical camera privacy shutter (a slider over the webcam — common on Lenovo and HP) and open it. IR face recognition needs the camera physically unobstructed.
3. Clean the fingerprint sensor with a dry microfiber cloth — skin oils genuinely degrade recognition over time. A quick wipe once a week keeps the sensor reading reliably.

### Fix 6: Restart the Windows Biometric Service

A stalled service silently kills Hello.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **Windows Biometric Service**, right-click, and choose **Restart**. Set its **Startup type** to **Automatic**.
3. Try Hello again. If the service will not stay running, continue to the file-repair step.

### Fix 7: Repair system files and reset the biometric database

For stubborn corruption, rebuild the biometric store.

1. Open an elevated Command Prompt and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. To reset the biometric database: stop the **Windows Biometric Service**, take ownership of `C:\Windows\System32\WinBioDatabase`, rename or back up its contents, restart the service, and re-enroll your biometrics fresh.
3. Reboot and test. Microsoft documents additional Hello recovery steps on Microsoft Support if the database reset does not help.

## Closing

Windows Hello failures follow a chain — PIN, enrollment data, drivers, hardware — and fixing them means walking that chain in order. Reset the PIN, re-enroll, install the manufacturer's biometric drivers, and check the BIOS and physical shutter. One of those links is always the broken one. After you get it working, re-enroll in the lighting conditions where you actually use the laptop — enrollments done in a dark room at midnight recognize you worst at your bright desk at noon, and a fresh daytime enrollment noticeably improves reliability.
