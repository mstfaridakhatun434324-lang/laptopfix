---
title: "Windows 11 PIN Not Working? Here's What to Do"
slug: what-to-do-if-pin-not-working-on-windows-11
date: 2026-09-26
categories: ["windows-errors"]
tags: ["windows hello", "pin not working", "sign-in", "ngc folder", "windows 11"]
description: "Your Windows 11 PIN stopped working or won't set up? Fix PIN sign-in failures in 7 steps — from quick resets to the Ngc folder fix."
thumbnail: "/images/thumbs/what-to-do-if-pin-not-working-on-windows-11.webp"
faqs:
  - q: "Why does Windows say my PIN is incorrect when it isn't?"
    a: "The PIN credential store (the Ngc folder) is usually corrupted — Windows can't read the stored PIN, so everything you type fails. Deleting the Ngc folder contents and setting up the PIN fresh resolves this in most cases."
  - q: "Can I sign in without my PIN?"
    a: "Yes — use your Microsoft account password instead. On the sign-in screen, click Sign-in options and choose the password icon. Once you're in, you can fix or reset the PIN from Settings."
  - q: "Why is the 'Add PIN' button greyed out?"
    a: "Usually a policy or TPM issue. On work/school devices, administrators can disable PIN via policy. On personal devices, check that the TPM is enabled in BIOS (tpm.msc should say 'ready for use') and that you're signed in with an account that allows Hello."
  - q: "Will resetting my PIN delete anything?"
    a: "No — resetting the PIN only affects the sign-in credential. Your files, apps, and settings are untouched. You'll need your Microsoft account password (or another sign-in method) to authorize the reset."
---

The Windows Hello PIN is the backbone of Windows sign-in — fast, local, and required before face or fingerprint even work. When it breaks ("your PIN is no longer available," endless incorrect-PIN errors, or setup that won't complete), everything built on top of it breaks too.

The fixes go from the simple password fallback to the famous Ngc folder reset that resolves the stubborn cases.

## Why this happens

- **Corrupted Ngc credential folder.** The encrypted store holding your PIN gets damaged — the top cause.
- **TPM problems.** The PIN is sealed to the TPM; TPM errors or clearing break the PIN.
- **Windows update damaged Hello components.** Updates occasionally corrupt the credential stack.
- **Microsoft account sync issues.** Password changes or account problems invalidate the cached credential.
- **Policy restrictions.** Work/school policies or registry settings disabling PIN.
- **Corrupted user profile.** Profile damage takes the PIN store with it.

## How to fix it

Work through these in order — start with Fix 1 and stop when the PIN works.

### Fix 1: Sign in with your password instead

Get into Windows first; fix the PIN from inside.

1. On the sign-in screen, click **Sign-in options** below the PIN field.
2. Select the password (key) icon and enter your Microsoft account password.
3. If you've forgotten that too, use another device to reset it at Microsoft's account recovery page.
4. Once signed in, don't set up the PIN yet — work the fixes below first so the new PIN lands on a healthy foundation.
5. If no sign-in method works, use the recovery environment's password reset options.

### Fix 2: Remove and re-add the PIN

The straightforward reset.

1. Go to **Settings > Accounts > Sign-in options**.
2. Under **PIN (Windows Hello)**, click **Remove** — confirm with your password.
3. Restart the laptop.
4. Return to **Sign-in options** and click **Set up** under PIN.
5. Create the new PIN and test sign-out/sign-in. If setup fails or the PIN breaks again quickly, the Ngc store needs the deeper fix next.

### Fix 3: Delete the Ngc folder contents

The definitive fix for "PIN is no longer available."

1. Open **File Explorer**, go to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc`.
2. You'll likely get a permission prompt — click **Continue** to gain access (or take ownership via the Security tab if denied).
3. Delete everything inside the Ngc folder (not the folder itself).
4. Restart the laptop.
5. Go to **Settings > Accounts > Sign-in options** and set up a fresh PIN — it now builds on a clean store. This resolves the majority of stubborn PIN failures.

### Fix 4: Check TPM health

The PIN depends on the TPM.

1. Press **Windows + R**, type `tpm.msc`, and press Enter.
2. Confirm it says **"The TPM is ready for use."**
3. If not, enter BIOS/UEFI and enable TPM/PTT/fTPM.
4. If the TPM was cleared, you'll need to redo Fix 3 (Ngc reset) afterward since the old PIN was sealed to the old TPM state.
5. Then set up the PIN fresh. For full Hello biometric issues beyond the PIN, see our [Windows Hello troubleshooting guide](/articles/how-to-fix-windows-hello-not-working-reddit/).

### Fix 5: Fix Microsoft account sync

Account-side problems invalidate the PIN.

1. Go to **Settings > Accounts > Your info** and verify you're signed in correctly.
2. If you recently changed your Microsoft account password, sign out and back in to refresh cached credentials.
3. Check **Settings > Accounts > Email & accounts** for sync errors and resolve them.
4. Try switching to a local account and back (**Your info > Sign in with a local account instead**, then reverse) to rebuild the credential binding.
5. Set up the PIN again after the account is healthy.

### Fix 6: Check policies and run system repairs

Rule out policy blocks and corruption.

1. On Pro editions, open `gpedit.msc` and check **Computer Configuration > Administrative Templates > System > Logon** and **Windows Components > Windows Hello for Business** for disabled PIN policies.
2. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow`.
3. Install all pending Windows updates — Microsoft fixes Hello regressions regularly.
4. Restart and attempt PIN setup.
5. On Home edition (no gpedit), check the registry path `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System` for an `AllowDomainPINLogon` value that might be blocking.

### Fix 7: New user profile as a last resort

When the profile itself is damaged.

1. Create a new administrator account via **Settings > Accounts > Other users > Add account**.
2. Sign into the new account and set up a PIN there.
3. If the PIN works in the new profile, your old profile is corrupted — migrate your files over.
4. Copy data from `C:\Users\OldName` to the new profile (Documents, Desktop, etc.).
5. Microsoft's [sign-in troubleshooting](https://support.microsoft.com/en-us/windows) covers account recovery edge cases. Brand-specific PIN walkthroughs, like our [PIN fix for Dell laptops](/articles/how-to-fix-pin-not-working-on-windows-11-on-dell-laptop/), cover manufacturer driver quirks.

### Fix 8: Repair from the built-in Administrator account

A damaged main profile can block PIN setup even after the Ngc reset.

1. Open **Terminal (Admin)** and run `net user administrator /active:yes`, then restart.
2. Sign into the **Administrator** account on the sign-in screen.
3. From here, verify the Ngc folder fix (Fix 3) applied cleanly and check `tpm.msc` without profile interference.
4. Create your new PIN setup from this clean administrative context if needed, then test it.
5. When done, sign back into your normal account and disable the built-in one for security: `net user administrator /active:no`.

## Closing

PIN failures look alarming but they're credential-store problems, not security breaches — and the Ngc folder reset fixes most of them in minutes. Remember the order: get in with your password, clear the corrupted store, check the TPM, then rebuild. And keep your Microsoft account password accessible somewhere safe; it's the master key that unlocks every PIN problem. If the PIN breaks again within days of a fix, look at what changed — usually a Windows update or a TPM-related BIOS tweak — and redo the Ngc reset after addressing that root cause.
