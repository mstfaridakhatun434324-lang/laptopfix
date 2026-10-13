---
title: "How to Run DISM RestoreHealth on Windows 11 (24H2 Guide)"
slug: how-to-run-dism-restore-health-in-windows-11-24h2
date: 2026-10-11
categories: ["windows-errors"]
tags: ["dism", "system repair", "windows 11"]
description: "Learn how to run DISM /RestoreHealth correctly on Windows 11 24H2 to repair corrupted system files, including what to do when it fails."
thumbnail: "/images/thumbs/how-to-run-dism-restore-health-in-windows-11-24h2.webp"
faqs:
  - q: "How long should DISM /RestoreHealth take on Windows 11 24H2?"
    a: "Typically 15 to 45 minutes on an SSD with a decent internet connection. It commonly appears stuck at percentages like 62% or 84% — that's normal while it downloads and stages files. Only worry if there's zero progress for over an hour, or if it errors out."
  - q: "What's the difference between SFC and DISM?"
    a: "SFC scans your live system files and replaces corrupted ones using the local component store as its source. DISM repairs that component store itself, downloading clean files from Windows Update or an ISO. That's why the correct order is DISM first, then SFC — SFC can only fix what its source allows."
  - q: "Why does DISM fail with error 0x800f081f?"
    a: "Windows can't find the source files it needs — usually because Windows Update is blocked, the connection drops, or group policy disables online repair. Mounting a matching Windows 11 ISO and pointing DISM at it with the /Source and /LimitAccess switches bypasses the problem entirely."
  - q: "Can I run DISM in Safe Mode?"
    a: "Yes, DISM works fine in Safe Mode with Networking (it needs network access for the default online repair). If even Safe Mode is broken, run it offline from the recovery environment's Command Prompt with the /Image switch pointing at your Windows drive."
---

DISM with the RestoreHealth option is the heavy artillery of Windows repair: when SFC can't fix corrupted system files, DISM fetches clean copies and repairs the underlying component store. On Windows 11 24H2 the command works the same as ever, but there are a few 24H2-specific quirks worth knowing.

This guide covers the correct command sequence, how long each step takes, and what to do when DISM itself errors out. If you're here because of crashes rather than curiosity, our [SFC and DISM crash-repair notes](/articles/best-way-to-fix-your-pc-ran-into-a-problem/) pair well with this.

## Why this happens

- SFC reports corrupted files it couldn't repair — meaning the component store DISM maintains is itself damaged.

- Windows updates failing repeatedly with corruption-related error codes.

- Blue screens or app crashes traced to damaged system components.

- DISM failing with errors like 0x800f081f (source files not found) on 24H2 systems.

- Running DISM without admin rights, which silently fails to do anything useful.

- Interfering third-party 'debloater' scripts that ripped out components DISM expects to find.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Open an elevated Terminal

DISM must run as administrator. Without elevation it fails or pretends to work — the single most common DISM mistake.

1. Press **Win + X** and choose **Terminal (Admin)**.

2. Click **Yes** on the User Account Control prompt.

3. Confirm the window title shows **Administrator**.

4. If you only see PowerShell without admin, close it and retry — elevation is non-negotiable.

### Fix 2: Check the component store health first

A quick health scan tells you whether a full restore is even needed, and it finishes in under a minute.

1. In the admin Terminal, run `DISM /Online /Cleanup-Image /CheckHealth`.

2. If it reports **No component store corruption detected**, you don't need RestoreHealth.

3. If it reports corruption (or 'repairable'), continue to the next fix.

4. For a deeper scan, `DISM /Online /Cleanup-Image /ScanHealth` takes 5-10 minutes and gives more detail.

### Fix 3: Run RestoreHealth

This is the main event: DISM downloads clean component files from Windows Update and repairs the store. Plan for it to take a while.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth`.

2. Expect it to sit at certain percentages (like 62% or 84%) for a long time — this is normal, don't close it.

3. Typical runtime is **15-45 minutes** depending on your connection and SSD speed.

4. When it reports **The restore operation completed successfully**, restart the laptop, then run `sfc /scannow` to finish the job.

### Fix 4: Fix error 0x800f081f with a local source

This error means DISM couldn't download repair files. Pointing it at a Windows 11 24H2 ISO as the source bypasses the download entirely.

1. Download the Windows 11 24H2 ISO from the [official Microsoft software download page](https://www.microsoft.com/en-us/software-download/windows11) and mount it by double-clicking.

2. Note the drive letter (say **E:**) and check whether it has **install.wim** or **install.esd** under `E:\Sources`.

3. For a WIM, run: `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:E:\Sources\install.wim:1 /LimitAccess`.

4. For an ESD, use `/Source:ESD:E:\Sources\install.esd:1` instead. Then restart and run `sfc /scannow`.

### Fix 5: Run DISM from the recovery environment

If Windows is too damaged to repair itself while running, offline DISM from WinRE repairs the installed system from outside it.

1. Boot into recovery (force-power-off twice during the Windows logo, or **Settings > System > Recovery > Advanced startup**).

2. Go to **Troubleshoot > Advanced options > Command Prompt**.

3. Identify your Windows drive letter with `diskpart` then `list volume` (it's often **D:** here, not C:).

4. Run `DISM /Image:D:\ /Cleanup-Image /RestoreHealth` using the correct letter, then `exit` and continue to Windows.

### Fix 6: Check the DISM log when it fails

DISM writes a detailed log. When the summary message is cryptic, the log names the exact file or operation that failed.

1. Open `C:\Windows\Logs\DISM\dism.log` in Notepad.

2. Scroll to the bottom and search upward for **Error** or **Failed**.

3. Common findings: a specific package name (uninstall that update), or CBS corruption (run `sfc /scannow` first, then DISM again).

4. If the log points at a Windows Update package, remove it via **Settings > Windows Update > Update history > Uninstall updates**. More on update repairs is on [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 7: Do an in-place upgrade repair

When DISM can't repair the component store — or repairs don't stick — an in-place upgrade reinstalls Windows over itself, replacing every system file while keeping your files, apps, and settings. It's the step above DISM on the repair ladder.

1. Download the Windows 11 24H2 ISO from the [official Microsoft software download page](https://www.microsoft.com/en-us/software-download/windows11) and mount it.

2. Run **setup.exe** from the mounted drive.

3. Choose **Keep personal files and apps** when asked what to keep.

4. Let setup complete — it takes 30-90 minutes and reboots several times.

5. Afterward, run `sfc /scannow` once to verify everything is clean.

## Closing

DISM /RestoreHealth is the tool you reach for when SFC gives up — it repairs the repair system itself. Run it elevated, give it time at those stuck percentages, and use a mounted 24H2 ISO as the source if error 0x800f081f appears. Once DISM reports success, always follow with sfc /scannow and a restart; the two tools are a pair, and skipping the second half leaves the job unfinished. Think of the repair ladder as SFC, then DISM, then in-place upgrade — each step replaces more of Windows while keeping your files. For lighter problems where you just want to undo a recent change, our [System Restore guide](/articles/best-way-to-use-system-restore-on-windows-11/) is the faster tool. Knowing which rung to grab saves hours.
