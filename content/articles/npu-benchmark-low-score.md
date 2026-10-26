---

title: "NPU Benchmark Score Too Low? How to Improve It on Windows 11"

slug: "npu-benchmark-low-score"

date: 2026-10-26

categories: ["ai-pc"]

tags: ["windows-11", "npu", "ai-pc", "drivers", "troubleshooting"]

description: "Fix NPU benchmark scores on Windows 11 with this practical guide — driver checks, app repairs and settings that restore it without reinstalling Windows."

thumbnail: "/images/thumbs/npu-benchmark-low-score.webp"

faqs:

  - q: "Why is NPU benchmark scores not working on my AI laptop?"

    a: >

      Most often the cause is an outdated driver, an outdated app or a requirement that is not met, such as a Copilot+ PC, a signed-in account or a pending Windows update. Work through the driver and app checks in this guide before assuming the hardware is faulty, because software causes are far more common.

  - q: "Do I need a Copilot+ PC for NPU benchmark scores?"

    a: >

      Many on-device AI features do need a Copilot+ PC with a qualifying NPU, while others run on any modern Windows 11 laptop using the CPU or GPU. Check the feature's requirements in the app and in Task Manager to see whether your NPU is present and active.

  - q: "Will reinstalling fix NPU benchmark scores?"

    a: >

      Reinstalling helps when the app or driver installation itself is damaged, but it will not fix a missing requirement, an unsupported device or a driver problem. Try updating and repairing first, and keep a clean reinstall as a later step in this guide.

  - q: "When should I contact support about NPU benchmark scores?"

    a: >

      Contact the laptop maker or app vendor if the NPU is missing from Device Manager after a clean driver reinstall, if a firmware update failed, or if the problem affects every AI feature at once. Note your driver versions and error messages first, since support will ask for them.

---



If NPU benchmark scores has stopped working on your Windows 11 AI laptop, you are not alone, and the problem is usually fixable without replacing hardware or reinstalling Windows. A low NPU benchmark score is not always a hardware fault, but when the same laptop scores far below published results, something in drivers, power settings or background load is holding the NPU back. The good news is that most failures come from a short list of causes — drivers, app versions, settings and requirements — and each one has a straightforward check.

This feature is one of the reasons many people bought an AI laptop in the first place, because it promises to do in seconds work that used to take minutes of manual effort. When it fails, it is tempting to assume the laptop is faulty or the feature was marketing hype, but in practice the underlying hardware is rarely the problem. More often, a single update, driver or setting has drifted out of step with the rest of the system, and restoring that alignment brings the feature back.

This guide walks through the likely causes first, then works through fixes in order, from the quickest checks to a clean reinstall. Along the way you will also find related fixes, such as [surface pro 11 ai issues](/articles/surface-pro-11-ai-issues/) and [lm studio npu not working](/articles/lm-studio-npu-not-working/), which cover neighbouring AI features that share the same drivers and settings. Follow the steps in order, testing after each one, so you know exactly which fix solved it.

## Why this happens

- **Power mode limiting the NPU:** Battery saver and balanced power plans can throttle or park the NPU, so workloads run slowly or fall back to other hardware.

- **Missing runtime or framework:** Frameworks such as DirectML or ONNX Runtime need matching runtimes, and a missing or mismatched runtime produces errors even with a healthy driver.

- **NPU disabled or hidden in firmware:** A BIOS or firmware setting, or a firmware update gone wrong, can hide the NPU from Windows entirely.

- **Conflicting driver or background load:** A second AI tool, a stuck inference job or a conflicting driver version can monopolise the NPU or report misleading usage figures.

- **Outdated or corrupted NPU driver:** The NPU driver is what lets Windows and apps see and use the neural processor, so a stale, partially installed or corrupted driver breaks NPU benchmark scores first.

- **App not built to use the NPU:** Not every AI app or model targets the NPU; some default to CPU or GPU, which looks like an NPU failure when it is actually the app's design.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Repair the app or runtime

When the driver is healthy but the app still fails, the app's own runtime or installation is the next suspect, and repair is quicker than a full reinstall.

1. Open Settings, then Apps, and find the affected app.

2. Use Repair in its advanced options where available.

3. For framework tools, reinstall the matching runtime version.

4. Restart the laptop after the repair.

5. Run a small test workload to confirm the fix.

### Fix 2: Clean-reinstall the NPU driver

A driver that was updated over a broken install can stay broken, so removing it fully and installing fresh resolves problems that simple updates do not. Microsoft's own guidance at [Microsoft Windows support](https://support.microsoft.com/en-us/windows) is a good cross-check for the steps below.

1. Download the correct latest driver first, before removing anything.

2. In Device Manager, uninstall the NPU device, deleting driver software if offered.

3. Restart the laptop and let Windows redetect the hardware.

4. Install the downloaded driver and restart again.

5. Verify the NPU in Task Manager and retry NPU benchmark scores.

### Fix 3: Check firmware and BIOS settings

If the NPU is missing from Windows entirely, firmware is involved, and a BIOS update or a toggled setting may be the only fix.

1. Check the laptop maker's support page for a BIOS or firmware update.

2. Apply it only while plugged in, and do not interrupt it.

3. Enter BIOS setup and confirm any NPU or AI accelerator setting is enabled.

4. Save, exit and boot into Windows.

5. Check Device Manager and Task Manager for the NPU.

### Fix 4: Verify with Task Manager and a test workload

Finally, confirm the fix with evidence rather than a feeling: a healthy NPU should appear in Task Manager and take load during an AI task.

1. Open Task Manager and select the NPU under Performance.

2. Run a small AI workload or benchmark.

3. Watch for NPU activity rising during the task.

4. If usage stays at zero, the app may not target the NPU — check its settings.

5. Record the result so you can spot a regression later.

### Fix 5: Update the NPU driver from the vendor

Start with the driver itself, using the chip vendor or laptop maker rather than a generic updater, since NPU drivers are model-specific. For driver downloads, stick to the official vendor or laptop-maker pages linked in this guide rather than third-party driver sites.

1. Open Device Manager and expand Neural processors.

2. Note the exact NPU name and current driver version.

3. Download the latest driver from the vendor or laptop maker's support page.

4. Install it and restart the laptop.

5. Confirm the NPU appears in Task Manager without a warning icon.

### Fix 6: Set a high-performance power plan

Power saving is a quiet NPU killer, so ruling it out early prevents chasing driver problems that are really power problems.

1. Open Settings, then System, then Power.

2. Set Power mode to Best performance while plugged in.

3. Plug in the charger for testing, even if you normally run on battery.

4. Close other AI apps that might be using the NPU.

5. Retry NPU benchmark scores and compare speed or behaviour.

## Closing

Once NPU benchmark scores is working again, keep it that way by installing app and driver updates promptly, staying on a current Windows build and checking Task Manager if performance ever slips. If a future update breaks it again, you now know which checks to repeat first. For a related older fix, see [recall app exclusions not working](/articles/recall-app-exclusions-not-working/), and if the problem persists across every AI feature, treat that as a sign to check drivers and firmware as a whole rather than one app at a time.
