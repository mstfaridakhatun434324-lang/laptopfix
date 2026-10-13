---
title: "No Battery Detected After a Windows Update on Windows 10: 7 Fixes"
slug: how-to-fix-no-battery-detected-after-windows-update-on-windows-10
date: 2026-10-10
categories: ["battery"]
tags: ["battery", "not detected", "windows update", "windows 10"]
description: "Windows 10 update made your battery vanish? Follow these 7 fixes — driver rollback, update uninstall, and EC reset — to bring it back."
thumbnail: "/images/thumbs/how-to-fix-no-battery-detected-after-windows-update-on-windows-10.webp"
faqs:
  - q: "Why does Windows 10 stop detecting the battery after an update?"
    a: "Updates overwrite the ACPI battery driver and chipset drivers. If the new driver doesn't match your hardware or the install corrupts, Windows can't communicate with the battery controller and reports no battery detected. The battery itself is usually fine."
  - q: "How do I uninstall a Windows 10 update that broke my battery?"
    a: "Go to Settings > Update & Security > Windows Update > View update history > Uninstall updates, select the recent update, and uninstall it. Restart afterward. Then pause updates for a week or two so it doesn't reinstall before you've confirmed the fix."
  - q: "Is System Restore safe for fixing battery detection?"
    a: "Yes — System Restore rolls back system files, drivers, and registry changes without touching your personal files. Pick a restore point from before the update installed. It's one of the safest recovery tools Windows 10 offers."
  - q: "What if the BIOS doesn't detect the battery either?"
    a: "Then it's a hardware problem, not Windows. The battery's internal controller may have failed, the internal connector may be loose (on sealed models), or the motherboard's charging circuit has an issue. A repair shop can test with a known-good battery."
---

You installed a routine Windows 10 update, the laptop restarted, and now there's a red X over the battery icon: "No battery is detected." The charger keeps the machine alive, but unplugging it kills the laptop instantly. On Windows 10 this scenario is well documented — the update pipeline, the driver servicing, and the older power management stack combine to produce exactly this failure more often than on newer Windows.

The fix strategy is classic Windows 10: use the built-in recovery tools the OS still does well — driver rollback, update uninstall, System Restore — plus the hardware resets that clear stuck controller states. Seven fixes, ordered by effort.

## Why this happens

- **The update replaced the ACPI battery driver with a bad copy.** The Microsoft ACPI-Compliant Control Method Battery driver is the OS's only window into the battery; a corrupt install blinds it.
- **A pushed chipset driver mismatches the BIOS.** Windows 10 updates sometimes deliver chipset drivers that assume newer firmware, breaking the battery interface.
- **Fast startup preserved the broken state.** Windows 10's hybrid shutdown is aggressive about caching hardware states, and the update's restart can lock in a bad battery snapshot.
- **The embedded controller got stuck mid-update.** If the update touched power management at the firmware level, the EC can hang and stop reporting the battery.
- **A pending update left the driver store inconsistent.** Interrupted or partially installed updates can leave two half-registered driver versions fighting over the battery device.
- **The battery genuinely failed.** Least likely right after an update, but possible — the controller board inside the pack can die at any time.

## How to fix it

Work through these in order.

### Fix 1: Run a full shutdown and power drain

Clear the fast-startup cache before touching anything else.

1. Press **Win + R**, type `shutdown /s /t 0`, and press **Enter**.
2. Unplug the charger. Remove the battery if it's removable; if not, just leave the machine off.
3. Hold the power button for 30–60 seconds to drain residual power from the motherboard and embedded controller.
4. Reconnect the charger (reinsert the battery first if you removed it) and power on.
5. Check the battery icon. If Windows sees the battery now, you're done — and consider turning fast startup off permanently under **Control Panel > Power Options > Choose what the power buttons do**.

### Fix 2: Roll back the battery driver

If the update shipped a new driver version, the old one is still available.

1. Right-click **Start**, open **Device Manager**, and expand **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery** and open **Properties**.
3. On the **Driver** tab, click **Roll Back Driver** if it's available, pick a reason, and restart.
4. Also check **System devices** for anything battery-related with a recent driver date and roll that back too.
5. Verify detection after the restart.

### Fix 3: Uninstall and rescan the battery devices

Force Windows to rebuild the driver installation cleanly.

1. In **Device Manager > Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**. Confirm.
2. Do the same for **Microsoft AC Adapter**.
3. Click **Action > Scan for hardware changes**. Windows reinstalls both.
4. Shut down fully, wait 30 seconds, and boot. Check the icon.

### Fix 4: Uninstall the offending Windows update

Match the failure date to the update history, then remove it.

1. Open **Settings > Update & Security > Windows Update > View update history**.
2. Note the most recent **Quality Update** KB number and its install date.
3. Click **Uninstall updates**, select that KB, and uninstall it.
4. Restart the laptop and check for the battery.
5. If it returns, go to **Settings > Update & Security > Windows Update > Advanced options** and pause updates for 7–14 days. If the battery still misbehaves on charge, [calibrate it to restore accurate readings](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 5: Use System Restore to before the update

When you can't pinpoint the KB, restore the whole system state.

1. Press **Win + R**, type `rstrui`, and press **Enter**.
2. Choose **Choose a different restore point** and pick one dated before the update installed.
3. Confirm and let the restore complete — the laptop will restart.
4. Your personal files are untouched; only system files, drivers, and registry settings roll back.
5. Check battery detection after the restore finishes.

### Fix 6: Update the BIOS to match the new drivers

Sometimes the right move is forward, not back — the update's drivers may need newer firmware.

1. Press **Win + R**, type `msinfo32`, press **Enter**, and note the **BIOS Version/Date**.
2. On the manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — check for a newer BIOS for your exact model.
3. Install it with the charger connected; don't interrupt the flash.
4. Also install the latest **chipset driver** from the same page.
5. Reboot and check detection. Newer BIOS versions often include embedded-controller fixes that restore battery communication.

### Fix 7: Test the battery in BIOS diagnostics

Determine definitively whether it's hardware.

1. Restart and enter your brand's diagnostics — **F12 > Diagnostics** on Dell, **F2 > Component Tests > Battery** on HP, **F10 > Diagnostics** on Lenovo.
2. Run the battery test. If the diagnostic also reports no battery, the pack's controller has failed or the internal connection is broken.
3. If diagnostics see the battery but Windows doesn't, reinstall the chipset driver package from the manufacturer and repeat Fix 3.
4. A failed diagnostic means it's time for a replacement battery — and [checking design vs full charge capacity](/articles/how-to-check-battery-design-vs-full-charge-capacity-on-windows-10/) on the new pack gives you a baseline for its health.

## Closing

Windows 10's update-caused detection failures almost always yield to one of the software fixes above — full shutdown, driver rollback, update uninstall, or System Restore. Only when the BIOS diagnostics also draw a blank should you spend money on hardware. Once the battery is back, keep a restore point handy before the next big update, just in case history repeats itself.
