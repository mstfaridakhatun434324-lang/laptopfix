---
title: "How to Update Battery Drivers in Windows 11"
slug: how-to-update-battery-drivers-in-windows-11-24h2
date: 2026-09-10
categories: ["battery"]
tags: ["battery drivers", "windows 11", "device manager", "acpi", "drivers"]
description: "Battery misbehaving on Windows 11? Learn how to update, reinstall, and repair battery drivers in Device Manager and from your manufacturer."
thumbnail: "/images/thumbs/how-to-update-battery-drivers-in-windows-11-24h2.webp"
faqs:
  - q: "What are the battery drivers in Windows 11?"
    a: "There are two, both listed under Batteries in Device Manager: Microsoft AC Adapter, which handles the charger connection, and Microsoft ACPI-Compliant Control Method Battery, which lets Windows talk to the battery controller. They translate hardware signals into the percentage, charging status, and health data you see in the taskbar."
  - q: "Will updating battery drivers fix charging problems?"
    a: "Sometimes. If Windows shows the wrong percentage, says 'plugged in, not charging,' or cannot see the battery at all, corrupted or outdated battery drivers are a prime suspect. A clean reinstall takes two minutes and resolves a surprising number of charging complaints."
  - q: "Where do I download battery drivers for my laptop?"
    a: "You rarely need to download them manually. Windows Update and Device Manager handle the generic Microsoft drivers. For deeper fixes, get the chipset and power management drivers from your manufacturer's support site, such as Dell, HP, or Lenovo, since those control the hardware the battery drivers talk to."
  - q: "Is it safe to uninstall the battery drivers?"
    a: "Yes. Uninstalling the two drivers under Batteries in Device Manager is safe because Windows reinstalls them automatically on the next boot. Just do not uninstall anything under System Devices or Firmware unless you know exactly what it is."
---
Battery drivers are the quiet translators between your battery's hardware and Windows 11. When they go stale or corrupt, the symptoms look like hardware failure: wrong percentages, "plugged in, not charging," a battery Windows cannot see, or power features that misbehave. The good news is that fixing them is one of the quickest repairs in all of Windows troubleshooting.

This guide covers every legitimate way to update and repair battery drivers on Windows 11, from the two-minute reinstall to manufacturer driver packs.

## Why this happens

- **Drivers corrupt during updates.** Major Windows updates occasionally leave the battery driver stack in a half-migrated state.
- **The wrong driver gets installed.** Windows Update sometimes substitutes a generic driver that does not fully match the battery controller.
- **Chipset drivers go stale.** Battery drivers sit on top of chipset and ACPI drivers. When those age, battery communication degrades too.
- **Manufacturer utilities conflict.** Power tools from Dell, Lenovo, HP, or ASUS can fight Windows over battery control and destabilize the driver.
- **Firmware and driver mismatch.** A BIOS update can change how the battery controller behaves, leaving the old driver speaking the wrong language.
- **Residual corruption accumulates.** Months of sleep, hibernate, and fast-startup cycles can leave the driver stack in a confused state that only a clean reinstall clears.

## How to fix it

Work through these in order, from the simplest reinstall to full manufacturer driver packs.

### Fix 1: Reinstall the battery drivers in Device Manager

1. Press **Win + X** and select **Device Manager**.
2. Expand the **Batteries** category. You should see **Microsoft AC Adapter** and **Microsoft ACPI-Compliant Control Method Battery**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery**, choose **Uninstall device**, and confirm. If it asks about deleting driver software, leave that unchecked.
4. Do the same for **Microsoft AC Adapter**.
5. Restart the laptop with the charger plugged in. Windows detects the hardware during boot and installs fresh copies of both drivers.
6. Check the battery icon. If the percentage now behaves sanely, the old driver was the problem. This resolves most [battery detection issues](/articles/laptop-battery-not-detected-windows-11/) outright.

### Fix 2: Update the drivers through Device Manager

1. In **Device Manager**, expand **Batteries** again.
2. Right-click each battery device and choose **Update driver > Search automatically for drivers**.
3. Windows checks its driver store and Windows Update. This rarely finds anything new for these generic drivers, but it takes seconds and is worth ruling out.
4. If Windows says the best driver is already installed, move on to Fix 3, which is where the real updates live.

### Fix 3: Install optional driver updates from Windows Update

1. Open **Settings > Windows Update > Advanced options > Optional updates**.
2. Expand **Driver updates** and look for anything from your manufacturer: chipset, ACPI, power management, or battery entries.
3. Check them all and install. These optional updates are the channel through which manufacturers ship fixed power drivers.
4. Restart after installation, even if Windows does not demand it. Driver changes to the power stack apply cleanly only at boot.

### Fix 4: Update the chipset drivers from your manufacturer

1. Battery communication depends on the chipset and ACPI platform drivers, which only the manufacturer updates properly.
2. Go to your manufacturer's support site, for example [Lenovo Support](https://support.lenovo.com/us/en/), enter your model, and download the latest chipset driver package.
3. Intel-based machines should also run the [Intel Driver and Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), which detects outdated chipset and management engine drivers automatically.
4. Install everything it flags, restart, and retest the battery behavior.

### Fix 5: Update or reinstall the manufacturer's power utility

1. Open **Dell Power Manager**, **Lenovo Vantage**, **HP Support Assistant**, **MyASUS**, or your brand's equivalent.
2. Check for updates inside the app itself, then check the support site for a newer version.
3. If battery problems started right after one of these tools updated, uninstall it completely, restart, and test with plain Windows power management.
4. Reinstall the latest version only if you need its features. A surprising number of charging glitches trace back to these utilities rather than the Microsoft drivers.

### Fix 6: Update the BIOS

1. The battery controller's firmware lives in the BIOS, and the Windows drivers must match its behavior.
2. Download the latest BIOS for your exact model from the manufacturer's support site.
3. Flash it with the AC adapter connected and the battery above 30 percent. Never interrupt a BIOS flash.
4. After the update, Windows may reinstall the battery drivers on the next boot on its own. Check Device Manager to confirm both battery devices are present and healthy.

### Fix 7: Disable fast startup to stabilize the driver stack

1. Open **Control Panel > Hardware and Sound > Power Options > Choose what the power button does**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Restart fully. Fast startup saves a hibernated kernel state that can preserve a corrupted driver stack across reboots, defeating your reinstalls.
4. With fast startup off, every boot loads the battery drivers fresh, which keeps small corruptions from accumulating again.

### Fix 8: When nothing helps, check for hardware failure

1. If fresh drivers, current chipset software, and a new BIOS still leave the battery misbehaving, the problem is likely the battery or its connector, not software.
2. Run `powercfg /batteryreport` and check whether full charge capacity has collapsed.
3. Boot into the BIOS and see whether the battery is detected there. A battery invisible in BIOS has a hardware problem no driver can fix.
4. If the machine previously showed [no battery after a Windows update](/articles/how-to-fix-no-battery-detected-after-windows-update-on-windows-10/), and drivers did not help, reseat the battery connector or have a technician inspect it.

## Closing

Battery driver problems are mercifully easy to fix: uninstall the two devices, reboot, and let Windows rebuild the stack. When that is not enough, the chipset drivers and BIOS are the next layer, because the Microsoft battery drivers are only as good as the platform underneath them. Work the list in order and you will either fix it in minutes or prove conclusively that the battery itself needs attention.
