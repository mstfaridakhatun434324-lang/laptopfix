---
title: "Audio Driver Keeps Crashing? What to Do About It"
slug: what-to-do-if-audio-driver-keeps-crashing
date: 2026-09-04
categories: ["drivers"]
tags: ["audio driver", "driver crash", "realtek", "blue screen", "sound fix"]
description: "Sound cuts out, stutters, or crashes the system repeatedly? Stabilize a crashing audio driver with this ordered diagnostic and repair sequence."
thumbnail: "/images/thumbs/what-to-do-if-audio-driver-keeps-crashing.webp"
faqs:
  - q: "What does it mean when an audio driver 'crashes'?"
    a: "It means the driver software controlling your sound hardware fails repeatedly — symptoms range from audio cutting out for seconds, to the sound device vanishing from Windows, to full system freezes or blue screens naming the audio driver. The driver restarts itself each time, which is why sound comes and goes."
  - q: "Can a crashing audio driver cause blue screens?"
    a: "Yes. Audio drivers run in kernel mode, so a serious bug can take down the whole system — typically with stop codes like SYSTEM_THREAD_EXCEPTION_NOT_HANDLED or DRIVER_IRQL_NOT_LESS_OR_EQUAL naming files like RTKVHD64.sys. If your crashes include blue screens, treat the audio driver as the prime suspect."
  - q: "Why does my audio driver crash only in certain apps?"
    a: "Different apps use different audio APIs and formats. A game using exclusive-mode surround or a DAW requesting low-latency ASIO stresses driver paths that YouTube never touches. App-specific crashes point to a format, sample rate, or exclusive-mode conflict rather than a totally broken driver."
  - q: "Should I use the driver from Windows Update or the manufacturer?"
    a: "For audio, the laptop manufacturer's driver almost always wins. Windows Update's generic drivers are safe but stripped of the vendor customizations the hardware expects, and mismatches are a leading cause of instability. Download audio drivers from your laptop maker's support page."
---

An audio driver that keeps crashing is worse than one that's simply broken — broken is at least predictable. Crashing means sound that cuts in and out, devices that vanish and reappear, apps that freeze when they touch audio, and in bad cases blue screens with the audio driver's name on them. It feels random, but driver crashes have causes, and causes can be eliminated one by one.

The pattern matters: crashes tied to specific apps, formats, or power states point at configuration; crashes that happen constantly, everywhere, point at the driver binary itself. This guide covers both.

## Why this happens

- **A corrupted driver binary.** Partial updates, interrupted installs, or disk errors can leave a driver that loads but fails under load. This is the most common cause of chronic crashing.
- **Driver/OS version mismatch.** A driver written for an older Windows build running on a new feature update can crash when it calls changed kernel interfaces.
- **Conflicting audio software.** Multiple enhancers, virtual audio cables, or VoIP apps installing their own audio drivers can destabilize the whole audio stack.
- **Faulty audio enhancements.** Real-time processing (bass boost, virtualization) that the driver can't handle reliably can crash the driver when specific content plays.
- **Hardware resource conflicts.** IRQ or memory conflicts, especially after hardware changes or BIOS updates, can make a healthy driver crash.
- **Failing audio hardware.** A dying codec chip or damaged traces can produce errors the driver can't recover from — the driver crashes because the hardware lies to it. Compare [audio that crackles but never crashes](/articles/how-to-fix-realtek-audio-not-working-in-windows-11-24h2/).
- **Overheating or power instability.** Thermal throttling and voltage droop under load can corrupt driver state, producing crashes that only happen during heavy use.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Capture the crash pattern

Diagnosis before surgery — the pattern picks the fix.

1. Note exactly when crashes happen: specific apps, specific audio (games? video calls?), on battery vs. plugged in, and whether the system blue-screens or just loses sound.
2. Check **Event Viewer** (Win + X > Event Viewer) > **Windows Logs** > **System**. Filter for **Error** events around crash times and look for the audio driver's filename (e.g., RTKVHD64.sys, IntcAzAud.sys).
3. If blue screens occur, note the stop code and the named file. Photograph the screen if it flashes by too fast.
4. Check **Reliability Monitor** (search for it in Start) — it gives a timeline of crashes that's easier to read than Event Viewer.

### Fix 2: Strip the audio path to basics

Remove every processing layer that could be crashing the driver.

1. Right-click the speaker icon > **Sound settings** > **More sound settings**. Select your device > **Properties** > **Enhancements** tab > check **Disable all enhancements**.
2. On the **Advanced** tab, set **Default Format** to **16 bit, 44100 Hz (CD Quality)** — the most compatible format — and uncheck both **Exclusive Mode** boxes.
3. Uninstall third-party audio software temporarily: virtual cables, VoIP driver add-ons, EQ apps, recording software drivers.
4. Retest under the conditions that used to crash. If crashes stop, reintroduce components one at a time to find the trigger.

### Fix 3: Roll back or clean-reinstall the driver

The core repair for a corrupted or mismatched driver.

1. Open **Device Manager** > **Sound, video and game controllers**. Right-click the audio device > **Properties** > **Driver** tab.
2. If **Roll Back Driver** is available (not grayed out), use it — this restores the pre-update driver that was presumably stable. Restart and test.
3. If rollback isn't available or doesn't help: **Uninstall device** with "Attempt to remove the driver" checked, then restart.
4. Download the audio driver for your exact model from the manufacturer's support page and install it as administrator — for AMD-based systems, [AMD's driver page](https://www.amd.com/en/support/download/drivers.html) covers chipset-side audio components.
5. Do not let Windows Update immediately replace it; test stability first (see Fix 6 for blocking driver replacement).

### Fix 4: Update the surrounding stack

Audio drivers don't crash in isolation — the chipset, BIOS, and OS matter.

1. Install all pending **Windows Updates** — cumulative updates regularly include kernel fixes that stabilize third-party drivers.
2. Update the **chipset driver** from your laptop manufacturer's support page. The audio codec talks to the CPU through the chipset; chipset bugs manifest as audio crashes.
3. Check for a **BIOS/UEFI update** for your model. BIOS updates fix hardware initialization bugs that drivers trip over — but only update BIOS on AC power and never interrupt it.
4. Update the **graphics driver** too — HDMI/DisplayPort audio endpoints live in the GPU driver and can destabilize the audio stack. Our [NVIDIA crash guide](/articles/how-to-fix-nvidia-driver-crashing-after-windows-11-update/) covers GPU-side audio faults.

### Fix 5: Check for hardware and thermal causes

When software fixes don't stabilize the crashes.

1. Monitor temperatures with **HWiNFO** or similar during the workload that crashes. Audio-adjacent crashes under heat point to thermal throttling corrupting driver state — clean the vents and check fans.
2. Run **Windows Memory Diagnostic** (search in Start) — bad RAM corrupts drivers in memory and produces "random" crashes across different drivers.
3. Test with an external **USB audio adapter** (even a cheap one). If crashes vanish with USB audio, the internal codec or its connection is suspect.
4. If crashes follow the internal audio across driver versions and a clean Windows install, the codec hardware is likely failing — a motherboard-level issue.

### Fix 6: Prevent recurrence

Stability you have to defend, because Windows Update will try to "fix" it.

1. Once stable, open **Device Installation Settings** (System > About > Advanced system settings > Hardware) and set it to **No** so Windows doesn't auto-replace your working audio driver.
2. Use the **Show or hide updates** troubleshooter to hide audio driver updates specifically.
3. Record the stable driver version somewhere — when a future update breaks things again, you'll know exactly what to roll back to.
4. Keep a copy of the working driver installer in a folder on the laptop. Future-you will be grateful.

### Fix 7: Repair or reinstall Windows as a last resort

For crashes that survive everything above.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` in an admin Terminal to repair OS-level corruption.
2. Try an **in-place upgrade**: download the Windows 11 ISO, mount it, and run setup choosing "Keep personal files and apps." This reinstalls Windows without wiping your data and fixes deep system corruption.
3. Only as a final step, do a clean Windows install, then install drivers strictly in order: chipset, then audio, then the rest — testing audio stability after each.
4. If crashes persist on a clean install with manufacturer drivers, it's hardware. No software fix remains.

Microsoft documents driver and blue-screen troubleshooting on the official [Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

A crashing audio driver is telling you something specific — you just have to read the pattern. Capture when and how it crashes, strip the audio path to basics, then rebuild the driver stack cleanly from the manufacturer's packages: audio driver, chipset, BIOS, OS updates. Most chronic audio crashes end at Fix 3. The ones that don't have identified themselves as hardware or deep OS corruption, and now you know which.
