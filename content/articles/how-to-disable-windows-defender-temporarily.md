---
title: "How to Disable Windows Defender Temporarily (Safely)"
slug: how-to-disable-windows-defender-temporarily
date: 2026-09-07
categories: ["performance"]
tags: ["windows defender", "disable defender", "real-time protection", "antivirus", "windows security"]
description: "Need to disable Windows Defender temporarily? The safe methods to pause real-time protection, when it's justified, and how to turn it back on."
thumbnail: "/images/thumbs/how-to-disable-windows-defender-temporarily.webp"
faqs:
  - q: "Is it safe to disable Windows Defender temporarily?"
    a: "For short, specific tasks — installing trusted software, running a demanding game or render, troubleshooting a false positive — yes, with precautions: disconnect from risky browsing, re-enable immediately after, and never download files while unprotected. Leaving it off for days or disabling it permanently without a replacement antivirus is not safe."
  - q: "Why does Windows turn Defender back on by itself?"
    a: "That is by design. The Settings toggle for real-time protection is temporary — Windows re-enables it automatically after a short period or on reboot to prevent users from accidentally running unprotected. Persistent disabling requires Group Policy or registry changes, which Microsoft deliberately made harder to discourage permanent disabling."
  - q: "Will disabling Defender speed up my laptop?"
    a: "Sometimes noticeably, especially during specific workloads: large file copies, software compilation, game installations, and video rendering all trigger heavy real-time scanning. For general desktop use the difference is small. Targeted exclusions for trusted folders usually give 80 percent of the benefit with none of the risk."
  - q: "What is the difference between disabling and adding exclusions?"
    a: "Disabling turns off all real-time protection everywhere — maximum speed, maximum risk. Exclusions tell Defender to skip scanning specific files, folders, or processes — most of the speed benefit for trusted workloads while everything else stays protected. Exclusions are almost always the better choice."
---

There are legitimate reasons to disable Windows Defender temporarily: a trusted installer that Defender keeps quarantining, a competitive game where every background scan costs frames, a massive file operation that real-time scanning turns into a crawl, or troubleshooting whether Defender is the thing slowing you down. This guide covers the safe ways to do it — and the precautions that keep "temporarily" from becoming "regrettably."

One principle governs everything here: **disable for the task, re-enable for everything else.** Defender is genuinely good protection, it's free, and running without any antivirus is the single riskiest thing a Windows user can do. Every method below includes its own re-enable path.

## Why this happens

- **Real-time scanning overhead**: Every file read/write gets scanned — heavy during installs, copies, and compilations.
- **Scheduled scan storms**: Full scans kicking off during active use instead of idle time.
- **False positives**: Legitimate tools (game mods, developer utilities, niche software) flagged and blocked.
- **Troubleshooting need**: Isolating whether Defender is the cause of slowdowns or blocked operations.
- **Performance testing**: Benchmarking with and without antivirus to measure its true cost.
- **Conflicts with other security software**: Two real-time scanners fighting over every file.
- **Tamper Protection**: Windows' self-defense that reverts casual disable attempts — by design.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the official temporary toggle

The intended method — quick and self-reverting.

1. Open **Windows Security** > **Virus & threat protection** > **Manage settings** (under Virus & threat protection settings).
2. Toggle **Real-time protection** to **Off** — Windows warns you and may require admin approval.
3. Do your task immediately — install the software, run the benchmark, complete the file operation.
4. Toggle it back **On** the moment you're done. Don't "do it later."
5. Know its limits: Windows re-enables real-time protection automatically after a while or on restart. For longer tasks, use exclusions (Fix 2) instead of fighting the toggle.

### Fix 2: Use exclusions instead of disabling (recommended)

80% of the benefit, ~0% of the risk.

1. **Windows Security** > **Virus & threat protection** > **Manage settings** > scroll to **Exclusions** > **Add or remove exclusions**.
2. **Add an exclusion** > **Folder** — add the folder containing your trusted workload: game installs, project directories, video scratch disks.
3. For specific processes: **Add an exclusion** > **Process** — add the executable name (e.g., your compiler or game).
4. Exclusions persist across reboots and don't expire — unlike the toggle, they keep working while everything else stays protected.
5. **Hygiene**: review exclusions periodically and remove ones for projects you finished — an exclusion is a blind spot, so keep the list minimal and intentional.

### Fix 3: Schedule around Defender instead of disabling it

If scans are the problem, move the scans.

1. Open **Task Scheduler** > **Microsoft** > **Windows** > **Windows Defender**.
2. Open **Windows Defender Scheduled Scan** > **Triggers** — change it to run at 3 AM or whenever you're asleep.
3. In **Conditions**, check **Start the task only if the computer is idle** and **on AC power** — scans then avoid your active hours entirely.
4. For gamers: enable **Game Mode** (**Settings** > **Gaming**) — Windows deprioritizes background Defender activity during games. If Defender's service itself is the CPU hog, our [antimalware high-CPU guide](/articles/antimalware-service-executable-high-cpu-windows-11/) shows how to tame it without disabling protection.
5. This solves "Defender slows me down" for most people without ever touching protection — the scans still happen, just not while you're working.

### Fix  4: Disable via Group Policy (persistent, Pro+)

For lab machines, test systems, and other justified persistent cases.

1. Press `Win + R`, type `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Microsoft Defender Antivirus**.
2. Enable **Turn off Microsoft Defender Antivirus** — this is the persistent switch.
3. Also consider **Real-time Protection** > **Turn off real-time protection** if you want scheduled scans to continue but real-time off.
4. Run `gpupdate /force` and reboot.
5. **Warning**: only do this if another reputable antivirus is installed and active — Windows expects exactly one real-time protector. Microsoft documents Defender management at their [support hub](https://support.microsoft.com/en-us/windows).

### Fix 5: Disable via Registry (Home edition)

The persistent method without gpedit — same warnings apply.

1. First, disable **Tamper Protection**: **Windows Security** > **Virus & threat protection** > **Manage settings** > **Tamper Protection** > **Off**. (Without this, Windows reverts your registry changes.)
2. Open `regedit`, navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender`.
3. Create DWORD **DisableAntiSpyware** = **1**. (Create the Windows Defender key if missing.)
4. For real-time only: `...\Windows Defender\Real-Time Protection` > DWORD **DisableRealtimeMonitoring** = **1**.
5. Reboot. To re-enable: delete the DWORDs (or set to 0) and turn Tamper Protection back on. Verify protection status in Windows Security afterward.

### Fix 6: Handle the "another antivirus" scenario correctly

The legitimate permanent-disable case.

1. If you install a reputable third-party antivirus (Bitdefender, ESET, Malwarebytes Premium, etc.), **Windows Defender disables itself automatically** — this is the designed handoff, not a hack.
2. Verify in **Windows Security** > **Virus & threat protection** that your new AV shows as the provider — you should see its name, not Defender.
3. Never run two real-time antiviruses simultaneously — they fight over every file, doubling the performance cost and causing false positives.
4. If you uninstall the third-party AV, Defender reactivates automatically — confirm it's on afterward. And if the system is still sluggish with protection properly configured, work through our [step-by-step slow laptop method](/articles/how-to-fix-laptop-running-slow-step-by-step/) to find the real bottleneck.
5. Our [antimalware CPU guide](/articles/antimalware-service-executable-high-cpu-windows-11/) covers tuning whichever protector you keep.

### Fix 7: Re-enable and verify protection

Closing the loop — never skip this.

1. After your task: **Windows Security** > **Virus & threat protection** > **Manage settings** > **Real-time protection** > **On**.
2. Re-enable **Tamper Protection** if you disabled it.
3. Run a **Quick scan** to confirm the engine is healthy after the toggle cycle.
4. Check **Protection history** for anything that happened while protection was off — quarantine anything suspicious.
5. If you used Group Policy/registry for a justified persistent disable, set a calendar reminder to review — "temporary" disables have a way of becoming permanent through forgetfulness.

## Closing

Disabling Windows Defender temporarily is fine when done deliberately: use the Settings toggle for quick tasks, exclusions for trusted workloads (the better choice 90% of the time), and scheduling to keep scans out of your way. Reserve Group Policy and registry methods for justified persistent cases with a replacement antivirus installed. And whatever method you use — re-enable promptly. The few minutes of protection you skip are exactly when something finds you.
