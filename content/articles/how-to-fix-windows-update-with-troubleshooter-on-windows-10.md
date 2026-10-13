---
title: "Fixing Windows Update With the Troubleshooter on Windows 10"
slug: how-to-fix-windows-update-with-troubleshooter-on-windows-10
date: 2026-09-19
categories: ["windows-update"]
tags: ["troubleshooter", "windows 10", "windows update", "automatic fix"]
description: "Use the Windows 10 Update troubleshooter effectively: what it fixes, what it misses, and the manual steps to take when it comes up short."
thumbnail: "/images/thumbs/how-to-fix-windows-update-with-troubleshooter-on-windows-10.webp"
faqs:
  - q: "What does the Windows Update troubleshooter actually do?"
    a: "It runs a scripted series of checks and repairs: restarting the update services, clearing temporary cache flags, resetting the update database markers, checking for missing system files related to updates, and repairing registry entries. It then reports what it found and fixed. Think of it as an automated version of the first few manual fixes a technician would try."
  - q: "Why does the troubleshooter sometimes find nothing when updates clearly fail?"
    a: "Because it only checks the failure signatures it was programmed to recognize. Novel corruption, hardware-adjacent problems (like a failing drive), and third-party software conflicts fall outside its checks. 'No problems found' means none of its known patterns matched — not that your system is healthy. The manual steps in this article cover what it misses."
  - q: "How is the Windows 10 troubleshooter different from Windows 11's?"
    a: "Functionally they are very similar — same checks, same repairs. The difference is location: Windows 10 keeps it under Settings > Update & Security > Troubleshoot > Additional troubleshooters, while Windows 11 moved it to System > Troubleshoot > Other troubleshooters. Our [Windows 11 troubleshooter guide](/articles/how-to-fix-windows-update-with-troubleshooter-in-windows-11-24h2/) covers the newer layout."
  - q: "Can I run the troubleshooter from the command line?"
    a: "Yes. Open an elevated Command Prompt and run msdt.exe /id WindowsUpdateDiagnostic. This launches the same troubleshooter with administrative rights, which sometimes succeeds where the Settings-launched version fails silently on permissions. It is a useful trick when the GUI path misbehaves."
---

The Windows Update troubleshooter is the official first step for update problems on Windows 10 — and it deserves that position. It automates the tedious early repairs (service restarts, cache flags, registry checks) in a few minutes, and it resolves a solid share of common failures without you touching a command line.

But it is a scripted tool with fixed checks, not a technician. It misses whole categories of problems, and knowing what it does — and what to do when it comes up short — turns it from a coin flip into a reliable first step. This guide shows you how to run it properly, interpret its results, and continue manually exactly where it stops. If the troubleshooter itself [will not run at all](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/), that is a different problem with its own fix path.

## Why this happens

- **Service stalls:** The update services are stuck — the troubleshooter's best fix.
- **Cache flag corruption:** Temporary state flags confusing the engine — also in its wheelhouse.
- **Registry drift:** Update-related registry values damaged — it repairs common ones.
- **Missing system files:** Damaged update components — it detects some, misses others.
- **Database inconsistency:** DataStore problems beyond its scripted checks.
- **Driver conflicts:** Entirely outside what the troubleshooter examines.
- **Third-party interference:** Antivirus and optimizers blocking updates — invisible to the tool.
- **Hardware issues:** Failing drives and bad memory — not its department at all.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the troubleshooter correctly

Most people run it once and move on; run it properly and give it what it needs.

1. Close all programs — the troubleshooter works best on a quiet system.
2. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
3. Select **Windows Update** and click **Run the troubleshooter**.
4. Let it finish completely — do not click away or open other programs.
5. Apply every fix it offers, then restart the laptop even if it does not ask.

### Fix 2: Interpret the results honestly

What the troubleshooter reports tells you where to go next. Microsoft explains the tool's scope on the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. If it says it fixed problems, test immediately: run **Check for updates** and watch.
2. If it found problems but could not fix them, note the exact wording — it names the area to repair manually.
3. If it found nothing, do not assume health — proceed to the manual fixes; your problem is outside its checks.
4. Run it a second time after any manual fix — it sometimes catches secondary issues once the primary one is cleared.
5. Keep a mental log of what it reports across runs; changing reports mean progress.

### Fix 3: Do the service restart manually

When the troubleshooter's automated service restart is not enough, do it by hand with the full sequence.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
3. Run `net start wuauserv`, `net start bits`, `net start cryptsvc`, `net start msiserver`.
4. Check for updates.
5. If updates now work, the troubleshooter's service logic was right but its execution was incomplete.

### Fix 4: Clear the cache the troubleshooter only flags

The troubleshooter detects cache problems more often than it fully clears them.

1. Open an elevated Command Prompt.
2. Stop the four services as in Fix 3.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services and reboot.
5. Check for updates — then run the troubleshooter again to confirm a clean bill.

### Fix 5: Repair system files

Damage the troubleshooter cannot see or fix.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `sfc /scannow`.
4. Restart the laptop.
5. Run the troubleshooter once more — with repaired files, its checks may now pass.

### Fix 6: Remove third-party interference

The troubleshooter never examines your other software — you must.

1. Temporarily disable third-party antivirus real-time protection.
2. Disconnect from VPNs during the update attempt.
3. Check for "optimizer" or "debloat" tools that may have disabled update components.
4. Retry the update with this minimal interference.
5. Re-enable security software immediately after.

### Fix 7: Reset and re-register update components

The deepest manual repair short of reinstalling Windows.

1. Open an elevated Command Prompt.
2. Re-register the core DLLs: `regsvr32 wuapi.dll`, `regsvr32 wuaueng.dll`, `regsvr32 wups.dll`.
3. Reset the services to Automatic via `sc config wuauserv start= auto` and `sc config bits start= delayed-auto`.
4. Restart the laptop.
5. Run the troubleshooter one final time — it should now report a healthy system.

### Fix 8: Use the offline troubleshooter package

Microsoft's downloadable troubleshooter package sometimes works when the built-in one does not.

1. Search Microsoft's support site for the Windows Update troubleshooter download for Windows 10.
2. Download and run the .diagcab package as administrator.
3. Walk through its checks — it is the same engine with a fresh package.
4. Apply its fixes and restart.
5. Verify with **Check for updates** in Settings. If even this fails, the [manual repair sequence](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) for a non-running troubleshooter is your next stop.

## Closing

The Windows 10 Update troubleshooter is a good first step and a bad last step. Run it first, take its results seriously, and then continue manually through the repairs it cannot perform — the service resets, cache clears, and file repairs above. That combination — automated triage plus manual follow-through — resolves the overwhelming majority of Windows 10 update problems. The troubleshooter tells you where the smoke is; the manual steps put out the fire. Make the troubleshooter-plus-manual-follow-up your standard routine and update failures stop being emergencies. One last tip: run the troubleshooter once a quarter even when updates seem fine — it occasionally catches degrading service states before they turn into real failures. On Windows 11 24H2 the same troubleshooter behaves differently — our [24H2 troubleshooter guide](/articles/how-to-fix-windows-update-with-troubleshooter-in-windows-11-24h2/) covers the version-specific quirks.
