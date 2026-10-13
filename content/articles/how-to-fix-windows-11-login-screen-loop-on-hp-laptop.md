---
title: "How to Fix the Windows 11 Login Screen Loop on an HP Laptop"
slug: how-to-fix-windows-11-login-screen-loop-on-hp-laptop
date: 2026-09-27
categories: ["windows-errors"]
tags: ["login-screen-loop", "hp", "windows-11"]
description: "Stuck in a Windows 11 login loop on your HP laptop? Break the sign-in cycle with Safe Mode fixes, credential repairs, and profile checks."
thumbnail: "/images/thumbs/how-to-fix-windows-11-login-screen-loop-on-hp-laptop.webp"
faqs:
  - q: "What exactly is a login screen loop?"
    a: "You enter your password or PIN, Windows appears to sign you in, then dumps you right back at the login screen — sometimes with a 'Preparing Windows' message, sometimes flashing to a black screen first. The sign-in technically succeeds, but something in the user profile or shell fails immediately after, so Windows returns you to the login prompt."
  - q: "Will I lose my files fixing a login loop?"
    a: "No — your files are safe on the disk; you just can't get to them through your profile right now. Every fix here preserves data. In the worst case, you can create a new user profile and copy your files from the old one, which is covered in the steps below."
  - q: "Can a Windows update cause the login loop on HP laptops?"
    a: "Yes, it's a common trigger. Updates that touch the credential manager, user profile service, or graphics driver can break the post-login sequence. HP's own driver updates through HP Support Assistant occasionally contribute too. If the loop started within a day of updates, Safe Mode rollback is your fastest fix."
  - q: "Is the login loop the same as being locked out by a wrong password?"
    a: "No. A wrong password gives you an explicit 'password is incorrect' message and never attempts to sign in. In a loop, the password is accepted — Windows starts loading your profile and then fails. If you're seeing an incorrect-password message instead, that's a credential problem, not a loop."
---
The Windows 11 login loop is uniquely maddening: your password is correct, Windows accepts it, the screen flickers like it's signing you in — and then you're staring at the login screen again. On HP laptops this often follows a Windows update, an HP Support Assistant driver push, or a corrupted user profile. The operating system itself is fine; it's the handoff to your desktop that keeps failing.

Because you can't reach the desktop, the repairs run from Safe Mode and WinRE. The fixes below move from the quickest profile repairs to deeper system fixes. For other brands, see [the Lenovo login loop guide](/articles/how-to-fix-windows-11-login-screen-loop-on-lenovo-laptop/) or [the Acer variant](/articles/how-to-fix-windows-11-login-screen-loop-on-acer-laptop/).

## Why this happens

- **Corrupted user profile.** The most common cause — damage to the profile's registry hive or AppData breaks the sign-in sequence.
- **Broken credential or PIN data.** Corrupted Windows Hello or credential manager data fails post-login authentication steps.
- **Graphics driver crashing at login.** The driver loads during sign-in; a bad one kills the session before the desktop appears.
- **Shell or Explorer failing to start.** If explorer.exe can't launch, Windows returns you to the login screen.
- **Recent Windows or HP driver update.** Updates touching the profile service, credentials, or graphics stack trigger loops.
- **Disk errors in the profile area.** Bad sectors hitting your user folder corrupt profile files.

## How to fix it

Work through these in order. Safe Mode is your gateway.

### Fix 1: Boot into Safe Mode

Safe Mode uses a minimal profile path that often bypasses the loop.

1. At the login screen, hold **Shift** and click the **Power icon > Restart**.
2. When WinRE appears: **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press **4** for Safe Mode.
4. If Safe Mode signs in successfully, the problem is in your normal profile or a third-party driver — continue with the fixes below.
5. If Safe Mode loops too, skip to Fix 6 (system file repair) and Fix 7 (new profile from WinRE).

### Fix 2: Repair the user profile registry entry

A corrupted profile reference in the registry is the classic cause.

1. In Safe Mode, press **Win + R**, type `regedit`, and press **Enter**.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`.
3. Look for two similar keys (SIDs) — one ending in **.bak** and one without. The **.bak** one is your real profile.
4. Rename the key **without** .bak by adding **.tmp** to it, then remove **.bak** from the real one, then rename the **.tmp** one to **.bak**.
5. Select your profile key and set **RefCount** to **0** and **State** to **0** (double-click each DWORD to edit).
6. Close Registry Editor and restart normally.

### Fix 3: Remove corrupted credential data

Bad Windows Hello or credential data can abort the sign-in.

1. In Safe Mode, open **Settings > Accounts > Sign-in options**.
2. Under **PIN (Windows Hello)**, click **Remove** and confirm.
3. Also remove **Fingerprint** or **Facial recognition** if configured.
4. Restart and sign in with your password. Re-add the PIN afterward from the same settings page.
5. If you use a Microsoft account, also verify at account.microsoft.com from another device that the account itself is healthy.

### Fix 4: Roll back the graphics driver

A graphics driver that crashes during session start produces exactly this loop.

1. In Safe Mode, open **Device Manager** (**Win + X > Device Manager**).
2. Expand **Display adapters**, right-click your GPU, and choose **Properties**.
3. On the **Driver** tab, click **Roll Back Driver** if available.
4. If not available, choose **Uninstall device** (tick **Attempt to remove the driver for this device**), restart, and let Windows install its basic display driver.
5. Once you can sign in normally, install the proper driver from [HP Support](https://support.hp.com/us-en) for your model.

### Fix 5: Disable fast startup and problematic startup items

Isolate software interference with the sign-in sequence.

1. In Safe Mode, open **Control Panel > Power Options > Choose what the power buttons do**, click **Change settings that are currently unavailable**, and uncheck **Turn on fast startup**.
2. Open **Task Manager** (**Ctrl + Shift + Esc**), go to **Startup apps**, and disable everything non-Microsoft.
3. Restart normally and test the login.
4. Re-enable startup items in groups afterward to identify any culprit.

### Fix 6: Repair system files from Safe Mode

Fix Windows components involved in sign-in.

1. Right-click **Start** and choose **Terminal (Admin)**.
2. Run: `sfc /scannow`
3. Then: `DISM /Online /Cleanup-Image /RestoreHealth`
4. Restart and attempt a normal login.
5. Also run `chkdsk C: /f` from the same prompt to catch disk errors in the profile area — schedule it and restart if prompted.

### Fix 7: Create a new user profile and migrate

When the old profile is beyond repair, a fresh one gets you working in minutes.

1. In Safe Mode, open **Settings > Accounts > Other users** and click **Add account**.
2. Create a local account (choose **I don't have this person's sign-in information > Add a user without a Microsoft account**).
3. Sign into the new account normally — the loop should be gone.
4. Copy your files from `C:\Users\<old-username>\Documents`, `Desktop`, `Pictures`, etc. to the new profile.
5. For app settings, many programs store data under `AppData` — copy selectively, since corrupted AppData may have caused the loop.

### Fix 8: System Restore as the final fix

Roll the whole system back to before the loop began.

1. From WinRE (**Shift + Restart** from the login screen): **Troubleshoot > Advanced options > System Restore**.
2. Choose the most recent restore point predating the loop.
3. Let it complete and test the login.
4. Microsoft's official account and sign-in troubleshooting is on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

The login loop looks like a password problem but almost never is one — it's a broken profile or a driver crashing the sign-in sequence. The registry profile repair and the new-profile migration resolve the overwhelming majority of cases on HP laptops. Once you're back in, keep a second admin account on the machine; it's the fastest recovery tool you'll ever need if a profile corrupts again.
