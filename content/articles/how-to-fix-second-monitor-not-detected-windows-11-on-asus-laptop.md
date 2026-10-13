---
title: "Second Monitor Not Detected on an ASUS Laptop in Windows 11"
slug: "how-to-fix-second-monitor-not-detected-windows-11-on-asus-laptop"
date: "2026-09-02"
categories: ["drivers"]
tags: ["second monitor not detected", "asus laptop", "windows 11", "vivobook", "rog"]
description: "Second monitor not detected on your ASUS VivoBook, ZenBook, or ROG in Windows 11? Fix ASUS-specific causes from MyASUS drivers to Armoury Crate display settings."
thumbnail: "/images/thumbs/how-to-fix-second-monitor-not-detected-windows-11-on-asus-laptop.webp"
faqs:
  - q: "Why won't my ASUS laptop detect a second monitor?"
    a: "Common ASUS-specific causes include MyASUS or Windows Update installing a mismatched graphics driver, Armoury Crate display or GPU-mode settings overriding Windows on ROG/TUF models, and USB-C DisplayPort alternate-mode being disabled. Standard causes — cable quality, projection mode, and stale display topology — apply on ASUS exactly as on other brands."
  - q: "Can Armoury Crate block external monitor detection?"
    a: "Yes, on ROG and TUF models. Armoury Crate's GPU modes (Eco, Standard, Ultimate) change which GPU drives the display outputs, and Eco mode in particular can disable the discrete GPU's ports. Switching to Standard or Ultimate mode and updating Armoury Crate itself resolves many ROG detection failures."
  - q: "Does MyASUS help with monitor detection problems?"
    a: "MyASUS helps on the driver side: its System Update installs ASUS-validated graphics drivers matched to your model, which handle ASUS's display routing better than generic Windows drivers. It does not manage display topology directly, so combine it with the Windows detection steps in this guide."
  - q: "Why does USB-C video work on some ASUS ports but not others?"
    a: "On many ASUS models only specific USB-C ports support DisplayPort alternate mode — the others are data-only. Check your model's specifications or the port markings (a DisplayPort or Thunderbolt icon indicates video support). Using a data-only port for video is a common and easily fixed mistake."
---

ASUS's VivoBook, ZenBook, ExpertBook, TUF, and ROG laptops span simple integrated-graphics ultrabooks and complex MUX-equipped gaming machines — and second-monitor detection fails differently across that range. On mainstream ASUS models the usual suspects (driver, cable, projection mode) dominate; on ROG/TUF gaming laptops, Armoury Crate's GPU modes join them as a first-class cause.

This guide covers both: the universal detection steps, then the ASUS layer — MyASUS validated drivers, Armoury Crate GPU modes, USB-C port capabilities, and BIOS display settings. Check **Settings > System > Display** after each fix.

## Why this happens

- **Mismatched graphics driver**: Windows Update or MyASUS installs a driver build that mishandles ASUS's display routing.
- **Armoury Crate GPU mode (ROG/TUF)**: Eco mode disables the discrete GPU and its wired display outputs; Ultimate/Standard modes change routing.
- **Wrong USB-C port**: many ASUS models have only one USB-C port with DisplayPort alternate mode; the others are data-only.
- **Stale display topology**: cached multi-monitor arrangement conflicts with the actual connection after updates.
- **USB-C/Thunderbolt firmware**: outdated controller firmware fails display negotiation with docks and monitors.
- **Projection mode flipped**: updates reset Windows to PC-screen-only, deactivating external output.
- **BIOS display settings**: some models gate external display initialization in firmware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the correct port and cycle projection modes

Two instant checks: the right physical port, and Windows' projection state. Together they resolve a large fraction of ASUS detection failures.

1. Identify which ports support video: look for DisplayPort/Thunderbolt icons next to USB-C ports, or check your model's spec sheet — use only video-capable ports.
2. Connect the monitor to the HDMI port first for baseline testing; HDMI is the most universally wired output.
3. Press **Windows key + P** and choose **Extend**.
4. In **Settings > System > Display**, click **Detect**.
5. If the monitor appears on HDMI but not USB-C, the USB-C port may be data-only or need alternate-mode enabled — note which path works, as in [our external-monitor chain guide](/articles/how-to-fix-external-monitor-not-detected-after-windows-11-update/).

### Fix 2: Set the correct Armoury Crate GPU mode (ROG/TUF)

On ROG and TUF laptops, Armoury Crate's GPU mode directly controls which GPU — and therefore which ports — are active. This is the ROG-specific step generic guides miss.

1. Open **Armoury Crate** and find the **GPU Mode** setting (iGPU Mode toggle or Eco/Standard/Ultimate selector).
2. Switch away from **Eco mode** — it powers down the discrete GPU and its display outputs.
3. Try **Standard** first, then **Ultimate** if detection still fails; each mode reboots the display routing.
4. Update Armoury Crate itself to the latest version before judging — old Crate builds have display-routing bugs.
5. After changing modes and restarting, retest in **Settings > System > Display**; mode-caused failures resolve immediately, similar to the MUX fixes in [our Lenovo monitor guide](/articles/how-to-fix-second-monitor-not-detected-windows-11-on-lenovo-laptop/).

### Fix 3: Update graphics drivers through MyASUS

MyASUS delivers ASUS-validated graphics drivers matched to your model's display architecture — better than Windows Update generics for ASUS routing quirks.

1. Open **MyASUS**, run **System Update**, and install all recommended graphics and chipset updates.
2. Restart with a full shutdown after installation.
3. Retest monitor detection on your video-capable port.
4. If MyASUS offers nothing, download the graphics driver manually from the manufacturer's support page for your exact model.
5. For Intel integrated graphics, [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) confirms the correct package before you install.

### Fix 4: Isolate the cable and monitor

Prove the physical chain before deeper driver work. ASUS HDMI ports are generally robust, but cable quality still matters — especially at high refresh rates.

1. Test the monitor with another source to confirm the panel and input selection.
2. Test your ASUS on a different display or TV.
3. Swap in a certified cable appropriate to your resolution and refresh rate.
4. Try both HDMI and video-capable USB-C to determine whether one output path works.
5. If the chain is proven good, the fault is software — proceed with confidence.

### Fix 5: Clean-install the graphics driver

When validated-driver updates do not fix it, wipe the graphics driver state completely and reinstall. Update leftovers are a persistent cause of detection failures.

1. Download the correct graphics driver for your exact ASUS model.
2. Disconnect from the internet, uninstall the current graphics driver in Device Manager (ticking driver removal), and restart.
3. Install the downloaded driver with the clean-installation option.
4. Full shutdown, cold boot, reconnect the monitor to the video-capable port.
5. Set **Device Installation Settings** to **No** to stop Windows Update replacing the working driver.

### Fix 6: Clear stale monitor entries and check refresh rates

Stale monitor cache entries and impossible refresh-rate settings both block detection. Clean both.

1. In Device Manager (**View > Show hidden devices**), uninstall grayed-out entries under **Monitors**.
2. Click **Action > Scan for hardware changes**, then **Detect** in Display settings.
3. If the monitor appears, open **Advanced display settings** and set a conservative refresh rate (60Hz) for testing.
4. Gradually raise the refresh rate to find the maximum your cable sustains.
5. Rearrange the display layout and restart to confirm the topology persists — the cleanup technique from [our hidden-devices guide](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/).

### Fix 7: Check BIOS settings and firmware

The final layer: firmware gating of display outputs and controller firmware for USB-C/Thunderbolt paths.

1. Enter the BIOS (**F2** or **Del** during the ASUS logo) and look for graphics/display output options.
2. Ensure no integrated-only graphics mode is disabling discrete-wired ports on gaming models.
3. Load optimized defaults, save, and exit.
4. Check for USB-C/Thunderbolt controller firmware updates for your model and install them.
5. If no output path works across all software states but monitors are proven good, check [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for known issues, then consider professional diagnosis — or use a working alternate port as the everyday connection.

## Closing

ASUS second-monitor detection spans two machines in one brand: mainstream models where driver, cable, and projection mode explain nearly everything, and ROG/TUF gaming laptops where Armoury Crate's GPU mode is a first-class suspect. Check the port capability and the Crate mode early — those two ASUS-specific steps resolve cases that stump generic troubleshooting. Then it is the standard chain: validated driver, clean install, cable isolation, and firmware. Change one variable at a time, and the missing display always turns out to have a specific, findable reason.
