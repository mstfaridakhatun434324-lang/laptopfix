---
title: "Fix Windows Update Error 0x80070020 on Windows 10: Sharing Violation"
slug: how-to-fix-windows-update-error-0x80070020-on-windows-10
date: 2026-09-16
categories: ["windows-update"]
tags: ["windows update", "0x80070020", "file in use", "antivirus", "windows 11"]
description: "Windows 10 error 0x80070020 is a sharing violation — something holds the files Windows Update needs. These fixes release the locks and finish the install."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070020-on-windows-10.webp"
faqs:
  - q: "What does error 0x80070020 mean?"
    a: "On Windows 10, 0x80070020 is ERROR_SHARING_VIOLATION: Windows Update tried to access a file that another process has locked. The most common lockers are third-party antivirus real-time scanning, a second installer running simultaneously, or stale handles from an interrupted update. Restarting, pausing the antivirus, or clean-booting releases the locks."
  - q: "Can antivirus really block Windows Update?"
    a: "Yes — it is the leading cause of this error. Real-time scanning opens files the instant they are accessed, which keeps handles on the executables Windows Update must replace. Pausing the third-party suite for one update attempt is the standard test; if the update then succeeds, add servicing exclusions in the antivirus settings rather than disabling it permanently."
  - q: "Why does Restart work but Shut down does not?"
    a: "With Fast Startup enabled, Shut down hibernates the kernel session, preserving driver and service state — including some file locks. Restart performs a full kernel reinitialization, which genuinely releases every lock. For any sharing-violation error, always choose Restart when the fix calls for a reboot."
  - q: "How do I find which program is locking the file?"
    a: "Open Task Manager and look for installer, setup, updater, or antivirus processes holding activity during the update. For precision, Microsoft's free Process Explorer can show exactly which process holds a handle on a given file. In practice, clean-booting is faster than detective work: if the update succeeds with third-party services disabled, the culprit is among them."
---
On Windows 10, 0x80070020 translates to ERROR_SHARING_VIOLATION: the process cannot access the file because it is being used by another process. In update terms, Windows Update needs to overwrite system files that your antivirus, a background installer, or a utility currently has locked. The update is fine; the timing is the problem.

Laptops are especially prone to this because OEM utilities, updaters, and security suites all compete for the same files during the narrow window when updates install. The strategy below removes the competition one layer at a time until the update gets the exclusive access it needs.

The [Windows 11 guide](/articles/how-to-fix-windows-update-error-0x80070020-on-windows-11/) handles this error on Windows 11, and the [companion guide for 0x80070652](/articles/how-to-fix-windows-update-error-0x80070652-on-windows-10/) helps when the competing process is a stuck installer. Work through these in order.

## Why this happens

- **Antivirus real-time scanning holds the files open:** Third-party security suites scan files the moment they are touched, which keeps handles open on exactly the executables and libraries Windows Update is trying to replace — the number-one cause of 0x80070020.
- **Another installer is running at the same time:** If a program's own updater, a Store app update, or a second Windows Installer session is active, its file locks collide with the update engine's, and one of them loses with this error.
- **A previous update attempt left stale locks:** An interrupted update can leave processes or pending file operations holding references that are never released until the system restarts, so every retry hits the same wall.
- **Background utilities hook system files:** System optimizers, overlay tools, and some gaming utilities inject into or monitor system components, keeping those files open and unreplaceable during servicing.
- **Windows Search or indexing has files open:** The indexer occasionally holds handles on files being serviced, particularly right after boot when it is catching up on a backlog.
- **Malware is protecting its own files:** Malicious software sometimes locks the very system files it has infected to resist removal, and an update trying to replace those files trips the sharing violation.
- **The update queue itself is in a conflicted state:** Corrupted pending operations in the servicing stack can make the engine fight itself for file access, producing a sharing violation with no visible third-party culprit.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart and retry before anything else

Use Restart rather than Shut down — on machines with Fast Startup enabled, shutdown hibernates the kernel session and preserves some locks, while Restart truly reinitializes everything.

1. Close all open programs and save your work.
2. Click Start > Power > Restart (not Shut down).
3. After logging back in, wait two minutes for startup activity to settle.
4. Open Settings > Update & Security > Windows Update and click Check for updates.
5. If the error is gone, you are done — the lock was transient.

### Fix 2: Temporarily disable third-party antivirus

Re-enable protection immediately after the test. The long-term fix is an exclusion or a settings change in the suite, not running unprotected.

1. Open your third-party antivirus and disable real-time protection and any behavior shield.
2. Keep Windows Security's own real-time protection active as your safety net.
3. Run the update from Settings > Update & Security > Windows Update while the third-party suite is paused.
4. If it succeeds, re-enable the suite, then add the Windows servicing folders to its exclusions per the vendor's documentation.
5. If it still fails, re-enable protection and continue — the AV is innocent.

### Fix 3: End stuck installer processes

Check both the Processes list and the Details tab, since installer processes sometimes hide under generic names.

1. Press Ctrl + Shift + Esc to open Task Manager.
2. On the Processes tab, look for any Setup, Installer, or msiexec entries and end them.
3. Switch to the Details tab and end any remaining `msiexec.exe` processes.
4. Also end obvious third-party updater processes (OEM update tools, game launchers).
5. Retry the update in Settings > Update & Security > Windows Update.

### Fix 4: Perform a clean boot, then update

This is diagnostic and therapeutic in one step: many users simply perform updates in a clean boot whenever the error appears, then return to normal startup.

1. Press Win + R, type `msconfig`, and press Enter.
2. On the Services tab, check Hide all Microsoft services, then Disable all.
3. In Task Manager's Startup tab, disable all startup items.
4. Restart, run the update from Settings > Update & Security > Windows Update, then undo the msconfig changes and restart again.
5. For background on isolating the culprit, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the clean-boot procedure in detail.

### Fix 5: Restart the Windows Update services

This takes a minute from an elevated command prompt and is harmless to installed updates.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv` and `net stop bits`.
3. Wait ten seconds, then run `net start bits` and `net start wuauserv`.
4. Also restart the cryptographic service: `net stop cryptsvc` then `net start cryptsvc`.
5. Check for updates again.

### Fix 6: Scan for malware and repair system files

Run the scan first so SFC restores files that are actually clean rather than re-validating infected ones.

1. Open Windows Security > Virus & threat protection and run a Full scan.
2. If anything is found, remove it and restart.
3. Open Command Prompt as administrator and run `sfc /scannow`.
4. After the scan completes, restart once more.
5. Retry the update — with the hooks gone, the sharing violation should be gone too.

## Closing

On Windows 10, sharing violations during updates are almost always a third-party program refusing to let go of system files. The discipline is simple: restart first, suspect the antivirus second, and use a clean boot to prove it. Updates need a quiet moment with exclusive file access — give them that moment and 0x80070020 disappears.
