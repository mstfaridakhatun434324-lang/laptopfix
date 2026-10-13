---
title: "Cumulative Update Fails to Install After a Windows 11 Update? Here's the Fix"
slug: how-to-fix-cumulative-update-fails-to-install-after-windows-11-update
date: 2026-09-03
categories: ["windows-update"]
tags: ["cumulative update", "update fails", "windows 11", "kb install error", "patch tuesday"]
description: "The monthly cumulative update keeps failing to install on Windows 11? From cache clears to manual installs, here's the complete fix sequence."
thumbnail: "/images/thumbs/how-to-fix-cumulative-update-fails-to-install-after-windows-11-update.webp"
faqs:
  - q: "What is a cumulative update and why does it matter?"
    a: "A cumulative update bundles all previous security and quality fixes for the month into one package — Patch Tuesday's main event. Because each cumulative supersedes the last, you only ever need the latest one. When it fails, you miss that month's security fixes, which is why these failures deserve prompt attention unlike optional driver hiccups."
  - q: "The same cumulative update fails every month. Is my system broken?"
    a: "Not necessarily broken, but something is persistently wrong — usually a corrupt component store, a damaged servicing stack, or a specific conflict like insufficient recovery partition space. Monthly repetition means the root cause survives each attempt, so stop retrying blindly and work through the diagnostic sequence below."
  - q: "Can I skip a failed cumulative update and wait for next month's?"
    a: "You can, and next month's cumulative includes everything the failed one had. But if the failure cause is systemic (corrupt store, bad servicing stack), next month's will fail identically. Only skip-and-wait when the failure looks package-specific, and use the waiting month to repair the underlying system."
  - q: "How do I manually install a cumulative update?"
    a: "Note the KB number from Update history, search for it on the Microsoft Update Catalog, download the x64 package for your Windows version, and run the .msu file. Manual installation bypasses the Windows Update agent entirely and succeeds in many cases where the automated install fails."
---

The cumulative update is the most important regular update Windows ships — the monthly bundle of security fixes that keeps your laptop safe. So when it fails, it's not a minor annoyance; it's a security gap that grows every month it stays uninstalled. The failure pattern is depressingly familiar: Patch Tuesday arrives, the update downloads, the install churns, and then "Failed to install" with an error code. Next month, the new cumulative fails the same way.

Cumulative update failures have a well-understood set of causes, and they respond to a well-understood sequence of fixes. The key is ordering: clear the transient problems first (cache, pending restarts), then repair the servicing infrastructure (DISM, SFC, servicing stack), then bypass the agent (manual install), and only then escalate to heavy repairs. Work the sequence — don't jump to step seven first.

## Why this happens

- **Corrupt download cache**: The multi-hundred-MB package corrupted in transit, failing verification on every retry.
- **Damaged component store**: WinSxS corruption that the cumulative update can't build on.
- **Outdated servicing stack**: The SSU predates what the cumulative package requires.
- **Pending restart deadlock**: A previous update's pending operations blocking the new install.
- **Insufficient recovery partition space**: The cumulative needs to update WinRE; a cramped recovery partition fails it.
- **Third-party antivirus interference**: Security software blocking the update's file operations.
- **Stuck update orchestrator state**: The Update Orchestrator service holding stale session data.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Note the KB number and error code

Precision first. "Cumulative update failed" isn't a diagnosis; "KB50XXXXX failed with 0x800F0922" is.

1. Go to **Settings > Windows Update > Update history**.
2. Find the failed cumulative update — note the **KB number** and **error code**.
3. Common codes: **0x800F0922** (often .NET or secure boot/partition), **0x80073701** (missing assembly — DISM territory), **0x80070002** (corrupt cache), **0x80070070** (disk space).
4. Check whether it's failing at download, install, or restart — each phase points differently.
5. This code directs which fixes below matter most.

### Fix 2: Clear the cache and restart cleanly

The fastest genuine fix. Corrupt downloads are common with large cumulative packages.

1. Open **Command Prompt as administrator**.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Delete everything in `C:\Windows\SoftwareDistribution\Download`.
4. Restart the three services with `net start`.
5. Perform a full **Restart** (not shutdown) to clear any pending-restart deadlock.
6. Go to **Settings > Windows Update** and retry immediately after the reboot.

### Fix 3: Install the latest servicing stack update

The cumulative update sits on top of the servicing stack. An outdated SSU rejects modern packages.

1. Search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for "servicing stack update" plus your Windows 11 version.
2. Download the latest x64 SSU and install the `.msu`.
3. Restart when prompted — SSU installs always need it.
4. Retry the cumulative update.
5. Check Update history afterward: you should see the SSU listed as installed, then the cumulative succeeding.

### Fix 4: Repair the component store with DISM and SFC

When the failure code points at assemblies or the store (0x80073701, 0x800F081F), this is the core fix.

1. Elevated Command Prompt: `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Wait for completion (15–30 minutes, needs internet).
3. Run `sfc /scannow`.
4. Restart and retry the cumulative update.
5. If DISM reports it couldn't repair, the store damage is severe — skip to Fix 7's in-place upgrade.
6. Our [Feature Experience Pack guide](/articles/how-to-fix-feature-experience-pack-failed-to-install-in-windows-11-24h2/) covers the same DISM technique for smaller package failures.

### Fix 5: Install the cumulative update manually

Bypass the agent. The standalone installer uses a simpler, more robust code path.

1. Using the KB number from Fix 1, find the package on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
2. Download the x64 version matching your Windows 11 build.
3. Double-click the `.msu` and let it install — this can take 20–40 minutes.
4. Restart when prompted.
5. Verify in **Settings > Windows Update > Update history** that the KB shows as installed.
6. Future cumulative updates should then flow through the normal agent again.

### Fix 6: Address WinRE partition space issues

The silent killer: cumulative updates that update Windows Recovery Environment fail when the recovery partition is too small, with unhelpful error codes.

1. Open **Disk Management** and check the **Recovery Partition** size and free space.
2. 24H2-era updates may need ~500 MB free in the recovery partition for WinRE updates.
3. If cramped, the supported fix is Microsoft's documented partition-resize procedure (see the [Windows support site](https://support.microsoft.com/en-us/windows) for the current script).
4. Alternatively, disable WinRE temporarily (`reagentc /disable`), install the cumulative, then re-enable (`reagentc /enable`) — the update then skips the WinRE portion.
5. This is a known pattern for 0x800F0922 failures.

### Fix 7: In-place upgrade for persistent monthly failures

When every month's cumulative fails despite all of the above, the servicing infrastructure needs rebuilding.

1. Download the current Windows 11 ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount it and run `setup.exe`, choosing **Keep personal files and apps**.
3. The in-place upgrade reinstalls Windows with a healthy servicing stack and component store.
4. Afterward, run Windows Update — the cumulative should install cleanly.
5. If failures persist even after this, suspect hardware: run `chkdsk C: /f /r` and check SMART status.
6. For the full post-reinstall update sequence, see our [clean install update guide](/articles/how-to-fix-windows-update-error-after-clean-install-in-windows-11-24h2/).

## Closing

Cumulative update failures feel chronic because the same root cause fails every month's package identically. Break the cycle by fixing the cause, not retrying the symptom: clear the cache, update the servicing stack, repair the store with DISM, and install manually when the agent won't cooperate. One good month of updates — with the underlying repair done — restores the automatic rhythm Patch Tuesday is supposed to have.
