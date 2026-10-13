---
title: "Laptop Battery Not Charging? Fixes That Actually Work"
slug: how-to-fix-laptop-battery-not-charging-youtube
date: 2026-09-27
categories: ["battery"]
tags: ["not charging", "charger issues", "battery driver", "troubleshooting"]
description: "A battery that will not charge is usually a charger, driver, or settings problem — not a dead battery. Work through these proven fixes."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-not-charging-youtube.webp"
faqs:
  - q: "Why is my laptop plugged in but the battery is not charging?"
    a: "The usual suspects, in order: a faulty or underpowered charger, a loose or dirty charging port, a tripped battery protection circuit, a corrupted ACPI battery driver, a manufacturer charge limiter capping the charge, or a worn-out battery. The fixes below address them in that order so you find the cause fast."
  - q: "How do I know if the problem is the charger or the battery?"
    a: "Test with a known-good charger of the correct wattage. If the battery charges with a different adapter, your charger is the problem. If no charger helps, run powercfg /batteryreport — a healthy capacity reading points to drivers or settings, while a tiny full-charge capacity points to a worn battery."
  - q: "Can a Windows update stop the battery from charging?"
    a: "Yes, it happens. Updates can corrupt the ACPI battery driver, reset power plans, or — via a bundled firmware update — change charging behavior. If charging broke right after an update, reinstalling the battery drivers (Fix 4) and checking for a new BIOS (Fix 6) are the most likely cures."
  - q: "My battery says 0% available, plugged in, not charging. Is it dead?"
    a: "Not necessarily. That exact message often appears with a deeply discharged battery whose protection circuit has tripped, or with a driver glitch. Leave it plugged in and powered off for an hour first — deeply discharged packs sometimes need a slow trickle before the system recognizes them again."
---

Few things are more frustrating than a charger plugged in, the LED lit, and the battery percentage refusing to move — or worse, the dreaded "plugged in, not charging" message. Before you assume the battery is dead and start shopping for a replacement, know this: most charging failures are caused by the charger, the port, the driver, or a settings quirk. Actual dead batteries are further down the list.

The trick is testing in the right order so you do not waste money on a new battery when a $0 driver reset was the fix. That is what this guide does. If your specific message is the "plugged in, not charging" variant, our [dedicated troubleshooting guide](/articles/troubleshoot-laptop-plugged-in-not-charging/) goes deeper on that exact symptom.

## Why this happens

- **Failing or underpowered charger.** A damaged cable, dying brick, or wrong-wattage adapter cannot deliver the current the battery needs.
- **Loose or dirty charging port.** Lint, bent pins, or a worn jack break the connection intermittently.
- **Tripped battery protection circuit.** Deep discharge or a fault can lock the pack until reset.
- **Corrupted ACPI battery driver.** Windows loses proper communication with the battery after updates or crashes.
- **Manufacturer charge limiter active.** Conservation or lifespan modes cap charging and can look like a failure.
- **Worn-out battery.** A pack at the end of its life may refuse charge entirely.
- **Faulty motherboard charging circuit.** The least common cause, but real — the board cannot route power to the battery.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the battery still will not charge.

### Fix 1: Rule out the outlet, cable, and charger

Plug the adapter directly into a wall outlet you know works — test it with a lamp or phone charger. Inspect the entire cable for damage, and check that the connector seats firmly in the laptop with no wobble. If the brick has its own LED, confirm it is lit. Then, if possible, test with a different charger of the exact wattage your laptop requires (printed on the original brick). If charging resumes with another adapter, yours is the problem — replace it with the manufacturer's original, since wrong-wattage and cheap third-party chargers cause repeat issues. Genuine replacements are identifiable via maker sites such as [Dell's support pages](https://www.dell.com/support).

### Fix 2: Clean the charging port and check the connection

Power off and unplug. Shine a light into the charging port and look for lint, dust, or bent pins — pocket lint in USB-C ports is a classic culprit. Clean gently with a dry wooden toothpick or short bursts of compressed air; never use metal tools or liquids. Plug the charger back in firmly and watch the charging LED for a full minute. If it flickers when you wiggle the plug, the port itself is worn and needs professional repair — no software fix will help a physically loose jack.

### Fix 3: Perform a hard power reset

This clears tripped protection circuits and confused power controllers. Shut down completely, unplug the adapter, and remove the battery if removable. Press and hold the power button for 30 seconds. Reconnect the adapter only, boot up, shut down again, reinstall the battery, then plug in and leave it charging — powered off — for at least an hour. Check the percentage afterward. This single procedure resolves a remarkable number of "not charging" cases, especially after deep discharges.

### Fix 4: Reinstall the ACPI battery drivers

Driver corruption is a top cause, particularly after Windows updates. Open **Device Manager**, expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and select **Uninstall device**. Uninstall **Microsoft AC Adapter** too if listed. Then click **Action > Scan for hardware changes** — Windows reinstalls fresh copies of both. Restart the laptop, plug in the charger, and check whether charging resumes. This takes two minutes and fixes more cases than most people expect.

### Fix 5: Check for a charge limiter

Open your manufacturer's utility — **Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, **MSI Center** — and look for conservation mode, battery health charging, or charge thresholds. If a limiter is capping the charge (commonly at 60 or 80 percent), the battery is behaving exactly as configured, not broken. Turn the limiter off temporarily to confirm charging works, then decide whether to keep it for battery longevity. Also check the BIOS for battery-care settings that may have been enabled by a recent update.

### Fix 6: Update the BIOS and chipset drivers

Charging behavior is managed partly by firmware, and manufacturers fix charging bugs in BIOS updates. Visit your maker's support site, download the latest **BIOS** and **chipset** drivers for your exact model, and install them with the adapter plugged in. After the update, shut down, unplug for a minute, reconnect, and test charging. If a Windows update caused the problem, also check [Microsoft's Update Catalog](https://www.catalog.update.microsoft.com/) for any revised driver packages for your hardware.

### Fix 7: Verify battery health and consider replacement

If everything above checks out, get the verdict from the battery itself. Run in an elevated **Command Prompt**:

```
powercfg /batteryreport
```

Compare **Design Capacity** with **Full Charge Capacity** in **battery-report.html**. A full charge capacity below 30 to 40 percent of design, or a report showing erratic capacity history, means the pack is spent — replacement is the fix. Buy a genuine battery with the exact part number from your old pack. If the report shows a healthy battery that still will not charge after all fixes, the motherboard's charging circuit is suspect and needs a repair-shop diagnosis. Our [battery health deep-dive](/articles/how-to-check-battery-health-on-windows-11-laptop/) helps you read the full report before you spend money.

## Closing

"Not charging" sounds terminal, but it is usually the charger, the port, a tripped circuit, or a driver — all fixable without spending much. Work the list in order, testing after each step, and you will either have a charging battery again or a battery report that proves the pack is done. Either outcome beats guessing and buying parts at random.
