---
title: "How to Fix HDMI Not Working on Laptop — Step by Step"
slug: how-to-fix-hdmi-not-working-on-laptop-step-by-step
date: 2026-10-04
categories: ["drivers"]
tags: ["hdmi not working", "laptop hdmi", "external monitor", "display driver", "hdmi no signal"]
description: "HDMI not working on your laptop? Follow this step-by-step guide to fix no-signal, undetected displays, and HDMI driver problems."
thumbnail: "/images/thumbs/how-to-fix-hdmi-not-working-on-laptop-step-by-step.webp"
faqs:
  - q: "Why is my laptop not detecting the HDMI display?"
    a: "The most common reasons are a display driver that isn't initializing the HDMI port, the laptop defaulting to internal-display-only projection mode, a faulty cable, or the TV/monitor being on the wrong input. Start with the cable and input checks — they take a minute — then move to Windows display settings and the graphics driver reinstall below."
  - q: "Should I update my graphics driver to fix HDMI?"
    a: "Yes, if the cable and settings check out. HDMI port initialization is handled by the GPU driver, and a corrupt or outdated Intel, AMD, or NVIDIA driver is the top software cause of dead HDMI output. Use a clean install of the current driver from Intel, AMD, or NVIDIA — or your laptop maker's validated package — rather than layering over the old one."
  - q: "Why does HDMI work on one laptop but not another?"
    a: "That pattern almost always means the non-working laptop's driver or port configuration is at fault, not the cable or display — assuming you used the same cable and input. Different laptops also wire HDMI differently: some route it through the discrete GPU, some through the integrated GPU, and USB-C-to-HDMI adapters add another variable. Test with a direct HDMI-to-HDMI cable to isolate the laptop."
  - q: "Can a Windows update break HDMI output?"
    a: "Yes. Windows feature updates sometimes replace the manufacturer's graphics driver with a generic Microsoft one that doesn't initialize the HDMI port, or reset the display configuration. If HDMI died right after an update, roll back the display driver in Device Manager or clean-install the manufacturer's driver — that resolves update-triggered HDMI failures in most cases."
---

HDMI failures on laptops come in three flavors: the external display shows "no signal," Windows doesn't detect the display at all, or the display is detected but stays black. All three share the same short list of causes — cable, input, projection mode, and the graphics driver — which is why a strict step-by-step order works so well here. Do the physical checks first; they resolve a surprising share of cases in under five minutes.

This guide assumes a standard HDMI-to-HDMI connection. If you're using a USB-C adapter or dock, the adapter adds its own failure modes — check its driver and firmware too.

## Why this happens

- **Faulty or loose HDMI cable.** The single most common cause — cables fail silently.
- **Wrong input selected on the display.** The TV/monitor is listening on HDMI 2 while you're plugged into HDMI 1.
- **Projection mode set to PC screen only.** Windows isn't sending anything to the external output.
- **Corrupt graphics driver.** The GPU driver failing to initialize the HDMI port.
- **Display detected but disabled.** Windows sees the monitor but has it turned off in display settings.
- **HDMI port power/EDID handshake failure.** The display's identification data not reaching the laptop.
- **Damaged HDMI port.** Bent pins or a loose solder joint — the hardware end of the list.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the cable and the display input

The two-minute physical check that resolves the plurality of HDMI failures.

1. Unplug the HDMI cable at both ends and firmly reseat it — loose connections are the top cause.
2. Try a **different HDMI cable** — preferably a short, known-good one. Long and cheap cables fail the most.
3. On the TV/monitor, cycle through the **inputs** (HDMI 1, HDMI 2, HDMI 3) — make sure you're on the input matching the physical port.
4. If the display has multiple HDMI ports, try a different port on the display itself.
5. Test the same cable and display with a different laptop or device — if it works there, your laptop is the problem; if not, replace the cable.

### Fix 2: Set the correct projection mode

Windows may simply not be sending video to the external display.

1. Press **Windows + P** to open the projection menu.
2. Choose **Duplicate** (mirror) or **Extend** — **PC screen only** sends nothing to the HDMI port.
3. If the menu shows only "PC screen only" as an option, Windows doesn't see the display — move to Fix 4.
4. After selecting Extend, open **Settings > System > Display** — the external display should appear as display 2.
5. Click **Detect** under display settings if the monitor doesn't appear automatically.

### Fix 3: Configure the display in Windows settings

When Windows sees the display but shows nothing on it.

1. Open **Settings > System > Display**.
2. Select the external display (click **Identify** to see which number it is).
3. Under **Multiple displays**, make sure it's not set to **Disconnect this display**.
4. Set the **resolution** to the monitor's native resolution — a wrong resolution can produce a black screen on some TVs.
5. Try lowering the **refresh rate** (Display > Advanced display) — some cables can't carry 4K at 60Hz and the handshake fails silently.

### Fix 4: Restart the graphics driver

A stuck GPU driver can drop the HDMI output without affecting the internal screen.

1. Press **Windows + Ctrl + Shift + B** — the screen will blink as Windows restarts the graphics driver. This is safe and takes seconds.
2. Reconnect the HDMI cable after the blink and check for a signal.
3. If that fails, open **Device Manager > Display adapters**, right-click your GPU, choose **Disable device**, wait 10 seconds, then **Enable device**.
4. Test the HDMI output again.
5. If the internal display works but HDMI never does, the driver needs a clean reinstall — Fix 5.

### Fix 5: Clean-install the graphics driver

The core software fix — HDMI port initialization lives in the GPU driver.

1. Identify your GPU: **Device Manager > Display adapters** (Intel, AMD, NVIDIA — or both Intel + NVIDIA on gaming laptops).
2. Download the current driver: Intel via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA from [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx) with **clean install** checked, AMD from [AMD's driver page](https://www.amd.com/en/support/download/drivers.html).
3. Install, restart, then reconnect the HDMI cable.
4. On laptops with both GPUs, update the **Intel** driver first, then the discrete GPU — the HDMI port is usually wired through the integrated GPU's display engine.
5. If HDMI broke right after a Windows update, use **Device Manager > GPU Properties > Driver > Roll Back Driver** first — it's faster than a full reinstall.

Related multi-monitor detection problems have their own walkthrough: [how to fix laptop not detecting second monitor on Windows 11](/articles/how-to-fix-laptop-not-detecting-second-monitor-on-windows-11/).

### Fix 6: Reset the EDID handshake

When the display and laptop fail to agree on capabilities, forcing a fresh handshake helps.

1. Power off the TV/monitor completely (unplug it for 30 seconds — standby isn't enough).
2. With the display unplugged, restart the laptop.
3. Plug the display back into power, turn it on, select the correct HDMI input.
4. Connect the HDMI cable to the laptop last.
5. This order — display fully booted before the laptop probes it — resolves EDID handshake failures that survive normal reboots.

For the specific case where the external monitor isn't detected at all after updates, see [how to fix external monitor not detected after Windows 11 update](/articles/how-to-fix-external-monitor-not-detected-after-windows-11-update/).

### Fix 7: Test the port hardware and adapt

The final verdict on the physical port.

1. Try the HDMI port with a different display and cable — if it fails with everything, the port is suspect.
2. Inspect the laptop's HDMI port with a flashlight — bent pins or debris inside are visible.
3. On laptops with USB-C/Thunderbolt, a **USB-C to HDMI adapter** bypasses a dead HDMI port entirely and often gives a better signal.
4. Check your laptop maker's support site for a **BIOS update** mentioning display or HDMI fixes — port initialization firmware does get patched.
5. If the port is physically damaged, a repair shop can replace it — but a $15 USB-C adapter is the pragmatic fix on most modern laptops. Check Microsoft's official display troubleshooting guidance if you need a second reference.

## Closing

HDMI failures follow a short, predictable chain: cable, input, projection mode, driver, handshake, hardware. Work it in order and you'll find the break quickly — most of the time it's the cable or the driver, and both are cheap fixes. Only after all seven steps fail should you conclude the port itself is damaged.
