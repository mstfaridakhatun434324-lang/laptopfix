---
title: "How to Fix a Laptop Plugged In But Not Charging"
slug: how-to-fix-laptop-plugged-in-not-charging-reddit
date: 2026-09-02
categories: ["battery"]
tags: ["plugged in not charging", "troubleshooting", "windows 11", "charger"]
description: "Laptop says plugged in but the battery won't charge? Work through this proven fix order, from settings to hardware."
thumbnail: "/images/thumbs/how-to-fix-laptop-plugged-in-not-charging-reddit.webp"
faqs:
  - q: "What does 'plugged in, not charging' mean?"
    a: "Windows detects the AC adapter but the battery percentage isn't increasing. It's different from 'no battery detected' — here Windows sees the battery fine, but no charge current is flowing into it. Causes range from charge-limit settings to driver issues to hardware faults."
  - q: "Is plugged in not charging bad for the battery?"
    a: "Not inherently — if it's caused by a charge limit setting (like an 80% cap), it's actually protecting the battery. But if the battery is draining while plugged in, or stuck at a very low percentage, you should troubleshoot promptly since you have no real backup power."
  - q: "Why does my laptop stop charging at 80%?"
    a: "That's almost certainly a battery health feature: Lenovo charge thresholds, Dell battery health settings, ASUS Battery Health Charging, HP Battery Health Manager, or Surface Smart Charging. Check your manufacturer's battery app first."
  - q: "Can a Windows update cause charging to stop?"
    a: "Yes. Updates frequently corrupt the ACPI battery driver or reset power management behavior. If charging broke right after an update, reinstalling the battery drivers in Device Manager is the first thing to try."
---

"Plugged in, not charging" — four words that have launched a thousand forum threads. The charger is connected, Windows acknowledges it, and yet the percentage sits frozen. Sometimes it even slowly drops. The good news: this specific symptom has a well-trodden fix path, and most cases resolve without new hardware. It's also worth knowing that this message is different from a battery that won't hold charge — here the battery may be perfectly healthy, just not receiving current.

The single most useful observation you can make: *where* does it stop? Exactly 80%, 60%, or 55% means a manufacturer charge limit is doing its job. Stuck at a random number, or slowly draining, means something is actually wrong. That distinction shapes everything below.

## Why this happens

- **Manufacturer charge limits:** Battery longevity features capping charge at 80% or lower — the top cause by far.
- **Corrupted battery drivers:** The ACPI driver stack breaks after Windows updates, stopping charge negotiation.
- **Underpowered or failing adapter:** Wrong-wattage or damaged chargers may power the laptop without charging the battery.
- **Worn battery:** Degraded cells trigger protection circuits that refuse or limit charging.
- **Overheating:** Hot batteries charge slowly or not at all until they cool — a safety behavior.
- **Dirty or damaged charging port:** Poor contact interrupts the power path.
- **BIOS/firmware bugs:** Outdated firmware mishandles charging, especially after OS updates.

## How to fix it

Work through these in order — check the intentional limits before assuming a fault.

### Fix 1: Check for a manufacturer charge limit

This resolves the majority of cases. Open your brand's battery app — **Lenovo Vantage** (charge threshold), **Dell Power Manager** (battery health setting), **MyASUS** (Battery Health Charging), **HP BIOS / HP Battery Health Manager**, **Surface app** (Smart Charging), or **Acer Care Center**. Look for any cap like 80%, 60%, or "maximum lifespan" mode. If one is active and your battery is parked exactly at that number, everything is working as designed. Disable it or raise it to 100% if you need full charges. This one check saves more time than any other step in this guide.

### Fix 2: Inspect the charger, cable, and port

Confirm you're using the original charger at the correct wattage — a phone charger or weak spare will show "plugged in" while barely charging, and some laptops display the message specifically because the adapter can't meet the minimum wattage. Check the cable for frays and kinks, and look into the charging port with a flashlight for lint, dust, or bent pins. Clean gently with a dry toothbrush or compressed air. Try a different wall outlet. If you charge via USB-C, verify you're in the designated charging port with a properly rated cable — not every USB-C port on a laptop accepts full charging power.

### Fix 3: Reinstall the battery drivers

Press **Win + X** → **Device Manager** → expand **Batteries**. Right-click **Microsoft ACPI-Compliant Control Method Battery** → **Uninstall device**, then do the same for **Microsoft AC Adapter**. Restart — Windows reinstalls both automatically. This is the classic fix for "plugged in, not charging" appearing after a Windows update, and it works because it forces Windows to renegotiate the entire charging handshake from scratch. For the deeper driver walkthrough, see our guide on [updating battery drivers](/articles/how-to-update-battery-drivers-in-windows-11-24h2/).

### Fix 4: Cool the laptop down

Feel the chassis — if it's hot, charging may be paused as a safety measure. Shut down demanding apps, make sure vents aren't blocked (not on a bed or couch), and let the laptop cool on a hard surface for 15–20 minutes. Then check whether charging resumes. Also check **Settings → System → Power & battery → Battery saver** — turn it off during testing, since it can alter charging behavior on some systems. Persistent overheating during normal use suggests dust-clogged fans, which is a separate cleaning job.

### Fix 5: Reset the power state

Shut down fully, unplug the adapter and all peripherals. Hold the power button for **30 seconds** (or use the battery reset pinhole if your brand has one — common on Acer and Lenovo). Reconnect only the AC adapter and power on. This drains residual charge and resets the embedded controller that manages charging. It's particularly effective when charging stopped working suddenly with no settings change — the "it worked yesterday" cases.

### Fix 6: Update BIOS and chipset drivers

Visit your manufacturer's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — and install the latest BIOS and chipset/power drivers for your model. Charging logic lives partly in firmware, and manufacturers ship fixes for exactly this symptom. Keep the adapter plugged in during a BIOS flash and don't interrupt it. After updating, recheck your charge-limit settings since BIOS updates sometimes reset them.

### Fix 7: Test the battery's health

If software and charger are ruled out, check the battery itself:

```cmd
powercfg /batteryreport /output "C:\battery-report.html"
```

Open the report and compare **Design Capacity** to **Full Charge Capacity**. Below 60–70% indicates heavy wear, and worn batteries often trigger the protection behavior you're seeing. Also try charging with the laptop fully powered off for an hour — if it charges while off but not while on, Windows-side software is the culprit; if it won't charge while off either, it's hardware. Our guide on [checking battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/) explains how to read the report.

## Closing

"Plugged in, not charging" is a symptom with a clear diagnostic ladder: charge limit first (it's the cause most of the time), then charger and port, then drivers, then firmware, then the battery itself. The percentage where it stalls tells you most of what you need to know before you even start. Work the list in order and you'll either be charging again or holding a battery report that justifies a replacement — no guesswork, no wasted money on parts you didn't need. And if it was just a charge limit all along, consider leaving it on: your battery will thank you in two years.
