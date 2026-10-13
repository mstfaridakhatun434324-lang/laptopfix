---
title: "Windows Update Stuck on Restarting? The Best Way to Fix It"
slug: best-way-to-fix-windows-update-stuck-on-restarting
date: 2026-09-05
categories: ["windows-update"]
tags: ["stuck on restarting", "windows update", "frozen update", "windows 11", "boot loop"]
description: "Your laptop has been 'restarting' for an hour with no progress. Here's the safe way to break the freeze and finish the update."
thumbnail: "/images/thumbs/best-way-to-fix-windows-update-stuck-on-restarting.webp"
faqs:
  - q: "How long should I wait before deciding the update is stuck?"
    a: "Wait at least two hours with the drive light active before intervening. Large updates legitimately sit on the restarting screen for a long time, especially on laptops with spinning hard drives or slow SSDs. Only act when there is zero disk activity for an extended period, or when the same screen has persisted far beyond three hours."
  - q: "Is it safe to force-shut-down during a stuck update?"
    a: "It is safer than most people think. Windows is designed to recover from interrupted updates by rolling back to the previous state. Hold the power button for ten seconds to power off, wait thirty seconds, then power on. The system will either resume the update or roll it back — both are handled automatically."
  - q: "Will I lose files if the update was stuck while restarting?"
    a: "No. The restarting phase does not touch your personal files; it only swaps system files. Even if the update rolls back completely, your documents, photos, and applications remain untouched. File loss during updates is extremely rare and usually tied to failing drives, not stuck restarts."
  - q: "Why does my laptop get stuck on restarting every update?"
    a: "Recurring stuck restarts usually mean a driver is hanging during shutdown, Fast Startup is preserving bad state, or the disk is struggling. If it happens with every update, investigate shutdown-blocking drivers and disk health rather than treating each incident in isolation."
---

The screen says "Restarting" and the little spinner keeps spinning — for an hour, then two. Your laptop is neither finishing the update nor returning to Windows. This is one of the most stressful Windows moments because it feels like any action might break something, and the machine gives you nothing to work with.

Here is the reassuring truth: the restarting phase is recoverable by design. Windows anticipates interruptions here and knows how to roll back. The best fix is a calm, ordered sequence: confirm it is truly stuck, break the freeze safely, let the rollback happen, then address the root cause so it does not repeat.


First, rule out normal slowness: large updates on laptops with hard drives or nearly full SSDs can legitimately display the restarting screen for over an hour. Check for drive activity and heat before concluding anything is wrong. The fixes below assume you have waited at least two hours with zero activity — intervening earlier risks interrupting a working update.
## Why this happens

- **Driver hanging at shutdown:** A misbehaving driver refuses to unload, freezing the restart sequence.
- **Fast Startup preserving bad state:** Hybrid shutdown carries the frozen state forward across reboots.
- **Disk errors:** Bad sectors in the update staging area stall the file swap.
- **Insufficient free space:** The update cannot complete its file operations mid-restart.
- **Conflicting software:** Disk encryption or third-party security tools can block the restart handoff.
- **Corrupted update payload:** A damaged download fails integrity checks during the restart phase.
- **Failing storage:** A dying SSD or HDD stalls on writes the update requires.
- **Windows Update Medic interference:** The medic service restarting components mid-shutdown in a loop.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is genuinely stuck

1. Wait at least **two hours** from when the spinner started, longer on older laptops.
2. Watch the drive activity light (if your laptop has one) and listen for disk sounds.
3. Zero activity for 30+ minutes means stuck; intermittent activity means still working.
4. Do not intervene while the drive is active — patience here prevents a rollback you might not need.
5. Note the exact time the spinner started so you can measure the wait objectively.
6. If the laptop has a removable battery, note whether the behavior differs on battery versus AC power.

### Fix 2: Force a safe shutdown

1. Press and hold the power button for a full **10 seconds** until the machine powers off.
2. Unplug the charger and, if the battery is removable, remove it for 30 seconds.
3. Wait another 30 seconds to let all capacitors drain and state clear.
4. Power on. Windows will detect the interrupted update and either resume it or begin rolling back automatically.
5. If the laptop immediately returns to the stuck screen on power-up, force shutdown once more and try booting to Safe Mode.
6. Do not open the laptop or remove internal components — the fix is software-side.

### Fix 3: Let the rollback complete

1. On boot you may see "Undoing changes made to your computer" — this is the safety net working.
2. Do not power off during the rollback; interrupting the rollback is riskier than interrupting the update.
3. Give it up to an hour. Rollbacks on slow disks take a while.
4. When Windows returns to the desktop, verify your files and settings are intact before doing anything else. If the rollback itself stalls, see our guide on [updates stuck on the restarting screen](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/).
5. During the rollback, keep the charger connected — a power loss mid-rollback is the one scenario to avoid.
6. If the rollback percentage stalls too, give it the same two-hour patience before acting. For rollbacks that never complete, see our guide on [updates that get stuck undoing changes](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-windows-11/).

### Fix 4: Disable Fast Startup

1. Once back in Windows, open **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Shut down fully (not restart), then power on.
4. Fast Startup is a frequent contributor to stuck restarts because it preserves driver state that should have been cleared.
5. After disabling Fast Startup, also disable hibernation temporarily with powercfg /hibernate off for a full cold boot.
6. Re-enable hibernation later only if you use it — many laptop users never miss it.

### Fix 5: Clear the failed update and its cache

1. Open an elevated Command Prompt and run `net stop wuauserv` and `net stop bits`.
2. Delete the contents of `C:\Windows\SoftwareDistribution\Download`.
3. Restart both services with `net start wuauserv` and `net start bits`.
4. Run Disk Cleanup on C: including **Windows Update Cleanup** to remove the failed payload's remnants.
5. After clearing the cache, run the Windows Update troubleshooter to validate the reset.
6. Check that the SoftwareDistribution folder was recreated with fresh timestamps.

### Fix 6: Check disk health

1. In an elevated Command Prompt, run `chkdsk C: /f /r` and approve the scan for the next restart.
2. Restart and let the full scan complete — it can take an hour or more.
3. Check the drive's SMART status with your manufacturer's diagnostic tool or a third-party utility.
4. Recurring stuck restarts with disk errors mean the drive is failing; back up immediately and plan a replacement.
5. Focus the disk check on the system partition; bad sectors there stall the restart file swap.
6. If chkdsk finds bad sectors, schedule monthly disk health checks going forward.

### Fix 7: Retry the update cleanly

1. Update your chipset and storage drivers from the manufacturer's support site first.
2. Temporarily disable third-party antivirus during the retry.
3. Run Windows Update and install the update again, keeping the laptop plugged in.
4. If it stalls again at the same point, install it manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) using its KB number, or follow Microsoft's [official troubleshooting guidance](https://support.microsoft.com/en-us/windows).
5. Install chipset and storage drivers before the retry — they govern the shutdown and boot handoff.
6. After the successful update, re-enable Fast Startup only if you want it; leaving it off is harmless.

## Closing

A stuck "Restarting" screen is frightening but almost always survivable: confirm the freeze, power off cleanly, let the rollback do its job, then fix the underlying cause before retrying. If it keeps happening with every update, the pattern points at drivers or a struggling disk rather than bad luck. Address that root cause once, and updates go back to being boring — which is exactly what you want. If stuck restarts become a pattern rather than an incident, treat it as a maintenance signal: update drivers, check disk health, and clear update debris regularly. Prevention beats recovery every time.
