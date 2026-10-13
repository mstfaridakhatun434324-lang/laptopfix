---
title: "Windows Update Service Not Running on Windows 10: Restoring It"
slug: how-to-fix-windows-update-service-not-running-on-windows-10
date: 2026-09-13
categories: ["windows-update"]
tags: ["update service", "wuauserv", "windows 10", "service fix"]
description: "The Windows Update service won't start on Windows 10? Restore wuauserv with service repairs, dependency checks, and registry fixes."
thumbnail: "/images/thumbs/how-to-fix-windows-update-service-not-running-on-windows-10.webp"
faqs:
  - q: "What is the Windows Update service (wuauserv)?"
    a: "It is the background service that powers the entire update pipeline — checking for updates, downloading them, and coordinating installation. Without it running, Windows Update cannot do anything: the Settings page shows errors, downloads never start, and the troubleshooter reports the service as missing. Every update operation depends on this one service."
  - q: "Why does the service keep stopping on its own?"
    a: "The usual reasons: a dependency service (like BITS or RPC) is failing, the service's registry configuration is damaged, third-party software is killing it, or the service executable itself is corrupted. If it starts and then stops within seconds, check the Event Viewer under Windows Logs > System for the exact error — it usually names the cause."
  - q: "Is it safe to edit the registry to fix the service?"
    a: "Yes, if you follow the steps exactly and back up the key first. The fixes here only touch the wuauserv service configuration, which is a well-documented area. Export the key before changing anything (right-click > Export), so you can restore it if something goes wrong. Do not wander into unrelated registry areas."
  - q: "Could malware be stopping the update service?"
    a: "Possibly — some malware deliberately disables Windows Update to prevent security patches from removing it. If the service will not stay running and you also see other security features disabled, run a full scan with Windows Security and consider an offline scan from Windows Security > Virus & threat protection > Scan options > Microsoft Defender Offline scan."
---

When the Windows Update service refuses to run on Windows 10, everything update-related breaks at once: Settings shows error messages, the troubleshooter complains, and no update will ever download. The service — wuauserv — is the engine room of the whole pipeline, and this guide is about getting it running again and keeping it running.

Service failures fall into a few clear patterns: the service is disabled, its dependencies are broken, its registry configuration is damaged, or something is actively killing it. The sequence below diagnoses which pattern you have before applying the fix, so you are not blindly resetting things. If you are on Windows 11 instead, the [Windows 11 version of this guide](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/) covers the same repairs with 11-specific notes.

## Why this happens

- **Service set to Disabled:** The startup type was changed — by software, a tweak tool, or malware.
- **Broken dependencies:** BITS, RPC, or the DCOM launcher failing takes wuauserv down with them.
- **Corrupted service registry keys:** The service's configuration under HKEY_LOCAL_MACHINE\\SYSTEM is damaged.
- **Corrupted service files:** The wuauserv DLL or its host process files are damaged.
- **Third-party interference:** "Debloat" tools and some optimizers disable the service deliberately.
- **Malware:** Malicious software stopping updates to protect itself.
- **Failed update state:** A crashed update left the service in an inconsistent state.
- **Permission problems:** The service account lost its required logon permissions.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Start the service manually and set it to Automatic

The simplest case: something flipped the switch, and flipping it back is enough.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find **Windows Update** in the list and double-click it.
3. Set **Startup type** to **Automatic** (not Automatic Delayed Start for now).
4. Click **Start** — watch for an immediate error message, which is diagnostic gold.
5. If it starts cleanly, check for updates to confirm the pipeline works.

### Fix 2: Check and repair the dependencies

wuauserv depends on other services; if they are down, it cannot start. Microsoft documents service dependencies on the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. In the Windows Update service properties, open the **Dependencies** tab.
2. Note the listed services — typically Remote Procedure Call (RPC) and DCOM Server Process Launcher.
3. Verify each dependency is running in services.msc; start any that are stopped.
4. Also confirm **Background Intelligent Transfer Service** is running — the update engine needs it.
5. Try starting the Windows Update service again.

### Fix 3: Reset the service configuration via command line

When the GUI will not cooperate, the command line resets the service cleanly.

1. Open Command Prompt as administrator.
2. Run `sc config wuauserv start= auto` (note the space after the equals sign — it is required).
3. Run `sc config bits start= delayed-auto`.
4. Run `net start wuauserv` and watch the result.
5. If it starts, run `net start bits` too, then check for updates.

### Fix 4: Repair the service registry keys

Damaged registry configuration is a common cause of services that will not start.

1. Press Win + R, type `regedit`, and press Enter.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv`.
3. Right-click the wuauserv key and choose **Export** to back it up.
4. Check that the **Start** value is `2` (Automatic) — change it if it is `4` (Disabled).
5. Check that **ImagePath** points to a valid svchost invocation; if the key looks truncated or garbage, restore from a working machine's export or continue to Fix 5.

### Fix 5: Re-register the update DLLs

Corrupted service components can be re-registered without reinstalling Windows.

1. Open an elevated Command Prompt.
2. Run these commands one at a time:
   ```
   regsvr32 wuapi.dll
   regsvr32 wuaueng.dll
   regsvr32 wups.dll
   regsvr32 wuwebv.dll
   ```
3. Confirm each registration succeeds.
4. Restart the laptop.
5. Start the Windows Update service and test.

### Fix 6: Run DISM and SFC

System file damage affecting the service host gets repaired here.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `sfc /scannow` after DISM completes.
4. Restart the laptop.
5. Attempt to start the service again.

### Fix 7: Scan for malware and undo debloat damage

If the service was deliberately disabled, find out by what. The [troubleshooter repair path](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) is worth running afterward to confirm the whole pipeline is healthy.

1. Run a full scan with Windows Security.
2. Run a Microsoft Defender Offline scan for persistent threats.
3. If you ever ran a "debloat" or "privacy" tool, check its settings — many disable wuauserv — and re-enable the service through it.
4. Check Task Scheduler for third-party tasks that stop the service on a schedule.
5. Once the cause is removed, set the service to Automatic and verify it survives a reboot.

### Fix 8: Reset the Windows Update policies

Stale or corrupt update policies can prevent the service from starting correctly.

1. Open an elevated Command Prompt.
2. Run `rd /s /q "%windir%\System32\GroupPolicy"` to clear local policy storage (this resets all local policies, not just update ones).
3. Run `rd /s /q "%windir%\System32\GroupPolicyUsers"` as well.
4. Run `gpupdate /force` to rebuild default policies.
5. Restart and try starting the Windows Update service — policy-level blocks are now gone.

## Closing

A dead Windows Update service on Windows 10 is a plumbing problem: the pipes are the service configuration, its dependencies, and its files, and the fixes above work through each in turn. Most cases resolve at Fix 1 or Fix 2 — a flipped startup type or a stopped dependency. The deeper repairs exist for the stubborn minority, and they work because they address the actual mechanism rather than the symptom. Once wuauserv is running and set to Automatic, the rest of the update pipeline comes back to life on its own.
