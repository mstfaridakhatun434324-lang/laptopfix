---
title: "Why Your Geekbench AI NPU Score Is Low — and How to Raise It"
slug: geekbench-ai-npu-score-low
date: 2026-10-23
categories: ["ai-pc"]
tags: ["geekbench ai", "npu", "benchmark", "copilot+ pc", "performance", "thermals"]
description: "Low Geekbench AI NPU score on your Copilot+ laptop? Power modes, thermals, drivers, and settings all affect results — here's how to raise your score fast."
thumbnail: "/images/thumbs/geekbench-ai-npu-score-low.webp"
faqs:
  - q: "What is a good Geekbench AI score for a Copilot+ NPU?"
    a: >
      It depends on the chip and precision — Snapdragon X Elite, Intel Core Ultra, and AMD Ryzen AI NPUs each have different TOPS ratings, and quantized scores run much higher than full-precision ones. Compare against the same chip and same precision on the Geekbench browser, never against a different laptop.
  - q: "Why is my NPU score lower on battery?"
    a: >
      Windows caps NPU clocks on battery to save power, and Balanced or Power saver plans throttle the neural processor aggressively. Plug in the charger and switch to Best performance before benchmarking — battery scores aren't comparable to plugged-in scores.
  - q: "Can background apps really change the score?"
    a: >
      Yes, measurably. Recall snapshotting, search indexing, antivirus scans, and even a browser with hardware acceleration can steal NPU and memory bandwidth mid-benchmark. Close everything non-essential and pause background AI features before a run.
  - q: "Should I update drivers before benchmarking?"
    a: >
      Absolutely. NPU drivers on Windows are still maturing, and vendors regularly ship performance fixes that move scores by double-digit percentages. An outdated driver is one of the most common reasons a healthy laptop scores below expectations.
---

You ran Geekbench AI on your Copilot+ laptop, picked the NPU, and the score came back far below the numbers reviewers posted for your exact chip. The laptop isn't defective — NPU benchmarks are exquisitely sensitive to conditions, and reviewers test under conditions your laptop wasn't in: plugged in, cooled down, background-quiet, on the latest driver, with the right precision selected. Miss any one of those and the score drops.

On Windows AI PCs the NPU shares power, thermal headroom, and memory bandwidth with everything else in the chassis. Windows throttles it on battery without telling you, heat soak from earlier workloads slows it within minutes, background Windows features like Recall quietly consume NPU cycles, and an old driver can leave double-digit performance on the table. Geekbench AI also reports separate scores per precision — comparing your full-precision score against someone else's quantized score is a category error, not a hardware problem.

This guide gives you six fixes in order: set the power conditions reviewers use, silence background workloads, control thermals, update the driver and sanity-check against your chip's rated TOPS, pick the right precision, and establish a repeatable run procedure so your numbers are actually comparable.

## Why this happens

- **Benchmarking on battery or Balanced mode:** Windows throttles NPU clocks aggressively off-charger — the biggest score killer.
- **Thermal throttling:** The NPU shares the chassis thermal budget; a warm laptop scores lower than a cool one within minutes.
- **Background AI workloads:** Recall snapshotting, search indexing, and Studio Effects consume NPU cycles during your run.
- **Outdated NPU driver:** Vendors ship real performance fixes in driver updates — old drivers benchmark like old hardware.
- **Wrong precision selected:** Comparing full-precision scores to published quantized scores guarantees disappointment.
- **First-run compilation overhead:** The NPU compiles graphs on first execution, so a cold single run understates sustained performance.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Benchmark plugged in on Best performance

This resolves most "low score" reports by itself. On battery, Windows caps NPU clocks to protect runtime, and the Balanced plan throttles the neural processor even on AC power on many Copilot+ designs. Reviewers' numbers are essentially always taken plugged in on the highest performance plan — comparing your battery score to their AC score is meaningless. Plug in the charger, open Settings > System > Power & battery, and set Power mode to Best performance. Also disable Battery saver, since its automatic threshold can engage mid-benchmark and crater the second half of a run.

1. Plug in the original charger — under-delivering third-party chargers still throttle.
2. Set **Power & battery > Power mode** to **Best performance**.
3. Turn off **Battery saver**, including its automatic threshold.
4. Wait two minutes for clocks to settle, then run Geekbench AI.
5. Record the score with a note of the exact power conditions.

### Fix 2: Silence background workloads

Your NPU is shared, and Windows runs quiet consumers that benchmark guides never mention. Recall's snapshotting periodically wakes the NPU to process captures; search indexing hammers memory bandwidth; a browser tab with hardware acceleration or a Teams call with Studio Effects can shave points off your run. These workloads are bursty — they inflate run-to-run variance, so one run looks fine and the next looks broken. If Recall seems to misbehave in the background, the [Recall timeline filters troubleshooting guide](/articles/recall-timeline-filters-not-working/) covers the service behavior that also affects benchmarking. Kill the noise before measuring.

1. Close all apps except Geekbench AI — especially browsers and Teams.
2. Pause Windows Search indexing for the benchmark window.
3. Disable Recall snapshotting for the test (re-enable after).
4. Check Task Manager for anything using the NPU before starting.
5. Run three times and keep the median — variance signals background noise.

### Fix 3: Control thermals

NPUs live under the same thermal ceiling as the CPU and GPU, and Copilot+ laptops are thin machines with limited sustained cooling. A laptop that just finished a Teams call or a previous benchmark is heat-soaked: the NPU boosts for the first minute, then throttles — which is why scores decay across back-to-back runs. Reviewers let machines cool and test in cool rooms. You don't need lab conditions, just don't benchmark a hot machine: idle to room temperature, elevate the rear for airflow, and leave cooldown gaps between runs.

1. Close heavy apps and idle 10 minutes before benchmarking.
2. Elevate the laptop's rear slightly for airflow.
3. Avoid hot rooms and soft surfaces like beds.
4. Leave 5+ minutes between runs — never stack benchmarks.
5. If scores decay across runs, that's thermal throttling confirmed.

### Fix 4: Update the driver and sanity-check your chip

NPU drivers on Windows are still young, and vendors regularly ship updates with real, measured performance gains — double-digit deltas between driver versions are not unusual. Before concluding your hardware is slow, make sure you're not benchmarking last year's driver. Then sanity-check expectations: look up your chip's rated TOPS and compare against identical chips on the Geekbench result browser. If every identical laptop scores like yours, the hardware is fine and the "low" score was an unfair comparison. Intel users can verify their stack with [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html).

1. Update the NPU/chipset driver from your maker's support site.
2. Restart and let the system settle for a few minutes.
3. Find matching results for your chip on the Geekbench browser.
4. Compare only same chip, same OS build, same precision.
5. If you match the pack, stop — the score was never low.

### Fix 5: Select the right precision in Geekbench AI

Geekbench AI reports separate scores per precision — typically quantized and full/half precision — and these live on completely different scales. The big headline scores reviewers quote are almost always the quantized ones, because that's where NPUs shine. If you ran full-precision and compared it to a reviewer's quantized number, the gap is expected physics, not a problem. Run all available precisions, match your comparison to the same one, and judge the NPU on the workload you care about — quantized inference is the realistic NPU workload anyway.

1. Note exactly which precision each score corresponds to.
2. Run every precision the benchmark offers, not just the default.
3. Compare each score only against the same precision.
4. Weight the quantized score most — it reflects real NPU usage.
5. Save the full result PDF for future comparisons.

### Fix 6: Establish a repeatable run procedure

One-off benchmark numbers are noise; repeatable numbers are data. Between-run variance comes from Windows housekeeping — updates, Defender scans, disk optimization kicking in at idle. A clean reboot before a benchmark session clears most of it. One caution: if a reboot drops you at a BitLocker recovery prompt, don't panic — the [BitLocker recovery key guide for ARM laptops](/articles/bitlocker-recovery-key-arm-laptop/) walks through retrieving it. And if Geekbench needs to download assets, do it on a stable connection first: [5G WWAN issues on Snapdragon laptops](/articles/5g-wwan-not-working-snapdragon-laptop/) can stall those downloads and produce failed runs that look like hardware faults.

1. Reboot cleanly before each session — no hibernate or fast-startup resume.
2. Wait 3 minutes after login for startup tasks to finish.
3. Apply Fixes 1–3 identically every time.
4. Run three times, keep the median, log conditions with the score.
5. Compare new scores only against this same procedure.

## Closing

A low Geekbench AI NPU score is almost never a hardware fault — it's a conditions fault: battery throttling, background workloads, heat, old drivers, or comparing the wrong precision. Control the conditions, update the driver, compare like with like, and the score lands where your chip belongs.
