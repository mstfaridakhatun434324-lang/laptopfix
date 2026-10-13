---
title: "How to Disable Automatic Restart After a Blue Screen in Windows"
slug: how-can-i-disable-automatic-restart-after-bsod
date: 2026-10-11
categories: ["windows-errors"]
tags: ["blue screen", "automatic restart", "startup settings"]
description: "Tired of Windows rebooting before you can read the blue screen? Here's how to disable automatic restart — via Settings, command line, or recovery."
thumbnail: "/images/thumbs/how-can-i-disable-automatic-restart-after-bsod.webp"
faqs:
  - q: "Why does Windows restart automatically after a blue screen?"
    a: "By default, Windows is configured to reboot immediately on system failure to minimize downtime. That's convenient for servers but terrible for troubleshooting — the blue screen vanishes before you can read the stop code. Disabling it keeps the error on screen until you manually restart."
  - q: "Will disabling automatic restart harm my laptop?"
    a: "No. It only changes what happens after a crash: instead of rebooting instantly, Windows waits on the blue screen. The crash itself is unaffected. It's purely a diagnostic setting, and you can re-enable it anytime."
  - q: "Can I disable it if Windows won't boot?"
    a: "Yes — use the recovery environment. Boot into Automatic Repair (via forced shutdowns or installation media), go to Troubleshoot > Advanced options > Startup Settings, and choose 'Disable automatic restart after failure.' You can also set it from the recovery Command Prompt with a registry or bcdedit command."
  - q: "Does this stop the blue screens from happening?"
    a: "No — it only stops the instant reboot, giving you time to read the stop code and gather evidence. You still need to fix the underlying cause. Think of it as turning on the lights before fixing the wiring."
---
When Windows blue screens and instantly reboots, it robs you of the one thing you need most: the error message. That stop code — MEMORY_MANAGEMENT, DRIVER_IRQL_NOT_LESS_OR_EQUAL, whatever it is — is the starting point for every fix. Disabling automatic restart keeps the blue screen visible so you can actually read it, photograph it, and troubleshoot properly.

This is a settings change, not a repair — it takes two minutes and makes every future blue screen ten times easier to diagnose. Pair it with our [BSOD-on-startup guide](/articles/best-way-to-fix-bsod-on-startup-windows-11/) if crashes are also preventing normal boot, and check [what to do when stuck on restarting](/articles/how-do-i-fix-windows-11-stuck-on-restarting-screen/) for related reboot issues.

## Why this happens

- **Default Windows behavior:** "Automatically restart" is checked by default in Startup and Recovery settings on every Windows install.
- **Fast reboot hides the evidence:** Modern SSDs reboot so quickly you may never even see the blue screen flash by.
- **Designed for unattended machines:** The default makes sense for servers that should recover alone — not for a laptop you're actively troubleshooting.
- **Crash dumps still get written:** Disabling auto-restart doesn't affect minidump creation; you still get logs either way.
- **Re-enabling is trivial:** It's a single checkbox, so there's no risk in turning it off temporarily.
- **Also applies to update reboots:** A separate but related setting controls whether Windows Update restarts your PC automatically — worth taming while you're here (see Fix 6).

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as the setting is changed.

### Fix 1: Disable it in System Properties (Windows boots normally)

The standard method — two minutes, fully reversible.

1. Press **Win + R**, type `sysdm.cpl`, and press Enter.
2. Go to the **Advanced** tab and click **Settings** under **Startup and Recovery**.
3. Under **System failure**, uncheck **Automatically restart**.
4. While you're here, confirm **Write debugging information** is set to **Automatic memory dump** or **Small memory dump** — you want crash logs.
5. Click **OK**, then **OK** again. The next blue screen will stay on screen until you hold the power button.
6. Pro tip: when the next blue screen appears, photograph it with your phone — the stop code and the faulting file name (often shown as "What failed: something.sys") are gold for diagnosis.

### Fix 2: Disable it from the command line

Same result, useful for scripts or remote administration.

1. Open an **administrator Command Prompt**.
2. Run `wmic recoveros set AutoReboot = False`.
3. You'll see confirmation that the property was updated.
4. To verify, run `wmic recoveros get AutoReboot` — it should show **FALSE**.
5. To re-enable later, run `wmic recoveros set AutoReboot = True`.

### Fix 3: Disable it via the registry

For when the GUI is uncooperative or you're scripting across machines.

1. Press **Win + R**, type `regedit`, and press Enter (approve the UAC prompt).
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CrashControl`.
3. Double-click **AutoReboot** and set its value data to **0**.
4. Click OK and close Registry Editor — no restart needed for this to take effect.
5. To re-enable, set the value back to **1**. (Back up the key first via **File** > **Export** if you're cautious — good habit with any registry edit.)

### Fix 4: Disable it from the recovery environment (Windows won't boot)

When crashes prevent reaching the desktop, change it from outside Windows.

1. Force the recovery environment: power on, and when the Windows logo appears, hold the power button. Repeat twice; the third boot opens **Automatic Repair**.
2. Choose **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. Press **9** (or **F9**) for **Disable automatic restart after failure**.
4. Windows boots with auto-restart disabled for that session — the blue screen will stay visible so you can read the stop code.
5. Write down the full stop code and any file name shown. Then, once you can boot normally, use Fix 1 to make the change permanent.
6. If even Startup Settings won't load, boot from Windows installation media, choose **Repair your computer**, and follow Fix 5's Command Prompt method instead.

### Fix 5: Set it via the recovery Command Prompt

A permanent change made from outside a non-booting Windows.

1. In the recovery environment, go to **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. Identify your Windows drive letter — in recovery it's often **D:** instead of C:. Run `diskpart`, then `list volume`, then `exit` to check.
3. Load the offline registry: run `reg load HKLM\OfflineSys D:\Windows\System32\config\SYSTEM` (adjust the drive letter).
4. Run `reg add "HKLM\OfflineSys\ControlSet001\Control\CrashControl" /v AutoReboot /t REG_DWORD /d 0 /f`.
5. Unload with `reg unload HKLM\OfflineSys`, then restart. Auto-restart is now permanently off.

### Fix 6: Also disable automatic restart for Windows Update reboots (bonus)

A related annoyance: Windows rebooting overnight for updates. Tame that too.

1. Open **Settings** > **Windows Update** > **Advanced options**.
2. Set **Active hours** to cover your real usage window so updates don't reboot mid-work.
3. Turn on **Notify me when a restart is required** so reboots never surprise you.
4. For update-related blue screens specifically, see our [blue screen after update guide](/articles/how-to-fix-blue-screen-after-windows-11-update/).

## Closing

Disabling automatic restart after a blue screen is the single most useful two-minute change a troubleshooter can make. It doesn't fix anything by itself — but it transforms every future crash from a blink-and-miss-it reboot into readable evidence: a stop code you can photograph, search, and match to a fix. Combine it with minidumps (left enabled by default) and you have everything needed for real diagnosis instead of guessing. For more on reading those crash logs, see [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows). Once you've diagnosed and repaired the underlying cause, feel free to re-enable it. But while you're in troubleshooting mode, keep it off. The blue screen is trying to tell you something — let it finish the sentence. Future-you, mid-troubleshoot at midnight, will be grateful.
