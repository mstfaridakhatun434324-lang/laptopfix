---
title: "How to Check NPU TOPS in Windows 11 (3 Easy Ways)"
slug: how-to-check-npu-tops-windows-11
date: 2026-10-19
categories: ["ai-pc"]
tags: ["npu tops", "windows 11", "task manager", "ai pc", "check npu"]
description: "How to check NPU TOPS in Windows 11? Three quick ways to see your AI chip's trillions of operations per second and confirm Copilot+ readiness."
thumbnail: "/images/thumbs/how-to-check-npu-tops-windows-11.webp"
faqs:
  - q: "What does TOPS mean for an NPU?"
    a: "TOPS stands for trillions of operations per second — the standard measure of AI accelerator throughput. Higher TOPS means the NPU can run larger AI models faster. Microsoft requires 40+ TOPS for Copilot+ PC certification."
  - q: "How many TOPS does my NPU need for Copilot+ features?"
    a: "Microsoft's Copilot+ bar is 40 NPU TOPS. Snapdragon X Elite (45 TOPS), AMD Ryzen AI 300 (50 TOPS), and Intel Core Ultra Series 2 (48 TOPS) clear it; first-gen Core Ultra (11 TOPS) does not."
  - q: "Why doesn't Task Manager show my NPU's TOPS?"
    a: "Task Manager shows live NPU utilization but not the TOPS rating. For the rated figure, check your processor's spec page or use the methods in this guide."
  - q: "Is a higher TOPS always better?"
    a: "For raw AI throughput, yes — but real-world benefit depends on software using the NPU. A 45-TOPS chip with no supported apps performs no AI work at all, which is why [apps not using the NPU](/articles/npu-not-used-by-apps-windows-11/) is worth checking too."
---

TOPS — trillions of operations per second — is the horsepower rating of the AI era. It tells you how much AI math your NPU can chew through, and it is the number Microsoft uses to decide whether your laptop earns the Copilot+ badge (40 TOPS minimum). But Windows 11 does not put this number anywhere obvious, which sends owners hunting through spec sheets.

The good news: you can confirm your NPU's TOPS three ways, from a 30-second check to a definitive measurement. If your NPU is not detected at all, fix that first with our [NPU detection guide](/articles/npu-not-detected-windows-11/) — TOPS only matters once the chip is visible.

## Why this happens (why the number is hard to find)

- **Windows shows utilization, not rating:** Task Manager's NPU graph shows live activity percentage, never the chip's rated TOPS.
- **Marketing vs silicon:** "AI laptop" branding rarely prints TOPS; vendors advertise features, not the metric.
- **Three vendors, three disclosures:** Intel, AMD, and Qualcomm each publish TOPS differently — some per NPU, some whole-SoC.
- **Driver-dependent reporting:** Some detection tools only report TOPS when the correct NPU driver is installed.
- **TOPS inflation confusion:** Vendors sometimes quote combined CPU+GPU+NPU TOPS, which is not the NPU figure Microsoft cares about.
- **No built-in Windows tool:** Unlike `dxdiag` for GPUs, Windows ships no NPU spec reporter.

## How to fix it (find your number)

Work through these in order — diagnose first, then act.

### Fix 1: Check Task Manager for the NPU (30-second check)

The fastest confirmation that an NPU exists and is working.

1. Press Ctrl + Shift + Esc to open Task Manager.
2. Click the Performance tab and look for an "NPU" entry in the left list.
3. Click it — you will see live utilization, though not the TOPS rating.
4. No NPU entry? Your chip may lack one — verify with our [check-if-your-laptop-has-NPU guide](/articles/check-if-laptop-has-npu/).
5. If the entry exists but is greyed out, see [AI Boost greyed out in Task Manager](/articles/ai-boost-greyed-out-task-manager/).

### Fix 2: Look up your processor's official spec

The authoritative source for the rated figure.

1. Find your exact processor: Win + R, `msinfo32`, note the full model name.
2. Intel: search Intel ARK for your Core Ultra model — the spec page lists "NPU TOPS" (e.g., 11 TOPS for Series 1, 48 for Series 2).
3. AMD: check AMD's Ryzen AI processor page — XDNA NPU figures are listed (e.g., 50 TOPS for Ryzen AI 300).
4. Qualcomm: Snapdragon X Elite is rated 45 NPU TOPS; X Plus the same NPU block.
5. Record whether it clears 40 — that is the Copilot+ threshold that unlocks Recall and friends.

### Fix 3: Measure it live with a benchmark

Specs tell you the rating; a benchmark confirms the silicon delivers.

1. Install a free NPU-aware benchmark (Geekbench ML/AI or UL Procyon AI Inference).
2. Close background apps, run the NPU/AI workload test.
3. Compare your score against published results for your chip — it should land in the expected band.
4. A score far below expectations suggests driver or thermal issues, not a weak chip — and if a driver update broke things, an [Intel NPU update failure](/articles/intel-npu-driver-update-failed/) has its own fix path.
5. If the benchmark cannot find the NPU at all, treat it as a detection problem and [roll back or reinstall the driver](/articles/npu-driver-rollback-windows-11/).

### Fix 4: Use vendor utilities for live telemetry

Chip makers ship tools that expose what Windows hides.

1. Intel: Intel Driver & Support Assistant ([intel.com](https://www.intel.com/content/www/us/en/support/detect.html)) can report NPU details on Core Ultra systems.
2. AMD: Ryzen Master or the AMD Software suite shows XDNA NPU status on Ryzen AI machines.
3. Check Device Manager, Neural processors, NPU Properties, Details tab — the Hardware Ids sometimes encode the NPU generation.
4. Third-party tools like HWiNFO64 list NPU blocks with their rated throughput on supported chips.
5. Cross-check any tool's figure against the official spec — tools occasionally misread engineering-sample values.

### Fix 5: Confirm Copilot+ eligibility from the number

Turn the TOPS figure into a practical answer.

1. 40+ NPU TOPS: your laptop qualifies for Copilot+ features (Recall, Live Captions translation, Studio Effects).
2. Below 40: Windows will not offer those exclusives regardless of drivers — it is a hardware bar, not a bug.
3. If you are at 40+ but features are missing, the issue is software — see [Recall not available on my PC](/articles/recall-not-available-on-my-pc/).
4. Remember TOPS is NPU-only for this bar; a powerful GPU does not substitute.

## Closing

Checking NPU TOPS takes under a minute once you know where Windows hides the pieces: Task Manager for presence, the vendor spec page for the rated number, and a benchmark for proof. The magic threshold is 40 — above it, you are in Copilot+ territory; below it, your AI workloads fall back to CPU and GPU. Either way, knowing the number turns vague "AI laptop" marketing into a concrete fact about your machine.
