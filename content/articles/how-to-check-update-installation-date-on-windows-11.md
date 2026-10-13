---
title: "How to Check the Installation Date of Updates on Windows 11"
slug: how-to-check-update-installation-date-on-windows-11
date: 2026-09-24
categories: ["windows-update"]
tags: ["windows 11", "update history", "installation date", "kb updates"]
description: "Find exactly when each Windows 11 update was installed: use Settings, PowerShell, and system tools to date every KB on your laptop."
thumbnail: "/images/thumbs/how-to-check-update-installation-date-on-windows-11.webp"
faqs:
  - q: "Where do I see when a Windows update was installed?"
    a: "Open Settings, then Windows Update, then Update history. Each entry shows its install date next to the KB number. For a complete chronological list with precise timestamps, PowerShell's Get-HotFix cmdlet shows the InstalledOn date for every update. The two sources complement each other: Settings is readable, PowerShell is comprehensive."
  - q: "Why does Update history not show dates for old updates?"
    a: "Windows keeps only a rolling window of update history, and resetting the SoftwareDistribution cache wipes it entirely. Older entries age out even on healthy systems. The Get-HotFix registry query retains install dates longer, so when Settings history looks thin, PowerShell usually still has the dates you need."
  - q: "Can I tell when a feature update like 24H2 was installed?"
    a: "Yes. In Update history, look under Feature updates for the entry naming the version — it carries the install date. You can also check Settings, then System, then About, which shows the installation date of the current Windows build under Windows specifications. The original install date and the last feature update date are shown separately."
  - q: "How do I find the install date of a specific KB number?"
    a: "In PowerShell, run Get-HotFix -Id KB5034765 using the KB you want — the InstalledOn field gives the date, or it errors if the KB is absent. In Settings, use the search-like scan of Update history under Quality updates. For scripting across many machines, pipe Get-HotFix to Where-Object filtering on HotFixID."
---

"When did this update install?" is one of the most useful diagnostic questions you can ask. A problem that started the morning after KB5034765 landed is a very different investigation from a problem with no recent updates at all. Installation dates let you correlate symptoms with changes — the single most powerful troubleshooting technique there is.

Windows 11 records these dates in several places, and each has its strengths. Settings shows them in a friendly list. PowerShell exposes them for every hotfix including ones Settings forgets. System Information and the registry hold them for the truly stubborn cases.

This guide shows you each method, explains which dates each source can and cannot provide, and shows how to answer the specific question: when did KB number X install on this laptop?

## Why this happens

- **History is a rolling window:** The Settings page drops older entries over time, so dates for old updates simply disappear from the friendly view.
- **Cache resets wipe history:** Clearing SoftwareDistribution — a common troubleshooting step — erases the Settings history, though the registry dates survive.
- **Feature updates reset the clock:** A successful feature update can make the system look freshly installed, hiding the dates of older cumulative updates.
- **Multiple date sources disagree:** The update agent, the hotfix registry, and the CBS logs each record slightly different timestamps for the same event.
- **Failed attempts also get dated:** Update history records failed installs with dates too, which is useful — a failure date tells you when the problem started.
- **Time zone confusion:** PowerShell dates display in local time while some logs use UTC; a few hours of skew is normal, not an error. Pair this with the [installed KB inventory](/articles/how-to-view-installed-kb-updates-in-windows-11-24h2/) for the complete what-and-when picture.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read dates in Update history

1. Open **Settings → Windows Update → Update history**.
2. Expand **Quality updates** — each KB shows its install date and status.
3. Check **Feature updates** for the date your current Windows version installed.
4. Scan **Driver updates** and **Other updates** for their dates too.
5. Screenshot or note the dates relevant to your problem — this is your timeline baseline.

### Fix 2: Get precise dates with PowerShell

1. Open **Terminal** and run `Get-HotFix | Sort-Object InstalledOn -Descending`.
2. The **InstalledOn** column gives the date for every hotfix, newest first.
3. For one KB: `Get-HotFix -Id KB5034765 | Select-Object HotFixID, InstalledOn`.
4. Export the timeline: `Get-HotFix | Sort-Object InstalledOn | Export-Csv C:\update-dates.csv -NoTypeInformation`.
5. This list survives Settings history wipes, making it the reliable long-term record. For the 24H2-specific variant of this check, see [checking update dates in 24H2](/articles/how-to-check-update-installation-date-in-windows-11-24h2/).

### Fix 3: Check the Windows installation and build dates

1. Open **Settings → System → About** and look under **Windows specifications** for the install date of the current build.
2. Press **Win + R**, type `winver`, and note the build — then map the build to its release KB on the [Microsoft support site](https://support.microsoft.com/en-us/windows).
3. In an admin Command Prompt, run `systeminfo | find "Original Install Date"` for the first-ever install date.
4. Compare original install date versus feature update dates to understand the machine's history.
5. A machine whose "install date" is last week probably just took a feature update, not a clean install.

### Fix 4: Date a specific KB across all sources

1. Write down the KB number you are investigating.
2. Check **Update history** in Settings for its listed date and status.
3. Run `Get-HotFix -Id KBxxxxxxx` in PowerShell for the registry date.
4. Search `C:\Windows\Logs\CBS\CBS.log` for the KB number to find the exact timestamp of the install operation.
5. If all three agree, you have a solid date; if Settings is silent but PowerShell has it, trust PowerShell — history was likely cleared.

### Fix 5: Correlate dates with your symptom timeline

1. Write down when your problem first appeared, as precisely as you can.
2. List every update installed in the 7 days before that date from your PowerShell export.
3. The most recent cumulative or driver update before symptom onset is your prime suspect.
4. Check that suspect KB's status — a "failed" entry on that date is a strong lead.
5. This correlation is exactly what support engineers do first; doing it yourself speeds up every support interaction.

### Fix 6: Recover dates after history was wiped

1. If Settings history is empty after a cache reset, do not panic — the data is not fully gone.
2. `Get-HotFix` still shows install dates from the registry.
3. `C:\Windows\Logs\CBS\CBS.log` retains timestamps of servicing operations for weeks.
4. Event Viewer → **Windows Logs → Setup** records update installation events with dates.
5. Rebuild going forward: after recovering the timeline, avoid unnecessary SoftwareDistribution resets.

### Fix 7: Verify the current patch level date

1. Run `winver` and note the full build number.
2. Look up that build's release date to know how current the laptop is.
3. In **Settings → Windows Update**, confirm the "last checked" date is recent.
4. If the laptop has not successfully installed anything in months, treat that as the real problem — see our [monthly cumulative failure guide](/articles/how-to-fix-monthly-cumulative-update-failed-youtube/) for the repair sequence.
5. Document the current state so the next troubleshooting session starts from facts, not guesses.

### Fix 8: Pull the authoritative timeline from Event Viewer

When Settings and PowerShell disagree, Event Viewer settles the argument with timestamped servicing events.

1. Open **Event Viewer → Windows Logs → Setup** and filter for recent events.
2. Each successful update writes an event carrying the exact timestamp and KB reference.
3. Cross-check these timestamps against your PowerShell export for the definitive timeline.
4. Export the filtered events for your records: right-click the log → **Save All Events As**.
5. This log survives cache resets and history wipes, making it the ultimate source of truth.

## Closing

Installation dates turn "my laptop broke" into "my laptop broke the day after KB5034765 installed" — and that sentence solves problems. Learn the three views (Settings, PowerShell, system info), export the timeline before you troubleshoot, and always correlate symptoms with dates before changing anything. It is the cheapest diagnostic step in Windows, and the most underused.
