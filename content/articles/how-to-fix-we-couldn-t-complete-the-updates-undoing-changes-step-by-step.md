---
title: "How to Fix 'We Couldn't Complete the Updates, Undoing Changes' Step by Step"
slug: how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-step-by-step
date: 2026-09-23
categories: ["windows-update"]
tags: ["couldn't complete updates", "undoing changes", "step by step", "windows 11", "update fix"]
description: "A clear step-by-step walkthrough to fix 'We couldn't complete the updates, undoing changes' on any Windows laptop — no guesswork, just ordered steps."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-step-by-step.webp"
faqs:
  - q: "How long does the full step-by-step fix take?"
    a: "Budget about two hours if you do everything, though most loops break much earlier. The rollback observation takes 30 to 60 minutes, the cache reset about 10, and DISM/SFC another 20 to 40. The in-place upgrade at the end is the longest single step at 30 to 90 minutes. Because each step includes a verification check, you stop the moment updates work — most people never reach the final steps."
  - q: "Do I need any special tools or downloads for these steps?"
    a: "No. Every step uses tools already on your laptop — Settings, Command Prompt, Disk Cleanup, and the built-in troubleshooter — except two optional downloads: Microsoft's show-or-hide updates troubleshooter and the Windows 11 ISO for the final repair step. Both come from official Microsoft sources linked in the guide. No third-party utilities are needed or recommended."
  - q: "What if I get stuck on one of the steps?"
    a: "Each step is designed to be safe to repeat or skip past. If a command fails, note the exact error message — it is diagnostic information, not a dead end — and continue to the next step; later repairs often resolve whatever blocked the earlier one. The in-place upgrade at the end rebuilds the entire servicing stack, which is why it sits last: it fixes problems the earlier steps cannot even see."
  - q: "Can I do these steps in a different order?"
    a: "You can, but the order is deliberate: it runs from most likely cause to least, and from least invasive to most. Jumping to the in-place upgrade first wastes an hour when a five-minute cache reset would have fixed it. The one exception is a frozen rollback screen — handle that emergency first with the recovery steps, then return to this sequence."
---

This is the no-guesswork version: a strict step-by-step sequence for "We couldn't complete the updates, undoing changes" that works on any Windows laptop, any brand. No branching, no "try this random tip from a forum" — just ordered steps where each one rules out a cause and verifies before you move on. Follow them top to bottom, stop when updates work, and you will have fixed the loop in the minimum possible time.

The sequence is built on one principle: likelihood order. The steps that fix the most cases come first, and the most invasive steps come last. That means the average reader finishes in under an hour without ever reaching the heavy repairs. Keep the charger connected throughout, and do not skip the verification checks — they are what tell you to stop.

If the rollback screen is currently displayed and frozen, read Fix 1 carefully before anything else: it tells you how to confirm "frozen" versus "slow," because the two demand opposite responses.

## Why this happens

- **Corrupted update cache:** the most common cause — bad staged downloads failing every retry identically.
- **Damaged component store:** WinSxS corruption blocking all package staging.
- **Driver conflicts:** OEM or outdated drivers failing migration during the update.
- **Low disk space:** the update plus rollback snapshot needs 10 to 20 GB of room.
- **Security software interference:** file locks from third-party suites during installation.
- **Outdated firmware:** BIOS prerequisites failing silently on newer Windows builds.
- **A defective update package:** occasionally the KB itself is broken.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Observe the rollback and gather facts

Step one is always information. Do not change anything until you have it.

1. If the "undoing changes" screen is showing, plug in the charger and watch the disk activity light for 30 minutes — blinking means working, dark means stuck.
2. On the desktop, open Settings, then Windows Update, then Update history; write down the failed KB number and error code.
3. Check free space on C: under Settings, then System, then Storage.
4. Look up the error code on Microsoft's [update support pages](https://support.microsoft.com/en-us/windows).
5. If the screen is confirmed frozen (no activity for over an hour), follow the [frozen rollback recovery steps](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-in-windows-11-24h2/) first, then return here.

### Fix 2: Run the Windows Update troubleshooter

The automated first repair — clears stuck services and bad metadata with no risk.

1. Open Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Click Run next to Windows Update.
3. Apply every fix it recommends.
4. Restart the laptop.
5. Open Windows Update and click Check for updates — if the failed package installs, stop here. If the troubleshooter itself fails, use the [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/).

### Fix 3: Reset the update cache

The highest-yield manual repair. A poisoned cache is the number-one persistent cause.

1. Open Command Prompt as administrator (search "cmd," right-click, Run as administrator).
2. Type `net stop wuauserv` and press Enter; repeat for `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Type `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and press Enter.
4. Type `ren C:\Windows\System32\catroot2 catroot2.old` and press Enter.
5. Restart the four services with `net start` versions of the same commands, reboot, and check for updates.

### Fix 4: Repair system files with DISM and SFC

If the loop survived the cache reset, repair the store the updates stage into.

1. In an elevated Command Prompt, type `DISM /Online /Cleanup-Image /RestoreHealth` and press Enter.
2. Wait for it to reach 100 percent — 10 to 30 minutes; do not close the window.
3. Type `sfc /scannow` and press Enter; wait for verification to complete.
4. Restart the laptop.
5. Check Windows Update again and verify in Update history.

### Fix 5: Update drivers and free disk space

Two parallel tracks in one step: refresh the driver stack and give the installer room.

1. Visit your laptop manufacturer's support site and install current chipset, graphics, and storage drivers for your exact model.
2. Check for a BIOS update; install it with the charger connected if one is available.
3. Run Disk Cleanup as administrator, select Windows Update Cleanup and Temporary files, and confirm 20 GB free on C:.
4. Disconnect USB peripherals and temporarily disable third-party antivirus.
5. Retry Windows Update in this clean, current state.

### Fix 6: Hide the specific failing update

If exactly one KB keeps failing while everything else succeeds, quarantine it.

1. In Update history, confirm the same KB fails every time.
2. Download and run Microsoft's show-or-hide updates troubleshooter.
3. Choose Hide updates and select the failing KB.
4. Run Windows Update — everything else should now install cleanly.
5. Revisit the hidden KB in a month; Microsoft often revises broken packages quietly.

### Fix 7: In-place upgrade repair

The final step rebuilds the entire servicing stack while keeping your files and apps.

1. Download the Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Double-click the ISO to mount it, then run setup.exe.
3. Choose "Keep personal files and apps" when asked.
4. Let the upgrade complete — 30 to 90 minutes — without interrupting it.
5. Open Update history afterward and confirm clean, successful entries. For ongoing methodical troubleshooting habits, our [diagnostic walkthrough](/articles/windows-update-says-undoing-changes-made-to-your-computer-troubleshooting/) is a good companion.

## Closing

That is the whole sequence: observe, troubleshoot, reset the cache, repair the store, refresh drivers and space, quarantine the bad KB, and rebuild the stack as the finale. It works because it is ordered by likelihood and verified at each stage — no step is wasted, and you always know exactly where you stand. Save this page; the next update loop will be shorter because you will start with answers instead of anxiety.
