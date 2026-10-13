---
title: "Windows Hello Not Working on ASUS Laptop: Fix Guide"
slug: how-to-fix-windows-hello-not-working-on-asus-laptop
date: 2026-10-02
categories: ["windows-errors"]
tags: ["windows hello", "asus", "biometric", "face recognition"]
description: "Windows Hello face or fingerprint sign-in not working on your ASUS laptop? Here's how to fix drivers, PIN issues, and camera problems."
thumbnail: "/images/thumbs/how-to-fix-windows-hello-not-working-on-asus-laptop.webp"
faqs:
  - q: "Why is Windows Hello not available on my ASUS laptop?"
    a: "Hello needs compatible hardware — an IR camera for face recognition or a fingerprint reader — plus a PIN set up first. If the option is greyed out, either the biometric driver is missing, the camera is disabled, or no PIN exists yet. Check Device Manager for the biometric device."
  - q: "Why does Windows Hello say 'something went wrong' on ASUS?"
    a: "That generic error usually means the biometric driver crashed or the Windows Biometric Service isn't running. Updating the fingerprint/camera driver from ASUS and restarting the biometric service fixes most cases."
  - q: "Do I need a PIN before setting up Windows Hello?"
    a: "Yes — Windows requires a PIN as the fallback credential before enabling face or fingerprint sign-in. If Hello setup fails immediately, set up a PIN first in Settings > Accounts > Sign-in options, then add Hello."
  - q: "Can a Windows update break Windows Hello?"
    a: "Yes, updates sometimes replace working biometric drivers with incompatible generic ones, or break the Hello credential store. Rolling back the driver or removing and re-adding your PIN usually restores it."
---

Windows Hello is one of those features you don't appreciate until it breaks — then every login becomes a password-typing chore. On ASUS laptops, Hello failures cluster around a few familiar causes: the fingerprint or IR camera driver got replaced by a Windows update, the PIN credential backing Hello got corrupted, or the biometric service itself stopped running. Face recognition adds camera privacy settings to the suspect list.

The fix order here starts with the quick checks (is the hardware even detected?) before moving to driver surgery and credential resets. Most ASUS Hello problems resolve by Fix 4.

## Why this happens

- **Biometric driver replaced or corrupted**: Windows Update installs a generic fingerprint/camera driver over ASUS's working one, and Hello stops recognizing the hardware.
- **PIN credential corrupted**: Hello's face/fingerprint data is tied to your PIN. If the PIN credential store corrupts, Hello fails with vague errors.
- **Windows Biometric Service stopped**: The background service Hello depends on gets disabled — often by "optimizer" utilities.
- **Camera disabled or blocked**: For face recognition, a disabled camera (function key, privacy shutter, or privacy settings) kills Hello silently.
- **IR camera driver missing**: Some ASUS models need a separate IR camera driver from ASUS's support site; without it, Windows sees a regular webcam and Hello face setup isn't offered.
- **Corrupt Hello credential store after an update**: Updates occasionally damage the stored biometric templates, requiring re-enrollment.
- **BIOS/firmware issues**: Outdated BIOS on some ASUS models breaks the TPM-backed credential storage Hello relies on.

## How to fix it

Work through these in order — verify hardware detection first, then drivers, then credentials.

### Fix 1: Confirm the hardware is detected

Don't troubleshoot software for a hardware problem.

1. Open **Device Manager** (**Win + X**) and expand **Biometric devices** — your fingerprint reader should be listed without a warning icon.
2. Expand **Cameras** / **Imaging devices** and confirm the IR camera appears (often named with "IR" or listed as a second camera device).
3. If either is missing or has a yellow triangle, that's your problem — skip to Fix 2 for drivers.
4. Also check the physical camera shutter — many ASUS laptops have a physical privacy shutter or **Fn** key camera toggle. A covered camera means face Hello can never work.

### Fix 2: Update biometric and camera drivers from ASUS

ASUS's drivers, not Windows' generics.

1. In **Device Manager**, right-click the fingerprint reader and choose **Update driver** > **Search automatically for drivers**.
2. Better: download the fingerprint and camera/IR drivers for your exact model from ASUS's support site (use your model number, not a "similar" one).
3. Install them, restart, and check **Settings** > **Accounts** > **Sign-in options** — the Hello options should now be configurable.
4. If Windows Update later replaces them again, pause driver updates or use the device's **Driver** tab > **Roll Back Driver** to restore ASUS's version.

### Fix 3: Remove and re-add your PIN, then re-enroll Hello

The credential reset that fixes corrupted Hello stores.

1. Go to **Settings** > **Accounts** > **Sign-in options**.
2. Under **PIN (Windows Hello)**, click **Remove**. Confirm — this also removes face/fingerprint data tied to it.
3. Restart the laptop (don't skip this — the credential store needs the reboot to clear).
4. Go back to **Sign-in options**, set up a new **PIN**, then add **Facial recognition** or **Fingerprint recognition** fresh.
5. This is Microsoft's recommended recovery for Hello credential corruption — see [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for related sign-in troubleshooting.

### Fix 4: Restart the Windows Biometric Service

A stopped service silently disables all of Hello.

1. Press **Win + R**, type `services.msc`, press Enter.
2. Find **Windows Biometric Service**. Set **Startup type** to **Automatic** and click **Start** if it's stopped.
3. If it was already running, right-click and choose **Restart**.
4. Test Hello immediately. If an "optimizer" tool disabled this, check what else it turned off.

### Fix 5: Check camera privacy settings (face recognition)

Windows can block Hello's access to the camera.

1. Go to **Settings** > **Privacy & security** > **Camera**.
2. Make sure **Camera access** is on. Hello uses a system-level path, but misconfigured privacy settings have been known to interfere.
3. Also check **Settings** > **Bluetooth & devices** > **Cameras** to confirm the IR camera is enabled there.
4. Test face setup again in **Sign-in options**.

### Fix 6: Update the BIOS

Firmware-level credential storage issues need firmware fixes.

1. Check your BIOS version with `msinfo32`.
2. Download the latest BIOS for your model from ASUS support and install it with the charger plugged in.
3. ASUS BIOS updates have fixed Hello/TPM issues on several model lines — worth doing if you're multiple versions behind.

### Fix 7: Repair system files

Corruption in Hello's OS components.

1. Open **Terminal (Admin)** and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Restart and re-test Hello. If it broke right after a Windows update, this often repairs it.

### Fix 8: Clean up the Hello credential store manually

For stubborn cases where re-enrollment keeps failing.

1. Remove PIN and Hello data in **Sign-in options** as in Fix 3.
2. Open **File Explorer**, navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC` (you'll need to take ownership — it's a protected folder).
3. Delete the contents of the NGC folder, restart, and set up PIN + Hello fresh.
4. If Hello works in a new local user account but not yours, your profile's credential store is damaged beyond repair — migrate to the new profile. For the general Windows 11 Hello guide, see [Windows Hello not working on Windows 11](/articles/how-to-fix-windows-hello-not-working-on-windows-11/).

## Closing

Windows Hello failing on an ASUS laptop is usually a driver or credential problem, not broken hardware: confirm the biometric device is detected, install ASUS's drivers, reset the PIN and re-enroll, and check the biometric service. Face recognition adds the camera shutter and IR driver to the checklist. Work the list in order and you'll be back to password-free sign-ins — and you'll know exactly which piece broke if it ever happens again. The same steps apply across brands, so the [HP Hello fix guide](/articles/how-to-fix-windows-hello-not-working-on-hp-laptop/) is worth a skim if you manage multiple laptops.
