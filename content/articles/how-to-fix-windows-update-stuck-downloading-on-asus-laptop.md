---
title: "Windows Update Stuck Downloading on an Asus Laptop? Fix It"
slug: how-to-fix-windows-update-stuck-downloading-on-asus-laptop
date: 2026-09-23
categories: ["windows-update"]
tags: ["update stuck downloading", "asus", "windows update", "bits"]
description: "Windows Update frozen mid-download on your Asus laptop? The download pipeline — BITS, cache, and network — is the culprit. Here is the ordered fix."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-downloading-on-asus-laptop.webp"
faqs:
  - q: "How do I know if the download is stuck or just slow?"
    a: "Watch the percentage for 30 to 60 minutes and check Task Manager's network graph. A slow download shows steady network activity and gradual progress; a stuck one shows 0% network usage with a frozen percentage. Only the stuck case needs the fixes below."
  - q: "Why does the download keep restarting from 0%?"
    a: "Because the Background Intelligent Transfer Service (BITS) discards corrupted partial downloads and starts over. Repeated restarts mean the partial data keeps failing validation — usually a cache or disk problem, occasionally an unstable connection. Three or more restarts to the same point is the signature of cache corruption rather than a network problem."
  - q: "Can Asus software interfere with update downloads?"
    a: "Yes. MyASUS and Armoury Crate update their own components, and aggressive Asus power or network profiles can throttle background transfers. They rarely block downloads outright, but updating them removes a variable. Update them from the Microsoft Store before deeper troubleshooting, so they are ruled out cleanly."
  - q: "Is it safe to delete the SoftwareDistribution folder?"
    a: "Yes, after stopping the update services. It contains only cached downloads and metadata, which Windows rebuilds on the next check. Renaming it (rather than deleting) keeps a fallback copy just in case. Stop the wuauserv and BITS services first, then rename the folder — Windows rebuilds it automatically."
---

The download starts, climbs to 12 percent — or 47, or 83 — and stops. Hours later it has not moved a point. Restarting the check sometimes resets it to zero, where it climbs back to the same spot and freezes again. On Asus laptops this maddening loop almost always lives in the download pipeline: BITS, the update cache, or the network path between you and Microsoft's servers.

Download stalls are a different animal from install failures. The update has not failed — it has never fully arrived. That narrows the fix list considerably, and it means the repairs are lower-risk: you are dealing with plumbing, not surgery. Work through these in order and the download completes.

BITS — the Background Intelligent Transfer Service — is the engine behind every Windows Update download, and it has its own state machine. A BITS job can be queued, connecting, transferring, suspended, or in error, and a job wedged in error with automatic retry is exactly what a frozen percentage looks like. You can inspect these jobs directly with the `bitsadmin` tool, which shows what Settings hides: which job is stuck, how many bytes transferred, and how many times it errored. When the GUI gives you nothing, bitsadmin gives you the truth.

## Why this happens

- **A corrupted partial download in the cache.** Damaged chunks fail validation, BITS discards them, and the cycle repeats.
- **The BITS service is stuck or misconfigured.** The transfer engine itself wedges, and no download can progress.
- **Unstable Wi-Fi dropping the connection.** Intermittent drops corrupt in-flight chunks on Asus models with aggressive power-saving wireless.
- **Metered connection pausing the download.** Windows halts large downloads on connections it believes are metered.
- **Asus power profiles throttling background transfers.** Battery-saver profiles can starve BITS of network access.
- **Third-party firewall blocking the transfer.** Security software interrupting the CDN connection mid-download.
- **Disk errors corrupting cached chunks.** Bad sectors damage the partial download as it is written.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall and check the network

Rule out the obvious before touching services.

1. Note the exact frozen percentage and wait 30 minutes to confirm zero movement.
1. Open Task Manager > **Performance** > **Wi-Fi** or **Ethernet** — flatlined network means a true stall.
1. Test general browsing; if the internet is down, fix that first.
1. If you are on a metered or hotspot connection, the pause may be intentional — see [metered connection blocking updates](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/).

### Fix 2: Restart BITS and the update services

Unwedges the transfer engine without deleting anything.

1. In an elevated Command Prompt: `net stop wuauserv`, `net stop bits`.
1. Wait 30 seconds, then `net start bits`, `net start wuauserv`.
1. Check for updates and watch the download for 15 minutes.
1. If it resumes, the service was wedged — no deeper repair needed.

### Fix 3: Clear the download cache

Removes the corrupted partial download the pipeline keeps tripping over.

1. Stop wuauserv, cryptSvc, bits, and msiserver.
1. Rename `C:\Windows\SoftwareDistribution` to `C:\Windows\SoftwareDistribution.old`.
1. Restart the services and check for updates.
1. The download restarts from zero with clean cache — let it run uninterrupted.

### Fix 4: Stabilize the network path

Intermittent connectivity is a top cause of chunk corruption.

1. Switch to Ethernet or move closer to the router.
1. Disable VPNs during the download — they add a failure-prone hop.
1. In Device Manager, disable power-saving on the Wi-Fi adapter's **Power Management** tab.
1. Update MyASUS and Armoury Crate from the Microsoft Store to rule out Asus-side interference.

### Fix 5: Run the troubleshooter and reset components

For stalls that survive a cache clear.

1. Run **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update**.
1. If it finds nothing, run `DISM /Online /Cleanup-Image /RestoreHealth` elevated.
1. Follow with `sfc /scannow` and restart.
1. Retry the download. Persistent stalls at this point suggest disk issues — run `chkdsk C: /f`.

### Fix 6: Try the manual Catalog download

When the BITS pipeline will not cooperate, go around it.

1. Find the KB number in **Update history** or the update's details.
1. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
1. Install the .msu directly — this uses no BITS transfer at all.
1. If the manual install works, the download pipeline was the sole problem. For the Dell-side version of this fix, see [update stuck downloading on Dell](/articles/how-to-fix-windows-update-stuck-downloading-on-dell-laptop/).

### Fix 7: Check disk health as the last resort

Repeated chunk corruption with a stable network points at storage.

1. Run `chkdsk C: /f /r` and reboot to scan.
1. Review SMART data with Asus or Windows tools.
1. Clear the cache once more after any disk repairs.
1. If the drive is failing, replace it before trusting the machine with updates — a dying disk corrupts more than downloads. For deeper update-system repair, [Microsoft support](https://support.microsoft.com/en-us/windows) documents the full component reset.

### Fix 8: Inspect the stuck BITS job directly

See what the Settings page will not show you.

1. In an elevated Command Prompt, run `bitsadmin /list /allusers /verbose`.
1. Look for jobs in ERROR or SUSPENDED state with transfer errors counting upward.
1. Run `bitsadmin /reset /allusers` to cancel all jobs cleanly.
1. Check for updates afterward — the fresh job starts without the wedged state.

## Closing

A download that freezes mid-way is a pipeline problem: BITS, the cache, or the network path. Restart the services, clear the cache, stabilize the connection, and the download finishes. Keep the manual Catalog install in your back pocket for the stubborn cases — it bypasses the entire download pipeline and gets the update onto the machine regardless. For recurring stalls, consider a weekly maintenance window: plug in, connect via Ethernet, and let Windows Update run undisturbed. Machines updated regularly develop fewer cache problems than machines updated in panicked bursts after months of postponement. Consistency is the cheapest update repair there is, and it costs nothing but a little planning.
