---
title: "DirectML Not Using the NPU on Windows 11: How to Fix It"
slug: directml-not-using-npu-windows-11
date: 2026-10-20
categories: ["ai-pc"]
tags: ["directml", "npu not used", "windows 11", "ai acceleration", "troubleshooting"]
description: "DirectML not using the NPU on Windows 11? Learn why AI workloads fall back to CPU or GPU and how to get DirectML execution routed to your laptop's NPU."
thumbnail: "/images/thumbs/directml-not-using-npu-windows-11.webp"
faqs:
  - q: "How can I tell whether DirectML is using my NPU?"
    a: "Open Task Manager's Performance tab and watch the NPU graph while running the AI workload. If the NPU sits at zero while CPU or GPU spikes, DirectML is not routing to it. Some apps also log the selected adapter at startup."
  - q: "Does every AI app use DirectML?"
    a: "No. Many use ONNX Runtime, which can sit on top of DirectML or use its own execution providers. If the app uses ONNX Runtime directly, an [ONNX Runtime NPU execution provider error](/articles/onnx-runtime-npu-execution-provider-error/) is the more likely culprit than DirectML itself."
  - q: "Do I need a special DirectML version for NPU support?"
    a: "NPU support in DirectML depends on both the OS build and the NPU driver exposing a DirectML-compatible device. Windows 11 24H2 with a current vendor driver is the combination that works reliably."
  - q: "Can I force an app to use the NPU instead of the GPU?"
    a: "Only if the app exposes a device-selection setting. DirectML picks the device the app requests; there is no reliable OS-level override. For apps without the option, the fixes below ensure the NPU is at least visible and eligible."
---

DirectML is Microsoft's API for running machine-learning workloads on Windows hardware, and on an AI PC it should target the NPU. But many users find AI apps grinding away on the CPU or GPU while the NPU sits idle at zero percent. The app works — just slowly, hotly, and with worse battery life than the NPU would deliver.

The cause is usually not DirectML itself but the chain beneath it: the NPU driver must expose a DirectML-compatible device, Windows must enumerate it, and the app must request it. Break any link — an outdated driver, an OS build without NPU routing, an app hard-coded to the GPU — and DirectML quietly falls back to whatever is available. It never errors out; it just picks something slower.

This guide shows how to check each link and fix what is broken so DirectML workloads land on the NPU. If the NPU is not visible to apps at all, start with [NPU not used by apps in Windows 11](/articles/npu-not-used-by-apps-windows-11/). If your workload goes through ONNX Runtime, see the [ONNX Runtime NPU execution provider error](/articles/onnx-runtime-npu-execution-provider-error/) guide instead.

## Why this happens

- **NPU driver too old for DirectML routing:** Early NPU drivers exposed the hardware to vendor SDKs but not to DirectML's device enumeration.
- **Windows build lacks NPU support:** Reliable DirectML-to-NPU routing needs recent Windows 11 builds; older builds enumerate the NPU inconsistently.
- **App hard-codes its device:** Many apps request the high-performance GPU explicitly and never query for an NPU adapter.
- **NPU driver exposes the wrong device class:** If the driver registers the NPU oddly, DirectML's adapter query skips it silently.
- **Power or thermal policy parks the NPU:** Aggressive power plans can keep the NPU in a low state that DirectML treats as unavailable.
- **Multiple runtimes conflict:** Vendor SDKs and DirectML competing for the NPU can leave it locked to one runtime and invisible to the other.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the NPU is visible and idle during the workload

Before changing anything, establish the baseline: is DirectML ignoring an available NPU, or is the NPU not available to begin with? The answer decides which of the later fixes applies.

1. Open Task Manager to the Performance tab and keep it visible on a second monitor or snapped beside the app.
2. Run the AI workload and watch the NPU graph — zero activity with CPU/GPU spiking means DirectML is falling back.
3. Open Device Manager and confirm the NPU device (Intel AI Boost, AMD IPU, or Qualcomm Hexagon) shows no warning icon.
4. If Device Manager shows a problem, fix the driver first — no runtime fix can route to a broken device.

### Fix 2: Update Windows 11 and the NPU driver together

DirectML NPU routing is a three-way handshake between the OS, the driver, and the app. Updating only one side is the most common reason the handshake keeps failing, so do both before anything fancier.

1. Install all pending Windows updates and confirm you are on 24H2 or newer under Settings, System, About.
2. Update the NPU driver from your laptop maker's support page — Intel users can also use [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
3. Restart after both updates, even if only one of them asks for it.
4. Re-run the workload with Task Manager open and check whether the NPU graph now shows activity.

### Fix 3: Check the app's device and backend settings

A surprising number of "DirectML ignores my NPU" cases are just the app defaulting to GPU. Apps with backend or device pickers use the NPU only if you tell them to — DirectML never overrides the app's choice.

1. Open the app's settings and look for AI, performance, hardware acceleration, or inference device options.
2. If there is a backend choice, select DirectML explicitly rather than Auto or CUDA.
3. If there is a device picker, choose the NPU (it may be listed as AI Boost, IPU, or by vendor name).
4. Restart the app after changing the setting — most apps enumerate devices only at startup.

### Fix 4: Switch Windows to the Best performance power mode

Windows power policy can park the NPU aggressively on battery-saver or balanced plans, and a parked NPU may not appear in DirectML's adapter list. This is especially common on laptops running on battery.

1. Plug the laptop into AC power for this test to remove battery policy from the equation.
2. Go to Settings, System, Power & battery, and set Power mode to Best performance.
3. In the legacy Control Panel power options, check that any vendor power plan is not forcing the NPU into a low state.
4. Re-run the workload and watch Task Manager — if the NPU wakes up now, power policy was the blocker.

### Fix 5: Reinstall the NPU driver to repair device registration

If the driver is current but DirectML still cannot see the NPU, the driver's device registration may be corrupt — it works for the vendor's own SDK but fails DirectML's enumeration. A clean reinstall rebuilds that registration.

1. In Device Manager, right-click the NPU device, choose Uninstall device, and tick "Attempt to remove the driver for this device."
2. Restart the laptop and let Windows reinstall a baseline driver, or install the OEM package manually.
3. Verify the device appears cleanly with no warning icons before testing.
4. Test with a known DirectML workload — features like [Copilot image generation](/articles/copilot-image-generation-not-working/) depend on this same device path working.

### Fix 6: Test with a minimal DirectML sample to isolate the app

If the OS and driver check out but your specific app still avoids the NPU, the app itself is the variable. A minimal test separates a platform problem from an app problem so you stop fixing the wrong layer.

1. Find a small open-source DirectML sample that lists available adapters at startup.
2. Run it and note whether the NPU appears in its adapter list.
3. If the sample sees the NPU but your app does not, the app is hard-coding its device — check for updates or report it to the developer.
4. If the sample also misses the NPU, return to Fix 2 and Fix 5 — the platform chain is still broken somewhere.

## Closing

DirectML not using the NPU is a chain-of-custody problem: OS, driver, and app must all agree the NPU exists and is eligible. Update Windows and the driver together, check the app's device settings, and rule out power policy before assuming anything exotic. When the chain is intact, the NPU picks up the work — faster inference, a cooler laptop, and battery life that actually reflects the AI PC you bought.
