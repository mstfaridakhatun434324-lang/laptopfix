---
title: "How to Read Dump Files with WinDbg on Windows 10"
slug: how-to-read-dump-files-with-windbg-on-windows-10
date: 2026-09-18
categories: ["windows-errors"]
tags: ["windbg", "dump files", "bsod analysis", "windows 10"]
description: "Still on Windows 10 and fighting blue screens? Here's how to read crash dumps with WinDbg and find the exact failing driver."
thumbnail: "/images/thumbs/how-to-read-dump-files-with-windbg-on-windows-10.webp"
faqs:
  - q: "Does WinDbg work on Windows 10?"
    a: "Yes. The Microsoft Store version of WinDbg runs on Windows 10 (version 1809 and later) and analyzes Windows 10 dumps perfectly. The steps are nearly identical to Windows 11 — the differences are noted in this guide."
  - q: "Where are dump files on Windows 10?"
    a: "Same locations as Windows 11: minidumps in C:\\Windows\\Minidump and the full dump at C:\\Windows\\MEMORY.DMP. Configure them via Control Panel > System > Advanced system settings > Advanced tab > Startup and Recovery Settings."
  - q: "Do I need the old Debugging Tools for Windows on Windows 10?"
    a: "No — the Microsoft Store WinDbg is the current, supported version and works fine on Windows 10. Avoid old tutorials pointing at the standalone SDK installer; the Store app is easier and stays updated."
  - q: "Can WinDbg analyze dumps from another PC?"
    a: "Yes. Copy the .dmp file from C:\\Windows\\Minidump to any PC running WinDbg and open it there. Minidumps are tiny (~256 KB), so they're easy to share when asking for help."
---

Windows 10 blue screens write the same crash dumps as Windows 11 — snapshots of the system at the moment of the crash, containing the stop code, the failing driver, and the call stack. Reading them with **WinDbg** (free, from the Microsoft Store) turns "my PC keeps crashing" into "this specific driver is crashing," which is the difference between guessing and fixing. The process on Windows 10 is nearly identical to Windows 11; this guide notes the small differences.

If you're comfortable on Windows 10 and just need the technique, this is the whole thing: install, open dump, set symbols, run one command, read the answer. Our [Windows 11 WinDbg guide](/articles/how-to-read-dump-files-with-windbg-on-windows-11/) covers the same ground for the newer OS — the analysis skills transfer completely.

## Why this happens (why dumps are worth reading)

- **The stop code isn't enough**: It tells you the crash *type*; the dump tells you the *culprit*. `IRQL_NOT_LESS_OR_EQUAL` could be ten different drivers — the dump names one.
- **Windows 10's update drivers cause crashes too**: Windows Update on Windows 10 replaces manufacturer drivers just as aggressively, and the dump identifies which replacement broke.
- **Patterns beat single crashes**: Several dumps blaming one driver = update that driver. Different drivers every time = test the RAM.
- **It's the same tool the pros use**: Microsoft support engineers analyze dumps with WinDbg. You're using the genuine article, not a third-party guesser.
- **Minidumps are small and portable**: At ~256 KB each, you can email one to anyone for a second opinion.
- **One-time setup**: Installing WinDbg and configuring symbols takes fifteen minutes once; every analysis after that takes two.

## How to fix it (how to analyze a dump)

Work through these in order — setup once, analyze forever.

### Fix 1: Install WinDbg from the Microsoft Store

1. Open the **Microsoft Store** on your Windows 10 PC (version 1809 or later required) and search for **WinDbg**.
2. Install the **WinDbg** app published by Microsoft — free, and the current supported version.
3. Launch it once to finish first-run setup.

On older Windows 10 builds where the Store version won't install, update Windows 10 first — the Store WinDbg is worth it over the legacy SDK tools.

### Fix 2: Confirm dump creation is enabled

Windows 10 usually creates minidumps by default, but verify — especially if a "cleaner" utility has been run.

1. Open **Control Panel** > **System and Security** > **System** > **Advanced system settings**.
2. On the **Advanced** tab, click **Settings** under **Startup and Recovery**.
3. Set **Write debugging information** to **Small memory dump (256 KB)** (or **Automatic memory dump**). Microsoft documents these [startup and recovery settings](https://support.microsoft.com/en-us/windows) if you need more detail.
4. Note the dump path: `%SystemRoot%\Minidump` by default.
5. Ensure the page file exists on the system drive: same dialog chain > **Performance Settings** > **Advanced** tab > **Change** — the system drive needs a page file (Windows manages this automatically unless someone disabled it; minidumps require it).

### Fix 3: Open the minidump

1. In WinDbg: **File** > **Open dump file** (**Ctrl + D**).
2. Browse to `C:\Windows\Minidump`, sort by date, and open the newest `.dmp`.
3. Accept default workspace prompts. The command input bar at the bottom is where you'll type the analysis command.

To analyze someone else's crash: have them copy the `.dmp` from their Minidump folder and send it to you — open it the same way.

### Fix 4: Configure the symbol path

Symbols translate raw addresses into readable function names. Set this once.

1. In WinDbg: **File** > **Settings** > **Debugging settings**.
2. In **Symbol path**, enter: `srv*C:\Symbols*https://msdl.microsoft.com/download/symbols`
3. WinDbg downloads what it needs from Microsoft on first use (allow firewall access) and caches it in `C:\Symbols` for instant reuse.

### Fix 5: Run !analyze -v and read the output

1. Type `!analyze -v` in the command bar and press Enter. Wait 10-60 seconds (longer the first time while symbols download).
2. Read these fields:
   - **BugCheck / stop code**: the crash type in hex and name.
   - **Probably caused by**: WinDbg's verdict — usually the exact driver file.
   - **IMAGE_NAME / MODULE_NAME**: the driver module.
   - **STACK_TEXT**: the call stack — scan for third-party `.sys` names even if you don't understand the rest.
   - **FAILURE_BUCKET_ID**: Microsoft's crash signature — excellent search term.
   - **PROCESS_NAME**: which program was running — useful context (crashes only in one game point at the GPU driver, for instance).
3. Common mappings: `nvlddmkm.sys` = NVIDIA, `atikmdag.sys` = AMD, `igdkmd64.sys` = Intel graphics, `rtwlanu.sys` / `Netwtw10.sys` = wireless, `ntoskrnl.exe` blamed = usually *not* the kernel's fault (suspect RAM or a corrupting driver).

### Fix 6: Act on the result

1. **Third-party driver named** → update from the vendor/laptop maker, or roll back if crashes started after an update. Clean-install graphics drivers.
2. **Windows file blamed** → usually collateral damage; check other dumps for the real pattern and test RAM.
3. **Same driver across dumps** → that driver is the problem. Focus everything there.
4. **Different drivers each time** → run `mdsched.exe`, then MemTest86 — rotating blame means hardware (RAM or drive).
5. Search the **FAILURE_BUCKET_ID** + driver name online for known issues and fixed versions.

### Fix 7: Build a crash table from multiple dumps

1. Analyze every dump in the Minidump folder (`!analyze -v` each — use **File** > recent files to move fast).
2. Record: date, stop code, "probably caused by."
3. Look for the pattern: one repeat offender (driver fix), rotating offenders (hardware test), or a start date matching an update (rollback).

## Closing

Dump analysis on Windows 10 is the same skill as on Windows 11, and it's the highest-leverage troubleshooting technique for recurring blue screens on either OS. The fifteen-minute setup pays for itself the first time you skip a week of random driver updates because the dump named the culprit in one command. Keep WinDbg installed — the next crash is a matter of when, not if, on any long-lived Windows 10 machine, and you'll be ready. Pair this with our [blue screen hub](/articles/how-to-fix-blue-screen-of-death-windows-11/) to route each identified cause to its fix.
