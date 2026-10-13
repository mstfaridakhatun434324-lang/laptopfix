---
title: "'We Couldn't Complete the Updates, Undoing Changes' on Windows 10 — How to Fix It"
slug: how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-windows-10
date: 2026-09-16
categories: ["windows-update"]
tags: ["windows 10", "couldn't complete updates", "undoing changes", "update failed", "windows update fix"]
description: "Windows 10 stuck on 'We couldn't complete the updates, undoing changes'? Work through these ordered fixes to break the loop and update cleanly."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-windows-10.webp"
faqs:
  - q: "Why does Windows 10 still get the undoing changes loop?"
    a: "Windows 10's servicing stack is mature but aging, and the monthly cumulative updates keep growing. Older hardware, fragmented update caches from years of patching, and drivers that vendors stopped updating all raise the failure rate. The rollback itself works the same as on Windows 11 — the engine reverses the failed transaction — so the same repair sequence applies, adjusted for Windows 10's menus."
  - q: "Should I upgrade to Windows 11 instead of fixing the loop?"
    a: "If your hardware supports Windows 11 and the loop keeps returning, an upgrade can be the pragmatic fix — it replaces the entire servicing stack. But do not upgrade to escape a broken update pipeline without diagnosing it first: a corrupted cache or failing drive will sabotage the upgrade too. Fix the loop with this guide, verify updates flow, then upgrade on your own schedule."
  - q: "How much free space does Windows 10 need to avoid rollback loops?"
    a: "Aim for at least 20 GB free on C:, and more before a feature update. Windows 10 needs room for the staged update, the rollback snapshot, and the WinSxS growth that accumulates over years of cumulative updates. Machines that have run for years without a Disk Cleanup often carry 10 to 15 GB of superseded update payload that cleanup reclaims in minutes."
  - q: "Can I use the Media Creation Tool to fix repeated update failures?"
    a: "Yes — it is one of the best tools for this. The Media Creation Tool can perform an in-place upgrade repair that reinstalls Windows 10 while keeping your files and apps, rebuilding the servicing stack completely. Download it from Microsoft, choose 'Upgrade this PC now,' and select the keep-everything option. It resolves loops that cache resets and DISM cannot."
---

Windows 10 may be in its twilight, but millions of laptops still run it — and they still hit "We couldn't complete the updates, undoing changes" with regularity. The causes skew a little different than on Windows 11: years of accumulated cumulative updates have bloated the component store, vendors have stopped refreshing drivers for older models, and the update cache has had years to fragment. The rollback mechanics are identical, though — a failed transaction being reversed — and so is the repair logic.

There is one Windows 10-specific consideration before you start: the menus moved. Troubleshooters live under Settings, then Update & Security, then Troubleshoot; Update history sits under Windows Update, then View update history. The commands — DISM, SFC, the net stop/start service dance — are exactly the same. Work through the fixes below in order, noting the failed KB and error code first.

And a practical note for older hardware: if this laptop has a mechanical hard drive, multiply every time estimate in this guide. Rollbacks and repairs that take 20 minutes on an SSD can take two hours on a spinning disk. That is normal, not broken.

## Why this happens

- **Years of accumulated WinSxS bloat:** superseded update payloads crowding the component store and the system drive.
- **Vendors abandoning driver updates:** old drivers that modern cumulative updates cannot migrate cleanly.
- **A fragmented, aging update cache:** years of SoftwareDistribution history raising corruption odds.
- **Low disk space on older small drives:** the staged update plus rollback snapshot exceeding available room.
- **Third-party antivirus with deep hooks:** legacy security suites interfering with file replacement.
- **Pending servicing operations:** unfinished previous updates leaving the stack inconsistent.
- **Failing aging hardware:** older SSDs and HDDs developing read errors the installer reads as corruption.
- **A specific cumulative update with a known bug:** some months' updates simply break on certain configurations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback finish and record the failure

Patience first, evidence second. The error code shapes everything downstream.

1. Keep the charger connected and give the "undoing changes" screen 30 to 60 minutes (longer on HDDs), watching the disk light.
2. Once on the desktop, go to Settings, then Update & Security, then Windows Update, then View update history.
3. Note the failed KB number and error code.
4. If the desktop never appears, the [Windows 10 undoing-changes stuck guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-windows-10/) covers the recovery path in detail.

### Fix 2: Run the Windows Update troubleshooter

Windows 10's troubleshooter resets the classic failure points automatically.

1. Go to Settings, then Update & Security, then Troubleshoot, then Additional troubleshooters.
2. Run the Windows Update troubleshooter and apply all recommended fixes.
3. Restart the laptop.
4. Check for updates again. If the troubleshooter will not run, see our [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-windows-10/).

### Fix 3: Deep-clean years of update bloat

On a long-running Windows 10 install, this step alone frequently breaks the loop.

1. Run Disk Cleanup as administrator and click "Clean up system files."
2. Select Windows Update Cleanup, Temporary files, and Previous Windows installations — this can reclaim 10 to 15 GB.
3. Confirm at least 20 GB free on C: afterward.
4. Turn on Storage Sense under Settings, then System, then Storage for ongoing hygiene.
5. Retry the update with the reclaimed space.
6. For the deepest clean, also tick "Device driver packages" in Disk Cleanup's system-files view — years of superseded drivers can occupy several gigabytes on old installs.

### Fix 4: Reset the update cache

Standard servicing repair: a corrupted cache fails the same package identically forever.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the services and reboot.
5. Check for updates on a stable connection. Microsoft's [update support pages](https://support.microsoft.com/en-us/windows) document this procedure.

### Fix 5: Repair the component store with DISM and SFC

Years of patching make store damage more likely on Windows 10 — repair it before retrying.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Allow 15 to 40 minutes on older hardware.
3. Follow with `sfc /scannow`.
4. Reboot and retry the update.

### Fix 6: Update drivers from the manufacturer and strip interference

Old drivers are a prime Windows 10 rollback trigger — refresh them from the source.

1. Visit your laptop manufacturer's support site and install the latest Windows 10 drivers for your model, especially chipset and storage.
2. Disconnect all USB peripherals except keyboard and mouse.
3. Temporarily disable third-party antivirus and disconnect VPNs.
4. Retry the update in this clean state.
5. If a specific driver update keeps failing, hide it with the show-or-hide updates troubleshooter.
6. After success, re-enable your antivirus and reconnect peripherals one at a time to confirm nothing reintroduces the conflict.

### Fix 7: In-place upgrade repair with the Media Creation Tool

The definitive fix for a Windows 10 servicing stack that will not heal — reinstall Windows over itself, keeping everything.

1. Download Microsoft's Media Creation Tool for Windows 10 from the [official software download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it and choose "Upgrade this PC now."
3. Select "Keep personal files and apps" when prompted.
4. Allow one to two hours for the repair to complete.
5. Afterward, updates should install cleanly — verify in Update history.

## Closing

Windows 10's undoing-changes loop is usually a maintenance story: years of update bloat, aging drivers, and a cache that has never been reset. The deep cleanup in Fix 3 plus a cache reset resolves most cases without touching the heavier tools. And if the loop keeps returning on hardware that qualifies, treat the repaired system as your launchpad for a planned Windows 11 upgrade — on your schedule, not the rollback screen's. Once updates flow again, make the cleanup a monthly ten-minute habit: it keeps a Windows 10 machine updating smoothly for years.
