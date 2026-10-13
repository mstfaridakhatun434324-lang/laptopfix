---
title: "How to Fix a Laptop Battery Not Charging After the Windows 11 24H2 Update"
slug: how-to-fix-laptop-battery-not-charging-after-windows-11-24h2-update-youtube
date: 2026-09-08
categories: ["battery"]
tags: ["battery not charging", "windows 11 24h2", "charging fix"]
description: "Laptop plugged in but not charging after the Windows 11 24H2 update? Work through these proven fixes — most people are charging again in 20 minutes."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-not-charging-after-windows-11-24h2-update-youtube.webp"
faqs:
  - q: "Why did my laptop stop charging right after the 24H2 update?"
    a: "The 24H2 update replaces low-level drivers, including the battery controller driver. If the new driver doesn't handshake correctly with your battery's firmware, Windows shows 'plugged in, not charging.' A driver reinstall usually restores the handshake."
  - q: "Is 'plugged in, not charging' dangerous for the laptop?"
    a: "No. It means the charger is powering the laptop but the battery isn't accepting charge. You can keep working plugged in while you troubleshoot — just don't unplug until it's fixed."
  - q: "Should I roll back the 24H2 update to fix charging?"
    a: "Try the driver and power-reset fixes first — they solve it in most cases. Rollback is a last resort because it removes security updates, and the same driver issue can return with the next update anyway."
  - q: "How do I know if my charger is the problem?"
    a: "Test with a different compatible charger, or check whether the laptop charges while powered off. If it charges when off but not in Windows, it's software. If it never charges, suspect the charger or battery hardware."
---
"Plugged in, not charging." Four words nobody wants to see — especially when they appeared the morning after Windows 11 24H2 installed itself overnight. Your charger is fine, the outlet is fine, and the laptop was charging perfectly yesterday. So what changed? The update did.

The 24H2 update touches the driver stack that talks to your battery. When that handshake breaks, Windows sees the charger but can't negotiate charging. The fix is methodical, not mysterious — start simple, and most people are back to charging within twenty minutes.

## Why this happens

- **The battery driver got replaced.** 24H2 installs its own version of the ACPI battery driver, which doesn't always handshake correctly with older battery firmware.
- **A charge limit got activated silently.** Manufacturer tools (ASUS Battery Health Charging, Lenovo Conservation Mode) can flip to a limit mode during the update, capping charge at 60-80% — which looks like "not charging."
- **The battery controller needs a reset.** The update can leave the controller in a stuck state where it refuses charge commands until power-cycled.
- **Power plans were reset.** 24H2 sometimes resets custom power settings, including battery thresholds set through manufacturer software.
- **The charger handshake failed.** USB-C PD negotiation is software-driven; a driver glitch can make the laptop reject a charger it accepted yesterday.
- **Coincidence with hardware failure.** Occasionally the timing is just bad luck — a dying charger or battery gives up the same week as an update.

## How to fix it

Work through these in order. Don't skip the simple ones — they fix more cases than you'd expect.

### Fix 1: Check for a sneaky charge limit first

Before anything else, rule out the "feature, not bug" scenario.

1. Hover over the battery icon: if it says something like "80% available (plugged in)" and holds steady, a limit is active.
2. Open your manufacturer's app — **MyASUS** > Battery health charging, **Lenovo Vantage** > Power, **Dell Power Manager** > Battery settings — and check whether a limit or conservation mode is on.
3. Set it back to **Full capacity** / off temporarily. If charging resumes, that was it. You can re-enable an [80% limit](/articles/how-to-limit-battery-charge-to-80/) deliberately afterward.

### Fix 2: Power-cycle the battery controller

1. Shut down completely (**Start** > **Power** > **Shut down**).
2. Unplug the charger. If the battery is removable, remove it for 60 seconds.
3. Hold the power button down for **30 seconds** with everything disconnected.
4. Reconnect the battery (if removed), plug in the charger, wait 2 minutes, then power on.

### Fix 3: Reinstall the battery driver

The core 24H2 fix — this resolves the broken driver handshake.

1. Press **Windows key + X** > **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device** > **Uninstall**.
3. Also uninstall any **Microsoft ACPI-Compliant Embedded Controller** entries you see there if present.
4. Click **Action** > **Scan for hardware changes**, or just restart — Windows reinstalls fresh drivers on boot.
5. Plug in the charger and watch the battery icon for 2-3 minutes.

### Fix 4: Try a different charger and port

1. If you use USB-C charging, try a different USB-C port — on many laptops only one or two ports support Power Delivery.
2. Test with the original manufacturer charger if you have it. Third-party chargers that worked before 24H2 sometimes get rejected after the driver change.
3. Check the charger's wattage against what the laptop needs — an underpowered charger can show "plugged in, not charging" under load. The official [Microsoft software download page](https://www.microsoft.com/en-us/software-download/windows11) also hosts the 24H2 installer if you ever need a clean reinstall as a last resort.

### Fix 5: Run the battery report to check for hardware clues

1. Open **Terminal (Admin)** and run: `powercfg /batteryreport /output "C:\battery-report.html"`.
2. If **FULL CHARGE CAPACITY** is drastically lower than **DESIGN CAPACITY**, the battery may have genuinely failed — coinciding with the update.
3. Check **Battery capacity history** for a cliff edge exactly at the update date (gauge reset — fixable) versus a long decline (wear — not fixable).

### Fix 6: Update the BIOS and chipset drivers

1. Visit your manufacturer's support page and install the latest **chipset driver** first, then the **BIOS** update for your exact model.
2. 24H2-era BIOS updates often include battery controller firmware fixes specifically for this issue.
3. Keep the charger plugged in throughout and don't touch the laptop during the BIOS flash.

### Fix 7: Check if it charges while powered off

This one test separates software from hardware.

1. Shut the laptop down completely and plug in the charger.
2. Look for the charging LED. Leave it 30 minutes, then boot and check the percentage.
3. If it charged while off but not in Windows → it's a Windows/driver problem; repeat Fix 3 or consider the [dedicated troubleshooting guide](/articles/laptop-battery-not-charging-after-windows-11-24h2-update-troubleshooting/) for deeper steps.
4. If it didn't charge while off either → it's the charger, port, or battery hardware. Try another charger, then contact support.

### Fix 8: Do a Windows repair install as the last software resort

If every driver fix fails, repair Windows itself without losing your files.

1. Go to the [Microsoft software download page](https://www.microsoft.com/en-us/software-download/windows11) and download the Windows 11 installation assistant or ISO for 24H2.
2. Run setup from within Windows and choose **Keep personal files and apps**.
3. The repair install refreshes every system driver — including the battery stack — while leaving your data and programs in place. It takes 30-60 minutes.
4. After it completes, check charging before reinstalling any manufacturer utilities, so you can tell whether Windows or the utility was the problem.

## Closing

"Plugged in, not charging" after 24H2 is overwhelmingly a software handshake problem: check for charge limits, reset the controller, reinstall the battery driver. The off-vs-on charging test tells you in half an hour whether you're fighting Windows or fighting hardware — and most of the time, it's Windows, and Windows can be fixed without replacing anything.
