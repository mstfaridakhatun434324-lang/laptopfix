---
title: "How to Fix Windows Update Error 0x80070570 on a Dell Laptop"
slug: "how-to-fix-windows-update-error-0x80070570-on-dell-laptop"
date: 2026-10-08
categories: ["windows-update"]
tags: ["windows update", "0x80070570", "file corrupt", "dell laptop", "update error"]
description: "Error 0x80070570 means an update file is corrupt on your Dell laptop. Clear the cache, verify the download, and check disk health."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070570-on-dell-laptop.webp"
faqs:
  - q: "What does 0x80070570 mean?"
    a: >
      ERROR_FILE_CORRUPT: a file needed by the update is corrupt or
      unreadable. The corruption may be in the download itself or caused
      afterward by disk or memory problems — the fixes distinguish between
      the two. The fixes below separate a one-off bad download from
      recurring hardware-level corruption using cache clears, chkdsk, and
      memory tests.
  - q: "How do I know if it’s the download or my hardware?"
    a: >
      If a fresh download after clearing the cache installs fine, it was
      the download. If corruption recurs across fresh downloads —
      especially with manual Catalog files — suspect the disk or RAM and
      run chkdsk and the memory diagnostic. The pattern is the tell:
      one-off corruption is environmental, while repeat corruption of
      different files at different times points squarely at failing
      storage or memory.
  - q: "Can bad RAM really cause update errors?"
    a: >
      Yes. Faulty RAM corrupts data as it moves through memory, producing
      damaged files that fail integrity checks. It is an underappreciated
      cause of persistent, ‘random’ corruption errors like this one. Every
      downloaded byte passes through RAM, so a bad module can damage any
      file at any time. The Windows Memory Diagnostic (mdsched.exe)
      catches most faults — run it if corruption keeps recurring despite
      fresh downloads.
  - q: "Should I replace my SSD if chkdsk finds bad sectors?"
    a: >
      A few remapped sectors on a modern SSD are normal, but growing
      counts or repeated corruption are warning signs. Back up your data
      and check the SSD’s health with the manufacturer’s tool before
      deciding. SSDs remap bad blocks automatically up to a point; when
      the spare pool runs low or errors keep appearing, replacement time
      is near. Dell diagnostics or Samsung/Crucial/Western Digital
      utilities report the drive’s remaining life percentage.
---

Error 0x80070570 (ERROR_FILE_CORRUPT) means Windows found a file it needed for the update to be corrupt or unreadable. The file may have downloaded damaged, been corrupted on disk afterward, or failed an integrity check during installation. Either way, the update cannot proceed with a file it cannot trust.

On Dell laptops this appears in two flavors: update-payload corruption (the downloaded package is bad) and storage-level corruption (the drive or RAM mangled a good file). The first is far more common and easy to fix; the second is rarer but worth ruling out, because repeatedly ‘fixing’ a download that the hardware keeps corrupting is a losing game. Memory errors, in particular, can corrupt files in transit in ways that look exactly like bad downloads.

The plan: discard the corrupt files, verify the storage and memory underneath, and re-apply the update on a trustworthy foundation. If you are dealing with a related symptom instead, see [the 0x80070017 CRC data error](/articles/how-to-fix-windows-update-error-0x80070017-on-dell-laptop/) and [the 0x8024200D re-download error](/articles/how-to-fix-windows-update-error-0x8024200d-on-dell-laptop/).

The key question with this error is where the corruption happened, because the fix depends entirely on the answer. A damaged download is fixed in minutes by clearing the cache and fetching a clean copy; damage from a failing drive or faulty RAM will keep recurring no matter how many times you re-download. The guide below handles both paths — quick cache repair first, then the disk and memory checks that rule out the hardware causes.

## Why this happens

- **Corrupted download payload** the package arrived damaged and fails integrity checks.

- **Bad sectors on the system drive** storage corruption damages files after download.

- **Faulty RAM corrupting data in transit** memory errors mangle files during download or extraction.

- **Antivirus quarantining update files** partial quarantine leaves a broken file set.

- **Interrupted write operations** power loss mid-write leaves truncated files.

- **Corrupt SoftwareDistribution cache** stale cache serves damaged files repeatedly.

- **Failing SSD** a dying drive produces escalating corruption.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear the update cache and re-download

Removes the corrupt payload so a clean one can replace it. After clearing the cache, retry on a different network if possible; if the corruption came from a bad proxy, the same network will just corrupt the next download too. After deleting the cache, watch the re-download’s progress; if it fails at the identical byte count twice in a row, the network path — not chance — is corrupting the transfer.

1. Elevated prompt: net stop wuauserv, net stop bits.

2. Delete all contents of C:\Windows\SoftwareDistribution\Download.

3. net start wuauserv, net start bits.

4. Retry the update on a stable connection.

### Fix 2: Run the Windows Update troubleshooter

Automated detection of cache and service issues. The troubleshooter’s log at C:\Windows\Logs\WindowsUpdate tells you exactly which checks ran, which is useful if you need to escalate to manual repairs. Run the troubleshooter with the laptop plugged in and awake; some of its background resets pause when the machine sleeps, producing misleading ‘no issues found’ results.

1. Settings > System > Troubleshoot > Other troubleshooters.

2. Run Windows Update troubleshooter and apply its fixes.

3. Restart and retry.

### Fix 3: Run SFC and DISM

Repairs system-file corruption that can masquerade as payload corruption. There is no harm in running DISM and SFC even when you suspect a pure download problem; they take a while but they rule out an entire category of causes. There is real diagnostic value in the order: if DISM finds and fixes corruption, the payload theory weakens and the hardware theory strengthens, guiding your next steps.

1. Elevated prompt: DISM /Online /Cleanup-Image /RestoreHealth to 100%.

2. Then sfc /scannow.

3. Restart and retry the update.

### Fix 4: Check the disk for errors

Rules out storage-level corruption. Pay attention to whether chkdsk finds new bad sectors on a repeat run weeks later; a growing count means the drive is deteriorating and needs replacing. Note the reallocated-sector count in your SSD’s SMART data before and after the scan; a count that climbs between checks means the drive is actively deteriorating.

1. Elevated prompt: chkdsk C: /f /r, confirm, and reboot to run it.

2. Let the full check complete — it takes a while.

3. Afterward, clear the update cache once more and retry.

### Fix 5: Test the RAM with Windows Memory Diagnostic

Memory faults corrupt files invisibly; this test finds them. Run the extended memory test rather than the standard one if time allows; the standard pass misses intermittent faults that the extended patterns catch. If the extended test finds nothing but corruption persists, try reseating the RAM modules; poor contact causes intermittent faults that diagnostics sometimes miss.

1. Press Win + R, type mdsched.exe, press Enter.

2. Choose ‘Restart now and check for problems’.

3. Let the test complete and note any errors on reboot.

4. If errors appear, the RAM needs replacement — no software fix will hold.

### Fix 6: Temporarily disable third-party antivirus

Prevents quarantine interference during the fresh download. If the update succeeds with protection off, do not just re-enable and forget — add the exclusions, or the same quarantine will strike the next update. Consider switching to Windows Security temporarily instead of just disabling the third-party suite; a disabled-but-present suite can still hook file operations.

1. Disable real-time protection temporarily.

2. Clear the update cache (Fix 1) and retry the download.

3. Re-enable protection once installed.

### Fix 7: Install the update manually from the Catalog

A direct download bypasses the suspect automatic pipeline. Compare the SHA-256 hash of the downloaded .msu with the Catalog’s published value when corruption is suspected; a mismatch proves the download is the problem. Save the .msu to the local disk rather than running it from a network share; SMB transfers add another corruption opportunity that muddies the diagnosis.

1. Find the KB number in update history.

2. Download the x64 .msu from [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).

3. If the manual file also reports corruption, suspect RAM or disk — run Fixes 4 and 5.

4. Otherwise, install it and restart.

## Closing

Error 0x80070570 is Windows refusing to build on a rotten file, which is the right call. Clear the corrupt payload, verify the disk and memory underneath it, and the re-downloaded update will install on solid ground. For official guidance, see [Microsoft’s Windows update support hub](https://support.microsoft.com/en-us/windows).
