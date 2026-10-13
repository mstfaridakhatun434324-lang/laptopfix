---
title: "How to Fix PIN Sign-In Not Working on Windows 11"
slug: how-to-fix-pin-not-working-on-windows-11-reddit
date: 2026-09-11
categories: ["windows-errors"]
tags: ["pin sign-in", "windows hello", "login problems", "windows 11"]
description: "Fix Windows 11 PIN sign-in when it stops working — clear the NGC folder, re-register your PIN, and repair the sign-in options in 7 steps."
thumbnail: "/images/thumbs/how-to-fix-pin-not-working-on-windows-11-reddit.webp"
faqs:
  - q: "Why does Windows 11 say my PIN is unavailable?"
    a: "The PIN credential store — a protected folder called NGC — is corrupted, usually after a Windows update, a TPM hiccup, or a failed feature update. Deleting the NGC folder contents and setting up the PIN again fixes it in nearly every case."
  - q: "I forgot my PIN and the reset option does nothing. What now?"
    a: "Sign in with your Microsoft account password instead (click Sign-in options on the login screen). Once you are in, remove the PIN under Settings > Accounts > Sign-in options and add a fresh one. If the password sign-in is also broken, use another admin account or the recovery environment."
  - q: "Does deleting the NGC folder delete anything important?"
    a: "No. It only removes stored PIN and Windows Hello credentials, which you re-create in two minutes. Your files, Microsoft account, and password sign-in are completely unaffected."
  - q: "Can a Windows update break PIN sign-in?"
    a: "Yes — it is one of the most common triggers. Updates sometimes invalidate the TPM-backed credential container. The NGC reset below was practically designed for exactly this scenario."
---

You type your PIN, Windows 11 shakes its head with **"Something happened and your PIN isn't available"** — or the PIN option has vanished from the sign-in screen entirely. This is one of the most reported Windows 11 annoyances on forums, and it almost always traces back to a corrupted PIN credential store rather than anything you did wrong.

The fix is quick: clear the corrupted credential folder, re-register your PIN, and you are back to one-tap sign-in. This guide covers the standard case and the trickier variants (forgotten PIN, missing PIN option, post-update breakage). If your whole sign-in flow is broken rather than just the PIN, our guide to [factory resetting without a password](/articles/how-to-factory-reset-windows-11-laptop-without-password/) is the escalation path.

## Why this happens

- **Corrupted NGC folder.** Your PIN lives in `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc`. If those files get damaged — common after updates — Windows cannot validate the PIN.
- **TPM state changed.** The PIN is sealed to the TPM chip. A BIOS update, TPM clear, or firmware change invalidates the stored credential.
- **Failed or partial Windows update.** Updates that touch the credential stack can leave the PIN registration in a half-migrated state.
- **Domain or policy changes.** On work laptops, a Group Policy or Intune change can disable PIN sign-in remotely, making the option disappear.
- **Corrupted user profile.** Rare, but a damaged profile breaks the link between your account and its Hello credentials.
- **"I forgot my PIN" loop.** The reset link on the login screen sometimes fails silently when the NGC store is corrupted, leaving you stuck.

## How to fix it

Work through these in order — Fix 2 resolves the vast majority of cases.

### Fix 1: Sign in with your password first

You need to get into Windows before you can repair the PIN.

1. On the sign-in screen, click **Sign-in options** and choose the **password** (key) icon.
2. Enter your Microsoft account or local account password.
3. If you do not remember the password either, use the **I forgot my password** link or sign in with another administrator account on the machine.
4. Once you are on the desktop, continue to Fix 2.

### Fix 2: Delete the NGC folder and re-create the PIN

This is the canonical fix. It works because it forces Windows to build a fresh credential store.

1. Open **File Explorer** and navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc`. (You may need to click through "you don't have permission" prompts — click **Continue**.)
2. Delete **everything inside** the Ngc folder. If Windows refuses, take ownership: right-click the folder, choose **Properties > Security > Advanced > Change** owner to your account, grant yourself **Full control**, then delete.
3. Go to **Settings > Accounts > Sign-in options**.
4. Under **PIN (Windows Hello)**, click **Set up** (or **Remove** first, then **Add**) and create your new PIN.
5. Lock the screen (**Win + L**) and test the new PIN immediately.

### Fix 3: Use the "I forgot my PIN" reset properly

If the NGC delete felt too manual, the built-in reset does the same thing through the UI.

1. Go to **Settings > Accounts > Sign-in options > PIN (Windows Hello)**.
2. Click **I forgot my PIN** and follow the Microsoft account verification.
3. Set a new PIN when prompted.
4. If the reset errors out, fall back to Fix 2's manual NGC deletion — it bypasses whatever the UI is choking on.

### Fix 4: Check that TPM is healthy

Since the PIN is TPM-backed, a TPM problem breaks PIN sign-in at the root.

1. Press **Win + R**, type `tpm.msc`, and press Enter.
2. Confirm it says **"The TPM is ready for use."** If not, restart and check the TPM setting in your BIOS (usually under **Security**).
3. If the TPM shows errors, choose **Clear TPM** in the console (this removes all TPM-stored keys — you will need to re-set up the PIN and BitLocker afterward).
4. Re-create the PIN after the TPM is healthy.

### Fix 5: Toggle the PIN requirement and convenience PIN sign-in

A policy or registry quirk can hide or break the PIN option.

1. Press **Win + R**, type `gpedit.msc` (Windows 11 Pro) and go to **Computer Configuration > Administrative Templates > System > Logon**. Set **Turn on convenience PIN sign-in** to **Enabled**.
2. On Home edition (no gpedit), press **Win + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System`. Create a DWORD (32-bit) value named `AllowDomainPINLogon` set to **1**.
3. Also check **Settings > Accounts > Sign-in options** and make sure **"For improved security, only allow Windows Hello sign-in for Microsoft accounts"** is toggled in a way that still permits your PIN.
4. Restart and test.

### Fix 6: Run SFC and DISM to repair the credential stack

1. Open **Terminal (Admin)** with **Win + X**.
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` once more.
3. Restart, then re-create the PIN via **Settings > Accounts > Sign-in options**.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents additional sign-in repair steps if system file damage is extensive.

### Fix 7: Create a new user profile (last resort)

If the PIN works for other accounts but not yours, the profile itself is damaged.

1. Create a new local administrator account: **Settings > Accounts > Other users > Add account**, then change it to **Administrator**.
2. Sign in as the new account and set up a PIN there to confirm the system is fine. (If the new account has its own shell quirks, our [Start menu fix guide](/articles/how-to-fix-start-menu-not-working-on-windows-11/) covers those — but the PIN itself should work.)
3. Move your files from `C:\Users\<oldname>` to the new profile, reinstall your apps, and retire the old profile.

## Closing

A dead PIN on Windows 11 is annoying but almost never serious — the NGC folder reset in Fix 2 clears it up for the overwhelming majority of people, usually in under ten minutes. The PIN is a convenience layer on top of your real account credential, so nothing is ever truly lost when it breaks. Re-create it, test it with **Win + L**, and get back to the one-second sign-in you are used to.
