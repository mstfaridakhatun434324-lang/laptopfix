---
title: "How to Fix Your PIN Not Working on Windows 11"
slug: how-to-fix-pin-not-working-on-windows-11
date: 2026-09-11
categories: ["windows-errors"]
tags: ["pin not working", "windows hello", "sign-in", "windows 11"]
description: "Windows 11 says your PIN is unavailable or incorrect? Here are the fixes — from resetting the PIN to repairing the NGC folder — that restore sign-in."
thumbnail: "/images/thumbs/how-to-fix-pin-not-working-on-windows-11.webp"
faqs:
  - q: "Why does Windows 11 say my PIN is unavailable?"
    a: "The PIN credentials are stored in a protected system folder called NGC. If that folder's contents get corrupted — by a failed update, disk error, or permission change — Windows can't read your PIN and reports it as unavailable. The fix is to take ownership of the folder, clear it, and set a fresh PIN, which rebuilds clean credentials."
  - q: "I know my PIN is correct, but Windows rejects it. Why?"
    a: "This usually happens after a motherboard or TPM change, a major Windows update, or when the cached credential no longer matches the TPM-stored key. Signing in with your Microsoft account password instead, then removing and re-adding the PIN, resynchronizes everything and almost always resolves it."
  - q: "Can I sign in if my PIN stops working?"
    a: "Yes — click Sign-in options on the login screen and choose the password (key) icon to sign in with your Microsoft account password instead. Local accounts can use their account password the same way. This bypass never deletes anything; it just gets you into Windows so you can repair the PIN."
  - q: "Will resetting my PIN delete my files?"
    a: "No. Removing and re-adding a PIN only affects sign-in credentials — your files, apps, and settings are untouched. The NGC folder cleanup in Fix 4 also only removes sign-in data. Think of it like changing a door lock: the house and everything in it stays exactly as it was."
---

Few things are more annoying than typing the PIN you've used a thousand times and having Windows 11 refuse it — or worse, telling you "Your PIN is no longer available." The good news: this is a credentials problem, not an account problem. Your Microsoft account is fine, your files are fine, and you can still sign in with your password while you fix it. The PIN itself lives in a protected system folder, and when that folder's data gets corrupted, Windows loses the ability to verify your PIN.

The most common triggers are Windows updates (especially feature updates), TPM or motherboard changes, disk errors, and occasionally antivirus software locking the credential store. The fixes below go from the quickest (just reset the PIN from Settings) to the definitive (clearing the NGC credential folder and rebuilding it). If you're locked out entirely, start with Fix 1 — it gets you signed in with your password so you can do the rest. For related sign-in trouble, see our [Windows Hello repair guide](/articles/how-to-fix-windows-hello-not-working-on-windows-11/) and our [login screen loop fix](/articles/how-to-fix-windows-11-login-screen-loop-on-dell-laptop/).

## Why this happens

- **Corrupt NGC folder**: The `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC` folder holds PIN credentials; corruption here makes the PIN "unavailable."
- **TPM changes**: PINs are bound to the Trusted Platform Module — a TPM reset, firmware update, or motherboard swap invalidates stored PINs.
- **Windows update damage**: Feature updates sometimes break the credential provider chain that handles PIN sign-in.
- **Permission drift**: System permission changes on the NGC folder can lock Windows itself out of reading your PIN.
- **Corrupt user profile**: A damaged profile can break the link between your account and its PIN credential.
- **Antivirus interference**: Some security products aggressively guard credential folders and block legitimate access after their own updates.
- **Microsoft account sync issues**: For Microsoft accounts, a sync hiccup can desynchronize the local PIN from the account credential.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Sign in with your password instead

Get into Windows first; fix the PIN second.

1. On the login screen, click **Sign-in options** below the PIN field.
2. Click the **key icon** (password) and enter your Microsoft account password — or your local account password if you use a local account.
3. Once signed in, don't skip the remaining fixes: password sign-in works, but you want your PIN back, and the underlying corruption won't heal itself.
4. If you've forgotten the password too, use another device to reset it at Microsoft's account recovery page, then return here.

### Fix 2: Remove and re-add the PIN from Settings

The standard reset resolves most cases.

1. Go to **Settings** > **Accounts** > **Sign-in options**.
2. Under **PIN (Windows Hello)**, click **Remove**. Confirm with your password when prompted.
3. Restart the laptop — this clears any cached credential state.
4. Return to **Settings** > **Accounts** > **Sign-in options** > **PIN (Windows Hello)** and click **Set up** (or **Add**).
5. Enter your password to verify, then choose a new PIN. Test it by locking the PC (**Windows + L**) and signing back in.

### Fix 3: Use the "I forgot my PIN" link

When Settings won't cooperate, the recovery link does the same job from the login screen.

1. On the login screen, enter any PIN (or leave it blank) and click **OK** — when it fails, look for **I forgot my PIN** below the field.
2. Click it and verify your identity with your Microsoft account password.
3. Follow the prompts to set a new PIN. This path rebuilds the credential even when the Settings route is blocked.
4. If the link doesn't appear, you're likely on a local account — sign in with the account password (Fix 1) and use Fix 2 instead.

### Fix 4: Clear the NGC folder and rebuild

The definitive fix for "PIN is unavailable" errors.

1. Sign in with your password (Fix 1). Open **File Explorer**, click **View** > **Show** > **Hidden items**.
2. Navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC`.
3. If access is denied: right-click the **NGC** folder > **Properties** > **Security** > **Advanced** > **Change** (owner) > enter your username > tick **Replace owner on subcontainers and objects** > **OK**, then grant yourself **Full control**.
4. Delete everything inside the NGC folder (not the folder itself).
5. Restart, then go to **Settings** > **Accounts** > **Sign-in options** > **PIN (Windows Hello)** > **Set up** and create a fresh PIN.
6. This forces Windows to generate clean credentials from scratch — the corruption is gone because the corrupted files are gone.

### Fix 5: Check the TPM and credential services

A PIN depends on the TPM and two background services.

1. Press **Windows + R**, type `tpm.msc`, and confirm the TPM reports "The TPM is ready for use." If not, clear it via the BIOS/UEFI (this resets TPM keys — you'll re-add the PIN after).
2. Press **Windows + R**, type `services.msc`, and verify **Credential Manager** and **CNG Key Isolation** are **Running** with **Automatic** (or **Manual (Trigger Start)**) startup.
3. If either service is stopped, right-click > **Start**, then set the startup type correctly.
4. Restart and try the PIN again. Check your laptop vendor's guidance too — Dell, HP, and Lenovo all publish TPM firmware updates that fix PIN-related bugs; [Microsoft's support site](https://support.microsoft.com/en-us/windows) documents the services involved.

### Fix 6: Run system file repair and update Windows

Catch-all for update damage and corrupted components.

1. Open **Terminal (Admin)** or **Command Prompt (Admin)** and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Go to **Settings** > **Windows Update** and install everything pending — Microsoft regularly ships fixes for PIN and Hello sign-in bugs. Grab the latest build with [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) if Windows Update itself is stuck.
3. After updating, remove and re-add the PIN one final time (Fix 2) so the credential is generated under the fixed components.
4. If the PIN breaks again immediately after the next update, pause updates temporarily and report the pattern — recurring update breakage is a known-issue candidate.

## Closing

PIN problems feel personal — it's your code, and the machine is rejecting it — but they're mechanical: corrupted credential files, a desynced TPM, or a damaged sign-in component. The NGC folder rebuild in Fix 4 resolves the stubborn cases that simple PIN resets can't touch, and it's safe to do because it only affects sign-in data. Once your PIN works again, write it down somewhere secure (a password manager, not a sticky note) so a future glitch never turns into a lockout. And if the PIN field itself never appears — just a spinning login screen — that's a different fault covered in our [login loop guide](/articles/how-to-fix-windows-11-login-screen-loop-on-dell-laptop/).
