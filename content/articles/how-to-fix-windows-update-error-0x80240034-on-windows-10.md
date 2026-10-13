---
title: "Fix Windows Update Error 0x80240034 on Windows 10: Download Failed"
slug: how-to-fix-windows-update-error-0x80240034-on-windows-10
date: 2026-09-08
categories: ["windows-update"]
tags: ["windows 10", "windows update", "error 0x80240034", "download failed", "troubleshooting"]
description: "Error 0x80240034 on Windows 10 means the update download failed. Repair the download pipeline with these Windows 10-specific steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80240034-on-windows-10.webp"
faqs:
  - q: "What does 0x80240034 mean on Windows 10?"
    a: "It is the download-failed error (WU_E_DOWNLOAD_FAILED). Windows 10 found the update but could not download its files completely. The usual culprits are BITS problems, a corrupted download queue, VPN or proxy interference, and unstable connections — not the update itself."
  - q: "Why does the download fail at the same percentage each time?"
    a: "A consistent failure point suggests a corrupted partial file in the queue that every retry chokes on, or a network device (proxy, firewall) blocking a specific content range. Clearing the SoftwareDistribution download folder eliminates the local cause; testing on a different network eliminates the network cause."
  - q: "Can low disk space cause 0x80240034?"
    a: "Yes. If the drive fills up mid-download, the transfer cannot complete and fails with this error. Windows 10 needs the full package size plus staging room free. Check that C: has at least 10 GB free before retrying, and run Disk Cleanup if space is tight."
  - q: "Is there a way to download the update without Windows Update?"
    a: "Yes — the Microsoft Update Catalog lets you download the same update as a standalone .msu file through your browser, bypassing BITS entirely. This is the most reliable workaround when the automated download pipeline keeps failing, and the resulting install is identical to one delivered through Windows Update."
---

Windows 10 reports error 0x80240034 when an update's download fails — the files never arrived intact, so there was nothing to install. This is a pipeline error, not a system error: your Windows installation is fine, but the machinery that fetches updates is not. On Windows 10, the usual suspects are the BITS download service, a poisoned download queue, VPN/proxy interference, and the metered-connection gotchas that Windows 10 applies enthusiastically.

Because the error is specific to downloading, the fix sequence stays in the download layer: network path, services, queue, DNS, antivirus, and finally the manual-download bypass. Work through them using Windows 10's menus below.

## Why this happens

- **BITS service problems:** The Background Intelligent Transfer Service hung, disabled, or misconfigured.
- **Corrupted partial downloads:** Damaged files in the download queue that every retry trips over.
- **VPN or proxy breaking BITS traffic:** Intermediaries that handle browser traffic fine but mangle BITS transfers.
- **Unstable Wi-Fi:** Drops during large transfers that BITS cannot always resume from cleanly.
- **Metered connection throttling:** Windows 10 aggressively limits update downloads on metered connections.
- **Antivirus blocking payloads:** Real-time protection quarantining update files mid-download.
- **DNS resolution failures:** Cannot resolve Microsoft's delivery endpoints.
- **Full system drive:** Download cannot complete when C: fills up.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the network path and metered status

Eliminate environmental causes first.

1. Disconnect the VPN entirely and retry — VPN interference is a top cause of this error.
2. Go to **Settings > Network & Internet > Wi-Fi**, click your network, and ensure **Set as metered connection** is **Off**.
3. Check proxy settings under **Settings > Network & Internet > Proxy** and disable any proxy you do not actively need.
4. Retry the update.

### Fix 2: Restart BITS and Windows Update services

Revive the download machinery.

1. Press **Win + R**, type `services.msc`, press Enter.
2. Restart **Background Intelligent Transfer Service** and **Windows Update** (start them if stopped).
3. Go to **Settings > Update & Security > Windows Update** and click **Retry**.

### Fix 3: Run the Windows Update troubleshooter

Automated repair of BITS registration and the download queue.

1. Open **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply all fixes.
3. Restart and retry.

### Fix 4: Empty the SoftwareDistribution download folder

Remove the poisoned partial files causing repeat failures.

1. Open **Command Prompt (Admin)**.
2. Run `net stop wuauserv` and `net stop bits`.
3. In File Explorer, delete everything inside `C:\Windows\SoftwareDistribution\Download`.
4. Run `net start wuauserv` and `net start bits`.
5. Check for updates — the download restarts cleanly. This mirrors the fix for [frozen downloads](/articles/how-to-fix-windows-update-stuck-downloading-step-by-step/), which shares the same queue mechanics.

### Fix 5: Flush DNS and reset the network stack

For downloads that fail instantly, suspect name resolution or stack damage.

1. In **Command Prompt (Admin)**, run `ipconfig /flushdns`, then `netsh winsock reset`, then `netsh int ip reset`.
2. Restart the laptop.
3. If problems persist, set a public DNS (8.8.8.8 / 1.1.1.1) in the adapter properties.

### Fix 6: Verify disk space and pause antivirus scanning

Two quick environmental checks.

1. Confirm at least 10 GB free on C: via **Settings > System > Storage**; run Disk Cleanup if needed.
2. Temporarily disable real-time antivirus protection and retry the download immediately.
3. Re-enable protection after the download finishes.
4. If antivirus was the blocker, exclude the SoftwareDistribution folder permanently.

### Fix 7: Install the update manually from the Update Catalog

The definitive bypass: note the KB number, download the `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) in your browser, and install it directly. Browser-based downloading sidesteps BITS, the queue, and proxy quirks in one move. After a successful manual install, run the standard update-component reset to restore the automated pipeline for next month — see the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows) for the current procedure.

Windows 10's relationship with metered connections deserves a paragraph of its own, because it causes more 0x80240034 errors than any other single setting. Windows 10 treats metered connections conservatively: it pauses most update downloads entirely and throttles the rest. The trap is that the metered flag is per-network and sticky — set it once on a hotel Wi-Fi to save data, and months later you may simply forget it is on. Whenever downloads fail on Windows 10, the metered check is thirty seconds that pays for itself. Beyond that, consider the age of the BITS configuration on long-lived Windows 10 installs: years of VPN clients, proxy experiments, and privacy scripts can leave the download service in a state no single reset fully cleans. If you have tried every fix here and downloads still fail, the full component reset — stopping services, renaming both cache folders, re-registering the update DLLs — is worth doing as one combined operation rather than piecemeal. And remember the escape hatch: the Update Catalog manual download uses your browser's networking, which is almost always healthier than a long-abused BITS configuration. For the Windows 11 variant, see our [Windows 11 0x80240034 guide](/articles/how-to-fix-windows-update-error-0x80240034-on-windows-11/).

Finally, a note on patience versus action: a download that is moving slowly is not a download that has failed. BITS deliberately yields bandwidth to your foreground activity, so a large cumulative update can take a couple of hours on a busy connection without anything being wrong. The signal to act is the error code itself or a progress bar frozen for hours on an idle machine — not mere slowness. Give a slow-but-moving download the time it needs, preferably overnight with the charger connected and sleep disabled.

## Closing

On Windows 10, 0x80240034 is the download pipeline telling you it cannot deliver. Work the pipeline from the outside in — network and VPN, BITS service, download queue, DNS, disk space, antivirus — and use the Update Catalog manual download whenever the automated path refuses to cooperate. The update itself is fine; once delivery works, installation follows.
