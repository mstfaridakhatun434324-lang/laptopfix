---
title: "KB5036893 Stuck Downloading on Windows 10? Here's the Fix"
slug: how-to-fix-kb5036893-stuck-downloading-on-windows-10
date: 2026-10-12
categories: ["windows-update"]
tags: ["kb5036893", "stuck downloading", "windows 10", "windows update"]
description: "Fix KB5036893 stuck downloading on Windows 10: reset the update agent, clear the download queue, and install the update without the endless wait."
thumbnail: "/images/thumbs/how-to-fix-kb5036893-stuck-downloading-on-windows-10.webp"
faqs:
  - q: "Is KB5036893 available for Windows 10?"
    a: "KB numbers are shared across Windows versions with version-specific packages. On Windows 10 the equivalent monthly rollup may carry the same KB number with a different build. The stuck-download mechanics — BITS jobs, the SoftwareDistribution cache, and metered connections — are identical on Windows 10."
  - q: "Where is the update troubleshooter on Windows 10?"
    a: "Open Settings, then Update and Security, then Troubleshoot, then Additional troubleshooters, and run Windows Update from the list. Windows 10 keeps the classic troubleshooter layout rather than Windows 11's reorganized path, but it performs the same repairs to services, registrations, and permissions."
  - q: "Can I install the update with the Media Creation Tool instead?"
    a: "The Media Creation Tool is for Windows 11 and Windows 10 feature upgrades, not monthly cumulative updates. For a stuck monthly KB, the Microsoft Update Catalog's standalone .msu package is the right manual path — it is the same signed update without the Windows Update pipeline."
  - q: "Why does Windows 10 show 0% for so long?"
    a: "The progress bar often sits at 0% while BITS negotiates and while the package is verified before the counter moves. Give it thirty minutes of idle time. If Task Manager shows no network activity at all in that window, the download is genuinely stuck."
---

Windows 10 handles updates a little differently from Windows 11, but a stuck download feels exactly the same: KB5036893 frozen at some percentage, no error, no progress, just a spinner and growing suspicion. On Windows 10 the usual suspects are the older update agent's quirks, a wedged BITS queue, and the peer-to-peer sharing that Windows 10 enables aggressively.

The fix sequence below is tuned for Windows 10's menus and behaviors. Follow it top to bottom and the download will either resume or be replaced by a manual install that just works.

A quick note on patience versus action: Windows 10's progress reporting is notoriously coarse, so verify with Task Manager before you start resetting things. But once you have confirmed zero network activity for half an hour, stop waiting — every additional hour of hoping is an hour you could spend fixing it.

## Why this happens

- **Wedged BITS jobs:** Windows 10's Background Intelligent Transfer Service queues can stall and never time out on their own.
- **Corrupt SoftwareDistribution cache:** Partial downloads from interrupted sessions poison the cache the downloader resumes from.
- **Delivery Optimization P2P stalls:** Windows 10 shares updates with other PCs by default, and bad peers stall the whole download.
- **Metered connection throttling:** A connection marked metered silently pauses cumulative update downloads on Windows 10.
- **Windows Update service in a bad state:** The wuauserv service can end up half-started after a failed update cycle.
- **Proxy or VPN interference:** System-wide proxies and VPNs break the CDN endpoints Windows Update prefers.
- **Antivirus download inspection:** Real-time scanners can choke the large .msu stream mid-download.
- **Failing disk sectors:** On older Windows 10 laptops with aging HDDs, bad sectors in the staging area cause repeated silent write failures — the same hardware angle behind many [post-clean-install update failures](/articles/how-to-fix-windows-update-error-after-clean-install-on-windows-10/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall with Task Manager

1. Note the percentage shown in **Settings → Update & Security → Windows Update**.
2. Open **Task Manager → Performance** and watch the network graph for five minutes.
3. Zero meaningful traffic for 30+ minutes means stuck, not slow.
4. Also check free space on C: — under 10 GB free can stall staging silently.

### Fix 2: Restart the Windows Update service properly

1. Press **Win + R**, type `services.msc`, and find **Windows Update**.
2. If it shows Running, right-click and **Restart** it; if it shows anything else, start it.
3. Do the same for **Background Intelligent Transfer Service**.
4. Return to Windows Update and click **Check for updates** — a clean service restart unblocks many stalls.
5. If the service refuses to stay running, note that — it points at deeper corruption that Fix 4's cache reset addresses.

### Fix 3: Run the Windows 10 update troubleshooter

1. Go to **Settings → Update & Security → Troubleshoot → Additional troubleshooters**.
2. Run **Windows Update** and apply all suggested fixes.
3. Reboot when prompted, then check for updates again.
4. The troubleshooter re-registers the update DLLs that Windows 10's older agent sometimes loses.

### Fix 4: Clear the SoftwareDistribution download folder

1. In an elevated Command Prompt: `net stop wuauserv` and `net stop bits`.
2. Delete all contents of `C:\Windows\SoftwareDistribution\Download`.
3. Restart both services with `net start wuauserv` and `net start bits`.
4. Check for updates — the download restarts cleanly from zero.
5. If the percentage freezes at the exact same point again, the network path itself is suspect — try a mobile hotspot to isolate it.

### Fix 5: Disable peer-to-peer update sharing

1. Go to **Settings → Update & Security → Delivery Optimization**.
2. Turn off **Allow downloads from other PCs** entirely.
3. This forces a direct download from Microsoft, removing bad peers from the equation.
4. Retry the update and watch the percentage — direct downloads rarely stall the same way.

### Fix 6: Check metered connection and proxy settings

1. In **Settings → Network & Internet → Wi-Fi**, select your network and turn off **Set as metered connection**.
2. Check **Settings → Network & Internet → Proxy** for any unexpected manual proxy.
3. Disconnect any VPN for the duration of the download.
4. Corporate and school networks with filtering proxies are frequent culprits — try a home network if one is available.

### Fix 7: Reset the network components

1. In an elevated Command Prompt, run `netsh winsock reset` and `netsh int ip reset`, then reboot.
2. After rebooting, run `ipconfig /flushdns`.
3. Reconnect and retry the download on the fresh stack.
4. Microsoft documents these network reset steps on the [Windows support hub](https://support.microsoft.com/en-us/windows) for persistent connectivity issues.

### Fix 8: Install the KB manually from the Update Catalog

1. Search KB5036893 on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and download the Windows 10 x64 package.
2. Close everything, disconnect the VPN, and run the .msu.
3. Reboot and confirm the update in **View update history**.
4. Manual installation bypasses the entire stuck pipeline. If you also run Windows 11 on another machine, the [Windows 11 version of this fix](/articles/how-to-fix-kb5036893-stuck-downloading-on-windows-11/) covers its different menus.

## Closing

On Windows 10, a stuck KB5036893 download is almost always the update agent's own state: a wedged BITS job, a poisoned download cache, or peer-to-peer sharing gone wrong. Restart the services, run the classic troubleshooter, clear the cache, disable P2P sharing, and check metered settings. When the pipeline refuses to cooperate, the catalog's standalone installer gets the update on the system in minutes.

Going forward, keep Delivery Optimization's PC-to-PC sharing off unless you are on a fast LAN with other Windows 10 machines, and do not let the system drive drop below 15 GB free. Windows 10's updater is less forgiving of tight storage than Windows 11's, and most "mystery" stalls trace back to one of those two settings. A monthly manual check for updates beats waiting for the automatic cycle to surprise you.
