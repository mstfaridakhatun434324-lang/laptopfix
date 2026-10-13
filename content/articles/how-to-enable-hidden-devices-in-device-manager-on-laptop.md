---
title: "How to Show Hidden Devices in Device Manager on a Laptop"
slug: how-to-enable-hidden-devices-in-device-manager-on-laptop
date: 2026-10-03
categories: ["drivers"]
tags: ["device manager", "hidden devices", "windows 11", "ghost devices", "troubleshooting"]
description: "Missing hardware in Device Manager? Learn to reveal hidden and ghost devices, read their error codes, and clean up safely."
thumbnail: "/images/thumbs/how-to-enable-hidden-devices-in-device-manager-on-laptop.webp"
faqs:
  - q: "What are hidden devices in Device Manager, and why are they hidden?"
    a: "Hidden devices are hardware entries Windows keeps in its database but does not currently detect as active — disconnected USB devices, disabled components, and drivers for hardware that failed to start. Device Manager hides them by default to keep the view focused on working hardware. Revealing them is essential for troubleshooting, because a missing device often exists as a hidden entry with an error code explaining exactly what went wrong."
  - q: "Is it safe to uninstall hidden greyed-out devices?"
    a: "Usually yes, with care. Greyed-out entries for devices you no longer own — old USB drives, removed printers — are safe to uninstall and it cleans up driver clutter. Never uninstall hidden system devices you do not recognize, such as greyed-out system or processor entries, since Windows may need them. When in doubt, uninstall only the specific device you are troubleshooting."
  - q: "Why does a device keep reappearing as hidden after I uninstall it?"
    a: "Because the driver package is still in the driver store, Windows redetects the hardware ID on the next scan and recreates the entry. To remove it permanently, tick Delete the driver software for this device during uninstall, or remove the driver package with pnputil. For built-in laptop hardware that keeps failing, the reappearing hidden entry is a symptom — the underlying driver or hardware fault needs fixing."
  - q: "What's the difference between hidden devices and unknown devices?"
    a: "Hidden devices are known hardware that is currently inactive, disconnected, or disabled — Windows knows what they are. Unknown devices are hardware Windows detected but cannot identify because no driver matched, shown with a yellow warning. A device can be both: unknown and hidden. Fix unknown devices by installing the right driver; investigate hidden devices by reading their error codes."
---

Device Manager only shows you part of the truth by default. Disconnected, disabled, and failed devices are tucked away as hidden entries, which means the touchpad, Wi-Fi adapter, or camera you are hunting for may be sitting right there — greyed out, carrying an error code that names the problem. Learning to reveal hidden devices is one of the highest-leverage troubleshooting skills on Windows, because it turns "the hardware vanished" into a specific, fixable diagnosis.

This matters most on laptops, where you cannot just reseat a card. A Wi-Fi adapter that disappeared after an update, a fingerprint reader Windows Hello cannot find, a touchpad with no entry anywhere — all of these frequently exist as hidden devices with codes like 10, 43, or 45 that point straight at the cause. Once you know how to find and interpret these entries, pair the skill with our [driver version guide](/articles/how-to-check-driver-version-in-device-manager-on-laptop/) to audit exactly what is installed, and our [unknown device repair](/articles/how-to-fix-unknown-device-in-device-manager-in-windows-11-24h2/) for hardware Windows cannot identify at all.

## Why this happens

- **Device Manager hides non-present devices by default**, so disconnected or failed hardware disappears from the normal view.
- **A failed driver leaves the device in a hidden error state** instead of showing it normally with a warning.
- **Windows disables a device after repeated failures**, hiding it to keep the device tree clean.
- **Ghost entries accumulate from old USB devices**, cluttering the hidden view with hardware you no longer own.
- **Driver updates orphan old device entries**, leaving hidden duplicates alongside the new working ones.
- **Firmware-disabled hardware** (camera kill switches, BIOS-disabled radios) appears only as hidden entries, if at all.
- **Corrupted device metadata** prevents Windows from displaying the entry normally even though the driver database holds it.

- **Devices disabled by group policy or MDM on managed laptops** appear hidden and cannot be re-enabled locally, which is normal on corporate machines with restricted hardware policies.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable Show hidden devices

The basic toggle that reveals the hidden layer. Write down the exact code wording — paraphrased codes lead to wrong fixes when searching for help.

1. Press Win + X and open Device Manager.
2. Click the View menu at the top and select Show hidden devices.
3. Watch for new greyed-out entries to appear across the categories.
4. Expand the category for your missing hardware first — network adapters, biometric devices, imaging devices, and human interface devices are the usual suspects.

### Fix 2: Reveal non-present devices with the environment variable

The View menu toggle misses some ghost devices. This method shows everything.

1. Press Win + R, type cmd, and press Ctrl + Shift + Enter for an elevated prompt.
2. Run `set devmgr_show_nonpresent_devices=1` and press Enter.
3. In the same window, run `start devmgmt.msc` to open Device Manager with the variable active.
4. Enable Show hidden devices in the View menu — the ghost device list will be longer and more complete.

### Fix 3: Read the error code on the hidden device

The code is the diagnosis. Do not skip reading it.

1. Double-click the greyed-out device and read the Device status box on the General tab.
2. Code 10 or 43 means the driver failed to start — reinstall the driver.
3. Code 45 means Windows thinks the hardware is disconnected — check BIOS settings and physical switches.
4. Code 24 means the device is not present or not working properly — often fixed by a driver reinstall or firmware toggle.

### Fix 4: Uninstall the ghost entry and rescan

A corrupted hidden entry can block clean reinstallation — remove it so Windows starts fresh.

1. Right-click the problematic hidden device and choose Uninstall device.
2. Tick Delete the driver software for this device if the option appears.
3. Click Action in the menu bar and select Scan for hardware changes.
4. Watch whether the device returns as a normal entry, a hidden entry, or not at all — each outcome narrows the diagnosis.

### Fix 5: Clean up stale ghost devices safely

Old ghosts can conflict with new installations of similar hardware.

1. With hidden devices shown, expand each category and look for greyed-out duplicates.
2. Uninstall ghosts for hardware you no longer own — old USB drives, removed docks, retired printers.
3. Leave greyed-out system devices alone unless you are specifically troubleshooting them.
4. Restart after cleanup and rescan to confirm the device tree is clean.

### Fix 6: Reinstall the driver for the hidden device

Once you know which device is hiding, give it a working driver. Microsoft's [Windows support documentation](https://support.microsoft.com/en-us/windows) covers driver installation fundamentals.

1. Identify the exact hardware from the hidden entry's Details tab, Hardware Ids property.
2. Search that hardware ID to find the precise driver, or get it from your laptop manufacturer's support page.
3. Uninstall the hidden entry with driver deletion, then install the fresh package.
4. Rescan for hardware changes and confirm the device appears as a normal, working entry.

### Fix 7: Check firmware switches when the device stays hidden

A device that will not unhide is often switched off below Windows' level.

1. Check physical kill switches, privacy shutters, and Fn-key toggles for the hardware.
2. Enter the BIOS/UEFI setup and verify the device is enabled there.
3. On some laptops, wireless and camera devices have BIOS-level enables independent of Windows.
4. After enabling in firmware, boot Windows and rescan — the device should appear normally.

## Closing

Hidden devices turn invisible hardware problems into readable ones: reveal them, read the error code, and act on what it says. The environment-variable method plus a careful uninstall-and-rescan resolves most ghost-device tangles. Make this the first step whenever hardware "vanishes" after an update — the answer is usually sitting in the hidden view, waiting to be read. Make hidden-device inspection a habit whenever hardware misbehaves after updates — it takes seconds and frequently reveals the exact error code. Paired with the driver version check, these two Device Manager skills resolve a remarkable share of 'my hardware vanished' complaints without any third-party tools.
