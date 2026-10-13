---
title: "How to Show Hidden Devices in Device Manager on Windows"
slug: how-can-i-enable-hidden-devices-in-device-manager
date: 2026-09-18
categories: ["drivers"]
tags: ["device manager", "hidden devices", "drivers", "troubleshooting", "windows"]
description: "Can't find a device in Device Manager? Learn how to reveal hidden and ghost devices in Device Manager to fix missing hardware and driver conflicts."
thumbnail: "/images/thumbs/how-can-i-enable-hidden-devices-in-device-manager.webp"
faqs:
  - q: "Why don't hidden devices show up in Device Manager by default?"
    a: "Windows hides non-present and inactive devices to keep the list clean and fast. Hardware that is disconnected, disabled, or only loaded on demand is filtered out of the normal view. Enabling hidden devices reveals ghost entries, disconnected peripherals, and inactive driver installations so you can inspect or remove them."
  - q: "What does a grayed-out device icon mean in Device Manager?"
    a: "A dimmed or grayed-out icon means the device is not currently present or connected. Windows keeps the driver entry in its database so settings are remembered if the hardware returns. Ghost entries from old USB devices are the most common example, and they are usually harmless unless they conflict with new hardware."
  - q: "Is it safe to uninstall grayed-out hidden devices?"
    a: "Usually yes, especially for ghost entries of USB devices you no longer own. Removing them frees driver slots and resolves conflicts with replacement hardware. Don't uninstall hidden entries for system devices or hardware that is only temporarily disconnected, like a printer you still use, because Windows will just reinstall them anyway."
  - q: "Can hidden devices cause problems with new hardware?"
    a: "Yes. Stale ghost drivers can reserve COM ports, USB addresses, or device names that block replacement hardware from installing correctly. If a new device fails with an error code even though drivers look fine, revealing and clearing conflicting hidden entries is a classic technician step that often fixes it."
---

Device Manager is the first place any technician looks when hardware misbehaves, but out of the box it doesn't tell the whole story. By default it only lists devices Windows considers present and active. The device you're hunting — a phantom USB stick, an old printer, a Bluetooth adapter that vanished — is very often still in Windows' driver database, just hidden from the normal view.

Learning to reveal hidden devices turns Device Manager from a simple list into a diagnostic tool. Ghost entries show you what Windows *thinks* it has installed, which is frequently different from what you *think* you installed. That gap is where some of the most stubborn hardware mysteries live: devices that "disappeared," replacement hardware that refuses to install, and driver conflicts that make no sense until you see the duplicates hiding underneath.

## Why this happens

- **Non-present hardware filtering:** Windows hides devices that aren't currently connected to keep the list readable.
- **Ghost driver entries:** every USB device you ever plugged in can leave a dimmed entry behind.
- **Disabled devices:** a device you disabled months ago vanishes from the normal view.
- **Inactive driver packages:** drivers staged but not bound to active hardware stay invisible.
- **Phantom duplicates:** reinstalling the same device can create a second entry the old one shadows.
- **Filtered device classes:** some system classes are suppressed unless the view is changed.
- **Corrupt device enumeration:** Windows occasionally fails to enumerate hardware, pushing entries into the hidden state.
- **Driver conflicts:** two entries fighting over the same hardware ID push one into hiding.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable the hidden devices view

1. Press **Win + X** and choose **Device Manager**. The quickest way to reveal more is the View menu.
2. Click **View > Show hidden devices**. Hidden entries appear immediately, shown with dimmed or grayed-out icons.
3. Scan the tree for the device you're missing. Non-present items appear under their normal category, faded out.
4. If you see your device here but grayed out, it's installed but not detected — skip to Fix 4.
5. If it's not listed at all even after this step, the device was likely never installed or Windows has no record of it — move on to Fix 2. General Windows troubleshooting guidance is available at [Microsoft support](https://support.microsoft.com/en-us/windows).

### Fix 2: Use the environment variable for a full ghost listing

1. The View menu trick only reveals *some* hidden devices. For the complete picture, set an environment variable first.
2. Press **Win + S**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
3. Type `set devmgr_show_nonpresent_devices=1` and press Enter, then type `start devmgmt.msc` in the same window and press Enter.
4. Device Manager opens with full non-present device visibility. Again choose **View > Show hidden devices**.
5. Now scroll through — you'll often find far more ghost entries than the menu-only method showed.
6. This variable only lasts for that Command Prompt session, so close and reopen if you need to repeat it.

### Fix 3: Scan for hardware changes

1. In Device Manager, click **Action > Scan for hardware changes**.
2. Windows re-enumerates the buses and can pull hidden devices back into the visible list.
3. If your device appears with a yellow warning icon, right-click it and choose **Update driver**.
4. If it appears normally, the problem was stale enumeration — check whether the hardware now works.
5. Repeat the scan after physically reseating the hardware (USB devices, SD cards, removable modules) for best results.
6. Devices that keep appearing as hidden after a scan usually have driver or connection problems rather than enumeration problems.

### Fix 4: Check a grayed-out device's properties

1. Double-click the dimmed device to open its Properties window.
2. On the **General** tab, read the **Device status** box — codes like 24, 45, or "not connected" explain exactly why it's hidden.
3. Code 45 means "currently disconnected": the hardware simply isn't attached. Reconnect it and rescan.
4. Code 24 means the device is prepared for removal or missing: uninstall it and let Windows rediscover the hardware.
5. Check the **Events** tab too — the timestamped log shows when the device last worked and what changed.
6. These status codes are the most honest diagnostic Windows gives you, so read them before changing anything.

### Fix 5: Remove ghost duplicates that block new hardware

1. Find dimmed entries for hardware you no longer own — old USB drives, retired printers, replaced adapters.
2. Right-click each ghost entry and choose **Uninstall device**. Leave "delete driver software" unchecked unless you're sure.
3. Pay special attention to duplicates: two entries for one physical device means one of them is stale.
4. After clearing the ghosts, click **Action > Scan for hardware changes** to let the real hardware claim its slot.
5. This resolves the classic "new device won't install" problem where a ghost reserves the device's identity. The same cleanup helps when peripherals vanish — see [fixing Bluetooth that disappeared from Device Manager](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-11/) for a related walkthrough.
6. Reboot after bulk removals so Windows rebuilds its enumeration cleanly.

### Fix 6: Reinstall the driver for a hidden-but-present device

1. If the device is physically connected but shows as hidden/grayed, the driver binding is broken.
2. Right-click it and choose **Uninstall device**, this time checking "Attempt to remove the driver for this device" if offered.
3. Disconnect the hardware, wait ten seconds, and reconnect it.
4. Windows should detect it fresh and install the driver as a normal, visible entry.
5. If it still lands in the hidden list, download the driver from the manufacturer instead of relying on Windows' copy — a damaged driver store is a common cause.
6. Similar ghost-driver issues affect optical drives too; the steps in [dvd drive not detected on Windows 11](/articles/how-to-fix-dvd-drive-not-detected-on-windows-11/) follow the same logic.

### Fix 7: Check for disabled devices in the list

1. With hidden devices shown, look for entries with a small down-arrow overlay — that marks a disabled device.
2. Right-click it and choose **Enable device**. It should move to the normal visible list immediately.
3. Devices get disabled by accident more often than people admit: a misclick, a "tuning" script, or power-management software.
4. If the same device keeps disabling itself, check **Power Management** on its Properties tab and uncheck "Allow the computer to turn off this device to save power."
5. Also check your laptop vendor's utility (Dell Power Manager, Lenovo Vantage) — these can disable hardware silently.
6. After enabling, test the hardware before moving on; a device that re-disables itself points at a deeper driver or policy issue.

## Closing

Showing hidden devices is one of those small skills that separates guessing from diagnosing. Most "missing hardware" cases are actually hidden hardware — a ghost entry, a disabled device, or a stale driver binding that the normal Device Manager view politely refuses to show you. Once you know the View menu trick and the environment-variable method, you can see what Windows really has installed, and from there the fix is usually obvious. Make it a habit: whenever hardware vanishes or a replacement refuses to install, reveal the hidden list before you reinstall anything. The answer is usually already there, dimmed and waiting.
