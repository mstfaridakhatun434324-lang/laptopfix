---
title: "Windows 11 PIN Not Working on a Lenovo Laptop? Here's How to Fix It"
slug: how-to-fix-pin-not-working-on-windows-11-on-lenovo-laptop
date: 2026-09-17
categories: ["windows-errors"]
tags: ["windows 11", "lenovo", "pin sign-in"]
description: "PIN not working on your Lenovo Windows 11 laptop? Fix the corrupted Ngc folder, TPM hiccups, and account glitches with these proven steps now."
thumbnail: "/images/thumbs/how-to-fix-pin-not-working-on-windows-11-on-lenovo-laptop.webp"
faqs:
  - q: "Why does my PIN break after every BIOS update?"
    a: "The PIN is cryptographically sealed to the TPM, and BIOS updates can change the TPM's measurements or firmware state. When the seal no longer matches, Windows rejects the PIN as a security measure — it cannot distinguish a legitimate firmware update from tampering. Deleting the Ngc folder and recreating the PIN re-seals it to the new state."
  - q: "Is a PIN less secure than a password?"
    a: "For local device security, a PIN is actually stronger in practice: it is tied to the TPM on that specific device and never transmitted over the network, while a password can be phished or replayed from anywhere. A short PIN backed by the TPM beats a long password typed into a fake login page."
  - q: "The PIN option is completely missing from Sign-in options. Why?"
    a: "Usually a policy or a broken Hello stack. Check Settings, Accounts, Sign-in options for a message about requirements. On work or school devices, administrators can disable Hello via policy. On personal devices, run the SFC/DISM repairs in Fix 5 — a damaged Hello infrastructure hides the PIN option entirely."
  - q: "Can I use fingerprint instead while the PIN is broken?"
    a: "Only if fingerprint was set up before the failure — and often it breaks too, since both depend on the same Hello credential store and TPM state. Fix the underlying store with the Ngc deletion first; then re-enroll both PIN and fingerprint fresh. Setting up biometrics on a corrupted store just wastes time."
---

You type your PIN — the one you have used a thousand times — and Windows 11 says it is incorrect, or the PIN option vanishes entirely, or you get the dreaded something happened and your PIN isn't available. On Lenovo laptops (ThinkPad, IdeaPad, Yoga), PIN failures cluster around a few known causes: a corrupted PIN credential store, a TPM hiccup after a BIOS or Windows update, or the account itself getting tangled.

The fixes below start with the immediate workaround that gets you signed in today (your password still works), then repair the PIN system itself. None of them risk your files, and most take under ten minutes.

## Why this happens

- **Corrupted Ngc folder:** your PIN is stored encrypted in `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc`. If that folder corrupts, every PIN attempt fails.
- **TPM state changed:** the PIN is sealed to the TPM chip. A BIOS update, TPM firmware update, or clearing the TPM invalidates the stored PIN.
- **Windows update broke Hello:** feature updates occasionally damage the Windows Hello credential plumbing, breaking PIN, fingerprint, and face sign-in together.
- **Account sync issues:** for Microsoft accounts, a password change or security event can desync the local PIN credential.
- **Lenovo Vantage or BIOS updates:** firmware updates that touch the TPM or secure boot chain commonly trigger PIN failures on the next boot.
- **Corrupted user profile:** in rare cases the profile's credential store is damaged beyond the Ngc folder, and only profile-level repair helps.

## How to fix it

Work through these in order, from the quickest checks to the deeper repairs. Most people are back up and running by Fix 4 or 5.

### Fix 1: Sign in with your password instead

First, get into Windows. Your Microsoft account or local account password always works as a fallback, even when Hello is completely broken.

1. On the sign-in screen, click **Sign-in options** under the PIN box.
2. Select the password icon (the key symbol) and enter your account password.
3. If you forgot the password too, click **I forgot my password** and follow the Microsoft account recovery on another device.
4. Once inside Windows, do not just set a new PIN yet — a broken credential store will corrupt the new one too. Continue to Fix 2 first.
5. If this is a work laptop with no password option visible, contact your IT admin — organization policies may restrict sign-in methods, as [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) explains.

### Fix 2: Delete the Ngc folder and recreate the PIN

This is the definitive fix for most PIN failures. Deleting the corrupted credential folder forces Windows to build a fresh one.

1. Open **File Explorer**, click **View > Show > Hidden items** so system folders are visible.
2. Navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft`.
3. Right-click the **Ngc** folder and delete it. You will need administrator permission — click **Continue** through the prompts.
4. If deletion is denied, take ownership first: right-click Ngc, **Properties > Security > Advanced > Change** owner to your account, tick **Replace owner on subcontainers**, apply, then delete.
5. Go to **Settings > Accounts > Sign-in options > PIN (Windows Hello)** and click **Set up** to create a fresh PIN. Test it with a lock (**Win + L**) and unlock cycle.

### Fix 3: Toggle the TPM-related settings

When the PIN broke right after a BIOS or firmware update, the TPM binding is the issue. Re-establishing it fixes the seal.

1. Press **Win + R**, type `tpm.msc`, and press Enter. Check the status reads **The TPM is ready for use**.
2. If it shows an error, restart into BIOS (**Settings > System > Recovery > Advanced startup > Restart now**, then **Troubleshoot > UEFI Firmware Settings**), find the **Security** tab, and ensure **TPM / Security Chip** is enabled.
3. Back in Windows, open an elevated PowerShell and run `Clear-Tpm` only if you have your BitLocker recovery key handy — clearing the TPM without it can lock an encrypted drive.
4. After any TPM change, delete the Ngc folder again (Fix 2) and set up a fresh PIN so it seals to the current TPM state.
5. Lenovo's [support site](https://support.lenovo.com/us/en/) documents TPM firmware updates per model if `tpm.msc` shows a firmware problem.

### Fix 4: Remove and re-add the PIN through Settings

Sometimes the gentler path works: Windows lets you remove the broken PIN and set up a new one without touching system folders.

1. Go to **Settings > Accounts > Sign-in options > PIN (Windows Hello)**.
2. Click **Remove** and confirm. (If Remove is greyed out, Fix 2's folder deletion bypasses this.)
3. Restart the laptop — this clears cached credential state.
4. Return to the same page and click **Set up**, following the prompts to create a new PIN.
5. Test thoroughly: lock with **Win + L**, unlock with the PIN, then do a full restart and test again. One successful unlock is not enough — test the cold-boot path too.

### Fix 5: Fix Windows Hello with SFC and the Hello services

If PIN, fingerprint, and face sign-in all broke together, the Hello infrastructure itself is damaged rather than just your PIN.

1. Open an elevated Command Prompt and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Press **Win + R**, type `services.msc`, and verify **Windows Biometric Service** and **Credential Manager** are both running.
3. Open **Settings > Accounts > Sign-in options** and check whether the Windows Hello options show errors — a persistent **Something happened** message after SFC points to Fix 6.
4. Also check **Settings > Windows Update** and install everything — Microsoft has shipped Hello-specific fixes in cumulative updates.
5. The related [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) can help if you need a minimal environment to run these repairs, and the [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the wider crash family.

### Fix 6: Switch to a local account and back (Microsoft accounts)

For Microsoft-account sign-ins with a desynced credential, breaking and remaking the account link clears the desync.

1. Go to **Settings > Accounts > Your info** and click **Sign in with a local account instead**. Follow the wizard (your files stay put).
2. Restart, sign in with the local account, and delete the Ngc folder once more (Fix 2).
3. Return to **Settings > Accounts > Your info** and click **Sign in with a Microsoft account instead**. Complete the sign-in.
4. Set up a fresh PIN under **Sign-in options**. The new PIN seals against the freshly linked account state.
5. If your organization manages the device (school/work), skip this fix — account switching may violate policy. Ask IT instead.

### Fix 7: Create a fresh user profile

The last resort for profile-level credential corruption. A new profile gets a pristine credential store.

1. Go to **Settings > Accounts > Other users > Add account** and create a new local administrator account.
2. Sign into the new account and set up a PIN there. If it works, the old profile's credential store is the problem.
3. Copy your files from `C:\Users\<oldname>` to the new profile (Documents, Desktop, Downloads, etc.).
4. Reinstall or re-sign-in to apps as needed, then remove the old account from **Other users** once you are confident everything moved.
5. Before deleting, double-check browser passwords and app licenses migrated — that is the one thing people forget.

## Closing

A broken PIN on a Lenovo is rarely a real security problem — it is a corrupted credential folder or a TPM state change, both fixable in minutes. Sign in with your password, delete the Ngc folder, set up a fresh PIN, and test it through a full restart. If it breaks again after the next BIOS update, you will know exactly why and exactly what to do.
