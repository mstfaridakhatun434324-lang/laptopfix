---
title: "'We Couldn't Complete the Updates, Undoing Changes' in Windows 11 24H2 — Full Fix Guide"
slug: how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-in-windows-11-24h2
date: 2026-09-03
categories: ["windows-update"]
tags: ["couldn't complete updates", "windows 11 24h2", "undoing changes", "update failed", "windows update fix"]
description: "Seeing 'We couldn't complete the updates, undoing changes' on Windows 11 24H2? Follow this technician-ordered guide to break the loop and get updates installing cleanly."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-in-windows-11-24h2.webp"
faqs:
  - q: "What does 'We couldn't complete the updates, undoing changes' actually mean?"
    a: "It means Windows tried to install an update, hit an error it could not recover from, and is now reversing every change the installer made. The servicing engine restores system files, drivers, and registry entries from a pre-update snapshot so you boot back into a working system. It is a protection mechanism, not damage — the update failed, but your data and installed programs are untouched."
  - q: "Why does this error keep coming back on Windows 11 24H2 specifically?"
    a: "Version 24H2 tightened several installation requirements, including stricter driver signature checks and virtualization-based security defaults. Older drivers, outdated BIOS firmware, and third-party antivirus products that were tolerated by earlier builds now trigger hard failures. If the same update fails repeatedly, check your manufacturer's support page for 24H2-ready drivers and firmware before retrying."
  - q: "Can I just disable Windows Update to stop the loop?"
    a: "You can pause updates for up to five weeks in Settings, which buys time but does not fix anything — the failed package will retry when the pause expires. A better approach is to identify the failing KB in Update history, hide it with the show-or-hide updates troubleshooter, and fix the underlying cause. Permanently disabling updates leaves security holes and is not recommended."
  - q: "How do I find which update is causing the rollback?"
    a: "Open Settings, then Windows Update, then Update history. The failed entry shows a KB number and an error code such as 0x800f0922 or 0x80070002. Search that exact code on Microsoft's support site — it usually maps to a specific cause like low disk space, a .NET conflict, or a driver problem — and then apply the matching fix from this guide."
---

"We couldn't complete the updates, undoing changes" is Windows 11's polite way of saying the installer gave up and is cleaning up after itself. On 24H2 this message has become more common, not because the update engine got worse, but because the bar got higher: stricter driver checks, new virtualization-based security requirements, and tighter component-store validation mean packages that limped through on 23H2 now fail loudly instead.

The mechanics are worth understanding because they shape the fix. Every update is installed as a transaction. If any step fails — a driver refuses to migrate, a file hash mismatches, the disk fills up — the engine aborts the transaction and plays it backwards, restoring the pre-update snapshot. That reversal is the "undoing changes" phase. Your job is not to fight the rollback; it is to remove whatever made the transaction fail so the next attempt commits cleanly.

Start by noting the KB number and error code in Update history. Codes like 0x800f0922 (often .NET or low space), 0x80070002 (missing update files), and 0x80070003 follow patterns that point straight at the right fix. With that code in hand, work through the steps below in order.

## Why this happens

- **A driver that fails 24H2's stricter checks:** graphics, Wi-Fi, and storage drivers written for older builds are the top cause of aborted 24H2 updates.
- **Corrupted staged files in the update cache:** an incomplete download in SoftwareDistribution fails its integrity check and the whole transaction unwinds.
- **Insufficient free disk space:** 24H2 feature updates need substantial working room; running out mid-install guarantees a rollback.
- **Third-party antivirus interfering:** security suites that hook the kernel can block file replacements the installer needs to make.
- **A damaged component store (WinSxS):** if DISM-level corruption exists, new components cannot be staged at all.
- **Outdated BIOS/UEFI firmware:** 24H2's security features expect reasonably current firmware; very old firmware can fail the update's prerequisites.
- **Pending servicing operations:** a previous update that never finished leaves the servicing stack in a state the next update cannot build on.
- **A specific KB with a known bug:** sometimes the package itself is broken for certain hardware, and no local fix will help until Microsoft revises it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Record the error code, then wait out the rollback

Diagnosis before action. The error code in Update history is the single most useful piece of information you have, and the rollback needs time to finish safely.

1. If you can reach the desktop, open Settings, then Windows Update, then Update history, and write down the failed KB number and error code.
2. Search the code on the [Microsoft Windows update support pages](https://support.microsoft.com/en-us/windows) to identify the documented cause.
3. If the machine is currently on the "undoing changes" screen, give it 30 to 60 minutes with the charger plugged in and the disk activity light as your guide.
4. Do not interrupt the rollback — a half-reversed transaction is worse than a slow one. The same patience rule applies when Windows is [stuck on the restarting screen](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/).

### Fix 2: Run the Windows Update troubleshooter

The built-in troubleshooter resets the most common failure points — stuck services, misconfigured policies, and corrupted cache metadata — automatically.

1. Open Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Click Run next to Windows Update and let it complete.
3. Apply every fix it recommends, even ones that look unrelated.
4. Restart the laptop and check for updates again.
5. If the troubleshooter itself fails to run, follow our dedicated guide for the [troubleshooter not working](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/).

### Fix 3: Clear the SoftwareDistribution and catroot2 caches

A poisoned update cache makes the same package fail identically on every retry. Clearing it forces a clean re-download and rebuilds the update database.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, and `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart all four services with `net start` commands.
5. Reboot, then run Windows Update and let it re-scan from scratch.

### Fix 4: Repair the component store with DISM and SFC

When the WinSxS store is damaged, the installer cannot stage new components and every update unwinds. DISM repairs the store image; SFC verifies system files against it.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and allow 10 to 30 minutes.
3. Follow with `sfc /scannow` and wait for verification to complete.
4. If SFC reports unfixable corruption, run DISM again, then SFC once more.
5. Reboot and retry the update.

### Fix 5: Update drivers and BIOS from the manufacturer

Because 24H2 enforces stricter driver validation, manufacturer-provided drivers matter more than ever. Windows Update's own driver offerings sometimes lag behind.

1. Visit your laptop manufacturer's support page and download 24H2-ready chipset, graphics, Wi-Fi, and storage drivers.
2. Check for a BIOS/UEFI update and install it following the manufacturer's instructions exactly — keep the charger connected.
3. In Device Manager, look for any device with a yellow warning icon and resolve it before retrying.
4. If a specific driver update delivered through Windows Update keeps failing, hide it with the show-or-hide updates troubleshooter.
5. Retry the feature update only after drivers and firmware are current.

### Fix 6: Free disk space and remove interference

Low space and external interference are the two environmental causes you can eliminate in minutes.

1. Confirm at least 20 GB free on C: via Settings, then System, then Storage.
2. Run Disk Cleanup as administrator, selecting Windows Update Cleanup and Temporary files.
3. Disconnect all USB peripherals except keyboard and mouse.
4. Temporarily disable third-party antivirus and disconnect any VPN.
5. Retry the update in this clean state.

### Fix 7: Perform an in-place upgrade repair

If the servicing stack itself is broken, an in-place upgrade reinstalls Windows 11 over itself — keeping files and apps — and rebuilds the update components completely.

1. Back up important files first, as a matter of habit.
2. Download the Windows 11 ISO from the [official software download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Mount the ISO, run setup.exe, and choose "Keep personal files and apps."
4. Allow 30 to 90 minutes for the upgrade to complete.
5. Afterward, run Windows Update — the previously failing package usually installs cleanly.

## Closing

The "we couldn't complete the updates" loop on 24H2 is frustrating precisely because the message tells you what happened but not why. The error code in Update history is your why — match it to a fix above instead of retrying blindly. In the majority of cases, a cache reset plus current manufacturer drivers breaks the loop permanently. And if the same KB fails on a fully healthy system, check Microsoft's known-issues list: sometimes the right move is simply to wait for the revised package.
