---
title: "NPU Not Used by Apps in Windows 11? Force It to Work"
slug: npu-not-used-by-apps-windows-11
date: 2026-10-19
categories: ["ai-pc"]
tags: ["npu", "apps", "ai workloads", "windows 11", "copilot plus pc"]
description: "NPU not used by apps in Windows 11? Learn why AI workloads bypass your NPU and how to route them to the AI chip for speed and battery savings."
thumbnail: "/images/thumbs/npu-not-used-by-apps-windows-11.webp"
faqs:
  - q: "How do I know if an app is using the NPU?"
    a: "Open Task Manager, Performance tab, click the NPU entry, then run the app's AI feature. If the NPU graph spikes, the app is using it. A flat line during AI work means the workload is going to CPU or GPU instead."
  - q: "Why would an app ignore a working NPU?"
    a: "Most commonly the app was not built with NPU support — it only knows CPU/GPU paths. Other causes: outdated app version, the app defaulting to GPU, or Windows routing the workload elsewhere due to driver issues."
  - q: "Can I force any app to use the NPU?"
    a: "No — the app must contain NPU-targeted code paths (via DirectML, OpenVINO, ONNX Runtime, or vendor SDKs). You cannot force an app that was never programmed for the NPU, but you can make sure NPU-aware apps actually choose it."
  - q: "Does it matter if the GPU handles AI instead?"
    a: "For speed, sometimes the GPU is actually faster. For battery life, the NPU wins by a wide margin. On a laptop running on battery, NPU routing can mean hours of extra runtime during AI-heavy work."
---

Your NPU shows up fine in Task Manager — healthy, detected, driver good — but when you run AI features, the NPU graph stays flat while the CPU or GPU does all the work. The chip is ready; nothing is sending it jobs. This is a routing and software-support problem, not a hardware problem, and it is extremely common because most applications were written before NPUs existed.

Think of it this way: detection means the road is built, but apps need directions to use it. If your NPU is not even detected, fix that first ([NPU not detected guide](/articles/npu-not-detected-windows-11/)). If it is detected but idle during AI work, the fixes below get workloads routed correctly.

## Why this happens

- **App lacks NPU support:** The overwhelming cause. Most apps only implement CPU/GPU paths; NPU support requires explicit developer work.
- **Outdated app version:** NPU support often arrives in newer releases — the installed version may predate it.
- **App defaults to GPU:** Some NPU-aware apps still default to GPU and need a settings toggle to prefer the NPU.
- **Wrong execution provider order:** Frameworks like ONNX Runtime try providers in order; a misconfigured app tries GPU first and never falls to NPU.
- **Driver too old for the app's API:** The app may require a newer NPU driver exposing specific DirectML or OpenVINO features.
- **Windows power policy:** On battery saver modes, Windows may route AI work to the most available processor rather than the NPU.
- **NPU disabled at firmware level for apps:** Rare BIOS modes expose the NPU to the OS but block workload submission.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify with a known NPU-aware app

Establish whether the problem is your app or your system.

1. Test with a guaranteed NPU user: Windows Studio Effects (camera), Live Captions, or Recall — all route to NPU on Copilot+ PCs.
2. Watch Task Manager's NPU graph during the test — spikes confirm the system path works.
3. If system features use the NPU but your app does not, the app is the problem — continue to Fix 2.
4. If even system features leave the NPU flat, suspect drivers — reinstall the OEM NPU driver.
5. Our [TOPS check guide](/articles/how-to-check-npu-tops-windows-11/) helps confirm the chip is genuinely capable.

### Fix 2: Update the app

NPU support is new; your version may predate it.

1. Check the app's website or store page for the latest version and its changelog — look for "NPU," "AI acceleration," or "Copilot+ PC" mentions.
2. Update to the latest release.
3. Dig through the app's settings for AI/hardware acceleration options — enable NPU or "AI chip" if offered.
4. Some apps need a separate "AI features" plugin or model download — check for those.
5. Retest with Task Manager open.

### Fix 3: Check the app's execution settings

Many apps let you choose the AI processor.

1. Open the app's settings or preferences — look under Performance, AI, or Advanced.
2. Select NPU / AI accelerator instead of Auto or GPU.
3. For developer tools using ONNX Runtime or OpenVINO, check config files for execution provider ordering — NPU/DirectML should precede GPU for efficiency.
4. Restart the app after changing the setting — provider selection often happens at startup.
5. Verify with Task Manager that the NPU graph now moves during the workload.

### Fix 4: Update the NPU driver for API support

Apps may need driver features your current version lacks.

1. Install the latest OEM NPU driver ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
2. Also update the app's framework if it bundles one (some ship their own ONNX Runtime).
3. Reboot and retest — new drivers expose new DirectML feature levels apps check for.
4. If the app worked with an older driver, [roll back](/articles/npu-driver-rollback-windows-11/) — API regressions happen.
5. Check the app vendor's support page for a driver compatibility list.

### Fix 5: Adjust Windows power and graphics settings

Windows may be steering work away from the NPU.

1. Settings, System, Power & battery — use Balanced or Best performance, not Best power efficiency, during testing.
2. Settings, System, Display, Graphics — find the app, set it to "Let Windows decide" or Power saving (which favors the NPU path on some systems).
3. Ensure the NPU itself is fully enabled in [BIOS](/articles/how-to-enable-npu-in-bios/) — not a limited mode.
4. Retest on AC power first; battery-saver policies legitimately reroute work.
5. Once working on AC, test on battery to find your acceptable tradeoff.

### Fix 6: Accept app limitations gracefully

Sometimes the answer is that the app simply cannot use the NPU yet.

1. Check the vendor's roadmap or forums — NPU support may be announced but unreleased.
2. Use Windows' built-in AI features (which do use the NPU) as alternatives where possible.
3. For heavy AI work, the GPU fallback is often faster anyway — the NPU's advantage is efficiency, not raw speed. Our [NPU vs GPU guide](/articles/npu-vs-gpu-which-runs-ai-tasks/) breaks down when each wins.
4. Revisit after major app updates — NPU support is being added across the industry monthly.
5. Do not chase this with registry hacks promising to "force" NPU usage — they cannot create code paths the app lacks.

## Closing

An idle NPU during AI work is a software-routing reality, not a defect: most apps predate NPUs, and even aware ones need correct settings, current drivers, and cooperative power policies. Verify with system AI features first, update everything, check the app's own toggles, and accept that some apps simply are not NPU-aware yet. The ecosystem is moving fast — the app ignoring your NPU today may target it in next quarter's update. And if the NPU runs hot while being ignored, that heat is worth investigating separately in our [NPU overheating guide](/articles/npu-overheating-laptop/).
