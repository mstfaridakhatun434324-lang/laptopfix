---
title: "Fix TiWorker.exe High CPU During Windows Update on a Lenovo Laptop"
slug: how-to-fix-tiworker-exe-high-cpu-windows-update-on-lenovo-laptop
date: 2026-09-17
categories: ["windows-update"]
tags: ["tiworker.exe", "high cpu", "windows update", "lenovo laptop"]
description: "TiWorker.exe eating CPU on your Lenovo during Windows Update? Learn what it does, when it's normal, and how to calm it down."
thumbnail: "/images/thumbs/how-to-fix-tiworker-exe-high-cpu-windows-update-on-lenovo-laptop.webp"
faqs:
  - q: "What is TiWorker.exe?"
    a: "TiWorker.exe (Windows Modules Installer Worker) is the process that installs, modifies, and removes Windows updates and optional components. High CPU from TiWorker means Windows is actively working on updates — installing, staging, or cleaning up after them. Sustained high CPU with no update activity is the signal that something underneath it is stuck."
  - q: "Is TiWorker.exe high CPU normal?"
    a: "Temporarily, yes. During and after updates, TiWorker legitimately uses significant CPU for 30 minutes to a few hours. It becomes a problem only when it runs hot for many hours or days with no update activity to justify it — that indicates a stuck update operation."
  - q: "Can I end TiWorker.exe in Task Manager?"
    a: "You can, but it restarts itself because the update operation it serves is still queued. Killing it treats the symptom for minutes. The fix is resolving the stuck update operation underneath, which is what this guide does. Check Settings → Windows Update first: visible update progress means the CPU usage is legitimate work."
  - q: "Why is TiWorker.exe worse on Lenovo laptops?"
    a: "Lenovo's large driver sets and frequent Vantage-delivered updates give TiWorker more work, and Lenovo-specific driver packages that fail to install cleanly can leave TiWorker retrying indefinitely. The process is the same on all brands; Lenovos just feed it more. Its disk-heavy sibling is covered in the [Windows Modules Installer Worker disk guide](/articles/best-way-to-fix-windows-modules-installer-worker-high-disk-usage/)."
---

TiWorker.exe — the Windows Modules Installer Worker — is supposed to be invisible. When it works, it installs your updates in the background and exits. When it goes wrong, it pins a CPU core at 100% for hours, the fan screams, the battery drains, and ending the task in Task Manager does nothing because it simply comes back.

On Lenovo laptops this has a recognizable pattern: a Windows or driver update gets stuck mid-operation, and TiWorker keeps grinding on the stuck work forever. The CPU usage is real work — just work that will never complete. The fix is not killing the process; it is unblocking or clearing the operation underneath it.

This guide shows you how to tell normal TiWorker activity from stuck TiWorker, then walks through the unblocking sequence from gentle (let it finish) to decisive (clear the stuck update).

## Why this happens

- **Stuck update installation:** An update that cannot complete keeps TiWorker retrying its install loop indefinitely.
- **Corrupt component store:** TiWorker does its work against WinSxS; store corruption makes its operations fail and retry.
- **Failed driver package:** A Lenovo driver update that will not install cleanly leaves TiWorker chewing on it.
- **Post-update cleanup backlog:** After a feature update, TiWorker legitimately works through a large cleanup queue for hours.
- **Corrupt update cache:** Damaged payloads that fail verification keep the installer loop spinning.
- **Windows Update service wedged:** The service feeding TiWorker its work queue stuck in a bad state.
- **Disk errors slowing I/O:** TiWorker is I/O-heavy; a struggling drive turns normal work into hours of grinding.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether it is working or stuck

TiWorker doing real work should be left alone. Check before intervening.

1. Open Settings → Windows Update: if updates are downloading/installing, TiWorker's CPU is legitimate — let it finish (up to a few hours).
2. Check Task Manager → TiWorker.exe: sustained 100% on one core for 6+ hours with no update progress means stuck.
3. Note when it started — right after Patch Tuesday points at a specific update.

### Fix 2: Let legitimate work finish first

The gentlest fix is patience, once, with the machine properly set up.

1. Plug in the charger and set sleep to Never temporarily.
2. Leave the machine alone for 2–3 hours.
3. If TiWorker settles on its own, it was legitimate post-update work — no further action needed.

### Fix 3: Run the Windows Update troubleshooter

The troubleshooter detects and clears the stuck operations that keep TiWorker spinning.

1. Settings → System → Troubleshoot → Other troubleshooters → Windows Update → Run.
2. Apply all fixes and reboot.
3. Watch TiWorker for 30 minutes after reboot — a fixed queue lets it finish and exit. For the disk-heavy side of the same process, the [best-way disk usage guide](/articles/best-way-to-fix-windows-modules-installer-worker-high-disk-usage/) covers the mitigations.

### Fix 4: Clear the stuck update cache

When the payload TiWorker is chewing on is corrupt, remove it.

1. Elevated Command Prompt: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`.
3. Restart the services and reboot.
4. TiWorker should now have an empty queue; confirm its CPU drops.

### Fix 5: Repair the component store

Store corruption makes TiWorker's operations fail in a loop. Fix the store.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated prompt.
2. Follow with `sfc /scannow` and reboot.
3. Monitor TiWorker — store repair resolves the retry-loop pattern in most cases.

### Fix 6: Update Lenovo drivers and check Vantage

A stuck Lenovo driver update is a common TiWorker anchor on these machines.

1. Open Lenovo Vantage and complete any pending driver updates.
2. Check [Lenovo support](https://support.lenovo.com/us/en/) for newer chipset/storage drivers for your model.
3. In Update history, look for a repeatedly failing driver update and hide it with wushowhide.diagcab if the vendor package supersedes it.
4. Reboot and verify TiWorker settles. If a specific driver update keeps failing underneath, the [step-by-step driver repair](/articles/how-to-fix-driver-updates-failing-in-windows-update-step-by-step/) resolves it.

### Fix 7: Limit the damage while it works

For the cases where TiWorker has legitimate but long work, reduce its impact.

1. In Task Manager → Details, you can lower TiWorker.exe's priority to Below Normal — it still finishes, just more politely.
2. Schedule heavy updates for plugged-in idle time via Active Hours.
3. Keep 15 GB+ free on C: so its staging I/O is not fighting a full disk.
4. If TiWorker still never settles after all fixes, check drive health — a failing drive turns its I/O into an endless grind, and no update repair fixes hardware.

### Fix 8: Identify the stuck package with the Windows Update log

When TiWorker spins with no visible update progress, the Windows Update log shows exactly which operation it is stuck on — turning a blind cache clear into the targeted removal of one looping package. The log looks intimidating at first — thousands of lines — but you only need the repeating failure block near the end. One KB number is usually responsible for the entire storm. Removing that single package from the queue is the difference between a targeted fix and another blind cache clear that changes nothing.

1. Open PowerShell as administrator and run `Get-WindowsUpdateLog` — Windows assembles a readable log on your Desktop.
2. Open WindowsUpdate.log and search for failure entries repeating with recent timestamps.
3. Note the KB number or package name caught in the loop — that is TiWorker's anchor.
4. Hide that specific update with wushowhide.diagcab, or download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it manually.
5. Reboot and watch TiWorker: with the looping package gone from its queue, CPU usage should settle within the hour.

## Closing

TiWorker.exe high CPU is the sound of Windows Update working — or failing to work — underneath. Tell the two apart by checking for real update progress, then unstick it: troubleshooter, cache clear, store repair, and Lenovo driver updates. Killing the process never fixes anything; clearing the stuck operation it serves fixes everything.
