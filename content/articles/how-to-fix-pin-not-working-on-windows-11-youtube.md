---
title: "Windows 11 PIN Not Working? Get Signed In Again"
slug: how-to-fix-pin-not-working-on-windows-11-youtube
date: 2026-09-19
categories: ["windows-errors"]
tags: ["pin", "sign-in", "windows hello"]
description: "Your Windows 11 PIN stopped working and you're locked out? These fixes reset Windows Hello, repair the PIN store, and restore sign-in access."
thumbnail: "/images/thumbs/how-to-fix-pin-not-working-on-windows-11-youtube.webp"
faqs:
  - q: "Why does Windows 11 suddenly say my PIN is incorrect?"
    a: "The PIN's encrypted credential store can corrupt after updates, TPM issues can invalidate it, or the NGC folder permissions break. It's rarely your actual PIN being wrong — the stored credential Windows compares against is usually the damaged part."
  - q: "I forgot my PIN and can't sign in. What are my options?"
    a: "On the sign-in screen, click Sign-in options and use your Microsoft account password instead. Once in, go to Settings > Accounts > Sign-in options > PIN and set a new one. For local accounts, you'll need a password reset disk or an admin account."
  - q: "Will deleting the NGC folder delete my files?"
    a: "No. The NGC folder only holds Windows Hello credentials (PINs, fingerprints). Deleting it removes your PIN so you can set a fresh one. Your files, apps, and settings are completely unaffected."
  - q: "My PIN option is grayed out in Settings. How do I fix that?"
    a: "This usually means the TPM is disabled or not detected. Enable TPM in your BIOS/UEFI settings, or check that the TPM Management Console (tpm.msc) shows the TPM ready. Some older laptops genuinely lack a TPM, in which case PIN may be unavailable."
---
You type your PIN — the same one you've used a hundred times — and Windows 11 insists it's wrong. Or the PIN option doesn't appear at all, or it throws an error like "Something went wrong." Being locked out of your own laptop is stressful, but the PIN system is repairably fragile, and these fixes cover every common failure.

Start at the top and work down. If you're currently locked out at the sign-in screen, jump to Fix 1 first for the emergency way back in. For broader login trouble beyond the PIN, see our guide on [factory resetting without a password](/articles/how-to-factory-reset-windows-11-laptop-without-password/) as a last resort.

## Why this happens

- **Corrupted NGC credential store.** The folder holding your PIN data gets damaged, often after updates.
- **TPM problems.** Windows Hello PINs are tied to the Trusted Platform Module; if the TPM resets or is disabled, the PIN breaks.
- **Broken Windows Hello components.** System file corruption can disable the PIN sign-in path.
- **Microsoft account sync issues.** Password changes or account security events can invalidate the cached PIN.
- **Corrupted user profile.** Profile-level damage can break Hello credentials for one account only.
- **Group Policy or registry changes.** Some tweaks and enterprise policies disable PIN sign-in.
- **Failed Windows update.** Updates that touch security components frequently break PINs temporarily.

## How to fix it

Work through these in order — stop when your PIN works again.

### Fix 1: Sign in with your password instead

Get back into Windows first; fix the PIN second.

1. On the sign-in screen, click **Sign-in options** below the PIN box.
2. Choose the **password** icon (it looks like a key) instead of the PIN icon.
3. Enter your Microsoft account password. If you've forgotten it, use another device to reset it at Microsoft's account site.
4. For a local account, enter the account password you set when creating it.
5. Once you're on the desktop, don't skip the remaining fixes — the PIN won't heal itself.
6. If no sign-in options appear at all, click the **power icon** on the sign-in screen, hold **Shift**, and click **Restart** to reach the Recovery Environment for the deeper fixes below. Our [Safe Mode boot guide](/articles/how-to-boot-windows-11-in-safe-mode/) lists other ways to reach recovery if that doesn't work.

### Fix 2: Reset your PIN from Settings

The official reset path — quick when it works.

1. Open **Settings > Accounts > Sign-in options**.
2. Under **PIN (Windows Hello)**, click **Remove**. Confirm the removal.
3. Restart the laptop (this clears cached credential state).
4. Go back to **Settings > Accounts > Sign-in options > PIN (Windows Hello)** and click **Set up**.
5. Verify your identity with your Microsoft account password when asked.
6. Enter a new PIN twice and click **OK**. Sign out and test the new PIN.

### Fix 3: Delete the NGC folder and recreate the PIN

This is the heavy-hitter fix for corrupted PIN stores.

1. Open File Explorer and navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft`.
2. You'll see a folder called **NGC**. If access is denied, you need to take ownership: right-click **NGC > Properties > Security > Advanced > Change** owner to your account, then grant yourself full control.
3. Alternatively, open an elevated terminal and run:
   `takeown /f C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /r /d y`
   `icacls C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /grant administrators:F /t`
4. Delete everything inside the **NGC** folder (not the folder itself if Windows resists — emptying it is enough).
5. Restart the laptop.
6. Go to **Settings > Accounts > Sign-in options > PIN (Windows Hello) > Set up** and create a fresh PIN.

### Fix 4: Check and reset the TPM

Since PINs are TPM-backed, a sick TPM breaks them.

1. Press **Win + R**, type `tpm.msc`, and press **Enter**.
2. Check the status: it should say **The TPM is ready for use**. Note the specification version too.
3. If it shows an error or "TPM not found," restart and enter your BIOS/UEFI (usually **F2**, **Del**, or **F12** during boot).
4. Find the TPM/Security chip setting (often under **Security** or **Advanced**) and make sure it's **Enabled**.
5. Save and exit. If `tpm.msc` still shows problems, use its **Clear TPM** action — you'll need to re-set-up the PIN afterward, but it fixes TPM corruption. Microsoft's [TPM guidance](https://support.microsoft.com/en-us/windows) explains the implications before you clear.
6. After the TPM is healthy, set up a new PIN via Fix 2.

### Fix 5: Re-register Windows Hello components

If the PIN infrastructure itself is damaged, rebuild it.

1. Open an elevated PowerShell: right-click **Start > Terminal (Admin)**.
2. Re-register the Hello credential packages:
   `Get-AppxPackage -AllUsers Microsoft.AccountsControl | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Then repair system files that Hello depends on:
   `sfc /scannow`
4. Restart the laptop.
5. Go to **Settings > Accounts > Sign-in options** and check whether the PIN option is available and functional.
6. If the PIN section is still missing, continue to Fix 6.

### Fix 6: Enable PIN via policy and registry

Sometimes the PIN option is administratively disabled.

1. Press **Win + R**, type `gpedit.msc`, and press **Enter** (Pro/Enterprise editions only).
2. Navigate to **Computer Configuration > Administrative Templates > System > Logon**.
3. Find **Turn on convenience PIN sign-in** and set it to **Enabled**.
4. On Home edition, use the registry instead: open `regedit`, go to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System`, and create a DWORD named **AllowDomainPINLogon** set to **1**.
5. Restart the laptop.
6. Check **Settings > Accounts > Sign-in options** — the PIN setup should now be available.

### Fix 7: Create a new user profile

If everything else fails, the profile's credential store may be unrecoverable.

1. Sign in with your password (Fix 1) and open **Settings > Accounts > Other users**.
2. Add a new local account, make it an administrator.
3. Sign into the new account and set up a PIN there via **Settings > Accounts > Sign-in options**.
4. If the PIN works on the new profile, your old profile is corrupt — move your files over.
5. Copy data from `C:\Users\<oldname>` to the new profile (Documents, Desktop, Downloads, Pictures).
6. Once everything is moved, you can remove the old account. Keep the new PIN backed by your Microsoft account password as a fallback.

## Closing

A dead PIN is almost never a forgotten PIN — it's a corrupted credential store, and deleting the NGC folder fixes the vast majority of cases. Keep your Microsoft account password memorized (or in a password manager) as your permanent backup key, and you'll never be truly locked out. If PIN problems keep recurring after updates, check that your TPM firmware is current — laptop makers occasionally ship TPM firmware updates that stabilize Windows Hello.
