---
title: "Fix Windows Update Error 0x80070422 on Windows 10: Service Won't Start"
slug: how-to-fix-windows-update-error-0x80070422-on-windows-10
date: 2026-10-13
categories: ["windows-update"]
tags: ["windows 10", "windows update", "error 0x80070422", "update service", "services"]
description: "Error 0x80070422 on Windows 10 means the update service can't start. Re-enable it, fix dependencies, and remove whatever turned it off."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070422-on-windows-10.webp"
faqs:
  - q: "What does 0x80070422 mean on Windows 10?"
    a: "It means a required service cannot start — almost always the Windows Update service itself or one of its dependencies like BITS or Cryptographic Services. The service is typically disabled by a third-party tool, a group policy, or manual changes, not by Windows itself."
  - q: "How is this different from other Windows Update errors?"
    a: "Most update errors are about corrupted files or bad downloads. This one is about the machinery: the service that performs updates will not run at all. That makes it more straightforward to diagnose — you work in services.msc, not in the update cache — though you should still check for tools that keep re-disabling it."
  - q: "Can I just set the service to Automatic and be done?"
    a: "Often, yes — that is Fix 1 and it resolves many cases immediately. But if an update-blocker tool, scheduled task, or group policy is re-disabling it, the error returns after reboot. The lasting fix includes finding and removing the cause."
  - q: "Does 0x80070422 put my laptop at risk?"
    a: "Indirectly, yes. While the service is disabled you receive no security updates, leaving known vulnerabilities unpatched. Re-enabling updates promptly matters more here than with most update errors — this one blocks all patching entirely, not just a single update, so every week delayed increases exposure."
---

On Windows 10, error 0x80070422 appears in Windows Update with the message that the service cannot be started, and everything update-related stops dead: no checking, no downloading, no installing. Unlike file-corruption errors that let some updates through, a dead update service blocks all of them — which makes this error both urgent and, fortunately, quite fixable.

Windows 10 is the operating system where third-party "tweaking" tools have done the most damage to update services. Years of debloating scripts, update disablers, and privacy tools have left countless Windows 10 laptops with deliberately crippled update machinery. The repair is a services-focused sequence: re-enable, verify dependencies, remove the culprit, and repair any registration damage. Navigate it through Windows 10's tools below.

## Why this happens

- **Windows Update service disabled:** Startup type set to Disabled by a tool, policy, or manual change.
- **Legacy update-blocker tools:** Windows 10-era utilities that kill updates by breaking services remain installed and active.
- **Debloating scripts:** "Remove Windows bloat" scripts commonly disable wuauserv, BITS, and related services.
- **Group Policy from managed environments:** Ex-work or ex-school laptops often retain policies that disable update services.
- **Corrupted service registration:** Damaged registry entries for the service prevent the Service Control Manager from starting it.
- **Dependency failures:** BITS, Cryptographic Services, DCOM, or RPC failing to start takes the update service down too.
- **Altered service logon:** Logon account changed from Local System prevents startup.
- **Malware suppressing updates:** Malicious software disabling updates to avoid removal is a real, documented behavior.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Re-enable the Windows Update service

The immediate fix, done in the Services console.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Update**, double-click it, set **Startup type** to **Automatic**.
3. Click **Start**, then OK.
4. Open **Settings > Update & Security > Windows Update** and click **Check for updates**.

### Fix 2: Verify dependency services

Check the services the update service relies on.

1. In `services.msc`, ensure these are running with correct startup types: **Background Intelligent Transfer Service** (Manual), **Cryptographic Services** (Automatic), **DCOM Server Process Launcher** (Automatic), **RPC Endpoint Mapper** (Automatic).
2. Start any stopped ones and correct their startup types.
3. Check the **Dependencies** tab of the Windows Update service to confirm nothing else is listed as missing.
4. Retry the update check.

### Fix 3: Confirm the Local System logon

Services with changed logon credentials fail silently.

1. Double-click **Windows Update** in `services.msc` and open the **Log On** tab.
2. Verify **Local System account** is selected.
3. If it was changed to a user account, switch it back, click Apply, and start the service.
4. Repeat the check for BITS.

### Fix 4: Hunt down and remove the disabling tool

Windows 10 laptops accumulate update killers. Remove them or the error recurs.

1. Open **Control Panel > Programs > Programs and Features** and look for update blockers, "Windows 10 update disablers," debloaters, and aggressive privacy tools. Uninstall them.
2. Open **Task Scheduler** and look for tasks that stop or disable update services — disable or delete them.
3. If the laptop was ever workplace-managed, check **Settings > Accounts > Access work or school** and disconnect old enrollments.
4. Re-enable the services and reboot to confirm they stay running — the same persistence check recommended in the [Windows 11 version of this fix](/articles/how-to-fix-windows-update-error-0x80070422-on-windows-11/).

### Fix 5: Re-register the Windows Update DLLs

Repair corrupted service registrations from an elevated command prompt.

1. Open **Command Prompt (Admin)** via right-click on Start.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run: `regsvr32 /s wuapi.dll`, `regsvr32 /s wuaueng.dll`, `regsvr32 /s wups.dll`, `regsvr32 /s wups2.dll`, `regsvr32 /s wuwebv.dll`.
4. Run `net start wuauserv`, `net start bits`, `net start cryptsvc`, then check for updates.

### Fix 6: Run a full malware scan

Unexplained disabled update services warrant suspicion.

1. Open **Windows Security > Virus & threat protection** and run a **Full scan**.
2. Also run the **Microsoft Defender Offline scan** from Scan options for rootkit-level threats.
3. Clean anything found, restart, re-enable services, and verify updates flow.

### Fix 7: Reset update components and repair system files

The final comprehensive repair for stubborn cases.

1. In **Command Prompt (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`.
2. Stop the update services, rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`, then restart the services. These same steps, expanded with a service-by-service explanation, are in our [Windows 10 update component reset guide](/articles/how-to-reset-windows-update-components-on-windows-10/).
3. Reboot and check for updates. If services still refuse to start after all this, an in-place upgrade repair install (keeping files and apps) rebuilds the service registrations wholesale — download media from the official [Microsoft software download pages](https://www.microsoft.com/en-us/software-download/windows11) and choose the Windows 10 option.

Windows 10 deserves special mention here because it lived through the golden age of update-blocking utilities. Tools with names promising to stop Windows 10 updates or debloat your system were downloaded millions of times, and their service-disabling changes persist indefinitely — through feature updates, through antivirus scans, through everything except deliberate reversal. If your Windows 10 laptop has been around since 2018 or earlier, assume something in its past touched these services and audit accordingly: check installed programs, scheduled tasks, and the registry policies under the WindowsUpdate policy key. The Windows 11 version of this repair covers the same ground with Windows 11's tools in our [Windows 11 0x80070422 guide](/articles/how-to-fix-windows-update-error-0x80070422-on-windows-11/). Once the disabling agent is gone and the services hold their configuration across reboots, updates resume their normal monthly rhythm. Verify with two consecutive reboots before declaring victory — some scheduled tasks only re-disable services on the second boot.

## Closing

On Windows 10, 0x80070422 is overwhelmingly a story about something disabling the update service — usually a tool the user installed years ago and forgot. Re-enable the service, verify its dependencies, and remove the tool that broke it, and updates resume. Treat any recurrence as a signal that the disabling agent is still present, and hunt it down rather than just restarting the service again.
