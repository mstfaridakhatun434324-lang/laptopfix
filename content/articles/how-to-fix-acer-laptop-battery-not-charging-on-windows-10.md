---
title: "How to Fix an Acer Laptop Battery Not Charging on Windows 10"
slug: how-to-fix-acer-laptop-battery-not-charging-on-windows-10
date: 2026-09-18
categories: ["battery"]
tags: ["acer", "battery not charging", "windows 10"]
description: "Plugged in but not charging on your Acer laptop? Follow these 8 proven fixes for Windows 10, from driver resets to Acer Care Center settings."
thumbnail: "/images/thumbs/how-to-fix-acer-laptop-battery-not-charging-on-windows-10.webp"
faqs:
  - q: "Why does my Acer laptop say plugged in but not charging?"
    a: "The most common causes are a faulty AC adapter, corrupted battery drivers, a battery charge limit enabled in Acer Care Center, or a physically worn-out battery. Work through the driver reset and charge-limit steps below first — they fix this for most users without any new hardware."
  - q: "Does uninstalling the battery driver harm my Acer laptop?"
    a: "No. Uninstalling the Microsoft ACPI-Compliant Control Method Battery driver is safe. Windows 10 reinstalls it automatically the next time you restart or scan for hardware changes. It simply clears a corrupted driver state that can block charging, and takes less than two minutes."
  - q: "Where is the battery charge limit setting on Acer laptops?"
    a: "Open the Acer Care Center app from the Start menu, go to Checkup, and look for Battery Charge Limit or Battery Health options. If a limit such as 80% is enabled, the battery will stop charging once it reaches that level. Disable the limit to allow a full charge."
  - q: "When should I replace the Acer laptop battery?"
    a: "Run powercfg /batteryreport and compare the design capacity with the full charge capacity. If the battery holds under 50% of its original capacity, or it only works while plugged in, replacement is the practical fix. Most Acer batteries are rated for roughly 300 to 500 charge cycles."
---

You plug in the charger, the little plug icon appears on the battery, and Windows tells you the laptop is "plugged in, not charging." The percentage stays frozen no matter how long you leave it connected. On Acer laptops running Windows 10, this is one of the most reported battery problems, and it rarely means your battery is dead.

The good news is that most of the causes are software or settings problems you can fix at home. Before you buy a new battery or charger, run through the steps below. Start at the top — the first few fixes solve this for the majority of users.

## Why this happens

- **Faulty AC adapter or cable** — a damaged brick or loose DC jack means the laptop gets enough power to run but not enough to charge the battery.
- **Corrupted battery drivers** — the Microsoft ACPI battery driver can glitch after a Windows update and stop communicating with the charger.
- **Battery charge limit enabled** — Acer Care Center can cap charging at 80% to extend battery life, which looks exactly like "not charging."
- **Residual charge glitch** — a power state can get stuck in the laptop's embedded controller, confusing the charging circuit.
- **Worn-out battery cells** — after hundreds of charge cycles, a degraded battery may refuse to take a charge at all.
- **Power plan corruption** — a broken power scheme can mismanage charging behavior, especially after feature updates.

## How to fix it

Work through these in order, testing the charger after each step.

### Fix 1: Rule out the charger and outlet

Start here because adapter problems cause this symptom more often than any software issue. A charger that partially failed can still power the laptop while the battery refuses to charge, which is exactly what many people describe.

1. Unplug the adapter from the wall and the laptop. Inspect the brick and cable for fraying, kinks, or a burning smell.
2. Plug it into a different wall outlet — skip power strips and surge protectors for this test.
3. Push the connector firmly into the laptop's charging port. Wiggle it gently; if the charging LED flickers, the port or plug is loose.
4. If you have access to a compatible adapter (same voltage and wattage), test with it. A mismatched low-wattage charger often runs the laptop but cannot charge the battery.

### Fix 2: Drain residual power

1. Shut the laptop down completely and unplug the AC adapter.
2. If your Acer has a removable battery, take it out. If not, skip that part.
3. Press and hold the power button for a full 30 seconds. This clears stored charge in the capacitors.
4. Reconnect the battery (if removable), plug in the charger, and boot up. Check whether the battery icon now shows "charging."

### Fix 3: Reset the battery drivers in Device Manager

1. Right-click the **Start** button and open **Device Manager**.
2. Expand **Batteries**. You will see entries like **Microsoft AC Adapter** and **Microsoft ACPI-Compliant Control Method Battery**.
3. Right-click each entry and choose **Uninstall device**. Confirm when asked.
4. Click **Action** > **Scan for hardware changes**. Windows reinstalls the drivers automatically.
5. Restart the laptop with the charger connected and check the battery status.

### Fix 4: Turn off the battery charge limit in Acer Care Center

1. Open **Acer Care Center** from the Start menu (install it from the Microsoft Store if it is missing).
2. Go to the **Checkup** tab and look for **Battery Charge Limit** or **Battery Health**.
3. If a limit is set (commonly 80%), turn it **Off**.
4. Some Acer models manage this in the BIOS instead: restart, press **F2** repeatedly to enter BIOS, find the battery charge limit option under the **Main** or **Power** tab, and disable it.
5. Save, exit, and verify the battery charges past the previous stopping point.

### Fix 5: Run the power troubleshooter and reset power plans

1. Go to **Settings** > **Update & Security** > **Troubleshoot** > **Additional troubleshooters**.
2. Run the **Power** troubleshooter and apply any fixes it suggests.
3. Open **Command Prompt** as administrator and run `powercfg /restoredefaultschemes` to reset all power plans to factory defaults.
4. Restart and check charging behavior. Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows) has more background on power troubleshooting if the built-in tool misses something.

### Fix 6: Update the BIOS and chipset drivers

1. Visit Acer's support site and download the latest **BIOS** and **chipset driver** for your exact model.
2. Close all apps, connect the AC adapter, and run the BIOS update — do not interrupt it.
3. Install the chipset driver update and restart.
4. BIOS updates often fix charging and battery-detection bugs that no Windows setting can touch.

### Fix 7: Check battery health with a battery report

1. Open **Command Prompt** as administrator and run `powercfg /batteryreport`.
2. Open the generated report from `C:\Windows\System32\battery-report.html`.
3. Compare **Design Capacity** with **Full Charge Capacity**. If you want a deeper read on what these numbers mean, see our guide to [check your battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/).
4. If full charge capacity is below half of design capacity, the battery itself is worn and software fixes will not help — replacement is the next step.

### Fix 8: Test with a minimal boot to rule out software interference

1. Press **Win + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, check **Hide all Microsoft services**, then click **Disable all**.
3. On the **Startup** tab, open **Task Manager** and disable every startup item.
4. Restart with the charger connected. If the battery charges now, re-enable services in groups to find the conflicting program — security suites and hardware utilities are common culprits.

## Closing

An Acer laptop that refuses to charge on Windows 10 is usually a driver, setting, or adapter issue rather than a dead battery. Work from the simple checks toward the deeper resets, and if nothing changes, [generate a battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/) to confirm whether the battery itself has reached the end of its life. A genuine hardware failure is much cheaper to confirm than to guess at, so let the report make the call.
