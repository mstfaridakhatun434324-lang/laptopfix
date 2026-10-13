---
title: "Stop Your Laptop From Auto-Restarting After a Blue Screen"
slug: how-to-disable-automatic-restart-after-bsod-on-laptop
date: 2026-09-10
categories: ["windows-errors"]
tags: ["bsod", "auto-restart", "windows-11"]
description: "Windows reboots instantly after a blue screen, hiding the error code. Here's how to disable automatic restart so you can actually read it."
thumbnail: "/images/thumbs/how-to-disable-automatic-restart-after-bsod-on-laptop.webp"
faqs:
  - q: "Why does my laptop restart immediately after a blue screen?"
    a: "Windows is configured by default to automatically restart on system failure. It is meant to recover unattended servers quickly, but on a laptop it just hides the stop code you need to diagnose the problem."
  - q: "Does disabling auto-restart fix the blue screen?"
    a: "No — it only stops the reboot so you can read the error code and troubleshoot properly. The underlying cause still needs fixing. Think of it as turning on the lights before you start looking for the problem."
  - q: "What if the laptop crashes before I can change the setting?"
    a: "Use the recovery environment instead. Interrupt the boot three times to reach the blue recovery screen, then go to Troubleshoot > Advanced options > Startup Settings and press F9 to disable automatic restart for that boot."
  - q: "Will the blue screen stay on screen forever after this?"
    a: "Essentially, yes — it will sit there until you hold the power button to shut down. That is the point: it gives you unlimited time to photograph or write down the stop code and the failing file name."
---

There is nothing more frustrating than a blue screen that vanishes in two seconds. Your laptop flashes an error, and before you can read a single word, it reboots — taking the one piece of information you needed with it. That behavior is not a bug; Windows is configured out of the box to restart automatically after a system failure.

Disabling that automatic restart is the single most useful thing you can do when you are chasing a recurring blue screen. It does not fix the crash, but it freezes the error on screen so you can read the stop code, photograph it, and actually diagnose the problem. Without it, you are troubleshooting blind — with it, every crash hands you a clue.

Here is how to do it three different ways, depending on whether Windows still boots.

## Why this happens

- **Windows defaults to "Automatically restart" on system failure.** The setting lives in the Startup and Recovery options and is enabled on every fresh install.
- **The default exists for unattended machines.** Servers benefit from auto-recovery; a laptop you are sitting in front of does not.
- **Fast boot sequences hide the screen.** On modern laptops with fast SSDs, the reboot happens so quickly you may not even see the blue screen at all.
- **Crash dumps still get written either way.** Disabling the restart does not affect dump files — `%SystemRoot%\Minidump` still captures the crash for later analysis.
- **The setting is per-machine, not per-user.** Changing it once applies to the whole system and survives user switches.
- **Some "tune-up" tools re-enable it.** Aggressive system optimizers occasionally flip this setting back to default without telling you.

## How to fix it

Work through these in order, from least to most invasive. You only need one method to succeed — pick whichever matches your situation.

### Fix 1: Disable auto-restart from System Properties

The standard method, and it takes about thirty seconds when Windows still boots.

1. Press `Win + R`, type `sysdm.cpl`, and press **Enter** to open System Properties.
2. Go to the **Advanced** tab and click **Settings** under **Startup and Recovery**.
3. Under **System failure**, uncheck **Automatically restart**.
4. Make sure **Write an event to the system log** is checked — you want the crash recorded.
5. Confirm the **Dump file** path is set to `%SystemRoot%\MEMORY.DMP` so full dumps are available if you ever need them.
6. Click **OK** twice. The next blue screen will stay on screen until you power off manually.

### Fix 2: Disable it from the recovery environment

Use this when crashes happen so early or so often that you cannot reach the desktop.

1. Interrupt the boot process: hold the **power button** to force a shutdown while Windows is loading, three times in a row.
2. On the fourth boot you will land on the blue **Choose an option** screen — select **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. When the numbered menu appears, press **F9** (or **9**) for **Disable automatic restart after failure**.
4. Windows boots with auto-restart disabled for this session, so the next crash stays visible.
5. Note that this is temporary — once you can reach the desktop, apply Fix 1 to make it permanent. If you cannot get into Safe Mode either, our guide on [Windows 11 Safe Mode not working on Lenovo laptops](/articles/fix-windows-11-safe-mode-not-working-on-lenovo-laptop/) has more recovery options.

### Fix 3: Disable it from the command line

Handy when you prefer the terminal, or when you are helping someone remotely.

1. Open an elevated Command Prompt (**Start** > type `cmd` > right-click **Command Prompt** > **Run as administrator**).
2. Run: `wmic recoveros set AutoReboot = False`
3. You should see a confirmation that the property was updated.
4. Alternatively, use the registry directly: `reg add "HKLM\SYSTEM\CurrentControlSet\Control\CrashControl" /v AutoReboot /t REG_DWORD /d 0 /f`
5. Restart the laptop so the change takes full effect.

### Fix 4: Read the stop code properly once it stays on screen

Now that the blue screen stays put, capture the information correctly.

1. When the next crash happens, photograph the full screen with your phone — include the stop code and any file name shown (like `ntoskrnl.exe` or a `.sys` file).
2. Write down the exact stop code text, for example `KERNEL_SECURITY_CHECK_FAILURE` or `MEMORY_MANAGEMENT`.
3. Note what you were doing when it crashed — gaming, waking from sleep, plugging in a device — since the trigger matters as much as the code.
4. Search our [blue screen after Windows 11 update guide](/articles/how-to-fix-blue-screen-after-windows-11-update-reddit/) or the specific stop-code article matching what you photographed.

### Fix 5: Check the crash dump after rebooting

With auto-restart off, you power down manually — the dump file is still saved for deeper analysis.

1. After the crash, hold the **power button** to shut down, then boot normally.
2. Open `%SystemRoot%\Minidump` and confirm a new `.dmp` file was created at the crash time.
3. Open it in **WinDbg Preview** (free from the Microsoft Store) and run `!analyze -v`.
4. The `MODULE_NAME` line usually names the exact driver that crashed.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official blue-screen troubleshooting flow if you want the full reference.

### Fix 6: Re-enable auto-restart after you fix the crash

Once the underlying problem is solved, most people prefer the default behavior back.

1. Repeat Fix 1 but **check** the **Automatically restart** box this time.
2. Click **OK** twice and restart.
3. Some people leave it disabled permanently so they never miss a stop code again — that is a reasonable choice too, especially on a laptop you use daily.

## Closing

Disabling automatic restart does not fix a single blue screen — but it turns every future crash from a mystery into a readable error message, and that changes everything about troubleshooting. Take the thirty seconds to flip the setting, photograph your next stop code, and then go fix the actual problem with real information instead of guesses.
