---
title: "How Do I Fix a Laptop That Says Plugged In, Not Charging?"
slug: how-do-i-fix-laptop-plugged-in-not-charging
date: 2026-10-04
categories: ["battery"]
tags: ["plugged in not charging", "troubleshooting", "Windows"]
description: "\"Plugged in, not charging\" on your laptop? Follow this complete fix guide covering drivers, charge limits, adapters, and battery health."
thumbnail: "/images/thumbs/how-do-i-fix-laptop-plugged-in-not-charging.webp"
faqs:
  - q: "What does 'plugged in, not charging' mean?"
    a: "Windows detects the AC adapter but the battery is not accepting charge. The laptop runs on adapter power fine. Causes range from intentional charge limits and driver glitches to worn batteries and faulty adapters."
  - q: "How do I fix plugged in not charging on Windows 11?"
    a: "First check your manufacturer's battery app for charge limits. Then reinstall the ACPI battery driver in Device Manager, perform a hard reset (hold power 30 seconds with everything unplugged), and verify the adapter wattage matches your laptop's requirement."
  - q: "Can a Windows update cause 'plugged in, not charging'?"
    a: "Yes, frequently. Windows updates — especially feature updates like 24H2 — can corrupt or replace the battery driver. Reinstalling the Microsoft ACPI-Compliant Control Method Battery driver resolves most update-triggered cases."
  - q: "Is 'plugged in, not charging' bad for the laptop?"
    a: "Not immediately — the laptop runs normally on AC power. But you have no backup if power flickers, and if the cause is a dying battery, it will only get worse. Diagnose it rather than ignoring it."
---

"Plugged in, not charging" is Windows telling you, with unusual precision, exactly what it sees: power is coming in, but none of it is reaching the battery. The laptop works fine on the desk — until the power blips and everything dies instantly. It is one of the most common laptop complaints, and fortunately one of the most fixable.

The causes split into two camps: the laptop is *choosing* not to charge (limits, thresholds, protective behavior), or it *cannot* charge (drivers, adapter, battery). This guide helps you determine which camp you are in and fix it. For the broader diagnostic sweep, our [battery not charging troubleshooting guide](/articles/laptop-battery-not-charging-troubleshooting/) covers adjacent symptoms.

## Why this happens

- **Charge limit enabled.** Manufacturer utilities (Lenovo Vantage, MyASUS, Dell Power Manager) can hold the battery at 50–80% deliberately. This is the single most common cause.
- **Corrupted battery driver.** The ACPI battery driver translates charge commands; when corrupted by an update, charging silently stops.
- **Stuck embedded controller.** The EC can latch into a state where it ignores charge requests until hard-reset.
- **Wrong or failing adapter.** An underpowered, damaged, or unrecognized adapter may run the laptop without charging the battery — Dell is particularly strict about adapter authentication.
- **Worn-out battery.** A battery at end of life may be refused charging by its own safety controller.
- **BIOS bug or outdated firmware.** Charging logic lives partly in firmware; bugs there produce exactly this message.

## How to fix it

Work through these in order — the first three fix most cases.

### Fix 1: Check for charge limits in the manufacturer app

Rule out deliberate behavior first.

1. Open **Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, **Acer Care Center**, **HP Support Assistant**, or **MSI Center**.
2. Look for **conservation mode**, **battery health charging**, **charge threshold**, or **battery lifespan** settings.
3. If any limit is active, disable it temporarily and wait 15–30 minutes with the charger connected.
4. If charging resumes, that was it. Learn the trade-offs in our [charge limit guide](/articles/how-to-limit-battery-charge-to-80/) before deciding whether to re-enable it.

### Fix 2: Reinstall the battery driver

The classic fix for update-triggered cases.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and select **Uninstall device**.
3. Click **Action > Scan for hardware changes** to reinstall the driver automatically.
4. Shut down (do not just restart), wait 10 seconds, power on with the adapter connected, and check the battery status.
5. For the complete driver-stack version including chipset drivers, see our [Windows 11 driver guide](/articles/how-to-update-battery-drivers-on-windows-11/).

### Fix 3: Perform a hard reset

Clear the embedded controller's stuck state.

1. Shut down completely. Unplug the AC adapter and disconnect all peripherals.
2. If the battery is removable, remove it for 30 seconds, then reseat it.
3. Press and hold the power button for a full **30 seconds**.
4. Reconnect the adapter first, wait 30 seconds, then power on.
5. Check whether the battery icon now shows charging.

### Fix 4: Verify the adapter

Make sure the power supply is actually adequate.

1. Read the wattage on the adapter brick and compare it to your laptop's requirement (bottom sticker or manual).
2. Inspect the cable and plug for damage; wiggle the connector gently to check for intermittency.
3. If possible, test with a known-good adapter of the correct wattage.
4. On Dell, check the BIOS (**F2 > Battery Information**) for the **AC Adapter Type** — "Unknown" means the adapter failed Dell's authentication check.

### Fix 5: Check the battery health

Determine whether the battery itself is refusing charge.

1. In an administrator **Terminal**, run `powercfg /batteryreport`.
2. Compare **Full Charge Capacity** to **Design Capacity**. Below 60% suggests a worn battery whose controller may refuse charging.
3. Check the **cycle count** — very high counts mean end of life.
4. Also check the manufacturer's diagnostics (Dell **F12 Diagnostics**, HP **F2 Battery Test**, Lenovo Vantage hardware scan) for a direct health verdict.

### Fix 6: Update the BIOS

Firmware-level charging bugs are real and patchable.

1. Go to your manufacturer's support site, find your exact model, and download the latest **BIOS**.
2. With the adapter plugged in and all programs closed, run the update without interruption.
3. After the automatic restart, check the charging status.

### Fix 7: Test with the battery removed (if removable)

Isolate whether the battery is the problem.

1. Shut down, unplug, and remove the battery.
2. Plug in the adapter alone and power on. If the laptop runs fine, the charging circuit and adapter work.
3. Reinstall the battery. If "not charging" returns immediately, the battery is the faulty component — replace it with the exact part number.
4. If the laptop will not run on the adapter alone either, the adapter or charging circuit is suspect, not the battery.

### Fix 8: Inspect the battery's physical condition and seating

A battery with dirty contacts or a swollen cell can refuse charging while looking fine in software.

1. Shut down, unplug, and remove the battery if it is externally removable. Inspect the metal contacts for corrosion or grime — clean them gently with a dry cloth or a cotton swab barely dampened with isopropyl alcohol, then let them dry fully.
2. Reseat the battery firmly until it clicks, reconnect the adapter, and test.
3. For internal batteries, check for swelling: a bottom panel that bulges or a trackpad that feels raised means a swollen cell, which safety circuits isolate from charging. Stop using it and arrange a replacement.
4. Also confirm the battery's age against the laptop's warranty — many manufacturers cover premature battery failure. Microsoft's [Windows battery support pages](https://support.microsoft.com/en-us/windows) explain how Windows reports battery status if you want to cross-check the readings.

## Closing

"Plugged in, not charging" looks alarming but is usually a configuration or driver issue, not a dead laptop. The winning sequence — check limits, reinstall the driver, hard-reset the controller, verify the adapter — resolves the large majority of cases in under half an hour. When those all pass and the battery report shows heavy wear, you have a clear, evidence-based answer: the battery has earned its retirement, and a replacement will fix what no setting can.
