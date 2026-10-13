---
title: "How to Fix Driver Power State Failure on a Lenovo Laptop"
slug: how-to-fix-driver-power-state-failure-on-lenovo-laptop
date: 2026-09-20
categories: ["windows-errors"]
tags: ["bsod", "lenovo", "power", "driver"]
description: "Fix DRIVER_POWER_STATE_FAILURE blue screens on Lenovo laptops with power-plan tweaks, driver updates, and sleep-state repairs."
thumbnail: "/images/thumbs/how-to-fix-driver-power-state-failure-on-lenovo-laptop.webp"
faqs:
  - q: "What does Driver Power State Failure mean?"
    a: "A driver failed to handle a power state transition, such as sleep, hibernate, or wake, within the time Windows allows. The system halted because the driver left a device in an undefined state. It most often happens when waking from sleep or hibernation, and the culprit is usually a network, graphics, or chipset driver."
  - q: "Why does it happen when waking from sleep on Lenovo laptops?"
    a: "Lenovo's power management interacts with drivers during sleep transitions, and an outdated network or graphics driver can fail to wake its device in time. Fast startup and hybrid sleep complicate the transition further. Updating the network and graphics drivers resolves most wake-related cases."
  - q: "Can changing power settings really fix a blue screen?"
    a: "Yes, for this specific stop code. Since the crash is a power-transition failure, preventing the problematic transition, such as disabling fast startup or changing what sleep does, removes the trigger. It is a legitimate fix, not a workaround, when the underlying driver cannot be updated."
  - q: "Is it safe to disable fast startup permanently?"
    a: "Completely safe. Fast startup is a hybrid shutdown that speeds up booting by a few seconds on modern SSDs. Disabling it gives you a true full shutdown every time, which is actually more reliable. Most users notice no meaningful difference in boot speed on an SSD-equipped Lenovo."
---

DRIVER_POWER_STATE_FAILURE is the blue screen of bad naps. It strikes when your Lenovo laptop tries to sleep, hibernate, or wake up, and some driver fails to manage the transition in time. You close the lid, open it later, and instead of your desktop you get a blue screen. Or the laptop crashes the moment it tries to sleep.

The good news: because the trigger is so specific, the fix is usually straightforward. This guide targets the power-transition chain on Lenovo laptops, from the drivers that fail to the settings that provoke them. Work through the fixes in order, and test each one with actual sleep and wake cycles before moving on.

## Why this happens

- **A driver times out during a power transition.** The core cause: a driver does not complete its sleep or wake routine in time.
- **Outdated network drivers.** Wi-Fi drivers failing to reinitialize on wake are the top trigger on Lenovo laptops.
- **Outdated graphics drivers.** GPUs mishandling sleep states cause crashes on lid-close and wake.
- **Fast startup conflicts.** The hybrid shutdown state confuses drivers across power transitions.
- **Corrupted hibernation file.** A damaged hiberfil.sys breaks the hibernate path.
- **Lenovo power management drivers.** Outdated Lenovo power or thermal drivers can mishandle transitions.
- **External devices.** USB devices that do not sleep properly stall the whole transition.

## How to fix it

Work through these in order, testing for stability after each fix before moving on.

### Fix 1: Disable fast startup

Remove the most common trigger first.

1. Open **Control Panel** then **Hardware and Sound** then **Power Options**.
2. Click **Choose what the power buttons do**.
3. Click **Change settings that are currently unavailable**.
4. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
5. Shut down fully (not restart), power on, and test sleep and wake cycles. A full shutdown clears the hybrid state that fast startup was preserving, so this first clean boot is an important part of the test.

### Fix 2: Update network and graphics drivers

Fix the drivers that fail transitions most often.

1. Visit [Lenovo Support](https://support.lenovo.com/us/en/) and download the latest **Wi-Fi**, **Ethernet**, **chipset**, and **graphics** drivers for your model.
2. Install the network drivers first, then chipset, then graphics, restarting between each.
3. For Intel Wi-Fi, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can find the newest version.
4. Test by putting the laptop to sleep and waking it several times. Vary the test: short naps of a minute and longer sleeps of half an hour, since different timeout paths can expose different driver bugs.

### Fix 3: Change the power plan settings

Stop the problematic transitions from occurring.

1. Open **Control Panel** then **Power Options** and click **Change plan settings** on your active plan.
2. Click **Change advanced power settings**.
3. Expand **Sleep** and set **Allow hybrid sleep** to **Off**.
4. Expand **PCI Express** then **Link State Power Management** and set it to **Moderate power savings** instead of Maximum.
5. Expand **Wireless Adapter Settings** then **Power Saving Mode** and set it to **Maximum Performance** on both battery and plugged in.
6. Click **Apply** and **OK**, then test sleep cycles. If a specific setting change brings the crashes back, you have found a trigger worth leaving at its default permanently.

### Fix 4: Disable hibernation and rebuild the hibernation file

Eliminate a corrupted hiberfil.sys.

1. Open **Terminal (Admin)** with **Win + X**.
2. Run `powercfg /h off` to disable hibernation and delete the hibernation file.
3. Restart the laptop.
4. Run `powercfg /h on` to re-enable hibernation with a fresh file.
5. Test hibernate and wake.

### Fix 5: Update the Lenovo BIOS and power drivers

Bring firmware-level power handling current.

1. Check your BIOS version with `msinfo32`.
2. Download the latest BIOS and **Lenovo Power Management** drivers from [Lenovo Support](https://support.lenovo.com/us/en/).
3. Install the BIOS update with the charger connected and nothing else running.
4. Install the power management driver afterward.
5. Test sleep, hibernate, and wake thoroughly. A BIOS update changes low-level behavior, so give each transition type several real-world tests before declaring success.

### Fix 6: Disconnect external devices and update their drivers

Rule out USB devices stalling transitions.

1. Unplug all USB devices, docks, and external drives.
2. Test sleep and wake with nothing attached.
3. If the crashes stop, reconnect devices one at a time to find the culprit.
4. Update that device's driver from its manufacturer.
5. For docks, check the dock maker's site for firmware updates as well.

### Fix 7: Run SFC and DISM

Repair damaged power-management components.

1. Open **Terminal (Admin)**.
2. Run `sfc /scannow` and let it complete.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` if SFC reports unfixable damage.
4. Run `sfc /scannow` again to confirm.
5. Restart and test sleep cycles.

### Fix 8: Reset the power plans to defaults

Clear any corrupted custom power configuration.

1. Open **Terminal (Admin)**.
2. Run `powercfg -restoredefaultschemes` to reset all power plans.
3. Restart.
4. Reapply only the changes you need, testing sleep after each change.
5. If crashes return after a specific change, leave that setting at default.

For the post-update variant, see [driver power state failure after a Windows 11 update](/articles/how-to-fix-driver-power-state-failure-after-windows-11-update/), and for the general Windows 11 guide, our [driver power state failure on Windows 11](/articles/driver-power-state-failure-windows-11-fix/) covers the same ground without brand specifics.

## Closing

DRIVER_POWER_STATE_FAILURE on a Lenovo laptop is a transition problem, so the fixes target transitions: disable fast startup, update the network and graphics drivers that fumble wake-ups, and tune the power plan away from the aggressive settings that provoke them. Test with real sleep and wake cycles, not just restarts, because this error only shows its face when the laptop actually naps. Once the cycles are clean for a week, you can consider the problem solved.
