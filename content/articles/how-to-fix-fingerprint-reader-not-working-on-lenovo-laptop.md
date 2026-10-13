---
title: "Fingerprint Reader Not Working on a Lenovo Laptop? Re-enroll Biometrics"
slug: how-to-fix-fingerprint-reader-not-working-on-lenovo-laptop
date: 2026-09-19
categories: ["drivers"]
tags: ["fingerprint reader", "windows hello", "lenovo", "biometrics"]
description: "Fix the fingerprint reader on a Lenovo laptop: repair Windows Hello enrollment, reinstall the biometric driver, and fix BIOS and power issues."
thumbnail: "/images/thumbs/how-to-fix-fingerprint-reader-not-working-on-lenovo-laptop.webp"
faqs:
  - q: "Why does Windows Hello say the fingerprint option is currently unavailable?"
    a: "That message means Windows cannot communicate with the biometric sensor, not that your fingerprint data is bad. The usual causes are a disabled or error-flagged biometric device in Device Manager, a BIOS-level sensor disable, or a driver mismatch after a Windows update. Re-enabling the device and reinstalling Lenovo's biometric driver clears it."
  - q: "Do I need to delete my fingerprints and start over?"
    a: "Often yes, and it is harmless. Corrupted biometric templates in the system's secure store can make a healthy sensor fail every scan. Removing the existing fingerprints under Sign-in options and re-enrolling with clean, dry fingers fixes template corruption in minutes."
  - q: "Why does the fingerprint reader work after restart but not after sleep?"
    a: "The sensor is failing to reinitialize when the laptop wakes. Windows powers the biometric device down during sleep, and on some Lenovo firmware the sensor does not come back without a full driver reload. Disabling power management on the biometric device and updating the BIOS usually ends the pattern."
  - q: "Can a BIOS update really affect the fingerprint reader?"
    a: "Yes. The fingerprint sensor initializes partly in firmware, and Lenovo BIOS updates regularly include fixes for biometric device enumeration and power sequencing. If the sensor is missing from Device Manager even with hidden devices shown, a BIOS update is one of the most effective remaining steps."
---

The fingerprint reader on a Lenovo laptop is one of those features you stop appreciating until it breaks — and then every login becomes a password you half-remember. The typical failure presents as Windows Hello reporting that the fingerprint option is currently unavailable, or the sensor light staying dark no matter how you position your finger. PIN login still works, which confirms Windows itself is healthy and the problem is isolated to the biometric path.

That path has more layers than most people expect. The sensor hardware talks through a biometric driver to the Windows Biometric Service, which compares scans against templates stored in a secured system vault. Above that sits Lenovo's firmware and power management, which can keep the sensor asleep permanently. A break at any layer produces the same symptom: Hello shrugs and offers no fingerprint option.

The fixes below move from the fastest — re-enrolling fingerprints and checking the sensor's device state — through driver reinstallation and service repairs, ending with the BIOS checks that catch firmware-level disables.

## Why this happens

- **Corrupted biometric templates:** The stored fingerprint templates can corrupt during updates, making a working sensor reject every scan or refuse to offer enrollment.
- **Biometric device disabled in Device Manager:** Updates can disable the sensor device or leave it error-flagged. Windows Hello then reports the option as unavailable.
- **Driver mismatch after a Windows update:** A generic driver substituted for Lenovo's biometric package may enumerate the sensor but fail actual scans.
- **Windows Biometric Service stopped:** If the underlying biometric service is disabled or crashing, Hello has nothing to talk to regardless of driver health.
- **Power management keeping the sensor asleep:** The sensor may not reinitialize after sleep, so fingerprints work after a restart but never after waking the laptop.
- **Sensor disabled in BIOS:** Lenovo BIOS can disable the fingerprint reader at the firmware level, hiding it from Windows completely.
- **Dirty or damaged sensor surface:** Skin oils, moisture, and fine scratches degrade scan quality. A sensor that fails intermittently before failing totally often just needs cleaning — or has a worn surface.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean the sensor and re-enroll your fingerprints

Start with the physical layer and the template store. This resolves scan-quality failures and corrupted enrollments in minutes.

1. Wipe the sensor with a soft, dry microfiber cloth — no liquids.
1. Open Settings, then Accounts, then Sign-in options, and remove the existing fingerprint data.
1. Re-enroll the same finger twice if offered, using clean dry hands and varying the angle slightly across scans.

### Fix 2: Check the biometric device in Device Manager

Confirm Windows sees the sensor and that it is enabled and error-free before touching drivers.

1. Open Device Manager and expand Biometric devices.
1. If the fingerprint sensor is grayed out, right-click and enable it. If it shows a warning, note the error code.
1. If the entire Biometric devices category is missing, open the View menu and choose Show hidden devices — a grayed entry means a driver or BIOS problem, not dead hardware.

### Fix 3: Reinstall the biometric driver

A corrupted or mismatched driver is the most common software cause. Remove it fully so Windows cannot reinstall the same broken copy.

1. Right-click the fingerprint sensor in Device Manager and choose Uninstall device, checking Delete the driver software.
1. Restart the laptop.
1. Download the biometric or fingerprint driver for your exact model from [Lenovo support](https://support.lenovo.com/us/en/) and install it.
1. Return to Sign-in options and try enrollment again.

### Fix 4: Restart the Windows Biometric Service

Hello depends on the Windows Biometric Service running. If it is disabled or stuck, no sensor will ever work.

1. Press Win+R, type services.msc, and press Enter.
1. Find Windows Biometric Service, set its Startup type to Automatic, and start it if it is stopped.
1. Restart the laptop and check whether the fingerprint option returns in Sign-in options.

### Fix 5: Disable power management on the sensor

For readers that die after sleep, stop Windows from managing the sensor's power at all.

1. In Device Manager, open the fingerprint sensor's Properties.
1. On the Power Management tab, uncheck Allow the computer to turn off this device to save power.
1. Test across several sleep-wake cycles before declaring it fixed — this failure mode is intermittent by nature.

### Fix 6: Check the BIOS fingerprint setting

A firmware-level disable hides the sensor from Windows completely, and BIOS updates can flip this setting without warning.

1. Enter the BIOS with F2 or the Novo button during boot.
1. Look for a fingerprint reader or biometric device option under Security and set it to Enabled.
1. Save and boot to Windows, then check Device Manager for the sensor's return.

### Fix 7: Update the BIOS

Lenovo ships biometric enumeration and power-sequencing fixes in BIOS updates regularly. When the sensor is missing despite correct drivers, firmware is the remaining suspect.

1. Compare your BIOS version against the newest for your model on Lenovo's support page.
1. Apply the update with the charger connected.
1. After booting, verify the sensor appears in Device Manager and enroll a fingerprint. If Hello's camera-based sign-in also misbehaves, the [camera troubleshooting guide](/articles/laptop-camera-not-working-windows-11/) covers the shared Hello infrastructure, and you can confirm installed versions via [checking driver versions](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/).

### Fix 8: Reset Windows Hello completely when enrollment keeps failing

When individual fixes do not restore the reader, corrupted Hello state across PIN, fingerprint, and face data can keep the sensor from initializing. A full reset of Windows Hello clears every credential store at once, which succeeds where piecemeal re-enrollment fails. You will set up sign-in options again afterward, so keep your password handy.

1. Remove every Windows Hello method — fingerprint, face, and PIN — under Sign-in options, keeping only the password.
1. Restart the laptop, then confirm the Windows Biometric Service is running before re-enrolling anything.
1. Add the PIN first, then the fingerprint, testing each login method before adding the next.

## Closing

Fingerprint reader failures on Lenovo laptops cluster around three causes: corrupted enrollments, driver mismatches after updates, and power management that never wakes the sensor. Clean the sensor, re-enroll cleanly, reinstall Lenovo's driver, and take power management out of the equation. The sensor that refused every scan usually becomes a one-touch login again — and stays that way once the right driver is pinned in place.
