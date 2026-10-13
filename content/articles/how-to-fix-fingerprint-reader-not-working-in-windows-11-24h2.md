---
title: "How to Fix a Fingerprint Reader Not Working in Windows 11 24H2"
slug: how-to-fix-fingerprint-reader-not-working-in-windows-11-24h2
date: 2026-09-23
categories: ["drivers"]
tags: ["fingerprint reader not working", "windows hello", "biometric driver", "windows 11 24h2"]
description: "Fingerprint reader not working on Windows 11 24H2? Six fixes for Windows Hello biometrics, from driver reinstalls to re-enrolling fingerprints."
thumbnail: "/images/thumbs/how-to-fix-fingerprint-reader-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why did my fingerprint reader stop working after the Windows 11 24H2 update?"
    a: "The 24H2 upgrade reinstalls the biometric driver stack, and the fingerprint sensor driver — often a vendor-specific package from Synaptics, Goodix, or ELAN — can fail to migrate or get replaced with an incompatible build. Windows Hello then can't communicate with the sensor. The sensor hardware is almost never damaged by an update; reinstalling the vendor's biometric driver restores the link in the great majority of cases."
  - q: "Windows Hello says my fingerprint isn't recognized anymore. Is the sensor dirty?"
    a: "Possibly — a dirty or wet sensor is the most common cause of recognition failures on a working reader. Wipe the sensor with a dry microfiber cloth and make sure your finger is clean and dry. If recognition fails consistently after cleaning, delete the enrolled fingerprints and re-enroll; skin changes, cuts, and dryness can invalidate old templates even when the hardware is perfect."
  - q: "Should I remove my PIN when fixing Windows Hello fingerprint?"
    a: "No — Windows Hello requires a PIN as the fallback credential, and removing it can lock you out of Hello setup entirely. The PIN is the recovery path when biometrics fail, so keep it. If you're troubleshooting, verify your PIN works first (proving Hello's credential framework is healthy), then fix the fingerprint component specifically."
  - q: "The fingerprint option is missing from Windows Hello settings entirely. Why?"
    a: "Windows hides the fingerprint option when it can't find a compatible biometric device — meaning the sensor driver isn't loaded or the device is disabled. Check Device Manager > Biometric devices: if the sensor is missing or has a warning, that's your problem, and the driver fixes in this guide apply. If the device looks healthy but Hello still hides the option, the biometric service or group policy may be blocking it."
---

You lift the lid, rest your finger on the sensor, and... nothing. Or Windows Hello tells you the fingerprint option isn't available. The fingerprint reader worked before the 24H2 update, and now it's as if the sensor doesn't exist. This is a driver-and-enrollment problem far more often than a hardware problem — biometric sensors don't die on update schedules, but their drivers get orphaned by updates constantly.

The diagnostic split is quick: open **Settings** > **Accounts** > **Sign-in options** > **Fingerprint recognition**. If the option is missing entirely, Windows can't see the sensor — that's a driver problem (Fixes 1–4). If the option is present but recognition fails, the sensor works and the problem is enrollment quality or sensor cleanliness (Fixes 5–6). One more quick check before the fixes: try the sensor with a different finger than your usual — if a fresh finger enrolls and works, your primary template was the problem all along. We'll cover both paths. Biometric devices share Device Manager patterns with other orphaned hardware — the [unknown device guide](/articles/how-to-fix-unknown-device-in-device-manager-in-windows-11-24h2/) helps if your sensor shows up unidentified.

## Why this happens

- **The biometric driver didn't survive the 24H2 upgrade.** The Synaptics/Goodix/ELAN sensor driver failed to migrate, leaving Windows with no path to the sensor.
- **Windows Update installed an incompatible biometric driver.** A generic driver replaced the vendor's sensor-specific build and can't initialize the hardware.
- **The sensor is disabled in Device Manager.** The update flipped the biometric device to disabled status.
- **The fingerprint enrollment database corrupted.** The stored templates were damaged during the update, so recognition fails even though the sensor reads fine.
- **The Windows Biometric Service isn't running.** The service Hello depends on is stopped or disabled.
- **Group policy or MDM blocks biometrics.** A policy (common on work laptops) disables Windows Hello biometrics after a policy refresh.
- **The sensor is dirty or the finger changed.** Physical recognition failures from contamination, moisture, cuts, or dry skin — the most mundane and most common cause of "not recognized."

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reinstall the biometric sensor driver

Restore Windows' path to the sensor.

1. Device Manager > **Biometric devices** — right-click the fingerprint sensor > **Uninstall device** (check **Attempt to remove the driver**).
2. Restart — Windows attempts to reinstall on boot.
3. If it doesn't, or installs a broken generic: download the **Biometric/Fingerprint** driver for your exact model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/) and install it.
4. Verify the sensor appears in Biometric devices with no warning icon, then check **Sign-in options** for the fingerprint entry.

### Fix 2: Enable the sensor and restart the biometric service

Clear the disabled/stopped states.

1. In Device Manager > **Biometric devices**, if the sensor shows a down arrow, right-click > **Enable device**.
2. Press **Win + R**, type `services.msc`, find **Windows Biometric Service** — set **Startup type** to **Automatic** and start it if stopped.
3. Restart the laptop and test Hello fingerprint enrollment.
4. If the service won't stay running, run `sfc /scannow` in an admin terminal — service failures can indicate system file corruption.

### Fix 3: Check for policy blocks

Rule out administrative disabling.

1. Press **Win + R**, type `gpedit.msc` (Pro editions) > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Biometrics** — ensure nothing is set to **Disabled**.
2. In the registry, check `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Biometrics` — delete or correct any disabling values (back up the key first).
3. On work-managed laptops, check with IT — MDM policies can disable Hello biometrics remotely, and no local fix overrides that.
4. After policy correction, restart and re-check **Sign-in options**.

### Fix 4: Update the chipset and sensor firmware

Fix the layers beneath the driver.

1. Install the latest **Chipset** driver package from your laptop vendor — biometric sensors connect through chipset-managed buses.
2. Check the vendor's support page for **fingerprint sensor firmware** updates for your model and apply them per instructions.
3. Update the BIOS if release notes mention biometric or sensor fixes.
4. Reinstall the biometric driver (Fix 1) after firmware updates, since firmware changes can require driver re-initialization.

### Fix 5: Clean the sensor and re-enroll fingerprints

Fix recognition-quality failures.

1. Wipe the sensor with a dry microfiber cloth; ensure your finger is clean and dry.
2. **Settings** > **Accounts** > **Sign-in options** > **Fingerprint recognition** > **Remove** all enrolled fingerprints.
3. Click **Set up** and enroll again — press firmly, cover the sensor fully, and vary the finger angle slightly across scans as prompted.
4. Enroll the same finger twice (as two entries) if you use it heavily — this improves recognition tolerance. Test unlock several times.
5. If one specific finger consistently fails while others work, the issue is that finger's template, not the sensor — delete just that enrollment and re-enroll it with extra attention to full-sensor coverage during the setup scans.

### Fix 6: Reset Windows Hello completely

The nuclear option for stubborn Hello corruption.

1. **Settings** > **Accounts** > **Sign-in options** — remove fingerprint, then remove your PIN (you'll re-add it).
2. Restart, then re-add the PIN first (Hello requires it), then set up fingerprint fresh.
3. If Hello still fails, check **Settings** > **Privacy & security** for any biometric-related toggles and confirm your account is an administrator or has Hello rights.
4. As a final check, create a new local user account and test fingerprint there — if it works for the new user, your profile's Hello store is corrupt and migrating to a fresh profile is the fix. For camera-based Hello face issues (a different sensor path), the [camera detection guide](/articles/how-to-fix-laptop-camera-not-detected-after-windows-11-update/) covers the IR camera side.

## Closing

Fingerprint failures on 24H2 are driver orphans and enrollment problems, not dead sensors: reinstall the vendor's biometric driver, make sure the service runs, clean the sensor, and re-enroll. The sensor that "stopped working" after the update is almost always just waiting for Windows to remember how to talk to it — give it the driver, and it remembers.
