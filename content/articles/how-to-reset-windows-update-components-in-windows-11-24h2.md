---
title: "How to Reset Windows Update Components in Windows 11 24H2"
slug: how-to-reset-windows-update-components-in-windows-11-24h2
date: 2026-10-11
categories: ["windows-update"]
tags: ["reset windows update components", "windows 11 24h2", "softwaredistribution", "wuaueng"]
description: "Windows Update broken on 24H2? Reset its components step by step: stop services, clear the update cache, re-register DLLs, and start fresh."
thumbnail: "/images/thumbs/how-to-reset-windows-update-components-in-windows-11-24h2.webp"
faqs:
  - q: "What does resetting Windows Update components actually do?"
    a: "It stops the update-related services, clears the SoftwareDistribution and catroot2 caches where downloaded updates and certificates live, re-registers the DLLs those services depend on, and restarts everything clean. This removes the corrupted state that causes most persistent update failures without touching your files, settings, or installed programs."
  - q: "Will resetting Windows Update delete my installed updates?"
    a: "No. Installed updates remain installed and your update history is untouched. The reset only clears temporary download caches and the pending-download queue. If an update was half-downloaded, it simply downloads again from scratch after the reset, which is usually what you want when the cache was the problem."
  - q: "Is it safe to delete the SoftwareDistribution folder?"
    a: "Yes, as long as the Windows Update service is stopped first. SoftwareDistribution holds only temporary files: downloads, the download database, and event history. Windows recreates it automatically the next time it checks for updates. Never delete it while the update service is running, or files may be locked and the folder will rebuild in a corrupted state."
  - q: "What if the reset doesn't fix my update error?"
    a: "Then the problem is likely deeper than the update components: corrupted system files, a failing disk, or an update that is genuinely incompatible with your hardware. Run DISM and SFC repairs, check your drive health, or install the failing update manually from the Microsoft Update Catalog as the next step."
---

Resetting the Windows Update components is the single most reliable fix for update problems that survive every other attempt. When updates fail repeatedly with different errors, hang during download, or the Windows Update page itself behaves strangely, the cause is usually corruption inside the update machinery itself — the services, caches, and registration data that Windows Update depends on. Rebuilding that machinery from scratch clears years of accumulated damage in about ten minutes.

On Windows 11 24H2 this procedure is exactly the same as on earlier builds, but it is worth doing cleanly rather than running a random script from the internet. The manual method below stops the right services in the right order, clears the right caches, and re-registers the components — and you will know exactly what changed on your system if anything goes wrong.

It is worth understanding what you are not doing here: this reset does not reinstall Windows, does not touch your programs, and does not delete a single personal file. It only rebuilds the plumbing Windows Update drinks through. Technicians reach for it precisely because it is high-impact and low-risk — the closest thing update repair has to a free lunch. The ten minutes it takes are almost always cheaper than another round of blind retries, and unlike random scripts from the internet, every step below is transparent and reversible.

## Why this happens

- **Corrupted SoftwareDistribution cache.** Interrupted downloads and crashes leave partial files and a damaged download database that the service cannot recover from.
- **Damaged catroot2 catalog data.** The cryptographic catalog store can corrupt, breaking signature verification for every subsequent update.
- **Update services stuck in a bad state.** BITS, Windows Update, and the cryptographic services can deadlock or lose their configuration after a failed install.
- **Unregistered or mismatched DLLs.** Component registrations can break during failed updates or aggressive registry cleaning.
- **Stuck pending-download queue.** A poisoned entry in the queue blocks everything behind it, and ordinary retries never clear it.
- **Leftover state from a rolled-back feature update.** The 24H2 upgrade can leave component state that confuses the servicing stack.
- **Third-party interference.** Antivirus, firewalls, or system optimizers can modify component state in ways that accumulate over time.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the built-in troubleshooter first

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply any recommended fixes.
3. Restart the laptop, then check for updates once more.
4. If updates still fail the same way, the automated reset was not enough — continue to the manual reset below. The official [Windows Update support page](https://support.microsoft.com/en-us/windows) also documents this escalation path.

### Fix 2: Open an elevated Command Prompt

1. Press the **Windows key**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Click **Yes** on the User Account Control prompt.
3. Keep this window open for the entire procedure — every command below runs here.
4. Do not close it between steps; the services must stay stopped while you clear the caches.

### Fix 3: Stop the update-related services

1. Run these four commands one at a time, pressing Enter after each:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
2. If a service says it is not started, that is fine — move on to the next one.
3. If a service refuses to stop, note its name; you will handle it in the next fix with a stronger stop command.
4. Verify all four are stopped before touching any folders.

### Fix 4: Rename the SoftwareDistribution and catroot2 folders

1. In the same elevated Command Prompt, run:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
2. Renaming instead of deleting keeps a backup — if something unexpected happens, you can rename them back.
3. Do not touch the plain `catroot` folder (without the 2); only `catroot2` is safe to reset.
4. If either rename fails with "access denied," a service is still running — re-run the stop commands, adding `net stop dosvc` as well, then retry. More on cache fixes: [stuck downloads guide](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/).

### Fix 5: Re-register the update DLLs

1. Still in the elevated prompt, run each of these commands:
   `regsvr32.exe /s atl.dll`
   `regsvr32.exe /s urlmon.dll`
   `regsvr32.exe /s mshtml.dll`
   `regsvr32.exe /s shdocvw.dll`
   `regsvr32.exe /s browseui.dll`
   `regsvr32.exe /s jscript.dll`
   `regsvr32.exe /s vbscript.dll`
   `regsvr32.exe /s scrrun.dll`
   `regsvr32.exe /s msxml.dll`
   `regsvr32.exe /s msxml3.dll`
   `regsvr32.exe /s wuapi.dll`
   `regsvr32.exe /s wuaueng.dll`
2. The `/s` flag keeps each registration silent; a missing dialog means success.
3. If one fails, note it and continue — one failed registration rarely blocks the whole repair.
4. These registrations restore the component entries that failed updates sometimes damage.

### Fix 6: Restart the services and reset the network stack for updates

1. Restart the services you stopped earlier:
   `net start wuauserv`
   `net start cryptSvc`
   `net start bits`
   `net start msiserver`
2. Optionally reset the Winsock catalog, which updates use for connections:
   `netsh winsock reset`
3. Restart the laptop so everything comes up in a clean state.
4. After reboot, open **Settings** > **Windows Update** and click **Check for updates** — the first check rebuilds the caches and may take several minutes.

### Fix 7: Verify the reset worked

1. After the first successful check for updates, open **Settings** > **Windows Update** > **Update history** and confirm new updates are being offered.
2. Install one small update (a Defender definition update is ideal) to prove the pipeline works end to end.
3. If the small update installs cleanly, let the larger pending updates follow.
4. If failures return immediately with a specific error code, look up that code next — the reset did its job and the real problem is narrower. See also [fixing monthly cumulative update failures](/articles/how-to-fix-monthly-cumulative-update-failed-on-windows-11/).

### Fix 8: Clear the BITS queue and Delivery Optimization cache

Two related caches sometimes survive a component reset and keep poisoning downloads: the BITS job queue and the Delivery Optimization peer cache.

1. In an elevated Command Prompt, run `net stop bits` and `net stop dosvc`.
2. Delete all `qmgr*.dat` files in `C:\ProgramData\Microsoft\Network\Downloader` — these are stuck BITS jobs.
3. Open **Disk Cleanup** on C:, check **Delivery Optimization Files**, and clean them.
4. Restart both services with `net start`, reboot, and check for updates. This clears the last hiding spots for corrupted transfer state.

## Closing

Resetting the Windows Update components is the deep-clean option: it clears every piece of temporary state the update engine keeps, which is why it resolves failures that survive troubleshooters and retries. Do it manually as shown here so you know exactly what changed, verify with a small update first, and keep the `.old` folders for a few days before deleting them. If updates still fail after the full reset plus the BITS cleanup, the problem has escaped the update subsystem — run the DISM and SFC repairs, check the drive with chkdsk, and consider a manual install of the specific failing KB. But in practice, very few failures survive this complete a rebuild.
