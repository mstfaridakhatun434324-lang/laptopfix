---
title: "How to Temporarily Disable Windows Defender on Windows 11"
slug: how-to-disable-windows-defender-temporarily-on-windows-11
date: 2026-09-27
categories: ["performance"]
tags: ["windows defender", "disable defender", "real-time protection", "msmpeng", "troubleshooting"]
description: "Need to temporarily disable Windows Defender on Windows 11? Safe methods for real-time protection pauses, installs, and diagnostics."
thumbnail: "/images/thumbs/how-to-disable-windows-defender-temporarily-on-windows-11.webp"
faqs:
  - q: "How do I temporarily turn off Windows Defender real-time protection?"
    a: "Open Windows Security > Virus & threat protection > Manage settings, and toggle Real-time protection off. Windows shows a warning and automatically re-enables it after a short period (typically on next restart or within hours) — this is by design. This method is intended for brief tasks like installing trusted software that Defender flags, and it's the only Microsoft-supported way to pause protection on Windows 11 Home."
  - q: "Why does Windows Defender turn itself back on?"
    a: "Tamper protection and the built-in health monitoring deliberately re-enable real-time protection — Microsoft designed Defender to be resilient against both malware and users accidentally leaving themselves unprotected. Any 'permanent disable' tutorial is fighting this design, and on current Windows 11 builds most such methods are reverted within hours or by the next update. If you need Defender off longer, the supported path is installing a third-party antivirus that registers properly."
  - q: "Is it safe to disable Defender to install software?"
    a: "For brief, deliberate installs of software you trust — yes, with precautions: download only from the vendor's official site, disconnect from the network if the install doesn't need it, re-enable protection immediately after, and run a full scan afterward. Never disable protection to run cracks, keygens, or pirated software — that's precisely the scenario where 'temporarily disabled' becomes 'infected', and no legitimate software requires it."
  - q: "Can I disable Defender permanently on Windows 11 Pro?"
    a: "Technically Group Policy (Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > 'Turn off Microsoft Defender Antivirus') exists on Pro, but tamper protection must be off first, and Windows still nags and may re-enable components. More importantly, you shouldn't — an unprotected Windows machine in 2026 is compromised quickly. The legitimate permanent alternative is a reputable third-party antivirus, which disables Defender cleanly through the Security Center."
---

There are legitimate reasons to briefly disable Windows Defender: installing a trusted driver package that gets false-flagged, diagnosing whether Defender is the cause of high CPU or slow file operations, or running a specialized tool that conflicts with real-time scanning. The key word is **temporarily** — and Windows 11 is designed to make "temporary" the easy path and "permanent" a fight, because permanent is almost never what you actually want.

This guide covers the supported temporary methods, how to use them safely, the diagnostic technique for confirming Defender is your performance culprit, and — frankly — why the permanent-disable tutorials are a bad idea. If Defender's CPU usage is the actual problem, see [taming Antimalware Service Executable](/articles/how-to-fix-antimalware-service-executable-high-cpu-reddit/) instead of disabling anything. For broader performance work, [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Real-time protection auto re-enables**: Tamper protection and health monitoring restore it by design.
- **False positives on legitimate software**: Heuristic detection occasionally flags trusted installers and tools.
- **Performance diagnostics**: Temporarily disabling confirms whether Defender causes observed slowness.
- **Conflicting security tools**: Some specialized tools require real-time scanning paused during operation.
- **Tamper protection blocks changes**: Even administrators can't silently neuter Defender — malware can't either.
- **Group Policy reverts**: Domain policies and Windows updates can undo manual disables.
- **"Permanent" guides are outdated**: Most registry-disable tutorials predate current tamper protection and no longer work reliably.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Pause real-time protection (the supported method)

The official temporary off switch.

1. Open **Windows Security** > **Virus & threat protection** > **Manage settings** (under Virus & threat protection settings).
2. Toggle **Real-time protection** to **Off** — confirm the UAC prompt.
3. Windows immediately warns you with a red **Actions needed** state — that's expected.
4. Do your task (install the trusted software, run the diagnostic).
5. Toggle it back **On** immediately when done — or let Windows re-enable it automatically (it will, typically within hours or at restart). Verify it's on: the Windows Security icon should return to normal.

### Fix 2: Use the diagnostic pause to test performance issues

Confirm Defender is actually the culprit before making changes.

1. Note your symptom precisely first: which app is slow, what Task Manager shows (MsMpEng.exe CPU %), when it happens.
2. Toggle **Real-time protection** off for 10 minutes (Fix 1).
3. Reproduce the symptom — if it's dramatically better with protection off, Defender's scanning is confirmed as the cause.
4. Toggle protection back on immediately.
5. Now fix the actual problem properly: add **exclusions** for the affected trusted folders (**Manage settings** > **Exclusions**) rather than leaving protection off — see our [Defender tuning guide](/articles/how-to-fix-antimalware-service-executable-high-cpu-reddit/) for the full technique.

### Fix 3: Add a process or folder exclusion instead of disabling

The better solution for recurring conflicts.

1. If a specific trusted program conflicts with Defender every time (developer tools, game modding tools, specialized utilities), exclude it instead of repeatedly disabling protection.
2. **Windows Security** > **Virus & threat protection** > **Manage settings** > **Exclusions** > **Add or remove exclusions**.
3. Add the program's **folder** or the specific **process** — process exclusions are narrower and safer.
4. Only exclude software from vendors you trust, downloaded from official sources.
5. This survives reboots and updates, unlike the temporary toggle — it's the durable version of "Defender, leave this alone." Microsoft's guidance: [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 4: Disable tamper protection (Pro, advanced, careful)

Required before any deeper Defender configuration.

1. **Windows Security** > **Virus & threat protection** > **Manage settings** > toggle **Tamper Protection** off.
2. Understand what this does: it allows changes to Defender settings that malware (and you) otherwise can't make. Your machine is meaningfully less secure while it's off.
3. With tamper protection off, Group Policy or registry Defender settings will actually stick — but so will malware's attempts to disable Defender.
4. Turn tamper protection back on the moment your task is complete — don't leave it off "for convenience."
5. On Windows 11 Home, tamper protection can only be toggled here in the UI — there's no Group Policy alternative.

### Fix 5: The Group Policy method (Pro only, not recommended)

Documented for completeness — think twice.

1. Turn off **Tamper Protection** first (Fix 4) or nothing below will stick.
2. `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Microsoft Defender Antivirus**.
3. Enable **Turn off Microsoft Defender Antivirus**, then restart.
4. Windows will show persistent security warnings, some Store apps behave oddly, and major updates may revert this.
5. Honestly: if you've reached for this, stop and reconsider — the legitimate need for permanently-disabled Defender is vanishingly rare. A conflicting third-party AV (Fix 6) is the supported path.

### Fix 6: Install a proper third-party antivirus instead

The legitimate "replace Defender" path.

1. Choose a reputable AV (Bitdefender, Kaspersky, ESET, Malwarebytes Premium, etc.) — see our [antivirus guide](/articles/best-free-antivirus-for-windows-11-laptop/).
2. Install it normally — it registers with **Windows Security Center**, and Windows automatically stands Defender down cleanly. No hacks, no warnings, no fighting tamper protection.
3. Verify: **Windows Security** > **Virus & threat protection** should show your new provider as active.
4. This is how "not using Defender" is supposed to work — one real-time engine, properly registered, instead of a crippled Defender plus nothing.
5. Uninstalling the third-party AV later automatically restores Defender — the handoff works both ways.

### Fix 7: Safe practices while protection is paused

If protection is off, even briefly, act like it.

1. Disconnect from the network if your task doesn't need internet — no network, no drive-by exposure.
2. Don't browse, don't open email attachments, don't download anything else while paused.
3. Download installers only from official vendor sites, and verify checksums when the vendor publishes them.
4. Re-enable protection the instant the task completes, then run **Windows Security** > **Virus & threat protection** > **Quick scan** as a sanity check.
5. Never, ever disable protection to run pirated software, cracks, or keygens — that scenario ends with malware essentially 100% of the time, and "I turned Defender back on after" doesn't undo an infection.

## Closing

Temporarily disabling Windows Defender is a supported, two-click operation — pause real-time protection, do the trusted task, turn it back on. Everything beyond that (registry hacks, permanent disables) fights Windows' security design and trades a small convenience for real risk. And if the reason you want it off is performance, the tuning guides fix the actual problem without ever leaving you unprotected.
