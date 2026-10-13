---
title: "Feature Experience Pack Failed to Install After a Windows 11 Update — How to Fix It"
slug: how-to-fix-feature-experience-pack-failed-to-install-after-windows-11-update
date: 2026-09-06
categories: ["windows-update"]
tags: ["feature experience pack", "windows 11 update", "update failed", "windows feature experience pack", "0x800f0922"]
description: "The Windows Feature Experience Pack keeps failing to install after a Windows 11 update. Here is why it happens and how to get it installed cleanly."
thumbnail: "/images/thumbs/how-to-fix-feature-experience-pack-failed-to-install-after-windows-11-update.webp"
faqs:
  - q: "What is the Windows Feature Experience Pack?"
    a: "It is a Microsoft package that delivers updates to Windows shell features — things like the Snipping Tool, the emoji picker, and input experiences — independently of full OS builds. Because it updates through Windows Update like a normal package, it can fail for the same reasons: corrupted cache, a damaged component store, or a conflicting app. A failed install does not break Windows, but the features it carries stay outdated."
  - q: "Will my laptop work normally if the Feature Experience Pack fails?"
    a: "Yes. The pack updates ancillary shell features, not core system files, so Windows boots and runs fine without it. You might notice an older Snipping Tool or missing input improvements, but nothing critical stops working. Still, repeated failures often signal an underlying servicing problem that will eventually block important updates too, so it is worth fixing rather than ignoring."
  - q: "Why does the Feature Experience Pack fail with error 0x800f0922?"
    a: "That code most often points to low disk space on the system reserved partition or the system drive, or to a .NET Framework servicing conflict. Free at least 20 GB on C:, run Disk Cleanup with the system-files option to clear old update payloads, and make sure the EFI system partition has breathing room. If the error persists, DISM and SFC repairs usually resolve the underlying store damage."
  - q: "Can I install the Feature Experience Pack manually?"
    a: "Yes. You can download the matching package from the Microsoft Update Catalog by searching for the KB number shown in Update history. Run the downloaded .msu or .cab installer with the update services healthy — clear the SoftwareDistribution cache first if previous attempts failed. Manual installation bypasses download corruption, which is one of the most common causes of this specific failure."
---

The Windows Feature Experience Pack is one of those updates most people never notice until it fails. It is Microsoft's vehicle for shipping shell-level improvements — the Snipping Tool, the emoji panel, touch keyboard updates — without waiting for a full feature release. When it installs, nothing dramatic happens. When it fails, Update history shows a red entry that nags you on every subsequent scan, and the failed package can hold up the rest of the update queue behind it.

The failure is rarely about the pack itself. It rides the same servicing rails as every other update: the same download cache, the same component store, the same driver and disk-space prerequisites. That is good news, because it means the standard update-repair toolkit applies directly. Work through the fixes below in order, and check Update history after each one — the pack often installs quietly on the next scan once the underlying blockage is gone.

Note the exact error code next to the failed entry before you start. 0x800f0922, 0x80070002, and 0x80073701 each point at different causes, and matching the code to the fix saves you from working the whole list blind.

## Why this happens

- **A corrupted download of the pack:** interrupted or partial downloads fail the package integrity check every time.
- **Low disk space on C: or the system partition:** the pack needs working room to stage; 0x800f0922 is the classic low-space signature.
- **A damaged component store:** WinSxS corruption blocks staging of the pack's components just like any other update.
- **Conflicting shell extensions or customization tools:** third-party Start menu and shell modifiers can lock files the pack needs to replace.
- **A stuck update queue ahead of it:** a failed cumulative update earlier in the queue can block everything behind it.
- **Corrupted SoftwareDistribution metadata:** the update database can mark the pack as failed permanently until the cache is rebuilt.
- **Pending reboot from a previous install:** servicing operations that never completed leave the stack unable to start new ones.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the error code and retry cleanly once

Sometimes the failure is transient — a locked file during a busy session. A clean retry with nothing competing is worth one attempt before deeper repairs.

1. Open Settings, then Windows Update, then Update history, and note the pack's KB number and error code.
2. Close all applications and reboot the laptop.
3. Immediately after login, open Windows Update and click Check for updates before launching anything else.
4. If the pack installs, you are done. If it fails again with the same code, continue below — and if the whole update pipeline seems broken, our [update troubleshooter guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) is the right companion read. Should the failed install push your machine into a rollback, follow [what to do when Windows says undoing changes](/articles/what-to-do-if-windows-update-says-undoing-changes-made-to-your-computer/).

### Fix 2: Run the Windows Update troubleshooter

The troubleshooter clears the routine blockages — stopped services, bad cache metadata, misregistered DLLs — that commonly sink small packages like this one.

1. Go to Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Run the Windows Update troubleshooter and apply all suggested fixes.
3. Restart the laptop.
4. Check for updates again and watch whether the pack entry turns green.

### Fix 3: Clear the update cache

A poisoned cache makes the same package fail identically forever. Resetting it forces a fresh download of the pack.

1. Open Command Prompt as administrator.
2. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the services and reboot.
5. Run Windows Update and let it re-download the pack from scratch. This reset is documented on Microsoft's [Windows update support pages](https://support.microsoft.com/en-us/windows).

### Fix 4: Free disk space aggressively

The Feature Experience Pack is small, but the servicing engine's working requirements are not. Low space is the number-one fixable cause of 0x800f0922.

1. Check free space on C: — you want at least 20 GB before retrying.
2. Run Disk Cleanup as administrator, click "Clean up system files," and select Windows Update Cleanup, Temporary files, and Previous Windows installations if present.
3. Empty the Recycle Bin and clear C:\Windows\Temp.
4. If the EFI/system reserved partition is full, do not touch it manually — the space on C: is what matters most.
5. Retry the update after cleanup.

### Fix 5: Repair the component store with DISM and SFC

When the store is damaged, the pack's components cannot be staged regardless of how clean the download is.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Allow 10 to 30 minutes for the repair to complete.
3. Follow with `sfc /scannow`.
4. Reboot and check for updates.
5. If DISM reports it could not repair, run it again — second passes often succeed after the first pass fixes the servicing stack itself.

### Fix 6: Remove shell customization tools temporarily

Third-party Start menu replacements, taskbar modifiers, and shell extensions can lock exactly the files this pack updates.

1. Uninstall or disable Start menu/taskbar customization tools temporarily.
2. Reboot to release any locked shell files.
3. Run Windows Update and let the pack install.
4. Reinstall your customization tools afterward and check for updated versions that tolerate the new pack.

### Fix 7: Install the pack manually from the Update Catalog

If the automated pipeline keeps failing, sideloading the package bypasses download and metadata problems entirely.

1. Copy the KB number from Update history.
2. Search for it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and download the version matching your system (x64 for most laptops).
3. Double-click the downloaded file to install, keeping the laptop plugged in.
4. Reboot when prompted and confirm the pack shows as installed in Update history.
5. If manual install also fails, run an in-place upgrade repair with the [Windows 11 ISO](https://www.microsoft.com/en-us/software-download/windows11) — a broken servicing stack is the remaining suspect.

## Closing

A failed Feature Experience Pack looks minor, but treat it as an early warning: it fails for the same reasons cumulative updates fail, just sooner and more visibly. Clear the cache, free the disk, repair the store, and it almost always installs on the next pass. And once it is green, take it as a prompt to check that your bigger updates are flowing too — a healthy servicing stack shows no red entries at all.
