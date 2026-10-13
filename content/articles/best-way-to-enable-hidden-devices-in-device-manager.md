---
title: "Best Way to Enable Hidden Devices in Device Manager"
slug: best-way-to-enable-hidden-devices-in-device-manager
date: 2026-10-06
categories: ["drivers"]
tags: ["device manager", "hidden devices", "windows", "troubleshooting", "drivers"]
description: "Learn the best way to enable hidden devices in Device Manager: reveal ghost hardware, remove stale drivers, and fix phantom device problems."
thumbnail: "/images/thumbs/best-way-to-enable-hidden-devices-in-device-manager.webp"
faqs:
  - q: "How do I show hidden devices in Device Manager?"
    a: "Open Device Manager, click View > Show hidden devices. For the complete view, open an elevated Command Prompt, run 'set devmgr_show_nonpresent_devices=1', then launch Device Manager from the same window with 'start devmgmt.msc' — this reveals non-present devices the menu option misses."
  - q: "Is it safe to uninstall grayed-out devices?"
    a: "Generally yes for hardware you recognize and no longer use — grayed entries are disconnected devices. Never uninstall hidden entries under System devices, Computer, or Processors, and leave WAN Miniport and Microsoft virtual adapters alone. When unsure, disable instead of uninstall."
  - q: "Why does my USB device fail to install repeatedly?"
    a: "A ghost entry from a previous failed install is likely holding the driver binding. Reveal hidden devices, uninstall the grayed-out entries for that device under USB controllers and related categories, reboot, then plug the device in for a clean enumeration."
  - q: "What are WAN Miniport devices in hidden view?"
    a: "They are Windows' built-in virtual network adapters for VPN, PPPoE, and legacy dial-up protocols, and they appear normally in the hidden and devices-by-connection views. Leave them alone — removing them breaks VPN functionality, and Windows recreates them on the next boot anyway."
---

Device Manager hides devices by default — disconnected USB hardware, failed driver installs, and 'ghost' entries from hardware you removed months ago. The 'Show hidden devices' view reveals all of them, and it's one of the most useful diagnostic views in Windows that most people never open.

Why does this matter for troubleshooting? Because ghost devices hold onto drivers, COM port numbers, and hardware IDs that block new hardware from installing cleanly. A USB device that won't install, a network adapter with a phantom duplicate, a printer holding a port hostage — the hidden-devices view is where you find the squatters.

This guide covers the proper way to reveal hidden devices, how to interpret what you see, and the safe cleanup that fixes real problems.

A quick mental model before you begin: Device Manager's normal view answers what is working right now, while the hidden-devices view answers what has ever been here. Troubleshooting lives in the gap between those two answers — the ghost entries in that gap are what block reinstalls, hold port numbers, and confuse driver installers.

## Why this happens

- **View filter hiding non-present devices:** Device Manager's default view only shows currently connected hardware; everything else is filtered out, not gone.
- **Ghost drivers blocking reinstalls:** A failed device's driver binding persists as a hidden entry and conflicts when you reinstall the device.
- **Stale COM port assignments:** Removed USB serial devices keep their COM port numbers as hidden entries, causing 'port in use' errors for new devices.
- **Duplicate network adapters:** Old WiFi/Ethernet adapters linger hidden and confuse driver installers and network profiles.
- **Failed installs leaving phantom entries:** Interrupted driver installations create half-registered hidden devices that block clean reinstalls.
- **Disabled devices vs hidden devices:** A device you disabled shows grayed in normal view; a disconnected one only appears in hidden view — different fixes.
- **Driver store bloat:** Every hidden ghost ties to driver packages in the store; mass cleanup sometimes requires store-level removal.
- **Misreading normal hidden entries:** Many hidden entries (system devices, WAN miniports) are normal — deleting the wrong ones breaks things.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable the hidden devices view properly

There's the menu option — and then there's the thorough method.

1. Open **Device Manager** (Win+X → Device Manager).
2. Click **View → Show hidden devices**. Disconnected and ghost devices now appear grayed out.
3. For the complete view including all non-present devices, set the environment variable first: open an elevated Command Prompt and run **set devmgr_show_nonpresent_devices=1**, then **start devmgmt.msc** from the same window.
4. Compare the two views — the environment-variable method reveals entries the menu option misses.

### Fix 2: Learn to read the ghost entries

Not every grayed entry is a problem. Learn the taxonomy before deleting anything.

1. Grayed-out entries = not currently present. These are safe to inspect and usually safe to remove if you recognize the hardware.
2. Entries with warning icons = present but failing. These are your actual troubleshooting targets.
3. **WAN Miniport**, **System devices**, and Microsoft virtual entries are normal — leave them alone.
4. Focus on ghosts in the category matching your problem: **Network adapters** for WiFi issues, **USB controllers** for USB issues, **Ports (COM & LPT)** for serial issues.

### Fix 3: Remove ghost USB devices blocking reinstalls

The classic fix for USB hardware that refuses to install.

1. In the hidden view, expand **Universal Serial Bus controllers**.
2. Right-click each **grayed-out** entry for your problem device type → **Uninstall device**.
3. Expand **Disk drives** and **Human Interface Devices** and clear ghosts of the same device there too.
4. Unplug the device, reboot, then plug it back in for a truly clean enumeration. This pairs well with our [USB troubleshooting steps](/articles/how-to-turn-off-usb-selective-suspend-on-windows-11/).

### Fix 4: Free stuck COM port numbers

For 'COM port in use' errors with USB serial adapters.

1. Hidden view → **Ports (COM & LPT)** → note which COM numbers are taken by grayed-out ghosts.
2. Uninstall the ghost port entries to release their numbers.
3. For the active device, open **Properties → Port Settings → Advanced** and reassign it to a freed COM number.
4. If ports still conflict, the assignment lives in the registry — but ghost cleanup resolves it 95% of the time.

### Fix 5: Clear phantom network adapters

Ghost NICs cause duplicate network profiles and driver installer confusion.

1. Hidden view → **Network adapters** → uninstall grayed-out WiFi/Ethernet entries for adapters no longer in the machine.
2. Then open **Device Manager → View → Devices by connection** to spot adapters bound to removed hardware.
3. Reinstall the current adapter's driver fresh afterward so it binds without the phantom competing.
4. If WiFi is missing entirely rather than duplicated, see [adapter missing fixes](/articles/how-to-fix-wifi-adapter-not-showing-up-step-by-step/).

### Fix 6: Clean the driver store for stubborn ghosts

When uninstalling the ghost doesn't stick because the driver package reloads it. Sometimes evicting the ghost is not enough: Windows keeps the driver package in its driver store, and the next hardware scan resurrects the phantom from the stored INF. The pnputil commands below remove the package itself, which is the only way to make the deletion permanent. Always note the OEM INF number before deleting — removing the wrong package disables working hardware.

1. Open an elevated Command Prompt and run **pnputil /enum-drivers** to list third-party driver packages.
2. Identify the OEM inf for the ghost hardware (check the ghost's **Properties → Driver → Driver Details** for the inf name).
3. Remove it with **pnputil /delete-driver oemXX.inf /uninstall** (replace oemXX with the actual number).
4. Reboot and verify the ghost is gone from the hidden view.

### Fix 7: Know what NOT to delete

Enthusiastic cleanup breaks systems. The guardrails:

1. Never uninstall hidden entries under **System devices**, **Computer**, or **Processors** — these are live system components shown grayed for other reasons.
2. Leave **WAN Miniport** entries and **Microsoft** virtual adapters alone.
3. Don't delete a ghost for hardware still in the machine that you plan to keep using — uninstalling it just forces a reinstall.
4. When in doubt, **Disable** instead of **Uninstall** — disabling is reversible with one click.

## Closing

The hidden-devices view turns Device Manager from a status display into a diagnostic instrument. The discipline is simple: reveal everything with the environment-variable method, read before you delete, clear ghosts only in the category matching your problem, and never touch system devices. Most 'device won't install' mysteries end the moment the squatting ghost is evicted. Microsoft documents Device Manager views and driver management at [Windows support](https://support.microsoft.com/en-us/windows).
