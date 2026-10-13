---
title: "USB Ports Not Working on Your HP Laptop? Here's How to Fix Them"
slug: how-to-fix-usb-ports-not-working-on-hp-laptop
date: 2026-09-25
categories: ["drivers"]
tags: ["hp usb ports not working", "usb device not recognized hp", "hp laptop usb fix", "usb ports dead", "usb selective suspend"]
description: "USB ports dead on your HP laptop? From HP's own diagnostics to driver resets and power settings, here's the complete fix sequence for HP machines."
thumbnail: "/images/thumbs/how-to-fix-usb-ports-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why did all my USB ports stop working at once on my HP laptop?"
    a: "When every port dies simultaneously, it's almost never the physical ports — it's the USB controller driver, a power management state, or a chipset driver problem. A single crashed USB host controller takes all its ports down together. The fix is usually a driver reset or a full power drain, not hardware repair. If only one port is dead while others work, that's when you suspect physical damage to that specific port."
  - q: "Does HP have a built-in tool to test USB ports?"
    a: "Yes. HP PCs include HP PC Hardware Diagnostics, accessible by pressing Esc during boot and selecting F2, or from Windows via the HP PC Hardware Diagnostics app. It has a component test for USB ports that checks the controller hardware independently of Windows. If the ports fail there too, you're looking at a hardware fault; if they pass, the problem is in Windows drivers or settings."
  - q: "Can USB selective suspend break my USB ports?"
    a: "Yes, and it's a classic cause of ports that work intermittently or stop recognizing devices until a reboot. Selective suspend lets Windows power down individual USB ports to save battery, but the wake-up handshake sometimes fails. Disabling it in the power plan is safe — it costs a tiny amount of battery life — and it permanently eliminates this whole category of flaky USB behavior on laptops."
  - q: "Should I update the chipset driver to fix USB issues on HP?"
    a: "Often, yes. The USB host controllers are part of the chipset, and HP periodically releases chipset driver updates that fix USB stability and compatibility problems. Get the chipset driver from HP's support site for your exact model rather than from Intel or AMD directly, since HP customizes the package for their hardware. Install it after uninstalling the problematic USB controllers for the cleanest result."
---

When USB ports quit on an HP laptop, the symptoms range from "device not recognized" popups to ports that are completely dead — no power, no data, nothing. HP machines have a few brand-specific angles worth knowing: the built-in hardware diagnostics that can test ports outside of Windows, HP's customized chipset drivers, and the power management defaults that HP ships.

This guide is ordered the way HP's own support escalation works: rule out the device and the port, test the hardware with HP diagnostics, then repair the Windows driver layer. Follow it in sequence — jumping straight to driver surgery before checking the basics wastes time.

A quick note on how HP structures USB on most of their laptops: the USB 2.0, USB 3.x, and USB-C ports typically hang off a small number of host controllers managed by the chipset driver, which means a single driver or power-state problem can take out every port at once. That is actually good news — when all ports fail together, the cause is almost never five broken ports, but one unhappy controller. The fixes below target that controller layer directly after the quick physical checks, which is why they work even when the failure looks catastrophic.

## Why this happens

- **USB selective suspend** powered the port down and it never woke back up — the most common cause of flaky ports.
- **Corrupted USB host controller driver**, often after a Windows update.
- **The connected device needs more power** than the port delivers, common with external hard drives on battery power.
- **Chipset driver is outdated**, causing enumeration failures on newer USB devices.
- **Static charge / stuck embedded controller** holding the USB subsystem in a bad state.
- **Physical port damage** — bent pins, debris, or cracked solder joints from repeated plugging.
- **Fast Startup hibernation state** carrying a broken USB stack across reboots.
- **BIOS USB settings** disabled, or a BIOS bug affecting the controller.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test the device and the port independently

Isolate whether the problem is the device, the port, or the laptop.

1. Plug the USB device into a different port on the same laptop.
2. Plug the same device into a different computer to confirm the device itself works.
3. Try a simple low-power device (a basic mouse or flash drive) in the suspect port — if that works but your external drive doesn't, it's a power issue.
4. Inspect the port with a flashlight for bent pins, lint, or debris. Clean gently with compressed air.

### Fix 2: Do a full power drain

This clears the embedded controller state that can wedge the USB subsystem.

1. Shut the laptop down completely and unplug the charger and all USB devices.
2. If your HP has a removable battery, take it out. If not, hold the power button for 30 seconds with everything unplugged.
3. Reconnect the charger (leave USB devices unplugged), power on, and test the ports before plugging anything else in.

### Fix 3: Run HP PC Hardware Diagnostics

HP's built-in test tells you definitively whether it's hardware or software.

1. Restart and press **Esc** repeatedly during boot, then press **F2** for System Diagnostics.
2. Run the **Component Tests > USB** port test if available, or the full system test.
3. If ports fail here — outside of Windows — it's a hardware fault. Contact HP support or a repair shop.
4. If they pass, the hardware is fine and the problem is in Windows. Continue below with confidence.

### Fix 4: Reinstall the USB controllers in Device Manager

The core Windows-side fix.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Universal Serial Bus controllers**.
3. Right-click each **USB Root Hub** and **USB Host Controller** entry and choose **Uninstall device**. Do them one at a time — your mouse may stop working if it's USB, so keep a touchpad handy.
4. When all are uninstalled, restart. Windows redetects and reinstalls every controller fresh.
5. Test the ports before reinstalling any third-party USB software.

### Fix 5: Disable USB selective suspend

Stops Windows from power-napping your ports.

1. Open **Control Panel > Power Options** and click **Change plan settings** on your active plan, then **Change advanced power settings**.
2. Expand **USB settings > USB selective suspend setting**.
3. Set both **On battery** and **Plugged in** to **Disabled**.
4. Click OK and restart. This is also the fix when ports work after reboot but die again later — the exact signature of selective suspend.

For a deeper look at this setting, see [how to turn off USB selective suspend](/articles/how-to-turn-off-usb-selective-suspend-on-windows-11/).

### Fix 6: Update the HP chipset driver

The chipset driver owns the USB controllers.

1. Go to [HP's support site](https://support.hp.com/us-en) and enter your exact model number.
2. Download the latest **chipset** driver package (Intel or AMD, matching your CPU).
3. Install it and restart — even if the version looks similar, HP's package includes customizations for your board.
4. Retest all ports, including USB-C ports, which are especially chipset-dependent.

### Fix 7: Disable Fast Startup

Fast Startup can carry a broken USB stack from one boot to the next, making reboots useless.

1. Open **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup** and save.
4. Shut down fully (not restart) and power back on — this is the first true cold boot the machine has had.

## Closing

On HP laptops, the winning combination is usually the power drain plus the USB controller reinstall, with selective suspend disabled to keep the problem from coming back. HP's boot-time diagnostics are your best friend here — a two-minute test that tells you whether to keep troubleshooting software or start planning a hardware repair. If your USB-C ports specifically are misbehaving (charging or display issues rather than data), our guide to [USB-C charging problems](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-on-windows-11/) covers the power-delivery side of those ports.
