---
title: "Windows Update Error 0x80070005 on HP Laptop? Access Denied — Fixed"
slug: how-to-fix-windows-update-error-0x80070005-on-hp-laptop
date: 2026-10-07
categories: ["windows-update"]
tags: ["windows update", "0x80070005", "hp", "permissions"]
description: "Error 0x80070005 (Access Denied) blocking Windows Update on your HP laptop? Fix the permissions and get updates installing again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070005-on-hp-laptop.webp"
faqs:
  - q: "What does error 0x80070005 actually mean?"
    a: "It is the standard Windows 'Access Denied' error. During Windows Update, it means the installer was refused permission to read or write a file, folder, or registry key it needs. Unlike missing-file errors, the files usually exist — the installer just is not allowed to touch them. The causes range from altered folder permissions to security software blocking legitimate system writes."
  - q: "Can antivirus cause 0x80070005?"
    a: "Yes — it is one of the more common causes. Security products that aggressively protect system folders can block the update installer's legitimate writes, producing access denied errors that persist through cache clears. A controlled test with real-time protection temporarily disabled identifies this quickly. If confirmed, add the update working folders to the antivirus exclusions rather than leaving protection off."
  - q: "Why does 0x80070005 survive a cache clear?"
    a: "Because the cache is rarely the problem for access denied errors. Clearing SoftwareDistribution fixes missing-file errors, but permission errors live in the ACLs, the registry, the security subsystem, or interfering software — none of which a cache clear touches. That persistence is itself diagnostic: when cache clearing does nothing, investigate permissions next."
  - q: "Is it safe to reset permissions on system folders?"
    a: "The approach in this guide — renaming the update working folders so Windows rebuilds them with correct default ACLs — is safe and standard. It does not touch the permissions of Windows, System32, or user data. Manual ACL editing of core system folders is riskier and unnecessary here; the rename-and-rebuild method achieves the repair without it."
---

Error 0x80070005 means 'Access Denied' — Windows Update tried to read or write something and was refused permission. On HP laptops this surfaces as updates that download fine but fail the moment installation begins, because the install phase is when the engine touches protected system locations.

Permission failures have a distinct flavor: they are consistent, they survive cache clears, and they often trace back to tightened ACLs from security software, botched ownership changes, or corrupted user profiles. This guide repairs the permissions layer methodically, from the update folders outward to the system ACLs, until the installer can do its job.

Access denied errors feel personal — as if the laptop does not trust you. In reality the installer runs as the SYSTEM account, not as you, so your administrator status is irrelevant to the failure. The permission problem exists between Windows' own components, which is why the fixes below target system ACLs and services rather than your user account.

## Why this happens

- **Tightened folder permissions:** The SoftwareDistribution and catroot2 folders need specific system permissions. If ACLs were altered — by optimizers, scripts, or malware — the installer gets access denied.
- **Corrupted user profile permissions:** The update engine runs partly in user context during some phases; a damaged profile with broken permissions poisons those operations.
- **Security software overreach:** Antivirus and endpoint tools that lock down system folders can deny the installer access to locations it legitimately needs.
- **Broken registry permissions:** Update-related registry keys need SYSTEM write access. Altered registry ACLs produce access denied errors deep in the install.
- **HP security suite policies:** HP's enterprise security features can enforce folder restrictions that block servicing operations on business laptops.
- **Ownership drift:** Files owned by deleted user accounts or with broken inheritance chains deny access to the SYSTEM account the installer uses.
- **Corrupted system files:** Damage to the security subsystem itself — the code that evaluates permissions — produces spurious access denied errors.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Take ownership back with the update troubleshooter

Start with the automated repair: the Windows Update troubleshooter resets permissions on update folders and re-registers components, resolving the straightforward ACL cases without manual registry work. A service that refuses to start at all is the [Windows Update service not running](/articles/how-to-fix-windows-update-service-not-running-after-windows-11-update/) problem rather than a permissions one.

1. Open Settings, System, Troubleshoot, Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its fixes.
3. Restart the HP laptop.
4. Retry the failing update to test whether permissions were the issue.

### Fix 2: Reset permissions on the update folders

When the troubleshooter is not enough, reset the ACLs on the update working folders directly. This restores the SYSTEM and administrator access the installer requires.

1. Open Command Prompt as administrator.
2. Stop the update services: net stop wuauserv, net stop cryptSvc, net stop bits.
3. Rename SoftwareDistribution and catroot2 to .old variants so Windows rebuilds them with correct permissions.
4. Restart the services — the rebuilt folders inherit proper ACLs automatically.

### Fix 3: Run the installer as SYSTEM via a clean boot

Third-party software holding locks or injecting permission filters is a classic 0x80070005 source. A clean boot removes those filters so the installer runs with unobstructed system privileges. Once permissions are repaired, restart-phase stalls belong to the [update stuck on restarting](/articles/how-to-fix-windows-update-stuck-on-restarting-after-windows-11-update/) guide.

1. Open msconfig, hide Microsoft services, disable the rest.
2. Disable startup items in Task Manager and restart.
3. Run Windows Update in the clean state.
4. Re-enable normal startup after testing.

### Fix 4: Check HP security suite restrictions

On HP business laptops, Wolf Security or similar suites may enforce policies that restrict servicing. Review the suite's settings for anything blocking system folder writes during updates. HP documents its enterprise update and security policies on the [official HP support site](https://support.hp.com/us-en).

1. Open the HP security suite console and review its protection policies.
2. Look for features restricting writes to Windows or System32 folders.
3. Temporarily relax the relevant policy for a controlled update test — coordinate with IT on managed machines.
4. Document the change so the restriction can be tuned rather than permanently disabled.

### Fix 5: Repair the security subsystem with SFC and DISM

Persistent access denied errors after permission resets suggest damage to the permission-evaluating code itself. The standard system file repairs restore those components.

1. Run DISM /Online /Cleanup-Image /RestoreHealth from an elevated prompt.
2. Follow with sfc /scannow and restart.
3. Retry the update after both repairs complete.
4. If 0x80070005 persists, the error code will now be accompanied by clearer symptoms.

### Fix 6: Create a fresh administrator profile as a diagnostic

A corrupted user profile can poison the user-context portions of updating. Testing updates from a brand-new administrator account isolates profile damage definitively.

1. Create a new local administrator account in Settings, Accounts.
2. Log into the new account.
3. Run Windows Update from the fresh profile.
4. If updates succeed there, migrate to the new profile — the old one's permission damage is not worth repairing piecemeal.

### Fix 7: Use the in-place upgrade for widespread permission damage

When permission repairs, clean boots, and profile tests all fail, the ACL damage is too widespread to fix piecemeal. An in-place upgrade reinstalls Windows with fresh, correct permissions across every system folder while preserving your files and applications — the definitive reset for permission chaos.

1. Back up important files as a precaution first.
2. Download current Windows 11 installation media.
3. Run setup.exe from the mounted ISO, keeping files and apps.
4. Verify that updates install normally after the upgrade.

## Closing

Error 0x80070005 is a permissions problem wearing an update problem's clothes: the installer is ready, the files are present, but access is denied. Reset the update folder permissions, eliminate interfering software with a clean boot, check HP's security policies, and repair the security subsystem when the damage runs deeper. Restore the installer's access and the updates flow.
