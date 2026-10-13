---
title: "Windows 11 Login Screen Loop: Break Free"
slug: how-to-fix-windows-11-login-screen-loop
date: 2026-09-11
categories: ["windows-errors"]
tags: ["login screen loop", "windows 11", "sign-in problem", "login loop"]
description: "Windows 11 returns you to the login screen after every sign-in? Fix the profile, credential, and service causes behind the loop."
thumbnail: "/images/thumbs/how-to-fix-windows-11-login-screen-loop.webp"
faqs:
  - q: "Why does Windows 11 keep returning me to the login screen?"
    a: "The sign-in succeeds but the user session fails to start, so Windows drops you back at the login prompt. Common causes: a corrupt user profile, a broken credential manager state, the User Profile Service failing to load, disk errors on the profile folders, or third-party software interfering with logon. The fixes below address each in order."
  - q: "Will I lose my files fixing a login loop?"
    a: "No. The repair steps — Safe Mode troubleshooting, profile repair, SFC scans, and credential resets — don't touch your personal files. Only creating a new profile involves moving files, and that's a copy operation, not a deletion. Your data remains on the drive throughout."
  - q: "Can I bypass the login screen to fix the loop?"
    a: "You can't skip authentication, but you can reach a working environment: boot into Safe Mode (which uses a minimal profile path) or sign in as a different user account. From there you can repair the broken profile. The Recovery Environment's Command Prompt is another route that needs no sign-in at all."
  - q: "What if the login loop affects all user accounts?"
    a: "If every account loops, the problem is system-wide, not profile-specific: corrupt system files, a broken credential provider, or disk errors. Prioritize SFC/DISM repairs, chkdsk, and checking the User Profile Service and Credential Manager services. Profile-level fixes only help when one account is affected."
---

The **login screen loop** is a special kind of maddening: you enter the correct password or PIN, Windows appears to sign you in — then dumps you right back at the login screen. Your credentials are fine (wrong passwords give a different error); the problem is that the **user session fails to start** after authentication succeeds. That narrows the suspects to the user profile, the logon services, credential state, and disk errors on profile folders.

First, determine the scope: does it happen for **one account or all accounts**? One account = corrupt profile (most common). All accounts = system-wide (services, system files, disk). That single observation directs the whole repair. For the step-by-step variant of this fix, see [login screen loop step by step](/articles/how-to-fix-windows-11-login-screen-loop-step-by-step/); for PIN-specific failures, [PIN not working step by step](/articles/how-to-fix-pin-not-working-on-windows-11-step-by-step/).

## Why this happens

- **Corrupt user profile**: Damaged profile registry data or profile folders — the number one cause for single-account loops.
- **User Profile Service failure**: The service that loads profiles failing to start or crashing.
- **Corrupt credential state**: Broken Windows Hello, PIN, or Credential Manager data interrupting session setup.
- **Disk errors on profile folders**: Bad sectors or filesystem corruption in `C:\Users\<name>`.
- **Third-party credential providers**: Fingerprint software, corporate logon tools, or "tweaks" breaking the logon chain.
- **Corrupt system files**: Damaged logon components (`winlogon`, `userinit`).
- **Windows update damage**: Updates corrupting profile or credential components.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine the scope — test another account

One test that directs everything.

1. At the login screen, check whether other user accounts are listed. Try signing into a different account.
2. **Other account works** = your profile is corrupt. Skip to Fix 4.
3. **No other account exists or all accounts loop** = system-wide. Continue with Fix 2.
4. If you can't test another account, boot into **Safe Mode** (**Shift** > **Restart** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **4**) — Safe Mode's minimal profile path often succeeds where normal logon fails.

### Fix 2: Check the User Profile Service and Credential Manager

Services that must run for logon to complete.

1. In Safe Mode (or another working account), press **Win + R**, type `services.msc`, press Enter.
2. Find **User Profile Service** — it must be **Running** with **Automatic** startup. If not, start it and set it to Automatic.
3. Do the same for **Credential Manager** and **Windows Biometric Service** (if you use Hello/fingerprint).
4. Restart and test logon. A disabled logon service produces exactly this loop.

### Fix 3: Repair system files and check the disk

For system-wide loops with no profile distinction.

1. Open **Terminal (Admin)** in Safe Mode or a working account.
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `chkdsk C: /f` and restart to scan — filesystem damage in the Users folder breaks profile loading.
4. Restart and test. If SFC repaired logon components, the loop often ends here.

### Fix 4: Repair the corrupt user profile via registry

The definitive fix for single-account loops.

1. Sign into a **different administrator account** (or enable the built-in Administrator from WinRE Command Prompt: `net user administrator /active:yes`).
2. Press **Win + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`.
3. Find your profile's SID key. If it ends in **.bak**, that's the corrupt marker: rename the good key (without .bak) by adding `.tmp`, remove `.bak` from yours, then rename `.tmp` out of the way — or simply delete the `.bak` key if a duplicate exists and yours is the broken one.
4. Check the `RefCount` and `State` values in your key — set both to **0**. Restart and sign in.

### Fix 5: Create a new profile and migrate

When registry repair fails or the profile is too damaged.

1. In a working admin account, go to **Settings** > **Accounts** > **Other users** > **Add account** and create a new local administrator account.
2. Sign into it once (this builds a clean profile), then sign out.
3. Copy your files from `C:\Users\<oldname>\Documents`, `Desktop`, `Pictures`, etc. to the new profile — **don't copy the entire AppData folder**, which may carry the corruption.
4. Reinstall needed applications under the new profile. Keep the old profile until you're sure everything migrated.

### Fix 6: Reset Windows Hello and credential state

For loops tied to PIN, fingerprint, or Hello.

1. In Safe Mode or a working account, go to **Settings** > **Accounts** > **Sign-in options**.
2. Under **PIN (Windows Hello)**, choose **Remove**, then set up the PIN again fresh.
3. Delete stale credentials: **Control Panel** > **Credential Manager** > **Windows Credentials** > remove entries for the affected account's services.
4. Restart and sign in with password first, then re-enroll biometrics. Corrupt Hello containers are a known loop trigger.

### Fix 7: Uninstall recent updates and conflicting logon software

The remaining system-wide causes.

1. **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — remove the most recent quality update if the loop started after it.
2. Uninstall third-party credential providers: fingerprint utilities, corporate VPN logon agents, and Start-menu/logon "tweakers" (**Settings** > **Apps** > **Installed apps**).
3. Check [Microsoft's support site](https://support.microsoft.com/en-us/windows) for known logon issues with your build.
4. Final option: in-place upgrade repair with the Windows 11 ISO (setup > **Keep personal files and apps**), which rebuilds logon components cleanly.

## Closing

The login loop is a session-startup failure, not an authentication failure — and that distinction is the whole diagnosis. One account affected means profile repair or migration; all accounts means services, files, or disk. Work the scope test first and you'll skip half the list. And once you're back in, make a second administrator account: the single most useful recovery tool for any future profile problem is another way to sign in. Test the fix by signing out and back in twice — a loop that survives one successful logon can still return on the next.
