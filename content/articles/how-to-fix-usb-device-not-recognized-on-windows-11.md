---
title: "How to Fix USB Device Not Recognized on Windows 11"
slug: how-to-fix-usb-device-not-recognized-on-windows-11
date: 2026-09-29
categories: ["drivers"]
tags: ["usb device not recognized", "windows 11", "usb driver", "device manager", "usb troubleshooting"]
description: "USB device not recognized on Windows 11? Fix the error with 7 proven repairs — from power resets to USB controller driver reinstalls."
thumbnail: "/images/thumbs/how-to-fix-usb-device-not-recognized-on-windows-11.webp"
faqs:
  - q: "Why does Windows 11 keep saying USB device not recognized?"
    a: "The message means Windows detected something on the USB bus but could not load a working driver for it, or the port did not supply stable power during enumeration. Corrupt USB controller drivers, selective suspend cutting power, a faulty cable or hub, and dirty contacts are the usual causes. The fix order below rules out power and cable problems before touching drivers."
  - q: "Can a Windows update cause the USB not recognized error?"
    a: "Yes, and it is a common trigger. Feature updates sometimes replace the manufacturer's USB or chipset driver with a generic Microsoft one that mis-handles certain controllers, especially older Renesas, VIA, or Fresco Logic chips. Rolling back the USB controller driver or reinstalling the laptop maker's chipset package usually resolves update-triggered failures within minutes."
  - q: "Should I disable USB selective suspend to fix USB errors?"
    a: "Disabling USB selective suspend is worth trying when the error appears after the laptop sleeps or when devices disconnect randomly. The setting lets Windows cut power to idle ports, and some devices fail to re-enumerate cleanly. Turn it off in the advanced power plan options; the only cost is slightly higher idle power draw on battery."
  - q: "When is the USB not recognized error a hardware problem?"
    a: "Suspect hardware when the error follows the device or port everywhere — the device fails on every port and every computer, or one specific port fails with every device you plug in. If the error moves with the device, replace the cable or device; if it stays with one port, that port's physical connector or its link to the motherboard is damaged."
---

Few Windows errors are as maddening as "USB device not recognized." You plug in a flash drive, an external hard disk, or a phone, and Windows 11 tells you the last USB device you connected malfunctioned — without telling you why. The device may work fine on another machine, which makes the error feel personal. It isn't. It almost always comes down to three things: unstable power on the port, a corrupt USB controller driver, or a cable that can't carry the signal cleanly.

The good news is that this error resolves in the great majority of cases without replacing anything. Windows' own USB stack, the hardware troubleshooter, and a careful driver reinstall fix most instances. This guide walks you through seven fixes in order — starting with the two-minute checks, moving into driver repairs, and ending with the hardware verdict. Work through them in sequence rather than jumping ahead.

## Why this happens

- **Corrupt or generic USB controller driver.** Windows replaced the maker's chipset driver with a generic one that mis-enumerates the device.
- **USB selective suspend cutting power.** Windows powers down the idle port and the device fails to re-enumerate on wake.
- **Faulty or under-rated cable.** Cheap cables cause signal errors that Windows reads as a malfunctioning device.
- **Under-powered hub or front-panel port.** The port can't deliver the 500–900 mA the device needs during startup.
- **Dirty or damaged connector contacts.** Oxidation on pins causes intermittent enumeration failures.
- **Device firmware mismatch.** The peripheral's firmware predates Windows 11's stricter USB enumeration.
- **Damaged USB port or device controller.** Physical failure — rare, but the last stop on the list.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Power-cycle the USB bus

A stale electrical state in the controller causes a surprising share of these errors.

1. Unplug the device and any USB hubs from the laptop.
2. Shut the laptop down completely — hold **Shift** while clicking Shut down to skip Fast Startup.
3. If the battery is removable, take it out; otherwise unplug the AC adapter and hold the power button for 15 seconds.
4. Wait a full minute, reconnect power, boot up, then plug the device directly into a built-in USB port (no hub).
5. Try a different built-in port if the error persists — one port's power delivery may be flaky.

### Fix 2: Try the device and cable elsewhere

Isolate whether the fault is the device, the cable, or your laptop.

1. Plug the same device with the same cable into a different computer — if it fails there too, the device or cable is the problem.
2. Swap the cable for a short, known-good one — especially with external drives and phones, the cable is the culprit more often than people believe.
3. If the device works elsewhere, your laptop's port or driver stack is at fault — continue to Fix 3.
4. For external hard drives, use the maker's own cable; long aftermarket cables cause voltage drop during spin-up.

### Fix 3: Run the Hardware and Devices troubleshooter

Windows 11's automated check repairs common USB enumeration glitches.

1. Press **Windows + R**, type `msdt.exe -id DeviceDiagnostic`, and press Enter.
2. Click **Advanced**, check **Apply repairs automatically**, then **Next**.
3. Let it detect problems — it commonly flags and fixes malfunctioning USB composite devices.
4. Restart when it asks, then reconnect the device.
5. Check the latest [Windows 11 guidance](https://support.microsoft.com/en-us/windows) if the troubleshooter reports an unfixable driver issue.

### Fix 4: Disable USB selective suspend

Stop Windows from cutting power to idle ports — a top fix for devices that fail after sleep.

1. Open **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **USB settings > USB selective suspend setting**.
3. Set both **On battery** and **Plugged in** to **Disabled**.
4. Click OK, restart, and test the device.
5. Also in **Device Manager**, under **Universal Serial Bus controllers**, right-click each **USB Root Hub**, open **Properties > Power Management**, and uncheck **Allow the computer to turn off this device to save power**.

### Fix 5: Reinstall the USB controller drivers

The core driver fix for stubborn "not recognized" errors.

1. Open **Device Manager** (Windows + X > Device Manager).
2. Expand **Universal Serial Bus controllers**.
3. Right-click each **USB Root Hub** and **USB Host Controller** entry and choose **Uninstall device** — do not delete the driver software if it asks; you want Windows to reuse the store.
4. Restart the laptop — Windows rebuilds the entire USB stack from scratch on boot.
5. If the error persists, download your laptop maker's **chipset driver** package from their support site and install it over the generic drivers.

When Device Manager shows an **Unknown USB Device (Device Descriptor Request Failed)**, the reinstall above is exactly the fix — that entry is Windows' record of the failed enumeration. Related Thunderbolt port issues have their own guide: [how to fix Thunderbolt not working on laptop in Windows 11 24H2](/articles/how-to-fix-thunderbolt-not-working-on-laptop-in-windows-11-24h2/).

### Fix 6: Update the device's own driver or firmware

Some devices need their own software before Windows can talk to them.

1. In **Device Manager**, find the device under **Universal Serial Bus controllers** or as an **Unknown device**.
2. Right-click it, choose **Update driver > Search automatically for drivers**.
3. If that fails, check the device manufacturer's site for a Windows 11 driver or firmware updater — common for printers, scanners, DACs, and Android phones (which may need the Google USB driver or the maker's MTP driver).
4. For phones stuck as "MTP USB Device," install the manufacturer's USB driver package, then toggle the phone's USB mode from **Charging** to **File transfer**.
5. After installing, unplug and reconnect the device so Windows enumerates it with the new driver.

### Fix 7: Reset USB power limits and check hardware

The last software stops before concluding it's physical.

1. Unplug all USB devices except keyboard and mouse.
2. In **Device Manager**, check for any device with a yellow exclamation mark under **Universal Serial Bus controllers** — its **Properties > General** tab states the exact error.
3. A **Code 43** on a controller usually means driver corruption; repeat Fix 5, but this time check **Delete the driver software** during uninstall so Windows fetches a fresh copy.
4. If one specific port fails with every device, that port's connector is damaged — use a powered USB hub on a working port as a workaround.
5. For ports that worked after a Windows update and broke again, block driver updates for the USB controller via the maker's chipset installer rather than Windows Update.

If you see an **Unknown device** entry that refuses to resolve, our guide on [how to fix unknown device in Device Manager in Windows 11 24H2](/articles/how-to-fix-unknown-device-in-device-manager-in-windows-11-24h2/) covers identifying and tracking down its driver.

## Closing

The "USB device not recognized" error looks alarming but is a driver or power problem in the vast majority of cases — the power-cycle, the selective-suspend disable, and the controller reinstall resolve it. If you've worked through all seven fixes and one port still fails with every device, that's your signal that the port itself is damaged and it's time for a repair shop.
