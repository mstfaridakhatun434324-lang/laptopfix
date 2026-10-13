---
title: "How to Analyze BSOD Dump Files on Windows 11 (24H2)"
slug: how-to-analyze-bsod-dump-files-in-windows-11-24h2
date: 2026-09-08
categories: ["windows-errors"]
tags: ["bsod", "windbg", "dump files"]
description: "Learn to read Windows 11 24H2 crash dumps with WinDbg: find the faulty driver behind any blue screen in under 15 minutes."
thumbnail: "/images/thumbs/how-to-analyze-bsod-dump-files-in-windows-11-24h2.webp"
faqs:
  - q: "Where are BSOD dump files stored on Windows 11?"
    a: "Minidumps live in C:\\Windows\\Minidump, one file per crash named by date (e.g., 101326-12345-01.dmp). Full memory dumps go to C:\\Windows\\MEMORY.DMP but are huge; minidumps contain everything needed for driver identification and are the better default."
  - q: "Do I need programming skills to analyze a dump?"
    a: "No. Running !analyze -v and reading the MODULE_NAME and IMAGE_NAME lines requires zero coding — it's closer to reading a report than debugging software. The deeper commands (!thread, lmvm) are optional and only needed when the basic analysis is inconclusive."
  - q: "Why does WinDbg say 'Probably caused by ntoskrnl.exe'?"
    a: "Ntoskrnl.exe is the Windows kernel itself — it's blamed when the real culprit corrupted kernel memory and vanished, or when the analysis can't pin a third-party driver. Treat it as 'systemic cause': test RAM, check overclocks, and update drivers broadly rather than targeting one file."
  - q: "My Minidump folder is empty after a blue screen — why?"
    a: "Either dumps are disabled in Startup and Recovery settings, a disk cleaner deleted them, or the crash happened so early (or the disk is so full) that Windows couldn't write one. Enable Small memory dump in Fix 1, ensure a few GB free on C:, and exclude the Minidump folder from cleaner tools."
---

Every blue screen leaves behind a crash dump — a snapshot of exactly what Windows was doing when it died. Learning to read these dumps turns every future blue screen from a mystery into a named suspect, and on Windows 11 24H2 the tools are free and the process takes about 15 minutes once you know it.

This guide walks through installing WinDbg, opening your latest dump, and running the two commands that identify the culprit in most cases. If you'd rather start with a specific error, our [KMODE walkthrough](/articles/kmode-exception-not-handled-blue-screen-error-fix/) shows dump analysis applied to a real crash.

## Why this happens

- Guessing at blue screen causes wastes hours — the dump usually names the faulty driver directly.

- Minidumps being disabled, so crashes leave no dump to analyze.

- WinDbg symbol setup confusion stopping people before they start.

- Not knowing which of the several dump files is the relevant one.

- Automatic memory dumps overwriting each other, losing the crash you cared about.

- Trying to analyze dumps on a different PC without the right symbol path.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Make sure dumps are being created

No dump, no analysis. First confirm Windows is actually saving crash data.

1. Open **Settings > System > About**, click **Advanced system settings**, then **Settings** under **Startup and Recovery**.

2. Set **Write debugging information** to **Small memory dump (256 KB)** — minidumps are all you need for driver identification.

3. Note the dump location: `%SystemRoot%\Minidump` (usually `C:\Windows\Minidump`).

4. Untick **Automatically restart** while you're here — it keeps the blue screen visible so you can photograph the stop code. Our [auto-restart guide](/articles/best-way-to-disable-automatic-restart-after-bsod/) covers this too.

### Fix 2: Install WinDbg from the Microsoft Store

The modern WinDbg Preview is a free Store app — no SDK download, no ancient installer wizards.

1. Open the **Microsoft Store** and search for **WinDbg**.

2. Install **WinDbg Preview** (published by Microsoft).

3. Launch it once so it creates its folders.

4. If the Store itself won't open, our [Store repair guide](/articles/how-to-fix-windows-store-not-opening-on-hp-laptop/) fixes that first — the steps work on any brand.

### Fix 3: Open your latest minidump

Each crash writes one minidump file named by date. Open the newest one.

1. In WinDbg, press **Ctrl + O** or use **File > Open dump file**.

2. Navigate to `C:\Windows\Minidump` and open the most recent **.dmp** file.

3. WinDbg will churn for a minute downloading symbols — let it finish.

4. If the folder is empty, dumps are disabled (see Fix 1) or a cleaner tool deleted them.

### Fix 4: Run !analyze -v

This single command is 90% of dump analysis. It processes the crash and usually names the faulty module outright.

1. In the command box at the bottom, type `!analyze -v` and press **Enter**.

2. Wait for the analysis to complete — it takes 30-90 seconds.

3. Read the **MODULE_NAME** and **IMAGE_NAME** lines — that's your culprit file (e.g., `nvlddmkm.sys`).

4. Read the **Probably caused by** line, but treat it as a hint, not gospel — it can blame `ntoskrnl.exe` when the real cause is a driver it loaded.

### Fix 5: Dig deeper with follow-up commands

When !analyze -v is vague, these commands extract more: the driver version, the stack, and Verifier data.

1. Run `lmvm <drivername>` (e.g., `lmvm nvlddmkm`) to see the driver version, date, and company — outdated third-party drivers stand out immediately.

2. Run `!thread` to see what the crashing thread was doing.

3. If Driver Verifier was involved, `!verifier` shows the violation details.

4. Run `.ecxr` to inspect the exception context record for the exact faulting instruction.

### Fix 6: Act on what the dump tells you

Analysis without action is trivia. The dump result maps directly to a fix.

1. If a third-party **.sys** is named: update, roll back, or cleanly reinstall that driver from the manufacturer's site.

2. If `ntoskrnl.exe` or `hal.dll` is blamed with no clear driver: test RAM with `mdsched.exe` and check for overclocks — the cause is systemic.

3. If the same driver recurs after updating: try the previous stable version, or check the vendor's forums for known issues.

4. Document the stop code and driver name — if you ever need shop help, this is exactly what a technician asks for. Microsoft's debugging resources are linked from [their Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 7: Set up a local symbol cache

WinDbg downloads debugging symbols from Microsoft on every analysis, which is slow and fails offline. A local symbol cache downloads once and reuses — making every future analysis dramatically faster.

1. In WinDbg's command box, type `.sympath srv*C:\Symbols*https://msdl.microsoft.com/download/symbols` and press **Enter**.

2. Run `.reload` to populate the cache with the symbols for your current Windows build.

3. Wait for the download to finish — it's a one-time cost of a few minutes.

4. Save your workspace (**File > Save workspace**) so the path persists.

5. Future dump analyses will resolve symbols from the local cache in seconds.

6. If symbols ever look stale after a Windows update, just run `.reload` again.

## Closing

Dump analysis sounds intimidating, but the actual workflow is: open WinDbg, open the newest minidump, run !analyze -v, read MODULE_NAME. Fifteen minutes, and you know more about your blue screen than most forum threads ever will. Make it a habit — every crash you analyze makes the next one faster, and you'll stop fearing blue screens once you can read their autopsy reports. Once symbols are cached, dump analysis becomes a two-minute job: open the dump, run !analyze -v, read the module name. Save each verdict in a notes file — over months that log becomes a personal reliability database for your exact hardware, and patterns you'd never notice one crash at a time start jumping out.
