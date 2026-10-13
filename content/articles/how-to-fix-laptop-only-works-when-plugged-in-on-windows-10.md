---
title: "How to Fix a Laptop That Only Works When Plugged In on Windows 10"
slug: how-to-fix-laptop-only-works-when-plugged-in-on-windows-10
date: 2026-09-29
categories: ["battery"]
tags: ["plugged in", "battery dead", "windows 10"]
description: "Windows 10 laptop dies the instant you unplug it? Find out if the battery is dead, undetected, or just not charging."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-when-plugged-in-on-windows-10.webp"
faqs:
  - q: "Why does my Windows 10 laptop turn off when I unplug the charger?"
    a: "The battery is not supplying any power. Either the cells are worn out, Windows 10 cannot detect the battery due to a driver problem, or the battery never charges because of a charger or charging-circuit fault. The charger powers the laptop directly, which is why it works fine plugged in."
  - q: "How do I test my laptop battery on Windows 10?"
    a: "Open an admin Command Prompt and run powercfg /batteryreport. The report shows design capacity versus full charge capacity — a huge gap means a worn battery. If the report has no battery data, Windows cannot detect the battery at all."
  - q: "Can a Windows 10 update cause the battery to stop working?"
    a: "It can break battery detection — updates sometimes corrupt the ACPI battery driver or change power management behavior. The battery hardware is unaffected. Reinstalling the battery driver in Device Manager usually restores detection."
  - q: "My laptop works without the battery when plugged in. Is that OK?"
    a: "Yes, most laptops run fine on AC power with the battery removed — it is a good diagnostic step. Just be careful: with no battery there is no backup, so any power flicker shuts the laptop down instantly and you could lose unsaved work."
---

The charger comes out, the laptop dies. Instantly, no warning, no low-battery popup — as if the battery were not there at all. On Windows 10 this usually means one of three things: the battery is genuinely exhausted, Windows lost track of it, or it simply never receives a charge. Each one looks identical from the outside, so the job is to figure out which you have.

This guide is built around that diagnosis. A single battery report tells you most of what you need, and the fixes branch from there — software first, hardware last.

## Why this happens

- **End-of-life battery.** Cells degraded beyond delivering usable current — the most common cause on older laptops.
- **Broken battery detection.** A corrupt ACPI driver means Windows 10 ignores a perfectly good battery.
- **Charging failure.** Bad charger, loose DC jack, or faulty charging circuit — the battery drained long ago and never refilled.
- **Disconnected battery.** Internal connector loosened by drops or heat cycling.
- **Swollen battery safety cutoff.** The protection circuit disconnects a dangerous pack.
- **BIOS battery disable.** Servicing modes can electrically isolate the battery.

## How to fix it

Work through these in order — the report in Fix 1 directs everything after.

### Fix 1: Generate the battery report

This is the diagnostic that decides the whole repair path.

1. Right-click **Start** > **Command Prompt (Admin)**.
2. Run `powercfg /batteryreport`.
3. Open the HTML report from the path it prints.
4. **Battery data present, capacity collapsed?** The battery is worn out — go to Fix 7.
5. **No battery information at all?** Detection failure — go to Fix 3.
6. **Capacity looks okay?** The battery exists but is not engaging — work through Fixes 2-6.
7. New to this report? Our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) walks through each section (written for Windows 11, but the report is identical on 10). Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) also documents the report command.

### Fix 2: Confirm the battery is actually charging

A battery that never charges looks exactly like a dead one.

1. Hover over the taskbar battery icon. You want "plugged in, charging" with a climbing percentage.
2. "Plugged in" alone means no charge is flowing — check the charger wattage against the laptop's requirement on the bottom panel.
3. Charge for 2 uninterrupted hours. Zero movement means the charging path is broken, not the battery.
4. Try another outlet and, if available, another charger of the correct wattage.
5. A flickering charge indicator suggests a loose DC jack — wiggle the plug gently (laptop on a table, careful) and watch the icon. If it flickers, the jack needs repair.

### Fix 3: Reinstall the battery driver

Windows 10 updates break this driver regularly. Reinstalling takes two minutes.

1. Press **Win + X** > **Device Manager**.
2. Expand **Batteries** > right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**.
3. Click **Action** > **Scan for hardware changes**.
4. Restart the laptop with the charger connected.
5. Unplug briefly — any runtime at all means detection is restored.
6. If the Batteries category is empty or the driver will not come back, follow our [battery not detected guide](/articles/laptop-battery-not-detected-windows-11/) — the Device Manager steps are the same on Windows 10.

### Fix 4: Do a full power reset

Clears stuck charge-controller state that can block battery engagement.

1. Shut down the laptop completely.
2. Unplug the charger and all USB devices.
3. If the battery is removable, remove it now.
4. Press and hold the power button for 30 seconds to drain residual power.
5. Reinsert the battery, reconnect the charger, and power on.
6. Let it charge for 30 minutes, then unplug and test.
7. This old-school reset still fixes a surprising number of "dead battery" complaints that are really stuck controllers.

### Fix 5: Check BIOS battery status

See what the firmware thinks — it does not lie about detection.

1. Restart and enter BIOS (**F2** for Dell, **F10** for HP, **Del** for most others, **F1** for Lenovo).
2. Find the battery status or information page.
3. Note exactly what it says: health percentage, "not detected," or an error code.
4. Look for battery disconnect or ship-mode options and make sure they are off.
5. If BIOS also cannot see the battery, it is hardware — connector, pack, or motherboard circuit. Continue to Fix 6.

### Fix 6: Reseat the battery connector

Only open the laptop if you are comfortable — otherwise take it to a shop for this step.

1. Power off, unplug everything, and remove the back panel.
2. Locate the battery's multi-pin connector on the motherboard. Unplug it and inspect for corrosion, bent pins, or burn marks.
3. Reseat it firmly until it clicks or sits flush.
4. **Inspect the battery itself.** Swelling, warping, or a chemical smell means stop — do not reconnect a swollen battery. Arrange safe disposal.
5. Reassemble, charge for 30 minutes, then unplug and test.

### Fix 7: Replace a worn-out battery

When the report shows the capacity is gone, replacement is the fix.

1. Double-check the numbers: full charge capacity under ~20% of design, or the laptop dies on unplug after all the above.
2. Find the exact part number on the old battery. Match voltage, watt-hour rating, and connector — close is not good enough.
3. Buy genuine or quality OEM-equivalent. Cheap knockoffs often misreport to Windows and cause new problems.
4. After installing, charge fully, then calibrate: drain to shutdown, rest a few hours, recharge to 100%. See our [calibration guide](/articles/how-to-calibrate-laptop-battery-windows-11/).
5. If even a new battery will not engage, the motherboard charging circuit is faulty — a shop-level board repair.

## Closing

On Windows 10, "dies when unplugged" is a diagnosis problem first and a repair problem second. The battery report tells you in minutes whether you are fighting a dead battery, a blind operating system, or a broken charger. Fix the right one and you will know it worked the first time you pull the plug and the screen stays on. And whatever the outcome, save your work more often until it is fixed — a laptop with no battery backup forgives nothing.
