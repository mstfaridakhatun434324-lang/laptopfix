---
title: "How to Enable Hidden Devices in Device Manager on Windows 11 24H2"
slug: "how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2"
date: "2026-10-09"
categories: ["drivers"]
tags: ["hidden devices", "device manager", "windows 11 24h2", "ghost devices", "show hidden devices"]
description: "Learn how to show hidden devices in Device Manager on Windows 11 24H2, why ghost devices matter, and how to safely clean them up to fix driver problems."
thumbnail: "/images/thumbs/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2.webp"
faqs:
  - q: "How do I show hidden devices in Device Manager on Windows 11 24H2?"
    a: "Open Device Manager (Windows key + X > Device Manager), click the View menu, and select Show hidden devices. Grayed-out entries appear for devices that are installed but not currently connected or enumerated. This works identically on 24H2 as on earlier Windows 11 versions."
  - q: "What are ghost devices and should I delete them?"
    a: "Ghost devices are driver entries for hardware not currently present — old USB devices, previously installed GPUs, or failed adapters. Deleting ghosts for devices you no longer use is safe and often fixes conflicts. Never delete grayed-out entries for hardware that is physically present but failing; those need driver repair, not deletion."
  - q: "Why do I need the devmgr_show_nonpresent_devices variable?"
    a: "The basic Show hidden devices view reveals disconnected Plug-and-Play devices, but truly removed devices (like an old graphics card) need the environment variable devmgr_show_nonpresent_devices=1 set before launching Device Manager. This exposes the full ghost list for thorough cleanup after hardware changes."
  - q: "Can deleting hidden devices break my system?"
    a: "Deleting ghosts of removed hardware is safe — Windows reinstalls drivers when hardware reconnects. The risk is deleting a grayed-out entry for hardware that is present but temporarily undetected (like a failing Bluetooth radio); that just removes its driver, which you can reinstall. When in doubt, create a restore point first."
---

Device Manager's **View > Show hidden devices** option is one of the most powerful — and most misunderstood — troubleshooting tools in Windows 11 24H2. Behind that single menu toggle lies the full history of every device driver Windows has ever installed: disconnected USB drives, old graphics cards, failed Bluetooth radios, and phantom network adapters. Learning to read this ghost layer is often the difference between guessing at a driver problem and seeing it.

On 24H2 specifically, hidden devices matter more than usual. The 24H2 upgrade migrates drivers between OS builds, and that migration leaves behind non-present entries that can conflict with new installations — a factor in Bluetooth disappearances, monitor detection failures, and audio problems after the upgrade. This guide covers showing hidden devices, interpreting what you see, and cleaning up safely.

## Why this happens

- **Non-present device entries accumulate**: every USB device, dock, and adapter you have ever connected leaves a driver entry behind when unplugged.
- **24H2 driver migration orphans entries**: the upgrade process can orphan old driver entries that conflict with freshly installed ones.
- **Failed devices hide as ghosts**: a Bluetooth radio or GPU that fails enumeration appears grayed-out — present in the driver store but not on the bus.
- **Duplicate entries confuse Windows**: two driver entries for one physical device (common after updates) can deadlock installation and enumeration.
- **Stale monitor and audio endpoints**: previously connected displays and headsets leave entries that block re-detection of the same hardware.
- **Driver-store bloat**: hundreds of ghost entries slow Device Manager operations and complicate driver troubleshooting.
- **Hidden system devices**: 24H2 also hides low-level system devices by default, some of which matter for advanced diagnostics.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable Show hidden devices (the basic view)

This is the foundation everything else builds on. The basic hidden-devices view reveals disconnected Plug-and-Play devices and failed-but-installed adapters — enough for most troubleshooting.

1. Press **Windows key + X** and select **Device Manager**.
2. Click the **View** menu and select **Show hidden devices** — a checkmark appears next to it.
3. Expand categories relevant to your problem: **Bluetooth**, **Network adapters**, **Sound, video and game controllers**, **Monitors**, **Universal Serial Bus controllers**.
4. Grayed-out icons indicate non-present devices; normal icons with warning symbols indicate present-but-faulty devices.
5. Note what you find before changing anything — a grayed-out Bluetooth adapter, for example, tells you the driver is installed but the radio is not enumerating, directing you to [our Bluetooth enumeration guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-11/).

### Fix 2: Expose the full ghost list with the environment variable

The basic view misses devices removed long ago or never fully installed. The `devmgr_show_nonpresent_devices` variable forces Device Manager to show every ghost in the driver store.

1. Press **Windows key + R**, type `cmd`, and press **Ctrl + Shift + Enter** for an elevated prompt (or just run normally — elevation is not required for viewing).
2. Type `set devmgr_show_nonpresent_devices=1` and press Enter.
3. In the same window, type `start devmgmt.msc` to launch Device Manager with the variable active.
4. Click **View > Show hidden devices** in this instance.
5. Compare with the basic view — the additional grayed-out entries (old GPUs under Display adapters, ancient USB devices) are the deep ghosts this variable reveals.

### Fix 3: Identify which ghosts are safe to remove

Not every grayed-out entry should be deleted. The rule: remove ghosts of hardware that is gone; repair (don't delete) entries for hardware that is present but failing.

1. For each grayed-out entry, ask: is this hardware still in/on the computer? Old USB flash drives, replaced graphics cards, and long-gone printers are safe to remove.
2. Grayed-out entries for built-in hardware (Bluetooth radio, integrated camera, internal Wi-Fi) indicate a present-but-failing device — these need driver reinstallation, not deletion.
3. When unsure, right-click the entry, open **Properties > Details > Last known parent** or check the driver date for clues about its age.
4. Create a system restore point before any bulk deletion (**System Properties > System Protection > Create**).
5. Delete ghosts one category at a time, rescanning (**Action > Scan for hardware changes**) between categories to catch mistakes early.

### Fix 4: Clean ghost Bluetooth and network adapters

Bluetooth and network ghosts are the most common troublemakers — stale entries here directly cause "adapter disappeared" and "device cannot start" errors after 24H2 upgrades.

1. With hidden devices shown, expand **Bluetooth** and **Network adapters**.
2. Uninstall every grayed-out Bluetooth and wireless entry, ticking "Attempt to remove the driver for this device" only for entries you are sure are obsolete.
3. Expand **Universal Serial Bus controllers** and remove grayed-out USB composite devices tied to old Bluetooth dongles.
4. Click **Action > Scan for hardware changes** and let Windows re-enumerate the real, present hardware.
5. Reinstall the manufacturer's current Bluetooth/wireless driver afterward — a clean enumeration plus a fresh driver resolves the conflicts that ghost entries caused, as detailed in [our 24H2 Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-in-windows-11-24h2/).

### Fix 5: Clean ghost display and monitor entries

Stale monitor entries block re-detection of displays, and ghost GPU entries (from a replaced card or a driver migration) cause "device cannot start" errors. 24H2 upgrades are prolific producers of these.

1. Expand **Monitors** with hidden devices shown and uninstall grayed-out entries for displays you no longer connect.
2. Expand **Display adapters** — uninstall grayed-out GPU entries only if the hardware was physically replaced or removed.
3. Never uninstall the grayed-out entry for your current GPU if it is present but failing; instead reinstall its driver.
4. Scan for hardware changes and let Windows rediscover connected monitors.
5. If a monitor still fails detection, the cleaned enumeration often lets the **Detect** button in **Settings > System > Display** succeed where it previously found nothing — see [our monitor detection guide](/articles/how-to-fix-laptop-not-detecting-second-monitor-after-windows-11-update/).

### Fix 6: Clean ghost audio endpoints

Old headsets, USB audio devices, and HDMI audio endpoints accumulate as ghosts and can prevent new audio devices from becoming the default — or from appearing at all.

1. Expand **Sound, video and game controllers** and **Audio inputs and outputs** with hidden devices shown.
2. Uninstall grayed-out entries for headsets, USB DACs, and monitor audio you no longer use.
3. Leave the entries for your built-in speakers and microphone alone unless they are faulty.
4. Scan for hardware changes, then open **Sound settings** and verify the device list is clean.
5. Reconnect your current audio devices and set defaults fresh — the cleaned endpoint list eliminates the stale-entry conflicts behind many [headphone detection failures](/articles/how-to-fix-laptop-not-detecting-headphones-after-windows-11-update/).

### Fix 7: Use Device Manager's hidden system devices for deep diagnosis

Beyond ghosts, Device Manager can show hidden system devices — the low-level drivers and bus enumerators that underpin everything. This is advanced territory, but occasionally the fault is here.

1. With the environment variable set (Fix 2), also examine **System devices** for grayed-out bus enumerators.
2. Look for warning icons on PCI bus, ACPI, or USB host controller entries — these indicate platform-level problems affecting all child devices.
3. Do not uninstall system-device entries casually; instead, update their drivers or check for BIOS updates.
4. For persistent platform issues, check [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for known 24H2 device-enumeration issues.
5. If system-device entries show faults across the board after a 24H2 upgrade, a chipset driver reinstall from your laptop manufacturer's support page — or an in-place Windows repair from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) — is the appropriate escalation.

## Closing

Hidden devices are Device Manager's memory, and on Windows 11 24H2 that memory is longer — and more conflict-prone — than ever thanks to driver migration. The basic **Show hidden devices** toggle plus the `devmgr_show_nonpresent_devices` variable give you full visibility; the judgment call is knowing which ghosts to exorcise and which grayed-out entries are actually cries for driver help. Clean the true ghosts, repair the failing present devices, and rescan — most "mysterious" post-24H2 device problems turn out to be enumeration conflicts that this cleanup dissolves.
