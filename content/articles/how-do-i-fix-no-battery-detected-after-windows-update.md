---
title: "No Battery Detected After a Windows Update? Fix It Now"
slug: how-do-i-fix-no-battery-detected-after-windows-update
date: 2026-10-03
categories: ["battery"]
tags: ["no battery detected", "windows update", "battery driver"]
description: "Windows shows 'no battery detected' after an update? Reinstall the ACPI battery driver, roll back the bad driver, and restore battery detection."
thumbnail: "/images/thumbs/how-do-i-fix-no-battery-detected-after-windows-update.webp"
faqs:
  - q: "Why does Windows say no battery detected after an update?"
    a: "The update installed an incompatible battery, chipset, or ACPI driver, breaking communication between Windows and the battery controller. The battery is usually physically fine — Windows just can't see it. Reinstalling the correct driver restores detection."
  - q: "Will my laptop work with no battery detected?"
    a: "Yes, on AC power it runs normally. But you have no backup — a power blip means instant shutdown and possible data loss. Also, some laptops throttle performance when no battery is detected, so fix it promptly."
  - q: "How do I roll back a battery driver in Windows?"
    a: "Open Device Manager > Batteries, right-click Microsoft ACPI-Compliant Control Method Battery > Properties > Driver tab > Roll Back Driver. If that's greyed out, uninstall the device and restart — Windows reinstalls the last working driver."
  - q: "Could the update have damaged my battery?"
    a: "Extremely unlikely. Software updates can't damage battery cells. 'No battery detected' after an update is a software/communication problem in virtually every case — the hardware is untouched."
---
Windows Update finished, you rebooted, and now the taskbar shows a battery icon with a red X: "No battery detected." The battery was fine yesterday. The update didn't touch the hardware — it just broke Windows' ability to talk to it.

This is one of the most common post-update battery issues, and it's almost always fixable in software. The update replaced a working driver with a broken one, or scrambled the ACPI battery interface. Here's how to get detection back — most people are fixed before they reach the halfway mark.

## Why this happens

- **A bad battery driver was installed.** The update pushed a new ACPI battery or chipset driver that's incompatible with your machine's embedded controller.
- **The driver stack got corrupted mid-update.** Interrupted or overlapping updates can leave the battery driver half-installed.
- **BIOS/EC and new driver disagree.** The update's driver expects a newer embedded-controller interface than your current BIOS provides.
- **Fast startup cached the broken state.** The hybrid shutdown preserved the bad driver state, so restarts keep "re-detecting" the same failure.
- **Coincidental hardware timing.** Rarely, the battery connector chose the same week to fail — worth ruling out after software fixes.
- **Third-party battery utilities conflict.** Manufacturer tools (old Dell Power Manager, etc.) can fight the new driver for control of the battery interface.

## How to fix it

Work through these in order — start with the driver, since that's the cause 90% of the time.

### Fix 1: Reinstall the ACPI battery driver

1. Right-click **Start** > **Device Manager**, expand **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**. Check **Attempt to remove the driver** if offered. Repeat for any second entry.
3. Also expand **System devices** and look for **Microsoft ACPI-Compliant Embedded Controller** — leave it alone for now.
4. Click **Action** > **Scan for hardware changes**, or shut down fully and power back on.
5. Check the taskbar: the battery icon should return within a minute of boot. If it does, generate a `powercfg /batteryreport` to confirm Windows is reading real capacity data again, not just showing the icon.

### Fix 2: Roll back the driver Windows Update installed

1. In **Device Manager** > **Batteries**, right-click the battery device > **Properties** > **Driver** tab.
2. If **Roll Back Driver** is clickable, use it and choose "previous driver worked better" — then restart.
3. If it's greyed out, the driver wasn't the kind that keeps a backup — continue to Fix 3.
4. After rollback, pause updates briefly: **Settings** > **Windows Update** > **Pause updates** for a week, so the bad driver isn't immediately reinstalled.

### Fix 3: Do a full shutdown to clear the cached state

1. Hold **Shift** and click **Shut down** in the Start menu (bypasses fast startup).
2. Unplug the charger, and if the battery is removable, take it out for 60 seconds.
3. Hold the power button for 30 seconds with everything disconnected.
4. Reconnect and boot — this forces a clean hardware re-enumeration, which often restores detection when a warm reboot doesn't.

### Fix 4: Update the chipset driver and BIOS

1. The battery talks to Windows through the chipset and EC — get both current. Visit your manufacturer's support page: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
2. Install the latest chipset driver first, then the latest BIOS (charger plugged in, don't interrupt).
3. Reboot and check for the battery icon. BIOS updates frequently restore compatibility with newer Windows ACPI drivers.

### Fix 5: Check for the bad update and block it

1. Go to **Settings** > **Windows Update** > **Update history** and note the most recent driver updates — look for anything under "Driver updates" dated when the problem started.
2. If you identify it, use **Show or hide updates** troubleshooter (from [Microsoft support](https://support.microsoft.com/en-us/windows)) to hide that specific driver update.
3. As a longer-term guard, consider switching driver updates to manual: **System** > **About** > **Advanced system settings** > **Hardware** > **Device Installation Settings** > **No**.

### Fix 6: Rule out hardware

1. Boot into BIOS/UEFI (usually **F2** or **Del**) and look for a battery status page — if the BIOS sees the battery but Windows doesn't, it's 100% a Windows driver problem.
2. If the BIOS also shows no battery, reseat it (removable models) or check the internal connector if you're comfortable opening the chassis.
3. Run the manufacturer's diagnostic — Dell ePSA, HP Hardware Diagnostics, Lenovo Vantage scan — for a definitive battery hardware verdict.

### Fix 7: System restore as the safety net

1. If detection broke on a specific date, use **System Restore**: search **Start** for **Create a restore point**, open **System Protection**, click **System Restore**.
2. Pick a restore point from before the update and let it roll back.
3. After restore, pause updates and install drivers manually from the manufacturer instead.
4. For the step-by-step troubleshooting variant of this issue, see [troubleshoot no battery detected](/articles/troubleshoot-no-battery-detected-after-windows-update/).

### Fix 8: Prevent the next update from breaking it again

1. Once detection is restored, open **Settings** > **Windows Update** > **Advanced options** and consider turning off **Receive updates for other Microsoft products** if driver updates keep causing trouble — you'll then install drivers manually from the manufacturer.
2. In **System** > **About** > **Advanced system settings** > **Hardware** tab > **Device Installation Settings**, choose **No** to stop Windows from auto-replacing your working drivers.
3. Bookmark your manufacturer's driver page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) and check it yourself every few months instead.
4. If the laptop later shows "plugged in, not charging" instead of "no battery," that's a different issue — see [battery not charging on Windows 10](/articles/how-to-fix-laptop-battery-not-charging-on-windows-10/).

## Closing

"No battery detected" after an update is Windows losing the conversation with your battery, not the battery dying. The driver reinstall in Fix 1 resolves most cases in under five minutes — and the BIOS rarely needs to be involved at all. Keep driver updates on a short leash afterward, and this particular headache won't repeat.
