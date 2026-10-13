---
title: "How to Defragment a Hard Drive on Windows 11"
slug: how-to-defragment-hard-drive-on-windows-11
date: 2026-10-11
categories: ["performance"]
tags: ["defragment", "hard drive", "hdd", "windows 11", "optimization"]
description: "Should you defrag on Windows 11? Learn when defragmentation helps, when it harms (SSDs), and how to run and schedule it correctly."
thumbnail: "/images/thumbs/how-to-defragment-hard-drive-on-windows-11.webp"
faqs:
  - q: "Should I defragment my SSD on Windows 11?"
    a: "No — never run traditional defragmentation on an SSD. SSDs have no moving parts, so file fragmentation doesn't slow them, and defragging just wastes write cycles, shortening the drive's life. Windows 11 knows this: its Optimize Drives tool sends a TRIM command to SSDs instead of defragmenting them. If your drive shows as 'Solid state drive' in Optimize Drives, use Optimize (TRIM), not Defragment."
  - q: "How do I know if my drive needs defragmenting?"
    a: "Open the Optimize Drives tool (search 'Defragment' in Start) and click Analyze on your hard drive — it reports the current fragmentation percentage. Under about ten percent, defragging isn't worth the time; above fifteen to twenty percent on a spinning HDD, you'll likely feel the improvement. Windows also runs automatic optimization weekly by default, so heavy fragmentation usually means that schedule was disabled."
  - q: "How long does defragmenting take?"
    a: "It depends on drive size, fragmentation level, and speed — anywhere from twenty minutes to several hours on a large, badly fragmented HDD. Run it when you don't need the laptop, ideally overnight, and leave the machine plugged in. Interrupting a defrag isn't dangerous (the tool is designed to be stoppable), but it wastes the progress made so far."
  - q: "Does Windows 11 defragment automatically?"
    a: "Yes. Windows 11 schedules automatic optimization weekly by default — defrag for HDDs, TRIM for SSDs — through the Optimize Drives schedule. Most fragmentation problems happen because this schedule got turned off by a 'tweaking' guide or third-party optimizer. Before defragging manually, check that the automatic schedule is on; that's the real long-term fix."
---

Defragmentation is one of the oldest Windows maintenance rituals — and one of the most misunderstood on modern hardware. On a spinning hard drive, it still genuinely helps: it reorganizes scattered file fragments into contiguous runs so the read head stops dancing across the platter. On an SSD, it's pointless at best and harmful at worst. Windows 11 handles both cases, but only if you use the right tool the right way.

This guide covers how to check fragmentation, run the built-in Optimize Drives tool correctly, schedule it, and — critically — how to make sure you're not defragging an SSD. Five minutes of correct setup beats every third-party "disk optimizer" on the market.

## Why this happens

- **File fragmentation on HDDs:** As files are created, modified, and deleted, new data lands in scattered free-space gaps.
- **Disabled automatic optimization:** Tweaking guides and third-party tools often turn off Windows' weekly schedule.
- **Nearly full drives:** Fragmentation accelerates when free space is scarce, since the drive can't find contiguous runs.
- **Large file churn:** Video editing, downloads, and game installs fragment HDDs faster than office use.
- **Confusing SSD with HDD:** Running defrag on an SSD wastes write endurance for zero speed benefit.
- **Third-party "optimizers":** Aggressive third-party defraggers can fight Windows' own schedule and cause churn.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify your drive type before touching anything

Open the Optimize Drives tool (search "Defragment and Optimize Drives" in Start) and look at the Media type column: it says "Hard disk drive" or "Solid state drive" for each volume. This single check decides everything — HDDs get defragmentation, SSDs get TRIM optimization, and never the reverse. While you're here, note the "Last run" column: if automatic optimization hasn't run in months, that's likely your whole problem. Getting the drive type wrong is the one mistake in this guide that can actually harm hardware, so don't skip this step.

1. Search "Defragment and Optimize Drives" and open it.
2. Check the Media type column for each drive.
3. Note the "Last analyzed" and last-run dates.
4. Proceed with HDD steps or SSD steps accordingly.

### Fix 2: Analyze fragmentation on a hard drive

Select your HDD in Optimize Drives and click Analyze. The tool reports the fragmentation percentage — this is your evidence-based go/no-go decision. Below 10%: don't bother; the drive is fine and defragging wastes time. Above 15–20%: defragmentation will likely produce a noticeable improvement in file access and boot times. Between 10–15%: optional, do it if the laptop feels sluggish and the drive is old. Write down the number before you start so you can verify the improvement afterward — technicians measure, they don't guess.

1. Select the hard drive and click Analyze.
2. Read the fragmentation percentage.
3. Defragment if above 15–20%; skip if below 10%.
4. Record the number for before/after comparison.

### Fix 3: Run the defragmentation correctly

With the HDD selected, click Optimize and let it work — plug the laptop in, close heavy apps, and let it run undisturbed. Don't use the laptop heavily during the pass; every new write during defrag creates new work for the tool. For very fragmented large drives, expect an hour or more — start it before bed. When it finishes, re-analyze: fragmentation should read near 0%. If it barely moved, the drive may be too full (Fix 4) or failing (Fix 6). One clean pass is the goal; running defrag repeatedly back-to-back accomplishes nothing extra.

1. Click Optimize on the fragmented HDD.
2. Keep the laptop plugged in and idle during the pass.
3. Re-analyze afterward to confirm near-zero fragmentation.
4. Don't run multiple back-to-back passes.

### Fix 4: Free space first if the drive is nearly full

Defragmentation needs elbow room — Windows recommends at least 15% free space for an effective pass. If your HDD is 90%+ full, defrag can't find contiguous runs to move fragments into, and the analyze number won't improve. Free space first: run Disk Cleanup, empty the Recycle Bin, move large media to external storage, and uninstall unused programs. Then re-analyze and defragment. This ordering matters — defragging a nearly-full drive is like tidying a closet that's stuffed to the door. The [scheduled cleanup guide](/articles/how-to-schedule-disk-cleanup-on-windows-11/) automates keeping that free space.

1. Check free space — aim for at least 15% free.
2. Run Disk Cleanup and remove large unneeded files.
3. Re-analyze fragmentation after freeing space.
4. Run the defrag pass on the now-roomier drive.

### Fix 5: Turn on (or repair) the automatic optimization schedule

Manual defragging is a one-time fix; the schedule is the permanent one. In Optimize Drives, click "Change settings" and confirm scheduled optimization is on, set to Weekly, with all drives selected. If it was off, that's why fragmentation built up — turn it on and the problem won't recur. If it was on but the "Last run" column shows it hasn't actually run, check Task Scheduler's conditions (the task may be blocked by power or idle settings) and fix those. Microsoft documents the Optimize Drives schedule in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open Change settings in Optimize Drives.
2. Enable scheduled optimization, Weekly, all drives.
3. Verify the Last run column shows recent activity.
4. Fix Task Scheduler conditions if runs are being skipped.

### Fix 6: Optimize SSDs correctly — TRIM, not defrag

If Fix 1 showed a solid-state drive, the correct maintenance is TRIM, which tells the SSD which blocks are free so writes stay fast. In Optimize Drives, selecting an SSD and clicking Optimize sends the TRIM command — safe, quick, and the only "optimization" an SSD needs. Verify TRIM is actually enabled: run `fsutil behavior query DisableDeleteNotify` in an admin Command Prompt — it should return 0. If your SSD feels slow despite TRIM, check its health with the manufacturer's tool and free space (SSDs slow down when nearly full, exactly like HDDs). Never let a third-party tool "defrag" your SSD. For broader SSD-era speedups, see the [Windows 11 speed-up guide](/articles/how-to-speed-up-windows-11-laptop/).

1. Select the SSD in Optimize Drives and click Optimize (TRIM).
2. Verify TRIM with `fsutil behavior query DisableDeleteNotify`.
3. Keep 15–20% free space for the SSD controller to work with.
4. Check SSD health with the manufacturer's diagnostic if slowdowns persist.

## Closing

Defragmentation isn't dead — it's just drive-specific now. HDDs: analyze, defragment when fragmentation is high, and keep the weekly schedule on. SSDs: TRIM via the same tool, never defrag. Get the drive type right in Fix 1, and everything else in this guide is straightforward maintenance that keeps storage fast for years.
