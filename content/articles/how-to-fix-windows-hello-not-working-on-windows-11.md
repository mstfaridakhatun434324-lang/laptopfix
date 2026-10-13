---
title: "How to Fix Windows Hello Not Working on Windows 11"
slug: how-to-fix-windows-hello-not-working-on-windows-11
date: 2026-09-11
categories: ["windows-errors"]
tags: ["windows hello", "windows 11", "biometric login"]
description: "Windows Hello face or fingerprint sign-in stopped working? Fix driver, PIN, and compatibility issues so password-free login works again."
thumbnail: "/images/thumbs/how-to-fix-windows-hello-not-working-on-windows-11.webp"
faqs:
  - q: "Why does Windows Hello say 'this option is currently unavailable'?"
    a: "That message usually means Windows cannot find compatible biometric hardware, the camera or fingerprint driver failed to load, or a Windows update broke the Hello components. Updating biometric drivers and re-registering your face or fingerprint clears it in most cases."
  - q: "Will removing my PIN break Windows Hello?"
    a: "Yes, temporarily. A PIN is the required fallback for Windows Hello, so you cannot use face or fingerprint sign-in without one. If Hello is broken, remove the PIN, restart, set a fresh PIN, and then re-enroll your biometrics."
  - q: "Can a Windows update disable Windows Hello?"
    a: "It can break it. Updates sometimes replace the camera or fingerprint driver with an incompatible version. Rolling back that driver or reinstalling the manufacturer's version usually restores Hello."
  - q: "Does Windows Hello work on all Windows 11 laptops?"
    a: "No. Face sign-in needs an infrared camera with special hardware, and fingerprint sign-in needs a fingerprint reader. If your laptop lacks the hardware, the options stay greyed out no matter what software fixes you try."
---

You lift the lid, the camera should recognize you and log you in, and instead Windows Hello shows an error or quietly falls back to asking for your password. Or the fingerprint reader does nothing at all when you touch it. Losing password-free sign-in is more than an inconvenience, because Hello also backs the PIN and passkeys that protect your account.

The fix depends on whether this ever worked. If it worked yesterday, the cause is almost certainly a driver or update glitch. If it never worked on this laptop, the hardware may simply not support it. The steps below cover both situations, in the order a technician would try them.

## Why this happens

- **Broken biometric driver.** Windows updates frequently replace the IR camera or fingerprint driver with an incompatible version, and Hello stops recognizing the hardware.
- **Corrupted PIN.** Windows Hello depends on the PIN as its foundation. A damaged PIN store disables face and fingerprint sign-in with it.
- **Failed Windows update.** An interrupted or buggy update can leave the Hello components half-installed.
- **Camera privacy settings.** If Windows camera access is disabled, face recognition has no video feed and silently fails.
- **Incompatible hardware.** Budget laptops often lack the infrared camera Hello face sign-in requires, so the option is unavailable by design.
- **Fast Startup or hybrid sleep.** On some laptops, the biometric sensor does not reinitialize properly after hybrid sleep, and Hello only works after a full restart.
- **Corrupted biometric database.** The stored face or fingerprint templates can become damaged, and Hello refuses to match against them.
- **TPM or secure boot changes.** Windows Hello stores its keys in the TPM chip. If a BIOS update clears or resets the TPM, Hello loses its keys and stops working until you set it up again.

## How to fix it

Work through these in order, starting with the quickest fixes first.

### Fix 1: Restart fully and check for updates

1. Hold **Shift** and click **Power** > **Restart** to do a full restart instead of a hybrid shutdown.
2. When you are back in Windows, open **Settings** > **Windows Update** and install every pending update.
3. Restart again and test Hello. Many Hello breakages are fixed by a cumulative update you simply had not installed yet.

### Fix 2: Update the camera and fingerprint drivers

1. Open **Device Manager** with **Windows key + X**.
2. Expand **Biometric devices** and **Cameras**. If your fingerprint reader appears under **Human Interface Devices**, check there too.
3. Right-click each biometric device and choose **Update driver** > **Search automatically for drivers**.
4. For the best results, get the driver from your laptop maker's support page instead: [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), or [Lenovo support](https://support.lenovo.com/us/en/).
5. Restart after updating.

### Fix 3: Check camera permissions

1. Open **Settings** > **Privacy & security** > **Camera**.
2. Make sure **Camera access** is turned on.
3. Scroll down and confirm that **Let desktop apps access your camera** is enabled.
4. While you are here, open the built-in **Camera** app. If it shows an error, the camera hardware or driver is the problem, not Hello itself.

### Fix 4: Remove and re-add your PIN

A fresh PIN rebuilds the foundation Hello stands on.

1. Open **Settings** > **Accounts** > **Sign-in options**.
2. Under **PIN (Windows Hello)**, click **Remove** and confirm. You may need to verify with your Microsoft account password.
3. Restart the laptop.
4. Return to **Sign-in options** and click **Set up** under PIN. Create a new PIN.
5. Now re-enroll face recognition or your fingerprint using the **Set up** buttons in the same screen.

### Fix 5: Delete the corrupted biometric data

If re-enrollment fails, wipe the stored templates.

1. Open an elevated Terminal (**Windows key + X** > **Terminal (Admin)**).
2. Stop the biometric service: `net stop WbioSrvc`.
3. Open File Explorer and navigate to `C:\Windows\System32\WinBioDatabase`. Back up the files there, then delete them.
4. Restart the laptop. Windows recreates the database automatically.
5. Go back to **Settings** > **Accounts** > **Sign-in options** and enroll your face or fingerprint from scratch.

### Fix 6: Disable Fast Startup

1. Press **Windows key + R**, type `powercfg.cpl`, and press Enter.
2. Click **Choose what the power buttons do**, then **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
4. Shut down fully, power back on, and test Hello. On some laptops the sensor only initializes correctly after a true cold boot.

### Fix 7: Roll back the driver or reset Hello components

1. In **Device Manager**, right-click the biometric device, choose **Properties** > **Driver**, and click **Roll Back Driver** if the option is active. This is ideal when Hello broke right after an update.
2. If the fingerprint reader still fails, run a system file check: `sfc /scannow` in an elevated Terminal.
3. As a final step, use **Settings** > **System** > **Recovery** > **Fix problems using Windows Update** to repair Windows in place without losing files.

### Fix 8: Check TPM and enhanced sign-in security

Windows Hello leans on the TPM chip, so check it when nothing else works.

1. Press **Windows key + R**, type `tpm.msc`, and press Enter.
2. The status should read **The TPM is ready for use**. If it shows an error, you may need to clear the TPM from the BIOS security settings and set Hello up again from scratch.
3. In **Settings** > **Accounts** > **Sign-in options**, scroll down and try toggling **Require Windows Hello sign-in for Microsoft accounts** off and on. This forces Windows to rebuild its sign-in configuration.
4. Related reading: our guide on [Windows 11 install error 0x80070002](/articles/what-to-do-if-windows-11-install-error-0x80070002/) covers the in-place repair path, and if your sign-in problems extend to error codes during updates, the [0x80070057 fix](/articles/error-code-0x80070057-fix/) is worth a look. Microsoft's account sign-in help is on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

## Closing

Windows Hello usually fails for boring reasons: a driver Windows Update swapped out, a corrupted PIN, blocked camera access, or a TPM that got reset during a BIOS update. Work through the list, re-enroll your biometrics with a fresh PIN, and Hello comes back to life in most cases. If the options stay greyed out after every fix, check your laptop's spec sheet, because some machines simply lack the infrared camera or fingerprint reader that Hello needs, and no software fix can add hardware that is not there.
