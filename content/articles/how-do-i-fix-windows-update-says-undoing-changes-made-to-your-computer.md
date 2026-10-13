---
title: "How Do I Fix Windows Update Saying 'Undoing Changes Made to Your Computer'?"
slug: how-do-i-fix-windows-update-says-undoing-changes-made-to-your-computer
date: 2026-10-04
categories: ["windows-update"]
tags: ["undoing changes", "update rollback", "windows 11", "failed update", "update fix"]
description: "Stuck watching 'Undoing changes made to your computer'? A direct, step-by-step answer: what to do right now, how to recover, and how to make the retry succeed."
thumbnail: "/images/thumbs/how-do-i-fix-windows-update-says-undoing-changes-made-to-your-computer.webp"
faqs:
  - q: "What should I do first when I see 'Undoing changes'?"
    a: "Nothing — for at least two hours. Make sure the laptop is plugged in, then leave it alone. The rollback is Windows restoring your system to its pre-update state, and interrupting it is the main way a recoverable situation becomes an unbootable one. Patience is the entire first step."
  - q: "The screen has been stuck for hours. Can I turn off my laptop?"
    a: "If the spinner is frozen and there's been no disk activity for over an hour past the two-hour mark, yes — hold the power button for 10 seconds. Windows journals rollback progress and usually resumes on reboot. This is safe only after you've confirmed genuine inactivity, not just slowness."
  - q: "How do I stop the same update from failing again?"
    a: "Find the error code in Settings > Windows Update > Update history, then fix what it indicates: free disk space, clear the update cache, update your BIOS and drivers, or repair the component store with DISM. Pausing updates for two weeks while you fix the root cause prevents an immediate repeat failure."
  - q: "Do I need to reinstall Windows after a rollback?"
    a: "Almost never. A completed rollback returns your system to exactly its pre-update state — that's the whole point. Only consider an in-place upgrade or reset if rollbacks keep recurring after you've fixed drivers, firmware, disk space, and the component store."
---

Short answer: wait two hours with the laptop plugged in. If it finishes on its own — which it usually does — find out why the update failed and fix that before letting it retry. If it's genuinely frozen past that point, force a restart and let the rollback resume. That's the whole strategy; everything below is the detail that makes each step safe and effective.

The "Undoing changes made to your computer" screen means an update failed and Windows is reversing it. Your files are fine. Your system is returning to its pre-update state. The danger isn't the rollback — it's impatience: yanking the power or hammering the power button during an active rollback is the one thing that can corrupt the process. So here's the direct, no-fluff sequence for getting through it and making sure the next attempt works.

## Why this happens

- **The update failed its own safety checks**: Windows detected a problem mid-install and triggered the automatic reversal.
- **A driver refused to migrate**: The new build couldn't bring a device driver along, failing the installation.
- **The download was corrupt**: Damaged update files failed verification during install.
- **Disk space ran out mid-install**: Staging needs room; without it, the install aborts and reverses.
- **Security software blocked system file changes**: Third-party antivirus guarding files the update needed to replace.
- **Firmware too old for the new build**: Outdated BIOS/UEFI conflicting with update expectations.
- **The component store was already broken**: Pre-existing corruption the update couldn't build on.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait the full two hours, plugged in

This is the fix for most people, because most rollbacks complete on their own. The only requirement is not interfering.

1. Plug the laptop into AC power immediately — do not let the battery die mid-rollback.
2. Note the time. Commit to **2 full hours** without touching anything.
3. Signs it's working: the spinner animates, you hear drive activity, the fan cycles.
4. Signs it's stuck: spinner frozen solid, total silence from the drive for 60+ minutes.
5. If it finishes, you get the login screen — go to Fix 2.
6. If your deadline passes with zero activity, skip to Fix 4.

### Fix 2: Find the failure's error code

Knowledge first. The code tells you exactly which of the remaining fixes to prioritize.

1. After the rollback completes, open **Settings > Windows Update > Update history**.
2. Locate the failed update and its error code.
3. **0x80070002 / 0x80070003** → corrupt cache (Fix 3). **0xC1900101** → driver conflict (see our [0xC1900101 deep-dive](/articles/how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update/)). **0x800F0922** → often .NET or partition space. **0x80070070** → disk space.
4. Note the KB number as well.
5. If no code is shown, the generic fixes (3, 5, 6) cover the most common causes.

### Fix 3: Clear space and purge the corrupt download

The two quickest wins. Do both even if space looks okay — the cache purge is harmless.

1. Open **Settings > System > Storage** — confirm at least 15–20 GB free on C:.
2. Use **Temporary files** cleanup to remove Windows Update Cleanup and Delivery Optimization files.
3. Open **Command Prompt as administrator**:
   - `net stop wuauserv`
   - `net stop bits`
   - Delete everything in `C:\Windows\SoftwareDistribution\Download`
   - `net start wuauserv`
   - `net start bits`
4. Don't retry the update yet — work through Fix 5 and 6 first so the retry has the best chance.

### Fix 4: Force-restart a truly frozen rollback

Only for confirmed-frozen rollbacks: spinner dead, no disk sound, past your two-hour deadline.

1. Hold **power** for 10 seconds until fully off.
2. Disconnect all USB devices and docks.
3. Wait 30 seconds, power on.
4. In most cases you'll see "Undoing changes" resume and finish within 30 minutes.
5. If it boots to desktop, continue to Fix 5.
6. If it returns to the frozen screen, force off again, then interrupt boot three times to reach **Automatic Repair > Troubleshoot > Advanced options > Startup Repair**.

### Fix 5: Update BIOS and drivers before the retry

Outdated firmware and drivers cause the majority of repeat rollbacks. Fix them while updates are paused.

1. In **Settings > Windows Update**, **pause updates** for 2 weeks to stop the doomed retry loop.
2. Visit your manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — and install the latest **BIOS/UEFI** and **chipset** drivers for your exact model.
3. Update graphics drivers from the GPU maker's official site (Intel, NVIDIA, or AMD) as appropriate.
4. Our [driver update guide](/articles/how-to-update-drivers-on-windows-11-laptop/) walks through doing this systematically.
5. Only unpause Windows Update after firmware and drivers are current.

### Fix 6: Repair the component store with DISM

If the update failed because the system it was building on was damaged, DISM rebuilds the foundation.

1. Open **Command Prompt as administrator**.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait (15–30 min).
3. Run `sfc /scannow` afterward.
4. Restart the laptop.
5. Check the drive too: `chkdsk C: /f` — bad sectors cause exactly these mid-install failures.
6. Now unpause updates and retry. If it rolls back again, note whether it's the same KB — a pattern points to that specific package, which you can hide with Microsoft's "Show or hide updates" tool.

### Fix 7: Do a clean-boot retry for stubborn cases

When everything checks out but the update still rolls back, something loading at startup is interfering. A clean boot removes all suspects at once.

1. Press Win + R, type `msconfig`, go to the **Services** tab.
2. Check **Hide all Microsoft services**, click **Disable all**.
3. In Task Manager's **Startup** tab, disable everything.
4. Restart, temporarily disable third-party antivirus, and run Windows Update.
5. After a successful install, re-enable everything in msconfig.
6. If it still fails after all seven fixes, an in-place upgrade (Windows 11 ISO > setup.exe > Keep files and apps) gives you a fresh system without data loss — details in our [troubleshooting walkthrough](/articles/troubleshoot-windows-update-says-undoing-changes-made-to-your-computer/).

## Closing

You fix "Undoing changes" by respecting what it is: a safety net, not the problem. Wait it out, read the error code it leaves behind, fix the underlying cause — space, cache, drivers, firmware, or component store — and the retry succeeds. Do the diagnosis once, properly, and you won't be watching that screen again next month.
