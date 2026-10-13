---
title: "How to Temporarily Disable Windows Defender on Windows 10"
slug: "how-to-disable-windows-defender-temporarily-on-windows-10"
date: "2026-10-01"
categories: ["performance"]
tags: ["windows defender", "disable defender", "real-time protection", "windows 10", "tamper protection"]
description: "Need to pause Windows Defender on Windows 10 for a software install or troubleshooting? Here's the safe way to disable real-time protection temporarily — and what to watch for."
thumbnail: "/images/thumbs/how-to-disable-windows-defender-temporarily-on-windows-10.webp"
faqs:
- q: "How long does Windows Defender stay disabled when I turn off real-time protection?"
  a: "When you toggle off real-time protection through Settings, Windows 10 automatically turns it back on after a short period — usually within minutes to a few hours — or after the next restart. It is intentionally designed to be temporary. If you need it off for longer, you must use Group Policy or Registry edits on supported editions."
- q: "Is it safe to temporarily disable Windows Defender?"
  a: "For short, controlled windows — such as installing trusted software or testing a suspected conflict — yes, as long as you are not browsing, downloading, or opening email attachments while it is off. Re-enable protection immediately afterward and run a quick scan. Never leave Defender off indefinitely without a replacement antivirus."
- q: "Why does the real-time protection toggle keep turning itself back on?"
  a: "Windows 10 is designed to re-enable real-time protection automatically as a safety measure, especially after restarts. This is normal behavior, not a bug. Tamper protection also prevents apps and users from silently changing security settings. If it turns back on, it means the system is working as designed."
- q: "Does disabling Windows Defender speed up my laptop?"
  a: "It can slightly reduce background CPU and disk usage, especially during heavy file operations, but the gain is usually small and short-lived. If Defender is causing severe slowdowns, the better fix is to tune exclusions and scan schedules rather than disable protection. See our guide on [Defender high CPU fixes](/articles/how-to-fix-windows-defender-high-cpu-usage-in-windows-11-24h2/) for the safer approach."
---

There are legitimate reasons to pause Windows Defender for a bit — a trusted installer that keeps getting quarantined, testing whether Defender is behind a performance problem, or running a specific troubleshooting session. Windows 10 makes this easy to do through Settings, and just as importantly, it makes sure you can't accidentally leave yourself unprotected forever.

The catch is knowing the difference between the quick temporary toggle and the deeper methods. The quick toggle is safe and self-reversing; the permanent methods are a different beast entirely, and most people should never touch them. I'll walk through the safe path first and explain when (and whether) you need anything more.

## Why this happens

- **Real-time protection is designed to be temporary-only in Settings** — Microsoft built the toggle to re-enable itself so users can't accidentally leave the system unprotected.
- **Tamper protection blocks setting changes** — this feature prevents apps, malware, and even administrators from silently altering security configuration.
- **Third-party antivirus takes over automatically** — when a recognized AV product is installed, Windows Defender steps aside on its own.
- **Group Policy can lock the setting** — on Pro and Enterprise editions, IT policies or previous tweaks can disable the toggle entirely.
- **Some installers trigger false positives** — developer tools, game mods, and niche utilities get flagged by heuristic scanning even when they're safe.
- **You suspect Defender is causing a slowdown** — pausing it briefly is a legitimate diagnostic step to confirm whether it's the culprit.
- **The toggle is greyed out** — usually caused by Group Policy settings, an enterprise management tool, or a malware infection fighting to stay hidden.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the Settings toggle (the safe temporary method)

This is the method Microsoft intends for short-term use. Real-time protection turns back on by itself, which is exactly what you want.

Steps:

1. Open **Settings → Update & Security → Windows Security**.
2. Click "Virus & threat protection."
3. Under "Virus & threat protection settings," click "Manage settings."
4. Toggle **Real-time protection** to Off.
5. If prompted by User Account Control, click Yes.
6. Do your task (install software, run the test), then return and toggle it back On immediately.

### Fix 2: Handle Tamper Protection if the toggle is greyed out

On the same settings page, Tamper Protection may prevent the change. For official guidance on these controls, see Microsoft's [Windows security documentation](https://support.microsoft.com/en-us/windows).

Steps:

1. In the same Virus & threat protection settings page, find **Tamper Protection**.
2. Toggle it Off temporarily (Windows will warn you — this is expected).
3. Now toggle Real-time protection Off.
4. Complete your task and re-enable **both** switches in reverse order: Real-time protection first, then Tamper Protection.
5. Never leave Tamper Protection off — it blocks malware from disabling Defender silently.

### Fix 3: Disable via Group Policy (Windows 10 Pro and Enterprise)

For a longer pause on Pro editions, Group Policy gives you a supported off switch. Note: on Windows 10 version 1903 and later, the "Turn off Windows Defender Antivirus" policy is ignored when Tamper Protection is on.

Steps:

1. Press `Win + R`, type `gpedit.msc`, and press Enter.
2. Navigate to **Computer Configuration → Administrative Templates → Windows Components → Microsoft Defender Antivirus → Real-time Protection**.
3. Double-click "Turn off real-time protection," set it to Enabled, and click OK.
4. Restart the laptop for the policy to take effect.
5. To reverse it, set the policy back to "Not Configured" and restart.

### Fix 4: Disable via Registry (Windows 10 Home)

Home edition has no Group Policy editor, so the Registry is the equivalent path. Back up the registry key first — a wrong edit here can cause real problems.

Steps:

1. Press `Win + R`, type `regedit`, and press Enter.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender`.
3. Right-click in the right pane → New → DWORD (32-bit) Value, name it `DisableAntiSpyware`, and set its value to `1`.
4. If you only want real-time scanning off, go to the `Real-Time Protection` subkey and create a DWORD named `DisableRealtimeMonitoring` set to `1`.
5. Restart the laptop.
6. To undo, delete the DWORD values you created (or set them to `0`) and restart.

### Fix 5: Install a third-party antivirus instead of disabling protection

The cleanest way to turn Defender off "permanently" is to replace it, not gut it. Windows automatically yields to a registered third-party antivirus.

Steps:

1. Choose a reputable antivirus and download it only from the vendor's official site — see our roundup of the [best free antivirus options for Windows 11 laptops](/articles/best-free-antivirus-for-windows-11-laptop/) if you need a starting point.
2. Install it and let it register with Windows Security Center.
3. Open Windows Security and confirm it now shows your new antivirus as the provider.
4. Verify Defender's real-time protection is off (it should be, automatically).
5. Keep the third-party product updated — an expired AV that stops working can leave you with neither engine active.

### Fix 6: Re-enable protection and verify afterward

Whatever method you used, always close the loop. An unprotected laptop on the open internet picks up malware fast.

Steps:

1. Return to Windows Security → Virus & threat protection.
2. Confirm Real-time protection, Cloud-delivered protection, and Tamper Protection are all On.
3. Run a **Quick scan** to check nothing slipped in while protection was paused.
4. If you used Group Policy or Registry edits, revert them and restart so the system returns to a managed state.
5. If you're still fighting false positives on a specific program, [add a Defender exclusion](/articles/how-to-fix-antimalware-service-executable-high-cpu-fix/) for that program's folder instead of disabling everything.

## Closing

Temporarily disabling Windows Defender on Windows 10 is straightforward — the Settings toggle exists for exactly this purpose, and Windows turns protection back on by itself so you can't forget. Use Group Policy or Registry methods only if you genuinely need a longer window, and always re-enable protection when you're done. If Defender keeps interfering with a program you trust, folder exclusions are the safer long-term answer than switching protection off.
