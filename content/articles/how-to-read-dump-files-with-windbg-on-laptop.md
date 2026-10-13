---
title: "How to Read Dump Files with WinDbg on Your Laptop"
slug: how-to-read-dump-files-with-windbg-on-laptop
date: 2026-09-24
categories: ["windows-errors"]
tags: ["WinDbg", "crash dump analysis", "BSOD debugging"]
description: "Learn how to read Windows crash dump files with WinDbg on your laptop: install it, load the dump, run !analyze -v, and decode the failing driver."
thumbnail: "/images/thumbs/how-to-read-dump-files-with-windbg-on-laptop.webp"
faqs:
  - q: "Where does Windows store crash dump files on my laptop?"
    a: "By default, Windows writes small minidumps to C:\\Windows\\Minidump (one per crash) and a full kernel memory dump to C:\\Windows\\memory.dmp. If you crash regularly and the Minidump folder is empty, check Settings > System > About > Advanced system settings > Startup and Recovery, and set the dump type to Small memory dump (256 KB)."
  - q: "Is WinDbg free, and which version should I install?"
    a: "Yes, WinDbg is completely free from Microsoft. Install WinDbg Preview from the Microsoft Store on your laptop; it is the modern version with a better interface than the classic WinDbg. Both versions read the same dump files, but WinDbg Preview handles symbols and dark mode more gracefully."
  - q: "What does the !analyze -v command actually tell me?"
    a: "The !analyze -v command loads Microsoft's symbol server, walks the crashed thread's stack, and prints the bug check code, the faulting module, and the probable cause. For most laptop crashes, the line labeled MODULE_NAME or IMAGE_NAME points directly at the driver or system file responsible, saving you hours of blind guessing."
  - q: "Do I need to be online to read a dump file with WinDbg?"
    a: "Only for the first pass. WinDbg downloads debug symbols from Microsoft's symbol server the first time you analyze a dump, which requires internet access. After that, symbols are cached locally in your symbol folder, so you can reopen and re-read dumps offline without any delay."
---

When your laptop crashes to a blue screen, Windows quietly leaves a forensic report behind: a crash dump file. That little `.dmp` file records exactly what the kernel was doing when everything fell apart — which driver was running, what memory it touched, and which check failed. Learning to read it is the difference between guessing and knowing.

WinDbg is Microsoft's own debugger, and it is free. It looks intimidating the first time you open it, but reading a dump takes about five minutes once you know the handful of commands that matter. If you can follow a stop code like [CRITICAL_PROCESS_DIED](/articles/critical-process-died-blue-screen-error-fix/), you can follow this guide. Let's get your first dump open.

## Why this happens

- Windows writes minidumps to `C:\Windows\Minidump` by default, but a changed setting or a full disk can silently stop that from happening.
- Most guides assume you already have WinDbg installed and symbols configured, which is exactly the part beginners get stuck on.
- Reading a dump without symbols gives you raw memory addresses instead of names, which is useless for identifying the culprit.
- The classic WinDbg and WinDbg Preview have different menus, so following an old tutorial in the new app leads to dead ends.
- Dump files come in sizes — minidump, kernel dump, full dump — and picking the wrong one wastes time or disk space.
- Even a perfect `!analyze -v` run sometimes names a generic Windows file instead of the real third-party driver, which needs one more step to decode.

## How to fix it

Work through these in order: each step builds on the last, and by Fix 6 you will have a named culprit. If you are new to dump analysis in general, our broader walkthrough on [how to analyze BSOD dump files on Windows 11](/articles/how-to-analyze-bsod-dump-files-on-windows-11/) covers the concepts behind each command.

### Fix 1: Make sure Windows is actually saving dump files

Before anything else, confirm crash dumps are being written. Many laptops arrive with dumps disabled or set to "None" after a manufacturer tune-up.

1. Press **Win + R**, type `sysdm.cpl`, and press Enter to open System Properties.
2. Go to the **Advanced** tab and click **Settings** under Startup and Recovery.
3. In the **Write debugging information** dropdown, choose **Small memory dump (256 KB)**.
4. Confirm the small dump directory reads `%SystemRoot%\Minidump` and click **OK** twice.
5. After your next crash, check that `C:\Windows\Minidump` contains a `.dmp` file.

### Fix 2: Install WinDbg Preview from the Microsoft Store

WinDbg Preview is the current, supported debugger and the one Microsoft updates.

1. Open the **Microsoft Store** app on your laptop.
2. Search for `WinDbg Preview` and click **Get** to install it.
3. Launch **WinDbg Preview** once so it creates its settings folder.
4. If you prefer the classic version, it ships inside the Windows SDK, but Preview is easier for this job.
5. Keep it closed for now — you will open your dump file directly in the next fix.

### Fix 3: Locate and open your dump file

Minidumps live in one predictable place, and WinDbg Preview can open them straight from the File menu.

1. Open **File Explorer** and navigate to `C:\Windows\Minidump`.
2. Pick the most recent `.dmp` file (sort by **Date modified** if there are several).
3. Right-click the file, choose **Open with**, and select **WinDbg Preview**.
4. Alternatively, in WinDbg Preview go to **File > Open dump file** and browse to the `.dmp`.
5. Wait a few seconds while the debugger loads the file and prints initial output.

### Fix 4: Configure the symbol path once

Symbols translate memory addresses into human-readable function names. Without them, the analysis is gibberish.

1. In WinDbg Preview, go to **File > Settings** (or press **Ctrl + ,**).
2. Find the **Default symbol path** field.
3. Enter `SRV*C:\Symbols*https://msdl.microsoft.com/download/symbols` exactly as shown.
4. Click the back arrow to save — WinDbg creates the `C:\Symbols` cache folder automatically.
5. You need internet access the first time so symbols can download; afterwards they are cached locally.

### Fix 5: Run !analyze -v and read the verdict

This is the single most useful command in dump analysis, and it does most of the detective work for you.

1. In the command box at the bottom of WinDbg Preview, type `!analyze -v` and press Enter.
2. Wait while it downloads symbols and processes the dump — this can take a minute or two the first time.
3. Scroll to the section labeled **BUGCHECK_STR** to see the stop code (for example `0xEF`).
4. Look at **MODULE_NAME** and **IMAGE_NAME** — these name the file most likely responsible.
5. Read the short **ANALYSIS** summary; it often states the probable cause in plain language.

### Fix 6: Decode the faulting driver with lmvm

When the analysis names a `.sys` file, one more command tells you exactly which driver package it belongs to.

1. Note the driver name from **IMAGE_NAME**, for example `rtwlanu.sys`.
2. In the command box, type `lmvm rtwlanu` (the name without the `.sys`) and press Enter.
3. Read the **Image path** and **Company** lines to identify the vendor.
4. Check the **Timestamp** — a driver dated years before your Windows build is a prime suspect.
5. With the vendor identified, head to the manufacturer's site or [Microsoft's update catalog](https://www.catalog.update.microsoft.com/) to find a current version.

### Fix 7: Act on what the dump actually says

A dump that names a third-party driver is a gift — you know precisely what to fix instead of reinstalling Windows blindly.

1. If the culprit is a driver, update it from the hardware vendor's support page first.
2. If no newer driver exists, roll the driver back in **Device Manager > Properties > Driver > Roll Back Driver**.
3. If the dump blames a Windows system file, run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated Command Prompt.
4. Save the WinDbg output (**File > Save**) so you can compare dumps if crashes continue.
5. For recurring mystery crashes, Microsoft's own [Windows troubleshooting hub](https://support.microsoft.com/en-us/windows) documents the common stop codes the dump reveals.

## Closing

Reading a dump with WinDbg turns a scary blue screen into a labeled, actionable report. Once symbols are configured, the whole routine — open dump, `!analyze -v`, `lmvm` — takes under five minutes and points you at the real cause far more reliably than guesswork. Keep your symbol cache warm, save your analyses, and the next crash will be a quick diagnosis instead of a weekend project.
