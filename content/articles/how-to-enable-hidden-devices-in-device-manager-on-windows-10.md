---
title: "Reveal Hidden and Ghosted Devices in Device Manager on Windows 10"
slug: how-to-enable-hidden-devices-in-device-manager-on-windows-10
date: 2026-09-30
categories: ["drivers"]
tags: ["device manager", "hidden devices", "ghost devices", "windows 10", "driver troubleshooting"]
description: "Learn how to show hidden devices in Device Manager on Windows 10, clean up grayed-out ghost entries, and fix phantom hardware conflicts."
thumbnail: "/images/thumbs/how-to-enable-hidden-devices-in-device-manager-on-windows-10.webp"
faqs:
  - q: "Why can't I see some devices in Device Manager on Windows 10?"
    a: "Device Manager hides any device that is not currently connected, so phones, USB drives, docks, and old network adapters only appear as grayed-out ghost entries after you enable View, then Show hidden devices. Without that toggle, the entire hidden layer stays invisible, which is why a conflicting phantom driver can block new hardware while remaining completely out of sight."
  - q: "Is it safe to delete grayed-out devices in Device Manager?"
    a: "Yes, provided the hardware is genuinely gone from your setup. Uninstalling a ghosted entry removes its leftover driver binding and frees the resources it was squatting on. Never delete grayed entries for components still inside the laptop, such as a temporarily disabled Wi-Fi adapter, because Windows will simply recreate the node or lose the device configuration."
  - q: "What is the devmgr_show_nonpresent_devices command?"
    a: "It is an environment variable that forces Device Manager to expose nonpresent device nodes. Open Command Prompt, run set devmgr_show_nonpresent_devices=1, then launch devmgmt.msc from the same window. The resulting Device Manager instance reveals ghost entries that even the View menu toggle misses, giving you the deepest native view available."
  - q: "Why do hidden devices keep reappearing after I delete them?"
    a: "Because the driver package is still staged in the Windows driver store, so the system rebuilds the device node at the next boot or hardware scan. Deleting the entry alone never removes the package. To stop the resurrection loop, check Delete the driver software during uninstall or run pnputil /delete-driver against the staged oem.inf package."
---

Device Manager on Windows 10 does not show you everything installed on your laptop. By design, it hides devices that are not currently connected — old USB drives, a phone you plugged in once, a dock you returned, even network adapters from a previous motherboard driver install. These ghosted entries sit in the background, and they are one of the most common sources of phantom driver conflicts.

When a new piece of hardware refuses to install properly, or Windows claims a device is already in use, the culprit is very often a hidden duplicate occupying the same driver slot. Learning how to reveal and clean up these hidden devices takes about five minutes and solves an entire class of problems: code 10 errors, USB devices that install endlessly, Bluetooth adapters that vanish, and printers that appear twice. If you are a technician chasing an elusive conflict, this is always step one.

## Why this happens

- **Non-present devices are ghosted, not removed:** When you unplug a USB device, Windows keeps its device node marked as "not present." It only becomes visible when hidden devices are shown.
- **The View toggle defaults to off:** Device Manager's standard view hides ghosted and disconnected entries, so the list looks clean while stale entries pile up underneath.
- **Phantom driver assignments cause conflicts:** A new device that matches an old ghosted entry can inherit the wrong driver or fail to claim its resources, producing install errors.
- **USB enumeration leaves residue:** Every USB port remembers devices it has seen. Swap one flash drive between ports and you create multiple hidden entries for a single drive.
- **Driver upgrades orphan old entries:** Installing a new driver version sometimes leaves the old device node behind, especially with network and audio drivers.
- **Fast Startup changes enumeration:** Windows 10 Fast Startup skips full hardware re-enumeration, so Device Manager's view of "present" hardware can lag reality after sleep or hibernate.
- **Registry enum keys persist:** Device instance paths under the Enum registry keys survive the unplug event, and Device Manager reads them when hidden devices are shown.
- **Staged driver packages reinstall ghosts:** Even after you delete a hidden entry, Windows can recreate it from the driver store at next boot if the driver package is still staged.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle "Show hidden devices" from the View menu

1. Press **Win + X** and select **Device Manager**.
2. Click **View** in the menu bar, then click **Show hidden devices**.
3. Scroll through each category. Devices that are not currently present appear grayed out or semi-transparent.
4. This single toggle is enough for most diagnosis — if the problem device shows up grayed, you now know Windows thinks it is disconnected, which points to a detection issue rather than a driver issue. For related checks, see how to [check driver versions in Device Manager](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/).

### Fix 2: Launch Device Manager as an administrator

1. Press **Win + S**, type **Device Manager**, right-click it, and choose **Run as administrator**.
2. Confirm the UAC prompt.
3. With elevated rights, uninstall and driver-store operations on hidden devices actually complete instead of failing silently — grayed entries that refuse to delete in a normal session usually delete cleanly here.

### Fix 3: Force full non-present visibility with the environment variable

1. Open **Command Prompt** (not PowerShell — the variable syntax differs).
2. Type `set devmgr_show_nonpresent_devices=1` and press Enter.
3. In the same window, type `devmgmt.msc` and press Enter.
4. Device Manager opens in a special mode that exposes every nonpresent device node, including ones the View toggle misses.
5. Keep this window open while you work — the variable only applies to the Device Manager instance launched from that prompt.

### Fix 4: Uninstall grayed-out ghost devices safely

1. With hidden devices visible, expand each category and look for dimmed icons.
2. Right-click a grayed entry you no longer use — an old USB drive, a returned dock — and choose **Uninstall device**.
3. If the dialog offers **Delete the driver software for this device**, check it when you want the driver gone permanently (for example, a printer driver from a printer you no longer own).
4. Work category by category. Never uninstall grayed entries for hardware still inside the laptop, like a disabled internal Wi-Fi adapter — disabling is not the same as absent.
5. Restart after a cleanup round so enumeration starts fresh.

### Fix 5: Scan for hardware changes to reset the view

1. In Device Manager, click **Action → Scan for hardware changes**.
2. Wait for the scan to finish. Connected devices that were incorrectly marked absent get re-detected and turn solid again.
3. If a device you know is plugged in stays grayed after a scan, the problem is physical — cable, port, or the device itself — not the hidden-device view.

### Fix 6: Inspect hidden devices from the command line with pnputil

1. Open an elevated **Command Prompt**.
2. Run `pnputil /enum-devices /connected` to list present devices, then `pnputil /enum-devices /disconnected` to list non-present ones.
3. Match instance IDs against the grayed entries you saw in Device Manager.
4. Remove a specific stubborn ghost with `pnputil /remove-device "instance-id"` — useful when the GUI uninstall fails with an error.
5. This method also works over remote sessions where the Device Manager GUI is awkward.

### Fix 7: Remove stale driver packages from the driver store

1. Run `pnputil /enum-drivers` in an elevated prompt to list every staged driver package with its published name (oem*.inf).
2. Identify packages belonging to hardware you no longer own — old printers, retired docks, replaced network adapters.
3. Run `pnputil /delete-driver oemNN.inf /uninstall` for each one.
4. Reboot. Ghost entries tied to those packages stop reappearing because there is nothing left to reinstall them.
5. If Windows needs the driver later for new hardware, it will fetch it fresh from Windows Update — you can confirm the driver situation in [Microsoft's Windows support documentation](https://support.microsoft.com/en-us/windows).

## Closing

When a revealed entry carries a warning icon instead of a simple ghosted look, follow the [unknown-device diagnosis steps](/articles/how-to-fix-unknown-device-in-device-manager-in-windows-11-24h2/) to identify the hardware before removing anything. Showing hidden devices in Device Manager turns an invisible problem into a visible one. Once you can see the ghosted entries, cleanup is mechanical: uninstall what is gone, keep what is present, and remove staged drivers that keep resurrecting phantoms. Make this a routine part of any driver-conflict diagnosis and you will stop chasing errors that were never really about the current hardware at all.
