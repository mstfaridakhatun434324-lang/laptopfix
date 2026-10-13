---
title: "Windows Update Troubleshooter Not Working? Try These Fixes"
slug: "how-to-fix-windows-update-troubleshooter-not-working"
date: "2026-10-02"
categories: ["windows-update"]
tags: ["windows-update", "troubleshooter", "windows-11", "repair"]
description: "The Windows Update troubleshooter itself failing is a special kind of annoying. Here's why it breaks and how to repair it — or work around it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-troubleshooter-not-working.webp"
faqs:
  - q: "What does it mean when the troubleshooter says it can't fix the problem?"
    a: "It means the automated tool ran its checks but could not repair what it found, usually because the underlying corruption is outside its scripted scope. This is common with damaged system files, broken service registrations, or policy restrictions. The manual fixes in this guide cover exactly those situations, so a failed troubleshooter run is a starting point for diagnosis, not a dead end."
  - q: "Can I reinstall the Windows Update troubleshooter?"
    a: "The troubleshooter is a built-in Windows component, not a separate app you can uninstall and reinstall. However, running System File Checker and DISM repairs the files it depends on, which effectively restores it. On newer Windows 11 builds, the troubleshooters also update through Windows Update itself, so getting updates working again refreshes the tool."
  - q: "Why does the troubleshooter crash or freeze when I run it?"
    a: "Crashes usually indicate that a service the troubleshooter depends on, such as the Background Intelligent Transfer Service or the cryptographic service, is in a broken state. Heavy system file corruption or an interfering third-party security tool can also kill it mid-run. Stopping conflicting software and repairing system files first gives the troubleshooter a stable platform to work from."
  - q: "Is there an alternative to the built-in troubleshooter?"
    a: "Yes. Microsoft's former standalone 'wushowhide' and update repair tools have been folded into the built-in experience, but the manual component reset described here does everything the troubleshooter does and more. Third-party repair utilities exist but are unnecessary and sometimes risky; the built-in commands are the safest alternative."
---

It is a special kind of frustration: the tool designed to fix Windows Update is itself broken. You click Run, and it either errors out immediately, freezes halfway, or cheerfully reports that it could not identify the problem. Before you assume the situation is hopeless, know that a failing troubleshooter is usually a symptom with a clear cause — and the manual repairs below do everything the automated tool was supposed to do, with more control.

The troubleshooter is essentially a script that checks services, permissions, and cache integrity. When it cannot run, something it depends on is damaged. Fix the foundation, and the troubleshooter often starts working again; either way, you will have repaired the update pipeline itself in the process.

There is a particular irony in a diagnostic tool that needs diagnosing, but technicians actually welcome it: a troubleshooter that cannot run is giving you information. It is telling you that the failure is not a misconfigured setting it can toggle, but damage in the services, files, or policies it stands on. That reframes the job. Instead of asking the tool to fix Windows Update, you fix the ground the tool stands on — and in doing so, you usually fix Windows Update itself.

## Why this happens

- **Corrupt system files:** The troubleshooter depends on system components that System File Checker can verify and repair.
- **Broken service registrations:** If the Windows Update or BITS services are misregistered, the troubleshooter cannot query or restart them.
- **Third-party interference:** Security suites and "optimizer" tools sometimes block the troubleshooter's diagnostic actions.
- **Policy restrictions:** Group Policy or registry settings on some machines disable troubleshooting or the update services it touches.
- **Outdated troubleshooter packs:** On builds that have not updated in months, the troubleshooter definitions themselves can be stale.
- **User profile issues:** Rarely, a damaged user profile prevents the Settings-based troubleshooters from launching correctly.
- **Pending reboot locks:** A half-finished earlier update can hold locks that freeze any diagnostic touching the servicing stack.
- **DISM component store damage:** Deep corruption in the component store undermines both the troubleshooter and the updates it tries to fix.

## How to fix it

Work through these in order — diagnose first, then act.

One practical tip before you begin: run through these fixes in the order given and test the troubleshooter after each one. The moment it starts working again, you can let it finish the job it was designed for, which often resolves the underlying update problem in the same pass.

### Fix 1: Restart and retry the troubleshooter cleanly

A surprising number of troubleshooter failures are transient — a stuck service or a pending lock clears with a restart.

1. Save your work and restart the laptop fully, not just sleep and wake.
2. After booting, wait two minutes for all startup services to settle.
3. Open Settings, System, Troubleshoot, Other troubleshooters, and run Windows Update again.
4. If it completes this time, apply its fixes and test Windows Update.

### Fix 2: Run the troubleshooter from an administrator context

Some diagnostic actions need elevation that the Settings path does not always provide.

1. Open Command Prompt as administrator.
2. Run `msdt.exe /id WindowsUpdateDiagnostic` to launch the classic update diagnostic with elevation.
3. Follow the wizard, choosing to apply fixes automatically when offered.
4. Restart the laptop after it finishes and check whether updates now work.

### Fix 3: Repair system files with SFC and DISM

This restores the components the troubleshooter depends on, which often revives the tool itself.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to complete — this can take 15 minutes or more.
3. Then run `sfc /scannow` and let it verify and repair protected files.
4. Restart the laptop and run the Windows Update troubleshooter again from Settings.

### Fix 4: Check that required services are running

The troubleshooter cannot function if the services it diagnoses are disabled or broken.

1. Press Win + R, type `services.msc`, and press Enter.
2. Locate Windows Update, Background Intelligent Transfer Service, and Cryptographic Services.
3. Set each one's Startup type to Manual or Automatic, and start any that are stopped.
4. Retry the troubleshooter after confirming all three services respond normally.

### Fix 5: Temporarily disable third-party security software

Overprotective suites are a classic cause of troubleshooters that crash or freeze mid-run.

1. Open your third-party antivirus and disable real-time protection temporarily.
2. Also pause any "PC optimizer" or registry cleaner tools running in the background.
3. Run the Windows Update troubleshooter while the interference is paused.
4. Re-enable your security software immediately afterward, regardless of the outcome.

### Fix 6: Reset the Windows Update components manually

This performs the troubleshooter's core job by hand, and then some.

1. Open Command Prompt as administrator.
2. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the data folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
5. Reboot and test both the troubleshooter and Windows Update itself.

### Fix 7: Check for policy blocks

On some machines, policies silently neuter the troubleshooting infrastructure.

1. Press Win + R, type `gpedit.msc`, and press Enter. If the editor is missing, you are on Home edition and can skip this fix.
2. Navigate to Computer Configuration, Administrative Templates, System, Troubleshooting and Diagnostics.
3. Ensure nothing here is set to disable scripted diagnostics.
4. Also check Windows Components, Windows Update policies for anything disabling the update service.
5. After correcting policies, run `gpupdate /force` and retry the troubleshooter.

### Fix 8: Create a fresh administrator account and test

If the troubleshooter fails only under your profile, the profile itself may be damaged.

1. Open Settings, Accounts, Other users, and add a new local administrator account.
2. Sign out and sign in as the new account.
3. Run the Windows Update troubleshooter from the new profile.
4. If it works there, consider migrating to the new profile or repairing your original one.

If you have worked through the full sequence and the troubleshooter still refuses to run, the remaining possibilities narrow considerably: a deeply damaged user profile, a policy pushed by management software you have not found yet, or system corruption beyond what DISM can repair from the online image. At that point, an in-place upgrade repair — reinstalling Windows 11 over itself while keeping files and apps — rebuilds the entire servicing and diagnostics stack and resolves essentially every remaining case. It takes under an hour on most laptops and leaves you with a fully working troubleshooter. And if the underlying update failure turns out to be the classic disabled-service problem, our guide on [fixing Windows Update error 0x80070422](/articles/how-to-fix-windows-update-error-0x80070422-on-laptop/) walks through that specific repair.

## Closing

A broken troubleshooter is not a dead end — it is a clue pointing at damaged services, files, or policies. The manual repairs above cover the same ground the automated tool was meant to cover, and they usually leave both the troubleshooter and Windows Update itself working again. For the common case where the underlying fault is a stuck service, our guide on [fixing the Windows Update service not running](/articles/how-to-fix-windows-update-service-not-running-reddit/) goes deeper.
