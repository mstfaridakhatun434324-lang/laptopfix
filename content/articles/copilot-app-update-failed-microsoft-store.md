---
title: "How to Fix Copilot App Update Failures in the Microsoft Store"
slug: copilot-app-update-failed-microsoft-store
date: 2026-10-21
categories: ["ai-pc"]
tags: ["copilot update failed", "microsoft store update error", "copilot app won't update", "windows 11", "ai pc", "wsreset"]
description: "Copilot stuck with a failed Microsoft Store update? Get six proven fixes for Copilot app update errors, from the wsreset cache clear to a clean reinstall."
thumbnail: "/images/thumbs/copilot-app-update-failed-microsoft-store.webp"
faqs:
  - q: "Why does the Copilot update keep failing in the Microsoft Store?"
    a: "Most failures come from a corrupt Store cache, a stuck update service, missing disk space, or the Copilot package being half-registered. The Store then aborts the download rather than installing a broken package, and the error repeats on every retry."
  - q: "Is it safe to reset the Microsoft Store?"
    a: "Yes. Running wsreset or resetting the Store app only clears the Store's cache and temporary files. Your installed apps, purchases, and sign-ins stay untouched — you may need to sign in to the Store again."
  - q: "Will uninstalling Copilot delete my conversations?"
    a: "No. Your Copilot chat history is stored against your Microsoft account, not locally. After reinstalling and signing back in, your history syncs back down."
  - q: "What if the update fails with an error code like 0x80073CF9?"
    a: "That family of codes almost always points to the Store cache or the update folders. Fix 1 (wsreset) and Fix 4 (SoftwareDistribution cleanup) resolve the majority of them; a full reinstall covers the rest."
---

You open the Microsoft Store, hit update on Copilot, and watch it fail — again. Maybe it shows an error code like 0x80073CF9, maybe it just spins and gives up. Either way you are stuck on an old version, missing features and bug fixes.

Copilot updates ride on the Microsoft Store's packaging pipeline, which is stricter than a normal installer: if the Store cache is corrupt, the update service is stuck, or the existing package is half-registered, the Store aborts rather than risk a broken install. That strictness protects you, but it turns small glitches into repeated failures.

This guide walks you through six fixes in technician order: clearing the Store cache first, then repairing Store services and update folders, and ending with a clean Copilot reinstall. Work down the list until updates flow.

## Why this happens

- **Corrupt Microsoft Store cache**: A damaged cache makes the Store misread the Copilot package manifest, so every update attempt aborts before downloading.
- **Stuck Windows Update service**: Store app updates share infrastructure with Windows Update. If that service is wedged, package updates queue behind it forever.
- **Half-registered Copilot package**: A previous failed or interrupted update leaves the Copilot package in a limbo state the Store cannot cleanly overwrite.
- **Broken SoftwareDistribution data**: Corrupt metadata in the update download folder causes the Store to keep fetching a bad package copy.
- **Low disk space**: Package updates need room to stage the download, unpack it, and swap it in. Below roughly 5–10 GB free, updates silently fail.
- **Wrong date, time, or region**: The Store validates package certificates against your clock and region. A wrong time or a mismatched region can invalidate signatures and block updates.
- **Metered connection pause**: On a metered connection, Windows defers Store updates — and a mislabeled network can stall them indefinitely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reset the Microsoft Store cache with wsreset

This is the classic Store fix and it clears the most common cause of repeated update failures in about ten seconds.

1. Close the Microsoft Store completely — end any **Microsoft Store** process in Task Manager too.
2. Press **Win + R**, type **wsreset.exe**, and press Enter.
3. A blank command window appears; wait for it to close on its own and the Store to open.
4. In the Store, go to **Downloads** (or Library), find Copilot, and retry the update. Microsoft documents Store basics at [Microsoft Support](https://support.microsoft.com/en-us/windows) if the Store itself is missing.

### Fix 2: Repair and reset the Microsoft Store app

If wsreset was not enough, reset the Store app itself — this re-registers its components and clears deeper state.

1. Open **Settings > Apps > Installed apps** and search for **Microsoft Store**.
2. Click **three dots > Advanced options**, then click **Repair** first.
3. If the update still fails, click **Reset** and confirm.
4. Restart the PC, reopen the Store, and retry the Copilot update.

### Fix 3: Free disk space and fix date/time settings

Two silent blockers are trivial to check, so rule them out before touching services.

1. Open **Settings > System > Storage** and make sure you have at least **10 GB free**; run Disk Cleanup or empty the Recycle Bin if not.
2. Open **Settings > Time & language > Date & time**, enable **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
3. Check **Settings > Network & internet > Wi-Fi**, and if your network is set as **metered**, turn that off (or set **Download apps over metered connections** to On in the Store's settings).
4. Retry the Copilot update from the Store library.

### Fix 4: Clear the SoftwareDistribution update folder

When the Store keeps downloading a corrupt package copy, deleting the cached update data forces it to fetch fresh metadata.

1. Press **Win + R**, type **services.msc**, and stop the **Windows Update** service (right-click > Stop).
2. In File Explorer, open **C:\Windows\SoftwareDistribution\Download** and delete its contents (leave the folder).
3. Go back to Services and **start** Windows Update again.
4. Reopen the Store and retry — the Copilot update now pulls a fresh package manifest.

### Fix 5: Re-register the Copilot package with PowerShell

A half-registered package resists normal updates. Re-registering it rewrites the registration cleanly without deleting your data. Use this fix too when the app opens but [keeps crashing instead of updating](/articles/copilot-app-crashing/) — crashes and update failures usually share the same broken package state, so one repair clears both.

1. Right-click Start and choose **Terminal (Admin)**.
2. Run: `Get-AppxPackage -Name Microsoft.Copilot | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for the command to finish, then restart the PC.
4. Check the Store — Copilot often updates itself cleanly right after re-registration. If the app also refuses to launch between update attempts, the [Copilot app not opening guide](/articles/copilot-app-not-opening-windows-11/) covers launch repair.

### Fix 6: Uninstall Copilot completely, then install the latest version

When every repair fails, the package is too damaged to patch. A full removal plus a fresh install is the reliable endgame — the package is small, so the whole swap takes under five minutes, and signing back in with the same Microsoft account brings everything back.

1. In Settings > Apps > Installed apps, **uninstall** Microsoft Copilot and restart the PC.
2. Confirm at least 10 GB free space and a stable connection.
3. Open the Microsoft Store, search **Microsoft Copilot**, and install it fresh — this always pulls the newest build.
4. Sign in and confirm the version under the app's settings. Update failures sometimes cluster with other stuck system updates on Snapdragon machines — if background updates are also misbehaving, see the [sleep battery drain fix for Snapdragon laptops](/articles/battery-drain-in-sleep-snapdragon-laptop/) and, for firmware-side stalls, the [Intel NPU firmware update stuck guide](/articles/intel-npu-firmware-update-stuck/).

## Closing

Copilot update failures are a Store-pipeline problem, not a Copilot problem: clear the cache, repair the Store, clean the update folders, and the packages flow again. Keep 10 GB free and your clock synced, and you will rarely see this screen again. A full reinstall is always there as the final, reliable reset.
