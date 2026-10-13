---
title: "How to Defragment a Hard Drive in Windows 11 24H2"
slug: how-to-defragment-hard-drive-in-windows-11-24h2
date: 2026-09-12
categories: ["performance"]
tags: ["defragment", "hard drive", "windows 11 24h2", "optimize drives"]
description: "Defrag in Windows 11 24H2 explained: when it helps, when to leave SSDs alone, and how to optimize any drive step by step."
thumbnail: "/images/thumbs/how-to-defragment-hard-drive-in-windows-11-24h2.webp"
faqs:
  - q: "Should I defragment an SSD in Windows 11?"
    a: "No — never run a traditional defrag on an SSD. Flash memory has no seek penalty, so defragmenting gains nothing and wastes write cycles, shortening the drive's life. Windows 11 knows this: on SSDs the Optimize Drives tool sends a TRIM command instead, which is the correct maintenance. Just run the automatic optimization and let Windows choose the right operation."
  - q: "How often should I defragment a mechanical hard drive?"
    a: "Windows 11's default weekly automatic optimization is enough for almost everyone. Manual defrags are only worth it after major events — a feature update, installing or removing tens of gigabytes, or noticing the drive is heavily fragmented. More frequent than weekly gives diminishing returns and just wears the drive."
  - q: "Does defragmenting actually make a laptop faster?"
    a: "On a mechanical drive with significant fragmentation, yes — measurably. Boot times, app launches, and large file operations improve because the read head stops jumping around the platter. On a lightly fragmented drive or any SSD, you will not feel a difference. It fixes fragmentation slowness specifically, not general slowness."
  - q: "How long does defragmenting take?"
    a: "Anywhere from a few minutes to several hours. A 1TB mechanical drive at 20% fragmentation typically takes 1–3 hours; a nearly full drive takes longer because the tool needs free space to shuffle files. SSD TRIM optimization finishes in seconds to a couple of minutes. Run it plugged in and let it finish uninterrupted."
---

Defragmentation is one of the oldest Windows maintenance tasks, and also one of the most misunderstood. On a mechanical hard drive, it still matters: files scattered across the platter in hundreds of fragments force the read head to dance, and every dance costs milliseconds that add up to a sluggish laptop. On an SSD, the same operation is pointless at best and harmful at worst.

Windows 11 24H2 handles most of this automatically — but "most" is doing heavy lifting in that sentence. This guide shows you how to check fragmentation, run the right optimization for your drive type, schedule it properly, and recognize when fragmentation is not actually your problem.

## Why this happens

- **Files fragment naturally:** As files grow, shrink, and get edited, Windows places new pieces wherever free space exists — fragmentation is normal physics, not a malfunction.
- **Nearly full drives fragment faster:** With little free space, Windows cannot place files contiguously, so fragmentation accelerates as the drive fills.
- **Large installs and updates scatter data:** Feature updates and big game installs write gigabytes in pieces, leaving the drive heavily fragmented afterward.
- **Automatic optimization gets disabled:** Third-party "optimizer" tools and some tweaks turn off the scheduled task, so fragmentation accumulates for years.
- **SSDs get mistreated:** Running old-school defrag tools on SSDs wastes write endurance for zero benefit — the wrong maintenance on the wrong drive.
- **People defrag the wrong bottleneck:** Fragmentation gets blamed for slowness actually caused by a dying drive, malware, or 100% disk saturation from services.
- **External and secondary drives are forgotten:** Windows only auto-optimizes on its default schedule for drives it knows about; externals often go years without it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify your drive type first

1. Open Task Manager (**Ctrl + Shift + Esc**) → **Performance** and click each disk — the label says **HDD** or **SSD**.
2. Alternatively, search **Defragment and Optimize Drives** in the Start menu and open it — the **Media type** column shows the same info.
3. This determines everything: HDDs get defragmented, SSDs get TRIMmed. Never mix them up.
4. If you are unsure about the drive's health before optimizing, our [100% disk guide](/articles/how-to-fix-disk-active-time-100-percent-youtube/) shows how to check SMART status first — defragging a dying drive is wasted effort.

### Fix 2: Analyze fragmentation before acting

1. Open **Defragment and Optimize Drives** from the Start menu.
2. Select your C: drive and click **Analyze**. Wait for the scan to complete.
3. Read the **Current status**: under 10% fragmented on an HDD is fine — leave it; over 10–15% is worth optimizing.
4. For SSDs the tool shows **OK** or a TRIM status rather than fragmentation — that is normal and needs no action beyond the scheduled optimization.

### Fix 3: Run the optimization

1. In **Defragment and Optimize Drives**, select the drive and click **Optimize**.
2. On an HDD, the status changes to show the defrag pass and consolidation percentage — let it run to completion.
3. On an SSD, the tool issues TRIM commands, which typically finish in under a minute.
4. Do not use the laptop heavily during an HDD defrag — competing disk activity slows the process and can leave the drive half-optimized.

### Fix 4: Verify and schedule automatic optimization

1. In the same tool, click **Change settings** under Scheduled optimization.
2. Check **Run on a schedule**, set frequency to **Weekly**, and click **Choose** to confirm all drives are included.
3. Make sure the task can wake or run when the laptop is idle — check the task in **Task Scheduler → Microsoft → Windows → Defrag**.
4. With the schedule active, you should never need to think about this again — weekly is the sweet spot the Windows team tuned for.

### Fix 5: Free space before defragging a packed drive

1. Defrag needs working room — aim for at least 15% free space on the drive.
2. Run Disk Cleanup (`cleanmgr` → **Clean up system files**) and uninstall large unused programs first.
3. Our [temporary files guide](/articles/how-to-clean-temporary-files-in-windows-11-24h2/) walks through reclaiming gigabytes before you optimize.
4. Re-run **Analyze** after freeing space — the fragmentation percentage often drops on its own once Windows has room to work.

### Fix 6: Handle SSDs correctly

1. Confirm the SSD shows **Solid state drive** in Optimize Drives and that scheduled optimization is on — that is all the maintenance an SSD needs.
2. Never install third-party defrag tools that do not distinguish drive types, and never force a "full defrag" on flash storage.
3. Check that TRIM is active: in an elevated Command Prompt, run `fsutil behavior query DisableDeleteNotify` — a result of `0` means TRIM is enabled.
4. If an SSD feels slow despite TRIM, the issue is elsewhere — firmware, nearly full drive, or a failing controller. SSD slowness is covered in our [disk active time diagnosis](/articles/how-to-fix-disk-active-time-100-percent-youtube/).

### Fix 7: Know when defrag will not help

1. If **Analyze** shows low fragmentation but the laptop is still slow, stop optimizing and investigate elsewhere — CPU, RAM, or background services.
2. Clicking, grinding, or buzzing from the drive means hardware trouble — back up immediately instead of defragging.
3. Run `chkdsk C: /scan` from an elevated Command Prompt to rule out file system corruption mimicking fragmentation symptoms.
4. Background on keeping the whole storage stack healthy is on the [Microsoft support site](https://support.microsoft.com/en-us/windows), which documents the Optimize Drives behavior per Windows version.

## Closing

Defragmentation is simple maintenance with one critical rule: defrag the HDDs, TRIM the SSDs, and let the weekly schedule handle both. Check fragmentation before you optimize, free space before you defrag, and never let an old habit wear out a modern drive.

If you manage more than one PC, it is worth checking the schedule on each of them once — family laptops and old desktops are where the automatic optimization quietly gets disabled and forgotten. A five-minute check per machine, once a year, keeps every drive in the house running the way its technology intended.
