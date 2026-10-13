---
title: "How to Fix the 'Your PC Ran Into a Problem' Blue Screen"
slug: how-to-fix-your-pc-ran-into-a-problem-youtube
date: 2026-09-12
categories: ["windows-errors"]
tags: ["your pc ran into a problem", "blue screen", "stop code", "windows 11", "crash"]
description: "Stuck on 'Your PC ran into a problem'? Find the real stop code behind it and fix the crash with this practical troubleshooting guide."
thumbnail: "/images/thumbs/how-to-fix-your-pc-ran-into-a-problem-youtube.webp"
faqs:
  - q: "What does 'Your PC ran into a problem' actually mean?"
    a: "It's the generic message on every Windows blue screen. The useful information is the stop code printed in smaller text (like MEMORY_MANAGEMENT or DRIVER_IRQL_NOT_LESS_OR_EQUAL) and the percentage counter. The message itself tells you nothing — the stop code tells you everything."
  - q: "Where do I find the real error code?"
    a: "It's on the blue screen under the message, labeled as a 'Stop code.' After rebooting, check Event Viewer > Windows Logs > System for the bugcheck entry, or analyze C:\\Windows\\Minidump files with WinDbg for the full technical details."
  - q: "My PC restarts too fast to read the code — what do I do?"
    a: "Disable automatic restart: Control Panel > System > Advanced system settings > Startup and Recovery > Settings, then uncheck 'Automatically restart.' Next time, the blue screen stays up so you can read and photograph the stop code."
  - q: "Is 'Your PC ran into a problem' a virus?"
    a: "No — it's Windows' own crash screen, not malware. (Fake blue screens in web browsers are scams, but the real full-screen BSOD with the sad-face emoticon is a genuine Windows system crash.)"
---

**"Your PC ran into a problem and needs to restart"** is the least informative error message in Windows — it's the same sentence for a bad driver, failing RAM, a dying SSD, or a corrupted update. The message is just the cover page; the actual diagnosis is the **stop code** printed beneath it.

So step one of fixing this is always the same: **find the stop code.** Everything else follows from it. This guide shows you how to capture it, what the common ones mean, and the fix order that handles most of them. (For the Reddit-flavored discussion of this same screen, see [your PC ran into a problem — Reddit edition](/articles/how-to-fix-your-pc-ran-into-a-problem-reddit/).)

There's one more source of truth worth setting up before you troubleshoot: Reliability Monitor. Search for it in Start — it plots every crash, driver install, and update on a timeline. When you're staring at a generic "your PC ran into a problem," that timeline often reveals the trigger (like a driver update the day before crashes began) in seconds.

## Why this happens

The generic screen appears for all of these — the stop code distinguishes them:

- **Bad or outdated driver:** The most common cause overall — graphics, network, or storage drivers crashing the kernel.
- **Failing RAM:** Memory errors corrupting whatever the system is doing.
- **Disk errors or failing drive:** Corrupted reads crashing file system or boot components.
- **Corrupted Windows update:** A half-applied update leaving the system inconsistent.
- **Overheating:** Thermal instability crashing the system under load.
- **Corrupted system files:** Damaged Windows components from disk errors or interrupted updates.

## How to fix it

Work through these in order.

### Fix 1: Capture the stop code

You can't fix what you can't name. The stop code is the entire diagnosis compressed into a constant — everything downstream (which driver, which test, which fix) flows from it. Make capturing it step zero, before you change a single setting.

1. On the next blue screen, read the **Stop code** line (e.g., `CRITICAL_PROCESS_DIED`, `MEMORY_MANAGEMENT`, `INACCESSIBLE_BOOT_DEVICE`) — photograph it with your phone.
2. To stop the auto-restart: **Control Panel > System > Advanced system settings > Startup and Recovery > Settings** > uncheck **Automatically restart** > OK.
3. After rebooting, open **Event Viewer > Windows Logs > System** and find the **BugCheck** entry — it records the stop code and its parameters.
4. For the full picture, analyze `C:\Windows\Minidump` dumps with **WinDbg Preview** (`!analyze -v`).

### Fix 2: Match the stop code to its fix path

Use the code to aim your effort. Each family of stop codes has its own proven fix path — memory codes mean RAM testing, driver codes mean driver work, boot codes mean WinRE repairs. Guessing across families wastes days; the code tells you which family you're in.

- **Memory-type codes** (`MEMORY_MANAGEMENT`, `PAGE_FAULT_IN_NONPAGED_AREA`, `FAULTY_HARDWARE_CORRUPTED_PAGE`) → test RAM with `mdsched.exe` and MemTest86; see our [memory management guide](/articles/how-to-fix-memory-management-bsod-in-windows-11-24h2/).
- **Driver codes** (`DRIVER_IRQL_NOT_LESS_OR_EQUAL`, `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED`, `VIDEO_TDR_FAILURE`) → update/roll back the named driver.
- **Boot codes** (`INACCESSIBLE_BOOT_DEVICE`, `BAD_SYSTEM_CONFIG_INFO`) → WinRE boot repairs (Fix 5).
- **Update-related** (crashes started after an update) → uninstall the update (Fix 4).

### Fix 3: Update or roll back the suspect drivers

The highest-probability fix for most stop codes.

1. Open **Device Manager** and update (or roll back, if the crash followed an update) the **display**, **network**, and **storage controller** drivers.
2. Get drivers from your laptop manufacturer's support site rather than relying solely on Windows Update.
3. For graphics crashes, do a clean install with **DDU** in Safe Mode.
4. Restart and use the PC normally — including the activity that triggered the crash — to verify.

### Fix 4: Undo the last Windows update

If the timeline points at an update:

1. **Settings > Windows Update > Update history > Uninstall updates** — remove the most recent one.
2. If you can't boot: WinRE (**Troubleshoot > Advanced options > Uninstall Updates**) > remove the latest quality update, then the feature update if needed.
3. Pause updates for a week or two afterward.

### Fix 5: Repair boot and system files

For crashes at startup or with boot-related codes, from WinRE Command Prompt:

1. `bootrec /fixmbr`, `bootrec /fixboot`, `bootrec /rebuildbcd` (answer **Y**).
2. `sfc /scannow /offbootdir=X:\ /offwindir=X:\Windows` (your drive letter).
3. `chkdsk X: /r` for disk-level damage.
4. Restart and test after each major step.

### Fix 6: Test RAM and drive health

When the stop code is memory- or storage-flavored, prove the hardware.

1. RAM: `mdsched.exe` first, then **MemTest86** for one full pass if needed.
2. Drive: `chkdsk C: /f`, plus SMART check via `wmic diskdrive get status` or the manufacturer's boot diagnostics.
3. Replace what fails — software can't fix bad hardware.

### Fix 7: Strip third-party software

1. Uninstall third-party antivirus, VPNs, and "optimizer" tools — their kernel drivers cause a disproportionate share of generic-looking crashes.
2. In **Task Manager > Startup apps**, disable non-Microsoft entries; in **msconfig > Services**, hide Microsoft services and disable the rest, then re-enable in groups.
3. Test stability for a day or two.

### Fix 8: In-place upgrade repair as the comprehensive fix

When the cause remains elusive:

1. Download the Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, run **setup.exe**.
2. Choose **Keep personal files and apps**.
3. This reinstalls Windows cleanly over itself — fresh system files, fresh driver stack, update components rebuilt — resolving most mystery crashes in one shot.

## Closing

"Your PC ran into a problem" is Windows saying *something* broke without telling you what — so your first job is always capturing the stop code, and your second is letting that code direct the fix. Resist the urge to reinstall Windows immediately: most of these crashes are a driver, an update, or a memory issue with a targeted fix. Work the code, not the generic message, and you'll fix it faster with far less disruption. And photograph every blue screen. Future-you will thank present-you when the third crash shows a different code and you can compare — patterns across multiple codes (all memory-flavored, all driver-flavored) are themselves a diagnosis.
