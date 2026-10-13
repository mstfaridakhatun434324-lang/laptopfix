---
title: "How to Fix Windows Update Error 0x80070643 Step by Step"
slug: how-to-fix-windows-update-error-0x80070643-step-by-step
date: 2026-09-04
categories: ["windows-update"]
tags: ["windows update", "0x80070643", "install failure", "windows 11"]
description: "Error 0x80070643 means an update installer failed during installation. Follow this step-by-step guide — repair .NET, check the recovery partition, and finish it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070643-step-by-step.webp"
faqs:
  - q: "What causes Windows Update error 0x80070643?"
    a: "The code is ERROR_INSTALL_FAILURE: the update's installer executed and failed partway through. The leading causes are a damaged .NET Framework installation aborting the .NET update, the WinRE security update failing against a too-small recovery partition, a malfunctioning Windows Installer service, antivirus interfering with the install, or a corrupted download. Identifying which installer failed determines the entire repair path."
  - q: "How do I repair the .NET Framework properly?"
    a: "Start with Microsoft's .NET Framework Repair Tool run as administrator — it detects and fixes the common damage patterns automatically. If that doesn't clear it, toggle the .NET features off and back on in the Windows Features dialog, which reinstalls them cleanly, and restart. Retry the update only after the restart, since .NET repairs finalize at boot."
  - q: "Why would the recovery partition matter for an update?"
    a: "The Windows Recovery Environment lives on a small hidden partition, and its security updates must install the new recovery image there. If the partition has less than about 250 MB free — common on factory layouts — the installer aborts and the update reports 0x80070643. Extending the partition by shrinking the main Windows partition slightly is the permanent fix."
  - q: "Is it safe to re-register the Windows Installer service?"
    a: "Yes. Restarting the Windows Installer service and re-registering its components with msiexec commands only affects the installation engine, not your programs or data. It is a standard, documented troubleshooting step. The service should be on Manual startup; if something set it to Disabled, returning it to Manual restores normal MSI behavior."
---

Error 0x80070643 means ERROR_INSTALL_FAILURE — the installer ran and failed. That distinguishes it from the errors that stop updates before they begin: the download was fine, the prerequisites were fine, and then the actual installation fell over. The code doesn't say which part of the install broke, so the first job is always identifying the failing installer.

In practice, this error has three repeat offenders: the .NET Framework updater choking on a damaged .NET installation, the Windows Recovery Environment update hitting a too-small recovery partition, and the Windows Installer engine itself misbehaving. The sequence below identifies your offender first, then applies the targeted repair — because the .NET fix and the partition fix have nothing in common, and guessing wastes an afternoon. One more diagnostic shortcut worth knowing: if the same KB fails with 0x80070643 on every retry but installs fine from the manual .msu download, the problem was never the installer or its target — it was the automatic delivery path, usually a corrupted cache or a transient metadata issue. That pattern tells you the system is healthy and you can stop repairing it; just install the handful of affected updates manually and move on with a clear cache.

## Why this happens

- **Damaged .NET Framework.** The MSI-based .NET updater aborts when patching a broken .NET installation.
- **Undersized recovery partition.** The WinRE update needs ~250 MB free that factory layouts often don't provide.
- **Broken Windows Installer service.** The MSI engine misconfigured, stuck, or disabled.
- **Corrupted package download.** A damaged installer that fails its own checks mid-install.
- **Antivirus interference.** Security software blocking installer operations as they happen.
- **Pending reboot locks.** A previous half-finished install holding what the new one needs.
- **Stale update metadata.** The updater handing the installer incorrect instructions.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the failing installer

Everything downstream depends on this diagnosis.

1. Open **Settings > Windows Update > Update history**; find the 0x80070643 failure and read its full name and KB number.
2. **.NET Framework** in the name means the .NET branch (Fix 3). **Recovery Environment** or WinRE means the partition branch (Fix 4).
3. Anything else usually means the Windows Installer engine or a corrupted package — continue in order.
4. Keep the KB number handy for the manual-install fallback in Fix 6.

### Fix 2: Restart the Windows Installer service

A stuck MSI engine fails every MSI-based update until it's restarted.

1. Open `services.msc` and locate **Windows Installer**.
2. Right-click and choose **Restart** (or **Start** if stopped); verify startup type is **Manual**.
3. For deeper trouble, re-register the engine in an administrator Command Prompt: `msiexec /unregister` followed by `msiexec /regserver`.
4. Retry the update; a healthy engine clears the generic installer-failure variant.

### Fix 3: Repair .NET Framework

The most common specific cause gets its dedicated repair.

1. Run Microsoft's **.NET Framework Repair Tool** as administrator and apply all its recommended fixes.
2. If the error persists, open **Control Panel > Programs > Turn Windows features on or off**, uncheck all .NET Framework entries, restart, re-check them, and restart again.
3. The double restart matters — .NET servicing finalizes across reboots.
4. Retry the failing .NET update; a clean .NET target lets the installer complete.

### Fix 4: Extend the recovery partition

The definitive fix for the WinRE variant.

1. Run `reagentc /info` in an administrator Command Prompt to find the WinRE partition, then inspect it in `diskpart` (`list disk` → `select disk 0` → `list partition` → `select partition N` → `detail partition`).
2. Under ~250 MB free means the partition is guilty. Back up, shrink C: by ~500 MB in Disk Management, and extend the recovery partition.
3. Re-enable with `reagentc /enable` and confirm it reports enabled.
4. Retry the update; the WinRE installer now has room to work.

### Fix 5: Clean boot to isolate interference

Rule out third-party sabotage of the install process.

1. In `msconfig`, hide Microsoft services and **Disable all** the rest; disable all **Startup apps** in Task Manager.
2. Restart into the clean state and retry the update.
3. Success here indicts a third-party program — re-enable in halves to identify it.
4. Antivirus with aggressive behavior shields is the usual suspect; configure exclusions rather than leaving protection off.

### Fix 6: Reset the cache and install the package manually

Fresh metadata plus a direct install for the stubborn package.

1. In an administrator Command Prompt: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`; rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `catroot2` to `catroot2.old`; restart the services.
2. Download the exact KB as an x64 `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Run the standalone installer with antivirus temporarily paused, then restart.
4. Confirm the install in Update history.

### Fix 7: In-place upgrade as the final repair

Rebuild the servicing and installer stack when nothing targeted works.

1. Get the Windows 11 ISO from [Microsoft's official software download page](https://www.microsoft.com/en-us/software-download/windows11) and mount it.
2. Run `setup.exe`, accept the terms, select **Keep personal files and apps**.
3. Let the 30–90 minute upgrade complete with the charger connected.
4. Verify the update installs afterward. For further reading on installer failures, Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) is the authoritative source.

### Fix 8: Use the Installation Assistant for stuck feature updates

When the failing package is a feature update rather than a cumulative one, sidestep Windows Update entirely.

1. Download the **Windows 11 Installation Assistant** from Microsoft's official software download page.
2. Run it and let it handle the feature update end-to-end — it uses its own download and install flow.
3. Keep the laptop plugged in and undisturbed for the 30–90 minute process.
4. Afterward, return to **Settings > Windows Update** for the remaining smaller updates, which now install without the feature-update roadblock ahead of them.

## Closing

Error 0x80070643 rewards correct diagnosis over repeated retrying — .NET, recovery partition, or installer engine, each with its own fix. For HP-specific wrinkles like factory partition layouts, see the [HP laptop version](/articles/how-to-fix-windows-update-error-0x80070643-on-hp-laptop/), and if your update fails because another install is already running, the [0x80070652 step-by-step guide](/articles/how-to-fix-windows-update-error-0x80070652-step-by-step/) addresses that sibling error.
