---
title: "How to Fix Microsoft Store Errors Step by Step"
slug: how-to-fix-microsoft-store-error-step-by-step
date: 2026-09-23
categories: ["windows-errors"]
tags: ["microsoft-store", "step-by-step", "windows-11"]
description: "A complete step-by-step repair sequence for any Microsoft Store error: cache resets, account fixes, update repairs, and the PowerShell re-register trick."
thumbnail: "/images/thumbs/how-to-fix-microsoft-store-error-step-by-step.webp"
faqs:
  - q: "What are the most common Microsoft Store error codes?"
    a: "The frequent ones are 0x80070005 (access denied, usually cache or permissions), 0x803F8001 (license sync problem), 0x80070422 (a required service is disabled), and 0x8024001E (Windows Update components broken). Most share the same handful of root causes, which is why a fixed repair sequence works for nearly all of them."
  - q: "How long does it take to fix a Microsoft Store error?"
    a: "Most Store errors are fixed in under 15 minutes. The cache reset takes about a minute, the app reset another two, and the troubleshooter around five. Only the SFC/DISM repairs and Windows Update component resets take longer — 15 to 30 minutes — and you only need those if the quick steps fail."
  - q: "Why does the Store say 'Try again later' for every app?"
    a: "That generic message usually means the Store can't reach Microsoft's servers or can't verify your licenses. Check your internet connection, confirm the date and time are correct, and sign out and back into your Microsoft account in the Store. If it persists, the Windows Update service may be stuck."
  - q: "Can I reinstall the Microsoft Store if nothing works?"
    a: "Yes, but try the PowerShell re-register command first — it rebuilds the Store's registration without a true reinstall. A full removal and reinstall via PowerShell is possible but rarely needed, and it carries a small risk of leaving the Store in a worse state if the commands are mistyped."
---
Microsoft Store errors come in many flavors — cryptic codes like 0x80070005, blank pages, downloads stuck at "Pending," or the classic "Try again later." But underneath the variety, almost every Store failure traces back to the same short list of causes. That means one fixed sequence, followed in order, resolves nearly all of them without guesswork.

Think of this as the master checklist. Each step takes a few minutes, each targets the next most likely cause, and you stop as soon as the Store works. No step deletes your apps or purchases — those live with your Microsoft account, not on the laptop.

## Why this happens

- **Corrupted Store cache**: the temporary files the Store uses for speed get damaged and the app can't load properly.
- **Incorrect system clock**: certificate validation fails when your date or time is off, blocking the Store's secure connections.
- **Signed-out or stale Microsoft account**: license checks fail when the account token is expired or corrupted.
- **Broken Windows Update components**: the Store shares download machinery with Windows Update, so one breaks the other.
- **Disabled background services** like Background Intelligent Transfer Service (BITS), which the Store needs for downloads.
- **Damaged Store app registration**: failed updates can unregister the Store's package from Windows.
- **Proxy or VPN interference** rerouting Store traffic through servers that Microsoft's license checks don't trust.
- **Pending Windows updates** holding shared components in a half-updated state that the Store can't work with.

## How to fix it

Work through these in order, from quickest to most involved.

### Fix 1: Clear the cache with WSReset

The fastest fix and the right first move for any Store misbehavior.

1. Press **Win + R**, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window opens. Leave it alone until the Store launches by itself.
3. Try downloading or updating an app immediately.
4. If the Store still errors, continue to Fix 2 — cache wasn't the whole story.

### Fix 2: Verify date, time, and region

Takes thirty seconds and fixes a surprising number of "mystery" Store errors.

1. Open **Settings** → **Time & language** → **Date & time**.
2. Enable **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
3. Open **Time & language** → **Language & region** and confirm the country/region matches where you are.
4. Relaunch the Store and test.

### Fix 3: Repair, then reset the Store app

Windows can repair the Store's files in place — try repair before the heavier reset.

1. Go to **Settings** → **Apps** → **Installed apps**, find **Microsoft Store**, click **···** → **Advanced options**.
2. Click **Repair** and wait for the checkmark. Test the Store.
3. Still broken? Click **Reset** and confirm. This clears the Store's local data; your apps and purchases are unaffected.
4. Open the Store again — a reset Store often needs one successful launch to re-sync licenses.

### Fix 4: Sign out and back into your Microsoft account

A stale account token causes license errors like 0x803F8001 that look like Store bugs.

1. In the Store, click your profile picture (top right) and choose **Sign out**.
2. Close the Store completely — check Task Manager to make sure no Store process lingers.
3. Reopen the Store and sign back in with your Microsoft account.
4. If sign-in itself fails, verify your credentials at account.microsoft.com in a browser first.

For HP-specific Store quirks like outdated network drivers after recovery installs, see our [HP laptop Store fix guide](/articles/how-to-fix-microsoft-store-error-on-hp-laptop/).

### Fix 5: Run the Store Apps troubleshooter

Let Windows check the services and permissions the Store depends on.

1. Open **Settings** → **System** → **Troubleshoot** → **Other troubleshooters**.
2. Click **Run** next to **Windows Store Apps**.
3. Apply any recommended fix, then restart the laptop even if it reports no problems.
4. Test the Store after the reboot.

### Fix 6: Re-register the Store via PowerShell

When the Store's package registration is damaged, this rebuilds it.

1. Press **Win + X** → **Terminal (Admin)**.
2. Run: `Get-AppXPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for completion — the command produces no success message, just a new prompt.
4. Restart and open the Store.

### Fix 7: Reset Windows Update components and repair system files

The heavy artillery for Store errors rooted in broken update machinery (0x8024001E, stuck downloads).

1. In **Terminal (Admin)**, stop the update services:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
2. Rename the data folders:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
3. Restart the services:
   `net start wuauserv`
   `net start cryptSvc`
   `net start bits`
   `net start msiserver`
4. Run `sfc /scannow` and then `DISM /Online /Cleanup-Image /RestoreHealth`.
5. Open **Settings** → **Windows Update**, install pending updates, then test the Store. If the Store broke right after a feature update, our [Store error after Windows 11 update](/articles/how-to-fix-microsoft-store-error-after-windows-11-update/) guide covers that specific scenario.

If your Store problems started right after a Windows update, check Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) for known issues with that update — sometimes the fix is simply the next cumulative patch.

### Fix 8: Check required services and test a new user profile

The last two suspects: a disabled service, or a corrupted user profile.

1. Press **Win + R**, type `services.msc`, and confirm these are running (set to Automatic or Manual, not Disabled): **Background Intelligent Transfer Service**, **Windows Update**, **Microsoft Store Install Service**.
2. If any is Disabled, double-click it, set **Startup type** to **Automatic**, click **Start**, then **OK**.
3. If the Store still fails, create a test account: **Settings** → **Accounts** → **Other users** → **Add account**.
4. Sign into the Store on the new profile. Working there means your main profile is corrupted — migrate your files to the new account rather than fighting the old one.

## Closing

That's the complete sequence: cache, clock, repair, account, troubleshooter, re-register, update components, services and profile. In practice, nine out of ten Store errors surrender somewhere in the first five steps, and the remaining one is usually a broken update service hiding underneath. Work the list top to bottom, stop when the Store behaves, and let it update itself and your apps afterward — a current Store is a far less troublesome Store.
