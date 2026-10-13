---
title: "Feature Experience Pack Failed to Install: Step-by-Step Fix"
slug: how-to-fix-feature-experience-pack-failed-to-install-step-by-step
date: 2026-10-04
categories: ["windows-update"]
tags:
  - feature experience pack
  - windows update
  - microsoft store
  - step-by-step
  - troubleshooting
description: "Step-by-step fix for the Windows Feature Experience Pack failing to install: Store resets, cache clears, PowerShell re-registration, and profile tests."
thumbnail: "/images/thumbs/how-to-fix-feature-experience-pack-failed-to-install-step-by-step.webp"
faqs:
  - q: "What does error 0x80073D02 mean for the Feature Experience Pack?"
    a: >
      It means a package deployment operation was blocked because the package is in use — typically the Store or a shell component the pack needs to replace is locked. Closing Store apps, rebooting fresh, and retrying usually clears it. If it persists, the PowerShell re-registration in Fix 4 rebuilds the package state that is causing the lock.
  - q: "Why would a Windows Update component need the Microsoft Store fixed?"
    a: >
      The Feature Experience Pack is serviced through infrastructure shared with the Store — its payload staging and registration depend on Store components even though you install it from Windows Update. That is why Store-targeted repairs like wsreset fix what looks like a pure Windows Update failure.
  - q: "Is the PowerShell re-registration command safe?"
    a: >
      Yes. The Add-AppxPackage command with the Store's own manifest simply re-registers the existing Store package for your account — it does not download anything or change your apps and data. Run it in an elevated PowerShell exactly as written. Red warnings about packages already in use are normal and harmless.
  - q: "Do I really need the Feature Experience Pack?"
    a: >
      Not urgently — it carries UX improvements, not security fixes, so skipping it does not leave you vulnerable. But chronic failure usually signals Store or update-cache corruption that will eventually affect important updates, so use it as an early warning and repair the underlying layer rather than ignoring it forever.
---

The Windows Feature Experience Pack fails quietly and annoyingly: update history shows a failed entry, sometimes with 0x80073D02 or 0x80070005, and retrying changes nothing. Because the pack updates shell components through Store-adjacent infrastructure, the fix sequence looks different from a normal update repair — Store health matters as much as Windows Update health.

This is the brand-neutral, step-by-step master guide. It goes deeper than the quick fixes: full Store re-registration via PowerShell, the update cache reset, permission repairs, and the profile-isolation test that tells you whether the problem is your account or your Windows.

Follow the steps in order. Each one targets a specific layer of the pack's delivery chain.

## Why this happens

- **Corrupted Microsoft Store cache:** the pack's payload flows through Store infrastructure; a damaged cache breaks staging.
- **Broken Store app registration:** if the Store app itself is misregistered, dependent component installs fail.
- **Windows Update cache corruption:** a poisoned SoftwareDistribution cache fails the download or hash verification.
- **Permission errors (0x80070005):** the installer cannot write to protected locations, often after overzealous cleanup tools.
- **Stuck Store updates ahead in the queue:** the pack waits behind other frozen Store downloads.
- **Corrupted user profile app data:** per-user pack components fail when the profile's package data is damaged.
- **Servicing stack or system file damage:** the registration step fails even with a good download.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Retry cleanly and note the exact error

Establish the baseline: one clean retry with the error code recorded, so you can measure progress as you work. A reboot clears transient locks on the package files, and closing every app removes the background contention that causes a surprising share of these failures. If the retry succeeds, you just saved yourself six more steps — and if it fails, you now have a documented error code to track against.

1. Reboot fresh with no apps open.
2. Go to Settings > Windows Update, click Check for updates, and install the pack if offered.
3. Record the exact error code from Update history if it fails.
4. A different code after later fixes means progress — keep notes.

### Fix 2: Reset the Store cache with wsreset

The fastest Store-layer fix. It clears cached data without removing apps or changing settings.

1. Press Win + R, type wsreset.exe, and press Enter.
2. Wait for the blank Store window to close by itself.
3. Reboot and retry the pack from Windows Update.
4. If the Store will not open at all afterward, continue — its registration needs repair.

### Fix 3: Repair and reset the Microsoft Store app

Deeper than wsreset: this rebuilds the Store app's own state through Settings. Repair reinstalls the app's files while keeping its data; Reset wipes its data and starts it fresh. Work through them in that order — Repair first because it is non-destructive, Reset only if Repair changes nothing — and reboot between attempts so no stale Store process holds the old state.

1. Go to Settings > Apps > Installed apps > Microsoft Store > Advanced options.
2. Click Repair, then retry the pack install.
3. If it still fails, return and click Reset, then reboot.
4. Retry the pack once more before moving on.

### Fix 4: Re-register the Store package with PowerShell

When the Store's registration is broken at the package level, this command reinstalls it for your account — the heavy artillery of Store repair.

1. Open PowerShell as administrator.
2. Run: Get-AppxPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}.
3. Wait for completion — errors in red about in-use packages are usually harmless.
4. Reboot and retry the pack install from Windows Update.

### Fix 5: Reset the Windows Update components

With the Store layer healthy, fix the Update layer: clear both caches so the pack downloads and verifies cleanly. This is the same cache reset technicians use for every update failure, and it works here because the pack's payload travels through the exact same download pipeline as every other Windows update.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv, net stop bits, net stop cryptsvc.
3. Run: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Restart the services, reboot, and check for updates.

### Fix 6: Test with a new local user account

The definitive isolation test: a fresh profile has clean per-user package data. If the pack installs there, your main profile is the problem.

1. Create a new local account in Settings > Accounts > Other users.
2. Sign in as the new user and run Windows Update.
3. Pack installs fine? Plan a profile migration or repair for your main account.
4. Fails there too? The issue is system-wide — continue to Fix 7.

### Fix 7: Repair system files and check the error code's meaning

The last layer: repair the servicing components, then look up any remaining error specifically.

1. Run DISM /Online /Cleanup-Image /RestoreHealth then sfc /scannow in an elevated prompt, and reboot.
2. Retry the pack install and note any remaining error code.
3. Look up the specific code on the [Windows support hub](https://support.microsoft.com/en-us/windows) for targeted guidance.
4. If the pack installed, run Windows Update once more to confirm everything else is healthy too. For the HP-specific variant of this problem, see [Feature Experience Pack failed on HP](/articles/how-to-fix-feature-experience-pack-failed-to-install-on-hp-laptop/).

## Closing

The Feature Experience Pack fails at the intersection of the Store and Windows Update, so the fix sequence repairs both layers in turn: wsreset, Store re-registration, cache reset, then profile and image repair. Work it top to bottom and the pack installs silently as designed. Most people never need to go past Fix 5 — the profile test in Fix 6 and the image repair in Fix 7 exist for the stubborn minority where the corruption runs deeper than the caches. If the underlying update engine is broken too, the [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-step-by-step/) gets it running again.
