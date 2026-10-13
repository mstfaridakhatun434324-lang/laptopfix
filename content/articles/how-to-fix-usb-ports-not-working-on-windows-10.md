---
title: "How to Fix USB Ports Not Working on Windows 10"
slug: how-to-fix-usb-ports-not-working-on-windows-10
date: 2026-09-18
categories: ["drivers"]
tags: ["usb ports", "usb not recognized", "windows 10", "usb controller", "device manager"]
description: "USB ports dead on Windows 10? Reset the USB controller stack, fix power management, and clear ghost devices to get every port working again."
thumbnail: "/images/thumbs/how-to-fix-usb-ports-not-working-on-windows-10.webp"
faqs:
  - q: "Why did all my USB ports stop working at once?"
    a: "All ports dying together usually means the USB controller driver crashed or a power event put the USB root hubs into a failed state, not that every port broke physically. Restarting the controller stack in Device Manager fixes this in most cases. If only one port is dead while others work, that points to a physical port problem instead."
  - q: "Should I uninstall all USB controllers in Device Manager?"
    a: "Yes, this is a safe and standard fix. Uninstall every entry under Universal Serial Bus controllers, then restart — Windows rebuilds the entire USB stack automatically at boot. Your keyboard and mouse will stop working during the process if they are USB, so have a PS/2 alternative or use the laptop's built-in keyboard and touchpad."
  - q: "Can power settings disable my USB ports?"
    a: "Absolutely. Windows can suspend USB root hubs to save power, and the USB selective suspend setting can leave ports in a state they never wake from. Disabling selective suspend and unchecking power management on each USB root hub resolves ports that die after sleep or idling."
  - q: "My USB device works on another computer but not mine — why?"
    a: "That rules out the device itself and points to your USB stack: a ghost entry for that device, a corrupted controller driver, or a power delivery issue on your ports. Clear hidden USB ghosts in Device Manager, reinstall the controller drivers, and try the device on a different port, preferably one directly on the machine rather than a hub."
---

Dead USB ports on Windows 10 are usually a software problem wearing a hardware costume. When every port stops responding at once — no recognition chime, no power to devices, nothing in Device Manager — the USB controller driver has almost certainly crashed or been left in a failed state by a power event. Individual dead ports are a different story and usually physical, but a full-port outage is fixable from your desk.

The repair strategy is straightforward: reset the USB controller stack, stop Windows from power-managing the ports into oblivion, clear out ghost entries, and verify with a clean boot state. Work through the steps in order and test after each one.

## Why this happens

- **USB controller driver crash:** The xHCI controller driver can fail after updates or sleep/wake cycles, taking every port down with it while the rest of the system runs fine.
- **USB selective suspend stuck:** Windows suspends idle USB hubs to save power. Sometimes a hub never wakes, and its ports stay dark until the suspend state is cleared.
- **Power management on root hubs:** The "allow the computer to turn off this device" option on USB Root Hubs can shut ports down aggressively, especially on laptops.
- **Ghost device conflicts:** Old entries for previously connected USB devices can conflict with new connections, producing "device not recognized" on every port.
- **Fast Startup preserving a bad state:** Fast Startup hibernates the kernel, so a crashed USB stack survives restarts and the ports stay dead.
- **Chipset driver outdated or corrupt:** The USB controllers are part of the chipset; a broken chipset driver package breaks USB enumeration at the root.
- **BIOS USB settings changed:** BIOS updates can reset USB configuration, disabling xHCI mode or legacy USB support that your devices need.
- **Physical power delivery failure:** Rare, but a blown USB power rail or damaged port can kill ports electrically — distinguishable because it affects specific ports, not all of them.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the scope — one port or all ports

1. Test every USB port on the laptop with a simple device like a wired mouse or USB stick.
2. Try the same device on another computer to confirm the device itself works.
3. If ALL ports are dead, continue with the software fixes below — this pattern is almost never physical.
4. If only one port is dead, inspect it with a flashlight for bent pins or debris, and try a different cable. A single dead port after a drop or yank is usually mechanical damage.
5. Note whether ports provide power (phone charging light) but no data — power without data points to a driver/enumeration issue rather than a power rail failure.

### Fix 2: Uninstall and rebuild the USB controller stack

1. Press **Win + X** and open **Device Manager**.
2. Expand **Universal Serial Bus controllers**.
3. Right-click each **USB Root Hub**, **Generic USB Hub**, and **USB xHCI Compliant Host Controller** and choose **Uninstall device**. Do not check driver deletion boxes.
4. When finished, click **Action → Scan for hardware changes**, or simply restart — Windows rebuilds the entire USB stack at boot.
5. Test the ports after the rebuild. This is the highest-yield fix for full-port outages; if your USB keyboard/mouse die mid-process, use the laptop's built-in keyboard and touchpad to finish. Checking the [driver version](/articles/best-way-to-check-driver-version-in-device-manager/) afterward confirms the stack rebuilt cleanly.

### Fix 3: Disable USB selective suspend

1. Open **Control Panel → Hardware and Sound → Power Options**.
2. Click **Change plan settings** next to your active plan, then **Change advanced power settings**.
3. Expand **USB settings → USB selective suspend setting**.
4. Set both **On battery** and **Plugged in** to **Disabled**.
5. Click OK and restart. This stops Windows from parking USB hubs in suspend states they sometimes never leave — the classic cause of ports that die after the laptop idles.

### Fix 4: Turn off power management on USB root hubs

1. In Device Manager, expand **Universal Serial Bus controllers**.
2. For each **USB Root Hub** (and Generic USB Hub), right-click → **Properties → Power Management**.
3. Uncheck **Allow the computer to turn off this device to save power**.
4. Repeat for every hub entry — missing even one leaves a path for the problem to return.
5. Restart and test. On laptops this setting is particularly aggressive, and disabling it costs negligible battery while preventing suspend-related port death.

### Fix 5: Clear hidden USB ghost devices

1. In Device Manager, click **View → Show hidden devices**.
2. Expand **Universal Serial Bus controllers** and **Disk drives**, and look for greyed-out ghosts of USB devices.
3. Right-click each ghost and choose **Uninstall device**.
4. Pay special attention to faded **USB Mass Storage Device** entries — these are the most common blockers for sticks and external drives.
5. Scan for hardware changes afterward. Ghost cleanup is often the missing step when [ports work for some devices but not others](/articles/best-way-to-fix-usb-ports-not-working/), because the conflict is per-device rather than per-port.

### Fix 6: Disable Fast Startup for a true cold boot

1. Open **Control Panel → Power Options → Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Shut down fully (not Restart), wait ten seconds, and power on.
4. Test the USB ports on the cold boot.
5. Fast Startup preserves kernel driver state across "shutdowns," so a crashed USB controller survives indefinitely until you force a real cold boot.

### Fix 7: Reinstall the chipset driver package

1. Visit your laptop maker's support page ([Dell](https://www.dell.com/support) or [HP](https://support.hp.com/us-en)) and download the **chipset driver** for your exact model.
2. Install it and restart when prompted — the installer refreshes the USB xHCI controller drivers as part of the chipset package.
3. Intel-based laptops can also use [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to detect the right chipset package.
4. After reinstalling, re-check Device Manager for warning icons under USB controllers.
5. If Windows Update keeps replacing the chipset driver with a broken one, consider pausing driver updates until the manufacturer publishes a fixed package.

### Fix 8: Check BIOS USB settings

1. Restart and enter BIOS/UEFI (**F2** or **Del**).
2. Look for USB configuration under **Advanced** — ensure **USB Controller**, **xHCI Mode**, and **Legacy USB Support** are enabled.
3. If a recent BIOS update preceded the problem, use the BIOS option to **Load Optimized Defaults**, then re-enable anything you specifically need.
4. Save and exit, then test the ports in Windows.
5. As a diagnostic bonus: if USB devices work in the BIOS setup screens (a USB keyboard navigates fine) but not in Windows, the fault is definitively in the Windows USB stack, not hardware.

## Closing

Full USB port outages on Windows 10 are a controller-stack problem, and the stack rebuild in Fix 2 resolves most of them outright. The power management fixes (selective suspend, root hub power saving, Fast Startup) handle the cases that keep coming back after sleep or idle. Only when a single port stays dead across all software fixes — and works for no device — should you conclude the port itself is physically damaged.
