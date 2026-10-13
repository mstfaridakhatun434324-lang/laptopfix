---
title: "How to Fix Media Creation Tool Error 0x80070002 on a Laptop"
slug: "how-to-fix-media-creation-tool-error-0x80070002-on-laptop"
date: 2026-09-03
categories: ["windows-update"]
tags: ["media creation tool", "0x80070002", "windows 11", "iso", "usb"]
description: "Media Creation Tool failing with 0x80070002 on your laptop? Fix the missing-file error and create your Windows 11 USB successfully."
thumbnail: "/images/thumbs/how-to-fix-media-creation-tool-error-0x80070002-on-laptop.webp"
faqs:
  - q: "What does 0x80070002 mean in the Media Creation Tool?"
    a: >
      ERROR_FILE_NOT_FOUND: the tool expected a file — part of its
      download, staging set, or working files — and could not find it. The
      cause is usually an interrupted download, antivirus quarantine, or
      running the tool from an unsuitable location.
  - q: "How much free space does the tool need?"
    a: >
      At least 8 GB on the USB drive, plus roughly 8–16 GB of free space
      on C: for staging — the tool downloads and assembles files locally
      even when writing to USB. Aim for 20 GB free to be safe.
  - q: "Can I run the tool from an external drive?"
    a: >
      It is not recommended. Run it from a simple local folder like
      C:\\Temp with administrator rights. Network drives, synced cloud
      folders, and paths with special characters are known to trigger
      0x80070002. The tool creates and deletes staging files rapidly
      during the build, and any latency or locking from a network or
      synced location breaks its file tracking. A short local path with
      full admin rights is the reliable setup.
  - q: "Is the ISO download as good as the tool’s USB?"
    a: >
      Yes — identical Windows image. Writing the ISO to USB with Rufus (or
      mounting it for an in-place upgrade) gives you exactly what the
      Media Creation Tool would have produced. The tool itself just
      downloads this same ISO and writes it to the drive; doing those two
      steps manually skips the tool’s fragile staging logic. Verify the
      ISO download completes fully, and the result is byte-for-byte
      equivalent.
---

Error 0x80070002 (ERROR_FILE_NOT_FOUND) in the Media Creation Tool means the tool went looking for a file it expected — a download manifest, a staging file, or a component of its own working set — and could not find it. The tool downloads Windows, stages it locally, and builds your USB or ISO; a missing piece anywhere in that chain aborts the whole job with this code.

On laptops the usual causes are mundane: the tool’s download was interrupted and its resume logic lost track, antivirus quarantined one of its staging files, the download folder ran out of space, or the tool itself was launched from a location (like a network drive or a path with special characters) where it cannot manage its files properly. It can also strike when Windows’ own update components — which the tool reuses — are in a bad state.

The fixes run from the tool’s own hygiene (fresh download, right location, enough space) through the system-level repairs, ending with the direct ISO download that skips the tool entirely. If you are dealing with a related symptom instead, see [the 0x80070017 CRC error on Dell](/articles/how-to-fix-windows-update-error-0x80070017-on-dell-laptop/) and [the 0xC1900101 feature-update failure on Dell](/articles/how-to-fix-windows-update-error-0xc1900101-on-dell-laptop/).

The Media Creation Tool does three jobs — download Windows, stage the files locally, and build your USB or ISO — and 0x80070002 means it lost track of a file somewhere in that chain. On laptops the causes are almost always mundane: an interrupted download it cannot resume cleanly, antivirus quarantining a staging file, too little working space, or the tool launched from a location where it cannot manage its files. The fixes run from tool hygiene through system repair to the direct ISO download that skips the tool entirely.

## Why this happens

- **Interrupted tool download** partial staging files confuse the tool’s resume logic.

- **Antivirus quarantining staging files** security software removes files the tool just downloaded.

- **Insufficient disk space for staging** the tool needs several GB of working space.

- **Tool run from a bad location** network drives or odd paths break its file handling.

- **Corrupt Windows Update components** the tool reuses the update stack; damage carries over.

- **Corrupt tool download itself** the MediaCreationTool.exe you ran is damaged.

- **USB drive problems** a failing flash drive breaks the write phase.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Re-download the Media Creation Tool fresh

Eliminates a corrupt tool binary as the cause. Always download the tool fresh from Microsoft rather than reusing an old copy; the tool itself is updated periodically and old versions cause odd failures.

1. Delete the MediaCreationTool.exe you have.

2. Download a fresh copy from [Microsoft’s Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

3. Save it to a simple local path like C:\Temp (create the folder).

4. Right-click it and choose ‘Run as administrator’.

### Fix 2: Free staging space and use a local folder

Gives the tool the room and location it needs. The tool stages files on C: even when building a USB, so free space on the system drive matters more than space on the flash drive at this stage.

1. Ensure at least 16–20 GB free on C: (the tool stages there even for USB creation).

2. Run Disk Cleanup if needed.

3. Do not run the tool from a USB stick, network drive, or synced OneDrive folder.

### Fix 3: Temporarily disable third-party antivirus

Stops quarantine interference with staging files. Re-enable protection the moment the build finishes — the window of reduced protection should last minutes, not hours.

1. Disable real-time protection temporarily.

2. Run the Media Creation Tool immediately.

3. Re-enable protection when the USB/ISO is built.

### Fix 4: Clear the Windows Update cache

The tool shares the update stack — clean it. The Media Creation Tool shares the update stack’s download machinery, so a corrupted cache can break the tool even when Windows Update itself seems fine.

1. Elevated prompt: net stop wuauserv, net stop bits.

2. Clear C:\Windows\SoftwareDistribution\Download.

3. net start wuauserv, net start bits.

4. Re-run the Media Creation Tool.

### Fix 5: Run the update troubleshooter and DISM

Repairs the shared servicing components. Run these in the order given: the troubleshooter’s quick resets first, then DISM’s deeper repair only if the tool still fails afterward.

1. Run the Windows Update troubleshooter (Settings > System > Troubleshoot).

2. Elevated prompt: DISM /Online /Cleanup-Image /RestoreHealth, then sfc /scannow.

3. Restart and re-run the tool.

### Fix 6: Try a different USB drive and port

Rules out the write target as the failure point. Avoid USB hubs for the creation step; a direct port gives the most reliable power and data connection during the long write phase.

1. Use a different USB flash drive, at least 8 GB.

2. Plug it directly into the laptop (no hub); try a USB 2.0 port if 3.0 fails.

3. Re-run the tool targeting the new drive.

### Fix 7: Skip the tool: download the ISO directly

The reliable bypass when the tool will not cooperate. This two-step method also lets you verify the ISO’s size before writing, catching download corruption the tool would only discover mid-build.

1. On [Microsoft’s download page](https://www.microsoft.com/en-us/software-download/windows11), choose ‘Download Windows 11 Disk Image (ISO)’.

2. Download the ISO in your browser.

3. Use Rufus (or mount the ISO) to create the bootable USB.

4. This achieves the identical end result without the Media Creation Tool.

## Closing

Error 0x80070002 is the Media Creation Tool losing track of its own files — annoying, but almost always fixed by a fresh tool, a clean local staging area, and antivirus kept at bay during the build. And when the tool simply will not cooperate, the direct ISO download gets you the same USB by a different road. For official guidance, see [Microsoft’s Windows update support hub](https://support.microsoft.com/en-us/windows).
