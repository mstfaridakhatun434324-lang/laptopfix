---
title: "How to Fix Widgets.exe High CPU, Step by Step"
slug: how-to-fix-widgets-exe-high-cpu-step-by-step
date: 2026-09-13
categories: ["performance"]
tags: ["widgets.exe", "high cpu", "windows widgets", "widgets board", "troubleshooting"]
description: "Widgets.exe eating CPU in the background? Disable, tame, or fix the Windows 11 Widgets board with this step-by-step guide."
thumbnail: "/images/thumbs/how-to-fix-widgets-exe-high-cpu-step-by-step.webp"
faqs:
  - q: "What is Widgets.exe and do I need it?"
    a: "Widgets.exe powers the Windows 11 Widgets board — the news, weather, stocks, and calendar panel that slides in from the left. It's a WebView-based app that periodically refreshes content. You don't need it: nothing in Windows depends on it, and disabling it removes a background CPU consumer with zero effect on system functionality. Most users never open the board deliberately."
  - q: "Is Widgets.exe a virus?"
    a: "No — the legitimate Widgets.exe lives in C:\\Windows\\SystemApps\\MicrosoftWindows.Client.CBS... or the WindowsApps folder and is signed by Microsoft. Malware occasionally impersonates the name, so verify: right-click the process in Task Manager > Open file location. If it's in a Windows system folder, it's genuine. If it's in Downloads, Temp, or AppData, treat it as suspicious and scan immediately."
  - q: "Why does Widgets.exe use CPU when I never open widgets?"
    a: "The Widgets service refreshes its content on a schedule regardless of whether you open the board — fetching news, weather, and stocks in the background. A buggy WebView runtime, a stuck refresh loop, or corrupted widget data can turn that periodic refresh into constant CPU burn. Disabling the board or the scheduled refresh stops it entirely."
  - q: "Will disabling widgets break anything else?"
    a: "No. The Widgets board is standalone — disabling it doesn't affect the Start menu, search, notifications, or any other Windows feature. The taskbar widgets button simply disappears or goes inert. Everything else works exactly as before, usually with measurably lower idle CPU usage."
---

`Widgets.exe` sitting at 15–30% CPU permanently is one of Windows 11's more annoying background burns. You never opened the Widgets board, you don't read its news headlines, yet there it is in Task Manager, chewing cycles and warming the laptop. The Widgets board is a WebView app that refreshes content on a schedule — and when that refresh loop goes wrong, it never stops.

The fix ladder is simple: tame it (reduce its work), disable it (remove it from the equation), or repair it (if you actually like widgets). Most people choose disable and never look back. For the Windows 11-specific variant see [fixing Widgets.exe high CPU on Windows 11](/articles/how-to-fix-widgets-exe-high-cpu-on-windows-11/); for the board-focused Dell variant see [fixing Widgets board high CPU](/articles/how-to-fix-widgets-board-high-cpu-windows-11-on-dell-laptop/).

## Why this happens

- **Stuck content refresh loop**: The board's scheduled fetch never completing, retrying forever.
- **Buggy WebView2 runtime**: The embedded browser engine widgets run on, misbehaving after updates.
- **Corrupt widget data/cache**: Damaged local data causing the renderer to spin.
- **News feed hammering**: Aggressive refresh of MSN content feeds in the background.
- **Weather widget polling**: Location/weather updates firing far too often.
- **Third-party widgets**: Added widgets with inefficient or broken code.
- **Taskbar integration overhead**: The taskbar button's live content (weather) updating constantly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it's the legitimate Widgets.exe

Thirty seconds of due diligence.

1. In Task Manager's **Details** tab, right-click **Widgets.exe** > **Open file location** — genuine copies live under `C:\Windows\SystemApps\` or `C:\Program Files\WindowsApps\` in Microsoft-signed folders.
2. Right-click the file > **Properties** > **Digital Signatures** — it should be signed by Microsoft.
3. If it's anywhere else (Downloads, Temp, AppData\Roaming), stop here and run a full Defender scan plus an offline scan — that's malware wearing the name.
4. Note the CPU pattern: constant moderate usage points to a refresh loop; spiking usage points to scheduled refreshes working normally but too often.
5. Assuming it's genuine, continue — the fixes below are safe for the real Widgets.exe.

### Fix 2: Turn off the Widgets board (the popular fix)

Remove it from the equation entirely.

1. Go to **Settings** > **Personalization** > **Taskbar** and toggle **Widgets** to **Off** — this removes the taskbar button and stops the board's UI.
2. Check Task Manager after a minute — on many systems, Widgets.exe exits on its own once the board is disabled.
3. If it persists, open **Settings** > **Apps** > **Installed apps**, find **Windows Web Experience Pack** (the Widgets host), click **...** > **Advanced options** > **Terminate**, then set **Background apps permissions** to **Never**.
4. Verify in Task Manager that Widgets.exe is gone and stays gone after a restart.
5. This is reversible — toggling Widgets back on in taskbar settings restores everything. Nothing else in Windows depends on it.

### Fix 3: Disable it via Group Policy / Registry (thorough)

For when the toggle isn't enough.

1. **Windows 11 Pro**: press **Win+R**, type `gpedit.msc`, go to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Widgets** > enable **Allow widgets** set to **Disabled**.
2. **Windows 11 Home** (no gpedit): open Registry Editor, navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Dsh`, create DWORD **AllowNewsAndInterests** = 0 (create the Dsh key if missing). Back up the key first (File > Export).
3. Restart — the Widgets board is now policy-disabled and Widgets.exe shouldn't launch at all.
4. To reverse: set the policy to **Not configured** or delete the registry value.
5. Note: major feature updates occasionally reset this — if Widgets.exe mysteriously returns after an update, re-check the policy.

### Fix 4: Repair it (if you actually use widgets)

For those who like the board and want it fixed, not gone.

1. Update **Microsoft Edge WebView2 Runtime** — Widgets run on WebView2, and an outdated or corrupt runtime causes the CPU burn. Download the latest from Microsoft's WebView2 page or via Windows Update's optional updates.
2. Open the Widgets board (**Win+W**), click your profile icon > **Widget settings**, and remove third-party widgets — keep only Microsoft's stock ones as a test.
3. Turn off the most aggressive feeds: in widget settings, disable news topics you don't read — fewer feeds, less refresh work.
4. **Settings** > **Apps** > **Installed apps** > **Windows Web Experience Pack** > **...** > **Advanced options** > **Repair**, then **Reset** if repair doesn't help.
5. Reinstall the Web Experience Pack from the Microsoft Store if reset fails — a fresh copy clears corrupt local data.

### Fix 5: Stop the background refresh behavior

Tame it without fully disabling.

1. In **Windows Web Experience Pack** > **Advanced options**, set **Background apps permissions** to **Power optimized** (instead of Always) — refreshes yield to battery and idle states.
2. Open the Widgets board settings and sign out of the Microsoft account in widgets if you don't need personalized feeds — personalization drives much of the refresh traffic.
3. In **Settings** > **Privacy & security** > **Location**, review whether Widgets needs location access — constant location polling for the weather widget adds wakeups.
4. Reduce **Notifications** from widgets: **Settings** > **System** > **Notifications** > turn off widget notification badges that trigger refreshes.
5. Check Task Manager after each change — you want Widgets.exe at 0% when the board is closed, with only brief activity on manual open.

### Fix 6: Check for the deeper cause

When Widgets.exe burns CPU despite everything.

1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` — the Web Experience Pack depends on system components.
2. Check **Event Viewer** > **Windows Logs** > **Application** for WebView2 or Widgets errors at the times of high CPU — they often name the failing module.
3. Create a new local user account and test — if Widgets.exe behaves there, your profile's widget data is corrupt; the Reset in Fix 4 (per-user data) or profile migration fixes it.
4. Review [Microsoft's Windows support](https://support.microsoft.com/en-us/windows) for known Widgets issues in your build — some builds ship with Widgets regressions fixed by cumulative updates.
5. Final option: the Fix 2/3 disable route. A Widgets board you never open isn't worth diagnostic heroics — disable it and reclaim the CPU permanently.

## Closing

Widgets.exe high CPU is a background-content problem: a news-and-weather panel refreshing like it has something urgent to tell you, forever. Verify it's genuine, then either tame its refresh behavior or disable the board outright — both take minutes, both are reversible, and neither affects anything else in Windows. The Widgets board is the easiest performance win in Windows 11 precisely because nobody misses it.
