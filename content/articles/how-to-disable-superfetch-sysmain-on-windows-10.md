---
title: "How to Disable Superfetch (SysMain) on Windows 10"
slug: how-to-disable-superfetch-sysmain-on-windows-10
date: 2026-09-27
categories: ["performance"]
tags: ["superfetch", "sysmain", "windows 10", "disk usage"]
description: "SysMain (Superfetch) causing 100% disk usage on Windows 10? Learn what it does, when disabling actually helps, and the three ways to turn it off safely."
thumbnail: "/images/thumbs/how-to-disable-superfetch-sysmain-on-windows-10.webp"
faqs:
  - q: "What is the difference between Superfetch and SysMain?"
    a: "They're the same service, renamed. Microsoft called it Superfetch from Vista through early Windows 10, then renamed it to SysMain in the Windows 10 1809 update — same job, new name. You'll still see 'Superfetch' in older guides and some registry keys, but on any current Windows 10 install the service is listed as SysMain. Disabling either name refers to the same action."
  - q: "Will disabling SysMain make my computer slower?"
    a: "On an SSD, you likely won't notice any difference — SSDs are fast enough that preloading apps into RAM provides minimal benefit, which is why many SSD guides recommend disabling it. On an old mechanical HDD, disabling SysMain can make frequently-used apps launch slightly slower, since the preloading genuinely helps spinning disks. If you disable it and app launches feel slower, just turn it back on."
  - q: "Is it safe to disable the SysMain service?"
    a: "Yes, completely safe. SysMain is a pure optimization service — Windows runs fine without it, just without the app-preloading behavior. Microsoft designed it to be stoppable, and disabling it doesn't affect stability, updates, or security. It's one of the few services that's genuinely safe to disable, unlike most entries in random 'services to disable' lists."
  - q: "Why does SysMain cause 100% disk usage?"
    a: "SysMain analyzes your usage patterns and preloads apps it predicts you'll open, which means heavy disk reads — on a slow mechanical HDD, this saturates the disk at 100% in Task Manager, especially after boot. The irony is it's trying to speed things up but the HDD can't keep up with both preloading and your actual work. This is the one scenario where disabling SysMain reliably fixes 100% disk usage."
---

If you've ever googled "100% disk usage Windows 10," you've seen the advice: disable Superfetch. The service is actually called **SysMain** now (renamed in 2018), but the advice persists because in one specific situation it's genuinely correct — a Windows 10 laptop with a mechanical hard drive where SysMain's preloading saturates the disk. On SSDs, though, disabling it is usually pointless. This guide covers what SysMain actually does, how to tell if it's your problem, and the three ways to disable it safely. For the broader 100% disk usage picture, see [Windows 11 high disk usage at startup](/articles/how-to-fix-windows-11-high-disk-usage-on-startup-on-lenovo-laptop/); for general speed, our [slow laptop guide](/articles/laptop-running-slow-windows-11-how-to-speed-up/) applies.

## Why this happens

- **Preloading on a slow HDD**: SysMain's predictive loading saturates mechanical disks, showing 100% disk usage.
- **Post-boot analysis spike**: After every boot, SysMain studies recent patterns — heavy for the first 10–20 minutes.
- **SysMain bugs in specific builds**: Certain Windows 10 builds had a SysMain memory/disk leak fixed by later updates.
- **Confusion with other 100% disk causes**: Antivirus scans, Windows Update, and the search indexer get blamed on SysMain.
- **Myth-driven disabling**: Most guides recommend it blindly; on SSDs it rarely matters either way.
- **Prefetch folder corruption**: Damaged prefetch data makes SysMain re-analyze constantly.
- **Low RAM amplifying the effect**: With 4GB RAM, SysMain's caching competes with actual app memory needs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm SysMain is actually the disk hog

Don't disable it on a hunch — verify first.

1. Open **Task Manager** > **Processes** tab, click the **Disk** column to sort, and look for **Service Host: SysMain** at the top during the 100% disk episodes.
2. Check the timing: SysMain spikes hardest in the first 10–20 minutes after boot, then should settle. Constant 100% disk all day is rarely SysMain alone.
3. Note your drive type in Task Manager > **Performance** tab: **HDD** = SysMain is a plausible culprit; **SSD** = look elsewhere first (antivirus, Windows Update, indexer).
4. Open **Resource Monitor** (`resmon`) > **Disk** tab and check which files SysMain (under svchost) is reading — prefetch-style reads of program files confirm it's preloading.
5. If the top disk consumer is actually `MsMpEng.exe`, `TiWorker.exe`, or `SearchIndexer.exe`, fix those instead — disabling SysMain won't help.

### Fix 2: Disable SysMain via Services (recommended method)

The clean, reversible way.

1. Press `Win + R`, type `services.msc`, and press Enter.
2. Scroll to **SysMain**, double-click it to open properties.
3. Click **Stop** to halt it immediately, then change **Startup type** to **Disabled**.
4. Click **OK** and reboot — the service stays off across restarts.
5. To re-enable later (if app launches feel slower on an HDD), just set Startup type back to **Automatic** and start it. Nothing is deleted; it's fully reversible.

### Fix 3: Disable SysMain via the Registry

For scripting, or when Services access is restricted.

1. Press `Win + R`, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SysMain`.
2. Double-click the **Start** value: `4` = disabled, `3` = manual, `2` = automatic. Set it to `4`.
3. Also check `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters` — **EnableSuperfetch** = `0` disables the prefetching behavior at the kernel level too.
4. Reboot for the change to take full effect.
5. Verify: in `services.msc`, SysMain should show **Disabled** and **Stopped**. Microsoft documents service behavior in the [Windows support hub](https://support.microsoft.com/en-us/windows) if you want official background.

### Fix 4: Disable SysMain via Command Prompt

The fastest method for a technician.

1. Open **Command Prompt as Administrator** (right-click Start > Command Prompt (Admin) or Windows PowerShell (Admin)).
2. Stop it now: `net.exe stop sysmain` (or `sc stop SysMain`).
3. Disable it permanently: `sc config SysMain start=disabled` — note the space after `start=`, which is required.
4. Confirm with `sc query SysMain` — STATE should eventually show STOPPED and the config disabled.
5. Re-enable anytime with `sc config SysMain start=auto` followed by `sc start SysMain`.

### Fix 5: Fix the underlying disk bottleneck instead

Disabling SysMain treats a symptom — consider the disease.

1. If you're on a mechanical HDD, the real fix is an **SSD upgrade** — a 2.5" SATA SSD transforms a Windows 10 laptop more than any tweak, and eliminates the entire 100% disk class of problems.
2. Check disk health: run `chkdsk C: /scan` and check S.M.A.R.T. data — a failing HDD shows 100% usage from read retries, which no service tweak fixes.
3. Make sure **Windows is fully updated** — the SysMain disk-leak bugs in early Windows 10 builds were fixed in later cumulative updates; check the [Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update is stuck.
4. Clear the prefetch folder if corrupted: delete contents of `C:\Windows\Prefetch` (not the folder itself) — Windows rebuilds it cleanly.
5. If RAM is 4GB, consider upgrading — with adequate RAM, SysMain's caching is harmless; with starved RAM, everything disk-related hurts.

### Fix 6: Verify the fix worked

Confirm the change did what you intended.

1. Reboot and open Task Manager > **Processes**, sorted by Disk — **Service Host: SysMain** should be absent from the list.
2. Monitor disk usage for a full boot cycle: 100% episodes in the first minutes after boot should be gone or greatly reduced (some boot disk activity is normal regardless).
3. Test your most-used apps' launch times over a few days — on an HDD, note whether launches got slower (if so, re-enable SysMain; the tradeoff wasn't worth it).
4. If 100% disk persists without SysMain, the cause was never SysMain — investigate antivirus scans, Windows Update (`TiWorker.exe`), or the search indexer next.
5. Document what you changed (a sticky note in the PC's records is enough) so future troubleshooting doesn't chase a ghost.

## Closing

SysMain/Superfetch is a legitimate optimization that only becomes a problem on slow mechanical drives — which is exactly where the "disable Superfetch" advice came from. Verify it's your actual disk hog, disable it cleanly via Services, and consider that an SSD upgrade makes the whole question moot. On SSDs, leave it alone; it wasn't hurting anything.
