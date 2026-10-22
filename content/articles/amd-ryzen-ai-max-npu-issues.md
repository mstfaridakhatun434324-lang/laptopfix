---
title: "AMD Ryzen AI Max NPU Issues: Detection, Driver, and Performance Fixes"
slug: amd-ryzen-ai-max-npu-issues
date: 2026-10-22
categories: ["ai-pc"]
tags: ["amd-ryzen-ai", "npu", "xdna-2", "drivers", "ai-pc", "troubleshooting"]
description: "AMD Ryzen AI Max NPU not detected or underperforming? Fix XDNA 2 detection failures, driver problems, and slow AI performance with this step-by-step guide."
thumbnail: "/images/thumbs/amd-ryzen-ai-max-npu-issues.webp"
faqs:
  - q: "How many TOPS does the Ryzen AI Max NPU deliver?"
    a: >
      Ryzen AI Max processors, known as Strix Halo, include an XDNA 2
      NPU rated up to 50 TOPS depending on the specific SKU. If your
      system reports far less throughput in benchmarks, the cause is
      usually drivers, power policy, or app provider selection rather
      than the silicon itself.
  - q: "Where do I download Ryzen AI Max NPU drivers?"
    a: >
      From AMD's official driver download page for your exact processor,
      plus your laptop maker's support site for certified builds. Install
      the chipset driver first, then AMD's Ryzen AI Software package,
      restarting between the two installs.
  - q: "Why does Windows Update keep breaking my AMD NPU driver?"
    a: >
      Windows Update may replace AMD's newer NPU driver with an older
      inbox version it considers authoritative. After installing AMD's
      package, hide the older driver offer in optional updates or use
      update policy settings to stop driver downgrades from recurring.
  - q: "Do I need Ryzen AI Software if Device Manager shows the NPU?"
    a: >
      Detection is only half the stack. Without AMD's Ryzen AI Software
      runtime, applications cannot dispatch work to the chip. Install it
      even when Device Manager looks healthy if AI features keep ignoring
      the NPU.
---

AMD's Ryzen AI Max chips pack one of the most powerful laptop NPUs on the market — up to 50 TOPS of XDNA 2 compute — which makes it especially frustrating when Windows cannot see the chip, AI features ignore it, or performance falls far short of the spec sheet. The hardware is willing; the software stack just has not caught up on your machine.

Most Ryzen AI Max NPU problems fall into three buckets: the chip is not detected at all, the driver stack is incomplete or mismatched, or the NPU is detected but performs poorly. If your chip is simply absent from Device Manager, start with our [AMD Ryzen AI NPU not showing up](/articles/amd-ryzen-ai-npu-not-showing-up/) detection guide, then return here for the Max-specific layers.

This guide covers all three buckets in diagnostic order: confirming detection, installing AMD's full AI software stack, fixing BIOS and driver mismatches, and tuning performance. One quick sanity check before you begin: fire up any working NPU feature — even the caption pipeline discussed in our [live captions HDMI audio troubleshooting](/articles/live-captions-not-working-hdmi-audio/) article — to see whether the NPU works at all while your main workload does not.

## Why this happens

- **Missing AMD NPU (XDNA) driver:** Windows Update often installs the chipset driver but not AMD's separate NPU/IPU driver, leaving the neural processor invisible to AI runtimes.
- **Ryzen AI Software not installed:** AMD's Ryzen AI Software stack — drivers plus runtime — is a separate download; without it, detection succeeds but no application can dispatch work to the chip.
- **NPU disabled in BIOS:** Some firmware ships with the NPU or IPU device disabled by default, or a BIOS update quietly resets the toggle back to off.
- **Windows Update driver conflicts:** Windows Update can overwrite AMD's NPU driver with an older inbox version, breaking the stack silently after a reboot with no warning.
- **Outdated BIOS or AGESA:** Early firmware for Ryzen AI Max platforms had NPU enumeration bugs that were fixed in later AGESA releases — no driver can work around those.
- **App not built for XDNA 2:** Some AI applications target older XDNA or generic DirectML paths and fail to use the Max's full capability, which looks like a performance problem but is really a software-targeting one.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the NPU is detected in Windows

Start with ground truth. The Ryzen AI Max NPU should appear in Device Manager and Task Manager; if it does not, every later fix is premature. This check takes two minutes and splits the problem cleanly into detection versus performance, which need completely different fixes.

1. Open Device Manager and look under System devices or Neural processors for AMD IPU or NPU entries.
2. Open Task Manager, go to the Performance tab, and check for an NPU section.
3. If both are missing, the issue is detection — continue to Fix 2 and Fix 3.
4. If Device Manager shows the device with a warning icon, note the error code (such as Code 10 or Code 43) for later.
5. If it appears healthy but AI apps ignore it, skip ahead to Fix 4.

### Fix 2: Install AMD chipset drivers and Ryzen AI Software

The Max's NPU needs AMD's full stack, not just what Windows Update provides. AMD publishes chipset drivers and the Ryzen AI Software package separately, and installing both in the right order resolves the majority of detected-but-unusable cases.

1. Go to [AMD's driver download page](https://www.amd.com/en/support/download/drivers.html) and select your exact Ryzen AI Max processor.
2. Download and install the latest chipset driver package, then restart the laptop.
3. Download AMD's Ryzen AI Software (NPU driver plus runtime) for your platform and install it.
4. Restart again and verify the NPU appears in Device Manager without warnings.
5. Open Task Manager and confirm the NPU section now shows the device as present.

### Fix 3: Enable the NPU in BIOS and update firmware

Firmware can hide a perfectly good NPU. Check that the IPU or NPU device is enabled in BIOS, and update to firmware carrying a recent AGESA — early Ryzen AI Max BIOS versions had real enumeration bugs that no driver install can work around.

1. Restart into BIOS or UEFI setup (usually Del or F2 during boot).
2. Find the NPU, IPU, or "AI Engine" toggle — often under Advanced, then AMD CBS, or a similar menu — and set it to Enabled.
3. Check your maker's support site for a newer BIOS and note whether the release notes mention NPU or AGESA fixes.
4. Update the BIOS on AC power with all applications closed, following the maker's instructions exactly.
5. Boot into Windows and recheck Device Manager and Task Manager for the NPU.

### Fix 4: Stop Windows Update from downgrading the driver

A special frustration: you install AMD's driver, everything works, and after the next Patch Tuesday the NPU is broken again because Windows Update replaced it with an older version. Pinning the driver stops the cycle. This kind of worked-yesterday regression has cousins across Windows — the [Copilot app dark mode stuck](/articles/copilot-app-dark-mode-stuck/) issue is another case where an update quietly changed behavior — so treat update-driven regressions as a category, not a mystery.

1. After installing AMD's NPU driver, open Device Manager and note the driver version and date.
2. Go to Settings, then Windows Update, then Advanced options, and check Optional updates for any AMD NPU driver offers — skip them if they are older than yours.
3. Consider pausing driver delivery via the "do not include drivers" update setting if regressions keep repeating.
4. If a bad driver already landed, roll back: in Device Manager, open the NPU's Properties, go to the Driver tab, and choose Roll Back Driver.
5. Reinstall AMD's package after the rollback and verify the version sticks across a reboot.

### Fix 5: Clean-reinstall when the stack is tangled

Partial installs — chipset without the NPU driver, or two competing NPU drivers — create tangled stacks that no update can untangle. When the earlier fixes leave warnings or flaky behavior, tear the whole AMD AI stack down and rebuild it cleanly, a process our [AMD NPU driver update failed](/articles/amd-npu-driver-update-failed/) guide covers in extra depth for stubborn cases.

1. Download fresh copies of the chipset driver and Ryzen AI Software before you remove anything.
2. In Device Manager, uninstall every AMD IPU or NPU entry, checking "Attempt to remove the driver for this device."
3. Restart normally — use Safe Mode only if the normal uninstall leaves remnants behind.
4. Install the chipset package first, restart, then install the Ryzen AI Software, then restart again.
5. Verify clean detection in both Device Manager and Task Manager before testing AI applications.

### Fix 6: Tune for full XDNA 2 performance

A detected, driver-healthy NPU can still underperform if Windows or the application is not feeding it properly. Power policy, application provider selection, and background contention decide whether you see the Max's rated TOPS or a fraction of them.

1. Set Settings, then System, then Power and battery, then Power mode to Best performance while plugged in for benchmarking.
2. In the AI application's settings, select the NPU, XDNA, or DirectML provider explicitly rather than leaving it on Auto.
3. Close competing AI workloads such as Recall indexing or Studio Effects during performance testing.
4. Compare throughput against the application's published expectations for Ryzen AI Max — small gaps are normal, large ones are not.
5. Keep the AMD stack updated; XDNA 2 performance fixes ship regularly in new releases.

## Closing

Ryzen AI Max NPU issues look intimidating because the platform is new, but the fix pattern is familiar: confirm detection, install AMD's complete stack, keep firmware current, and stop Windows Update from "helping." Once the XDNA 2 chip is properly enumerated with matching drivers, it is one of the most capable laptop NPUs you can buy — the software just needs to get out of its way.
