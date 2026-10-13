---
title: "Fix a Cumulative Update That Won't Install on Windows 11 24H2"
slug: how-to-fix-cumulative-update-fails-to-install-in-windows-11-24h2
date: 2026-10-12
categories: ["windows-update"]
tags: ["cumulative update fails", "windows 11 24h2", "update won't install", "kb update error"]
description: "A cumulative update keeps failing to install on Windows 11 24H2? Diagnose the cause and apply proven fixes, from cache resets to manual installation."
thumbnail: "/images/thumbs/how-to-fix-cumulative-update-fails-to-install-in-windows-11-24h2.webp"
faqs:
  - q: "Why do cumulative updates fail to install on Windows 11 24H2?"
    a: "The usual suspects are a corrupt download cache, an outdated servicing stack, or a conflict with a driver or security product. Cumulative updates are large single packages, so any interruption during download or a mismatch in the component store causes the whole package to roll back instead of installing."
  - q: "Should I keep retrying a failed cumulative update?"
    a: "Two or three retries are fine, but if it fails identically every time, stop retrying and diagnose. Repeated identical failures mean a systemic problem — a bad cache, a blocking driver, or a damaged component store — that another attempt will not fix on its own."
  - q: "Is it safe to install a cumulative update manually from the Catalog?"
    a: "Yes. The Microsoft Update Catalog hosts the exact same signed packages Windows Update delivers. Download the update matching your architecture (x64 for most laptops), install the servicing stack update first if one is listed, then install the cumulative update MSU package."
  - q: "How do I find which cumulative update keeps failing?"
    a: "Open Settings → Windows Update → Update history. Failed updates appear with an error code such as 0x800f0922 or 0x80073712. Note the KB number — you will use it to download the package manually and to look up known issues for that specific release."
---

Cumulative updates are the monthly backbone of Windows 11 servicing: one package carrying every security and quality fix since the last one. When a cumulative update refuses to install on 24H2 — downloading, reaching some percentage, then failing and rolling back — it leaves the machine exposed and the update queue stuck behind it, because later updates will not proceed until this one succeeds.

Failure patterns tell you a lot. An update that fails at the download stage points at the cache or network; one that fails during installation and rolls back points at the component store, a driver conflict, or a servicing stack problem. Error codes like 0x800f0922 (often .NET or partition space) and 0x80073712 (component store corruption) narrow it further.

The fixes below run from least to most invasive: clear the cache, fix the store, remove blockers, and finally install the package by hand. If this update has failed repeatedly across many attempts, also read the companion guide on a [cumulative update that fails every time](/articles/how-to-fix-cumulative-update-fails-every-time-in-windows-11-24h2/) for the deeper repair sequence.

## Why this happens

- **Corrupt SoftwareDistribution cache:** The downloaded package is damaged or incomplete. Windows Update verifies the payload before installing, and a bad cache fails verification every time.
- **Outdated servicing stack:** The servicing stack installs the update. If it predates what the cumulative update expects, installation fails partway and rolls back.
- **Component store corruption:** The WinSxS store tracks every system file version. Damage here makes the installer unable to stage the update, typically with error 0x80073712.
- **Driver or software conflicts:** Storage drivers, disk encryption, and some third-party antivirus products hook the same files the update touches, causing the install to abort.
- **.NET or EFI partition issues:** Error 0x800f0922 commonly traces to a full EFI/system partition or a broken .NET installation blocking the update's payload.
- **Insufficient disk space:** Cumulative updates need several gigabytes of free space for staging. The installer checks late, so the failure can appear deep into the progress bar.
- **Stuck update services:** The Windows Update, BITS, and cryptographic services can wedge in a bad state where downloads never validate and installs never start.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Note the KB number and error code

You cannot fix what you have not identified. The update history page gives you both the KB number and the error code, which decide which fix to prioritize.

1. Open Settings → Windows Update → Update history and find the failed cumulative update.
2. Write down the KB number (for example KB5034765) and the error code.
3. If the code is 0x80073712, jump to the DISM fix first. If it is 0x800f0922, check disk space and the .NET repair steps. Otherwise continue in order.

### Fix 2: Free space and clear the download cache

A surprising number of cumulative update failures are just space or a bad download. Clear both variables before doing surgery on the system.

1. Make sure C: has at least 15–20 GB free; run Disk Cleanup (cleanmgr) including system files if needed.
2. Open an elevated Command Prompt and run `net stop wuauserv` and `net stop bits`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`.
4. Run `net start wuauserv` and `net start bits`, reboot, and retry the update.

### Fix 3: Run the Windows Update troubleshooter

The troubleshooter automatically repairs the service registrations and policies that silently break cumulative update installs.

1. Go to Settings → System → Troubleshoot → Other troubleshooters → Windows Update → Run.
2. Apply all recommended fixes and reboot.
3. Retry the update. If it fails again with the same code, the problem is deeper than service configuration.

### Fix 4: Repair the component store with DISM and SFC

This is the core fix for 0x80073712 and for rollbacks late in installation. DISM restores the component store from Windows Update or a local source, and SFC repairs system files afterward.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to complete.
3. Run `sfc /scannow`, then reboot.
4. Try the update again. If DISM cannot reach its repair source, note the error — you may need the manual install in Fix 6 instead.

### Fix 5: Remove blockers: third-party antivirus and driver conflicts

Security products and outdated storage drivers are the most common third-party causes of cumulative update rollbacks on laptops.

1. Temporarily uninstall (not just disable) third-party antivirus — Windows Defender takes over automatically.
2. Update your storage and chipset drivers from the laptop manufacturer's support site.
3. Disconnect non-essential USB devices during the update.
4. Retry the installation. Reinstall your antivirus after the update succeeds.

### Fix 6: Install the update manually from the Microsoft Update Catalog

Manual installation bypasses the entire Windows Update client — cache, services, and all. If the package itself is good, this succeeds where the automatic path kept failing.

1. Visit the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for the KB number you noted.
2. Download the x64 version (most laptops), and the servicing stack update too if one is listed for your build.
3. Install the servicing stack MSU first, reboot, then install the cumulative update MSU.
4. Reboot once more and confirm the build number in Settings → System → About. Also check Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) for any known issues with that KB.

### Fix 7: Use the servicing-stack-first sequence for stubborn cases

Some 24H2 cumulative updates will not install until a specific servicing stack update is in place. When the automatic path keeps failing at the same percentage, the stack is the likely culprit.

1. Check your current servicing stack version in the update history — failed SSU entries show there too.
2. Download the latest SSU for 24H2 from the Catalog and install it manually.
3. Reboot, then install the cumulative update manually as in Fix 6.
4. If even this fails, the in-place upgrade repair described in the [servicing stack failure guide](/articles/how-to-fix-servicing-stack-update-failed-after-windows-11-update/) is the next step before considering a reset.

## Closing

A cumulative update that will not install is usually a cache, store, or servicing-stack problem — not a broken Windows. Clear the cache, repair the store with DISM, remove third-party blockers, and install the package manually from the Catalog when the automatic path keeps failing. One of these steps resolves the vast majority of cases without a reset.
