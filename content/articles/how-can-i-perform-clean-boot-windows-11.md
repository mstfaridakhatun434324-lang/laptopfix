---
title: "How to Perform a Clean Boot in Windows 11"
slug: how-can-i-perform-clean-boot-windows-11
date: 2026-09-07
categories: ["windows-errors"]
tags: ["clean boot", "windows 11", "startup troubleshooting", "msconfig"]
description: "Learn to perform a clean boot in Windows 11 — isolate the program or service causing crashes, errors, and slowdowns."
thumbnail: "/images/thumbs/how-can-i-perform-clean-boot-windows-11.webp"
faqs:
  - q: "What is a clean boot in Windows 11?"
    a: "A clean boot starts Windows with only Microsoft services and drivers, disabling all third-party startup programs and non-Microsoft services. It doesn't delete anything — it temporarily isolates third-party software so you can determine whether a problem is caused by Windows itself or by something installed on top of it."
  - q: "Is a clean boot the same as Safe Mode?"
    a: "No. Safe Mode loads a minimal set of Microsoft drivers with a basic display and no network (unless chosen), while a clean boot loads your normal drivers and full Windows functionality but disables third-party startup software. Clean boot is better for testing whether installed programs cause a problem; Safe Mode is better for deep system repair."
  - q: "Will a clean boot delete my programs or files?"
    a: "No. A clean boot only temporarily disables startup items and non-Microsoft services — nothing is uninstalled or deleted. When you re-enable everything afterward, the system returns to exactly how it was. It's one of the safest diagnostic procedures in Windows."
  - q: "How do I undo a clean boot and restore normal startup?"
    a: "Open msconfig, go to the Services tab, click Enable all, then go to the Startup tab, open Task Manager, and re-enable your startup apps. Restart. If you identified the culprit during testing, uninstall it instead of re-enabling it — that's the point of the exercise."
---

A **clean boot** is the most useful diagnostic technique most Windows users have never heard of. It starts Windows 11 normally — full drivers, full display, full functionality — but with all **third-party startup programs and non-Microsoft services disabled**. If your problem disappears in a clean boot, something you installed is causing it. If it persists, Windows itself (or hardware) is at fault. That single binary answer saves hours of guessing.

Technicians use clean boots to chase crashes, blue screens that only happen in normal mode, mysterious slowdowns, software conflicts, and errors that vanish in Safe Mode but return in normal use. It's completely reversible: nothing is uninstalled, nothing is deleted, and restoring normal startup takes two minutes. For the broader crash workflow this fits into, see our [blue screen troubleshooting guide](/articles/how-to-fix-blue-screen-of-death-windows-11/); for the loop variant, [automatic repair loop fixes](/articles/how-to-fix-automatic-repair-loop-windows-11-youtube/). When should you reach for a clean boot? Any time a problem appears in normal Windows but disappears in Safe Mode — that is the signature of third-party interference. It is also the right move for software that worked yesterday and broke today, for error messages that appear at every logon, and for performance problems with no obvious cause. Ten minutes of clean-boot testing often replaces hours of reinstalling programs at random.

## Why this happens

- **Conflicting third-party services**: Two programs fighting over the same system resources at startup.
- **Buggy startup programs**: A program that crashes or hangs every time Windows loads it.
- **Driver-adjacent software**: Utilities that install kernel helpers (RGB controllers, "boosters," overclock tools) destabilizing normal mode.
- **Antivirus conflicts**: Two security products — or one aggressive one — conflicting with Windows components.
- **Corrupt startup entries**: Damaged startup registrations causing errors on every boot.
- **Software that breaks after updates**: Programs incompatible with a new Windows build, failing at startup.
- **Resource exhaustion at logon**: Too many heavy startup programs overwhelming the system.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Open System Configuration (msconfig)

The control panel for the whole procedure.

1. Press **Win + R**, type `msconfig`, and press Enter.
2. The **System Configuration** window opens. You'll work on the **Services** tab first, then the **Startup** tab.
3. Don't change anything on the **General** or **Boot** tabs — the clean boot is done entirely through Services and Startup.
4. Keep this window open; you'll return here to restore normal startup later.

### Fix 2: Disable all non-Microsoft services

The critical step — and the one people get wrong by skipping the "hide" checkbox.

1. In **msconfig**, go to the **Services** tab.
2. **Tick "Hide all Microsoft services"** at the bottom-left. This is essential — disabling Microsoft services can make Windows unbootable.
3. With Microsoft services hidden, click **Disable all**. Every remaining (third-party) service is now unchecked.
4. Click **Apply** but don't restart yet — startup programs come next.

### Fix 3: Disable all startup programs

The second half of the clean boot.

1. In **msconfig**, go to the **Startup** tab and click **Open Task Manager**.
2. In Task Manager's **Startup apps** list, select each **Enabled** item, one at a time, and click **Disable**.
3. Close Task Manager and return to **msconfig**. Click **OK**.
4. When prompted, click **Restart**. Windows now boots clean — only Microsoft services and your normal drivers load.

### Fix 4: Test in the clean boot state

Now reproduce the problem — or enjoy its absence.

1. After restart, try to reproduce the original issue: run the crashing program, wait for the usual error, or test performance.
2. **Problem gone?** A disabled program or service was the cause. Continue to Fix 5 to identify it.
3. **Problem still present?** Third-party startup software is innocent — the cause is Windows itself, a driver, or hardware. Skip to Fix 6, then restore normal startup with Fix 7.
4. Note exactly what you tested and the result. Vague testing produces vague conclusions.

### Fix 5: Identify the culprit by halves

Binary search through the disabled items.

1. Reopen **msconfig** > **Services** tab (hide Microsoft services again) and re-enable the **top half** of the disabled services. Restart and test.
2. Problem returns = the culprit is in that half. Problem stays away = it's in the other half. Repeat, halving each time, until one service remains.
3. Do the same with **Startup apps** in Task Manager if services prove innocent.
4. Once identified, **uninstall** the offending program (**Settings** > **Apps** > **Installed apps**) rather than leaving it disabled — then re-enable everything else and restart. Keep notes as you go — with dozens of services, it is easy to lose track of which half you are testing.

### Fix 6: When the clean boot doesn't help

The problem is below the software layer you just eliminated.

1. Update drivers — especially the one related to your symptom (graphics for display issues, network for connectivity) — from the manufacturer's site.
2. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` in **Terminal (Admin)** to repair Windows components.
3. Check [Microsoft's support site](https://support.microsoft.com/en-us/windows) for known issues with your Windows build.
4. Consider hardware: run the Windows Memory Diagnostic (`mdsched.exe`) if crashes or corruption are involved.

### Fix 7: Restore normal startup

Don't leave the system in diagnostic state.

1. **Win + R** > `msconfig` > **Services** tab > click **Enable all** (keep "Hide all Microsoft services" ticked or untick it — Enable all restores everything).
2. **Startup** tab > **Open Task Manager** > re-enable the startup apps you want (leave the identified culprit disabled/uninstalled).
3. Click **OK** and **Restart**.
4. Verify normal operation. If you removed the culprit in Fix 5, the original problem should be gone in normal startup too.

## Closing

The clean boot is the closest thing Windows troubleshooting has to a scientific instrument: change one variable (third-party software on/off), observe, conclude. Learn this procedure once and you'll use it for years — on crashes, slowdowns, conflicts, and mysteries alike. Just remember the two rules: always hide Microsoft services before disabling, and always restore normal startup when you're done.
