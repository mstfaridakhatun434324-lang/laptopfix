---
title: "How to Fix Media Creation Tool Error 0x80070002 on Windows 10"
slug: "how-to-fix-media-creation-tool-error-0x80070002-on-windows-10"
date: 2026-09-25
categories: ["windows-update"]
tags: ["media creation tool", "0x80070002", "windows 10", "iso download", "usb installer"]
description: "Getting 0x80070002 from the Media Creation Tool on Windows 10? Clear stale staging files, run as admin, fix the network path, or grab the ISO directly instead."
thumbnail: "/images/thumbs/how-to-fix-media-creation-tool-error-0x80070002-on-windows-10.webp"
faqs:
  - q: "Is the Windows 10 Media Creation Tool still available?"
    a: "Yes. Microsoft still offers the Windows 10 Media Creation Tool on the Windows 10 download page, and it remains the supported way to create Windows 10 installation media or ISOs. If you are creating Windows 11 media from a Windows 10 PC, use the Windows 11 Media Creation Tool instead — running the wrong version for your target is a common source of confusing failures."
  - q: "Why does 0x80070002 happen more on older Windows 10 PCs?"
    a: "Older machines combine several risk factors: smaller system drives that fill up during staging, aging Wi-Fi adapters that drop long downloads, third-party antivirus suites with aggressive download scanning, and years of accumulated temp-file cruft. Any one of these can produce the 'file not found' staging failure, and old PCs often have two or three at once — which is why the fix sequence addresses all of them."
  - q: "Can I create the USB on Windows 10 for a different computer?"
    a: "Absolutely — that is one of the tool's main purposes. Uncheck 'Use the recommended options for this PC' and select the language, edition, and architecture (usually 64-bit) for the target machine. This is also a useful diagnostic: if the tool works on a second PC but not yours, the fault is local to your machine's environment, not the tool or Microsoft's servers."
  - q: "What USB drive do I need for the Media Creation Tool?"
    a: "An 8 GB or larger USB flash drive, and the tool will erase everything on it — back up any files first. Use a USB 3.0 drive in a USB 3.0 port if available; the write phase is much faster. Avoid USB hubs during creation, and do not use SD cards in adapters — the tool is picky about removable media types."
---
Error 0x80070002 from the Media Creation Tool on Windows 10 means the same thing it does on Windows 11 — 'the system cannot find the file specified' — but the Windows 10 context changes the odds. Windows 10 machines tend to be older, with tighter disk space, flakier Wi-Fi, and longer-lived software cruft, so the staging failures behind this error are more often environmental than mysterious.

The tool's job is simple: download the Windows image in chunks to a temp staging area, assemble it, and write it to USB or an ISO. 0x80070002 fires when the assembly step reaches for a chunk that is not there — truncated by the network, quarantined by antivirus, or never written for lack of space or permissions. The fix is to give the tool a clean, unobstructed run, and this guide does that methodically.

You will need about 12 GB free on C: and an 8 GB+ USB drive if making bootable media. If you actually need Windows 11 media, use our [Windows 11 Media Creation Tool 0x80070002 guide](/articles/how-to-fix-media-creation-tool-error-0x80070002-on-windows-11/) instead — the steps are similar but the download sources differ.

## Why this happens

- **Stale partial downloads** — Previous failed runs leave incomplete ESD chunks; the tool resumes from them and fails when pieces are missing.

- **Running without administrator rights** — The tool needs admin rights to write staging files and access system temp locations; without them, writes silently fail.

- **Antivirus quarantining image chunks** — Heuristic scanners sometimes flag pieces of the Windows image mid-download, breaking the set.

- **Proxy or VPN mangling the transfer** — Middleboxes can truncate the large range-request downloads, delivering an incomplete file set.

- **Wi-Fi instability on old adapters** — Aging wireless hardware drops long multi-gigabyte transfers more often, and resume does not always recover.

- **Low disk space** — Staging needs ~8-12 GB free; writes that run out of space produce exactly this 'file not found' at assembly time.

- **Wrong tool version for the target** — Using the Windows 10 tool to fetch Windows 11 media (or vice versa) requests mismatched server paths.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Get the correct, latest tool and run it as administrator

Match the tool to your target Windows version, get a fresh copy, and give it the rights it needs.

1. Decide your target: Windows 10 media uses the Windows 10 download page; Windows 11 media uses the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Delete any old MediaCreationTool.exe and download a fresh copy.
3. Right-click the new file and choose **Run as administrator**.
4. If it still fails, continue — the environment needs cleaning, not just the tool.

### Fix 2: Purge temp files and old staging folders

Remove every leftover from previous attempts so nothing stale gets resumed. Pay special attention to folders named $Windows.~WS or $Windows.~BT — these are the tool's staging areas and the most common hiding place for the corrupted chunks behind 0x80070002.

1. Press **Win + R**, type `%temp%`, select all, and delete (skip in-use files).
2. Run **Disk Cleanup** (search it in Start), select C:, check **Temporary files**, and clean.
3. Delete **C:\$Windows.~WS** and **C:\$Windows.~BT** if they exist.
4. Empty the Recycle Bin and re-run the tool as administrator.

### Fix 3: Strip network interference: VPN, proxy, Wi-Fi

Give the multi-gigabyte download the cleanest possible path. Corporate laptops are frequent victims here — company VPNs and proxies are the number-one environmental cause of truncated Media Creation Tool downloads.

1. Disconnect VPNs and turn off proxy settings (**Settings > Network & Internet > Proxy**).
2. Switch to wired Ethernet if available; otherwise move closer to the router and avoid bandwidth-heavy activity during the download.
3. Temporarily pause third-party antivirus real-time scanning.
4. Re-run the tool as administrator and let the download proceed uninterrupted.

### Fix 4: Free space and check the USB drive

Staging and USB-writing both fail cryptically when space or media is marginal. If space is chronically tight, also run Disk Cleanup's 'Clean up system files' option — old Windows Update backups often hide gigabytes there.

1. Ensure 15 GB free on C: using **Settings > System > Storage** tools.
2. Use a known-good 8 GB+ USB 3.0 drive, plugged directly into the PC (no hub).
3. Back up the USB's contents — the tool erases it — and let the tool format it.
4. If USB creation fails but the download seemed fine, choose **ISO file** instead and write it to USB separately.

### Fix 5: Download the ISO directly from Microsoft

Bypass the tool entirely with a plain browser download of the official ISO. If even the direct ISO download fails or corrupts, try a different network entirely (a phone hotspot, for instance) — that isolates your local network as the variable.

1. Visit the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) (or the Windows 10 download page for Windows 10 media) and use the **Download Disk Image (ISO)** section.
2. Download the ISO in your browser — use a download manager if your connection is flaky.
3. Confirm the file size matches what the page states.
4. Mount it (double-click) to upgrade, or write it to USB. Media guidance is in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Clean-boot the PC and retry

When everything else looks right, a background program is sabotaging the run. Prove it with a clean boot.

1. Run `msconfig`, hide Microsoft services, **Disable all** others.
2. Disable all Task Manager **Startup** items and restart.
3. Run the fresh tool as administrator in this minimal environment.
4. Success here means a third-party program was the cause — re-enable in halves to identify it. For related download-stall issues, see [updates stuck downloading](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/).

## Closing

On Windows 10, Media Creation Tool error 0x80070002 is almost always environmental: stale temp files, missing admin rights, a meddling VPN, or tight disk space. Clean the environment, run the right tool as administrator — and remember the direct ISO download as your always-available Plan B.
