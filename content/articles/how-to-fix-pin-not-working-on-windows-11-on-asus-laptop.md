---
title: "PIN Not Working on Windows 11? Fix It on Your ASUS Laptop"
slug: how-to-fix-pin-not-working-on-windows-11-on-asus-laptop
date: 2026-09-24
categories: ["windows-errors"]
tags: ["windows hello pin", "pin not working", "asus laptop", "sign-in issue", "ngc folder"]
description: "Windows 11 PIN sign-in broken on your ASUS laptop? Rebuild the NGC credential store, reset the TPM, and get one-tap sign-in working again."
thumbnail: "/images/thumbs/how-to-fix-pin-not-working-on-windows-11-on-asus-laptop.webp"
faqs:
  - q: "Why did my PIN stop working after a Windows update?"
    a: "Updates migrate the credential system, and the migration sometimes corrupts the NGC folder where your PIN is stored. Windows then rejects the correct PIN because it cannot decrypt and verify it. This is the single most common cause, and clearing the NGC folder plus re-creating the PIN fixes it."
  - q: "Do I need internet to reset my PIN?"
    a: "For the 'I forgot my PIN' flow with a Microsoft account, yes — Windows must verify your identity online. For the manual NGC-folder method with a local account or cached credentials, no internet is needed. If you are offline with a Microsoft account, connect to Wi-Fi from the login screen first."
  - q: "My fingerprint also stopped working. Is it the same problem?"
    a: "Very likely yes. PIN, fingerprint, and face sign-in all live in the same NGC credential store and depend on the same TPM. When the store corrupts, every Windows Hello method breaks together while the password keeps working. Fixing the NGC folder usually restores all of them at once."
  - q: "Will clearing the TPM lock me out of BitLocker?"
    a: "It can trigger a BitLocker recovery prompt on next boot, which is why you should save your 48-digit BitLocker recovery key from your Microsoft account before clearing the TPM. With the key in hand, you just type it once and everything proceeds normally."
---
Same story as every other brand, with an ASUS twist: your PIN was fine yesterday, and today Windows 11 insists it is wrong — or the PIN option has vanished entirely. On ASUS laptops this crops up most often after Windows feature updates and ASUS firmware updates, both of which touch the TPM and credential system the PIN depends on.

Your PIN is not the problem. The encrypted vault that stores it is. Let's rebuild it.

## Why this happens

- **Corrupted NGC folder:** The credential store at `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC` gets damaged during updates — the number one cause.
- **TPM desynchronization:** ASUS firmware updates can reset or alter TPM state, invalidating the sealed PIN credentials.
- **Broken Windows Hello components:** Feature updates occasionally leave the biometric and PIN stack in a half-migrated state.
- **ASUS fingerprint driver conflicts:** Outdated ASUS biometric drivers can block the entire Hello stack, including PIN setup.
- **Enhanced sign-in security (VBS) blocking setup:** On some ASUS models the virtualization-based sign-in protection conflicts with PIN enrollment.
- **Corrupted user profile:** Damage to profile-level credential files breaks Hello sign-in for one account while others work fine.
- **Work or school account policies:** MDM policies can disable or restrict PIN sign-in without any visible explanation.

## How to fix it

Work through these in order, starting at Fix 1. Sign in with your password (via **Sign-in options** on the login screen) to perform these steps.

### Fix 1: Delete the NGC folder contents and set up a fresh PIN

The core fix — clears the corrupted credential store.

1. Sign in with your password. Open **Terminal (Admin)** (**Win + X > Terminal (Admin)**).
2. Take ownership of the NGC folder:
   `takeown /f C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /r /d y`
   `icacls C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /grant administrators:F /t`
3. Open File Explorer, navigate to that NGC path, and delete everything inside it.
4. Go to **Settings > Accounts > Sign-in options > PIN (Windows Hello)** and click **Set up** (or **Change**).
5. Authenticate with your password, create the new PIN, then sign out and test it at the login screen.

If biometrics broke along with the PIN, our [Windows Hello troubleshooting guide](/articles/how-to-fix-windows-hello-not-working-in-windows-11-24h2/) covers the fingerprint and face-recognition side.

### Fix 2: Use "I forgot my PIN" on the login screen

The official reset path when you cannot access the system yet.

1. On the login screen, select the PIN sign-in option and click **I forgot my PIN**.
2. Verify your identity — Microsoft account password, authenticator approval, or emailed code.
3. Set the new PIN and sign in. This rebuilds the credential store automatically.

### Fix 3: Clear the TPM

When the TPM's sealed data no longer matches what Windows expects, a clear forces a clean re-provisioning.

1. Save your BitLocker recovery key first (check your Microsoft account devices page online).
2. Press **Win + R**, type `tpm.msc`, press Enter.
3. In the right-hand Actions pane, click **Clear TPM** and confirm the restart.
4. After reboot, Windows re-provisions the TPM. Go to **Settings > Accounts > Sign-in options** and create your PIN again.
5. If BitLocker asks for the recovery key at boot, enter the 48-digit key once — normal boot resumes afterward.

### Fix 4: Update ASUS biometric and chipset drivers

Stale ASUS drivers are a brand-specific trigger for Hello failures.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Under **Biometric devices**, right-click your fingerprint sensor and choose **Update driver > Search automatically for drivers**.
3. Do the same under **System devices** for TPM and chipset entries.
4. Then visit ASUS's official support downloads for your exact model and install the latest ATK package, chipset, and fingerprint drivers — ASUS's own packages are newer than what Windows Update provides.
5. Restart and set up the PIN again.

### Fix 5: Check the Windows Biometric Service

If the supporting service is disabled, Hello enrollment silently fails.

1. Press **Win + R**, type `services.msc`, press Enter.
2. Find **Windows Biometric Service** — double-click it.
3. Set **Startup type** to **Automatic**, click **Start** if it is not running, then **OK**.
4. Also verify **Credential Manager** is running.
5. Restart and retry PIN setup.

For general sign-in and account recovery techniques, the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows) documents the official flows.

### Fix 6: Disable conflicting fast startup and credential software

Fast Startup's saved session state can preserve the broken credential state across reboots.

1. Press **Win + R**, type `powercfg.cpl`, press Enter → **Choose what the power buttons do** → **Change settings that are currently unavailable** → uncheck **Turn on fast startup** → **Save changes**.
2. Check **Settings > Apps > Installed apps** for third-party credential managers or old ASUS security utilities that hook into sign-in, and uninstall or update them.
3. Restart fully (not a fast-startup hybrid boot) and set up the PIN.

### Fix 7: Test with a new local account

Determines whether the damage is profile-specific.

1. Go to **Settings > Accounts > Other users > Add account**.
2. Choose **I don't have this person's sign-in information**, then **Add a user without a Microsoft account**, and create it.
3. Sign into the new account and set up a PIN. If it works there, your original profile's credential storage is damaged — migrate your files to the new profile.
4. If PIN fails on the new account too, the problem is system-wide: consider the in-place Windows repair described in our [PIN troubleshooting overview](/articles/how-do-i-fix-pin-not-working-on-windows-11/).

## Closing

On ASUS laptops, PIN failures are a credential-store problem far more often than a real security problem — the NGC folder corrupts, the TPM desynchronizes after a firmware update, or a stale biometric driver jams the Hello stack. Clear the store, re-provision the TPM, and bring the ASUS drivers current, and one-tap sign-in comes back. And keep your Microsoft account password memorized: it is the master key that unlocks every one of these recovery paths.
