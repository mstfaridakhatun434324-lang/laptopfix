---
title: "TiWorker.exe High CPU After a Windows 11 Update? Fix It"
slug: how-to-fix-tiworker-high-cpu-after-windows-11-update
date: 2026-09-06
categories: ["performance"]
tags: ["tiworker.exe", "windows modules installer", "high cpu", "windows update", "fix"]
description: "TiWorker.exe (Windows Modules Installer Worker) hammering CPU after a Windows 11 update? Learn when to wait and when to intervene."
thumbnail: "/images/thumbs/how-to-fix-tiworker-high-cpu-after-windows-11-update.webp"
faqs:
  - q: "What is TiWorker.exe?"
    a: "TiWorker.exe is the Windows Modules Installer Worker — the process that installs Windows updates, enables/disables Windows features, and runs post-update cleanup and component servicing. It is a legitimate, essential Windows process. High CPU from TiWorker after an update usually means it's doing real work: installing, configuring, or cleaning up. It becomes a problem only when it never finishes."
  - q: "How long should TiWorker run after an update?"
    a: "After a monthly cumulative update, expect elevated TiWorker activity for 30 minutes to a few hours, including a reboot or two. After a feature update, it can legitimately work for several hours across a day. Give it one full plugged-in day before intervening — interrupting genuine update work mid-flight is how systems end up in broken half-updated states."
  - q: "Is it safe to end TiWorker.exe in Task Manager?"
    a: "You can end it, but it will restart and resume its work — and killing it mid-install risks corrupting the update. It's safe only as a diagnostic (to confirm TiWorker is truly the CPU consumer, since it restarts cleanly). Never kill it repeatedly to 'keep CPU down'; that just stretches the same work over days and increases corruption risk."
  - q: "Why does TiWorker keep coming back every day?"
    a: "Because its work isn't completing. The usual reasons: a corrupted update download it keeps retrying, the SoftwareDistribution cache in a bad state, insufficient disk space aborting cleanup, or a failing update it can't install. Each boot, Windows retries. The fixes below break the cycle by clearing the corrupted state so the work can actually finish."
---

Right after a Windows 11 update, `TiWorker.exe` — the Windows Modules Installer Worker — pegs your CPU at 50%, 80%, sometimes 100%. The fans roar, everything else crawls, and it just... keeps going. Hours later, it's still there.

Here's the uncomfortable truth: most of the time, TiWorker is doing legitimate, necessary work — installing the update's components, configuring features, cleaning up superseded files. Killing it is like yanking the power cord mid-surgery. But sometimes it's genuinely stuck, retrying the same failed operation forever. This guide teaches you to tell the difference — and to fix the stuck cases properly.

## Why this happens

- **Legitimate post-update servicing**: Component installation, feature configuration, and update cleanup — real work that takes time.
- **Corrupted update download**: A damaged package TiWorker retries endlessly.
- **Stuck SoftwareDistribution cache**: The update datastore in a bad state, causing repeated failed attempts.
- **Low disk space**: Cleanup phases aborting for lack of room, then retrying.
- **Conflicting pending operations**: Multiple updates or feature toggles queueing conflicting work.
- **Corrupt component store**: Damaged servicing stack making every operation fail and retry.
- **Interrupted previous update**: A past update killed mid-flight leaving the servicing stack confused.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether it's working or stuck

The most important step — don't "fix" legitimate work.

1. Note when the update installed (**Settings** > **Windows Update** > **Update history**) and how long TiWorker has been busy. Under 24 hours with a recent update = probably legitimate.
2. Open Task Manager > **Details** > right-click TiWorker.exe > **Open file location** — confirm it's `C:\Windows\WinSxS\` (genuine). Anything else is malware wearing the name.
3. Check **Settings** > **Windows Update**: if it says "installing," "pending restart," or shows progress, TiWorker is mid-job — let it finish.
4. Give it one full plugged-in session: TiWorker needs the machine on and idle-ish; sleep and shutdowns pause it, stretching the work across days and making it look "stuck" when it's just starved of time.
5. Legitimate TiWorker shows progress: disk activity in Task Manager > Performance, and Windows Update status changing. A stuck TiWorker shows high CPU with zero status change over many hours — that's your intervention signal.

### Fix 2: Let it finish properly

If it's working, help it finish faster.

1. Plug in the charger — Windows deprioritizes servicing work on battery.
2. Leave the laptop on overnight with the lid open (or set to do nothing when closed) — don't let it sleep.
3. Close your heavy apps — give TiWorker uncontested CPU and disk so it finishes sooner.
4. Don't reboot repeatedly "to make it stop" — each reboot restarts servicing phases and extends the total time.
5. Check in the morning: **Settings** > **Windows Update** should show everything installed, and TiWorker should be quiet. If so, you're done — it was never broken.

### Fix 3: Run the Windows Update troubleshooter

For TiWorker that's genuinely stuck, start with the automated fix.

1. **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
2. Apply everything it suggests — it resets update services, clears caches, and repairs common stuck states.
3. Reboot after it completes, then check Windows Update for what happens next: successful install = fixed.
4. If the troubleshooter says it couldn't fix everything, note what it reports — that directs the manual steps below.
5. Give the system one more plugged-in idle session after the troubleshooter before judging — repaired update pipelines often need a clean run to finish.

### Fix 4: Reset the Windows Update components manually

Clear the corrupted state TiWorker keeps tripping on.

1. Open an elevated terminal (Terminal as Administrator).
2. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
5. Go to **Settings** > **Windows Update** > **Check for updates** — Windows rebuilds fresh caches and re-downloads what's needed.
6. This is the fix for the classic "TiWorker at 80% CPU every boot for weeks" — a corrupted datastore it could never get past. The old folders can be deleted after a week of healthy updates.

### Fix 5: Free disk space and repair the component store

TiWorker fails when it has no room or a broken store.

1. Check free space on C: — TiWorker needs several GB of working room. If under 10GB free, clean up: **Settings** > **System** > **Storage** > **Temporary files** (see our [disk space guide](/articles/how-to-free-up-disk-space-on-windows-11/)).
2. Elevated terminal: `DISM /Online /Cleanup-Image /RestoreHealth` — this repairs the component store TiWorker services. It can take 20+ minutes; let it finish.
3. Then `sfc /scannow` and reboot.
4. After repairs, check Windows Update again — a repaired store often lets the previously-failing update install cleanly on the next attempt.
5. If DISM itself fails, use a Windows 11 ISO as the repair source (`DISM /Online /Cleanup-Image /RestoreHealth /Source:...`) — Microsoft documents the servicing commands at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 6: Identify and remove the blocking update

Sometimes one specific update is the problem.

1. **Settings** > **Windows Update** > **Update history** — look for updates marked **Failed** with error codes, especially ones failing repeatedly.
2. Note the KB number. Search it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) — check its release notes and known issues; sometimes Microsoft acknowledges a bad update within days.
3. Uninstall the suspect update: **Update history** > **Uninstall updates** > select the KB > Uninstall. Reboot.
4. Then **Pause updates** for 1–2 weeks (Windows Update > Pause updates) to avoid immediate reinstallation while Microsoft fixes it.
5. Alternatively, download the KB manually from the Update Catalog and install it standalone — manual installs bypass whatever was corrupting the Windows Update pipeline delivery.
6. After the pause expires, unpause and let updates flow — the fixed version usually installs cleanly.

### Fix 7: The servicing-stack escalation

For TiWorker broken at a fundamental level.

1. Install the latest **Servicing Stack Update (SSU)** manually from the Update Catalog — the SSU is the update-installer itself, and an outdated/broken SSU breaks everything above it. Search the catalog for "servicing stack" + your Windows build.
2. Check for pending file-rename operations stuck in the registry (`HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\PendingFileRenameOperations`) — a huge backlog here means reboots aren't completing servicing; clear it only if you understand the entries, or let an expert handle it.
3. [Perform a clean boot](/articles/how-to-perform-clean-boot-windows-11-on-laptop/) and run Windows Update there — if updates complete in clean boot, a third-party filter driver (AV, encryption) is interfering with servicing.
4. Last resort before reinstall: in-place upgrade with [Windows 11 media](https://www.microsoft.com/en-us/software-download/windows11) — keeps files and apps while replacing the entire servicing stack.
5. Document the KB numbers and error codes from your Update history — if you end up seeking help, "KB50XXXXX fails with 0x800f0922, TiWorker loops" gets expert attention immediately.

## Closing

TiWorker high CPU after an update is usually the system finishing its work — give it a plugged-in night before touching anything. When it's genuinely stuck, the cycle is always the same: corrupted update state, retried forever. Reset the update components, repair the store, remove the blocking KB, and TiWorker goes back to being the quiet background worker it was designed to be.
