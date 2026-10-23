---
title: "How to Fix Microsoft Defender Slowing Down Your ARM Laptop"
slug: defender-arm-laptop-performance
date: 2026-10-23
categories: ["ai-pc"]
tags: ["defender", "performance", "arm laptop", "antimalware", "slow pc", "exclusions"]
description: "Microsoft Defender making your ARM laptop slow? Fix high CPU from Antimalware Service Executable with scan scheduling, exclusions, and ARM-specific tuning."
thumbnail: "/images/thumbs/defender-arm-laptop-performance.webp"
faqs:
  - q: "Why is Antimalware Service Executable using so much CPU on my ARM laptop?"
    a: >
      It is usually a real-time scan stuck on a large or constantly-changing file set — developer folders, AI model directories, or a download in progress. Adding targeted process and folder exclusions for trusted workloads drops the CPU usage without disabling protection.
  - q: "Is it safe to add Defender exclusions on a Copilot+ PC?"
    a: >
      Yes, when done narrowly: exclude specific trusted processes or folders, never whole drives, and never exclude temp or download directories. Exclusions are the officially supported way to fix performance conflicts with known-good software.
  - q: "Should I disable Defender and install a third-party antivirus on ARM?"
    a: >
      Rarely worth it. Most third-party AV products are x86-emulated on ARM and perform worse than native Defender, while adding their own conflicts. Tune Defender first; replacement is almost never the faster path.
  - q: "Can Defender scheduled scans wake my ARM laptop?"
    a: >
      Yes, if scheduled outside active hours with wake timers allowed. Set scans inside your active hours or disable wake for the scan task in Task Scheduler to stop the laptop warming up in your bag overnight.
---

Your Snapdragon laptop felt instant out of the box; now folders stutter, builds crawl, and Task Manager shows Antimalware Service Executable camped at 20-40% CPU. The instinct is to blame the ARM chip — but the chip is fine. Defender's real-time protection is re-scanning the same files over and over, and on ARM the cost of each scan is amplified by emulation layers and NPU-adjacent workloads competing for the same cores.

On Copilot+ PCs the pattern is sharpest: large AI model files, inference tools writing constantly to cache directories, and toolchains with thousands of small files create exactly the workload Defender handles worst. The fix is not disabling protection — it is aiming it with exclusions, scheduling, and ARM-specific settings.

This guide gives you six fixes in order: identifying what Defender is actually scanning, excluding trusted workloads, scheduling scans sanely, and tuning the settings that hit ARM hardest.

## Why this happens

- **Real-time scanning of constantly-changing working sets:** AI tools, model servers, and dev toolchains rewrite cache files continuously; Defender re-scans every write, turning a background task into a permanent CPU tax.
- **Large single files scanned repeatedly:** Multi-gigabyte model weights and disk images get fully re-scanned on each access unless excluded — a workload x64 desktops muscle through but ARM efficiency cores feel.
- **Emulated processes cost more to scan:** x86 processes under Prism emulation draw more Defender scrutiny per operation, so the same app costs more on ARM than on native x64.
- **Full scans scheduled during work hours:** The default quick scan is light, but a full scan triggered at the wrong time saturates the CPU for an hour — and on a thin ARM laptop, thermal throttling makes it feel twice as bad.
- **Conflicting third-party security agents:** Two real-time engines (Defender plus an x86-emulated third-party AV) fight over every file access, doubling the overhead and occasionally deadlocking installers.
- **Corrupted scan history or definition state:** A damaged signature store or scan cache can send the engine into a re-scan loop on already-cleared files — high CPU with no visible progress.
- **Archive and network-drive scanning enabled aggressively:** Deep archive scanning and mapped-drive real-time protection multiply scan work on machines that handle large downloads or network shares.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find out what Defender is actually chewing on

Never tune blind. Two minutes in Task Manager and Resource Monitor tells you whether Defender is scanning a legitimate workload (fixable with exclusions) or stuck in a loop (fixable with a reset).

1. Open Task Manager, sort by CPU, and confirm **Antimalware Service Executable (MsMpEng.exe)** is the actual consumer — not a similarly-named third-party process.
2. In **Resource Monitor > Disk**, filter by MsMpEng.exe and read the file paths in Disk Activity — the repeating paths are your exclusion candidates.
3. Note the pattern: the same folder repeatedly (working set — needs exclusions) versus system-wide churn with no clear target (possible corruption — skip to Fix 6).
4. Check **Windows Security > Virus & threat protection > Protection history** for blocked items that might be re-triggering scans.
5. If the hot paths are AI model folders, confirm the owning app is behaving — a [Foundry Local model download stuck in a retry loop](/articles/foundry-local-model-download-stuck/) keeps Defender re-scanning partial files indefinitely.

### Fix 2: Add targeted exclusions for trusted workloads

Exclusions are the supported, safe fix for scan overhead on known-good software. The rule is narrow and specific: exclude the process or folder you trust, never broad paths like entire drives or user profile roots.

1. Open **Windows Security > Virus & threat protection > Manage settings > Exclusions > Add or remove exclusions**.
2. Add **folder** exclusions for trusted high-churn directories: your code workspace, AI model/cache folders, and VM disk folders — one entry per folder.
3. Add **process** exclusions for trusted heavy tools (your IDE, local inference server executables) using the full process path — process exclusions skip scanning of everything that process touches.
4. Do NOT exclude `C:\Users\<you>\Downloads`, temp directories, or email attachment paths — those are the highest-risk locations on the machine.
5. Re-check Task Manager after 10 minutes of normal work; MsMpEng.exe should settle near zero when the excluded workload is all that is running.

### Fix 3: Schedule scans inside active hours and tame wake behavior

Defender's scheduled scans are fine — scheduled at 2 AM with wake timers, they turn a cool ARM laptop into a warm bag heater and leave the CPU pegged when you open the lid. Put scans where you can see them.

1. Open **Windows Security > Virus & threat protection > Microsoft Defender Antivirus options** and confirm **Active hours** match your real work schedule.
2. Open **Task Scheduler > Microsoft > Windows > Windows Defender** and open the **Windows Defender Scheduled Scan** task properties.
3. On the **Conditions** tab, uncheck **"Wake the computer to run this task"** if overnight wakes are the complaint.
4. On the **Triggers** tab, move the full scan to a time you are using the machine lightly — lunch hour beats 3 AM for a laptop that sleeps.
5. Keep the quick scan on its default frequent schedule; it is cheap and catches the things that matter between full scans.

### Fix 4: Remove the second antivirus and fix driver-level conflicts

Two real-time engines on ARM is a performance disaster, and the emulated third-party one usually loses while still charging full overhead. One engine, properly configured, beats two fighting.

1. Open **Settings > Apps > Installed apps** and look for any third-party antivirus, "PC optimizer," or security suite — uninstall anything you did not deliberately choose.
2. After uninstalling, verify Defender re-enables itself: **Windows Security** should show all green with no "another provider" notices.
3. Check Device Manager for leftover filter drivers from the removed suite (**View > Show hidden devices > Non-Plug and Play Drivers**) and remove them.
4. If you removed a suite that bundled its own firewall, confirm Windows Firewall is active so you are not left exposed.
5. Driver-layer security tools can also interfere with hardware utilities — if you run AMD-based AI hardware alongside, the same conflict pattern behind [Adrenalin Ryzen AI driver issues](/articles/amd-adrenalin-ryzen-ai-driver-issues/) applies: security filter drivers versus hardware driver installs.

### Fix 5: Tune the scan settings that hit ARM hardest

A few Defender settings have outsized cost on ARM specifically. Adjusting them trades a small amount of theoretical coverage for a large, measurable responsiveness gain.

1. In Group Policy or Intune, under **Microsoft Defender Antivirus > Scan**, disable **"Scan archive files"** for real-time protection if you handle large archives routinely — on-demand scans still catch threats on open.
2. Disable scanning of mapped network drives in real-time protection if your workflow touches network shares constantly; schedule it instead.
3. Cap scan CPU: set **"Specify the maximum percentage of CPU utilization during a scan"** to 30-50 so full scans cannot saturate efficiency cores.
4. Turn off **"Scan removable drives during full scans"** unless you routinely plug in untrusted USB media — it doubles full-scan time for most laptop users.
5. After changes, run a manual quick scan to confirm protection still functions, then monitor Task Manager during your heaviest workload for a day.

### Fix 6: Reset Defender when it is stuck in a scan loop

When MsMpEng.exe burns CPU with no hot file path and exclusions change nothing, the engine state itself is usually corrupt — a damaged signature store or scan cache. A reset is faster than another week of guessing.

1. Open an elevated PowerShell and run `Update-MpSignature` to force a fresh definition download — stale or partial definitions cause re-scan loops.
2. Clear the scan history: stop the **Microsoft Defender Antivirus Service** (services.msc), delete contents of `C:\ProgramData\Microsoft\Windows Defender\Scans\History`, and restart the service.
3. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` — underlying system file corruption produces exactly these symptoms.
4. Check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for the current Defender platform update; platform updates regularly fix engine-level performance bugs.
5. On input symptoms: delayed keystrokes during heavy scans are input-queue lag from CPU saturation, not a keyboard fault — but if the Copilot key misbehaves even when idle, see the [Copilot key double-press issue](/articles/copilot-key-double-press-issue/).

## Closing

Defender on ARM is not the enemy — untargeted scanning is. Identify the hot paths, exclude trusted workloads narrowly, schedule scans inside your day, and keep exactly one real-time engine. Do that and the Snapdragon laptop feels like day one again, with protection intact.
