---
title: "NPU Usage High at Idle? Find and Stop the Culprit"
slug: npu-usage-high-idle
date: 2026-10-19
categories: ["ai-pc"]
tags: ["npu", "high usage", "idle", "copilot plus pc", "task manager"]
description: "NPU usage high at idle on your Copilot+ PC? Learn how to see what is using the NPU in Task Manager, why background AI spikes it, and how to calm it down."
thumbnail: "/images/thumbs/npu-usage-high-idle.webp"
faqs:
  - q: "How do I see NPU usage in Task Manager?"
    a: >
      Open Task Manager (Ctrl + Shift + Esc), go to the Performance tab, and look for the NPU entry in the left column (on Copilot+ PCs it appears alongside CPU, Memory, and GPU). Click it to see a live utilization graph. If there's no NPU entry, your laptop may not have one or its driver isn't installed.
  - q: "Is it normal for the NPU to spike occasionally at idle?"
    a: >
      Yes — brief spikes are normal. Windows runs periodic AI maintenance (index updates, model refreshes, Recall snapshot processing) that wakes the NPU for seconds or minutes. What's abnormal is sustained high usage (above ~30%) for tens of minutes while you're doing nothing.
  - q: "Can a virus use my NPU for crypto mining?"
    a: >
      In theory any compute can be abused, but NPU-targeting malware is essentially nonexistent in the wild — NPUs are poor mining hardware and hard to program maliciously. Sustained NPU usage at idle is overwhelmingly likely to be legitimate Windows AI features, not malware. Still, a Defender full scan is cheap reassurance.
  - q: "Does high NPU idle usage damage the chip?"
    a: >
      No. The NPU is designed for sustained inference and sips power doing it. High idle usage wastes battery and generates mild heat, but it won't harm the silicon. The fix is about battery life and quiet, not hardware preservation.
---

Task Manager's Performance tab has a new graph most owners ignore — until the day they notice the NPU sitting at 40% while the laptop does absolutely nothing. The Neural Processing Unit is supposed to be the efficiency hero of your Copilot+ PC, sipping power while it handles AI tasks. So why is it grinding away at idle?

Usually, it's Windows itself: background AI maintenance that never quite finishes. Recall processing its snapshot backlog, search indexing new files, a stuck Live Captions session, or an app that requested NPU time and never released it. Occasionally it's a misbehaving driver. This guide shows you how to see exactly what's using the NPU and shut down the offenders — plus how to tell the difference between normal background hum and a real problem. If your whole system feels slow (not just the NPU graph), [laptop slow when AI features are on](/articles/laptop-slow-when-ai-features-on/) is the broader guide; for battery impact specifically, see [AI features draining laptop battery](/articles/ai-features-draining-laptop-battery/).

And if the NPU's busy-ness comes with heat and noise, you're looking at [Copilot+ PC overheating](/articles/copilot-plus-pc-overheating/) territory. Let's first find out what's actually keeping your NPU awake.

## Why this happens

- **Recall backlog processing:** After updates or heavy use days, Recall chews through queued snapshots — sustained NPU activity until the backlog clears.
- **Search index churn:** Windows AI search re-indexes changed files in the background, spiking NPU usage in waves that look random.
- **Stuck app sessions:** An app (video call, transcription tool) can hold NPU resources after you close its window if its background process lingers.
- **Driver-level busy loops:** Buggy NPU drivers occasionally spin at high utilization doing nothing — a known issue fixed by driver updates.
- **Windows ML maintenance:** The OS periodically refreshes AI models and runs health checks, causing brief but noticeable spikes.
- **Multiple features stacking:** Recall + indexing + a lingering call effect can combine into sustained high usage no single feature would cause alone.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the NPU is really busy (and what's using it)

Task Manager shows the NPU graph, but attributing usage to processes takes one more step. Don't act on the graph alone.

1. Open Task Manager > Performance tab > click NPU in the left column to see the live graph.
2. Watch for 2–3 minutes: brief spikes are normal; sustained 30%+ at idle is not.
3. Switch to the Processes tab, sort by CPU — NPU-heavy processes often also show CPU activity.
4. Note the process names during spikes (Search Indexer, Recall, specific apps).
5. If usage is high only in the first 10 minutes after boot, that's normal startup activity — wait it out.

### Fix 2: Clear the Recall backlog

Recall is the most common sustained-NPU culprit. Its snapshot queue can take hours to drain after busy periods.

1. Open Settings > Privacy & security > Recall & snapshots.
2. Check storage usage — a large backlog means heavy background processing.
3. Click "Delete snapshots" to wipe the queue (this stops the processing immediately).
4. Toggle "Save snapshots" off temporarily if you want the NPU fully quiet.
5. Monitor the NPU graph for 10 minutes — it should settle to near-zero.

### Fix 3: Kill lingering app sessions

Apps don't always release the NPU when you close them. Their background processes keep inference sessions alive.

1. In Task Manager > Processes, look for video calling, transcription, or AI apps you thought you closed.
2. End those tasks (right-click > End task), including their background/helper processes.
3. Check the system tray for hidden app icons — right-click and fully quit them.
4. In Task Manager > Startup, disable AI apps you don't want auto-launching.
5. Re-test: close your usual apps one by one and watch which one drops the NPU graph.

### Fix 4: Update the NPU driver

Driver-level busy loops are real and documented — and fixed in newer driver releases. This is the fix when nothing in Task Manager explains the usage.

1. Open Device Manager > expand "Neural processors" (or "System devices").
2. Right-click the NPU device (Intel AI Boost / AMD / Qualcomm Hexagon) > Update driver.
3. Also run Windows Update with optional driver updates checked.
4. Check your OEM's support page ([Intel](https://www.intel.com/content/www/us/en/support/detect.html), [AMD](https://www.amd.com/en/support/download/drivers.html), or your laptop maker) for a newer NPU driver.
5. If high idle usage started right after a driver update, roll back: Properties > Driver > Roll Back Driver.

### Fix 5: Reduce background AI workload

If the NPU is legitimately busy (not a bug), reduce what Windows asks it to do in the background.

1. Set search indexing to Classic mode: Settings > Privacy & security > Searching Windows.
2. Exclude large, frequently-changing folders from indexing.
3. Disable Live Captions autostart and Studio Effects you're not actively using.
4. In Battery saver settings, enable automatic Battery saver — it throttles background AI.
5. For a full teardown of background AI, see [AI background processes in Windows 11](/articles/ai-background-processes-windows-11/).

### Fix 6: Rule out malware and reset if needed

It's unlikely, but cheap to rule out — and a reset is the definitive test for software-caused NPU churn.

1. Run a Windows Defender full scan: Windows Security > Virus & threat protection > Scan options > Full scan.
2. Check for unknown processes with high NPU-correlated CPU usage and research any you don't recognize.
3. Boot into Safe Mode — if NPU usage is normal there, a third-party app or driver is the cause.
4. Clean-boot (msconfig > selective startup) to isolate the offender systematically.
5. As a last resort, Settings > System > Recovery > Reset this PC (keep files) gives you a clean AI stack.

## Closing

High NPU usage at idle is almost never the chip's fault — it's Windows' background AI (usually Recall or indexing) or a stuck app session keeping it awake. Diagnose with Task Manager's NPU graph, clear the Recall backlog, kill lingerers, and update the NPU driver. Brief spikes are normal life on a Copilot+ PC; sustained high usage is a solvable software issue. If the NPU graph is calm but the laptop still runs hot and loud, the heat is coming from the CPU/GPU instead — and that's a cooling or workload question, not an NPU one.
