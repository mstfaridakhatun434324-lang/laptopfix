---
title: "Fix DRIVER_POWER_STATE_FAILURE After a Windows 11 Update"
slug: how-to-fix-driver-power-state-failure-after-windows-11-update
date: 2026-10-10
categories: ["windows-errors"]
tags: ["driver power state failure", "blue screen", "windows 11 update"]
description: "Fix DRIVER_POWER_STATE_FAILURE after a Windows 11 update: update power-related drivers, disable Fast Startup, and tune power settings."
thumbnail: "/images/thumbs/how-to-fix-driver-power-state-failure-after-windows-11-update.webp"
faqs:
  - q: "What does DRIVER_POWER_STATE_FAILURE mean?"
    a: "Stop code 0x0000009F: a driver failed to complete a power state transition — usually sleep, hibernate, or shutdown — in the allowed time. The classic scenario is closing the laptop lid or waking from sleep and getting a blue screen instead."
  - q: "Why did it start after the Windows 11 update?"
    a: "The update replaced a power-related driver (chipset, graphics, Wi-Fi, or storage) with a version that mishandles sleep/wake transitions. Power management is timing-sensitive, so even a small driver regression shows up immediately."
  - q: "Which drivers cause this error most often?"
    a: "Chipset drivers, graphics drivers, Wi-Fi drivers, and storage controller drivers — in that rough order. Anything involved in putting a device to sleep or waking it up is a candidate."
  - q: "Will disabling sleep fix it?"
    a: "It avoids the trigger but does not fix the driver — and you lose sleep functionality. Better to update the power-related drivers properly. Use sleep-disable only as a temporary workaround while you troubleshoot."
---

DRIVER_POWER_STATE_FAILURE (0x0000009F) is the blue screen of bad naps: a driver failed to finish a power transition — sleep, wake, shutdown, or hibernate — within the time Windows allows, and Windows gave up on it. After a Windows 11 update, this almost always means the update swapped in a driver that fumbles power management on your hardware.

The signature symptom is unmistakable: the laptop crashes when it sleeps, when it wakes, or when it shuts down — the exact moments drivers are supposed to power devices down and back up in an orderly sequence. The fix targets the drivers that own those transitions, plus the Windows power settings that interact with them.

## Why this happens

- **Chipset driver regression:** The chipset driver orchestrates device power states across the whole system; a bad version from the update breaks the choreography and something misses its deadline.
- **Graphics driver mishandling sleep:** GPUs have the most complex power states of any component — a buggy graphics driver hangs the entire transition.
- **Wi-Fi driver failing to sleep/wake:** Network adapters that will not power down cleanly are a classic 0x9F source, especially on laptops.
- **Fast Startup conflicts:** Hybrid shutdown interacts badly with drivers that expect a full, honest shutdown sequence.
- **USB selective suspend issues:** USB devices or hubs that refuse to suspend hang the power transition while Windows waits on them.
- **Outdated BIOS:** Firmware-level power management bugs that the new Windows build exposes through stricter ACPI expectations.
- **Storage driver timeouts:** NVMe/SATA drivers that stall during the sleep transition hold up every device behind them in the power queue.

## How to fix it

Work through these in order — test sleep/wake after the driver steps.

### Fix 1: Update chipset, graphics, and Wi-Fi drivers

1. Download the latest **chipset** driver from your laptop maker's support page (Dell, HP, Lenovo, ASUS, or Acer) for your exact model — this is the highest-priority update for 0x9F.
2. Clean-install the newest **graphics** driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD's driver page, or [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html), using the clean-install option where offered.
3. Update **Wi-Fi** and **Bluetooth** drivers from the manufacturer's support page — do not rely on Device Manager's automatic search for these.
4. Restart the laptop.
5. Test deliberately: put the laptop to sleep, wait a full minute, wake it. Repeat five times. Also test hibernate and shutdown. Power drivers cause the large majority of 0x9F cases, so this step resolves most of them outright.

### Fix 2: Disable Fast Startup

1. Open **Control Panel → Power Options → Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
4. Shut down fully (not restart), wait 10 seconds, and power on.
5. Fast Startup's hybrid shutdown is a frequent 0x9F accomplice — disabling it forces honest shutdowns that do not depend on drivers correctly handling hibernation. Retest your sleep/wake cycles after this change.

### Fix 3: Tune USB and PCI Express power settings

1. Open **Control Panel → Power Options → Change plan settings → Change advanced power settings**.
2. Expand **USB settings → USB selective suspend setting** and set both **On battery** and **Plugged in** to **Disabled**.
3. Expand **PCI Express → Link State Power Management** and set both to **Off** for testing (you can try **Moderate** later as a compromise).
4. Click **OK** and test sleep/wake cycles again.
5. Over-aggressive link power management trips marginal drivers constantly — relaxing these settings removes a whole category of timing failures.

### Fix 4: Update the BIOS

1. Check your current BIOS version: press **Win + R**, type `msinfo32`, and look at **BIOS Version/Date**.
2. Compare it against the latest release on your manufacturer's support page for your exact model.
3. Download and install the BIOS update while plugged into AC power — do not touch the laptop until it finishes and restarts on its own.
4. BIOS updates frequently include ACPI power-management fixes that current Windows 11 builds expect to find.
5. After updating, retest sleep, hibernate, and shutdown cycles deliberately. Related power-transition crashes are covered in our [driver power state guide](/articles/driver-power-state-failure-windows-11-fix/).

### Fix 5: Run the Power troubleshooter and reset power plans

1. Open **Settings → System → Troubleshoot → Other troubleshooters** and click **Run** next to **Power**.
2. Apply every recommendation it makes.
3. Then reset your power plans to factory defaults: open **Terminal (Admin)** and run `powercfg -restoredefaultschemes`.
4. Restart the laptop.
5. Corrupted or overly aggressive custom power plan settings can cause 0x9F even with perfect drivers — the reset eliminates that variable completely.

### Fix 6: Identify the specific hanging driver

1. Install **WinDbg** from the Microsoft Store.
2. Open the newest dump file in **C:\Windows\Minidump** and run `!analyze -v` in the command window.
3. Look at the **BLOCKING_PROCESS** / stack output — 0x9F dumps usually name the driver that missed its power deadline.
4. Alternatively, open **Event Viewer → Windows Logs → System** and look for **Kernel-Power** errors timestamped around your crashes.
5. Update or roll back that specific driver. A named culprit beats blanket updating — our [dump-reading guide](/articles/best-way-to-read-dump-files-with-windbg/) walks through the full analysis procedure.

### Fix 7: Roll back the Windows update if crashes just started

1. Open **Settings → Windows Update → Update history → Uninstall updates**.
2. Remove the update whose install date matches the start of the crashes, then restart.
3. If stability returns, pause updates for 2–3 weeks (**Settings → Windows Update → Pause updates**) to give vendors time to ship fixed drivers.
4. When you resume, install the manufacturer's chipset and graphics drivers first, then take the Windows update.
5. The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) lets you reinstall the update manually later while skipping its bundled driver updates — useful when only the driver portion was bad.

### Fix 8: Disable hybrid sleep and test hibernate separately

1. In the advanced power settings (**Control Panel → Power Options → Change advanced power settings**), expand **Sleep → Allow hybrid sleep** and set it to **Off** for both battery and plugged in.
2. Test sleep alone for a day, then test hibernate alone (**Power → Hibernate** from the Start menu).
3. If one works and the other crashes, you have narrowed the fault to the specific transition — mention this if you ever contact support, because it points directly at the driver owning that path.
4. As a temporary workaround (not a fix), you can disable sleep entirely in **Settings → System → Power & battery** while you work through the driver updates — but circle back and re-enable it once the real fix lands.

## Closing

DRIVER_POWER_STATE_FAILURE is a power-transition timeout, and after an update the new driver is guilty until proven innocent. Update chipset, graphics, and Wi-Fi drivers first; disable Fast Startup; relax USB and PCIe power saving; bring the BIOS current; and use WinDbg to name the hanging driver if the blanket approach does not land it. Test with deliberate sleep/wake cycles after each change — when five clean cycles pass in a row, the driver that was missing its deadline is fixed.
