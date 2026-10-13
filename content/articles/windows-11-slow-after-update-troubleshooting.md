---
title: "Windows 11 Slow After an Update? Troubleshoot It in Order"
slug: "windows-11-slow-after-update-troubleshooting"
date: "2026-10-09"
categories: ["performance"]
tags: ["windows 11 slow after update", "update problems", "performance", "troubleshooting", "cumulative update"]
description: "PC slowed down right after a Windows 11 update? Diagnose whether it's background optimization, a driver conflict, or a bad update — and fix it."
thumbnail: "/images/thumbs/windows-11-slow-after-update-troubleshooting.webp"
faqs:
  - q: "How long should I wait before fixing slowness after an update?"
    a: "Give it 24-48 hours of plugged-in time first. After feature updates especially, Windows performs legitimate background work — search re-indexing, .NET native image optimization, driver re-enumeration, and Store app updates — that hammers CPU and disk temporarily. If slowness persists past 48 hours with all updates fully installed, it's a real problem worth troubleshooting, not background settling."
  - q: "Can I uninstall a Windows 11 update that made my PC slow?"
    a: "Yes, for cumulative updates: Settings > Windows Update > Update history > Uninstall updates, then select the recent KB. For feature updates (like 24H2), Settings > System > Recovery > Go back works within 10 days. Uninstalling is a valid diagnostic — if speed returns, the update (or its driver payload) was the cause, and you can then reinstall drivers before trying the update again."
  - q: "Why do updates make my laptop slower each time?"
    a: "They shouldn't, cumulatively — but each feature update carries over your existing drivers and software into a new OS build, and incompatibilities accumulate. The pattern of 'slower after every update' usually means outdated chipset/storage drivers that each new Windows build tolerates less well, plus update debris (old driver versions, stale caches). Updating drivers from your laptop maker after each feature update breaks the cycle."
  - q: "Should I pause Windows updates to keep my PC fast?"
    a: "Pausing briefly (1-2 weeks) after a problematic update is reasonable troubleshooting. Pausing permanently is not — you miss security patches, and eventually the deferred feature update installs anyway, often more disruptively. The sustainable approach: let updates install, keep drivers current from your manufacturer, and address the occasional bad update by uninstalling that specific KB rather than blocking the pipeline."
---

The pattern is maddeningly consistent: Windows 11 installs an update overnight, and in the morning your laptop feels like it's wading through mud. Apps crawl, the disk churns, fans spin — and you're left wondering whether to wait it out or start ripping things out. The answer depends on which of three situations you're in, and this guide tells you how to tell.

Situation one: legitimate post-update background work that finishes on its own (wait). Situation two: a driver or software conflict the update exposed (fix the driver). Situation three: a genuinely bad update (remove it). Most troubleshooting guides treat all three the same — they shouldn't be, because the fixes are opposites: waiting vs. acting vs. uninstalling. The 24H2 update deserves special mention here: as a full build replacement it triggers the heaviest post-update workload of any recent release, so Situation One lasts the full 48 hours on it.

Work through the diagnosis in order and you'll land in the right situation within an hour. If the update specifically spiked CPU rather than general slowness, our [high CPU in 24H2 guide](/articles/how-to-fix-high-cpu-usage-in-windows-11-24h2/) pairs with this one.

## Why this happens

- **Post-update background optimization** — Re-indexing, .NET optimization, and app re-registration legitimately saturate the system for 24-48 hours after feature updates. The most common 'cause' — and not a problem.
- **Carried-over incompatible drivers** — Feature updates keep third-party drivers; old audio, network, and storage drivers misbehave on the new build — the top real cause of persistent post-update slowness.
- **Stuck update components** — A partially installed cumulative update retries endlessly (TiWorker.exe), burning CPU/disk indefinitely until the corrupted cache is cleared.
- **Reset power and visual settings** — Updates sometimes reset power plans to Balanced-with-aggressive-saving or re-enable visual effects you'd disabled — free performance lost silently.
- **Old update debris** — Each update leaves superseded components; without cleanup, WinSxS and the SoftwareDistribution cache bloat, costing disk space and slowing servicing.
- **Antivirus re-scanning everything** — After system files change en masse, Defender and third-party AV re-scan the system — days of elevated background scanning on slow disks.
- **A genuinely bad KB** — Occasionally Microsoft ships a cumulative update with a real performance regression — rare, but it happens, and uninstalling that KB is the fix.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Diagnose first: wait or act?

The 10-minute triage that prevents fixing a non-problem.

1. Open **Settings > Windows Update** — is everything installed, including optional driver updates? If installs are pending, let them finish first.
1. Check the update date: if the feature update landed <48 hours ago and Task Manager shows SearchIndexer/mscorsvw/TiWorker busy, you're in Situation One — leave it plugged in overnight and re-evaluate tomorrow.
1. If it's been 3+ days, updates are complete, and it's still slow — you're in Situation Two or Three; continue below.
1. Also glance at Task Manager's Startup tab — updates sometimes re-enable startup entries you'd previously disabled; re-disable them. And check Device Manager for yellow warning icons, which signal a device the update left driverless.
1. Note exact symptoms: general sluggishness (continue) vs. specific app broken (update that app) vs. no boot (recovery options).

### Fix 2: Clear stuck update components

For the TiWorker-always-busy pattern — a corrupted download cache retrying forever.

1. Run **Settings > System > Troubleshoot > Other troubleshooters > Windows Update > Run**.
1. If it doesn't resolve: admin Command Prompt, `net stop wuauserv` + `net stop bits`, rename `C:\Windows\SoftwareDistribution` to `.old`, `net start wuauserv` + `net start bits`.
1. Re-check for updates and install whatever appears.
1. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents this reset procedure officially.

### Fix 3: Update the drivers the update disturbed

The highest-yield real fix for persistent post-update slowness.

1. Get chipset, storage/IRST, graphics, and network drivers from your laptop maker's support page — [Dell](https://www.dell.com/support), HP, or Lenovo — for your exact model.
1. Install chipset first, restart, then the rest — one restart between chipset and graphics at minimum.
1. Pay special attention to audio drivers (Conexant/Realtek): post-update audio driver conflicts cause the stuttery-sluggish feeling many report.
1. If a driver was working before, note its version — rollback is your fallback.

### Fix 4: Restore your power and visual settings

Updates silently reset tunings. Reclaim them.

1. **Settings > System > Power & battery > Power mode**: set back to **Best performance** (plugged in) if the update reset it.
1. Check your custom power plan still exists in **Control Panel > Power Options** — recreate if the update wiped it.
1. Re-disable visual effects you'd turned off: our [transparency guide](/articles/how-can-i-disable-transparency-in-windows-11/) has the steps.
1. These silent resets explain a surprising share of 'update made me slower' reports.

### Fix 5: Clean up update debris

Reclaim the gigabytes and servicing speed.

1. **Settings > System > Storage > Temporary files**: check **Windows Update Cleanup** and **Delivery Optimization Files**, then remove.
1. Run `dism /Online /Cleanup-Image /StartComponentCleanup` from admin Command Prompt to trim WinSxS.
1. Also enable **Storage Sense** (**Settings > System > Storage**) so temporary update files clean themselves up going forward.
1. Don't use third-party 'update cleaners' — they cause more corruption than they fix.
1. Reboot after cleanup; servicing operations speed up noticeably.

### Fix 6: Uninstall the bad KB (Situation Three)

When slowness started the day a specific cumulative update installed.

1. **Settings > Windows Update > Update history**: note the most recent KB number and its install date.
1. **Uninstall updates** > select that KB > uninstall, then restart.
1. If speed returns, pause updates for 2 weeks (**Pause updates**) to skip the bad KB while Microsoft fixes it.
1. For feature-update regressions within 10 days: **Settings > System > Recovery > Go back**. Grab fresh drivers from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) before retrying the update later.

## Closing

Post-update slowness is usually patience (48 hours), drivers (update them from your maker), or one bad KB (uninstall it) — in that order of likelihood. Diagnose which situation you're in first, and you'll fix it in an hour instead of fighting it for a week.
