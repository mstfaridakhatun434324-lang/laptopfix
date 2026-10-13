---
title: "How to Fix ‘Windows Update Service Not Running’ on an ASUS Laptop"
slug: how-to-fix-windows-update-service-not-running-on-asus-laptop
date: 2026-09-11
categories: ["windows-update"]
tags: ["windows update service not running", "asus windows update error", "0x80070422 fix", "wuauserv not starting"]
description: "Windows Update service not running on your ASUS laptop? Start wuauserv, repair dependencies, check MyASUS conflicts, and reset update components."
thumbnail: "/images/thumbs/how-to-fix-windows-update-service-not-running-on-asus-laptop.webp"
faqs:
  - q: "Is it safe to leave the Windows Update service disabled?"
    a: "No. A disabled update service means no security patches, which leaves known vulnerabilities open. Some Asus utilities and Microsoft Store apps also misbehave when updates are blocked. Keep the service on Automatic and use pause options if you need a temporary break from updates."
  - q: "Can MyASUS replace Windows Update?"
    a: "No — MyASUS handles Asus drivers and utilities, while Windows Update delivers OS security and quality updates. They are complementary. Letting MyASUS manage drivers while Windows Update handles the OS is the setup Asus intends, and disabling either one causes problems."
  - q: "What are the correct default settings for the update services?"
    a: "Windows Update: Manual (trigger start) is the Windows 11 default, though Automatic also works. Background Intelligent Transfer Service: Manual. Cryptographic Services: Automatic. Remote Procedure Call and DCOM Server Process Launcher: Automatic. If a tuner changed these, restoring the defaults usually fixes the issue."
  - q: "Do I need the Group Policy fix on Windows 11 Home?"
    a: "No. The Local Group Policy Editor (gpedit.msc) does not exist on Windows 11 Home, so policy-based blocking cannot be the cause there. Home users should focus on the service settings, debloat tools, and component reset steps instead. Everything in this guide except the policy step applies fully to Home."
---

When Windows Update reports that its service is not running, the update engine is effectively switched off on your Asus laptop. The service in question is wuauserv, and it depends on several others — Remote Procedure Call, DCOM Server Process Launcher, and RPC Endpoint Mapper — so a failure in any dependency produces the same symptom. [the update service stopping after an update](/articles/how-to-fix-windows-update-service-not-running-after-windows-11-update/)

On Asus machines this often follows a botched update or a MyASUS driver install that left the service stack in a bad state. The good news: the service itself is rarely truly broken. It is usually stopped, set to the wrong startup type, or blocked by a dependency, and all three are quick to check.

## Why this happens

- **Third-party tuner or debloat tool.** Privacy and debloat utilities often disable Windows Update services deliberately. These tools usually log what they changed; check their restore or undo options first.
- **MyASUS conflict.** Asus's updater can leave the service stack in an inconsistent state after a failed driver push. Close MyASUS and retest to isolate whether Asus's updater is involved.
- **Corrupted service registration.** The service's registry entries under HKLM\SYSTEM\CurrentControlSet\Services\wuauserv are damaged. The relevant keys live under HKLM\SYSTEM\CurrentControlSet\Services\wuauserv.
- **Group Policy restriction.** On Pro editions, a policy under Windows Update settings can disable the service. Run rsop.msc to see which policies are actually applying to the machine.
- **BITS also stopped.** The Background Intelligent Transfer Service works alongside wuauserv; if both are down, updates are fully dead. Both services must be healthy for the full update pipeline to function.
- **Malware interference.** Some malware disables update services to avoid being removed by security updates. A service that re-disables itself within minutes is behaving like malware victim behavior.
- **Corrupted system files.** Damage to the servicing stack binaries prevents the service from initializing. The servicing binaries live in System32; compare hashes only if you suspect tampering.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check MyASUS settings

MyASUS manages drivers and sometimes update scheduling on Asus laptops; a misconfiguration can fight Windows Update. After any change here, always test with an actual update check rather than assuming the Services console status tells the whole story.

1. Open MyASUS and look for update or automatic-update settings.
2. Make sure MyASUS is not set to block or fully take over Windows updates.
3. Install any pending MyASUS updates, then restart.
4. Test Windows Update again with MyASUS closed.
5. If MyASUS itself is broken, reinstall it from Asus support.
6. Check Event Viewer > Windows Logs > System for new Service Control Manager errors mentioning wuauserv.

### Fix 2: Run the Windows Update troubleshooter

The built-in troubleshooter knows how to restart and re-register the update services automatically. The System event log (Event Viewer > Windows Logs > System) records service start failures with event IDs that name the failing dependency explicitly.

1. Go to Settings > System > Troubleshoot > Other troubleshooters.
2. Run the Windows Update troubleshooter.
3. Apply every fix it recommends, even if they sound unrelated.
4. Restart when it finishes and test for updates.
5. If the troubleshooter itself will not run, skip to the manual reset below.
6. If the service will not start, note the exact error code from net start wuauserv for the next diagnostic step.

### Fix 3: Reset the Windows Update components manually

When the service registration is damaged, a full component reset rebuilds the working state. [the Windows Update troubleshooter failing to run](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) On Asus laptops, check MyASUS after re-enabling the service, since its own update scheduler can conflict if both try to manage updates aggressively.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv & net stop bits & net stop cryptsvc & net stop msiserver.
3. Rename C:\Windows\SoftwareDistribution to SoftwareDistribution.old and C:\Windows\System32\catroot2 to catroot2.old.
4. Re-register the update DLLs: regsvr32 wuapi.dll, wuaueng.dll, wups.dll (confirm each prompt).
5. Restart the services with net start and test Windows Update.
6. Confirm BITS is also running, since a dead BITS queue stalls downloads even with wuauserv healthy.

### Fix 4: Check Group Policy (Pro editions)

A policy can force the update service off. This applies to Windows 11 Pro, not Home. A quick way to test dependencies is to try starting the service from an elevated prompt with net start wuauserv and read the exact error message it returns.

1. Press Win + R, type gpedit.msc, and press Enter.
2. Go to Computer Configuration > Administrative Templates > Windows Components > Windows Update.
3. Look for 'Configure Automatic Updates' and any policy set to Disabled that should not be.
4. Set questionable policies to 'Not Configured'.
5. Run gpupdate /force in Command Prompt, restart, and retest.
6. Test that MyASUS still opens and functions, confirming you did not break Asus's utilities.

### Fix 5: Scan for malware

Malware that disables update services is a real category. If the service keeps turning itself off, suspect infection. If you dual-boot or use third-party boot managers, verify the correct Windows installation's services are the ones you are editing.

1. Run a full scan with Windows Security (Virus & threat protection > Scan options > Full scan).
2. Also run a second-opinion scan with the free Malwarebytes scanner.
3. Remove anything found and restart.
4. Re-enable the Windows Update service afterward.
5. If the service disables itself again, consider a clean Windows reinstall.
6. Run Windows Update twice in a row; the second pass catches updates that only appear after the first installs.

### Fix 6: Repair system files with SFC and DISM

Corrupted servicing binaries stop the service from initializing even when everything is configured correctly. Corporate or school laptops may have the service managed by an MDM policy, in which case local changes get reverted and the IT admin is the right contact.

1. Open Command Prompt as administrator and run: sfc /scannow.
2. Then run: DISM /Online /Cleanup-Image /RestoreHealth.
3. Restart and check whether the Windows Update service now starts.
4. If DISM reports it could not repair everything, note the CBS log path it gives.
5. Persistent DISM failures mean deep store damage — an in-place upgrade is the next step.
6. Document which change fixed it, so you can reverse course quickly if a tuner re-applies its settings later.

### Fix 7: Do an in-place upgrade repair

When nothing else restores the service, an in-place upgrade reinstalls Windows while keeping files and apps, rebuilding the entire servicing stack. Once the service runs reliably for a week, delete any SoftwareDistribution.old folders left over from the repairs to reclaim the disk space.

1. Back up important files first.
2. Download the Windows 11 media creation tool from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Run setup.exe from the created media and choose 'Keep personal files and apps'.
4. Let the repair install complete — it takes 30 to 90 minutes.
5. Windows Update services are rebuilt fresh by this process.
6. Leave the Services console open on the Windows Update entry while you test, watching for it stopping unexpectedly.

## Closing

Nine times out of ten this is a configuration problem, not corruption: a disabled service, a stopped dependency, or a debloat tool's handiwork. The manual component reset at the end covers the tenth case. Keep the services at their defaults going forward, and see [general Windows 11 update failures](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-windows-11/) for the next layer of update troubleshooting.
