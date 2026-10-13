---
title: "USB Ports Not Working? Step-by-Step Fixes"
slug: how-to-fix-usb-ports-not-working-step-by-step
date: 2026-09-15
categories: ["drivers"]
tags: ["usb ports", "usb not recognized", "device manager", "step by step"]
description: "USB ports dead on your laptop? A technician's step-by-step sequence to bring back unresponsive USB ports."
thumbnail: "/images/thumbs/how-to-fix-usb-ports-not-working-step-by-step.webp"
faqs:
  - q: "Why did all my USB ports stop working at the same time?"
    a: "Simultaneous failure of every port points above the individual ports — to the USB controller driver, the chipset driver, or a power-management state. Individual dead ports suggest physical damage, but all-at-once is almost always software: a crashed USB controller, a bad chipset driver update, or the controller suspended by power management and never waking."
  - q: "One USB port works but the others don't. Is that a driver issue?"
    a: "Unlikely — drivers operate per-controller, not per-port, and ports on the same controller share the driver. One dead port among working ones is usually physical: bent pins inside the port, debris, or a cracked solder joint. Inspect the dead port with a flashlight before doing any software troubleshooting."
  - q: "My USB device works on other computers but not my laptop. What's wrong?"
    a: "Then the device is fine and your laptop's USB subsystem is the problem. Work through the controller and driver fixes below — particularly reinstalling the USB controllers in Device Manager and the chipset driver. Also test the device in every port on the laptop; some devices are picky about USB 2.0 versus 3.0 ports."
  - q: "Can a Windows update break USB ports?"
    a: "Yes — chipset and USB controller driver updates are a known cause of USB failures, including the infamous 'USB device not recognized' loops. If the failure lines up with an update, reinstall the USB controllers and the chipset driver from your laptop manufacturer's site, which restores the validated driver set."
---

When USB ports die, the laptop loses its connection to the outside world — no mouse, no drives, no phone tethering. The failure feels total, but USB problems are among the most diagnosable in Windows because the subsystem is so layered: ports, hubs, controllers, chipset drivers, and power management each leave distinct fingerprints. The trick is reading those fingerprints instead of randomly reinstalling drivers.

This is the step-by-step sequence a technician follows: establish the scope first (one port? all ports? one device?), then work up the stack from power state to controllers to chipset. Each step's result tells you where to go next. For the specific "USB device not recognized" error on a working port, see our [USB device recognition guide](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/).

## Why this happens

- **The USB controller crashed.** The controller chip manages all ports on its bus; when it wedges, every port on that bus dies simultaneously while the rest of the laptop is fine.
- **Power management suspended the controller.** Windows' USB power saving puts controllers to sleep and sometimes can't wake them — the classic "worked until the laptop slept" pattern.
- **The chipset driver is broken or mismatched.** The USB controllers hang off the chipset; a bad chipset driver update orphans them all at once.
- **Individual port hardware failed.** Bent pins, debris, or cracked solder joints kill single ports — physical, per-port, and invisible to software fixes.
- **The USB driver stack corrupted.** Failed updates can leave the USB driver files in a half-upgraded state that Device Manager doesn't flag.
- **A single bad device is hanging the bus.** A malfunctioning USB device can lock up the entire controller, making all ports appear dead until the offender is unplugged.
- **BIOS disabled USB ports.** Some BIOSes expose per-port USB toggles; firmware updates can flip them, removing ports below the OS level.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Establish the scope (one port, all ports, one device)

The diagnosis that directs everything after it. Take two minutes.

1. Test a **known-good simple device** (a basic USB mouse or flash drive) in **every** USB port. Note exactly which ports respond.
2. **One dead port, rest fine** = physical port problem. Inspect it with a flashlight for bent pins or debris; skip to Fix 7.
3. **All ports dead** = controller/driver/power problem. Continue to Fix 2.
4. **One device dead in all ports, other devices fine** = the device itself (try it on another computer to confirm) — not a laptop problem at all.

### Fix 2: Unplug everything and cold-reset the USB bus

A bad device can hang the whole controller. Clear the bus completely.

1. **Shut down** the laptop fully (not sleep — full shutdown).
2. Unplug **every** USB device, the charger, and any dock. If the battery is removable, remove it.
3. Press and hold the power button for **30 seconds** with everything unplugged — this drains residual power and resets the USB controllers at the hardware level.
4. Reconnect only the charger, boot up, then plug in **one** simple USB device (a mouse). If it works, add devices back one at a time — the one that kills the bus is your culprit.

### Fix 3: Check BIOS USB settings

Rule out firmware-level disables before fighting Windows.

1. Enter **BIOS/UEFI** and find the USB configuration section (often under **Advanced** or **Integrated Peripherals**).
2. Ensure **USB ports** / **USB controller** are **Enabled** — check for per-port toggles too, on models that have them.
3. Look for **USB legacy support** or **XHCI mode** settings — if USB fails specifically in certain situations, toggling XHCI between Auto and Enabled can help.
4. Save and boot into Windows, then retest the ports before changing any Windows settings.

### Fix 4: Reinstall the USB controllers in Device Manager

The core software fix — forces Windows to rebuild the USB stack.

1. Open **Device Manager** (**Win + X** > Device Manager) and expand **Universal Serial Bus controllers**.
2. For each **USB Root Hub**, **Generic USB Hub**, and **USB Host Controller** entry: right-click > **Uninstall device**. (Your USB mouse/keyboard will stop working as you go — that's expected; use the keyboard or finish with the touchpad.)
3. When all are uninstalled, click **Action > Scan for hardware changes** — Windows redetects and reinstalls the entire USB stack fresh.
4. Alternatively, just **restart** the laptop — Windows reinstalls the controllers during boot. Test every port afterward.

### Fix 5: Reinstall the chipset driver

The USB controllers depend on the chipset driver — fix the foundation.

1. Download the **chipset driver** for your exact model from the laptop manufacturer's support site.
2. Install it as administrator and reboot — chipset installers re-enumerate all the internal controllers, including USB.
3. After reboot, check **Device Manager > Universal Serial Bus controllers** for a clean list with no warning icons.
4. If a Windows update caused the failure, this is also the moment to consider [blocking automatic driver updates](/articles/how-to-disable-automatic-driver-updates-in-windows-11-24h2/) so the validated chipset driver isn't replaced again.

### Fix 6: Disable USB power management everywhere

The definitive fix for sleep-related USB death.

1. In **Device Manager > Universal Serial Bus controllers**, open **Properties > Power Management** on every hub and controller and uncheck *Allow the computer to turn off this device to save power*.
2. **Control Panel > Power Options > Change advanced power settings > USB settings > USB selective suspend setting** > **Disabled** for both battery and plugged-in.
3. Restart and test across sleep/wake cycles specifically — this fix only proves itself at resume.
4. Microsoft's [Windows hardware support pages](https://support.microsoft.com/en-us/windows) document the current USB power-management behavior if you need the official reference.

### Fix 7: Address physical port damage

For the single dead port that software can't touch.

1. Inspect the port with a flashlight and magnifier — look for **bent pins** (the small contacts inside), packed lint, or a loose-feeling connector shell.
2. **Gently** straighten a bent pin with a toothpick or plastic spudger — never metal, and never with power connected. If pins are broken off, stop; the port needs professional repair.
3. Blow out debris with compressed air. Test with a sacrificial cable/device — not your most precious flash drive — in case of a short.
4. A single dead port on an otherwise healthy laptop is a fine candidate to simply abandon — you have other ports, and a small USB hub ($10–15) restores the lost connectivity without a repair bill.

## Closing

USB failures announce their cause if you scope them first: one dead port is physical, all dead ports is controller/driver/power, one dead device is the device. Cold-reset the bus, reinstall the controllers, refresh the chipset driver, and kill USB power management — that sequence revives the overwhelming majority of dead USB subsystems without ever opening the laptop.
