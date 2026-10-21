---
title: "How to Fix Live Captions High Memory Usage in Windows 11"
slug: live-captions-high-memory-usage
date: 2026-10-21
categories: ["ai-pc"]
tags: ["live captions high memory", "livecaptions.exe memory", "captions ram usage", "windows 11 memory leak", "ai pc troubleshooting", "npu offload"]
description: "Fix live captions high memory usage in Windows 11 with six step-by-step methods covering process restarts, language trimming, NPU offload, and updates."
thumbnail: "/images/thumbs/live-captions-high-memory-usage.webp"
faqs:
  - q: "How much memory should live captions normally use?"
    a: >
      A healthy LiveCaptions process sits around 150 to 400 MB while actively transcribing. Sustained usage above 1 GB, or usage that climbs the longer captions run, points to a leak or a model stuck on the CPU.
  - q: "Why does live captions use more memory over time?"
    a: >
      The speech model accumulates session state as it transcribes, and a known leak pattern keeps memory that should be released between sessions. Restarting the captions process resets it back to baseline.
  - q: "Does the NPU reduce live captions memory usage?"
    a: >
      Yes. On Copilot+ PCs the NPU handles transcription with far less system RAM than CPU fallback. If captions are running on the CPU because the NPU driver is broken, memory usage climbs noticeably.
  - q: "Will turning off live captions free the memory immediately?"
    a: >
      Toggling captions off with Win+Ctrl+L should release most of the memory within seconds. If the LiveCaptions process keeps holding hundreds of megabytes, end it in Task Manager to force the release.
---

You open Task Manager and there it is: **LiveCaptions.exe** chewing through a gigabyte of RAM — sometimes more — just to put words on your screen. On an 8 GB laptop that is enough to make everything else stutter, and the longer captions run, the worse it gets.

Live captions load a full speech recognition model into memory, so some RAM use is the price of on-device transcription. But there is a line between normal and broken: a healthy session stays in the low hundreds of megabytes, while a leaking or CPU-fallback session climbs without stopping. The fixes below bring it back under control.

High memory use and battery drain often travel together — if your laptop also dies faster with captions on, read the [captions battery drain guide](/articles/live-captions-draining-battery/) alongside this one.

## Why this happens

- **Speech model stuck on the CPU:** When the NPU driver fails, transcription falls back to the CPU, which needs far more system RAM to hold the model and run inference.
- **Memory leak across sessions:** LiveCaptions.exe accumulates state the longer it runs and does not fully release it when you toggle captions off — a classic slow leak.
- **Multiple languages loaded:** Every installed caption language keeps its model data resident. Three languages loaded means roughly three times the baseline memory.
- **Corrupt model cache:** A damaged speech model can cause the loader to keep retrying allocations, ballooning memory with duplicate buffers.
- **Another listener doubling the load:** A second always-listening app — for example a malfunctioning [Copilot press-to-talk key that never releases the mic](/articles/copilot-press-to-talk-not-working/) — forces two speech engines to run at once.
- **Outdated build with known leak:** Some Windows builds shipped a LiveCaptions memory leak that Microsoft later patched; unpatched systems leak indefinitely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the LiveCaptions process to reset the baseline

If memory climbs the longer captions run, a restart is both the diagnosis and the treatment. It takes ten seconds and instantly shows you whether the problem is a leak (memory resets low) or a constant overhead (memory jumps right back).

1. Press **Ctrl+Shift+Esc**, find **LiveCaptions** under Processes, and note its current memory figure.
2. Right-click it and choose **End task**.
3. Press **Win+Ctrl+L** to relaunch captions and transcribe for five minutes.
4. Check Task Manager again — if memory is back near baseline, schedule a process restart whenever you take long caption breaks.

### Fix 2: Trim your caption languages down to one

Each extra language is another model sitting in RAM. Most people caption in exactly one language, so the others are pure overhead.

1. Open **Settings > Time & language > Language & region**.
2. Remove the speech components (or the full languages) you never caption in.
3. Keep only your primary caption language installed.
4. Restart captions and compare the new baseline memory in Task Manager.

### Fix 3: Get transcription back onto the NPU

This is the big one on Copilot+ PCs. CPU fallback is the single largest cause of abnormally high captions memory. A healthy NPU driver moves inference off the CPU and drops RAM use dramatically.

1. Open Device Manager and check your NPU entry for warning icons.
2. Install the latest chipset/NPU driver for your platform — AMD Ryzen AI owners can use [AMD's driver download page](https://www.amd.com/en/support/download/drivers.html).
3. Restart, launch captions, and watch Task Manager: NPU-offloaded sessions stay flat instead of climbing.
4. If the NPU entry is missing entirely, work through NPU driver repair before anything else.

### Fix 4: Stop captions from running when you do not need them

The simplest memory saver is not running the model at all. Many systems auto-start captions at login or leave them on for hours out of habit.

1. Press **Win+Ctrl+L** to toggle captions fully off when you finish a session — do not just minimize the box.
2. Check **Settings > Accessibility > Live captions** and turn off any auto-start option.
3. Make it a habit: captions on for the meeting, off afterwards.
4. Verify in Task Manager that LiveCaptions.exe actually exits when toggled off.

### Fix 5: Install the Windows updates that patch the leak

Microsoft has fixed LiveCaptions memory leaks in cumulative updates before. If your system is months behind, you may be running a known-leaky build for no reason.

1. Open **Settings > Windows Update** and install every pending update.
2. Check **Advanced options > Optional updates** for driver and preview fixes.
3. Restart, run captions for a typical session, and monitor memory over an hour.
4. If usage now stays flat, the update contained the fix — keep updates current going forward.

### Fix 6: Clear out competing background apps

Captions do not exist in a vacuum — every background app competes for the same RAM, and crashed apps can leave zombie processes behind. Heavy or misbehaving background apps amplify the problem: [Spotify crashing on ARM Windows](/articles/spotify-app-crashing-arm-windows/), for instance, can leave orphaned processes eating memory that captions then fight for.

1. In Task Manager's Processes tab, sort by memory and look for anything unexpectedly large.
2. End zombie or crashed app processes you are not using.
3. Check the **Startup apps** tab and disable anything that launches a listener or overlay you do not need.
4. Retest captions with a lean background and confirm total system memory stays comfortable.

## Closing

Live captions will always use some RAM — on-device speech recognition is genuinely heavy work — but it should stay in the low hundreds of megabytes, not climb into the gigabytes. Restart the process to clear leaks, keep one language installed, and above all make sure transcription runs on the NPU rather than falling back to the CPU. Do those three things consistently and captions stay light enough that you will forget they are even running in the background while you work, browse, join meetings, and watch videos.
