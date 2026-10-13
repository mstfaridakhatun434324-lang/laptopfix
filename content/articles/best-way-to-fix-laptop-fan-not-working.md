---
title: "Laptop Fan Not Working? The Best Fix Sequence for a Silent, Overheating Machine"
slug: best-way-to-fix-laptop-fan-not-working
date: 2026-09-20
categories: ["drivers"]
tags: ["laptop fan not working", "fan not spinning", "overheating laptop", "fan control", "windows 11"]
description: "Laptop fan not spinning? Work through the best fix sequence: diagnose the fan, clean dust, fix silent-mode settings, update BIOS and chipset drivers, and know when the fan motor is dead."
thumbnail: "/images/thumbs/best-way-to-fix-laptop-fan-not-working.webp"
faqs:
  - q: "How do I know if my laptop fan is actually dead?"
    a: "A dead fan stays at zero RPM even when the CPU hits 85-95°C under load and no fan-control software can spin it up. Check RPM in HWiNFO64 or your BIOS hardware monitor while running a stress test. If the temperature climbs past 90°C and the fan never moves, the motor, connector, or power circuit has failed. If it spins in BIOS but not in Windows, it is a software problem."
  - q: "Can dust alone stop a laptop fan from spinning?"
    a: "Dust rarely stops the motor entirely, but a clogged heatsink and vent grilles can make the fan spin ineffectively or trigger overheat shutdowns that look like fan failure. Heavy dust also strains the bearings and can seize an older fan. Cleaning the vents with short bursts of compressed air resolves a large share of overheating complaints before any driver or BIOS work is needed."
  - q: "Why does my fan work in BIOS but not in Windows?"
    a: "That pattern almost always means software is holding the fan at zero RPM — a silent or quiet power plan, the manufacturer's fan-control app, or a third-party utility like a fan curve tool. It can also be a corrupted embedded-controller or chipset driver. BIOS spins the fan on firmware logic alone, so working in BIOS proves the motor and connector are fine."
  - q: "Should I replace the fan myself or use warranty?"
    a: "If the laptop is under warranty, use it — opening the chassis can void coverage and fan replacement often requires removing the heatsink and reapplying thermal paste. Out of warranty, fan replacement is a moderate DIY job: replacement fans are cheap, and guides exist for most models. If the fan connector or power circuit on the board is damaged, send it to a repair shop."
---

A laptop fan that never spins is not a feature — it is a countdown. A modern laptop CPU can go from idle to 95°C in under a minute of sustained load, and without airflow the firmware's only defense is brutal thermal throttling that turns a fast machine into a stuttering hand-warmer. Most "fan not working" reports, though, are not dead fans: they are dusty vents, a silent-mode fan curve set to zero, or a BIOS update that quietly broke fan control. The fixes for those are completely different from the fix for a dead motor, which is why this guide starts with diagnosis before touching anything.

The order below is deliberate. We confirm the fan is truly dead or merely misbehaving, clear the physical causes, then fix the software layer (power plans, vendor fan apps, chipset and BIOS firmware), and only at the end do we talk about opening the machine or replacing hardware. Most cases resolve in the first half without a screwdriver.

## Why this happens

- **Dust-clogged vents and heatsink.** Blocked airflow forces the fan to work harder for less cooling, and heavy buildup can strain bearings until the fan seizes.
- **Silent or quiet mode engaged.** Power plans and vendor apps (MyASUS, Lenovo Vantage, OMEN Hub) can hold the fan at zero RPM until high temperatures.
- **BIOS fan-control regression after an update.** Firmware updates occasionally break the embedded controller's fan curve.
- **Corrupted or outdated chipset/EC driver.** The fan is driven by the embedded controller; bad chipset drivers can leave it without instructions.
- **Temperature sensor misread.** If the firmware reads the wrong temperature, it never commands the fan to spin.
- **Fan connector dislodged.** After any prior repair, the tiny fan header can be loose or unplugged.
- **Failed fan motor or bearing.** Genuine hardware death — the fan gets power but cannot turn.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Prove the fan is really dead (don't skip this)

Everything downstream depends on this verdict, so get it right.

1. Install **HWiNFO64** (portable version is fine) and watch the fan RPM sensor — or enter BIOS/UEFI and find the hardware monitor showing fan speed.
2. Run a sustained CPU load (a 4K video export, a game, or a stress test) for 3–5 minutes while watching RPM and CPU temperature.
3. If the fan spins up in BIOS but stays at zero in Windows under 85°C+, you have a software problem (Fixes 3–5). If RPM stays zero everywhere while temps pass 90°C, it is physical (Fixes 2, 6, 7).
4. Listen closely with the vent to your ear during the load — a faint clicking or buzzing means a dying bearing; total silence means no power or a seized motor.
5. Note the exact behavior: never spins, spins then stops, or spins weakly. Each points somewhere different.

For driver-level diagnostics on related cooling hardware, the same Device Manager techniques in [how to update drivers on a Windows 11 laptop](/articles/how-to-update-drivers-on-windows-11-laptop/) apply.

### Fix 2: Clean the dust out of the cooling system

The highest-yield physical fix, and it takes five minutes.

1. Shut the laptop down fully and unplug it.
2. Hold the fan blades still through the vent with a toothpick or plastic tool — letting compressed air spin them freely can damage the bearings.
3. Blow **short bursts** of compressed air into the exhaust vents first (pushing dust out the way it came), then into the intake grilles underneath.
4. Do this outdoors or over a bin; the dust cloud from a two-year-old laptop is impressive.
5. Test again under load. If temperatures drop 10–20°C and the fan behaves, you are done.

### Fix 3: Get out of silent/quiet mode

Silent modes are the most common reason a healthy fan never spins.

1. Open your manufacturer's control app (Lenovo Vantage, MyASUS, HP OMEN Gaming Hub, Dell Power Manager) and set the thermal/fan mode to **Balanced** or **Performance**, not Silent or Quiet.
2. In Windows, go to **Settings > System > Power & battery** and set **Power mode** to Best performance while testing.
3. Check the vendor app for a manual fan-speed or "max fan" test option and run it — if the fan roars, the motor is fine.
4. Uninstall or disable third-party fan-control utilities (NoteBook FanControl, SpeedFan forks) that may be overriding the curve with a zero-RPM profile.
5. Some laptops have a **Fn key** combo for fan modes — check your manual; it is easy to trigger accidentally.

### Fix 4: Update BIOS and chipset drivers

When the embedded controller gets confused, firmware is the fix.

1. Identify your exact model and go to the manufacturer's support page — [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/) — and download the latest **BIOS** and **chipset** drivers.
2. Install the chipset driver first, then the BIOS update, with the AC adapter plugged in and the battery above 50%.
3. Do not interrupt a BIOS flash — a failed flash is far worse than a broken fan curve.
4. After flashing, load **BIOS defaults** (usually F9 in the BIOS menu) to clear any corrupted fan-control settings, then save and exit.
5. Recheck fan behavior under load. BIOS changelogs frequently list "fan curve" and "thermal policy" fixes, which is why this step matters.

### Fix 5: Repair the Windows driver layer

A corrupted embedded-controller or system device driver can leave the fan unmanaged.

1. Open **Device Manager**, expand **System devices**, and look for anything with a yellow warning — especially ACPI thermal/fan entries.
2. Right-click suspicious entries → **Update driver** → search automatically.
3. If that fails, uninstall the entry (do **not** check "delete driver software" unless you have the manufacturer's driver ready), then restart and let Windows reinstall it.
4. Run **Windows Update** and install everything, including optional driver updates — EC firmware sometimes ships this way.
5. Check your driver versions against the manufacturer's site using the method in [how to check the driver version in Device Manager](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/).

### Fix 6: Reseat the fan connector (for comfortable DIYers)

Only attempt this if you are out of warranty and comfortable opening a laptop.

1. Power off, unplug, and remove the bottom panel (keep track of screw lengths — they differ).
2. Disconnect the battery connector from the motherboard first — non-negotiable safety step.
3. Find the fan's small cable header on the motherboard; unplug it gently and plug it back in firmly.
4. Inspect for dust packed around the fan hub and clear it with a soft brush.
5. If the fan spins freely by hand but never powered on, and reseating changes nothing, the motor is likely dead — proceed to Fix 7.
6. Reconnect the battery, reassemble, and retest under load before fully tightening every screw.

### Fix 7: Replace the fan or use the warranty

The final verdict when everything else fails.

1. If the laptop is **under warranty**, file a claim — fan replacement is a standard warranty repair and opening the chassis yourself can void it.
2. Out of warranty: search your exact model number plus "replacement fan" — laptop fans are model-specific but usually inexpensive.
3. Fan replacement typically requires removing the heatsink, which means **replacing the thermal paste** — budget for quality paste and isopropyl alcohol.
4. If a new fan still does not spin, the fault is the fan power circuit on the motherboard — a board-level repair for a professional shop.

## Closing

A silent fan is either misbehaving software or dying hardware, and the diagnostic split — works in BIOS, dead in Windows, or dead everywhere — tells you which within ten minutes. Dust cleaning, exiting silent mode, and BIOS/chipset updates revive the vast majority of cases without opening the machine. When the motor itself is gone, warranty or a model-specific replacement fan finishes the job.
