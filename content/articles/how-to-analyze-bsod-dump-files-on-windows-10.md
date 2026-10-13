---
title: "How to Read BSOD Dump Files on Windows 10"
slug: how-to-analyze-bsod-dump-files-on-windows-10
date: 2026-09-23
categories: ["windows-errors"]
tags: ["bsod", "dump files", "windbg"]
description: "Stop guessing at blue screens: learn to open minidump files with WinDbg and BlueScreenView and identify the exact failing driver."
thumbnail: "/images/thumbs/how-to-analyze-bsod-dump-files-on-windows-10.webp"
faqs:
  - q: "What is a BSOD dump file?"
    a: "When Windows blue-screens, it writes a snapshot of memory at the moment of the crash — by default a 256KB minidump in C:\\Windows\\Minidump. It records the stop code, the faulting driver, and the call stack, which is everything needed to identify the cause instead of guessing."
  - q: "Do I need to be a programmer to read a dump?"
    a: "No. The !analyze -v command in WinDbg does the heavy lifting and prints a plain-English summary naming the suspect driver. BlueScreenView is even simpler — a table with the guilty driver highlighted. You need curiosity, not coding skills."
  - q: "What if there are no dump files after a crash?"
    a: "Dumps may be disabled, or the crash may occur too early (or the drive too damaged) for Windows to write one. Check Settings > System > About > Advanced system settings > Startup and Recovery > Settings and confirm a dump type is selected and the page file is on the system drive."
  - q: "Can one dump be misleading?"
    a: "Yes — a dump occasionally blames the victim driver rather than the culprit, especially with memory corruption. Collect three or more dumps: if they all name the same driver, it is guilty. If each names a different driver, suspect RAM instead."
---
Every blue screen writes down exactly what killed it — most people just never read the note. Windows 10 saves **minidump files** to `C:\Windows\Minidump` after each crash, and those small files contain the stop code, the faulting driver, and the chain of calls that led to the crash. Learning to read them turns blue-screen troubleshooting from guesswork into diagnosis.

This guide covers both tools worth knowing: **BlueScreenView** for quick answers and **WinDbg Preview** for definitive ones.

## Why this happens

Dumps go unread (or missing) for understandable reasons:

- **Nobody enables or checks them:** Dumps are on by default, but most users never look in the Minidump folder.
- **Automatic restart hides the evidence:** The default reboot wipes the blue screen before you can read the filename — the dump preserves it.
- **Cleaner tools delete dumps:** Disk cleaners and "optimizers" often wipe minidumps as "junk files."
- **Dumps disabled by tweaks:** Debloating scripts sometimes disable crash dumps to "save space."
- **Crashes too early or drive too damaged:** If Windows cannot write during the crash, no dump exists — itself a clue pointing at storage or very early boot failure.
- **Small SSDs with no page file:** Minidumps need a page file on the system drive; removing it disables dump writing.

## How to fix it

Work through these in order — setup first, then analysis technique.

### Fix 1: Make sure dumps are being saved

No dumps, no analysis. Verify the configuration.

1. Open **Settings > System > About > Advanced system settings**, and under **Startup and Recovery** click **Settings**.
2. Set **Write debugging information** to **Small memory dump (256 KB)** and note the dump location: `%SystemRoot%\Minidump`.
3. Uncheck **Automatically restart** so you can also read the blue screen directly.
4. Confirm the page file exists on the system drive: **Advanced system settings > Performance > Settings > Advanced > Virtual memory** — it should show a paging file on C:. No page file means no dumps.

### Fix 2: Get the quick answer with BlueScreenView

The fastest path from dump to suspect driver.

1. Download **BlueScreenView** (free, NirSoft) and run it — no installation needed. It automatically loads every dump in `C:\Windows\Minidump`.
2. The top pane lists crashes by date; the bottom pane shows the drivers involved, with the suspect highlighted in red.
3. Click each recent crash and note the **Bug Check String**, **Caused By Driver**, and the red-highlighted filename. If three crashes all highlight the same driver, you have your culprit — update, roll back, or remove it.
4. BlueScreenView's answer is right most of the time. When crashes blame different drivers each time, suspect RAM (see our [memory-management-bsod-windows-11-fix](/articles/memory-management-bsod-windows-11-fix/) guide) rather than chasing each driver.

### Fix 3: Install WinDbg Preview for definitive analysis

When BlueScreenView is inconclusive, Microsoft's own debugger settles it.

1. Install **WinDbg Preview** free from the Microsoft Store.
2. Open it, choose **File > Open dump file**, and navigate to `C:\Windows\Minidump` — open the most recent `.dmp`.
3. On first use, set the symbol path so WinDbg can resolve Windows internals: in the command box at the bottom, run `.sympath SRV*C:\Symbols*https://msdl.microsoft.com/download/symbols` then `.reload`.
4. Symbols download automatically on first analysis (needs internet) — subsequent analyses are fast.

### Fix 4: Run !analyze -v and read the summary

One command produces the verdict.

1. In WinDbg's command box, type `!analyze -v` and press **Enter**. Wait for the analysis to complete.
2. Read these fields:
   - **BUGCHECK_STR** / **BugCheck Code**: the stop code (e.g., `0xD1`).
   - **MODULE_NAME** and **IMAGE_NAME**: the driver WinDbg blames.
   - **PROCESS_NAME**: what was running when it crashed — patterns here reveal triggers (a game, a backup tool).
   - **STACK_TEXT**: the call chain; the frames just above the crash show what the guilty driver was doing.
3. The **DEFAULT_BUCKET_ID** line often summarizes the fault class (e.g., `DRIVER_IRQL_NOT_LESS_OR_EQUAL`).

### Fix 5: Interpret common results correctly

Knowing what the output means prevents misdiagnosis.

1. **A third-party .sys named consistently** across dumps: update or remove that driver. Done — this is the most common outcome.
2. **ntoskrnl.exe blamed**: almost never the real culprit; the kernel is where crashes land, not where they start. Look deeper at the stack or suspect RAM.
3. **Different driver every crash**: classic failing-RAM signature. Run `mdsched.exe` before touching any driver.
4. **No dump written at all**: points at storage failure or crashes during the earliest boot phase — check the drive with `chkdsk` and SMART data.

### Fix 6: Correlate with the system timeline

One dump is a data point; a pattern is a diagnosis.

1. Open **Reliability Monitor** (**Win + R** > `perfmon /rel`) alongside your dump dates — match crashes to software installs, updates, or new hardware.
2. Check **Event Viewer > Windows Logs > System** around each crash time for disk, driver, or service errors that precede the bug check.
3. If crashes cluster after a specific update, roll it back (**Settings > Update & Security > Windows Update > View update history > Uninstall updates**) and watch for a week.

### Fix 7: Act on the findings and verify

Analysis without action is trivia.

1. Guilty driver identified: get the correct version from the laptop manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) or the chip maker — never from a driver-updater utility.
2. RAM suspected: reseat or replace sticks, then retest for a week.
3. Keep collecting dumps after the fix. A week with no new minidumps in `C:\Windows\Minidump` is the objective confirmation that the problem is solved. For applying driver-level fixes, our [driver IRQL troubleshooting guide](/articles/driver-irql-not-less-or-equal-troubleshooting/) walks through verification with Driver Verifier.

## Closing

Reading a minidump takes five minutes and replaces hours of guessing: BlueScreenView for the quick answer, WinDbg's `!analyze -v` for the definitive one, and the discipline to collect several dumps before concluding. The blue screen already wrote down who did it — this is how you read the note.
