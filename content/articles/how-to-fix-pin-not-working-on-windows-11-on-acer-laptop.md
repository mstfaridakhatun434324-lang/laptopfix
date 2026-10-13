---
title: "PIN Not Working on Windows 11? Fix It on Your Acer Laptop"
slug: how-to-fix-pin-not-working-on-windows-11-on-acer-laptop
date: 2026-09-22
categories: ["windows-errors"]
tags: ["windows hello pin", "pin not working", "acer laptop", "sign-in error", "0x80090016"]
description: "Can't sign in with your PIN on an Acer laptop running Windows 11? Clear the corrupted NGC folder, reset your PIN, and get signing in again."
thumbnail: "/images/thumbs/how-to-fix-pin-not-working-on-windows-11-on-acer-laptop.webp"
faqs:
  - q: "Why does Windows 11 say my PIN is incorrect when it isn't?"
    a: "The PIN itself is usually fine — the encrypted credential store (the NGC folder) that holds it gets corrupted, often after a Windows update. Windows then cannot verify the correct PIN and reports it as wrong. Deleting the NGC folder contents and setting up the PIN fresh resolves this in most cases."
  - q: "What is the NGC folder?"
    a: "NGC stands for Next Generation Cryptography. It is the protected folder at C:\\Windows\\ServiceProfiles\\LocalService\\AppData\\Local\\Microsoft\\NGC where Windows stores your PIN and biometric credentials. When its contents corrupt, PIN and Windows Hello sign-in break even though your password still works."
  - q: "Will resetting my PIN delete anything?"
    a: "No. Resetting or re-creating your PIN only affects that one sign-in method. Your files, apps, Microsoft account, and password are untouched. You will need your account password (or another verification method) once to authorize the new PIN."
  - q: "What if the PIN option is greyed out in Settings?"
    a: "This usually means a policy or security setting is blocking Hello PIN setup — commonly 'enhanced sign-in security' (VBS) on a device whose hardware does not fully support it, or a work/school account policy. Check Settings, Accounts, Sign-in options, and if needed toggle the enhanced security setting under Windows Security, Device security, Core isolation."
---
You type your PIN — the one you have used a hundred times — and Windows 11 tells you it is incorrect, or the PIN field does not appear at all, or you get error 0x80090016. Your password still works, which makes it extra maddening. This is an extremely common issue on Acer laptops after Windows updates, and it is fixable in about ten minutes.

The root cause is almost always a corrupted credential store, not a forgotten PIN. Here's how to clear it out and set up a fresh one.

## Why this happens

- **Corrupted NGC credential folder:** The encrypted store holding your PIN gets damaged during updates, and Windows can no longer validate the PIN you type.
- **TPM (Trusted Platform Module) glitches:** The PIN is sealed to the TPM chip; if the TPM state gets out of sync after a firmware or Windows update, PIN verification fails.
- **A Windows update breaks the Hello components:** Updates sometimes leave the biometric/PIN stack half-migrated, especially on 24H2.
- **Changed motherboard or major hardware change:** The PIN is bound to the device's TPM — significant hardware changes invalidate it by design.
- **Corrupted user profile credential files:** Damage in your profile's credential storage breaks PIN sign-in while leaving password sign-in working.
- **Enhanced sign-in security conflicts:** Virtualization-based security settings can block PIN setup on hardware configurations that do not fully support them.
- **Acer bloatware or credential managers:** Preinstalled utilities that hook into sign-in (fingerprint software, credential managers) occasionally interfere after updates.

## How to fix it

Work through these in order, starting at Fix 1. You will need your Microsoft account password (or another sign-in method) for a couple of these steps.

### Fix 1: Clear the NGC folder and recreate your PIN

This is the definitive fix for the corrupted-credential-store problem, and it works in the majority of cases.

1. Sign in with your **password** instead of the PIN (click **Sign-in options** on the login screen and choose the password icon).
2. Open **File Explorer** and navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC`. (You may need to click through permission prompts.)
3. If Windows denies access, take ownership: open **Terminal (Admin)** (**Win + X > Terminal (Admin)**) and run:
   `takeown /f C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /r /d y`
   then `icacls C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /grant administrators:F /t`
4. Delete everything inside the NGC folder (not the folder itself).
5. Go to **Settings > Accounts > Sign-in options**, click **PIN (Windows Hello)**, and choose **Set up**. Enter your password when asked, then create your new PIN.
6. Sign out and test the PIN on the login screen.

If your fingerprint or face sign-in is also broken, our [Windows Hello not working guide](/articles/how-to-fix-windows-hello-not-working-in-windows-11-24h2/) covers the biometric side of the same credential system.

### Fix 2: Use the "I forgot my PIN" reset

If you cannot reach the NGC folder, the built-in reset does the same job through the official channel.

1. On the login screen, click **Sign-in options** and select the PIN icon.
2. Click **I forgot my PIN** below the PIN box.
3. Verify your identity with your Microsoft account password or the emailed code.
4. Create a new PIN when prompted and sign in with it.

### Fix 3: Reset the TPM

When the TPM and Windows disagree about the PIN's encryption, clearing the TPM forces a fresh handshake.

1. Press **Win + R**, type `tpm.msc`, and press Enter.
2. In the Actions pane on the right, click **Clear TPM** and restart when prompted.
3. After reboot, Windows re-provisions the TPM automatically.
4. Go to **Settings > Accounts > Sign-in options** and set up your PIN again.
5. Note: on a BitLocker-encrypted drive, have your BitLocker recovery key handy before clearing the TPM — you can find it in your Microsoft account online.

### Fix 4: Reinstall the biometric and TPM drivers

Corrupted Hello-related drivers break PIN setup even when the credential store is fine.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Expand **Biometric devices** and **Security devices** (TPM).
3. Right-click each device, choose **Uninstall device**, and check **Attempt to remove the driver** if offered. Do not worry — Windows reinstalls them.
4. Restart the laptop. Windows detects the hardware and installs fresh drivers.
5. Then set up your PIN again under **Settings > Accounts > Sign-in options**.
6. For the latest Acer-specific drivers, check Acer's official support downloads for your model after Windows reinstalls the generics.

### Fix 5: Toggle enhanced sign-in security

Virtualization-based sign-in protection can block PIN creation on some Acer configurations.

1. Open **Windows Security** from the Start menu.
2. Go to **Device security > Core isolation details**.
3. If **Enhanced sign-in security** (or Memory integrity) is on, try turning it **off**, restart, and set up the PIN.
4. If the PIN works with it off, you can try turning it back on afterward — sometimes the toggle itself clears the conflict.
5. If your device is managed by a school or workplace, this setting may be locked by policy — contact your IT admin in that case.

### Fix 6: Create a fresh user profile

If the PIN fails for your account but works for a new one, your profile's credential storage is damaged beyond the NGC fix.

1. Go to **Settings > Accounts > Other users** and click **Add account**.
2. Create a local account (choose **I don't have this person's sign-in information > Add a user without a Microsoft account**).
3. Sign into the new account and set up a PIN there to confirm it works.
4. Move your files from `C:\Users\<oldname>` to the new profile, reinstall needed apps, and switch to the new account permanently.

### Fix 7: Repair Windows with an in-place upgrade

When nothing else works, refresh Windows while keeping everything.

1. Go to the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and download the Installation Assistant or ISO.
2. Run setup from inside Windows, choose **Keep personal files and apps**, and let it reinstall.
3. After completion, set up your PIN fresh. This repairs the Hello stack at the OS level without touching your data.
4. Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows) has the full in-place upgrade walkthrough if you want step-by-step screenshots.

## Closing

A PIN that suddenly "stops working" is one of those problems that feels personal — it rejects you at your own front door. But it is really just a corrupted credential file in most cases, and clearing the NGC folder plus a fresh PIN setup resolves it quickly. If you find yourself repeating this fix after every update, keep an eye on your TPM driver and the enhanced sign-in security toggle, since those two are the usual repeat offenders on Acer hardware. For the general PIN failure codes and flows that apply to every brand, see our [PIN troubleshooting overview](/articles/how-do-i-fix-pin-not-working-on-windows-11/).
