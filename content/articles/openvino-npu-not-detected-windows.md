---
title: "OpenVINO Not Detecting Your NPU on Windows? How to Fix It"
slug: openvino-npu-not-detected-windows
date: 2026-10-21
categories: ["ai-pc"]
tags: ["openvino npu", "npu not detected", "openvino windows", "ai inference npu", "ai pc", "troubleshooting"]
description: "OpenVINO not detecting your NPU on Windows? Fix it with six step-by-step methods covering driver repair, runtime install, device plugins, and permissions."
thumbnail: "/images/thumbs/openvino-npu-not-detected-windows.webp"
faqs:
  - q: "Why does OpenVINO see my CPU and GPU but not the NPU?"
    a: "The NPU needs its driver plus the OpenVINO NPU plugin and runtime components. CPU and GPU work through drivers Windows always has; the NPU path breaks if the NPU driver, the vendor stack, or the OpenVINO runtime is missing or mismatched."
  - q: "Do I need a special OpenVINO version for NPU support?"
    a: "Yes — NPU support needs a recent OpenVINO release with the NPU plugin, matched to your NPU generation. An old install simply has no NPU plugin to load."
  - q: "Will these fixes affect my other AI frameworks?"
    a: "No. The steps target the NPU driver and the OpenVINO runtime only. PyTorch, ONNX Runtime, and DirectML are untouched — though fixing the NPU driver often helps them too."
  - q: "How do I confirm OpenVINO finally sees the NPU?"
    a: "Run OpenVINO's device query sample — 'NPU' should appear alongside CPU and GPU. Then run a small model targeting the NPU and watch Task Manager's NPU graph during inference."
---

You installed OpenVINO, your script lists CPU and GPU as available devices, but the NPU — the reason you bought an AI PC laptop — is nowhere to be found. No error, just absence. The model runs on the wrong hardware: slower and hotter than it should be. For anyone running local inference on Intel Core Ultra, Ryzen AI, or Snapdragon X machines, this is uniquely annoying because everything else looks healthy.

The cause is almost always a broken link in a three-part chain: the NPU hardware driver, the vendor's NPU driver stack that OpenVINO talks to, and the OpenVINO runtime with its NPU plugin. Windows can show the NPU as healthy in Device Manager while OpenVINO still cannot see it, because the two ask the driver different questions.

This guide gives you six fixes in dependency order: confirm the hardware layer, repair the NPU driver, install the correct OpenVINO runtime, check the plugin, fix environment conflicts, and test properly.

## Why this happens

- **NPU driver missing or broken:** OpenVINO queries the NPU through its driver. A driver that cannot initialize makes the NPU invisible to OpenVINO even when Windows boots fine.
- **Wrong OpenVINO version:** NPU plugins are version-specific. An older install predates your NPU generation's plugin, so no NPU is ever enumerated.
- **NPU plugin not installed:** Some distributions split plugins into optional components — a minimal install may lack the NPU plugin entirely.
- **Vendor stack mismatch:** On Intel, the plugin needs the Intel NPU driver stack; on AMD, the XDNA driver path. A mismatched stack breaks enumeration.
- **Conflicting installs:** A system-wide install plus a pip install plus a conda environment can shadow each other, so your script loads a copy without NPU support.
- **No hardware access:** Sandboxed apps, containers, or restricted sessions cannot open the NPU device handle even when everything is installed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the NPU is healthy at the Windows level

OpenVINO cannot see an NPU that Windows itself cannot use. Rule out the hardware layer before touching any OpenVINO install.

1. In Device Manager, check the NPU entry for warnings.
2. In Task Manager's Performance tab, confirm an NPU graph exists.
3. Run a built-in NPU feature like background blur to prove the chip computes.
4. If the NPU is missing or broken here, work through the [NPU not detected in Windows 11 guide](/articles/npu-not-detected-windows-11/) first — no OpenVINO fix bypasses a broken driver.

### Fix 2: Repair the NPU driver stack

Even a warning-free NPU can have a driver stack the plugin cannot talk to — common after Windows Update swaps an OEM driver for a generic one.

1. Identify your vendor: Intel Core Ultra, AMD Ryzen AI, or Qualcomm Snapdragon X.
2. For Intel, run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) and install the latest NPU and graphics stack.
3. For AMD or Qualcomm, get the latest chipset/NPU package from your laptop maker's support page for your exact model.
4. In Device Manager, uninstall the NPU with **"Attempt to remove the driver for this device"** checked, restart, then install the fresh package and verify the NPU is healthy.

### Fix 3: Install the correct OpenVINO version with NPU support

Version mismatch is the most common OpenVINO-side cause: the runtime must be new enough to include your hardware generation's NPU plugin, and the plugin must actually be present.

1. Check your version (`pip show openvino`) against the latest release notes for NPU support on your platform.
2. Uninstall the old OpenVINO completely — pip package, system install, and conda copies — so no stale copy shadows the new one.
3. Install the latest full Windows release including hardware plugins (not a CPU-only build), selecting the NPU plugin component if offered.
4. Re-run your device query. If the NPU is still absent while CPU and GPU appear, continue to Fix 5.

### Fix 4: Verify the NPU plugin loads

Sometimes the plugin exists but fails to initialize — a missing dependency or blocked load produces silence rather than an error.

1. Confirm an NPU plugin library is physically present in your OpenVINO install's plugin directory.
2. Run OpenVINO's device-query sample from an elevated terminal and read the full output for NPU load errors.
3. If it reports a missing system DLL, service your Windows 11 install via the [official Microsoft Windows download page](https://www.microsoft.com/en-us/software-download/windows11), then reinstall OpenVINO.
4. Temporarily disable third-party antivirus and re-run the query — security software sometimes blocks the plugin's hardware access.

### Fix 5: Clean up conflicting Python environments

Multiple OpenVINO copies are a notorious trap: your script imports a two-year-old pip copy while you carefully upgraded the system install.

1. Run `python -c "import openvino; print(openvino.__file__)"` to see exactly which copy your script loads.
2. Hunt down other copies in site-packages folders, conda envs, and Program Files, and remove all but one.
3. Reinstall the current release into the single environment you use, ideally a fresh virtual environment.
4. Re-run the device query there. (App-level capture problems like [Recall not recording specific apps](/articles/recall-not-recording-specific-apps/) are a separate issue — do not chase them together with device enumeration.)

### Fix 6: Test NPU inference the right way

Some "not detected" reports come from testing methodology: the NPU is detected but busy, or the test never requested it. A disciplined test settles it.

1. Close other AI apps first — if live captions hold the NPU, OpenVINO may fail to claim it. (For caption problems themselves, see the [live captions high memory usage guide](/articles/live-captions-high-memory-usage/).)
2. Write a minimal script that explicitly requests device `NPU` (not `AUTO`) and prints the device list first.
3. Run it while watching Task Manager's NPU graph — activity during inference is definitive proof.
4. Document the working combination (OpenVINO, driver, BIOS versions) so the next update does not silently break it.

## Closing

OpenVINO not detecting your NPU is a chain problem: Windows driver health, the vendor's NPU stack, the right OpenVINO version with its NPU plugin, and one clean install. Work the chain in order — confirm the NPU in Device Manager and Task Manager first, repair the driver, install a current full OpenVINO release, eliminate duplicates, and test with an explicit device request. Then pin those versions and update deliberately.
