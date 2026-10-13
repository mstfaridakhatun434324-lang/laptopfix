---
title: "Fingerprint Reader Not Working? How to Fix It on Windows Laptops"
slug: "how-do-i-fix-fingerprint-reader-not-working"
date: "2026-09-21"
categories: ["drivers"]
tags: ["fingerprint reader", "windows hello", "biometric", "login issues"]
description: "Windows Hello fingerprint login failing or the reader not detected? Fix enrollment errors, driver issues, and hardware detection step by step."
thumbnail: "/images/thumbs/how-do-i-fix-fingerprint-reader-not-working.webp"
faqs:
  - q: "Why is there no fingerprint option in Windows Hello?"
    a: "The fingerprint option appears only when three conditions are met: a compatible reader is detected, its driver is working, and a Hello PIN exists. Check Device Manager for the biometric device, set up a PIN first, and confirm the reader is enabled in the BIOS."
  - q: "Why does my fingerprint reader fail to recognize my finger?"
    a: "Recognition failures are usually caused by a dirty or moist sensor, poorly enrolled prints, or skin condition changes. Clean the sensor, wash and dry your hands, delete the old enrollment, and re-enroll capturing multiple angles of the finger for a more complete template."
  - q: "Can a Windows update break the fingerprint reader?"
    a: "Yes. Feature updates can replace the vendor biometric driver with a generic one, reset the BIOS-adjacent security settings, or corrupt the Hello credential store. Reinstalling the vendor driver and re-enrolling fingerprints after major updates resolves most cases, so verify Hello still works after each feature update."
  - q: "Is it safe to delete the NGC folder to fix Hello?"
    a: "Deleting the NGC folder forces Windows Hello to rebuild its credential store and is a recognized fix for persistent enrollment errors. You will need to set up your PIN and biometrics again afterward. Take ownership of the folder first, and only do this when standard re-enrollment has failed."
---

The fingerprint reader is one of those features that works invisibly until it does not — and then every login becomes a password-typing chore. Fingerprint failures divide into two groups: the reader is not detected at all (missing from Device Manager, no Windows Hello fingerprint option), or it is detected but will not enroll or recognize prints (errors during setup, 'couldn't recognize' loops).

Detection problems are driver or BIOS issues. Recognition problems are usually about the sensor surface, the enrolled print data, or Windows Hello's configuration. The fixes below handle both, in the order a technician would try them — quick checks first, driver work second, re-enrollment third.

One prerequisite that trips people up: Windows Hello fingerprint requires a PIN to be set up first. If you never created a PIN, the fingerprint option stays grayed out no matter how healthy the reader is. Our companion guide on [fingerprint reader issues in Windows 11 24H2](/articles/how-to-fix-fingerprint-reader-not-working-in-windows-11-24h2/) covers the update-specific variant of this problem.

## Why this happens

- **Biometric device disabled in BIOS**: Many laptops have a BIOS toggle for the fingerprint reader. Firmware updates can reset it to disabled, making the reader vanish from Windows entirely.
- **Corrupted biometric driver**: The fingerprint sensor needs its vendor driver (Synaptics, ELAN, Goodix). A generic driver or a corrupted install leaves the device undetected or nonfunctional.
- **Windows Hello configuration corruption**: The Hello credential store can corrupt after updates, producing enrollment failures even with a healthy sensor.
- **Dirty or wet sensor surface**: Fingerprint sensors are optical or capacitive surfaces. Moisture, oil, or grime prevents clean reads and causes endless 'try again' loops.
- **PIN not set up**: Windows Hello biometrics are layered on top of a PIN. Without one, fingerprint setup is blocked at the first step.
- **Conflicting security software**: Some endpoint security tools restrict biometric enrollment as a policy, particularly on business laptops.
- **Windows Biometric Service not running**: The Windows Biometric Service (WbioSrvc) must be running for any biometric device to function. If it is disabled, the reader goes dark.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set Up a PIN First

Open Settings, Accounts, Sign-in options. If PIN (Windows Hello) shows 'not set up,' click it and create a PIN. Only then will the Fingerprint recognition option become available. This is by design — the PIN is the fallback credential that biometrics unlock.

If a PIN exists but Hello still will not proceed, remove the PIN and recreate it. PIN data can corrupt during feature updates, and recreating it clears the corruption for the whole Hello stack.

1. Open Settings, Accounts, Sign-in options.
2. Set up a PIN if none exists.
3. Check whether Fingerprint recognition is now available.
4. If Hello misbehaves, remove and recreate the PIN.
5. Retry fingerprint setup.

### Fix 2: Clean the Sensor and Re-enroll Prints

Wipe the sensor with a soft, dry, lint-free cloth — no liquids. Wash and dry your hands. Then remove existing fingerprints under Sign-in options (select each enrolled finger and click Remove) and re-enroll: place the finger flat, lift and reposition between scans to capture different angles, and enroll the same finger twice if the option exists.

Enroll fingers you actually log in with, in the condition your hands are usually in. Enrolling a freshly washed finger and then trying to log in with dry winter hands is a classic self-inflicted recognition failure.

1. Clean the sensor with a dry lint-free cloth.
2. Wash and thoroughly dry your hands.
3. Remove all enrolled fingerprints.
4. Re-enroll with varied finger angles and positions.
5. Test login with each enrolled finger.

### Fix 3: Enable the Reader in BIOS

Restart into the BIOS/UEFI setup and look under Security or Advanced for 'Fingerprint Reader,' 'Biometric Device,' or similar. Set it to Enabled, save, and exit. While there, check that any 'Biometric' or 'Pre-boot authentication' options match your needs.

If the reader was working and stopped after a BIOS update, this toggle is the prime suspect — firmware updates reset security-related settings to defaults. This also applies to laptops where the reader never appeared: some models ship with it disabled.

1. Restart and enter BIOS/UEFI setup.
2. Find the fingerprint/biometric device option under Security or Advanced.
3. Set it to Enabled, save, and exit.
4. Boot into Windows and check Device Manager for the biometric device.
5. Retry Windows Hello fingerprint setup.

### Fix 4: Reinstall the Biometric Driver

In Device Manager, expand Biometric devices, right-click the fingerprint sensor, and choose Uninstall device with driver deletion. Restart, then install the biometric driver from your laptop maker's support site for your exact model — Synaptics, ELAN, and Goodix sensors each need their vendor driver, and the generic Windows driver often fails to initialize them.

After reinstalling, verify the device appears in Device Manager without warnings before attempting enrollment. A sensor with a yellow triangle will never enroll successfully. You can confirm driver versions with our [driver version check guide](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/).

1. In Device Manager, uninstall the biometric device with driver deletion.
2. Restart the laptop.
3. Install the vendor biometric driver from the maker's site.
4. Confirm the device appears without warnings.
5. Attempt fingerprint enrollment again.

### Fix 5: Restart the Windows Biometric Service

Press Windows key + R, type services.msc, and find Windows Biometric Service. Set its startup type to Automatic and start it if it is stopped. This service brokers all communication between biometric hardware and Windows Hello — without it, even a perfect sensor is invisible to Hello.

If the service will not stay running, system file corruption is likely — run sfc /scannow from an elevated Command Prompt. Microsoft documents biometric troubleshooting steps in its [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open services.msc and locate Windows Biometric Service.
2. Set startup type to Automatic.
3. Start the service.
4. Restart and verify it is still running.
5. Retry fingerprint enrollment.

### Fix 6: Reset Windows Hello

If enrollment fails with a healthy sensor and correct drivers, reset Hello's data: go to Settings, Accounts, Sign-in options, remove all Hello methods (face, fingerprint, PIN), restart, then set them up fresh starting with the PIN. This clears corrupted credential-store entries that block enrollment.

For stubborn cases, deleting the NGC folder (C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC) after taking ownership forces Hello to rebuild its store from scratch — a known fix for 'something went wrong' enrollment errors.

1. Remove all Windows Hello sign-in methods.
2. Restart the laptop.
3. Set up a fresh PIN first.
4. Enroll fingerprints again.
5. For persistent errors, clear the NGC folder and repeat.

## Closing

Fingerprint reader problems are rarely the sensor dying — they are PIN prerequisites, dirty sensors, BIOS toggles, and driver mismatches. Clean the sensor, confirm the BIOS setting, reinstall the vendor driver, and re-enroll carefully. That sequence restores Hello fingerprint login in the overwhelming majority of cases.
