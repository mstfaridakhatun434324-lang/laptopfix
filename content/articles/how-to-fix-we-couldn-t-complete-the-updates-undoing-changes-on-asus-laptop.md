---
title: "'We Couldn't Complete the Updates, Undoing Changes' on an ASUS Laptop — Fixed Step by Step"
slug: how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-asus-laptop
date: 2026-09-10
categories: ["windows-update"]
tags: ["asus laptop", "couldn't complete updates", "undoing changes", "myasus", "windows 11"]
description: "ASUS laptop looping on 'We couldn't complete the updates, undoing changes'? Fix it with ASUS-specific driver and BIOS steps plus proven Windows repairs."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-asus-laptop.webp"
faqs:
  - q: "Why does my ASUS laptop keep undoing Windows updates?"
    a: "ASUS laptops carry a thick OEM software layer — MyASUS services, Armoury Crate on gaming machines, ASUS-tuned audio and touchpad drivers — that collides with Windows Update's driver migration during feature updates. When one ASUS component fails to migrate cleanly, the installer aborts and rolls back. Updating everything through MyASUS before running Windows Update removes most of these collisions."
  - q: "Should I use MyASUS or Windows Update for drivers?"
    a: "MyASUS wins for drivers on ASUS hardware. ASUS tests its driver packages against its own firmware, while Windows Update periodically offers generic substitutes that misbehave on ASUS machines — which is precisely what triggers this rollback cycle. The healthy split: MyASUS manages drivers and firmware, Windows Update manages OS patches. Running both at once is asking for a fight."
  - q: "Can Armoury Crate cause Windows updates to fail?"
    a: "Yes, it contributes on ROG and TUF models. Armoury Crate installs deep services for fan curves, power plans, and device lighting that hook the OS at a low level, and those hooks can block file replacements the installer needs. If feature updates keep rolling back on a gaming ASUS, try switching off Armoury Crate's startup services for the update attempt."
  - q: "How do I update the BIOS on an ASUS laptop safely?"
    a: "Fetch the BIOS file for your exact model from ASUS support, or use the BIOS update feature inside MyASUS. Keep the charger connected, close every application, and leave the machine completely alone during the flash — an interrupted BIOS update can brick the motherboard. It takes a few minutes and the laptop reboots itself. Only flash when you have a reason, like update failures or a documented compatibility fix."
---

ASUS laptops — VivoBook, ZenBook, ROG, TUF Gaming — arrive at every Windows update with a heavy proprietary entourage: MyASUS background services, the ASUS System Control Interface driver, ASUS-tuned audio and touchpad packages, and on gaming models, Armoury Crate with its deep hooks into fan control, power profiles, and lighting. When a Windows 11 feature update starts migrating that entourage and one member digs in its heels, the installer calls off the migration and you land on "We couldn't complete the updates, undoing changes."

The order of operations is what matters here. Let the rollback run its course — it is shielding your system, not damaging it. Then bring the ASUS side up to date through MyASUS before Windows Update gets a turn, because an update that never has to wrestle ASUS's own drivers is an update that typically sails through. The generic servicing repairs below close out whatever remains. Take them in order.

Plug in the charger and leave it there for the whole process. ASUS gaming laptops especially can pull serious power while finalizing updates, and losing power mid-transaction is the one error that converts a harmless rollback into an actual problem.

## Why this happens

- **MyASUS services fighting the migration:** ASUS's own services and the System Control Interface driver refusing to be replaced mid-upgrade.
- **Armoury Crate's deep hooks:** low-level services for fans, power, and lighting blocking the file replacements the installer needs.
- **A stale ASUS BIOS:** firmware prerequisites on recent Windows 11 builds failing without an explicit error.
- **A damaged update cache:** interrupted downloads failing integrity validation and killing the transaction.
- **Too little free space:** the staged payload plus its rollback snapshot requires 10 to 20 GB.
- **Third-party antivirus getting in the way:** kernel-level security suites locking files during installation.
- **Leftovers from a previous update:** an unfinished earlier update leaving the servicing stack in an inconsistent state.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback finish, then pull the error code

The rollback is working in your favor — let it complete, then read what it recorded.

1. Keep the charger attached and let the "undoing changes" screen sit for 30 to 60 minutes, keeping an eye on storage activity.
2. Back on the desktop, open Settings, then Windows Update, then Update history.
3. Write down the failed KB number and its error code.
4. If the machine refuses to reach the desktop at all, start with our ASUS [stuck undoing-changes guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-asus-laptop/) instead.

### Fix 2: Update the ASUS stack first with MyASUS

This is the highest-value ASUS-specific move — refresh ASUS's own software before Windows attempts to migrate it.

1. Open MyASUS, head to System Update, and install every offered driver and firmware package.
2. Give priority to the ASUS System Control Interface, chipset, and BIOS entries.
3. On ROG and TUF machines, update Armoury Crate itself — recent versions migrate far more gracefully.
4. Reboot once the MyASUS batch is done.
5. Only then run Windows Update. If the troubleshooter acts up along the way, the general [troubleshooter repair pattern](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-acer-laptop/) applies here too.

### Fix 3: Silence Armoury Crate and ASUS background services for the update

On gaming models, Armoury Crate's services are the usual migration blocker. Muting them for a single update cycle is harmless and fully reversible.

1. In Armoury Crate, switch off its startup launch — or use Task Manager's Startup tab to disable the ASUS services temporarily.
2. Reboot so those services never load.
3. Run Windows Update and install the pending updates.
4. Switch the ASUS services back on afterward and reboot once more.
5. If updates now succeed reliably, keep the habit of muting them during future feature updates.

### Fix 4: Clear the Windows Update cache

A damaged SoftwareDistribution folder fails the same package identically on every attempt, no matter how current your ASUS drivers are.

1. Open an elevated Command Prompt and stop the update services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`, then restart the services and reboot.
3. Run Windows Update again on a reliable connection — Microsoft documents this exact reset on its [update support pages](https://support.microsoft.com/en-us/windows).

### Fix 5: Mend the component store with DISM and SFC

Store corruption blocks staging for every package — fix it before the next attempt.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` (allow 10 to 30 minutes), then `sfc /scannow` to verify the protected files.
2. Reboot and retry the update.

### Fix 6: Refresh the BIOS and reclaim disk space

Two environmental fixes that dissolve a surprising share of ASUS rollback loops.

1. Check your BIOS version in MyASUS or System Information, then compare it with the newest release on ASUS support for your exact model.
2. If it is behind, flash the BIOS with the charger connected and nothing else running — never interrupt it.
3. Run Disk Cleanup as administrator and make sure C: holds at least 20 GB free.
4. Unplug USB peripherals and switch off third-party antivirus while the update runs.
5. Retry Windows Update in this clean, current state.

### Fix 7: Hide the offending update or repair-install Windows

Quarantine a KB that keeps failing, or rebuild the servicing stack if rollbacks span multiple packages.

1. Note the failing KB number in Update history.
2. Hide it using Microsoft's show-or-hide updates troubleshooter.
3. If rollbacks span multiple KBs, fetch the Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, start setup.exe, select "Keep personal files and apps", and set aside 30 to 90 minutes.
5. Afterward, update through MyASUS first, then Windows Update.

## Closing

On ASUS machines, the undoing-changes loop is usually a standoff between Windows Update and the ASUS software stack — and the standoff ends once ASUS's side is current. Keep MyASUS updates ahead of Windows feature updates, mute Armoury Crate during the big installs, and keep the standard servicing repairs in your back pocket. The rollback screen stops showing up when there is nothing left for the installer to collide with.
