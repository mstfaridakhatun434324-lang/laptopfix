---
title: "Stuck on the Restarting Screen? Fixes Windows Users Swear By"
slug: how-to-fix-windows-11-stuck-on-restarting-screen-reddit
date: 2026-09-09
categories: ["windows-errors"]
tags: ["windows-11", "restarting", "stuck", "troubleshooting"]
description: "Windows 11 stuck on the Restarting screen forever? Force a safe shutdown and fix the stuck service, driver, or update causing it."
thumbnail: "/images/thumbs/how-to-fix-windows-11-stuck-on-restarting-screen-reddit.webp"
faqs:
  - q: "Why does Windows 11 get stuck on the Restarting screen?"
    a: "A process or driver refuses to shut down, so Windows waits for it indefinitely. Common culprits include a hung Windows Update, a misbehaving driver, a background program that will not terminate, and fast startup preserving a bad system state. The screen spins because Windows is politely waiting for something that will never finish."
  - q: "Is it safe to force shut down when stuck on Restarting?"
    a: "Yes, holding the power button for 5 to 10 seconds is safe in this situation. Windows has already closed your programs and saved what it could; the hang is in the final shutdown phase. Forced shutdowns are only risky if the drive light shows heavy activity from an update actively writing, so wait a few minutes first if an update was installing."
  - q: "How long should I wait before forcing a shutdown?"
    a: "Give it 10 to 15 minutes. Some restarts legitimately take a while, especially when updates are finalizing. If the spinner is still going after 15 minutes with no drive activity, it is genuinely stuck and a forced shutdown is the right move."
  - q: "Will this keep happening every time I restart?"
    a: "It can, if the underlying cause is not fixed. A hung service or driver will hang the next restart too. Work through the fixes below after you get back in, especially disabling fast startup and updating drivers, to break the cycle."
---

The little spinning dots. "Restarting." Five minutes pass. Ten. The dots keep spinning, and your laptop is going nowhere. Windows 11 stuck on the Restarting screen is one of the most common hangs in Windows, and it is almost always a software problem: some process or driver that refuses to die, leaving Windows waiting forever.

The immediate fix is simple, but the permanent fix requires finding what hung. This guide covers both: how to get unstuck right now, and how to stop it from happening again. The good news is that the cause is almost always identifiable, and the fixes below are ordered so the most common culprits get addressed first.

## Why this happens

- **A hung background process.** A program that ignores the shutdown signal keeps Windows waiting indefinitely.
- **A misbehaving driver.** Drivers that do not handle power transitions correctly stall the restart sequence.
- **Windows Update finalizing.** Updates sometimes take far longer than expected during restart.
- **Fast startup preserving bad state.** The hybrid shutdown can carry a corrupted driver state from one boot to the next.
- **Corrupted system files.** Damage to shutdown-related components breaks the restart sequence.
- **External devices.** USB drives, docks, and peripherals can stall the restart while Windows waits on them.
- **Disk errors.** A struggling drive slows every phase of shutdown and restart.

## How to fix it

Work through these in order, testing for stability after each fix before moving on.

### Fix 1: Force a shutdown and restart cleanly

Get unstuck first; diagnose second.

1. Press and hold the power button for 5 to 10 seconds until the laptop powers off.
2. Unplug all USB devices, docks, and external drives. A misbehaving USB device is one of the most common yet overlooked causes of restart hangs.
3. Wait 30 seconds, then power on.
4. If Windows boots normally, continue with the fixes below to prevent recurrence.
5. If it hangs again immediately, boot into Safe Mode (interrupt boot three times to reach recovery) and continue from there. In Safe Mode, minimal drivers load, so a successful Safe Mode boot points squarely at a third-party driver or startup program.

### Fix 2: Disable fast startup

Fast startup is a leading cause of repeat restart hangs.

1. Open **Control Panel** then **Hardware and Sound** then **Power Options**.
2. Click **Choose what the power buttons do**.
3. Click **Change settings that are currently unavailable**. If the option is grayed out, disable hibernation first by running `powercfg /h off` in an elevated Command Prompt.
4. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
5. Restart normally to test; the restart will be a true full restart now.

### Fix 3: Run the Windows Update troubleshooter and install updates

A stuck update component often causes the hang.

1. Open **Settings** then **System** then **Troubleshoot** then **Other troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply its fixes.
3. Go to **Settings** then **Windows Update** and install all pending updates. Do not skip optional driver updates here if any are offered for your chipset or storage controller.
4. Restart and check whether the hang is gone.

### Fix 4: Update drivers, especially chipset and storage

Drivers that mishandle power transitions stall restarts.

1. Press **Win + X** and open **Device Manager**.
2. Update drivers for **storage controllers**, **system devices** (chipset), and **display adapters**.
3. Get the latest versions from your laptop maker's support site rather than relying solely on Windows Update.
4. Restart and test.

### Fix 5: Find the hanging process with Event Viewer

Identify what refused to shut down.

1. After booting, open **Event Viewer** (**Win + X**).
2. Go to **Windows Logs** then **System** and filter for events around the time of the hang.
3. Look for warnings about applications or services blocking shutdown.
4. Uninstall, update, or disable the identified program. Pay special attention to backup tools, cloud sync clients, and remote desktop software, which are notorious for ignoring shutdown requests.
5. For services, open `services.msc` and set the offending service to **Manual** if you do not need it at boot.

### Fix 6: Run SFC and DISM

Repair damaged shutdown components.

1. Open **Terminal (Admin)** with **Win + X**.
2. Run `sfc /scannow` and let it finish.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` if needed.
4. Run `sfc /scannow` again to confirm.
5. Restart and test.

### Fix 7: Check the drive health

A failing drive makes every shutdown slow and unreliable.

1. Open **Terminal (Admin)** and run `chkdsk C: /f`.
2. Approve the reboot scan if asked and let it complete.
3. Check SMART status with your drive maker's diagnostic tool.
4. If the drive is failing, back up immediately and replace it.
5. A healthy drive rules out the slowest variable in the restart chain.

### Fix 8: Reset Windows if hangs persist

When the installation is damaged, a fresh start ends the cycle.

1. Open **Settings** then **System** then **Recovery** and click **Reset PC**.
2. Choose **Keep my files**.
3. If hangs continue, back up and choose **Remove everything**.
4. After reinstalling, update drivers from the vendor before installing other software.

If your restart problem involves a full boot loop rather than a hang, see our [SrtTrail.txt blue screen guide](/articles/how-to-fix-srttrail-txt-blue-screen-error-on-windows-11/), and for update-related restart issues, the [Windows 11 install error 0x80070002](/articles/how-to-fix-windows-11-install-error-0x80070002-youtube/) walkthrough covers the update side. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) also documents recovery options for machines that will not boot.

## Closing

A Windows 11 machine stuck on "Restarting" is Windows being too polite to a process that will never finish. Force the shutdown, disable fast startup, and hunt down the hanging driver or service with Event Viewer. The hang is a symptom with a specific cause, and once you remove that cause, restarts go back to taking seconds instead of forever. Keep fast startup off permanently if your machine is prone to this; the few seconds of slower boot are a fair trade for reliable restarts.
