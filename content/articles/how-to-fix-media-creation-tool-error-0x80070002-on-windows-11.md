---
title: "How to Fix Media Creation Tool Error 0x80070002 on Windows 11"
slug: "how-to-fix-media-creation-tool-error-0x80070002-on-windows-11"
date: 2026-09-24
categories: ["windows-update"]
tags: ["media creation tool", "0x80070002", "windows 11", "iso download", "usb installer"]
description: "Media Creation Tool failing with 0x80070002 on Windows 11? That is 'file not found' during the download. Fix it with admin rights, a clean temp folder, and the direct ISO fallback."
thumbnail: "/images/thumbs/how-to-fix-media-creation-tool-error-0x80070002-on-windows-11.webp"
faqs:
  - q: "What does Media Creation Tool error 0x80070002 mean?"
    a: "Error 0x80070002 means 'The system cannot find the file specified.' In the Media Creation Tool, it almost always fires during the download phase: the tool cannot find or access a file it expects — usually because a previous partial download left corrupted temp files, the download was blocked or truncated, or permissions prevent the tool from writing to its working folders. It is a download/ staging failure, not a problem with your PC's Windows installation."
  - q: "Why does the Media Creation Tool keep failing at the same percentage?"
    a: "A consistent failure point suggests a corrupted partial download the tool keeps trying to resume, or a network issue (proxy, VPN, unstable Wi-Fi) that breaks the transfer at the same stage. Deleting the tool's temp files forces a genuinely fresh download, and switching to a wired connection or disabling the VPN removes the network variable. If it still fails identically, download the ISO directly instead."
  - q: "Can I use the Media Creation Tool on a different PC?"
    a: "Yes, and it is a legitimate troubleshooting step. The tool can create installation media for another PC — just uncheck 'Use the recommended options for this PC' and pick the right language, edition, and architecture. If the tool fails on your laptop but works on another computer, the problem is local to your machine (permissions, antivirus, disk space), which narrows the diagnosis considerably."
  - q: "How much space do I need for the Media Creation Tool?"
    a: "You need about 8 GB free for the download staging plus a USB drive of at least 8 GB (the tool will erase it). In practice, have 12-15 GB free on the system drive to be safe — the tool stages the ESD/WIM files locally before writing them to USB. Space-related failures often masquerade as 0x80070002, so check this early."
---
The Media Creation Tool is Microsoft's official way to build Windows 11 installation media, and error 0x80070002 is its most common failure: 'The system cannot find the file specified.' In practice, the tool downloads the Windows image in pieces to a temp folder, and something — a truncated download, blocked temp files, missing permissions — leaves it reaching for a file that is not there. The download aborts, sometimes at the same percentage every time.

The frustrating part is how uninformative the error is. 0x80070002 tells you what broke (a file lookup) but not why, so the fix sequence below eliminates the causes in likelihood order: stale temp files first, then permissions, then network interference, then the nuclear option of skipping the tool entirely with a direct ISO download. One of these resolves essentially every case.

Before starting: you will need roughly 12 GB free on the system drive and, if making USB media, an 8 GB+ USB stick you are willing to erase. If your actual goal is fixing a broken Windows Update rather than creating media, our [Windows Update cache reset steps](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/) may solve the underlying problem without any media at all.

## Why this happens

- **Corrupted partial download in temp files** — An interrupted previous run leaves partial ESD files; the tool tries to resume from them and fails when expected chunks are missing.

- **Insufficient permissions** — Running without administrator rights, or restrictive permissions on the temp folders, blocks the tool from writing or reading its staging files.

- **Antivirus blocking the download** — Security software quarantining parts of the downloaded image breaks the file set the tool expects to assemble.

- **VPN or proxy interfering** — Proxies and VPNs can truncate or alter the large download streams, delivering an incomplete file set.

- **Unstable network connection** — Wi-Fi drops mid-download corrupt the multi-gigabyte transfer; the tool's resume logic does not always recover cleanly.

- **Disk space shortage** — With too little free space, staging files get written incompletely, producing the same 'file not found' when the tool looks for the complete set.

- **Outdated Media Creation Tool version** — An old copy of the tool may request image files that no longer exist on Microsoft's servers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Re-download the latest Media Creation Tool

Start by eliminating the stale-tool variable. Old copies reference retired file paths on the server.

1. Delete your existing MediaCreationTool.exe.
2. Go to the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and download a fresh copy.
3. Save it to the Desktop (not a network or synced folder).
4. Right-click it and choose **Run as administrator** — this alone fixes permission-related 0x80070002 cases.

### Fix 2: Clear the tool's temp and staging folders

Purge the corrupted partial downloads so the new run starts from zero instead of resuming broken files.

1. Press **Win + R**, type `%temp%`, and delete everything Windows allows (skip files in use).
2. Also check **C:\$Windows.~WS** and **C:\$Windows.~BT** — delete these folders if present (they are MCT staging leftovers).
3. Empty the Recycle Bin.
4. Run the fresh Media Creation Tool as administrator again.

### Fix 3: Disable VPN, proxy, and third-party antivirus temporarily

Remove everything that can tamper with the download stream. If Windows Update itself is also misbehaving on this machine, our [Windows Update troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) is worth running alongside these steps.

1. Disconnect any VPN and disable proxy settings (**Settings > Network & internet > Proxy** — turn everything off).
2. Temporarily disable third-party antivirus real-time protection (Defender stays on).
3. Prefer a wired Ethernet connection over Wi-Fi for the download if possible.
4. Re-run the tool as administrator.

### Fix 4: Free up disk space on the system drive

Staging failures from low space produce exactly this error. Give the tool room.

1. Ensure at least 15 GB free on C: (**Settings > System > Storage**).
2. Run **Storage Sense** and **Cleanup recommendations** to reclaim space.
3. Move large personal files off the system drive.
4. Retry the Media Creation Tool with space available.

### Fix 5: Try creating an ISO instead of USB media

The USB-writing phase has its own failure modes. Creating an ISO file first isolates whether the problem is the download or the USB writing.

1. In the tool, choose **ISO file** instead of **USB flash drive** when asked.
2. Save the ISO to the Desktop and let the tool complete.
3. If the ISO succeeds, use it directly (mount and run setup) or write it to USB with the tool afterward.
4. If ISO creation also fails with 0x80070002, the download phase is the problem — continue to Fix 6.

### Fix 6: Download the ISO directly (skip the tool)

Microsoft offers the Windows 11 ISO as a direct download — no tool, no staging, no 0x80070002. This is the definitive fallback.

1. On the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), scroll to **Download Windows 11 Disk Image (ISO)**.
2. Select the edition, confirm, choose your language, and download the ISO directly in your browser.
3. Verify the download completed fully (check the file size against the page).
4. Mount the ISO by double-clicking it, or write it to USB with a tool like Rufus. Microsoft documents media options in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Run the tool from a clean boot

If it still fails, a background program is interfering. A clean boot proves it.

1. Press **Win + R**, type `msconfig`, go to **Services**, check **Hide all Microsoft services**, and **Disable all**.
2. In Task Manager's **Startup** tab, disable all startup items, then restart.
3. Run the fresh Media Creation Tool as administrator.
4. If it succeeds, re-enable services in groups to find the interfering program.

## Closing

Media Creation Tool error 0x80070002 is a download-staging failure, not a verdict on your PC. Fresh tool, clean temp folders, admin rights, and an uninterrupted network fix it — and the direct ISO download is always there when the tool itself is the problem.
