---
title: "How to Stop Windows 10 From Restarting Automatically After a BSOD"
slug: how-to-disable-automatic-restart-after-bsod-on-windows-10
date: 2026-09-27
categories: ["windows-errors"]
tags: ["windows 10", "bsod", "automatic restart"]
description: "Tired of Windows 10 rebooting before you can read the blue screen? Disable automatic restart after system failure and finally see the stop code."
thumbnail: "/images/thumbs/how-to-disable-automatic-restart-after-bsod-on-windows-10.webp"
faqs:
  - q: "Will disabling automatic restart stop the blue screens?"
    a: "No — and anyone who implies otherwise is confused. This setting changes only what happens after the crash: hold on the blue screen versus reboot immediately. The underlying cause (bad driver, failing RAM, whatever it is) still needs its own fix. Think of it as turning on the lights, not fixing the wiring."
  - q: "The blue screen still reboots even though I disabled it. Why?"
    a: "Three possibilities: the setting did not save (verify in the dialog), the crash is happening so early in boot that the setting is not loaded yet, or what you are seeing is not a bug check at all but a hard reset from overheating or power loss — those reboot regardless of this setting. Event ID 41 without a 1001 points to the latter."
  - q: "Is there a Group Policy for this?"
    a: "Yes — useful for managing multiple machines. Under Computer Configuration, Administrative Templates, System, there are policies controlling crash behavior, though the specific auto-restart maps most directly to the registry value in Fix 2, which you can deploy via Group Policy Preferences. For a single home PC, the checkbox is simpler."
  - q: "Should I change the memory dump type too?"
    a: "For most troubleshooting, no — the default Automatic memory dump (which writes a minidump plus kernel memory) is the right balance. Switch to Small memory dump only if disk space is critically tight, and to Complete only if a driver developer specifically asks for it. Bigger dumps help almost nobody outside active driver debugging."
---

The most frustrating part of a blue screen is often not the crash — it is that Windows reboots in seconds, before you can read the stop code, the QR code, or the faulting driver name. Automatic restart after system failure is enabled by default, and it turns every BSOD into a blink-and-you-miss-it event that leaves you with no information to troubleshoot with.

Disabling it is a one-minute settings change (with a registry alternative for when Windows will not boot). The blue screen will then stay on screen until you restart manually, giving you time to photograph it, note the stop code, and actually diagnose the problem. This guide covers the standard method, the registry method, and the recovery method.

## Why this happens

- **Automatic restart is the Windows default:** a fresh install enables Automatically restart under Startup and Recovery — most users never know the option exists.
- **You need the stop code to troubleshoot:** without the code (e.g. IRQL_NOT_LESS_OR_EQUAL) and the faulting driver name, every BSOD is a mystery; with them, it is a solvable problem.
- **The reboot destroys context:** minidumps are still written, but the on-screen details — the QR code, the what failed line — vanish with the reboot.
- **Rapid reboot loops hide the pattern:** when crashes come in clusters, a held blue screen lets you confirm whether it is the same stop code every time.
- **You may want a memory dump choice too:** the same settings page controls dump type — complete dumps help deep analysis, minidumps are enough for most cases.
- **It changes nothing about stability:** disabling auto-restart does not cause more crashes or fix anything — it purely changes what happens after the crash, giving you information instead of a reboot.

## How to fix it

Work through these in order, from the quickest checks to the deeper repairs. Most people are back up and running by Fix 4 or 5.

### Fix 1: Disable it in Startup and Recovery settings

The standard method. One checkbox, immediate effect, fully reversible.

1. Press **Win + R**, type `sysdm.cpl`, and press Enter to open System Properties.
2. Go to the **Advanced** tab and click **Settings** under **Startup and Recovery**.
3. Under **System failure**, untick **Automatically restart**.
4. While here, confirm **Write an event to the system log** is ticked and the dump is set to **Automatic memory dump** (the default is fine for most).
5. Click **OK** twice. The next blue screen will hold until you power off manually — photograph it.

### Fix 2: Disable it via the registry

For scripting, remote administration, or when the GUI is awkward. Same result, different path.

1. Press **Win + R**, type `regedit`, and press Enter.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CrashControl`.
3. Double-click **AutoReboot** and set its value to **0**. (1 enables auto-restart; 0 disables it.)
4. If AutoReboot does not exist, right-click, choose **New > DWORD (32-bit) Value**, name it **AutoReboot**, and set it to 0.
5. Close the editor — the change takes effect immediately, no reboot needed. Verify by reopening the Startup and Recovery dialog from Fix 1.

### Fix 3: Disable it from recovery when Windows won't boot

If BSODs strike during boot, change the setting offline from the recovery command prompt.

1. Boot into **Automatic Repair** (three interrupted boots), then **Troubleshoot > Advanced options > Command Prompt**.
2. Load the offline registry: type `regedit` to open the editor inside recovery.
3. Select **HKEY_LOCAL_MACHINE**, then **File > Load Hive**, navigate to `C:\Windows\System32\config\SYSTEM`, and name it **OfflineSys**.
4. Go to `HKEY_LOCAL_MACHINE\OfflineSys\ControlSet001\Control\CrashControl`, set **AutoReboot** to **0**.
5. Select **OfflineSys**, then **File > Unload Hive**, close regedit, type `exit`, and **Continue**. The next boot-time BSOD will hold on screen.

### Fix 4: Photograph and decode the held blue screen

Now that the screen stays put, extract every bit of information from it.

1. Photograph the full screen — include the stop code, the what failed line (e.g. `What failed: Netwtw10.sys`), and the QR code.
2. The stop code (in ALL_CAPS_WITH_UNDERSCORES) is your search term — it identifies the crash class.
3. The what failed line names the faulting driver directly — that is your prime suspect for updating or rolling back.
4. The QR code links to Microsoft's generic BSOD help page — mildly useful, but the stop code plus driver name beats it.
5. File the photo somewhere safe; you will reference it through the whole troubleshooting process. The [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) (applies to Windows 10 too) is the natural next step once you have the code.

### Fix 5: Check the dump files for the full story

The held screen gives you the headline; the dump file gives you the article. Both are worth reading.

1. After the next crash and manual restart, open `C:\Windows\Minidump` and find the newest `.dmp`.
2. Install **WinDbg Preview** from the Microsoft Store, open the dump, run `!analyze -v`.
3. Compare **IMAGE_NAME** with the what failed line from your photo — they should agree, and the dump adds the driver version and stack trace.
4. No dump file? Check **Startup and Recovery** settings (Fix 1) — the dump path may be misconfigured, or crashes during very early boot may not write one.
5. Save the `!analyze` output to a text file alongside the photo — this pair is everything a forum or technician needs. If Windows will not boot far enough to reach the desktop, [this Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) covers reaching recovery from a dead boot.

### Fix 6: Use Event Viewer for the crash history

For recurring crashes, the event log shows the pattern: frequency, timing, and whether the code is consistent.

1. Press **Win + R**, type `eventvwr`, and open **Windows Logs > System**.
2. Filter for **Event ID 1001** (bug check) — each entry records the stop code and parameters of a crash.
3. Look at the pattern: same code every time points at one driver; varying codes point at RAM or deeper hardware.
4. Also check for **Event ID 41** (unexpected shutdown) entries without a matching 1001 — those are hard hangs or power losses, a different problem class.
5. Export the relevant events if you are asking for help online — helpers love data, and this is the cleanest form of it.

### Fix 7: Re-enable auto-restart when you're done (optional)

An honest note on when to turn it back on — because a held BSOD is a diagnostic tool, not a lifestyle.

1. While actively troubleshooting recurring BSODs, leave it disabled — you want the information.
2. On a stable machine, or a machine that runs unattended (media server, remote PC), re-enable it: tick **Automatically restart** back on in **Startup and Recovery**.
3. Servers and unattended PCs benefit from auto-restart — a held BSOD on a machine nobody is watching just means extended downtime.
4. For your daily laptop, many technicians leave it disabled permanently — the information is worth more than the 30 seconds a reboot saves.
5. Either way, it is one checkbox. Change it to suit the machine's role, as [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents for the Startup and Recovery options.

## Closing

Disabling automatic restart is the single highest-value one-minute change for anyone fighting recurring blue screens. The stop code and driver name on a held screen turn guesswork into diagnosis — photograph it, read the dump, check the event log, and troubleshoot with actual evidence. Turn it back on for unattended machines; leave it off for the laptop you are actively fixing.
