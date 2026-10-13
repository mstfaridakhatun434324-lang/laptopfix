---
title: "Fix Widgets.exe High CPU on Windows 11"
slug: "how-to-fix-widgets-exe-high-cpu-on-windows-11"
date: 2026-09-27
categories: ["performance"]
tags: ["widgets.exe", "high cpu", "windows 11", "widgets board", "msn feed"]
description: "Widgets.exe spiking CPU on Windows 11? Tame the Widgets board feed, stop its background refreshes, or remove it cleanly with these safe methods."
thumbnail: "/images/thumbs/how-to-fix-widgets-exe-high-cpu-on-windows-11.webp"
faqs:
  - q: "What is Widgets.exe in Windows 11?"
    a: "Widgets.exe is the backend process for the Windows 11 Widgets board — the panel that slides in from the left showing weather, news, stocks, sports, and calendar items. It fetches fresh content from Microsoft's MSN services on a schedule and renders the board's cards. The process is legitimate and signed by Microsoft. Its CPU usage comes from those scheduled content refreshes, which run whether or not you ever open the board."
  - q: "Why does Widgets.exe run if I never open the Widgets board?"
    a: "The board pre-fetches content in the background so it opens instantly when you click the taskbar widget or press Win + W. That means scheduled downloads, image decoding, and layout rendering happen on a timer regardless of your usage. Microsoft designed it for instant gratification; the cost is background CPU several times a day. Disabling the board or its refresh schedule stops the background work entirely."
  - q: "Is it safe to uninstall the Widgets feature?"
    a: "Yes. The Widgets board is an optional shell feature — removing or disabling it does not affect Windows stability, updates, notifications, or any application. The taskbar weather widget disappears along with the board, which most users consider a bonus. If you change your mind, reinstalling the Web Experience Pack from the Microsoft Store brings the whole feature back in minutes."
  - q: "Will disabling Widgets break the taskbar weather icon?"
    a: "The taskbar weather icon is part of the Widgets feature, so disabling the board removes the icon too — they cannot be separated through normal settings. If you love the at-a-glance weather but hate the CPU usage, the compromise is keeping the board enabled but reducing its refresh behavior and muting content topics. That cuts most background CPU while preserving the weather glance."
---
On Windows 11, Widgets.exe is hard to miss once you look: a process that periodically jumps to 15–35 percent CPU, spins up the fans, and then vanishes — several times a day, every day, whether you have ever opened the Widgets board or not. For a feature many users never asked for, it demands a surprising amount of attention from your processor.

The Widgets board lives to feel instant. To achieve that, Widgets.exe fetches news, weather, stocks, and sports content on a schedule, decodes images, and pre-renders cards in the background. Each refresh cycle is a burst of network, CPU, and disk activity — and on laptops already juggling real work, those bursts are felt as stutters, heat, and battery drain.

Because the feature is entirely optional, the fixes range from gentle (fewer refreshes, fewer topics) to absolute (removing the board completely). Work through them in order of aggressiveness and stop when Task Manager stays quiet. If background bloat is a wider theme on your PC, our [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) continues the cleanup.

## Why this happens

- **Scheduled MSN content refreshes:** the board downloads fresh cards every few hours, each cycle spiking CPU to decode and render.

- **Image and animation decoding:** weather animations and news thumbnails cost far more CPU than the text they accompany.

- **Location-based weather polling:** repeated location queries wake the process and the radio together.

- **Too many enabled widgets:** every active widget (stocks, sports, traffic, esports) adds its own refresh workload.

- **Corrupted board cache:** damaged cached content forces full re-downloads and re-renders instead of deltas.

- **Outdated Web Experience Pack:** older backend versions had refresh bugs that looped instead of completing.

- **Taskbar widget always animating:** the live taskbar weather widget re-renders continuously, not just during refreshes.

- **Multiple signed-in users:** each active user session runs its own Widgets.exe instance with its own refresh schedule.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Remove the Widgets entry point from the taskbar

Hiding the taskbar widget does not fully stop background refreshes on all builds, but on current Windows 11 it significantly reduces the board's activity — and it is the fastest first step.

1. Right-click the taskbar and choose Taskbar settings.
2. Toggle Widgets to Off.
3. Open Task Manager and watch Widgets.exe over the next few hours.
4. On many builds the process now stays dormant; if yours still spikes, continue below.
5. This step is instantly reversible from the same settings page.

### Fix 2: Declutter the board and mute topics

If you want to keep the board, shrink its appetite. Every widget you remove and every topic you mute reduces the size of each refresh payload — smaller downloads, less decoding, shorter CPU bursts.

1. Press Win + W to open the Widgets board.
2. Click the settings gear and remove every widget you never look at (stocks, sports, traffic).
3. Open any news card's menu and choose Manage interests to mute publishers and topics you ignore.
4. In board settings, turn off content personalization and notification badges if present.
5. Fewer cards means measurably smaller refresh cycles — verify in Task Manager over a day.

### Fix 3: Disable the board with Group Policy or Registry

For a durable disable that survives feature updates, policy is the answer. This stops the board — and its background refreshes — at the source, and Microsoft documents widget policy behavior on its [Windows support pages](https://support.microsoft.com/en-us/windows).

1. On Pro/Enterprise: open gpedit.msc and go to Computer Configuration > Administrative Templates > Windows Components > Widgets.
2. Enable the Allow widgets policy set to Disabled (the naming varies slightly by build — the effect is “widgets off”).
3. On Home: open regedit and navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Dsh.
4. Create a DWORD (32-bit) value named AllowNewsAndInterests and set it to 0 (create the Dsh key if missing).
5. Restart and confirm Widgets.exe never appears in Task Manager again.

### Fix 4: Uninstall the Web Experience Pack

The Widgets board ships as part of the Windows Web Experience Pack, a Store app you can remove cleanly. This is the closest thing to a true uninstall, and it is fully reversible through the Store.

1. Open Settings > Apps > Installed apps and search for Windows Web Experience Pack.
2. Click the three dots and choose Uninstall, then confirm.
3. Restart the laptop.
4. Verify in Task Manager that Widgets.exe is gone entirely — no process, no spikes.
5. To restore later, search Windows Web Experience Pack in the Microsoft Store and reinstall it.

### Fix 5: Use winget for a scriptable removal

If you manage several machines — or just prefer the terminal — winget removes the same package from an elevated prompt. Handy for setup scripts on fresh Windows 11 installs.

1. Open Terminal or PowerShell as administrator.
2. Run: winget uninstall "Windows Web Experience Pack"
3. Confirm the prompt and wait for the uninstall to complete.
4. Restart the laptop.
5. Check Task Manager to confirm the process is permanently gone.

### Fix 6: Update instead of removing (the keeper's path)

Prefer keeping the board? Then make sure its backend is current: Microsoft has fixed several Widgets.exe CPU bugs through Web Experience Pack updates, and running an old version is a common cause of abnormal spikes. Our [Widgets board guide](/articles/how-to-fix-widgets-board-high-cpu-windows-11-on-lenovo-laptop/) covers board-specific tuning in more depth.

1. Open the Microsoft Store > Library and install all updates, especially Windows Web Experience Pack.
2. Install pending Windows updates from Settings > Windows Update.
3. Restart so the new backend loads.
4. Monitor Widgets.exe across several refresh cycles for a day.
5. If spikes remain abnormal after updating, fall back to the disable options above — the feature is not worth the CPU.

## Closing

Widgets.exe is the easiest kind of CPU problem: an optional feature doing optional work on your processor's time. Declutter it, disable it, or uninstall its package — whichever matches how (little) you use the board — and the background spikes stop. Nothing else in Windows depends on it, so this is one fix you can apply with total confidence.
