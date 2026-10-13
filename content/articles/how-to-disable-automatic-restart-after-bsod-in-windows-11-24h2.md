---
title: "How to Stop Windows 11 24H2 From Restarting Automatically After a Blue Screen"
slug: how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2
date: 2026-09-25
categories: ["windows-errors"]
tags: ["disable automatic restart", "bsod", "windows 11 24h2"]
description: "Stop Windows 11 24H2 from auto-restarting after a blue screen so you can read the stop code. Two methods: Settings GUI and registry edit."
thumbnail: "/images/thumbs/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2.webp"
faqs:
  - q: "Why should I disable automatic restart after a BSOD?"
    a: "With auto-restart on, the blue screen flashes for a second and the laptop reboots before you can read the stop code. Turning it off keeps the error on screen so you can note the code and the failing driver name — essential information for fixing the actual problem."
  - q: "Is it safe to leave automatic restart disabled?"
    a: "Yes. It only changes what happens after a crash: instead of rebooting immediately, Windows waits on the blue screen until you restart manually. It does not make crashes more likely or harm anything."
  - q: "The blue screen still disappears too fast — what now?"
    a: "If the screen vanishes even with auto-restart off, check Event Viewer → Windows Logs → System for BugCheck entries after rebooting. Windows always logs the stop code there, so the information is never truly lost."
  - q: "Can I do this from the registry instead?"
    a: "Yes. Set AutoReboot to 0 under HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\CrashControl. The Settings method does exactly the same thing — the registry edit is just the scriptable alternative for advanced users."
---

Windows 11 24H2 restarts automatically after every blue screen by default. That is convenient when a crash is a one-off, but infuriating when you are trying to diagnose a recurring problem — the stop code vanishes before you can read it, and you are left guessing. Disabling automatic restart keeps the blue screen on display until you are ready.

This is a two-minute settings change (or a thirty-second registry edit), and it is one of the first things any technician does when chasing a repeat BSOD. Here is how, plus what to do with the information once you can actually see it.

## Why this happens

- **The default is "restart immediately":** Windows has shipped with **Automatically restart** checked since forever. It assumes most users prefer a reboot over an error screen.
- **Crash dumps still get written:** Disabling auto-restart does not affect dump files — Windows still saves the minidump before showing the screen.
- **Fast boot shortens the visible window:** On modern laptops with fast SSDs, the reboot cycle is so quick the blue screen may be visible for under a second.
- **24H2 did not change the setting, but updates can:** Feature updates occasionally reset system settings. If the blue screen started flashing past after 24H2, check whether the box got re-ticked.
- **You cannot diagnose what you cannot read:** The stop code (e.g., MEMORY_MANAGEMENT) and the failing driver name on the screen cut hours off troubleshooting.

- **Group Policy overriding the setting:** On Pro editions, a local or domain policy can force auto-restart back on. Check `gpedit.msc` under Computer Configuration → Administrative Templates → System if the checkbox will not stay off.
- **Fast Startup hiding the blue screen:** With Fast Startup enabled, some crashes cycle so fast the blue screen never visibly renders — disabling it makes the frozen error screen reliable.
## How to fix it

Work through these in order — Method 1 is enough for almost everyone.

### Fix 1: Disable it in System Properties (recommended)

1. Press **Win + R**, type `sysdm.cpl`, and press Enter to open System Properties.
2. Go to the **Advanced** tab and click **Settings** under **Startup and Recovery**.
3. Under **System failure**, uncheck **Automatically restart**.
4. Click **OK** twice. The next blue screen will stay on screen until you hold the power button. While you are in this dialog, confirm **Write debugging information** is set to **Automatic memory dump** — you will want that dump later.

### Fix 2: Disable it via the registry

1. Press **Win + R**, type `regedit`, and press Enter. Approve the UAC prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CrashControl`.
3. Double-click **AutoReboot** and set its value data to `0` (zero = do not reboot).
4. Close the editor. No restart needed — the change applies to the next crash. This is the same setting the GUI checkbox controls, so use whichever method you prefer. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the Startup and Recovery options.

### Fix 3: Disable it from the recovery environment (if Windows will not boot)

1. Force WinRE: interrupt boot three times by holding the power button during the Windows logo.
2. Go to **Troubleshoot → Advanced options → Command Prompt**.
3. Type `regedit` and press Enter. In the editor, click **HKEY_LOCAL_MACHINE**, then **File → Load Hive**.
4. Browse to **C:\Windows\System32\config\SYSTEM**, name it `temp`, navigate to `temp\ControlSet001\Control\CrashControl`, set **AutoReboot** to `0`, then **File → Unload Hive**. This edits the offline registry so the next crash stays visible.

### Fix 4: Read the stop code and driver name from the frozen screen

1. The next time the blue screen appears, it will stay put. Write down the **stop code** (e.g., DRIVER_POWER_STATE_FAILURE) at the bottom.
2. Note any **driver filename** shown (e.g., `nvlddmkm.sys`) — that names the culprit directly.
3. Photograph the screen with your phone as backup.
4. Look up the stop code: our [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the most common ones, or search this site for the exact code.

### Fix 5: Pull the same information from Event Viewer after rebooting

1. After you manually restart, press **Win + R**, type `eventvwr`, and press Enter.
2. Go to **Windows Logs → System** and filter for **BugCheck** events.
3. Open the most recent one — it lists the stop code in hex and often the faulting driver.
4. This works even if you re-enable auto-restart later, so it is worth learning regardless.

### Fix 6: Analyze the memory dump with WinDbg

1. Confirm dumps exist at **C:\Windows\Minidump** (`.dmp` files dated to your crashes).
2. Install **WinDbg** from the Microsoft Store.
3. Open the newest dump, run `!analyze -v`, and read the **MODULE_NAME** / **IMAGE_NAME** lines.
4. This names the exact driver or component — the definitive answer when the blue screen text is ambiguous. Our [dump-reading walkthrough](/articles/best-way-to-read-dump-files-with-windbg/) shows the full process.

### Fix 7: Re-enable auto-restart once the problem is fixed (optional)

1. When the crashes are resolved, return to `sysdm.cpl` → **Advanced → Startup and Recovery → Settings**.
2. Re-check **Automatically restart** if you prefer the laptop to recover on its own from any future one-off crash.
3. Leave it off if you would rather always see the error — there is no wrong choice, only preference.
4. Either way, keep **Automatic memory dump** enabled so future crashes remain diagnosable.

### Fix 8: Verify the setting stuck with a registry check

The checkbox and the registry are two doors to the same room. A quick registry check confirms the change actually took — useful when a crash still reboots too fast.

1. Press **Win + R**, type `regedit`, and approve the UAC prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CrashControl`.
3. Confirm **AutoReboot** has value data `0`. If it shows `1`, double-click it and set it to `0`.
4. You can also check from the command line: run `reg query "HKLM\SYSTEM\CurrentControlSet\Control\CrashControl" /v AutoReboot` in an elevated Command Prompt.
5. If the value keeps reverting to 1, a group policy or third-party tuner is overriding it — investigate that before assuming the setting is broken.

## Closing

Disabling automatic restart is not itself a fix for blue screens — it is the step that makes every other fix possible, because you can finally read what Windows is trying to tell you instead of watching it vanish. Uncheck one box in System Properties (or set one registry value), photograph the next blue screen, pull the dump, and chase the actual stop code rather than guessing. Once the underlying problem is solved, flip the setting back on if you prefer the laptop to recover from one-off crashes by itself.
