---
title: "PIN Not Working on Windows 11? Fix It on Your Dell Laptop"
slug: how-to-fix-pin-not-working-on-windows-11-on-dell-laptop
date: 2026-09-25
categories: ["windows-errors"]
tags: ["windows hello pin", "pin not working", "dell laptop", "sign-in error", "tpm"]
description: "Locked out of PIN sign-in on your Dell laptop? Fix the 0x80090016 error and corrupted credentials with these step-by-step Windows 11 repairs."
thumbnail: "/images/thumbs/how-to-fix-pin-not-working-on-windows-11-on-dell-laptop.webp"
faqs:
  - q: "What is error 0x80090016 when setting up a PIN?"
    a: "Error 0x80090016 means Windows cannot create or verify the PIN because the TPM-backed credential store is corrupted or the TPM is in a bad state. The standard fix is deleting the NGC folder contents and re-creating the PIN; if that fails, clearing the TPM resolves the underlying trust issue."
  - q: "Does Dell Data Protection affect Windows Hello PIN?"
    a: "It can. Dell's encryption and security tools (Dell Data Protection, Dell Encryption) interact with the TPM, and after major updates they occasionally leave the TPM in a state where Hello PIN enrollment fails. Updating those tools — or temporarily pausing their TPM interaction — often unblocks PIN setup."
  - q: "Can I still sign in if my PIN is broken?"
    a: "Yes. Click Sign-in options on the login screen and choose the password icon to sign in with your Microsoft account or local account password. Your password always works independently of the PIN. From there you can perform every fix in this guide."
  - q: "Should I disable the PIN and just use a password?"
    a: "You could, but the PIN is actually more secure on your own device — it is bound to the TPM and never leaves the laptop, unlike a password that can be phished. Fixing the PIN is worth the ten minutes; falling back to password-only is less convenient and less secure against remote attacks."
---
Dell laptops — Latitudes, XPS, Inspirons — run into the broken-PIN problem for the usual Windows reasons plus one Dell-specific wrinkle: Dell's security and encryption tools share the TPM with Windows Hello, and after updates the two can step on each other. The symptom is the same everywhere, though: correct PIN rejected, error 0x80090016, or no PIN option at all.

Sign in with your password to get started (click **Sign-in options** on the login screen), then work through the fixes.

## Why this happens

- **Corrupted NGC credential folder:** The encrypted PIN store gets damaged during Windows updates — the most common cause on any brand.
- **TPM state conflicts with Dell security software:** Dell Data Protection/Encryption tools and Windows Hello both use the TPM; updates can leave them disagreeing.
- **Dell firmware updates resetting TPM:** BIOS updates on Dell machines sometimes clear or alter TPM provisioning, invalidating sealed PIN credentials.
- **Broken Hello system components:** Feature updates can leave the PIN/biometric stack half-migrated.
- **Outdated TPM or biometric drivers:** Stale drivers from Dell's image break Hello enrollment after Windows moves forward.
- **Enhanced sign-in security (VBS) conflicts:** Virtualization-based protection can block PIN setup on configurations that do not fully support it.
- **Corrupted user profile credentials:** Profile-level damage breaks Hello for one user while others sign in fine.

## How to fix it

Work through these in order, starting at Fix 1.

### Fix 1: Clear the NGC folder and recreate the PIN

The highest-success-rate fix for every PIN failure mode.

1. Sign in with your password. Open **Terminal (Admin)** (**Win + X > Terminal (Admin)**).
2. Take ownership of the credential folder:
   `takeown /f C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /r /d y`
   `icacls C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /grant administrators:F /t`
3. In File Explorer, open `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC` and delete all contents inside.
4. Go to **Settings > Accounts > Sign-in options > PIN (Windows Hello)** → **Set up**, authenticate with your password, and create a new PIN.
5. Sign out and verify the PIN works at the login screen.

Dell's own driver and firmware updates live on the [Dell support site](https://www.dell.com/support) — grab the latest TPM and chipset drivers for your Service Tag after the PIN works again.

### Fix 2: Reset via "I forgot my PIN"

The built-in recovery flow that rebuilds credentials through Microsoft's verification.

1. On the login screen, pick the PIN option and click **I forgot my PIN**.
2. Verify with your Microsoft account password or the code sent to your email/phone.
3. Create the new PIN. Windows rebuilds the NGC store in the process.

### Fix 3: Clear and re-provision the TPM

For cases where the TPM itself is the disagreement point — especially after Dell BIOS updates.

1. Back up your BitLocker recovery key from your Microsoft account (Settings > your account online, or printed copy).
2. Press **Win + R**, type `tpm.msc`, press Enter → in the Actions pane click **Clear TPM** → restart.
3. Windows re-provisions the TPM on boot. If BitLocker prompts for the recovery key, enter it once.
4. Set up the PIN again under **Settings > Accounts > Sign-in options**.

If Hello biometrics are also down, see our [Windows Hello fix guide](/articles/how-to-fix-windows-hello-not-working-in-windows-11-24h2/) for the fingerprint/face side of the same system.

### Fix 4: Update Dell TPM, chipset, and biometric drivers

Dell-specific driver staleness is a real trigger — use Dell's own packages.

1. Open **Dell Command Update** or **Dell SupportAssist** and install all recommended updates, especially TPM firmware, chipset, and biometric drivers.
2. In **Device Manager** (**Win + X > Device Manager**), verify **Security devices** (TPM 2.0) and **Biometric devices** show no warning icons.
3. If a device shows an error, right-click → **Uninstall device** (check remove driver), restart, and let Windows reinstall it fresh.
4. Retry PIN setup.

### Fix 5: Check Dell security software interference

Dell Data Protection or Dell Encryption fighting Hello over the TPM.

1. Open **Settings > Apps > Installed apps** and look for Dell Data Protection, Dell Encryption, or similar.
2. Check for updates to those tools first — vendors patch TPM conflicts regularly.
3. If fully updated and the PIN still fails, temporarily disable the tool's pre-boot/TPM features (consult Dell's documentation for your product), set up the PIN, then re-enable.
4. On corporate machines, your IT department manages these tools — ask them before changing anything.

### Fix 6: Toggle Memory integrity and enhanced sign-in security

VBS features can block Hello enrollment after updates change the security baseline.

1. Open **Windows Security > Device security > Core isolation details**.
2. Note the current state of **Memory integrity** and enhanced sign-in security, then try toggling them off, restarting, and setting up the PIN.
3. If the PIN enrolls successfully, you may turn them back on — the toggle often clears the stale state causing the conflict.
4. For error-code-specific guidance during this process, our [PIN troubleshooting overview](/articles/how-do-i-fix-pin-not-working-on-windows-11/) covers the common codes.

### Fix 7: Create a new user profile

Isolates profile-level credential corruption.

1. **Settings > Accounts > Other users > Add account** → create a local account without a Microsoft account.
2. Sign in as the new user and set up a PIN. Success here means your original profile is damaged — migrate files from `C:\Users\<old>` and adopt the new profile.
3. Failure on the new account too means system-wide damage — run an in-place Windows repair from the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), keeping files and apps.

## Closing

Dell adds its own flavor to PIN problems through TPM-sharing security tools and firmware updates, but the fix hierarchy is the same: clear the NGC store, re-provision the TPM, and bring Dell's drivers current. The ten minutes this takes beats typing a full password at every login for the next year — and on a TPM-backed device, the PIN remains the sign-in method I'd recommend keeping.
