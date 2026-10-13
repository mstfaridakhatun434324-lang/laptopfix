---
title: "Fix the Windows Update Database Error on Windows 11"
slug: how-to-fix-windows-update-database-error-after-windows-11-update
date: 2026-09-04
categories: ["windows-update"]
tags: ["update database error", "windows 11", "0x80070490", "datastore corrupt"]
description: "Seeing a Windows Update database error after a Windows 11 update? Repair the corrupt update database with these proven, step-by-step fixes."
thumbnail: "/images/thumbs/how-to-fix-windows-update-database-error-after-windows-11-update.webp"
faqs:
  - q: "What is the Windows Update database?"
    a: "It is the DataStore database inside the SoftwareDistribution folder that tracks every update's download state, installation history, and metadata. When this database corrupts, the update client cannot read its own records and reports a database error instead of scanning normally."
  - q: "What causes the update database to corrupt?"
    a: "Interrupted scans, forced shutdowns during updates, disk errors writing to the DataStore, and antivirus quarantining update database files are the main causes. It often appears right after a feature update because the migration rewrites large parts of the store. Keeping the machine plugged in and undisturbed during updates prevents most of these causes."
  - q: "Will resetting the database delete my update history?"
    a: "Yes, the visible update history list will be cleared, but installed updates themselves remain installed. Windows rebuilds the database fresh on the next scan. Your files and apps are completely unaffected. Think of it as clearing a ledger, not deleting the transactions — the installed updates remain recorded in the system itself."
  - q: "How do I know the database is corrupt versus another problem?"
    a: "The troubleshooter explicitly reports a database error, or you see error 0x80070490, or the update scan fails instantly every time while DISM and SFC report no system damage. Instant, repeatable scan failures point at the database rather than the payload."
---

The 'Windows Update database error' message is one of the more honest errors Windows produces: it is telling you exactly what broke. The DataStore database — the ledger Windows Update keeps of every download, install, and scan — has corrupted, and the update client cannot function until the ledger is rebuilt.

This often surfaces right after a Windows 11 feature update, because the upgrade migrates the update database and any interruption or disk hiccup during that migration leaves it unreadable. The symptom is distinctive: update scans fail immediately or the troubleshooter flags the database, while the rest of Windows runs fine.

The repair is straightforward and safe: stop the services, remove the corrupt database, and let Windows rebuild it. The steps below escalate from the automatic troubleshooter to manual rebuilds and the deeper store repairs for stubborn cases.

## Why this happens

- **Interrupted database migration:** A shutdown or crash during a feature update's migration of the DataStore leaves it half-written and unreadable.
- **Disk errors:** Bad sectors or a failing drive corrupting the DataStore.edb file produce exactly this error.
- **Antivirus quarantine:** Overzealous security software occasionally quarantines update database or catalog files as suspicious.
- **Forced shutdowns during scans:** Holding the power button while Windows Update is writing its database is a reliable way to corrupt it.
- **Corrupt catroot2 catalogs:** The cryptographic catalogs that validate updates live alongside the database; damage there cascades into database errors.
- **Stuck update services:** Services wedged mid-write leave the database locked or inconsistent.
- **Third-party 'debloater' tools:** Scripts that aggressively strip Windows components sometimes delete or damage update database files.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter first

The troubleshooter detects database corruption explicitly and can rebuild the DataStore automatically — the fastest path when it works.

1. Go to Settings → System → Troubleshoot → Other troubleshooters → Windows Update → Run.
2. If it reports a database error and offers a fix, apply it and reboot.
3. Run a manual update scan. If the scan completes, you are done; if the error returns, continue.

### Fix 2: Manually rebuild the SoftwareDistribution database

This is the definitive fix: delete the corrupt database files and let Windows regenerate them cleanly.

1. Open Command Prompt as administrator.
2. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart all four services with `net start`, reboot, and check for updates — the scan will take longer as it rebuilds the database.

### Fix 3: Check the disk for errors

If the database corrupted because the disk is failing, rebuilding it just buys time. Verify the drive.

1. Run `chkdsk C: /f` from an elevated prompt and reboot to let it scan.
2. Check SMART health with your manufacturer's diagnostics.
3. If chkdsk finds and repairs bad sectors, rebuild the database again afterward — the first rebuild may have inherited the damage.

### Fix 4: Repair the component store with DISM

Database corruption sometimes accompanies component-store damage, especially after a rough feature update. Fix both.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated prompt.
2. Follow with `sfc /scannow` and reboot.
3. Retry the update scan. If DISM reports the store is healthy but the database error persists, the issue is isolated to the DataStore and Fix 2's rebuild should have resolved it — repeat Fix 2 carefully, ensuring all services were stopped.

### Fix 5: Re-register the update DLLs

When the database is fine but the client still cannot read it, the client's own components may be unregistered — common after aggressive cleanup tools.

1. Open an elevated Command Prompt.
2. Re-register the core DLLs: `regsvr32 wuapi.dll`, `regsvr32 wuaueng.dll`, `regsvr32 wups.dll`, `regsvr32 wuwebv.dll`, `regsvr32 atl.dll` — confirm each success dialog.
3. Reboot and scan again.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents additional manual reset steps if registration alone does not help.

### Fix 6: Reset the update services to a known-good state

Services stuck in a bad state can re-corrupt a fresh database. Reset their startup configuration.

1. Open `services.msc` and set Windows Update, BITS, Cryptographic Services, and Windows Installer to their defaults (Manual or Automatic as originally configured).
2. Ensure none are Disabled.
3. Reboot and run the scan. If a service immediately wedges again, the [service not running repair guide](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/) covers the deeper service-level repair.

### Fix 7: Use an in-place upgrade as the last resort

When the database corrupts again after every rebuild, the Windows installation itself is damaged beyond component repair.

1. Back up your files.
2. Mount a Windows 11 ISO matching your edition and run setup, choosing Keep personal files and apps.
3. This reinstalls Windows while preserving everything and rebuilds the entire update subsystem.
4. Afterward, the database error should be gone permanently — if it returns even now, suspect the drive hardware.

### Fix 8: Scan for malware and rogue filter drivers

Database corruption that returns after every rebuild has an active cause. Malware that patches system files and rogue disk filter drivers that corrupt writes both produce exactly this recurring pattern.

1. Run Windows Security → Virus & threat protection → Scan options → Full scan and let it complete.
2. Run a second-opinion scan with the free Microsoft Safety Scanner for anything Defender missed.
3. In an elevated prompt, run `fltmc` to list file-system filter drivers; research any entry you do not recognize.
4. If anything malicious or unknown is found and removed, rebuild the database once more using Fix 2 — with the corruption source gone, the rebuild finally sticks.

## Closing

A Windows Update database error sounds severe, but the database is disposable by design — Windows rebuilds it from scratch whenever the corrupt copy is removed. Run the troubleshooter, rebuild the SoftwareDistribution folder manually, check the disk, and only escalate to an in-place upgrade if the corruption keeps returning. Your files and installed updates survive the whole process. If the troubleshooter is your starting point, the [Windows Update troubleshooter walkthrough](/articles/how-to-fix-windows-update-with-troubleshooter-in-windows-11-24h2/) explains exactly what its database repairs do.
