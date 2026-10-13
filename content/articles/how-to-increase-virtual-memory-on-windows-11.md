---
title: "How to Increase Virtual Memory on Windows 11 (Correctly)"
slug: how-to-increase-virtual-memory-on-windows-11
date: 2026-09-04
categories: ["performance"]
tags: ["virtual memory", "pagefile", "ram", "windows 11", "paging file"]
description: "Increase virtual memory (pagefile) on Windows 11 the right way: when it helps, what size to set, and when more RAM is the real answer."
thumbnail: "/images/thumbs/how-to-increase-virtual-memory-on-windows-11.webp"
faqs:
  - q: "What is virtual memory and how does the pagefile work?"
    a: "Virtual memory is disk space Windows uses as an overflow area when RAM fills up — the pagefile (pagefile.sys) holds memory pages moved off RAM. It prevents 'out of memory' crashes when demand exceeds physical RAM. But it's far slower than RAM: paging to an SSD is tolerable, paging to a spinning hard drive causes the infamous constant-disk-thrashing slowness."
  - q: "What size should I set the pagefile to?"
    a: "For most systems, leave it system-managed — Windows sizes it dynamically and correctly. If you must set it manually, the old rule of 1.5x RAM is outdated; a reasonable manual setting is a fixed size with minimum equal to RAM and maximum 2–3x RAM on SSDs. Never disable the pagefile entirely — some programs and crash dumps require it regardless of how much RAM you have."
  - q: "Will increasing virtual memory make my laptop faster?"
    a: "Only if the current pagefile is the bottleneck — i.e., you're getting out-of-memory errors or the pagefile is on a nearly-full drive. Increasing it doesn't speed anything up; it just raises the ceiling before crashes. If the system is constantly paging (high disk usage, stuttering), the real fix is more RAM or fewer apps, not a bigger pagefile."
  - q: "Should the pagefile be on my SSD or HDD?"
    a: "Always the fastest drive — your SSD. Pagefile speed directly affects how painful paging is, and SSDs handle the random I/O of paging orders of magnitude better than HDDs. If Windows is on an SSD but the pagefile got moved to an HDD (some old guides recommended this to 'save' the SSD), move it back — modern SSD endurance makes that advice obsolete."
---

"Increase your virtual memory" is one of the oldest pieces of Windows advice — and one of the most misunderstood. Done right, adjusting the pagefile prevents out-of-memory crashes and smooths over RAM shortages. Done wrong (or for the wrong reasons), it changes nothing while giving false confidence. This guide covers when increasing virtual memory actually helps, the correct way to set it, and — just as important — when the honest answer is "buy more RAM."

First, the mental model: virtual memory doesn't make anything faster. RAM is the workspace; the pagefile is the overflow parking lot across town. A bigger parking lot means fewer "lot full" crashes, but nobody drives faster because the lot got bigger. Related: [fixing Windows 11 using too much RAM at idle](/articles/how-to-fix-windows-11-using-too-much-ram-idle-on-acer-laptop/) and [taming Chrome's RAM usage](/articles/how-to-fix-chrome-using-too-much-ram-laptop/).

## Why this happens

- **RAM exhaustion**: Demand exceeds physical RAM, forcing heavy paging — the actual problem a bigger pagefile papers over.
- **Pagefile on a nearly-full drive**: Windows can't grow a system-managed pagefile when the disk is full, causing instability.
- **Pagefile manually set too small**: Old "optimization" guides that shrunk or disabled it, now causing crashes.
- **Pagefile on a slow HDD**: Paging to spinning rust makes every page fault agonizingly slow.
- **Memory leaks in apps**: Buggy programs growing unboundedly until they consume RAM plus pagefile.
- **Crash dumps need pagefile space**: Certain dump types require a pagefile at least the size of RAM.
- **Split pagefiles across drives**: Fragmented configurations from years of tweaks causing inconsistent behavior.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether you actually need more virtual memory

Don't change what isn't broken.

1. Open Task Manager (**Ctrl+Shift+Esc**) > **Performance** > **Memory** and look at **Committed** — if the committed number regularly approaches the **Commit limit** (RAM + pagefile), you're genuinely running out of virtual memory.
2. Check **Event Viewer** > **Windows Logs** > **System** for event ID 2004 ("resource exhaustion") — Windows logs these when virtual memory runs low. No events means no problem.
3. If you're seeing "out of memory" errors from specific apps, note which ones — a single leaky app is better fixed by updating it than by growing the pagefile for everything.
4. Check current pagefile settings first: `sysdm.cpl` > **Advanced** > **Performance Settings** > **Advanced** > **Virtual memory** > **Change** — note whether it's system-managed and its current size.
5. Decision rule: out-of-memory errors or commit limit pressure → adjust the pagefile. Mere slowness with high RAM usage → you need more RAM or fewer apps, not a bigger pagefile.

### Fix 2: Let Windows manage it (the default, and usually right)

Undo bad manual tweaks.

1. Open `sysdm.cpl` > **Advanced** tab > **Performance** > **Settings** > **Advanced** tab > **Virtual memory** > **Change**.
2. Check **Automatically manage paging file size for all drives** — this is the correct setting for 95% of systems.
3. If it was already checked and you're having problems, the pagefile isn't your issue — look at RAM pressure and disk space instead.
4. Click **Set**, then **OK**, and restart — Windows will size the pagefile dynamically from here on.
5. Verify afterward with `wmic pagefile list /format:list` in Command Prompt — confirm the allocated size looks sane (typically 1–4 GB minimum growing as needed on modern systems).

### Fix 3: Set a manual pagefile size (when you have a reason)

For the cases where manual control is justified.

1. Valid reasons: pagefile on a full drive that can't grow, specific software (video editing, VMs) recommending a fixed size, or needing a full memory dump for debugging.
2. In the Virtual Memory dialog, uncheck automatic management, select the **C:** drive (your fastest SSD), choose **Custom size**.
3. Set **Initial size** to roughly your RAM size in MB (e.g., 16384 for 16 GB) and **Maximum size** to 2–3x RAM — then click **Set** (clicking Set is mandatory; OK alone discards the change).
4. If you have a second fast SSD with plenty of space, you can additionally place a pagefile there — but one well-sized pagefile on the fastest drive beats split configurations.
5. Restart and verify the new size took effect. Never set the pagefile to zero/"No paging file" — Windows components and many applications assume it exists.

### Fix 4: Move the pagefile to the fastest drive

Location matters more than size.

1. In the Virtual Memory dialog, if the pagefile is currently on an HDD (or a nearly-full SSD), select that drive, choose **No paging file**, and click **Set**.
2. Select your fastest SSD (ideally the system drive), choose **System managed size** or your custom size, and click **Set**.
3. Restart — Windows needs the reboot to relocate pagefile.sys.
4. Confirm the old pagefile.sys is gone from the old drive and the new one exists on the SSD (it's hidden — enable hidden files to check).
5. If C: is critically full, free space first — a pagefile that can't grow is worse than useless; see our disk-space guides for reclaiming gigabytes.

### Fix 5: Reduce the demand instead of growing the supply

The fix most people actually need.

1. In Task Manager's **Processes** tab sorted by **Memory**, identify the biggest consumers — browsers with many tabs, Electron apps (Teams, Slack, Discord, Spotify), and VMs are the usual giants.
2. Close what you don't need; for browsers, use tab suspension extensions or the browser's built-in memory saver.
3. Check **Startup apps** and disable memory-heavy auto-launchers — every resident app permanently occupies RAM.
4. Look for memory leaks: a process whose memory grows unboundedly over hours (check Task Manager's **Memory** column periodically) should be updated or replaced.
5. This is the honest math: if committed memory constantly exceeds physical RAM by gigabytes, no pagefile setting fixes the thrashing — only more RAM or fewer concurrent apps does.

### Fix 6: Handle the special cases

Dumps, VMs, and old advice.

1. **Crash dumps**: **Settings** > **System** > **About** > **Advanced system settings** > **Startup and Recovery** — a **Complete memory dump** needs a pagefile ≥ RAM + 1 MB on the system drive. For most users, **Automatic memory dump** with a system-managed pagefile is correct.
2. **Virtual machines**: allocate VM RAM conservatively — overcommitting host RAM forces the host to page, and a VM's "RAM" paging to the host's pagefile is brutally slow.
3. **"Disable the pagefile with lots of RAM" myth**: don't. Some applications explicitly allocate against the pagefile, and crash diagnostics need it. With 32 GB RAM and an SSD, the pagefile costs you almost nothing — leave it system-managed.
4. **SSD wear worries**: modern SSDs handle pagefile writes for many years; the endurance concern is a decade out of date. Performance beats hypothetical wear.
5. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) confirm the guidance: system-managed on the fastest drive is the recommended configuration.

## Closing

Virtual memory is a safety net, not a speed booster. Check whether you're actually hitting the commit limit, restore system-managed sizing if some old guide broke it, put the pagefile on your fastest SSD, and — when the numbers show constant thrashing — accept the real verdict: the workload needs more RAM. A correctly configured pagefile is invisible. That's the goal: set it right once, then never think about it again.
