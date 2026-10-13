---
title: "Fix Windows Update Error 0x80070020 on Windows 11 (File in Use)"
slug: how-to-fix-windows-update-error-0x80070020-on-windows-11
date: 2026-09-15
categories: ["windows-update"]
tags: ["windows update", "0x80070020", "file in use", "antivirus", "windows 11"]
description: "Windows 11 error 0x80070020 means another program locked files the update needs. Identify the conflict, free the files, and install your updates."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070020-on-windows-11.webp"
faqs:
  - q: "What does error 0x80070020 mean?"
    a: "On Windows 11, 0x80070020 is ERROR_SHARING_VIOLATION: Windows Update tried to touch a file another process has locked. The usual lockers are third-party antivirus real-time scanning, a second installer running alongside, or stale handles from an interrupted update. Restarting, pausing the antivirus, or clean-booting releases the locks."
  - q: "Can antivirus really block Windows Update?"
    a: "Yes — it is the leading cause of this error. Real-time scanning opens files the moment they are accessed, keeping handles on the executables Windows Update must replace. Pausing the third-party suite for one update attempt is the standard test; if the update then succeeds, add servicing exclusions in the antivirus settings instead of disabling it permanently."
  - q: "Why does Restart work but Shut down does not?"
    a: "With Fast Startup enabled, Shut down hibernates the kernel session, preserving driver and service state — including some file locks. Restart performs a full kernel reinitialization, genuinely releasing every lock. For any sharing-violation error, always pick Restart when a reboot is called for."
  - q: "How do I find which program is locking the file?"
    a: "Check Task Manager for installer, setup, updater, or antivirus processes showing activity during the update. For precision, Microsoft's free Process Explorer reveals exactly which process holds a handle on a given file. In practice, clean-booting is faster than detective work: if the update succeeds with third-party services disabled, the culprit is among them."
---
Error 0x80070020 is a sharing violation: Windows Update tried to replace a file that another process is holding open, and Windows refused to rip it away. The engine did nothing wrong — some other program has its hands on those files. On Windows 11 laptops the prime suspect is third-party antivirus real-time scanning, with a second background installer close behind.

Because this is about timing and locks rather than damage, the remedies are about sequencing: quiet the machine down, temporarily remove the competing program from the picture, and grant the update exclusive access to the files it needs.

If the twin error appears on your other OS, the [Windows 10 guide](/articles/how-to-fix-windows-update-error-0x80070020-on-windows-10/) handles it there, and when the competing installer is another update stuck mid-flight, the [companion guide for 0x80070652](/articles/how-to-fix-windows-update-error-0x80070652-on-windows-11/) covers that scenario. Begin with the simplest remedy — a restart.

## Why this happens

- **Antivirus real-time scanning keeps files open:** third-party suites scan files the instant they are touched, holding handles on precisely the executables and libraries Windows Update must replace — the number-one cause of 0x80070020.
- **Another installer runs concurrently:** a program's own updater, a Store app update, or a second Windows Installer session can lock files the update engine needs, and one side loses with this error.
- **A previous attempt left stale locks:** an interrupted update can leave processes or pending file operations holding references that never release until restart, so every retry slams into the same wall.
- **Background utilities hook system files:** optimizers, overlay tools, and some gaming utilities hook into or monitor system components, keeping those files open and unreplaceable during servicing.
- **Search indexing holds files open:** the indexer occasionally keeps handles on files being serviced, especially right after boot while clearing a backlog.
- **Malware guards its own files:** malicious software sometimes locks the system files it infected to resist removal, and an update trying to replace them trips the sharing violation.
- **The servicing queue fights itself:** corrupted pending operations can make the engine fight itself for file access, producing a sharing violation with no obvious third-party culprit.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart and retry before anything else

A restart is a legitimate first remedy for this sharing violation, not a platitude: it frees up every file lock, stops competing installers, and sweeps away stale handles from interrupted attempts. Most 0x80070020 cases never survive a clean reboot.

1. Close open programs and save your work.
2. Choose Start > Power > Restart (not Shut down).
3. After signing back in, give startup activity two minutes to calm.
4. Open Settings > Windows Update and press Check for updates.
5. If the error has vanished, you are done — the lock was transient.

### Fix 2: Briefly disable third-party antivirus

When the error survives a restart, antivirus becomes the prime suspect: real-time scanning locks files at the precise moment the engine needs to replace them. Pausing protection for one update attempt is a safe, standard diagnostic — and a success identifies the culprit with certainty.

1. Open your third-party antivirus and switch off real-time protection and any behavior shield.
2. Leave Windows Security's own real-time protection switched on as your safety net.
3. Run the update via Settings > Windows Update while the third-party suite is paused.
4. On success, re-enable the suite, then add the Windows servicing folders to its exclusions per the vendor's documentation.
5. On failure, re-enable protection and move on — the AV is innocent.

### Fix 3: End wedged installer processes

A frozen msiexec or a hung setup from another program can grip locks indefinitely while showing no window. Task Manager exposes these ghosts, and ending them frees the files instantly — a stuck installer was never going to finish anyway.

1. Hit Ctrl + Shift + Esc to open Task Manager.
2. On the Processes tab, look for Setup, Installer, or msiexec entries and end them.
3. On the Details tab, end any remaining `msiexec.exe` processes.
4. Also end obvious third-party updaters (OEM update tools, game launchers).
5. Attempt the update again in Settings > Windows Update.

### Fix 4: Clean-boot the machine, then update

A clean boot starts Windows with Microsoft services only, silencing every third-party file-locker at once — antivirus filters, utilities, updaters, overlays. If the update installs cleanly here, the conflict is certainly third-party, and you can bisect to find it.

1. Press Win + R, enter `msconfig`, and hit Enter.
2. On the Services tab, tick Hide all Microsoft services, then choose Disable all.
3. In Task Manager's Startup tab, switch off all startup items.
4. Restart, run the update via Settings > Windows Update, then undo the msconfig changes and reboot again.
5. For background on isolating the culprit, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the clean-boot procedure.

### Fix 5: Restart the Windows Update services

Sometimes the servicing stack holds the conflicting state itself — a previous attempt left the engine jammed mid-operation. Restarting the Windows Update, BITS, and cryptographic services resets that internal state and drops every lock the engine was holding against itself.

1. Start an elevated Command Prompt.
2. Execute `net stop wuauserv` and `net stop bits`.
3. Wait ten seconds, then execute `net start bits` and `net start wuauserv`.
4. Restart the cryptographic service too: `net stop cryptsvc` then `net start cryptsvc`.
5. Check for updates once more.

### Fix 6: Scan for malware and mend system files

If no legitimate program explains the locks, suspect the illegitimate kind: malware latched onto system files will fight updates that try to replace them. A full scan plus SFC addresses both the infection and any damage it caused.

1. Open Windows Security > Virus & threat protection and launch a Full scan.
2. Remove anything found and restart.
3. Open an administrator Command Prompt and run `sfc /scannow`.
4. Once the scan completes, restart one more time.
5. Attempt the update again — with the hooks removed, the sharing violation should vanish too.

## Closing

Error 0x80070020 is a traffic jam rather than a breakdown: two programs want the same files, and Windows forces them to alternate. A restart clears most jams; a clean boot with antivirus paused clears nearly all the remainder. Once you know which program was holding the lock, configure its exclusions properly and this error stops revisiting your Windows 11 laptop.
