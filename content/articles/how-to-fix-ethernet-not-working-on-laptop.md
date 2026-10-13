---
title: "Ethernet Not Working on Your Laptop? Here's How to Fix It"
slug: how-to-fix-ethernet-not-working-on-laptop
date: 2026-10-12
categories: ["drivers"]
tags: ["ethernet", "wired network", "lan driver", "troubleshooting", "device manager"]
description: "Wired connection dead on your laptop? Diagnose whether it's the cable, the adapter driver, or Windows settings, then restore your Ethernet link step by step."
thumbnail: "/images/thumbs/how-to-fix-ethernet-not-working-on-laptop.webp"
faqs:
  - q: "Why does my laptop not recognize the Ethernet cable at all?"
    a: "Three suspects in order: a bad or loose cable, a disabled or corrupted network adapter driver, and a BIOS-level Ethernet setting that got switched off. Check Device Manager's Network adapters section first — if the Ethernet adapter is missing, disabled, or shows a warning icon, the problem is software or firmware, not the cable."
  - q: "Do I need a special driver for laptop Ethernet?"
    a: "Most modern laptops use Realtek, Intel, or Killer Ethernet controllers, and Windows ships generic drivers that work for basic connectivity. But the generic driver can lack power management and speed features, so downloading the vendor-specific driver from your laptop maker's support page is the better long-term fix."
  - q: "My Ethernet works through a USB dock but not the built-in port. Why?"
    a: "That narrows it to the built-in port: a bent pin, oxidation on the contacts, a disabled controller in BIOS, or the built-in adapter's driver being corrupted. The dock proves the network and cable are fine, so focus all troubleshooting on the internal Ethernet controller and its driver."
  - q: "Can a Windows update break Ethernet?"
    a: "Yes — major feature updates sometimes replace a working vendor driver with a generic one, reset power management settings, or corrupt the adapter's configuration. If Ethernet died right after an update, rolling back or reinstalling the network adapter driver is the highest-yield fix."
---

You plug in the cable, expect the little green lights, and get nothing. The taskbar shows the globe or the "no internet" warning, and your laptop stubbornly refuses to use the wired connection it was using yesterday. Ethernet problems feel hardware-y and scary, but on laptops they're a driver or configuration issue far more often than a dead port.

The good news: Ethernet failures follow a very predictable diagnostic path. Cable, port, adapter state, driver, Windows network stack — check them in that order and you'll find the culprit in minutes rather than hours. This guide walks the whole path.

## Why this happens

- **A failed or marginal cable.** Cables fail more often than ports do. A cable with a broken pair can work intermittently for weeks, then drop entirely. See [how cable faults mimic driver issues](/articles/how-to-fix-ethernet-not-working-on-laptop-in-windows-11-24h2/).
- **The network adapter is disabled.** Windows or a power-saving feature turned the adapter off. Device Manager shows it grayed out — a one-click fix once you know to look.
- **A corrupted or replaced adapter driver.** Windows updates love swapping your vendor Ethernet driver for a generic one. The generic driver usually works, but sometimes it doesn't.
- **Aggressive power management.** "Allow the computer to turn off this device to save power" can put the Ethernet controller into a state it never wakes from, especially on battery.
- **A misbehaving network stack.** Corrupted TCP/IP configuration, a stale DHCP lease, or a wrong static IP can make the port look dead even though link is up.
- **The Ethernet controller is disabled in BIOS/UEFI.** Some laptops expose the LAN controller as a BIOS toggle. A reset BIOS defaults or an update can flip it off.
- **Physical port damage.** Bent pins, debris, or a loose solder joint. Rare on laptops, but real — especially if the jack feels wobbly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out the cable and the port in 60 seconds

Don't touch drivers until you've confirmed the physical layer.

1. Plug the same cable into a different device (another laptop, a game console, anything). If it fails there too, replace the cable — done.
2. Try a different port on the router or switch, and watch the link LEDs on the laptop's jack. No LEDs at all usually means the adapter isn't initialized (software) rather than a dead cable.
3. Inspect the laptop's RJ-45 jack with a flashlight. Look for bent pins, lint, or debris. Blow it out with compressed air; use a toothpick to straighten a gently bent pin.
4. If you use a USB-to-Ethernet adapter or dock, test the built-in port separately — this isolates which controller is actually broken.

### Fix 2: Check the adapter state in Device Manager

This is where most Ethernet mysteries get solved.

1. Press **Win + X** and open **Device Manager**. Expand **Network adapters**.
2. Look for your Ethernet controller (often "Realtek PCIe GbE Family Controller," "Intel Ethernet Connection," or similar).
3. If it's missing entirely, skip to Fix 5 (driver reinstall). If it's grayed out, right-click it and choose **Enable device**.
4. If it shows a yellow warning icon, note the error code and proceed to Fix 4.
5. Also check **Network Connections** (Win + R, type `ncpa.cpl`). Right-click the Ethernet connection and make sure it's **Enabled**, not **Disabled**.
6. Compare with our guide on [USB devices that vanish from Device Manager](/articles/how-to-fix-usb-device-not-recognized-in-windows-11-24h2/) — the diagnostic pattern is the same.

### Fix 3: Disable power management on the adapter

The single most common silent Ethernet killer on laptops.

1. In **Device Manager**, right-click the Ethernet adapter and choose **Properties**.
2. Go to the **Power Management** tab and **uncheck** "Allow the computer to turn off this device to save power."
3. Go to the **Advanced** tab. Look for properties like **Energy Efficient Ethernet**, **Green Ethernet**, or **Power Saving Mode** — set them to **Disabled**.
4. If you see **Wake on LAN** options and don't use them, disable those too; they can leave the controller in a half-asleep state.
5. Click **OK**, unplug the cable for 10 seconds, plug it back in, and retest.

### Fix 4: Reset the Windows network stack

When the link is up but nothing flows, the stack is usually the culprit.

1. Open **Terminal (Admin)** and run these commands in order:
   - `netsh winsock reset`
   - `netsh int ip reset`
   - `ipconfig /release`
   - `ipconfig /renew`
   - `ipconfig /flushdns`
2. Restart the laptop.
3. Alternatively, use the nuclear option: **Settings** > **Network & internet** > **Advanced network settings** > **Network reset**. This reinstalls every adapter and resets all network components to defaults.
4. After a network reset, reconnect and retest. You'll need to rejoin Wi-Fi networks, but Ethernet should just work.

### Fix 5: Reinstall the Ethernet driver properly

Driver corruption is the classic post-update Ethernet killer.

1. In **Device Manager**, right-click the Ethernet adapter and choose **Uninstall device**. Check the box "Attempt to remove the driver for this device" if offered.
2. Restart the laptop. Windows will reinstall a driver automatically — test with it first.
3. If that doesn't work, download the exact Ethernet driver for your model from your manufacturer's support page — for example [Dell support](https://www.dell.com/support) — rather than letting Windows pick one.
4. Before installing, run the installer as administrator and choose a **clean** or **custom** install if offered.
5. After installation, reapply Fix 3's power-management settings — driver reinstalls reset them.

### Fix 6: Check BIOS/UEFI and test with a live environment

If Windows-level fixes fail, look below the OS.

1. Reboot into BIOS/UEFI (usually F2 or Del during startup). Find the **Onboard LAN**, **Ethernet Controller**, or **LAN** setting and make sure it's **Enabled**.
2. While there, check that **Deep Sleep** or similar aggressive power states aren't interfering.
3. Save and exit, then test again in Windows.
4. For a definitive hardware-vs-software verdict, boot a Linux live USB and test the Ethernet port there. If it works in Linux, the hardware is fine and the problem is 100% Windows-side — go back to Fixes 2–5.

### Fix 7: Inspect for hardware failure

The last stop — only after the software path is exhausted.

1. If the jack feels loose or the cable won't click in firmly, the port may be physically damaged. Laptops with RJ-45 ports that get yanked sideways can crack solder joints.
2. Try a USB-to-Ethernet adapter as a workaround — this also confirms the rest of the network path is healthy.
3. If the port is damaged and you need the built-in jack, contact the manufacturer for a board-level repair quote. Out-of-warranty, a quality USB Ethernet adapter is far cheaper than a motherboard replacement.

Microsoft documents network troubleshooting in more depth on the official [Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

Ethernet failures almost always yield to methodical diagnosis: confirm the cable and jack, verify the adapter is enabled and healthy in Device Manager, kill the power-saving gremlins, reset the network stack, and reinstall the vendor driver. The port itself is rarely dead — it's usually just silenced by a setting, a driver, or a tired cable. Work the list top to bottom and you'll have link lights again.
