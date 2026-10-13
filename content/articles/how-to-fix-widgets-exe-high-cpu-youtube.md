---
title: "Widgets.exe High CPU? Calm Down the Windows 11 Widgets Board"
slug: how-to-fix-widgets-exe-high-cpu-youtube
date: 2026-09-01
categories: ["performance"]
tags: ["widgets.exe", "high cpu", "widgets board", "windows 11", "news feed"]
description: "Widgets.exe spiking CPU — often while watching YouTube or browsing? Disable the news feed, tame the Widgets board, or remove it cleanly."
thumbnail: "/images/thumbs/how-to-fix-widgets-exe-high-cpu-youtube.webp"
faqs:
  - q: "What is Widgets.exe and why is it running?"
    a: "Widgets.exe (formally Windows Web Experience Pack) powers the Widgets board — the panel that slides in from the left showing weather, news, stocks, and calendar. It is a web-based runtime, essentially a lightweight browser constantly refreshing content feeds. It runs at startup and in the background even if you never open the board, which is why it can consume CPU and network while you do unrelated things like watching YouTube."
  - q: "Why does Widgets.exe use CPU when I'm watching YouTube?"
    a: "Two compounding factors: the Widgets board's web runtime refreshes its feeds on timers regardless of what you're doing, and video playback already loads the CPU/GPU — the extra background work pushes a busy system over the edge into stutter. Users also conflate the two because Task Manager's CPU sort puts Widgets.exe near the browser during playback. Disabling the feed or the board removes the background contention."
  - q: "Will disabling Widgets break anything in Windows 11?"
    a: "No. The Widgets board is a standalone feature — disabling or uninstalling it doesn't affect the taskbar (beyond removing the weather/news button), Start menu, search, or notifications. The underlying Web Experience Pack can be safely removed; Windows Update may occasionally reinstall it, in which case you repeat the removal. Nothing you depend on lives inside the Widgets board."
  - q: "Is Widgets.exe a virus?"
    a: "The genuine Widgets.exe lives in C:\\Program Files\\WindowsApps\\MicrosoftWindows.Client.WebExperience_* with a Microsoft digital signature — verify via Task Manager > Open file location and the file's Properties > Digital Signatures tab. Malware rarely bothers impersonating this particular process, but any Widgets.exe running from another location (Temp, AppData) is suspicious and deserves a full Defender scan."
---

You open Task Manager because YouTube is stuttering, and there it is: **Widgets.exe**, burning 10-20% CPU while you watch a video. You never opened the Widgets board. You may not even know what the Widgets board *is*. Yet here it is, refreshing news headlines and weather animations in the background, stealing cycles from your video playback like a tab you never opened.

Widgets.exe is the runtime behind Windows 11's Widgets board — the slide-in panel of weather, news, stocks, and calendar cards. It's built on web technology, which means it behaves like a hidden browser: JavaScript timers, animated content, periodic feed refreshes, all running whether the board is visible or not. On a powerful desktop it's background noise; on a laptop with video playing, it's the straw that stutters the camel. Here's how to confirm it's the problem, neuter its feed, or remove it entirely.

## Why this happens

- **Feed refresh timers**: News, weather, and stocks refresh on schedules regardless of board visibility.
- **Animated web content**: The board's cards use animations and video thumbnails that consume CPU/GPU.
- **Startup launch**: Widgets.exe starts with Windows and stays resident all session.
- **Compounding with video playback**: Background web runtime + foreground video decode = contention on busy systems.
- **Memory-leaking web views**: Long sessions with the board open occasionally leak in the web runtime.
- **Network-triggered refresh storms**: Reconnecting to Wi-Fi or waking from sleep triggers bulk feed refreshes.
- **Taskbar widget button**: The weather/news taskbar widget keeps the runtime warm even with the board closed.
- **Update-reinstalled package**: Windows Update occasionally restores the Web Experience Pack after removal.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Widgets.exe is really the problem

Make sure the CPU blame is correctly assigned.

1. Open Task Manager > **Processes**, click **CPU** to sort, and watch during your typical trigger (YouTube playback, for example) — note Widgets.exe's sustained CPU, not just spikes.
2. Right-click Widgets.exe > **Open file location** — confirm it's under `C:\Program Files\WindowsApps\MicrosoftWindows.Client.WebExperience_*`. Anything else is suspicious.
3. Test causation: right-click Widgets.exe > **End task**, then immediately test your YouTube playback — if stutter vanishes, you've confirmed the link. (It will restart at next boot unless you apply the fixes below.)
4. Check the **Startup apps** tab for Widgets-related entries and the **App history** tab for cumulative CPU over time.
5. If ending the task doesn't change your symptom, the real hog is elsewhere — check the browser's own GPU process or see [Chrome high CPU fixes](/articles/how-do-i-fix-chrome-high-cpu-windows-11/) instead of fighting Widgets.

### Fix 2: Disable the Widgets board and taskbar button

Remove the UI; the runtime usually idles down with it.

1. Right-click the taskbar > **Taskbar settings** > turn **Widgets** **Off** — this removes the weather/news button that keeps the runtime active.
2. Open **Settings** > **Personalization** > **Taskbar** and confirm the Widgets toggle is off there too (same setting, two paths — verify both).
3. Press **Win + W** to confirm the board no longer opens.
4. Restart and check Task Manager: Widgets.exe should either not appear or sit at 0% CPU. The package still exists but has nothing to do.
5. This is the right stopping point if you *might* want widgets later — everything is reversible with one toggle. For the related board-specific variant, see [Widgets board high CPU fixes](/articles/how-to-fix-widgets-board-high-cpu-windows-11-on-dell-laptop/).

### Fix 3: Turn off the news feed and personalized content

If you want the weather widget without the CPU cost.

1. Open the Widgets board (**Win + W**), click your profile icon (top-right) > **Widget settings**.
2. Turn off **Show feeds** / news content options — the news feed's constant refresh is the hungriest part of the board; the static weather card costs almost nothing.
3. Disable **personalized ads/content** options in the same settings — personalization means more background data fetching.
4. Close the board and monitor Widgets.exe CPU for an hour of normal use — feed-disabled boards typically idle near zero.
5. This middle-ground suits users who like glancing at weather but don't need MSN headlines refreshing behind their YouTube videos.

### Fix 4: Uninstall the Web Experience Pack

The clean removal for people who never want it back.

1. Open **Settings** > **Apps** > **Installed apps**, search for **Windows Web Experience Pack**.
2. Click **...** > **Uninstall** and confirm. This removes Widgets.exe entirely — no board, no background runtime, no taskbar button.
3. Restart and verify in Task Manager that Widgets.exe is gone.
4. Note: major Windows updates sometimes reinstall it — if Widgets.exe mysteriously returns months later, check Installed apps and remove it again. It takes 30 seconds.
5. PowerShell alternative (for scripting across machines): `Get-AppxPackage *WebExperience* | Remove-AppxPackage` from an elevated prompt — same result.

### Fix 5: Block it with policy (enterprise/persistent)

For managed machines or update-proofing.

1. On Pro editions, `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Widgets** > **Allow widgets** = **Disabled**.
2. This is a machine policy — it survives the feature updates that reinstall the package, keeping the board dead even if the files return.
3. On Home edition, the registry equivalent: `reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Dsh" /v AllowNewsAndInterests /t REG_DWORD /d 0 /f` from an elevated prompt (this covers the news-and-interests taskbar integration that shares the runtime).
4. Verify after the next Patch Tuesday that the board stays dead — policy is the only method that reliably does.
5. Microsoft documents the Widgets policy in the Windows support hub for IT admins managing fleets.

### Fix 6: Fix the underlying contention (video stutter specifically)

If YouTube stutters even with Widgets tamed, the board was a contributor, not the cause.

1. In your browser, check **Task Manager** (Shift+Esc in Chrome) for the **GPU Process** — high GPU-process CPU during video means decode/contention issues, not Widgets.
2. Toggle browser hardware acceleration (**Settings** > **System** > **Use hardware acceleration when available**) — try both states; the right answer depends on your GPU driver.
3. Update the GPU driver cleanly: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or Intel via the [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
4. In YouTube, drop from 4K to 1440p as a test — if stutter vanishes, your GPU's video decoder (not CPU) is the bottleneck, and no background-process tweak will fix that.
5. Keep Widgets disabled anyway — even when it's not the primary cause, a background web runtime refreshing news during 4K playback is pure overhead you don't need.

## Closing

Widgets.exe high CPU is a background web runtime doing work nobody asked for, and the fix matches your tolerance: hide the button (Fix 2), kill the feed (Fix 3), uninstall the pack (Fix 4), or policy-block it (Fix 5). Any of them takes under five minutes. And if your real complaint was YouTube stutter, Fix 6 makes sure you don't stop at Widgets when the browser's GPU path needs attention too.
