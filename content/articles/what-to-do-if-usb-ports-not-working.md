---
title: "What to Do If USB Ports Are Not Working on Your Laptop"
slug: what-to-do-if-usb-ports-not-working
date: 2026-10-10
categories: ["drivers"]
tags: ["usb ports", "usb not working", "device manager", "power management", "drivers"]
description: "USB ports not working on your Windows laptop? Work through port tests, power settings, driver resets, and BIOS checks to bring them back."
thumbnail: "/images/thumbs/what-to-do-if-usb-ports-not-working.webp"
faqs:
  - q: "All my USB ports stopped working at once. What is the most likely cause?"
    a: "When every port fails simultaneously, the USB controller driver or its power state is the prime suspect, not the individual ports. Reinstall the USB controllers in Device Manager and disable USB selective suspend. Simultaneous failure of all ports is rarely a hardware problem with the ports themselves."
  - q: "One USB port works but the others do not. Is the motherboard damaged?"
    a: "Not necessarily. Individual ports can be disabled in software, starved by power management, or suffering from a bent pin inside the connector. Test each port with a simple device like a wired mouse, check Device Manager for disabled hubs, and inspect the port with a flashlight before assuming board damage."
  - q: "Can USB selective suspend really break my ports?"
    a: "Yes. Selective suspend powers down idle USB devices to save battery, and on some laptops the port fails to wake the device afterward. Disabling it in the power plan is a standard fix for ports that work after a reboot but die after the laptop sleeps. It costs a small amount of battery life."
  - q: "My USB device works on another computer but not on my laptop. Why?"
    a: "That isolates the fault to your laptop: its driver stack, power delivery, or port hardware. Run through the driver reinstall and power management fixes in this guide. If the device is power-hungry, like an external hard drive, also try a powered hub — the laptop's port may simply not supply enough current."
---

USB ports fail in two distinct patterns, and the pattern is the diagnosis. Every port dead at once means the controller or its driver. One port dead means that port's hardware, its hub entry, or its power state. A port that works after reboot but dies after sleep means power management. Read your pattern before you start, because it tells you which half of this guide matters most.

The fixes run from instant (try another device) through software (drivers, power settings) to hardware (BIOS, physical inspection). Almost all USB port failures on Windows laptops are software — the ports themselves are simple and sturdy.

## Why this happens

- **USB controller driver corruption:** The host controller driver manages all ports; when it corrupts, every port on that controller dies together.
- **USB selective suspend:** Power saving suspends idle ports and some never wake cleanly, especially after sleep.
- **Disabled USB hub in Device Manager:** Hubs can be disabled by software or user error, killing their downstream ports silently.
- **Power delivery limits:** Unpowered ports cannot feed hungry devices like external drives; the device fails while the port is fine.
- **Physical damage or debris:** Bent pins, pocket lint, and worn connectors cause single-port failures.
- **BIOS USB settings:** Firmware can disable USB ports or legacy support independently of Windows.
- **Static charge on the controller:** A buildup can wedge the USB controller until a full power drain clears it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test with a different device and different port

Plug a simple, known-good device — a wired mouse is ideal — into each port in turn. If the mouse works everywhere, your original device is the problem, not the ports. If the mouse fails on one port but works on others, you have a single-port issue: inspect that port with a flashlight for bent pins or debris and try gently cleaning it with compressed air. If the mouse fails on all ports, continue — the fault is in the controller or software. This two-minute test prevents hours of driver work for a dead flash drive.

### Fix 2: Do a full power drain

Shut the laptop down completely, unplug the charger, and if the battery is removable, take it out. Hold the power button down for 30 seconds. Reconnect power (leave the battery out if you removed it) and boot. This drains fleeting charge from the USB controller and forces it to reinitialize from cold — a classic fix for controllers wedged by static or a bad sleep cycle. Test the ports immediately after boot, before the laptop sleeps again. If ports work now but die after sleep, you have confirmed a power-management problem and Fix 4 is your permanent answer.

### Fix 3: Reinstall the USB controllers in Device Manager

Open Device Manager (Win + X), expand "Universal Serial Bus controllers," and for each "USB Root Hub" and "USB Host Controller" entry, right-click and choose Uninstall device. Do not worry — Windows reinstalls them on restart. Reboot and let Windows redetect the entire USB subsystem fresh. This clears corrupted controller state that survives ordinary reboots and is the highest-yield software fix for all-ports-dead scenarios. After the reboot, verify the controllers reappear with no warning icons before testing devices. If a controller shows an error after reinstall, the chipset driver underneath needs attention — see our guide on [updating drivers properly](/articles/how-to-update-drivers-on-windows-11-laptop/).

### Fix 4: Disable USB selective suspend

Open Control Panel, Power Options, "Change plan settings" for your active plan, then "Change advanced power settings." Expand USB settings, then "USB selective suspend setting," and set both On battery and Plugged in to Disabled. Click OK and restart. Selective suspend is the leading cause of ports that work after boot but fail after sleep, because the port never properly resumes the attached device. Disabling it costs a small amount of battery life — a fair trade for reliable ports. Our focused guide on [turning off USB selective suspend](/articles/how-to-turn-off-usb-selective-suspend-on-windows-11/) covers the registry-level variant for stubborn cases.

### Fix 5: Check power management on each USB hub

In Device Manager, under Universal Serial Bus controllers, right-click each USB Root Hub, open Properties, and on the Power Management tab uncheck "Allow the computer to turn off this device to save power." Repeat for every hub entry. This is selective suspend's cousin at the device level, and on some laptops it is the actual culprit even with the plan setting disabled. While you are here, look for any hub showing as disabled — right-click and enable it. A single disabled hub silently kills every port downstream of it, which mimics a hardware failure convincingly.

### Fix 6: Check the BIOS USB settings

Restart into BIOS/UEFI setup and look for USB configuration: ensure USB ports, USB controller, and legacy USB support are enabled. Some business laptops allow individual ports to be disabled in firmware — verify none are switched off. Save and exit. If ports were disabled here, no Windows fix could ever have helped, which is why this check belongs in the sequence. Also note your BIOS version against the latest on the manufacturer's site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — since USB controller firmware fixes ride along with BIOS updates. Microsoft's Windows support hub documents USB troubleshooting basics as supplementary reading.

### Fix 7: Test hardware with diagnostics and a powered hub

Run the manufacturer's hardware diagnostics USB test. If a specific port fails while others pass, that port's hardware is damaged — on most laptops individual ports are not economically repairable, so remap your usage to working ports or add a hub. If all ports fail diagnostics, the board-level controller may be faulty — a repair-shop matter. As an immediate workaround, a powered USB hub on a working port (or a USB-C dock) restores connectivity for your devices regardless of the underlying fault. For devices that enumerate but misbehave, our guide to [USB device not recognized errors](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/) picks up where this one leaves off.

## Closing

USB port failures are pattern problems: all ports means controller software, one port means that port's hardware or hub entry, after-sleep means power management. Match your pattern, apply the matching fix, and the ports come back — usually without spending anything. Keep selective suspend off if your laptop is prone to it, and keep the chipset driver current, since the USB controllers live or die with the chipset underneath them.
