---
title: "How to Fix Windows Update Error 0x80070020 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80070020-in-windows-11-24h2
date: 2026-10-08
categories: ["windows-update"]
tags: ["windows update", "0x80070020", "error code", "windows 11", "file lock"]
description: "Error 0x80070020 means another process is holding files the update needs. Find the lock-holder and free the files with this guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070020-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80070020 mean?"
    a: "ERROR_SHARING_VIOLATION: the update cannot replace files because another process is holding them open. The message spells it out — the process cannot access the file because it is being used by another process. It is a tug-of-war over files, and the update loses rather than risk a half-written system file."
  - q: "What usually holds the files on a laptop?"
    a: "Third-party antivirus real-time shields are the single most common lock-holder, followed by cloud sync tools like OneDrive gripping DLLs, and previous update installers that never exited cleanly. Heavy desktop applications with files open during the update window can also trigger it."
  - q: "Is a clean boot safe to perform?"
    a: "Yes. A clean boot starts Windows with only Microsoft services and no third-party startup items — nothing is uninstalled or deleted. It is a diagnostic state: if the update succeeds there, a third-party program was the lock-holder. You re-enable everything afterward through the same dialogs."
  - q: "Should I disable my antivirus to install updates?"
    a: "A brief, controlled pause of the real-time shield during the install window is the standard workaround — with protection restored immediately after. Never browse the web with protection off. For a permanent fix that avoids the pause entirely, add the update cache folders to the antivirus exclusions."
---

Two cooks, one knife. That is 0x80070020: Windows Update tried to replace a file, found another process gripping it, and backed off rather than risk corruption. It is one of the few update errors that tells you exactly what went wrong — something else is using the file — even if it does not name the culprit. The error message is refreshingly direct — Windows reports that "the process" cannot "access the file" since "another process" already has it open — naming the whole problem: a sharing violation, two parties wrestling over files.

Laptop lock-holders are usually third-party antivirus shields, cloud sync tools clutching DLLs like OneDrive does, or an earlier update installer that never quit properly. Each culprit wants a different remedy, so the first fix below is investigation: sixty seconds of detective work reveals antivirus, a stuck installer, or something else entirely. Skipping this step is the classic mistake — people disable their antivirus, reboot three times, and only then discover OneDrive was the holder all along.

Every sharing violation has one specific holder, and the holder is usually something mundane rather than sinister. Find it, free the files, and the update proceeds. The detective work in Fix 1 is the highest-value two minutes in this entire guide — everything after it depends on knowing the answer.

## Why this happens

- **Antivirus shield clutching system files.** The scanner keeps files open for examination precisely when the installer demands exclusive access.
- **Sync clients keep files open.** OneDrive, Dropbox, and their kin can lock files the update intends to replace.
- **An installer that never quit.** An installer left running holds its file locks without end.
- **Third-party services start with Windows.** Background optimizers and utilities can grab files at boot.
- **Heavy applications were left running.** Open programs with DLLs loaded block the files the update targets.
- **The pending-rename queue is jammed.** Phantom rename operations from old updates act like permanent locks.
- **Disk errors confuse the lock tracking.** Filesystem damage can make Windows misreport which files are in use.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify what is holding the files

A minute of detective work here prevents an afternoon of wrong fixes. The three checks below take almost no time and point directly at the responsible program.

1. Identify the failed update under Settings > Windows Update > Update history — driver updates suffer locks most often. Our [update history guide](/articles/how-to-check-windows-update-history-on-windows-11/) helps interpret the entries.
2. Launch Task Manager (Ctrl + Shift + Esc) and hunt for duplicated or frozen `msiexec.exe`, `setup.exe`, or installer processes.
3. Look in the notification area for third-party antivirus, sync utilities, and optimizers running behind the scenes.

### Fix 2: Clean-boot to release third-party locks

Booting clean starts Windows with Microsoft services alone, cutting out the third-party programs behind most lock failures. It is the fastest way to answer the binary question: is the holder something Windows ships with, or something you installed?

1. Press Win + R, type `msconfig`, and open the System Configuration dialog.
2. On the Services tab, select Hide all Microsoft services, then press Disable all.
3. On the Startup tab, press Open Task Manager and switch off every startup item.
4. Reboot the machine, open Windows Update, and let the update install.
5. Turn the services and startup items back on afterward through the same dialogs.

### Fix 3: Pause real-time antivirus for the install window

Antivirus shields top the list of lock-holders. Briefly pausing protection for the install window — restoring it right after — is the accepted workaround.

1. For third-party antivirus, pause its real-time shield from the system-tray menu.
2. In Windows Security, the same lives under Virus & threat protection > Manage settings.
3. Launch the Windows Update install at once while the shield stays down.
4. Restore protection the instant the install finishes — never browse while it is off.

### Fix 4: End stuck installers and clear the rename queue

An earlier update installer that never quit holds its locks indefinitely. Terminating it and emptying the pending-rename queue eliminates phantom locks that outlive reboots.

1. Under Task Manager's Details tab, terminate any `msiexec.exe` processes — but only when no installation is visibly in progress.
2. In an administrator Command Prompt, run `sfc /scannow` afterward to verify that system file integrity survived the ordeal.
3. Retry the update and confirm the sharing violation is gone.

### Fix 5: Give the troubleshooter a chance

The troubleshooter detects file-lock patterns and stuck installer states, applying automatic repairs. It is a quick, safe step that occasionally resolves the code without any manual intervention — always worth trying before deeper surgery.

1. Summon Settings and advance to System > Troubleshoot > Other troubleshooters.
2. Free the Windows Update entry and shadow its prompts.
3. Reboot the PC and assay the update again.

### Fix 6: Install the KB yourself from the Catalog

Installing by hand puts you in charge of timing — shut everything, pause the shield, install on your schedule. Every cumulative release waits on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/). Do the install with no other programs running, and the sharing violation has nothing left to collide with.

1. Find the failed KB entry in Update history and search the Catalog for it.
2. Download the x64 Windows 11 package.
3. Close all applications, pause the antivirus shield, run the `.msu` file, and re-enable protection immediately after.

## Closing

File locks bow to identification: name the holder, free the files, and the installer stops complaining. Going forward, installing updates with heavy applications closed and the antivirus exclusion in place prevents most recurrences. If a different code appears after the lock clears, the [24H2 update-error guide](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) decodes it — locks often mask a second, unrelated problem underneath. The clean-boot procedure is documented in [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).
