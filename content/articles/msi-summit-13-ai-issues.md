---
title: "MSI Summit 13 AI Evo Issues? How to Fix Them on Windows 11"
slug: msi-summit-13-ai-issues
date: 2026-10-26
categories: ["ai-pc"]
tags: ["msi summit 13 ai evo", "intel core ultra", "copilot app", "directml npu", "windows 11 ai", "msi troubleshooting"]
description: "Fix MSI Summit 13 AI Evo issues on Windows 11: Copilot app, DirectML NPU performance, VPN and driver problems with clear step-by-step repair guides here."
thumbnail: "/images/thumbs/msi-summit-13-ai-issues.webp"
faqs:
  - q: "Why is the Copilot app not working on my MSI Summit 13 AI Evo?"
    a: >
      Usually the Copilot app cache is corrupted, the app is outdated, or the Intel AI drivers are missing. Repairing or resetting the app in Settings and reinstalling the Intel AI drivers fixes most cases without touching your files.
  - q: "Why is DirectML slow on the Summit 13's NPU?"
    a: >
      DirectML falls back to the CPU or GPU when the NPU driver is outdated or the app is not built for the Intel AI Boost NPU. Updating Intel graphics and NPU drivers and using a DirectML build that targets the NPU restores hardware acceleration.
  - q: "Can a VPN break AI features on this laptop?"
    a: >
      A VPN can block Copilot's cloud services and model downloads, which makes Copilot look broken even though the local NPU is fine. Disconnecting the VPN and testing Copilot isolates the cause quickly.
  - q: "Do I need MSI Center for AI features to work?"
    a: >
      No, but MSI Center manages power profiles and some AI-adjacent utilities. If MSI Center is missing or corrupted, power throttling can slow AI work, so reinstalling it is worth trying when performance is the complaint.
---

The MSI Summit 13 AI Evo is a business ultrabook built around Intel's Core Ultra platform, with an integrated NPU meant to handle AI workloads quietly in the background. When Copilot stutters, DirectML apps crawl, or a VPN refuses to cooperate, the laptop feels less like an AI Evo machine and more like an ordinary notebook with a fancy badge. The good news is that these problems are almost always fixable in software.

Intel AI laptops have a more complex driver stack than they appear to: the graphics driver, the NPU driver, and the Intel AI software all have to agree. When one piece lags behind after a Windows update, AI features degrade in confusing ways — Copilot works but is slow, or an app claims NPU support yet runs everything on the CPU. This guide untangles that stack in order.

Work through the fixes below one at a time, testing an AI feature after each step. That way you find the actual cause instead of reinstalling everything at once.

## Why this happens

- **Intel NPU driver outdated or replaced:** Windows Update can install a generic graphics driver that lacks the AI Boost NPU component, leaving DirectML and AI apps without hardware acceleration.
- **Copilot app cache corrupted:** A damaged Copilot installation produces blank windows, failed sign-ins, or missing widgets even when the NPU is perfectly healthy.
- **DirectML app not targeting the NPU:** Not every DirectML build routes work to the NPU; older or CPU-targeted builds silently fall back to slower hardware.
- **VPN filtering or blocking AI traffic:** VPN clients can block Copilot's cloud endpoints, model downloads, or authentication, which looks exactly like a broken AI feature.
- **MSI power profile throttling the NPU:** Silent or Eco modes in MSI Center throttle the whole platform, and AI workloads are often the first to slow down.
- **Windows AI platform components damaged:** A failed feature update can corrupt the Windows AI runtime that Copilot and DirectML apps depend on.
- **Conflicting network filter drivers:** Some VPN and security tools install filter drivers that interfere with local AI service connections as well as internet traffic.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the Intel AI Boost NPU is detected

Start with the hardware check. If Windows cannot see the NPU, every other fix is premature — you have a driver problem, not an app problem.

1. Open Task Manager with Ctrl + Shift + Esc and look for the NPU tile under Performance.
2. If it is missing, open Device Manager and expand System devices, looking for Intel AI Boost or any device with a warning icon.
3. Note the device name and error code, if any, since this tells you whether the driver failed or the device is disabled.
4. Right-click the device and choose Enable device if that option is available, then restart.
5. If the NPU appears but shows 0% during AI work, continue to Fix 3 — the driver loads, but apps are not using it.

### Fix 2: Reinstall Intel graphics and NPU drivers

The graphics driver package carries the NPU driver on Core Ultra machines, so a clean reinstall of both fixes most detection and performance problems in one step.

1. Download the latest Intel graphics driver from the Intel driver support page for your exact Core Ultra processor.
2. Open Device Manager, expand Display adapters, right-click the Intel graphics device, and choose Uninstall device, ticking the driver-removal option if shown.
3. Restart the laptop, then install the downloaded Intel driver package and restart again.
4. Open Task Manager and confirm the NPU tile has returned.
5. Run Windows Update afterwards and check whether it tries to replace the Intel driver with an older one; if it does, reinstall the Intel package once more. For official Intel downloads, use the Intel driver detection tool at [Intel support](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 3: Repair the Copilot app and its widget

When the NPU is healthy but Copilot misbehaves, the app itself is the problem. Copilot's widget, in particular, depends on WebView and app permissions that break silently after updates.

1. Open Settings, go to Apps, then Installed apps, and find Microsoft Copilot.
2. Click the three dots, choose Advanced options, click Repair, and test Copilot again.
3. If Repair fails, return to the same page and click Reset to clear the app's stored data.
4. Open Copilot, sign out completely, sign back in, and check the Microsoft Store for pending Copilot updates.
5. If the widget specifically is broken rather than the main app, the fixes for a [Copilot app widget not working](/articles/copilot-app-widget-not-working/) cover the WebView, permission, and pinning checks that restore it.

### Fix 4: Get DirectML workloads onto the NPU

DirectML is the bridge between AI apps and the NPU, and it only accelerates work when the app, the driver, and the runtime all target the same hardware. A mismatch anywhere sends work to the CPU.

1. Confirm the app version you run actually supports NPU execution on Intel Core Ultra, checking its release notes.
2. Update the Intel graphics and NPU drivers as in Fix 2, since DirectML depends on them for NPU access.
3. In the app's settings, look for an execution provider or device option and select the NPU or DirectML device explicitly rather than leaving it on Auto.
4. Run a test workload while watching the NPU tile in Task Manager to confirm utilization rises above zero.
5. If the app still runs on the CPU, the detailed walkthrough for [DirectML slow performance on the NPU](/articles/npu-directml-slow-performance/) explains the runtime and driver combinations that actually deliver acceleration.

### Fix 5: Fix VPN interference with Copilot and AI services

VPN software is a frequent hidden cause of Copilot failures, because Copilot needs both cloud connectivity and local service access. A VPN that blocks either one makes AI features fail in ways that look like hardware problems.

1. Disconnect the VPN completely and test Copilot immediately; if it works, the VPN is the cause.
2. If your VPN has split tunnelling, add Copilot and Microsoft services to the bypass list and retest.
3. Update the VPN client to its latest version, since ARM and NPU-era network changes have broken older clients.
4. If the VPN fails to connect at all on this laptop, check whether its filter driver conflicts with Windows security features and reinstall the client cleanly.
5. For ExpressVPN users, the specific fixes for [ExpressVPN not working on ARM64 Windows](/articles/expressvpn-arm64-windows-not-working/) cover the driver and protocol settings that restore connectivity without disabling protection.

### Fix 6: Repair power profiles and Windows AI components

If everything above checks out but AI work is still slow, power throttling or a damaged Windows AI runtime is likely. Both are fixable without a full reset.

1. Open MSI Center and set the performance profile to Balanced or Performance, not Silent or Super Battery.
2. In Windows Settings, go to System, then Power and battery, and set Power mode to Best performance for testing.
3. Run Windows Update until no updates remain, then restart and retest AI performance.
4. If problems persist, run System File Checker by opening Terminal as administrator and typing sfc /scannow, then restart.
5. As a final software step, perform an in-place Windows 11 repair install from the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), keeping files and apps.
6. After the repair, reinstall the Intel drivers once more and test Copilot and DirectML workloads before restoring any aggressive power profile.

## Closing

MSI Summit 13 AI Evo issues usually come down to one of three things: an Intel driver that lost the NPU, a Copilot app that needs resetting, or a network tool quietly blocking AI traffic. The fixes above address them in the order that wastes the least of your time. If the NPU still does not appear after clean Intel drivers, contact MSI support with your exact model — that is the one result that points beyond software.
