---
title: "'We Couldn't Complete the Updates, Undoing Changes' on an Acer Laptop — Step-by-Step Fix"
slug: how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-acer-laptop
date: 2026-09-12
categories: ["windows-update"]
tags: ["acer laptop", "couldn't complete updates", "undoing changes", "acer care center", "windows 11"]
description: "Acer laptop looping on 'We couldn't complete the updates, undoing changes'? Fix it with Acer-specific driver steps and ordered Windows servicing repairs."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-acer-laptop.webp"
faqs:
  - q: "Why does my Acer laptop keep rolling back Windows updates?"
    a: "Acer machines ship with Acer Care Center services, custom power and touchpad drivers, and model-specific audio packages that Windows Update must migrate during feature updates. When one of these OEM components conflicts with the incoming build, the installer aborts and reverses. Updating drivers through Acer Care Center or Acer's support site before running Windows Update prevents the majority of these conflicts."
  - q: "Should I update Acer drivers through Windows Update or Acer's site?"
    a: "Use Acer Care Center or Acer's support site for drivers. Acer validates its packages against your model's firmware, while Windows Update can offer generic versions that fail against Acer hardware and trigger the rollback loop. Let Acer handle drivers and BIOS, and let Windows Update handle OS patches — that separation keeps both pipelines healthy."
  - q: "Does Acer's recovery partition help with update loops?"
    a: "The recovery partition is for full system recovery, not for fixing update loops, and using it wipes your files unless you choose a refresh carefully. Work through the servicing repairs in this guide first — cache resets, DISM, and driver updates resolve the loop without touching your data. Reserve recovery for cases where Windows will not boot at all."
  - q: "Can low disk space cause the undoing changes loop on Acer laptops?"
    a: "Yes, and it is especially common on Acer's budget models with small eMMC or 128 GB SSD storage. The update needs room for the staged package plus the rollback snapshot — often 10 GB or more. When space runs out mid-install, the transaction unwinds itself. Keep at least 20 GB free on C: and run Disk Cleanup's system-files option regularly on small drives."
---

Acer laptops — Aspire, Swift, Nitro, Predator — occupy every price tier, and the budget end of the range brings a specific vulnerability to the "We couldn't complete the updates, undoing changes" loop: small storage. A 128 GB SSD or 64 GB eMMC drive that is three-quarters full simply cannot stage a feature update and its rollback snapshot at the same time. Add Acer's OEM driver layer — Care Center services, custom touchpad and audio drivers — and you have the two most common triggers sitting side by side. This is doubly true on Acer's entry-level models, where small eMMC drives and lean driver support make the update process less forgiving of neglect.

The diagnostic order on an Acer therefore starts with the cheapest checks: disk space and the Acer driver stack. Those two resolve the loop more often than any servicing-stack surgery. Only after they check out do you move to cache resets, DISM repairs, and the heavier tools. Work through the steps below in sequence, and note the failed KB and error code in Update history before you begin — that code focuses everything that follows.

Keep the charger connected throughout, and if the machine is currently on the rollback screen, give it 30 to 60 minutes with an eye on the disk activity light before deciding it is stuck.

## Why this happens

- **Insufficient disk space on small drives:** budget Acer models with 128 GB SSDs or eMMC storage run out of staging room mid-install.
- **Acer OEM drivers conflicting with migration:** Care Center services and model-specific drivers resisting replacement during feature updates.
- **Outdated Acer BIOS firmware:** prerequisite failures on recent Windows 11 builds that abort the install silently.
- **A corrupted update cache:** interrupted downloads on unstable Wi-Fi failing integrity checks.
- **Third-party antivirus locking files:** security suites intercepting the file replacements the installer needs.
- **Pending operations from a previous update:** an unfinished earlier update leaving the servicing stack inconsistent.
- **A specific KB with a known issue:** occasionally the package itself is broken for certain hardware configurations.
- **Acer background utilities holding files:** Quick Access and Care Center services locking files or registry keys the installer needs to replace during migration.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Free disk space first — the Acer priority check

On small-drive Acers, this single step resolves the loop outright more often than any other.

1. Open Settings, then System, then Storage, and check free space on C:.
2. Run Disk Cleanup as administrator, click "Clean up system files," and select Windows Update Cleanup, Temporary files, and Previous Windows installations.
3. Uninstall applications you do not use and move large personal files to external storage or the cloud.
4. Confirm at least 20 GB free before retrying the update.
5. Turn on Storage Sense so the drive does not silently fill again. Space-related update stalls share DNA with machines [stuck on the restarting screen](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-on-lenovo-laptop/).

### Fix 2: Update the Acer stack through Care Center

Bring Acer's own drivers current before Windows Update tries to migrate them.

1. Open Acer Care Center and run its update check; install all offered drivers.
2. Prioritize chipset, storage, and BIOS/firmware entries.
3. Alternatively, download drivers for your exact model from Acer's support site.
4. Install BIOS updates with the charger connected and nothing else running.
5. Reboot, then run Windows Update. If the troubleshooter acts up, the [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-acer-laptop/) covers the manual path.
6. If Care Center shows no updates but a driver still fails in Windows Update, download that driver manually from Acer's support site using your serial number — the app's catalog occasionally lags behind the website.

### Fix 3: Run the Windows Update troubleshooter

Clear the generic blockages automatically once space and drivers are handled.

1. Go to Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Run the Windows Update troubleshooter and apply every recommended fix.
3. Restart the laptop.
4. Check for updates again.

### Fix 4: Reset the update cache

A corrupted SoftwareDistribution folder fails the same package identically on every retry.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the services and reboot.
5. Retry Windows Update on a stable connection. Microsoft documents this reset on its [update support pages](https://support.microsoft.com/en-us/windows).

### Fix 5: Repair the component store with DISM and SFC

When the WinSxS store is damaged, no package stages cleanly.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Wait 10 to 30 minutes for completion.
3. Run `sfc /scannow` and let it verify protected files.
4. Reboot and retry the update.

### Fix 6: Strip peripherals and security interference

External factors that cost minutes to eliminate.

1. Disconnect all USB devices, docks, and SD cards.
2. Temporarily disable third-party antivirus (Windows Security stays on).
3. Disconnect any VPN.
4. Retry the update in this minimal state.
5. Re-enable security software after success.

### Fix 7: Hide the failing update or repair-install Windows

Quarantine a repeat-offender KB, or rebuild the servicing stack if failures span packages.

1. Note the failing KB in Update history.
2. Hide it with Microsoft's show-or-hide updates troubleshooter.
3. If rollbacks persist across KBs, download the Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
4. Mount the ISO, run setup.exe, choose "Keep personal files and apps," and allow 30 to 90 minutes.
5. Afterward, update Acer drivers first, then Windows updates — and keep that 20 GB of free space guarded.

## Closing

On Acer laptops, the undoing-changes loop is a space story first and a driver story second — check both before anything exotic. Budget models with small drives need active storage hygiene, and every Acer benefits from Care Center updates running ahead of Windows feature updates. With those two habits in place, the rollback screen becomes a rarity instead of a routine. On machines with soldered eMMC storage that can never be upgraded, this discipline matters even more: the drive will never get bigger, so your habits have to.
