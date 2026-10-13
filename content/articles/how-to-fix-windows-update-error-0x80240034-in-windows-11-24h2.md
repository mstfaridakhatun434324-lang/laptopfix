---
title: "How to Fix Windows Update Error 0x80240034 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80240034-in-windows-11-24h2
date: 2026-10-04
categories: ["windows-update"]
tags: ["windows update", "0x80240034", "error code", "windows 11", "download"]
description: "Error 0x80240034 means a Windows Update download failed or stalled. Clear the download cache, fix metered settings, and retry."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80240034-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80240034 mean?"
    a: "WU_E_DOWNLOAD_FAILED: the update download failed. This is the download phase specifically — the update was found and approved, but fetching its payload broke down. The cause is usually a corrupted partial download, a metered connection quietly blocking, or antivirus mangling the file stream."
  - q: "Why does the download keep failing at the same percentage?"
    a: "A corrupted partial download. Windows resumes the broken file instead of starting over, so it stalls at the same point every time. Deleting the SoftwareDistribution Download cache forces a genuinely fresh fetch and usually breaks the pattern."
  - q: "Can a metered connection cause this error?"
    a: "Yes — metered connections pause or throttle downloads silently, which the engine can report as a download failure. Check Settings > Network & internet > Wi-Fi, open your connection, and switch off Metered connection before retrying. Mobile hotspots set this automatically."
  - q: "Is it safe to delete the SoftwareDistribution folder?"
    a: "Yes. It holds only cached downloads and update metadata — Windows rebuilds it on the next update check. Rename rather than delete (SoftwareDistribution.old) so you have a fallback, and only stop the update services while doing it."
---

The update was found. It was approved. And then the download collapsed. That is the whole story of 0x80240034 — WU_E_DOWNLOAD_FAILED, the download phase specifically. Everything upstream worked; fetching the payload broke down.

The usual villains are a corrupted partial download that Windows keeps resuming instead of replacing, a metered connection quietly throttling, or antivirus mangling the file stream mid-transfer. Big cumulative updates on flaky connections stall the most.

The key diagnostic never lies: a download stalling repeatedly at the same percentage means the partial file is poisoned, while an instant failure points at a blocker. Fix 1's observations route you to the right repair — guessing costs more time than the two minutes of observation. If it fails instantly, the metered setting or antivirus is the likelier author.

## Why this happens

- **Partial downloads are corrupt.** Interrupted fetches leave broken fragments that resume loops keep reusing.
- **The connection is metered.** Metered settings pause or throttle downloads without an obvious warning.
- **Antivirus mangles the stream.** Overzealous scanning corrupts or quarantines chunks mid-download.
- **Wi-Fi drops mid-transfer.** Unstable wireless breaks long downloads that can't resume cleanly.
- **Disk space is too tight.** Downloads need working room beyond the final package size.
- **The BITS queue is wedged.** Damaged Background Intelligent Transfer Service jobs stall the queue.
- **VPN or proxy interrupts.** Middleboxes that cut long streams produce failed downloads.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Assess the connection and the download state

The stall pattern names the cause: same percentage means poisoned cache, instant failure means a blocker.

1. Note the percentage where the download stalls, if it shows one.
2. Confirm the Wi-Fi signal is strong and stable — move closer to the router if not.
3. Check free space on the system drive; free up several gigabytes if it is tight, since cramped disks abort downloads mid-write.
4. Same-percentage stalls go to Fix 3 first; instant failures go to Fix 2. This routing is the whole point of the diagnosis — the two failure modes have almost no overlap in their repairs.

### Fix 2: Disable the metered connection completely

Metered connections pause downloads silently, and mobile hotspots enable this setting automatically — often without any visible banner. This is the most common ‘invisible’ cause on laptops, which hop between home Wi-Fi and phone hotspots constantly.

1. Open Settings > Network & internet > Wi-Fi (or Ethernet) and open your connection.
2. Switch off the Metered connection toggle.
3. If you tether from a phone, check the hotspot's own metered setting too.
4. Retry the download and watch whether it proceeds past its previous stall point. The full [metered-connection guide](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/) covers stubborn cases where the toggle alone does not stick.

### Fix 3: Delete the corrupted partial downloads

A poisoned cache is the classic same-percentage stall, and deleting it is the single highest-yield repair in this guide. Windows keeps resuming the broken fragment because resuming is cheaper than refetching — until you prove the fragment is the problem by removing it. Deleting it forces a genuinely fresh fetch.

1. From an elevated Command Prompt, run `net stop wuauserv` and `net stop bits`.
2. Open `C:\Windows\SoftwareDistribution\Download` and delete its contents.
3. Restart the services: `net start wuauserv` and `net start bits`.
4. Check for updates — the download starts over from zero.

### Fix 4: Ease off antivirus while the download runs

Security software that scans every chunk can corrupt the stream or quarantine pieces mid-transfer. The irony is sharp: the protector becomes the saboteur, and the failure looks exactly like a network problem — which is why Fix 4's controlled test matters.

1. Temporarily disable real-time protection in your antivirus — re-enable it immediately after.
2. If the download succeeds with protection off, add a Windows Update exclusion permanently.
3. Retry the download while protection is paused.
4. Restore full protection the moment the download completes — never leave the system unguarded longer than the test requires.

### Fix 5: Let the troubleshooter examine the download

The troubleshooter detects stuck download states and damaged BITS jobs, repairing them automatically.

1. Make for Settings > System > Troubleshoot > Other troubleshooters.
2. Commence the Windows Update entry and follow its prompts to the end.
3. Reboot the machine and re-attempt the download.

### Fix 6: Restore the Windows Update components

If the download cache and services are both suspect, a full reset rebuilds the entire download pipeline.

1. Mute the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Corral the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Rekindle the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Fetch updates and confirm the download pipeline is healthy.

### Fix 7: Grab the update manually from the Catalog

A browser download uses completely different machinery — resumable by design, throttled differently, unbothered by BITS. When every engine-side repair fails, this alternative path is not a workaround but the rational choice: the payload is identical, only the delivery truck changes. The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) archives every cumulative release.

1. Capture the KB number from Update history.
2. Secure the x64 Windows 11 package via your browser.
3. Start the `.msu` and reboot if asked. Browser downloads resume cleanly after interruptions, which is precisely the capability the broken engine lacked.

## Closing

Downloads fail for boring reasons — poisoned caches, metered flags, jittery antivirus — and each has a boring fix. The boring fix that worked is worth remembering, because download failures are chronic on machines with flaky Wi-Fi, and the same repair will serve you every Patch Tuesday. If other phases fail instead of the download, the [24H2 update-error guide](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) decodes them. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official download troubleshooting.
