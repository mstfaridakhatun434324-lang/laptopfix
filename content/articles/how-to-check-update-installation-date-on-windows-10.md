---
title: "How to Check When Updates Were Installed on Windows 10"
slug: how-to-check-update-installation-date-on-windows-10
date: 2026-09-13
categories: ["windows-update"]
tags: ["update history", "installation date", "windows 10", "powershell"]
description: "Check update installation dates on Windows 10: seven methods from Settings to PowerShell to find exactly when any update was installed."
thumbnail: "/images/thumbs/how-to-check-update-installation-date-on-windows-10.webp"
faqs:
  - q: "Why would I need to know when an update was installed?"
    a: "The most common reason is troubleshooting: a problem that started on a specific date usually traces to whatever updated that day. Support technicians also ask for install dates to determine whether a machine is behind on patching, and auditors sometimes need the dates for compliance records."
  - q: "Does Windows 10 keep a full history of every update?"
    a: "Settings shows a useful recent history, but the complete record lives in the Event Viewer and the CBS logs. Note that resetting the SoftwareDistribution folder clears the Settings history view — the underlying install dates remain discoverable through PowerShell and the event logs regardless."
  - q: "Can I see update dates from the command line?"
    a: "Yes. PowerShell's Get-HotFix cmdlet lists installed updates with their InstalledOn dates, and wmic qfe list gives a similar table from Command Prompt. Both are scriptable, which makes them the right choice when you need dates from many machines or want to export the list."
  - q: "What is the difference between InstalledOn and the release date?"
    a: "The release date is when Microsoft published the update; InstalledOn is when your specific machine applied it. For troubleshooting, InstalledOn is what matters — it tells you what changed on your system and when, which is how you connect a new problem to its cause."
---

Knowing exactly when an update was installed on your Windows 10 laptop is one of those small skills that pays off disproportionately. A printer that stopped working "a few days ago," Wi-Fi that broke "last week" — matching the symptom's start date to an update's install date turns a mystery into a suspect list of one.

Windows 10 records install dates in several places, from the friendly Settings page to scriptable PowerShell commands. This guide walks all of them, simplest first, so you can pick the method that fits whether you are checking one laptop or fifty.

## Why this happens

- **Symptoms need timelines:** Connecting "it broke Tuesday" to "KB installed Tuesday" is the fastest diagnostic shortcut in Windows troubleshooting.
- **Settings history is incomplete:** The friendly history view only goes back so far and can be wiped by cache resets.
- **Different tools, different truths:** Settings, PowerShell, and the event log can disagree after partial installs — knowing all three lets you reconcile them.
- **Compliance needs proof:** Some workplaces and auditors require documented patch dates, not just "we think we're current."
- **Rollback decisions need dates:** Uninstalling the right update requires knowing which one actually installed before the problem started.
- **Support asks for them:** Every competent support technician's second question after "what's the error" is "when did it last work" — install dates answer the follow-up.
- **Feature vs. quality updates differ:** Feature updates and monthly cumulative updates record differently, which confuses people checking only one place.
- **Cache resets erase the easy view:** Clearing SoftwareDistribution wipes the Settings history, sending people to PowerShell — the same reset used in [Windows 10 pipeline repairs](/articles/how-to-fix-windows-update-error-after-clean-install-on-windows-10/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Settings update history

1. Open **Settings → Update & Security → Windows Update → View update history**.
2. Expand **Quality Updates**, **Driver Updates**, and **Feature Updates** — each entry shows its install date.
3. Match the dates against when your problem started; the closest preceding update is your prime suspect.
4. Click any entry for details including the KB number.
5. This covers most needs in under a minute — try deeper methods only if the history looks incomplete.

### Fix 2: Use Control Panel's installed updates list

1. Open **Control Panel → Programs → Programs and Features → View installed updates**.
2. The **Installed On** column shows the date for each update, sortable by clicking the header.
3. Sort by date descending to see the most recent changes first.
4. Right-click any update to uninstall it — useful when Fix 1 identifies the culprit.
5. This classic view sometimes shows entries the Settings page omits.

### Fix 3: Query with PowerShell's Get-HotFix

1. Open **PowerShell** (no admin needed) and run `Get-HotFix | Sort-Object InstalledOn -Descending`.
2. Each entry shows HotFixID, description, and **InstalledOn** date.
3. Filter to a specific update: `Get-HotFix -Id KB5036893`.
4. Export the full list: `Get-HotFix | Export-Csv updates.csv`.
5. This is the method for fleet checks and documentation — scriptable and complete.

### Fix 4: Use WMIC from Command Prompt

1. Open **Command Prompt** and run `wmic qfe list brief /format:table`.
2. For dates specifically: `wmic qfe get HotFixID,InstalledOn /format:table`.
3. The output lists every installed update with its install date in a clean table.
4. Note: on the newest Windows 10 builds WMIC may warn about deprecation — it still works.
5. Prefer PowerShell for new scripts, but WMIC remains the quickest one-liner on older systems.

### Fix 5: Read the Setup event log

1. Press **Win + R**, type `eventvwr.msc`, open **Windows Logs → Setup**.
2. Successful installs log events with timestamps — filter by the KB number or date range.
3. This log survives SoftwareDistribution resets that wipe the Settings history.
4. Cross-reference with Fix 1 when the two disagree; the event log is the ground truth.
5. Export relevant events if you need to share them with support.

### Fix 6: Check Reliability Monitor's timeline

1. Press **Win + R**, type `perfmon /rel`, and open **Reliability Monitor**.
2. The timeline shows Windows updates as informational events on their install days.
3. Click any day to see exactly what installed, alongside failures and warnings.
4. This is the best visual correlation tool: update installs plotted against crashes and errors.
5. A red X appearing the day after an update install is practically a signed confession.

### Fix 7: Inspect the registry for install dates

1. Press **Win + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\Packages`.
2. Each package key carries an **InstallTime** value (high/low parts of a timestamp).
3. This is the rawest source — useful when every higher-level view disagrees.
4. Do not modify anything here; this method is read-only diagnosis.
5. Convert the timestamp with PowerShell if you need a human date: `[datetime]::FromFileTime($t)`.

### Fix 8: Document and act on what you find

1. Write down the suspect KB number and its install date alongside your symptom's start date.
2. If they align, uninstall the update from the Control Panel view (Fix 2) as a test.
3. If the symptom resolves, [hide that update](/articles/how-to-disable-automatic-driver-updates-on-windows-10/) with the show/hide troubleshooter to prevent reinstallation while you report it.
4. If dates do not align with any update, the cause lies elsewhere — drivers, software installs, or hardware.
5. Keep the exported list from Fix 3 with your troubleshooting notes; future problems get faster. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official update-history views if you need the reference.

## Closing

Checking when updates were installed on Windows 10 is a ladder: Settings history for the quick look, Control Panel for the sortable list, PowerShell for the scriptable truth, and the event log plus Reliability Monitor when you need ground truth or visual correlation. Learn the two-minute version (Fix 1) for daily use and keep the PowerShell one-liner in your back pocket for everything else. The next time something breaks "out of nowhere," you will know exactly where to look — and "nowhere" will turn out to be a Tuesday with a KB number attached.
