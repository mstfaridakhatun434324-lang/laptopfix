---
title: "Media Creation Tool Error 0x80070002 on Windows 11 24H2 (Fixed)"
slug: how-to-fix-media-creation-tool-error-0x80070002-in-windows-11-24h2
date: 2026-09-18
categories: ["windows-update"]
tags:
  - media creation tool
  - 0x80070002
  - windows 11 24h2
  - windows update
  - iso
description: "Media Creation Tool failing with error 0x80070002 on Windows 11 24H2? Here is why the download breaks and seven proven fixes to get your ISO or USB built."
thumbnail: "/images/thumbs/how-to-fix-media-creation-tool-error-0x80070002-in-windows-11-24h2.webp"
faqs:
  - q: "What does Media Creation Tool error 0x80070002 actually mean?"
    a: >
      The code translates to the system cannot find the file specified. In the Media Creation Tool it almost always means a downloaded image chunk went missing or was corrupted — because of an interrupted download, antivirus quarantine, or a damaged temp folder — and the tool cannot resume from it. Clearing the staging folders and running the tool as administrator resolves the large majority of cases.
  - q: "Why does the Media Creation Tool fail halfway through the download?"
    a: >
      Halfway failures point to network truncation or disk-space exhaustion. The tool downloads a multi-gigabyte ESD file, and if your connection drops chunks or C: fills up mid-download, the partial file becomes unusable and the tool reports 0x80070002 instead of retrying cleanly. Use a wired connection, free 15 GB on C:, and delete the $Windows.~BT folder before retrying.
  - q: "Is it safe to disable antivirus to run the Media Creation Tool?"
    a: >
      Yes, briefly. Pause only real-time protection, only for the duration of the download, and re-enable it immediately afterward. Download the tool solely from Microsoft's official site so you are not exposing yourself to a tampered binary. Never leave protection off longer than needed, and do not browse elsewhere while it is paused.
  - q: "Should I use the Media Creation Tool or download the ISO directly?"
    a: >
      Both produce the same Windows image. The Media Creation Tool is convenient because it can write the USB directly, but the direct ISO download is more resilient on unreliable networks since browsers and download managers resume better. If the tool fails repeatedly with 0x80070002, grab the ISO and write it with Rufus — the result is identical.
---

Error 0x80070002 means the system cannot find the file specified, and when the Media Creation Tool throws it, the file it cannot find is usually a chunk of the Windows 11 24H2 download it just tried to fetch. The tool is excellent at downloading Windows, but fragile at recovering when a download is interrupted or a temp file goes missing.

This error shows up in two flavors: the tool fails immediately on launch with 0x80070002, or it downloads for a while and then dies partway through. Both have the same family of causes — permissions, blocked temp folders, antivirus interference, or a corrupted partial download the tool keeps tripping over.

Work through the fixes below in order. Most people are building their USB successfully by Fix 4, and the later steps cover the stubborn cases where the tool's own cache is the problem.

## Why this happens

- **The tool is not running as administrator:** the Media Creation Tool writes to protected temp locations and needs elevation. Without it, downloads fail with file-not-found errors partway through.
- **Corrupted partial download in the temp folder:** an interrupted earlier run leaves half-downloaded ESD files behind. The tool tries to resume from them, cannot parse them, and throws 0x80070002.
- **Antivirus quarantining tool components:** security software sometimes flags the tool's downloader modules or the downloaded image chunks, deleting files the tool expects to find.
- **Not enough free space on C:** the tool stages the full Windows image on the system drive before writing the USB. With less than about 12 GB free, staging fails mid-download.
- **Network interruptions or proxy interference:** corporate proxies, VPNs, and unstable Wi-Fi can truncate downloads. The tool's resume logic is weak, so a truncated file becomes a permanent failure.
- **Running the tool from a synced or protected folder:** launching it from OneDrive-synced Desktop or a network share can cause file-access errors that surface as 0x80070002.
- **Outdated tool version:** old Media Creation Tool builds sometimes cannot fetch the current 24H2 image metadata, and the mismatch surfaces as a file-not-found error.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the tool as administrator from a local folder

This resolves the single most common cause. Elevation plus a plain local path removes two failure modes at once, and it takes thirty seconds.

1. Download a fresh copy of the Media Creation Tool from the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Move the downloaded file to a simple local path like C:\Temp (create the folder first).
3. Right-click the tool and choose Run as administrator, then accept the license terms.
4. Try the download again before changing anything else.

### Fix 2: Free up space and clear temp files

Staging failures are silent until they are not. Give the tool the room it needs and clear out the temp files a previous failed run left behind.

1. Open Settings > System > Storage and check free space on C: — aim for at least 15 GB.
2. Run Disk Cleanup (cleanmgr.exe), tick Temporary files and Delivery Optimization Files, and clean them.
3. Press Win + R, type %temp%, delete everything Windows allows you to delete.
4. Retry the Media Creation Tool with the space cleared.

### Fix 3: Temporarily disable third-party antivirus

When antivirus eats the tool's download chunks, no retry logic can save you. A brief, controlled pause of real-time protection is safe if you re-enable it immediately after.

1. Open your antivirus settings and pause real-time protection for 15 to 30 minutes.
2. Keep Windows Defender's own real-time protection on if your third-party tool allows it.
3. Run the Media Creation Tool immediately while protection is paused.
4. Re-enable your antivirus the moment the download completes, before writing the USB.

### Fix 4: Delete the tool's staging folders

A corrupted partial download poisons every subsequent attempt. Clearing the $Windows.~BT folder and the SoftwareDistribution cache forces a genuinely fresh start.

1. Open Command Prompt as administrator.
2. Run: rd /s /q C:\$Windows.~BT — do not worry if it says the folder does not exist.
3. Run: net stop wuauserv, then ren C:\Windows\SoftwareDistribution SoftwareDistribution.old, then net start wuauserv.
4. Reboot and run the Media Creation Tool as administrator again.

### Fix 5: Check your network path to Microsoft's servers

Truncated downloads from flaky connections or interfering proxies are a classic 0x80070002 trigger. Simplify the network and the tool stops tripping.

1. Disconnect any VPN and pause proxy settings in Settings > Network > Proxy.
2. Switch from Wi-Fi to a wired Ethernet connection if possible.
3. Restart your router to clear stale NAT sessions to the download servers.
4. If problems persist, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents connectivity checks for update downloads.

### Fix 6: Re-download the tool and run it from Safe Mode with Networking

A brand-new tool binary plus a minimal driver environment eliminates both a corrupted tool and third-party interference in one move.

1. Delete your current MediaCreationTool.exe and download it again from Microsoft.
2. Boot into Safe Mode with Networking (Settings > Recovery > Advanced startup).
3. Run the fresh tool as administrator from C:\Temp.
4. If it succeeds here, a startup program on your normal boot was the blocker — investigate with a clean boot.

### Fix 7: Repair Windows system files, then retry

When every network and permission fix fails, the file-not-found error may be coming from damaged system components the tool depends on, such as BITS or the servicing stack.

1. Open Command Prompt as administrator and run: sfc /scannow.
2. Follow with: DISM /Online /Cleanup-Image /RestoreHealth.
3. Reboot, then run the Media Creation Tool as administrator one final time.
4. If it still fails, download the ISO directly from Microsoft's site instead and write it with Rufus — the ISO path bypasses the tool entirely.

## Closing

Error 0x80070002 from the Media Creation Tool is almost always an environment problem, not a broken Windows image: permissions, a poisoned temp folder, antivirus, or a shaky network. Run it elevated from a local folder, clear the staging areas, and simplify the network, and the 24H2 ISO builds cleanly. If the tool keeps fighting you, the direct ISO download is a perfectly good plan B — and if the install itself later throws the same code, see our guide to [error 0x80070002 in Windows 11 24H2](/articles/how-to-fix-error-0x80070002-in-windows-11-24h2/) and the [best way to fix install error 0x80070002](/articles/best-way-to-fix-windows-11-install-error-0x80070002/).
