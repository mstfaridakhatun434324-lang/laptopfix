---
title: "How to Disable Automatic Restart After a Blue Screen on Windows 11"
slug: how-to-disable-automatic-restart-after-bsod-on-windows-11
date: 2026-10-03
categories: ["windows-errors"]
tags: ["windows 11", "blue screen", "bsod", "startup settings"]
description: "Windows 11 reboots instantly after a blue screen? Learn how to disable automatic restart so you can actually read the error code and fix the problem."
thumbnail: "/images/thumbs/how-to-disable-automatic-restart-after-bsod-on-windows-11.webp"
faqs:
  - q: "Why does Windows 11 restart immediately after a blue screen?"
    a: "Windows is set to reboot automatically when it hits a fatal system error. The setting, called AutoReboot, is enabled by default so the machine recovers on its own. That is convenient for servers but frustrating on a laptop, because the stop code vanishes before you can read it. Turning the option off freezes the blue screen so you can note the code."
  - q: "Will disabling automatic restart harm my laptop?"
    a: "No. It only changes what Windows does after a crash: instead of rebooting instantly, it holds the blue screen so you can read the stop code. It does not cause crashes, change performance, or affect your files. Once you have fixed the underlying problem, you can turn automatic restart back on if you prefer the old behavior."
  - q: "What if my laptop restarts so fast I can't change the setting?"
    a: "Boot into the Windows Recovery Environment by holding the power button to force a shutdown twice during startup, then choosing Troubleshoot on the third boot. From there you can open a Command Prompt and change the AutoReboot registry value, or use Startup Settings to boot into Safe Mode, where the graphical setting is easy to reach."
  - q: "Where can I find the blue screen error code after it happened?"
    a: "Windows writes a minidump file to C:\\Windows\\Minidump after every crash. Free tools like BlueScreenView read these dumps and show the stop code and the driver that caused it in plain language. You can also find details in Event Viewer under Windows Logs > System, where each crash is logged as a bugcheck event."
---

How to Disable Automatic Restart After a Blue Screen on Windows 11

There is a special kind of frustration that comes with a Windows blue screen that flashes past in half a second. You see a sad face, a percentage counter, and then your laptop is already rebooting. The one piece of information you actually need — the stop code — is gone before you can read it.

The good news is that this instant reboot is just a setting, and you can turn it off in under a minute. Once disabled, your laptop will hold the blue screen until you restart it yourself, giving you time to photograph the error code and work out what is actually wrong. If the blue screen keeps coming back after you read the code, follow our broader guide on [how to fix the blue screen of death on Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/).

## Why this happens

- **AutoReboot is enabled by default.** Windows sets the `AutoReboot` value to 1 after every clean install, so a crash triggers an instant reboot with no confirmation.
- **Windows treats a crash as unrecoverable.** A bugcheck (the technical name for a blue screen) means the kernel hit something it could not safely continue from, so the default response is to collect a dump and restart.
- **The dump is written silently.** Windows saves a minidump to `C:\Windows\Minidump` and an event to Event Viewer, assuming you will look there later instead of reading the screen.
- **Fast Startup hides the crash.** With Fast Startup enabled, a "shutdown" is really a hibernate, so crashes can loop in ways that make the reboot feel even more abrupt.
- **OEM images keep the default.** Dell, HP, and Lenovo factory images all ship with automatic restart turned on, so this behavior survives a factory reset.
- **Group Policy can enforce it.** On work or school laptops, an IT policy may re-enable automatic restart even after you turn it off.

## How to fix it

Work through these in order. The first method is the easiest; the later ones are for laptops that crash too fast to change settings normally.

### Fix 1: Turn it off in Startup and Recovery

This is the official graphical way, and it takes about thirty seconds.

1. Press **Win + R**, type `sysdm.cpl`, and press **Enter** to open System Properties.
2. Switch to the **Advanced** tab and click **Settings** under **Startup and Recovery**.
3. Uncheck **Automatically restart** under **System failure**.
4. Confirm the **Write debugging information** dropdown is set to **Automatic memory dump** so crash data is still collected.
5. Click **OK** twice to save. The next blue screen will stay on screen until you hold the power button.

### Fix 2: Disable it with a registry edit

If you prefer precision or want to script this across machines, the registry holds the same setting.

1. Press **Win + R**, type `regedit`, and press **Enter**. Approve the UAC prompt.
2. Navigate to **HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CrashControl**.
3. Double-click **AutoReboot** and set its value to `0`. If the value does not exist, right-click in the pane, choose **New > DWORD (32-bit) Value**, name it `AutoReboot`, and set it to `0`.
4. Close Registry Editor and restart once so the change takes effect.

### Fix 3: Disable it from an elevated Command Prompt

A single command does the same job, which is handy if you are helping someone over the phone.

1. Press **Win + S**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Run this command to disable automatic restart:
   `wmic RecoverOS set AutoReboot = False`
3. On newer builds where WMIC is deprecated, use PowerShell instead. Open **Windows PowerShell as administrator** and run:
   `Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\CrashControl" -Name AutoReboot -Value 0`
4. Restart your laptop to confirm the change sticks.

### Fix 4: Change it from the Recovery Environment

When crashes happen so early that Windows never reaches the desktop, change the setting from WinRE.

1. Hold the power button to force a shutdown while Windows is loading. Repeat twice.
2. On the third boot, Windows enters the **Recovery** screen. Click **Troubleshoot**, then **Advanced options**, then **Command Prompt**.
3. Type `regedit` and press **Enter** to open Registry Editor.
4. Select **HKEY_LOCAL_MACHINE**, then go to **File > Load Hive**.
5. Navigate to your Windows drive (often `D:` in WinRE) at `\Windows\System32\config\SYSTEM`, give the hive a temporary name like `OfflineSys`, and set `OfflineSys\ControlSet001\Control\CrashControl\AutoReboot` to `0`.
6. Select the loaded hive and choose **File > Unload Hive**, then close everything and choose **Continue** to boot normally.

### Fix 5: Boot into Safe Mode to make the change

Safe Mode loads a minimal driver set, which often avoids the crashing driver long enough to change settings.

1. From the Recovery screen, go to **Troubleshoot > Advanced options > Startup Settings** and click **Restart**.
2. Press **4** for Safe Mode (or **5** for Safe Mode with Networking).
3. Once in Safe Mode, use Fix 1 (the `sysdm.cpl` method) to uncheck **Automatically restart**.
4. Restart normally. If you need a refresher on getting in and out of Safe Mode, see our guide on [how to boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/).

### Fix 6: Read the stop code from the memory dump

Disabling the reboot is only half the battle — now you need to identify the culprit.

1. Download BlueScreenView from NirSoft on another device if yours is unstable, and copy it over on a USB stick.
2. Run it — it automatically reads `C:\Windows\Minidump` and lists every crash with its stop code and the driver highlighted in red.
3. Note the driver name (often something like `nvlddmkm.sys` or `rtwlanu.sys`). That is your prime suspect for updating or rolling back.
4. You can also open **Event Viewer**, go to **Windows Logs > System**, and filter for **Event ID 1001** (BugCheck) to see the same data without extra tools.

### Fix 7: Update or roll back the suspect driver

Most recurring blue screens trace back to one bad driver, and now you know which one.

1. Open **Device Manager** (**Win + X**, then **Device Manager**).
2. Find the device matching the driver from Fix 6, right-click it, and choose **Update driver > Search automatically for drivers**.
3. If the crash started right after a driver update, choose **Properties > Driver > Roll Back Driver** instead.
4. For graphics and Wi-Fi drivers, grab the latest version directly from the manufacturer. Intel users can run the automatic check at [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), and NVIDIA owners should use the official [driver download page](https://www.nvidia.com/Download/index.aspx).

### Fix 8: Repair system files if crashes persist

If no single driver stands out, corrupted system files may be triggering the bugchecks.

1. Open an elevated **Command Prompt** and run:
   `sfc /scannow`
2. When it finishes, run the DISM repair commands one at a time:
   `DISM /Online /Cleanup-Image /RestoreHealth`
3. Restart and watch for further crashes. If they continue, a clean look at recent Windows updates is worthwhile — check **Settings > Windows Update > Update history** and uninstall anything installed just before the crashes began. Microsoft documents blue screen troubleshooting steps further at [Windows support](https://support.microsoft.com/en-us/windows).

## Closing

Disabling automatic restart will not fix the crash itself, but it turns a maddening half-second flash into a readable error screen — and a readable error is a solvable one. Change the setting using whichever method suits your situation, grab the stop code, chase down the faulty driver, and your laptop should be back to boring, reliable normality.
