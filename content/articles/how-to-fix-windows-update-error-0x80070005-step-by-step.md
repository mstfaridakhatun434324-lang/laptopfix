---
title: "Windows Update Error 0x80070005: Access Denied Fix That Actually Works"
slug: how-to-fix-windows-update-error-0x80070005-step-by-step
date: 2026-10-13
categories: ["windows-update"]
tags:
  - "windows update"
  - "error 0x80070005"
  - "access denied"
  - "windows 11"
description: "Error 0x80070005 means Windows Update was denied access to files it needs. Follow this technician-tested sequence to fix permissions, reset update components, and get updates installing again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070005-step-by-step.webp"
faqs:
  - q: "What does Windows Update error 0x80070005 actually mean?"
    a: "Error 0x80070005 is the Windows code for ACCESS DENIED. It means the update engine tried to read or write a file, registry key, or service it did not have permission for. On laptops the usual triggers are corrupted permissions on the SoftwareDistribution folder, an overprotective antivirus, or a user account that lost administrator rights."
  - q: "Can my antivirus cause error 0x80070005 during updates?"
    a: "Yes, and it is one of the most common causes. Third-party security suites sometimes lock the folders and services Windows Update relies on, which produces an access-denied failure. Temporarily disabling real-time protection while you retry the update is a safe diagnostic step, and you should re-enable protection immediately afterward."
  - q: "Will resetting Windows Update components delete my personal files?"
    a: "No. Resetting the components only clears the update cache folders (SoftwareDistribution and catroot2) and re-registers update services. Your documents, photos, installed programs, and settings are untouched. The next update check simply re-downloads fresh copies of the update files it needs."
  - q: "How can I stop error 0x80070005 from coming back?"
    a: "Keep your everyday account as an administrator or run updates from an admin account, leave the Windows Update service on its default Automatic startup type, avoid aggressive system-tweaking utilities, and keep your antivirus definitions current instead of disabling protection permanently. A clean system image backup before major feature updates also helps."
---

Error 0x80070005 is Windows telling you, in its own cryptic way, that it was denied access to something it needs. When Windows Update throws this code on a laptop, the download may finish fine but the install fails, or the update check itself errors out immediately. Either way, the machine keeps missing security patches, and that is not a state you want a portable computer in.

As a technician, I see this error most often after a third-party antivirus was installed, after a registry cleaner or tweaker ran, or after file permissions got mangled by a botched migration. The good news: this is a permissions and services problem, not a hardware problem, and it responds well to a methodical repair sequence. Randomly reinstalling Windows is overkill here.

Below is the exact order I use on customer laptops: start with the lightweight checks, repair system files, reset the update engine cleanly, and only then touch permissions and security software. If you are stuck in a loop where updates keep failing, also read our guide on [updates that fail and roll back](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-step-by-step/) — the two problems often travel together.

## Why this happens

- **Access denied at the file-system level:** the classic meaning of 0x80070005 is that a process tried to touch a file or folder without the rights to do so, and the update engine hits this when its cache folders have broken ACLs.

- **Third-party antivirus interference:** security suites can quarantine update temp files or block the TrustedInstaller service, which surfaces as an access-denied error mid-install.

- **Corrupted SoftwareDistribution permissions:** if a previous update was interrupted, the download cache can end up owned by the wrong security principal, so every later update fails the same way.

- **Windows Update service misconfiguration:** the wuauserv, cryptSvc, bits, and msiserver services must run with the right logon accounts and startup types; a tweaker or malware can change them.

- **Non-administrator user account:** standard users cannot always approve the elevated operations a feature update needs, and on some domain-joined laptops policy restrictions compound this.

- **Corrupt system files:** damaged servicing stack or component store files make the installer bail out with a generic access error instead of a precise one.

- **Malware or rootkit activity:** malicious software sometimes locks system directories deliberately, and update failures are a common side effect worth ruling out.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter

Start with the built-in diagnostic. It checks service states, repairs common registry entries, and clears stale update tasks. It resolves permission-adjacent failures more often than people expect, and it takes two minutes.

1. Open Settings with Win + I, go to System, then Troubleshoot, then Other troubleshooters.
2. Click Run next to Windows Update and let the scan finish completely.
3. Apply every fix it offers, then restart the laptop even if it does not ask.
4. Return to Settings, then Windows Update, and click Check for updates to test.
5. If the troubleshooter itself errors, our guide on [a broken update troubleshooter](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) covers that scenario.

### Fix 2: Repair system files with SFC and DISM

Corrupt servicing files are a frequent hidden cause of access-denied update failures. The System File Checker and DISM restore them from known-good copies, which often clears the error without touching permissions at all.

1. Right-click Start, choose Terminal (Admin), and approve the elevation prompt.
2. Run `sfc /scannow` and wait for it to reach 100 percent, then restart.
3. Back in an admin terminal, run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Let DISM finish (it can take 15-30 minutes on a laptop), then restart again.
5. Retry Windows Update before moving on to deeper fixes.

### Fix 3: Reset the Windows Update components

This is the core repair for 0x80070005. Stopping the update services, renaming the cache folders, and restarting everything forces Windows to rebuild the download cache with correct ownership and permissions from scratch.

1. Open Terminal (Admin) from the Start right-click menu.
2. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services with `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
5. Restart the laptop and run Check for updates again.

### Fix 4: Verify your account has administrator rights

Updates that touch the servicing stack need elevation. If your account was silently demoted to Standard, or you are approving UAC prompts with a different credential, access-denied errors are the predictable result.

1. Go to Settings, then Accounts, then Your info, and confirm it says Administrator.
2. If it says Standard user, sign in with an admin account and promote yours under Settings, then Accounts, then Other users.
3. Re-run Windows Update from the administrator account to confirm the error is account-related.
4. On work laptops, ask IT before changing account types, since policy may forbid it.

### Fix 5: Temporarily disable third-party antivirus

Security suites are the number one external cause of this error. Disabling real-time protection for a single update attempt is a legitimate diagnostic step; leaving the laptop unprotected for days is not.

1. Open your antivirus settings and turn off real-time protection temporarily (usually 15-60 minutes).
2. Also disable any firewall or ransomware-shield component from the same suite.
3. Run Check for updates and let the install complete.
4. Immediately re-enable all protection, then restart and confirm the suite reports healthy.
5. If updates now succeed, check the vendor's support pages for an exclusion list for Windows Update folders.

### Fix 6: Perform a clean boot and retry the update

Background utilities — RGB controllers, fan tools, OEM updaters — can lock files the update engine needs. A clean boot starts Windows with only Microsoft services, which isolates the conflict cleanly.

1. Press Win + R, type `msconfig`, and open System Configuration.
2. On the Services tab, tick Hide all Microsoft services, then click Disable all.
3. On the Startup tab, click Open Task Manager and disable every startup item.
4. Restart, then run Windows Update and let it finish.
5. Re-enable your services and startup items afterward with the same tool.

### Fix 7: Install the update manually from the Microsoft Update Catalog

When the automatic engine keeps hitting access-denied walls, sidestepping it works. Downloading the standalone package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and installing it by hand bypasses the broken automatic pipeline entirely.

1. In Windows Update history, note the exact KB number of the failing update.
2. Search that KB number on the Microsoft Update Catalog site.
3. Download the package matching your architecture (x64 for most laptops).
4. Double-click the .msu file and let the standalone installer run.
5. Restart when prompted and verify the KB appears in update history.

## Closing

Error 0x80070005 looks intimidating but it is almost always a fixable permissions or services problem, and the sequence above resolves it on the vast majority of laptops without a reinstall. Work the list in order, test after each major step, and keep notes on which step worked — that record is gold if the error ever returns after a future update.
