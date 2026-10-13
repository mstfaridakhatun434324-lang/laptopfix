---
title: "Quiet a Laptop Fan That Never Stops in Windows 11 24H2"
slug: how-to-fix-laptop-fan-always-running-in-windows-11-24h2
date: 2026-09-04
categories: ["performance"]
tags: ["laptop fan always running", "windows 11 24h2", "fan noise fix", "cpu overheating", "cooling"]
description: "Fan screaming non-stop after the 24H2 update? Find the background process driving it, fix cooling behavior, and get your laptop quiet again."
thumbnail: "/images/thumbs/how-to-fix-laptop-fan-always-running-in-windows-11-24h2.webp"
faqs:
  - q: "Why does my laptop fan run constantly after the 24H2 update?"
    a: "The update often leaves background tasks — indexing, Defender rescans, stuck update components — running far longer than normal, which keeps CPU warm and the fan spinning. Dust buildup and dried thermal paste make it worse by reducing cooling efficiency at the same time."
  - q: "Is it bad if my laptop fan always runs?"
    a: "The noise itself cannot damage anything — it is just the fan doing its job. But constant full-speed operation means constant heat, and sustained heat is what shortens component and battery life over years. Treat loud idle fan noise as a useful early warning: find the heat source now rather than replacing a worn-out fan or battery later."
  - q: "Will a cooling pad fix a constantly running fan?"
    a: "It helps marginally by improving airflow, but it treats the symptom. If a stuck process is pinning your CPU at 50 percent, a cooling pad will not fix that. Diagnose the software cause first, then improve cooling as a bonus."
  - q: "How do I know if my fan problem is dust or software?"
    a: "Check Task Manager: if CPU is high at idle, it is software. If CPU is low but the fan still roars and the chassis is hot, airflow is blocked — clean the vents. Both can be true at once, so check software first since it is free."
---

A laptop fan that never stops is trying to tell you something: the machine is hot, and it is hot for a reason. Since the Windows 11 24H2 update, that reason is very often software — a background process that the update left churning, keeping the CPU warm enough that the fan never gets to rest. The fan is not broken. It is responding correctly to a problem upstream.

The technician's rule is simple: never fight the fan, find the heat. A process pinning the CPU, a stuck indexer, or an update component in a loop will keep temperatures elevated no matter how clean your vents are. Only after the software side is quiet does it make sense to look at dust, paste, and cooling profiles.

Follow this order — software first, cooling second — and most constant-fan cases resolve without opening the machine.

## Why this happens

- **Stuck post-24H2 background tasks:** Indexing, Defender rescans, and update components can run for days after the feature update.

- **A process pinning the CPU:** One runaway process — check Task Manager — generates constant heat the fan must fight.

- **Dust-clogged vents and fans:** Restricted airflow forces the fan to spin faster to move the same heat.

- **Dried-out thermal paste:** After a few years, paste between CPU and heatsink degrades and heat transfer worsens.

- **Aggressive performance power plan:** High-performance modes hold clocks high, generating heat even at moderate load.

- **Blocked intake vents:** Using the laptop on a bed or couch smothers the intakes underneath.

- **BIOS fan curve changes:** Some 24H2-era BIOS updates altered fan curves to be more aggressive. Similar background-load issues are covered in [laptop fan always running after the Windows 11 update](/articles/how-to-fix-laptop-fan-always-running-after-windows-11-update/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find the process keeping the CPU warm

The fan follows temperature, and temperature follows CPU load. Find the load and you find the real problem.

1. Open Task Manager with Ctrl plus Shift plus Esc and sort by CPU.
2. Let it sit for two minutes and note any process consistently above 10 percent at idle.
3. Check the Startup apps tab for anything suspicious launching at boot.
4. If a Windows service is the hog, address it specifically — search indexer, Defender, and update components are the usual suspects.
5. End the task temporarily to confirm the fan calms down, then fix the underlying cause.

### Fix 2: Let post-24H2 background work finish

Right after the feature update, heavy background work is legitimate. The trick is distinguishing 'still settling' from 'stuck'.

1. Check Settings, Windows Update — if updates are still installing, let them finish.
2. Check Settings, Privacy and security, Searching Windows for active indexing.
3. Give a fresh 24H2 install 48 hours of plugged-in idle time to settle.
4. If background tasks are still hammering the CPU after 48 hours, they are stuck — treat them as broken, not busy.
5. Rebuild the search index or clear the Defender scan history as appropriate.

### Fix 3: Switch to a balanced power plan

High-performance plans hold the CPU at high clocks even when idle, generating constant heat. Balanced lets it idle properly.

1. Open Settings, System, Power and battery.
2. Set Power mode to Balanced or Best power efficiency.
3. Open Control Panel, Power Options, Change plan settings, Change advanced power settings.
4. Under Processor power management, set Maximum processor state to 95 percent on battery — this disables turbo boost heat spikes.
5. Apply and monitor fan behavior over the next hour.

### Fix 4: Clean the vents without opening the laptop

Dust in the exhaust fins is the most common physical cause, and you can clear a surprising amount without disassembly.

1. Power off the laptop and unplug it.
2. Use short bursts of compressed air into the exhaust vents — hold the can upright.
3. Blow into the intake vents on the bottom to dislodge dust from the other side.
4. Never use a vacuum directly on the vents — static discharge can damage components.
5. Place the laptop on a hard, flat surface so intakes stay clear during use.
6. Retest: if the fan is quieter under the same workload, dust was a factor.

### Fix 5: Update BIOS and chipset drivers

Manufacturers tune fan curves and thermal management in BIOS updates. An old BIOS on a new Windows build can mismanage cooling. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has additional guidance on managing overheating in Windows 11.

1. Check your laptop maker's support site for a BIOS update mentioning thermal or fan behavior.
2. Install it with the charger connected and do not interrupt the process.
3. Update the chipset driver from the same support site.
4. Check for a fan-control or thermal utility from the maker and set it to a balanced profile.
5. Monitor temperatures with HWMonitor or the maker's utility after updating.
6. For Intel-based machines, Intel's driver detection tool keeps chipset drivers current.

### Fix 6: Reposition and improve airflow

Physics matters: a laptop smothered on bedding cannot cool itself no matter how good the software and paste are.

1. Always use the laptop on a hard, flat surface — or at least a lap desk.
2. Prop the rear up slightly with a stand or even a book to open the intake gap.
3. Keep the room reasonably cool; ambient temperature directly affects fan speed.
4. Consider a cooling pad as a supplement, not a solution.
5. If the fan still screams at low CPU with clean vents, suspect dried thermal paste — a repaste is a shop job for most users.

## Closing

A fan that never stops is a messenger, not the problem. In the 24H2 era the message is usually a stuck background task keeping the CPU warm — find it, fix it, and the fan goes quiet on its own. Clean the vents while you are at it, and your laptop gets the cool, silent idle it was designed for. Background utilities like the [Widgets board can also drive idle CPU](/articles/how-to-fix-widgets-board-high-cpu-windows-11-on-lenovo-laptop/) — check it if the usual suspects come up clean.
