---
title: "How to Fix Error 0x800f0922 on Windows 11"
slug: how-to-fix-error-0x800f0922-on-windows-11
date: 2026-10-09
categories: ["windows-errors"]
tags: ["error-0x800f0922", "windows-11", "windows-update"]
description: "Error 0x800f0922 blocking Windows 11 updates? Fix the .NET, Secure Boot, and component issues behind it."
thumbnail: "/images/thumbs/how-to-fix-error-0x800f0922-on-windows-11.webp"
faqs:
  - q: "What does error 0x800f0922 mean?"
    a: "It means a Windows update or feature install failed during the component-installation phase — often tied to .NET Framework installation problems, a disabled Secure Boot conflicting with the update, or corrupted servicing components. The System Reserved partition being full is another classic trigger."
  - q: "Why does 0x800f0922 mention .NET Framework?"
    a: "Because many cumulative updates include .NET servicing, and if the .NET installation pipeline is broken — corrupted payloads, missing manifests — the whole update fails with this code. Repairing .NET or the component store usually clears it."
  - q: "Can Secure Boot really block a Windows update?"
    a: "In some configurations, yes. Certain firmware updates and secure-boot-related components fail to install when Secure Boot is disabled in a way the update doesn't expect. Re-enabling it in the BIOS has resolved 0x800f0922 for some users."
  - q: "Will I lose data fixing this?"
    a: "No. The fixes here — repairing .NET, resetting update components, freeing the reserved partition — don't touch your files. Only a full reinstall would, and that's not needed for this error."
---
# How to Fix Error 0x800f0922 on Windows 11

**Error 0x800f0922** typically strikes during Windows Update when the install reaches its component phase — and it loves to involve **.NET Framework**. The update downloads fine, starts installing, then dies with this code. It's also the error you'll see when the System Reserved partition is full or when Secure Boot settings confuse the installer.

The fix path depends on which trigger is yours, so this guide covers all three in likelihood order. A quick way to guess: if the failure mentions .NET or happens on updates that include .NET servicing, start with Fix 1. If you've cloned your drive or dual-boot and the reserved partition was resized, suspect Fix 2.

If your update error is a different code, check our [error 0x80070057 fix](/articles/error-code-0x80070057-fix/) for the parameter-incorrect variant.

## Why this happens

- **Broken .NET Framework installation:** Corrupted .NET payloads cause the servicing phase to fail.
- **Full System Reserved partition:** The small boot partition has no room for the update's boot files.
- **Secure Boot disabled or misconfigured:** Firmware-related update components fail when Secure Boot state is unexpected.
- **Corrupted servicing stack:** Damaged component-store or update components abort the install phase.
- **Third-party antivirus interference:** Real-time scanning locking files the installer needs to replace.
- **Corrupted update cache:** Damaged downloaded files failing validation mid-install.

## How to fix it

Work through these in order. Fixes 1–2 handle the most common triggers.

### Fix 1: Repair .NET Framework

Since .NET is implicated so often, start here.

1. Download the **.NET Framework Repair Tool** from Microsoft's website and run it — it fixes common .NET installation corruption automatically.
2. If the tool doesn't resolve it, turn .NET off and on: go to **Control Panel > Programs > Turn Windows features on or off**, uncheck **.NET Framework 3.5** and **.NET Framework 4.8 Advanced Services**, restart, then re-check them and restart again.
3. Retry Windows Update. If .NET was the blocker, the update now sails through the phase that used to fail.
4. As an extra check, run `sfc /scannow` afterward — .NET corruption and system-file corruption often travel together, and fixing only one can leave the other to fail the next update.

### Fix 2: Free space on the System Reserved partition

A full reserved partition is the second classic cause.

1. Press **Win + R**, type `diskmgmt.msc`, and identify the System Reserved partition (usually 100–500 MB, no drive letter).
2. Right-click it, choose **Change Drive Letter and Paths**, and assign a temporary letter.
3. Open an admin Command Prompt, navigate to that drive, and delete unnecessary files — old fonts, logs — but never delete folders you don't recognize.
4. Remove the drive letter afterward (**Change Drive Letter and Paths > Remove**).
5. Retry the update. Even 50 MB of freed space can be enough — the boot files the installer needs to stage are small, so you don't need to empty the partition, just give it breathing room.

### Fix 3: Check Secure Boot status

An unexpected Secure Boot state trips certain updates.

1. Press **Win + R**, type `msinfo32`, and check the **Secure Boot State** line.
2. If it says **Off** and your hardware supports it, restart into the BIOS/UEFI (**Settings > System > Recovery > Advanced startup > Troubleshoot > UEFI Firmware Settings**).
3. Find the **Secure Boot** option (usually under **Security** or **Boot**) and set it to **Enabled**.
4. Save and exit, then retry the update.
5. If your organization requires Secure Boot off, skip this fix — it's a workaround for consumer setups, not a mandate.

### Fix 4: Reset Windows Update components

Clear the corrupted cache and reset the servicing pipeline.

1. Open **Terminal (Admin)** and run:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
2. Rename the caches:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
3. Restart the services with matching `net start` commands.
4. Check for updates again.
5. After the reset, give the first update check extra time — Windows is rebuilding its entire update metadata from scratch, so the initial scan can take noticeably longer than usual.

### Fix 5: Repair system files with SFC and DISM

Damaged servicing files abort installs regardless of the other fixes.

1. In an admin Terminal, run `sfc /scannow`.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. If DISM reports it can't find source files, mount a Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11) and use it as the source (for example: `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:E:\Sources\Install.wim:1 /LimitAccess`).
4. Restart and retry the update.

### Fix 6: Temporarily disable third-party antivirus

File locks from security software can abort the install phase.

1. Disable real-time protection temporarily in your antivirus.
2. Retry the update immediately.
3. Re-enable protection as soon as the test is done.
4. If it worked, update the antivirus to the latest version before the next update cycle.

### Fix 7: Install the update manually

When the automatic pipeline keeps failing at the same phase, the standalone installer often succeeds.

1. Find the KB number in **Settings > Windows Update > Update history**.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Run the `.msu` and follow the prompts.
4. If manual install also fails with 0x800f0922, run an in-place upgrade with the Windows 11 ISO — it rebuilds the servicing stack while keeping your files and apps. Microsoft documents update troubleshooting on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Error 0x800f0922 is an install-phase failure, and the phase most often breaks on .NET problems, a full System Reserved partition, or Secure Boot surprises. Repair .NET, free the reserved partition, check Secure Boot, and reset the update components — one of those clears the path for the update to finish. It's a fiddly error, but every cause on the list is fixable without reinstalling Windows. If a failed update left your system unstable, our [black screen after update guide](/articles/windows-11-black-screen-after-update-fix/) covers recovery — and the update will install cleanly once its blocker is gone.
