---
title: "Windows Hello Stopped Working and Blue Screens: Fix It"
slug: windows-hello-not-working-blue-screen-error-fix
date: 2026-10-01
categories: ["windows-errors"]
tags: ["windows hello", "blue screen", "biometric"]
description: "Windows Hello failing with blue screens on your laptop? Fix the camera, fingerprint, and driver conflicts behind this frustrating combination."
thumbnail: "/images/thumbs/windows-hello-not-working-blue-screen-error-fix.webp"
faqs:
  - q: "Why does Windows Hello cause blue screens?"
    a: "Windows Hello itself rarely crashes the system — the blue screens come from the biometric drivers underneath it. Faulty camera, infrared, or fingerprint drivers can crash when Hello activates them at the login screen, especially after a driver or Windows update changed the driver stack."
  - q: "How do I fix Windows Hello not recognizing my face or fingerprint?"
    a: "Go to Settings > Accounts > Sign-in options, remove the existing face or fingerprint data, and set it up again. If the option is greyed out, the biometric driver is missing or broken — reinstall it from your laptop maker's support page and the option will return."
  - q: "Can I disable Windows Hello to stop the crashes?"
    a: "Yes, as a diagnostic step. Remove all Hello sign-in methods under Settings > Accounts > Sign-in options and sign in with your password or PIN instead. If the blue screens stop, you have confirmed the biometric driver stack is the trigger and can focus your fix there."
  - q: "What if the camera doesn't work at all, even outside Hello?"
    a: "Then the camera driver or hardware is the problem, not Hello specifically. Check Device Manager for the camera under Cameras or Imaging devices, reinstall the driver from the manufacturer, and check the physical privacy shutter — many laptops have one, and a surprising number of 'broken camera' reports end there."
---
Windows Hello failing is annoying. Windows Hello failing *and* blue-screening is a special kind of frustrating, because the crash often happens at the login screen — the worst possible moment. The good news: these two symptoms usually share one cause, which is the biometric driver stack (camera, IR sensor, or fingerprint reader) misbehaving when Hello tries to use it.

The strategy is simple: stabilize the crashes first by sidestepping Hello, then repair the biometric drivers properly, then re-enable Hello on a solid foundation. Don't try to fix Hello while the system is still crashing.

## Why this happens

- **A faulty biometric driver crashes at login.** When Hello activates the IR camera or fingerprint reader, a buggy driver throws the system into a blue screen.
- **A Windows or driver update broke the biometric stack.** Updates frequently replace working camera or fingerprint drivers with incompatible versions.
- **Corrupted Hello enrollment data.** Damaged face or fingerprint templates can cause the authentication service to fail repeatedly.
- **Conflicting security software.** Third-party antivirus or endpoint tools that hook the login process can clash with Hello's components.
- **Camera privacy shutter or disabled device.** A physical shutter or a disabled camera in Device Manager makes Hello fail — though this causes errors, not blue screens, it often accompanies the driver mess.
- **TPM or firmware issues.** Hello's security depends on the TPM; firmware problems there can cascade into authentication failures.

## How to fix it

Work through these in order — stop the crashes first, then rebuild Hello.

### Fix 1: Bypass Hello to stabilize the system

Remove the crash trigger so you can work on the machine calmly.

1. Boot into **Safe Mode** if login-screen crashes block you (**Shift + Restart > Troubleshoot > Advanced options > Startup Settings**, press **4**).
2. Go to **Settings > Accounts > Sign-in options** and remove **Facial recognition** and **Fingerprint recognition** entries.
3. Set up a **PIN** if you don't have one — it's the fastest reliable sign-in while Hello is out of commission.
4. Restart normally and confirm the blue screens stop. If they do, the biometric driver stack is confirmed as the trigger.

### Fix 2: Identify the crashing driver from the dump

If blue screens occurred, the dump names the driver — don't skip this evidence.

1. Open the newest minidump in `C:\Windows\Minidump\` with **WinDbg Preview** and run `!analyze -v`.
2. Look for camera (`usbvideo.sys`, vendor camera drivers), IR, or fingerprint driver files in the blame line.
3. Note the exact driver name — you'll target it specifically in the next step instead of updating drivers blindly. A misbehaving camera driver can also cause [SYSTEM_THREAD_EXCEPTION_NOT_HANDLED](/articles/how-do-i-fix-system-thread-exception-not-handled/) crashes.

### Fix 3: Reinstall the biometric drivers from the manufacturer

Generic Windows drivers for IR cameras and fingerprint readers are a frequent source of this exact problem.

1. Open **Device Manager** and expand **Biometric devices**, **Cameras**, and **Imaging devices**.
2. Right-click each Hello-related device (IR camera, fingerprint sensor), choose **Uninstall device**, and tick **Attempt to remove the driver for this device**.
3. Restart, then download the proper drivers from your laptop maker's support page — search for camera, IR, and fingerprint drivers for your exact model.
4. Install them in this order: chipset, then camera/IR, then fingerprint reader, restarting between each if the installer asks.

### Fix 4: Clear and re-enroll Hello data

Corrupted enrollment templates cause persistent Hello failures even with good drivers.

1. Go to **Settings > Accounts > Sign-in options**.
2. Under each Hello method, click **Remove** to delete the stored face/fingerprint data.
3. Restart the laptop, return to **Sign-in options**, and set up facial recognition and fingerprint fresh.
4. During face setup, ensure good lighting and remove glasses if you normally wear them — poor enrollment data causes intermittent failures that look like bugs.

### Fix 5: Check the TPM and related services

Hello's cryptography depends on the Trusted Platform Module running correctly.

1. Press **Win + R**, type `tpm.msc`, and confirm the TPM is present and ready — status should read "The TPM is ready for use."
2. Open **Services** and verify **Windows Biometric Service** is running and set to **Automatic**.
3. If the TPM shows an error, check your BIOS for TPM settings (sometimes labeled PTT on Intel or fTPM on AMD) and ensure it's enabled.
4. A TPM that won't initialize after a BIOS update may need the BIOS re-flashed or defaults loaded.

### Fix 6: Repair system files and update Windows

Damaged system components behind Hello cause failures no driver update fixes.

1. Open an elevated **Command Prompt** and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Go to **Settings > Windows Update** and install all pending updates — Microsoft periodically fixes Hello and biometric framework bugs.
3. Restart and test Hello again. If a specific update broke Hello originally, check the [update troubleshooting guide](/articles/troubleshoot-blue-screen-after-windows-11-update/) for rollback steps.

### Fix 7: Rule out hardware failure

If software fixes all fail, the sensor itself may be dying.

1. Test the camera in the **Camera** app — if it shows nothing there either, the issue is hardware or its driver, not Hello.
2. Test the fingerprint reader enrollment — repeated "couldn't recognize" during setup with clean fingers suggests a worn sensor.
3. Run your manufacturer's hardware diagnostics on the camera and biometric devices.
4. A failed sensor on a laptop under warranty is a manufacturer repair; out of warranty, an external USB fingerprint reader is a cheap workaround that works fine with Hello.

## Closing

When Windows Hello and blue screens arrive together, treat it as a driver problem wearing a Hello costume: bypass Hello to stop the crashes, reinstall the biometric drivers from your laptop maker, clear the enrollment data, and re-enable Hello last. The login screen becomes boring again, which is exactly what you want. For the broader picture on reading crash dumps to identify any faulty driver, Microsoft's [Windows support documentation](https://support.microsoft.com/en-us/windows) covers the built-in recovery and diagnostic tools.
