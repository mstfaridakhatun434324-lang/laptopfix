---
title: "How to Check Windows Update History on Windows 11"
slug: how-to-check-windows-update-history-on-windows-11
date: 2026-10-09
categories: ["windows-update"]
tags: ["update history", "windows 11", "installed updates", "kb updates"]
description: "See exactly which updates installed on your Windows 11 laptop — Settings, PowerShell, and log-file methods, plus what failed entries mean."
thumbnail: "/images/thumbs/how-to-check-windows-update-history-on-windows-11.webp"
faqs:
  - q: "Where do I find update history in Windows 11 Settings?"
    a: "Open Settings with Win + I, go to Windows Update, and click Update history. The page groups entries into Feature updates, Quality updates, Driver updates, Definition updates, and Other updates, each showing the KB number, install date, and status. It's the fastest way to see what changed recently and identify which update to investigate or remove."
  - q: "Why does my Windows 11 update history show failed updates?"
    a: "A failed entry means an update was attempted but didn't install — usually due to an interrupted download, insufficient disk space, or a conflicting driver. The history preserves the KB number so you can troubleshoot that specific package. If the same update keeps failing, run the Windows Update troubleshooter or install the KB manually from the Microsoft Update Catalog."
  - q: "Can I uninstall an update from the history page?"
    a: "The history page itself is read-only, but it links directly to the uninstall view. Scroll to the bottom of the Update history page and click Uninstall updates, which opens the classic installed-updates list where you can remove a problematic KB. Quality updates can be removed individually; feature updates roll back through the Recovery settings within ten days."
  - q: "How far back does Windows 11 update history go?"
    a: "The Settings history page shows a rolling record of recent updates, typically covering several months of quality updates plus the last feature update. The underlying records persist longer and can be queried with PowerShell's Get-HotFix or the wmic qfe command. Resetting the SoftwareDistribution folder clears the displayed history but doesn't remove the installed updates themselves."
---

Something changed on your Windows 11 laptop — a driver misbehaves, an app crashes, the battery drains faster — and the prime suspect is always the last update. Windows 11 keeps a detailed history of every update it installs: quality updates, feature updates, drivers, even Defender definitions, each stamped with a date and a success or failure status. Learning to read that history is the difference between guessing and diagnosing.

This guide covers every way to check it, from the friendly Settings page to PowerShell queries you can send to support. Once you can identify the exact KB that arrived before the trouble started, fixes like our [update troubleshooter guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-windows-11/) become targeted instead of scattershot.

## Why this happens

- **You need the KB number** — Every Microsoft fix, forum thread, and support article references updates by KB number; the history page is where you find yours.
- **A failure left no notification** — Some failed updates never pop up an alert; the history is the only record the attempt happened.
- **A driver arrived silently overnight** — Windows Update pushes hardware drivers automatically, and the history's driver section names the culprit.
- **You're verifying a fix worked** — After reinstalling a failed update, the history confirms the new status and timestamp.
- **You're deciding what to uninstall** — You can't remove the right update without first identifying it by name and install date.
- **Support will ask for it** — The first thing any technician wants is "what updated just before the problem started."

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check history in the Settings app

The primary method — clean, grouped by update type, and always available.

1. Press Win + I to open Settings, then select **Windows Update** in the left sidebar.
2. Click **Update history** in the main pane.
3. Browse the sections: **Feature Updates** (annual upgrades), **Quality Updates** (monthly KBs), **Driver Updates**, **Definition Updates**, and **Other Updates**.
4. Each entry shows the update name or KB number, the date it installed, and whether it succeeded.
5. Click any entry to expand it for more detail, including links to the Microsoft support article for that update.

### Fix 2: Uninstall a problematic update from the history page

The history page doubles as your launch point for removing a bad update.

1. On the Update history page, scroll to the very bottom and click **Uninstall updates**.
2. This opens the classic installed-updates list showing every KB with its install date — click **Installed On** to sort newest first.
3. Select the suspect update and click **Uninstall**, then reboot.
4. After removal, pause updates for a week or two (Settings > Windows Update > Pause updates) so the bad one doesn't reinstall immediately.
5. If the same quality update keeps failing rather than misbehaving, our guide to [monthly updates that fail](/articles/how-to-fix-monthly-cumulative-update-failed-after-windows-11-update/) covers the deeper repair sequence.

### Fix 3: Query history with PowerShell or Terminal

For a precise, copyable record — ideal when reporting issues to support or documenting a fleet of laptops.

1. Open Terminal as administrator (right-click Start > **Terminal (Admin)**).
2. Run `Get-HotFix | Sort-Object InstalledOn -Descending | Format-Table HotFixID, InstalledOn` for a clean newest-first list.
3. For full detail, run `Get-HotFix | Format-List *` and scroll through every property of each patch.
4. Export it with `Get-HotFix | Export-Csv C:\update-history.csv` to attach to a support ticket.
5. Compare KB numbers against the release notes on Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) to see exactly what each update changed.

### Fix 4: Read the Windows Update log for failed entries

When the history shows a failure but no useful detail, the log file has the full story.

1. Open PowerShell as administrator and run `Get-WindowsUpdateLog` — this compiles the modern binary log into a readable `WindowsUpdate.log` on your Desktop.
2. Open the log and search (Ctrl + F) for the KB number or for `FAILED`.
3. Look at the timestamps around the failure for error codes like 0x80070002 or 0x80240034.
4. Those codes tell you whether it was a download problem, a missing file, or a service failure — each with its own fix path.
5. Armed with the real error, you can search precisely instead of guessing, or install the KB manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).

### Fix 5: Check the Reliability Monitor timeline

Reliability Monitor gives you the update history in context — updates plotted alongside crashes and failures on the same timeline.

1. Search for **Reliability Monitor** in the Start menu (it's under "View reliability history").
2. The chart shows each day's stability index; click any day to see that day's events.
3. Windows Update installations, failures, and application crashes all appear in the same list.
4. This is the fastest way to answer "did the crash start the day after the update?" — the correlation is visual.
5. Click any update event for the KB number, then cross-reference with the Settings history for the full picture.

### Fix 6: Reset the history database when it's corrupted

Sometimes the history page itself lies — blank entries, duplicates, or phantom failures. Resetting the database fixes the view.

1. Open an elevated Terminal and run `net stop wuauserv` and `net stop bits`.
2. Delete the `DataStore` folder inside `C:\Windows\SoftwareDistribution` (this holds the history database).
3. Restart the services with `net start wuauserv` and `net start bits`.
4. Go to Settings > Windows Update and click **Check for updates** to rebuild the records.
5. The history repopulates accurately on the next check-in; installed updates themselves are never affected by this reset.

## Closing

Checking update history on Windows 11 is a thirty-second habit that pays off every time something breaks: Settings for the quick view, PowerShell for the precise record, Reliability Monitor for the timeline context. Make it your first step whenever a laptop starts misbehaving after Patch Tuesday, and you'll spend your troubleshooting time fixing the actual culprit instead of hunting for it.
