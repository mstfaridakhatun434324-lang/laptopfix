---
title: "Media Creation Tool Error 0x80070002: What to Do"
slug: what-to-do-if-media-creation-tool-error-0x80070002
date: 2026-10-09
categories: ["windows-update"]
tags: ["media creation tool", "0x80070002", "error fix", "windows 11"]
description: "The Media Creation Tool fails with error 0x80070002? This guide fixes the missing-file problem behind it and gets your installer built."
thumbnail: "/images/thumbs/what-to-do-if-media-creation-tool-error-0x80070002.webp"
faqs:
  - q: "What does error 0x80070002 mean in the Media Creation Tool?"
    a: "It means the tool cannot find files it expects, either in the download it is assembling or in your system's update components. The code translates to file not found. Common triggers include a corrupted tool download, broken Windows Update services the tool depends on, antivirus quarantining downloaded files, or insufficient permissions on the working folders."
  - q: "Can I still upgrade Windows if the Media Creation Tool keeps failing?"
    a: "Yes. The Windows 11 Installation Assistant performs in-place upgrades without the Media Creation Tool, and direct ISO downloads from Microsoft's site let you mount the image and run setup manually. The Media Creation Tool is convenient but not mandatory. If the tool itself is the problem, these alternatives bypass it entirely."
  - q: "Does 0x80070002 mean my USB drive is bad?"
    a: "Not usually, but a failing USB drive can trigger it when the tool cannot write files reliably. Test with a different USB stick of at least 8 GB from a reputable brand. If the error appears before the USB stage, during the download phase, the drive is innocent and the problem is in the download pipeline or your system's update components."
  - q: "Will running the Media Creation Tool delete anything on my laptop?"
    a: "No. Creating installation media only writes to the USB drive you select, and even the upgrade option preserves your files and apps when you choose to keep them. The 0x80070002 error happens during preparation, long before anything is modified. Your system is untouched by the failed attempt, so you can troubleshoot without fear."
---

Error 0x80070002 is Windows for file not found, and when the Media Creation Tool throws it, the tool cannot assemble the files it needs. It might fail during the download, during verification, or when writing to your USB drive. Each stage has different culprits, but they all share a theme: something between Microsoft's servers and your machine is breaking the file pipeline.

The frustrating part is that the tool gives you the code and nothing else. No log location, no hint about which file went missing. This guide supplies the missing diagnostics: how to tell which stage failed, how to fix each stage's common causes, and the alternative paths when the tool itself refuses to cooperate.

## Why this happens

- **Corrupted tool download:** The Media Creation Tool executable itself downloaded incompletely and misbehaves from the start.
- **Broken Windows Update services:** The tool relies on the same BITS and update services as Windows Update, and their failure breaks downloads.
- **Antivirus quarantining files:** Security software flags or locks downloaded installer files mid-assembly.
- **Insufficient permissions:** The tool lacks write access to its working folders or the target USB drive.
- **Failing USB drive:** Bad flash memory corrupts writes, producing file-not-found errors during the media creation stage.
- **Corrupted system files:** Damaged servicing components on your laptop break the download and verification pipeline.
- **Network interference:** Proxies, VPNs, or unstable connections corrupt large downloads silently.
- **Insufficient disk space:** The tool needs several gigabytes of working space beyond the final USB image.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify which stage failed

1. Note exactly when the error appears: during the download percentage, during verification, or during USB writing. Each stage points at different fixes below.
2. Download-phase failures implicate services, network, or antivirus. USB-phase failures implicate the drive or permissions.
3. If the tool fails instantly on launch, the executable itself is likely corrupt. Re-download it before anything else.
4. Write down the stage. This two-minute observation prevents you from fixing the wrong half of the pipeline.

### Fix 2: Re-download the Media Creation Tool cleanly

1. Delete the existing Media Creation Tool executable completely.
2. Download a fresh copy from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), preferably in a different browser or with extensions disabled.
3. Right-click the new file, choose **Run as administrator**, and accept the license terms.
4. A surprising number of 0x80070002 cases are simply a damaged tool binary. Fresh downloads with admin rights clear them immediately.

### Fix 3: Repair the Windows Update services

1. The tool downloads through BITS and the update stack. Open an admin Command Prompt and run `net stop bits` and `net stop wuauserv`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`, then restart both services with `net start` commands.
3. Verify the **Background Intelligent Transfer Service** is running in `services.msc` with startup type Manual.
4. Retry the tool. When downloads were failing because the underlying services were broken, this repair unblocks them. The [update service troubleshooting](/articles/windows-update-service-not-running-troubleshooting/) guide covers deeper service damage.

### Fix 4: Temporarily disable antivirus and firewall

1. Turn off real-time protection in your antivirus, or in Windows Security under **Virus & threat protection > Manage settings**.
2. If you run a third-party firewall, disable it temporarily as well. Overzealous firewalls can interrupt the tool's large downloads mid-stream.
3. Re-run the Media Creation Tool with protection paused. Many 0x80070002 failures vanish the moment scanning stops interfering with downloaded chunks.
4. Re-enable everything afterward. If antivirus was quarantining tool files, add the tool's folder to exclusions before your next attempt.

### Fix 5: Run from a clean local account with full permissions

1. Create a temporary local administrator account in **Settings > Accounts > Other users** and sign into it.
2. Copy the Media Creation Tool to the desktop of the new account and run it as administrator from there.
3. Profile-specific corruption, broken permissions, or misconfigured user folders in your main account can all produce file-not-found errors that vanish in a clean profile.
4. If the tool works in the new account, your main profile has the problem. You can migrate to the new profile or repair the old one's permissions.

### Fix 6: Try a different USB drive

1. If the error hits during the USB writing stage, the drive is suspect. Use a different USB stick with at least 8 GB capacity from a known brand.
2. Format it as FAT32 before starting, using Disk Management or the format option in File Explorer.
3. Avoid USB hubs for this operation. Plug the drive directly into the laptop, preferably into a USB port on the opposite side from the one that failed.
4. If you only need an upgrade rather than bootable media, choose the ISO option instead and mount it directly, skipping USB entirely.

### Fix 7: Repair system files and free space

1. Run `sfc /scannow` in an admin Command Prompt to repair protected system files the tool depends on.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` to fix the component store.
3. Ensure at least 15 GB free on the system drive. The tool stages the full Windows image locally before writing media.
4. Disconnect from VPNs and disable proxy settings during the download. Direct connections produce the cleanest large downloads. Microsoft documents the tool's requirements on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 8: Use the alternatives that bypass the tool

1. For an in-place upgrade, download the Windows 11 Installation Assistant from the same Microsoft download page and run it instead.
2. For bootable media, download the ISO directly from Microsoft's site, right-click it, and choose **Mount**, then run `setup.exe` from the virtual drive.
3. For stubborn update failures that drove you to the tool in the first place, the standalone KB installer from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) may be all you needed.
4. If the underlying problem is a failing feature update rather than the tool, the [23H2 failure fix guide](/articles/how-do-i-fix-windows-11-23h2-feature-update-failed/) addresses that directly.

## Closing

Media Creation Tool error 0x80070002 is a file-pipeline problem, and the fix depends on which stage breaks: re-download the tool for launch failures, repair update services for download failures, and swap the USB drive for media failures. When the tool itself will not cooperate, the Installation Assistant and direct ISO downloads get you to the same destination by a different road.
