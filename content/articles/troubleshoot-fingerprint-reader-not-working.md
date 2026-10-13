---
title: "Fingerprint Reader Not Working: Troubleshooting Walkthrough"
slug: "troubleshoot-fingerprint-reader-not-working"
date: "2026-10-02"
categories: ["drivers"]
tags: ["fingerprint reader", "biometric troubleshooting", "windows hello", "synaptics"]
description: "A systematic walkthrough for dead fingerprint readers: determine whether it's BIOS, driver, Hello config, or hardware — then apply the right fix."
thumbnail: "/images/thumbs/troubleshoot-fingerprint-reader-not-working.webp"
faqs:
  - q: "How do I tell if my fingerprint reader is a hardware or software problem?"
    a: "Open Device Manager: a listed sensor with recognition failures points to software (drivers, Hello config, dirty sensor), while a completely absent sensor across all Device Manager views — after enabling it in BIOS — points to hardware. A Linux live USB test gives a definitive second opinion."
  - q: "Why does my fingerprint reader work after reboot but stop later?"
    a: "Intermittent failure usually means power management is suspending the biometric device, or the Windows Biometric Service is crashing. Disable power-saving on the device in Device Manager, set the Biometric Service to Automatic, and check Event Viewer for service errors at the failure times."
  - q: "Can company policy disable my fingerprint reader?"
    a: "Yes. Group policies and endpoint security tools on business laptops can disable biometric authentication entirely, and no driver reinstall overrides a policy block. If the reader is healthy but Hello refuses to enable biometrics, check with your IT administrator before further troubleshooting."
  - q: "Do I need to set up a PIN to use fingerprint login?"
    a: "Yes. Windows Hello biometrics are layered on top of a PIN — the PIN is the fallback credential, and the fingerprint option stays unavailable until one exists. If Hello misbehaves, removing and recreating the PIN also clears corruption affecting the whole Hello stack."
---

When a fingerprint reader stops working, the efficient move is diagnosis before action — because the fix for a BIOS-disabled reader, a corrupted driver, and a broken Hello credential store are completely different, and applying the wrong one wastes your afternoon. This walkthrough is built around quick verdict tests that tell you which category your failure belongs to.

The three categories: not detected (no biometric device in Device Manager, no Hello fingerprint option), detected but failing (enrollment errors, endless 'couldn't recognize you' loops), and intermittently working (works after reboot, dies later). Each has a distinct cause profile and fix sequence, mapped out below.

For the condensed fix list without the diagnostic framework, see our [fingerprint reader fix guide](/articles/how-do-i-fix-fingerprint-reader-not-working/). The Windows 11 24H2-specific variant is covered in our [24H2 fingerprint guide](/articles/how-to-fix-fingerprint-reader-not-working-in-windows-11-24h2/).

## Why this happens

- ****Reader disabled in BIOS/firmware**:** Produces the 'not detected' category cleanly — no device in Device Manager, no Hello option, no errors.
- ****Wrong or corrupted biometric driver**:** The sensor needs its vendor driver (Synaptics, ELAN, Goodix). Generic or damaged drivers produce detection failures or Code 10 errors.
- ****Windows Hello credential store corruption**:** Produces the 'detected but failing' category — enrollment errors and recognition loops with healthy hardware.
- ****Windows Biometric Service stopped**:** Kills all biometric function regardless of hardware health; the reader simply goes dark.
- ****Contaminated sensor surface**:** Oil, moisture, and grime defeat capacitive and optical sensors, producing recognition failures with perfect hardware and software.
- ****Missing Hello PIN prerequisite**:** Without a PIN, the fingerprint option never activates — a configuration gap, not a malfunction.
- ****Group policy or security software restriction**:** Business laptops may have biometrics disabled by policy, which no driver reinstall will override.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verdict Test 1: Is the Reader Detected?

Open Device Manager and expand Biometric devices. If your fingerprint sensor is listed without warnings, the reader is detected — skip to the recognition-failure track. If the category is missing or the device shows a warning icon, you are on the detection track: check the BIOS toggle first (restart into setup, look under Security for the biometric/fingerprint option, enable it), then the driver.

Also check for the device under 'Unknown devices' — a reader detected without a driver lands there. Note any error code on the device's status tab; Code 10 means driver failure, Code 45 means disconnected hardware. This single check decides your entire path forward.

1. 1. Open Device Manager and look for Biometric devices.
2. 2. Listed cleanly: recognition track — go to the enrollment fixes.
3. 3. Missing or warning icon: detection track — check BIOS first.
4. 4. Check Unknown devices for a driverless reader.
5. 5. Note error codes (10 = driver, 45 = hardware).

### Fix 2: Detection Track: Fix BIOS and Driver

Enable the reader in BIOS/UEFI under Security or Advanced, save, and exit. In Windows, uninstall the biometric device in Device Manager with driver deletion, restart, and install the vendor biometric driver from your laptop maker's support site — Synaptics, ELAN, and Goodix sensors each need their specific driver, and Windows' generic driver frequently fails to initialize them.

Verify the device appears cleanly in Device Manager afterward. Then open services.msc and confirm the Windows Biometric Service is set to Automatic and running — without it, even a perfect sensor is invisible to Hello. Compare driver versions using our [driver version guide](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/) if problems persist.

1. 1. Enable the biometric device in BIOS.
2. 2. Uninstall the biometric device with driver deletion.
3. 3. Install the vendor biometric driver and restart.
4. 4. Confirm clean detection in Device Manager.
5. 5. Verify the Windows Biometric Service is running.

### Fix 3: Recognition Track: Clean Sensor and Re-enroll

Wipe the sensor with a dry lint-free cloth and wash and dry your hands. In Settings, Accounts, Sign-in options, remove all enrolled fingerprints and re-enroll carefully: varied angles, firm flat placement, lifting between scans. Enroll the fingers you actually use, in typical hand condition.

If recognition fails immediately after enrollment with clean hands and a clean sensor, the enrolled template data is likely corrupt — the remove-and-re-enroll cycle you just did addresses exactly that. Test login (not just the enrollment preview) with each finger.

1. 1. Clean the sensor with a dry lint-free cloth.
2. 2. Wash and dry your hands thoroughly.
3. 3. Remove all enrolled fingerprints.
4. 4. Re-enroll with varied angles and firm placement.
5. 5. Test actual login with each enrolled finger.

### Fix 4: Recognition Track: Reset Windows Hello

If re-enrollment fails or loops with errors, reset Hello's credential store: remove all Hello methods (PIN, fingerprint, face) under Sign-in options, restart, then set up fresh starting with the PIN. For persistent 'something went wrong' errors, delete the NGC folder at C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC (take ownership first) to force a full Hello store rebuild.

Recreate the PIN before attempting fingerprint enrollment — Hello biometrics layer on top of the PIN, and the option stays unavailable without one. Microsoft documents Hello recovery steps in its [Windows support hub](https://support.microsoft.com/en-us/windows).

1. 1. Remove all Windows Hello sign-in methods.
2. 2. Restart the laptop.
3. 3. Create a fresh PIN first.
4. 4. Enroll fingerprints again.
5. 5. Clear the NGC folder for stubborn enrollment errors.

### Fix 5: Intermittent Track: Services, Power, and Policy

For readers that work after reboot then die: check the Windows Biometric Service stays running (services.msc, Automatic), and in Device Manager uncheck power-saving on the biometric device so Windows cannot suspend it. Check Event Viewer, Windows Logs, System for biometric service crash entries around the failure times.

On business laptops, check with IT whether a group policy disables biometrics — policy blocks survive every driver fix. Also review endpoint security software for biometric restrictions. Intermittent failures with clean logs and no policy almost always resolve to the power-management fix.

1. 1. Confirm the Biometric Service stays running across reboots.
2. 2. Disable power-saving on the biometric device.
3. 3. Check Event Viewer for biometric errors at failure times.
4. 4. Rule out group policy or security software blocks.
5. 5. Reinstall the vendor driver if intermittency persists.

### Fix 6: Final Verdict: Hardware Failure

If the reader never appears in Device Manager — not under Biometric devices, not as an unknown device, not with hidden devices shown — across BIOS-enabled state and multiple driver installs, the sensor hardware or its cable has failed. Fingerprint sensors connect via small internal cables that can loosen, but they are often integrated into the palm rest or power button, making DIY repair model-dependent.

Before concluding hardware failure, test with a Linux live USB: if the reader is absent there too, it is definitively hardware. Contact the manufacturer for warranty service — biometric sensor replacement is inexpensive on most models when done as a warranty repair.

1. 1. Confirm total absence across Device Manager views.
2. 2. Verify the BIOS toggle is enabled.
3. 3. Test with a Linux live USB for a second opinion.
4. 4. Absent everywhere means hardware failure.
5. 5. Contact the maker for warranty sensor service.

## Closing

Fingerprint troubleshooting is triage: the Device Manager verdict test splits detection from recognition failures in under a minute, and each track has a short fix list. BIOS and vendor drivers handle detection; sensor cleaning and Hello resets handle recognition; power management and policy handle the intermittent cases. Diagnose the track first and the fix follows.
