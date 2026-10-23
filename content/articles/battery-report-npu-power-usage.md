---
title: "How to Read a Battery Report and Check NPU Power Usage on Windows 11"
slug: battery-report-npu-power-usage
date: 2026-10-23
categories: ["ai-pc"]
tags: ["battery report", "npu", "power usage", "powercfg", "copilot+ pc", "troubleshooting"]
description: "Generate a battery report that reveals real NPU and AI workload power usage on your Copilot+ PC, then cut the idle and active drain with targeted fixes."
thumbnail: "/images/thumbs/battery-report-npu-power-usage.webp"
faqs:
  - q: "Does the battery report show NPU power usage separately?"
    a: "Not as a dedicated NPU line item — the battery report shows per-app usage and system drain rates. You infer NPU load by correlating AI app activity (Recall, Studio Effects, Cocreator) with drain spikes, and Task Manager's NPU graph confirms real-time utilization."
  - q: "How much power does the NPU actually use?"
    a: "NPUs are designed for efficiency: sustained AI workloads typically draw single-digit watts, far less than the CPU or GPU doing the same task. If your battery report shows heavy drain during AI features, the workload is probably falling back to CPU or GPU instead."
  - q: "Why does my Copilot+ PC drain fast when using AI features?"
    a: "Usually because the AI workload is not actually running on the NPU — a missing driver, an app update, or a disabled NPU forces inference onto the power-hungry CPU or GPU, which shows up as high drain in the battery report."
  - q: "Can I limit how much power AI features use?"
    a: "Yes: disable AI features you do not use (Recall snapshots, Studio Effects, background blur), set power mode to Best power efficiency, and make sure the NPU driver is current so workloads run on the efficient engine instead of the CPU."
---

Your Copilot+ PC promised all-day battery, but the moment you start using Recall, Windows Studio Effects, or Cocreator, the percentage drops noticeably faster. Is the NPU — the chip sold as the efficiency hero — actually the thing draining your battery? The answer is in a report Windows already generates for you.

Windows 11's battery report (`powercfg /batteryreport`) logs per-app consumption and drain rates over days, but it does not label a neat "NPU" row — the NPU's draw hides inside system and app totals. Reading the report alongside Task Manager's NPU graph lets you separate efficient on-NPU work from wasteful CPU/GPU fallback, which is where the real drain lives.

This guide shows you how to generate the report, interpret what it says about AI workloads, confirm whether the NPU is actually doing the work, and cut the drain with targeted fixes.

## Why this happens

- **AI workloads falling back to CPU or GPU:** When the NPU driver is missing or an app update breaks NPU offload, inference runs on far less efficient engines — the battery report shows this as high drain during AI features.
- **Recall capturing snapshots continuously:** Recall's background screenshotting and NPU processing run all day by default; on heavy-use days this is a measurable slice of battery.
- **Studio Effects always on:** Background blur, eye contact, and auto-framing in every Teams call keep the NPU (or its fallback) busy for hours.
- **Cocreator and Paint AI features rendering repeatedly:** Diffusion workloads are the heaviest consumer AI task on Copilot+ PCs — each generation costs real watt-hours.
- **Click to Do and live captions running in the background:** Text recognition and captioning models idle in memory and wake frequently, adding up over a full day.
- **Power mode set to Best performance:** The performance power plan raises clocks across the SoC, multiplying the cost of every AI workload.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Generate the battery report and find the AI drain

Before changing settings, measure. The battery report gives you per-app usage percentages and drain-rate history so you act on data, not suspicion.

1. Open an elevated Terminal and run `powercfg /batteryreport` — Windows saves an HTML report and prints the path.
2. Open the report and scroll to **Battery usage** (per-app percentages) and **Battery capacity history** — look for days with unusually steep drain.
3. Check the **Usage history** section for drain rates (mW): compare days you used AI features heavily against light days.
4. Note which apps top the usage list during heavy-AI days — Recall-related processes, camera apps with Studio Effects, Paint/Cocreator, and Teams are the usual suspects.
5. Keep this report as your baseline; you will regenerate it after the fixes below to prove the improvement.

### Fix 2: Confirm the NPU is actually doing the work

High drain during AI features usually means the NPU is *not* doing the work. Task Manager shows live NPU utilization — if it sits at 0% while an AI feature runs, you have found your inefficiency.

1. Open **Task Manager > Performance** and look for the **NPU** graph (on Copilot+ PCs it appears alongside CPU, GPU, and memory).
2. Run an AI feature — background blur in a camera app, or image generation — and watch the NPU graph: healthy offload shows clear NPU activity.
3. If NPU stays at 0% while CPU or GPU spikes, the workload is falling back — note which app does this.
4. Check **Device Manager > Neural processors** (or System devices) for the NPU entry — a missing or warning-marked device explains the fallback.
5. Update the NPU/chipset driver from [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html), [AMD's driver page](https://www.amd.com/en/support/download/drivers.html), or your laptop maker's support site, then retest. If the NPU does not appear in Task Manager at all, the same [hardware-visibility checks used for missing NPUs](/articles/msinfo32-npu-not-listed/) apply here — Windows cannot use silicon it cannot see.

### Fix 3: Trim Recall's snapshot schedule

Recall is the most persistent AI background workload on Copilot+ PCs — it screenshots your activity all day and processes it on the NPU. Reducing its scope cuts both NPU time and storage churn.

1. Open **Settings > Privacy & security > Recall & snapshots** and review what is enabled.
2. Exclude apps and websites that do not need snapshots — browsers with sensitive work and media apps are the biggest wins.
3. Reduce the snapshot storage limit so old snapshots (and their reprocessing) stop accumulating.
4. If you rarely search your timeline, consider pausing Recall on days you need maximum battery — the toggle is in the same settings page.
5. Regenerate the battery report after a few days and compare drain rates against your baseline. If Recall also misbehaves in other ways, the [guide to Recall's AI rewrite features](/articles/notepad-ai-rewrite-not-working/) covers the same settings area from a different angle.

### Fix 4: Disable Studio Effects and AI camera features you do not need

Studio Effects (background blur, eye contact correction, auto framing, voice focus) run for the entire duration of every call — on long meeting days they are a major battery line item.

1. Open **Settings > Bluetooth & devices > Cameras**, select your camera, and review which Studio Effects are on.
2. Turn off effects you do not actively need — eye contact and auto-framing are the most expensive; basic background blur is cheaper.
3. In Teams/Zoom, disable their own background effects too, so you are not stacking two blur pipelines.
4. For calls where video does not matter, turn the camera off entirely — no frames means no NPU work at all.
5. If an effect you want is missing rather than draining, [the Click to Do indicator guide](/articles/click-to-do-sparkle-icon-missing/) covers the sibling AI-feature visibility issues on the same machines.

### Fix 5: Switch to Best power efficiency and cap background AI

Power mode multiplies everything: the same NPU workload costs more under Best performance because the whole SoC runs hotter and clocks higher. This is the cheapest global fix.

1. Go to **Settings > System > Power & battery** and set **Power mode** to **Best power efficiency** when on battery.
2. Turn on **Battery saver** at a sensible threshold (30-40%) so Windows throttles background activity during long unplugged stretches.
3. In **Settings > Apps > Installed apps**, open **Advanced options** for AI-heavy apps (including photo editors — [Lightroom's ARM performance issues](/articles/lightroom-arm-windows-slow/) often trace to the same fallback problem) and set background permissions to **Power optimized** or **Never**.
4. Close Cocreator/Paint and live-captioning tools when not in use rather than minimizing them — minimized AI apps still hold models in memory.
5. Regenerate the battery report after several days on the efficiency plan and compare per-app percentages with your baseline.

### Fix 6: Update the platform stack so AI stays on the NPU

The long-term fix for AI battery drain is keeping workloads on the efficient engine. Stale NPU drivers, chipset packages, or Windows builds silently break offload and push work to the CPU — this maintenance pass prevents that.

1. Install all pending Windows Updates — NPU driver and DirectML stack fixes ship through Windows Update on Copilot+ PCs.
2. Check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for known NPU or AI-feature issues on your build.
3. Update the chipset/NPU package from your SoC vendor or laptop maker, then verify in Task Manager that the NPU graph responds to AI workloads again.
4. Update the AI apps themselves (Photos, Paint, Notepad, Teams) from the Microsoft Store — offload bugs are frequently fixed app-side.
5. Run one final `powercfg /batteryreport` after a week and confirm the drain-rate trend improved — the report is your proof, not your hope.

## Closing

The NPU itself is the most efficient way to run AI on your laptop — battery drain during AI features almost always means work is falling back to the CPU or GPU, or background AI is running unchecked. Measure with the battery report, verify the NPU is engaged, trim Recall and Studio Effects, and keep the platform updated so inference stays where it belongs.
