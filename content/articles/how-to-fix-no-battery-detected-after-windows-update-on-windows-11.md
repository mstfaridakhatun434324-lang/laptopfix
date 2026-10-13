---
title: "No Battery Detected After a Windows Update on Windows 11? Fix It Now"
slug: how-to-fix-no-battery-detected-after-windows-update-on-windows-11
date: 2026-10-09
categories: ["battery"]
tags: ["battery", "not detected", "windows update", "windows 11"]
description: "Windows 11 update left your laptop saying no battery detected? These 7 fixes target the update itself — rollbacks, driver repair, and firmware recovery."
thumbnail: "/images/thumbs/how-to-fix-no-battery-detected-after-windows-update-on-windows-11.webp"
faqs:
  - q: "Can a Windows update really make the battery disappear?"
    a: "Yes. Updates replace the ACPI battery driver, the chipset driver, and sometimes touch firmware interfaces. If any of those installs corrupt or mismatch, Windows loses communication with the battery's controller and reports no battery detected — even though the pack is physically fine."
  - q: "How do I know which update broke battery detection?"
    a: "Open Settings > Windows Update > Update history and match the install date to when the problem started. The culprit is usually the most recent cumulative update or driver update. Note its KB number so you can block it after rolling back."
  - q: "Should I uninstall the update or fix the drivers?"
    a: "Do both in sequence: first try the driver repair in this guide, because it's quick and keeps you on the latest security patches. If the battery still isn't detected, roll back the specific update — that confirms the cause and buys time until Microsoft ships a corrected version."
  - q: "Will the battery come back on its own with the next update?"
    a: "Sometimes. Microsoft occasionally fixes driver regressions in the following cumulative update. But don't wait passively — roll back the bad update or repair the drivers now, because running with no battery backup risks data loss on every power flicker."
---

Everything was normal until Patch Tuesday. The update installed, the laptop restarted, and now the taskbar battery icon carries a red X with the message "No battery is detected." The machine runs fine on the charger but dies the instant you unplug it. The timing isn't a coincidence — something in that update broke the chain of drivers and firmware that lets Windows see your battery.

Unlike generic detection failures, update-caused cases have a clear suspect: the update itself. That changes the strategy. Instead of only resetting hardware, you work the problem from the update side — identifying the KB, repairing what it damaged, rolling it back if needed, and blocking it from reinstalling. Here's the full playbook.

## Why this happens

- **A corrupted ACPI battery driver install.** The update replaced the Microsoft ACPI-Compliant Control Method Battery driver with a version that fails to bind to your hardware.
- **A mismatched chipset or MEI driver.** Updates sometimes push a new Intel/AMD chipset driver that expects newer BIOS firmware than you have, breaking battery communication.
- **Firmware update side effects.** Some updates trigger embedded-controller or BIOS-adjacent changes that leave the battery interface in a bad state.
- **The update changed power-related services.** A disabled or misconfigured power service can prevent battery enumeration at boot.
- **Fast startup cached the broken state.** If the update's final restart used fast startup, the bad battery state got baked into the hibernation file and repeats every boot.
- **Coincidental hardware failure.** Rare, but a battery's controller board can die at any moment — including right after an update. The tests below distinguish this from software causes.

## How to fix it

Work through these in order — they move from the update itself outward to the hardware.

### Fix 1: Identify the suspect update

Knowing the KB number focuses everything that follows.

1. Open **Settings > Windows Update > Update history**.
2. Note the most recent **quality update** and any **driver updates** with install dates matching when the problem appeared.
3. Write down the KB number (e.g., KB5034441).
4. If a driver update for "battery," "chipset," or "firmware" appears, that's your prime suspect. Keep this window in mind for Fix 6.

### Fix 2: Do a true full shutdown to clear the cached state

The update's restart may have saved a broken hardware snapshot via fast startup.

1. Press **Win + R**, type `shutdown /s /t 0`, and press **Enter**.
2. Unplug the charger. If the battery is removable, take it out and hold the power button for 30 seconds.
3. Reconnect everything and power on.
4. If the battery reappears, the update's cached state was the whole problem. Consider [disabling fast startup](/articles/how-to-disable-fast-startup-to-fix-battery-drain-in-windows-11-24h2/) so it can't recur.

### Fix 3: Roll back the battery driver the update installed

Windows keeps the previous driver version around for exactly this situation.

1. Right-click **Start** and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Properties**.
3. Go to the **Driver** tab. If **Roll Back Driver** is clickable, use it, choose a reason, and restart.
4. If the button is greyed out, the update didn't keep a backup — move to Fix 4.
5. After restarting, check whether the battery is detected.

### Fix 4: Uninstall and redetect the battery devices

A clean reinstall forces Windows to rebuild the driver binding from scratch.

1. In **Device Manager**, expand **Batteries**.
2. Right-click and **Uninstall device** on **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
3. Click **Action > Scan for hardware changes** at the top of Device Manager.
4. Windows reinstalls both devices. Restart the laptop fully afterward.
5. If the battery appears, the update's driver install was corrupt and is now repaired.

### Fix 5: Check the BIOS — the update may have exposed a firmware gap

A chipset driver from the update can demand firmware your BIOS doesn't have.

1. Restart and enter BIOS (**F2**, **F10**, **Del**, or **Esc** depending on brand).
2. Check whether the BIOS itself detects the battery. If it does, the hardware is fine and this stays a Windows problem.
3. Note your BIOS version, then check your manufacturer's support site for a newer one — [Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en), [Dell](https://www.dell.com/support).
4. Install the BIOS update with the charger plugged in, then boot into Windows and recheck detection. If the percentage reads wrong afterward, [recalibrate the battery](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 6: Uninstall the problematic update

When the battery vanished the same day an update landed, removing the update is the decisive test.

1. Go to **Settings > Windows Update > Update history > Uninstall updates**.
2. Select the KB you identified in Fix 1 and uninstall it.
3. Restart and check battery detection.
4. If the battery returns, pause updates for 2–3 weeks under **Settings > Windows Update** so the bad update doesn't reinstall overnight.
5. Use the **Show or hide updates** troubleshooter from Microsoft's support site to block that specific KB longer-term. Report the regression in **Feedback Hub** with the KB number.

### Fix 7: Repair the servicing stack as a last software resort

If rolling back isn't possible (some updates can't be uninstalled), repair the component store instead.

1. Open **Terminal (Admin)** and run `DISM /Online /Cleanup-Image /RestoreHealth`. Wait for it to finish — this can take 15–30 minutes.
2. Then run `sfc /scannow` and restart when it completes.
3. After rebooting, repeat Fix 4 (uninstall and redetect the battery devices) so the repaired system files produce clean driver installs.
4. If the battery is still undetected after all of this — and the BIOS can't see it either — the battery pack itself has likely failed and needs replacement.

## Closing

Update-caused detection failures are annoying but very fixable: identify the KB, clear the cached state, repair or roll back the driver, and close the firmware gap. Most users get their battery back by Fix 4 without ever uninstalling anything. And once it's back, keep updates paused just long enough to confirm the fix sticks before letting the next cumulative update through.
