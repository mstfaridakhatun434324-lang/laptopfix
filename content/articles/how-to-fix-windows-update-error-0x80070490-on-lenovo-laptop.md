---
title: "Windows Update Error 0x80070490 on a Lenovo Laptop: Fixing It"
slug: how-to-fix-windows-update-error-0x80070490-on-lenovo-laptop
date: 2026-09-24
categories: ["windows-update"]
tags: ["0x80070490", "windows update", "lenovo laptop", "element not found"]
description: "Error 0x80070490 means Windows Update can't find an element it needs. Fix it on your Lenovo with component store and driver repairs."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070490-on-lenovo-laptop.webp"
faqs:
  - q: "What does error 0x80070490 mean?"
    a: "It translates to 'element not found' — the update engine looked for a specific component, manifest, or package element and could not find it. The usual culprits are a corrupted component store (WinSxS), a damaged driver package the update references, or corrupted update metadata. The update aborts because it cannot verify what it is installing."
  - q: "Is 0x80070490 a driver problem or a Windows problem?"
    a: "It can be either, which is why diagnosis matters. When the missing element is a driver package — common on Lenovo laptops with staged Lenovo drivers — updating drivers through Lenovo Vantage fixes it. When the missing element is a system component manifest, DISM's component store repair is the answer. The sequence below covers both paths."
  - q: "Will DISM fix 0x80070490?"
    a: "Very often, yes. DISM with the RestoreHealth option specifically repairs the component store, which is where the 'element not found' failures usually originate. Run it before the deeper manual steps — it resolves the majority of 0x80070490 cases that are not driver-related."
  - q: "Can I ignore 0x80070490 if everything seems to work?"
    a: "Not safely. The error means an update failed to install, so your system is missing whatever that update contained — usually security fixes. The laptop works fine today, but the unpatched vulnerability remains. Fix the error rather than ignoring it; the repairs are straightforward."
---

Error 0x80070490 — "element not found" — sits at the intersection of two common failure types: corrupted system components and broken driver packages. The update engine expected to find a specific element — a manifest in the component store, a driver package, a catalog entry — and it was not there. Without it, verification fails and the update aborts.

On Lenovo laptops, the driver-package variant is notably common: Lenovo's staged driver packages sometimes go missing or corrupt, and updates that reference them fail with this code. The sequence below starts with the component-store repair (the most common fix overall), then addresses the Lenovo driver angle. Work it in order. The [0x80070002 file-not-found guide](/articles/how-to-fix-windows-update-error-0x80070002-after-windows-11-update/) is a useful parallel reference for the cache side of these failures.

It helps to think of this error as a checklist problem: the installer has a list of elements it must verify, and it stops at the first one it cannot find. Your job is not to guess which element — it is to repair the places elements live. The component store, the driver store, and the update cache are those places, and Fixes 1 through 5 repair each of them in turn. One of them holds your missing element.

## Why this happens

- **Corrupted component store:** Damaged WinSxS manifests the update needs for verification.
- **Missing driver package:** A Lenovo driver package the update references is absent or corrupt.
- **Corrupted update metadata:** Catalog entries pointing at elements that do not exist.
- **Damaged update cache:** Staged files with missing pieces.
- **Broken driver store:** Orphaned driver entries confusing the installer.
- **Interrupted previous update:** A half-completed install leaving inconsistent component state.
- **Disk errors:** File system damage removing component files.
- **Antivirus quarantine:** Security software removing files the update expects.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Repair the component store with DISM

The highest-yield fix for this error — repair the store where elements go missing. Microsoft documents DISM repair on the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to complete — allow up to thirty minutes.
3. Run `sfc /scannow` afterward to fix any remaining file issues.
4. Restart the laptop.
5. Check for updates — the missing elements are now restored.

### Fix 2: Run the Windows Update troubleshooter

Let the automated tool handle the metadata and service side.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply its fixes.
3. Restart the laptop.
4. Retry the update.
5. If the error persists, the problem is in the store or drivers — continue.

### Fix 3: Update drivers through Lenovo Vantage

Address the Lenovo driver-package variant directly. Lenovo's driver guidance is on [Lenovo support](https://support.lenovo.com/us/en/).

1. Open **Lenovo Vantage** and run **System Update**.
2. Install all pending driver updates — especially chipset, storage, and system drivers.
3. Restart after the installs complete.
4. Retry Windows Update.
5. If a specific driver was the missing element, the error clears now.

### Fix 4: Reset the update components

Clear corrupted metadata and cache that reference missing elements.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart all four services and reboot.
5. Check for updates with a clean cache and rebuilt metadata.

### Fix 5: Clean the driver store

Remove orphaned driver packages that the installer trips over.

1. Open Device Manager, enable **View > Show hidden devices**, and uninstall grayed-out devices.
2. In an elevated Command Prompt, run `pnputil /enum-drivers`.
3. Delete packages for hardware you no longer own with `pnputil /delete-driver`.
4. Restart the laptop.
5. Retry the update — the driver side is now clean.

### Fix 6: Check disk health

Missing elements sometimes mean a disk that is losing files.

1. Back up important files first.
2. Run `chkdsk C: /f` from an elevated Command Prompt.
3. After the scan, re-run the DISM repair from Fix 1 on the healthy file system.
4. Retry the update.
5. If chkdsk found extensive damage, consider the drive suspect.

### Fix 7: Manual install, then monitor

Install the failed update directly and watch whether the error was a one-off. If [driver updates keep failing in Windows Update](/articles/how-to-fix-driver-updates-failing-in-windows-update-after-windows-11-update/) alongside this error, treat the driver pipeline as the root cause.

1. Note the KB number from update history.
2. Download it from the Microsoft Update Catalog and install manually.
3. Restart when prompted.
4. Run **Check for updates** afterward — if new updates install cleanly, the store repair held.
5. If 0x80070490 returns on the next update, the component store needs deeper attention — consider an in-place upgrade repair.

### Fix 8: In-place upgrade repair for deep store damage

When DISM cannot fully repair the component store, the in-place upgrade rebuilds it.

1. Download the Windows 11 Media Creation Tool from Microsoft.
2. Run it, choose **Upgrade this PC now**, and keep personal files and apps.
3. The repair install reconstructs the entire component store from clean sources.
4. After completion, run **Check for updates** — the store is now pristine.
5. The 0x80070490 error should not return; if it does, suspect the drive itself.

## Closing

Error 0x80070490 is the update engine reporting a gap — a component, manifest, or driver package it expected is not there. DISM fills the component-store gaps, Vantage fills the Lenovo driver gaps, and the cache reset clears the metadata confusion. Work the sequence in order and the gap closes; the update that failed verification installs cleanly, and the code that looked cryptic turns out to have been describing something perfectly mechanical all along. Component store health is worth checking proactively — a DISM scan once or twice a year catches this class of problem before it blocks an update.
