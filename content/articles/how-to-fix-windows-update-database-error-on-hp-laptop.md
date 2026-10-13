---
title: "Windows Update Database Error on HP Laptop? Fix It for Good"
slug: how-to-fix-windows-update-database-error-on-hp-laptop
date: 2026-10-01
categories: ["windows-update"]
tags: ["database error", "hp laptop", "datastore", "0x80070490"]
description: "Windows Update database error on your HP laptop? Combine the standard database rebuild with HP-specific driver and BIOS steps for a lasting fix."
thumbnail: "/images/thumbs/how-to-fix-windows-update-database-error-on-hp-laptop.webp"
faqs:
  - q: "Why does my HP laptop get Windows Update database errors?"
    a: "HP laptops aren't more prone to database corruption than others, but HP-specific factors complicate recovery: HP Support Assistant can fight Windows Update for driver installs, outdated HP BIOS versions cause update failures that corrupt the database, and HP's custom drivers sometimes leave inconsistent entries when they fail mid-install."
  - q: "Will HP Support Assistant fix the database error?"
    a: "Not directly — Support Assistant updates drivers and BIOS but doesn't repair the Windows Update database. However, running it AFTER the database rebuild is smart: it ensures HP drivers and BIOS are current, which prevents the driver failures that corrupted the database in the first place."
  - q: "Should I use HP's recovery tools for this?"
    a: "No — HP recovery tools reinstall Windows, which is overkill for a database error. The database rebuild in this guide fixes the problem while keeping everything installed. Save HP Cloud Recovery for genuine emergencies where Windows itself won't boot at all."
  - q: "Can an old HP BIOS cause update database corruption?"
    a: "Indirectly, yes. An outdated BIOS can cause firmware-adjacent updates and driver installs to fail partway, and those interrupted installs are what corrupt the database. Updating the BIOS after rebuilding the database breaks this corruption cycle on affected HP models."
---

# Windows Update Database Error on HP Laptop? Fix It for Good

A Windows Update database error is the same beast on every PC — a corrupted ledger of what's installed and what's pending. But on an HP laptop, the recovery has an extra dimension: HP's driver ecosystem (Support Assistant, custom drivers, BIOS delivery) interacts with Windows Update in ways that can both cause the corruption and complicate the fix. Treat it as a generic database error and you'll fix it today and see it again next month.

This guide does both jobs: the standard database rebuild that fixes the immediate error, plus the HP-specific steps — Support Assistant, BIOS, driver hygiene — that keep it from coming back. Do them in this order.

## Why this happens

- **Corrupted DataStore from interrupted updates.** Power loss or forced shutdowns mid-install damage the update ledger.
- **HP Support Assistant vs. Windows Update conflicts.** Both installing drivers simultaneously leaves inconsistent database entries.
- **Failed HP driver installs.** HP's customized drivers failing partway through corrupt the rows tracking them.
- **Outdated HP BIOS.** Firmware-adjacent update failures cascade into database corruption.
- **Disk errors on the system drive.** Bad sectors hitting the database file damage it directly.
- **Antivirus locking database files.** Real-time scanning interfering with database writes.
- **Aggressive cleaner utilities.** Third-party tools purging update caches the database still references.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the Error and Run the Troubleshooter

Verify you're dealing with a database error, not a lookalike.

1. Note the exact error code in **Settings > Windows Update** — 0x80070490 and 0x80070003 point at the database.
2. Run the Windows Update troubleshooter (**Settings > System > Troubleshoot > Other troubleshooters**).
3. If it reports a database error and fixes it, retry updates immediately — minor corruption sometimes yields here.
4. Check whether HP Support Assistant is also showing update errors — dual failures suggest a driver conflict underlying the corruption.
5. If the troubleshooter fails or the error returns, proceed to the manual rebuild.

### Fix 2: Pause HP Support Assistant During the Repair

HP's updater must not fight you while you rebuild — sideline it temporarily.

1. Open HP Support Assistant and pause or disable automatic updates within it.
2. Alternatively, close it completely and prevent it from launching at startup via Task Manager's **Startup apps** tab.
3. This isn't permanent — you'll re-enable it in Fix 6 after the database is healthy.
4. The goal: exactly one update pipeline (Windows Update) active during the rebuild.
5. Note which HP driver updates were pending — you'll address them deliberately later, not in a scrum.

### Fix 3: Rebuild the Update Database

The core repair — identical in mechanics to the generic fix, but done with HP's updater sidelined.

1. Open an elevated Command Prompt.
2. Stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
3. Rename the stores:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`, `net start msiserver`.
5. Run **Check for updates** and let the extended first scan rebuild the database completely. The generic [database error walkthrough](/articles/how-to-fix-windows-update-database-error-on-windows-10/) covers the theory if you want deeper background.

### Fix 4: Update the HP BIOS

An outdated BIOS is the HP-specific root cause behind many recurring database corruptions — fix it now while the database is fresh.

1. Open HP Support Assistant (temporarily re-enable it) or visit [HP's support site](https://support.hp.com/us-en) and enter your exact model/serial.
2. Download the latest BIOS for your model and read HP's instructions.
3. Flash on AC power with all applications closed — never on battery.
4. After the flash, boot into BIOS (F10 or Esc at startup on most HPs) and load defaults, then save.
5. A current BIOS eliminates the firmware-level update failures that were corrupting your database entries.

### Fix 5: Let HP Support Assistant Update Drivers — After Windows Update

Now reintroduce HP's updater in the right order: Windows Update first, HP drivers second.

1. In **Settings > Windows Update**, install all pending Windows updates and reboot.
2. Confirm update history shows success across the board — the rebuilt database should now track cleanly.
3. Now open HP Support Assistant and install its recommended driver and firmware updates.
4. Reboot again after HP's updates complete.
5. This sequencing — Windows first, HP second — prevents the simultaneous-install conflicts that corrupted the database originally.

### Fix 6: Check Disk Health and Repair System Files

Rule out the hardware and OS damage that makes database corruption recur.

1. Open an elevated Command Prompt and run `chkdsk C: /f` (reboot to let it run).
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`.
3. If chkdsk reports bad sectors, back up immediately — a failing drive will corrupt every database you rebuild.
4. Restart after repairs and run **Check for updates** once more to confirm stability.
5. If corruption returns despite a healthy disk, suspect a [servicing stack problem](/articles/how-to-fix-servicing-stack-update-failed-on-hp-laptop/) underneath — the SSU and the database fail together more often than people realize.

### Fix 7: Establish Update Hygiene Going Forward

Prevent the next corruption with habits tailored to HP's dual-updater reality.

1. Never run HP Support Assistant updates and Windows Update simultaneously — sequence them, Windows first.
2. Keep 15–20GB free on the system drive at all times.
3. Never force-shutdown during updates — let "Working on updates" screens finish, however long they take.
4. Keep HP Support Assistant itself updated — old versions are buggier about conflicting with Windows Update.
5. After a month of clean update cycles, delete the `.old` backup folders from Fix 3 to reclaim the space.

## Closing

On HP laptops, Windows Update database errors need the standard rebuild plus HP-specific follow-through: sideline Support Assistant during the repair, update the BIOS, then sequence Windows and HP updates properly. The database rebuild fixes today; the HP hygiene prevents tomorrow. Do both and the error stays gone.
