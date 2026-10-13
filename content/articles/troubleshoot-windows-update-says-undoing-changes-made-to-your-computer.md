---
title: "Troubleshooting 'Undoing Changes Made to Your Computer' After a Windows Update"
slug: troubleshoot-windows-update-says-undoing-changes-made-to-your-computer
date: 2026-10-05
categories: ["windows-update"]
tags: ["undoing changes", "update troubleshooting", "windows update logs", "error codes", "windows 11"]
description: "A technician's diagnostic approach to 'Undoing changes made to your computer': reading logs, decoding error codes, and isolating the exact failure."
thumbnail: "/images/thumbs/troubleshoot-windows-update-says-undoing-changes-made-to-your-computer.webp"
faqs:
  - q: "Where do I find logs for a failed Windows update?"
    a: "The main log is C:\\Windows\\Logs\\CBS\\CBS.log, which records servicing operations in detail. For update-specific history, PowerShell's Get-WindowsUpdateLog generates a readable log on the desktop. The Event Viewer under Windows Logs > System, filtered for the WindowsUpdateClient source, gives a cleaner timeline of what failed and when."
  - q: "What does error 0xC1900101 mean during an update?"
    a: "It's a driver-related rollback code — Windows couldn't migrate a driver to the new build. The extended code after it (like 0x30018 or 0x40017) pinpoints the phase: 0x30018 is a first-boot driver failure, 0x40017 is a second-boot failure. Our dedicated [0xC1900101 guide](/articles/how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update/) decodes each variant."
  - q: "How can I tell if the rollback damaged anything?"
    a: "Run sfc /scannow and DISM /Online /Cleanup-Image /ScanHealth after the rollback completes. A clean rollback leaves the system identical to its pre-update state, and these tools confirm it. If they report corruption, repair it before retrying the update or the next attempt will fail the same way."
  - q: "Should I use SetupDiag for update failures?"
    a: "Yes, for feature update failures especially. SetupDiag is Microsoft's free diagnostic that parses setup logs and matches failure signatures against known issues, often naming the exact driver or component that caused the rollback. Download it from Microsoft's site and run it after any failed feature update."
---

Most "undoing changes" advice is a list of things to try. This guide is different: it's about diagnosing before you touch anything. A rollback leaves evidence — error codes, log entries, setup diagnostics — and reading that evidence first means you apply one correct fix instead of seven hopeful ones. If you've already rolled back two or three times trying random suggestions, stop and troubleshoot properly. The failure is telling you exactly what's wrong; you just need to know where it wrote it down.

Think of it like a check-engine light. You can clear codes and hope, or you can read the code and fix the sensor. Windows' update engine is verbose to a fault — CBS.log alone records every file operation — so the challenge isn't finding information, it's knowing which sources matter. Below is the diagnostic sequence a technician follows: history and codes first, logs second, targeted isolation third, and only then the repair.

## Why this happens

- **Driver migration failure**: The most common diagnosed cause — a driver that can't transition to the new build, logged with 0xC1900101 variants.
- **Servicing stack corruption**: The update engine itself is damaged, visible as repeated CBS.log errors during the install phase.
- **Disk or filesystem errors**: Chkdsk-repairable bad sectors in the paths the update writes to.
- **Incompatible firmware**: BIOS/UEFI versions the new build explicitly rejects, sometimes logged plainly in setupact.log.
- **Antivirus file locks**: Security software holding exclusive locks on files the update must replace.
- **Staged package corruption**: The downloaded payload failing hash checks, visible in the WindowsUpdateClient event log.
- **Insufficient reserved partition space**: The EFI or recovery partition too small for the update's boot file changes — a classic silent rollback cause.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Extract the full story from Update history

Start with the highest-signal, lowest-effort source. The history page often contains more detail than people notice.

1. Go to **Settings > Windows Update > Update history**.
2. Find the failed update and expand it — note the **KB number**, **error code**, and **timestamp**.
3. Click **Learn more** if offered; Microsoft's KB articles sometimes document known rollback causes for that specific package.
4. Check whether **driver updates** failed in the same window — a failed driver alongside the OS update strongly suggests the driver caused the rollback.
5. If multiple updates failed simultaneously, the earliest timestamp is usually the root cause; later failures are collateral.

### Fix 2: Read the WindowsUpdateClient events in Event Viewer

The Event Viewer gives you a clean timeline without the noise of CBS.log. This is where you confirm what actually failed versus what merely reported afterward.

1. Press Win + R, type `eventvwr.msc`, and press Enter.
2. Navigate to **Windows Logs > System**.
3. Click **Filter Current Log** and set the event source to **WindowsUpdateClient**.
4. Look at events around the failure timestamp — **error** and **warning** entries describe download, install, and rollback phases.
5. Note event IDs: **20** is installation failure, **31** is download failure. The message text often names the failing component.
6. Cross-reference the timestamps with the Update history entry to build the failure sequence.

### Fix 3: Run SetupDiag for feature update rollbacks

For feature updates (the big twice-yearly ones), Microsoft's SetupDiag tool automates the log analysis you'd otherwise do by hand. It matches your logs against known failure signatures.

1. Download **SetupDiag** from Microsoft's official site (search "SetupDiag download Microsoft").
2. After a failed feature update, run `SetupDiag.exe` from an elevated Command Prompt.
3. It analyzes logs in `C:\$Windows.~BT\Sources\Panther` and produces **SetupDiagResults.log**.
4. Open the results — it names the failure rule, e.g., "FindAbruptDownlevelFailure" or a specific driver block.
5. Follow its specific recommendation; it's matched to Microsoft's known-issue database.
6. Keep the results file — if you end up contacting support, it's the first thing they'll ask for.

### Fix 4: Decode 0xC1900101 extended codes

If your error is in the 0xC1900101 family, the digits after the dash identify the exact phase. Different phases mean different fixes.

1. Find the full code in Update history or setupact.log — format is **0xC1900101 - 0xXXXXX**.
2. **0x2000C / 0x30018**: driver failure during first boot phase — update or remove recently added drivers.
3. **0x4000D / 0x40017**: second-boot failure — often storage or display drivers; try the [driver rollback procedure](/articles/how-to-rollback-driver-update-in-windows-11-24h2/).
4. **0x50012 / 0x50015**: app or driver compatibility block — uninstall the flagged application.
5. Check `C:\$Windows.~BT\Sources\Panther\setupact.log` and search for "Failed" near the end — the log names the specific driver file (e.g., `oem42.inf` or `driver.sys`).
6. Once identified, update that driver from the manufacturer or temporarily uninstall the device.

### Fix 5: Verify system integrity before the retry

A rollback should leave the system pristine, but verify rather than assume. Retrying on a damaged foundation wastes another cycle.

1. Open **Command Prompt as administrator**.
2. Run `DISM /Online /Cleanup-Image /ScanHealth` — if it reports repairable corruption, run `/RestoreHealth`.
3. Run `sfc /scannow` and confirm "did not find any integrity violations."
4. Run `chkdsk C: /f` to rule out filesystem damage from the failed install.
5. Check free space: `wmic logicaldisk get caption,freespace` — ensure 20+ GB on C:.
6. Only when all four are clean should you unpause updates and retry.

### Fix 6: Isolate with a clean boot and staged retry

If logs point at software interference but don't name it, a clean boot plus a staged update sequence isolates the culprit methodically.

1. Pause updates for one week to control the timing.
2. Perform a clean boot: `msconfig` > hide Microsoft services > disable all; disable all Task Manager startup items.
3. Unpause and install **only** the failing update (use "Show or hide updates" to block others temporarily).
4. If it succeeds, re-enable services in halves to identify the conflicting software.
5. Common culprits found this way: third-party disk encryption, old VPN clients, and "system optimizer" tools.
6. Document what you find — if it's a work laptop, IT needs to know before the next update cycle.

### Fix 7: Check the partitions the logs don't mention

Some rollbacks trace to partition space, not files. The EFI system partition and recovery partition need room for boot file updates, and Windows' error messages rarely say so.

1. Open **Disk Management** (Win + X > Disk Management).
2. Check the **EFI System Partition** — if it's 100 MB and nearly full, feature updates can fail here.
3. Check the **Recovery Partition** — 24H2-era updates sometimes need to update WinRE, requiring ~500 MB free.
4. If partitions are cramped, the reliable fix is a clean install with modern partition sizes, or an in-place upgrade which recreates them.
5. Microsoft documents WinRE space requirements on the [Windows support site](https://support.microsoft.com/en-us/windows).
6. For the full step-by-step recovery sequence after diagnosis, our [direct fix guide](/articles/how-do-i-fix-windows-update-says-undoing-changes-made-to-your-computer/) picks up where this diagnostic leaves off.

## Closing

Troubleshooting beats trying. Fifteen minutes with Update history, Event Viewer, and SetupDiag tells you more than a day of random fixes — and the error code you extract points at exactly one of the repairs above. Diagnose first, act second, and the "undoing changes" screen becomes a one-time event with a known cause instead of a recurring mystery.
