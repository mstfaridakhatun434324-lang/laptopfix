---
title: "Your PC Ran Into a Problem? What to Do Next (Blue Screen Guide)"
slug: what-to-do-if-your-pc-ran-into-a-problem
date: 2026-09-13
categories: ["windows-errors"]
tags: ["pc ran into a problem", "bsod", "blue screen", "stop code"]
description: "Seeing 'Your PC ran into a problem and needs to restart'? Don't panic — here's exactly what to do, how to read the stop code, and the fixes that work."
thumbnail: "/images/thumbs/what-to-do-if-your-pc-ran-into-a-problem.webp"
faqs:
  - q: "What should I do first when I see this blue screen?"
    a: "Read the stop code at the bottom of the screen and photograph it with your phone — that's your diagnosis. Let the percentage counter finish so Windows can write a crash dump. Then restart normally; a one-off crash after an update or driver install often never returns. Only start troubleshooting if it happens again."
  - q: "Does this blue screen mean I lost my files?"
    a: "Almost certainly not. The blue screen stops Windows to protect your data, and the restart that follows doesn't delete anything. Your files are at risk only if the underlying cause is a dying drive — which is why checking drive health is part of the fix sequence — not from the crash itself."
  - q: "Why does it say it's collecting error info?"
    a: "Windows is writing a memory dump file (MEMORY.DMP or a minidump) containing the state of the system at the crash moment. Technicians analyze these dumps with tools like WinDbg to identify the exact failing driver or component. The percentage counter shows the dump's progress — let it reach 100% before forcing anything."
  - q: "How do I stop it from happening again?"
    a: "Fix the root cause rather than the symptom: update or roll back the driver named in the dump, uninstall the update that preceded the crashes, test your RAM and drive, and keep Windows current. Also disable automatic restart temporarily so future crashes show you the stop code instead of rebooting past it."
---

"Your PC ran into a problem and needs to restart." It's the friendliest possible wording for a system crash, and the least informative. That blue screen — with its sad emoticon and a percentage counter — is Windows' last resort: something went wrong at a level it couldn't recover from, so it stopped everything, wrote down what happened, and restarted. The screen gives you one genuinely useful piece of information: the stop code near the bottom (like MEMORY_MANAGEMENT or DRIVER_IRQL_NOT_LESS_OR_EQUAL). Everything in this guide starts from that code.

First, the reassurance: your files are fine. A blue screen is a protective stop, not a data wipe. Second, the mindset: one crash is an incident, two is a pattern. If this just happened once after an update or a new driver, restart and carry on — but photograph the stop code first in case it returns. If it's recurring, the fixes below take you from reading the code to resolving the cause, in the right order. For the specific case where the message names no code at all, see our [follow-up guide](/articles/how-to-fix-your-pc-ran-into-a-problem-after-windows-11-update/); to keep future crashes visible instead of auto-rebooting, see our [disable automatic restart guide](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/).

## Why this happens

- **Faulty drivers**: The number one cause — a driver accessing memory or hardware incorrectly forces the protective stop.
- **Bad Windows update**: Updates replace kernel files and drivers; a buggy or interrupted update destabilizes the system.
- **Failing RAM**: Memory errors corrupt whatever Windows is doing at that moment, producing varied, confusing stop codes.
- **Dying storage**: Bad sectors in system areas cause crashes that look random but aren't.
- **Overheating**: Thermal shutdowns under load can present as blue screens, especially on gaming laptops with clogged cooling.
- **Overclocking**: Unstable CPU, GPU, or RAM overclocks are a classic source of recurring crashes.
- **Malware**: Deep infections that hook kernel functions can trigger protective stops.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Capture the stop code and check for a pattern

Diagnosis before action — five minutes here saves hours later.

1. Photograph the blue screen with your phone, capturing the stop code (the ALL_CAPS phrase near the bottom) and any named file (like `nvlddmkm.sys`).
2. Let the percentage counter reach 100% so the crash dump is written completely.
3. After restarting, ask: did this start after an update, a new driver, new hardware, or new software? The answer points at the cause.
4. Open **Event Viewer** > **Windows Logs** > **System** and look for **BugCheck** entries — they record every stop code with timestamps, revealing whether it's one code repeating or many different ones (many different codes strongly suggests RAM or drive hardware).

### Fix 2: Boot into Safe Mode to isolate the cause

Determine whether third-party software is involved.

1. If Windows boots normally, press **Windows + R**, type `msconfig`, go to the **Boot** tab, tick **Safe boot** > **Minimal**, restart — or interrupt boot three times to reach recovery and choose Safe Mode.
2. If the system is stable in Safe Mode, a third-party driver or program is the trigger — proceed to Fix 4.
3. If it crashes in Safe Mode too, suspect system files or hardware — prioritize Fixes 3 and 6.
4. Remember to untick **Safe boot** in msconfig afterward, or you'll boot into Safe Mode every time.

### Fix 3: Roll back the recent change

Undo whatever preceded the crashes.

1. **If it started after a Windows update**: **Settings** > **Windows Update** > **Update history** > **Uninstall updates**, and remove the most recent one. Check [Microsoft's support pages](https://support.microsoft.com/en-us/windows) for known issues with that update.
2. **If it started after a driver update**: **Device Manager** > right-click the device > **Properties** > **Driver** > **Roll Back Driver**.
3. **If it started after new software**: **Settings** > **Apps** > **Installed apps**, sort by install date, and remove the newest additions — antivirus trials and system utilities first.
4. **If it started after new hardware**: remove or reseat the hardware and test. New RAM is the most common hardware trigger.

### Fix 4: Update or reinstall the suspect driver

A named file on the blue screen tells you exactly which driver to fix.

1. If the blue screen named a `.sys` file, identify its owner: `nvlddmkm.sys` is NVIDIA, `atikmdag.sys` is AMD, `rtwlanu.sys` is Realtek Wi-Fi, and so on.
2. Download the latest driver from the manufacturer's site — not from Windows Update — and do a clean install (NVIDIA and AMD installers both offer a "clean installation" checkbox).
3. Get a fresh Windows image with [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) if you suspect the installed driver store itself is damaged.
4. If no file was named, update the big three anyway: graphics, chipset, and network drivers — they cause the majority of unnamed crashes.

### Fix 5: Repair system files

Corrupted Windows components cause crashes that look random.

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`, then run SFC once more.
3. Restart and monitor. If crashes persist with the same stop code after clean SFC/DISM runs, the cause is almost certainly a driver or hardware, not Windows itself.

### Fix 6: Test memory and storage

Rule out the hardware that produces "random" crashes.

1. Run Windows Memory Diagnostic: **Windows + R** > `mdsched.exe` > **Restart now and check for problems**.
2. Run `chkdsk C: /f /r` from an administrator prompt (schedule at restart) to find bad sectors.
3. Run your laptop vendor's built-in diagnostics (**F12** > **Diagnostics** on Dell, **F2** on HP) for a manufacturer-grade drive and memory test.
4. Replace failing RAM or drives promptly — continued use risks actual data loss, unlike the crashes themselves.

### Fix 7: Check thermals and reset overclocks

Heat and unstable clocks crash systems under load.

1. Install a monitoring tool like HWMonitor and watch CPU/GPU temperatures during normal use and under load — sustained CPU temps above 95°C or GPU above 90°C indicate a cooling problem.
2. Clean vents and fans with compressed air; on older laptops, dried thermal paste may need professional replacement.
3. Reset any CPU, GPU, or RAM overclocks (including XMP profiles) to stock in the BIOS/UEFI and vendor utilities.
4. If crashes only happen in games or heavy apps and thermals are fine, the GPU driver is the prime suspect — return to Fix 4.

## Closing

The "your PC ran into a problem" screen is the beginning of a diagnosis, not a verdict. The stop code tells you the category, the timing tells you the trigger, and the sequence above — capture, isolate, roll back, update drivers, repair files, test hardware — resolves the overwhelming majority of cases without reinstalling Windows. Keep that phone photo of the stop code; if the crash ever returns months later, comparing codes tells you instantly whether it's the same problem or a new one. And remember the cardinal rule of blue screens: fix the cause, not the crash — suppressing the symptom while the driver or dying drive remains guarantees a sequel.
