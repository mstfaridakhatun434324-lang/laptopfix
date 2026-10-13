---
title: "Windows Update Error 0x80080005 on Windows 11: Restart the Update Engine"
slug: how-to-fix-windows-update-error-0x80080005-on-windows-11
date: 2026-10-09
categories: ["windows-update"]
tags: ["windows update", "0x80080005", "windows 11", "server execution failed", "com error"]
description: "Error 0x80080005 means Windows 11 could not start its own update engine. This guide restarts the failed components and repairs the underlying cause."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80080005-on-windows-11.webp"
faqs:
  - q: "What does error 0x80080005 mean in Windows 11 Update?"
    a: "It is a COM server execution failure: Windows tried to launch the update engine's background components and they failed to start. The root cause is usually a wedged update service, corrupted component registrations, or damaged system files rather than a network problem."
  - q: "Is 0x80080005 caused by my internet connection?"
    a: "Rarely. This code fires before any network traffic happens — the failure is local, in starting the update machinery. If your browser works fine but updates fail with this code, the connection is innocent and the repair belongs to the services and system files."
  - q: "Can third-party software cause 0x80080005?"
    a: "Yes. Aggressive system cleaners, old driver utilities, and some antivirus products can damage or block the COM registrations Windows Update needs. If the error started right after installing such software, uninstalling it is a sensible early step. Reinstall such tools only from the vendor's current release after updates work again."
  - q: "How is this different from other update errors?"
    a: "Most update codes describe something that went wrong during download or installation. 0x80080005 is earlier in the chain: the engine itself would not start. That is why the fixes focus on services, COM registrations, and file integrity instead of network settings."
---

Error 0x80080005 has a distinctive signature: Windows Update fails almost instantly, sometimes the moment you open the page, with a code that translates to server execution failed. In plain terms, Windows 11 tried to spin up the background machinery that handles updates — and the machinery would not start. No download was attempted, no server was contacted; the failure happened entirely inside your laptop.

That actually narrows the hunt nicely. The suspects are the update services themselves, the COM registrations they depend on, and the system files underneath both. It is a local repair job, not a network adventure, which means every fix below runs on your machine with no waiting on servers. The one exception: if an update previously got stuck mid-rollback on this machine, check our [undoing changes stuck guide](/articles/best-way-to-fix-undoing-changes-made-to-your-computer-stuck/) first, since a wedged rollback can hold the same services hostage.

Work through the fixes in order. The early ones restart and re-register the engine; the later ones repair the files it stands on.

## Why this happens

- **Wedged update services**: wuauserv or BITS stuck in a stopping state prevents the engine from launching a fresh instance.
- **Broken COM registrations**: The update engine is COM-based; unregistered or corrupted DLLs make activation fail immediately.
- **Damaged system files**: Corruption in core Windows files that the update stack loads at startup.
- **Interference from cleanup utilities**: Overzealous cleaners sometimes delete or unregister components Windows Update needs.
- **Corrupt SoftwareDistribution state**: A badly damaged cache can crash the service during initialization.
- **Insufficient disk space for staging**: The engine checks working space at startup and aborts if there is not enough.
- **Conflicting third-party services**: Some driver updaters and system tools hook the same components and block startup.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter

The troubleshooter's first job is checking whether the update services can start at all, which makes it a natural opener for an engine-startup failure. Let it attempt the automatic repairs before you go manual.

1. Open Settings > System > Troubleshoot > Other troubleshooters.
2. Run the Windows Update troubleshooter and apply all suggested fixes.
3. Restart the laptop, then open Settings > Windows Update and observe whether the page loads without the error.
4. If the error persists instantly, continue — the engine still needs manual help.

### Fix 2: Force-restart the update services

A service stuck in the stopping state will defeat both the troubleshooter and a reboot's fast startup. Stopping the services hard from an elevated prompt and starting them fresh clears that trap.

1. Open Command Prompt as administrator.
2. Run taskkill /f /fi "SERVICES eq wuauserv" to force-kill any wedged update service process.
3. Then run net stop bits, net stop cryptSvc, and net stop msiserver, followed by net start wuauserv, net start bits, net start cryptSvc, and net start msiserver.
4. Open Settings > Windows Update and test.

### Fix 3: Re-register the update engine DLLs

Server execution failed is frequently a COM activation problem in disguise. Re-registering the engine's libraries restores the activation paths Windows uses to launch the update components.

1. In an elevated Command Prompt, run regsvr32 wuapi.dll, regsvr32 wuaueng.dll, regsvr32 wuaueng1.dll, regsvr32 wucltui.dll, regsvr32 wups.dll, regsvr32 wups2.dll, and regsvr32 wuwebv.dll, confirming each dialog.
2. Follow with regsvr32 atl.dll, regsvr32 msxml3.dll, and regsvr32 qmgr.dll for the supporting libraries.
3. Reboot the laptop to let the fresh registrations take effect.
4. Retry Windows Update.

### Fix 4: Clear the SoftwareDistribution cache

If the cache is damaged badly enough, the service can crash while reading it at startup. Clearing it removes that possibility and is harmless — Windows rebuilds the folder on the next scan.

1. In an elevated Command Prompt, run net stop wuauserv and net stop bits.
2. Run ren C:\Windows\SoftwareDistribution SoftwareDistribution.old.
3. Run net start wuauserv and net start bits.
4. Reboot and check for updates.

### Fix 5: Free up disk space

The update engine verifies staging space when it starts. On a nearly full system drive it may abort with this code rather than a clearer disk-space message, so rule this out early.

1. Open Settings > System > Storage and check free space on C: — you want at least 20 GB.
2. Run Disk Cleanup as administrator and remove Temporary files, Windows Update Cleanup, and Delivery Optimization Files.
3. Uninstall large apps you no longer use via Settings > Apps > Installed apps.
4. Empty the Recycle Bin and retry the update.

### Fix 6: Repair system files with DISM and SFC

When the engine's own files are corrupt, only a file-level repair helps. DISM restores the component store from Windows Update or local sources, then SFC fixes protected files against that store.

1. In an elevated Command Prompt, run DISM /Online /Cleanup-Image /RestoreHealth and wait for completion.
2. Then run sfc /scannow.
3. Reboot after both finish.
4. If you need background on the error family, [Microsoft's support hub](https://support.microsoft.com/en-us/windows) documents the servicing tools used here.

### Fix 7: Clean-boot and retry

If a third-party service is hooking the update components at startup, a clean boot isolates it. This is diagnostic: if updates work in a clean boot, some startup program is the culprit.

1. Press Windows + R, type msconfig, and open the Services tab.
2. Tick Hide all Microsoft services, then click Disable all and restart.
3. Test Windows Update in the clean-boot state.
4. If it works, re-enable services in halves to identify the offender, then update or remove that software.

### Fix 8: Perform an in-place repair install

When the engine refuses to start after every targeted repair, the installation itself needs refreshing. An in-place upgrade reinstalls Windows 11 over itself, rebuilding the update stack while keeping files and apps. Grab the installer from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

1. Download the Windows 11 ISO from Microsoft and mount it by double-clicking.
2. Run setup.exe, choose Keep personal files and apps, and let the repair install complete.
3. The process takes 30 to 90 minutes; keep the charger connected.
4. Afterward, Windows Update should open and scan normally.

## Closing

Error 0x80080005 is Windows 11 admitting its update engine would not turn over — and engines that will not turn over need their starter, fuel lines, and spark checked in that order. The DLL re-registration and the forced service restart fix the large majority of cases; the file repairs and the clean boot catch the stubborn remainder. Once the engine starts, let it finish a full update cycle before reinstalling any system utilities, so you know the repair held. The same engine-startup repair for Windows 10 is in our [0x80080005 Windows 10 guide](/articles/how-to-fix-windows-update-error-0x80080005-on-windows-10/).
