---
title: "How to Fix Windows Update Error 0x80070017 on a Lenovo Laptop"
slug: "how-to-fix-windows-update-error-0x80070017-on-lenovo-laptop"
date: 2026-09-07
categories: ["windows-update"]
tags: ["error 0x80070017", "windows update", "lenovo laptop", "crc error", "windows 11"]
description: "Windows Update error 0x80070017 means CRC check failures — corrupted downloads or failing hardware on your Lenovo laptop. Seven fixes inside."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070017-on-lenovo-laptop.webp"
faqs:
  - q: "What does error 0x80070017 mean?"
    a: "It means ERROR_CRC: downloaded data failed its cyclic redundancy check, a checksum proving the bits changed somewhere in transit or storage. The installer saw that the update no longer matched its expected checksum and refused it. The corruption can come from the network path, RAM flipping bits in transit, bad disk sectors, overheating parts, or a poisoned cache recycling already-damaged files."
  - q: "Is CRC failure always a hardware problem?"
    a: "No — one CRC failure is usually just a bad download, and a fresh copy resolves it. Hardware becomes the suspect when checksum failures repeat across different updates and networks. The pattern is what matters: a single failure is noise, but every large download failing checksums is faulty RAM or a dying drive announcing itself. Test the hardware before blaming the network."
  - q: "Why do only large updates fail CRC?"
    a: "Probability. A bit-flip rate that corrupts one large file will likely spare small ones — a 5 GB cumulative update has roughly a thousand times more bits at risk than a 5 MB definition update. Small updates succeeding while large ones fail checksums is the textbook signature of marginal RAM or a flaky network path, and it is highly diagnostic of the cause."
  - q: "Can I ignore a CRC error and install anyway?"
    a: "No, and Windows will not let you try — the installer rejects checksum-failed payloads because installing corrupted system files could leave the machine unbootable. There is no supported bypass, and unofficial ones risk genuine damage. The correct answer is always to obtain clean data and fix whatever corrupted it, not to force damaged bits into your operating system."
---

Error 0x80070017 is a failed cyclic redundancy check — the mathematical checksum on the downloaded data does not add up, which proves the bits changed somewhere between Microsoft and your Lenovo laptop. CRC is deliberately unforgiving: a single flipped bit fails the whole check, and the installer rejects the damaged goods outright.

The puzzle is where the damage happened. Network, disk, and RAM can all flip bits. If files arrive structurally unreadable rather than merely checksum-failed, the [0x800F0831 missing-prerequisite guide](/articles/how-to-fix-windows-update-error-0x800f0831-on-lenovo-laptop/) addresses that adjacent error instead.

Work from the cheapest cause outward: get a fresh download first, then interrogate the hardware that might be damaging it. The disk and memory tests below are not optional extras — they are the point of this guide.
## Why this happens

- **Bit corruption in transit:** Noisy connections, bad cables, or ailing network hardware can flip bits during the long transfers that updates demand.
- **Failing system RAM:** Memory is the classic CRC villain — data passes through RAM between the network and the disk, and bad RAM damages it on the way.
- **Bad sectors on the drive:** Sectors that write unreliably corrupt whatever they store, failing checksums when the data is read back.
- **Overheating components:** Heat-induced errors in memory or storage controllers show up as random bit flips under sustained load.
- **A dying network adapter:** A failing Wi-Fi or Ethernet chip can corrupt packets in ways that lower-layer checksums occasionally miss.
- **Unstable power delivery:** Voltage sags during writes can leave bits in indeterminate states that read back wrong.
- **Poisoned cache reuse:** Once a checksum-failed file lands in the cache, every retry reuses it and fails identically until the cache is purged.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Purge the update cache and start over

A corrupted file sitting in the cache will fail checksums forever, no matter how many times you retry. Stopping the update services and renaming the SoftwareDistribution and catroot2 folders forces Windows to rebuild them empty, so the next attempt downloads genuinely fresh bits instead of recycling the damaged ones.

1. Bring up an elevated Command Prompt — right-click the Start button and choose Terminal (Admin).
2. Shut down the update services with net stop wuauserv, net stop cryptSvc, net stop bits, and net stop msiserver.
3. Give both folders .old names: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Fire the services back up with net start, then retry the update check.

### Fix 2: Reset networking to a clean state

When the corruption happens in transit, the network stack is the suspect. Stale DNS entries, damaged socket configuration, and lingering proxy settings can all mangle the connection to Microsoft's servers; a stack reset returns everything to known-good defaults without touching files or applications.

1. Launch an elevated prompt with admin rights.
2. Execute ipconfig /flushdns, then netsh winsock reset and netsh int ip reset.
3. Restart the machine so the reset applies.
4. Reconnect and retry the update now that the stack is clean.

### Fix 3: Test the RAM with Windows Memory Diagnostic

Veteran troubleshooters run this one almost by reflex when CRC errors recur. Faulty memory corrupts data in transit, and update packages are large enough that a marginal stick will damage them during download or extraction. If checksum failures keep appearing across different updates, the memory — not the network — is the likely culprit. Test RAM with mdsched.exe: bad memory is the number-one hardware cause of CRC failures, per Microsoft's [official Windows support hub](https://support.microsoft.com/en-us/windows).

1. Hit Win + R, type mdsched.exe, and press Enter.
2. Pick Restart now and check for problems.
3. Allow the full test to complete and note any errors it finds.
4. If errors show up, reseat or replace the faulty module before updating again.

### Fix 4: Hunt for bad sectors on the disk

Damaged sectors corrupt files as they are written, and update payloads are big targets. A full disk check scans for physical defects and moves data away from damaged areas, cutting the corruption off at its source.

1. Open an elevated Command Prompt for this.
2. Run chkdsk C: /f /r and approve the check for the next restart.
3. Reboot and let the full scan finish — large drives can take an hour.
4. Try the update again once the disk check comes back clean.

### Fix 5: Grab the update manually from the Update Catalog

Sidestep the damaged pipeline entirely. When automatic delivery keeps producing checksum failures, downloading the package yourself skips the whole broken download path. The Microsoft Update Catalog publishes each cumulative update as a standalone installer, and a manual install often succeeds where Windows Update stalls. The standalone package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) hands you fresh bits with valid checksums.

1. Open Settings, go to Windows Update and Update history, and record the failing update's KB number.
2. Type the KB number into the Microsoft Update Catalog site and open its page.
3. Download the x64 edition for your Windows 11 build.
4. Double-click the .msu file, walk through the installer, and restart when prompted.

### Fix 6: Switch to a completely different network

Some networks mangle large downloads in ways that masquerade as system errors — office firewalls, campus filters, ISP-level caching proxies. Moving to a totally different connection, even briefly, proves whether the network or the laptop is at fault.

1. Disconnect from your current Wi-Fi network.
2. Join a mobile hotspot or a different Wi-Fi network.
3. In Settings, Network and internet, confirm the connection is not set as metered.
4. Try the update once more over the new connection.

### Fix 7: Check system files with SFC

Corrupted Windows files can sabotage the installer in subtle ways that look like download damage. The System File Checker scans every protected file against a known-good copy and repairs what it finds, removing a whole category of failures at once.

1. Bring up an elevated Command Prompt or Terminal (Admin).
2. Run sfc /scannow from the prompt and wait for completion.
3. Reboot the laptop if the scan repaired files.
4. Re-run the update install after the reboot.

## Closing

CRC errors are the checksum doing its job — refusing damaged data before it can hurt your system. Respect the signal: clear out the bad bits, then verify the hardware chain that carried them. Most cases here end at either a fresh download or a replaced RAM stick. Lenovo owners with removable memory can also check the Lenovo support site for their model's memory specs before buying a replacement stick. If downloads fail outright instead of failing checks, the [0x80240034 download-failure guide](/articles/how-to-fix-windows-update-error-0x80240034-on-lenovo-laptop/) covers that neighboring problem.
