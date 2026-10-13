---
title: "KB5041585 Stuck at Downloading on Your Dell Laptop? Unstick It"
slug: how-to-fix-kb5041585-stuck-at-downloading-on-dell-laptop
date: 2026-09-22
categories: ["windows-update"]
tags: ["windows 11", "kb5041585", "dell", "windows update"]
description: "KB5041585 stuck at downloading — 0%, 20%, or frozen for hours on your Dell laptop? Here's how to unstick the download and finish the update."
thumbnail: "/images/thumbs/how-to-fix-kb5041585-stuck-at-downloading-on-dell-laptop.webp"
faqs:
  - q: "Why is KB5041585 stuck at 0% downloading?"
    a: "A 0% stall usually means the download never actually started transferring: a jammed BITS queue, a network block such as a VPN or proxy, or corrupted metadata telling Windows a download is in progress when it is not. Stopping the update services, clearing the download cache, and resetting BITS resolves the large majority of 0% stalls."
  - q: "How long should a Windows update download take?"
    a: "It depends on the update size and your connection, but a cumulative update on a decent broadband link typically downloads in minutes, not hours. If the percentage has not moved for over an hour on a working connection, the download is genuinely stuck rather than slow. Do not wait it out — clear the cache and restart the download as described above."
  - q: "Will deleting the SoftwareDistribution folder harm my laptop?"
    a: "No. The Download subfolder contains only pending update files, and Windows rebuilds it automatically. Installed updates, personal files, applications, and settings are completely untouched. The only cost is that Windows re-downloads any pending updates, which is exactly what you want when the existing downloads are corrupted."
  - q: "Can Dell SupportAssist interfere with Windows Update downloads?"
    a: "Yes, occasionally. Dell's utilities download drivers and firmware through their own channels, and running a Dell scan at the same time as a Windows Update download can saturate your connection or contend for file locks. Pausing Dell's tools while Windows Update downloads a large package like KB5041585 avoids the conflict, and you can run Dell's checks afterward."
---

You click Download, the progress bar crawls to some percentage — or does not move at all — and hours later KB5041585 is still sitting there, mocking you. Restarting does not help. The troubleshooter shrugs. Meanwhile the laptop runs warm and sluggish because the update engine is grinding away in the background trying to finish a download that will never complete.

On Dell laptops, stuck downloads usually trace back to a corrupted partial file that Windows keeps resuming instead of replacing, a network quirk, or Dell's own update utilities competing for the same bandwidth and file locks. The fix is to stop the broken download decisively, clear the debris, and let Windows fetch a clean copy. Here is exactly how to do that.

One more thing worth knowing before you start: a download stuck at a fixed percentage is different from a slow download. Slow means the number creeps upward over hours; stuck means it never moves at all. Slow deserves patience, stuck deserves intervention. Everything below assumes you have confirmed the true stall — no progress for at least an hour on a working connection.

## Why this happens

- **Corrupted partial download:** Windows resumes interrupted downloads instead of restarting them. If the partial file is damaged, every resume attempt stalls at the same point, freezing the progress bar indefinitely.
- **BITS transfer queue jammed:** The Background Intelligent Transfer Service manages update downloads. A jammed or corrupted BITS queue leaves the download in a permanent waiting state that a simple retry cannot clear.
- **Metered or unstable connection:** Metered flags, captive portals, and flaky Wi-Fi all throttle or interrupt the download. Windows may not report the network as the problem, so the bar just sits still.
- **Dell update utilities competing:** Dell SupportAssist and Dell Update can download the same drivers and firmware simultaneously, contending for bandwidth and occasionally locking files Windows Update needs.
- **Insufficient disk space:** If the drive fills mid-download, the transfer halts without a clear error. Dell laptops with smaller SSDs hit this wall more often.
- **Corrupted SoftwareDistribution metadata:** The DataStore database tracking the download can become inconsistent, leaving Windows Update believing a download is in progress when nothing is actually transferring.
- **VPN or proxy interference:** Corporate VPNs and misconfigured proxies can block or throttle Microsoft's update servers while regular browsing works fine, producing a download that never progresses.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Stop the stuck download properly

Do not just reboot and hope. A stuck download needs its services stopped and its partial files removed, or Windows will cheerfully resume the same broken transfer after every restart. [Dell's support site](https://www.dell.com/support) documents this same reset procedure for update downloads that stall on Dell systems.

1. Open Command Prompt as administrator.
2. Run net stop wuauserv and net stop bits to halt the update engine.
3. Leave the window open — you will restart these services after clearing the cache.

### Fix 2: Delete the partial download files

With the services stopped, the corrupted partial files can be removed safely. This is the step that actually breaks the stall, because it forces Windows to start the KB5041585 download from zero with clean files.

1. Open File Explorer and go to C:\Windows\SoftwareDistribution\Download.
2. Select everything inside and delete it.
3. Also rename the DataStore folder's database by stopping the services first if you skipped step one — but the Download folder alone fixes most stalls.
4. Restart the services with net start wuauserv and net start bits.

### Fix 3: Reset the BITS queue

If the download still stalls after clearing the cache, the BITS queue itself is likely jammed. Resetting BITS clears all queued transfer jobs, including the invisible ones holding your update hostage. The same BITS queue jam freezes [Insider builds stuck downloading](/articles/how-to-fix-windows-insider-build-stuck-downloading-in-windows-11-24h2/) in exactly this way.

1. In the elevated Command Prompt, run bitsadmin /reset /allusers.
2. Wait for confirmation that the jobs were canceled.
3. Restart the laptop to let BITS rebuild its queue cleanly.
4. Open Windows Update and click Check for updates to start a fresh download.

### Fix 4: Rule out network interference

A download that stalls at 0% while everything else browses fine often means something between you and Microsoft's servers is interfering. Eliminate the network variables before assuming system damage. Also rule out a quiet network policy: [metered connections block update downloads](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/) without any visible error.

1. Disconnect any VPN and disable proxy settings in Settings, Network and internet, Proxy.
2. If on Wi-Fi, move closer to the router or switch to a wired connection temporarily.
3. Turn off the metered connection flag for your network.
4. Retry the download and watch whether the percentage actually advances.

### Fix 5: Pause Dell's update utilities during the download

Dell's own tools are useful, but running them alongside Windows Update can cause contention. Pause them until KB5041585 finishes, then let them do their own checks afterward.

1. Open Dell SupportAssist or Dell Update and pause any active scans or downloads.
2. In Task Manager, end any Dell update background processes if they are consuming bandwidth.
3. Retry the Windows Update download with Dell's tools idle.
4. Re-enable Dell's utilities after the update completes.

### Fix 6: Download KB5041585 manually as a last resort

When the automated pipeline will not cooperate, the standalone package sidesteps it entirely. This is the reliable fallback that works even when the download cache and BITS queue are both misbehaving.

1. Find KB5041585 on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Download the x64 package for your Windows build.
3. Run the installer as administrator and restart when prompted.
4. Confirm the KB appears in Update history as successfully installed.

## Closing

A KB5041585 download stuck for hours is not slow — it is broken, and waiting will not fix it. Stop the services, delete the partial files, reset BITS, and let Windows fetch a clean copy; rule out VPN and metered-network interference along the way. And when the pipeline itself refuses to cooperate, the manual installer from the Update Catalog gets the job done without any of the drama.
