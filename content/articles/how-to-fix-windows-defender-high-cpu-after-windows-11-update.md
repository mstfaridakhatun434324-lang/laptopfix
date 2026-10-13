---
title: "Windows Defender High CPU After a Windows 11 Update? Fix It"
slug: how-to-fix-windows-defender-high-cpu-after-windows-11-update
date: 2026-09-14
categories: ["performance"]
tags: ["windows defender", "high cpu", "windows update", "msmpeng", "windows 11"]
description: "MsMpEng.exe spiking after a Windows 11 update? Learn why Defender works overtime post-update and how to calm it safely."
thumbnail: "/images/thumbs/how-to-fix-windows-defender-high-cpu-after-windows-11-update.webp"
faqs:
  - q: "Why does Windows Defender use high CPU after every Windows update?"
    a: "Updates touch tens of thousands of files, and Defender's real-time protection scans each touched file as the system settles. Feature updates additionally trigger a full re-baseline scan so Defender's understanding matches the new OS build. This one-two punch — re-scanning everything the update touched plus a deliberate full scan — is why CPU spikes are near-universal after updates and why they reliably fade within a day or two once the work completes."
  - q: "How long should I wait before treating Defender CPU as a problem?"
    a: "Give it 24 to 48 hours of normal use, including one good idle window (plugged in, a few uninterrupted hours). Post-update scanning is legitimate work with a defined end. It becomes a problem when high CPU persists past 48 hours, survives reboots unchanged, or pairs with Protection history showing repeated scans of the same files — those patterns indicate a stuck scan, a corrupted definition, or a high-churn folder keeping the engine busy indefinitely."
  - q: "Will a third-party antivirus use less CPU than Defender?"
    a: "Sometimes, but not reliably — every real-time antivirus scans file operations, and the workload (your files changing) is the same regardless of vendor. Third-party products can be lighter on specific workloads and heavier on others; there is no universal efficiency winner. Switch antiviruses for features or preference, not as a CPU fix — and never run two real-time antiviruses simultaneously, which doubles scanning overhead and causes conflicts."
  - q: "Does pausing Windows Updates stop Defender from rescanning?"
    a: "Pausing updates prevents new update-triggered scan waves, which helps if you are caught in a cycle of daily updates each triggering re-scans. But it does nothing for the scan already in progress, and staying paused indefinitely leaves security holes unpatched. The better approach: let the current post-update scan finish, then keep updates current — a system that updates smoothly on schedule has shorter, less disruptive scan episodes than one catching up in bursts."
---

There is a rhythm to it: Windows installs an update, you reboot, and for the next day or two Antimalware Service Executable (MsMpEng.exe) sits at the top of Task Manager, fans humming, everything slightly sluggish. It happens after nearly every update, and it sends a steady stream of users searching for a way to turn Defender off. Resist that urge — what you are watching is your antivirus doing exactly what it should after the ground shifts beneath it.

An update touches tens of thousands of files, and Defender scans them. A feature update goes further, triggering a deliberate full-system re-baseline. The CPU spike is the sound of legitimate work — but legitimate work should end, and sometimes it does not. This guide covers both halves: letting the real scan finish efficiently, and fixing the stuck scan that never does. For the wider CPU picture, see [fixing high CPU usage in Windows 11 24H2](/articles/how-to-fix-high-cpu-usage-in-windows-11-24h2/); to reduce boot-time load, read [disabling startup programs in Windows 11](/articles/how-to-disable-startup-programs-windows-11/).

## Why this happens

- **Re-scanning every file the update touched**: Tens of thousands of modified files each pass through real-time protection as the system settles.
- **Post-feature-update full re-baseline**: Major updates trigger a deliberate full scan so Defender's baselines match the new OS build.
- **Security Intelligence update churn**: Updates often bundle definition and platform updates that change scanning behavior temporarily.
- **High-churn folders amplified by the update**: Folders that change constantly get rescanned relentlessly in the unsettled post-update period.
- **Scheduled scan colliding with the aftermath**: The regular scheduled scan may fire right into the post-update re-scan, doubling the load.
- **Corrupted definitions from the update**: A damaged definition or platform update can send the engine into inefficient scanning loops.
- **Third-party AV remnants conflicting**: Leftover filter drivers from old antivirus products fight Defender on every file access the update touches.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the scan is legitimate and current

Two minutes of checking separates 'busy' from 'broken'.

1. Open **Windows Security** > **Virus & threat protection** > **Protection history** — recent scan entries and no stuck warnings mean legitimate activity.
2. Verify definitions are current under **Virus & threat protection updates** — stale definitions after an update cause inefficient scanning.
3. In **Task Manager** > **Details**, check whether MsMpEng.exe CPU tracks with disk activity (active scanning) or sits high while idle (stuck).
4. Note the start time: if high CPU began within hours of the update installing, it is almost certainly the post-update scan.
5. Only proceed to tuning if the pattern looks wrong — constant, reboot-surviving, or days-old high CPU.

### Fix 2: Give the post-update scan a clean idle window

The fastest way through legitimate scanning is an uncontested machine.

1. Plug in, disable sleep temporarily (**Settings** > **System** > **Power & battery**), and leave the machine idle for 2–3 hours — overnight is ideal.
2. Do not run heavy apps during the window; every file you create or change gets scanned and extends the job.
3. Pause optional background churn: Widgets off, Game Bar background recording off, cloud sync paused.
4. After the window, check Task Manager at idle — MsMpEng.exe near zero means the baseline completed.
5. If it is still high after a full idle night, the scan is not finishing on its own — continue to the repairs.

### Fix 3: Reschedule Defender's heavy scans

Keep future scan waves out of your working hours.

1. Open **Task Scheduler** (`taskschd.msc`) > **Microsoft** > **Windows** > **Windows Defender** > **Windows Defender Scheduled Scan** > **Properties**.
2. Set the trigger to an idle hour (e.g., 3 AM) and enable **Run task as soon as possible after a scheduled start is missed**.
3. On **Conditions**, check **Start the task only if the computer is idle** and **Stop if the computer ceases to be idle**.
4. Review the **Cache Maintenance** task too — stagger it away from the main scan.
5. This does not stop real-time protection; it only moves the scheduled deep scans.

### Fix 4: Exclude trusted high-churn folders

The biggest lever for developers, gamers, and creators.

1. **Windows Security** > **Virus & threat protection** > **Manage settings** > **Exclusions** > **Add or remove exclusions**.
2. Add folders you control and trust: code workspaces, Steam libraries, video scratch disks — specific paths, never whole drives.
3. Consider excluding trusted heavy processes (compiler, game launcher) if folder exclusions are not enough.
4. Never exclude Downloads, Temp, or system folders — exclusions are a scalpel, not a chainsaw.
5. Re-test under your normal workload: brief spikes on new files are normal; permanent high CPU is not.

### Fix 5: Refresh definitions and repair the platform

When the engine itself is damaged, no scheduling tweak helps.

1. Elevated PowerShell: `Update-MpSignature` to force a clean definition pull.
2. **Settings** > **Windows Update** — install all pending updates, including Security Intelligence and Defender platform entries.
3. `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` — Defender is a Windows component and these repairs cover it.
4. Reboot and observe 30 idle minutes; a repaired engine settles quickly.
5. If a specific definition version correlates with the spike, the next definition update usually resolves it — check [Windows support](https://support.microsoft.com/en-us/windows) for acknowledged issues.

### Fix 6: Remove conflicting antivirus remnants

Old security software leaves filter drivers that turn every file access into a tug-of-war.

1. **Settings** > **Apps** — uninstall any third-party antivirus still present, properly.
2. Run the vendor's official **removal tool** (search '[vendor] antivirus removal tool') — uninstallers leave drivers behind; removal tools do not.
3. Reboot and confirm **Windows Security** shows Microsoft Defender as the active provider with no warnings.
4. **Device Manager** > **View** > **Show hidden devices** — check **Non-Plug and Play Drivers** for orphaned AV filters and remove them.
5. Monitor for a day: driver-conflict CPU is the most stubborn kind, and also the most satisfying to finally kill.

### Fix 7: Run an offline scan before considering alternatives

Rule out the heroic scenario: Defender fighting real malware hard enough to look broken.

1. **Windows Security** > **Virus & threat protection** > **Scan options** > **Microsoft Defender Offline scan** > **Scan now**.
2. Let the rebooted offline scan complete fully — up to an hour; it runs outside Windows where rootkits cannot hide.
3. If it finds threats, the CPU was legitimate — monitor for normal behavior after remediation.
4. If clean and tuning failed, the sane alternative to disabling Defender is a reputable third-party AV that registers with Security Center properly.
5. Never disable Defender via registry hacks with Tamper Protection off — you would trade real protection for a quieter Task Manager, a terrible bargain.

## Closing

Defender's post-update CPU spike is the sound of your antivirus re-learning a changed system — legitimate, temporary, and best handled by giving it a clean idle window and smarter scheduling. When the spike outlives its welcome, the cause is a stuck scan, a corrupted definition, or a folder it cannot stop rescanning, and each has a direct fix. The off switch remains what it always was: the one option that makes everything worse.
