---
title: "NPU Draining Battery? How to Stop High Power Usage"
slug: npu-high-power-usage-draining-battery
date: 2026-10-19
categories: ["ai-pc"]
tags: ["npu", "battery drain", "power usage", "windows 11", "copilot plus pc"]
description: "NPU high power usage draining your laptop battery? Find which AI features burn power and tame NPU consumption without losing Copilot+ features."
thumbnail: "/images/thumbs/npu-high-power-usage-draining-battery.webp"
faqs:
  - q: "Is it normal for the NPU to use battery?"
    a: "Yes, in small amounts — the NPU is actually more efficient than CPU/GPU for AI tasks. Abnormal drain means something is keeping AI workloads running constantly, like Recall snapshotting aggressively or a stuck background process."
  - q: "How much battery should the NPU use?"
    a: "Typically 1-3% of total drain during normal use. If Task Manager shows the NPU pegged at high utilization while you are doing nothing, that is the anomaly to fix."
  - q: "Does turning off Recall save battery?"
    a: "Yes, measurably. Recall's constant snapshotting and on-device AI processing is one of the heaviest NPU consumers. Disabling it is the single biggest battery saver among AI features."
  - q: "Can the NPU get stuck at high usage?"
    a: "Yes — buggy drivers or crashed AI services sometimes leave the NPU spinning at load with no visible app responsible. A driver reinstall or service restart clears it."
---

The NPU was supposed to *save* battery — that is the whole pitch, AI tasks done efficiently on dedicated silicon instead of the power-hungry CPU. So when your Copilot+ PC starts draining noticeably faster and Task Manager shows the NPU working hard while you are just reading email, something is wrong. Either a legitimate feature is overworking, or a stuck process has the NPU spinning with no purpose.

Before changing anything, get a baseline: open Task Manager, Performance tab, click the NPU entry, and watch utilization for a few minutes of idle time. Near-zero with occasional blips is normal. Sustained high usage is not. If you want the full picture of what your NPU can do when healthy, see [how to check NPU TOPS](/articles/how-to-check-npu-tops-windows-11/) — but for drain issues, the fixes below go straight at the consumers.

## Why this happens

- **Recall snapshotting constantly:** Recall captures and AI-processes screen snapshots every few seconds. On busy days this is the heaviest sustained NPU workload in Windows.
- **Stuck AI background service:** A crashed Windows AI service can leave the NPU at load indefinitely with no visible owner.
- **Live Captions always on:** Real-time transcription with translation is a continuous NPU workload — expensive if left running 24/7.
- **Buggy NPU driver:** Some driver versions fail to clock the NPU down at idle, burning power for nothing.
- **Third-party AI apps polling:** Apps with "AI features" sometimes hammer the NPU in the background even when you are not using them.
- **Windows Studio Effects left enabled:** Camera effects process every frame while any camera app is open — including ones you forgot about.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the actual consumer

Do not guess. Find what is using the NPU.

1. Task Manager, Performance tab, click NPU — note whether usage is constant or spiky.
2. Switch to the Processes tab, right-click column headers, and enable GPU engine / NPU columns if available; sort by NPU usage.
3. In Settings, Privacy & security, check which apps have camera/microphone access — Studio Effects consumers hide here.
4. Note the top consumers before changing anything, so you can measure improvement.

### Fix 2: Tame or disable Recall

Recall is the biggest lever.

1. Settings, Privacy & security, Recall & snapshots — check if Recall is saving snapshots.
2. Reduce snapshot frequency or pause saving during battery use.
3. If you do not use Recall, turn off "Save snapshots" entirely — this alone often restores hours of battery.
4. Delete old snapshots to stop background indexing of the backlog (Settings, Recall, Delete snapshots).
5. Our guide on [Recall using too much disk space](/articles/recall-using-too-much-disk-space/) covers the storage side of the same problem.

### Fix 3: Audit always-on AI features

Stack up the small consumers.

1. Turn off Live Captions when not needed (Win + Ctrl + L toggles it).
2. In Settings, Bluetooth & devices, Cameras — disable Windows Studio Effects for cameras you are not actively using.
3. Check Copilot settings for any "always listening" or background modes and disable them.
4. Review Startup apps (Task Manager, Startup apps) for AI utilities you do not recognize and disable them.
5. Re-measure NPU idle usage after each change to find your biggest saver.

### Fix 4: Update the NPU driver

Idle power bugs are frequently driver bugs.

1. Get the latest NPU/chipset driver from your OEM or chip vendor ([Intel](https://www.intel.com/content/www/us/en/support/detect.html), [AMD](https://www.amd.com/en/support/download/drivers.html)).
2. Install it and reboot — then watch Task Manager idle NPU usage for 10 minutes.
3. Compare against your Fix 1 baseline; a proper driver should idle near zero.
4. If a *new* driver caused the drain, [roll it back](/articles/npu-driver-rollback-windows-11/) — regressions happen.

### Fix 5: Restart stuck AI services

A wedged service keeps the NPU hot with no owner.

1. Open Services (Win + R, `services.msc`).
2. Look for Windows AI / machine learning related services; restart any that show odd states.
3. In Task Manager Details tab, sort by power usage and end clearly stuck AI host processes (they restart automatically).
4. Reboot if usage does not drop — a clean boot clears wedged driver states.
5. If the same service wedges repeatedly, note its name; it is a candidate for a bug report to Microsoft via Feedback Hub.

### Fix 6: Adjust power policy for the NPU

Cap how aggressively the NPU can run on battery.

1. Settings, System, Power & battery — set power mode to "Best power efficiency" on battery.
2. Device Manager, NPU Properties, Power Management — allow the computer to turn off the device to save power.
3. In advanced power settings, ensure PCI Express Link State Power Management is on (Maximum power savings) for battery.
4. Test: unplug, idle 15 minutes, compare battery drain rate to before.
5. Keep a "plugged in" profile with full AI performance — you only need the restrictions on battery.

## Closing

NPU battery drain is a configuration problem, not a hardware flaw — the silicon is efficient, but Windows' default AI feature set is enthusiastic. Identify the consumer, tame Recall and always-on features, keep the driver current, and the NPU returns to its intended role: sipping power instead of gulping it. If drain persists with the NPU idling near zero, the culprit is elsewhere — our [AI features battery drain guide](/articles/ai-features-draining-laptop-battery/) covers the broader picture.
