---
title: "Stop GamingServices From Eating CPU on Your ASUS Laptop"
slug: how-to-fix-gamingservices-high-cpu-usage-on-asus-laptop
date: 2026-10-10
categories: ["performance"]
tags: ["gamingservices.exe high cpu", "asus laptop", "xbox game bar", "windows 11 gaming", "cpu usage fix"]
description: "GamingServices.exe spiking CPU on your ASUS laptop even when you're not gaming? Reset the Xbox services, fix stuck updates, and reclaim your processor."
thumbnail: "/images/thumbs/how-to-fix-gamingservices-high-cpu-usage-on-asus-laptop.webp"
faqs:
  - q: "What is GamingServices.exe and why is it using CPU?"
    a: "GamingServices.exe is the Windows service behind the Xbox app, Game Bar, and Microsoft Store games. It uses CPU when installing or updating games, syncing cloud saves, or when its update pipeline gets stuck in a retry loop — which is the most common cause of constant high usage."
  - q: "Can I disable GamingServices.exe safely?"
    a: "You can stop the service, but the Xbox app and Microsoft Store games need it to install, update, and launch. Better to repair it than disable it. If you never use Xbox features, disabling the related startup entries is the cleaner option."
  - q: "Why does GamingServices use CPU when I'm not gaming?"
    a: "Because it never fully sleeps. The service performs background catalog checks, cloud-save syncs, and update scans on its own schedule. Normally that costs almost nothing — but when an update job fails and retries forever, that background work becomes a constant CPU drain. Clearing the stuck download queue usually returns it to near-zero."
  - q: "Will reinstalling the Xbox app fix GamingServices CPU usage?"
    a: "In most stubborn cases, yes. The Xbox app and Gaming Services share state, and a corrupted install of either keeps the service churning. Remove Gaming Services via PowerShell, restart, then reinstall the Xbox app from the Microsoft Store — this pulls a clean copy of both. Your game library and saves are tied to your account, not the local install."
---

GamingServices.exe is supposed to be invisible — a quiet background service that keeps your Xbox app and Microsoft Store games updated. But on many ASUS laptops it becomes the opposite of invisible, chewing through 20 to 50 percent CPU around the clock, keeping fans spinning and battery draining while you do nothing remotely game-related.

The usual trigger is a stuck update pipeline. Gaming Services downloads game updates and store catalog data in the background, and when one of those jobs fails partway, the service retries forever instead of giving up gracefully. ASUS's gaming-focused software stack — Armoury Crate, background game services — can make the symptom more visible, but the root cause is almost always in the service itself.

Here is how to confirm Gaming Services is the problem, unstick it, and keep it quiet going forward.

## Why this happens

- **Stuck game or store update:** A failed download retries in an endless loop, keeping the service permanently busy.

- **Corrupted Gaming Services installation:** Partial updates leave the service in a half-installed state that burns CPU doing nothing useful.

- **Xbox app constantly syncing:** Cloud save sync or catalog refreshes firing too often, sometimes triggered by a corrupted local cache.

- **Gaming features running at startup:** Game Bar, Game Mode helpers, and Xbox startup entries add background load on every boot.

- **Microsoft Store update loop:** The Store itself stuck checking for updates drags Gaming Services along with it.

- **Conflicting ASUS background services:** Armoury Crate's game-detection hooks occasionally interact badly with Xbox services after updates.

- **Corrupted system files:** Damaged Windows components underneath the gaming stack prevent the service from completing its tasks. Similar stuck-service behavior shows up elsewhere — see [GamingServices high CPU after the Windows 11 update](/articles/how-to-fix-gamingservices-high-cpu-usage-after-windows-11-update/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm GamingServices is the hog

Multiple Xbox-related processes exist, and fixing the wrong one wastes time. Identify the exact process first.

1. Open Task Manager with Ctrl plus Shift plus Esc and sort by CPU.
2. Look for GamingServices.exe — and also GamingServicesNet.exe — and note their usage.
3. Right-click the process and choose Go to details to confirm the executable name.
4. Check whether the Xbox app shows a stuck download or update on its library page.
5. If CPU is high with no visible download, the service is stuck — continue below.

### Fix 2: Reset the Xbox app and Gaming Services

A reset clears the corrupted local cache that usually causes the retry loop, without removing your games or saves.

1. Open Settings, Apps, Installed apps.
2. Find Xbox, click the three dots, choose Advanced options.
3. Click Repair first, wait for the checkmark, and test for a few minutes.
4. If CPU is still high, return and click Reset — this clears local app data but keeps your library.
5. Do the same Repair/Reset sequence for the Microsoft Store app.
6. Restart the laptop and monitor the service in Task Manager.

### Fix 3: Reinstall Gaming Services via PowerShell

When reset is not enough, a full removal and reinstall replaces the corrupted service binaries entirely. This is the fix that works most often for stubborn cases.

1. Open PowerShell as administrator.
2. Run `get-appxpackage Microsoft.GamingServices | remove-appxpackage -allusers` to remove the service.
3. Restart the laptop.
4. Open the Microsoft Store, search for the Xbox app, and install it — this pulls a fresh Gaming Services with it.
5. Alternatively run `start ms-windows-store://pdp/?productid=9MWPM2CQNLHN` in PowerShell to open the Gaming Services store page directly.
6. After installation, restart once more and verify CPU usage is back to near zero at idle.

### Fix 4: Stop the endless update retry

If a specific game update is the loop trigger, clearing the Store's pending downloads stops the service from churning.

1. Open the Microsoft Store and go to Library.
2. Cancel or pause any stuck or repeatedly failing downloads.
3. Open Settings, Apps, Installed apps, find the game with the stuck update, and repair it via Advanced options.
4. Check your disk space — updates fail and retry when the drive is nearly full.
5. In the Store settings, turn off automatic app updates temporarily to test.
6. Re-enable automatic updates after confirming the service has calmed down.

### Fix 5: Trim gaming startup entries

Xbox and Game Bar components launching at every boot add background load and re-trigger the service. If you rarely game on this machine, trimming them helps a lot.

1. Open Task Manager and go to the Startup apps tab.
2. Disable Xbox Game Bar, Xbox app, and any game launchers you do not use daily.
3. Open Settings, Gaming, Xbox Game Bar, and turn it off if you never use it.
4. In Armoury Crate, check for game-detection or overlay features you do not need and disable them.
5. Restart and confirm fewer gaming processes appear in Task Manager.
6. For general startup cleanup, see [how to disable startup programs in Windows 11](/articles/how-to-disable-startup-programs-windows-11/).

### Fix 6: Repair Windows system files underneath

Gaming Services depends on core Windows components. If SFC finds corruption, the service may never have been the real problem.

1. Open Command Prompt as administrator.
2. Run `sfc /scannow` and wait for it to complete.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store.
4. Restart the laptop after both complete.
5. Check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for known Gaming Services issues after recent updates.
6. Re-test idle CPU usage over 15 minutes.

## Closing

GamingServices.exe should sip CPU, not chug it. In nearly every case the culprit is a stuck update or corrupted service state, and the reset-to-reinstall ladder above clears it. Once idle usage is back near zero, keep an eye on the Xbox app's download queue — that is where the next loop will start if it ever comes back.
