---
title: "Laptop Battery Not Charging When Plugged In? The Fixes That Actually Work"
slug: how-to-fix-laptop-battery-not-charging-when-plugged-in-youtube
date: 2026-09-06
categories: ["battery"]
tags: ["battery not charging", "plugged in", "troubleshooting"]
description: "Plugged in but not charging? Skip the generic advice — these are the specific fixes technicians use, in the order they use them."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-not-charging-when-plugged-in-youtube.webp"
faqs:
  - q: "What does 'plugged in, not charging' actually mean?"
    a: "It means Windows detects the AC adapter but the battery isn't accepting charge. Causes range from intentional charge limits and driver glitches to a dead adapter, a worn battery, or a failed charging circuit. The status alone doesn't tell you which — you have to test."
  - q: "Should I try a different charger first or check software first?"
    a: "Check the physical basics first: outlet, cable, and connector take two minutes and rule out the most common causes. Then move to software — EC reset and driver reinstall — before spending money on a new charger or battery."
  - q: "How do I know if it's the charger or the battery that's bad?"
    a: "If the laptop runs fine on AC power with the battery removed (or at 0% without shutting off), the charger works and the battery is suspect. If the laptop won't run on AC alone, the charger or charging circuit is the problem."
  - q: "Can Windows updates cause 'plugged in, not charging'?"
    a: "Yes. Updates can reinstall generic battery drivers, reset power plans, or deliver firmware that re-enables charge limits. If charging broke right after an update, start with the driver reinstall and charge-limit checks."
---
"Plugged in, not charging" is the most searched battery phrase for a reason: it's infuriatingly vague. The message tells you the charger is detected but says nothing about why the battery refuses to take power. You've probably already tried unplugging and replugging it. The web is full of one-line "fixes" that amount to turning it off and on again — those help when the problem is trivial, but most charging failures need actual diagnosis: charger, controller, drivers, settings, battery, in that order. Let's go deeper, the way a repair technician would.

This guide assumes the obvious — charger firmly seated, outlet live — and starts where real diagnosis starts. Every step includes a concrete test, so you always know whether to keep going or stop because you've found the fault.

## Why this happens

- **Charge limit features engaged.** Manufacturer battery-care modes intentionally stop charging at 60–80%.
- **Stale or corrupt battery drivers.** The ACPI battery driver misreports or blocks charging after updates.
- **Embedded controller stuck.** The EC manages charging and can latch into a no-charge state.
- **Failing or underpowered adapter.** The charger is detected but can't deliver charge current.
- **Worn-out battery.** A pack with dead cell groups may refuse charge entirely.
- **Dirty or damaged charging port.** Poor contact allows detection but not current flow.
- **Overheating protection.** The system blocks charging when the battery is too hot.

## How to fix it

Work through these in order, testing whether the battery charges after each step.

### Fix 1: Verify the outlet, cable, and connector properly

Don't skip this — it takes two minutes and catches the most common cause.

1. Plug a phone charger into the same outlet to confirm it's live.
2. Unplug the laptop charger from both the wall and the laptop, then firmly reseat both ends.
3. Inspect the laptop's charging port with a flashlight — look for bent pins, lint, or scorch marks.
4. Check the cable along its full length for damage, especially where it meets the brick and the connector.

If anything looks damaged, stop here and replace that part. A surprising number of "not charging" cases end at this step.

### Fix 2: Reset the embedded controller

The EC is the chip that decides whether charging happens. Reset it:

1. Shut down fully — hold **Shift** while clicking **Shut down** to bypass Fast Startup.
2. Unplug the charger and all USB devices.
3. Hold the power button for 30–60 seconds.
4. Plug the charger back in, wait 10 seconds, then power on.

Watch the battery icon for five minutes at the lock screen. This clears more "not charging" cases than any other single step.

### Fix 3: Reinstall the battery drivers

1. Press **Win + X** → **Device Manager**.
2. Expand **Batteries**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** → **Uninstall device**.
4. Right-click **Microsoft AC Adapter** → **Uninstall device**.
5. Click **Action > Scan for hardware changes**, then restart.

After rebooting, connect the charger at the desktop and give it a few minutes. Windows rebuilds the charging driver stack cleanly. This is also Microsoft's recommended step in their [Windows power troubleshooting](https://support.microsoft.com/en-us/windows) guidance.

### Fix 4: Check every charge limit

Manufacturers love to cap charging, and updates re-enable these silently:

- **Lenovo Vantage > Device > Power:** turn off **Conservation Mode**.
- **Dell Power Manager > Battery Settings:** set to **Standard**.
- **MyASUS > Battery Health Charging:** set to **Full capacity mode**.
- **HP BIOS (F10 at boot):** **Battery Health Manager** → **Let HP Manage My Charging**.
- **Windows Settings > System > Power & battery:** check for **Smart charging** holding the level.

Also verify in the BIOS for any battery threshold setting. If your battery was [only charging when the laptop is off](/articles/how-to-fix-battery-only-charges-when-laptop-is-off-in-windows-11-24h2/), that's a related symptom with its own causes.

### Fix 5: Run the battery report and read the verdict

Open an elevated Command Prompt and run:

```
powercfg /batteryreport /output %USERPROFILE%\Desktop\battery-report.html
```

Check **Full Charge Capacity** vs **Design Capacity** and scan the usage history for the moment charging stopped. If capacity is under half of design, the battery is worn out — no software fix will bring it back. If capacity is healthy but the charge rate is zero, the problem is upstream: adapter, port, or board.

### Fix 6: Test with a known-good charger

Borrow or buy a charger matching your laptop's exact voltage and equal-or-higher wattage. Test for 30 minutes. If charging resumes, your adapter was the fault — replace it with the correct spec, not a cheap universal knockoff with the wrong tip voltage. If charging still fails with a good adapter, the fault is in the laptop: battery or charging circuit.

### Fix 7: Cool the system and check thermals

Feel the chassis. If it's hot, power off and let it cool for 30 minutes on a hard surface, then retry. Chronic overheating while charging degrades both the battery and the charge controller — see [overheating while charging](/articles/how-to-fix-laptop-overheating-while-charging-after-windows-11-update/) if heat is a recurring theme. As a last software step, check **Settings > Windows Update** for pending firmware updates that might contain a charging fix, available via the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update misses them.

### Fix 8: Decide between battery and board

If you've reached this point: the charger is good, drivers are fresh, no limits are active, the system is cool, and it still won't charge. Run the manufacturer's built-in diagnostic (F12 on Dell, F2 on HP, Vantage on Lenovo). A failed battery test means replace the battery. A passed battery test with no charging means the charging circuit on the motherboard — that's a professional board repair, not a DIY job.

## Closing

"Plugged in, not charging" is a symptom with a dozen causes, but the diagnostic order never changes: physical connection, EC reset, drivers, charge limits, battery health data, adapter test, thermals, then the hardware verdict. Follow that sequence and you'll either fix it or know exactly which part to replace — no guessing, no wasted money on parts you didn't need. Keep notes as you go: which steps changed the icon, what the battery report said, whether the charger LED behaved oddly. If you end up at a repair shop or on a support call, that log turns a vague complaint into a precise fault description, and precise faults get fixed faster.
