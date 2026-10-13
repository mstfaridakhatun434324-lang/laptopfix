---
title: "\"Your PC Ran Into a Problem\": What to Do on Windows 11"
slug: how-to-fix-your-pc-ran-into-a-problem-on-windows-11
date: 2026-09-01
categories: ["windows-errors"]
tags: ["bsod", "stop code", "windows 11"]
description: "Stuck on the \"Your PC ran into a problem\" blue screen on Windows 11? Here's what that screen means and the exact steps to get past it."
thumbnail: "/images/thumbs/how-to-fix-your-pc-ran-into-a-problem-on-windows-11.webp"
faqs:
  - q: "What does \"Your PC ran into a problem\" mean?"
    a: "It's Windows 11's generic blue screen message, shown whenever the kernel hits a fatal error it can't recover from. The real diagnosis is the stop code at the bottom (like MEMORY_MANAGEMENT or DRIVER_IRQL_NOT_LESS_OR_EQUAL). Photograph that code — it determines which fix applies."
  - q: "Will I lose my files from this blue screen?"
    a: "The blue screen itself doesn't delete files. Your data is still on the drive. The risk comes only if you jump to drastic measures like a clean install without backing up, or if the underlying cause is a failing drive. Fix the cause first."
  - q: "Why does it restart and then show the same screen again?"
    a: "Because the trigger — a bad driver, corrupt system file, or failing hardware — is still there. Windows reboots, hits the same condition, and crashes again. You need to break the loop from the recovery environment or Safe Mode, where the bad component doesn't load."
  - q: "How do I stop it from restarting too fast to read the code?"
    a: "In the recovery environment, open a command prompt and run wmic recoveros set AutoReboot = False, or in Windows go to System Properties > Advanced > Startup and Recovery settings and uncheck Automatically restart. Then the blue screen stays put so you can note the stop code."
---

The "Your PC ran into a problem and needs to restart" screen is Windows 11's way of saying the kernel hit something it couldn't survive. It looks alarming, but the screen itself is just a messenger — the real information is the stop code printed near the bottom, and the fix depends on what that code is.

If your laptop is looping on this screen, don't keep letting it crash. Every restart lands on the same broken state. Instead, interrupt the cycle deliberately and work through the fixes below, starting with whatever stop code you can see.

## Why this happens

- **Faulty or incompatible device driver**: The most common cause. A driver accesses memory it shouldn't, mishandles hardware, or conflicts after a Windows update.
- **Failing RAM**: Bad memory corrupts whatever it touches — drivers, kernel data, file caches — producing random-looking crashes with changing stop codes.
- **Corrupted system files**: Damaged Windows core files from a bad update, forced shutdown, or malware can crash the kernel on every boot.
- **Failing storage drive**: A dying SSD or hard drive corrupts data as it's read, so Windows crashes on files that look fine but aren't.
- **Overheating or unstable hardware**: Thermal shutdowns and unstable power delivery can present as blue screens, especially under load.
- **Recent Windows update gone wrong**: A botched cumulative or feature update can leave the system in a half-migrated state that crashes on boot.

## How to fix it

Work through these in order — the goal is to identify the stop code, then attack the most likely cause.

### Fix 1: Read the stop code and note when it happens

Everything downstream depends on this information. Don't skip it.

1. When the blue screen appears, photograph it with your phone — capture the full stop code (e.g., `MEMORY_MANAGEMENT`, `SYSTEM_SERVICE_EXCEPTION`) and any driver filename shown.
2. Note the pattern: does it crash on boot, on login, when opening a specific app, or randomly?
3. If it reboots too fast to read, that's expected — Fix 3 shows how to slow it down.
4. If you already know the code, jump to the matching guide: our [general blue screen of death walkthrough](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the most common codes with targeted fixes.

### Fix 2: Boot into Safe Mode

Safe Mode loads only essential drivers. If the laptop is stable there, a third-party driver or startup program is the culprit.

1. Force the recovery environment: power on the laptop, and as soon as the Windows logo appears, hold the power button to force it off. Repeat three times.
2. On the fourth boot, Windows enters **Automatic Repair**. Click **Advanced options**.
3. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
4. Press **4** for Safe Mode (or **5** for Safe Mode with Networking).
5. If it's stable in Safe Mode, the next fixes apply. If it crashes even in Safe Mode, suspect hardware or core system corruption — jump to Fix 6.
6. Our detailed walkthrough on [booting Windows 11 into Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) covers alternative methods if this one doesn't work.

### Fix 3: Disable automatic restart to capture the error

Windows reboots immediately after a crash by default. Turn that off so you can actually read the screen.

1. In Safe Mode (or normal Windows if you can reach it), press **Win + R**, type `sysdm.cpl`, and press Enter.
2. Go to the **Advanced** tab and click **Settings** under **Startup and Recovery**.
3. Uncheck **Automatically restart** and click **OK**.
4. The next blue screen will stay on screen until you restart manually — photograph the stop code.
5. From the recovery environment command prompt, you can do the same with: `wmic recoveros set AutoReboot = False`.

Microsoft documents this and other recovery options on the [Windows support hub](https://support.microsoft.com/en-us/windows) if you need the official walkthrough.

### Fix 4: Uninstall the most recent update or driver

If crashes started after an update, that update is suspect number one.

1. In Safe Mode, open **Settings** > **Windows Update** > **Update history** > **Uninstall updates**.
2. Remove the most recent cumulative or driver update, then restart.
3. If the problem was a driver, open **Device Manager** (**Win + X** > **Device Manager**), find recently updated devices, open **Properties** > **Driver** tab, and click **Roll Back Driver**.
4. To stop Windows from reinstalling a bad driver update, download the **Show or hide updates** troubleshooter (`wushowhide.diagcab`) from Microsoft and hide that update.
5. Retest in normal mode. If the crashes followed a feature update, see our guide on [blue screens after a Windows 11 update](/articles/blue-screen-after-windows-11-update-troubleshooting/).

### Fix 5: Run system file and image repairs

Corrupted system files crash the kernel. Repair them from Safe Mode or the recovery command prompt.

1. Open an elevated Command Prompt: **Win + S**, type `cmd`, right-click **Command Prompt**, choose **Run as administrator**.
2. Run `sfc /scannow` and let it complete — this repairs protected Windows files.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to fix the component store that SFC relies on.
4. Restart and test. If SFC finds corruption it can't fix, the DISM repair usually resolves the underlying store damage — run SFC once more afterward.
5. If both fail, an in-place upgrade (repair install) from [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) reinstalls Windows while keeping files and apps.

### Fix 6: Test memory and storage hardware

If software fixes change nothing — especially if the stop code keeps changing — test the hardware.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**. Any error means bad RAM.
2. For the drive, open an elevated Command Prompt and run `chkdsk C: /f /r` (schedule it if prompted, then restart).
3. Check drive health with your manufacturer's tool — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) all provide diagnostics — or read SMART data with CrystalDiskInfo.
4. Reseat RAM and storage if your laptop allows access; loose modules cause intermittent crashes. Our guide on [disabling automatic restart after a BSOD in Windows 11 24H2](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) pairs well with hardware diagnosis since you'll want the screen to stay put.

### Fix 7: Clean-boot to isolate software conflicts

If Safe Mode is stable but normal boot crashes, a startup program or service is involved.

1. In Safe Mode with Networking, press **Win + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, check **Hide all Microsoft services**, then click **Disable all**.
3. On the **Startup** tab, click **Open Task Manager** and disable every startup item.
4. Restart into normal mode. If it's stable, re-enable items in halves until the crash returns — the last batch contains the culprit.
5. Common offenders: third-party antivirus, VPN clients, RGB/fan control utilities, and disk-encryption tools.

## Closing

"Your PC ran into a problem" is never the diagnosis — it's the announcement. The stop code, the timing, and whether Safe Mode is stable will point you at the real cause, and from there it's a methodical process: roll back what changed recently, repair system files, then test hardware. Most of these loops end at a bad driver or a bad update, both of which are fully fixable without losing a single file.
