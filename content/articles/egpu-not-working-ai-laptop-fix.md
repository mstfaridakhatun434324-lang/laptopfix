---
title: "How to Fix an eGPU Not Working on Your AI Laptop"
slug: egpu-not-working-ai-laptop-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["egpu", "external gpu", "thunderbolt", "usb4", "gaming", "troubleshooting"]
description: "Fix an eGPU not working on your AI laptop with steps for Thunderbolt detection, GPU drivers, BIOS settings, power supply, and enclosure compatibility."
thumbnail: "/images/thumbs/egpu-not-working-ai-laptop-fix.webp"
faqs:
  - q: "Do AI laptops with Snapdragon processors support eGPUs?"
    a: >
      Most Snapdragon X laptops do not support eGPUs well, because their USB4 ports lack the PCIe tunneling and driver support that eGPU enclosures need. Intel Lunar Lake and AMD Ryzen AI laptops with Thunderbolt or full USB4 PCIe tunneling are far better eGPU candidates.
  - q: "Why does my eGPU enclosure power on but Windows ignores it?"
    a: >
      Power and data are separate. An enclosure can spin its fans from wall power while the Thunderbolt or USB4 link fails to negotiate, which means Windows never sees a GPU. Check the cable, the port, and the Thunderbolt driver first.
  - q: "Can a laptop BIOS block an eGPU?"
    a: >
      Yes. Some laptop BIOS versions disable external PCIe tunneling, or a security setting blocks new Thunderbolt devices. Both settings live in the BIOS and can silently prevent the enclosure from enumerating.
  - q: "Do I need a separate GPU driver for the eGPU?"
    a: >
      Yes. The eGPU needs the desktop GPU vendor driver for its card — NVIDIA or AMD — installed in Windows, separate from the laptop's internal graphics driver. Without it, Device Manager may show the card with an error or as a generic device.
---

Your eGPU enclosure powers on, its fans spin, but Windows shows no external GPU — or the GPU appears with an error and games still run on internal graphics. External GPUs on AI laptops are the hardest accessory to get working because they stack three fragile layers: the Thunderbolt or USB4 link, the PCIe tunnel inside that link, and the desktop GPU driver.

Snapdragon laptops are a special case: many simply lack the PCIe tunneling eGPUs require, and no driver update can add it. Intel and AMD AI laptops fare better, but still need the right port, BIOS setting, and driver combination.

This guide walks through that stack in order, and starts with the compatibility check that saves wasted hours on machines that cannot support an eGPU at all.

## Why this happens

- **Platform lacks PCIe tunneling:** Many Snapdragon X laptops expose USB4 without full PCIe tunneling, which eGPU enclosures require. The enclosure powers on but can never present a GPU to Windows.
- **Wrong port or non-Thunderbolt cable:** The enclosure must connect to a Thunderbolt or full USB4 port with a rated cable. A plain USB-C port or charging cable cannot carry PCIe traffic.
- **Thunderbolt security blocking the enclosure:** Approval or security modes can block the enclosure's PCIe device until it is explicitly authorized in the Thunderbolt software or BIOS.
- **Missing desktop GPU driver:** Windows may detect the enclosure but not the card inside it without the NVIDIA or AMD desktop driver for that exact GPU.
- **Enclosure power supply insufficient:** A weak or failing enclosure PSU can power fans and lights but brown out when the GPU initializes, causing enumeration to fail.
- **BIOS or firmware disabling external PCIe:** Some BIOS versions ship with external GPU or PCIe tunneling support off, or a BIOS update changes the default.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your laptop can actually support an eGPU

This check comes first because it determines whether the rest of the guide can help at all.

1. Check your laptop's specifications for Thunderbolt 4 or 5, or USB4 with PCIe tunneling explicitly listed.
2. If you have a Snapdragon X laptop, search your maker's support pages for eGPU support statements — most models officially do not support eGPUs.
3. Confirm the enclosure maker lists your laptop platform as compatible; enclosure compatibility lists are usually honest about Snapdragon gaps.
4. If your platform lacks PCIe tunneling, no cable or driver will fix it — your options are a different laptop or cloud gaming instead.
5. If your platform does support eGPUs, continue — the remaining fixes apply to Intel and AMD AI laptops. Port capability questions like this also sit behind [Thunderbolt 5 failures](/articles/thunderbolt-5-lunar-lake-not-working-fix/) on Lunar Lake machines.

### Fix 2: Connect with a rated cable to the right port

The physical link carries PCIe traffic, so cable and port quality matter more here than with any other accessory. High-bandwidth connections can be equally finicky on these machines, so if your laptop also drops its wireless connection, see [Wi-Fi 7 not connecting on AI laptops](/articles/wifi-7-not-connecting-ai-laptop-fix/).

1. Use a Thunderbolt-rated cable, preferably the short cable supplied with the enclosure — long passive cables degrade the PCIe signal.
2. Connect to the port marked with the Thunderbolt symbol, not just any USB-C port.
3. Connect the enclosure's power cable and confirm its PSU switch is on before plugging in the data cable.
4. Wait up to a minute — eGPU enumeration includes PCIe training, which is slower than a USB device appearing.
5. Check Device Manager for a new display adapter or PCI device. If nothing appears, the link itself failed — continue to the driver and BIOS steps.

### Fix 3: Approve the device and repair the Thunderbolt driver

Security modes and stale drivers are the most common fixable blockers once the hardware path is right.

1. Open the Thunderbolt Control Center or **Settings > Bluetooth & devices > USB** and approve the enclosure if it appears as an unapproved device.
2. In Device Manager, check **System devices** for Thunderbolt controller warnings and **Display adapters** for the external card.
3. Reinstall the chipset and Thunderbolt drivers from your laptop maker's support page.
4. Restart, reconnect the enclosure, and approve it again if prompted.
5. If the enclosure appears in Device Manager but the GPU shows an error, move to the GPU driver fix next.

### Fix 4: Install the desktop GPU driver for the external card

The enclosure is only a shell — Windows needs the desktop driver for the card inside it, which is different from your laptop's internal graphics driver.

1. Identify the exact card in the enclosure, for example an NVIDIA RTX 4060 or AMD RX 7600.
2. Download the desktop driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) — not the laptop driver package.
3. Install with the enclosure connected and powered on so the installer detects the card.
4. Restart and check Device Manager — the card should now appear by name without a warning.
5. Open the GPU vendor control panel and confirm the external card is listed; if games still use internal graphics, set the game to high-performance graphics in **Settings > System > Display > Graphics**.

### Fix 5: Check the enclosure power supply and reseat the card

A PSU that cannot sustain the card's peak draw causes exactly this symptom: lights and fans work, but the GPU fails to initialize under load.

1. Confirm the enclosure PSU wattage meets the card maker's recommendation plus enclosure overhead.
2. Power the enclosure off, unplug it, and reseat the graphics card firmly in its PCIe slot.
3. Check that all PCIe power connectors on the card are fully seated — a loose 8-pin connector is a classic cause.
4. Try a different wall outlet and, if the enclosure has a PSU switch, cycle it off and on.
5. Reconnect and test. If the card enumerates only when the enclosure is cold and fails after warming up, the PSU is the likely fault and needs replacement.

### Fix 6: Update the BIOS and test with a cold boot

BIOS settings and stale controller state are the last software layers. A cold boot after a BIOS check clears both.

1. Enter the BIOS and confirm Thunderbolt support, external PCIe, or USB4 PCIe tunneling is enabled.
2. Check for a BIOS update from your maker that mentions Thunderbolt or external GPU fixes.
3. Install any BIOS update on AC power, load defaults once, and re-check the Thunderbolt setting.
4. Shut down fully with **Shift + Shut down**, unplug the charger for thirty seconds, then boot and connect the enclosure.
5. If the eGPU still does not enumerate after all of this on a platform that officially supports eGPUs, contact the enclosure maker with your laptop model, BIOS version, and card model. Related detection problems affect [USB4 devices generally](/articles/usb4-device-not-recognized-ai-laptop-fix/), so the same isolation evidence helps support diagnose faster.

## Closing

An eGPU that powers on but never appears in Windows is usually failing at the link, the security handshake, or the driver — not at the card itself. Confirm platform support first, then work the cable, approval, driver, and power layers in order. On supported Intel and AMD AI laptops, that sequence resolves nearly every dead-enclosure case; on unsupported Snapdragon machines, the honest answer is that the platform cannot carry an eGPU. If this fix did not fully resolve the issue, related troubleshooting for [Balders Gate 3 Arm Laptop Issues](/articles/balders-gate-3-arm-laptop-issues-fix/) and [Copilot File Search Not Working](/articles/copilot-file-search-not-working/) covers neighboring causes that can produce the same symptom on AI laptops. See also [Wifi 7 Not Connecting Ai Laptop](/articles/wifi-7-not-connecting-ai-laptop-fix/) for the other half of this connection chain.
