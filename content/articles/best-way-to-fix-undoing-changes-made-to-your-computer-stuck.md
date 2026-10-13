---
title: "The Best Way to Fix 'Undoing Changes Made to Your Computer' Stuck"
slug: best-way-to-fix-undoing-changes-made-to-your-computer-stuck
date: 2026-10-10
categories: ["windows-update"]
tags: ["undoing changes", "stuck rollback", "windows update", "best fix", "windows 11"]
description: "The definitive best-practice method for a stuck 'Undoing changes' screen: the right wait window, the safe intervention, and the root-cause fix that prevents repeats."
thumbnail: "/images/thumbs/best-way-to-fix-undoing-changes-made-to-your-computer-stuck.webp"
faqs:
  - q: "What is the single best first step for a stuck undo screen?"
    a: "Wait — but wait correctly. Give the rollback one full hour on an SSD or two hours on a hard drive, watching the disk activity light the whole time. Most 'stuck' rollbacks are slow rollbacks, and intervening early is the main way people convert a recoverable situation into a boot-repair project. Patience with verification beats every shortcut."
  - q: "Is there a best order for the fixes?"
    a: "Yes: verify the stall, force a safe restart, clear the update cache, free disk space, repair the system image, update drivers, then retry the update under controlled conditions. This order matters because each step assumes the previous one — retrying the update before clearing the corrupted cache just reproduces the same failure, which is the most common reason people get stuck in a loop."
  - q: "What is the biggest mistake people make with this screen?"
    a: "Force-restarting within the first 30 minutes. The rollback gives no progress feedback, so an hour of apparent stillness can be perfectly normal on a hard drive. Early restarts interrupt a working rollback and add boot corruption to the original problem. The second biggest mistake is retrying the update immediately without fixing the cause — that just schedules the next stuck rollback."
  - q: "How do I stop this from happening again?"
    a: "Fix the original update failure, not just the stuck screen. Clear the corrupted update cache, keep at least 20 GB free on the system drive, update drivers and BIOS before major updates, and run updates on AC power with a stable connection. The stuck rollback is a symptom; the failed update is the disease, and the disease is what the retry preparation cures."
---

Of all the Windows screens that inspire panic, 'Undoing changes made to your computer' with its endless spinning dots ranks near the top. The irony is that the screen itself is good news: it means a failed update is being rolled back to your last working system. The panic comes from the silence — no progress bar, no estimate, no way to tell whether the rollback is working or frozen.
There is a best way to handle this, and it is not the most common way. The common way is to wait twenty minutes, panic, force a restart, and then retry the update immediately — which reproduces the exact failure that caused the rollback. The best way is a disciplined sequence: verify the stall with a real wait window, intervene safely only when the stall is genuine, fix the root cause of the original failure, and retry under controlled conditions.
This guide is that sequence, distilled. It draws on the same repair logic as the brand-specific editions — the [HP undoing-changes guide](/articles/how-to-fix-windows-update-undoing-changes-stuck-on-hp-laptop/) covers HP's particular wrinkles — but here the focus is the universal best practice that works on any Windows 11 laptop. Follow it in order and you will fix this once instead of fighting it repeatedly.

## Why this happens

- **The update failed and the rollback began.** Driver conflicts, corrupted downloads, or blocked writes abort the install; Windows reverses course.
- **The rollback is slow, not stuck.** Thousands of file restorations take up to two hours on slow storage with no progress display.
- **The rollback genuinely stalled.** Drive problems, exhausted space, or software conflicts can freeze the undo mid-process.
- **The update cache is corrupted.** Bad download data poisons both the install and the rollback.
- **Disk space ran out.** The undo needs working room; a full drive stalls it.
- **Security software interfered.** Overly aggressive protection blocks the rollback's file operations.
- **The root cause was never fixed.** Retrying the update without repairs reproduces the failure and the stuck screen.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait the correct window — with verification

The best first step is disciplined patience. Most stuck screens are slow screens, and the disk light tells you which.

1. Note the exact time the screen appeared.
2. Wait one full hour on an SSD, two full hours on a mechanical hard drive.
3. Watch the disk activity light and listen for drive noise throughout the window.
4. Continue only after the full window with zero screen change and zero drive activity.

### Fix 2: Force a safe restart

A verified stall will not resolve itself. Interrupting a frozen rollback is safe because the system was already being restored.

1. Hold the power button for 10 seconds until the laptop powers off.
2. Disconnect all USB devices, docks, and external monitors.
3. Wait 30 seconds, then power on and let the boot complete uninterrupted.
4. If Automatic Repair appears, let it run to completion.

### Fix 3: Clear the update cache

The corrupted cache is the most common root cause of the original failure. Removing it is non-negotiable before any retry.

1. In an elevated Command Prompt, run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands and reboot.
4. Do not retry the update yet — the remaining fixes come first.

### Fix 4: Free disk space

Space starvation causes both the original failure and the stalled rollback. Confirm room before anything else proceeds.

1. Open Settings > System > Storage and verify at least 20 GB free on C:.
2. Run Disk Cleanup with system files selected; remove update cleanup and temporary files.
3. Move large personal files to external storage; uninstall unused programs.
4. Re-verify the free space — this step is quick and fixes a real share of cases.

### Fix 5: Repair the system image

Image corruption is the deeper root cause behind many original failures. Repair it before the retry.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` (15–30 minutes).
2. Follow with `sfc /scannow` to completion.
3. Restart the laptop after both tools finish.
4. Check the official [Microsoft support guidance](https://support.microsoft.com/en-us/windows) if either tool reports unfixable damage.

### Fix 6: Update drivers and BIOS

Driver conflicts are the other great root cause. Current drivers make the retry dramatically safer.

1. Update display, storage, and network drivers from the laptop manufacturer's support site.
2. Check for a BIOS update and install it on AC power if one is available.
3. In Device Manager, roll back any driver installed just before the failures began.
4. Reboot after the driver refresh.

### Fix 7: Retry the update under controlled conditions

The retry is the payoff for the preparation. Run it deliberately, not hopefully.

1. Connect to AC power and a stable, unmetered network.
2. Temporarily disable third-party antivirus real-time protection during the attempt.
3. Install via Settings > Windows Update while you can observe it.
4. If it fails, record the exact error code — or grab the standalone package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) — instead of retrying blindly.

### Fix 8: Learn the early warning signs of the next failure

The stuck rollback never arrives without warning — the original update failure telegraphs it. Recognizing the signs lets you intervene before the rollback screen appears.

1. An update stuck at the same percentage for over two hours is the classic precursor — investigate it with the [stuck undo-screen guide for Dell](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-dell-laptop/) logic before forcing anything.
2. Repeated 'failed to install' entries for the same KB in update history predict the next rollback.
3. Driver updates that fail in Device Manager often precede update-phase failures.
4. Acting on these warnings — clearing the cache early, updating the driver — prevents the stuck screen entirely.

## Closing

The best way to fix a stuck 'Undoing changes' screen is a sequence, not a trick: verify the stall, restart safely, clear the cache, free space, repair the image, refresh drivers, and retry deliberately. Every shortcut — the early restart, the immediate retry — is how people end up seeing this screen twice. Do it right once, and the screen becomes what it was meant to be: a brief safety net, not an afternoon.
