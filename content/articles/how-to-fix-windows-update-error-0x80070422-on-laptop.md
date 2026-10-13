---
title: "How to Fix Windows Update Error 0x80070422 on a Laptop"
slug: "how-to-fix-windows-update-error-0x80070422-on-laptop"
date: "2026-10-12"
categories: ["windows-update"]
tags: ["0x80070422", "service-disabled", "windows-update", "windows-11"]
description: "Error 0x80070422 means a required Windows Update service is disabled. Here's how to re-enable it and repair whatever turned it off."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070422-on-laptop.webp"
faqs:
  - q: "What service does error 0x80070422 refer to?"
    a: "It means 'the service cannot be started because it is disabled or has no enabled devices associated with it.' For Windows Update, it almost always refers to the Windows Update service itself, wuauserv, though the Background Intelligent Transfer Service can trigger it too. The fix is to set the service startup type back to Manual or Automatic and start it."
  - q: "What disables the Windows Update service without my knowledge?"
    a: "The usual culprits are third-party 'debloat' or privacy tools, aggressive optimizer apps, some enterprise management software left over from a work setup, and occasionally malware. Windows itself does not disable the service on its own. If you find it disabled and did not do it yourself, audit recently installed utilities — one of them is the likely offender."
  - q: "Is 0x80070422 the same as the service not running?"
    a: "Closely related but not identical. A service can be stopped yet still startable, which produces different errors. Code 0x80070422 specifically means the service is disabled, so Windows refuses to even attempt starting it. The distinction matters because the fix must change the startup type, not just click Start — Start alone fails on a disabled service."
  - q: "Will this error come back after I fix it?"
    a: "It returns if whatever disabled the service is still installed and active. Debloat scripts often reapply their changes on a schedule, and some 'privacy' tools re-disable update services after every reboot. After fixing the service, identify and remove or reconfigure the offending tool; otherwise you will be repeating this repair regularly."
---

Error 0x80070422 is refreshingly literal: Windows tried to start a service that something had disabled, and refused. In the update context, that service is almost always the Windows Update service itself, and the "something" is usually a debloat script, an optimizer, or a privacy tool that decided updates were optional. The code even tells you the fix — re-enable the service.

That said, simply flipping the switch without addressing the cause invites a repeat performance. The steps below fix the service, repair any damage underneath, and help you find the tool that turned it off so it stays on.

Few error codes are as literal as 0x80070422: Windows tried to start a service, the service was disabled, and Windows is telling you exactly that. In the update context the disabled service is wuauserv, and the mystery is not what broke but who disabled it — because Windows does not disable its own update service. The answer, in the large majority of cases, is software the user installed: debloat scripts promising a ‘clean’ Windows, privacy tools that treat updates as telemetry, or optimizers chasing benchmark scores. The fix has two halves of equal importance: re-enable the service, and evict whatever turned it off.

## Why this happens

- **Debloat and privacy tools:** Scripts that "remove bloat" routinely disable the update service as part of their routine.
- **Optimizer applications:** Third-party tuners sometimes disable update services in the name of performance.
- **Leftover enterprise management:** Machines previously managed by a workplace can carry policies that disable the service.
- **Malware:** Some malware disables updates to prevent its own removal — worth a scan if nothing else explains it.
- **Corrupted service registration:** Damage to the service's registry entries can present as a disabled state.
- **Failed updates to the servicing stack:** A bad servicing stack update can leave service configuration inconsistent.
- **Manual misconfiguration:** Well-meaning tutorials sometimes advise disabling the service to "stop forced updates."
- **Third-party update blockers:** Tools designed to pause updates indefinitely do it by disabling the service.

## How to fix it

Work through these in order — diagnose first, then act.

Test your fix across a reboot, not just in the current session. Some offending tools re-disable the service at startup or on a schedule, so a service that looks fixed now may be disabled again tomorrow morning. A reboot test is the only way to know the repair actually held.

### Fix 1: Re-enable the Windows Update service

The core fix — change the startup type, then start the service.

1. Press Win + R, type `services.msc`, and press Enter.
2. Double-click the Windows Update service.
3. Change Startup type from Disabled to Manual.
4. Click Start, then Apply and OK.
5. Confirm the status shows Running, then test Windows Update.

This is the same core procedure the [Windows Update service not running repair](/articles/how-to-fix-windows-update-service-not-running-on-windows-11/) is built around — worth reading if the service starts now but quietly stops again later.

### Fix 2: Check the BITS service too

The transfer service is the other common 0x80070422 trigger.

1. In services.msc, locate Background Intelligent Transfer Service.
2. Set its Startup type to Manual if it is disabled.
3. Start the service and confirm it stays running.
4. Retry Windows Update.

### Fix 3: Run the Windows Update troubleshooter

The troubleshooter detects and repairs disabled update services automatically.

1. Open Settings, System, Troubleshoot, Other troubleshooters.
2. Run the Windows Update troubleshooter.
3. Apply any fixes it recommends and restart.
4. Verify the service is still running after the reboot.

### Fix 4: Find what disabled the service

Fixing the symptom without removing the cause guarantees a repeat.

1. Review recently installed programs in Settings, Apps, Installed apps for debloat, optimizer, or "privacy" tools.
2. Uninstall anything whose purpose is disabling Windows features or updates.
3. Check Task Scheduler for scripts that run at startup or on a schedule modifying services.
4. After removal, re-enable the service per Fix 1 and monitor it across a reboot.

### Fix 5: Scan for malware

If nothing you installed explains the disabled service, check for malicious causes.

1. Open Windows Security and run a full scan, not just a quick scan.
2. Consider a second-opinion scan with the Microsoft Safety Scanner.
3. Remove any threats found and restart.
4. Re-enable the update service and confirm it stays enabled.

### Fix 6: Reset the update components

Repair any corruption in the service's data stores while you are at it.

1. In an admin Command Prompt, stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services and reboot.
4. Confirm the Windows Update service starts normally.
5. Our companion guide on [the update service not running](/articles/how-to-fix-windows-update-service-not-running-reddit/) covers additional service-repair angles.

### Fix 7: Check Group Policy

A lingering policy can force the service back to disabled.

1. Press Win + R, type `gpedit.msc`, and press Enter. Skip if you are on Home edition.
2. Navigate to Computer Configuration, Administrative Templates, Windows Components, Windows Update.
3. Set any update-disabling policies to Not Configured.
4. Run `gpupdate /force`, restart, and verify the service.

### Fix 8: Repair system files

If the service configuration is damaged at the system level, repair the foundation.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an admin Command Prompt.
2. Follow with `sfc /scannow`.
3. Restart and check the service status.
4. Test a full Windows Update cycle to confirm everything works end to end.

There is a broader lesson in this error about the ‘Windows debloating’ ecosystem. Many of those scripts and tools disable updates as a side effect of pursuing marginal performance gains, trading real security patches for a slightly snappier feel that most users cannot even perceive. If you ran such a tool in the past, consider whether its benefits outweigh a machine that cannot patch itself — for most people, they do not. A stock Windows 11 with sensible settings updates reliably and performs well; the debloat is usually the disease it claims to cure. For the general case of an update service that will not stay running, our companion guide on [the Windows Update service not running](/articles/how-to-fix-windows-update-service-not-running-reddit/) covers the corruption and dependency angles.

## Closing

Error 0x80070422 is Windows telling you plainly that updates were switched off at the service level. Switch them back on, evict whatever switched them off, and the error disappears — usually permanently, provided the debloat tool does not get a second chance.
