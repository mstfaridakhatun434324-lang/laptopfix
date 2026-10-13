---
title: "Fix Windows Update Error 0x800F0831 on Windows 11: Missing Update Fixed"
slug: how-to-fix-windows-update-error-0x800f0831-on-windows-11
date: 2026-09-05
categories: ["windows-update"]
tags: ["windows 11", "windows update", "error 0x800f0831", "missing update", "servicing stack"]
description: "Error 0x800F0831 means a required update is missing. Learn to install the missing prerequisite and repair the servicing chain on Windows 11."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0831-on-windows-11.webp"
faqs:
  - q: "What does error 0x800F0831 mean?"
    a: "It means the update you are installing requires another update that is not present — a missing prerequisite, usually a servicing stack update (SSU) or a specific earlier cumulative update. The installer detects the gap and refuses to proceed rather than installing into an unsupported state."
  - q: "Why would a prerequisite update be missing?"
    a: "Common reasons: updates were paused for a long time and the chain has gaps, a previous update failed silently, someone used a tool to hide updates, or the servicing stack update itself failed to install. The update history usually shows the gap if you look for failed or missing entries."
  - q: "Can I just install the missing update manually?"
    a: "Yes — that is the primary fix. Identify the required KB (often the latest servicing stack update for your Windows version), download it from the Microsoft Update Catalog, install it, and restart. The originally failing update will then usually proceed, because its prerequisite is finally satisfied and the chain is continuous again."
  - q: "Does 0x800F0831 ever indicate corruption rather than a missing update?"
    a: "Yes. Sometimes the 'missing' update is actually present but its servicing data is corrupted, so the installer cannot see it. In those cases the servicing stack update installs fine but the error persists, and DISM/SFC repair is needed to make the installed update visible again."
---

Error 0x800F0831 is Windows Update's way of saying "you skipped a step." The update you are trying to install depends on another update — most often a servicing stack update — that is not installed on your system. Rather than proceeding into an untested configuration, the installer stops and reports the missing prerequisite. On Windows 11 this commonly happens after long update pauses, after failed servicing stack updates, or when update-hiding tools have punched holes in the update chain.

The fix is logical: find the missing link and install it. The challenge is identifying exactly which update is missing, because Windows does not always name it clearly. The sequence below starts with the servicing stack (the most common missing piece), then widens to the update chain and servicing repairs.

## Why this happens

- **Missing servicing stack update:** The SSU that the cumulative update requires was never installed or failed silently.
- **Long-paused updates:** Months of paused updates create gaps in the prerequisite chain that a new update cannot bridge.
- **Hidden updates:** Update-hiding tools or manual hides removed a required update from the queue.
- **Silently failed prerequisite:** An earlier update reported success but did not actually complete, leaving a gap the next update detects.
- **Corrupted servicing data:** The prerequisite is installed but its servicing records are damaged, so it appears missing.
- **Out-of-order manual installs:** Manually installing updates out of sequence can leave prerequisite gaps.
- **Damaged update cache:** Corrupted metadata makes the installer miscalculate which prerequisites are present.
- **Component store corruption:** WinSxS damage can hide installed updates from prerequisite checks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the latest servicing stack update manually

The SSU is the missing prerequisite in most 0x800F0831 cases. Installing it directly unblocks the chain.

1. Determine your Windows 11 version: **Settings > System > About** (e.g., 23H2, 24H2).
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and search for "servicing stack update" plus your version.
3. Download the latest SSU for x64 and install the `.msu` file.
4. Restart the laptop, then check for updates — the previously failing update should now proceed.

### Fix 2: Check update history for gaps and failures

Find the hole in the chain by reading the history.

1. Go to **Settings > Windows Update > Update history**.
2. Look for failed updates, especially servicing stack updates or older cumulative updates that never succeeded.
3. Note their KB numbers — these are your missing prerequisites.
4. Install each missing KB manually from the Update Catalog, oldest first, restarting between them.

### Fix 3: Unhide any hidden updates

If you (or a tool) hid updates, a required one might be sitting in the hidden list.

1. Run Microsoft's **Show or hide updates** troubleshooter (wushowhide.diagcab).
2. Choose **Show hidden updates** and unhide anything update-related.
3. Check for updates again and install everything offered, in the order Windows presents it.

### Fix 4: Reset the update cache

Corrupted metadata can make the installer misjudge prerequisites. Rebuild it.

1. Open **Terminal (Admin)**.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Run `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Restart and check for updates.

### Fix 5: Repair the servicing layer with DISM and SFC

If the prerequisite is installed but invisible due to corruption, repair the servicing data.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow`.
3. Restart and retry the update. This repair also fixes [0x800F0922 CBS errors](/articles/how-to-fix-windows-update-error-0x800f0922-on-windows-11/), which share the servicing layer.

### Fix 6: Install the failing update manually after the SSU

With the servicing stack current, bypass any remaining queue confusion by installing the target update directly.

1. Note the KB number of the update failing with 0x800F0831.
2. Download it from the Microsoft Update Catalog (x64, matching your version).
3. Run the `.msu`, restart when prompted.
4. Verify in update history that it shows as successfully installed.

### Fix 7: Run an in-place upgrade for a badly gapped chain

If months of chaos have left the update chain unrecoverable — multiple missing prerequisites, repeated SSU failures — an in-place upgrade reinstalls Windows 11 with the full current update baseline, keeping your files and apps. Get the installer from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), choose **Keep personal files and apps**, and let it complete. Afterward, keep updates unpaused and let the chain stay continuous — the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows) documents the current update cadence.

Understanding why prerequisites go missing helps prevent repeats. The most common story is a long update pause: you paused updates for two months, Microsoft shipped two servicing stack updates in that window, and when you resumed, the cumulative update required an SSU you never got. Windows Update normally installs prerequisites automatically, but long pauses and manual update management break its assumptions. The second most common story is the hidden update: someone hid a servicing stack update months ago to stop a nagging prompt, forgetting that future updates would need it. Audit your hidden updates with the wushowhide tool whenever this error appears — the missing prerequisite is often sitting there waiting to be unhidden. The [Windows 10 version of this fix](/articles/how-to-fix-windows-update-error-0x800f0831-on-windows-10/) covers version-specific SSU selection for Windows 10's multiple builds. Keep the chain continuous and this error has no reason to exist. Monthly, unpaused, unhidden updates are the entire prevention strategy — boring, but effective.

## Closing

Error 0x800F0831 is a chain problem: something the update needs is not there. Install the servicing stack update, fill the gaps oldest-first, unhide hidden updates, and repair servicing data — in that order. Once the prerequisite chain is continuous again, the error disappears, and keeping updates running regularly (rather than paused for months) prevents it from ever coming back.
