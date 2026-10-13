---
title: "Fix Windows 11 Stuck on the Restarting Screen (Dell Laptop)"
slug: how-to-fix-windows-11-stuck-on-restarting-screen-on-dell-laptop
date: 2026-09-10
categories: ["windows-errors"]
tags: ["restarting screen", "windows 11", "dell", "stuck"]
description: "Windows 11 stuck on 'Restarting' on your Dell? Force a safe shutdown, then fix the driver or service hanging the reboot."
thumbnail: "/images/thumbs/how-to-fix-windows-11-stuck-on-restarting-screen-on-dell-laptop.webp"
faqs:
  - q: "Is it safe to force-shut-down when it's stuck on Restarting?"
    a: "Yes. When the screen has shown 'Restarting' with the spinner for more than 10–15 minutes, the reboot is genuinely hung — holding the power button for 5–10 seconds is the correct move. The risk of file corruption from a forced shutdown is far lower than the risk of leaving it hung indefinitely."
  - q: "Why does this happen on Dell laptops?"
    a: "Usually a driver or service that won't release during shutdown: Dell's own utilities (SupportAssist background tasks, Dell Update services), a misbehaving network or storage driver, or Windows Update stuck mid-install. Fast Startup can also wedge the reboot cycle."
  - q: "It happens every time I restart. What's the permanent fix?"
    a: "A recurring hang means a specific driver or service consistently blocks shutdown. The fixes below identify it — typically via clean boot bisection or by disabling Fast Startup — and the permanent fix is updating, disabling, or removing that component."
  - q: "Could this be a Windows Update problem?"
    a: "Often. Updates that are mid-install when you hit restart can hang the reboot for a very long time — sometimes legitimately. Rule: if the spinner is moving and the drive light is active, give it up to an hour. If the spinner is frozen or it's been over an hour, it's hung."
---
Your Dell has been showing "Restarting" with that hypnotic spinner for twenty minutes, and it's not going anywhere. This is one of the more common Windows 11 annoyances on Dell laptops: something — a driver, a service, a stuck update — refuses to let go during the shutdown phase, and the reboot waits forever for permission that never comes. The screen isn't frozen in the crash sense; it's patiently waiting on a component that's never going to respond.

The fix has two parts: get the machine unstuck safely right now, then find and fix whatever is hanging the reboot so it doesn't happen every time. Here's the order.

## Why this happens

- **A driver that won't unload.** Network, storage, and USB drivers that hang during the shutdown handshake are the top cause.
- **Dell background services stalling.** SupportAssist, Dell Update, and Dell Digital Delivery services occasionally block shutdown while doing background work.
- **Windows Update mid-install.** Updates finalizing during restart can take a long time — or wedge entirely.
- **Fast Startup wedging the reboot.** The hybrid shutdown state gets corrupted and the restart cycle can't complete.
- **A program refusing to close.** An app with unsaved state or a hung process that Windows waits on indefinitely.
- **Corrupted system files in the shutdown path.** Damaged files in the power management or update stack.

## How to fix it

Work through these in order. Fix 1 gets you unstuck now; the rest prevent the encore.

### Fix 1: Force the shutdown safely

When it's genuinely hung, holding the power button is correct.

1. Wait at least 10–15 minutes first — if the drive activity light is blinking, an update may legitimately be working.
2. If the spinner is frozen or nothing has changed in 15+ minutes, press and **hold the power button for 5–10 seconds** until the laptop powers off.
3. Unplug the charger and any USB devices. Wait 30 seconds.
4. Power on. Windows will usually boot normally — possibly running a quick disk check first, which is fine.
5. If it boots straight back into a stuck "Restarting," interrupt boot three times to reach WinRE and continue with Fix 6.

### Fix 2: Disable Fast Startup

The most common permanent fix for recurring restart hangs.

1. Once booted, open **Control Panel** > **Power Options** > **Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and save.
4. Restart to test. Fast Startup's hybrid shutdown is implicated in a huge share of Dell restart hangs — disabling it costs you a couple of seconds of boot time and buys reliability.

### Fix 3: Update Dell drivers and BIOS

Stale drivers are the next most common cause.

1. Open **Dell SupportAssist** and install all recommended **BIOS**, **chipset**, **network**, **storage**, and **USB** updates.
2. BIOS update rules: charger plugged in, nothing else running, don't touch it until it reboots itself.
3. Anything SupportAssist misses, grab by service tag from [Dell Support](https://www.dell.com/support).
4. Restart and test. Driver updates resolve the shutdown-handshake hangs that cause most recurring cases.

### Fix 4: Clean-boot to find the hanging service

If it still hangs, bisect the software.

1. **Win + R** > `msconfig` > **Services** tab > tick **Hide all Microsoft services** > **Disable all** > OK.
2. **Task Manager** > **Startup apps** > disable everything. Restart.
3. Restarts cleanly now? Re-enable services in halves, restarting each time, until the hang returns — the last batch contains the culprit.
4. Common Dell-land winners: Dell Update Service, SupportAssist background agents, third-party backup tools, and RGB/peripheral utilities. Update or uninstall the offender.

### Fix 5: Repair Windows Update and system files

A wedged update stack hangs restarts by design.

1. In **Terminal (Admin)**, reset the update components:
   `net stop wuauserv` / `net stop bits` / `net stop cryptSvc`
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
   `net start wuauserv` / `net start bits` / `net start cryptSvc`
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Check **Settings** > **Windows Update** for stuck or failed updates and let them complete or fail cleanly.
4. Microsoft documents the update troubleshooter on [Microsoft Support](https://support.microsoft.com/en-us/windows) if you prefer the automated route.

### Fix 6: Check the disk and run Dell diagnostics

Rule out hardware contributing to the hang.

1. In **Terminal (Admin)**, run `chkdsk C: /f`, reboot for the scan.
2. Reboot and tap **F12** > **Diagnostics** for Dell's pre-boot hardware scan — a failing drive can stall shutdown while Windows retries I/O.
3. Drive errors plus restart hangs is a replace-the-SSD signal. Back up first, diagnose second.

### Fix 7: System Restore to before the hangs started

When the trigger was a specific change, undo it wholesale.

1. Search Start for **Create a restore point** > **System Restore** > pick a date before the hangs began.
2. This reverses driver, update, and registry changes while keeping your files.
3. After restore, pause updates briefly and update Dell drivers manually before re-applying anything. See [how to use System Restore](/articles/how-to-use-system-restore-on-windows-11/) for setting up protection going forward.

### Fix 8: Read the Event Viewer shutdown trace

When the hang recurs rarely, the logs name the component that stalled.

1. After a successful boot following a hang, open **Event Viewer** (`eventvwr.msc`).
2. Go to **Windows Logs** > **System** and filter for source **User32** with event ID **1074** (shutdown initiations) and look at the entries just before the hang — they show which process held up shutdown.
3. Also check **Applications and Services Logs** > **Microsoft** > **Windows** > **Diagnostics-Performance** > **Operational** for event IDs **200–300**, which log shutdown performance degradations with the offending component named.
4. Once named, update, disable, or uninstall that specific component. This is how you catch intermittent hangs that clean-boot bisection misses because they only happen under specific conditions.

## Closing

A Dell stuck on "Restarting" is almost never a serious problem — it's a shutdown handshake that never completes, and the fixes are correspondingly mundane: force the power off, disable Fast Startup, update Dell's drivers, and bisect the services if it recurs. The 15-minute rule (wait, watch the drive light, then hold the power button) keeps you from either panicking too early or waiting forever. Do the permanent fixes once and restarts go back to taking thirty seconds. Acer owners hit the identical hang with different utilities behind it — the [Acer walkthrough](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-acer-laptop/) covers that variant.
