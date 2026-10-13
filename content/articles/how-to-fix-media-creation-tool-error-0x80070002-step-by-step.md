---
title: "Step-by-Step Fix for Media Creation Tool Error 0x80070002"
slug: how-to-fix-media-creation-tool-error-0x80070002-step-by-step
date: 2026-09-23
categories: ["windows-update"]
tags: ["media creation tool", "0x80070002", "windows 11", "bootable usb", "iso download"]
description: "A complete step-by-step repair for Media Creation Tool error 0x80070002: fresh download, temp cleanup, permissions, space checks, and the ISO fallback."
thumbnail: "/images/thumbs/how-to-fix-media-creation-tool-error-0x80070002-step-by-step.webp"
faqs:
  - q: "What is the fastest fix for error 0x80070002 in the Media Creation Tool?"
    a: "Delete the tool, clear the %temp% folder, download a fresh copy of the tool, and run it as administrator. That four-step sequence resolves the majority of 0x80070002 failures because the error is usually stale temp files or a damaged tool executable. If it still fails after that, move on to disabling security software and checking disk space."
  - q: "Does error 0x80070002 mean my Windows installation is broken?"
    a: "Not necessarily. The error points to missing or unreadable files in the tool's own download process, which is usually a temp-file or permissions problem, not system damage. However, if the tool shares its download machinery with a broken Windows Update stack, repairing those components helps. Run SFC and DISM if you suspect broader system corruption."
  - q: "Why does the tool fail at the same percentage every time?"
    a: "A consistent failure point means the tool is hitting the same corrupted or blocked file every run. Stale partial downloads in the temp cache are the usual cause — the tool resumes from the bad data and fails at the same spot. Clearing %temp% and the $Windows.~WS / $Windows.~BT folders forces a completely fresh download that does not touch the bad files."
  - q: "Is downloading the ISO directly as good as using the tool?"
    a: "Yes, for creating installation media. The ISO contains the same Windows image, and writing it with Rufus produces a fully functional bootable USB. The Media Creation Tool is just a convenience wrapper. Downloading the ISO from the official Microsoft software download page is safe, and many technicians prefer it when the tool misbehaves."
---

You need a Windows 11 USB stick — for a repair, a reinstall, or a fresh start on a misbehaving machine — and the Media Creation Tool keeps dying with error 0x80070002. The code translates to "file not found," which tells you the tool expected a file in its download process and could not read it. It does not tell you which file, or why, which is why the error feels so unhelpful.
The good news is that the causes cluster tightly. In order of frequency: leftover temporary files from an interrupted run, a damaged tool download, missing administrator rights, blocked writes from security software, and insufficient disk space. Each has a direct fix, and the sequence below walks through them from most to least likely, so the average user is done by step three.
Follow the steps in order and test the tool after each fix — there is no need to do everything if an early step resolves it. Begin with a fresh tool from the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11). If the machine you are repairing cannot boot at all, the [black-screen-after-update fix](/articles/windows-11-black-screen-after-update-fix/) may be the companion guide you need, and for update-stack problems the [troubleshooter guide](/articles/how-to-fix-windows-update-with-troubleshooter-on-windows-11/) covers the built-in repair path.

## Why this happens

- **Stale temporary files from an interrupted run.** Partial downloads sit in the temp cache, and the tool fails when it tries to resume from them.
- **A corrupted tool executable.** The MediaCreationTool.exe download itself can be incomplete or damaged.
- **Missing administrator privileges.** Without elevation, the tool cannot write to the protected folders it needs.
- **Security software blocking writes.** Antivirus or endpoint protection quarantines the tool's large temp files mid-write.
- **Not enough free disk space.** The tool stages gigabytes on the system drive before writing to USB.
- **Broken Windows Update components.** The tool shares download machinery with Windows Update; if that stack is damaged, the tool fails too.
- **A failing USB drive.** Bad flash memory produces read errors that surface as this exact code.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Get a fresh tool and run it elevated

Rule out the two simplest causes first. A damaged executable and missing admin rights account for a large share of these failures.

1. Delete the existing MediaCreationTool.exe from your Downloads folder.
2. Download a fresh copy from the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Right-click the file and select Run as administrator.
4. Try the media creation again and note exactly where it fails, if it still does.

### Fix 2: Clear all temporary files

This is the highest-yield fix for 0x80070002. Interrupted runs leave partial files that poison every subsequent attempt until they are removed.

1. Press Win+R, type `%temp%`, press Enter, and delete everything in the folder, skipping in-use files.
2. Delete the contents of `C:\$Windows.~WS` and `C:\$Windows.~BT` if those folders exist.
3. Run Disk Cleanup with system files selected and remove temporary files and delivery optimization files.
4. Restart the computer, then run the tool as administrator again.

### Fix 3: Disable security software temporarily

Real-time protection sometimes flags the tool's multi-gigabyte temp files. A brief disable during the download rules this out cleanly.

1. Temporarily disable your third-party antivirus real-time protection.
2. If you run additional endpoint or security suites, disable those too for the duration.
3. Keep Windows Defender active as your baseline protection.
4. Run the tool as administrator; re-enable everything afterward regardless of the outcome.

### Fix 4: Verify free space on both drives

The tool needs room in two places: the system drive for staging and the USB for the final image. Check both before assuming a deeper problem.

1. Confirm at least 20 GB free on the C: drive via Settings > System > Storage.
2. Use a USB drive of 8 GB or larger, and format it as FAT32 first.
3. Plug the USB directly into the computer, avoiding hubs and docks.
4. Retry the tool with both space requirements satisfied.

### Fix 5: Repair the Windows Update components

Because the tool reuses the Windows Update download engine, corrupted update components cause identical failures. Resetting them helps both.

1. In an elevated Command Prompt, run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, and `net stop msiserver`.
2. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands and reboot.
4. Run the Media Creation Tool as administrator again.

### Fix 6: Run SFC and DISM for system corruption

If the update stack reset did not help, check for broader system file damage that could be breaking the download pipeline.

1. Open an elevated Command Prompt and run `sfc /scannow` to completion.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`, allowing 15 to 30 minutes.
3. Restart the computer after both tools finish.
4. Attempt the media creation once more.

### Fix 7: Fall back to the direct ISO download

When the tool itself is the problem, go around it. The official ISO plus a USB writer produces identical bootable media.

1. On the Windows 11 download page, select the ISO download option.
2. Download Rufus from its official website and write the ISO to your USB drive.
3. Verify the USB boots on the target machine before you depend on it.
4. Check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) later if you need specific driver or update packages for the install.

## Closing

Error 0x80070002 looks cryptic, but it is one of the more mechanical failures in Windows tooling: clear the temp files, get a fresh elevated tool, confirm your space, and quiet the security software. Work the list in order, test after each step, and use the direct ISO fallback without shame if the tool keeps fighting you — the bootable USB is the goal, not the tool.
