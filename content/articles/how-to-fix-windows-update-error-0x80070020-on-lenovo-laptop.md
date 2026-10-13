---
title: "How to Fix Windows Update Error 0x80070020 on a Lenovo Laptop"
slug: "how-to-fix-windows-update-error-0x80070020-on-lenovo-laptop"
date: 2026-10-01
categories: ["windows-update"]
tags: ["error 0x80070020", "windows update", "lenovo laptop", "file in use", "windows 11"]
description: "Windows Update error 0x80070020 means another program is locking files the updater needs. Seven fixes from clean boots to antivirus pauses for Lenovo laptops."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070020-on-lenovo-laptop.webp"
faqs:
  - q: "What does error 0x80070020 mean?"
    a: "It is the standard Windows sharing-violation error: the update installer tried to touch a file that another process had locked. The installer needs exclusive access to replace system files, drivers, or staging data, and any program holding those files open — antivirus scanners, indexers, background updaters, or a crashed earlier install — causes the collision. Releasing the locks, rather than repairing anything, is the fix."
  - q: "Which program is locking the files?"
    a: "Antivirus real-time scanners top the suspect list, followed by the Windows Search indexer and third-party background updaters. A clean boot settles the question definitively: if the update installs in a clean boot, re-enable startup items in halves to find the offender. Lenovo utilities can also hold driver files open during driver updates, so keep them on the suspect list."
  - q: "Will restarting fix 0x80070020?"
    a: "Often, yes — a restart drops transient locks left by crashed processes and unfinished operations. But locks held by startup programs come back after every reboot, which is why a plain restart sometimes fails where a clean boot succeeds. If one normal restart does not clear it, do the clean boot instead of rebooting repeatedly and hoping for luck."
  - q: "Is it safe to disable antivirus for the update?"
    a: "Yes, briefly and with precautions. Pause real-time protection only for the length of the install, avoid untrusted sites in that window, and switch it back on immediately afterward. Windows Defender stays active as a backstop when you only pause the third-party suite. If the update then succeeds, add the updater to exclusions so you skip this dance every month."
---

Error 0x80070020 translates to "the process cannot access the file because it is being used by another process." The update installer needs to swap out certain files, but something on your Lenovo laptop is gripping them. Until those locks release, the installation cannot move forward.

Picture two people trying to walk through the same doorway: nothing is broken, they are just in each other's way. That is the entire nature of this error — contention, not corruption. If your failures mention corrupted data instead of locked files, the [0x80070070 disk-full guide](/articles/how-to-fix-windows-update-error-0x80070070-on-lenovo-laptop/) addresses that different failure mode.

The path forward is detective work: identify whatever is holding the files and quiet it down. Clean boots and antivirus pauses settle most cases; the service checks near the end handle the stubborn ones.
## Why this happens

- **Antivirus real-time scanning:** Security suites lock files while scanning them. If the updater tries to replace a file mid-scan, the two collide and the install fails.
- **Windows Search indexer at work:** The indexer opens huge numbers of files to catalog them, and updates touching indexed locations can clash with an active indexing pass.
- **Third-party updaters and overlays:** Driver updaters, game overlays, and sync clients keep hooks in files adjacent to what the installer must replace.
- **A crashed earlier installer:** A previous install that died can leave file handles open indefinitely, blocking every later attempt at the same files.
- **Update services tripping over themselves:** Occasionally the update services hold staging files open while a second phase of the install tries to use them.
- **Lenovo utilities gripping driver files:** Lenovo's own software — Vantage, its system update agents — can keep driver files open while a Windows driver update tries to replace them. Check the Lenovo support site for newer Vantage builds if this recurs.
- **Running apps with open locks:** Active applications, especially ones with auto-update components, can lock shared libraries the system update needs.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Clean-boot the laptop, then retry

Before anything else, rule out the obvious: some background program is probably holding the files. Updaters, overlays, and driver utilities lock files and services the installer needs. A clean boot starts Windows with only Microsoft services running, which reveals whether a third-party program is the culprit — without uninstalling anything.

1. Press Win + R, enter msconfig, and switch to the Services tab.
2. Select Hide all Microsoft services and click Disable all.
3. Open Task Manager, go to Startup apps, and disable each listed item.
4. Restart, attempt the update again, then restore your startup items.

### Fix 2: Pause third-party antivirus for the install

Here is where the trail often ends. Third-party security suites sometimes stop the update installer from writing files or launching services, and the errors they produce never mention the antivirus. Testing with real-time protection off for the install is a legitimate diagnostic — Windows Defender keeps watch in the meantime. Microsoft's [official Windows support hub](https://support.microsoft.com/en-us/windows) counts antivirus interference among the usual update blockers.

1. Bring up your antivirus dashboard and switch off real-time protection.
2. Run the update installation with protection still paused.
3. Re-enable real-time protection as soon as the install completes.
4. If this fixes it, add the updater to your suite's exclusions so the next update sails through.

### Fix 3: Make sure the update services are running

A quick service check eliminates a whole class of failures. Windows Update depends on several background services, and when any of them is disabled or stuck, installs fail. Tweaking tools and aggressive debloating scripts sometimes shut them off. The Services console settles the question in under a minute.

1. Hit Win + R, type services.msc, and press Enter.
2. Look for Windows Update, Background Intelligent Transfer Service, Cryptographic Services, and Windows Installer.
3. Set every startup type to Automatic (Manual for Windows Installer) and start the stopped ones.
4. With the services running, retry the update.

### Fix 4: Flush the SoftwareDistribution cache

When downloads or install states get corrupted, the updater keeps stumbling over its own leftovers. Stopping the update services and renaming the SoftwareDistribution and catroot2 folders forces Windows to rebuild them cleanly — fresh permissions, no stale pending operations for anyone to fight over.

1. Start an admin-level Command Prompt — right-click Start and pick Terminal (Admin).
2. Run these four stop commands: net stop wuauserv, net stop cryptSvc, net stop bits, net stop msiserver.
3. Archive the old folders by renaming: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old, then ren C:\Windows\System32\catroot2 catroot2.old.
4. Use net start to revive the services, then check for updates once more.

### Fix 5: Let the other installer finish first

Windows permits only one trusted installer operation at a time. If another update, a Store app update, or an MSI installer is running in the background, your update is correctly refused until that one completes. The remedy here is patience plus verification, not force.

1. In Settings, open Windows Update and check if a different update is currently installing.
2. Open Task Manager and look for msiexec.exe or TiWorker.exe using CPU.
3. Let any installation already running finish completely, then restart the laptop.
4. Attempt your update again after the system goes idle.

### Fix 6: Strip the laptop down to just its charger

USB devices, docks, external drives, and SD cards all load drivers during update installation, and a flaky one can stall or crash the installer. Lenovo docks and USB-C hubs are frequent offenders. Unplugging everything except the power adapter removes these variables in one move.

1. Shut the laptop down completely.
2. Unplug every USB device, dock, external monitor, and SD card — leave only the power adapter.
3. Power on and retry the update with nothing attached.
4. Reconnect devices one at a time afterward to identify the troublemaker.

### Fix 7: Repair Windows without losing files

If the locks refuse to clear, rebuild around them. A repair install reconstructs Windows around your files and apps instead of wiping them, replacing all system files, services, and update components with fresh copies. Back up your data beforehand anyway — repairs are safe, not risk-free. A repair install from the [official Windows 11 download](https://www.microsoft.com/en-us/software-download/windows11) replaces locked system files cleanly when nothing else releases them.

1. Download Microsoft's official Windows 11 media creation tool from its download page.
2. Start it, choose Upgrade this PC now, and opt to Keep personal files and apps.
3. Let the installation finish — several restarts will occur.
4. Once setup is done, run Windows Update a final time to catch leftovers from the repair image.

## Closing

File-lock errors are irritating but rarely serious — something is simply standing in the way, not broken underneath. A clean boot that lets the update install undisturbed resolves the overwhelming majority of these cases on Lenovo laptops. If the failure instead points at deep component damage, the [0x80073712 component-store guide](/articles/how-to-fix-windows-update-error-0x80073712-on-lenovo-laptop/) takes over from here.
