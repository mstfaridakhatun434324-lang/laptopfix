---
title: "'We Couldn't Complete the Updates, Undoing Changes' on a Lenovo Laptop — Fixed"
slug: how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-lenovo-laptop
date: 2026-09-07
categories: ["windows-update"]
tags: ["lenovo laptop", "couldn't complete updates", "undoing changes", "windows 11", "lenovo vantage"]
description: "Lenovo laptop stuck in the 'We couldn't complete the updates, undoing changes' loop? Use Lenovo-specific drivers, BIOS, and Vantage tools plus standard repairs to break it."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-lenovo-laptop.webp"
faqs:
  - q: "Why do Lenovo laptops hit the undoing changes loop so often?"
    a: "Lenovo ships a deep driver stack — Vantage services, custom power management, touchpad and thermal drivers — that Windows Update sometimes tries to replace with generic versions mid-feature-update. When a Lenovo-specific driver refuses to migrate, the update aborts and rolls back. Keeping drivers current through Lenovo Vantage or the support site, rather than relying solely on Windows Update, prevents most of these collisions."
  - q: "Should I update drivers through Windows Update or Lenovo Vantage?"
    a: "Use Lenovo Vantage or support.lenovo.com for drivers on a Lenovo machine. Lenovo validates its driver packages against its own firmware, while Windows Update occasionally pushes a mismatched generic driver that triggers exactly this rollback loop. Let Windows Update handle OS patches and let Lenovo handle hardware drivers — that division of labor is the most stable setup."
  - q: "Can a Lenovo BIOS update fix the undoing changes loop?"
    a: "Yes, in cases where the failure is a firmware prerequisite mismatch. Recent Windows 11 builds expect current UEFI firmware for virtualization-based security and power management handoffs. If your BIOS is several versions behind, the update can fail its preflight checks and roll back. Update the BIOS from Lenovo's support page with the charger connected, then retry the Windows update."
  - q: "Is it safe to use Lenovo's Novo button during the rollback screen?"
    a: "Avoid it while the rollback is actively running — interrupting the reversal risks component-store corruption. If the screen has been frozen with no disk activity for over an hour, a single hard reset is acceptable, and the Novo button menu is a fine way to reach recovery tools afterward. But let a working rollback finish first; patience is the safer repair."
---

Lenovo laptops have their own flavor of the "We couldn't complete the updates, undoing changes" loop, and it usually traces back to the same root: Lenovo's driver stack. Between Vantage services, the ImController system interface, custom power plans, and model-specific touchpad and thermal drivers, a ThinkPad, IdeaPad, or Legion carries more OEM software into an update than a generic machine does. When Windows Update tries to migrate those drivers during a feature update and one of them resists, the transaction aborts and you get the rollback screen.

The fix strategy therefore has two tracks. Track one is the standard Windows servicing repair — cache resets, DISM, disk space — which resolves the generic causes. Track two is Lenovo-specific: current drivers and BIOS from Lenovo's own channels, Vantage's system update tool, and awareness of Lenovo utilities that can interfere. Work the list below in order; the Lenovo-specific steps are woven in where they matter most.

As always, start from observation: if the machine is currently on the undoing-changes screen, confirm the charger is connected, watch the disk activity light, and give it 30 to 60 minutes before concluding it is stuck. Most rollbacks complete on their own.

## Why this happens

- **Lenovo drivers conflicting with the update:** Vantage-related and power-management drivers that Windows Update tries to replace with generic versions.
- **Outdated Lenovo BIOS/UEFI firmware:** firmware prerequisite mismatches on recent Windows 11 builds cause silent preflight failures.
- **A corrupted update cache:** interrupted downloads that fail integrity checks and abort the transaction.
- **Lenovo ImController or Vantage services locking files:** OEM background services can hold files the installer needs to replace.
- **Too little free disk space:** the rollback snapshot plus staged update needs 10 to 20 GB of working room.
- **Third-party antivirus with kernel hooks:** security suites intercepting file operations during installation.
- **Pending servicing operations from a previous update:** an unfinished earlier update leaves the servicing stack inconsistent.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback finish, then check Update history

Do not fight the rollback — read it. The error code it leaves behind tells you which track to prioritize.

1. Keep the charger connected and give the "undoing changes" screen 30 to 60 minutes, watching the disk light.
2. Once back on the desktop, open Settings, then Windows Update, then Update history.
3. Note the failed KB number and error code — 0x800f0922, 0x80070002, and driver-specific codes each point different directions.
4. If the machine never reaches the desktop, see our guide for an [update stuck on restarting](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-on-lenovo-laptop/) before continuing.

### Fix 2: Update everything through Lenovo Vantage first

This is the highest-value Lenovo-specific step. Bringing the OEM stack current removes the most common trigger before Windows Update ever runs.

1. Open Lenovo Vantage (install it from the Microsoft Store if missing) and run System Update.
2. Install all offered driver updates, especially chipset, power management, and BIOS/firmware entries.
3. Alternatively, download drivers for your exact model from [Lenovo support](https://support.lenovo.com/us/en/).
4. For BIOS updates, keep the charger connected and do not interrupt the flash process.
5. Reboot, then run Windows Update and retry the failed package.

### Fix 3: Run the Windows Update troubleshooter

With Lenovo drivers current, clear the generic blockages the troubleshooter handles automatically.

1. Open Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Run the Windows Update troubleshooter and apply every recommended fix.
3. Restart the laptop afterward.
4. Check for updates again. If the troubleshooter will not run at all, follow the [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-lenovo-laptop/).

### Fix 4: Reset the update cache

A corrupted SoftwareDistribution folder makes the same package fail identically on every attempt, regardless of driver state.

1. Open Command Prompt as administrator.
2. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the four services and reboot.
5. Retry Windows Update on a stable connection. Microsoft documents this reset on its [update support pages](https://support.microsoft.com/en-us/windows).

### Fix 5: Repair the component store with DISM and SFC

If the WinSxS store is damaged, staging fails no matter how current your drivers are.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Wait 10 to 30 minutes for completion.
3. Run `sfc /scannow` and let it verify system files.
4. Reboot and retry the update.

### Fix 6: Free disk space and strip interference

Environmental causes are quick to eliminate and commonly the whole story on smaller SSDs.

1. Confirm at least 20 GB free on C: via Settings, then System, then Storage.
2. Run Disk Cleanup as administrator and select Windows Update Cleanup and Temporary files.
3. Disconnect all USB peripherals and docks.
4. Temporarily disable third-party antivirus (leave Windows Security on) and disconnect VPNs.
5. Retry the update in this clean state.

### Fix 7: Hide the failing update or repair-install

When one package is the repeat offender, quarantine it — or rebuild the servicing stack if failures span multiple KBs.

1. Note the failing KB in Update history.
2. Use Microsoft's show-or-hide updates troubleshooter to hide that KB.
3. If rollbacks persist across different updates, download the Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
4. Mount the ISO, run setup.exe, choose "Keep personal files and apps," and allow 30 to 90 minutes.
5. After the repair install, install Lenovo Vantage updates first, then Windows updates.

## Closing

On Lenovo machines, the undoing-changes loop is a driver story more often than not — and the cure is to let Lenovo manage its own hardware. Keep Vantage's System Update current, keep the BIOS within a version or two of latest, and give Windows Update a clean cache and enough disk space to work with. Do that, and the rollback screen becomes something you read about rather than stare at.
