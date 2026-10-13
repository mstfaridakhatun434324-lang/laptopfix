---
title: "Best Way to Fix Media Creation Tool Error 0x80070002"
slug: best-way-to-fix-media-creation-tool-error-0x80070002
date: 2026-10-04
categories: ["windows-update"]
tags: ["media creation tool error 0x80070002", "mct error fix", "windows 11 iso download failed", "0x80070002 media creation"]
description: "Media Creation Tool failing with 0x80070002? The tool can't find files it needs. Fix permissions, temp files, and settings to build your media."
thumbnail: "/images/thumbs/best-way-to-fix-media-creation-tool-error-0x80070002.webp"
faqs:
  - q: "What does Media Creation Tool error 0x80070002 mean?"
    a: "It means ERROR_FILE_NOT_FOUND: the tool expected a file or folder that is not there. Usually its temporary working files were deleted, blocked, or never created properly, so the download or media-creation phase aborts with this code."
  - q: "Why does the Media Creation Tool fail but the ISO download work?"
    a: "They use different machinery. The tool downloads an ESD and converts it locally, creating large temp files along the way, while a direct ISO download is a single file transfer. Temp-folder, permission, and antivirus issues break the tool's workflow without affecting a plain download."
  - q: "How much free space does the Media Creation Tool need?"
    a: "The tool needs several gigabytes of temp space plus the target: at least 8 GB free for the USB drive itself, and a comfortable margin on the system drive for temporary files. Cramped drives are a common trigger for 0x80070002."
  - q: "Can I use a different computer to create the media?"
    a: "Yes, and it is a fine workaround. The Media Creation Tool runs on any Windows 10 or 11 PC; create the USB there and use it on the laptop that needs it. Just match the language and edition to the target machine."
---

Error 0x80070002 in the Media Creation Tool is the tool losing track of its own files. The code means file not found: somewhere in its download-and-convert workflow, the tool reaches for a temporary file or folder that is not where it expected, and the whole job aborts.

The triggers are almost embarrassingly mundane. Temp files cleaned mid-run by a disk utility. The tool launched from a network location or a path with special characters. Antivirus quarantining the downloaded ESD. A USB drive the tool cannot quite work with. None of them are serious, and all of them are fixable.

The best-practice sequence below gives the tool exactly the clean, simple environment it wants: local admin execution, healthy temp space, and no interference.

The Media Creation Tool is a small program doing a big job: downloading gigabytes, converting formats, and writing bootable media, all while juggling temporary files. Error 0x80070002 means it lost track of one of those files — a bookkeeping failure, not a system failure. Give it the simple, clean workspace it expects and it finishes the job.

## Why this happens

- **Temp files deleted mid-run.** Disk cleaners removing the tool's working files while it runs.

- **Tool launched from an odd location.** Running from a network drive, a synced folder, or a path with special characters breaks its file expectations.

- **Antivirus blocking the ESD.** Security software quarantining or locking the downloaded image files.

- **Insufficient temp or USB space.** The tool needs gigabytes of working room plus an 8 GB target drive.

- **Corrupt previous download state.** Leftover $Windows.~BT and temp data from a failed run poisoning the retry.

- **Language or edition mismatch.** Selecting options that do not match the running system confusing the tool's file layout.

- **Unstable internet connection.** Dropped connections corrupting the ESD download the tool then cannot find intact.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Run the tool as administrator from the Desktop

The two simplest variables, privileges and location, fixed in one move. The Desktop of the system drive is the path the tool expects. Avoid launching the tool from the Downloads folder inside a cloud-synced profile; OneDrive's file-on-demand placeholders have confused the tool's file checks in the past.

1. Download a fresh MediaCreationTool.exe.
2. Move it to your Desktop, right-click it, and choose Run as administrator.
3. Accept the UAC prompt and retry the media creation.

### Fix 2: Fix 2: Clear the tool's temp state

Leftover state from failed runs is a prime 0x80070002 trigger. Clearing the temp folders and the BT staging folders gives the tool a blank slate. The $Windows.~BT folder is hidden and protected; if Explorer refuses to delete it, take ownership or delete it from an admin Terminal with rd /s.

1. Delete the contents of C:\$Windows.~BT and C:\$Windows.~WS if they exist.
2. Press Win + R, type `%temp%`, and delete everything Windows allows.
3. Also run Disk Cleanup on temporary files, then retry the tool.

### Fix 3: Fix 3: Temporarily disable third-party antivirus

AV products love to interfere with the large ESD files the tool downloads. Disabling real-time protection for the run removes the interference cleanly. Some suites require disabling tamper protection first; the real-time toggle alone may silently do nothing while tamper protection guards it.

1. Disable third-party antivirus real-time protection.
2. Run the Media Creation Tool to completion.
3. Re-enable protection immediately afterward.

### Fix 4: Fix 4: Free space and prepare the USB properly

Give the tool room and a clean target. Format the USB as FAT32, confirm it is at least 8 GB, and ensure the system drive has breathing room. If media you create later fails with corruption errors, our [0x80070017 CRC error guide](/articles/how-to-fix-windows-update-error-0x80070017-on-laptop/) covers the hardware checks. USB 2.0 ports are actually preferable for the creation step on some older laptops; their simpler controllers cause fewer mid-write errors with picky flash drives.

1. Back up the USB's contents, then format it as FAT32.
2. Confirm 8 GB or larger capacity and at least 10 GB free on C:.
3. Retry the tool with the prepared drive in a direct laptop port, not a hub.

### Fix 5: Fix 5: Match language, edition, and architecture

Mismatched selections confuse the tool's download manifest. Accepting the recommended options for the current PC is the safest path. The recommended-options checkbox reads the running system's locale and edition; unchecking it is only useful when creating media for a different machine.

1. On the tool's options screen, check Use the recommended options for this PC.
2. If choosing manually, match the running system's language and edition exactly.
3. Proceed with the matched options.

### Fix 6: Fix 6: Stabilize the connection

A flaky connection corrupts the ESD download, and the tool then fails to find the intact files it expects. A stable link prevents the whole class of failure. If the connection drops mid-download, delete the partial temp state before retrying; the tool does not always resume cleanly from a broken ESD.

1. Prefer a wired connection or strong, stable Wi-Fi for the download phase.
2. Disconnect the VPN during the download.
3. Pause large downloads and streaming on the network while the tool runs.

### Fix 7: Fix 7: Download the ISO directly instead

When the tool refuses to cooperate, skip it. Microsoft offers the ISO as a direct download, which you can write to USB with Rufus or mount directly. Rufus and similar tools verify the written USB after creation; that verification pass catches the bad writes that would otherwise surface as setup errors later.

1. Visit the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and choose the ISO download option.
2. Download the ISO and verify it completes fully.
3. Create the USB with your preferred tool or mount the ISO directly. The mounted ISO is also the vehicle for the [0xC1900101 feature-update upgrade path](/articles/how-to-fix-windows-update-error-0xc1900101-on-laptop/) when Windows Update itself will not upgrade. For update-pipeline issues more broadly, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) is the official reference.

## Closing

Media Creation Tool error 0x80070002 is the tool tripping over its own temp files: run it as admin from a simple local path, clear the stale state, keep antivirus and cleaners away during the run, and it completes. When the tool keeps fighting, the direct ISO download is the pragmatic bypass. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the tool's requirements officially.
