---
title: "How to Fix Windows Update Error 0x80070643 on an HP Laptop"
slug: how-to-fix-windows-update-error-0x80070643-on-hp-laptop
date: 2026-09-03
categories: ["windows-update"]
tags: ["windows update", "0x80070643", "hp laptop", "windows 11"]
description: "Error 0x80070643 on your HP laptop means an update installation failed outright. This HP-focused guide covers .NET repair, the recovery partition, and manual installs."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070643-on-hp-laptop.webp"
faqs:
  - q: "What does error 0x80070643 mean on an HP laptop?"
    a: "It is ERROR_INSTALL_FAILURE: an update's installer ran and failed, rather than being blocked beforehand. On HP laptops the two classic triggers are a broken .NET Framework installation aborting the .NET update, and the Windows Recovery Environment update failing because the recovery partition is too small. The guide below addresses both, plus the Windows Installer service issues that cause the generic form of this error."
  - q: "Why does this error often involve .NET Framework?"
    a: "Because .NET updates use the Windows Installer (MSI) engine, which is fussier than the cumulative-update engine. If the existing .NET installation is damaged — missing files, broken registration — the MSI installer aborts instead of repairing it, and Windows Update reports 0x80070643. Repairing or reinstalling .NET first gives the update a healthy target to patch, which is why the .NET fixes come early in the sequence."
  - q: "Is the recovery partition really behind this error?"
    a: "Frequently, yes. The WinRE security update needs roughly 250 MB of free space on the hidden recovery partition, and many HP factory layouts leave far less. When the installer can't fit the new recovery image, it fails and the whole update reports 0x80070643. The partition check in this guide takes two minutes and is the highest-value diagnostic for this code on HP hardware."
  - q: "Can I just hide the failing update and move on?"
    a: "You can hide a specific update temporarily, but the packages behind most 0x80070643 cases — .NET security updates and the WinRE security update — patch real vulnerabilities, so hiding them leaves genuine exposure. The better investment is the hour it takes to work this guide: fix the .NET installation or extend the partition once, and the update installs cleanly along with everything queued behind it."
---

Error 0x80070643 is blunt: ERROR_INSTALL_FAILURE. The update's installer actually ran and then gave up — this isn't a download problem, a connection problem, or a missing prerequisite. Something in the installation itself went wrong, and Windows is reporting the failure honestly without much detail about which part broke.

On HP laptops, this code has two famous personalities. The first is the .NET Framework update that fails because the existing .NET installation is damaged — the installer tries to patch something broken and aborts. The second is the Windows Recovery Environment security update failing against a too-small recovery partition, an HP factory-layout specialty. The sequence below diagnoses which personality you're dealing with first, because the fixes diverge completely from there.

## Why this happens

- **A damaged .NET Framework installation.** The .NET updater is an MSI installer that aborts when its target is broken instead of repairing it.
- **Too-small recovery partition.** The WinRE update needs about 250 MB free on the hidden recovery partition; HP factory layouts often fall short.
- **A malfunctioning Windows Installer service.** The MSI engine itself misconfigured or stuck, failing every MSI-based update.
- **Corrupted update download.** A damaged package that fails its own installation integrity checks.
- **Third-party antivirus blocking the installer.** Security software interfering with the MSI process mid-install.
- **Pending reboot from a previous install.** A half-finished installation holding locks the new one needs.
- **Corrupted SoftwareDistribution metadata.** The updater feeding the installer bad instructions.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify which installer is failing

The fix path splits here, so get the diagnosis right.

1. Open **Settings > Windows Update > Update history** and find the 0x80070643 entry; note the KB number and the update's name.
2. If the name mentions **.NET Framework**, you're in the .NET branch — continue to Fix 2. If it mentions the **Windows Recovery Environment** or KB5034441-style WinRE updates, skip to Fix 4.
3. For anything else, note whether it's MSI-based (most driver and feature updates aren't) and continue in order.
4. Write down the exact KB — you'll need it for the manual install fallback later.

### Fix 2: Restart the Windows Installer service

The MSI engine sometimes just needs a fresh start.

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Find **Windows Installer**, right-click it, and choose **Restart** (or **Start** if it's stopped).
3. Confirm its startup type is **Manual** — that's the correct default; Disabled breaks all MSI installs.
4. Retry the update immediately; a healthy MSI engine clears the generic form of this error.

### Fix 3: Repair the .NET Framework installation

Give the .NET updater a healthy target to patch.

1. Download Microsoft's **.NET Framework Repair Tool**, run it as administrator, and apply every recommended fix.
2. If the tool doesn't resolve it, go to **Control Panel > Programs > Turn Windows features on or off**, uncheck the .NET Framework entries, restart, then re-check them to reinstall cleanly.
3. Restart the laptop after either repair path — .NET changes only fully apply at boot.
4. Retry the update; with .NET healthy, the previously failing .NET update installs normally.

### Fix 4: Check and extend the recovery partition

The highest-value check for the WinRE variant of this error.

1. In an administrator Command Prompt, run `reagentc /info` to locate the Windows RE partition, then use `diskpart` (`list disk`, `select disk 0`, `list partition`, `select partition N`, `detail partition`) to check its free space.
2. If free space is well under 250 MB, back up your files, shrink C: by about 500 MB in Disk Management, and extend the recovery partition into the freed space.
3. Run `reagentc /enable` to confirm the recovery environment still functions after the resize.
4. Retry the update — with room to install, the WinRE package completes instead of aborting.

### Fix 5: Clean boot to remove installer interference

Something may be sabotaging the install in progress.

1. Run `msconfig`; on the **Services** tab check **Hide all Microsoft services** and click **Disable all**.
2. Disable all **Startup apps** in Task Manager and restart.
3. Retry the failing update in the clean state.
4. If it succeeds, re-enable services in halves to find the interfering program — usually an overprotective security tool. HP's essential software can be restored from the [HP support site](https://support.hp.com/us-en) if needed.

### Fix 6: Reset the update cache and install manually

Clear stale data, then bypass the automatic path for the stubborn package.

1. In an administrator Command Prompt: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, then `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`, then restart the three services.
2. Download the failing KB as an x64 `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Run the standalone installer and restart when prompted.
4. Verify the KB shows as installed in Update history.

### Fix 7: Perform an in-place upgrade as the final repair

When installers keep failing despite healthy targets, rebuild the servicing stack.

1. Download the Windows 11 ISO from [Microsoft's official software download page](https://www.microsoft.com/en-us/software-download/windows11) and mount it.
2. Run `setup.exe`, accept the terms, and choose **Keep personal files and apps**.
3. Allow 30–90 minutes with several restarts, charger connected throughout.
4. After signing in, confirm the previously failing update installs cleanly — Microsoft's official Windows Update support hub documents these installer-failure scenarios in depth for further reading.

## Closing

Error 0x80070643 is an installer giving up mid-job, and on HP laptops the diagnosis that matters most is .NET versus recovery partition — get that right and the fix is straightforward. For the generic walkthrough, see the [step-by-step 0x80070643 guide](/articles/how-to-fix-windows-update-error-0x80070643-step-by-step/), and if your failure is a locked file rather than a failed install, the [0x80070020 guide for HP laptops](/articles/how-to-fix-windows-update-error-0x80070020-on-hp-laptop/) covers that distinct case.
