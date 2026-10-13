---
title: "How to Fix the Windows 11 Login Screen Loop"
slug: how-do-i-fix-windows-11-login-screen-loop
date: 2026-09-09
categories: ["windows-errors"]
tags: ["login loop", "sign-in", "user profile"]
description: "Windows 11 keeps kicking you back to the login screen? Fix the sign-in loop with profile repairs, credential resets, and Safe Mode cleanup."
thumbnail: "/images/thumbs/how-do-i-fix-windows-11-login-screen-loop.webp"
faqs:
  - q: "Why does Windows 11 keep returning to the login screen?"
    a: "The usual cause is a corrupted user profile or a broken credential component: Windows accepts your password, tries to load the profile, fails, and drops you back at sign-in. Other causes include a corrupted Credential Manager store, a misbehaving startup program that crashes the shell, Windows Hello data corruption, or disk errors damaging profile files. The loop itself rarely means your data is gone."
  - q: "Are my files safe if I'm stuck in a login loop?"
    a: "Almost certainly yes. The loop prevents your profile from loading, but your files still sit intact in C:\\Users\\YourName. You can verify and back them up from the recovery Command Prompt or by booting into Safe Mode. Avoid resetting the PC until you have confirmed your files are backed up, since some reset options remove them."
  - q: "Can I fix a login loop without the password?"
    a: "Many fixes need you to sign in at least once, but not all. From the recovery environment you can run SFC and DISM, create a new administrator account via Command Prompt, and check the disk — all without signing into the broken profile. If the account itself is the problem, a new local admin account created from WinRE often gets you back in."
  - q: "Does a login loop mean my profile is corrupted beyond repair?"
    a: "Not necessarily. Sometimes only the credential cache or a single startup entry is broken, and clearing it restores the profile fully. If the profile registry hive is genuinely damaged, Windows can usually be coaxed into building you a fresh profile while your old files remain accessible in the old profile folder for copying over."
---

The login screen loop is uniquely frustrating: you type your password or PIN, Windows appears to accept it, the screen flashes or spins for a moment — and then you are right back at the login prompt. No error message, no explanation. Your password is correct (a wrong one gives a clear error), but Windows cannot finish signing you in.

This almost always comes down to your user profile failing to load, or something crashing during the sign-in process. The fixes below start with the least disruptive — clearing cached credentials and testing Safe Mode — and work up to creating a fresh profile. Your files are safe through all of it; nothing here deletes data.

## Why this happens

- **Corrupted user profile.** Damaged registry hives or profile files prevent Windows from loading your account.
- **Broken Credential Manager store.** Corrupted saved credentials crash the sign-in process.
- **Windows Hello data corruption.** Damaged PIN or biometric data loops the sign-in even with a correct password.
- **Crashing startup programs or shell extensions.** Something loading at sign-in dies and takes the session down.
- **Disk errors.** Bad sectors in the profile folder corrupt the files Windows needs to sign you in.
- **Recent update damage.** A bad update can break sign-in components system-wide.

## How to fix it

Work through these in order, attempting a normal sign-in after each one.

### Fix 1: Try Safe Mode first

Safe Mode skips most startup items — if you can sign in there, a startup program is likely the culprit.

1. On the login screen, hold **Shift** and click the **power icon > Restart**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press **4** (or **F4**) for Safe Mode.
4. Try signing in. If it works, skip to Fix 3 to clean up startup items.
5. If Safe Mode also loops, continue with Fix 2.

### Fix 2: Remove Windows Hello PIN and biometric sign-in

Corrupted Hello data is a sneaky cause — removing it forces password-only sign-in.

1. If you can reach Safe Mode, go to **Settings > Accounts > Sign-in options**.
2. Under **PIN (Windows Hello)**, click **Remove** and confirm.
3. Remove **Fingerprint** and **Facial recognition** entries too.
4. Restart and sign in with your password.
5. Re-set up the PIN afterward from the same settings page.

If you cannot sign in at all, use the recovery Command Prompt method in Fix 5 to create a new admin account, sign in with that, and then remove the Hello data from the broken account.

### Fix 3: Clean boot — disable crashing startup items

A program crashing at sign-in produces exactly this loop.

1. In Safe Mode, press `Win + R`, type `msconfig`, and press Enter.
2. On the **Services** tab, check **Hide all Microsoft services**, then click **Disable all**.
3. Open **Task Manager** (`Ctrl + Shift + Esc`), go to **Startup apps**, and disable everything.
4. Restart normally and try signing in.
5. If it works, re-enable startup items a few at a time to find the offender.

### Fix 4: Clear the Credential Manager store

A corrupted credential vault can crash sign-in.

1. Sign in via Safe Mode if possible.
2. Open **Control Panel > User Accounts > Credential Manager**.
3. Under **Windows Credentials**, remove entries related to your Microsoft account or anything that looks stale or duplicated.
4. Alternatively, from an admin Command Prompt, the vault lives at `C:\Users\YourName\AppData\Local\Microsoft\Vault` — renaming it forces Windows to rebuild it.
5. Restart and sign in.

### Fix 5: Create a new administrator account from recovery

If the profile itself is broken, a fresh account gets you back into Windows.

1. Boot into WinRE: hold **Shift** on the login screen and click **power icon > Restart**, then **Troubleshoot > Advanced options > Command Prompt**.
2. Create a new admin: `net user FixUser TempPass123 /add` then `net localgroup administrators FixUser /add`.
3. Type `exit`, choose **Continue**, and sign in as **FixUser** with the temporary password.
4. Open **File Explorer** and verify your old files are intact under `C:\Users\YourOldName`.
5. Copy your documents, desktop, and other data to the new account.
6. You can keep using the new account permanently, or use it as a base to repair the old profile.

### Fix 6: Repair the old profile via the registry

If you would rather rescue the original profile:

1. Sign in with the new admin account from Fix 5.
2. Press `Win + R`, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`.
3. Find the subkey for your old account (check **ProfileImagePath**). If there are two similar keys and one ends in **.bak**, the .bak one is your real profile.
4. Rename the broken key, remove **.bak** from the good one, and set its **State** and **RefCount** values to **0**.
5. Restart and try signing into the old account.

Microsoft documents profile repair steps in their [Windows support articles](https://support.microsoft.com/en-us/windows) if you want the official reference.

### Fix 7: Run SFC, DISM, and check the disk

System-level damage can break sign-in for every account.

1. From WinRE's **Command Prompt**, run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the drive letter as needed).
2. Run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
3. Check the disk: `chkdsk C: /f`.
4. Restart and test sign-in.

Similar account and profile trouble on other brands follows the same pattern — see the [Lenovo login loop guide](/articles/how-to-fix-windows-11-login-screen-loop-on-lenovo-laptop/) for a brand-specific walkthrough, and if you can reach Safe Mode, our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) covers the boot options in detail.

## Closing

A login loop feels personal — Windows rejects you without saying why — but it is a mechanical problem with mechanical fixes. Nine times out of ten it is the profile, the Hello data, or a startup program, and the sequence above isolates which one within an hour. Create that backup admin account early so you always have a way in, rescue your files before attempting anything drastic, and you will be back at your desktop with everything intact.
