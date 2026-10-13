---
title: "How to Enable Hidden Devices in Device Manager"
slug: how-to-enable-hidden-devices-in-device-manager
date: 2026-09-16
categories: ["drivers"]
tags: ["device manager", "hidden devices", "show hidden devices", "ghost devices", "driver troubleshooting"]
description: "Can't find a device in Device Manager? Show hidden devices to reveal disconnected, ghost, and disabled hardware, then clean up or reinstall them."
thumbnail: "/images/thumbs/how-to-enable-hidden-devices-in-device-manager.webp"
faqs:
  - q: "What does Show hidden devices actually reveal?"
    a: "It reveals three kinds of entries Windows normally hides: devices that are physically disconnected but whose drivers remain installed, non-Plug-and-Play drivers and services, and devices that were disabled. These appear greyed out. They matter because leftover ghost entries can conflict with new hardware and block fresh driver installations."
  - q: "Is it safe to uninstall greyed-out hidden devices?"
    a: "Generally yes for greyed-out ghost devices you recognize, like an old printer or a removed USB device. Uninstalling them removes stale driver bindings and often fixes conflicts. Avoid removing hidden system devices you do not recognize, such as non-Plug-and-Play drivers, unless you are following a specific troubleshooting guide for them."
  - q: "Why do I need to see hidden devices to fix a driver?"
    a: "Because Windows remembers every device it ever installed. When you reinstall a driver for hardware that appears and disappears, like a USB device or a network adapter, the old ghost entry can keep the broken configuration and the new install inherits the problem. Removing the hidden ghost first gives the reinstall a clean slate."
  - q: "Does the devmgr_show_nonpresent_devices variable still work?"
    a: "Yes. Setting the environment variable devmgr_show_nonpresent_devices to 1 before opening Device Manager reveals even more non-present devices than the View menu alone shows. This is the technician-level view used when chasing stubborn ghost devices that survive ordinary cleanup, particularly with USB and network hardware."
---

Device Manager only shows you part of the story by default. Every device Windows has ever seen — every USB stick, every printer, every network adapter from a dock you no longer own — leaves a ghost entry behind, and Device Manager hides them all unless you ask. Those hidden entries are not just clutter. Stale ghost devices cause real problems: driver reinstalls that change nothing, "device already in use" errors, and hardware that refuses to appear no matter how many times you scan.

Learning to reveal hidden devices is a core troubleshooting skill. It takes ten seconds, it is completely safe, and it frequently exposes the exact entry that is blocking your fix. This guide covers both the standard view and the deeper technician view that shows everything.

## Why this happens

- **Windows hides non-present devices by design:** To keep the tree readable, Device Manager hides any device not currently connected, even though its driver and configuration remain installed.
- **Ghost entries keep broken configurations:** A ghost of a previously failed device can hold onto a bad driver binding, so reinstalling the driver "succeeds" but changes nothing.
- **Non-Plug-and-Play drivers are hidden too:** Legacy filter drivers and services only appear when hidden devices are shown, and they can interfere with storage and network hardware.
- **Disabled devices vanish from the normal view:** A device you disabled months ago is easy to forget — showing hidden devices is how you find it again.
- **USB enumeration leaves ghosts:** Every USB port and hub combination creates entries. Moved a device between ports? You now have multiple ghosts for one physical device.
- **Driver cleanup tools miss hidden entries:** Uninstalling a driver package does not remove its hidden device entries, which is why "clean reinstalls" sometimes fail.
- **Docking stations multiply ghosts:** Laptops that dock and undock accumulate network, audio, and display ghosts from every dock configuration.
- **Failed installs register phantom devices:** An installation that crashed halfway can leave a hidden entry that blocks the next attempt with cryptic errors.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Show hidden devices from the View menu

1. Press **Win + X** and open **Device Manager**.
2. Click **View** in the menu bar, then select **Show hidden devices**.
3. Scan the tree for greyed-out (dimmed) entries — these are the hidden ones. They appear in every category from Network adapters to USB controllers.
4. Look specifically for greyed duplicates of the device you are troubleshooting. Two entries for one physical device means a ghost conflict.
5. This single menu toggle is the foundation of everything below. Leave it on while you work — it stays enabled until you close Device Manager.

### Fix 2: Remove ghost entries blocking your device

1. With hidden devices shown, locate the greyed-out entries related to your problem hardware.
2. Right-click each ghost and choose **Uninstall device**. For simple ghosts, leave the "delete driver software" box unchecked.
3. Work through every duplicate — a USB Wi-Fi adapter moved between ports can leave three or four ghosts, and all of them must go.
4. Click **Action → Scan for hardware changes** to let Windows rebuild a clean entry for the connected hardware.
5. If you were chasing a missing device, check whether it now appears in its normal bright (non-greyed) form. Ghost removal is a classic fix for hardware that [won't show up after a driver reinstall](/articles/best-way-to-fix-wifi-adapter-not-showing-up/).

### Fix 3: Reveal non-present devices with the environment variable

1. Press **Win + R**, type `cmd`, and press **Ctrl + Shift + Enter** to open an elevated Command Prompt.
2. Run: `set devmgr_show_nonpresent_devices=1` then `start devmgmt.msc` from the same window.
3. In the Device Manager that opens, enable **View → Show hidden devices**.
4. You will now see additional faded entries that the plain View toggle does not reveal — these are devices Windows recorded as non-present.
5. This deeper view is especially useful for USB and storage ghosts that resist ordinary cleanup. Remove the offenders, then scan for hardware changes. Microsoft's [Device Manager guidance](https://support.microsoft.com/en-us/windows) covers the supported view options if you want the official reference.

### Fix 4: Find a device you disabled and forgot about

1. Show hidden devices and look for entries with a small **down arrow** overlay — that icon means disabled.
2. Right-click the disabled device and choose **Enable device**.
3. Test the hardware immediately.
4. Common victims: Bluetooth radios disabled during troubleshooting, webcams disabled for privacy, and network adapters disabled during a "fix" that was never undone.
5. If you disabled something in the BIOS instead, Device Manager cannot re-enable it — you will need to revisit the BIOS setting, as covered in guides for [unknown devices](/articles/best-way-to-fix-unknown-device-in-device-manager/).

### Fix 5: Expose hidden non-Plug-and-Play drivers

1. With hidden devices shown, expand **Non-Plug and Play Drivers** (it only appears in this view).
2. Look for third-party filter drivers from uninstalled antivirus, VPN, or disk tools — these are frequent troublemakers.
3. If a specific guide identifies one as the cause of your issue, right-click it and choose **Uninstall**. Do not bulk-remove entries here.
4. Restart after removing any filter driver — they load at boot, so the change only takes effect on restart.
5. When in doubt about an entry, leave it alone and research its exact name first. System-critical drivers live in this list too.

### Fix 6: Clean USB ghosts with a full enumeration reset

1. Show hidden devices and expand **Universal Serial Bus controllers**.
2. Uninstall every greyed-out **USB Mass Storage Device**, **USB Composite Device**, and unknown USB entry.
3. Also clear ghosts under **Disk drives** for USB sticks that no longer exist.
4. Restart the laptop. Windows rebuilds the USB enumeration from scratch at boot.
5. Reconnect your USB devices one at a time and confirm each is recognized. This reset fixes a large share of "USB device not recognized" loops where the same device fails on every port.

### Fix 7: Use hidden view to diagnose a missing network adapter

1. Show hidden devices and expand **Network adapters**.
2. If your Wi-Fi or Ethernet adapter appears greyed out, Windows has its driver but thinks the hardware is absent — this points to a BIOS toggle, a hardware switch, or a failed card rather than a driver problem.
3. If it appears with a warning icon, right-click → **Properties** and read the error code. Code 45 means "currently disconnected," which confirms the hardware is not being detected.
4. Try **Uninstall device** on the greyed entry (checking delete driver software), then **Scan for hardware changes** to force a fresh detection attempt.
5. If the adapter never appears even as a ghost, check BIOS settings and physical switches before assuming the card is dead — the same logic applies to [airplane mode stuck states](/articles/airplane-mode-stuck-on-troubleshooting/) that hide radios.

## Closing

Showing hidden devices turns Device Manager from a simple list into a forensic tool. The greyed-out ghosts it reveals explain why driver reinstalls sometimes do nothing and why removed hardware keeps haunting new installations. Make the View toggle and the environment-variable trick part of your standard routine, clean out the ghosts that matter, and leave the system entries you don't recognize alone.
