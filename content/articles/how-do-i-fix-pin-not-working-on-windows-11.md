---
title: "How Do I Fix PIN Not Working on Windows 11? (Sign-In Options Greyed Out)"
slug: how-do-i-fix-pin-not-working-on-windows-11
date: 2026-09-03
categories: ["windows-errors"]
tags: ["windows hello pin", "sign-in", "login problem", "windows 11"]
description: "Windows 11 PIN not working or the PIN option is missing? Fix corrupted NGC folders, TPM issues, and account glitches with this guide."
thumbnail: "/images/thumbs/how-do-i-fix-pin-not-working-on-windows-11.webp"
faqs:
  - q: "Why does Windows 11 say my PIN is unavailable?"
    a: "The usual message is 'Something happened and your PIN isn't available.' It means the encrypted PIN data stored in the NGC folder is corrupted, the TPM (the chip that protects the PIN) has an issue, or a recent update broke the Windows Hello components. Deleting the NGC folder contents and re-adding the PIN fixes it in most cases."
  - q: "Will deleting the NGC folder lock me out of my laptop?"
    a: "No, as long as you can sign in with your password first. The NGC folder only stores Windows Hello data (PIN, fingerprint, face). Deleting its contents just removes those sign-in methods — you then re-add your PIN from Settings. Make sure you know your Microsoft account or local account password before you start."
  - q: "Why is the PIN setup option greyed out in Settings?"
    a: "This happens when the 'For improved security, only allow Windows Hello sign-in' toggle is in a bad state, when TPM is disabled in the BIOS, or when group policy blocks Hello. Toggling that setting off and on, or enabling TPM in the BIOS, usually restores the option."
  - q: "Can I still sign in if my PIN stops working?"
    a: "Yes — click 'Sign-in options' on the login screen and choose the password (key) icon to sign in with your account password instead. Your files and everything else are unaffected. Fix the PIN at your convenience afterward using the steps below."
---
Few things are more annoying than a PIN that worked yesterday and refuses today — especially when the error message is the unhelpful "Something happened and your PIN isn't available." The good news: your PIN data is just a protected file on your disk, and when it corrupts, you can delete it and make a fresh one in about five minutes. You're never locked out as long as you know your password.

This guide covers every layer of the problem: the corrupted PIN store, TPM hiccups, account issues, and the greyed-out setup option.

## Why this happens

- **Corrupted NGC folder.** The PIN lives encrypted in `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc`. If those files corrupt, the PIN stops working.
- **TPM issues.** The Trusted Platform Module chip seals the PIN data; a TPM error or cleared TPM breaks the seal.
- **Windows update damage.** Feature updates sometimes break the Windows Hello stack or leave it half-configured.
- **Account sync problems.** For Microsoft accounts, a password change or sync glitch can invalidate the local PIN binding.
- **TPM disabled in BIOS.** Without TPM active, Windows Hello PIN setup can grey out entirely.
- **Third-party security software.** Some security suites interfere with the credential providers that handle PIN sign-in.

## How to fix it

Work through these in order.

### Fix 1: Sign in with your password, then remove and re-add the PIN

Start with the simplest path — sometimes the PIN just needs to be recreated.

1. On the login screen, click **Sign-in options** and select the password (key) icon, then sign in with your account password.
2. Go to **Settings > Accounts > Sign-in options > PIN (Windows Hello)**.
3. Click **Remove**, confirm, then click **Set up** or **Add** and create a new PIN.
4. Sign out and test the new PIN. If setup fails or the option is greyed out, continue to Fix 2.

### Fix 2: Delete the NGC folder contents

This is the definitive fix for "your PIN isn't available" — it wipes the corrupted PIN store.

1. Sign in with your password as in Fix 1.
2. Open **File Explorer**, go to **View**, and enable **Hidden items**.
3. Navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc`.
4. You may need to take ownership: right-click the **Ngc** folder, choose **Properties > Security > Advanced > Change** owner to your account, and grant yourself full control.
5. Delete everything inside the Ngc folder (not the folder itself).
6. Go to **Settings > Accounts > Sign-in options > PIN (Windows Hello)** and set up a fresh PIN.

### Fix 3: Toggle the Windows Hello sign-in setting

A stuck security toggle can grey out PIN setup.

1. Go to **Settings > Accounts > Sign-in options**.
2. Find **"For improved security, only allow Windows Hello sign-in for Microsoft accounts on this device"** and turn it **Off**.
3. Restart the laptop.
4. Return to the same setting, turn it back **On**, restart again, and try PIN setup. This toggle reset clears the corrupted Hello state for many users.

### Fix 4: Clear the TPM

If the TPM's stored keys are in a bad state, clearing it lets Windows re-provision cleanly.

1. Press **Win + R**, type `tpm.msc`, and press Enter.
2. In the Actions pane, click **Clear TPM** and restart when prompted.
3. During reboot you may need to press a key to confirm clearing the TPM — do so.
4. After Windows loads, go to **Settings > Accounts > Sign-in options** and set up your PIN again. Note: clearing TPM also removes other TPM-stored keys (like BitLocker protectors tied to TPM), so have your BitLocker recovery key handy if you use it.

### Fix 5: Enable TPM in the BIOS

If TPM is off, Hello features can't work at all.

1. Restart and enter the BIOS (**F2**, **Del**, or **Esc** depending on your laptop).
2. Find the security section and look for **TPM**, **PTT** (Intel), or **fTPM** (AMD) — enable it.
3. Also ensure **Secure Boot** is enabled, which Hello expects.
4. Save, exit, boot into Windows, and try PIN setup again.

### Fix 6: Fix Microsoft account sync issues

For Microsoft accounts, a sync glitch can break the PIN binding.

1. Go to **Settings > Accounts > Your info** and verify you're signed in properly — sign out and back in if anything looks off.
2. If you recently changed your Microsoft account password online, sign in on the laptop with the new password first, then re-add the PIN.
3. As an alternative, switch to a local account temporarily (**Settings > Accounts > Your info > Sign in with a local account instead**), set up the PIN, and switch back.
4. Verify your account at [Microsoft's support site](https://support.microsoft.com/en-us/windows) guidance if sign-in itself is failing.

### Fix 7: Repair system files and check for bad updates

If Hello components are damaged, repair the OS layer.

1. In **Terminal (Admin)**, run `sfc /scannow` then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Check **Settings > Windows Update > Update history** — if the PIN broke right after an update, uninstall it via **Uninstall updates**.
3. Restart and attempt PIN setup once more.
4. If it still fails across all fixes, your Windows Hello stack may need a repair install — the [troubleshooting companion guide](/articles/troubleshoot-pin-not-working-on-windows-11/) covers the deeper registry and policy angles.

## Closing

PIN problems look scary on the login screen but they're a data-corruption issue, not a security crisis — your password always remains as a fallback, and the NGC folder delete fixes the classic error nearly every time.

The one habit worth building: after any major Windows update, test your PIN before you need it in a hurry — discovering it's broken when you're rushing out the door is the worst possible timing. Keep your Microsoft account password (and BitLocker recovery key, if you use encryption) written down somewhere safe, because every Hello fix eventually asks for one of them. On Dell laptops specifically, the [Dell PIN fix guide](/articles/how-to-fix-pin-not-working-on-windows-11-on-dell-laptop/) covers model-specific TPM quirks. And if you manage a family laptop, make sure each person knows the password fallback; a broken PIN shouldn't mean a locked-out household.
