---
title: "How to Fix \"Your PC Ran Into a Problem\" — Step by Step"
slug: how-to-fix-your-pc-ran-into-a-problem-step-by-step
date: 2026-10-13
categories: ["windows-errors"]
tags: ["bsod", "troubleshooting", "windows-11"]
description: "\"Your PC ran into a problem\" blue screen? Follow this complete step-by-step walkthrough to diagnose the stop code and fix it for good."
thumbnail: "/images/thumbs/how-to-fix-your-pc-ran-into-a-problem-step-by-step.webp"
faqs:
  - q: "What does 'Your PC ran into a problem' mean?"
    a: "It's the friendly face of a Windows stop error (blue screen). Windows hit a critical fault it couldn't recover from — usually a bad driver, corrupted system files, or failing hardware — and restarted to protect itself. The stop code shown at the bottom (like MEMORY_MANAGEMENT) identifies the specific problem."
  - q: "Will I lose my files from this blue screen?"
    a: "The blue screen itself doesn't delete files. The risk is indirect: repeated crashes can corrupt open documents or, over time, the file system. Save your work frequently until the crashes stop, and every fix in this guide preserves your personal files."
  - q: "How do I find the actual error behind the message?"
    a: "Photograph the screen — the stop code is printed near the bottom. After rebooting, open Event Viewer (eventvwr.msc) > Windows Logs > System and look for the BugCheck entry, or check C:\\Windows\\Minidump for crash dumps analyzable with WinDbg Preview."
  - q: "How often is 'Your PC ran into a problem' a hardware failure?"
    a: "Less often than people fear. Roughly speaking, drivers and software cause the majority of cases; genuine hardware failure (RAM, SSD, overheating) accounts for a meaningful minority. That's why this guide starts with software — it's the likely culprit and the cheapest to fix."
---
"Your PC ran into a problem and needs to restart." The sad face, the percentage counter, the reboot. It's the most-seen error screen in Windows, and also the least informative — because the same screen appears for dozens of different underlying faults.

This guide is the full step-by-step walkthrough: capture the real error, work the software causes in order, check the hardware, and know when you've fixed it. Follow it top to bottom and don't skip the evidence-gathering steps — they're what turn guessing into diagnosing.

## Why this happens

- **Faulty or corrupted driver** — the single most common cause across all stop codes.
- **Corrupted Windows system files** — from failed updates, disk errors, or malware.
- **Failing RAM** — memory errors that surface as various stop codes.
- **Failing SSD or hard drive** — bad sectors corrupting drivers and system files.
- **Overheating** — thermal instability under load crashing the CPU or GPU.
- **Bad Windows update** — an update that installed badly or shipped a buggy driver.
- **Third-party software with kernel drivers** — antivirus, VPNs, "optimizers" hooking into the system.
- **Overclocking or unstable firmware settings** — pushed hardware faulting under stress.

## How to fix it

Work through these in order. The early steps gather information; the middle steps fix software; the later steps check hardware.

### Fix 1: Capture the stop code

Everything downstream depends on this.

1. The next time the blue screen appears, photograph it with your phone — capture the stop code (e.g., DRIVER_IRQL_NOT_LESS_OR_EQUAL) and any driver file named in parentheses.
2. After the reboot, press **Windows + R**, type `eventvwr.msc`, go to **Windows Logs** > **System**, and find the **BugCheck** error — it records the stop code and parameters permanently.
3. If crashes are frequent, disable automatic restart so the screen stays up: **Settings** > **System** > **About** > **Advanced system settings** > **Startup and Recovery** > **Settings** > uncheck **Automatically restart**.
4. Write down the code — a specific stop code turns this generic guide into a targeted repair (search our site for the exact code).

### Fix 2: Boot into Safe Mode and observe

Safe Mode loads only essential drivers — if crashes stop there, it's a third-party driver or startup program.

1. Go to **Settings** > **System** > **Recovery** > **Advanced startup** > **Restart now**.
2. **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, press **4** for Safe Mode.
3. Use the laptop in Safe Mode for a while. Stable? The culprit loads only in normal mode — proceed to Fix 3.
4. Crashing in Safe Mode too? Skip to Fix 5 — the problem is in core Windows or hardware.

### Fix 3: Update or roll back drivers

The highest-yield repair step.

1. In normal or Safe Mode, open **Device Manager** (**Windows + X**).
2. Look for yellow warning icons first — those devices get priority.
3. For the likely suspects (**Display adapters**, **Network adapters**, **Storage controllers**): right-click > **Properties** > **Driver** tab. If crashes started recently, **Roll Back Driver**; otherwise **Update driver** > **Search automatically for drivers**.
4. Get proper drivers from your laptop maker's support site for your exact model — they beat Windows Update's generic versions for stability.
5. Restart and test for a day or two before declaring victory — some driver bugs are intermittent.

### Fix 4: Remove recently installed software and updates

Undo recent changes systematically.

1. **Settings** > **Apps** > **Installed apps** — sort by install date. Uninstall anything added around when crashes began, especially antivirus trials, VPN clients, driver updaters, and "optimizers."
2. **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — remove the most recent quality update as a test if timing aligns.
3. **Settings** > **Apps** > **Startup** — disable everything non-essential and test.
4. Reintroduce things one at a time over several days; when crashes return, you've found the trigger.

### Fix 5: Repair Windows system files

Fix corruption in the OS itself.

1. Open **Terminal (Admin)** (**Windows + X**) and run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
2. Then run `sfc /scannow` and let it complete.
3. Run `chkdsk C: /f` (schedule at restart if prompted) to verify the file system.
4. Restart and monitor. If SFC finds corruption it can't fix repeatedly, suspect the drive (Fix 7).

### Fix 6: Test the RAM

Hardware check number one.

1. Press **Windows + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
2. For conclusive results, run MemTest86 from a bootable USB — at least one full pass, ideally more.
3. Errors mean reseating the sticks (power off, unplug, open the laptop, reseat firmly) and retesting; replace sticks that keep failing.
4. Also reset any memory overclocking (XMP) in BIOS to stock speeds as a test.

### Fix 7: Check drive health and temperatures

Hardware checks two and three.

1. In an admin Terminal: `wmic diskdrive get status` — expect **OK**. Anything else means backup immediately and replace the drive.
2. Monitor temperatures with HWMonitor during normal use and under load — sustained CPU temps near 100°C cause instability crashes.
3. Clean dust from vents with compressed air (laptop off and cool).
4. If the drive is healthy and temps are fine, hardware is likely innocent — return to software causes.

### Fix 8: Reset Windows as the final step

When the cause won't reveal itself, a fresh Windows will.

1. Back up your important files (external drive or cloud) — the Keep-my-files reset preserves data, but backups are non-negotiable before this step.
2. **Settings** > **System** > **Recovery** > **Reset PC** > **Keep my files** > **Cloud download**.
3. After the reset, install drivers from your laptop maker's site first, then Windows Update, then apps one at a time.
4. If crashes survive even a clean reset with manufacturer drivers, you're looking at a hardware fault — RAM, SSD, or board-level — and it's repair-shop time.

## Closing

"Your PC ran into a problem" is a symptom, not a diagnosis — but the diagnostic path is the same every time: capture the stop code, isolate software from hardware with Safe Mode, work the drivers, repair the OS, test the RAM and drive. Most cases end at Fix 3 or Fix 5. Once you have a specific stop code, our targeted guides take over — for example [MEMORY_MANAGEMENT after a Windows update](/articles/fix-memory-management-bsod-after-windows-11-update/) or the general [blue screen of death guide](/articles/how-to-fix-blue-screen-of-death-windows-11/). Microsoft's [blue screen troubleshooting](https://support.microsoft.com/en-us/windows) is the official companion reference.
