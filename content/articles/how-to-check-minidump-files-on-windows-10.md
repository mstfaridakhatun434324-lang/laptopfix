---
title: "How to Check Minidump Files on Windows 10"
slug: how-to-check-minidump-files-on-windows-10
date: 2026-10-11
categories: ["windows-errors"]
tags: ["minidump", "bsod", "windows-10"]
description: "Learn to read Windows 10 minidump files and identify exactly which driver is causing your blue screens."
thumbnail: "/images/thumbs/how-to-check-minidump-files-on-windows-10.webp"
faqs:
  - q: "What is a minidump file?"
    a: "A minidump is a small snapshot Windows saves automatically when it blue-screens — about 256 KB containing the stop code, the faulting driver, and the state of the crashed thread. It's enough to identify the culprit in most cases without the multi-gigabyte full memory dump."
  - q: "Where are minidump files stored?"
    a: "In C:\\Windows\\Minidump, named by date (like 101326-12345-01.dmp). They're only created if dumps are enabled in Startup and Recovery settings and the page file is on the system drive."
  - q: "Do I need WinDbg to read a minidump?"
    a: "Not necessarily. Free tools like BlueScreenView read minidumps in a simple table showing the stop code and likely driver. WinDbg gives deeper analysis but has a learning curve — start simple and go deeper only if needed."
  - q: "My Minidump folder is empty. Why?"
    a: "Dumps are probably disabled, the page file was moved off C:, or the crash happened too early in boot for the disk to be writable. Also, some 'cleaner' tools delete .dmp files — check their settings."
---
# How to Check Minidump Files on Windows 10

Every blue screen leaves a clue behind: a **minidump file** recording the stop code, the faulting driver, and what the system was doing when it crashed. Learning to read these files turns blue-screen troubleshooting from guesswork into detective work — instead of updating drivers at random, you update the one the dump names.

This guide covers the full workflow: making sure dumps are enabled, reading them with a simple free tool, and going deeper with WinDbg when needed. Once you can name the crashing driver, fixing the crash is usually straightforward — start with our [blue screen of death guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) for the fix side.

## Why this happens

Here's why minidump analysis is worth learning — and why dumps sometimes go missing when you need them:

- **The exact stop code:** No more squinting at a flashing blue screen.
- **The faulting driver:** The `.sys` file active when the crash happened — your prime suspect.
- **The crash pattern:** The same driver across multiple dumps means certainty; different drivers each time suggests hardware (usually RAM).
- **Timestamps:** Correlating crashes with driver installs or updates.
- **Stack traces:** For advanced users, the exact call path that failed.
- **What they can't tell you:** Dumps identify software suspects brilliantly but can't directly prove a hardware fault — patterns across dumps do that.

## How to fix it

Work through these in order: enable dumps, locate them, read them, interpret the pattern, then act.

### Fix 1: Make sure minidumps are enabled

No dumps, no detective work. Verify the settings first.

1. Press **Win + R**, type `sysdm.cpl`, and press **Enter**.
2. Go to the **Advanced** tab and click **Settings** under **Startup and Recovery**.
3. Under **Write debugging information**, select **Small memory dump (256 KB)**.
4. Confirm the dump path is `%SystemRoot%\Minidump` and that **Automatically restart** is ticked (or untick it if you want to read the stop code on screen — see our guide to [disabling automatic restart after a BSOD](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/)).
5. Click **OK**. Also verify your page file is on C: (**Advanced > Performance > Settings > Advanced > Virtual memory**) — dumps can't be written without one.

### Fix 2: Find your minidump files

After the next blue screen, collect the evidence.

1. Open File Explorer and navigate to `C:\Windows\Minidump`.
2. Files are named by date: `101326-12345-01.dmp` means October 13, 2026.
3. Copy any recent dumps to your Desktop or Documents — analyzing copies avoids permission hassles with the system folder.
4. If the folder is empty after a crash, recheck Fix 1's settings and make sure no "cleaner" app is deleting `.dmp` files on a schedule.

### Fix 3: Read dumps with BlueScreenView (easy method)

The fastest way to get answers — a free tool with no learning curve.

1. Download **BlueScreenView** from NirSoft's official site (it's portable — no install needed).
2. Run it as administrator so it can read the Minidump folder directly.
3. The top pane lists every crash with its stop code (e.g., `IRQL_NOT_LESS_OR_EQUAL`) and timestamp.
4. Click a crash: the bottom pane highlights the drivers in the stack, with the faulting one usually in pink.
5. Note the driver filename — `nvlddmkm.sys` means NVIDIA graphics, `Netwtw10.sys` means Intel Wi-Fi, and so on. That filename is your next search term for the fix.

### Fix 4: Analyze with WinDbg (thorough method)

When BlueScreenView isn't conclusive, Microsoft's own debugger goes deeper.

1. Install **WinDbg** from the Microsoft Store (the modern "WinDbg Preview" version).
2. Open it and go to **File > Open dump file**, selecting your copied `.dmp`.
3. In the command box at the bottom, type `!analyze -v` and press **Enter**.
4. Wait for the analysis — it downloads symbols from Microsoft automatically on first use.
5. Read the output: **BugCheck Code**, **Probably caused by**, and the **STACK_TEXT** section. "Probably caused by" is right most of the time but verify against the stack — the real culprit is sometimes the driver that called the crashed one, not the one holding the blame.
6. Use the **lmvm <drivername>** command (for example `lmvm nvlddmkm`) to see the driver's version and timestamp — an old timestamp confirms you're looking at an outdated driver worth updating.
6. Microsoft documents WinDbg commands fully on the [Windows support hub](https://support.microsoft.com/en-us/windows) and in the debugger documentation.

### Fix 5: Interpret the patterns

One dump is a hint; several dumps are a diagnosis.

1. **Same driver every time:** Update, roll back, or remove that driver — you've found it.
2. **Different drivers every time:** Suspect hardware, usually RAM — run the Windows Memory Diagnostic (`mdsched.exe`).
3. **`ntoskrnl.exe` blamed:** The kernel itself rarely crashes alone; it's usually covering for a driver or hardware fault. Look deeper at the stack, don't "update the kernel."
4. **Crashes only under load:** Points to heat, power, or marginal hardware rather than a pure driver bug.
5. **No dump created despite crashes:** Hardware failing too early/low for the disk write — check RAM and drive health directly.

### Fix 6: Act on what you found

Reading the dump is half the job — now fix the named culprit.

1. Search for the driver filename plus your stop code to find known issues and fixed versions.
2. Update the driver from the hardware or laptop maker's site — never from generic driver-updater tools.
3. If the driver is current and still crashing, roll it back or remove the associated software.
4. For antivirus filter drivers implicated in dumps, use the vendor's removal tool and test with Windows Security alone.
5. After fixing, keep the dumps for a week — if crashes return, compare new dumps to confirm it's the same cause and not a new one.

## Closing

Minidumps turn blue screens from mysteries into named suspects. Enable them, read them with BlueScreenView for the quick answer or WinDbg for the deep one, and look for patterns across multiple crashes. Five minutes of dump analysis routinely saves hours of blind driver updating — it's the closest thing to a cheat code in Windows troubleshooting, and it works on every blue screen you'll ever see.
