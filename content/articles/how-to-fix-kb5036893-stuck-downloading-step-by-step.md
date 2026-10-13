---
title: "KB5036893 Stuck Downloading? Step-by-Step Fix"
slug: how-to-fix-kb5036893-stuck-downloading-step-by-step
date: 2026-10-06
categories: ["windows-update"]
tags: ["kb5036893", "stuck downloading", "step by step", "windows update"]
description: "A meticulous step-by-step repair for KB5036893 stuck downloading: verify the stall, reset the pipeline, and finish with a manual install if needed."
thumbnail: "/images/thumbs/how-to-fix-kb5036893-stuck-downloading-step-by-step.webp"
faqs:
  - q: "What does it mean when KB5036893 is stuck downloading?"
    a: "It means the Windows Update downloader cannot complete fetching the package files — progress freezes because each attempt hits the same local blocker. The blocker is almost always on your laptop: a corrupted cache, a hung service, a network restriction, or a validation failure that restarts the transfer. The update itself is fine; the delivery path needs repair."
  - q: "Can I skip KB5036893 if it will not download?"
    a: "You can wait for the next cumulative update, which supersedes it, but a stuck download often signals pipeline damage that will block the next update too. Better to fix the pipeline now using this guide. If the download is the only problem and everything else works, waiting one month is harmless — but verify the next update downloads cleanly."
  - q: "Why does the download restart from 0% repeatedly?"
    a: "Windows Update validates downloaded chunks, and when validation fails it discards the bad data and restarts that portion — displayed as dropping back to 0%. Repeated restarts mean the same corruption recurs, usually because the cache folder itself is damaged or a proxy is altering the data in transit. Clearing the cache and disabling proxies breaks the cycle."
  - q: "Is a manual install just as good as the automatic download?"
    a: "Yes. The Microsoft Update Catalog hosts the identical signed package. Installing the MSU directly applies the same files and writes the same history entries. The only difference is delivery. For a stubbornly stuck download, manual installation is the recommended escalation — it is supported, safe, and definitive."
---

When KB5036893 will not finish downloading, precision beats speed. This is the step-by-step version of the repair: every action in order, every verification checkpoint included, no step skipped. Follow it exactly and you will either unstick the download or prove the pipeline needs the manual-install finish.

The structure is deliberate. Steps 1–3 confirm and attempt the gentle fixes. Steps 4–6 clear and reset the machinery. Step 7 is the manual installation that ends the saga regardless. Each step includes how to verify it worked before moving on — because blindly running every fix teaches you nothing about what was wrong.

Set aside thirty minutes, keep the charger connected, and work the list.

Precision matters more than speed with a stuck download. Rushing through fixes without verifying each one is how a thirty-minute repair becomes a lost weekend. The checkpoints below are not optional extras — they are what make this procedure definitive instead of hopeful.

## Why this happens

- **Clock skew breaking validation:** A system clock far off real time can fail the certificate checks on downloaded chunks, silently restarting the transfer.
- **Cache corruption loop:** Damaged partial files fail validation and restart the download endlessly.
- **Deadlocked services:** Wuauserv or BITS hangs, freezing progress at a fixed percentage.
- **Network restrictions:** Metered flags, VPNs, proxies, or firewalls silently throttle or block the transfer.
- **Validation failures in transit:** A proxy or security product modifying traffic causes checksum mismatches.
- **Insufficient staging space:** The drive cannot hold the expanding package, stalling the transfer.
- **Peer-download stall:** Delivery Optimization waiting on unreachable peers instead of Microsoft servers.
- **Database corruption:** A damaged update database makes the agent request the wrong byte ranges repeatedly. The [HP-specific KB5036893 guide](/articles/how-to-fix-kb5036893-stuck-downloading-on-hp-laptop/) adds vendor-aware checks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall with measurements

1. Record the exact percentage shown in **Settings → Windows Update** and the current time.
2. Open **Task Manager → Performance → Wi-Fi/Ethernet** and observe for five full minutes.
3. Wait 30 minutes, then compare the percentage — identical means stalled.
4. Check **Task Manager → Processes** for disk activity from Service Host; none for an hour confirms it.
5. Verify at least 10 GB free on C:. Only proceed when the stall is measured, not assumed.

### Fix 2: Restart services and retry cleanly

1. Open an admin Terminal and run `net stop wuauserv` then `net stop bits`.
2. Wait 30 seconds, then run `net start wuauserv` and `net start bits`.
3. In **Settings → Windows Update**, click **Retry** or **Check for updates**.
4. Observe for 20 minutes — note whether the percentage moves at all.
5. **Checkpoint:** if it progresses, let it finish. If it freezes at the same point, the cache is poisoned — continue.

### Fix 3: Eliminate network interference

1. Turn **off** Metered connection for your Wi-Fi network in Settings → Network & internet.
2. Disconnect all **VPN** connections completely.
3. Disable third-party firewall/antivirus network filtering temporarily.
4. In **Delivery Optimization** settings, disable "Allow downloads from other PCs".
5. Restart the laptop, then retry the download for 20 minutes. **Checkpoint:** movement means a network flag was the cause.

### Fix 4: Clear the download cache surgically

1. In an admin Terminal: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Navigate to `C:\Windows\SoftwareDistribution\Download` and delete **all** contents.
3. Restart the three services in reverse order.
4. Click **Check for updates** — the KB begins downloading from zero with a clean cache.
5. **Checkpoint:** observe for 30 minutes. Most genuine stalls resolve here; the [24H2 catalog variant](/articles/how-to-fix-kb5036893-stuck-downloading-in-windows-11-24h2/) covers build-specific cache issues.

### Fix 5: Run the automated troubleshooter

1. Go to **Settings → System → Troubleshoot → Other troubleshooters**.
2. Run **Windows Update**; apply every fix it suggests.
3. Restart the laptop when prompted, even if it seems unnecessary.
4. Retry the download and observe for 20 minutes.
5. **Checkpoint:** the troubleshooter repairs service registrations and policies that manual steps miss — verify progress before continuing.

### Fix 6: Perform the full component reset

1. In an admin Terminal, stop `wuauserv`, `bits`, `cryptsvc`, `msiserver`.
2. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
3. Run `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart all four services, then restart the laptop.
5. Check for updates and observe. **Checkpoint:** this rebuilds the entire pipeline — stalls surviving this are rare.

### Fix 7: Install KB5036893 manually to finish

1. Find the KB number in Update history to confirm the exact package.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com), matching your build and architecture.
3. Double-click the MSU, approve the prompt, and let the standalone installer run.
4. Restart when asked and confirm the KB in Update history.
5. **Final verification:** run **Check for updates** once more — a healthy pipeline with the manual install complete should report no pending download, matching the expected behavior on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

### Fix 8: Document the repair for next time

Turn this repair into a reusable runbook while the details are still fresh.

1. Write down which fix number resolved your stall and the symptom pattern it matched.
2. Save the exact commands you used in a notes file for next Patch Tuesday.
3. Note your network setup — what worked on this connection may differ on another.
4. Keep the catalog URL bookmarked with your build and architecture noted beside it.
5. Record how long each phase took so you can spot abnormal stalls faster next month.
6. Next time, start at the fix that worked this time instead of from the top.
7. Share the runbook with anyone else who maintains PCs in your household — it compounds.

## Closing

Step-by-step discipline is what separates a fixed update from a weekend of retries. Measure the stall, restart the services, clear the interference, reset the pipeline, and finish manually if needed — verifying at each checkpoint. KB5036893 will install, and you will know exactly which step fixed it.
