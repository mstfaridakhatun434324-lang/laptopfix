---
title: "How to Turn Off USB Selective Suspend in Windows 11 24H2"
slug: how-to-turn-off-usb-selective-suspend-in-windows-11-24h2
date: 2026-09-11
categories: ["battery"]
tags: ["usb selective suspend", "power settings", "usb devices", "windows 11"]
description: "USB devices randomly disconnecting or not waking properly? Disabling USB selective suspend in Windows 11 24H2 often fixes it. Here's exactly where the setting hides."
thumbnail: "/images/thumbs/how-to-turn-off-usb-selective-suspend-in-windows-11-24h2.webp"
faqs:
  - q: "What is USB selective suspend?"
    a: "It's a Windows power-saving feature that puts individual USB ports into a low-power suspended state when they're idle. In theory it saves battery. In practice, buggy device drivers often fail to wake the port properly, causing disconnects, unresponsive peripherals, and external drives that vanish until you replug them."
  - q: "Will disabling USB selective suspend hurt battery life?"
    a: "Barely. The savings from suspending idle USB ports are tiny on modern laptops — a few percent at most. If you're troubleshooting disconnects, disable it without guilt. You can re-enable it later once you've confirmed whether it was the cause."
  - q: "Why do my USB devices keep disconnecting on Windows 11?"
    a: "The most common causes are USB selective suspend putting ports to sleep, underpowered USB hubs, outdated chipset drivers, and Windows turning off the device to save power (a separate per-device setting in Device Manager). Work through all of them — they're independent settings."
  - q: "Does USB selective suspend affect USB-C charging?"
    a: "It can. On some laptops, selective suspend interferes with USB-C PD negotiation or causes the charging port to renegotiate repeatedly, which shows up as slow or intermittent charging. If your USB-C charging is flaky, disabling selective suspend is a worthwhile test."
---

Your external drive vanishes mid-transfer. Your USB headset crackles and dies until you unplug it. Your mouse freezes for two seconds every few minutes. If your USB devices behave like they're haunted, USB selective suspend is a prime suspect — a well-meaning power feature with a long history of breaking real hardware.

The setting is buried in the classic Control Panel power options, which Microsoft keeps hiding deeper with every Windows 11 update. Here's how to find it in 24H2 and turn it off properly — including the second, separate setting most guides miss.

## Why this happens (why the feature causes problems)

- **Buggy device firmware:** Many USB devices don't implement the suspend/resume protocol correctly and never wake up properly once suspended.
- **Driver conflicts:** The USB host controller driver and the device driver can disagree about power state, leaving the port in limbo.
- **Hub complications:** Cheap USB hubs often don't forward suspend/resume signaling correctly, so everything downstream misbehaves.
- **Aggressive power plans:** The Balanced plan enables selective suspend by default; some manufacturer "eco" utilities make it even more aggressive.
- **Separate per-device setting:** Even with selective suspend off, Windows can still power down individual devices via "Allow the computer to turn off this device to save power" in Device Manager — a different toggle.
- **USB-C PD interplay:** On charging-capable ports, suspend signaling can interrupt power negotiation, causing charge flapping.

## How to fix it

Work through these in order.

### Fix 1: Disable USB selective suspend in Power Options

The main setting. Buried, but straightforward once you know the path.

1. Press **Windows key + R**, type `control`, and press Enter to open the classic **Control Panel**.
2. Go to **Hardware and Sound > Power Options**.
3. Next to your active plan, click **Change plan settings**.
4. Click **Change advanced power settings** to open the Advanced Settings dialog.
5. Expand **USB settings**, then expand **USB selective suspend setting**.
6. Set both **On battery** and **Plugged in** to **Disabled**.
7. Click **Apply**, then **OK**. The change takes effect immediately — no reboot needed.
8. Test your problematic USB device for 15-30 minutes. If disconnects stop, you've found it.

### Fix 2: Disable per-device power management in Device Manager

This is the second setting most people miss — it operates independently of selective suspend.

1. Right-click **Start** and open **Device Manager**.
2. Expand **Universal Serial Bus controllers**.
3. For each **USB Root Hub** and **Generic USB Hub** entry: right-click → **Properties** → **Power Management** tab → **uncheck** "Allow the computer to turn off this device to save power" → OK.
4. Also expand **Human Interface Devices** and do the same for your mouse/keyboard entries if they have a Power Management tab.
5. If your problem device appears under another category (e.g., **Sound** for a headset, **Disk drives** for an external SSD), check its Properties for a Power Management tab too.
6. This is especially important for external drives that "sleep" and won't wake — the hub-level setting is usually the culprit there.

### Fix 3: Update chipset and USB controller drivers

Old host controller drivers suspend ports more aggressively and resume them worse.

1. In **Device Manager**, expand **Universal Serial Bus controllers** and note the host controller names (Intel, AMD, ASMedia, etc.).
2. Download the latest **chipset driver package** from your laptop manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) — or from [Intel](https://www.intel.com/content/www/us/en/support/detect.html)/[AMD](https://www.amd.com/en/support/download/drivers.html) directly for the chipset.
3. Install, reboot, and re-verify that selective suspend is still Disabled (driver installs sometimes reset power settings).
4. Check for a **BIOS update** too — USB power behavior is partly firmware-controlled, and manufacturers fix suspend bugs in BIOS releases.
5. Retest the device. If it was a driver-level resume bug, this fixes it even with selective suspend re-enabled — though leaving it disabled remains the safer choice.

### Fix 4: Test without hubs and with different ports

Isolate whether the port, the hub, or the device is at fault.

1. Plug the problem device **directly into the laptop**, bypassing all hubs, docks, and dongles.
2. Try a **different USB port** — preferably one on the opposite side of the laptop (different internal hub).
3. If the device works fine directly but fails through the hub, the hub is the problem: replace it with a **powered hub** (one with its own AC adapter). Unpowered hubs cause exactly these symptoms under load.
4. For USB-C devices, try both USB-C ports — on many laptops only one is full-featured.
5. If the device fails on every port directly connected, the device itself (or its cable) is likely faulty — try a different cable before replacing the device.

### Fix 5: Check USB power output

Some disconnects are brownouts, not suspend issues.

1. In **Device Manager > Universal Serial Bus controllers**, open each **USB Root Hub > Properties > Power** tab to see power available per port.
2. Power-hungry devices (external HDDs, audio interfaces) on unpowered hubs brown out under load — symptoms mimic suspend problems.
3. Move power-hungry devices to ports directly on the laptop, or use a powered hub.
4. For external drives specifically: if the drive has its own power adapter, use it. Bus-powered spinning drives are the most common victims.
5. In **Power Options > Advanced settings**, also check **PCI Express > Link State Power Management** — set to **Off** when troubleshooting USB issues, as PCIe power saving can affect the USB controller.

### Fix 6: Disable fast startup and check for interference

Fast Startup preserves driver state across shutdowns, which can preserve a broken USB power state.

1. **Control Panel > Power Options > Choose what the power buttons do > Change settings that are currently unavailable** → uncheck **Turn on fast startup**.
2. Do a full **Restart** (not shutdown) to clear driver state.
3. Check for RF interference if the device is wireless (2.4GHz mouse/keyboard dongles): move the dongle away from USB 3.0 ports using a short extension cable — USB 3.0 is notorious for interfering with 2.4GHz receivers.
4. Try the device with **Bluetooth** temporarily off if it's a wireless USB dongle, to rule out radio conflicts.
5. If disconnects correlate with the laptop going to sleep/wake, also check **Device Manager > Network adapters > Wi-Fi > Power Management** — Wi-Fi power saving during sleep can cascade into USB controller resets on some platforms.

### Fix 7: When to re-enable (and what to do if nothing works)

Selective suspend isn't evil — it's just buggy with certain hardware.

1. Once you've confirmed the disconnects are gone with it disabled, you can leave it off permanently. The battery cost is negligible.
2. If you want to re-enable it later (e.g., squeezing maximum battery on a long flight), do so knowing which device misbehaved — and disable it again at the first sign of trouble.
3. If **nothing** above fixed the disconnects, the issue is likely hardware: a failing USB port (try all ports), a dying device, or motherboard-level USB controller problems. Check **Event Viewer > Windows Logs > System** for repeated USB error entries as evidence.
4. For persistent issues on a laptop under warranty, the Event Viewer log plus your troubleshooting notes make a strong support case.

## Closing

USB selective suspend is a classic "feature" that causes more problems than the power it saves. Two toggles — the Power Options setting and the per-device Device Manager setting — resolve the large majority of mystery USB disconnects. Turn them both off, update the chipset drivers, and your peripherals should stay connected like they're supposed to.

*Related reading: [USB-C charging not working](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2/), [USB-C PD charger slow](/articles/how-to-fix-usb-c-pd-charger-charging-slowly-on-windows-11/)*
