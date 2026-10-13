---
title: "How to Check Minidump Files on Windows 11 (Read Blue Screen Dumps)"
slug: how-to-check-minidump-files-on-windows-11
date: 2026-09-26
categories: ["windows-errors"]
tags: ["minidump", "blue screen analysis", "WinDbg"]
description: "Minidump files record exactly what crashed your PC. Learn to read them with WinDbg and BlueScreenView to identify the faulty driver."
thumbnail: "/images/thumbs/how-to-check-minidump-files-on-windows-11.webp"
faqs:
  - q: "Where are minidump files stored on Windows 11?"
    a: "Minidumps live in C:\\Windows\\Minidump as .dmp files, one per crash, typically 256 KB to a few MB each. A full memory dump, if enabled, is stored as C:\\Windows\\MEMORY.DMP. If the Minidump folder is empty after crashes, check Settings > System > About > Advanced system settings > Startup and Recovery settings — the write-debugging-information option may be set to None, or a cleaner may be deleting the dumps."
  - q: "What's the easiest tool to read minidump files?"
    a: "BlueScreenView by NirSoft is the easiest: it lists every crash with the stop code and highlights the driver files involved in the stack, no commands needed. For deeper analysis, WinDbg Preview from the Microsoft Store runs the !analyze -v command that identifies the faulting module with high accuracy. Start with BlueScreenView; move to WinDbg when you need certainty."
  - q: "Can a minidump tell me which driver caused the blue screen?"
    a: "Usually, yes. The dump captures the faulting module name, the stop code, and the call stack at the moment of the crash. In roughly 80 percent of driver-caused crashes, !analyze -v in WinDbg or the highlighted drivers in BlueScreenView point directly at the culprit file, which you can then update, roll back, or remove."
  - q: "Why are there no minidump files after my blue screens?"
    a: "Three common reasons: the dump setting is disabled (set to None in Startup and Recovery), the pagefile is too small or on a different drive than Windows (dumps are written via the pagefile), or the crash happens so early in boot that the dump stack is not ready. Also check that disk-cleaning tools are not wiping the Minidump folder automatically."
---

Every blue screen leaves a witness: the minidump file. It is a small snapshot of what Windows was doing at the exact moment of the crash — the stop code, the faulting driver, the call stack. Learning to read it turns blue-screen troubleshooting from guesswork into diagnosis. Instead of updating drivers at random, you update the *right* driver.

There are two tools worth knowing: BlueScreenView for quick answers, and WinDbg for definitive ones. This guide covers both, plus how to make sure dumps are actually being created — because the most common minidump problem is that there are no minidumps.

## Why this happens (no dumps, or unreadable ones)

- **Dump writing disabled.** Startup and Recovery set to "(none)" — common after some "privacy" tweaks.
- **Pagefile too small or misplaced.** Dumps are staged through the pagefile on the system drive.
- **Crash too early in boot.** The dump stack is not initialized during very early startup crashes.
- **Cleaner tools deleting dumps.** Privacy utilities wiping `C:\Windows\Minidump` on schedule.
- **Failing storage.** The dump cannot be written if the drive dies mid-crash.
- **Automatic restart hiding the evidence.** The PC reboots before you note the stop code (the dump still exists, though).

## How to fix it (and read the dumps)

Work through these in order.

### Fix 1: Verify minidumps are being created

Make sure Windows is actually writing dumps.

1. Go to **Settings > System > About**, click **Advanced system settings**.
2. Under **Startup and Recovery**, click **Settings**.
3. Set **Write debugging information** to **Small memory dump (256 KB)** and note the dump file path (`%SystemRoot%\Minidump`).
4. Uncheck **Automatically restart** so you can read the stop code on the blue screen itself.
5. Ensure the pagefile is system-managed: **Advanced system settings > Performance Settings > Advanced > Virtual memory** should show **Automatically manage paging file size**.
6. Click OK, and check `C:\Windows\Minidump` after the next crash.

### Fix 2: Read dumps the easy way with BlueScreenView

Quick answers with no commands.

1. Download **BlueScreenView** from NirSoft's official site (it is a standalone .exe, no install needed).
2. Run it — it automatically loads every dump from `C:\Windows\Minidump`.
3. The top pane lists crashes by date with the **Bug Check String** (e.g. DRIVER_IRQL_NOT_LESS_OR_EQUAL) and **Bug Check Code**.
4. Click a crash; the bottom pane shows the stack with involved drivers highlighted in pink — the topmost highlighted third-party driver is your prime suspect.
5. Note the **Caused By Driver** column as a starting hypothesis, but verify with the stack rather than trusting it blindly.

### Fix 3: Get definitive answers with WinDbg Preview

When you need certainty, use Microsoft's own debugger.

1. Install **WinDbg Preview** from the Microsoft Store.
2. Open it, press `Ctrl + D`, and open the newest .dmp from `C:\Windows\Minidump`.
3. In the command box at the bottom, type `!analyze -v` and press Enter.
4. Wait for the analysis — the first run downloads symbols, which takes a few minutes.
5. Read the output: **BUGCHECK_STR** names the stop code, **MODULE_NAME** and **IMAGE_NAME** name the faulting driver, and **PROCESS_NAME** shows what was running.
6. The **STACK_TEXT** section shows the call chain — useful when the faulting module is a Windows file wrapping a third-party driver's mistake.

### Fix 4: Act on what the dump names

The dump is only useful if you follow through.

1. If a third-party .sys file is named, update it from the manufacturer's site or roll it back in **Device Manager > Properties > Driver**.
2. If a Windows system file (like ntfs.sys or ntoskrnl.exe) is named, it is usually the *victim* — look at the stack for the third-party driver above it, and also run `sfc /scannow` plus `DISM /Online /Cleanup-Image /RestoreHealth`.
3. If dumps consistently implicate memory corruption with no clear driver, test the RAM with MemTest86.
4. Document the pattern: same driver every time means a driver fix; different culprits each time leans toward RAM or hardware.

Our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) helps when the named driver crashes every boot, and disabling [automatic restart after BSOD](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) preserves the on-screen stop code as a cross-check against the dump.

### Fix 5: Stop cleaners from deleting your dumps

Protect the evidence.

1. Open your privacy/cleaner utility's settings and exclude `C:\Windows\Minidump` and `C:\Windows\MEMORY.DMP` from automatic cleaning.
2. In **Storage Sense** (**Settings > System > Storage**), verify it is not configured to delete debugging files aggressively.
3. Keep at least the last few dumps — patterns across multiple crashes are more diagnostic than any single one.

### Fix 6: Enable full dumps for elusive crashes

When minidumps do not capture enough:

1. In **Startup and Recovery** settings, change to **Automatic memory dump**.
2. Reproduce the crash; Windows writes `C:\Windows\MEMORY.DMP` (large — needs free space equal to RAM).
3. Analyze it in WinDbg the same way with `!analyze -v`.
4. Switch back to small dumps afterward to save disk space.

Microsoft documents dump configuration on [Microsoft Support](https://support.microsoft.com/en-us/windows), and advanced WinDbg usage is covered in their debugging documentation.

### Fix 7: Correlate dumps with Event Viewer for the full picture

Dumps plus event logs together beat either alone.

1. Open **Event Viewer > Windows Logs > System** and filter for **Error** and **Critical** events around each crash timestamp.
2. Look for disk errors (source: Disk, Ntfs), driver load failures, and **WHEA-Logger** entries near the crash.
3. A crash whose dump names a driver, preceded by disk errors in the log, suggests the driver file itself is corrupted on disk — run `chkdsk` and reinstall that driver rather than just updating it.
4. Save this correlation habit: for recurring crashes, keep a simple note of date, stop code, named driver, and any log anomalies. Patterns across five crashes diagnose what one crash cannot.

## Closing

Minidumps are the closest thing to a flight recorder your laptop has, and reading them is a skill that pays off every time a blue screen appears. BlueScreenView gives you the answer in thirty seconds for most crashes; WinDbg's `!analyze -v` settles the ambiguous ones. Make sure dumps are enabled *before* you need them, protect the Minidump folder from overzealous cleaners, and always act on what the dump names instead of updating drivers at random. Diagnose first, fix second — that is the whole game.
