---
title: "How to Change Your Power Plan to Best Performance on Windows 11"
slug: "how-to-change-power-plan-to-best-performance"
date: "2026-09-06"
categories: ["performance"]
tags: ["power plan", "best performance", "windows 11", "cpu performance"]
description: "Laptop feeling sluggish on Balanced mode? Switch to the Best performance power plan in Windows 11 with these exact steps."
thumbnail: "/images/thumbs/how-to-change-power-plan-to-best-performance.webp"
faqs:
  - q: "Where is the Best performance power plan in Windows 11?"
    a: "Microsoft moved the main control to Settings, then System, then Power and battery, where a Power mode dropdown offers Best power efficiency, Balanced, and Best performance. The classic Control Panel power plans still exist but are hidden on many laptops; you can reveal them by running powercfg.cpl and clicking Show additional plans if your manufacturer hid them."
  - q: "Does Best performance drain the battery faster?"
    a: "Yes, noticeably. Best performance keeps the CPU at higher clock speeds, prevents aggressive core parking, and keeps the disk and wireless radios fully awake. Expect 20 to 40 percent less battery life compared to Balanced, depending on workload. The sensible approach is Best performance when plugged in and Balanced or Best power efficiency on battery."
  - q: "Why is the High performance plan missing on my laptop?"
    a: "Many laptop manufacturers hide the classic High performance plan because Modern Standby replaces the old sleep states it was designed around. You can restore it by running powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 in an elevated Command Prompt, which recreates the High performance scheme and makes it selectable in powercfg.cpl."
  - q: "Is Best performance safe for my laptop long term?"
    a: "Yes, with normal cooling. The plan does not overclock anything; it simply stops Windows from throttling the CPU aggressively. Your laptop may run warmer and the fans may spin up more often under load, which is normal. Keep vents clear and the machine will operate within its designed thermal limits indefinitely."
---

Windows 11 decides how aggressively your CPU can run through its power plan. On Balanced or Best power efficiency, the operating system constantly parks CPU cores, drops clock speeds, and throttles background tasks to save battery. That is ideal on a plane, but on a desk with the charger plugged in, it leaves real performance on the table: slower compiles, choppier games, and laggy photo edits.

The fix is a 30-second settings change. Windows 11 exposes a Power mode dropdown with three options, and behind it the classic High performance and Ultimate Performance schemes still exist for users who want them. Switching to Best performance tells Windows to keep clocks high, keep cores awake, and prioritize responsiveness over battery life.

This guide shows the quick Settings method, how to reveal the hidden classic plans including Ultimate Performance, how to set different modes for battery versus plugged in, and what to do when the options seem to be missing entirely.

## Why this happens

- **Balanced mode throttling the CPU:** The default plan aggressively lowers clock speeds between tasks, which adds latency to bursty workloads like gaming and compiling.
- **Best power efficiency enabled by mistake:** Some laptops ship with the most aggressive battery saver as default, crippling performance even on AC power.
- **Manufacturer hiding classic plans:** OEMs often hide the High performance scheme in powercfg.cpl on Modern Standby laptops.
- **Per-plan settings never tuned:** Even on Best performance, sub-settings like maximum processor state may be capped by a manufacturer profile.
- **Battery saver overriding the plan:** When battery drops below the saver threshold, Windows forces efficiency mode regardless of your chosen plan.
- **Thermal throttling misread as a plan issue:** If vents are blocked, the CPU throttles for heat no matter which plan is active.
- **Power mode resetting after updates:** Feature updates occasionally reset the Power mode dropdown back to Balanced.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Switch Power mode to Best performance in Settings

This is the official Windows 11 method and takes seconds. It is also the setting most likely to survive updates.

1. Press Win+I to open Settings, then select System.
2. Click Power and battery in the right pane.
3. Find the Power mode dropdown near the top.
4. Select Best performance from the three options.
5. Plug in the charger if you have not already, since the difference is most noticeable on AC power.

### Fix 2: Reveal the hidden High performance plan

The classic High performance scheme still ships with Windows 11 but is hidden on many laptops. A single command restores it in the Control Panel applet.

1. Press Win+X and choose Terminal (Admin).
2. Type powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 and press Enter.
3. You should see confirmation that the Power Scheme GUID was created.
4. Press Win+R, type powercfg.cpl, and press Enter.
5. Click Show additional plans and select High performance.

### Fix 3: Enable the Ultimate Performance plan

Ultimate Performance is a step above High performance, originally built for workstations. It removes nearly all power-saving latency and is available on Windows 11 Pro.

1. Open Terminal (Admin) with Win+X.
2. Type powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 if you have not already, or use the Ultimate GUID de32e6c1-1a9b-4102-b705-34d7167f1c25.
3. Open powercfg.cpl and click Show additional plans.
4. Select Ultimate Performance.
5. Monitor temperatures during heavy work, since fans will run more aggressively.

### Fix 4: Set different plans for battery and plugged in

Running Best performance on battery will drain it fast. The smart setup is maximum performance on AC and Balanced on battery, which Windows handles per power source in advanced settings.

1. Open powercfg.cpl and click Change plan settings next to your active plan.
2. Click Change advanced power settings.
3. Expand Processor power management, then Maximum processor state.
4. Set On battery to 95 or 99 percent and Plugged in to 100 percent.
5. Click Apply and OK. Windows now scales back slightly on battery automatically.

### Fix 5: Stop Battery saver from overriding your plan

Battery saver forces efficiency behavior below a charge threshold. Raising or disabling that threshold keeps your chosen performance level consistent.

1. Open Settings, then System, then Power and battery.
2. Expand the Battery saver section.
3. Note the Turn battery saver on automatically at setting.
4. Raise it to a low value like 10 percent, or toggle battery saver off manually when you need full speed.
5. Remember to re-enable it on long flights where battery matters more than speed.

### Fix 6: Verify the CPU actually runs faster

Do not trust the label; verify with Task Manager that clocks actually rise under load after the switch.

1. Press Ctrl+Shift+Esc to open Task Manager.
2. Go to the Performance tab and select CPU.
3. Run a heavy task such as a game or a large file compression.
4. Watch the Speed readout; on Best performance it should sit near the chip's boost frequency.
5. If clocks stay low, check that vents are clear and the charger is connected, since thermal or power limits override any plan.

### Fix 7: Create a custom plan for plugged-in gaming

If none of the built-in plans match your needs, clone High performance and tune it. A custom plan survives updates better than modified defaults and lets you name it clearly.

1. Open powercfg.cpl and click Create a power plan in the left pane.
2. Choose High performance as the base and name it Gaming Plugged In.
3. Set display sleep to 30 minutes and computer sleep to Never for the plugged-in profile.
4. Open advanced settings and set Minimum processor state to 100 percent on Plugged in.
5. Save the plan and switch to it whenever the charger is connected.

### Fix 8: Create a custom plan for plugged-in gaming

If none of the built-in plans match your needs, clone High performance and tune it. A custom plan survives updates better than modified defaults and lets you name it clearly.

1. Open powercfg.cpl and click Create a power plan in the left pane.
2. Choose High performance as the base and name it Gaming Plugged In.
3. Set display sleep to 30 minutes and computer sleep to Never for the plugged-in profile.
4. Open advanced settings and set Minimum processor state to 100 percent on Plugged in.
5. Save the plan and switch to it whenever the charger is connected.

## Closing

Switching to Best performance is the simplest free speed boost on a Windows 11 laptop, especially when plugged in. Use the Settings dropdown for everyday control, restore the classic High performance or Ultimate Performance schemes when you want the old behavior, and keep Balanced on battery so you are not hunting for an outlet by noon. If the machine still feels slow after the switch, the bottleneck is elsewhere, and our guides to [disabling startup apps](/articles/how-to-disable-startup-apps-on-windows-11/) and [switching power plans per scenario](/articles/best-way-to-change-power-plan-to-best-performance/) are the logical next steps. You can read more about how power plans work in Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows). You can read more about how power plans work in Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows).
