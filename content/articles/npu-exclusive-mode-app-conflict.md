---
title: "NPU Exclusive Mode App Conflict? Share Your AI Chip Safely"
slug: npu-exclusive-mode-app-conflict
date: 2026-10-22
categories: ["ai-pc"]
tags: ["npu", "app-conflict", "windows-11", "ai-pc", "directml", "troubleshooting"]
description: "Two apps fighting over your NPU in exclusive mode? Learn why NPU access conflicts happen and how to make AI apps share the chip without crashes or errors."
thumbnail: "/images/thumbs/npu-exclusive-mode-app-conflict.webp"
faqs:
  - q: "What is NPU exclusive mode?"
    a: >
      Exclusive mode is when one application takes sole ownership of the
      NPU, blocking every other app from using it. Some AI tools request
      it for maximum performance or determinism. The downside is obvious:
      anything else that needs the NPU fails until the first app releases
      the chip.
  - q: "Why does one app block others from using the NPU?"
    a: >
      Either the app explicitly requested exclusive access, or the NPU
      driver stack serialized access because the runtime could not share
      safely. Older runtimes and some vendor SDKs default to exclusive
      locks even when sharing would work fine.
  - q: "Can two AI apps really use the NPU at the same time?"
    a: >
      Usually yes, through shared or partitioned execution — Windows'
      DirectML path and modern vendor runtimes time-slice the NPU between
      sessions. True simultaneous heavy inference on both can slow each
      app down, but they should not crash or refuse to start.
  - q: "How do I find which app is hogging the NPU?"
    a: >
      Open Task Manager, go to Performance, click the NPU graph, and check
      per-process usage at the bottom. The process with sustained high NPU
      usage while others fail is your exclusive-mode holder. End it and
      retest the blocked app.
---

You are running a local LLM in one app, then open your video call software — and its AI background blur refuses to start, or the second app crashes outright. Or two creative tools both want the NPU and only the first one launched gets it. Your AI PC has a perfectly good neural processor, but the apps are fighting over it like there is only one chair.

This is the NPU exclusive-mode conflict: one application grabs sole ownership of the chip and everything else gets locked out. Sometimes the app genuinely needs exclusivity for performance; more often it is a default nobody changed, or a runtime that cannot share properly. If only one specific app never touches the NPU at all, the issue may instead be [apps not using NPU acceleration](/articles/app-not-using-npu-acceleration/) for configuration reasons — but when app B works fine until app A is running, you are looking at a sharing conflict.

The fixes below help you find the hog, switch apps to shared mode where possible, update the runtimes that handle sharing, and set up your workflow so your AI tools coexist. You should not have to close your AI assistant just to join a video call.

## Why this happens

- **App requests exclusive access by default:** Some AI tools and SDKs ask for the NPU in exclusive mode unless configured otherwise, locking out everything else.
- **Runtime cannot share sessions:** Older DirectML, OpenVINO, or vendor runtimes serialize NPU access — only one session runs at a time and others queue or fail.
- **Driver-level locking bugs:** Immature NPU drivers can fail to release the hardware lock when an app closes or crashes, leaving a "ghost" exclusive holder.
- **Two heavy models at once:** Even with sharing support, two large models can exhaust NPU memory, causing the second session to fail allocation and report a conflict.
- **Zombie background processes:** An app you thought you closed keeps a background worker alive, silently holding the NPU.
- **Conflicting vendor SDKs:** Mixing runtimes from Intel, AMD, or Qualcomm toolkits in one workflow can confuse the sharing layer and force exclusive fallbacks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find the app holding the NPU

You cannot fix a conflict without knowing who holds the lock, so identify the hog first.

1. Open Task Manager (Ctrl + Shift + Esc) and go to the Performance tab.
2. Click the NPU graph and look at per-process usage at the bottom of the pane.
3. The process with sustained NPU activity is your current holder — note its name.
4. In the Processes tab, end that task, then immediately launch the app that was being blocked.
5. If the blocked app now works, you have confirmed an exclusive-mode conflict rather than a broken app. Similar privacy-layer blocks can also stop AI features cold — see [fixing Click to Do privacy settings](/articles/click-to-do-privacy-settings-fix/) for a related permissions-side example.

### Fix 2: Switch the hogging app to shared mode

Many apps that grab the NPU exclusively have a setting to share — it is just not the default.

1. Open the settings or preferences of the app that was holding the NPU.
2. Look for options like "NPU mode," "execution provider," "exclusive access," "allow sharing," or "device priority."
3. Change exclusive/dedicated mode to shared, or pick a shared execution provider such as DirectML shared session if offered.
4. Restart the app and retest: launch it first, then the second app, and confirm both now run.
5. If the app has a config file or command-line flag for device sharing, set it there — check the app's documentation for the exact key.
6. When no sharing option exists, check for a newer app version; sharing support is frequently added in updates.

### Fix 3: Update runtimes to sharing-capable versions

Old runtimes are a leading cause of forced exclusive access — modern ones time-slice the NPU properly.

1. Identify which runtime the conflicting apps use: DirectML (Windows ML), OpenVINO (Intel), or a vendor SDK.
2. Install all pending Windows updates from Settings > Windows Update, since DirectML sharing improvements ship with the OS — background on [Microsoft's support site](https://support.microsoft.com/en-us/windows) covers the AI platform components.
3. On Intel machines, update OpenVINO or the Intel NPU driver via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
4. Update both conflicting apps to their latest versions so they bind to the newer runtime behavior.
5. Retest the two-app scenario after every update, changing only one thing at a time so you know what fixed it.

### Fix 4: Kill zombie processes and trim startup apps

Ghost processes from crashed or "closed" apps are a sneaky source of phantom exclusive locks.

1. In Task Manager's Details tab, sort by name and look for processes belonging to AI apps you are not actively using.
2. End any AI-related background workers, updaters, or tray helpers you do not need right now.
3. Open Settings > Apps > Startup and disable AI tools from auto-starting — launch them only when needed.
4. Check the system tray for minimized AI utilities holding the NPU and exit them fully (right-click > Exit, not just closing the window).
5. Retest your two-app workflow on this clean slate. This is the same hygiene that fixes [apps ignoring the NPU entirely](/articles/npu-not-used-by-apps-windows-11/), since stale sessions confuse the scheduler in both directions.

### Fix 5: Stagger heavy workloads and reduce NPU memory pressure

When both apps legitimately need the NPU at once, reducing each one's footprint lets sharing actually work.

1. In each app, lower the model size or precision if options exist (quantized models use far less NPU memory).
2. Close the heaviest AI app's model when idle — many apps keep models loaded "for speed" and offer an "unload when idle" setting.
3. Avoid starting two large models simultaneously; launch the second after the first finishes initializing.
4. If one app only needs the NPU briefly (background blur on a call), prefer it over a permanently loaded local LLM during the call.
5. As a practical pairing tip, [Studio Effects' eye-contact teleprompter mode](/articles/studio-effects-teleprompter-eye-contact/) is a light NPU workload that coexists fine with heavier apps once sharing works — use it to validate your fix.

### Fix 6: Clean-reinstall the NPU driver to clear lock bugs

If locks survive app restarts or appear with no visible holder, the driver itself may be mishandling session teardown.

1. In Device Manager, expand Neural processors, right-click your NPU, and choose Uninstall device, ticking "Attempt to remove the driver."
2. Restart — Windows will install a base driver; then install the latest OEM or vendor driver package fresh.
3. Restart again and test the exact two-app scenario that used to conflict.
4. If conflicts persist only with one specific app pair, report it to that app's developer with both app versions and your NPU driver version — include Task Manager screenshots showing the lock.
5. As a temporary workflow, use GPU or CPU execution in one of the two apps until the developer or driver fixes the sharing path.

## Closing

NPU exclusive-mode conflicts look dramatic — crashing apps, greyed-out features — but they almost always come down to one app's default, a stale runtime, or a zombie process holding a lock it should have released. Find the holder, switch it to shared mode, and keep your runtimes current, and your AI tools will coexist the way the hardware intended. If a single app never uses the NPU even alone, that is a different problem — start with our guide on [apps not using NPU acceleration](/articles/app-not-using-npu-acceleration/) instead.
