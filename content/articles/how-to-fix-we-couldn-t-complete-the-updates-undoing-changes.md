---
title: "We Couldn't Complete the Updates, Undoing Changes: Breaking the Loop"
slug: how-to-fix-we-couldn-t-complete-the-updates-undoing-changes
date: 2026-09-02
categories: ["windows-update"]
tags: ["undoing changes", "update failed", "windows update", "update loop"]
description: "Staring at 'We couldn't complete the updates, undoing changes'? Learn why Windows rolls back updates and the exact steps to stop the cycle and install the update cleanly."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes.webp"
faqs:
  - q: "Is my computer safe while it says undoing changes?"
    a: "Yes, almost always. The message means Windows detected that the update did not install correctly and is deliberately reverting to your last working state. It is a protective mechanism, not damage. Give it time — the rollback can take thirty minutes or longer, and interrupting it is the one thing that can cause real problems."
  - q: "Why does the same update fail and roll back every time?"
    a: "Because nothing about the installation environment changed between attempts. The update fails at the same step for the same reason — a conflicting driver, low disk space, or a corrupted cache — and Windows correctly rolls back each time. You have to remove the blocker first, using the fixes in this article, before retrying."
  - q: "How long should I wait before assuming it is stuck?"
    a: "A normal rollback takes fifteen to forty-five minutes depending on disk speed. If the message has been static for over two hours with no disk activity (no drive light flickering, no fan noise), it is likely stuck. Laptops with old hard drives rather than SSDs can take longer, so be patient with mechanical drives."
  - q: "Will I lose files when Windows undoes the update?"
    a: "No. Rolling back an update only reverses system-level changes — drivers, system files, registry state. Your personal files, documents, photos, and installed programs are not touched by the rollback process. It is specifically designed to return you to a working computer, not to wipe anything."
---

There are few Windows moments more unnerving than watching "We couldn't complete the updates, undoing changes" sit on your screen. The good news is baked into the message itself: Windows is actively protecting you. It tried to install an update, detected that something was wrong, and is now reversing the installation to return your laptop to its last known-good state.

The message becomes a problem when it repeats. If the same update downloads, installs, fails, and rolls back on every attempt, you are in an update loop — and the only way out is to remove whatever keeps breaking the installation. The fixes below start with safe, simple steps and escalate to the deeper repairs that break stubborn loops. If the rollback screen itself is [frozen and never finishes](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update/), deal with that first, since you cannot fix anything until the rollback completes.

## Why this happens

- **Incompatible driver:** An old or buggy driver collides with the update's new driver version, and the installer aborts rather than risk a broken device.
- **Insufficient disk space:** Feature and cumulative updates need significant free space for staging; when it runs out mid-install, Windows rolls back.
- **Corrupted update download:** A damaged package in the download cache fails verification, so the installer backs out.
- **Third-party software conflict:** Antivirus tools, disk utilities, and some VPN clients hook deep into the system and block installer steps.
- **Damaged system files:** Pre-existing corruption in core Windows files makes the update's checks fail at some stage.
- **BIOS or firmware mismatch:** The update expects a certain firmware level, and an outdated BIOS on some laptops triggers the rollback.
- **Failing storage drive:** Bad sectors that surface during the heavy read-write activity of an update cause verification failures.
- **Registry leftovers from old software:** Half-uninstalled drivers and ghost devices create conflicts the update engine cannot resolve.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait out the rollback, then free disk space

First, let the rollback finish completely. Then attack the most common cause.

1. Let the "undoing changes" screen finish on its own — do not force a shutdown.
2. Once back at the desktop, open Settings and check your drive: **System > Storage**.
3. Free up space until you have at least 20 GB free on the system drive (run Disk Cleanup or uninstall unused programs).
4. Empty the Recycle Bin and clear the temporary files Disk Cleanup suggests.
5. Check for updates again and see whether the update now proceeds past its previous failure point.

### Fix 2: Run the Windows Update troubleshooter

The built-in troubleshooter detects the specific failure signature and often clears it automatically. Microsoft details this tool on [Windows support](https://support.microsoft.com/en-us/windows).

1. Open Settings and go to **System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to Windows Update.
3. Apply whatever fixes it recommends, even if the wording seems generic.
4. Restart the laptop afterward.
5. Retry the update.

### Fix 3: Remove recently updated drivers

A driver that updated just before the failure is the prime suspect.

1. Open Device Manager (right-click Start and select it).
2. Expand the categories most likely involved: Display adapters, Network adapters, Sound controllers.
3. Right-click any driver that updated recently and choose **Properties > Driver > Roll Back Driver**.
4. If rollback is grayed out, choose **Uninstall device** instead — Windows will reinstall a basic driver on restart.
5. Restart and retry the update with the rolled-back or generic driver in place.

### Fix 4: Clean out the update cache

A corrupted cache guarantees repeat failures, because Windows keeps retrying the same damaged files.

1. Open Command Prompt as administrator.
2. Run these commands to stop the update services:
   ```
   net stop wuauserv
   net stop bits
   ```
3. Rename the cache folders:
   ```
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   ren C:\Windows\System32\catroot2 catroot2.old
   ```
4. Restart the services with `net start wuauserv` and `net start bits`.
5. Check for updates — this forces a fresh, clean download.

### Fix 5: Disconnect third-party security software

Deep-hooking security tools are a classic cause of mid-install aborts.

1. Temporarily disable your third-party antivirus or firewall — keep Windows Security enabled.
2. If you use a VPN client with a system-level driver, uninstall it temporarily.
3. Disconnect any USB devices except keyboard and mouse (docks, external drives, dongles).
4. Retry the update with this minimal setup.
5. Reinstall or re-enable everything once the update succeeds.

### Fix 6: Repair the system image with SFC and DISM

This fixes pre-existing file corruption that the update's own checks keep tripping over.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` first and let it finish.
3. Then run `sfc /scannow`.
4. Restart the laptop.
5. Attempt the update again — with a clean image, the rollback trigger is gone.

### Fix 7: Install the update manually

If the automatic path keeps failing, a standalone installer often succeeds where the engine failed.

1. Note the KB number in **Settings > Windows Update > Update history**.
2. Download that KB from the Microsoft Update Catalog.
3. Close all programs and run the installer.
4. Restart when prompted.
5. Verify the KB appears in update history as installed.

### Fix 8: Pause updates, then use the Update Assistant

A clean pause clears the retry state, and the Update Assistant uses a different install path than the built-in engine — which sometimes succeeds where the standard flow keeps rolling back. This is also worth trying when a [specific update error code](/articles/how-to-fix-windows-update-error-0x80070002-after-windows-11-update/) keeps appearing alongside the rollback message.

1. Go to **Settings > Windows Update** and pause updates for one week.
2. Restart the laptop so the paused state fully takes effect.
3. Download the Windows Update Assistant from the Microsoft software download page.
4. Run the assistant and let it perform the update outside the normal engine.
5. Unpause updates afterward and confirm the next cycle behaves normally.

## Closing

The "undoing changes" loop is Windows doing its job — refusing to leave you with a half-installed update. Your job is to find the blocker the installer keeps hitting, and in the overwhelming majority of cases it is one of three things: disk space, a conflicting driver, or a corrupted download cache. Clear those, retry once, and the update that rolled back five times will usually sail straight through.
