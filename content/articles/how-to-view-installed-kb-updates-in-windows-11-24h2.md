---
title: "How to View Installed KB Updates in Windows 11 24H2"
slug: how-to-view-installed-kb-updates-in-windows-11-24h2
date: 2026-09-20
categories: ["windows-update"]
tags: ["windows 11 24h2", "kb updates", "update history", "system info"]
description: "See every KB update installed on your Windows 11 24H2 laptop: use Settings, PowerShell, and the command line to build a complete, accurate update inventory."
thumbnail: "/images/thumbs/how-to-view-installed-kb-updates-in-windows-11-24h2.webp"
faqs:
  - q: "Where is the list of installed updates in Windows 11 24H2?"
    a: "Open Settings, then Windows Update, then Update history. This page lists quality updates, driver updates, definition updates, and feature updates with their KB numbers and install status. For a deeper list including hotfixes installed outside Windows Update, use PowerShell or the wmic command, which query the system inventory directly."
  - q: "Why do some installed updates not appear in Update history?"
    a: "Update history shows a rolling window and can be cleared when the SoftwareDistribution cache is reset. Updates installed via DISM or manual packages sometimes appear under different names. The PowerShell Get-HotFix cmdlet and the systeminfo command read from the authoritative installed-updates registry, so they show entries that the Settings page may omit."
  - q: "How can I export a list of installed KB updates?"
    a: "In PowerShell, run Get-HotFix and pipe it to Export-Csv, for example Get-HotFix | Export-Csv C:\\updates.csv. This creates a spreadsheet-ready file with HotFixID, description, and install date. Technicians use this export to compare a laptop's patch level against a known-good baseline before troubleshooting."
  - q: "What is the difference between a KB number and a build number?"
    a: "The KB number identifies the update package, such as KB5034765, while the build number identifies the resulting OS version, such as 26100.2894. One KB moves the build number forward. Run winver to see the build; check Update history to see which KB produced it. Both matter when you are matching a problem to a specific patch."
---

Knowing exactly which KB updates are installed on your laptop is the starting point for half of all update troubleshooting. A support article says "install KB5034765" — but is it already there? An update failed — which KB was it? Before you download anything or reset anything, you need an accurate inventory of what is installed.

Windows 11 24H2 gives you several ways to see this inventory, and they do not all show the same thing. The Settings page is the friendliest; PowerShell is the most complete; the command line is the fastest for a quick check. A good technician knows all three and picks the right one for the question at hand.

This guide walks through each method, explains what each list includes and omits, and shows how to export the results so you can compare patch levels or hand the list to support.

## Why this happens

- **Update history is a rolling window:** The Settings page can drop older entries after cache resets, so it is not a permanent record.
- **Manual installs list differently:** Packages installed via DISM or standalone installers sometimes appear with generic names instead of their KB numbers.
- **Multiple update types exist:** Quality updates, driver updates, definition updates, and servicing stack updates all carry KB numbers but live in different parts of the history.
- **Superseded updates confuse the picture:** A newer cumulative update replaces the older one, so the old KB may vanish from history even though its fixes are included.
- **Pending versus installed:** An update can appear in history as "failed" or "pending" while a later retry succeeded — status matters as much as presence.
- **Inventory tools read different sources:** Settings reads the update agent's history; Get-HotFix reads the installed-updates registry. They legitimately disagree sometimes. If you also need dates alongside the KB numbers, the [installation date check](/articles/how-to-check-update-installation-date-in-windows-11-24h2/) pairs naturally with this inventory.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Update history in Settings

1. Open **Settings → Windows Update → Update history**.
2. Expand **Quality updates** — this is where cumulative KB updates live, with install dates and status.
3. Check **Driver updates** and **Definition updates** sections too, since those also carry KB or version identifiers.
4. Note any entry marked **Failed** — that is usually the update you are investigating.
5. If the list looks short or empty, the history may have been cleared; move on to PowerShell for the authoritative list.

### Fix 2: List hotfixes with PowerShell

1. Open **Terminal** (PowerShell works without admin for this read-only query).
2. Run `Get-HotFix` and press Enter — you get HotFixID, description, installed-by, and installed-on for each update.
3. Sort by date with `Get-HotFix | Sort-Object InstalledOn -Descending` to see the newest first.
4. Filter for a specific KB: `Get-HotFix -Id KB5034765` returns it or errors if absent — a fast yes/no check.
5. Compare this list against Update history; entries here that are missing there were likely installed outside the normal agent.

### Fix 3: Use systeminfo for a quick text list

1. Open **Command Prompt** or Terminal and run `systeminfo`.
2. Scroll to the **Hotfix(s)** section near the bottom — it lists installed KB numbers in brackets.
3. For just that section, run `systeminfo | findstr Hotfix` to skip the rest of the output.
4. This method is quick but shows only KB numbers, no dates or descriptions.
5. It is ideal for pasting into a support ticket or comparing two machines side by side.

### Fix 4: Query a specific KB across methods

1. Pick the KB number you care about, for example the one a troubleshooter asked you to verify.
2. Check Settings → Update history first for status and date context.
3. Run `Get-HotFix -Id KBxxxxxxx` in PowerShell for the registry-level confirmation.
4. Run `winver` to see the current build number and confirm it matches what that KB should produce.
5. If all three agree the KB is installed and healthy, your problem lies elsewhere — do not reinstall blindly. When the KB is genuinely missing and Windows Update will not offer it, our guide on [manual catalog installation](/articles/best-way-to-install-kb-update-manually-from-catalog/) shows how to apply it directly.

### Fix 5: Export the full inventory to a file

1. In PowerShell, run `Get-HotFix | Select-Object HotFixID, Description, InstalledOn | Export-Csv C:\kb-inventory.csv -NoTypeInformation`.
2. Open the CSV in Excel or Notepad to review the complete list.
3. For a text report instead, run `Get-HotFix | Out-File C:\kb-inventory.txt`.
4. Save this export before major troubleshooting — it is your "before" snapshot.
5. After fixing an update problem, export again and diff the two files to prove exactly what changed.

### Fix 6: Check the build number as a cross-reference

1. Press **Win + R**, type `winver`, and note the full build string, such as 26100.2894.
2. Search that build on the [Microsoft support site](https://support.microsoft.com/en-us/windows) to find which KB produced it.
3. If the build is older than the KB you expected, the update truly did not apply — history may be misleading you.
4. This cross-check catches the case where an update reports success but the build never moved.
5. Record the build number in your notes; support engineers always ask for it first.

### Fix 7: Rebuild history when the list is clearly wrong

1. If Settings shows updates you know failed, or PowerShell shows KBs that history omits, the agent's database may be corrupt.
2. Stop the Windows Update service: `net stop wuauserv` in an admin Terminal.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and restart the service.
4. Windows rebuilds the history database on the next update check — give it one full check cycle.
5. Re-run `Get-HotFix` afterward; the registry list is unaffected by this reset and remains your ground truth.

## Closing

An accurate update inventory turns guessing into diagnosis. Settings gives you the friendly view, PowerShell gives you the authoritative view, and the build number gives you the cross-check. Learn all three, export before you troubleshoot, and you will never again wonder whether a KB is actually installed — you will know, with evidence, in under a minute.
