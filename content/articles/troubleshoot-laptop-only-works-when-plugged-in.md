---
title: "Laptop Only Works When Plugged In? Troubleshooting Guide"
slug: troubleshoot-laptop-only-works-when-plugged-in
date: 2026-09-24
categories: ["battery"]
tags: ["plugged in only", "battery dead", "won't run on battery", "troubleshooting"]
description: "If your laptop dies the instant you unplug it, the battery is not doing its job. Here is how to find out why and fix it."
thumbnail: "/images/thumbs/troubleshoot-laptop-only-works-when-plugged-in.webp"
faqs:
  - q: "Why does my laptop turn off immediately when I unplug it?"
    a: "The battery is not supplying power. The most common reasons are a fully worn-out battery that cannot hold charge, a battery the system no longer detects, a tripped protection circuit, or a loose internal battery connector. Less often, a faulty charging circuit on the motherboard is the cause."
  - q: "Can a laptop work with a completely dead battery?"
    a: "Yes, most laptops run fine on AC power with a dead or even removed battery — that is exactly the symptom you are seeing. It is safe as a workaround, but you lose your built-in UPS: any power cut means instant shutdown and possible data loss, so do not treat it as a permanent solution."
  - q: "Will a battery report tell me if the battery is dead?"
    a: "Yes. Run powercfg /batteryreport in an elevated Command Prompt and compare Design Capacity to Full Charge Capacity. If full charge capacity is a small fraction of design — or the report shows no battery at all — the pack is worn out or disconnected, which explains why the laptop only runs plugged in."
  - q: "Is it worth replacing the battery or should I buy a new laptop?"
    a: "If the laptop is otherwise healthy and under five years old, a genuine replacement battery is far cheaper than a new machine and takes minutes to swap on models with removable packs. For thin ultrabooks with glued-in batteries, get a repair-shop quote first — the labor can change the math."
---

Unplug the charger and the laptop dies instantly — not a graceful shutdown, just off. Plug it back in and it boots like nothing happened. That pattern has one clear meaning: the battery is contributing nothing, and the machine is running purely on wall power.

This is one of the most common aging-laptop complaints, and the cause is usually the battery itself rather than anything exotic. The steps below will confirm whether the pack is dead, disconnected, or just confused — and tell you what to do in each case. If your machine shows a related symptom where the charger is connected but the battery will not charge, see [plugged in but not charging](/articles/how-to-fix-laptop-plugged-in-not-charging-step-by-step/) as well.

## Why this happens

- **The battery is worn out.** After hundreds of cycles, capacity can drop so low that the pack cannot sustain the laptop for even a second under load.
- **The battery is no longer detected.** A loose internal connector, corrosion, or a failed battery controller makes Windows act as if no battery exists.
- **The protection circuit has tripped.** A deep discharge or fault can lock the pack's safety circuit, cutting all output until it is reset or replaced.
- **The battery gauge is badly miscalibrated.** Rare, but a confused fuel gauge can cause instant shutdowns at false readings.
- **The charging circuit is faulty.** If the motherboard's power path cannot switch between AC and battery, the machine only runs on the adapter.
- **A swollen or damaged pack was disconnected.** Some laptops disable a battery the firmware deems unsafe, leaving AC-only operation.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the laptop still dies on unplug.

### Fix 1: Check whether Windows sees the battery at all

Click the battery icon in the taskbar. If it says something like "No battery detected" or shows no percentage, Windows cannot see the pack — skip ahead to Fix 4. If it shows a percentage that never changes or drops instantly, the pack is detected but useless. For a definitive answer, open an elevated **Command Prompt** and run:

```
powercfg /batteryreport
```

Open **battery-report.html** and look at **Design Capacity** versus **Full Charge Capacity**. A full charge capacity under 20 percent of design means the battery is effectively dead. Our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) explains how to read every section of this report.

### Fix 2: Do a hard power reset

A tripped protection circuit sometimes just needs a reset. Shut down completely, unplug the adapter, and remove the battery if it is removable. Hold the power button down for 30 seconds. Reconnect only the adapter and boot up, then shut down, reinstall the battery, and plug in to charge for an hour undisturbed. Unplug and test. If the laptop now runs on battery even briefly, the reset cleared the fault — let it charge fully and recalibrate.

### Fix 3: Reseat the battery and clean the contacts

For removable batteries: power off, remove the pack, and inspect both the battery terminals and the laptop's contacts for corrosion, bent pins, or debris. Wipe them with a dry microfiber cloth — a pencil eraser works gently on light oxidation, followed by a dry wipe. Reinstall firmly until it clicks or sits flush. For internal batteries, this means opening the bottom panel: only do this if you are comfortable, the laptop is out of warranty, and you disconnect the adapter first. A loose internal connector is a classic cause of sudden AC-only behavior after a drop or bump.

### Fix 4: Reinstall the battery drivers

Windows can lose track of a perfectly good battery through driver corruption. Open **Device Manager**, expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**. Also uninstall **Microsoft AC Adapter** if present. Click **Action > Scan for hardware changes** to reinstall both. Restart, then check the taskbar icon again — if the battery reappears, charge it fully and test on battery power.

### Fix 5: Test the battery's real capacity

If the battery is detected but dies instantly, confirm it is truly worn before spending money. Charge to whatever maximum it reports, then unplug and time how long the laptop survives doing light work. Under a minute confirms a dead pack. Cross-check with the battery report from Fix 1: high cycle counts (800+) and tiny full-charge capacity seal the diagnosis. At this point no software fix will help — the chemistry is spent.

### Fix 6: Replace the battery with a genuine part

Order a replacement from the manufacturer or an authorized parts seller — match the exact model number printed on the old pack. Avoid the cheapest third-party batteries; poor cells and missing safety circuits cause exactly the problems you are trying to escape, and in rare cases are a fire risk. For sealed ultrabooks, get a quote from a reputable repair shop rather than prying a glued battery yourself. After installing, charge to 100 percent uninterrupted, then run one full discharge-charge cycle to calibrate. Genuine parts can be identified through maker sites like [Dell's support pages](https://www.dell.com/support) using your service tag.

### Fix 7: Rule out a motherboard charging fault

If a brand-new genuine battery still does not power the laptop, the fault is in the motherboard's power circuitry — the charge controller or the AC/battery switching path. Signs pointing here: the battery charges fine in another identical laptop, or the machine behaves the same with two different known-good batteries. This is board-level repair territory: get a diagnostic quote from a repair shop before deciding between repair and replacement.

## Closing

A laptop that only works plugged in is almost always telling you the battery is dead, disconnected, or undetected — and the battery report plus a hard reset will identify which within half an hour. Replace a worn pack with a genuine one and you get your portable laptop back; if a new battery changes nothing, the motherboard is the answer and a repair quote tells you whether it is worth pursuing.
