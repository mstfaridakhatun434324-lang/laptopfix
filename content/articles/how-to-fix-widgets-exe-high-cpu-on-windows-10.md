---
title: "Fix Widgets.exe High CPU on Windows 10"
slug: "how-to-fix-widgets-exe-high-cpu-on-windows-10"
date: 2026-09-19
categories: ["performance"]
tags: ["widgets.exe", "high cpu", "windows 10", "news and interests", "taskbar"]
description: "Widgets.exe using high CPU on Windows 10? This is usually the News and Interests feed refreshing. Learn how to calm it down or switch it off cleanly."
thumbnail: "/images/thumbs/how-to-fix-widgets-exe-high-cpu-on-windows-10.webp"
faqs:
  - q: "What is Widgets.exe on Windows 10?"
    a: "On Windows 10, Widgets.exe is the backend process for the News and Interests taskbar feed — the weather and headlines panel that slides out when you hover over the taskbar widget area. It periodically downloads articles, images, and weather data from Microsoft's content services. The process is legitimate and signed by Microsoft, but its scheduled background refreshes can consume surprising CPU on older laptops, which is why many users choose to disable it."
  - q: "Is it safe to disable Widgets.exe on Windows 10?"
    a: "Yes, completely safe. Widgets.exe powers only the optional News and Interests feed; disabling it removes the taskbar weather panel and nothing else. Windows, your apps, and updates all work exactly as before. If you ever miss the headlines feed, re-enabling it is a single toggle in the taskbar settings, so there is no risk in trying the disabled state for a week or two."
  - q: "Why does Widgets.exe use CPU even when I never open the feed?"
    a: "The feed refreshes on a schedule in the background regardless of whether you hover over it, downloading new stories, images, and location-based weather data every couple of hours. Each refresh cycle wakes the process, uses CPU to render content, and writes cache files to disk. Reducing the refresh behavior or disabling the feed entirely stops these background cycles and the CPU spikes that come with them."
  - q: "Can I remove Widgets.exe from Windows 10 completely?"
    a: "You cannot cleanly uninstall the underlying Web Experience Pack the way you remove a normal app, but you can disable the News and Interests entry point so the process never launches — which is effectively the same thing for CPU purposes. Turning it off in taskbar settings, optionally reinforced with a Group Policy or registry setting, means the executable simply never runs and never consumes resources."
---
Hover over the weather icon on your Windows 10 taskbar and a panel of news headlines slides out. That panel is powered by Widgets.exe, a background process that refreshes its feed every couple of hours — and on many laptops, each refresh brings a noticeable CPU spike, warmer fans, and a small but steady battery drain.

Most people never asked for the feed and never open it deliberately, yet it runs all day. On older dual-core laptops or machines already tight on resources, those background refresh cycles are genuinely felt: Task Manager shows Widgets.exe jumping to 15–30 percent CPU several times a day for no visible benefit.

The fix is straightforward because the feature is entirely optional. Below are the ways to calm it down — from reducing its refresh appetite to switching it off completely — ordered from least to most invasive. If startup bloat is a wider issue on your machine, our [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) covers the rest of the usual suspects.

## Why this happens

- **Scheduled feed refreshes:** the News and Interests panel downloads fresh stories, images, and weather data every few hours, each cycle spiking CPU.

- **Image-heavy content rendering:** thumbnail images and animated weather graphics cost far more CPU to decode than plain text.

- **Location services polling:** the weather widget repeatedly queries your location, waking radios and the process together.

- **Corrupted feed cache:** a damaged cache forces full re-downloads and re-renders instead of quick incremental updates.

- **Outdated Web Experience Pack:** bugs in older versions of the feed backend caused refresh loops that newer releases fixed.

- **Full-rate refresh on metered connections:** the feed keeps refreshing aggressively unless told the connection is metered.

- **Multiple signed-in users:** on shared PCs, each active user runs their own Widgets.exe instance, multiplying the background cost.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off News and Interests from the taskbar

This is the one-click fix that solves it for most people. Disabling the taskbar entry point stops the feed from loading, which means Widgets.exe has nothing to refresh and stays dormant.

1. Right-click an empty area of the taskbar.
2. Hover over News and interests in the context menu.
3. Select Turn off.
4. Open Task Manager and confirm Widgets.exe drops to zero CPU and eventually exits.
5. Live with it off for a day; if you miss the headlines, the same menu brings it back instantly.

### Fix 2: Reduce the feed's background activity instead

If you actually like glancing at headlines, you do not have to kill the feature — just make it less aggressive. Fewer refreshes and no hover-to-open behavior cut most of the background CPU while keeping the panel available on click.

1. Right-click the taskbar, go to News and interests, and choose Reduce taskbar updates.
2. In the same menu, uncheck Open on hover so the panel only opens when you click it.
3. Open the feed once, use the options on any story card to mute topics you never read.
4. Fewer followed topics means smaller refresh payloads and shorter CPU spikes.
5. Check Task Manager over the next day to confirm spikes are smaller and rarer.

### Fix 3: Clear the feed cache

A corrupted feed cache makes Widgets.exe work much harder than it should — re-downloading and re-rendering content that should have been cached. Clearing it forces a clean rebuild, and Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the general cache-clearing approach for built-in features.

1. End Widgets.exe in Task Manager (Details tab, right-click, End task) so no cache file is locked.
2. Press Win + R, type %localappdata% and press Enter, then look for Microsoft feed cache folders.
3. Delete the contents of the feed-related cache folders you find.
4. Also run Disk Cleanup (cleanmgr) and check Temporary files to sweep related caches.
5. Reopen the feed once to let it rebuild cleanly, then watch CPU behavior over the next refresh cycle.

### Fix 4: Update the Web Experience Pack and Windows

Microsoft ships feed improvements through the Windows Web Experience Pack in the Microsoft Store, and older versions had refresh bugs that caused exactly these CPU spikes. Updating is the lowest-effort fix if you want to keep the feature.

1. Open the Microsoft Store, click Library, and install all pending updates — especially Windows Web Experience Pack.
2. Then open Settings > Update & Security > Windows Update and install any pending Windows updates.
3. Restart the laptop so the new feed backend loads cleanly.
4. Monitor Widgets.exe in Task Manager across two or three refresh cycles.
5. If spikes persist after updating, disabling the feed (Fix 1) remains the reliable answer.

### Fix 5: Block it with Group Policy or Registry

For a permanent, update-proof disable — useful on a laptop you administer for someone else — policy or registry settings stop the feed at the source so Windows updates cannot quietly re-enable it.

1. On Pro editions: open gpedit.msc, go to Computer Configuration > Administrative Templates > Windows Components > News and interests, and enable the Turn off news and interests policy.
2. On Home editions: open regedit and navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Feeds.
3. Create a DWORD (32-bit) value named EnableFeeds and set it to 0 (create the Windows Feeds key first if it is missing).
4. Restart the laptop and confirm the taskbar option is gone and Widgets.exe never launches.
5. To reverse, set the policy to Not Configured or delete the registry value.

### Fix 6: Check for a runaway refresh loop

If Widgets.exe sits at high CPU constantly rather than in periodic spikes, something is looping — usually a stuck network request or a corrupted profile. A short diagnostic confirms it before you take heavier measures.

1. In Task Manager, watch Widgets.exe for ten minutes and note whether CPU ever drops near zero between spikes.
2. Constant high CPU with no idle gaps suggests a loop; periodic spikes are normal refresh behavior.
3. Sign out and back in, or test another user account, to see whether the loop follows your profile.
4. If it follows the profile, clearing the cache (Fix 3) plus installing Windows updates usually breaks the loop.
5. Our [Windows 11 Widgets guide](/articles/how-to-fix-widgets-exe-high-cpu-on-windows-11/) covers the newer board's quirks if you dual-boot or upgrade.

## Closing

Widgets.exe on Windows 10 is one of the easiest CPU hogs to beat because the feature behind it is purely optional. Turn off News and Interests from the taskbar and the process simply goes quiet — no registry surgery required for most users. Keep it disabled if you never read the feed; your CPU, fans, and battery will all thank you, and nothing else in Windows changes one bit.
