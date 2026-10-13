---
title: "Troubleshoot Windows 11 Stuck on the Restarting Screen"
slug: troubleshoot-windows-11-stuck-on-restarting-screen
date: 2026-09-16
categories: ["windows-errors"]
tags: ["windows 11", "stuck restart", "troubleshooting"]
description: "A deeper troubleshooting guide for Windows 11 laptops that hang on the Restarting screen: diagnostics, logs, and permanent fixes that end the loop."
thumbnail: "/images/thumbs/troubleshoot-windows-11-stuck-on-restarting-screen.webp"
faqs:
  - q: "What is the difference between a restart and a shutdown on Windows 11?"
    a: "A shutdown with Fast Startup saves the kernel session to disk, while a restart always performs a full shutdown and fresh boot. That is why restart problems often disappear when Fast Startup is disabled: both paths start behaving the same way."
  - q: "How do I find which driver hangs during restart?"
    a: "Check Event Viewer under Windows Logs, System for errors timestamped at your last restart. Driver names appear in the details. You can also enable verbose shutdown messages through Group Policy to see exactly which service stalls."
  - q: "Can I make Windows show what it is doing during restart?"
    a: "Yes. In the Local Group Policy Editor, go to Computer Configuration, Administrative Templates, System, and enable Verbose vs normal status messages. Windows then names each service as it shuts down, making the stuck one obvious."
  - q: "Will a clean install fix a stuck restarting screen?"
    a: "Almost certainly, but it is overkill as a first step. A clean install removes every driver and program, so whatever was hanging goes with them. Try the targeted fixes first and keep the reinstall as your last resort."
---

If your Windows 11 laptop hangs on the Restarting screen regularly, you need more than a one-time escape: you need to find the actual cause and remove it. This guide is the deeper troubleshooting pass. It covers how to break the loop safely, how to read the logs that name the culprit, and the permanent fixes that stop the spinning dots from ever overstaying their welcome again.

Restart hangs are almost never random. Something in the shutdown sequence, a driver, a service, or a peripheral, is failing to quit, and Windows waits on it politely forever. Your goal is to identify that something.

## Why this happens

- **A service refuses to stop.** Background services from third-party software can ignore the shutdown signal entirely.
- **Driver unload hangs.** Display, network, and storage drivers sometimes wedge while releasing hardware.
- **Fast Startup corruption.** The hibernation-style kernel save can become damaged and poison every subsequent restart.
- **Pending file operations.** Windows Update staging or a large pending file move can block shutdown for far longer than expected.
- **Peripheral handshakes.** USB devices and docks that renegotiate power during shutdown can stall the whole sequence.
- **Corrupted power settings.** Damaged power plans or battery driver states confuse the shutdown path on laptops.
- **Disk errors.** Filesystem damage forces Windows into long repair waits during shutdown that look like a hang.

## How to fix it

Work through these in order, starting with the quickest fixes first.

### Fix 1: Break the loop and test a minimal restart

1. Hold the **power button** for ten seconds to force the laptop off.
2. Disconnect all USB devices and the dock, leaving only the charger.
3. Power on, then immediately restart from **Start** > **Power** > **Restart**.
4. If this clean restart works, reconnect devices one at a time with a restart between each to identify the blocker.

### Fix 2: Disable Fast Startup permanently

1. Press **Windows key + R**, type `powercfg.cpl`, and press Enter.
2. Click **Choose what the power buttons do**, then **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and save.
4. Restart twice to confirm the hang is gone. This single change resolves the majority of recurring cases.

### Fix 3: Enable verbose shutdown messages

This makes Windows tell you exactly where it stalls.

1. Press **Windows key + R**, type `gpedit.msc`, and press Enter. On Home edition, skip to the registry step below.
2. Go to **Computer Configuration** > **Administrative Templates** > **System**.
3. Double-click **Verbose vs normal status messages**, set it to **Enabled**, and click **OK**.
4. On Home edition, open `regedit`, go to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`, and create a DWORD named **VerboseStatus** set to `1`.
5. Restart. Windows now names each service as it shuts down, and the last one shown before the hang is your culprit.

### Fix 4: Read the shutdown logs in Event Viewer

1. Press **Windows key + X** and open **Event Viewer**.
2. Go to **Windows Logs** > **System**.
3. Click **Filter Current Log** and check **Critical**, **Error**, and **Warning**.
4. Look for entries timestamped at your last failed restart. Driver and service names in these entries point directly at the cause.
5. Search the web for the exact error text only after you have the name; guessing from symptoms wastes time.

### Fix 5: Update the drivers named by the logs

1. Whatever driver the logs implicate, update it first. Display and network drivers are the usual winners.
2. Get manufacturer drivers rather than relying on Windows Update: [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), or [Lenovo support](https://support.lenovo.com/us/en/).
3. If the driver is already current, try the previous version. Sometimes the newest release is the broken one.

### Fix 6: Clean boot to isolate software

1. Press **Windows key + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, check **Hide all Microsoft services**, then click **Disable all**.
3. On the **Startup** tab, click **Open Task Manager** and disable every startup item.
4. Restart. If restarts are clean now, re-enable services and startup items in small groups until the hang returns. The last group contains your culprit. When you find it, either update the program to a version that shuts down cleanly or replace it with an alternative that does.

### Fix 7: Repair the disk and system files

1. In an elevated Terminal, run `chkdsk C: /f /r`, type **Y** when prompted, and restart so the scan runs.
2. Afterward, run `sfc /scannow` in the same elevated Terminal.
3. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` if needed.

### Fix 8: Refresh the power plan and reset Windows if needed

1. In an elevated Terminal, run `powercfg -restoredefaultschemes` to rebuild all power plans from scratch.
2. Restart and test. Corrupted power plans are a real but underdiagnosed cause of laptop restart hangs.
3. If everything else fails, **Settings** > **System** > **Recovery** > **Reset this PC** with **Keep my files** gives you a clean slate.
4. Related guides: [Windows 11 stuck on restarting screen fix](/articles/windows-11-stuck-on-restarting-screen-fix/) and [Srttrail.txt blue screen error](/articles/how-to-fix-srttrail-txt-blue-screen-error-after-windows-11-update/). Microsoft's official help is on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

## Closing

Troubleshooting a stuck Restarting screen is detective work, and the logs are your witnesses. Break the loop, disable Fast Startup, turn on verbose messages, and read Event Viewer, and the culprit almost always introduces itself. Once you know the name, the fix is usually a driver update or a software removal away. Keep the system lean, keep drivers current, and restarts will go back to taking seconds instead of forever. And the next time a restart lingers past a couple of minutes, you will know exactly where to look instead of just staring at the spinning dots, which is the whole point of having done this troubleshooting once and written down what you found for next time.
