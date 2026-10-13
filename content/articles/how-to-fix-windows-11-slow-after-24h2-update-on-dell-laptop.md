---
title: "Fix Windows 11 Running Slow After the 24H2 Update (Dell Laptop)"
slug: how-to-fix-windows-11-slow-after-24h2-update-on-dell-laptop
date: 2026-10-02
categories: ["performance"]
tags: ["windows 11 24h2", "dell laptop", "slow after update", "24h2 performance fix", "dell drivers"]
description: "Restore speed on your Dell laptop after the Windows 11 24H2 update: fix driver regressions, reset power plans, and clear update leftovers."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-after-24h2-update-on-dell-laptop.webp"
faqs:
  - q: "Why did the 24H2 update specifically slow down my Dell laptop?"
    a: "Dell laptops depend on tuned chipset, storage, and power drivers that the 24H2 update can replace with generic versions or leave mismatched. The update also resets Dell-optimized power plans, re-enables disabled startup items, and triggers days of background reindexing. Each factor alone is minor; together they produce the unmistakable post-update slowdown Dell owners report."
  - q: "Should I use Dell Update or Windows Update for post-24H2 drivers?"
    a: "Use both, in order: Windows Update first for the OS-level pieces, then Dell Update (or Dell's support site with your Service Tag) for the tuned chipset, storage, BIOS, and power drivers. Dell's versions are validated against your exact model and 24H2, while Windows Update's generics can leave performance on the table. Never skip the Dell side after a feature update."
  - q: "How do I check if the 24H2 update is still doing background work?"
    a: "Open Task Manager and look at sustained CPU and disk consumers over several checks spaced an hour apart. Windows servicing processes like TiWorker.exe, SearchIndexer.exe, and the .NET optimization service indicate legitimate settling work — their activity should trend downward over 24 to 48 hours. Flat, unchanging high usage after two days means something is stuck, not settling."
  - q: "Is it safe to delete the Windows.old folder after 24H2?"
    a: "Yes, once you're confident you won't roll back — the folder exists solely to enable the 10-day rollback. Use Disk Cleanup's 'Clean up system files' option rather than deleting it manually, which can leave broken permissions behind. Removing it typically frees 20 to 30GB, which alone can lift an SSD out of its slow zone on nearly-full drives."
---

Your Dell laptop was fine on Tuesday. Windows installed the 24H2 feature update overnight, and now boot takes twice as long, apps hesitate, and the whole machine feels a generation older. Dell owners report this pattern more than most, and there's a reason: Dell laptops lean heavily on model-specific drivers for storage, chipset, and power management, and feature updates are exactly the kind of event that disrupts that tuning.

The encouraging news is that post-24H2 slowness on Dell hardware is a solved problem with a short list of causes. Work through them in the order below — settling time first, then the Dell-specific driver and settings checks — and most machines come all the way back without drastic measures.

## Why this happens

- **Generic drivers replacing Dell-tuned ones:** 24H2 can install generic chipset and Intel RST storage drivers over Dell's validated versions, silently reducing disk throughput.
- **Reset power plans:** The update often reverts custom or Dell-optimized power plans to Balanced, capping the boost behavior your workflow depended on.
- **Background settling work:** Search reindexing, .NET optimization, and deferred servicing legitimately consume resources for 24–48 hours after the update.
- **Re-enabled startup items:** Updates resurrect startup entries you'd disabled — Dell utilities, updaters, chat apps — restoring congestion you'd cleaned up.
- **Stuck servicing components:** A partially failed update can leave TiWorker.exe or the Modules Installer retrying endlessly.
- **Dell utilities conflicting with 24H2:** Older SupportAssist or Dell Update versions can misbehave on the new build until updated themselves.
- **Disk space crunch:** The update needs 20GB+ of working room and leaves Windows.old behind; a nearly-full drive crosses into SSD slowdown territory.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it's still settling (48-hour rule)

Check **Settings → Windows Update** for pending items, then watch Task Manager across several hours. If the heavy consumers are TiWorker.exe, SearchIndexer.exe, or ngen.exe and their activity trends downward, the laptop is finishing legitimate post-update work — let it run plugged in. Only treat it as a problem if usage stays flat and high past 48 hours.

1. Install any pending items in **Settings → Windows Update**.
2. Check Task Manager's top consumers at intervals over a day.
3. Decreasing servicing activity = settling; allow up to 48 hours plugged in.
4. Flat high usage after two days → continue to Fix 2.

### Fix 2: Restore your power plan

24H2 loves resetting power settings. Check **Settings → System → Power & battery → Power mode** — if it's on Balanced or Best power efficiency instead of your usual Best performance, you've found a big chunk of the slowdown. Dell machines with Dell Power Manager should also verify the thermal/power profile there.

1. Set **Power mode** to **Best performance** (plugged in).
2. Check **Control Panel → Power Options** for your custom plan if you used one.
3. Open **Dell Power Manager** (or MyDell) and confirm the thermal setting is back to your preference.
4. Test responsiveness before moving on — this alone fixes many reports.

### Fix 3: Update Dell drivers for 24H2

This is the highest-value Dell-specific step. Enter your Service Tag on [Dell support](https://www.dell.com/support) (or open SupportAssist → Drivers & Downloads) and install the 24H2-validated **chipset**, **Intel RST storage**, **graphics**, and **BIOS** updates. Storage and chipset drivers matter most for the "everything is slow" feeling.

1. Get your Service Tag from the sticker or **SupportAssist → System info**.
2. On Dell's support site, download chipset, storage, graphics, and BIOS updates for Windows 11 24H2.
3. Install drivers first, BIOS last — BIOS on AC power, battery charged, uninterrupted.
4. Restart and compare. The [general 24H2 slowdown guide](/articles/how-to-fix-laptop-slow-after-windows-11-24h2-update-step-by-step/) covers the non-Dell angles in parallel.

### Fix 4: Re-disable resurrected startup items

Open Task Manager → **Startup apps** and look for entries that are enabled again after the update. Dell Update, SupportAssist agents, and third-party updaters are frequent returnees. Disable what you don't need at boot.

1. Open Task Manager → **Startup apps**, sort by Status.
2. Disable non-essential re-enabled entries.
3. Keep antivirus, audio, and input drivers enabled.
4. Restart and observe boot and launch speed.

### Fix 5: Update Dell's own utilities

An outdated SupportAssist or Dell Update running on 24H2 can itself cause CPU spikes and failed background tasks. Update both to their latest versions — ironically, the tools that manage updates need updating first.

1. Open **SupportAssist** and install any self-update it offers.
2. Update **Dell Update** / **Dell Command Update** to the latest release.
3. Run a SupportAssist hardware scan afterward to rule out coincidental hardware issues.
4. Reschedule SupportAssist automatic scans to overnight hours.

### Fix 6: Repair stuck update components and free disk space

If TiWorker.exe or Windows Modules Installer still burns CPU days later, the servicing stack is stuck: run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` elevated, then the Windows Update troubleshooter. Separately, reclaim the 20–30GB Windows.old leaves behind via **Disk Cleanup → Clean up system files**, keeping C: at least 15–20% free. Microsoft's servicing guidance is at [Windows support](https://support.microsoft.com/en-us/windows).

1. Run SFC and DISM repairs in an elevated Command Prompt.
2. Run **Settings → System → Troubleshoot → Other troubleshooters → Windows Update**.
3. Disk Cleanup → Clean up system files → remove previous Windows installations.
4. Confirm C: has 15–20% free space; also see the [Lenovo 24H2 variant](/articles/how-to-fix-windows-11-slow-after-24h2-update-on-lenovo-laptop/) for cross-brand comparison.

### Fix 7: Roll back only if everything fails

Within 10 days of the update, **Settings → System → Recovery → Go back** returns you to the previous build. Back up first. This is the last resort — nearly all Dell 24H2 slowdowns yield to the driver and settings fixes above, and rolling back trades the problem for an older, less-supported build.

1. **Settings → System → Recovery → Go back** (only visible within 10 days).
2. Back up important files before starting.
3. Follow the prompts; the process preserves personal files.
4. After rollback, temporarily pause feature updates while you identify the conflicting driver.

## Closing

Post-24H2 slowness on a Dell laptop is rarely mysterious: it's settling time, generic drivers over Dell-tuned ones, reset power plans, or resurrected startup items. Give it 48 hours, restore your power settings, install Dell's 24H2-validated drivers, and clean up the leftovers. That sequence brings the overwhelming majority of Dell machines back to full speed — no rollback required.
