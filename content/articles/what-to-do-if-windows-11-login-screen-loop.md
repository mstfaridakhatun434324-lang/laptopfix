---
title: "Windows 11 Login Screen Loop: What to Do to Break the Cycle"
slug: what-to-do-if-windows-11-login-screen-loop
date: 2026-09-23
categories: ["windows-errors"]
tags: ["windows 11", "login loop", "boot repair"]
description: "Stuck entering your password over and over as Windows 11 throws you back to the login screen? Break the loop with these safe-mode and repair steps."
thumbnail: "/images/thumbs/what-to-do-if-windows-11-login-screen-loop.webp"
faqs:
  - q: "Why does Windows 11 keep returning me to the login screen?"
    a: "The login loop happens when the sign-in process starts but something crashes it before the desktop loads — usually a corrupted user profile, a broken Windows update, a bad graphics or credential driver, or damaged system files. Windows handles the crash by dumping you back at the login screen, which makes it look like your password was wrong even when it wasn't."
  - q: "Is my password actually wrong when this happens?"
    a: "Usually not. If you're sure the password or PIN is correct, the loop itself is the problem, not your credentials. One quick test: if you enter a deliberately wrong password, you should get an 'incorrect password' message. If correct credentials just spin and return you to the login screen with no error, it's the loop, not a credential issue."
  - q: "Can I fix a login loop without losing my files?"
    a: "Yes — every fix except a full clean install preserves your files. Safe Mode, update removal, SFC repairs, and even a 'keep my files' reset all leave your documents intact. Only choose 'remove everything' as an absolute last resort, and back up first by accessing the drive from the recovery command prompt or another PC."
  - q: "What if Safe Mode also loops back to login?"
    a: "Then the damage is deeper than your user profile — likely corrupted system files or a broken update. Skip the Safe Mode fixes and go straight to the recovery environment options: uninstall the latest update, run SFC offline, or use System Restore. Those all work without signing in."
---

Few things are more maddening than typing your correct password, watching Windows pretend to sign you in, and landing right back at the login screen. Again. And again. Your password isn't the problem — something in the sign-in chain is crashing, and Windows is covering it up by bouncing you back.

The way out is to stop trying to log in normally and work from Safe Mode or the recovery environment instead. Here's the full sequence.

## Why this happens

- **Corrupted user profile.** The profile service fails to load your desktop, so Windows aborts the sign-in and returns you to the login screen.
- **Broken Windows update.** An update that installed badly can damage the credential or shell components that sign-in depends on.
- **Faulty graphics driver.** The desktop can't render, so the session dies and you're bounced back.
- **Damaged system files.** Corruption in Winlogon or related components breaks the sign-in process itself.
- **Fast Startup glitches.** The hybrid shutdown state can trap the system in a half-initialized loop.
- **Third-party credential providers.** Fingerprint software, old VPN clients, or custom login tools can hijack and break sign-in.

## How to fix it

Work through these in order, from Fix 1 onward, and stop as soon as you can sign in normally.

### Fix 1: Get into Safe Mode

Safe Mode loads a minimal Windows that usually bypasses whatever is crashing your normal sign-in. Follow our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) if you need the detailed steps.

1. On the login screen, hold **Shift** and click the **Power icon > Restart**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press **4** for Safe Mode (or **5** for Safe Mode with Networking).
4. Sign in — Safe Mode uses a minimal driver set, so the loop usually doesn't happen here.
5. Once in, work through the fixes below from inside Safe Mode.

### Fix 2: Uninstall the latest Windows update

If the loop started after an update, this is very likely your fix.

1. In Safe Mode, open **Settings > Windows Update > Update history**.
2. Click **Uninstall updates** at the bottom.
3. Remove the most recent update and restart normally.
4. If you can't reach Safe Mode, do it from recovery: **Shift + Restart > Troubleshoot > Advanced options > Uninstall Updates**.
5. After you're back in, pause updates for a week so the bad one doesn't reinstall overnight.

### Fix 3: Repair system files

Corrupted sign-in components are repaired the same way as any other system file damage.

1. In Safe Mode, press **Win + X** and open **Terminal (Admin)**.
2. Run `sfc /scannow` and wait for it to complete.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and try signing in normally.
5. If SFC reports unfixable files, run DISM first and then SFC again — DISM repairs the source files SFC uses.

### Fix 4: Turn off Fast Startup

Fast Startup's saved system state can perpetuate the loop across restarts.

1. In Safe Mode, open **Control Panel > Power Options**.
2. Click **Choose what the power buttons do** on the left.
3. Click **Change settings that are currently unavailable**.
4. Uncheck **Turn on fast startup (recommended)**.
5. Click **Save changes**, then shut down fully (not restart) and power back on.

### Fix 5: Test with a new user account

This tells you whether your profile is the problem in about two minutes.

1. In Safe Mode, open **Settings > Accounts > Other users**.
2. Click **Add account** and create a local administrator account.
3. Restart and sign in with the new account.
4. If it works, your old profile is corrupt — migrate your files from `C:\Users\YourOldName` to the new profile.
5. You can keep using the new account permanently; it's cleaner than trying to surgically repair the old one.

### Fix 6: Update or roll back the graphics driver

A broken display driver can kill the desktop right as it loads, which looks exactly like a login loop.

1. In Safe Mode, press **Win + X** and open **Device Manager**.
2. Expand **Display adapters**, right-click your GPU, and choose **Update driver > Search automatically for drivers**.
3. If the loop started after a driver update, use **Properties > Driver > Roll Back Driver** instead.
4. Restart and test a normal sign-in.
5. For a stubborn case, uninstall the GPU driver entirely in Safe Mode and let Windows install its basic driver on reboot.

### Fix 7: Run Startup Repair and check the disk

If you can't get into Safe Mode at all, let the recovery environment do the work.

1. From the login screen, **Shift + Restart** to reach recovery.
2. Go to **Troubleshoot > Advanced options > Startup Repair** and let it run.
3. Then open **Command Prompt** from the same menu and run `chkdsk C: /f` (confirm the drive letter first with `diskpart > list vol`).
4. Also try `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` from that same prompt.
5. Choose **Continue** to restart into Windows and test.

### Fix 8: Reset Windows while keeping your files

When nothing else breaks the loop, a reset reinstalls Windows around your data.

1. From recovery, go to **Troubleshoot > Reset this PC**.
2. Choose **Keep my files**.
3. Prefer **Cloud download** for the cleanest copy of Windows.
4. Let it finish — it takes 30 to 60 minutes.
5. After setup, sign in with your Microsoft account and reinstall your apps fresh rather than restoring old settings that might reintroduce the problem.

## Closing

A login loop feels like being locked out of your own laptop, but it's a software problem with a software answer — you just have to approach from Safe Mode or recovery instead of hammering the password box repeatedly. Uninstall the recent update, repair system files, and test a fresh profile; one of those breaks the cycle in the vast majority of cases. If boot problems keep recurring, the [startup repair walkthrough](/articles/how-to-use-startup-repair-windows-11-on-laptop/) is worth bookmarking, and Microsoft's [official sign-in troubleshooting](https://support.microsoft.com/en-us/windows) covers edge cases.
