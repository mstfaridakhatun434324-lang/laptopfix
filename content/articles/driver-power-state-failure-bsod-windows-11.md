---
title: "Driver Power State Failure BSOD on Windows 11: How to Fix It"
slug: driver-power-state-failure-bsod-windows-11
date: 2026-09-01
categories: ["windows-errors"]
tags: ["driver power state failure", "bsod", "sleep issues", "windows 11"]
description: "DRIVER_POWER_STATE_FAILURE blue screen on Windows 11, often on sleep or wake? Fix it with driver updates, power settings, and clean boot testing."
thumbnail: "/images/thumbs/driver-power-state-failure-bsod-windows-11.webp"
faqs:
  - q: "What causes DRIVER_POWER_STATE_FAILURE?"
    a: "A driver failed to complete a power state transition in time — typically when the laptop sleeps, wakes, or hibernates. Windows waits for each driver to acknowledge the power change; if one hangs, the system crashes. The usual offenders are graphics, Wi-Fi, Bluetooth, and chipset drivers, especially after a Windows feature update changes the power management handshake."
  - q: "Why does this blue screen happen when my laptop wakes up?"
    a: "Wake is the most demanding power transition: every device driver must reinitialize in sequence. If a driver's resume routine is buggy or conflicts with new OS power handling, it stalls and Windows crashes. Updating the graphics and network drivers, plus changing the PCI Express power setting, resolves most wake-triggered cases."
  - q: "Is it safe to change the PCI Express Link State Power Management setting?"
    a: "Yes. Setting it to Maximum performance (or Off) simply stops Windows from aggressively powering down PCIe devices to save energy. It may reduce battery life slightly, but it cannot damage hardware. It is a standard diagnostic step for power-transition crashes and is fully reversible."
  - q: "Can a clean boot really find the driver causing this?"
    a: "Yes — clean boot is the most reliable way to isolate the culprit. By disabling all non-Microsoft services and startup items, you test whether the crash still occurs. If it stops, you re-enable items in halves until the crash returns, which pinpoints the exact driver or program. It takes patience but gives a definitive answer."
---
DRIVER_POWER_STATE_FAILURE is the blue screen of the sleep/wake cycle. Your laptop goes to sleep fine, you open the lid, and instead of your desktop you get a crash — or it blue-screens the moment it tries to sleep. The stop code means one of your drivers didn't finish a power transition in time, and Windows, which can't safely continue with a device in limbo, pulls the plug.

The pattern is the diagnosis: if crashes cluster around sleep, wake, hibernate, or lid-close, you're in the right place. Work the list in order — the first few fixes are quick settings changes, and the later ones isolate the exact driver.

## Why this happens

- **Outdated graphics driver.** The GPU driver handles the most complex power transitions; old versions clash with Windows 11's power management after feature updates.
- **Wi-Fi or Bluetooth driver bugs.** Network adapters power down aggressively on sleep, and buggy resume routines are a classic trigger.
- **PCI Express power saving conflicts.** Aggressive PCIe link-state power management can leave devices unresponsive when Windows asks them to wake.
- **Fast Startup stale state.** The hybrid shutdown preserves driver state across boots; corrupted state repeats the crash every cycle.
- **Third-party power utilities.** Battery managers, "performance boosters," and OEM utilities that override Windows power plans can fight the OS.
- **Failing hardware.** A dying Wi-Fi card or SSD that doesn't respond to power commands will trip this error no matter what the software does.

## How to fix it

Work through these in order, quickest first.

### Fix 1: Disable Fast Startup

The fastest win for sleep/wake crashes.

1. Open **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and save.
4. Shut down fully, wait ten seconds, power on, and test a sleep/wake cycle. This alone fixes a surprising number of cases.

### Fix 2: Update graphics, Wi-Fi, and chipset drivers

Replace the three drivers most involved in power transitions.

1. Download the latest chipset driver from your laptop maker's support site first — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and install it.
2. Update the graphics driver next: use [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx), [AMD's driver page](https://www.amd.com/en/support/download/drivers.html), or [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) depending on your GPU.
3. Update the Wi-Fi and Bluetooth drivers from the laptop maker's site — don't rely on Windows Update for these.
4. Restart and test sleep/wake several times; power bugs often need a few cycles to confirm fixed.

### Fix 3: Change PCI Express and sleep power settings

Stop Windows from powering devices down so aggressively.

1. Go to **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **PCI Express > Link State Power Management** and set it to **Off** (or Maximum performance on some systems).
3. Expand **Sleep > Allow hybrid sleep** and set it to **Off**.
4. Expand **USB settings > USB selective suspend setting** and set it to **Disabled**. Apply, then test sleep/wake cycles.

### Fix 4: Run the Power troubleshooter and check for bad devices

Let Windows audit its own power configuration.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run the **Power** troubleshooter.
2. Open **Device Manager** and look for any device with a yellow warning — a malfunctioning device often fails power transitions.
3. For network adapters specifically, open **Properties > Power Management** and uncheck **Allow the computer to turn off this device to save power** as a test.
4. If unchecking that box stops the crashes, the adapter's power handling is buggy — keep it unchecked and update its driver.

### Fix 5: Perform a clean boot to isolate the culprit

If crashes persist, find exactly which program or driver is hanging.

1. Press **Win + R**, type `msconfig`, and on the **Services** tab check **Hide all Microsoft services**, then click **Disable all**.
2. Open Task Manager's **Startup apps** tab and disable everything.
3. Restart and test sleep/wake. If the crash is gone, re-enable services in halves, testing each time, until the crash returns.
4. The last group you re-enabled contains the culprit — narrow it down item by item, then update or uninstall it.

### Fix 6: Update the BIOS

Power management lives partly in firmware, and vendors fix these bugs in BIOS updates.

1. Check your current BIOS version in **System Information**.
2. On your laptop maker's support site, compare with the latest release and read its changelog for power or sleep fixes.
3. With the charger connected, run the BIOS updater and don't touch the machine until it completes.
4. After updating, load BIOS defaults, boot into Windows, and test several sleep/wake cycles.

### Fix 7: Test hardware and reset if needed

If software is exhausted, verify the hardware.

1. Run your laptop maker's built-in diagnostics (**F12**/**F2** at boot) with focus on the network adapter and storage.
2. Try disabling Wi-Fi in the BIOS or removing the Wi-Fi card if accessible, then test — a dying card is a real cause of this error.
3. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` to rule out corrupted power management files.
4. As a last resort, **Settings > System > Recovery > Reset PC > Keep my files > Cloud download**. For the broader troubleshooting angle on this stop code, see [the driver power state failure troubleshooting guide](/articles/driver-power-state-failure-troubleshooting/).

## Closing

DRIVER_POWER_STATE_FAILURE is almost a checklist error: Fast Startup off, three drivers updated, PCIe power saving tamed — and most laptops stop crashing. If yours began right after a Windows update, the [post-update driver power state failure guide](/articles/how-to-fix-driver-power-state-failure-after-windows-11-update/) covers update-triggered variants. The clean-boot isolation in Fix 5 is your precision tool when the quick fixes don't land. Once stable, avoid third-party "driver updater" and "battery optimizer" utilities; they are disproportionately the software that reintroduces exactly this crash a month later.
