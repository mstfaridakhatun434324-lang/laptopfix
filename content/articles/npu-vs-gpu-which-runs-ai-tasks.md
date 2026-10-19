---
title: "NPU vs GPU: Which Actually Runs Your AI Tasks?"
slug: npu-vs-gpu-which-runs-ai-tasks
date: 2026-10-19
categories: ["ai-pc"]
tags: ["npu vs gpu", "ai tasks", "windows 11", "copilot plus pc", "hardware"]
description: "NPU vs GPU: which runs AI tasks on your laptop? Learn when the NPU wins on efficiency and when the GPU's raw power is the right choice."
thumbnail: "/images/thumbs/npu-vs-gpu-which-runs-ai-tasks.webp"
faqs:
  - q: "Is the NPU faster than the GPU for AI?"
    a: "Rarely in raw speed — a discrete GPU usually wins benchmarks. The NPU wins on efficiency: it does everyday AI tasks at a fraction of the power, which is why laptops route background AI there."
  - q: "Can the GPU do everything the NPU does?"
    a: "Functionally yes, but at much higher power draw. Some Copilot+ features are also gated to NPU hardware by Microsoft regardless of GPU capability, so the GPU cannot substitute for certification purposes."
  - q: "Why do laptops have both?"
    a: "They serve different jobs: the NPU handles always-on, low-power inference (effects, captions, indexing), while the GPU tackles burst-heavy work (gaming, rendering, large models). Together they cover the full range efficiently."
  - q: "How do I know which one an app is using?"
    a: "Task Manager's Performance tab shows both GPU and NPU graphs. Run the app's AI feature and watch which graph moves — that is your answer."
---

Your laptop has three processors that can run AI: CPU, GPU, and the new NPU. When you enable an AI feature, which one actually does the work — and does it matter? It matters a lot for battery life, and sometimes for whether the feature works at all. This guide maps each AI workload to its natural home so you can understand, predict, and occasionally control the routing.

If your NPU is detected but [apps are not using it](/articles/npu-not-used-by-apps-windows-11/), that is a routing problem worth fixing first — the theory below assumes a working NPU.

## Why this happens

- **Efficiency vs speed:** The NPU is built for maximum AI work per watt; the GPU for maximum AI work per second.
- **Battery impact:** NPU-routed AI can run for hours; the same work on GPU drains the battery visibly faster.
- **Feature gating:** Microsoft gates Copilot+ exclusives to NPU hardware — GPU power does not unlock them.
- **Thermal headroom:** The NPU sips power and stays cool; sustained GPU AI work heats the whole chassis.
- **App defaults vary:** Many apps default to GPU simply because GPU paths are older and better tested.
- **No universal "best":** The right processor depends entirely on the workload's shape.

## How to fix it

Work through these in order — understand first, then act.

### NPU wins: always-on and background AI

The NPU's home turf is continuous, lightweight inference.

1. Windows Studio Effects (background blur, eye contact) — designed for NPU, runs for hours in meetings.
2. Live Captions with translation — real-time transcription sips NPU power.
3. Recall snapshotting and indexing — constant background NPU work by design.
4. Camera and audio enhancement in calls — the NPU handles these while the CPU stays free.
5. Rule of thumb: if it runs all day in the background, it belongs on the NPU.

### GPU wins: burst-heavy creative AI

When raw throughput matters more than efficiency.

1. Local large language models (7B+ parameters) — GPUs handle the memory bandwidth these need.
2. AI image generation (Stable Diffusion and kin) — massively parallel, GPU territory.
3. Video upscaling and AI rendering — throughput-bound workloads favor GPU cores.
4. Batch photo processing with AI filters — faster on GPU, worth the power when plugged in.
5. Rule of thumb: if it is a "job" you start and wait for, the GPU usually finishes first.

### CPU's remaining role

Do not forget the oldest processor.

1. Small, infrequent AI tasks often just run on CPU — the overhead of waking the NPU is not worth it.
2. Apps without NPU or GPU paths fall back to CPU automatically.
3. CPU is the compatibility baseline: everything runs there, just slower and hotter.
4. If both NPU and GPU are busy, the CPU absorbs overflow.

### How to check and influence routing

See which chip does what, and nudge it.

1. Task Manager, Performance tab — watch NPU and GPU graphs during the workload.
2. In the app's settings, look for AI processor / hardware acceleration options and choose explicitly.
3. Settings, System, Display, Graphics — per-app GPU preference can steer work toward or away from the GPU.
4. On battery, prefer NPU routing for anything continuous; on AC, let speed win.
5. If the NPU graph never moves during AI work, revisit [NPU detection](/articles/check-if-laptop-has-npu/) — a missing NPU forces everything onto GPU/CPU.

### When the wrong chip is chosen

Fix misrouting.

1. App using GPU for background effects? Check its settings for an NPU/efficiency option.
2. App ignoring a working NPU? Update the app — NPU paths arrive in newer versions.
3. Update the NPU driver — apps check driver capabilities before routing.
4. Some misrouting is a Windows power-policy decision; test on Best performance mode.
5. Accept that a few apps will always prefer GPU — their developers optimized that path first.

### What your TOPS rating tells you

Your NPU's rated throughput frames the whole comparison.

1. Check your NPU's TOPS — 40+ is the Copilot+ bar; below that, the NPU handles light tasks while heavier AI leans on GPU.
2. A 45-TOPS Hexagon or 50-TOPS Ryzen AI NPU covers all Windows AI features comfortably; an 11-TOPS first-gen Core Ultra NPU is more limited.
3. Do not compare NPU TOPS directly with GPU TFLOPS — different precisions and architectures make the numbers non-comparable.
4. Judge by outcomes: smooth Studio Effects and all-day Recall mean your NPU is sufficient regardless of the spec sheet.

## Closing

NPU versus GPU is not a contest with one winner — it is a division of labor. The NPU owns efficient, always-on AI; the GPU owns heavy, bursty AI; the CPU catches the rest. Knowing which workload belongs where lets you read Task Manager like a dashboard, choose the right settings, and understand why your Copilot+ laptop behaves the way it does. When the routing looks wrong, the fix is usually an app setting or a driver update away — and note that a bad OS update can scramble this routing entirely, as we cover in our [24H2 NPU incompatibility guide](/articles/npu-driver-incompatible-windows-11-24h2/). When in doubt, let efficiency win on battery and speed win on AC power.
