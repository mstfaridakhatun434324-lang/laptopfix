---
title: "How to Fix Windows Update Error 0x80246007 on a Lenovo Laptop"
slug: "how-to-fix-windows-update-error-0x80246007-on-lenovo-laptop"
date: 2026-10-07
categories: ["windows-update"]
tags: ["error 0x80246007", "windows update", "lenovo laptop", "download manager", "windows 11"]
description: "Windows Update error 0x80246007 means the download manager failed on your Lenovo laptop. Seven fixes for BITS, cache, and network problems."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80246007-on-lenovo-laptop.webp"
faqs:
  - q: "What does error 0x80246007 mean?"
    a: "It means WU_E_DM_NOTDOWNLOADED: the download manager component could not download the update. The distinction matters — this is not a network block or a server refusal, but a failure in the local machinery (chiefly BITS, the Background Intelligent Transfer Service) responsible for fetching files. Causes range from a stopped BITS service and corrupted job queues to antivirus interference and the disk filling up mid-transfer."
  - q: "What is BITS and why does it matter?"
    a: "BITS — Background Intelligent Transfer Service — is Windows' managed download engine, built to move files using idle bandwidth without disturbing foreground work. Windows Update depends on it for every payload download. When BITS is stopped, its queue is corrupted, or its registration is damaged, updates cannot download at all. Restarting the service and clearing its queue resolves most BITS-related failures."
  - q: "Can I reset BITS without breaking anything?"
    a: "Yes. Stopping the BITS service, clearing its queue, and restarting it only discards in-progress background transfers, which Windows Update simply re-queues. Your files, apps, and settings are untouched. The component reset in this guide handles BITS as part of its service-restart sequence, so the BITS reset comes bundled with the broader fix."
  - q: "Why do downloads fail but browsing works?"
    a: "Because BITS transfers differently than your browser — throttled background transfers, its own protocols, its own queue. A network that handles bursty browser traffic fine can still disrupt BITS' long-lived managed transfers, and local BITS corruption breaks downloads while browsing sails on untouched. A working browser plus failing updates points at BITS or its configuration, not the connection."
---

Error 0x80246007 comes from the download manager itself: the component responsible for fetching update files reports that it could not complete the job. Your Lenovo laptop knows what it needs and where to get it — but the fetching machinery is broken. That is a subtle but important distinction from a network block.

Think of it as a delivery truck with a flat tire rather than a closed road. If the road itself were blocked — proxies, firewalls — the [0x800F0988 component-mismatch guide](/articles/how-to-fix-windows-update-error-0x800f0988-on-lenovo-laptop/) would cover that different problem.

The fixes target the download pipeline: the BITS service, the cache, and the network path. The manual catalog install at the end bypasses the pipeline completely.
## Why this happens

- **BITS stopped or broken:** The Background Intelligent Transfer Service does the actual downloading. If it is disabled, crashed, or corrupted, every download fails at the manager level.
- **A jammed BITS queue:** Stuck or damaged jobs in the queue can block the entire pipeline, so new downloads never begin.
- **A damaged download cache:** Corruption in SoftwareDistribution confuses the download manager's bookkeeping, and it aborts jobs it cannot track.
- **Antivirus intercepting transfers:** Security suites that proxy downloads can break the transfer protocol BITS expects, producing manager-level failures.
- **Repeated network drops mid-transfer:** Enough interruptions exhaust BITS retry logic, and the manager eventually reports failure instead of retrying forever.
- **The disk filling up mid-download:** If the drive fills while chunks are arriving, the manager cannot write them and fails the job.
- **Broken registration of the download manager:** If its COM registration is damaged, download jobs cannot even be created properly.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Get BITS and its companion services running

The delivery truck needs its engine on. Windows Update depends on a small crew of background services — BITS chief among them — and if any is disabled or stuck, downloads fail. System tweakers and debloating tools occasionally switch them off. The Services console exposes that in under a minute. BITS leans on several companion services — Microsoft's [official Windows support hub](https://support.microsoft.com/en-us/windows) documents the full dependency chain.

1. Press Win + R, type in services.msc, and press Enter.
2. Check on Windows Update, Background Intelligent Transfer Service, Cryptographic Services, and Windows Installer.
3. Make each startup type Automatic — Manual for Windows Installer — and start any stopped service.
4. With all four services up, attempt the update again.

### Fix 2: Reinitialize the Windows Update components

A corrupted cache jams the download manager's bookkeeping until it aborts jobs it cannot track. Stopping the update services and renaming the SoftwareDistribution and catroot2 folders forces Windows to rebuild them cleanly, with fresh permissions and no stale pending operations.

1. Pull up an elevated command line: right-click Start, then Terminal (Admin).
2. Stop the quartet with net stop wuauserv, net stop cryptSvc, net stop bits, net stop msiserver.
3. Retire both folders with new names: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Restore the services via net start, then check for updates anew.

### Fix 3: Clean up the network configuration

The truck cannot deliver on a broken road. Stale DNS entries, corrupted socket configuration, and leftover proxy settings can all degrade the connection to Microsoft's servers. Resetting the stack returns networking to known-good defaults without touching files or apps.

1. Get an elevated Command Prompt open.
2. Run the trio: ipconfig /flushdns, netsh winsock reset, netsh int ip reset.
3. Reboot to let the reset take hold.
4. Rejoin the network and retry the update with clean settings.

### Fix 4: Stop antivirus from intercepting the transfer

Security suites that proxy downloads can break the exact transfer protocol BITS expects — and the resulting failures never name the antivirus. Pausing real-time protection for the install is a legitimate diagnostic, with Windows Defender covering you meanwhile.

1. Start your antivirus dashboard and suspend real-time protection.
2. Execute the update install while real-time protection is paused.
3. Re-activate protection the instant the install completes.
4. If this fixes it, add the updater to your suite's exclusion list so future updates install smoothly.

### Fix 5: Make room on the disk before retrying

A download manager with nowhere to write is a download manager that fails. Windows Update needs working room — typically 10 GB or more free — to stage, extract, and install packages, and on Lenovo laptops with smaller SSDs the drive can be nearly full without warning. Freeing space takes two minutes and fixes more failures than most people expect.

1. Open Settings, go to System, then Storage, and turn on Storage Sense.
2. Open Disk Cleanup via Start and delete temporary files, delivery optimization files, and old update leftovers.
3. Uninstall bulky apps or games you no longer use.
4. Make sure at least 10 GB is free, then retry the update.

### Fix 6: Re-register the core update DLLs

If the download manager's COM registration is damaged, its jobs cannot even be created properly. The update engine is a collection of COM components, and re-registering the core DLLs rebuilds those registrations from scratch.

1. Bring up a Command Prompt with admin rights.
2. Stop the Windows Update service using net stop wuauserv.
3. Register the core files again: regsvr32 wuaueng.dll, regsvr32 wucltux.dll, regsvr32 wuwebv.dll, and regsvr32 wups2.dll, confirming every dialog.
4. Bring the service back using net start wuauserv and retry the update.

### Fix 7: Install the update manually from the Update Catalog

When the pipeline itself is broken, skip it. Downloading the package directly bypasses the download manager entirely. The Microsoft Update Catalog offers every cumulative update as a standalone installer, and installing by hand often works where Windows Update stalls. The standalone package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) gets you patched without the pipeline.

1. Within Settings, open Windows Update and then Update history to find the failing update's KB number.
2. Query the Microsoft Update Catalog with the KB number and open the result.
3. Pull the x64 version that fits your Windows 11 build.
4. Run the .msu download, follow the installation wizard, and reboot when prompted.

## Closing

Download-manager failures live one layer beneath the network: the road is open, but the truck is broken. Repairing BITS and clearing its queue restores the pipeline, and it tends to stay healthy afterward. Lenovo owners can let Lenovo Vantage handle driver and firmware updates in parallel, keeping the Windows pipeline focused on system updates. If downloads succeed but payloads mismatch during install, the [0x800F0989 delta-combination guide](/articles/how-to-fix-windows-update-error-0x800f0989-on-lenovo-laptop/) continues the troubleshooting path.
