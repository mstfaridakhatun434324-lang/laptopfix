---
title: "How to Fix Windows 11 Stuck on the Restarting Screen"
slug: how-do-i-fix-windows-11-stuck-on-restarting-screen
date: 2026-09-09
categories: ["windows-errors"]
tags: ["windows 11", "stuck restart", "boot issues"]
description: "Windows 11 stuck on the restarting screen for ages? Learn how to safely break the loop and stop it happening again with these tested fixes."
thumbnail: "/images/thumbs/how-do-i-fix-windows-11-stuck-on-restarting-screen.webp"
faqs:
  - q: "How long should a Windows 11 restart take?"
    a: "A normal restart takes one to three minutes on an SSD laptop. If the Restarting screen spins for more than ten to fifteen minutes, something is stuck. Waiting longer rarely helps; you are better off forcing a shutdown and diagnosing the cause."
  - q: "Is it safe to force shut down when Windows is stuck restarting?"
    a: "Yes, if it has been spinning for a long time. A restart in progress is not writing critical files the way an update is, so holding the power button for ten seconds is reasonably safe. The bigger risk is the underlying problem, not the forced shutdown itself."
  - q: "Why does my laptop get stuck on restart after every update?"
    a: "Usually a driver is hanging during shutdown, often a network, display, or power management driver. Fast Startup can also make restarts behave badly. Updating drivers and disabling Fast Startup fixes most recurring cases."
  - q: "Could a peripheral cause the restarting screen to hang?"
    a: "Yes. External drives, USB hubs, printers, and docking stations can all block the shutdown sequence. Disconnect everything except the charger, keyboard, and mouse before restarting to test this."
---

The blue screen says "Restarting" with those friendly spinning dots, and twenty minutes later it is still saying "Restarting." You cannot click anything, you cannot see what is happening, and you are stuck wondering whether to touch the power button. It is one of the most common Windows 11 complaints on laptops, and it is fixable.

The spinning dots mean Windows is trying to shut down services and drivers but one of them is refusing to quit. Your job is to identify the stuck piece and either update it, bypass it, or work around it. Start with the safe interrupt below, then apply the permanent fixes.

## Why this happens

- **A driver hangs during shutdown.** Network, display, audio, or power drivers can refuse to unload, and Windows waits on them indefinitely.
- **Fast Startup conflicts.** This hybrid shutdown feature saves the kernel session to disk and can corrupt the restart sequence on some laptops.
- **Pending Windows updates.** An update that downloads or stages during shutdown can wedge the restart process, especially on slow connections.
- **Corrupted system files.** Damaged files in the shutdown path mean Windows cannot complete the sequence no matter how long it waits.
- **Peripherals blocking shutdown.** USB drives, printers, and docks can send signals that keep the system from powering off cleanly.
- **Third-party software.** Antivirus, backup tools, and system utilities with deep hooks sometimes intercept shutdown and stall it.
- **Disk errors.** A drive with bad sectors or filesystem damage can stall the writes that happen during shutdown.
- **Broken power plans.** A corrupted power plan or a misbehaving battery driver on laptops can confuse the shutdown sequence, especially after major Windows upgrades that migrate old plans incorrectly.

## How to fix it

Work through these in order, starting with the quickest fixes first.

### Fix 1: Force shut down and disconnect peripherals

First, break the loop safely.

1. Hold the **power button** for about ten seconds until the laptop powers off completely.
2. Unplug every USB device, including external drives, printers, hubs, and docks. Leave only the charger connected.
3. Wait thirty seconds, then power the laptop back on.
4. If it boots normally, one of those peripherals was the culprit. Reconnect them one at a time, restarting between each, to find the offender.

### Fix 2: Disable Fast Startup

Fast Startup is the single most common cause of stuck restarts on laptops.

1. Press **Windows key + R**, type `powercfg.cpl`, and press Enter.
2. Click **Choose what the power buttons do** on the left.
3. Click **Change settings that are currently unavailable** at the top.
4. Uncheck **Turn on fast startup (recommended)** under Shutdown settings.
5. Click **Save changes** and restart the laptop to test.

### Fix 3: Run the power troubleshooter

Windows can detect shutdown and power issues automatically.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Click **Run** next to **Power**.
3. Apply any recommended fixes and restart.

### Fix 4: Update the drivers that hang most often

Display, network, and chipset drivers are the top offenders.

1. Open **Device Manager** with **Windows key + X**.
2. Expand **Display adapters** and **Network adapters**.
3. Right-click each device, choose **Update driver** > **Search automatically for drivers**.
4. For a deeper fix, download fresh chipset and power management drivers from your laptop maker's support page, such as [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), or [Lenovo support](https://support.lenovo.com/us/en/).
5. Restart after updating to confirm the loop is gone.

### Fix 5: Check for disk and system file errors

1. Open an elevated Terminal with **Windows key + X** > **Terminal (Admin)**.
2. Run `chkdsk C: /f /r`. Type **Y** when asked to schedule it, then restart so the scan runs before Windows loads.
3. After that scan completes, run `sfc /scannow` in the same terminal.
4. If SFC cannot fix everything, run `DISM /Online /Cleanup-Image /RestoreHealth` and repeat the SFC scan.

### Fix 6: Uninstall recently added software

If the stuck restarts began after installing something, that program is suspect.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Sort by **Date installed** to see what changed recently.
3. Uninstall any antivirus trial, system cleaner, backup tool, or VPN added around the time the problem started.
4. Restart the laptop twice to confirm normal behavior returns.

### Fix 7: Shorten how long Windows waits on stuck services

You can tell Windows to stop waiting so long on services that refuse to close.

1. Press **Windows key + R**, type `regedit`, and press Enter. Click **Yes** on the prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control`.
3. Double-click **WaitToKillServiceTimeout** on the right. If it does not exist, right-click empty space, choose **New** > **String Value**, and name it exactly that.
4. Set the value to `5000` (five seconds) and click **OK**.
5. Close the Registry Editor and restart to test. Do not set this below 2000, or Windows may kill services too aggressively during normal shutdowns.

### Fix 8: Boot into Safe Mode to isolate the cause

Safe Mode skips most drivers and startup software.

1. Hold **Shift** and click **Power** > **Restart** to open recovery.
2. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. Press **4** for Safe Mode.
4. Restart from Safe Mode. If the restart completes quickly there, a driver or startup program is the problem. Use **msconfig** to disable startup items selectively until you find it.
5. Our Safe Mode guide at [how to boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) has the full steps, and for the general fix set see [Windows 11 stuck on restarting screen fix](/articles/windows-11-stuck-on-restarting-screen-fix/).

Microsoft's official guidance for restart and shutdown problems lives on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

## Closing

A laptop stuck on the Restarting screen is annoying, but it is rarely serious. In nine cases out of ten, disconnecting peripherals or disabling Fast Startup ends the loop immediately, and the registry tweak in Fix 7 makes Windows far less patient with hung services in the future. The deeper fixes are about making sure it never comes back: updated drivers, a clean disk, and no aggressive software interfering with shutdown. Keep Windows and your drivers current, avoid force-closing driver installers, and those spinning dots will stay brief. If the problem ever returns after a specific update, uninstalling that update usually restores normal restarts while you wait for a corrected version.
