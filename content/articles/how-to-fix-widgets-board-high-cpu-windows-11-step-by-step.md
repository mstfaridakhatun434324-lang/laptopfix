---
title: "Widgets Board High CPU on Windows 11? Step-by-Step Fix"
slug: "how-to-fix-widgets-board-high-cpu-windows-11-step-by-step"
date: "2026-09-03"
categories: ["performance"]
tags: ["widgets board", "widgets.exe", "high cpu", "windows 11", "step by step"]
description: "A complete step-by-step walkthrough for fixing Widgets board high CPU on Windows 11 — from quick triage to permanent removal, in the exact order a technician would do it."
thumbnail: "/images/thumbs/how-to-fix-widgets-board-high-cpu-windows-11-step-by-step.webp"
faqs:
- q: "How do I know if Widgets is causing my high CPU?"
  a: "Open Task Manager, go to Processes, and look for 'Widgets' or 'Windows Widgets' — expand it to see its Microsoft Edge WebView2 subprocesses. If their combined CPU stays above 5% while you're doing nothing, Widgets is a meaningful contributor. Compare before and after ending the Widgets processes to confirm the difference it makes."
- q: "What is the fastest way to stop Widgets high CPU?"
  a: "End the Widgets processes in Task Manager for instant relief, then turn off the Widgets taskbar toggle in Taskbar settings to prevent accidental launches. For a permanent fix, disable Widgets via Group Policy or the Registry so it never starts again. The whole permanent procedure takes under five minutes."
- q: "Will Windows updates bring Widgets back after I disable it?"
  a: "Feature updates occasionally reinstall the Windows Web Experience Pack (which provides Widgets), re-enabling the board. The Group Policy/Registry disable usually survives, but if Widgets reappears after a major update, simply re-run the uninstall command. It takes thirty seconds and is worth checking after each feature update."
- q: "Do I lose anything important by removing Widgets?"
  a: "No. Widgets duplicates information available elsewhere: weather apps, news sites, calendar apps, and stock trackers all work independently. No Windows functionality, security feature, or application depends on the Widgets board. Removing it is one of the safest performance optimizations you can make."
---

This is the technician's sequence for Widgets board CPU problems: start with instant triage, confirm the diagnosis, try the lightweight repairs, then apply the permanent fix if you want it gone for good. Follow the steps in order, checking Task Manager after each one. Stop when your CPU is quiet — most people stop at step 4.

You'll need about fifteen minutes and administrator access for the permanent steps. Nothing here risks your data.

One note before you start: Widgets' CPU cost is easy to underestimate because it's spread across several processes — the main Widgets.exe plus multiple Edge WebView2 helpers. Add them together in Task Manager (expand the Widgets group) to see the true total. On laptops already running close to capacity, that combined load is frequently the difference between silent idle and constantly spinning fans.

## Why this happens

- **Scheduled background feed refreshes** — the board updates news, weather, and stocks whether you open it or not.
- **WebView2 rendering loops** — the Edge-based engine behind Widgets can spin on buggy feed content.
- **Corrupted feed cache** — damaged cache files cause repeated failed refresh cycles.
- **Accidental board launches** — the taskbar widget button or Win+W opens it, and it stays resident.
- **Outdated WebView2 runtime** — known high-CPU bugs fixed in newer runtime versions.
- **Animated widgets** — live weather and visual widgets cost disproportionate CPU.
- **Competing background software** — on busy systems, Widgets' constant activity is the straw that breaks the camel's back.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Triage — confirm and get instant relief

First, verify Widgets is actually the problem and stop the bleeding.

Steps:

1. Press `Ctrl + Shift + Esc` to open Task Manager.
2. In the Processes tab, find **Widgets** (may show as "Windows Widgets") and expand it.
3. Note the CPU percentage of Widgets plus its WebView2 children — screenshot or write down the numbers.
4. Right-click each Widgets/WebView2 process → **End task**.
5. Watch overall CPU for two minutes — if it drops noticeably, diagnosis confirmed; proceed.

### Fix 2: Remove the taskbar entry point

Stop accidental launches that keep resurrecting the processes.

Steps:

1. Right-click an empty area of the taskbar → **Taskbar settings**.
2. Find **Widgets** in the taskbar items list and toggle it **Off**.
3. The weather/news button disappears from the taskbar.
4. Restart the laptop.
5. Check Task Manager after reboot — Widgets processes should not start on their own (though they can still be triggered by Win+W).

### Fix 3: Update WebView2 and Edge

Rule out the known buggy-runtime cause before going nuclear.

Steps:

1. Open Microsoft Edge → Settings → About Microsoft Edge — let it update fully.
2. Check Installed apps for **Microsoft Edge WebView2 Runtime** and note the version.
3. Download the latest Evergreen WebView2 installer from Microsoft and install it over the existing runtime.
4. Restart the laptop.
5. Monitor Widgets CPU for an hour of idle time — if it's quiet now, the runtime was the cause. Microsoft's [support hub](https://support.microsoft.com/en-us/windows) has current WebView2 guidance.

### Fix 4: Clear the Widgets cache and data

A corrupted cache is the most common "it came back" cause.

Steps:

1. End all Widgets and WebView2 processes in Task Manager.
2. Press `Win + R`, type `%LOCALAPPDATA%\Packages`, and press Enter.
3. Find the folder starting with `MicrosoftWindows.Client.WebExperience` and open it.
4. Navigate into LocalState (or similar) and delete cached feed data — or rename the folder as a backup.
5. Restart — Widgets rebuilds its cache cleanly. Monitor for 24 hours.

### Fix 5: Disable Widgets permanently (Group Policy)

The definitive fix for Pro/Enterprise editions.

Steps:

1. Press `Win + R`, type `gpedit.msc`, press Enter.
2. Navigate to **Computer Configuration → Administrative Templates → Windows Components → Widgets**.
3. Double-click **Allow widgets**, set it to **Disabled**, click OK.
4. Open an elevated Command Prompt and run `gpupdate /force`.
5. Restart and verify in Task Manager that no Widgets processes exist after boot.

### Fix 6: Disable Widgets permanently (Registry, Home edition)

The same result for Windows 11 Home, via the registry.

Steps:

1. Press `Win + R`, type `regedit`, press Enter (approve the UAC prompt).
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows` — create a new key named `Dsh` under Windows if absent.
3. Inside `Dsh`, create a DWORD (32-bit) Value named `AllowNewsAndInterests` set to `0`.
4. Close Registry Editor and restart.
5. Verify Widgets is gone from Task Manager after reboot. (To reverse: delete the DWORD or set it to 1.)

### Fix 7: Uninstall the Web Experience Pack

Belt and suspenders — remove the Widgets application package entirely.

Steps:

1. Open Terminal as Administrator.
2. Run: `winget uninstall "Windows Web Experience Pack"`.
3. If winget doesn't find it, use PowerShell: `Get-AppxPackage *WebExperience* | Remove-AppxPackage`.
4. Restart the laptop.
5. Confirm no Widgets processes return. If a future feature update reinstalls it, repeat this command — and check our [HP-specific Widgets guide](/articles/how-to-fix-widgets-board-high-cpu-windows-11-on-hp-laptop/) for brand-specific background-trimming tips that pair well with removal.

### Fix 8: Verify the gain and lock it in

Confirm the fix worked and make sure it sticks.

Steps:

1. After reboot, open Task Manager and confirm zero Widgets/WebView2 processes at idle.
2. Compare idle CPU and fan behavior to your Fix 1 baseline — you should see a clear improvement.
3. Note your battery life over the next few days; many users gain 20–45 minutes.
4. After each future Windows feature update, glance at Task Manager to confirm Widgets hasn't returned.
5. If it returns, re-apply Fix 7 — thirty seconds, done.

## Closing

That's the full sequence: triage, remove the trigger, update the runtime, clear corruption, then disable or uninstall permanently. For most users, Fix 5 or 6 is where the story ends — Widgets never runs again, the fans quiet down, and nothing of value is lost. It's one of the highest reward-to-effort optimizations in Windows 11. If other background processes are still keeping your CPU busy, our [Windows 11 speed-up guide](/articles/how-to-speed-up-windows-11-laptop/) continues the cleanup.
