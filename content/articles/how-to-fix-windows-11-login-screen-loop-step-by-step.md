---
title: "How to Fix a Windows 11 Login Screen Loop, Step by Step"
slug: how-to-fix-windows-11-login-screen-loop-step-by-step
date: 2026-09-08
categories: ["windows-errors"]
tags: ["login loop", "windows 11", "sign-in fix", "step by step"]
description: "Stuck in a Windows 11 login loop? Enter your password and get thrown back every time? Fix it step by step, from Safe Mode to profile repair."
thumbnail: "/images/thumbs/how-to-fix-windows-11-login-screen-loop-step-by-step.webp"
faqs:
  - q: "What causes a Windows 11 login loop?"
    a: "The sign-in process starts loading your profile and something crashes it, throwing you back to the login screen. Common causes: corrupt user profile, broken credential or profile services, a recent update that damaged sign-in components, disk errors, or third-party software (especially antivirus or 'tweaker' tools) interfering with logon. Safe Mode usually still works because it skips most of these."
  - q: "Will I lose my files fixing a login loop?"
    a: "No — none of the standard fixes delete personal files. Safe Mode troubleshooting, SFC/DISM repairs, System Restore, and even creating a new profile all preserve your data. Only a full reset without the keep-my-files option risks data, and that's the last resort. Still, back up from Safe Mode or recovery if you can."
  - q: "I can't even get into Safe Mode. What now?"
    a: "Use the recovery environment: force it by interrupting boot twice (hold power during the Windows logo), then **Troubleshoot > Advanced options > Startup Settings > Restart** and press **4** for Safe Mode. If that fails too, use **System Restore** or the recovery **Command Prompt** to run repairs offline."
  - q: "Is the login loop a virus?"
    a: "Almost never. Malware that blocks logon is rare on modern Windows with Secure Boot and Windows Security. The loop is overwhelmingly caused by profile corruption, bad updates, or disk issues. Run a Windows Security offline scan from Safe Mode for peace of mind, but focus your energy on the profile and system repairs below."
---

The Windows 11 login loop is uniquely infuriating: you type your password or PIN, the spinner turns, the screen flashes — and you're right back at the login screen. Your password is correct. Windows just won't let you in. It feels personal, but it's mechanical: something in the sign-in chain is crashing, and Windows is dumping you back to the start instead of completing logon.

This guide walks you through it step by step, from the easiest checks to the deeper repairs. Follow in order and stop when you're back at your desktop.

## Why this happens

- **Corrupt user profile.** The most common cause — damaged profile registry data or profile folders crash the logon process.
- **Broken User Profile Service or Credential Manager.** The services behind sign-in failing to start or crashing.
- **Bad Windows update.** An update that damaged logon components or left the system in a half-updated state.
- **Disk errors.** Corruption in profile or system areas preventing the profile from loading.
- **Third-party interference.** Antivirus, "system optimizer," or credential-related utilities hooking into logon.
- **Incorrect password/PIN sync issues.** Especially with Microsoft accounts after password changes or network issues.
- **Corrupted system files.** Damaged `winlogon`, `lsass`, or related components.
- **Disk encryption pre-boot issues.** BitLocker or third-party encryption failing to unlock cleanly can interrupt the logon chain.

## How to fix it

Work through these in order. Steps 1–3 get most people back in.

### Fix 1: Break the cycle with a hard restart

Sometimes the loop is a one-time logon crash, not a permanent break. A single crashed logon attempt can leave a stuck session behind; a clean restart through recovery clears it.

1. At the login screen, hold **Shift**, click the **power icon**, and choose **Restart**. This boots into the recovery environment instead of retrying logon.
2. Choose **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press **4** for Safe Mode. If Safe Mode logs in fine, the problem is a driver, service, or startup program — continue to Fix 2.
4. If even Safe Mode loops, skip to Fix 5 (System Restore) — the damage is deeper.

### Fix 2: Clean-boot from Safe Mode

Find out whether third-party software is crashing logon.

1. In Safe Mode, press **Win + R**, type `msconfig`, and press **Enter**.
2. On the **Services** tab, tick **Hide all Microsoft services**, then **Disable all**.
3. On the **Startup** tab, open Task Manager and disable every startup item.
4. Restart normally and try logging in. If it works, re-enable services in halves until the culprit returns — then leave it disabled or uninstall it.

### Fix 3: Repair system files from Safe Mode

Fix damaged logon components.

1. In Safe Mode, open **Terminal (Admin)** from **Win + X**.
2. Run `sfc /scannow` and wait for completion.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and attempt a normal login. If SFC found and fixed corruption in logon components, you're likely done.

### Fix 4: Check and restart the profile services

Make sure the machinery behind sign-in is running.

1. In Safe Mode, press **Win + R**, type `services.msc`, and press **Enter**.
2. Verify **User Profile Service**, **Credential Manager**, and **Group Policy Client** are set to **Automatic** and **Running**.
3. If any won't start, note the error — then run `sfc /scannow` again, since a service that won't start usually means its files are damaged.
4. Also check **Event Viewer > Windows Logs > Application** for User Profile Service errors naming the corrupt profile.

### Fix 5: Use System Restore

Roll back whatever change started the loop.

1. From the recovery environment (**Shift + Restart** from the login screen), go to **Troubleshoot > Advanced options > System Restore**.
2. Choose a restore point from before the loop began.
3. Complete the restore and try logging in. This reverses updates, driver installs, and registry changes without touching personal files.

### Fix 6: Create a new user profile

If the old profile is corrupt beyond repair, sidestep it.

1. Boot into Safe Mode and open **Terminal (Admin)**.
2. Create a new admin account:
   `net user NewUser * /add` (set a password when prompted)
   `net localgroup administrators NewUser /add`
3. Restart and log in as NewUser. If it works, your old profile is the problem.
4. Copy your files from `C:\Users\<oldname>` (Documents, Desktop, Pictures, etc.) to the new profile. Don't copy the hidden `NTUSER.DAT` — that's where the corruption lives.

### Fix 7: Check the disk for errors

Disk corruption in profile areas causes persistent loops.

1. In Safe Mode's elevated terminal, run `chkdsk C: /f /r`.
2. Restart to allow the scan, which can take a while.
3. After it completes, retry normal logon. If CHKDSK keeps finding new errors on every run, the drive is failing — back up immediately and plan a replacement.

### Fix 8: Reset with file preservation

The last resort when nothing else breaks the loop.

1. From recovery, choose **Troubleshoot > Reset this PC > Keep my files**.
2. This reinstalls Windows and fixes any logon damage while preserving personal files (you'll reinstall apps).
3. If even the reset fails, the drive or installation is too damaged — back up via the recovery Command Prompt and clean-install from USB media made with the [Microsoft software download page](https://www.microsoft.com/en-us/software-download/windows11) tool.

If password/PIN issues rather than a loop are your problem, [Microsoft's account recovery guidance](https://support.microsoft.com/en-us/windows) covers sign-in troubleshooting. For neighboring issues, see our [Start menu troubleshooting guide](/articles/start-menu-not-working-on-windows-11-troubleshooting/) and the [SrtTrail.txt boot loop fix](/articles/srttrail-txt-blue-screen-error-blue-screen-error-fix/).

## Closing

A login loop is Windows failing to finish something it starts a hundred times a day — almost always a corrupt profile or a bad update. Safe Mode is your way in, System Restore is your time machine, and a fresh profile is your escape hatch. Work the steps in order and you'll be back at your desktop. Once you're in, create a second admin account as a spare key — future logon problems get much easier with a working backup account.
