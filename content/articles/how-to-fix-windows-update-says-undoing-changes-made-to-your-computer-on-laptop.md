---
title: "Windows Update Says 'Undoing Changes Made to Your Computer' on Your Laptop — What to Do"
slug: how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-on-laptop
date: 2026-09-04
categories: ["windows-update"]
tags: ["undoing changes", "windows update", "laptop update failed", "update rollback", "windows 11"]
description: "Your laptop is stuck saying 'Undoing changes made to your computer' during Windows Update. Here is a technician's ordered plan to get past it safely."
thumbnail: "/images/thumbs/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-on-laptop.webp"
faqs:
  - q: "Should I keep my laptop plugged in during the undoing changes screen?"
    a: "Yes, absolutely. A rollback is disk-intensive work, and losing power mid-transaction is one of the few things that can genuinely corrupt the component store and leave the machine unbootable. Plug into AC power, confirm the charging light is on, and leave it alone. Battery-only rollbacks on a low charge are a real risk, so this is the one step you should never skip."
  - q: "The screen has been showing for two hours. Is it stuck?"
    a: "Probably, but verify before acting. Check the disk activity light: steady blinking means the rollback is still working, and some older laptops legitimately need 90 minutes. No light and no fan noise for over an hour means the process has stalled. At that point, one controlled hard reset — hold power for 10 seconds, unplug USB devices, wait 30 seconds, power on — is the correct next step."
  - q: "Can I stop Windows from trying the failed update again?"
    a: "Yes. After you are back on the desktop, open Update history, note the failed KB number, and use Microsoft's show-or-hide updates troubleshooter to hide that package. Windows will install everything else normally and skip the hidden one. Unhide it after a revised version is released or after you have fixed the underlying cause, such as a driver conflict."
  - q: "Does the undoing changes screen mean my laptop is damaged?"
    a: "No. It means the update installer detected a failure and chose to reverse its changes rather than leave the system half-updated. The hardware is fine and your files are untouched. Recurring rollbacks point to a fixable software cause — a corrupted update cache, an incompatible driver, or low disk space — all covered in the steps above."
---

Laptops hit the "Undoing changes made to your computer" screen more often than desktops, and the reasons are physical as much as software. Laptops run on batteries that die mid-install, they sleep and hibernate at the worst moments, they carry OEM driver stacks from Dell, HP, Lenovo, ASUS, and Acer that do not always track Microsoft's update schedule, and their smaller SSDs fill up faster. Any one of these can turn a routine update into a rollback.

The screen itself is not the enemy. It is the servicing engine unwinding a failed update transaction — restoring system files, drivers, and registry entries from the snapshot taken before the install began. Think of it as Windows refusing to ship a broken build to your own machine. The fixes below respect that process: first you confirm whether the rollback is genuinely stuck, then you remove the cause so the next attempt succeeds.

One laptop-specific warning before you start: never let a rollback run on battery. If the screen appeared while unplugged, plug in the charger immediately. Power loss during the reversal is the fastest route from "annoying screen" to "unbootable machine," and it is entirely avoidable.

## Why this happens

- **The battery died or the lid closed mid-install:** power interruption during the update phase guarantees the transaction aborts and rolls back on next boot.
- **OEM driver stacks conflicting with the update:** laptop manufacturers layer custom power, thermal, and touchpad drivers that can fail migration during a feature update.
- **A nearly full system drive:** smaller laptop SSDs hit the space threshold faster; the installer runs out of room and unwinds.
- **Sleep or hibernate kicking in during installation:** aggressive power plans can suspend the machine mid-transaction on battery power.
- **Third-party antivirus with kernel hooks:** security suites that intercept file operations can make the installer believe files are corrupted.
- **A corrupted update cache:** interrupted downloads on flaky Wi-Fi leave staged packages that fail integrity checks.
- **Outdated BIOS or chipset drivers:** laptop firmware that predates the update's requirements can fail prerequisite checks silently.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Plug in, observe, and give it time

Most "stuck" rollbacks on laptops are simply slow, especially on older machines with spinning hard drives. The disk light is your diagnostic instrument.

1. Connect the AC adapter immediately and confirm the charging indicator lights up.
2. Open the lid if it is closed — some laptops pause everything with the lid shut.
3. Watch the disk activity light for 30 to 60 minutes without touching the machine.
4. Blinking light plus fan noise means real work; leave it alone until the desktop or login screen appears. This patience-first approach also resolves many cases of an [update stuck on restarting](/articles/how-to-fix-windows-update-stuck-on-restarting-after-windows-11-update/).

### Fix 2: Perform one controlled hard reset if it is truly frozen

Only after an hour with zero disk activity. A single clean power-cycle lets Windows re-attempt the rollback or boot into recovery on its own terms.

1. Verify no disk light and no fan activity for at least 30 consecutive minutes.
2. Hold the power button for a full 10 seconds until the laptop shuts off.
3. Unplug all USB devices, docks, SD cards, and external monitors.
4. Remove the charger for 30 seconds if the battery is removable or the model supports a hard reset via pinhole; otherwise just wait.
5. Reconnect power and boot. Back up your files first thing if the desktop loads.

### Fix 3: Boot into Safe Mode and run the update troubleshooter

Safe Mode sidesteps the third-party drivers that commonly trigger laptop rollbacks, giving you a clean environment to repair the update pipeline.

1. Interrupt the boot twice at the Windows logo to reach Automatic Repair.
2. Go to Troubleshoot, then Advanced options, then Startup Settings, then Restart, and press 4 for Safe Mode.
3. Open Settings, then System, then Troubleshoot, then Other troubleshooters, and run the Windows Update troubleshooter.
4. Apply all recommended fixes. If the troubleshooter will not run, see the guide for a [broken update troubleshooter](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-dell-laptop/).
5. Restart normally and attempt the update again.

### Fix 4: Reset the update cache from an elevated prompt

Laptop Wi-Fi dropouts are a prime source of corrupted staged downloads. Clearing the cache forces a fresh, verified download.

1. Open Command Prompt as administrator.
2. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the four services with `net start` and reboot.
5. Run Windows Update on a stable connection — preferably wired or strong Wi-Fi — and let it re-download. Microsoft's [update support pages](https://support.microsoft.com/en-us/windows) describe this reset as the standard fix for repeated failures.

### Fix 5: Repair system files with DISM and SFC

Repeated rollbacks can leave the component store itself inconsistent. Repair it before the next attempt.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Wait 10 to 30 minutes for it to complete; do not close the window.
3. Run `sfc /scannow` and let it verify protected files.
4. Reboot when both finish.
5. Check Windows Update again.

### Fix 6: Update OEM drivers and free disk space

Laptop-specific drivers and cramped SSDs are the two causes desktops rarely share. Address both before retrying.

1. Visit your manufacturer's support site (Dell, HP, Lenovo, ASUS, or Acer) and install the latest chipset, graphics, and storage drivers for your exact model.
2. Check for a BIOS update and install it with the charger connected, following the instructions precisely.
3. Run Disk Cleanup as administrator and remove Windows Update Cleanup files and temporary files.
4. Confirm at least 20 GB free on C: before retrying.
5. Temporarily disable third-party antivirus during the update attempt, then re-enable it.

### Fix 7: Hide the failing update or repair-install Windows

If one KB is the repeat offender, stop it from retrying while you wait for a revised package — or repair the servicing stack wholesale.

1. Note the failing KB in Update history.
2. Run Microsoft's show-or-hide updates troubleshooter and hide that KB.
3. If rollbacks continue across different KBs, download the Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
4. Mount the ISO, run setup.exe, and choose "Keep personal files and apps."
5. After the repair install completes, updates should proceed normally.

## Closing

On a laptop, the undoing-changes screen is usually a story about power, space, or OEM drivers — the three things that make portable machines different from desktops. Keep the charger connected, keep 20 GB free, and keep manufacturer drivers current, and most update loops never start. When one does start, resist the urge to hammer the power button: observe first, intervene second, and work this list top to bottom.
