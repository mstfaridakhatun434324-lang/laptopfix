---
title: "How to Analyze BSOD Dump Files on Windows 11"
slug: how-to-analyze-bsod-dump-files-on-windows-11
date: 2026-09-26
categories: ["windows-errors"]
tags: ["BSOD analysis", "crash dumps", "Windows 11"]
description: "Learn to analyze BSOD dump files on Windows 11: find minidumps, read stop codes with Event Viewer and WinDbg, and identify the driver behind every crash."
thumbnail: "/images/thumbs/how-to-analyze-bsod-dump-files-on-windows-11.webp"
faqs:
  - q: "What is the difference between a minidump and a full memory dump?"
    a: "A minidump is a small 256 KB file containing the stop code, loaded driver list, and the crashed thread's stack — enough to identify the culprit in most cases. A full memory dump copies your entire RAM to disk, which can be tens of gigabytes, and is only useful for deep driver-developer debugging. For laptop troubleshooting, minidumps are all you need."
  - q: "Can I analyze a dump file without installing WinDbg?"
    a: "Partially. Event Viewer shows the stop code and sometimes the faulting module for each crash, and tools like the built-in Reliability Monitor chart crash history. But only a debugger like WinDbg can walk the crashed stack and name the exact driver. For one-off crashes Event Viewer is enough; for recurring crashes, install WinDbg."
  - q: "Why does my Minidump folder not have any files after a crash?"
    a: "Three common reasons: dump writing is set to None in Startup and Recovery settings, the disk was too full to write the file, or a very early boot crash happened before the dump driver loaded. Set the dump type to Small memory dump in sysdm.cpl, free up disk space, and check again after the next crash."
  - q: "How do I read a dump from a crash that happened last week?"
    a: "Windows keeps one minidump per crash in C:\\Windows\\Minidump, named by date, so last week's file is still there unless cleanup tools deleted it. Open the dated .dmp file in WinDbg, configure symbols once, and run !analyze -v. Old dumps analyze exactly like fresh ones as long as symbols are available."
---

Every blue screen leaves evidence. Windows writes a dump file at the moment of the crash — a snapshot of the stop code, the running drivers, and the exact instruction that failed. Most people ignore these files and reinstall drivers at random. You are going to do better: this guide teaches you to read them like a technician.

You don't need a computer science degree for this. With Event Viewer for the quick read and WinDbg for the deep read, you can name the crashing driver in minutes. Our hands-on companion piece on [how to read dump files with WinDbg on your laptop](/articles/how-to-read-dump-files-with-windbg-on-laptop/) goes step-by-step through the debugger itself if you want the full walkthrough.

## Why this happens

- Windows writes dumps automatically, but most users never learn where they live or how to open them.
- The stop code on the blue screen disappears in seconds, while the dump file preserves it permanently.
- Guessing at drivers wastes hours; a five-minute dump read names the suspect directly.
- Minidumps are tiny (256 KB) yet contain the crashed thread's full call stack.
- Without symbols configured, WinDbg shows addresses instead of names, which confuses beginners.
- Some crashes overwrite or fail to write dumps, which itself is a diagnostic clue about storage or early-boot failures.
- Disk-cleanup tools and aggressive "PC cleaner" apps sometimes delete the Minidump folder, erasing the evidence you need.

## How to fix it

Work through these in order — start with the quick Event Viewer read, then move to WinDbg for the full analysis.

### Fix 1: Confirm dumps are being saved

You can't analyze what was never written, so verify the dump settings before anything else.

1. Press **Win + R**, type `sysdm.cpl`, and press Enter.
2. On the **Advanced** tab, click **Settings** under **Startup and Recovery**.
3. Set **Write debugging information** to **Small memory dump (256 KB)**.
4. Note the small dump directory: `%SystemRoot%\Minidump`.
5. Uncheck **Automatically restart** too, so you can read the stop code on screen next time.

### Fix 2: Get the quick story from Event Viewer

Event Viewer logs every crash with its stop code — often enough to point you at the right fix without a debugger.

1. Press **Win + X** and choose **Event Viewer**.
2. Navigate to **Windows Logs > System**.
3. Click **Filter Current Log** and check **Critical** and **Error**, then click OK.
4. Look for **BugCheck** events (source: BugCheck) around the crash time.
5. Open the event: the **Details** tab lists the stop code (e.g. `0x0000007e`) and sometimes the faulting file.

### Fix 3: Check Reliability Monitor for the pattern

Reliability Monitor turns your crash history into a timeline, which reveals whether crashes cluster around updates or installs.

1. Press **Win + R**, type `perfmon /rel`, and press Enter.
2. Scan the timeline for red X marks on crash days and click one.
3. Read the **Technical details** — it lists the stop code and occasionally the module.
4. Note any software installs or updates immediately before crashes began.
5. This pattern view pairs well with guides like [troubleshoot blue screen after Windows 11 update](/articles/troubleshoot-blue-screen-after-windows-11-update/) when updates are implicated.

### Fix 4: Open the minidump in WinDbg

Now for the definitive read: open the actual dump file in Microsoft's debugger.

1. Install **WinDbg Preview** from the Microsoft Store if you haven't already.
2. In WinDbg, go to **File > Open dump file** and browse to `C:\Windows\Minidump`.
3. Select the newest `.dmp` file and wait for it to load.
4. If Windows warns about permissions, copy the `.dmp` to your Desktop first and open the copy.
5. The initial output already shows the bug check code at the top.

### Fix 5: Set symbols and run !analyze -v

Symbols turn raw addresses into names. Configure them once and every future analysis is automatic.

1. In WinDbg, open **File > Settings** and set the **Default symbol path** to `SRV*C:\Symbols*https://msdl.microsoft.com/download/symbols`.
2. In the command box at the bottom, type `!analyze -v` and press Enter.
3. Wait for symbol downloads to finish (first run is slow; later runs are fast).
4. Read **BUGCHECK_STR**, **MODULE_NAME**, and **IMAGE_NAME** for the verdict.
5. The **STACK_TEXT** section shows the chain of calls that led to the crash.

### Fix 6: Identify the real driver behind generic blame

Sometimes the analysis blames `ntoskrnl.exe` — that's the kernel reporting the crash, not causing it.

1. Scroll through **STACK_TEXT** for third-party `.sys` files below the kernel frames.
2. Run `lmvm <drivername>` (without `.sys`) on any suspicious third-party driver.
3. Check the **Timestamp** and **Company** lines to identify the vendor and age.
4. Search the vendor's site for an updated driver, or check [Microsoft's update catalog](https://www.catalog.update.microsoft.com/) for newer versions.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents what common stop codes mean once you have the code.

### Fix 7: Correlate and act

One dump is a data point; several dumps are a diagnosis. Compare before you change anything.

1. Analyze two or three recent dumps and compare the **IMAGE_NAME** results.
2. If all dumps blame the same driver, update, roll back, or remove that driver.
3. If each dump blames something different, suspect RAM or storage hardware instead of drivers.
4. After fixing, monitor **Reliability Monitor** for a week to confirm stability.
5. Keep old dumps archived — if crashes return, comparing old and new analyses shows whether it's the same fault.

## Closing

Dump analysis is the closest thing to a crystal ball in Windows troubleshooting. Event Viewer gives you the stop code in thirty seconds; WinDbg with symbols gives you the exact driver in five minutes. Once you've read your first dump end to end, you'll never go back to guessing — and recurring blue screens become a solvable puzzle instead of a recurring nightmare. Pair this skill with a solid [system restore routine](/articles/best-way-to-use-system-restore-on-windows-11/) and few crashes will ever cost you more than an afternoon.
