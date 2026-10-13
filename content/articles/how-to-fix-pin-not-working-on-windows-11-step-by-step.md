---
title: "Windows 11 PIN Not Working? A Step-by-Step Fix Guide"
slug: how-to-fix-pin-not-working-on-windows-11-step-by-step
date: 2026-10-01
categories: ["windows-errors"]
tags: ["pin", "sign-in", "windows 11", "login error", "microsoft account"]
description: "Can't sign in with your Windows 11 PIN? Follow this step-by-step guide to fix PIN errors, reset credentials, and get back into your laptop."
thumbnail: "/images/thumbs/how-to-fix-pin-not-working-on-windows-11-step-by-step.webp"
faqs:
  - q: "Why does Windows 11 say 'something went wrong' when I enter my PIN?"
    a: "That message usually means the NGC credential folder is corrupted or the TPM state changed after an update. Renaming the Ngc folder and re-adding the PIN fixes it. It can also appear if you changed your Microsoft account password online but the laptop still caches old credentials."
  - q: "Can I sign in without the PIN?"
    a: "Yes — click 'Sign-in options' on the login screen and choose the password icon to use your Microsoft account or local account password instead. This gets you in so you can fix the PIN from inside Windows."
  - q: "What is error 0x8009002d when setting up a PIN?"
    a: "It means the TPM (Trusted Platform Module) or the NGC credential store failed to create the PIN credential. The standard fix is renaming the Ngc folder, or clearing the TPM in BIOS if that doesn't work. Back up BitLocker keys before touching the TPM."
  - q: "Will removing my PIN delete my files?"
    a: "No. Your PIN is only a sign-in credential. Removing it and adding a new one doesn't touch your files, apps, or settings. Your data is completely safe through any PIN reset procedure."
---

You type your PIN, Windows 11 shakes its head, and you're locked out of your own laptop. Or maybe the PIN option vanished entirely and all you get is "Something went wrong." Either way, it's a miserable way to start the day — but it's also one of the most fixable sign-in problems in Windows 11, because the PIN system is just a local credential store that can be rebuilt.

Before anything else: click **Sign-in options** on the login screen and try your account **password** instead. That gets most people in immediately, and every fix below is easier from inside Windows. Now let's repair the PIN properly, step by step.

## Why this happens

- **Corrupted NGC credential store.** The folder at `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc` holds your PIN; if it corrupts, the PIN stops working entirely.
- **TPM state changed.** A BIOS update, TPM clear, or motherboard-level change invalidates the PIN credential tied to the TPM chip.
- **Microsoft account password changed online.** If you reset your password on another device, the cached PIN can desync until you sign in with the new password once.
- **A Windows update damaged sign-in components.** Major updates occasionally break the credential providers that render the PIN field.
- **Group Policy or registry restrictions.** On work or school laptops, policies can disable PIN sign-in or require specific complexity that conflicts with your existing PIN.
- **Corrupted user profile.** Rare, but a damaged profile breaks everything tied to it — including Hello credentials.

## How to fix it

Work through these in order — start with Fix 1 and stop when your PIN works again.

### Fix 1: Sign in with your password, then remove and re-add the PIN

This is the fix that works for most people, and it takes two minutes.

1. On the login screen, click **Sign-in options** and select the **password** icon (the key symbol).
2. Sign in with your Microsoft account or local account password.
3. Open **Settings > Accounts > Sign-in options**.
4. Under **PIN (Windows Hello)**, click **Remove** and confirm with your password.
5. Restart the laptop, go back to the same page, and click **Set up** to create a fresh PIN.

If the PIN option is missing from Settings entirely, jump to Fix 4. If you hit error 0x8009002d during setup, skip ahead to Fix 5 — your credential store needs the deeper repair.

### Fix 2: Use "I forgot my PIN" from the login screen

Windows has a built-in PIN reset flow that many people overlook.

1. On the login screen, click **Sign-in options** and make sure the PIN method is selected.
2. Click **I forgot my PIN** below the PIN box.
3. Verify your identity with your Microsoft account password (you'll need internet access for this).
4. Set a new PIN when prompted.
5. Sign in with the new PIN.

This only works for Microsoft accounts, not local accounts. If the link doesn't appear, your account type or policy is blocking it — move to Fix 1's manual removal instead. Broader sign-in and startup failures sometimes overlap with this; if your laptop also struggles to boot cleanly, our guide on [fixing Windows 11 stuck on the restarting screen](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-hp-laptop/) may help.

### Fix 3: Delete the contents of the NGC folder

When the PIN is corrupted at the file level, you rebuild the store manually.

1. Sign in with your password (Fix 1, steps 1–2).
2. Open **File Explorer** and go to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft`.
3. Open the **Ngc** folder. If prompted, grant yourself permanent access as an administrator.
4. Delete everything inside the Ngc folder (not the folder itself).
5. Restart, then go to **Settings > Accounts > Sign-in options** and set up a new PIN.

This wipes all stored PIN and biometric credentials for every user on the machine, so everyone will need to re-add theirs. It's safe and doesn't touch personal files.

### Fix 4: Re-register the credential provider via PowerShell

If the PIN option is missing from Settings, the sign-in components may need re-registering.

1. Right-click **Start** and open **Terminal (Admin)**.
2. Run `sfc /scannow` and let it complete.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart the laptop.
5. Check **Settings > Accounts > Sign-in options** — the PIN option should be back.

If it still doesn't appear, your edition or policy may genuinely not support it (rare on Home/Pro). Check **Settings > Accounts > Sign-in options** for a message about your organization managing the setting — on personal machines, that message itself is a bug fixed by the steps above.

### Fix 5: Fix error 0x8009002d by resetting the TPM

This error during PIN setup points at the TPM.

1. Back up your BitLocker recovery key first if BitLocker is on (search **BitLocker** in Settings and save the key).
2. Press **Windows + R**, type `tpm.msc`, and press Enter to open the TPM console.
3. Click **Clear TPM** in the right-hand Actions pane and restart when prompted.
4. After reboot, Windows re-provisions the TPM automatically.
5. Go to **Settings > Accounts > Sign-in options** and set up your PIN again.

Microsoft documents TPM management in detail on the [Windows support site](https://support.microsoft.com/en-us/windows) if your firmware needs extra steps.

### Fix 6: Create a new local user account to test

This tells you whether the problem is your profile or the whole system.

1. Open **Terminal (Admin)** and run `net user TestUser *` — set a password when prompted.
2. Run `net localgroup administrators TestUser /add`.
3. Sign out and sign in as **TestUser**.
4. Go to **Settings > Accounts > Sign-in options** and try adding a PIN.
5. If the PIN works for TestUser, your original profile is corrupted — migrate your files to the new account. If it fails there too, the issue is system-wide; continue to Fix 7.

### Fix 7: Repair Windows with an in-place upgrade

When nothing else works, refresh Windows without losing anything.

1. Download the Windows 11 installation media from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run `setup.exe` from the mounted ISO or USB.
3. Choose **Keep personal files and apps** when asked.
4. Let the upgrade complete — it reinstalls Windows components including the entire sign-in stack.
5. Set up your PIN fresh afterward.

This is the nuclear option, but it's non-destructive and resolves any software-level cause. For related sign-in recovery scenarios, also see [how to disable automatic restart after a blue screen](/articles/how-to-disable-automatic-restart-after-bsod-on-windows-11/) so you can actually read error messages during troubleshooting.

## Closing

A broken PIN feels like a lockout, but it's really just a corrupted credential file — and now you know exactly how to rebuild it. In the vast majority of cases, removing and re-adding the PIN (or clearing the NGC folder once) is all it takes. Keep your Microsoft account password memorized or stored somewhere safe, because it's your master key whenever Hello credentials misbehave.
