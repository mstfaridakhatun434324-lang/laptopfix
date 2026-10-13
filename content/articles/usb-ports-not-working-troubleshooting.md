---
title: "USB Ports Not Working? Troubleshoot Dead Ports on Your Windows 11 Laptop"
slug: usb-ports-not-working-troubleshooting
date: 2026-09-25
categories: ["drivers"]
tags: ["usb ports not working", "usb not recognized", "dead usb port", "usb driver", "windows 11"]
description: "USB ports not working on your laptop? Troubleshoot dead ports systematically: power drain, USB controller reset, selective suspend, driver reinstalls, and hardware checks."
thumbnail: "/images/thumbs/usb-ports-not-working-troubleshooting.webp"
faqs:
  - q: "Why did all my USB ports stop working at once?"
    a: "All ports dying simultaneously is almost never individual port failure — it is the USB host controller driver crashing, a BIOS-level USB disable, or an embedded-controller lockup. A full power drain (shutdown, unplug, hold power 30 seconds) resets the controller and fixes most cases. If ports work in BIOS but not Windows, the Windows USB driver stack is the culprit."
  - q: "Can a Windows update disable USB ports?"
    a: "Yes. Windows Update can replace working USB controller drivers with broken ones, and some updates reset USB selective suspend or power-management settings. If ports died right after an update, roll back the USB controller driver in Device Manager or uninstall the update. Blocking bad driver updates afterward prevents recurrence."
  - q: "Why do my USB ports work in BIOS but not in Windows?"
    a: "That split proves the ports and controller hardware are fine — BIOS drives USB with firmware, while Windows uses its own driver stack. The fault is a corrupted USB host controller driver, a disabled controller in Device Manager, or a filter driver conflict. Reinstalling the USB controllers in Device Manager is the direct fix."
  - q: "Is it safe to uninstall all USB controllers in Device Manager?"
    a: "Yes, with one precaution: your keyboard and mouse may be USB, so have a PS/2 alternative or know that Windows reinstalls the controllers automatically on restart. Uninstall every entry under Universal Serial Bus controllers, restart, and Windows rebuilds the entire USB stack from scratch. It is the standard deep fix for persistent USB failures."
---

Dead USB ports feel catastrophic — no mouse, no external drive, no headset dongle — but the failure pattern tells you almost everything. One dead port is usually physical. All ports dead at once is almost never physical: it's the USB host controller driver, a power-management lockup, or a BIOS setting. And ports that work in BIOS but die in Windows are a driver-stack problem by definition, since the same silicon works under firmware control. This guide reads the pattern first, then applies the matching fix, from the 60-second power drain to a full USB stack rebuild.

Before anything else, note the pattern: which ports are dead, whether anything works in BIOS, and whether the failure started after an update. You'll use that information in every fix below.

## Why this happens

- **Embedded-controller lockup.** The EC managing USB power gets stuck; a power drain resets it.
- **Corrupted USB host controller driver.** Often after a Windows update replaces the working driver.
- **USB selective suspend cutting power.** Aggressive power saving disabling idle ports permanently.
- **Disabled USB controller in Device Manager.** Accidentally disabled, or disabled by a "tuning" utility.
- **USB ports disabled in BIOS.** Firmware-level disable affecting some or all ports.
- **Overcurrent protection tripped.** A shorted device causing the controller to shut ports down.
- **Physically damaged port.** Bent pins or broken solder joints — usually affects one port only.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Perform a full power drain

The 60-second fix for controller lockups.

1. Shut the laptop down **completely** (not sleep, not hibernate).
2. Unplug the AC adapter and **all** USB devices.
3. If the battery is removable, remove it; if not, that's fine — the next step still works.
4. Press and hold the **power button for 30 seconds** — this drains residual power and resets the embedded controller.
5. Reconnect only the AC adapter, power on, and test the USB ports with a simple device (a wired mouse is ideal).
6. If ports return, reconnect devices one at a time — a shorted peripheral can re-trip the protection instantly, identifying the culprit.

### Fix 2: Check whether ports work in BIOS

The diagnostic split that halves the problem space.

1. Restart and enter **BIOS/UEFI** (F2, Del, or F12 during boot).
2. Plug a USB keyboard or mouse in and see if it works in the BIOS menus.
3. **Works in BIOS, dead in Windows** → Windows driver-stack problem (Fixes 3–5). Skip hardware fixes.
4. **Dead in BIOS too** → hardware, BIOS setting, or EC issue (Fixes 6–7).
5. While in BIOS, check for **USB configuration** options — ensure USB ports and legacy USB support are **Enabled**.

### Fix 3: Reinstall the USB controller stack

The deep driver fix — safe and highly effective.

1. Open **Device Manager** → expand **Universal Serial Bus controllers**.
2. Look for any entry with a yellow warning — note its name before touching anything.
3. Right-click each **USB Root Hub** and **USB Host Controller** entry → **Uninstall device**. Work through all of them.
4. **Do not** uninstall entries your input devices depend on until last, or keep a backup input method ready.
5. Restart the laptop. Windows detects the hardware and rebuilds the entire USB stack automatically.
6. Test every port after the restart. This resolves the large majority of Windows-side USB deaths.

The same Device Manager rebuild technique helps related detection issues — see [how to fix a USB device not recognized after a Windows 11 update](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/).

### Fix 4: Disable USB selective suspend and power management

For ports that die after idle periods or sleep.

1. Open **Device Manager** → **Universal Serial Bus controllers** → for each **USB Root Hub** → Properties → **Power Management** → **uncheck** "Allow the computer to turn off this device to save power."
2. Control Panel → Power Options → Change plan settings → Change advanced power settings → **USB settings** → USB selective suspend setting → **Disabled** (both battery and plugged-in).
3. **Settings > System > Power & battery** → set Power mode to **Best performance** while testing.
4. Disable **fast startup** (Power Options → Choose what the power buttons do) — it preserves bad USB power states across "shutdowns."
5. Test with the specific device that kept disconnecting; selective-suspend failures need minutes of idle to manifest.

### Fix 5: Roll back the bad driver or update

For failures that started after a Windows update.

1. In Device Manager, open the **USB Host Controller** properties → **Driver** tab → **Roll Back Driver** if available.
2. **Settings > Windows Update > Update history > Uninstall updates** — remove the update that coincided with the failure.
3. Alternatively, download the **chipset driver** from your laptop maker's support page — the USB controllers are part of the chipset package, and the vendor's version is usually newer or more stable than Windows'.
4. For Intel systems, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) refreshes chipset and USB components.
5. After fixing, consider [disabling automatic driver updates](/articles/how-to-disable-automatic-driver-updates-in-windows-11-24h2/) so Windows doesn't reinstall the broken driver.

### Fix 6: Check for overcurrent and device conflicts

When one bad peripheral kills the whole bus.

1. Unplug **everything** USB and test ports with a single known-good device.
2. Reconnect devices one at a time, testing after each — the one that kills the ports has a short or power fault.
3. Check Device Manager for **Unknown USB Device (Port Reset Failed)** or overcurrent warnings — these name the offending port.
4. Inspect each port with a flashlight for bent pins or debris — a paperclip or staple in a port can short the bus.
5. Never use damaged cables; a frayed cable that shorts 5V to ground will trip protection repeatedly.

### Fix 7: Verify hardware and BIOS

The final tier for ports dead everywhere including BIOS.

1. Update the **BIOS** from the manufacturer's support page — USB controller firmware fixes appear in changelogs.
2. In BIOS, reset to **optimized defaults** to clear any corrupted USB configuration.
3. A single dead port with visibly bent pins or a loose housing is physical damage — board-level repair or a USB hub workaround.
4. All ports dead in BIOS after a power drain and BIOS reset points to controller or motherboard failure — a service-center diagnosis.
5. As a workaround, a **powered USB hub** on one working port, or a Thunderbolt/USB-C dock, can restore connectivity while you arrange repair. For dock-related issues, see [how to fix Thunderbolt not working on a laptop](/articles/how-to-fix-thunderbolt-not-working-on-laptop-in-windows-11-24h2/).

## Closing

USB port failures announce their cause through their pattern: all-at-once means controller or power state, one-port means physical, works-in-BIOS means Windows drivers. The power drain and the USB stack reinstall together resolve the overwhelming majority of cases without touching hardware. Keep selective suspend disabled if your ports have a history of dying after idle, and treat any peripheral that kills the bus on plug-in as the suspect it is — the ports are usually innocent.
