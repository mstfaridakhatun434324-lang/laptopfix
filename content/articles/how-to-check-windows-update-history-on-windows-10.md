---
title: "How to Check Windows Update History on Windows 10"
slug: how-to-check-windows-update-history-on-windows-10
date: 2026-10-02
categories: ["windows-update"]
tags: ["update history", "windows 10", "installed updates", "kb updates"]
description: "Need to see which updates installed on your Windows 10 laptop — or which failed? Here are 4 reliable ways to check your full update history."
thumbnail: "/images/thumbs/how-to-check-windows-update-history-on-windows-10.webp"
faqs:
  - q: "Where is the update history stored on Windows 10?"
    a: "Your update history is stored in the Windows Update database and shown in Settings under Update & Security > Windows Update > View update history. The same records appear in Control Panel's Installed Updates list and can be queried with PowerShell commands, so you have several independent ways to review what installed, when, and whether it succeeded or failed."
  - q: "Why does my update history show a failed update?"
    a: "A failed entry usually means the download was interrupted or the install hit an error and rolled back. The history keeps the failure record so you can identify the KB number and troubleshoot it. If the same update keeps failing, see our guide on [update troubleshooter problems](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-windows-10/) for the standard fix sequence."
  - q: "Can I delete Windows 10 update history?"
    a: "You can clear the displayed history by resetting the SoftwareDistribution folder, which wipes the cached records. The installed updates themselves remain on the system, though — clearing history only removes the log view. There's rarely a reason to do this unless the history database itself is corrupted and showing nonsense entries."
  - q: "Does update history show driver updates too?"
    a: "Yes. The history page has a Driver updates section listing hardware driver updates delivered through Windows Update, separate from quality and feature updates. If a device misbehaves after a listed driver update, you can roll that driver back in Device Manager without touching the rest of the updates."
---

If your Windows 10 laptop is acting strangely after Patch Tuesday, the first question a technician asks is always the same: what updated recently? The update history is your paper trail — it lists every quality update, feature update, driver update, and definition update, along with the exact date and whether each one installed cleanly or failed. Knowing how to read it turns vague "my laptop broke last week" complaints into precise, fixable problems.

This is a quick skill, but a powerful one. Once you can check the history, you can match a misbehaving driver to the day it arrived, find the KB number of a failed cumulative update, and decide whether an [update troubleshooter](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-windows-10/) or a manual reinstall is the right next step.

## Why this happens

- **You need the KB number** — Microsoft's fixes and error searches all reference KB numbers like KB5034441, and the history page is the fastest place to find yours.
- **A failure left no other trace** — Some failed updates show no notification; the history page is the only record that an install attempt even happened.
- **A driver update arrived silently** — Windows Update can push hardware drivers overnight, and the history's driver section identifies which one.
- **You're verifying a reinstall** — After fixing a broken update, the history confirms the replacement actually installed and when.
- **You're preparing to uninstall** — You can't remove the right update unless you first identify it by name, KB number, and install date.
- **Support asks for it** — Manufacturer and Microsoft support will always ask what updated just before the problem started.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check history in Settings (the easy way)

The Settings app gives you the cleanest view of recent updates, grouped by type, and it's where you should start.

1. Open Settings with Win + I, then go to **Update & Security > Windows Update**.
2. Click **View update history** under the Check for updates button.
3. Scroll through the sections: **Feature Updates**, **Quality Updates**, **Driver Updates**, and **Other Updates**.
4. Each entry shows the KB number, the install date, and the status — installed, failed, or pending.
5. Click any entry for more detail. Failed entries here give you the KB number you'll need for the manual fix in Fix 4.

### Fix 2: Use Control Panel's Installed Updates list

If you need to actually remove an update, the Settings history is read-only — you need the classic Control Panel list, which adds an Uninstall button.

1. Open Control Panel, go to **Programs > Programs and Features**, and click **View installed updates** on the left.
2. The list shows every update with its KB number, program name, version, and install date — sortable by clicking the column headers.
3. Click the **Installed On** column to sort by date and find the most recent updates instantly.
4. Right-click any update and choose **Uninstall** to remove it (useful for a bad cumulative update).
5. Note that feature updates also appear here; removing one rolls Windows back to the previous version within the 10-day window.

### Fix 3: Query update history with PowerShell

When the graphical views are slow or you want a clean list to share with support, PowerShell gives you a precise, copyable record.

1. Open PowerShell as administrator: search for **PowerShell**, right-click, and choose **Run as administrator**.
2. Run `Get-HotFix | Sort-Object InstalledOn -Descending | Format-Table HotFixID, InstalledOn, Description` for a quick list of installed patches with dates.
3. For deeper detail including failed attempts, run `wmic qfe list full /format:table` in Command Prompt instead.
4. Copy the output into a text file with `Get-HotFix | Out-File C:\update-history.txt` so you can email it to support.
5. Compare the KB numbers against Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) to read the release notes for each one.

### Fix 4: Install a failed update manually from the catalog

Once the history identifies a failed KB, the fastest fix is often to download that exact update and install it yourself, bypassing whatever broke the automatic attempt.

1. In the update history, note the exact KB number of the failed update (for example, KB5034441).
2. Visit the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and search for that KB number.
3. Download the version matching your system — x64 for most modern laptops — and run the `.msu` file.
4. Reboot when prompted, then re-check the history to confirm the status changed to successfully installed.
5. If manual install also fails, the problem is environmental (disk space, corrupted cache); you can learn the technique permanently in our [manual KB install guide](/articles/how-to-install-kb-update-manually-from-catalog-in-windows-11-24h2/).

### Fix 5: Reset the history when the database is corrupted

Sometimes the history page itself is the problem — blank entries, duplicates, or phantom failures. Resetting the update database gives you a clean slate.

1. Open an elevated Command Prompt and run `net stop wuauserv` followed by `net stop bits`.
2. Navigate to `C:\Windows\SoftwareDistribution` and delete the **DataStore** folder (this holds the history database).
3. Restart the services with `net start wuauserv` and `net start bits`.
4. Open Settings > Update & Security > Windows Update and click **Check for updates** to rebuild the database.
5. Your history will repopulate with accurate entries on the next check-in.

### Fix 6: Export and document your update baseline

For laptops you maintain long-term, keeping a written baseline makes future troubleshooting dramatically faster.

1. After confirming everything is healthy, run `Get-HotFix | Export-Csv C:\baseline.csv` in PowerShell.
2. Save the CSV somewhere safe — an external drive or cloud folder.
3. Months later, when something breaks, export again and diff the two files to see exactly what changed.
4. This five-minute habit is what separates quick fixes from hours of guessing, especially on laptops shared by a family or small office.

## Closing

Checking update history on Windows 10 takes less than a minute once you know where to look, and it's the single most useful diagnostic step in update troubleshooting. Whether you use Settings for a quick glance, Control Panel when you need to uninstall, or PowerShell for a shareable record, the history tells you exactly what changed and when — and that knowledge is what turns a frustrating mystery into a solvable problem.
