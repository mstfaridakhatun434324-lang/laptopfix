---
title: "Laptop Says Plugged In But Not Charging? How to Troubleshoot It"
slug: laptop-plugged-in-not-charging-troubleshooting
date: 2026-09-29
categories: ["battery"]
tags: ["plugged in not charging", "charger", "battery driver", "troubleshooting"]
description: "That 'plugged in, not charging' message has a short list of usual causes. Work through them in order and get charging again."
thumbnail: "/images/thumbs/laptop-plugged-in-not-charging-troubleshooting.webp"
faqs:
  - q: "What does 'plugged in, not charging' actually mean?"
    a: "It means Windows sees the AC adapter but no current is flowing into the battery. The cause ranges from intentional — a charge limiter holding the battery at a set level — to a failing charger, a tripped protection circuit, a driver glitch, or a worn battery. The message alone does not tell you which; the fixes below narrow it down."
  - q: "If it says 'plugged in, not charging' at 100%, is something wrong?"
    a: "No, that is normal. When the battery is full, Windows stops charging and runs the laptop directly from the adapter — the message just describes that idle state. It is only a problem when the percentage is well below full and refuses to climb."
  - q: "Can I fix 'plugged in, not charging' without buying anything?"
    a: "Often yes. The free fixes — a hard power reset, reinstalling the ACPI battery drivers, disabling a charge limiter, and cleaning the charging port — resolve the majority of cases. You only need to spend money if testing points to a dead charger or a worn battery."
  - q: "Why did 'plugged in, not charging' start after a Windows update?"
    a: "Updates frequently disturb the ACPI battery driver or reset manufacturer power utilities, and firmware bundled with updates can enable battery-care modes. Reinstalling the battery drivers and checking the manufacturer's app for newly enabled limiters fixes most post-update cases."
---

Hover over the battery icon and there it is: "plugged in, not charging." The adapter is connected, the laptop runs fine on wall power, but the percentage sits frozen — 62 percent today, 62 percent tomorrow. It is one of the most searched laptop complaints there is, and fortunately one of the most fixable.

The message is vague by design; it covers everything from a deliberate charge cap to a dying charger. The good news: the causes have a clear pecking order, and working through them in sequence finds the answer fast — usually within half an hour and without spending anything. For the broader "battery won't charge at all" picture, see [our general not-charging guide](/articles/how-to-fix-laptop-battery-not-charging-on-windows-10/) as well.

## Why this happens

- **A charge limiter is holding the level.** Manufacturer battery-care modes cap charging and report exactly this status.
- **The charger is weak or failing.** It powers the laptop but cannot spare current for the battery.
- **The battery protection circuit tripped.** Deep discharge or a fault locks the pack against charging.
- **The ACPI battery driver is corrupted.** Windows misreads the battery state after updates.
- **The charging port connection is poor.** Dirt or a loose jack interrupts the charge path.
- **The battery is worn out.** A spent pack may be detected but unable to accept charge.
- **Firmware changed charging behavior.** BIOS updates can enable conservative charging modes silently.
- **Overheating protection paused charging.** If the pack or charging circuit runs too hot, the system suspends charging until temperatures drop — which reads as "not charging" in Windows.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the message persists.

### Fix 1: Check whether a limiter is responsible

Before anything else, rule out the intentional cause. Open your manufacturer's app — **Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, **MSI Center** — and look for conservation mode, battery health charging, or charge thresholds. If the battery is sitting exactly at the limiter's cap (60, 80, or 95 percent are common), that is your answer: the laptop is doing what it was told. Disable the limiter temporarily and watch for 20 minutes. If charging resumes, you have a configuration, not a fault. Our [charge limiter troubleshooting guide](/articles/how-to-fix-battery-limiter-not-working-on-windows-10/) covers these settings in depth.

### Fix 2: Test the charger properly

A charger can run the laptop while being too weak to charge the battery — this is a classic trap. Check the wattage printed on the brick against what your laptop requires; a 65W adapter on a 130W machine produces exactly this symptom. Inspect the cable for damage, plug directly into a wall outlet, and if possible test with a known-good adapter of the correct wattage. If a different charger starts the charge, replace yours with the manufacturer's original part. Identify the right part through maker sites such as [Dell's support pages](https://www.dell.com/support) using your service tag.

### Fix 3: Do the hard power reset

Shut down completely, unplug the adapter, and remove the battery if it is removable. Hold the power button for 30 seconds to drain residual charge. Reconnect the adapter only and boot, then shut down, reinstall the battery, and charge — powered off — for an hour. This resets tripped protection circuits and confused embedded controllers, and it clears "plugged in, not charging" more often than any other single step, especially after deep discharges.

### Fix 4: Reinstall the battery drivers

Open **Device Manager**, expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**. Do the same for **Microsoft AC Adapter** if listed. Click **Action > Scan for hardware changes** to reinstall both drivers fresh, then restart. This is the go-to fix when the message appeared right after a Windows update, since updates are notorious for corrupting exactly these drivers. Check the battery icon after reboot.

### Fix 5: Clean and inspect the charging port

Power off and unplug everything. Examine the charging port with a flashlight for lint, dust, or bent pins, and clean it with a dry wooden toothpick or compressed air — never metal or liquids. A surprising number of stubborn "not charging" cases trace back to pocket lint packed into a USB-C port. Reconnect the charger firmly and watch the LED and the Windows battery status for a few minutes. If wiggling the plug changes the status, the jack is worn and needs professional repair; intermittent physical connections produce exactly this on-again-off-again charging state.

### Fix 6: Update BIOS and chipset drivers

Charging logic lives partly in firmware. Download the latest **BIOS** and **chipset** drivers for your exact model from the manufacturer's support site and install them with the adapter connected. Reboot, then test charging. If a Windows update triggered the problem, also look on [Microsoft's Update Catalog](https://www.catalog.update.microsoft.com/) for revised drivers for your specific hardware — Microsoft occasionally ships fixed battery drivers there before they reach Windows Update.

### Fix 7: Read the battery report and decide

If nothing has worked, let the battery speak for itself. In an elevated **Command Prompt**, run:

```
powercfg /batteryreport
```

Open **battery-report.html** and compare **Design Capacity** to **Full Charge Capacity**. A healthy-capacity battery that still will not charge after all the above points to a motherboard charging fault — time for a repair-shop diagnosis. A badly degraded capacity means the pack is spent and replacement is the fix; buy genuine, matched to the part number on the old battery. Either way, you now have evidence instead of guesses.

## Closing

"Plugged in, not charging" is Windows being honest but unhelpful — the message tells you what, not why. Work the list from limiter to charger to reset to drivers, and the why reveals itself quickly. Most of the time it is one of the free fixes; when it is not, the battery report gives you the proof you need before spending a cent on parts you might not need.
