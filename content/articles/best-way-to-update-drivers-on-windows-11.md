---
title: "The Best Way to Update Drivers on Windows 11"
slug: best-way-to-update-drivers-on-windows-11
date: 2026-09-02
categories: ["drivers"]
tags: ["update drivers", "driver update", "windows 11", "device manager", "oem drivers"]
description: "The best way to update drivers on Windows 11: when to trust Windows Update, when to use manufacturer drivers, and the order that avoids breakage."
thumbnail: "/images/thumbs/best-way-to-update-drivers-on-windows-11.webp"
faqs:
  - q: "What's the best way to update drivers on Windows 11?"
    a: "Use Windows Update for everyday drivers, but get critical drivers — graphics, WiFi, audio, and chipset — from your laptop manufacturer's support site for your exact model. Manufacturer drivers are validated against your hardware, while generic updates can introduce the mismatches that cause devices to fail."
  - q: "Are third-party driver updater tools safe?"
    a: "Generally no. Most driver updater utilities bundle adware, install wrong drivers, or charge for what Windows and manufacturers provide free. The safe sources are Windows Update, the laptop maker's support site, and the component maker's site (Intel, NVIDIA, AMD) — in that order of preference."
  - q: "How often should I update drivers?"
    a: "Update graphics drivers every few months for performance and security, and update other drivers when something breaks or a manufacturer release notes mention your issue. The 'if it ain't broke' rule applies: routine mass-updating of working drivers causes more problems than it prevents."
  - q: "Should I update BIOS as part of driver maintenance?"
    a: "Only when the release notes address your specific problem or add needed hardware support. BIOS updates carry a small but real bricking risk if interrupted, unlike driver updates which are easily rolled back. Never update BIOS casually alongside routine driver maintenance."
---

Driver updates on Windows 11 are a "best tool for the job" problem. Windows Update handles the basics competently, the laptop manufacturer's site provides validated packages for your exact hardware, and the component makers (Intel, NVIDIA, AMD) offer the newest generic versions. Using the wrong source for a given driver is how working hardware breaks overnight — the classic story being a graphics or WiFi driver that dies right after an automatic update.

The best approach is a deliberate order: know which source to use for which driver, update in the right sequence, and always keep a rollback path.

The underlying principle is that not all drivers are created equal in risk. Chipset and storage drivers touch everything and are hardest to recover from if bad; graphics and wireless drivers are the most frequently updated and the most likely to regress; peripheral drivers (printers, card readers) are low-risk and can be left alone for years. Windows Update is conservative and safe for the low-risk tier but often wrong for the high-impact tier, where the manufacturer's validation matters. This is why the "best way" isn't a single tool but a tiered strategy: match the caution level to the driver's blast radius. A graphics driver deserves a restore point and a rollback plan; a card-reader driver barely deserves your attention.

## Why this happens

- **Windows Update installs generic drivers:** Fine for basic function, but they lack OEM tuning for your specific hardware.
- **Driver updaters install wrong versions:** Third-party tools match loosely and frequently pick incompatible packages.
- **Updating everything at once:** Mass updates make it impossible to identify which one broke something.
- **Skipping the chipset driver:** The chipset driver underpins USB, storage, and power management — updating it last (or never) causes odd failures.
- **No restore point before updating:** Without a rollback path, a bad driver becomes a crisis instead of an inconvenience.
- **BIOS and driver mismatch:** New drivers sometimes expect firmware features an old BIOS lacks.
- **Optional updates ignored:** The best driver updates often hide under Optional updates where users never look.
- **Old drivers left in the store:** Accumulated driver versions cause Windows to bind the wrong one.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Create a restore point first

1. Search **Create a restore point**, open System Properties, and click **Create**.
2. Name it with today's date and "pre-driver-update."
3. This takes thirty seconds and is your escape hatch if any update misbehaves.
4. Make this a habit before every driver session — professionals never skip it, and neither should you.

### Fix 2: Check Windows Update's Optional updates

1. Go to **Settings → Windows Update → Advanced options → Optional updates**.
2. Expand **Driver updates** and review what's offered — these are Microsoft-validated and safe for most hardware.
3. Install them selectively: take chipset, storage, and peripheral drivers; be cautious with graphics and WiFi if those currently work.
4. Restart after installing and verify your key devices still work before continuing.

### Fix 3: Get critical drivers from the manufacturer

1. Find your exact model on the maker's support site — Dell at [Dell support](https://www.dell.com/support), HP at [HP support](https://support.hp.com/us-en), Lenovo at [Lenovo support](https://support.lenovo.com/us/en/).
2. Download drivers for your **exact model and Windows 11 version**: prioritize BIOS (only if needed), chipset, graphics, wireless, and audio.
3. These OEM packages are validated against your hardware revision — they include firmware, tuning, and device-ID mappings generic drivers lack.
4. When a device breaks after a Windows driver update, the manufacturer's package is the fix, not another generic update.

### Fix 4: Update in the right order

1. Install in this sequence: **chipset** first, then **storage/SATA**, then **graphics**, then **network (WiFi/Ethernet/Bluetooth)**, then **audio**, then peripherals.
2. Restart between major categories — especially after chipset and graphics.
3. The chipset driver lays the foundation (PCIe, USB, power management) that other drivers build on; installing it last invites strange conflicts.
4. Never update the BIOS in the same session as drivers — do it separately, on AC power, with nothing else running.

### Fix 5: Use component-maker tools for graphics

1. For Intel graphics, run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. For NVIDIA, use the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx) and choose clean installation.
3. For AMD, use [AMD's driver support page](https://www.amd.com/en/support/download/drivers.html).
4. Component-maker drivers are newer than OEM ones — great for gaming performance, but if stability matters more than new features, stick with the OEM version.

### Fix 6: Update one driver at a time when troubleshooting

1. If you're updating to fix a problem, change **one driver**, restart, and test.
2. Keep notes: driver name, old version, new version, result.
3. This discipline is what separates a fix from a new mystery — when something breaks, you know exactly which change caused it.
4. If the new driver makes things worse, roll back immediately in **Device Manager → Properties → Driver → Roll Back Driver**.

### Fix 7: Clean out old driver versions

1. In **Device Manager**, when uninstalling a driver, check **Attempt to remove the driver for this device** to purge it from the driver store.
2. For graphics drivers, use **Display Driver Uninstaller (DDU)** in Safe Mode for a truly clean slate before installing fresh.
3. Old versions lingering in the store cause Windows to "helpfully" reinstall the driver you just removed.
4. After cleanup, verify in **Properties → Driver** that the version and date match what you intended to install.

### Fix 8: Know when not to update

1. If every device works, skip optional driver updates — stability beats novelty for drivers.
2. Never use third-party "driver updater" utilities; they cause more breakage than all other sources combined.
3. Pause Windows driver updates via **System → Advanced system settings → Hardware → Device Installation Settings → No** if updates keep breaking a working driver. Our guide on [disabling automatic driver updates](/articles/best-way-to-disable-automatic-driver-updates/) walks through that setting in detail.
4. For battery-related drivers specifically, our [battery driver update guide](/articles/how-to-update-battery-drivers-on-windows-11/) covers the ACPI nuances. And if a driver update already broke something, the [show/hide updates troubleshooter](https://support.microsoft.com/en-us/windows) can block the offender.

## Closing

The best driver update strategy is boring on purpose: restore point first, Windows Update's optional drivers for the routine stuff, manufacturer packages for the critical hardware, component-maker tools for graphics when you want the newest, and one change at a time. Drivers are infrastructure — update them deliberately, and they stay invisible the way infrastructure should be. The one habit that pays for itself many times over: before any driver session, thirty seconds for a restore point. It's the cheapest insurance in all of Windows maintenance.
