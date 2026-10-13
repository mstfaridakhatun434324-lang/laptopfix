---
title: "Widgets Board High CPU on Your Lenovo Laptop? Shut It Down"
slug: how-to-fix-widgets-board-high-cpu-windows-11-on-lenovo-laptop
date: 2026-09-04
categories: ["performance"]
tags: ["widgets board", "high cpu", "lenovo laptop", "windows 11", "news and interests"]
description: "Widgets Board spiking CPU on your Lenovo laptop? Stop the news feed's background churn and reclaim your battery and performance."
thumbnail: "/images/thumbs/how-to-fix-widgets-board-high-cpu-windows-11-on-lenovo-laptop.webp"
faqs:
  - q: "What is the Widgets Board and why does it use CPU?"
    a: "The Widgets Board is the slide-out panel behind the taskbar Widgets button — weather, news, stocks, sports, and calendar cards powered by MSN content. It keeps background processes (Widgets.exe) alive to refresh feeds, download images, and pre-render cards even when you never open it. On some systems, aggressive refresh cycles, animated content, or a stuck feed download loop pins CPU and network, which is why never-opened Widgets can still cost you battery."
  - q: "Will I lose the weather widget if I disable Widgets?"
    a: "Disabling the Widgets board removes the taskbar entry point and its background processes, so the weather display on the taskbar goes away too. You lose nothing else — no apps, files, or settings depend on it. If you like glanceable weather, the free MSN Weather app or any weather app provides the same data without the full board's background churn. Most users never miss the board itself."
  - q: "Why is Widgets CPU usage worse on Lenovo laptops?"
    a: "It is not the Lenovo hardware — it is the software stack competing for resources. Lenovo ships Vantage, LegionZone or IdeaCentre utilities, and update agents that already consume background CPU; the Widgets feed's constant network and rendering activity stacks on top. Lenovo laptops also aggressively tune for battery life, so any background churn is more visible in battery drain. The Widgets board behaves the same on all brands — it is just more noticeable here."
  - q: "Can I keep Widgets but make it use less CPU?"
    a: "Partially. You can remove every news and content widget, leaving only weather and calendar, which cuts feed downloads dramatically. You can also disable the board's auto-open on hover so it never renders unexpectedly. But the background Widgets.exe processes still run and refresh on their schedule. If CPU usage stays high after stripping the board to essentials, full disable is the only reliable fix — there is no granular refresh-rate control."
---

Here is a special kind of absurdity: a feature you have never opened, consuming CPU like it is rendering video. The Windows 11 Widgets Board — that news-and-weather panel behind the taskbar button — keeps background processes churning through feed refreshes, image downloads, and card pre-rendering around the clock. On Lenovo laptops, where every background watt shows up in battery life, users are often shocked to find Widgets.exe among their top CPU consumers.

The board is optional in every sense: nothing in Windows depends on it, and its content is a duplicate of what browsers and apps already provide. This guide strips it down in stages — first the content diet, then the auto-open behavior, then the full disable — plus the Lenovo-specific background cleanup that makes the difference stick. For the broader slowdown picture, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/); to audit everything launching at boot, read [disabling startup programs in Windows 11](/articles/how-to-disable-startup-programs-windows-11/).

## Why this happens

- **Constant MSN feed refreshes**: News, stocks, and sports cards poll for fresh content on aggressive schedules, each refresh costing CPU and network.
- **Image and video preloading**: The board downloads and decodes thumbnails and animated content in the background so cards appear instant.
- **Widgets.exe kept alive permanently**: Background processes stay resident even when the board is never opened, refreshing on timers.
- **Animated and auto-playing card content**: Certain cards include animations or video snippets that render continuously while the board process runs.
- **Stuck or looping feed download**: A failing content endpoint can send the fetcher into retry loops that pin CPU indefinitely.
- **Hover-to-open triggering renders**: The default hover behavior opens and renders the board accidentally, spiking CPU on every accidental brush.
- **Stacking with Lenovo background utilities**: Vantage, update agents, and Lenovo telemetry already use background CPU; Widgets churn adds to an already-busy background.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Widgets is the actual culprit

Verify before disabling — background CPU has many suspects and you want the right one.

1. Open **Task Manager** > **Processes**, sort by CPU, and look for **Widgets** or **Widgets.exe** entries during the high-CPU periods.
2. Check **Task Manager** > **App history** over a few days to see Widgets' cumulative CPU time — background churn shows up clearly there.
3. In **Settings** > **System** > **Power & battery** > **Battery usage**, check whether Widgets appears among notable battery consumers.
4. Correlate timing: does CPU spike even with no apps open and the board never opened? That is the background refresh signature.
5. If Widgets is innocent, stop here and pursue the general high-Credit-CPU guide instead of disabling a feature for nothing.

### Fix 2: Put the board on a content diet

Less content means fewer refreshes, fewer downloads, and less rendering — try the gentle fix first.

1. Open the Widgets board (Win+W), click your profile icon or the settings gear, and remove every news, stocks, sports, and entertainment widget.
2. Keep only essentials like Weather and Calendar — static, low-refresh cards that cost almost nothing.
3. Turn off **Show notification badges** and any rotating or personalized content options in the board settings.
4. Disable **Allow widgets to show personalized ads** or similar content-personalization toggles if present.
5. Monitor Task Manager for a day — many users see Widgets CPU collapse after the content purge alone.

### Fix 3: Disable hover-to-open and taskbar presence

Stop the board from rendering unexpectedly and remove its constant taskbar footprint.

1. Right-click the taskbar > **Taskbar settings** and toggle **Widgets** off — this removes the button and its glanceable content.
2. Open the Widgets board settings and disable **Open Widgets board on hover** so accidental brushes never trigger a render.
3. In **Settings** > **Personalization** > **Taskbar**, confirm no Widgets-related entries remain enabled.
4. Restart Explorer (Task Manager > **Windows Explorer** > **Restart**) to ensure the taskbar change takes full effect.
5. Watch for a day: with no button and no hover-open, background activity should be the only remaining cost.

### Fix 4: Quiet Lenovo's own background stack

Lenovo utilities are the other half of the background-CPU equation on these machines.

1. Open **Lenovo Vantage** > **Settings** and disable automatic checkups, telemetry uploads, and aggressive background scanning schedules.
2. Check **Lenovo System Update** scheduling — set it to manual or monthly rather than frequent automatic checks.
3. In **Task Manager** > **Startup apps**, disable Lenovo utilities you never open (keep Vantage itself if you use battery/thermal controls).
4. Review **Task Scheduler** for Lenovo tasks running every few minutes and relax the chatty ones to daily.
5. Re-measure total idle CPU — the combination of a slimmed Widgets board and calmed Lenovo agents is often transformative.

### Fix 5: Disable the Widgets board completely

When the diet did not work, remove the feature. Nothing in Windows depends on it.

1. Right-click the taskbar > **Taskbar settings** > toggle **Widgets** **Off** (if not already done in Fix 3).
2. Open **Settings** > **Apps** > **Installed apps**, find **Windows Web Experience Pack** (the Widgets backend), and uninstall it if the option is available.
3. Alternatively, use Group Policy (Pro) or the registry: set `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Dsh` > DWORD **AllowNewsAndInterests** = 0.
4. Reboot and confirm no Widgets.exe processes appear in Task Manager after 10 idle minutes.
5. Your weather glance is gone from the taskbar — replace it with any weather app if you miss it; the CPU savings are permanent.

### Fix 6: Block its network and background permissions

Belt and suspenders: even disabled components sometimes leave scheduled tasks or background permissions behind.

1. Go to **Settings** > **Apps** > **Installed apps** > **Widgets** (or Web Experience Pack) > **Advanced options** and set **Background apps permissions** to **Never**.
2. Set **Let this app run in background** style toggles off wherever the Widgets-related entries expose them.
3. In **Task Scheduler**, look under **Microsoft** > **Windows** for Widgets-related refresh tasks and disable them.
4. Check **Settings** > **Privacy & security** > **Background apps** for any MSN/content-delivery entries and disable them.
5. Verify with a full idle hour in Task Manager: Widgets should now be entirely absent from CPU, disk, and network columns.

### Fix 7: Reinstall the Web Experience Pack if you want it back healthy

Sometimes the goal is not removal but a healthy Widgets board — a corrupted install causes the worst CPU behavior.

1. Uninstall **Windows Web Experience Pack** via **Settings** > **Apps** > **Installed apps** as in Fix 5.
2. Open the **Microsoft Store**, search for **Windows Web Experience Pack**, and reinstall it fresh.
3. Re-enable the taskbar Widgets toggle, open the board once, and immediately apply the Fix 2 content diet before it builds bad habits.
4. If CPU spikes return instantly on the fresh install, the problem is environmental (network/proxy issues with MSN endpoints) rather than corruption.
5. In that case, accept the disable — check [Lenovo's support pages](https://support.lenovo.com/us/en/) for any known software conflicts on your model, and enjoy the quieter machine.

## Closing

The Widgets Board is a content billboard that charges you CPU rent whether you look at it or not. On a Lenovo laptop where battery and thermals matter, that rent is too high for content you never asked for. Diet it, hide it, or remove it — any of the three beats letting a news feed you never open decide how hot your laptop runs.
