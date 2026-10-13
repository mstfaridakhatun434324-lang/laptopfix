---
title: "Windows Update Stuck Downloading on an Acer Laptop? Fix It"
slug: how-to-fix-windows-update-stuck-downloading-on-acer-laptop
date: 2026-10-02
categories: ["windows-update"]
tags: ["update stuck downloading", "acer", "windows update", "bits"]
description: "Update download frozen on your Acer laptop? BITS, cache corruption, and Acer power profiles are the usual causes. Work this ordered fix list."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-downloading-on-acer-laptop.webp"
faqs:
  - q: "Why does the download freeze at the same percentage every time?"
    a: "Because the transfer service validates each chunk and keeps rejecting the same corrupted segment. The cache holds the damaged partial download, so every retry trips over the same bad data until the cache is cleared. Clearing the SoftwareDistribution cache removes the damaged segment and is the direct fix."
  - q: "Do Acer's power settings affect update downloads?"
    a: "Yes. Acer's aggressive battery-saver profiles can throttle background network activity, and the wireless adapter's power-saving setting can drop the connection mid-transfer. Both are worth disabling while a large update downloads. Switch to Best performance and AC power for the duration of large downloads, then restore your preferences."
  - q: "How is a stuck download different from a failed update?"
    a: "A stuck download never completed, so there is nothing to roll back and no error code — just a frozen percentage. Failed updates, by contrast, downloaded fully and then failed installation. The fixes differ accordingly: downloads need pipeline repair, failures need package repair."
  - q: "Can I just download the update manually instead?"
    a: "Yes, and it is often the fastest resolution. The Microsoft Update Catalog hosts every KB as a standalone installer that bypasses BITS and the cache entirely. If the pipeline will not cooperate, the manual path gets the update installed today."
---

The update starts downloading on your Acer laptop, reaches some percentage, and freezes there. An hour later it has not moved. Retry, and it climbs back to the same number and stops again, like a commuter hitting the same traffic jam every morning. Nothing has failed — the update simply never finishes arriving.

Download stalls are plumbing problems: the Background Intelligent Transfer Service, the local cache, or the network path. On Acer laptops, add power-management profiles that throttle background transfers to the suspect list. The fixes below run from the two-minute service restart to the manual download that skips the plumbing entirely.

Windows Update downloads do not come from a single server. Microsoft distributes updates through a global CDN, and your machine is routed to an edge node based on network conditions — plus Delivery Optimization may pull chunks from other PCs. Most of the time this is invisible, but a bad edge node or a misbehaving peer can stall a download that has nothing wrong with it locally. That is why the same update downloads fine on one network and freezes on another. When local fixes fail, changing the network path is a legitimate diagnostic step.

## Why this happens

- **BITS stalled mid-transfer.** The transfer engine wedges and stops pulling data.
- **Corrupted partial download looping.** Damaged chunks fail validation and the download restarts or freezes.
- **Acer power profiles throttling background transfers.** Battery-saver settings starving BITS of network access.
- **Wireless adapter power-saving drops.** The radio sleeping mid-transfer and corrupting in-flight chunks.
- **Metered connection pausing the download.** Windows halting large transfers on metered networks.
- **VPN or firewall interference.** Security software breaking the CDN connection.
- **Disk errors damaging cached chunks.** Storage corruption altering the partial download.
- **A bad CDN edge node or peer.** Microsoft's distributed delivery can route you to a malfunctioning edge node, stalling downloads that are healthy on other networks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall

Thirty seconds of diagnosis.

1. Note the percentage, wait 30 minutes, confirm zero movement.
1. Check Task Manager > **Performance** for network activity.
1. Verify general internet works.
1. A true stall shows no network activity and no progress — proceed.

### Fix 2: Restart BITS and wuauserv

The quick unwedge.

1. Elevated Command Prompt: `net stop wuauserv`, `net stop bits`.
1. Wait 30 seconds, then `net start bits`, `net start wuauserv`.
1. Check for updates and watch for 15 minutes.
1. If the download resumes, the service was wedged — done.

### Fix 3: Disable Acer power throttling during the download

The Acer-specific step other brands skip.

1. Set the power mode to **Best performance** in **Settings** > **System** > **Power & battery**.
1. In Device Manager, uncheck power-saving on the Wi-Fi adapter.
1. Plug into AC power — background transfers throttle on battery.
1. Keep the lid open and the machine awake during the download.

### Fix 4: Clear the download cache

Removes the corrupted partial data.

1. Stop wuauserv, cryptSvc, bits, msiserver.
1. Rename `C:\Windows\SoftwareDistribution` to `C:\Windows\SoftwareDistribution.old`.
1. Restart the services.
1. Let the download restart from zero uninterrupted. For the Dell-side parallel, see [update stuck downloading on Dell](/articles/how-to-fix-windows-update-stuck-downloading-on-dell-laptop/).

### Fix 5: Stabilize the network

Chunk corruption feeds on flaky connections.

1. Prefer Ethernet for large updates.
1. Disable the VPN temporarily.
1. Confirm the connection is not marked metered.
1. Move closer to the router if Wi-Fi is the only option.

### Fix 6: Troubleshoot and repair components

For stalls surviving the above.

1. Run the **Windows Update** troubleshooter.
1. Run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
1. Restart and retry.
1. If `chkdsk C: /f` finds disk errors, clear the cache once more after repair. The [Asus stuck-downloading guide](/articles/how-to-fix-windows-update-stuck-downloading-on-asus-laptop/) covers the same pipeline on different hardware.

### Fix 7: Install manually from the Catalog

The guaranteed path around a broken pipeline.

1. Find the KB number in **Update history**.
1. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
1. Run the .msu installer and restart.
1. No BITS, no cache, no stall. For broader update-pipeline documentation, [Microsoft support](https://support.microsoft.com/en-us/windows) covers the full reset procedure.

### Fix 8: Change the network path as a diagnostic

Rules out CDN and peer problems in one test.

1. Try the download on a different network — phone hotspot, neighbor's Wi-Fi, office.
1. If it completes elsewhere, the stall is path-related, not machine-related.
1. Toggle Delivery Optimization's peer-to-peer off and retry on the original network.
1. A path-dependent stall resolves itself or responds to the network reset in Fix 6.

## Closing

Acer download stalls come down to the transfer service, the cache, the network, or Acer's own power throttling — usually in that order of likelihood. Restart the services, clear the cache, give the download full power and a stable connection, and it completes. And when the pipeline refuses to cooperate, the manual Catalog install ends the standoff on your terms. If the download only stalls on your home network, the router deserves a look — outdated firmware and aggressive QoS rules throttle update traffic in ways that mimic every local failure mode. Acer's power profiles are the silent partner in most of these stalls, so make the download environment deliberate: Best performance mode, AC power, lid open, machine awake. Background transfers are designed to be invisible, which means they also yield — to power saving, to sleep, to anything the system prioritizes higher. Remove the competition and BITS does in twenty minutes what it could not do in six hours. Keep a phone hotspot configured as the alternate network path for the day the home network is the problem, and remember the manual Catalog install as the permanent escape hatch for any single stubborn KB. The download will finish; the only variable is how much of your evening it costs.
