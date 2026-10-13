---
title: "Best Way to Fix the Update Assistant Stuck at 99 Percent"
slug: "best-way-to-fix-update-assistant-stuck-at-99-percent"
date: "2026-10-07"
categories: ["windows-update"]
tags: ["update-assistant", "stuck-99-percent", "windows-11", "best-fix"]
description: "The fastest, most reliable methods to fix the Windows 11 Update Assistant freezing at 99% — ranked from quickest win to guaranteed fallback."
thumbnail: "/images/thumbs/best-way-to-fix-update-assistant-stuck-at-99-percent.webp"
faqs:
  - q: "What is the single fastest fix for the 99 percent freeze?"
    a: "Pausing your antivirus real-time protection for a few minutes is the fastest fix with the highest success rate. The scanner is often grinding through the assistant's multi-gigabyte staged files at exactly that point, and pausing it lets the final verification complete. If the progress bar moves within 20 minutes, you have your answer and can re-enable protection right after."
  - q: "How long should I wait at 99 percent before doing anything?"
    a: "Give it a full hour on a modern SSD machine, longer on older hardware, before intervening. The final phase does real work — driver migration and compatibility checks — that legitimately takes time. Use Task Manager to check for CPU and disk activity during the wait; sustained activity means it is still progressing and patience is the correct fix."
  - q: "Does the Media Creation Tool avoid the 99 percent problem?"
    a: "Often yes. The Media Creation Tool and the mounted-ISO method use a different installation engine than the Update Assistant, so a hang specific to the assistant's staging process does not carry over. Many users who stall repeatedly in the assistant complete the same upgrade smoothly from an ISO. It is one of the most reliable fallbacks for this exact symptom."
  - q: "Will I lose files if I cancel the assistant at 99 percent?"
    a: "No. At 99 percent the assistant is still in the preparation phase and has not modified your running system; cancelling or closing it leaves your files, apps, and current Windows installation untouched. The only thing lost is time, since you may need to redownload the payload. Never cancel after the machine has rebooted into the actual installation phase."
---

When the Update Assistant parks itself at 99 percent, you want the fix that works — not a tour of every possible cause. This guide ranks the solutions by speed and reliability so you can start with the quickest win and escalate only if needed. Think of it as the shortlist; a companion troubleshooting guide covers the deep-dive diagnosis if you prefer to understand the stall first.

The ranking below reflects what actually resolves this symptom in practice. Most people never need to go past the second or third method, and the final fallback is close to guaranteed because it replaces the assistant entirely.

This guide is deliberately opinionated: instead of cataloguing every possible cause of the 99 percent freeze, it ranks the fixes by how often they actually work, so you can start with the highest-probability win. That ranking comes from the pattern of real-world reports — antivirus scanning the staged payload first by a wide margin, corrupt staging files second, and everything else trailing behind. If you prefer to understand the stall before acting, the companion diagnostic guide covers the full analysis; here, speed is the priority.

## Why this happens

- **Antivirus scanning the staged payload:** The top cause — real-time protection chews through gigabytes of staged files at the final step.
- **Corrupt staging files:** Damaged downloads fail the final integrity check and hang instead of erroring out.
- **Slow final-phase work:** Driver migration and compatibility checks legitimately take a long time on older or cluttered machines.
- **Disk space pressure:** The final phase needs working room beyond the download size.
- **Competing update activity:** Windows Update running its own operations can lock files the assistant needs.
- **Assistant-specific cache corruption:** The assistant's own staging area can corrupt independently of the main Windows Update cache.
- **Problem drivers stalling migration:** A driver that cannot migrate hangs the assistant at the same point every attempt.
- **Flaky network during verification:** The final handshake with Microsoft's servers can hang on an unstable connection.

## How to fix it

Work through these in order — diagnose first, then act.

Work the list top-down and stop at the first fix that works — there is no prize for completing all eight. Each method is self-contained, so you can jump straight to the ISO fallback in Fix 6 if you have already lost patience with the assistant entirely.

### Fix 1: Pause antivirus and wait 20 minutes

The highest-probability quick win, and it costs nothing to try.

1. Open your antivirus suite and pause real-time protection.
2. Do not close the assistant — leave it exactly as it is.
3. Wait 20 to 30 minutes and watch for the progress bar to move.
4. If it completes, re-enable protection immediately after the reboot finishes.

### Fix 2: Verify it is genuinely stuck with Task Manager

Before escalating, confirm the stall is real rather than slow.

1. Open Task Manager and locate the Update Assistant process.
2. Check CPU and disk columns — sustained activity means it is still working.
3. If the process is idle and an hour has passed at 99 percent, treat it as stuck.
4. Only move to Fix 3 once you have confirmed a genuine stall.

### Fix 3: Restart the assistant with a clean staging area

Clearing the assistant's corrupted staging files is the most reliable mid-level fix.

1. Close the Update Assistant, or end its task in Task Manager if it will not close.
2. Delete the `C:\$Windows.~BT` and `C:\$Windows.~WS` folders if present.
3. Restart the laptop to clear any locked handles.
4. Relaunch the assistant and let it download the payload fresh — this run usually sails past 99 percent.

### Fix 4: Free disk space and silence competing updates

Remove the two environmental factors that most often prolong the final phase.

1. Free at least 20 GB on the system drive using Storage Sense.
2. In Settings, Windows Update, pause updates so no background scan competes with the assistant.
3. Temporarily stop the Windows Update service from services.msc during the assistant run.
4. Relaunch the assistant and monitor the final phase.

### Fix 5: Strip peripherals and update key drivers

Eliminate the driver-migration hang that stalls the assistant at the same point every time.

1. Disconnect all USB devices except the power adapter.
2. Update chipset, storage, and wireless drivers from your laptop manufacturer's support page.
3. Temporarily uninstall third-party antivirus instead of merely disabling it.
4. Relaunch the assistant with the machine in this clean state.

### Fix 6: Switch to the ISO in-place upgrade

When the assistant itself is the problem, replace the tool — this is the most reliable fallback.

1. Download the Windows 11 ISO from Microsoft's software download page.
2. Double-click the ISO to mount it, then run setup.exe.
3. Choose to keep personal files and apps.
4. The in-place upgrade uses a different engine and typically completes without the 99 percent hang.
5. If you want the full diagnostic walkthrough instead of the ranked list, see [diagnosing the Update Assistant stuck at 99 percent](/articles/update-assistant-stuck-at-99-percent-troubleshooting/).

### Fix 7: Check the setup logs before the final retry

If even the ISO method hesitates, the logs identify the specific blocker.

1. After a failed attempt, open `C:\$Windows.~BT\Sources\Panther\setupact.log`.
2. Look at the final entries for the component active when progress stopped.
3. Resolve the named driver or component — update it, or uninstall the device.
4. Retry with the ISO method once the blocker is removed.

### Fix 8: Repair the system, then retry once

A last-resort foundation repair for machines where everything stalls.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an admin Command Prompt.
2. Follow with `sfc /scannow`.
3. Run `chkdsk C: /f` and restart to complete the disk check.
4. With the foundation repaired, make one final attempt using the ISO method.

A word on prevention for next time: the 99 percent stall recurs on machines where the same conditions persist — the same antivirus with the same aggressive scanning, the same nearly-full drive, the same outdated storage driver. If the assistant froze for you once, the fix that worked is worth remembering, because the next feature update will likely trip over the same obstacle. Apply the preventive version now — pause protection during upgrades, keep 20 GB free, update the chipset driver — and the next run finishes while you are making coffee. For the download-failure variant of this symptom, see our [0x80240034 repair guide](/articles/how-to-fix-windows-update-error-0x80240034-on-laptop/).

## Closing

Ranked by what actually works, the 99 percent freeze yields to a paused antivirus, a cleaned staging area, or — when the assistant itself is at fault — the ISO method that bypasses it entirely. Start at the top of the list, stop at the first method that works, and you will spend minutes on this instead of an evening.
