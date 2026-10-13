---
title: "GamingServices Eating Your CPU? Stop the Spikes"
slug: how-to-fix-gamingservices-high-cpu-usage-youtube
date: 2026-09-14
categories: ["performance"]
tags: ["gamingservices", "high cpu", "xbox game bar", "windows 11", "gaming"]
description: "GamingServices.exe spiking CPU even when you're not gaming? Repair the Xbox services, stop the update loop, and reclaim your processor."
thumbnail: "/images/thumbs/how-to-fix-gamingservices-high-cpu-usage-youtube.webp"
faqs:
  - q: "What is GamingServices.exe and why is it running when I'm not gaming?"
    a: "GamingServices is Microsoft's background service for Xbox features on Windows — it handles game installs, updates, licensing checks, and Game Bar integration. It runs at startup by default on Windows 10 and 11 whether or not you game, because it's tied to the Microsoft Store infrastructure. When it's healthy it idles near zero CPU; sustained high usage almost always means it's stuck in a failed update, license verification, or install loop."
  - q: "Is it safe to disable GamingServices?"
    a: "Disabling it outright can break the Xbox app, PC Game Pass titles, and Microsoft Store game installs, since they depend on the service for licensing. A better approach is to fix the underlying stuck state first — repairing or reinstalling the service usually drops CPU to zero while keeping everything functional. Only consider disabling it if you never use Xbox or Store games at all, and even then, setting it to manual is safer than disabling."
  - q: "Why does GamingServices spike after Windows updates?"
    a: "Feature updates frequently reset or partially corrupt the Gaming Services package, leaving it in a state where it retries a failed operation endlessly — checking for game updates against a broken package manifest, for example. The Store and Xbox app may also queue pending updates that GamingServices tries to process with mismatched components. Repairing the Gaming Services app package and letting the Store finish its updates typically resolves post-update spikes within a day."
  - q: "Will reinstalling GamingServices delete my installed games?"
    a: "No. Reinstalling the Gaming Services package only replaces the service components themselves — your installed games, save files, and Xbox app data live elsewhere and are untouched. At most, the Xbox app may ask you to verify game files on next launch, which is a quick integrity check, not a redownload. Your Game Pass subscription and entitlements are tied to your Microsoft account, not to the local service installation."
---

You're not gaming. Nothing is downloading. Yet Task Manager shows `GamingServices.exe` — or its sibling `GamingServicesNet.exe` — chewing through 20%, 40%, sometimes 70% of your CPU, your fans are roaring, and your laptop feels like it's rendering 3D graphics while sitting on the desktop. This is one of the more annoying Windows quirks because the process responsible is something you probably never asked for.

GamingServices is Microsoft's plumbing for Xbox-on-Windows: game installs, updates, license checks, Game Bar hooks. It's installed by default and starts with Windows, gamer or not. When it works, it's invisible. When it breaks — usually after a Windows update corrupts its package or a Store update gets stuck — it falls into a retry loop, hammering your CPU indefinitely. The fix is to unstick it, not to nuke it.

Quick check first: open the **Microsoft Store** > **Library** and the **Xbox app** and look for stuck or pending updates — a queued game update that can't complete is the most common trigger. For the broader Xbox-services picture, our [GamingServices on Windows 11 guide](/articles/how-to-fix-gamingservices-high-cpu-usage-on-windows-11/) covers variant scenarios, and if the spikes followed a recent update, the [post-update GamingServices fix](/articles/how-to-fix-gamingservices-high-cpu-usage-after-windows-11-update/) is worth reading.

## Why this happens

- **Stuck Store/Xbox update loop**: A game or services update that fails and retries forever, burning CPU each cycle.
- **Corrupted Gaming Services package**: Windows updates frequently damage the package manifest, leaving the service in a broken retry state.
- **License verification churn**: The service re-checking entitlements against a broken local cache, over and over.
- **GamingServicesNet network retries**: Failed license or content server calls retried aggressively with no backoff.
- **Game Bar hooks on non-game apps**: Game Bar trying to attach to apps that resist it, keeping the service active.
- **Multiple Xbox identities**: Signed-in account mismatches between Store and Xbox app causing auth retry loops.
- **Corrupt Microsoft Store cache**: The Store's cache corruption cascades into every service that depends on it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear the stuck updates first

The simplest cause is the most common — finish what it's chewing on.

1. Open the **Microsoft Store** > **Library** and check for pending updates. Let any Gaming Services, Xbox, or game updates complete; don't interrupt them.
2. Open the **Xbox app** and check its update queue too — pending game updates there also drive the service.
3. If an update is visibly stuck (0% for a long time), pause it, wait a minute, and resume — this often unsticks the queue.
4. After updates finish, watch Task Manager for 10 minutes. A healthy GamingServices should settle below 1% CPU when idle.
5. If there's nothing pending and CPU is still high, move on — the package itself is likely corrupt.

### Fix 2: Repair the Gaming Services app package

Use Windows' built-in repair before reaching for PowerShell.

1. Go to **Settings** > **Apps** > **Installed apps** and search for **Gaming Services**.
2. Click the **...** menu > **Advanced options**, then click **Repair** — wait for it to finish, then check Task Manager.
3. If Repair doesn't help, click **Reset** in the same panel (this clears its local data but not your games).
4. Also repair the **Xbox** app and **Microsoft Store** the same way — they share infrastructure, and one broken piece keeps the others churning.
5. Reboot after resetting and observe CPU for 15 minutes before concluding.

### Fix 3: Reinstall GamingServices via PowerShell

When repair fails, a clean reinstall of the service package fixes corrupt manifests.

1. Open **PowerShell as administrator**.
2. Remove the package: `Get-AppxPackage *gamingservices* -AllUsers | Remove-AppxPackage -AllUsers`
3. Also remove its provisioned package so it reinstalls cleanly: `Get-AppxProvisionedPackage -Online | Where-Object {$_.PackageName -like "*gamingservices*"} | Remove-AppxProvisionedPackage -Online`
4. Reboot. Windows will reinstall Gaming Services automatically — or trigger it by opening the Xbox app, which prompts for the install.
5. Verify in Task Manager that the fresh service idles near 0% CPU. Your games and saves are untouched by this.

### Fix 4: Reset the Microsoft Store cache

Store cache corruption cascades into GamingServices.

1. Press **Win+R**, type `wsreset.exe`, and press Enter — a blank Store window opens and closes when the cache clear completes.
2. After it finishes, open the Store, go to **Library**, and click **Get updates** to let everything refresh cleanly.
3. Sign out of the Store (profile icon > Sign out) and sign back in — this refreshes the entitlement tokens GamingServices keeps re-checking.
4. Do the same sign-out/sign-in in the **Xbox app** to align the two identities.
5. Monitor CPU for 15 minutes; auth-loop spikes usually vanish after the tokens refresh.

### Fix 5: Disable Game Bar hooks you don't need

Game Bar integration keeps GamingServices engaged with apps it shouldn't touch.

1. Go to **Settings** > **Gaming** > **Xbox Game Bar** and turn it **Off** if you never record or use widgets.
2. In **Settings** > **Gaming** > **Game Mode**, leave Game Mode on (it's harmless) but review **Captures** — turn off **Record in the background while I'm playing a game** if enabled.
3. Check **Settings** > **Apps** > **Installed apps** > **Xbox Game Bar** > **Advanced options** and set **Background apps permissions** to **Never** if you don't use it.
4. For per-app control, use **Settings** > **System** > **Display** > **Graphics**, select an app, and check its GPU preference — forcing the right GPU reduces compositor confusion that keeps services polling.
5. Retest with your usual apps open; overlay-related CPU churn should be gone.

### Fix 6: Set the services to Manual if you don't game

For non-gamers, the cleanest long-term fix is stopping the auto-start.

1. Open `services.msc` and find **Gaming Services** and **GamingServicesNet** (there may be two entries).
2. Double-click each, set **Startup type** to **Manual** (not Disabled — Manual lets the Xbox app start them on demand if you ever need them).
3. Stop both services now from the same dialog.
4. If you use PC Game Pass occasionally, leave them on Manual — launching the Xbox app will start them, and they'll idle properly when healthy.
5. Only choose **Disabled** if you are certain you'll never use Xbox or Store games; note that re-enabling later requires revisiting this dialog.

### Fix 7: Repair Windows' app infrastructure

When the whole Store/Xbox stack is sick, treat the foundation.

1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated Command Prompt — corrupt system files break app packages silently.
2. Check **Settings** > **Windows Update** for pending updates; Microsoft periodically ships Gaming Services fixes inside cumulative updates. Individual updates are also on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update stalls.
3. Re-register all built-in app packages: in elevated PowerShell, run `Get-AppxPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}` — this takes several minutes and re-registers every inbox app cleanly.
4. If problems persist, create a fresh local user account and test there — a healthy new profile points to corruption in your main profile's app data.
5. As a last resort, **Settings** > **System** > **Recovery** > **Reset this PC** (keep files) rebuilds the entire app platform.

## Closing

GamingServices high CPU is almost always a stuck update or a corrupted package, not a design flaw — fix the stuck state and it goes back to being invisible. Repair the package, clear the Store cache, and align your sign-ins; if you're not a gamer at all, Manual startup keeps it out of your way permanently. Either way, your CPU belongs to you again.
