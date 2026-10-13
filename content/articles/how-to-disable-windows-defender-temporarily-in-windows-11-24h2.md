---
title: "How to Disable Windows Defender Temporarily in Windows 11 24H2"
slug: how-to-disable-windows-defender-temporarily-in-windows-11-24h2
date: 2026-09-28
categories: ["performance"]
tags: ["windows defender", "disable antivirus", "real-time protection", "windows 11 24h2"]
description: "Need to pause Windows Defender briefly in Windows 11 24H2? The safe temporary methods — and what to do instead of disabling it."
thumbnail: "/images/thumbs/how-to-disable-windows-defender-temporarily-in-windows-11-24h2.webp"
faqs:
  - q: "Is it safe to disable Windows Defender temporarily?"
    a: "Briefly, yes — if you know why you're doing it. Common legitimate reasons: installing trusted software that Defender blocks, or testing whether Defender is the cause of high CPU or disk usage. The risk window is small if you re-enable protection immediately after and don't browse or download in the meantime. What's not safe: leaving it off for days, disabling it permanently, or turning it off to run untrusted software."
  - q: "Why does Windows turn Defender back on by itself?"
    a: "That's Tamper Protection doing its job — it prevents malware (and users) from silently disabling security. Real-time protection automatically re-enables after a short period, and always after a restart. This is intentional design, not a bug. If you need longer-term exclusion of a specific trusted program, use Defender's exclusion list instead of fighting the auto-reenable behavior."
  - q: "What's the difference between disabling real-time protection and Tamper Protection?"
    a: "Real-time protection is the active scanning engine — toggling it off pauses file scanning. Tamper Protection is the guard that prevents changes to Defender's own settings; with it on, some disable methods (Registry edits, Group Policy) are blocked. For a quick temporary test, you only touch real-time protection. Leave Tamper Protection on unless you have a specific reason and understand the risk."
  - q: "Are there better alternatives to disabling Defender?"
    a: "Almost always, yes. If Defender blocks a trusted program, add a file or folder exclusion instead of disabling everything. If Defender causes high CPU, schedule scans for idle hours and exclude high-churn folders. If you're installing another antivirus, it will disable Defender automatically and properly. Full temporary disable is the blunt instrument — exclusions and scheduling are the scalpels."
---

There are legitimate moments to pause Windows Defender: a trusted installer it keeps quarantining, a performance test to see if Defender is the bottleneck, or a software conflict to diagnose. Windows 11 24H2 makes the temporary toggle easy — but it also fights you if you try to make it permanent, thanks to Tamper Protection. That's a feature, not an obstacle.

This guide shows the safe temporary methods (Settings toggle, and what to know about the others), how long each lasts, and — more importantly — the better alternatives for the common scenarios that make people reach for the off switch. If Defender's resource usage is your actual complaint, read [taming Antimalware Service Executable](/articles/antimalware-service-executable-high-cpu-windows-11/) first; you probably don't need to disable anything. For the broader performance picture, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Defender blocks a trusted installer**: False positives on niche software, drivers, or game mods are the top reason people pause protection.
- **Diagnosing performance issues**: Temporarily disabling real-time protection is a valid test for whether Defender causes high CPU/disk.
- **Software conflicts**: Rare clashes with development tools, virtualization, or disk utilities.
- **Tamper Protection re-enables it**: The guard feature reverses disable attempts — by design.
- **Group Policy/Registry methods are blocked**: On 24H2 with Tamper Protection on, the old permanent-disable tricks don't work.
- **Third-party AV handles it automatically**: Installing another antivirus properly disables Defender — manual disabling is unnecessary.
- **Misunderstanding the need**: Many "disable Defender" searches are really "Defender is slow" problems with better fixes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the Settings toggle (the intended temporary method)

The official, safe way to pause protection.

1. Open **Windows Security** (search it in Start) > **Virus & threat protection** > **Manage settings** (under Virus & threat protection settings).
2. Toggle **Real-time protection** to **Off**. Confirm the UAC prompt.
3. Do the thing you needed to do — install the software, run the test — promptly.
4. Toggle **Real-time protection** back **On** immediately afterward. Don't browse, download, or open email attachments while it's off.
5. Note: Windows re-enables it automatically after a while and on every restart — this is expected. Plan your task to fit in the window.

### Fix 2: Add an exclusion instead of disabling everything

The better answer for blocked trusted software.

1. In **Windows Security** > **Virus & threat protection** > **Manage settings**, scroll to **Exclusions** > **Add or remove exclusions**.
2. Click **Add an exclusion** and choose **File**, **Folder**, or **Process** — point it at the trusted installer or program folder.
3. Folder exclusions are best for development tools or games with many files; process exclusions for a specific executable.
4. Never exclude broad locations (Downloads, Temp, entire drives) — exclusions are holes in your protection; keep them small and specific.
5. Test the software again — with the exclusion in place, Defender leaves it alone while protecting everything else.

### Fix 3: Schedule around Defender instead of disabling it

For the "Defender slows my work" scenario.

1. Open **Task Scheduler** (`taskschd.msc`) > **Microsoft** > **Windows** > **Windows Defender** > **Windows Defender Scheduled Scan** > **Properties**.
2. Set the scan trigger to idle hours (e.g., 3 AM) and enable **Start the task only if the computer is idle**.
3. Add exclusions for high-churn trusted folders (build outputs, game libraries) as in Fix 2.
4. Check **Protection history** in Windows Security — if Defender is repeatedly scanning the same files, those paths are your exclusion candidates.
5. This resolves the performance complaint permanently without any protection gap.

### Fix 4: Understand Tamper Protection (don't fight it)

Know what you're up against before trying advanced methods.

1. In **Windows Security** > **Virus & threat protection** > **Manage settings**, note the **Tamper Protection** toggle — it blocks changes to Defender settings by Registry, policy, or third-party tools.
2. With it on (the default), the old "disable via Registry/GPO" guides simply don't work on 24H2 — the setting reverts.
3. Turning Tamper Protection off to force a permanent disable is strongly discouraged: it removes the guard that stops malware from doing exactly what you're doing. Microsoft documents Tamper Protection in detail on [Microsoft Support](https://support.microsoft.com/en-us/windows).
4. Legitimate long-term need (e.g., enterprise tooling)? That's what Group Policy with proper management is for — not consumer toggle-hacking.
5. Bottom line: if you find yourself fighting Tamper Protection, you're solving the wrong problem — use exclusions (Fix 2) instead.

### Fix 5: Let a third-party antivirus take over properly

If you actually want different protection.

1. If your goal is replacing Defender (not just pausing it), install the reputable third-party antivirus of your choice — it registers with Windows Security Center and Defender stands down automatically and cleanly.
2. Never run two real-time antivirus engines simultaneously — they fight over every file and tank performance.
3. After installation, verify in **Windows Security** > **Virus & threat protection** that the new provider shows as active.
4. Uninstalling the third-party AV later re-awakens Defender automatically — no manual steps needed.
5. Keep Windows' **firewall** and **SmartScreen** considerations separate — those are independent layers worth leaving on regardless.

### Fix 6: Use Defender's own diagnostic data

Confirm Defender is actually your problem before disabling it.

1. Open **Task Manager** > **Processes** and check `MsMpEng.exe` (Antimalware Service Executable) CPU/disk during your slowdown — correlate timing.
2. Check **Windows Security** > **Virus & threat protection** > **Protection history** for scan activity matching the slow periods.
3. If Defender is quiet during the slowdown, disabling it won't help — look elsewhere (startup programs, disk health, thermals).
4. If it IS the cause, Fixes 2 and 3 are your permanent solutions — not the toggle.
5. For a deeper dive into Defender CPU specifically, see the [dedicated guide](/articles/antimalware-service-executable-high-cpu-windows-11/).

## Closing

Pausing Windows Defender temporarily in 24H2 is a two-click job in Windows Security — and Windows will turn it back on, which is exactly what you want. But treat the toggle as a diagnostic tool and a brief workaround, not a solution. For blocked software, exclusions are better; for performance complaints, scheduling and exclusions are better; for replacing protection, a proper third-party install is better. The off switch is the bluntest tool in the box — reach for the scalpels first.
