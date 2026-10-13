---
title: "System Thread Exception Not Handled: The Full Step-by-Step Fix"
slug: how-to-fix-system-thread-exception-not-handled-step-by-step
date: 2026-10-11
categories: ["windows-errors"]
tags: ["bsod", "stop code", "drivers", "troubleshooting"]
description: "A complete numbered walkthrough for SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — from capturing the failing driver name to verifying the fix holds."
thumbnail: "/images/thumbs/how-to-fix-system-thread-exception-not-handled-step-by-step.webp"
faqs:
  - q: "What does SYSTEM_THREAD_EXCEPTION_NOT_HANDLED actually mean?"
    a: "A thread running in kernel mode — usually inside a driver — hit an error it had no handler for, so Windows stopped the system to prevent corruption. In plain terms: a driver crashed hard. The fix is finding which driver and updating, rolling back, or removing it."
  - q: "Do I need special tools to diagnose this?"
    a: "No. The blue screen itself often names the failing driver file, and Windows saves a minidump to C:\\Windows\\Minidump after every crash. Those two sources are enough to identify the culprit without installing anything."
  - q: "What if I can't boot into Windows at all?"
    a: "Use Safe Mode or the recovery environment. Interrupt the boot three times to reach Automatic Repair, then Troubleshoot, Advanced options, Startup Settings, Restart, and press 4. From Safe Mode you can roll back drivers, uninstall updates, and run repairs."
  - q: "How long does the full fix take?"
    a: "Identifying the driver takes 10 minutes. The fix itself — a driver update or rollback — takes another 10-20 minutes plus a restart. The verification step (a day or two of normal use) is what takes the longest, but it's what proves the crash is really gone."
---

This is the complete, nothing-skipped walkthrough for `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED`. If other guides gave you fragments — "update your drivers" with no clue which one — this is the version that starts from the crash itself, identifies the failing driver by name, fixes it, and then proves the fix worked. Every step says exactly what to click and what success looks like.

Grab a pen or keep your phone handy: step 1 asks you to capture one detail from the blue screen, and everything after gets easier because of it.

## Why this happens

- **A driver threw an unhandled exception**: The literal meaning. Drivers for graphics cards, Wi-Fi adapters, audio chips, and storage controllers are the usual offenders — they run in kernel mode, so their crashes take down the system.
- **Driver and Windows version mismatch**: A driver written for an older Windows build can hit code paths that behave differently after a feature update, triggering exceptions the driver never expected.
- **Corrupted driver installation**: Interrupted updates or disk errors leave driver files inconsistent. The driver loads, hits the damaged section, and crashes without handling it.
- **Conflicting software at the driver level**: Antivirus filters, VPN drivers, and virtualization tools modify system behavior that other drivers depend on. The resulting exception gets blamed on whichever driver crashed first.
- **Overclocked or overheating hardware**: Unstable CPU/RAM overclocks and thermal problems cause the kind of low-level faults that drivers can't handle gracefully.
- **Failing hardware**: Bad RAM, a dying SSD, or a failing GPU produces errors beneath the driver layer. The driver throws its hands up — the unhandled exception — and Windows blue-screens.

## How to fix it

Follow these steps in order. Each one ends with a checkpoint.

### Fix 1: Capture the failing driver's name

**What to do:** The next time the blue screen appears (or from your memory of the last one), look for a line like "What failed: **drivername.sys**" beneath the stop code.

**Why:** That filename identifies the exact driver. `nvlddmkm.sys` means NVIDIA graphics, `Netwtw12.sys` means Intel Wi-Fi, `rtkvhd64.sys` means Realtek audio. Write it down — it turns the rest of this guide from guesswork into a targeted repair.

**If you missed it:** Open `C:\Windows\Minidump` in File Explorer, find the newest `.dmp`, and analyze it using [how to check minidump files on Windows 11](/articles/how-to-check-minidump-files-on-windows-11/).

**Checkpoint:** You have a driver filename written down. If no filename exists anywhere, proceed anyway — Fix 4 covers the blind approach.

### Fix 2: Boot into Safe Mode

**What to do:** Safe Mode loads only essential drivers, giving you a stable workspace.

1. Hold **Shift** and click **Restart** from the sign-in screen (or force Automatic Repair by interrupting boot three times).
2. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. Press **4** for Safe Mode (or **5** for Safe Mode with Networking if you need to download drivers).

**Checkpoint:** You're at the Safe Mode desktop. Everything from here happens in this stable environment.

### Fix 3: Update the identified driver

**What to do:**

1. Press **Win + X** and open **Device Manager**.
2. Find the device matching your driver filename (Display adapters for graphics .sys files, Network adapters for Wi-Fi ones).
3. Right-click it, choose **Update driver** > **Search automatically for drivers**.
4. If Windows finds nothing, download the driver manually from the hardware vendor — [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), [Intel](https://www.intel.com/content/www/us/en/support/detect.html) — or your laptop manufacturer's support page for your exact model.
5. Restart normally.

**Checkpoint:** Test the activity that used to crash (gaming, video calls, sleep/wake). Stable for a few hours? You're likely done — skip to Fix 8 to verify long-term.

### Fix 4: Roll back the driver (when you don't know which one, or the update is new)

**What to do:**

1. In **Device Manager**, check the **Driver** tab of your graphics, network, and audio devices in turn.
2. Where **Roll Back Driver** is available and the date matches when crashes began, click it, choose a reason, and restart.
3. Prioritize in this order: display adapter, network adapter, audio, storage controller.

**Checkpoint:** If rolling back one specific driver stops the crashes, you've found it. Block Windows Update from reinstalling the bad version (see Fix 7).

### Fix 5: Remove software that installs conflicting drivers

**What to do:**

1. In Safe Mode (or normal mode if stable), open **Settings** > **Apps** > **Installed apps**.
2. Uninstall third-party antivirus, VPN clients, disk tools, and "tune-up" utilities.
3. Use each vendor's official removal tool — filter drivers survive ordinary uninstalls.
4. Restart.

**Checkpoint:** A full day without crashes after removal confirms the conflict.

### Fix 6: Repair Windows system files

**What to do:** In an elevated Command Prompt or Terminal:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

then:

```cmd
sfc /scannow
```

Restart when both finish.

**Checkpoint:** SFC reports no integrity violations (or reports it fixed them). Corrupted system files are off the suspect list.

### Fix 7: Stop Windows Update from reinstalling the bad driver

**What to do:**

1. After a successful rollback, go to **Settings** > **Windows Update** > **Advanced options**.
2. Turn off **Receive updates for other Microsoft products** temporarily if driver updates keep appearing under optional updates — decline the driver ones.
3. For stubborn cases, use Microsoft's "Show or hide updates" troubleshooter to hide the specific driver update.

**Checkpoint:** A week passes with no driver reinstall and no crashes.

### Fix 8: Verify with a stress test and declare victory

**What to do:**

1. Deliberately do the thing that used to crash — game for an hour, run a video call, sleep and wake the laptop five times.
2. Check `C:\Windows\Minidump` for any new dump files. None means no crashes occurred.
3. Run Windows Memory Diagnostic (**Win + R** > `mdsched.exe`) once for completeness — memory faults mimic driver crashes.

**Checkpoint:** No new dumps, no crashes under deliberate stress. The fix is verified, not assumed.

## Closing

The step-by-step discipline is what makes this work: name the driver, fix that driver, prove it's fixed. Skipping straight to "update everything" wastes time and can introduce new problems. If you're hitting this on an HP specifically, the [HP-focused version](/articles/how-to-fix-system-thread-exception-not-handled-on-hp-laptop/) adds vendor-specific steps, and for a related kernel crash see [how to fix unexpected kernel mode trap](/articles/how-to-fix-unexpected-kernel-mode-trap-step-by-step/).
