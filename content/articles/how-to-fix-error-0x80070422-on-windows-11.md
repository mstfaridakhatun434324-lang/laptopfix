---
title: "How to Fix Error 0x80070422 on Windows 11"
slug: how-to-fix-error-0x80070422-on-windows-11
date: 2026-10-10
categories: ["windows-errors"]
tags: ["error-0x80070422", "windows-11", "windows-update"]
description: "Error 0x80070422 on Windows 11? Re-enable the disabled update services and stop it coming back."
thumbnail: "/images/thumbs/how-to-fix-error-0x80070422-on-windows-11.webp"
faqs:
  - q: "What does error 0x80070422 mean on Windows 11?"
    a: "It means a service Windows needs — usually Windows Update itself or BITS — is disabled and can't be started. Updates, the Microsoft Store, and sometimes Windows Security features fail with this code until the service is re-enabled."
  - q: "What disables the Windows Update service on Windows 11?"
    a: "Usually third-party 'debloater' or 'privacy' tools, update-blocker utilities, malware, or a misapplied group policy. Windows doesn't disable these services on its own."
  - q: "Should the Windows Update service be Automatic or Manual?"
    a: "Either works. Automatic starts it at boot; Manual lets Windows start it on demand when updates run. Both are fine — the only wrong setting is Disabled."
  - q: "It keeps getting disabled again after I fix it. Why?"
    a: "Something is actively re-disabling it: a scheduled task from a tweaker tool, a group policy, or malware. Check Task Scheduler, remove the offending tool, and run a full Defender scan."
---
# How to Fix Error 0x80070422 on Windows 11

**Error 0x80070422** on Windows 11 means exactly what it says: a required service is disabled and Windows can't start it. You'll see it in **Settings > Windows Update**, but it can also surface in the Microsoft Store or Windows Security when those features reach for the same disabled services.

The fix is quick — re-enable the services — but the important part is finding what disabled them so you're not repeating this monthly. Note that the same code can appear in the Microsoft Store or Windows Security when those features reach for the same disabled services; the fix is identical regardless of where you spotted it.

The same disabled-service problem can also break the Microsoft Store — see our [unexpected store exception guide](/articles/unexpected-store-exception-windows-11-fix/) if Store apps fail too.

## Why this happens

- **Disabled Windows Update service:** The direct cause in nearly every case.
- **Disabled BITS:** The Background Intelligent Transfer Service handles update downloads and is often disabled alongside.
- **Debloater and privacy scripts:** Third-party tools that "slim down" Windows routinely kill update services.
- **Update blockers:** Utilities designed to stop Windows updates do it by disabling these services.
- **Malware:** Disabling updates keeps security patches from removing the infection.
- **Group policy:** A misconfigured policy (or one pushed by old management software) forcing services off.

## How to fix it

Work through these in order. Fix 1 resolves it immediately in most cases.

### Fix 1: Re-enable the services in the Services console

The core fix takes under a minute.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Double-click **Windows Update**, set **Startup type** to **Automatic**, click **Start**, then **OK**.
3. Do the same for **Background Intelligent Transfer Service** — set it to **Automatic (Delayed Start)** and start it.
4. While you're here, open the **Recovery** tab for Windows Update and set all three failure actions to **Restart the Service**, so a future crash doesn't silently kill updates.
5. Go to **Settings > Windows Update** and check for updates to confirm the fix.
6. If the service shows as Disabled again after a reboot, don't just re-enable it a second time — something is actively fighting you, and Fix 5's cleanup is the real solution.

### Fix 2: Enable the supporting services

Windows Update needs its supporting cast; check them too.

1. In `services.msc`, verify these are not Disabled (Manual is the correct default for most):
   - **Cryptographic Services**
   - **DCOM Server Process Launcher**
   - **RPC Endpoint Mapper**
   - **Windows Installer**
2. Start any that aren't running.
3. Retry Windows Update. If 0x80070422 persists, a policy or malware is interfering — continue below.
4. As a sanity check, also confirm the **Windows Update Medic Service (WaaSMedicSvc)** exists and isn't disabled — it's Windows' self-healing service for the update stack, and some aggressive tools disable it too.

### Fix 3: Use the command line when the GUI is blocked

Greyed-out service options mean something is actively protecting the disabled state.

1. Open **Terminal (Admin)**.
2. Run:
   `sc config wuauserv start= demand`
   `sc config bits start= delayed-auto`
   (note the space after `start=` — it's required)
3. Then:
   `net start wuauserv`
   `net start bits`
4. If you get "access denied" even as admin, treat it as hostile interference and jump to Fix 5.

### Fix 4: Check Group Policy and the registry

Policies can force services off and override your GUI changes.

1. Press **Win + R**, type `gpedit.msc` (Pro/Enterprise), and check **Computer Configuration > Administrative Templates > Windows Components > Windows Update** for anything update-blocking set to Enabled — return it to **Not Configured** unless IT set it deliberately.
2. On Home editions, check the registry: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv` — the **Start** value should be `2` (Automatic) or `3` (Manual), never `4` (Disabled).
3. Run `gpupdate /force` in an admin Terminal and recheck.

### Fix 5: Scan for malware and remove tweaker tools

Something that disables updates on purpose needs removing, not just undoing.

1. Run a **Full scan** in **Windows Security > Virus & threat protection**, then a **Microsoft Defender Offline scan**.
2. Uninstall any "debloater," "privacy," "anti-telemetry," or update-blocker tools — they re-disable the services on every boot, usually via scheduled tasks.
3. Open **Task Scheduler** and delete tasks from those tools under **Task Scheduler Library**.
4. Re-enable the services (Fix 1) after cleanup and confirm they stay enabled across a reboot.
5. If Defender finds nothing but services still get disabled, check for lesser-known culprits: old enterprise management agents, "gaming optimizer" suites bundled with motherboards, and scripts in your Startup folder.

### Fix 6: Reset the update components

Corrupted cache and registrations can keep the error alive even with services running.

1. In admin Terminal:
   `net stop wuauserv`
   `net stop bits`
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `net start wuauserv`
   `net start bits`
2. Re-register the update DLLs:
   `regsvr32.exe /s wuapi.dll`
   `regsvr32.exe /s wuaueng.dll`
3. Check for updates again.
4. If the troubleshooter fixed service permissions but updates still fail with a different code, you've made progress — the 0x80070422 is gone and the new code points at the next layer to fix.

### Fix 7: Run the troubleshooter and lock in the fix

Final verification plus prevention.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run the **Windows Update** troubleshooter.
2. Restart and confirm updates install.
3. Going forward, pause updates the supported way (**Settings > Windows Update > Pause updates**) instead of using blocker tools — you get the control without breaking the servicing machinery. Microsoft documents safe update management on the [Windows support hub](https://support.microsoft.com/en-us/windows).
4. For other update errors that sometimes travel with this one, our [error 0x80070057 fix](/articles/error-code-0x80070057-fix/) covers the next most common update code.

## Closing

Error 0x80070422 is refreshingly honest — a disabled service, plain and simple. Turn Windows Update and BITS back on, verify the supporting services, then evict whatever turned them off. Do the second part properly and this is a once-ever fix, not a monthly chore — and your laptop stays protected by the security updates it was missing while the services were down.
