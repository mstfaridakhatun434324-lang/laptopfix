---
title: "How to Benchmark Your NPU on Windows 11"
slug: how-to-benchmark-npu-windows-11
date: 2026-10-23
categories: ["ai-pc"]
tags: ["npu", "benchmark", "copilot+ pc", "ai performance", "tops", "windows 11"]
description: "Benchmark your Windows 11 NPU the right way: tools, steps, and how to read TOPS scores so you know what your Copilot+ PC's AI hardware actually delivers."
thumbnail: "/images/thumbs/how-to-benchmark-npu-windows-11.webp"
faqs:
  - q: "Is there a built-in NPU benchmark in Windows 11?"
    a: "No, Windows 11 does not include a dedicated NPU benchmark. Task Manager shows NPU utilization, and you can use third-party tools like Procyon AI, AIDA64, or the ONNX Runtime performance tests to get real scores."
  - q: "What is a good NPU benchmark score?"
    a: "It depends on the workload and tool. For headline numbers, a Copilot+ PC NPU should deliver at least 40 TOPS for INT8 inference. For real workloads, compare your per-model inference times against published results for your exact NPU model."
  - q: "Why does my NPU score change between runs?"
    a: "NPU results vary with power mode, thermal state, driver version, and background load. For consistent results, plug in the charger, set Best performance, close other apps, and let the laptop cool before each run."
  - q: "Can benchmarking the NPU damage my laptop?"
    a: "No. Inference benchmarks run within the NPU's rated power and thermal envelope. The chip will throttle if it gets hot. Standard benchmark tools are safe to run repeatedly on any Copilot+ laptop."
---

Your Copilot+ laptop's box brags about a 45-TOPS NPU, but nothing in Windows 11 tells you what that number actually buys you in practice. Task Manager shows an "NPU" graph now, yet it reports utilization — a percentage of "busy" — not throughput, not latency, not anything you can compare against another machine.

A benchmark translates the marketing TOPS figure into a number you can actually reason about.

This guide walks you through six checks in technician order: confirming the NPU is present and healthy, picking the right tools, running controlled tests, and interpreting the numbers honestly. Work through them in sequence and you will know exactly what your NPU can and cannot do.

## Why this happens

- **Windows 11 shows utilization, not throughput:** Task Manager's NPU graph tells you the chip is busy but not how much work it is doing — a 100% reading at a tiny model and a big model look identical, which makes "is it fast?" unanswerable.
- **TOPS are a peak number, not a sustained one:** The 40+ TOPS figure is measured on ideal INT8 dense matrix work at full power; real models with different precisions, sparsity, and memory patterns rarely hit it, so marketing and measured scores diverge by design.
- **NPU drivers and runtime versions change results:** Windows ML, the NPU driver, and each app's runtime all sit in the path; updating any one of them can shift scores by double digits between runs weeks apart.
- **Power mode and thermals silently cap the NPU:** Battery-saver or "best power efficiency" modes clock the NPU down, and sustained tests throttle it as heat builds — identical tests give different numbers if conditions differ.
- **Different benchmarks measure different things:** A synthetic TOPS test, a Stable Diffusion inference run, and an LLM token-per-second test exercise different precisions and memory paths, so scores are only comparable within the same tool and workload.
- **No built-in, standardized NPU benchmark exists yet:** Unlike CPU and GPU testing, there is no PassMark-style standard everyone quotes, so you have to pick tools deliberately and document your setup.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the NPU is present and recognized by Windows

Before benchmarking anything, verify the chip Windows thinks it has. If the NPU is missing or unrecognized, every number you measure is meaningless — you would be benchmarking a fallback, not the silicon.

1. Open **Task Manager > Performance** and look for an **NPU** tab — on Copilot+ PCs it appears next to CPU and GPU, showing vendor (Qualcomm, Intel, or AMD) and utilization.
2. If there is no NPU tab, open **Device Manager > Neural processors** and check the device status; a yellow warning means the driver failed to load.
3. Confirm your machine is actually a Copilot+ PC — the [Copilot+ PC requirements](https://support.microsoft.com/en-us/windows) need 40+ TOPS; older AI PCs may simply lack the NPU tab.
4. Download the latest NPU driver from your laptop maker's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — since Windows Update drivers lag behind.
5. Restart and recheck Task Manager; a healthy NPU idles near 0% and spikes when AI features run.

### Fix 2: Set controlled test conditions

NPU numbers are only comparable when the conditions are fixed. Skip this and every comparison — against your own past runs or someone else's — is noise. This is the same discipline used when diagnosing [memory integrity conflicts with NPU drivers](/articles/memory-integrity-npu-driver-conflict/), where one changed variable masks the real cause.

1. Plug in the charger — battery modes downclock the NPU, so every run must be on AC power.
2. Set **Settings > System > Power & battery > Power mode** to **Best performance** and turn off Battery saver.
3. Close all other apps, especially anything AI-flavored (video calls with effects, Copilot, photo apps) that could steal NPU cycles mid-test.
4. Let the laptop sit idle for two minutes so thermals stabilize before the first run.
5. Note your driver version and Windows build — write them down, because a later update that moves scores needs a before/after paper trail.

### Fix 3: Run a synthetic inference benchmark

Synthetic tests give you the headline number closest to the marketing TOPS figure. They measure raw throughput on a controlled model so you can confirm the NPU reaches its rated performance at all.

1. Install a synthetic AI benchmark such as UL Procyon AI Inference (Windows ML backend) or check whether your tool supports your NPU vendor's execution provider.
2. Select the NPU as the target device — most tools default to CPU or GPU, which would benchmark the wrong chip entirely.
3. Run the standard inference test suite (typically MobileNet, ResNet, or similar vision models) and record the per-model scores and total.
4. Repeat the run twice more; take the median, not the best — the first run often includes warm-up effects and the third catches thermal drift.
5. Compare against published scores for your exact NPU (Snapdragon X Elite NPU, Intel Core Ultra NPU, or AMD Ryzen AI NPU) rather than across vendors — different toolchains make cross-vendor synthetic scores unreliable.

### Fix 4: Test a real-world generative workload

Synthetic scores are theory; generative workloads are practice. Running an actual diffusion model on the NPU shows you the number that matters day to day — seconds per image — and exposes memory-bandwidth limits that synthetics hide.

1. Install an NPU-accelerated image tool that supports your chip, such as a DirectML or Qualcomm AI Hub build of a Stable Diffusion pipeline.
2. Pick a fixed prompt, seed, step count, and resolution — changing any of these between runs makes the timing incomparable.
3. Time a full generation end to end and record seconds per image, not just the model-inference portion.
4. Compare the same workload on CPU and GPU backends to see the NPU's real advantage — many laptops show a modest NPU win on small models and a big one on sustained batches.
5. If generation fails to use the NPU at all, the same app-blocking behavior behind [Smart App Control blocking ARM apps](/articles/smart-app-control-blocking-arm-apps/) can be the culprit — check that security features are not quarantining the AI runtime.

### Fix 5: Measure feature latency, not just throughput

For Copilot+ features, what you feel is latency, not TOPS. Live captions, Click to Do, and Studio Effects each run small models where milliseconds of delay matter more than trillions of operations — so measure the delay directly.

1. Enable **Live captions** during a video call and watch for the caption lag; on a healthy NPU it stays under a second of drift from speech.
2. Trigger **Click to Do** (the default key is worth remapping — see [how to customize the Click to Do shortcut](/articles/customize-click-to-do-keyboard-shortcut/)) and time how long its suggestions take to appear after selecting text.
3. Join a video call with **Studio Effects** background blur on and check for stutter or frame lag — the NPU should handle this without touching the CPU.
4. If any feature lags while the NPU graph stays flat, the work is falling back to CPU or GPU, which usually means a driver or runtime problem, not a slow chip.
5. Record these latencies alongside your synthetic scores — together they tell the full story of whether your NPU is pulling its weight.

### Fix 6: Document, compare, and re-test after updates

A benchmark is only useful as a reference point. One-off numbers fade; a small log turns every driver update and Windows release into an experiment with a before and after.

1. Write down your full setup in one place: laptop model, NPU, driver version, Windows build, power mode, tool, and tool version.
2. Save your median synthetic scores, seconds-per-image, and feature latencies next to that setup line.
3. After each NPU driver update or Windows feature update, re-run the exact same tests under the same conditions — the same power discipline applies, since [Intel wireless driver quirks on AI laptops](/articles/intel-be200-wifi-issues-ai-laptop/) show how one driver change can ripple into unrelated subsystems.
4. Treat a sudden score drop as a regression signal: roll the driver back to your logged version and report it to your laptop maker's support.
5. Re-baseline quarterly — AI runtimes improve steadily, and your NPU may legitimately get faster without any hardware change.

## Closing

Benchmarking an NPU is less about the TOPS number on the box and more about building a repeatable test: confirm the chip is healthy, fix your conditions, measure synthetic throughput, then measure the real latency of the features you use. Do that once and every future driver update becomes an answer instead of a question.
