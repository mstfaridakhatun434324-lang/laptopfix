---
title: "How to Fix Error 0x80070002 on Windows 10"
slug: how-to-fix-error-0x80070002-on-windows-10
date: 2026-09-24
categories: ["windows-errors"]
tags: ["error-0x80070002", "windows-10", "windows-update"]
description: "Error 0x80070002 blocking Windows 10 updates? Clear the corrupted cache and repair update components with these steps."
thumbnail: "/images/thumbs/how-to-fix-error-0x80070002-on-windows-10.webp"
faqs:
  - q: "What does error 0x80070002 mean?"
    a: "It means 'the system cannot find the file specified.' In Windows Update it almost always points to corrupted or missing files in the update download cache. During upgrades or backups it can also mean a referenced file was deleted or moved."
  - q: "Why does Windows Update keep failing with 0x80070002?"
    a: "Because the SoftwareDistribution cache — where Windows stores downloaded updates — contains damaged files. Windows keeps retrying with the same broken cache. Deleting the cache contents forces a fresh download, which fixes it in most cases."
  - q: "Will resetting Windows Update delete my files?"
    a: "No. Resetting update components only clears downloaded update files and the update history. Your documents, apps, and settings are completely untouched."
  - q: "The error appears during backup, not updates. Same fix?"
    a: "Not exactly. For backup errors, 0x80070002 usually means a library location points to a missing folder. Check that every folder in your backup set still exists, and remove or re-add any that were moved or deleted."
---
# How to Fix Error 0x80070002 on Windows 10

**Error 0x80070002** — "the system cannot find the file specified" — is the classic Windows Update failure on Windows 10. Updates download, then fail, then fail again on every retry. The loop is maddening, but the cause is mundane: the update cache is corrupted, and Windows keeps choking on the same damaged files.

The core fix takes about five minutes: stop the update services, clear the cache, and let Windows download fresh copies. The same code also appears during system upgrades and File History backups when a referenced file has gone missing — the fixes below cover those cases too, so check which situation matches yours before diving in.

If your update failures show a different code, check our [error 0x80070057 fix](/articles/error-code-0x80070057-fix/) for the parameter-is-incorrect variant.

## Why this happens

- **Corrupted SoftwareDistribution cache:** Interrupted downloads or disk hiccups leave half-written update files that fail validation.
- **Damaged catroot2 signature catalog:** Windows can't verify update signatures, so installs abort.
- **Broken update components:** The Background Intelligent Transfer Service or Windows Update service itself is stuck or misconfigured.
- **Missing files referenced by backup:** In backup scenarios, a library pointing to a deleted folder triggers the same code.
- **Antivirus quarantining update files:** Overzealous scanning can remove files Windows Update just downloaded.
- **Failing hard drive:** Bad sectors corrupting cached files produce recurring, seemingly random update failures.

## How to fix it

Work through these in order. Fix 1 resolves the overwhelming majority of cases.

### Fix 1: Delete the SoftwareDistribution cache

This is the definitive fix — you're simply throwing away the damaged downloads so Windows fetches clean copies.

1. Open an **admin Command Prompt** (right-click **Start > Command Prompt (Admin)** or **Windows PowerShell (Admin)**).
2. Stop the update services:
   `net stop wuauserv`
   `net stop bits`
3. Open File Explorer and navigate to `C:\Windows\SoftwareDistribution`.
4. Select everything inside (**Ctrl + A**) and delete it. If a file refuses, make sure both services are stopped and retry.
5. Restart the services:
   `net start wuauserv`
   `net start bits`
6. Go to **Settings > Update & Security > Windows Update** and click **Check for updates**. The update will download fresh and should install cleanly this time around.

### Fix 2: Reset all Windows Update components

When the cache clear isn't enough, reset the entire update machinery.

1. In an admin Command Prompt, run:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
2. Rename the two cache folders:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
3. Re-register the update DLLs:
   `regsvr32.exe /s wuapi.dll`
   `regsvr32.exe /s wuaueng.dll`
   `regsvr32.exe /s wups.dll`
4. Restart all four services with `net start` commands matching step 1.
5. Check for updates again.
6. If the troubleshooter's automated fixes keep failing on the same component, note which one — that tells you where the manual reset in Fix 2 needs extra attention, usually BITS or the cryptographic service.

### Fix 3: Run the Windows Update troubleshooter

The built-in troubleshooter catches configuration issues the manual reset misses.

1. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
2. Select **Windows Update** and click **Run the troubleshooter**.
3. Apply every fix it recommends, then restart.
4. If the troubleshooter itself reports it couldn't identify the problem, continue to Fix 4 — the troubleshooter is helpful but not exhaustive.

### Fix 4: Repair system files with SFC and DISM

Corrupted servicing-stack files make every update fail regardless of cache state.

1. Open an admin Command Prompt.
2. Run `sfc /scannow` and wait for it to complete.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and try the update once more. Microsoft documents these repair tools on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 5: Check the drive for errors

If 0x80070002 keeps coming back after cache clears, the disk itself may be corrupting downloads.

1. Open an admin Command Prompt and run `chkdsk C: /f`.
2. Press **Y** to schedule the check and restart.
3. Let the scan finish completely — don't interrupt it.
4. After reboot, clear the SoftwareDistribution cache once more (Fix 1) so you're not retrying with files damaged by the disk errors, then update.
5. If chkdsk finds many bad sectors, back up your data promptly — the drive is failing.

### Fix 6: Install the update manually from the Catalog

Sometimes the automatic pipeline is broken but the update itself is fine.

1. Find the KB number in **Settings > Update & Security > Windows Update > View update history**.
2. Search for it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and download the version matching your system (x64 for most laptops).
3. Run the downloaded `.msu` file and follow the prompts.
4. If manual install works, the problem was purely in the automatic download pipeline — often a proxy or BITS issue worth investigating later.

### Fix 7: Perform an in-place upgrade repair

For stubborn cases where nothing else sticks, reinstalling Windows over itself fixes the servicing stack while keeping everything.

1. Back up important files first — this is safe, but backups are never a bad idea.
2. Download the Windows 10 Media Creation Tool from Microsoft and create installation media, or mount a Windows 10 ISO.
3. Run `setup.exe` and choose **Keep personal files and apps**.
4. Let the upgrade complete; it takes 30–90 minutes.
5. Afterward, Windows Update should work normally. For broader blue-screen troubleshooting on the same machine, see our [blue screen of death fix guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

## Closing

Error 0x80070002 is almost always a corrupted update cache, and deleting the SoftwareDistribution folder fixes it in minutes. When that isn't enough, resetting the update components, repairing system files, and checking the disk cover the remaining causes. It's a boring error with a boring fix — which is good news, because boring fixes are reliable ones, and your updates will be installing cleanly again today without further trouble at all.
