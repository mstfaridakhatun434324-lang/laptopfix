---
title: "How to Install Drivers Without Internet on a Windows Laptop"
slug: how-can-i-install-drivers-without-internet
date: 2026-09-29
categories: ["drivers"]
tags: ["offline drivers", "driver installation", "no internet", "usb drivers", "driver backup"]
description: "No internet on your laptop — maybe because the network driver itself is missing? How to get drivers onto an offline machine using another computer and a USB drive."
thumbnail: "/images/thumbs/how-can-i-install-drivers-without-internet.webp"
faqs:
  - q: "How do I get drivers if my laptop has no internet at all?"
    a: "Use a second device with internet access — a phone, another computer, or a library PC. Download the driver packages from the manufacturer's official support site, copy them to a USB flash drive, then run the installers on the offline laptop. Start with the network driver: once networking works, Windows Update can fetch the rest."
  - q: "Can I download drivers on my phone and transfer them?"
    a: "Yes. Download the driver installer (usually an .exe or .zip) on your phone, connect the phone to the laptop via USB, and copy the file over in file-transfer mode. Alternatively, save it to a microSD card if both devices accept one. The file doesn't care which device downloaded it — only that it reaches the laptop intact."
  - q: "What if I don't know which drivers I need?"
    a: "Open Device Manager on the offline laptop and note every device with a yellow warning icon, plus the exact model under Network adapters and Display adapters. On the manufacturer's support site, entering your laptop's serial number or Service Tag lists exactly the drivers your specific build needs — no guessing required."
  - q: "Should I use third-party offline driver packs?"
    a: "Avoid them. Offline driver packs from aggregator sites bundle outdated, mismatched, or modified drivers and occasionally malware. The safe path is slower but reliable: manufacturer packages transferred via USB. If you must prepare in advance, download the full driver set for your model while you have internet and archive it."
---

The cruelest driver problem is the circular one: your network driver is missing or broken, so you have no internet — and without internet, you can't download the network driver. Add to that the fresh Windows install with no drivers at all, or the laptop in a location with no connectivity, and you need an offline driver strategy.

The solution is a bridge: a second internet-capable device, a USB drive, and the manufacturer's official packages. This guide covers the full offline workflow — identifying what you need, getting it onto the machine, installing in the right order, and preparing an offline driver kit so this never strands you again. If your network adapter is missing rather than merely driverless, our [adapter troubleshooting guide](/articles/what-to-do-if-wifi-adapter-not-showing-up/) helps distinguish the two.

## Why this happens

- **Fresh Windows installs include minimal drivers.** A clean install often lacks network, chipset, and specialty drivers.
- **The network driver is the one that's broken.** The classic catch-22: you need the internet to fix the thing that gives you internet.
- **Windows Update can't reach the machine.** No connectivity means no automatic driver delivery at all.
- **Driver backups were never made.** Most people only think about offline drivers when they already need them.
- **Corporate or remote environments lack connectivity.** New machines provisioned offline need drivers before first network contact.
- **The wrong driver was installed.** A mismatched network driver can break connectivity that previously worked.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Inventory what's missing on the offline laptop

You can't fetch the right drivers until you know exactly what's absent.

1. On the offline laptop, open **Device Manager** (Win + X).
2. Expand each section and note every device with a yellow warning icon — these need drivers.
3. Record the exact names under **Network adapters** and **Display adapters**, even if they show as "Unknown device" — right-click > **Properties > Details > Hardware Ids** and copy the VEN/DEV codes.
4. Write down your laptop's exact model and serial number (sticker on the bottom or `msinfo32`).

The Hardware Ids are your Rosetta Stone: `VEN_8086&DEV_2725` identifies an Intel AX201 wireless card regardless of what Windows calls it. Photograph the Device Manager screen with your phone — it's faster than transcribing and you can reference it on the other device.

### Fix 2: Download the network driver first on another device

The network driver is the keystone: once networking works, everything else can be fetched directly on the laptop.

1. On an internet-capable device, go to your laptop manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en) — and enter your serial number.
2. Download the **network** driver package first: wireless (Wi-Fi) and wired (Ethernet), for your Windows version.
3. Copy the installer files to a USB flash drive (or transfer via phone USB as described in the FAQ).
4. If the manufacturer site is hard to navigate, the component vendor's site works too — e.g., [Intel's driver downloads](https://www.intel.com/content/www/us/en/support/detect.html) for Intel wireless cards.

Prioritize ruthlessly: one working network driver changes the situation from "offline emergency" to "routine driver installation." Everything else can wait until the laptop is online.

### Fix 3: Install the network driver on the offline laptop

With the package on USB, installation is straightforward.

1. Plug the USB drive into the offline laptop and copy the installer to the Desktop (running from USB works too, but local is more reliable).
2. Right-click the installer and choose **Run as administrator**.
3. Follow the installer prompts and restart when asked — network driver installs almost always need a reboot.
4. After rebooting, verify connectivity: the Wi-Fi icon should appear, or Ethernet should link.

If the installer fails, try the manual method: in Device Manager, right-click the network device > **Update driver > Browse my computer for drivers** and point it at the extracted driver folder. Some packages are driver-only (INF files) with no installer — the manual method handles those.

### Fix 4: Let Windows Update finish the job

Once the laptop is online, Windows becomes your driver-fetching assistant.

1. Connect to the internet and open **Settings > Windows Update**.
2. Click **Check for updates** and install everything offered, including **Optional updates > Driver updates**.
3. Restart as prompted — several rounds of update-and-reboot may be needed.
4. Re-check Device Manager: the yellow warnings should be gone or greatly reduced.

Windows Update's driver catalog is surprisingly complete for common hardware. It won't have every specialty driver (fingerprint readers, vendor utilities), but it resolves the bulk of the Device Manager warnings automatically. For any remaining gaps, our [missing drivers guide](/articles/how-to-find-missing-drivers-on-windows-11/) covers identification techniques.

### Fix 5: Fetch remaining specialty drivers manually

Vendor-specific hardware often needs the manufacturer's package even after Windows Update.

1. Revisit the manufacturer's support site (now from the laptop itself) and download drivers for any remaining yellow-flagged devices.
2. Install in this order: **chipset**, then **graphics**, then **audio/network leftovers**, then **specialty** (fingerprint, card reader, hotkeys).
3. Restart after the chipset and graphics drivers; the rest can usually batch.
4. Verify each in Device Manager as you go — don't batch-install blindly and hope.

The chipset-first ordering matters: chipset drivers define how Windows talks to the motherboard's controllers, and other drivers build on that foundation. Installing graphics before chipset occasionally produces the exact kind of instability you're trying to eliminate.

### Fix 6: Use manufacturer offline tools when available

Some vendors ship tools designed for exactly this scenario.

1. Dell's **SupportAssist OS Recovery** and similar tools can fetch drivers from a USB-prepared image.
2. Lenovo's **System Update** can be pointed at a local repository you've prepared on USB.
3. Intel's driver packages can be downloaded as full offline installers rather than web stub installers — choose the full package when downloading from another device.
4. For enterprise fleets, the manufacturer's **driver pack CAB files** (Dell Command, Lenovo SCCM packs) contain every driver for a model in one download.

The full offline installer versus web stub distinction is worth remembering: stub installers download components during installation and fail offline. When bridging via USB, always grab the full package — it's larger, but it's self-contained.

### Fix 7: Build an offline driver kit for next time

Never be stranded again: prepare the kit while you have internet.

1. Download the complete driver set for your exact model from the manufacturer's support site — chipset, graphics, network (wired and wireless), audio, and specialty drivers.
2. Store them on a dedicated USB drive labeled with the model and date, in clearly named folders.
3. Include a text file listing the install order (chipset → graphics → network → audio → rest).
4. Refresh the kit annually or after major Windows upgrades; drivers go stale.

Keep the kit with the laptop's documentation. The fifteen minutes this takes today saves the multi-hour scramble of the next offline emergency — and if you ever do a clean Windows install, you'll thank yourself immediately.

## Closing

Offline driver installation is a logistics problem, not a technical one: identify what's missing, bridge the packages via USB from any internet-capable device, install the network driver first, and let Windows Update finish the job. The catch-22 dissolves the moment you stop trying to download drivers on the machine that can't reach the internet. Build the offline kit afterward, and the next time this happens — to you or someone you're helping — it's a fifteen-minute task.
