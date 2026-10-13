---
title: "How to Check the Update Installation Date in Windows 11 24H2"
slug: how-to-check-update-installation-date-in-windows-11-24h2
date: 2026-09-22
categories: ["windows-update"]
tags: ["update history", "installation date", "windows 11 24h2", "troubleshooting"]
description: "Need to know exactly when an update installed on Windows 11 24H2? Here are four reliable ways to check update installation dates."
thumbnail: "/images/thumbs/how-to-check-update-installation-date-in-windows-11-24h2.webp"
faqs:
  - q: "Why would I need an update's installation date?"
    a: "The installation date is the single most useful fact when diagnosing a new problem. If your Wi-Fi broke on Tuesday and a driver update installed Monday night, you have your suspect. Support technicians ask for it first, and it tells you whether a 'recent update' is actually recent or months old."
  - q: "Does Update history show every update ever installed?"
    a: "No. Windows 11 keeps a rolling history that can be cleared by update component resets, Disk Cleanup's Windows Update Cleanup option, and major upgrades. For a permanent record, the Event Viewer logs and the systeminfo command preserve installation evidence longer than the Settings history page does."
  - q: "What's the difference between installed date and release date?"
    a: "The release date is when Microsoft published the update; the installed date is when it actually landed on your machine. They can differ by weeks due to rollout waves, paused updates, or failed attempts. For troubleshooting, the installed date is the one that matters — it tells you when your system changed."
  - q: "Can I check update dates from the command line?"
    a: "Yes. The command wmic qfe list brief /format:table shows installed hotfixes with their installation dates, and systeminfo lists them too. These command-line methods work even when the Settings app is misbehaving, which is exactly when you most need the information."
---

"When did this update install?" is the question that unlocks most update troubleshooting. A problem that started Thursday morning points at whatever installed Wednesday night. But Windows 11 24H2 does not put that date front and center — it is scattered across Update history, the Event Viewer, and command-line tools, each with different levels of detail and reliability. Knowing all four methods means you can always get the answer, even when one of them is broken or has been cleared.

The reason this matters more than people expect is that human memory is unreliable about system changes. Users routinely blame "yesterday's update" for a problem when the actual culprit installed three weeks ago, or dismiss updates entirely when one installed hours before the symptom appeared. An exact installation date replaces that guesswork with a fact, and facts are what separate a ten-minute fix — uninstall the update from last night — from an afternoon of random troubleshooting. Every professional technician establishes the timeline first, and this guide gives you the same capability.

This guide covers each method in order of convenience, plus what to do when the history itself is missing.

## Why this happens

- **Update history gets cleared.** Disk Cleanup, component resets, and feature upgrades can wipe the Settings history page.
- **Different tools show different dates.** Settings shows install completion; Event Viewer shows servicing events; WMIC shows hotfix registration — they can disagree by hours.
- **Failed updates pollute the timeline.** Update history lists failed attempts alongside successes, making the "real" install date ambiguous.
- **Rollout waves delay installation.** The date an update installed on your machine can be weeks after Microsoft's release date.
- **The Settings app itself can break.** When the update UI malfunctions, the history page may be empty or refuse to load.
- **Time zone and clock issues.** An incorrect system clock at install time records a wrong date permanently in some logs.
- **Multiple updates share a session.** A single restart can install several updates, and only careful log reading separates their timestamps.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Settings Update history

The fastest method when it works.

1. Open **Settings** > **Windows Update** > **Update history**.
2. Expand each category — Quality Updates, Driver Updates, Definition Updates, Other Updates — to see individual entries.
3. Each entry shows its install date (and KB number). This is the official record and the first place any technician looks.
4. If the page is empty or will not load, move to the next methods — the data exists elsewhere.

### Fix 2: Use the WMIC command for a clean table

A reliable command-line list of installed hotfixes.

1. Open **Command Prompt** (no admin needed) and run:
   ```
   wmic qfe list brief /format:table
   ```
2. The output lists each hotfix with its **InstalledOn** date in a clean table.
3. For a specific update, filter it: `wmic qfe where "HotFixID='KB5036893'" list brief`. Replace the KB number with the one you are investigating.

### Fix 3: Use systeminfo for the full picture

The built-in system report includes hotfix dates.

1. Open Command Prompt and run `systeminfo`.
2. Scroll to the **Hotfix(s)** section near the bottom — it lists installed updates.
3. For just that section, run `systeminfo | findstr /B /C:"Hotfix"`. Note that systeminfo can be slow to run; give it a minute.

### Fix 4: Dig into the Event Viewer servicing logs

The most detailed and hardest-to-erase record.

1. Press **Windows key + R**, type `eventvwr.msc`, and navigate to **Windows Logs** > **System**.
2. Filter for source **Microsoft-Windows-Servicing** or event IDs related to package installation.
3. Each servicing event carries an exact timestamp of when the package operation occurred — more precise than the Settings date.
4. Also check **Applications and Services Logs** > **Microsoft** > **Windows** > **WindowsUpdateClient** > **Operational** for the update client's own timeline.

### Fix 5: Check the CBS log for exact install times

When you need forensic precision.

1. Open `C:\Windows\Logs\CBS\CBS.log` in a text editor (it is large — use search, do not scroll).
2. Search for the KB number. The log records package operations with timestamps down to the second.
3. This is the log Microsoft support asks for when the other methods disagree — it is the ground truth of what the servicing stack did and when.

### Fix 6: Correlate the date with the symptom

Turn the date into a diagnosis.

1. Once you have the install date, compare it to when your problem started. A match within a day is a strong suspect.
2. Uninstall that specific update via **Settings** > **Windows Update** > **Update history** > **Uninstall updates** and test.
3. If the problem resolves, you have confirmed the culprit — pause updates and report it. Our guide to [viewing installed KB updates in 24H2](/articles/how-to-view-installed-kb-updates-in-windows-11-24h2/) covers the inventory side of this investigation in more depth.

### Fix 7: Rebuild history when it is missing

Restore the record for the future.

1. If Update history is empty because of a component reset, that is expected — resets clear it. The Event Viewer and CBS logs still hold the truth.
2. Going forward, avoid running Disk Cleanup's **Windows Update Cleanup** unless you need the space; it erases the history.
3. For ongoing tracking, export `wmic qfe` output to a file monthly: `wmic qfe list brief /format:table > C:\updates-%date%.txt`. Microsoft's [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents the official history tools if you need the supported reference.

## Closing

The update installation date is the key that turns "something broke recently" into "this specific update broke it." Start with Settings Update history, fall back to WMIC and systeminfo when the UI is uncooperative, and use the Event Viewer and CBS log when you need the forensic truth. And once you have the date, use it: correlate, uninstall, test. That single timestamp is worth more than an hour of guessing. Pair this timeline skill with [viewing your installed KB update inventory](/articles/how-to-view-installed-kb-updates-in-windows-11-24h2/) to build a complete picture of exactly what is on the machine and when each piece arrived. For the full chronological history behind individual install dates, see [checking your Windows update history on 24H2](/articles/how-to-check-windows-update-history-in-windows-11-24h2/).
