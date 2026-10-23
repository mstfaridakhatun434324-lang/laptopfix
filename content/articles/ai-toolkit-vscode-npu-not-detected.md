---
title: "How to Fix the AI Toolkit for VS Code Not Detecting Your NPU"
slug: ai-toolkit-vscode-npu-not-detected
date: 2026-10-23
categories: ["ai-pc"]
tags: ["ai toolkit", "vs code", "npu", "directml", "copilot+ pc", "troubleshooting"]
description: "Fix the AI Toolkit for VS Code not detecting your NPU on Copilot+ PCs. Check drivers, DirectML runtimes, execution providers, and model formats step by step."
thumbnail: "/images/thumbs/ai-toolkit-vscode-npu-not-detected.webp"
faqs:
  - q: "Why does the AI Toolkit only show CPU as a device?"
    a: >
      The NPU is reached through the ONNX Runtime DirectML execution provider, and that chain breaks silently at several points: a missing or generic NPU driver, a wrong execution-provider setting, or a model format the NPU cannot run. Work through the driver, runtime, and model checks in order and the NPU usually appears.
  - q: "Does the AI Toolkit work on Snapdragon and Intel NPUs alike?"
    a: >
      Yes — it targets the DirectML abstraction rather than a specific chip, so Qualcomm Hexagon, Intel AI Boost, and AMD Ryzen AI NPUs all work through the same path. The difference is in the driver: each vendor ships its own NPU driver package, and only the correct one makes the device visible to DirectML.
  - q: "Do I need the ARM64 build of VS Code?"
    a: >
      On Snapdragon machines, yes. The x64 build runs under Prism emulation, and that layer can hide the NPU from the extension's device enumeration even when Windows sees it perfectly well. Install the ARM64 user setup of VS Code for full, reliable NPU access.
  - q: "Can a work laptop block the NPU in the AI Toolkit?"
    a: >
      It can. Managed devices may carry policies that disable local model execution or restrict the Windows AI runtime components the toolkit depends on. If every fix checks out but the device list stays empty, ask your IT admin about Copilot and local-AI execution policies.
---

You installed Microsoft's AI Toolkit for VS Code on your Copilot+ PC, opened the model playground, and expected the NPU to appear as an execution device — instead you get only CPU, or a quiet "no compatible device" message. The laptop clearly has an NPU (Task Manager even shows it), so the extension looks broken. It isn't: the toolkit never talks to the NPU directly. It reaches it through a chain — VS Code's architecture, the ONNX Runtime, the DirectML execution provider, the NPU driver, and the model format — and any single broken link hides the device.

On Copilot+ PCs this chain is still young and fragile. The NPU driver model on Windows is maturing, VS Code ships in x64 and ARM64 builds that behave differently, and most popular models are published in formats the NPU cannot execute natively. The failure is silent by design: when the toolkit can't validate the full path to the NPU, it falls back to CPU instead of erroring, which makes the problem look like a missing feature rather than a configuration issue.

This guide walks you through six fixes in technician order: confirm the NPU is visible to Windows, repair the driver, get on the right VS Code build, set the execution provider, use an NPU-compatible model format, and finish with a clean reinstall if the extension's state is corrupted. Check the playground's device list after each step.

## Why this happens

- **NPU driver missing or generic:** Windows Update sometimes installs a basic driver exposing the NPU to Task Manager but not to DirectML.
- **DirectML execution provider not selected:** The playground defaults to CPU; unless DirectML is chosen and healthy, the NPU never enters the list.
- **Model format the NPU cannot execute:** GGUF and raw PyTorch checkpoints have no NPU path — only ONNX-style graphs run on the neural processor.
- **VS Code running as x64 under emulation:** On Snapdragon PCs, the emulated x64 build can fail device enumeration even when the native stack is fine.
- **Incomplete Windows AI runtime components:** A missing or half-updated AI runtime leaves DirectML unable to bind the NPU, with no visible error.
- **Managed-device policies blocking local AI:** Work laptops can disable local model execution through policy, graying out the controls you need.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Windows itself sees the NPU

Before touching the extension, prove the NPU is visible to Windows. The toolkit enumerates devices through DirectML, which can only offer what the OS exposes — if Task Manager's Performance tab has no NPU entry and Device Manager shows nothing under Neural processors, no extension setting will conjure one. This check takes a minute and splits the problem cleanly: a Windows-level gap means driver work, while a visible-but-unused NPU means the fault is higher in the toolkit chain. Device-enumeration failures on Windows on ARM usually trace to driver packages that never registered the hardware — the same root cause behind [haptic touchpads not working on Windows 11](/articles/haptic-touchpad-not-working-windows-11/).

1. Open Task Manager (Ctrl+Shift+Esc) > **Performance** and look for an **NPU** entry.
2. Open Device Manager, expand **Neural processors**, and confirm the NPU has no warning icon.
3. If the NPU is missing entirely, skip to Fix 2 — the driver is your problem.
4. If it shows a warning icon, note the error code before continuing.
5. If it is present and clean, move on — the issue is above the driver layer.

### Fix 2: Install the correct NPU driver

A Task Manager-visible NPU can still be invisible to DirectML if the driver is the generic one Windows Update prefers. Vendor NPU drivers register the device with the DirectML runtime; without that registration, the toolkit's enumeration comes back empty. Match the driver to your silicon: Intel systems can use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), AMD Ryzen AI systems should use [AMD's driver download page](https://www.amd.com/en/support/download/drivers.html), and Snapdragon laptops must use the laptop maker's support package, since Qualcomm NPU drivers ship through OEMs.

1. Identify your chip in **Settings > System > About**.
2. Download the matching NPU driver from the OEM site or a vendor tool above.
3. Run the installer as administrator; don't let the laptop sleep mid-install.
4. Restart, then recheck Device Manager and Task Manager.
5. Reopen the AI Toolkit playground and check the device list.

### Fix 3: Switch to the ARM64 build of VS Code

On Snapdragon Copilot+ PCs this is the most overlooked cause. The x64 build of VS Code runs under Prism emulation, and the AI Toolkit's native device-enumeration calls can fail to cross that boundary — Windows sees the NPU, the extension does not. The native ARM64 build removes the boundary entirely. Intel and AMD machines don't have this issue, but the architecture check still takes thirty seconds and catches the users who installed x64 VS Code out of habit on ARM hardware.

1. In VS Code, open **Help > About** and check the architecture line.
2. If it says x64 on Snapdragon, back up your settings first.
3. Download the ARM64 User Installer from the official VS Code website.
4. Reinstall the AI Toolkit extension inside the ARM64 build.
5. Open the playground and recheck the device list.

### Fix 4: Set the DirectML execution provider

Even with a healthy driver and the right VS Code build, the playground keeps offering only CPU if the execution provider is wrong — the toolkit does not auto-promote the NPU. You must explicitly select DirectML, the provider that routes work to the neural processor on Windows. One caveat for work laptops: if the provider dropdown is grayed out or your choice never sticks, the machine may be managed — [Copilot managed-device restrictions](/articles/copilot-managed-device-disabled/) can block local model execution through policy, and no reinstall overrides that.

1. Open the AI Toolkit playground or its settings panel.
2. Set the execution provider / device target to **DirectML** (not CPU).
3. Fully quit VS Code — check the system tray — and reopen it.
4. Return to the playground and verify the NPU appears as a target.
5. If the setting is locked, ask IT about local-AI execution policies.

### Fix 5: Use a model format the NPU can execute

The NPU cannot run every model in the toolkit catalog. GGUF checkpoints and raw PyTorch weights have no NPU execution path on Windows — the neural processor needs ONNX-format graphs, usually quantized to INT4 or FP16. Loading an incompatible format is why many users see the NPU vanish the moment they pick a specific model: the toolkit validates format against device and quietly drops the NPU from the candidates. Intel users hitting the same wall in the vendor's own app should read the [Intel AI Playground NPU detection guide](/articles/intel-ai-playground-npu-not-detected/) — the format constraint is identical there.

1. Check the format badge on the model you want in the toolkit catalog.
2. Choose an ONNX or NPU-quantized variant for NPU runs.
3. Convert PyTorch-only weights with the toolkit's conversion workflow if needed.
4. Retry the playground and confirm the NPU stays listed.
5. Keep a CPU-targeted copy of models the NPU will never run.

### Fix 6: Clean-reinstall the extension and clear its cache

When every layer checks out but the device list is still wrong, the extension's own state is the suspect — a corrupted model cache or a half-migrated settings file from the x64 build can pin enumeration to a stale result. A plain reinstall over the top doesn't clear this; remove the extension's folders manually. This last resort forces model re-downloads, but it resolves stubborn cases where Fixes 1–5 all looked correct. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) also document related Windows AI runtime repairs.

1. Uninstall the AI Toolkit extension from VS Code.
2. Delete its folder under `%USERPROFILE%\.vscode\extensions` and its model cache.
3. Reinstall the extension fresh from the marketplace.
4. Re-download your model in the NPU-compatible format from Fix 5.
5. Open the playground — the NPU should now appear.

## Closing

An NPU missing from the AI Toolkit is a chain problem: Windows must expose the device, the right driver must register it with DirectML, VS Code must be the native ARM64 build, the provider must be DirectML, and the model must be NPU-runnable. Verify the chain in that order and the NPU shows up where it belongs.
