---
title: "Best Way to Fix PIN Not Working on Windows 11"
slug: best-way-to-fix-pin-not-working-on-windows-11
date: 2026-10-05
categories: ["windows-errors"]
tags: ["pin", "sign-in", "windows-hello"]
description: "Windows 11 PIN not working or the option is missing? Here's the best fix order — from the Ngc folder reset to TPM and account repairs."
thumbnail: "/images/thumbs/best-way-to-fix-pin-not-working-on-windows-11.webp"
faqs:
  - q: "Why does Windows 11 say my PIN is incorrect when it's right?"
    a: "The PIN itself is rarely the problem — the encrypted PIN data stored in the Ngc folder is usually corrupted, so Windows can't verify what you typed. Corruption happens after updates, disk errors, or interrupted sign-ins. Deleting the Ngc folder contents and re-adding the PIN fixes it."
  - q: "What if the PIN option is completely missing from sign-in options?"
    a: "That usually means the TPM is disabled or cleared in BIOS, the PIN credential provider failed to load, or a policy/registry change hid it. Check that TPM is enabled in BIOS, and verify the PIN option exists under Settings, then Accounts, then Sign-in options."
  - q: "Will resetting my PIN delete anything?"
    a: "No. Removing and re-adding a PIN only affects that sign-in credential. Your files, apps, password, and Microsoft account are untouched. You'll sign in with your password once after the reset, then create a fresh PIN."
  - q: "Can I use Windows without a PIN?"
    a: "Yes — the PIN is optional. You can always sign in with your Microsoft account password, and you can remove the PIN entirely under Settings, then Accounts, then Sign-in options, then PIN. But the PIN is actually more secure against remote attacks than a password, so fixing it is better than dropping it."
---
"Something happened and your PIN isn't available." Click here to set up your PIN again — and then setup fails too. Or the PIN field rejects a code you know is right. PIN problems on Windows 11 are common after updates, and they're almost never about the PIN you typed. The encrypted credential store behind it got corrupted, and Windows can't verify anything until that's rebuilt. For a symptom-by-symptom diagnostic approach, see our full [PIN troubleshooting guide](/articles/pin-not-working-on-windows-11-troubleshooting/).

There are several ways to fix it floating around, but they're not equal — some are quick and safe, others are destructive overkill. Here's the best order: the Ngc reset first (fixes most cases in minutes), then the account and TPM checks, with the heavy options last.

## Why this happens

- **Corrupted Ngc folder** — the encrypted store holding your PIN data gets damaged by updates, disk errors, or interrupted sign-ins.
- **TPM issues** — the Trusted Platform Module (which protects the PIN) was cleared, disabled in BIOS, or hit a firmware bug.
- **Microsoft account sync problems** — the local PIN credential falls out of sync with the account, especially after password changes.
- **Corrupted user profile** or damaged credential manager components.
- **A Windows update** breaking the PIN credential provider.
- **Third-party "privacy" tools** disabling Windows Hello components or the TPM-related services.

## How to fix it

Work through these in order, from quickest to most involved.

### Fix 1: Reset the Ngc folder (the best fix)

This resolves the majority of PIN failures and takes five minutes.

1. Sign in with your **password** instead — click **Sign-in options** on the login screen and choose the password icon.
2. Open File Explorer and navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc`. You'll need to take ownership: right-click **Ngc** → **Properties** → **Security** → **Advanced** → change owner to your account, grant yourself full control.
3. Delete **everything inside** the Ngc folder (not the folder itself).
4. Go to **Settings** → **Accounts** → **Sign-in options** → **PIN (Windows Hello)** → **Set up**, and create a fresh PIN.

### Fix 2: Use the "I forgot my PIN" flow

If you can't be bothered with folder permissions, the built-in reset does the same job.

1. On the login screen, click **Sign-in options** and sign in with your password.
2. Go to **Settings** → **Accounts** → **Sign-in options** → **PIN (Windows Hello)**.
3. Click **Remove**, confirm, then click **Add** and set a new PIN.
4. If **Remove** is greyed out, use Fix 1's Ngc deletion instead — it bypasses the UI entirely.

### Fix 3: Check TPM status in BIOS and Windows

No working TPM, no working PIN — it's that simple.

1. Press **Win + R**, type `tpm.msc`, and press Enter. The TPM Management console should show **"The TPM is ready for use."**
2. If it shows an error or "TPM not found," restart into BIOS/UEFI and confirm TPM (or **PTT** on Intel, **fTPM** on AMD) is **Enabled**.
3. While in BIOS, check for a TPM firmware update from your laptop maker's support site — TPM firmware bugs have broken PINs on several laptop lines.
4. After enabling TPM, boot into Windows and re-add the PIN via **Sign-in options**.

### Fix 4: Fix Microsoft account sync

A password change or account hiccup can orphan the local PIN credential.

1. Go to **Settings** → **Accounts** → **Your info** and confirm you're signed in with the correct Microsoft account.
2. If you recently changed your Microsoft account password, sign out and back in: **Settings** → **Accounts** → **Your info** → **Sign in with a local account instead**, restart, then switch back to the Microsoft account.
3. Re-add the PIN afterward via **Sign-in options**.
4. Check account.microsoft.com in a browser to confirm the account itself is healthy and not locked.

For deeper PIN troubleshooting workflows, our companion guide to [PIN problems on Windows 11](/articles/how-to-fix-pin-not-working-on-windows-11-on-lenovo-laptop/) covers additional account-repair steps.

### Fix 5: Repair system files

Damaged credential components break PIN verification even with a healthy Ngc folder.

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart and try the PIN again — or re-add it if you cleared the Ngc folder earlier.
4. If SFC reports unfixable corruption, run DISM first and then SFC again; order matters.

### Fix 6: Check the credential-related services

The PIN depends on background services that "tweaking" tools love to disable.

1. Press **Win + R**, type `services.msc`, and verify these are running: **Credential Manager**, **CNG Key Isolation**, **TPM Base Services**.
2. Set any Disabled ones to **Automatic**, start them, and restart.
3. If you ever ran a "debloat" or "privacy" script, that's likely what broke them — consider undoing its changes.
4. Re-add the PIN after the services are healthy.

### Fix 7: Test a new user profile

If the PIN works on a fresh account, your profile's credential store is damaged beyond the Ngc fix.

1. Create a new local account: **Settings** → **Accounts** → **Other users** → **Add account**.
2. Sign in as the new user, link your Microsoft account, and set up a PIN.
3. If the PIN works there, migrate your files to the new profile.
4. If it fails there too, the problem is system-level — continue to Fix 8.

### Fix 8: In-place repair install (last resort)

For system-level PIN breakage that survives everything above.

1. Back up your files.
2. Create Windows 11 media from the [official download page](https://www.microsoft.com/en-us/software-download/windows11) and run setup from inside Windows, keeping files and apps.
3. After the repair, sign in with your password first, verify TPM is healthy (`tpm.msc`), then add a fresh PIN.
4. If even this fails, check with your laptop maker's support — a TPM hardware fault is rare but real, and it's a warranty issue.

## Closing

PIN failures are a credential-store problem, not a typing problem — which is why retyping the PIN harder never helps, but deleting the Ngc folder usually does. Work the list from the Ngc reset through TPM and account checks, and you'll have a working PIN again without touching your files. And once it's fixed, leave the TPM and Hello components alone: the "privacy" scripts that disable them are the number-one cause of encore performances.
