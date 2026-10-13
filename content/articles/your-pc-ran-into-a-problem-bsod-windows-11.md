---
title: "'Your PC Ran Into a Problem' on Windows 11: How to Fix It"
slug: your-pc-ran-into-a-problem-bsod-windows-11
date: 2026-10-03
categories: ["windows-errors"]
tags: ["blue screen", "windows 11", "troubleshooting"]
description: "Seeing 'Your PC ran into a problem' on Windows 11? Stop the auto-restart to read the stop code, then fix drivers, updates, and system files."
thumbnail: "/images/thumbs/your-pc-ran-into-a-problem-bsod-windows-11.webp"
faqs:
  - q: "What does 'Your PC ran into a problem' mean?"
    a: "It's the friendly face of the blue screen of death. Windows hit an error it couldn't recover from and restarted to protect itself. The screen also shows a stop code (like DRIVER_IRQL_NOT_LESS_OR_EQUAL) and sometimes a file name — that small text at the bottom is the actual diagnosis, and everything below starts from reading it."
  - q: "Why does my PC restart so fast I can't read the error?"
    a: "Windows is set to restart automatically after a system failure, which is unhelpful when you're trying to diagnose the problem. You can disable that in Startup and Recovery settings so the blue screen stays visible until you restart manually. Our guide on disabling automatic restart walks through the exact clicks."
  - q: "Will I lose unsaved work when this happens?"
    a: "Anything unsaved at the moment of the crash is gone — there's no recovering it. That's the painful reality of blue screens. The practical takeaway is to enable autosave in the apps you care about (Office, Adobe, browsers with session restore) so the next crash costs you minutes instead of hours."
  - q: "How do I stop it from happening again?"
    a: "Find the pattern: note the stop code, what you were doing, and whether it follows an update. Then work the standard sequence — update drivers, remove the recent update if timing matches, repair system files, and test memory. Random blue screens with no pattern usually mean a driver or RAM issue, both fixable with the steps below."
---

"Your PC ran into a problem and needs to restart" — that sad-face screen is Windows 11's way of saying something broke badly enough to stop everything. It's alarming the first time, but it's also Windows handling the failure correctly rather than letting corruption spread.

The key to fixing it is the small print: the stop code at the bottom of the screen. That code turns a generic crash into a specific repair job. Here's the full process, from reading the error to fixing it for good.

## Why this happens

- **Faulty or outdated driver.** The single most common cause — a driver crashing in kernel mode.
- **Bad Windows update.** An update that conflicts with your drivers or installs badly.
- **Failing RAM.** Memory errors crashing whatever happens to be running.
- **Overheating.** Thermal shutdowns disguised as blue screens under load.
- **Corrupted system files.** Damaged Windows components failing at runtime.
- **New hardware or peripherals.** Fresh devices with buggy drivers.
- **Disk errors.** Corruption in critical system files on a failing drive.
- **Power interruptions.** An unstable charger or loose battery connection causing brownouts mid-operation.

## How to fix it

Work through these in order, from Fix 1 onward, and stop as soon as the crashes stop.

### Fix 1: Stop the auto-restart so you can read the stop code

You can't fix what you can't see. Make the blue screen stay put.

1. Press **Win + R**, type `sysdm.cpl`, and press Enter.
2. Go to the **Advanced** tab and click **Settings** under **Startup and Recovery**.
3. Uncheck **Automatically restart** and click **OK**.
4. The next crash will leave the blue screen visible — photograph it, noting the stop code and any file name.
5. Our [guide to disabling auto-restart](/articles/how-to-disable-automatic-restart-after-bsod-on-windows-11/) has screenshots if you want them.

### Fix 2: Boot into Safe Mode and assess

Safe Mode strips Windows to the essentials, which tells you whether third-party software is involved.

1. Hold **Shift** while clicking **Restart** from the login screen, or interrupt boot three times.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4**.
3. If Safe Mode is stable, a third-party driver or program is your culprit — continue with the driver fixes below.
4. If Safe Mode crashes too, suspect Windows system files or hardware — jump to Fix 5.
5. Either way, note what you observe; it narrows everything that follows.

### Fix 3: Update your drivers

Cover the drivers responsible for the overwhelming majority of these crashes.

1. Press **Win + X** and open **Device Manager**.
2. Update display, network, audio, and storage controller drivers via **Update driver > Search automatically for drivers**.
3. Install the chipset package from your laptop maker's support page.
4. For the GPU, do a proper clean install rather than an express update.
5. Restart and use the laptop normally for a few days — intermittent crashes need time to prove they're gone.

### Fix 4: Uninstall the latest Windows update

If the crashes started within days of an update, remove it as a test.

1. Open **Settings > Windows Update > Update history > Uninstall updates**.
2. Remove the most recent quality update and restart.
3. Test thoroughly with your normal workload.
4. If stability returns, pause updates for one to two weeks while the driver vendors catch up.
5. Check the laptop maker's site during the pause — updated drivers often appear quickly after a breaking Windows update.

### Fix 5: Repair system files and check the disk

Fix corrupted Windows components and rule out disk damage.

1. Open **Terminal (Admin)** from the **Win + X** menu.
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `chkdsk C: /f` — schedule it with `Y` and restart if prompted.
4. After booting, run SFC once more to confirm a clean pass.
5. If CHKDSK keeps finding new errors, back up your data — the drive is failing.

### Fix 6: Test your memory and temperatures

Hardware causes hide behind identical blue screens, so check them.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. Check results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
3. Monitor temperatures with HWMonitor during heavy use — sustained CPU/GPU temps above 90 degrees Celsius on a laptop need attention.
4. Clean dust from vents and verify the laptop sits on a hard, flat surface.
5. Replace any failing RAM; no software fix exists for bad memory.

### Fix 7: Roll back with System Restore

When the crash started recently and you have a restore point, this is the fastest resolution.

1. Press **Win + S**, type `Create a restore point`, and open it.
2. Click **System Restore** and choose a point from before the crashes.
3. Review affected programs, finish the wizard, and let it restart uninterrupted.
4. Verify stability for a few days.
5. Enable System Protection afterward if it was off — future-you will be grateful.

### Fix 8: Reset Windows for a clean foundation

The last software resort before suspecting hardware failure.

1. Back up your files.
2. Go to **Settings > System > Recovery > Reset PC**.
3. Choose **Keep my files** and use **Cloud download** for a pristine copy.
4. After setup, install drivers only from your laptop maker's site, then test before adding other software.
5. If blue screens persist on a clean install with updated drivers, you're looking at failing hardware — usually RAM or the drive — and it's time for diagnostics or service.

## Closing

"Your PC ran into a problem" is the start of the diagnosis, not the end of it. Read the stop code, work the driver and update angles first, then verify the hardware — and keep notes on what you change so you can trace back if a later fix makes things worse. That order solves nearly every case. For crashes with a specific stop code, our [blue screen of death guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) goes deeper, and Microsoft's [official troubleshooting page](https://support.microsoft.com/en-us/windows) covers the edge cases.
