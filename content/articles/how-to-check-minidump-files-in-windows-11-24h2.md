---
title: "How to Check Minidump Files in Windows 11 24H2"
slug: how-to-check-minidump-files-in-windows-11-24h2
date: 2026-09-24
categories: ["windows-errors"]
tags: ["minidump", "bsod analysis", "windbg", "bluescreenview"]
description: "Read Windows 11 minidump files to find what caused your blue screen — enable dumps, use BlueScreenView for quick answers, and WinDbg for deep analysis."
thumbnail: "/images/thumbs/how-to-check-minidump-files-in-windows-11-24h2.webp"
faqs:
  - q: "What is a minidump file?"
    a: "A small snapshot Windows saves automatically every time it blue-screens. It records the stop code, which driver or component was executing when the crash happened, and the state of the system. It is the single most useful artifact for diagnosing any BSOD."
  - q: "Where are minidump files stored?"
    a: "In C:\\Windows\\Minidump, one .dmp file per crash, named by date (e.g., 091526-12345-01.dmp). You need administrator access to open the folder. If the folder is empty after a blue screen, dumps are disabled — Fix 1 shows how to turn them on."
  - q: "Do I need to be technical to read a minidump?"
    a: "Not for the basics. BlueScreenView shows the stop code and the suspected driver in plain text with zero expertise required. WinDbg takes more learning but gives the definitive answer for tricky cases."
  - q: "Can a minidump tell me exactly which driver crashed?"
    a: "Usually yes — the dump records the faulting module in most driver-caused crashes. Occasionally it names a Windows component that was merely the victim, in which case WinDbg's deeper analysis (!analyze -v) distinguishes the culprit from the bystander."
---

Every blue screen leaves behind a witness: the **minidump file**. Windows writes one automatically at each crash, capturing the stop code, the faulting driver or component, and a snapshot of what the system was doing. Learning to read these files turns BSOD troubleshooting from guesswork into evidence-based diagnosis — instead of trying fixes at random, you find the actual culprit first.

This guide covers Windows 11 24H2: making sure dumps are enabled, reading them the easy way with BlueScreenView, and going deeper with WinDbg when you need the full story. Once you can read dumps, every other blue screen guide on this site — from [DPC_WATCHDOG_VIOLATION](/articles/how-to-fix-dpc-watchdog-violation-on-windows-11/) to [Driver Verifier crashes](/articles/troubleshoot-driver-verifier-detected-violation/) — becomes twice as useful.

## Why this happens

Not "why do crashes happen" — but why dumps matter and why they sometimes go missing:

- **Dumps are disabled.** Some "debloat" scripts and privacy tools turn off crash dumps, leaving you with no evidence after a BSOD.
- **No page file, no dump.** Windows writes the dump through the page file mechanism — if the page file is disabled or too small, dumps silently fail.
- **The dump names a victim, not the killer.** A crash in `ntoskrnl.exe` usually means a driver corrupted the kernel, not that the kernel itself is broken — interpretation matters.
- **Old dumps get overwritten.** Windows keeps only a limited number of minidumps; new crashes push old ones out.
- **Third-party "cleaners" delete dumps.** Disk cleanup tools often wipe the Minidump folder, destroying your evidence.

## How to fix it

"Fix" here means: enable dumps, read them, and act on what they say. Work through these in order.

### Fix 1: Make sure minidumps are enabled

1. Press **Win + R**, type `sysdm.cpl`, and press Enter.
2. Go to the **Advanced** tab and click **Settings** under **Startup and Recovery**.
3. Under **Write debugging information**, select **Small memory dump (256 KB)**.
4. Confirm the **Small dump directory** is `%SystemRoot%\Minidump`.
5. Make sure **Automatically restart** is checked and click **OK**. Future blue screens will now leave dumps behind.

### Fix 2: Verify the page file is system-managed

Dumps depend on the page file — a disabled page file means no dumps.

1. In the same **System Properties > Advanced** tab, click **Settings** under **Performance**.
2. Go to the **Advanced** tab and click **Change** under **Virtual memory**.
3. Check **Automatically manage paging file size for all drives**. If it was unchecked with a custom tiny size (or "No paging file"), that is why dumps were missing.
4. Click **OK**, restart if prompted. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the page file requirements for crash dumps in detail.

### Fix 3: Find and copy your dump files

1. Open **File Explorer** and navigate to `C:\Windows\Minidump`. Click **Continue** when Windows asks for administrator permission.
2. You will see files like `091526-18432-01.dmp` — one per crash, dated in the filename.
3. **Copy** (do not move) the most recent few to your Desktop or Documents. Always analyze copies, so the originals stay intact.
4. If the folder is empty despite recent blue screens, revisit Fixes 1–2, and check that disk cleanup tools are not wiping the folder.

### Fix 4: Read dumps the easy way with BlueScreenView

BlueScreenView (free, from NirSoft) gives you the answer in 60 seconds with no expertise.

1. Download BlueScreenView and run it (no installation needed).
2. It automatically loads every dump in `C:\Windows\Minidump` and lists them top to bottom, newest first.
3. Click a crash: the bottom pane highlights the drivers involved. The one in **pink/red** is the prime suspect.
4. Note three things: the **Bug Check String** (e.g., DPC_WATCHDOG_VIOLATION), the **Bug Check Code** (e.g., 0x00000133), and the **Caused By Driver** filename.
5. Google the driver filename to identify its device, then update or remove that driver.

### Fix 5: Go deeper with WinDbg Preview

When BlueScreenView's answer is ambiguous (it blames `ntoskrnl.exe`, which is almost never the real culprit):

1. Install **WinDbg Preview** from the Microsoft Store.
2. Press **Ctrl + D** and open your copied dump file.
3. Type `!analyze -v` in the command box and press Enter. Wait for the full analysis.
4. Read **MODULE_NAME** / **IMAGE_NAME** for the faulting driver, and the analysis text for *what it did wrong* — e.g., "attempted to write to read-only memory."
5. For stack context, type `k` to see the call stack — the drivers listed just below the crash point are your suspects.
6. WinDbg downloads symbols from Microsoft automatically on first use; give it a minute on the first analysis.

### Fix 6: Interpret common patterns correctly

Knowing what the dump is really telling you:

1. **Dump blames ntoskrnl.exe / hal.dll** — almost never the actual cause. Look at the stack and the other loaded drivers; a third-party driver corrupted kernel memory.
2. **Same driver in every dump** — you have your culprit. Update it, roll it back, or remove the device.
3. **Different driver every time** — suspect RAM or a failing drive, not drivers. Run `mdsched.exe` (see our [Memory Diagnostic guide](/articles/how-to-run-memory-diagnostic-tool-on-windows-11/)).
4. **Dump blames a Windows driver like storahci.sys or tcpip.sys** — the Windows driver is usually the victim of a misbehaving filter driver or hardware fault beneath it.

### Fix 7: Act on the findings and verify

1. Update, roll back, or remove the identified driver via **Device Manager**.
2. If the dump pointed at hardware (RAM/disk patterns), run the hardware tests — memory diagnostic and `chkdsk C: /f /r`.
3. After the fix, monitor for a week. If a new blue screen occurs, analyze the *new* dump — do not assume it is the same cause.
4. Keep at least the last few dumps archived before any disk cleanup, so you have history if crashes return.

## Closing

Minidumps turn blue screen troubleshooting from superstition into science. Enable them, read them with BlueScreenView for the quick answer or WinDbg for the definitive one, and let the evidence — not guesswork — decide which driver you update. Ten minutes learning to read a dump will save you hours of randomly trying fixes, and it is the single skill that makes every other BSOD guide on this site work better.
