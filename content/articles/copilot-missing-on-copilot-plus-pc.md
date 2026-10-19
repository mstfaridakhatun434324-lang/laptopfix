---
title: "Copilot Missing on Your Copilot+ PC? How to Get It Back"
slug: copilot-missing-on-copilot-plus-pc
date: 2026-10-19
categories: ["ai-pc"]
tags: ["copilot", "copilot plus pc", "missing app", "windows 11", "ai pc"]
description: "Copilot missing on your Copilot+ PC? Find out why the app vanished from your AI laptop and how to restore it quickly."
thumbnail: "/images/thumbs/copilot-missing-on-copilot-plus-pc.webp"
faqs:
  - q: "Should Copilot come preinstalled on a Copilot+ PC?"
    a: >
      Yes. Copilot+ PCs ship with Copilot installed and the Copilot key mapped to it. If it is missing on a brand-new machine, something removed it — a first-boot cleanup, an IT image, or a debloat script. Reinstalling from the Store restores it in minutes.
  - q: "Can a Windows update remove Copilot?"
    a: >
      It should not, but feature updates have occasionally replaced the Copilot app with a stub or failed to migrate it. If Copilot vanished right after an update, reinstalling from the Microsoft Store is the standard fix.
  - q: "Is Copilot hidden or actually uninstalled?"
    a: >
      Check Settings > Apps > Installed apps and search for Copilot. If it is listed, it is installed but possibly unpinned or hidden — search Start for it. If it is not listed at all, it was uninstalled and needs reinstalling.
  - q: "Does my region affect whether Copilot appears?"
    a: >
      Yes. On first setup in an unsupported region, Windows may skip installing Copilot entirely. The fix is the same — install it manually from the Store — though some features may remain limited until region support arrives.
---

It is a strange thing to unbox a Copilot+ PC — a machine literally named for Microsoft's AI assistant — and find no Copilot anywhere. Not on the taskbar, not in the Start menu, not in the app list. The dedicated key sits there, but the software it was built for is gone.

A missing Copilot on a Copilot+ PC is never normal, but it is rarely serious. The usual suspects: an overzealous debloat script, a corporate IT image that stripped it, a region-skipped install, or a Windows update that fumbled the app package. Because Copilot is now a regular Store app, restoring it is as simple as reinstalling any other app. If Copilot is present but broken, our [Copilot app not opening on Windows 11](/articles/copilot-app-not-opening-windows-11/) guide is the right next stop; if the key does nothing, see [Copilot web view not loading](/articles/copilot-web-view-not-loading/) only after confirming the app exists.

First, verify whether it is truly gone or just hiding, then restore it.

## Why this happens

- **Debloat scripts:** "Windows debloat" tools and scripts commonly uninstall Copilot as part of their cleanup.
- **Corporate or school images:** IT departments often strip Copilot from their deployment images for policy reasons.
- **Region-skipped install:** First-time setup in an unsupported region may skip Copilot installation entirely.
- **Failed feature update:** A Windows update can occasionally drop the app package instead of migrating it.
- **Unpinned, not uninstalled:** The app may be installed but removed from the taskbar and Start, making it look missing.
- **Wrong Microsoft Store region:** A mismatched Store region can hide the app listing, making reinstall look impossible.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify whether Copilot is installed or truly gone
Do not reinstall until you know which situation you are in.

1. Press the Windows key and type "Copilot." Check both Apps and search results carefully.
2. Open Settings > Apps > Installed apps, search for "Copilot," and see if "Microsoft Copilot" is listed.
3. If it is listed, it is installed — skip to Fix 2 to unhide it.
4. If it is not listed anywhere, it was uninstalled — skip to Fix 3 to reinstall.
5. Also check the taskbar: right-click it, open Taskbar settings, and confirm the Copilot toggle is on. A hidden toggle explains many "missing" reports.

### Fix 2: Unhide and repin an installed Copilot
If the app exists but you cannot find it, it is a visibility problem, not an installation problem.

1. In Start menu search, type Copilot, right-click the result, and choose "Pin to taskbar" and "Pin to Start."
2. Check Taskbar settings (right-click taskbar > Taskbar settings) and enable the Copilot toggle if present.
3. Look in the system tray overflow — the icon may be hiding there.
4. If search does not find it but Installed apps lists it, rebuild the search index: Settings > Privacy & security > Searching Windows > Advanced indexing options > Rebuild.
5. After reindexing completes, search again — the app should now appear.

### Fix 3: Reinstall Copilot from the Microsoft Store
The standard fix for a genuinely uninstalled Copilot.

1. Open the Microsoft Store and search for "Microsoft Copilot."
2. If the listing appears, click Install and wait for it to finish.
3. If the Store says the app is not available, your Store region may be mismatched — go to Settings > Time & language > Language & region and set the correct country, then try again.
4. After installing, launch Copilot from Start and sign in with your Microsoft account.
5. Pin it to the taskbar for easy access.
6. Press the Copilot key to confirm the key now launches the restored app.

### Fix 4: Restore it if a debloat script removed it
Debloat tools sometimes also block reinstalls, so check for that.

1. If you ran a debloat script (like a popular GitHub "Windows10Debloater" variant), check whether it has an undo or reinstall-apps function and run it.
2. Open PowerShell as administrator and run `Get-AppxPackage -AllUsers *Copilot*` to see if any package remnants exist.
3. If remnants exist but the Store will not install, remove them first: `Remove-AppxPackage -Package <full package name>` using the name from the previous command.
4. Then install fresh from the Microsoft Store.
5. Going forward, avoid debloat scripts on a Copilot+ PC, or at least whitelist Copilot before running them.
6. For the official app source, the [Microsoft Store](https://www.microsoft.com/en-us/software-download/windows11) ecosystem and [Microsoft Support](https://support.microsoft.com/en-us/windows) pages document the supported install paths.

### Fix 5: Handle the region-skipped install
If your PC was first set up in an unsupported region, Copilot may never have been installed.

1. Go to Settings > Time & language > Language & region.
2. Set your country or region to one where Copilot is supported, if that reflects reality.
3. Restart the laptop, then try installing Copilot from the Microsoft Store.
4. If the Store still hides it, our guide on [Copilot not available in your region](/articles/copilot-not-available-in-my-region/) covers deeper workarounds.
5. Remember that some Copilot features remain region-gated even after the app installs — the app appearing does not guarantee every feature works.

### Fix 6: Check for IT policy blocks
On work or school laptops, the absence may be deliberate policy rather than an accident.

1. Look for signs of management: a work/school account in Settings > Accounts, or unfamiliar security software.
2. Try installing from the Store. If it installs but vanishes after reboot, a policy is removing it.
3. Check with your IT administrator — they may have a sanctioned way to request Copilot.
4. Do not try to bypass corporate policy with registry hacks on a machine you do not own; that can violate acceptable-use rules.
5. On a personal machine showing these symptoms, run a malware scan — some "optimizer" malware strips apps.
6. Once restored, verify your machine still qualifies as a Copilot+ PC with our guide on [how to check if your laptop is a Copilot+ PC](/articles/how-to-check-if-laptop-is-copilot-plus-pc/).

## Closing

A missing Copilot on the very machines named after it is ironic, but the fix is usually a five-minute Store reinstall. The key diagnostic is simply whether the app is listed in Installed apps — hidden versus uninstalled determines everything that follows. And if a debloat script was the culprit, consider that a lesson about running aggressive cleanup tools on a brand-new AI PC. Once restored, if the app opens to a blank window, our [Copilot web view not loading](/articles/copilot-web-view-not-loading/) guide fixes the renderer. And if the Copilot key starts launching the wrong program instead, see [why the Copilot key opens the wrong app](/articles/copilot-key-opens-wrong-app/).
