---
title: "Windows 11 Slow After an Update? Full Troubleshooting Walkthrough"
slug: "troubleshoot-windows-11-slow-after-update"
date: "2026-09-13"
categories: ["performance"]
tags: ["windows update", "slow after update", "windows 11", "performance", "troubleshooting"]
description: "Your laptop was fine until the latest Windows 11 update, and now everything lags. Follow this systematic walkthrough to identify what the update changed and roll back the damage."
thumbnail: "/images/thumbs/troubleshoot-windows-11-slow-after-update.webp"
faqs:
  - q: "Why is Windows 11 slow after installing an update?"
    a: "Updates change drivers, reset power and privacy settings, trigger days of background re-indexing and re-optimization, and occasionally introduce genuine performance bugs. Most post-update slowness is transitional — background tasks finishing — but persistent slowness beyond 48 hours usually means a driver regression, a changed setting, or a stuck update component."
  - q: "How long should I wait before troubleshooting post-update slowness?"
    a: "Give it 24 to 48 hours of normal use with the laptop plugged in and occasionally idle. Windows performs .NET optimization, search re-indexing, and update cleanup in the background after major updates. If slowness persists beyond two days, or is severe enough to prevent work, start troubleshooting immediately rather than waiting."
  - q: "Can I uninstall a Windows 11 update that made things slow?"
    a: "Yes, within 10 days for feature updates via Settings, System, Recovery, Go back. Quality (cumulative) updates can be uninstalled anytime via Settings, Windows Update, Update history, Uninstall updates. Uninstalling is a valid diagnostic step — if speed returns, you have confirmed the update as the cause and can pause updates while Microsoft fixes it."
  - q: "Do Windows updates reset my performance settings?"
    a: "Sometimes. Feature updates have been known to reset power plans to Balanced, re-enable startup apps, restore default privacy settings, and reinstall removed bloatware. Part of post-update troubleshooting is simply re-applying your previous tuning — check power mode, startup apps, and background app permissions after every major update."
---

The pattern is so common it has become a cliché: Tuesday evening your laptop is fine, Wednesday morning after an overnight update it feels like a different, worse machine. Boot takes longer, apps stutter, the fan runs constantly. Your first thought — "the update broke something" — is often half right. Updates do sometimes introduce real regressions, but just as often the slowness comes from what the update triggered: background re-indexing, driver swaps, reset settings, and cleanup tasks that all compete for your hardware at once.

The trick to post-update troubleshooting is distinguishing transitional slowness (which resolves itself) from real damage (which needs action). This walkthrough does that systematically: confirm the timeline, let legitimate background work finish, check what the update changed, and then repair or roll back as appropriate.

## Why this happens

- **Background post-update optimization:** .NET NGEN optimization, search re-indexing, and Store app updates run for hours after major updates.
- **Driver replacements:** Updates install new GPU, chipset, or storage drivers that may perform worse than the manufacturer's versions.
- **Reset power and performance settings:** Feature updates revert power plans to Balanced and re-enable power-saving throttles.
- **Reinstalled bloatware and startup apps:** Removed OEM apps and disabled startup entries sometimes return after feature updates.
- **Stuck update components:** A partially failed update leaves TiWorker and related services looping indefinitely.
- **New bugs in the update itself:** Some cumulative updates genuinely introduce performance regressions affecting specific hardware.
- **Disk cleanup of old system files:** Post-update cleanup of Windows.old and component stores is disk-heavy for a day or two.
- **Changed virtualization/security defaults:** Updates occasionally enable Memory Integrity or other VBS features that cost performance.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Establish the timeline and wait out background work

1. Confirm the correlation: check Settings, Windows Update, Update history for exactly what installed and when.
2. Note when slowness started relative to the update — same boot, or a day later.
3. Leave the laptop plugged in and idle for a few hours to let .NET optimization and indexing finish.
4. Check Task Manager during idle: if .NET Runtime Optimization Service or SearchIndexer dominate, background work is the cause.

If heavy background processes explain the slowness and they finish within a day or two, there is nothing to fix — this was transitional. Only proceed when slowness persists beyond 48 hours or no background culprit is visible. Rushing to roll back a healthy update wastes the one thing updates provide: security.

### Fix 2: Check what the update changed in your settings

1. Go to Settings, System, Power & battery — confirm Power mode is still Best performance (updates reset it to Balanced).
2. Open Task Manager's Startup apps tab — re-disable anything the update re-enabled.
3. Check Settings, Privacy & security for reset toggles: background apps, diagnostics, advertising ID.
4. Review installed apps for bloatware that returned, and remove it again.

This step alone resolves a large share of "slow after update" complaints, because the update did not make the laptop slower — it undid your tuning. It takes ten minutes and requires no technical risk. Make it a habit after every feature update: a quick settings audit before assuming anything is broken.

### Fix 3: Roll back regressed drivers

1. Open Device Manager and check Display adapters, Storage controllers, and Network adapters for driver dates matching the update.
2. For any suspect device, open Properties, Driver tab, and use **Roll Back Driver** if available.
3. Better: download the manufacturer's known-good driver from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or Lenovo's support site and install it over the update's version.
4. For Intel systems, the [Intel driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) identifies the correct chipset and graphics versions.

Driver regressions are the most common genuine cause of post-update slowness — particularly GPU drivers affecting games and video, and storage drivers affecting everything. Windows Update's driver versions prioritize compatibility over performance; manufacturer drivers prioritize your exact hardware. If rolling back a driver restores speed, block that driver from future updates via the "do not include drivers" update policy.

### Fix 4: Uninstall the problematic update (diagnostic)

1. Go to Settings, Windows Update, Update history, Uninstall updates.
2. Sort by installed date and uninstall the most recent cumulative update.
3. Restart and test performance for a day.
4. If speed returns, pause updates for two weeks (Windows Update, Pause updates) while Microsoft addresses it.

Uninstalling is both a fix and a diagnosis: if performance returns, the update was definitively the cause. For feature updates within the 10-day window, use Settings, System, Recovery, Go back instead. Do not leave updates paused indefinitely — security updates matter — but a short pause while a bad update gets fixed is reasonable and supported.

### Fix 5: Repair stuck update components

1. If TiWorker.exe or Windows Modules Installer dominates Task Manager for days, the update pipeline is stuck.
2. Open admin Command Prompt: `net stop wuauserv`, `net stop bits`, clear `C:\Windows\SoftwareDistribution\Download`, then restart both services.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`.
4. Check for updates again and let the repaired pipeline complete cleanly.

A stuck update keeps the whole system in a degraded state: background services loop, the component store stays half-updated, and performance suffers everywhere. Our [TiWorker high CPU guide](/articles/how-to-fix-tiworker-high-cpu-on-hp-laptop/) covers this failure mode in depth if update workers are your specific symptom.

### Fix 6: Check for newly enabled performance-costly features

1. Open Windows Security, Device security, Core isolation — check whether Memory Integrity got enabled by the update.
2. If enabled and you did not turn it on, test with it off (accepting the security trade-off).
3. Check Settings, Privacy & security, Windows Security for other newly enabled protections.
4. Compare performance with each change isolated — change one thing at a time.

Updates occasionally flip security features on that cost measurable performance, particularly virtualization-based security on gaming workloads. This is not a bug — it is a policy choice by Microsoft — but you deserve to make the trade-off consciously rather than discovering it as mystery slowness. Gamers should also re-check our [game stuttering fixes](/articles/how-to-fix-windows-11-stuttering-in-games/) if the slowdown is gaming-specific.

### Fix 7: Clean up post-update debris

1. Run Disk Cleanup as administrator (search "Disk Cleanup," right-click, Run as administrator).
2. Select Previous Windows installations (Windows.old) and Delivery Optimization Files if present — often tens of GB.
3. In Settings, System, Storage, run Storage Sense for a deeper pass.
4. Restart and verify free space and responsiveness.

Post-update debris wastes disk space and, on nearly-full drives, degrades performance through reduced caching and paging room. Windows.old alone can exceed 20 GB. Windows auto-deletes it after 10 days, but reclaiming it now both frees space and removes a variable. If disk pressure is your broader issue, our [disk space guide](/articles/how-to-free-up-disk-space-on-windows-11/) goes further.

## Closing

Post-update slowness is usually transitional background work, reset settings, or a regressed driver — in that order of likelihood. Wait out the background tasks, re-apply your tuning, roll back bad drivers, and only then consider uninstalling the update. Work the list methodically instead of assuming the worst, and most "the update ruined my laptop" stories end with the laptop running exactly as well as before, sometimes better.
