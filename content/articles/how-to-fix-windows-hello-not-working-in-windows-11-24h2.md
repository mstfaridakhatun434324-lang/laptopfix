---
title: "How to Fix Windows Hello Not Working in Windows 11 24H2"
slug: how-to-fix-windows-hello-not-working-in-windows-11-24h2
date: 2026-10-01
categories: ["windows-errors"]
tags: ["windows hello", "biometrics", "windows 11 24h2", "fingerprint", "face recognition"]
description: "Windows Hello fingerprint or face sign-in broken after the 24H2 update? Fix biometric sign-in with these driver, service, and settings repairs."
thumbnail: "/images/thumbs/how-to-fix-windows-hello-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why did Windows Hello break after the 24H2 update?"
    a: "The 24H2 update tightened biometric security requirements and changed how Hello components register with the system. Older fingerprint and camera drivers that worked on 23H2 are not 24H2-compliant, and the update sometimes leaves the biometric stack half-migrated. Updating to 24H2-certified drivers from your laptop maker fixes most cases."
  - q: "Windows says 'Windows Hello isn't available on this device.' What now?"
    a: "That message means Windows cannot find a compatible biometric device or the driver is missing/broken. Check Device Manager for your fingerprint sensor or IR camera — a yellow warning icon or a missing Biometric devices category confirms a driver problem. Install the driver from your manufacturer's support page."
  - q: "Do I need an IR camera for face recognition?"
    a: "Yes. Windows Hello face sign-in requires an infrared camera, not just a regular webcam — the IR sensor provides the anti-spoofing depth data. If your laptop only has a standard webcam, face recognition will never be available, but fingerprint or PIN sign-in will work if that hardware exists."
  - q: "Will I lose my saved fingerprints if I reinstall the driver?"
    a: "Usually not — biometric templates are stored in the secured NGC/TPM credential store, not in the driver. But if you clear the NGC folder or the TPM as part of troubleshooting, you will need to re-enroll fingerprints and face afterward. Re-enrollment takes two minutes per method."
---
Windows 11 24H2 has been rough on Windows Hello. Fingerprint readers that worked for years suddenly report "not available," face recognition greets you with an error, and PIN setup throws codes like 0x80090016. The update raised the bar for biometric drivers, and anything not 24H2-certified can fall over.

The good news: this is a driver and configuration problem, not a hardware death. Work through the fixes below and Hello comes back.

## Why this happens

- **Non-24H2-compliant biometric drivers:** 24H2 enforces stricter driver requirements; older fingerprint/camera drivers fail to load.
- **Half-migrated Hello components:** The feature update can leave the biometric stack partially updated, breaking enrollment and recognition.
- **Corrupted NGC credential store:** The shared vault for PIN, fingerprint, and face data gets damaged during the update.
- **Windows Biometric Service disabled or stuck:** The supporting service fails to start after the update.
- **Enhanced sign-in security conflicts:** New VBS requirements in 24H2 block Hello on hardware/firmware combinations that do not fully comply.
- **Camera privacy or driver issues:** IR camera drivers break, or privacy settings block Hello's camera access.
- **TPM desynchronization:** The update disturbs the TPM state that Hello credentials are sealed to.

## How to fix it

Work through these in order, starting at Fix 1.

### Fix 1: Install 24H2-certified biometric drivers

The number one fix — get drivers built for 24H2, not carried over from 23H2.

1. Open **Device Manager** (**Win + X > Device Manager**) and expand **Biometric devices**.
2. Right-click your fingerprint sensor → **Update driver > Search automatically for drivers**.
3. Then go to your laptop manufacturer's support page, find your exact model, and download the fingerprint and camera drivers explicitly labeled for Windows 11 24H2. Install them even if Windows claims you have the latest — vendor packages are newer.
4. Restart and check **Settings > Accounts > Sign-in options** to see if Hello options are available again.

If the PIN side is broken too, our [PIN not working guide](/articles/how-to-fix-pin-not-working-on-windows-11-on-acer-laptop/) covers the NGC credential store in depth.

### Fix 2: Restart the Windows Biometric Service

A stuck service silently disables all of Hello.

1. Press **Win + R**, type `services.msc`, press Enter.
2. Find **Windows Biometric Service** → double-click → set **Startup type** to **Automatic** → click **Start** if stopped → **OK**.
3. Right-click the service and choose **Restart** even if it was already running.
4. Also confirm **Credential Manager** is running.
5. Restart the laptop and test fingerprint/face enrollment.

### Fix 3: Rebuild the NGC credential store

When the shared credential vault corrupts, every Hello method fails together.

1. Sign in with your password. Open **Terminal (Admin)** (**Win + X > Terminal (Admin)**).
2. Run:
   `takeown /f C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /r /d y`
   `icacls C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /grant administrators:F /t`
3. Delete everything inside the NGC folder via File Explorer.
4. Go to **Settings > Accounts > Sign-in options** and re-enroll your fingerprint, face, and PIN fresh.
5. Test each method at the login screen.

### Fix 4: Fix the IR camera for face recognition

Face-specific failures are usually camera-driver or privacy issues.

1. In **Device Manager**, expand **Cameras** and **System devices** — update every camera and IR sensor driver.
2. Go to **Settings > Bluetooth & devices > Cameras** and confirm the IR camera is listed and enabled.
3. Check **Settings > Privacy & security > Camera** — make sure camera access is on (Hello needs it even though it uses IR).
4. If the camera shows a black preview or error code, uninstall it in Device Manager (**Uninstall device**, check remove driver), restart, and let Windows reinstall.
5. For the PIN companion problem, see [fixing PIN issues on Dell laptops](/articles/how-to-fix-pin-not-working-on-windows-11-on-dell-laptop/).

### Fix 5: Adjust enhanced sign-in security settings

24H2's tightened VBS requirements block Hello on some firmware.

1. Open **Windows Security > Device security > Core isolation details**.
2. Try toggling **Enhanced sign-in security** off, restart, and test Hello enrollment.
3. If it works with the toggle off, update your BIOS/UEFI firmware to the latest version, then try turning the setting back on — newer firmware often restores compliance.
4. On work/school-managed devices this may be policy-locked; check with IT.

### Fix 6: Run the hardware troubleshooter and check for conflicts

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run any biometric or hardware troubleshooter offered.
2. In **Device Manager**, look for yellow warning icons on biometric, camera, TPM (**Security devices**), and USB devices — resolve each with driver updates.
3. Disconnect USB fingerprint readers/docks temporarily to rule out external hardware conflicts, then retest the built-in sensor.

### Fix 7: Update BIOS and do an in-place Windows repair

The deep fix when drivers and services check out but Hello still fails.

1. Check your BIOS version (`msinfo32`), download the latest from your manufacturer's support page, and flash it following their instructions exactly.
2. If Hello still fails, do an in-place upgrade: download the Windows 11 24H2 ISO from the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), run setup from inside Windows, and choose **Keep personal files and apps**.
3. After the repair, install the 24H2-certified biometric drivers first, then enroll Hello fresh.
4. Microsoft's Hello troubleshooting reference is on the [Windows support page](https://support.microsoft.com/en-us/windows).

### Fix 8: Re-enroll Hello after updates fully complete

A surprising number of "broken Hello" cases are just enrollment data stranded mid-migration — finishing updates and re-enrolling cleanly resolves them.

1. Go to **Settings > Windows Update** and install everything, including **Advanced options > Optional updates**. Restart as many times as prompted until no updates remain.
2. Then remove the broken enrollments: **Settings > Accounts > Sign-in options** → for each Hello method (fingerprint, face, PIN), choose **Remove**.
3. Restart once more, return to **Sign-in options**, and enroll each method fresh — fingerprint first, then face, then PIN.
4. Test each at the lock screen (**Win + L**) before calling it done. Fresh enrollment after a fully updated system succeeds where repairing the old enrollment data kept failing.

## Closing

Windows Hello on 24H2 is a driver-compliance story more than anything else: the update moved the goalposts, and older biometric drivers did not move with them. Install the 24H2-certified drivers from your laptop maker, restart the biometric service, rebuild the credential store if needed, and Hello sign-in comes back. Do the driver update before anything exotic — it resolves the clear majority of these cases on its own.
