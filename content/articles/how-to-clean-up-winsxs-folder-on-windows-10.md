---
title: "How to Clean Up the WinSxS Folder on Windows 10 Safely"
slug: "how-to-clean-up-winsxs-folder-on-windows-10"
date: "2026-09-19"
categories: ["performance"]
tags: ["winsxs folder", "component store", "disk cleanup", "windows 10"]
description: "WinSxS folder eating 10+ GB? Clean the Windows component store safely with DISM, never by deleting files manually."
thumbnail: "/images/thumbs/how-to-clean-up-winsxs-folder-on-windows-10.webp"
faqs:
  - q: "What is the WinSxS folder?"
    a: "WinSxS, the Windows side-by-side component store, holds every version of every system component Windows might need: for installing updates, repairing files, enabling features, and rolling back. Much of its reported size is hard links, meaning the same file content counted multiple times, so the folder looks bigger than the disk space it truly consumes. It is essential to Windows servicing and must never be deleted by hand."
  - q: "Is it safe to delete the WinSxS folder?"
    a: "No, never. Deleting WinSxS or files inside it will break Windows Update, SFC repairs, and feature installation, and can render the system unbootable. The only safe cleanup is through official tools: Disk Cleanup with Windows Update Cleanup checked, or the DISM commands with StartComponentCleanup. These remove only superseded components Windows no longer needs."
  - q: "How big should WinSxS normally be?"
    a: "On a healthy Windows 10 system, 5 to 10 GB of actual disk usage is normal, though Explorer may report 12 to 15 GB because of hard-link double counting. After years of updates without cleanup, real usage can exceed 15 GB. Running the component cleanup typically reclaims several gigabytes on systems that have never had it done."
  - q: "What does DISM StartComponentCleanup do?"
    a: "It removes superseded component versions that updates have replaced, keeping only what the current system needs plus a safety margin. The ResetBase variant goes further, removing the ability to uninstall updates, which frees maximum space but is irreversible. Run the standard cleanup first; use ResetBase only when disk space is critical and the system is stable."
---

Every disk-space investigation on Windows eventually leads to the same suspect: C:\Windows\WinSxS, the component store, cheerfully reporting 12 or 15 gigabytes. It looks like the obvious thing to delete, and the internet is full of people asking whether they can. The short answer is no, you cannot delete it, but you can shrink it considerably with the right tools.

WinSxS is Windows' parts warehouse. Every update, every optional feature, every repair operation draws from it. Its reported size is also misleading: much of it consists of hard links, where one physical file is counted multiple times by Explorer. The real disk cost is smaller than it looks, but on neglected systems it still grows large enough to matter.

This guide shows the two supported cleanup methods, Disk Cleanup and the DISM component cleanup commands, how much space to expect back, and the one command you should think twice about before running.

## Why this happens

- **Years of superseded updates:** Each cumulative update leaves its replaced components in the store until cleanup runs.
- **Hard-link size illusion:** Explorer counts hard-linked files multiple times, making the folder look far bigger than its true cost.
- **Never-run component cleanup:** Windows 10 does not aggressively self-clean the store; manual cleanup is often years overdue.
- **Staged optional features:** Features like language packs and .NET versions keep their payloads in the store.
- **Update backups retained:** Superseded update packages are kept so updates can be uninstalled if they cause problems.
- **Driver packages accumulated:** Old driver versions staged by updates linger in the component store.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Analyze the real WinSxS size first

Before cleaning, get the true number. DISM reports actual disk usage, cutting through the hard-link illusion.

1. Open Command Prompt as administrator.
2. Type Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore and press Enter.
3. Wait for the analysis to complete.
4. Read the actual size versus the Explorer-reported size.
5. If cleanup is recommended, proceed with the steps below.

### Fix 2: Clean up with Disk Cleanup

The graphical method handles the common case and is the safest starting point.

1. Press Win+R, type cleanmgr, and press Enter.
2. Select the C drive, then click Clean up system files.
3. Check Windows Update Cleanup in the list.
4. Click OK and confirm the deletion.
5. This removes superseded update backups from the component store.

### Fix 3: Run the DISM component cleanup

The command-line cleanup goes deeper than Disk Cleanup, removing superseded components directly from the store.

1. Open Command Prompt as administrator.
2. Type Dism.exe /Online /Cleanup-Image /StartComponentCleanup and press Enter.
3. Let it run; it can take 10 to 30 minutes on a neglected system.
4. Do not interrupt it or shut down while it works.
5. Re-run the AnalyzeComponentStore command to see the new size.

### Fix 4: Consider ResetBase only when desperate

ResetBase removes the ability to uninstall updates, freeing maximum space. It is irreversible, so weigh it carefully.

1. Confirm the system is stable with all current updates for at least two weeks.
2. Open Command Prompt as administrator.
3. Type Dism.exe /Online /Cleanup-Image /StartComponentCleanup /ResetBase and press Enter.
4. Wait for completion without interrupting.
5. Understand that installed updates can no longer be uninstalled afterward.

### Fix 5: Schedule automatic component cleanup

Windows includes a scheduled task for this, but verifying it runs prevents the store from ballooning again.

1. Press Win+R, type taskschd.msc, and press Enter.
2. Navigate to Task Scheduler Library, Microsoft, Windows, Servicing.
3. Confirm StartComponentCleanup is present and enabled.
4. Check its history to see when it last ran successfully.
5. Leave it enabled; it handles maintenance quietly going forward.

### Fix 6: Free space around WinSxS too

WinSxS is rarely the only hog. A broader cleanup multiplies the recovered space.

1. Run Disk Cleanup with Temporary files and Delivery Optimization Files checked.
2. Cap System Protection as described in our [low disk space guide](/articles/how-to-fix-low-disk-space-on-c-drive-reddit/).
3. Uninstall unused programs under Settings, Apps.
4. Move large user folders to a second drive if available.
5. Re-measure free space after the full pass.

### Fix 7: Remove unused optional features

Optional features keep their payloads in the component store. Removing features you never enabled as capabilities still trims staged payloads.

1. Open Settings, Apps, Optional features.
2. Remove features like Internet Explorer mode helpers or legacy media components you never use.
3. Open Control Panel, Programs, Turn Windows features on or off.
4. Uncheck legacy components such as old .NET versions if nothing needs them.
5. Run the DISM component cleanup again to purge the freed payloads.

### Fix 8: Measure before and after to prove the savings

Documenting the numbers keeps you honest about what worked and gives you a baseline for next year.

1. Run Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore and note the actual size.
2. Perform the cleanup steps from the fixes above.
3. Re-run the analysis command and record the new size.
4. Typical savings on a neglected system run 3 to 8 GB.
5. Repeat the analysis yearly as part of routine maintenance.

### Fix 9: Remove unused optional features

Optional features keep their payloads in the component store. Removing features you never enabled as capabilities still trims staged payloads.

1. Open Settings, Apps, Optional features.
2. Remove features like Internet Explorer mode helpers or legacy media components you never use.
3. Open Control Panel, Programs, Turn Windows features on or off.
4. Uncheck legacy components such as old .NET versions if nothing needs them.
5. Run the DISM component cleanup again to purge the freed payloads.

### Fix 10: Measure before and after to prove the savings

Documenting the numbers keeps you honest about what worked and gives you a baseline for next year.

1. Run Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore and note the actual size.
2. Perform the cleanup steps from the fixes above.
3. Re-run the analysis command and record the new size.
4. Typical savings on a neglected system run 3 to 8 GB.
5. Repeat the analysis yearly as part of routine maintenance.

## Closing

WinSxS looks scary but responds well to the official tools: analyze first so you know the real number, clean with DISM, and reserve ResetBase for genuine emergencies. Never delete the folder by hand no matter what a forum post claims; the servicing stack depends on it. Pair the component cleanup with general disk hygiene and the C drive stays healthy for years. Our companion guide to [reclaiming C drive space](/articles/how-to-fix-low-disk-space-on-c-drive-reddit/) covers everything around the component store. Keep the scheduled component cleanup enabled and you will rarely need to think about WinSxS again. Microsoft documents the component store in its [Windows support hub](https://support.microsoft.com/en-us/windows). Keep the scheduled component cleanup enabled and you will rarely need to think about WinSxS again. Microsoft documents the component store in its [Windows support hub](https://support.microsoft.com/en-us/windows). For the broader picture beyond the component store, [this disk-space checklist](/articles/best-way-to-fix-low-disk-space-on-c-drive/) covers the other big wins.
