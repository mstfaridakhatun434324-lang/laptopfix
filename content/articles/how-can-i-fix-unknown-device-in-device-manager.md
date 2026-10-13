---
title: "How Can I Fix an Unknown Device in Device Manager?"
slug: how-can-i-fix-unknown-device-in-device-manager
date: 2026-10-06
categories: ["drivers"]
tags: ["unknown device", "device manager", "hardware id", "code 28", "missing driver"]
description: "Unknown device in Device Manager? Identify it by hardware ID, find the right driver, and clear the yellow warning for good."
thumbnail: "/images/thumbs/how-can-i-fix-unknown-device-in-device-manager.webp"
faqs:
  - q: "What does Unknown device mean in Device Manager?"
    a: "It means Windows detected hardware but has no driver identifying what it is, so it can't classify or operate the device. The device shows under Other devices with a yellow warning. The hardware is usually fine — Windows just needs the correct driver. The hardware ID in the device's properties tells you exactly what the device is."
  - q: "How do I find what an unknown device actually is?"
    a: "Open the device's Properties, go to the Details tab, select Hardware Ids, and copy the top value. The VEN portion identifies the manufacturer and DEV identifies the device. Searching that string online reveals the exact hardware, letting you download the precise driver instead of guessing."
  - q: "Can I just leave an unknown device alone?"
    a: "Sometimes. If everything you use works fine, the unknown device may be a sensor, management engine component, or other background hardware you don't interact with. But unknown devices can also be your card reader, fingerprint sensor, or power management hardware — worth identifying. At minimum, identify it so you know what you're ignoring."
  - q: "Why does the unknown device keep coming back after I uninstall it?"
    a: "Because uninstalling the device entry doesn't install a driver — Windows redetects the hardware on every boot and, finding no driver, lists it as unknown again. The cycle only ends when you install the correct driver. Alternatively, if the device is something you'll never use, you can disable it instead of uninstalling."
---

"Unknown device" with its yellow warning triangle is Device Manager's way of saying: I can see hardware here, but I have no idea what it is. It's rarely an emergency — but it's never nothing, either. That mystery hardware might be your card reader, a sensor, or a power management component that's silently degrading your laptop's behavior.

The fix is detective work, not guesswork. Every unknown device carries a hardware ID that names it precisely. This guide walks you from identification to driver installation to the stubborn cases that resist automatic methods.

## Why this happens

- **Missing vendor driver:** Clean installs and updates leave hardware driverless when the manufacturer's package isn't installed.
- **Chipset driver absent:** Without the chipset package, Windows can't classify whole categories of platform devices (SMBus, GPIO, serial IO).
- **Corrupted driver installation:** A failed install leaves the device detected but unidentifiable — Code 28 with no driver to bind.
- **BIOS not exposing the device properly:** Firmware quirks can present hardware with incomplete identification data.
- **Ghost entries:** Stale hidden entries for removed hardware linger as unknowns.
- **New hardware on old Windows:** Hardware newer than the OS build may have no inbox driver and no recognizable ID strings.
- **Wrong driver installed:** A mismatched driver can leave the device half-identified — present but "unknown."
- **Hardware fault:** Rarely, a failing device returns garbage identification data, presenting as permanently unknown.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the device's story in Properties

1. In Device Manager, expand **Other devices** and right-click the **Unknown device** → **Properties**.
2. Check the **Device status** box: **Code 28** (drivers not installed) is the common one; **Code 1** (not configured correctly) suggests a deeper problem.
3. Go to the **Details** tab → **Hardware Ids** and copy the top value, e.g., `ACPI\VEN_INT&DEV_3400` or `PCI\VEN_8086&DEV_A123`.
4. Also check the **Location** information — "on PCI bus" vs. "on Intel Serial IO" hints at the device family.
5. This evidence-gathering takes a minute and prevents every wrong guess that follows. The [missing drivers guide](/articles/best-way-to-find-missing-drivers-on-windows-11/) uses the same identification workflow as its foundation.

### Fix 2: Decode the hardware ID

1. Break the ID into **VEN** (vendor) and **DEV** (device) portions.
2. Common vendors: **8086** = Intel, **10DE** = NVIDIA, **1022** = AMD, **10EC** = Realtek, **14E4** = Broadcom, **8087** = Intel (USB/Bluetooth).
3. Search the full ID string online — device databases (like pcilookup-style sites) return the exact device name, e.g., "Intel(R) Serial IO I2C Host Controller."
4. **ACPI\** IDs indicate platform devices (sensors, buttons, thermal) that need the laptop maker's driver package.
5. **USB\VID_** IDs are USB devices — VID is the vendor equivalent. With the true name known, you can target the exact driver instead of guessing.

### Fix 3: Install the chipset driver first

1. Go to your laptop maker's support page ([Dell](https://www.dell.com/support) or [HP](https://support.hp.com/us-en)) and download the **chipset driver** for your exact model.
2. Install it and restart.
3. Recheck Device Manager — chipset installation resolves the majority of ACPI\ and PCI\ unknowns in one step, because these are platform devices Windows can't classify without chipset support.
4. If multiple unknowns clear at once, they were all chipset-family devices — a very common pattern after clean installs.
5. Only pursue individual drivers for whatever remains unknown after the chipset package.

### Fix 4: Match the remaining unknowns to maker drivers

1. For each remaining unknown, use its decoded identity to find the right category on the maker's driver page (Serial IO, Management Engine, Card Reader, Sensors, etc.).
2. Download and install each package, restarting when prompted.
3. Verify each device clears from **Other devices** into its proper category with no warning.
4. If the maker's page lacks a specific driver, try the component vendor: [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel platform devices.
5. Work through unknowns one at a time, verifying each — bulk-installing everything at once makes it impossible to tell which package fixed which device.

### Fix 5: Use Windows Update optional updates

1. Open **Settings → Windows Update → Advanced options → Optional updates → Driver updates**.
2. Look for entries matching your unknown hardware and install them.
3. Restart and recheck Device Manager.
4. Microsoft's driver catalog covers many common sensors and controllers that laptop makers don't package separately.
5. If optional updates offer nothing for your device, the hardware likely needs the maker's package — return to Fix 4 rather than waiting on Microsoft.

### Fix 6: Clear ghosts and force clean redetection

1. In Device Manager, enable **View → Show hidden devices**.
2. Uninstall any greyed-out ghosts related to the unknown hardware.
3. Right-click the unknown device → **Uninstall device**, then **Action → Scan for hardware changes**.
4. If Windows now identifies it (even partially), the ghost was blocking proper detection.
5. For persistent unknowns, try **Update driver → Browse my computer → Let me pick** and manually select a compatible driver from the list Windows offers — occasionally the right driver is present but not auto-matched. The [hidden devices guide](/articles/best-way-to-enable-hidden-devices-in-device-manager/) covers the deep-clean method for stubborn ghosts.

### Fix 7: Disable the device if it's unused hardware

1. If you've identified the device as something you'll never use (an unused sensor, a WWAN card with no SIM, an old dock component), right-click → **Disable device** instead of fighting for a driver.
2. Disabling stops Windows from redetecting it as unknown on every boot and silences the warning.
3. Only disable what you've positively identified — never disable unknown system devices blindly.
4. You can re-enable anytime if you later need the hardware.
5. This is a legitimate resolution, not a cop-out: not every background sensor needs a driver on every machine.

### Fix 8: Investigate hardware failure for unidentifiable devices

1. If a device remains unknown after chipset drivers, maker drivers, optional updates, and manual matching, check the BIOS for related toggles.
2. Boot a Linux live USB and run `lspci`/`lsusb` — if Linux also can't identify the device, the hardware may be failing to report its identity correctly.
3. Check whether the unknown appeared after a drop, spill, or repair — physical damage to a sensor or controller produces exactly this symptom.
4. Run the maker's built-in hardware diagnostics (F12/Esc/F2 at boot) for a component-level verdict.
5. A device that's unknown in Windows, Linux, and diagnostics alike has likely failed at the hardware level — at which point [finding all missing drivers](/articles/best-way-to-find-missing-drivers-on-windows-11/) won't help, and it's a repair-shop question.

## Closing

Unknown devices are puzzles with a guaranteed solution path: the hardware ID names the device, the chipset driver clears the platform family, and the maker's packages handle the rest. Resist the urge to uninstall repeatedly — without a driver, redetection just recreates the unknown. Identify, install, verify, and the yellow triangles disappear one by one.
