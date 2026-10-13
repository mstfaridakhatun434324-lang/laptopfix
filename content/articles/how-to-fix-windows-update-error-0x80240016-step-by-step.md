---
title: "Windows Update Error 0x80240016: A Complete Step-by-Step Repair Guide"
slug: how-to-fix-windows-update-error-0x80240016-step-by-step
date: 2026-09-24
categories: ["windows-update"]
tags: ["windows update", "error 0x80240016", "windows 11", "troubleshooting", "step by step"]
description: "Error 0x80240016 means another install is already running. Follow these 7 ordered steps to identify it, clear it safely, and resume updating."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80240016-step-by-step.webp"
faqs:
  - q: "Can two Windows updates install at the same time?"
    a: "No — Windows serializes installations deliberately. The update engine, the MSI installer, and the servicing stack all coordinate through locks so only one installation modifies system files at a time. 0x80240016 is that coordination working as designed, usually surfacing when the other install is stuck or invisible."
  - q: "The error persists after restart. What now?"
    a: "A persistent flag after a clean restart means the in-progress state is stale rather than real — no installer is actually running. The DISM servicing repair in this guide resets that state tracking. If DISM does not clear it, the manual catalog install bypasses the check for the urgent update."
  - q: "Should I disable background updaters to prevent this?"
    a: "Not entirely — background updaters keep drivers and apps secure. Instead, stagger them: let Windows Update finish its work before manually triggering manufacturer updaters, and avoid running two update tools simultaneously. Coordination beats disabling. A staggered schedule gives you security updates and collision-free installs at the same time."
  - q: "What is TrustedInstaller and why is it always busy?"
    a: "TrustedInstaller is Windows' own installer service, responsible for installing updates and system components. High activity after Patch Tuesday is normal — it can work for an hour on a big update. Only treat it as stuck after extended zero-activity periods, and prefer restarting over killing it."
---

Error 0x80240016 means exactly what it says: another installation is already in progress, so Windows Update will not start a competing one. Windows serializes installations to avoid two installers fighting over the same files — a sensible safety rule that becomes annoying when the other installation is stuck, invisible, or long finished but left its flag behind.

Your job is to figure out which of three situations you are in: a legitimate install that needs more time, a stuck installer process that needs clearing, or a stale in-progress flag from an install that already ended. Each has a different fix, and the steps below identify your situation before acting — because killing a healthy installer mid-run causes the very corruption you are trying to avoid.

Do not reboot randomly hoping it clears. Targeted identification first, action second.

## Why this happens

- **Genuine concurrent install:** A software installer is legitimately running and needs to finish first.
- **Background driver install:** Manufacturer updaters install drivers silently in the background.
- **Unfinished Windows update:** A previous update session did not complete cleanly.
- **Crashed installer holding the lock:** The installer died but the mutex it held was never released.
- **Servicing still committing:** TrustedInstaller working through a long queue of operations.
- **Stale pending operations:** pending.xml lists operations from an install that already rolled back.
- **Scheduled task installers:** Background scheduled tasks (Office, browsers) installing updates silently.
- **Flag corruption:** The in-progress indicator stuck on with nothing behind it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify whether an install is genuinely running

Look before you act. Killing a healthy installer causes corruption; waiting out a stuck one wastes hours. Identification first.

1. Open Task Manager, Processes tab, sorted by CPU.
2. Look for msiexec.exe, TrustedInstaller.exe, TiWorker.exe, or setup.exe.
3. Active CPU/disk usage means a real install — wait for it.
4. Zero activity for 15+ minutes means stuck — proceed to clear it.

### Fix 2: Give legitimate installs time to finish

If you found genuine activity, the correct action is patience. Large feature updates and Office installs can run 30 to 90 minutes. If the troubleshooter itself misbehaves, see [How to fix we couldn't complete the updates undoing changes on hp laptop](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-hp-laptop/) for a dedicated walkthrough.

1. Note which process is active and its resource usage.
2. Wait 45 minutes without using the machine heavily.
3. Check Task Manager again for completion.
4. Only escalate if the process is still active with no progress after that.

### Fix 3: Restart cleanly to release locks

A full restart is the safest way to clear transient installer locks and let pending work settle.

1. Close all applications and save work.
2. Choose Restart from the Start menu.
3. After booting, wait five minutes before touching Windows Update.
4. Test the update check.

### Fix 4: Terminate only confirmed-stuck processes

End processes that are demonstrably dead — zero CPU over an extended period — and leave healthy ones alone.

1. In Task Manager Details tab, confirm the suspect shows 0% CPU for 10+ minutes.
2. End only that specific process.
3. Do not end TrustedInstaller unless it is fully idle and stuck — prefer a restart for it.
4. Retry Windows Update immediately.

### Fix 5: Clean boot to find the background culprit

Isolates whether a startup program's background installer is the repeat offender.

1. Use msconfig to disable non-Microsoft services.
2. Disable startup items in Task Manager.
3. Restart and test Windows Update in the clean state.
4. If fixed, re-enable in groups to identify the culprit.

### Fix 6: Repair servicing state with DISM

When the in-progress flag itself is corrupt, servicing repair resets the state tracking. [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com) explains the servicing model.

1. In Terminal (Admin), run: DISM /Online /Cleanup-Image /RestoreHealth
2. Wait for full completion.
3. Restart the laptop.
4. Check for updates.

### Fix 7: Bypass with a manual catalog install

The standalone [Microsoft's installer guidance](https://support.microsoft.com/en-us/windows) package bypasses the queue's in-progress checks for the urgent update.

1. Get the KB number from Update history.
2. Download the matching x64 .msu.
3. Ensure no installer is visibly running, then launch it.
4. Restart, verify in Update history, then resolve the underlying stuck state at your leisure.

### Fix 8: Give every installer its own turn

Installations are serialized by design, so the human workflow should be serialized too. The habit that prevents 0x80240016 is simple: one installer at a time, each allowed to finish, with a restart between big ones. It feels slower than multitasking your updaters, but it is dramatically faster than untangling a collision — and collisions are where the real time goes.

1. Run Windows Update to full completion — including the restart — before starting any other installer.
2. Let manufacturer driver updaters finish entirely before touching Windows Update, and vice versa.
3. Avoid installing desktop applications during active Windows update sessions.
4. When something seems stuck, check Task Manager for genuine activity before intervening.
5. Prefer Restart over End Task for clearing stuck installers — it is safer and usually sufficient.
6. Keep a mental queue: updates first, drivers second, applications last, one at a time.

## Closing

With 0x80240016 resolved, updates should queue normally again. Prevent repeats by letting one installation finish before starting another, keeping background updaters from colliding, and restarting cleanly instead of killing installer processes. For related errors, see [How to fix superfetch high disk usage on hp laptop](/articles/how-to-fix-superfetch-high-disk-usage-on-hp-laptop/) and [How to fix windows 11 stuck on restarting screen reddit](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-reddit/). Serialized installers are a feature, not a limitation — they protect your system files from conflicting writes. Respect the queue, give each installer its turn, and this error becomes something you read about rather than experience again. The few minutes of patience it costs are nothing next to the hours a collision can waste. Every installer you run is borrowing your system's trust that it will finish cleanly and release its locks. Extend the same courtesy back: let each one complete, restart between the big ones, and collisions stop happening. It is a small discipline with an outsized payoff in reliability.
