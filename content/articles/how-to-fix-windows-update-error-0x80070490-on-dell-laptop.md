---
title: "How to Fix Windows Update Error 0x80070490 on a Dell Laptop"
slug: how-to-fix-windows-update-error-0x80070490-on-dell-laptop
date: 2026-09-14
categories: ["windows-update"]
tags: ["0x80070490", "element not found", "dell laptop", "component store"]
description: "Error 0x80070490 on your Dell means a required update element is missing. Repair the component store and reset updates to fix it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070490-on-dell-laptop.webp"
faqs:
  - q: "What does Windows Update error 0x80070490 mean?"
    a: "It means 'element not found.' The update engine went looking for a specific component — a manifest, a package registration, or a store entry — and it was not there. This points at component store damage or a broken update database rather than a bad download, which is why the fixes focus on DISM repairs and database rebuilds."
  - q: "Is 0x80070490 related to the Microsoft Store?"
    a: "The same code appears in Store errors, but in a Windows Update context it is a servicing problem, not a Store problem. Do not chase Store fixes for an update error — the component store (WinSxS) and the update database are the relevant targets, and the repairs below address exactly those."
  - q: "Can 0x80070490 be caused by a failed feature update?"
    a: "Yes, commonly. A feature update that rolled back partway can leave the component store with references to elements from the new build that were never fully installed. Every subsequent cumulative update then trips over the missing elements. The DISM restore-health repair is specifically designed to reconcile this kind of store inconsistency."
  - q: "Will I need to reinstall Windows for 0x80070490?"
    a: "Almost certainly not. DISM's restore-health operation rebuilds the component store from known-good sources and resolves this error in the great majority of cases. Reinstallation is only on the table if DISM itself fails and reports the store as unrepairable — which is rare and usually indicates deeper disk problems."
---

Error 0x80070490 — "element not found" — means Windows Update reached into its component store for something a package needs and came up empty. On Dell laptops this frequently follows a rolled-back feature update that left the store referencing components from a build that never finished installing. Every update after that fails the same way until the store is reconciled.

The repair ladder here is: clear the update database, repair the component store with DISM (the heavy hitter for this code), verify with SFC, and fall back to manual installation. This error responds well to methodical repair — it is specific enough that the right fix is knowable.

The component store is Windows' strangest and most important database: tens of thousands of files, hard-linked into place, versioned so multiple updates can coexist. "Element not found" means that database's internal ledger disagrees with its shelves — it recorded something it does not actually have. DISM exists specifically to audit that ledger against known-good sources and reconcile the differences. Understanding this makes the fix order obvious: you audit the ledger (DISM) before you blame the librarian (the update database).

## Why this happens

- **Component store (WinSxS) inconsistency** — manifests reference elements that are missing or damaged.
- **Rolled-back feature update** leaving store entries from the newer build behind.
- **Corrupted update database (DataStore.edb)** with broken package registrations.
- **Missing update manifests** in the servicing stack's bookkeeping.
- **Disk errors** damaging store files after they were written correctly.
- **Interrupted cumulative update** leaving partial package registrations.
- **Third-party cleanup tools** deleting WinSxS contents they should not have touched.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Note the failing update and run the troubleshooter

1. Open **Settings** > **Windows Update** > **Update history** and note the KB number and confirm the 0x80070490 code.
2. Run **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update**.
3. Apply its fixes and restart, then retry.
4. The troubleshooter sometimes resolves the database side of this error on its own. Microsoft's [Windows Update support page](https://support.microsoft.com/en-us/windows) covers the standard flow.

### Fix 2: Reset the update database

1. Open an elevated Command Prompt and stop the services:
   `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`
2. Rename the caches:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
3. Restart the services and reboot.
4. This rebuilds the DataStore database with its package registrations — the "element not found" can live here rather than in the store itself. Full walkthrough: [resetting update components](/articles/how-to-reset-windows-update-components-in-windows-11-24h2/).

### Fix 3: Repair the component store with DISM

1. In an elevated Command Prompt, run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
2. Allow 15–30 minutes; DISM compares your store against known-good sources and repairs inconsistencies.
3. If DISM reports it repaired the store, restart immediately.
4. This is the definitive fix for 0x80070490 in most cases — the error is literally about store elements, and DISM is the store repair tool.

### Fix 4: Verify with SFC and check the store health

1. After DISM, run:
   `sfc /scannow`
2. Then check store health explicitly:
   `DISM /Online /Cleanup-Image /CheckHealth`
3. If CheckHealth reports healthy and SFC found no violations, the store is reconciled.
4. Restart and retry the failed update. If it still fails with the same code, the problem is narrower than the store — continue.

### Fix 5: Manually reset the Catroot2 and re-register servicing DLLs

1. With services stopped (as in Fix 2), also re-register the servicing components:
   `regsvr32.exe /s wuapi.dll`
   `regsvr32.exe /s wuaueng.dll`
   `regsvr32.exe /s wups2.dll`
2. Delete (not rename, this time) the contents of the rebuilt `SoftwareDistribution\Download` to force completely fresh downloads.
3. Restart services and reboot.
4. Corrupted servicing registrations can mimic store damage; this rules that out. Related: [fixing service startup failures](/articles/how-to-fix-windows-update-error-0x80070422-on-dell-laptop/).

### Fix 6: Update Dell firmware and drivers

1. Open **Dell SupportAssist** and install pending BIOS, chipset, and storage driver updates from [Dell Support](https://www.dell.com/support).
2. Outdated storage drivers are a known contributor to store corruption during updates — the files get written wrong.
3. Restart after Dell's updates, then retry the Windows update.
4. If chkdsk has never been run on this machine, run `chkdsk C: /f` too — store damage from disk errors will recur until the disk is checked.

### Fix 7: Manual install of the failing KB

1. Download the KB from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
2. Run the `.msu` and restart when prompted.
3. Confirm it in **Update history**.
4. Manual installation uses the repaired store directly, bypassing the database layer. Once one update installs cleanly through the repaired store, subsequent automatic updates typically work — verify with a **Check for updates**. For recurring monthly patterns, see [cumulative update failure repairs](/articles/how-to-fix-monthly-cumulative-update-failed-on-windows-11/).

### Fix 8: Use an in-place upgrade as the final reconciliation

When DISM cannot reconcile the store, replace the store wholesale with an in-place upgrade.

1. Download the Windows 11 ISO from Microsoft's Windows 11 download page and mount it.
2. Run `setup.exe` with **Keep personal files and apps**.
3. The repair install builds a fresh, consistent component store from the ISO's known-good sources.
4. Retry the failed update afterward — with a pristine store, the missing-element error cannot recur from the old damage. This is the definitive endpoint for store corruption.

## Closing

0x80070490 on a Dell is the component store telling you something is missing — and DISM's restore-health is built exactly for that. Reset the database, repair the store, verify, and the missing elements get reconciled. It is one of the more technical-sounding update errors, but its fix is among the most reliable. Component store damage is the deep water of Windows repair, but it is navigable: audit with DISM, verify with SFC, and replace the store when auditing fails. Few errors survive all three — and the machine that emerges has a healthier store than it has had in years.
