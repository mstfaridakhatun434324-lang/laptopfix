---
title: "How to Fix Error 0x80070422 on Windows 10"
slug: how-to-fix-error-0x80070422-on-windows-10
date: 2026-10-01
categories: ["windows-errors"]
tags: ["error-0x80070422", "windows-10", "windows-update"]
description: "Error 0x80070422 stopping Windows 10 updates? Restart the disabled update services with these proven steps."
thumbnail: "/images/thumbs/how-to-fix-error-0x80070422-on-windows-10.webp"
faqs:
  - q: "What does error 0x80070422 mean?"
    a: "It means 'the service cannot be started' — Windows Update tried to use a required service (usually the Windows Update service itself or BITS) and found it disabled. Something — a tweaker tool, malware, or a bad script — turned the service off."
  - q: "Why is my Windows Update service disabled?"
    a: "Common culprits: 'privacy' or 'debloating' scripts that disable Windows services, third-party update blockers, malware, or a corrupted service configuration after a bad shutdown. It rarely disables itself."
  - q: "Is it safe to re-enable the Windows Update service?"
    a: "Yes — it's a core Windows service meant to run. Set it to Automatic (or Manual, which lets Windows start it on demand). Only leave it disabled if you have a specific, informed reason and an alternative patching strategy."
  - q: "The service keeps disabling itself. What now?"
    a: "Something is actively turning it off — usually a scheduled task from a tweaker tool, a group policy, or malware. Check Task Scheduler and Group Policy, remove the offending tool, and run a full Windows Security scan."
---
# How to Fix Error 0x80070422 on Windows 10

**Error 0x80070422** has a refreshingly literal meaning: Windows Update tried to start a service it needs, and the service was disabled. Updates can't run without their services, so everything halts with this code. The good news is the fix is equally literal — turn the services back on.

You'll usually see it in **Settings > Update & Security > Windows Update**, but the same code can pop up in the Microsoft Store or Windows Security when those features try to use the disabled services too. The fix is the same regardless of where you spotted it.

The catch is figuring out *what* turned them off, so it doesn't happen again. Work through the fixes below: first restore the services, then find the culprit. The same disabled-service problem can also break the Microsoft Store — see our [unexpected store exception guide](/articles/unexpected-store-exception-windows-11-fix/) if Store apps fail too.

## Why this happens

- **Disabled Windows Update service:** The direct cause — the wuauserv service is set to Disabled.
- **Disabled BITS:** The Background Intelligent Transfer Service, which downloads updates, is also off.
- **"Debloating" or privacy scripts:** Third-party tools that promise to slim down Windows routinely disable update services.
- **Update-blocker utilities:** Tools designed to stop Windows updates do it by disabling these exact services.
- **Malware:** Some malware disables updates to keep security patches from removing it.
- **Corrupted service configuration:** A bad shutdown or disk error can corrupt the service's registry settings.

## How to fix it

Work through these in order. Fix 1 solves it immediately in most cases.

### Fix 1: Re-enable the Windows Update service

This is the core fix — everything else is follow-up.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **Windows Update** in the list and double-click it.
3. Set **Startup type** to **Automatic** (or **Manual** if you prefer Windows to start it on demand).
4. Click **Start** to start it now, then **OK**.
5. Do the same for **Background Intelligent Transfer Service** — set it to **Automatic (Delayed Start)** and start it.
6. Open **Settings > Update & Security > Windows Update** and check for updates.
7. If the service was disabled, check **Recovery** tab settings while you're in its properties — set all three failure actions to **Restart the Service** so a future crash doesn't leave updates silently dead.

### Fix 2: Enable the dependent services

Windows Update relies on a small constellation of services; if any are disabled, 0x80070422 returns.

1. In `services.msc`, check each of these and set them to **Manual** (or Automatic) if disabled:
   - **Cryptographic Services**
   - **DCOM Server Process Launcher**
   - **RPC Endpoint Mapper**
   - **Windows Installer**
2. Start any that aren't running.
3. Don't set them all to Automatic — Manual is the correct default for most; Windows starts them when needed.
4. Retry Windows Update.

### Fix 3: Fix it from the command line

If the Services GUI won't cooperate (greyed-out options usually mean policy or malware interference), use the command line.

1. Open an **admin Command Prompt**.
2. Run:
   `sc config wuauserv start= demand`
   `sc config bits start= delayed-auto`
   `sc config cryptsvc start= demand`
   Note the space after `start=` — it's required.
3. Then start them:
   `net start wuauserv`
   `net start bits`
4. If `sc config` reports access denied even as admin, something (policy or malware) is actively protecting the disabled state — continue to Fix 5.

### Fix 4: Check Group Policy (Pro editions)

A policy may be forcing the services off, in which case the Services GUI changes won't stick.

1. Press **Win + R**, type `gpedit.msc`, and press **Enter**.
2. Navigate to **Computer Configuration > Administrative Templates > Windows Components > Windows Update**.
3. Look for policies like **Configure Automatic Updates** or **Turn off auto-restart** — set anything update-blocking to **Not Configured** unless your IT department set it deliberately.
4. Also check **Computer Configuration > Windows Settings > Security Settings > System Services** for forced service states.
5. Run `gpupdate /force` in an admin Command Prompt and recheck the services.

### Fix 5: Scan for malware

Malware that disables updates is protecting itself — remove it before it does more.

1. Open **Windows Security > Virus & threat protection** and run a **Full scan**.
2. Then run **Microsoft Defender Offline scan** (under **Scan options**) — it reboots into a clean environment where stubborn malware can't hide.
3. Remove everything found, restart, and re-enable the services from Fix 1.
4. If you previously ran a "privacy" or "anti-telemetry" tool, uninstall it — many disable update services as a side effect and will re-disable them on every boot via scheduled tasks. Check **Task Scheduler** for suspicious entries.

### Fix 6: Repair the service registration

If the service exists but is corrupted, re-register its components.

1. In an admin Command Prompt, run:
   `regsvr32.exe /s wuapi.dll`
   `regsvr32.exe /s wuaueng.dll`
   `regsvr32.exe /s wups.dll`
   `regsvr32.exe /s wups2.dll`
2. Then reset the update cache as well:
   `net stop wuauserv`
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `net start wuauserv`
3. Check for updates again.
4. If re-registration fixed it, the corruption likely came from a bad shutdown or disk error — consider running `chkdsk C: /f` at your next restart to make sure the disk itself is healthy.

### Fix 7: Reset Windows Update via the troubleshooter

As a final cleanup, let the automated tool verify everything.

1. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply its fixes.
3. Restart once more and confirm updates download and install.
4. To prevent recurrence, avoid "debloater" scripts and update blockers — pause updates properly instead via **Settings > Update & Security > Windows Update > Pause updates**. Microsoft documents safe update management on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Error 0x80070422 is Windows telling you exactly what's wrong: a service it needs is disabled. Re-enable Windows Update and BITS, check the supporting services, and then hunt down whatever disabled them — a tweaker tool, a policy, or malware — so the fix sticks. Ten minutes of service management now saves you from missing the security updates that actually matter, and from chasing this same error again next month. For update errors that survive the service fix, our [error 0x80070057 guide](/articles/error-code-0x80070057-fix/) covers the next most common code.
