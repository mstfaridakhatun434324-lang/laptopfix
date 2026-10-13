---
title: "How to Fix Windows Update Error 0x800704C7 on Windows 11 24H2"
slug: "how-to-fix-windows-update-error-0x800704c7-in-windows-11-24h2"
date: 2026-09-13
categories: ["windows-update"]
tags: ["0x800704c7", "windows update error", "windows 11 24h2", "update cancelled", "windows update"]
description: "Error 0x800704C7 on Windows 11 24H2 means the update operation was cancelled mid-process. Learn what cancels it — antivirus, broken services, user interruption — and how to get the update through."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800704c7-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x800704C7 mean in Windows Update?"
    a: "Error 0x800704C7 is the system code ERROR_CANCELLED: the operation was cancelled by the user or by another process. In Windows Update it typically means the install was interrupted — by a third-party antivirus killing the installer, a crashed update service, a forced shutdown during installation, or occasionally the user clicking cancel on a long-running update. Windows rolls back and reports the cancellation as this error."
  - q: "Why does 0x800704C7 keep happening on the same update?"
    a: "Recurrence usually points to something on your system that cancels the install every time it runs. The classic culprits are third-party antivirus software terminating the update process, a corrupted update service that dies mid-install, or a pending system state (like a half-applied previous update) that forces every new attempt to abort. A clean boot isolates the interfering software, and resetting the update components clears the stuck state."
  - q: "Is error 0x800704C7 caused by Microsoft's servers?"
    a: "Rarely. This code describes a local cancellation, not a download or server failure — the update reached your PC and something on the PC stopped it. Server-side problems produce different codes (usually 0x80072xxx network errors). If 0x800704C7 appears, focus your troubleshooting on local software conflicts, services, and system file health rather than your internet connection."
  - q: "Can I just ignore error 0x800704C7?"
    a: "You should not. The cancelled update is a security or cumulative update your system still needs, and Windows will keep retrying it — consuming bandwidth and forcing the 'undoing changes' rollback loop at shutdown. Fixing the underlying cancellation is faster than living with repeated attempts, and our guide to [updates that fail with 'we couldn't complete the updates'](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-windows-11/) covers the rollback side."
---
Error 0x800704C7 is Windows telling you, in its own terse way, that the update was cancelled. Not failed to download, not blocked by the server — cancelled, mid-operation, on your own machine. On Windows 11 24H2 this most often happens when a third-party antivirus terminates the installer, when an update service crashes partway through, or when the machine is shut down or put to sleep during a long install.

The tricky part is that the cancellation is usually silent. You see the update progress bar, walk away, and come back to the error — with no obvious sign of what pulled the plug. Because the cause is an interruption rather than corruption, the standard 'clear the cache' advice only helps if the interruption left the update state inconsistent. The real fix is finding and removing whatever keeps cancelling the operation.

The sequence below starts with the quick checks and moves to isolating the interfering software. Most 0x800704C7 cases are solved by Fix 3 or Fix 4. If the update instead completes but then rolls back at restart, see our walkthrough for [undoing-changes loops in Windows 11 24H2](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-in-windows-11-24h2/).

## Why this happens

- **Third-party antivirus terminating the installer** — Security suites with aggressive behavior monitoring sometimes kill the trusted installer process or quarantine update payloads mid-install, which Windows reports as a cancellation.

- **Windows Update services crashing** — If wuauserv, BITS, or the cryptographic service dies during the install phase — often due to corrupted service state — the operation aborts with 0x800704C7.

- **Shutdown or sleep during installation** — Closing the lid or forcing a power-off while the update is in its install phase cancels it. Laptops with aggressive sleep timers are especially prone to this.

- **Corrupted pending update state** — A half-applied previous update leaves the servicing stack in a 'reboot pending' limbo. Every new update attempt detects the inconsistent state and cancels itself.

- **Conflicting background software** — System utilities, driver updaters, and 'PC cleaner' tools that hook into system processes can interfere with the installer and trigger a cancellation.

- **Insufficient disk space at install time** — The download fits, but the extraction and staging phase needs several extra gigabytes. If space runs out mid-install, the operation cancels rather than failing cleanly.

- **Corrupted user profile permissions** — The installer runs with system privileges, but damaged ACLs on key folders can cause access-denied cancellations that surface as 0x800704C7.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Free up disk space before retrying

Rule out the simplest cancellation trigger first. The install phase needs breathing room beyond the download size — aim for at least 20 GB free on the system drive.

1. Open **Settings > System > Storage** and check free space on C:.
2. Run **Storage Sense** and **Cleanup recommendations** to clear temp files, old downloads, and the Recycle Bin.
3. Move large personal files off the system drive if you are under 20 GB free.
4. Retry the update from **Settings > Windows Update**.

### Fix 2: Run the Windows Update troubleshooter

The troubleshooter resets the update service state and clears the cancelled-operation flags. It is a quick first pass before manual service work.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update** and apply any recommended fixes.
3. Restart the laptop when it finishes.
4. Check for updates again and let the previously cancelled update retry.

### Fix 3: Perform a clean boot to isolate the interfering program

A clean boot starts Windows with only Microsoft services, which exposes whether third-party software is cancelling the install. This is the highest-yield diagnostic for 0x800704C7.

1. Press **Win + R**, type `msconfig`, and open the **Services** tab.
2. Check **Hide all Microsoft services**, then click **Disable all**.
3. Open the **Startup** tab, click **Open Task Manager**, and disable all startup items.
4. Restart, run Windows Update, and if it succeeds, re-enable services in halves to find the culprit — usually an antivirus or system utility.

### Fix 4: Reset the Windows Update components

Crashed or corrupted update services are a direct cause of mid-install cancellations. Stopping them, clearing their state folders, and restarting gives you a known-good baseline.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, and `net stop msiserver`.
3. Rename the state folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart all four services with `net start`, then check for updates. If the troubleshooter itself misbehaves, see our guide to [fixing a broken Windows Update troubleshooter](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/).

### Fix 5: Temporarily remove third-party antivirus

If the clean boot pointed at your security suite, do not just disable it — fully uninstall it for the test. Many suites leave filter drivers active even when 'disabled,' and those drivers are what kill the installer.

1. Open **Settings > Apps > Installed apps** and uninstall the third-party antivirus (Windows Defender activates automatically).
2. Restart the laptop to clear any loaded filter drivers.
3. Run Windows Update to completion.
4. Reinstall your antivirus afterward if you prefer it — or stay with Defender, which never conflicts with updates.

### Fix 6: Repair system files with SFC and DISM

A damaged servicing stack cancels installs unpredictably. These two tools repair the files the installer depends on.

1. Open an elevated Command Prompt and run `sfc /scannow`.
2. When it finishes, run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart the laptop after both complete.
4. Retry the update. Microsoft documents both utilities in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Install the update manually from the Microsoft Update Catalog

If the automatic installer keeps getting cancelled, the standalone installer often sails through — it runs as a single process with fewer moving parts for background software to interfere with.

1. Find the failing **KB number** in **Settings > Windows Update > Update history**.
2. Search for it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and download the x64 package.
3. Close all programs, then run the .msu file and do not touch the laptop until it finishes.
4. Restart when prompted and confirm the KB appears in update history.

## Closing

Error 0x800704C7 is almost always something on your PC pulling the plug on the installer — usually security software or a crashed update service. Isolate it with a clean boot, reset the components, and the update will finally get the uninterrupted run it needs.
