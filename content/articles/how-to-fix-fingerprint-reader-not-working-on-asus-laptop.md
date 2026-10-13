---
title: "How to Fix the Fingerprint Reader Not Working on an ASUS Laptop"
slug: how-to-fix-fingerprint-reader-not-working-on-asus-laptop
date: 2026-09-16
categories: ["drivers"]
tags: ["fingerprint reader not working", "asus fingerprint fix", "windows hello fingerprint"]
description: "Fingerprint reader not working on your ASUS laptop? Fix Windows Hello fingerprint sign-in with driver reinstalls, biometric service repairs, and re-enrollment."
thumbnail: "/images/thumbs/how-to-fix-fingerprint-reader-not-working-on-asus-laptop.webp"
faqs:
  - q: "Why did my ASUS fingerprint reader stop working?"
    a: "The usual causes are a biometric driver broken by a Windows update, the Windows Biometric Service failing to start, or corrupted fingerprint enrollment data. The sensor hardware rarely fails — software and enrollment issues account for nearly all cases. Start with the driver and service checks below before suspecting the sensor, since hardware failure is the least common cause by far."
  - q: "Do I need to set up a PIN before fingerprint sign-in works?"
    a: "Yes. Windows Hello requires a PIN as the fallback credential before it lets you enroll fingerprints. If the fingerprint setup option is grayed out, set up a PIN first under Settings > Accounts > Sign-in options, then the fingerprint option unlocks."
  - q: "Will removing my fingerprints delete anything important?"
    a: "No. Fingerprint templates are stored locally in a secure enclave and only used for sign-in. Removing them just means re-enrolling your finger afterward — a two-minute process. No files, accounts, or settings are affected. Re-enrollment takes about two minutes per finger, and you can register multiple fingers for convenience."
  - q: "Why does the fingerprint option not appear in sign-in options?"
    a: "That means Windows does not see a compatible biometric device — the driver is missing, the sensor is disabled in BIOS, or the device failed enumeration. Reinstalling the biometric driver from ASUS and checking the BIOS toggle are the fixes. The BIOS toggle is the fix when the sensor is completely invisible to Windows rather than merely malfunctioning."
---

You lift the lid, rest your finger on the sensor, and nothing happens — or Windows Hello says the fingerprint option is not available at all. On ASUS laptops the fingerprint reader is a small, reliable sensor, and when it stops working the cause is almost always the biometric driver, the Windows Biometric Service, or stale enrollment data rather than a dead sensor.

Fingerprint troubleshooting has a natural order: confirm Windows sees the sensor, fix the driver and service, then re-enroll your fingerprints cleanly. The steps below follow that order with ASUS-specific driver sources.

## Why this happens

- **Biometric driver broken by update:** Windows updates replace the ASUS fingerprint driver with an incompatible version.
- **Windows Biometric Service stopped:** The service that powers Windows Hello fingerprint is disabled or crashed.
- **Corrupted enrollment data:** Stored fingerprint templates get corrupted, causing recognition failures.
- **Sensor disabled in BIOS:** A firmware toggle for the fingerprint reader gets switched off.
- **PIN not configured:** Windows Hello fingerprint requires a PIN first; without it the option stays unavailable.
- **Conflicting security software:** Third-party security tools can block biometric credential providers.
- **Dirty or damaged sensor:** Skin oils and grime on the tiny sensor window degrade reads over time.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify Windows sees the fingerprint sensor

Confirm the hardware is enumerated before fixing software.

1. Open Device Manager and expand **Biometric devices**. Look for the fingerprint sensor (often labeled ELAN, Synaptics, or Goodix).
2. If it shows a warning icon, note the error code. If the section is missing, click **View > Show hidden devices**.
3. Ensure you have a PIN set: **Settings > Accounts > Sign-in options > PIN (Windows Hello)** — set one up if missing.
4. Check that the sensor window (on the power button or palmrest) is clean — wipe it gently with a dry microfiber cloth.

A missing Biometric devices section means a driver or BIOS problem — continue to Fix 2 and Fix 5. If the sensor is present but reads fail, skip ahead to Fix 6.

### Fix 2: Reinstall the ASUS biometric driver

The primary fix for update-broken fingerprint readers.

1. Open the **MyASUS** app on your laptop (or your laptop maker's support portal), enter your exact model, and download the **fingerprint** or **biometric** driver for your Windows version.
2. In Device Manager, right-click the fingerprint device, choose **Uninstall device**, and check driver removal if offered.
3. Install the downloaded driver and restart.
4. Go to **Settings > Accounts > Sign-in options > Fingerprint recognition** and check whether setup is now available.

Use the ASUS-provided driver rather than a generic sensor-vendor download — ASUS customizes the integration with its power-button sensors. If other [device-manager mysteries](/articles/best-way-to-fix-fingerprint-reader-not-working/) persist, the general fingerprint guide covers more sensor brands.

### Fix 3: Restart the Windows Biometric Service

Without this service, Windows Hello fingerprint cannot function.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **Windows Biometric Service**. Set **Startup type** to **Automatic**.
3. If it is stopped, click **Start**; if running, click **Restart**.
4. Try fingerprint sign-in or enrollment again.

If the service fails to start with an error, the underlying driver is broken — return to Fix 2. A healthy driver plus a running service is the entire foundation fingerprint needs.

### Fix 4: Remove and re-enroll your fingerprints

Corrupted templates cause "couldn't recognize" failures even with perfect hardware and drivers.

1. Go to **Settings > Accounts > Sign-in options > Fingerprint recognition (Windows Hello)**.
2. Click **Remove** to delete the stored fingerprint data.
3. Click **Set up** and follow the enrollment, lifting and repositioning your finger as instructed. Enroll the same finger twice (two entries) for better reliability.
4. Test sign-in from the lock screen (**Win + L**).

Enroll with the finger dry and the sensor clean. If enrollment fails partway repeatedly, the sensor window may be scratched — inspect it under bright light.

### Fix 5: Check the BIOS fingerprint toggle

Firmware can disable the sensor beneath Windows.

1. Reboot into BIOS/UEFI (**F2** or **Del** on most ASUS laptops).
2. Look under **Advanced** or **Security** for **Fingerprint**, **Biometric device**, or **FPR** options.
3. Ensure it is **Enabled**, save, and boot into Windows.
4. Recheck Device Manager for the biometric device.

This is uncommon but decisive when the sensor is invisible to Windows entirely.

### Fix 6: Clean the sensor and adjust for real-world conditions

The physical layer matters for capacitive sensors.

1. Power off and gently clean the sensor with a dry microfiber cloth — no liquids, no abrasives.
2. If your fingers are very dry, moisturize lightly before enrolling; if wet, dry them — capacitive sensors need normal skin conductivity.
3. Re-enroll after cleaning, since the stored template was captured through the grime.
4. Check for screen protectors or skins overlapping the sensor window on power-button sensors.

Technicians see "dead" fingerprint readers revived by cleaning more often than users expect — the sensor window is tiny and oils accumulate fast.

### Fix 7: Check for conflicting software and group policy

The last software layer.

1. Temporarily disable third-party antivirus/security suites and test fingerprint sign-in.
2. On Pro editions, check **Group Policy** (`gpedit.msc`) under **Computer Configuration > Administrative Templates > Windows Components > Biometrics** — ensure biometrics are **allowed**, not disabled.
3. Run `sfc /scannow` in an elevated prompt to repair system files the biometric stack depends on.

Domain-joined or company-managed ASUS laptops sometimes have biometrics disabled by policy — in that case your IT administrator owns the fix, not you. Microsoft documents Windows Hello setup on the [Windows support site](https://support.microsoft.com/en-us/windows). For camera-based Hello issues (a different sensor path), see our [webcam troubleshooting guide](/articles/best-way-to-fix-webcam-black-screen/).

## Closing

A non-working fingerprint reader on an ASUS laptop is a driver, service, or enrollment problem in nearly every case — not a dead sensor. Reinstall the ASUS biometric driver, ensure the Windows Biometric Service runs on Automatic, and re-enroll your fingerprints on a clean sensor. That trio restores Windows Hello fingerprint sign-in on the vast majority of machines.
