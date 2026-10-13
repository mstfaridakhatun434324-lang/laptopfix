---
title: "Widgets.exe High CPU After a Windows 11 Update? Fix It"
slug: how-to-fix-widgets-exe-high-cpu-after-windows-11-update
date: 2026-10-03
categories: ["performance"]
tags: ["widgets.exe", "high cpu", "windows 11 update", "widgets board"]
description: "Widgets.exe burning CPU after a Windows 11 update? Calm the Widgets board's background activity or disable it cleanly."
thumbnail: "/images/thumbs/how-to-fix-widgets-exe-high-cpu-after-windows-11-update.webp"
faqs:
  - q: "What is Widgets.exe and do I need it?"
    a: "Widgets.exe powers the Widgets board — the news, weather, stocks, and calendar panel that slides out from the left side of the taskbar in Windows 11. It's a convenience feature, not a system requirement. If you never open the Widgets board, the process is pure overhead and disabling it costs you nothing. Even if you like widgets, the fixes here calm its background CPU without removing the feature."
  - q: "Why did Widgets.exe start using CPU after the update?"
    a: "Windows updates frequently reset Widgets settings, re-enable the Widgets board and its taskbar entry, refresh the content feed configuration, and sometimes introduce feed bugs that make the process poll aggressively. Updates can also corrupt the Widgets cache, causing the process to retry failed content fetches in a loop. All of these are update-aftermath issues, not permanent behavior."
  - q: "Will disabling Widgets break anything in Windows?"
    a: "No. Widgets is a standalone feature — disabling the board and its background process affects nothing else in Windows. The taskbar, Start menu, notifications, and Microsoft Edge all work normally. The only loss is the Widgets panel itself. Microsoft provides official toggles for it, which signals it's designed to be optional."
  - q: "Is Widgets.exe related to high memory usage too?"
    a: "Often yes — the same feed-refresh and cache problems that spike CPU also bloat memory, since Widgets.exe is built on WebView2 (essentially a browser engine) and leaky content feeds accumulate. The fixes here address both: clearing the cache, limiting feed refresh, or disabling the feature entirely resolves the CPU and memory symptoms together."
---

After a Windows 11 update, you notice the fan spinning at idle — and Task Manager blames `Widgets.exe`, a process for a Widgets board you never open. Updates love to re-enable Widgets, reset its feed, and occasionally corrupt its cache into a CPU-burning retry loop. The good news: this is one of the most optional processes in Windows, and taming it is easy.

You have two philosophies available: keep Widgets but calm it down, or remove it from your life entirely. This guide covers both — start with calming, escalate to removal if the process won't behave.

For the broader Widgets board CPU topic see [Widgets board high CPU](/articles/best-way-to-fix-widgets-board-high-cpu-windows-11/); if animations feel sluggish too, [animation lag fixes](/articles/how-to-fix-windows-11-animations-lagging/).

## Why this happens

- **Update re-enabled the board**: Feature updates turn Widgets back on and reset its taskbar presence.
- **Corrupt Widgets cache**: Damaged feed cache causing endless failed refresh retries.
- **Aggressive feed polling**: News/weather/stocks feeds refreshing too frequently or error-looping.
- **WebView2 issues**: The underlying browser engine misbehaving after the update.
- **Location/weather polling**: Constant location checks for the weather widget keeping the process active.
- **Feed personalization churn**: Microsoft's content pipeline re-profiling after the update.
- **Stuck background task**: The Widgets background task failing to complete and retrying.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Widgets.exe is the sustained consumer

Make sure it's not a transient spike.

1. Task Manager > **Processes** — find **Widgets** (`Widgets.exe`). Note CPU over 5 minutes: sustained 5–15%+ at idle is the problem; brief spikes when opening the board are normal.
2. Expand it if possible and check memory too — feed-cache issues usually inflate both CPU and RAM.
3. Ask: did this start right after a Windows update? Check **Settings** > **Windows Update** > **Update history** for the date correlation.
4. Open the Widgets board (Win+W) once — does it load content, show errors, or spin forever? A board that can't load its feed is the visual symptom of the retry loop burning your CPU.
5. If the board loads fine and CPU is calm after opening it once, the process may have just needed to complete a post-update sync — monitor for a day before changing anything.

### Fix 2: Turn off the Widgets board and taskbar entry

The official off switch.

1. **Settings** > **Personalization** > **Taskbar** — toggle **Widgets** to **Off**. This removes the taskbar button and stops the board's UI presence.
2. Open Task Manager and end the **Widgets** process — with the toggle off, it should not respawn.
3. Monitor for a day: if Widgets.exe stays gone and CPU is calm, you're done — this is the intended "I don't use Widgets" configuration.
4. If it respawns despite the toggle (updates sometimes re-enable it), proceed to Fix 5 for stronger measures.
5. Note: this keeps the underlying capability installed but dormant — zero UI, zero background CPU, fully reversible by toggling back on.

### Fix 3: Clear the Widgets cache and reset the feed

For those who want to keep Widgets.

1. End **Widgets.exe** in Task Manager.
2. Open File Explorer and navigate to `%localappdata%\Microsoft\Windows\Widgets` (paste into the address bar) — delete the contents of this cache folder.
3. Also clear the WebView2 cache Widgets uses: `%localappdata%\Microsoft\EdgeWebView` — delete stale cache data (this is shared with Edge's engine; it rebuilds automatically).
4. Open the Widgets board (Win+W), click the **settings gear** > sign out and back into the Widgets/Microsoft content personalization, then re-add only the widgets you actually want (weather, calendar) — fewer widgets = less feed polling.
5. Watch CPU for a day — a clean cache plus minimal widgets usually returns Widgets.exe to near-zero idle CPU.

### Fix 4: Limit feed refresh and location polling

Reduce what the process does in the background.

1. In the Widgets board settings, turn off **news feed** / content personalization if you only want utility widgets (weather, calendar, stocks) — the news pipeline is the heaviest poller.
2. **Settings** > **Privacy & security** > **Location** — review whether Widgets needs location access; the weather widget polls location, and restricting it to a static city (set manually in the weather widget) stops constant location checks.
3. **Settings** > **Apps** > **Installed apps** — check for **Windows Web Experience Pack** (the Store package behind Widgets) and update it via the Microsoft Store — feed bugs are often fixed in these updates.
4. In the Microsoft Store, check for **WebView2 Runtime** updates too — the engine Widgets runs on.
5. After limiting feeds, the process should show only brief activity when you actually open the board — that's the healthy pattern.

### Fix 5: Disable Widgets via Group Policy or registry

When the toggle doesn't stick.

1. **Windows 11 Pro**: Win+R > `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Widgets** > enable **Allow widgets** = **Disabled**. This is the enterprise-grade off switch that updates respect.
2. **Windows 11 Home** (no gpedit): registry method — back up first, then create/modify `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Dsh` > DWORD `AllowNewsAndInterests` = `0`. Create the `Dsh` key if it doesn't exist.
3. Restart after either change. Verify in Task Manager that Widgets.exe is gone and doesn't return after reboot.
4. To re-enable later: set the policy to **Not configured** or delete the registry value, then restart.
5. These methods survive feature updates far better than the Settings toggle — which is exactly why they exist. Policy reference via [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 6: Repair WebView2 and the Web Experience Pack

For Widgets.exe that crashes, loops, or won't calm down.

1. **Settings** > **Apps** > **Installed apps** — find **Microsoft Edge WebView2 Runtime** > **⋯** > **Modify** > **Repair**.
2. Open the **Microsoft Store** > **Library** — update **Windows Web Experience Pack** to the latest version.
3. Elevated terminal: `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` — repairs the system components hosting Widgets.
4. After repairs, clear the Widgets cache once more (Fix 3) so the fixed components start from clean data.
5. Test: enable the board temporarily, open it, confirm content loads and CPU settles — then disable again if you don't want it. A repaired stack behaves; an unrepaired one relapses.

### Fix 7: Uninstall the Web Experience Pack (nuclear option)

Complete removal for the Widgets-averse.

1. Open an elevated **PowerShell** or Terminal.
2. Run `winget uninstall "Windows Web Experience Pack"` — this removes the Store package behind Widgets entirely.
3. Verify Widgets.exe is gone from Task Manager and the taskbar toggle disappears from Settings.
4. Understand the tradeoff: this is harder to reverse than a toggle (you'd reinstall from the Store), and major updates may reinstall the package — check after each feature update.
5. For most users Fix 2 or Fix 5 is sufficient — reserve uninstalling for cases where the package itself is corrupt and repair (Fix 6) failed.

## Closing

Widgets.exe burning CPU after an update is Windows re-enabling and breaking a feature you never asked for — the fix ranges from flipping the official toggle to Group Policy exile depending on how stubborn it is. There's no wrong answer here: calm it if you like glanceable weather, kill it if you don't. Either way, your idle CPU belongs to you again, not to a news feed refreshing in the dark.
