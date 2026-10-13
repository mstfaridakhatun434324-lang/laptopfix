---
title: "Windows 11 Login Screen Loop: Troubleshoot and Fix"
slug: troubleshoot-windows-11-login-screen-loop
date: 2026-10-04
categories: ["windows-errors"]
tags: ["login-loop", "windows-11", "sign-in"]
description: "Stuck in a Windows 11 login loop? Break the cycle with these Safe Mode, profile, and system repair steps."
thumbnail: "/images/thumbs/troubleshoot-windows-11-login-screen-loop.webp"
faqs:
  - q: "What causes a Windows 11 login screen loop?"
    a: "The most common causes are a corrupted user profile, a broken credential or sign-in component after an update, a startup program crashing the shell, or disk errors damaging profile data. The loop happens when Windows can't finish loading your desktop and throws you back to sign-in."
  - q: "Will I lose my files fixing a login loop?"
    a: "Usually not. Your files live in the profile folder and survive every fix here except a full reset — and even then, the 'Keep my files' option preserves them. Still, if you can reach Safe Mode, back up critical files first."
  - q: "Why does Safe Mode work but normal mode loops?"
    a: "Because Safe Mode skips third-party startup programs, non-essential drivers, and many shell extensions. If Safe Mode is stable, the loop is caused by something that only loads in normal mode — usually a startup app or a shell extension."
  - q: "Can a Windows update cause the login loop?"
    a: "Yes — a partially installed or buggy update can break the sign-in components. Booting to Recovery and uninstalling the latest quality or feature update fixes update-caused loops quickly."
---
# How to Fix the Windows 11 Login Screen Loop

You type your password, the screen goes black or shows "Welcome" forever, and then — you're back at the login screen. Again. The **Windows 11 login loop** means Windows can't finish loading your desktop session, so it bails out and returns you to sign-in. It's infuriating, but it's a solvable problem with a clear diagnostic path.

The key question is whether it's your user profile, a startup program, or the system itself. The fixes below answer that question in order, from least to most invasive. If your problem is a black screen rather than a loop back to login, see our [black screen after update guide](/articles/windows-11-black-screen-after-update-fix/) instead.

## Why this happens

- **Corrupted user profile:** Damaged registry hives or profile data prevent the desktop from loading.
- **Broken update:** A half-installed cumulative or feature update leaves sign-in components inconsistent.
- **Crashing startup program:** An app set to launch at sign-in crashes the shell, and Windows returns you to login.
- **Corrupted credential components:** Damage to the files managing authentication breaks the sign-in handshake.
- **Disk errors:** Bad sectors in the profile or system areas corrupt exactly the files login needs.
- **Malware:** Some malware hooks the login process and breaks it when partially removed.

## How to fix it

Work through these in order. Start by getting into Safe Mode or Recovery.

### Fix 1: Get into Safe Mode

Everything else depends on reaching a working desktop, even a minimal one.

1. At the login screen, hold **Shift** and click the power icon, then **Restart**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press **4** for Safe Mode (or **5** with networking if you need downloads).
4. If you can sign in normally in Safe Mode, the loop is caused by something normal-mode-only — continue to Fix 2. If Safe Mode loops too, skip to Fix 4.

### Fix 2: Disable startup programs

A crashing startup app is the most common normal-mode-only cause.

1. In Safe Mode, press **Ctrl + Shift + Esc** to open Task Manager.
2. Go to the **Startup apps** tab and disable everything (right-click > **Disable**).
3. Also check shell extensions: run `autoruns` (Microsoft Sysinternals, free) if you're comfortable, and disable non-Microsoft Explorer add-ons.
4. Restart normally. If the loop is gone, re-enable startup apps a few at a time to find the offender.
5. Pay special attention to "system optimizer," RGB control, and VPN apps — they're disproportionately responsible.
6. Also open **Task Scheduler** and look under **Task Scheduler Library** for tasks set to run at logon from software you don't recognize — a crashing logon task produces the same loop as a startup app.

### Fix 3: Test with a new user profile

If startup apps aren't it, the profile itself may be corrupted.

1. In Safe Mode, go to **Settings > Accounts > Other users** and click **Add account**.
2. Create a local account (choose **I don't have this person's sign-in information > Add a user without a Microsoft account**).
3. Restart and sign in with the new account.
4. If the new account works fine, your old profile is corrupted: sign in as the new user, copy your files from `C:\Users\<oldname>\Documents`, `Desktop`, etc., and migrate to the new profile.
5. Don't delete the old profile until you've verified every file made it over.

### Fix 4: Uninstall the latest Windows update

If the loop started right after Patch Tuesday, the update is suspect number one.

1. Boot into Recovery (Shift + Restart from the login screen).
2. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
3. Uninstall the latest **quality update** first, restart, and test.
4. If the loop persists, go back and uninstall the latest **feature update** too.
5. Once stable, pause updates for a couple of weeks (**Settings > Windows Update > Pause updates**) to avoid immediate reinstallation of the bad one.

### Fix 5: Repair system files from Recovery

Corrupted sign-in components need repairing outside the broken environment.

1. In Recovery, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the drive letter if your Windows drive mounts differently in Recovery).
3. Then run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
4. Type `exit`, choose **Continue** to reboot, and test login.
5. Microsoft documents offline repair syntax on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Check the disk for errors

Disk corruption in the profile area produces loops that survive every software fix.

1. From the Recovery Command Prompt, run `chkdsk C: /f /r`.
2. Let the full scan complete — it can take a long time on big drives.
3. After rebooting, try logging in again.
4. If chkdsk reports many bad sectors, back up your data immediately (from Safe Mode or by mounting the drive in another PC) — the drive is failing and the loop will return.

### Fix 7: System Restore or reset

When the cause won't reveal itself, restore or rebuild.

1. In Recovery, try **Troubleshoot > Advanced options > System Restore** first — pick a point from before the looping started.
2. If no restore point exists or it fails, use **Troubleshoot > Reset this PC**.
3. Choose **Keep my files** to preserve your data while reinstalling Windows.
4. After the reset, reinstall apps one at a time and test login between batches — if a particular app reintroduces the loop, you've found your culprit the hard way.
5. For crashes that accompany the loop, our [blue screen fix guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) helps with the underlying instability.

## Closing

A login loop is Windows failing to complete the handoff from sign-in to desktop — and the handoff fails for concrete reasons: a bad startup app, a corrupted profile, a broken update, or a damaged disk. Isolate which one with Safe Mode and a test profile, then fix it directly. The loop feels endless when you're in it, but it always has a cause, and causes can be fixed — usually within the hour.
