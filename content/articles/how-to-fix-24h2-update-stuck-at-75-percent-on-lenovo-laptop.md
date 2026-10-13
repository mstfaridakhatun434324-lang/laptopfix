---
title: "24H2 Update Stuck at 75 Percent on a Lenovo Laptop: Unsticking It"
slug: how-to-fix-24h2-update-stuck-at-75-percent-on-lenovo-laptop
date: 2026-09-20
categories: ["windows-update"]
tags: ["24h2", "stuck at 75", "lenovo laptop", "feature update"]
description: "The 24H2 update is frozen at 75% on your Lenovo laptop? Learn what the installer is doing at that stage and how to get it moving again."
thumbnail: "/images/thumbs/how-to-fix-24h2-update-stuck-at-75-percent-on-lenovo-laptop.webp"
faqs:
  - q: "What is the 24H2 installer doing at 75 percent?"
    a: "Around the three-quarter mark, the installer is typically in the driver migration and second-boot phases — moving your drivers to the new build and configuring devices. On Lenovo laptops this is the heaviest driver-migration workload of the whole install, because Lenovo's driver stack is deep. A stall here almost always means a driver that will not migrate."
  - q: "How long should I wait at 75 percent before acting?"
    a: "Give it at least two hours of zero progress with zero disk activity before intervening. Driver migration on a mechanical hard drive can legitimately take a very long time, and the percentage display is not linear — 75 percent can represent a long phase. Watch the disk light: activity means progress, even if the number never moves."
  - q: "Will interrupting the stuck install damage my Lenovo?"
    a: "Windows is designed to roll back an interrupted feature update to your previous build, and it usually does so cleanly. The risk is small but real — repeated interruptions compound partial states. One careful power cycle after confirming a genuine stall is the accepted recovery, followed by fixing the driver cause before retrying."
  - q: "Why 75 percent specifically on Lenovo laptops?"
    a: "The percentage where an install stalls reflects which phase is struggling, and Lenovo's heavy driver stack makes the migration phase the bottleneck. Lenovo-specific drivers — power management, hotkeys, thermal controls, Vantage components — all migrate in this window. An outdated or corrupted one stalls the whole phase at roughly the same percentage across machines."
---

A feature update freezing at exactly 75 percent is one of the more specific failure signatures in Windows — and specificity is useful, because it tells you where the installer is stuck. At the three-quarter mark of the 24H2 install, the process is deep in driver migration: moving your existing drivers onto the new build and configuring every device for it.

On Lenovo laptops, that phase carries an unusually heavy load. Lenovo's driver stack — power management, hotkey controls, thermal drivers, Vantage components — is deeper than most manufacturers', and every one of those drivers must migrate. When one will not, the installer waits. The sequence below starts with the critical assessment (is it stuck or just slow?), then works through recovery and the driver fixes that prevent a repeat. The [61-percent stall guide](/articles/how-to-fix-feature-update-stuck-at-61-percent-on-lenovo-laptop/) covers the earlier-phase variant of the same problem.

## Why this happens

- **Driver migration stall:** A Lenovo driver that cannot migrate blocks the whole phase.
- **Corrupted driver package:** A damaged driver in the store fails migration repeatedly.
- **Antivirus filter deadlock:** Security drivers blocking the migration's file operations.
- **Disk errors:** Bad sectors encountered during the migration's heavy writes.
- **Insufficient disk space:** Migration needs working room; a full drive stalls it silently.
- **Pending Lenovo firmware:** A half-installed BIOS or firmware update confusing device enumeration.
- **Power interruption risk:** Battery sag on an unplugged laptop freezing the process mid-migration.
- **Corrupted migration state:** A previous interrupted attempt left state the current one cannot reconcile.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall before touching anything

The 75-percent phase is legitimately slow — confirm it is dead, not working.

1. Watch the disk activity light for a full hour: any flickering means migration is progressing.
2. Listen for fan and disk sounds — sustained activity is a good sign.
3. If there is any activity at all, wait another hour; mechanical drives can take three hours in this phase.
4. Only act when there has been zero activity for two full hours.
5. Note the exact behavior for later diagnosis — frozen spinner versus circling spinner matters.

### Fix 2: Power cycle and let it roll back or resume

Once the stall is confirmed, a careful restart is the standard recovery.

1. Hold the power button for ten seconds until the laptop is fully off.
2. Unplug the charger, wait thirty seconds, reconnect, and power on.
3. Windows will resume the install, roll back to the previous build, or boot normally — allow up to an hour.
4. If it rolled back, your files and previous Windows are intact.
5. Do not immediately retry 24H2 — fix the driver cause first (Fixes 3–5).

### Fix 3: Update all Lenovo drivers before retrying

This is the preventive core: migrate-ready drivers do not stall. Lenovo documents driver preparation on [Lenovo support](https://support.lenovo.com/us/en/).

1. Open **Lenovo Vantage** and install every pending driver update.
2. Pay special attention to chipset, storage, power management, and hotkey drivers.
3. Check for a BIOS update and install it with the charger connected.
4. Restart after all updates complete.
5. Only then retry the 24H2 update.

### Fix 4: Clean the driver store

Remove the corrupted or ghost drivers that stall migration.

1. Open Device Manager and enable **View > Show hidden devices**.
2. Uninstall grayed-out (non-present) devices, especially storage and system devices.
3. Open an elevated Command Prompt and run `pnputil /enum-drivers`.
4. Delete packages for hardware you no longer own.
5. Retry 24H2 with the cleaned store.

### Fix 5: Strip the system for the retry

Fewer drivers to migrate means fewer stall points. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents clean-upgrade preparation.

1. Uninstall third-party antivirus completely (not just disabled).
2. Disconnect all USB devices except keyboard and mouse; undock the laptop.
3. Uninstall VPN clients with system drivers temporarily.
4. Free disk space to at least 30 GB.
5. Retry the 24H2 install in this minimal state.

### Fix 6: Use the Installation Assistant for the retry

A different install path sometimes migrates drivers more gracefully.

1. Download the Windows 11 Installation Assistant from Microsoft.
2. Close everything and run it with the charger connected.
3. Allow up to three hours — do not use the laptop heavily during migration.
4. If it stalls at 75 percent again, the driver cause is still present — return to Fixes 3 and 4.
5. On success, verify the build and re-run Vantage driver updates.

### Fix 7: Check drive health

Repeated migration-phase stalls can signal a failing drive.

1. Once booted (by rollback or otherwise), back up your files.
2. Run `chkdsk C: /f` from an elevated Command Prompt.
3. Check SMART data with Lenovo's diagnostics.
4. If the drive is failing, replace it before further update attempts.
5. A healthy drive eliminates the whole class of stall. Also verify [optional driver updates](/articles/how-to-fix-optional-updates-not-installing-windows-11-on-lenovo-laptop/) install cleanly afterward, confirming the driver pipeline is healthy.

### Fix 8: Retry from a clean boot with the assistant

Eliminate every third-party variable for the final retry.

1. Use msconfig to disable all non-Microsoft services and all startup items.
2. Restart into the clean boot state.
3. Run the Installation Assistant as administrator.
4. Let the migration phase run undisturbed — no other programs, no sleep.
5. After success, re-enable your services and startup items, then update drivers via Vantage.

## Closing

A 24H2 stall at 75 percent on a Lenovo is the installer telling you, in its numerical way, that driver migration is the problem. The percentage is not random — it marks the phase, and the phase marks the cause. Update the Lenovo driver stack, clean the driver store, strip the peripherals, and the retry migrates smoothly. Treat the stall as diagnostic information rather than a disaster, and the second attempt is usually the last one you need.
