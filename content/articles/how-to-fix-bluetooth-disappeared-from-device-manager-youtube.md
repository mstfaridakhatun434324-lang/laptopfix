---
title: "How to Fix Bluetooth Disappeared From Device Manager (Complete Guide)"
slug: how-to-fix-bluetooth-disappeared-from-device-manager-youtube
date: 2026-09-26
categories: ["drivers"]
tags: ["bluetooth disappeared", "device manager", "bluetooth driver", "windows 11"]
description: "Bluetooth vanished from Device Manager completely? Six fixes that restore the Bluetooth adapter, from power drains to BIOS toggles and driver reinstalls."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-disappeared-from-device-manager-youtube.webp"
faqs:
  - q: "Why would Bluetooth disappear from Device Manager entirely instead of just showing an error?"
    a: "Complete disappearance means Windows isn't enumerating the Bluetooth radio at all — the USB-attached Bluetooth module isn't presenting itself to the OS. This happens when the module is stuck in a bad power state, disabled at the BIOS level, or its USB enumeration failed after an update. It's actually a cleaner diagnostic than an error code: the problem is at the enumeration/power layer, not in the Bluetooth protocol stack."
  - q: "My Bluetooth toggle is also gone from Settings. Is that the same problem?"
    a: "Yes — the Settings toggle only appears when Windows detects a Bluetooth radio. No radio in Device Manager means no toggle in Settings; they're two views of the same absence. Don't chase the Settings toggle as a separate issue. Fix the Device Manager enumeration with this guide, and the Settings toggle returns automatically once the radio is detected."
  - q: "Can a Windows update really make the Bluetooth hardware invisible?"
    a: "It can make it invisible to Windows, which looks identical from your side. Updates can wedge the Bluetooth module's power state, install a broken USB driver that the Bluetooth module depends on, or reset a BIOS setting. The hardware is almost always fine — this is why the full power drain in this guide (which resets the module's hardware state) fixes so many 'disappeared' cases that driver reinstalls can't."
  - q: "How do I know if my laptop actually has Bluetooth?"
    a: "Check the specs for your exact model on the vendor's site — nearly all modern laptops include Bluetooth via the Wi-Fi card (Intel AX201/AX210 and similar combine Wi-Fi and Bluetooth on one module). If the specs confirm Bluetooth and it ever worked, its absence is a software/power problem. Only the cheapest or oldest netbooks lack it, in which case a USB Bluetooth adapter is the answer."
---

Bluetooth was there yesterday — the toggle, the paired devices, all of it — and today Device Manager shows no Bluetooth section at all, as if the radio never existed. Not an error, not a warning icon: absence. This is one of the most disorienting Windows problems because there's nothing to click on, nothing to update, nothing to troubleshoot in the usual sense. The device isn't broken; it's *unenumerated*.

Here's the key technical fact: on almost all modern laptops, Bluetooth lives on the Wi-Fi card (Intel AX201/AX210, MediaTek, Realtek combos) and connects to the system via an internal USB interface. "Disappeared from Device Manager" means that USB enumeration failed or the module is wedged in a power state where it won't announce itself. The fixes therefore target enumeration and power state — not the Bluetooth protocol stack, which never even gets involved. If your Bluetooth shows up but won't *work* (a different problem), the [Bluetooth not working guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-after-windows-11-update/) covers that side; for the Intel combo-card angle specifically, see the [Intel Wi-Fi 6 AX201 fix guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/).

## Why this happens

- **The Bluetooth module is wedged in a bad power state.** Modern standby transitions can leave the combo card's Bluetooth USB interface unresponsive until fully power-cycled.
- **A Windows update broke USB enumeration.** The update changed the USB hub driver the internal Bluetooth interface depends on, so the radio never enumerates.
- **The BIOS Bluetooth/WLAN toggle got reset.** Some laptops have a BIOS-level wireless toggle; the update process reset it, disabling the radio in hardware.
- **Fast Startup preserved the wedged state.** The "shutdown" wasn't a real shutdown, so the bad hardware state survived across reboots.
- **The Wi-Fi card driver is corrupt.** Since Bluetooth shares the physical card with Wi-Fi, a broken Wi-Fi driver package can take Bluetooth enumeration down with it.
- **Airplane mode or the physical wireless switch is stuck.** A stuck Fn wireless toggle or airplane-mode state can suppress the radio at a low level.
- **The card itself loosened or failed.** Rare: the M.2 combo card unseated (after a drop) or the Bluetooth portion of the silicon failed while Wi-Fi survives.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Perform a full power drain (not a restart)

Reset the module's hardware state — this fixes the majority of cases.

1. Shut down the laptop completely. Then hold **Shift** while clicking **Shut down** to bypass Fast Startup, ensuring a true power-off.
2. Unplug the charger and all USB devices.
3. Hold the power button down for a full 30 seconds (drains residual power and resets embedded controllers).
4. Plug the charger back in, boot normally, and open Device Manager — check for the **Bluetooth** section. This clears the wedged power state that survives normal restarts.

### Fix 2: Disable Fast Startup permanently

Stop the wedged state from being preserved across shutdowns.

1. **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable**.
2. Uncheck **Turn on fast startup (recommended)** and save.
3. Shut down fully (not restart) and power back on.
4. Check Device Manager for Bluetooth. Fast Startup's hibernation-style shutdowns are a notorious preserver of bad device states.

### Fix 3: Check BIOS wireless settings

Verify the radio isn't disabled below the OS.

1. Restart into BIOS/UEFI setup (F2/Del/F12/Esc depending on vendor).
2. Look under **Advanced**, **Security**, or **Devices** for **Bluetooth**, **Wireless**, or **WLAN/Bluetooth** toggles — ensure they're **Enabled**.
3. Also check for an **Airplane mode** or **wireless** hotkey lock state.
4. Save and exit. If Bluetooth was disabled here, it'll enumerate on the next boot — then update its driver (Fix 4) to keep it healthy.

### Fix 4: Reinstall the Wi-Fi/Bluetooth combo driver

Fix the driver package the radio depends on.

1. In Device Manager, expand **Network adapters** — find your Wi-Fi card (Intel Wi-Fi 6 AX201, etc.).
2. Right-click > **Uninstall device** (check **Attempt to remove the driver**).
3. Download the full Wi-Fi + Bluetooth driver package: Intel users get it from the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html); others from the laptop vendor ([Dell](https://www.dell.com/support), HP, or [Lenovo](https://support.lenovo.com/us/en/)).
4. Install the package (it includes both Wi-Fi and Bluetooth drivers), restart, and verify the Bluetooth section returns.

### Fix 5: Uncover hidden devices and rescan

Catch the radio in a hidden or failed state.

1. In Device Manager, click **View** > **Show hidden devices**.
2. Look under **Bluetooth** (if the section appears grayed) and **Universal Serial Bus controllers** for grayed-out or warning-marked entries — uninstall them.
3. Click **Action** > **Scan for hardware changes** to force re-enumeration.
4. If a Bluetooth entry appears with an error code, note the code — Code 43/45 here usually resolves with the Fix 4 driver reinstall.

### Fix 6: Toggle airplane mode and check the wireless switch

Clear stuck radio states.

1. Press **Win + A** and toggle **Airplane mode** on, wait 10 seconds, toggle it off.
2. Try the laptop's wireless Fn key (often **Fn + F2** or a dedicated key with an antenna icon) — press it and watch for an on-screen indicator.
3. Check for a physical wireless switch on the laptop's edge (rare on modern machines, but some business laptops still have them).
4. After toggling, do a full shutdown (not restart) and boot — then recheck Device Manager. If Bluetooth is back but misbehaves, the [post-update Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-in-windows-11-24h2/) covers the functional-repair side.

## Closing

Bluetooth disappearing from Device Manager is an enumeration and power-state problem, not a Bluetooth problem — which is why the fixes look nothing like Bluetooth troubleshooting. Full power drain, kill Fast Startup, check the BIOS toggle, reinstall the combo driver: in that order, the radio that "vanished" reappears. The hardware was there all along; Windows just needed to be forced to look properly.
