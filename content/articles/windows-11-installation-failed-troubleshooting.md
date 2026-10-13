---
title: "Windows 11 Installation Failed: Complete Troubleshooting Guide"
slug: windows-11-installation-failed-troubleshooting
date: 2026-09-29
categories: ["windows-errors"]
tags: ["installation", "upgrade failure", "Windows 11"]
description: "Windows 11 installation keeps failing? Diagnose the blocker — drivers, disk space, compatibility — and get it installed."
thumbnail: "/images/thumbs/windows-11-installation-failed-troubleshooting.webp"
faqs:
  - q: "Why does my Windows 11 installation keep failing?"
    a: "The top reasons are incompatible or outdated drivers (especially storage and graphics), insufficient disk space, corrupted installation media, and unmet system requirements (TPM 2.0, Secure Boot). The installer usually leaves a clue — an error code or a percentage where it always stops."
  - q: "Where do I find why the installation failed?"
    a: "Check C:\\$Windows.~BT\\Sources\\Panther\\setupact.log after a failed upgrade — it logs exactly where setup stopped. The Settings > Windows Update > Update history entry for the failed update also shows an error code you can look up."
  - q: "How much free space does a Windows 11 feature update need?"
    a: "Microsoft asks for 64 GB total drive capacity, but for the update itself you want at least 20 GB free — the installer stages gigabytes of files and needs working room. On 128 GB laptops that are nearly full, space is the most common silent failure."
  - q: "Should I clean install instead of upgrading?"
    a: "A clean install bypasses most upgrade-failure causes because there's no old system to conflict with — but it erases everything, so it's the last resort. Try the upgrade fixes first; they're less destructive and resolve the large majority of failures."
---
"Windows 11 installation failed" with no useful explanation is one of the more demoralizing messages in computing — you waited an hour, and all you got was a rollback and a vague error. But failed installations are almost never mysterious. The installer is picky about a specific checklist (drivers, space, compatibility, media integrity), and failures cluster around a handful of known blockers. Find your blocker, remove it, and the install goes through.

This guide covers both upgrade installs (Windows Update or setup.exe over your current system) and the failure patterns they share. Whether it dies at 30% or 87% every time, there's a reason — and it's fixable.

## Why this happens

- **Incompatible drivers.** The biggest single cause of upgrade failures. Storage drivers, graphics drivers, and antivirus filter drivers that aren't 24H2-ready make the installer abort rather than risk an unbootable system.
- **Insufficient disk space.** The installer needs room to stage the new Windows alongside the old one. When space runs out mid-install, it fails — sometimes with a space error, sometimes with a misleading generic code.
- **Corrupted installation media or downloads.** A USB stick with bad sectors, an ISO that downloaded incompletely, or a corrupted Windows Update cache all produce failures at consistent percentages.
- **Unmet system requirements.** TPM 2.0, Secure Boot, and CPU generation requirements are enforced. Machines that "mostly" meet them — TPM present but disabled in BIOS, for example — fail late in the process.
- **Peripheral interference.** USB devices with quirky drivers (old printers, exotic dongles, some docks) can hang the installer's hardware-detection phase. The installer waits, times out, and fails.
- **Third-party antivirus blocking the install.** Security suites that lock system files or quarantine setup components mid-install are a classic cause of rollbacks with no clear error.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Read the failure log

Don't guess — the installer logged exactly what went wrong.

1. After a failed upgrade, open **File Explorer**, enable **View > Show > Hidden items**, and navigate to `C:\$Windows.~BT\Sources\Panther\`.
2. Open **setupact.log** (it's large — use Find) and search for `0x` error codes or the word `Failed` near the end of the file. The last failure before the rollback is your answer.
3. Also check **Settings > Windows Update > Update history** for the error code on the failed update (common ones: [0x80070002](/articles/how-to-fix-windows-11-install-error-0x80070002/), 0x800f081f, 0xC1900101).
4. A `0xC1900101` code specifically means driver failure — note any driver filename mentioned near it and jump to Fix 3. A `0x800f081f` in the log points at component-store damage instead — see our [0x800f081f fix](/articles/how-to-fix-error-0x800f081f-in-windows-11-24h2/).

### Fix 2: Free up serious disk space

The quick win that resolves a shocking number of "mysterious" failures.

1. Open **Settings > System > Storage** and check free space. You want **20+ GB free** for a feature update.
2. Click **Temporary files**, tick everything substantial — **Windows Update Cleanup**, **Delivery Optimization Files**, **Temporary Internet Files**, **Previous Windows installations** (only if you're sure you won't roll back) — and click **Remove files**.
3. Move personal media (videos, downloads, game installers) to external storage temporarily. Uninstall programs you don't use via **Settings > Apps > Installed apps**, sorted by size.
4. Retry the install. If space was the blocker, it now sails through — and you've also made the laptop faster in the process.

### Fix 3: Update or remove problem drivers

Target the drivers the installer chokes on.

1. Update these from your laptop manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or Lenovo's support site): **chipset**, **storage/RAID**, **graphics**, and **BIOS/firmware**. Do BIOS first (on AC power), then the rest with restarts between.
2. If the setup log named a specific third-party driver, uninstall its software entirely via **Settings > Apps** — antivirus suites, VPN clients, and disk utilities are the usual names in the log.
3. In **Device Manager** (**Win + X**), look for any device with a yellow warning triangle and resolve or disable it before retrying.
4. Disconnect all non-essential USB devices before the install attempt — leave only keyboard, mouse, and the install media. This alone fixes the "hangs at hardware detection" failure pattern.

### Fix 4: Run the pre-install health checks

Verify the system is in a state the installer accepts.

1. Open **Terminal (Admin)** and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`. The installer validates system integrity, and these ensure it passes.
2. Check requirements: press **Win + R**, type `tpm.msc` — you want "TPM is ready for use." Check **System Information** (`msinfo32`) — **Secure Boot State** should be **On**, **BIOS Mode** should be **UEFI**.
3. If TPM shows as not ready, enter **BIOS/UEFI** and enable **TPM** (sometimes called **PTT** on Intel or **fTPM** on AMD) and **Secure Boot**.
4. Run `chkdsk C: /f` to make sure the file system is clean — schedule for restart if prompted.

### Fix 5: Use the Installation Assistant or fresh media

Bypass a broken delivery path.

1. If Windows Update keeps failing, download the **Windows 11 Installation Assistant** from the [official download page](https://www.microsoft.com/en-us/software-download/windows11) and run it — it uses a separate download and install path.
2. If the Assistant also fails, create fresh USB media with the **Media Creation Tool** from the same page, using a different USB stick than before if possible.
3. Boot from the USB and choose **Upgrade** (keeps files and apps) rather than Custom — you get fresh media without the nuclear option.
4. During setup from USB, keep the laptop plugged in and don't let it sleep — interrupted installs from power loss are a needless self-inflicted failure.

### Fix 6: Temporarily remove third-party antivirus

Eliminate the most common software blocker.

1. Uninstall (not just disable) your third-party antivirus via **Settings > Apps > Installed apps**. Disabling often leaves filter drivers loaded; uninstalling removes them.
2. **Windows Defender** activates automatically and protects you during the install — you're not unprotected.
3. Run the installation. If it succeeds, you can reinstall your preferred antivirus afterward — preferably the latest version, since the old one clearly didn't play well with the new Windows.
4. This step feels drastic but it's temporary and it's one of the highest-yield fixes for 0xC1900101-style driver failures.

### Fix 7: Clean install as the last resort

When the upgrade path is blocked beyond repair, start fresh.

1. Back up **everything** important to external storage or the cloud — a clean install erases the drive.
2. Boot from your fresh USB media, choose **Custom install**, delete the old partitions (or at least the Windows partition), and install.
3. After installation, install drivers from the manufacturer's support site in order: chipset, graphics, network, then the rest.
4. Restore your files and reinstall programs. A clean install also clears years of accumulated cruft — many laptops run noticeably better afterward, which softens the hassle. If you'd rather keep troubleshooting the upgrade path, our [Startup Repair guide](/articles/how-to-use-startup-repair-windows-11-on-laptop/) covers recovering when a failed install leaves the system unbootable.

## Closing

Failed Windows 11 installations are the installer telling you "something in your current setup isn't ready" — and it's usually right. Drivers, disk space, and antivirus cover the vast majority of cases, in that order. The setup log (Fix 1) turns the guessing game into a reading exercise, so always start there. And remember the ordering principle: fix the current system first (it's less destructive), escalate to fresh media second, and save the clean install for when everything else has genuinely failed. Patience with the checklist beats reinstalling in frustration every time.
