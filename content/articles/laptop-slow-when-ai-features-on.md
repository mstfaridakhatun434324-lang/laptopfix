---
title: "Laptop Slow When AI Features Are On? Fix the Slowdown"
slug: laptop-slow-when-ai-features-on
date: 2026-10-19
categories: ["ai-pc"]
tags: ["ai features", "slow laptop", "copilot plus pc", "performance", "windows 11"]
description: "Laptop slow when AI features are on? Diagnose which Windows 11 AI services hog CPU and memory, then restore full speed without disabling everything you use."
thumbnail: "/images/thumbs/laptop-slow-when-ai-features-on.webp"
faqs:
  - q: "Why does my fast laptop feel slow with AI features enabled?"
    a: >
      AI features compete for CPU, memory, and disk alongside your apps. Recall's snapshot processing, background indexing, and Live Captions transcription all consume resources continuously. On paper the NPU offloads AI work, but the surrounding CPU/memory/disk activity still slows everything else down.
  - q: "Is it the NPU or the CPU causing the slowdown?"
    a: >
      Usually the CPU, RAM, and disk — not the NPU itself. The NPU is efficient, but AI features also need CPU orchestration, memory for models, and disk I/O for snapshots and indexes. Task Manager will show you: if CPU or disk is pegged by AI processes, that's your bottleneck.
  - q: "Will disabling AI features make my laptop fast again?"
    a: >
      If AI background work is the cause, yes — often dramatically. But verify first: if the laptop is slow with AI features already off, the problem is elsewhere (startup bloat, thermal throttling, failing storage). Diagnose before you disable.
  - q: "Do AI features slow down gaming?"
    a: >
      They can. Background AI tasks steal CPU cycles and memory bandwidth that games need, causing stutters. For gaming sessions, close Copilot, pause Recall snapshots, and disable Live Captions — or use Game Mode, which deprioritizes background work automatically.
---

Your laptop benchmarks like a rocket but feels like it's wading through mud — but only sometimes. The pattern: it's fine after a reboot, then gradually gets sluggish as the day wears on. If that sounds familiar, Windows 11's AI features are prime suspects. They're designed to be invisible, which makes them the perfect invisible culprit.

Here's the mechanism: features like Recall, AI search indexing, and Live Captions don't just use the NPU — they generate constant CPU, memory, and disk activity around it. Snapshot encoding, index merging, model loading — all of that competes with your actual work. The slowdown is real, measurable, and fixable. If battery drain is your bigger complaint than speed, start with [AI features draining laptop battery](/articles/ai-features-draining-laptop-battery/) instead — same culprits, different lens.

This guide shows you how to prove AI features are the cause (not just suspect them) and then surgically fix the slowdown. If you'd rather just turn the whole AI stack off, [turn off AI features in Windows 11](/articles/turn-off-ai-features-windows-11/) is the quick path. And if Task Manager shows the NPU itself pinned, [NPU usage high at idle](/articles/npu-usage-high-idle/) digs into that specific symptom.

## Why this happens

- **Recall's snapshot pipeline:** Capturing, encoding, and AI-analyzing screen snapshots every few seconds creates sustained CPU and disk load.
- **Index merging churn:** Windows AI search constantly merges new index data in the background, spiking disk I/O for minutes at a time.
- **Model loading stalls:** When an AI feature first activates, loading its model into memory can freeze the system briefly — then it repeats after updates.
- **Memory pressure:** AI models and snapshot caches consume gigabytes of RAM, pushing other apps into the pagefile on 16GB machines.
- **Competing with foreground apps:** Background AI tasks don't always yield politely; a Recall encoding burst during a game or compile causes visible stutters.
- **First-week indexing storm:** New laptops and fresh Windows installs index everything at once — the worst slowdowns happen in the first days of ownership.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Prove AI features are the cause

Never "fix" by randomly disabling things. Confirm the diagnosis with Task Manager so your effort lands on the real culprit.

1. When the laptop feels slow, open Task Manager (Ctrl + Shift + Esc) > Processes, sorted by CPU.
2. Look for AI-related processes: Recall snapshots, Search Indexer, LiveCaptions, Copilot background tasks.
3. Check the Memory and Disk columns too — AI features often bottleneck disk, not CPU.
4. Note the correlation: does slowness coincide with high usage by these processes? That's your proof.
5. If no AI process is active during slowdowns, stop here — your problem is elsewhere (startup apps, thermals, storage).

### Fix 2: Pause Recall during work hours

Recall is the heaviest continuous AI workload. You don't have to kill it forever — pausing it when you need speed is often enough.

1. Open Settings > Privacy & security > Recall & snapshots.
2. Toggle "Save snapshots" off during demanding work, back on later if you value the timeline.
3. Alternatively, use the system tray Recall icon to pause snapshots for a set period.
4. Delete old snapshots to reduce the background processing queue.
5. Observe for a day — if responsiveness returns, you've found your main offender.

### Fix 3: Defer indexing to idle time

Search indexing is necessary but doesn't need to run while you're working. Windows lets you schedule its aggression.

1. Go to Settings > Privacy & security > Searching Windows.
2. Turn off "Enhanced" mode if on — Classic indexes less and churns less.
3. Exclude huge folders (media libraries, code repos, game installs) from indexing.
4. In Indexing Options (Control Panel) > Advanced, you can rebuild a corrupted index that loops endlessly.
5. Let the laptop sit plugged in and idle for a few hours to let indexing finish its backlog.

### Fix 4: Close Copilot and Live Captions when not in use

These are the AI apps people leave running out of habit. They're cheap individually but add up, and closing them is instant relief.

1. Fully quit the Copilot app (not just minimize) when you're not using it — check the system tray.
2. Toggle Live Captions off with Win + Ctrl + L the moment a call or video ends.
3. Remove Copilot from Startup apps (Task Manager > Startup) so it doesn't preload.
4. Disable Studio Effects in camera settings when not on calls.
5. Make "close AI apps after use" a habit for a week and compare the feel.

### Fix 5: Free up memory headroom

AI features plus modern apps on 16GB RAM is a tight fit. Memory pressure makes everything — AI or not — feel slow.

1. In Task Manager > Performance > Memory, check if you're consistently above 85% usage.
2. Close browser tabs aggressively — browsers are the other great memory hog.
3. Disable unnecessary Startup apps to reclaim RAM from boot.
4. If you're perpetually maxed, consider whether your next laptop needs 32GB — AI workloads are only growing.
5. As a stopgap, increase the pagefile: System > Advanced > Performance Settings > Advanced > Virtual memory.

### Fix 6: Use Game Mode and Focus sessions for demanding work

Rather than permanently disabling AI, let Windows deprioritize background work when it matters.

1. Enable Game Mode: Settings > Gaming > Game Mode — it throttles background tasks during games.
2. For creative work, close AI apps manually before starting (Game Mode doesn't cover everything).
3. Use Focus sessions (Clock app) to signal "don't disturb" — some background AI activity pauses.
4. Plug in for heavy tasks — Windows is less aggressive about background work on AC power, paradoxically making foreground apps smoother.
5. After the demanding session, re-enable whatever AI features you value.

## Closing

A laptop that's slow "only sometimes" is usually a laptop doing invisible work — and on Copilot+ PCs, that work is often AI-related. Diagnose with Task Manager, then target the actual hogs: Recall snapshots, runaway indexing, and always-on Live Captions. You don't have to choose between AI features and speed — scheduled, selective use gives you both. If the machine is slow even with every AI feature disabled and a clean Task Manager, look at thermals, startup bloat, or storage health next; the AI was a red herring.
