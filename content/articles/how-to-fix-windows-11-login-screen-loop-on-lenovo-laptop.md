---
title: "Windows 11 Login Screen Loop on a Lenovo Laptop: How to Break It"
slug: how-to-fix-windows-11-login-screen-loop-on-lenovo-laptop
date: 2026-10-11
categories: ["windows-errors"]
tags: ["windows 11", "login loop", "lenovo", "user profile"]
description: "Type your password, screen flashes, and you're back at login on your Lenovo? Here's how to break the Windows 11 login loop for good."
thumbnail: "/images/thumbs/how-to-fix-windows-11-login-screen-loop-on-lenovo-laptop.webp"
faqs:
  - q: "Why does Windows 11 keep returning to the login screen after I enter my password?"
    a: "The sign-in process is crashing partway through. The usual causes: a corrupted user profile, a broken credential or PIN component after an update, or a startup program that crashes the shell. Windows fails safe by dumping you back at the login screen instead of loading a broken desktop."
  - q: "Will I lose my files if I create a new user account to fix this?"
    a: "No. Your old profile's files stay on disk under C:\\Users\\YourName. After creating a new account and logging in, you can copy documents, photos, and desktop files from the old profile folder into the new one. Only some app settings won't transfer."
  - q: "Can I fix the login loop without another computer?"
    a: "Yes. Everything in this guide is done from the login screen itself or the built-in Recovery Environment — Safe Mode, Command Prompt, and System Restore are all reachable without installation media or a second device."
  - q: "Is the login loop caused by a Windows update?"
    a: "Often, yes. Updates that touch authentication components — PIN, Windows Hello, or credential managers — can leave sign-in broken. If the loop started right after an update, uninstalling it from the Recovery Environment is one of the most reliable fixes."
---

Windows 11 Login Screen Loop on a Lenovo Laptop: How to Break It

You type your password (or PIN), hit Enter, the screen flashes like it's about to load your desktop — and then you're staring at the login screen again. Welcome to the login loop: Windows accepts your credentials just fine, then something in the sign-in process falls over and you're bounced straight back. It's maddening, but it's fixable, and your files are safe.

Lenovo laptops have a couple of quirks worth knowing here — notably the Novo button for recovery access — which this guide covers alongside the standard fixes. Work from the login screen and the Recovery Environment; no second computer needed. If Windows won't even reach the login screen, our [Automatic Repair loop guide](/articles/how-to-fix-automatic-repair-loop-windows-11-step-by-step/) is the right starting point instead.

## Why this happens

- **The user profile is corrupted.** Damage to the profile registry hive or the NTUSER.DAT file makes Windows abort the sign-in and return you to the login screen.
- **A Windows update broke authentication.** Updates touching PIN, Windows Hello, or credential components can leave sign-in half-functional: password accepted, desktop never loads.
- **A startup program crashes the shell.** If Explorer or a startup app dies during logon, Windows drops you back to login.
- **The PIN credential provider is broken.** PIN sign-in failing silently while password works (or vice versa) is a classic post-update symptom.
- **Disk errors damaged profile files.** Bad sectors landing on profile data produce a loop that looks identical to corruption.
- **Third-party credential software conflicts.** Fingerprint utilities, corporate SSO tools, or old Lenovo VeriFace-style software can hook logon and break it.

## How to fix it

Work through these in order. Most login loops surrender by Fix 4.

### Fix 1: Try Safe Mode from the login screen

Safe Mode skips the startup programs and third-party credential hooks that often cause the loop.

1. On the login screen, hold **Shift** and click the **Power icon > Restart**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode.
3. Try logging in. If it works in Safe Mode, the problem is a startup program or driver — continue to Fix 2.
4. If Safe Mode also loops, skip ahead to Fix 4 (the profile is likely the issue). For more Safe Mode details, see [how to boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/).

### Fix 2: Disable startup programs and clean-boot

A crashing startup item is the easiest cause to eliminate.

1. In Safe Mode, press **Ctrl + Shift + Esc** to open Task Manager.
2. Go to the **Startup apps** tab and disable everything non-Microsoft.
3. Press **Win + R**, type `msconfig`, and on the **Services** tab tick **Hide all Microsoft services**, then click **Disable all**.
4. Reboot normally and try logging in. If it works, re-enable items in small groups to find the offender.

### Fix 3: Switch sign-in methods and reset the PIN

When the PIN provider is the broken piece, sidestep it.

1. On the login screen, click **Sign-in options** and try a different method — password instead of PIN, or vice versa.
2. If the password works but PIN loops, sign in with the password, then go to **Settings > Accounts > Sign-in options > PIN (Windows Hello)** and remove and re-add your PIN.
3. If you can't sign in at all to change it, use Fix 5 (System Restore) or Fix 6 (new account) instead.
4. Also worth trying: disconnect from Wi-Fi on the login screen (click the network icon) — a hanging Microsoft account verification can stall logon.

### Fix 4: Fix or replace the corrupted user profile

Profile corruption is the number one cause of true login loops.

1. Boot into Safe Mode and log in with the built-in Administrator account if it's enabled. If not, enable it from Recovery's Command Prompt with:
   `net user administrator /active:yes`
2. Once in as Administrator, open Registry Editor (`regedit`) and go to **HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList**.
3. Find your profile's SID key — if you see two similar keys with one ending in `.bak`, that's the corruption signature. Rename the non-`.bak` key by adding `.tmp`, remove `.bak` from the good one, and set its **RefCount** to `0` and **State** to `0`.
4. Reboot and try logging in normally.

### Fix 5: Create a fresh user account

When the profile is beyond repair, a new account gets you back in within minutes.

1. From Recovery, open **Command Prompt** via **Troubleshoot > Advanced options**.
2. Create a new admin account:
   `net user NewUser TempPass123 /add`
   `net localgroup administrators NewUser /add`
3. Reboot, log in as **NewUser**, and confirm the desktop loads.
4. Open File Explorer, navigate to `C:\Users\YourOldName`, and copy your **Desktop**, **Documents**, **Pictures**, and other personal folders into the new profile.
5. Change the temporary password immediately via **Settings > Accounts > Sign-in options**.

### Fix 6: Run System Restore from the Recovery Environment

A restore point from before the loop began undoes whatever broke sign-in.

1. From the login screen, **Shift + Restart** to reach Recovery, then **Troubleshoot > Advanced options > System Restore**.
2. Choose the most recent point dated before the loop started.
3. Let it finish and reboot. Your files are untouched by System Restore.
4. Lenovo owners: you can also reach recovery via the **Novo button** (the small pinhole button beside the power button) — power off, press it with a paperclip, and choose **System Recovery**.

### Fix 7: Uninstall the latest update and check the disk

If the loop began with an update, remove it; then verify the disk isn't the root cause.

1. In Recovery, go to **Troubleshoot > Advanced options > Uninstall Updates** and remove the latest quality update, then test.
2. Open **Command Prompt** in Recovery and run `chkdsk C: /f` (confirm the Windows drive letter first) to fix file-system errors that may have damaged the profile.
3. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` to repair system files offline.
4. If the loop survives all of this, a failing drive is likely — check SMART health with Lenovo's diagnostics (via the Novo button menu) and back up your data promptly. Lenovo's [support site](https://support.lenovo.com/us/en/) can help verify warranty status with your serial number.

## Closing

The login loop is Windows failing safe: rather than load a broken desktop, it hands you back the login screen. That protectiveness is actually convenient — it means the system underneath is intact. Fix the profile, evict the bad update or startup program, and you'll be typing your password exactly once from now on.
