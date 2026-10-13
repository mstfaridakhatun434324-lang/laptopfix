---
title: "How to Test Your Laptop Charger on Windows 11 (5 Methods)"
slug: how-to-test-laptop-charger-on-windows-11
date: 2026-09-07
categories: ["battery"]
tags: ["laptop charger", "windows 11", "power adapter test"]
description: "Charger suspect on Windows 11? Test it properly — Quick Settings checks, powercfg charge rates, USB-C power meters, and the definitive multimeter test."
thumbnail: "/images/thumbs/how-to-test-laptop-charger-on-windows-11.webp"
faqs:
  - q: "How do I test if my laptop charger is working on Windows 11?"
    a: "Start simple: plug into a known-good wall outlet, watch the taskbar battery icon for the plug symbol, and check Settings, then System, then Power & battery for charging status. Then get quantitative: `powercfg /batteryreport` shows actual charge rates in mW. For certainty, measure the charger's DC output with a multimeter (barrel plugs) or a USB-C power meter (USB-C chargers)."
  - q: "What should powercfg show for a good charger?"
    a: "In the battery report's Recent usage section, the charge rate while plugged in and idle should be a healthy fraction of your charger's rating — for example, 30-50W+ on a 65W charger with the laptop idle. Single-digit mW rates on a high-wattage charger, or rates that collapse under load, indicate a failing or underpowered adapter."
  - q: "Can I test a USB-C charger without a multimeter?"
    a: "Yes — with a USB-C power meter dongle ($15-20). It sits between charger and laptop and displays live voltage, amperage, and wattage, including the negotiated power-delivery profile. This is actually more informative than a multimeter for USB-C, because it shows whether the PD handshake succeeded and at what wattage."
  - q: "Why does Windows 11 say 'plugged in' but the battery won't charge?"
    a: "'Plugged in, not charging' usually means a charge limit is active (check your manufacturer's battery utility), the battery is already at its cap, or the charger is too weak to both run the laptop and charge. It can also mean the battery is worn or the EC is stuck. Detection works but charging does not — a different problem from a dead charger."
---

Windows 11 gives you better built-in tools for charger testing than Windows 10 did — the Power & battery page is more informative, Quick Settings shows status at a glance, and `powercfg` remains the quantitative backbone. This guide uses all of them, from the ten-second glance to the definitive electrical measurement.

If your testing shows the charger is fine but Windows will not charge the battery, the [complete not-charging guide](/articles/how-do-i-fix-laptop-battery-not-charging/) takes over from there.

## Why This Happens

- **Chargers die quietly.** No drama — one day the brick just stops converting power.
- **Cables fail before bricks.** Internal wire breaks near the connectors are the most common physical failure.
- **USB-C negotiation is fragile.** The PD handshake can fail while the charger itself is electrically fine.
- **Wattage mismatch.** Phone chargers and low-wattage adapters "connect" without usefully charging.
- **Windows 11 driver quirks.** The AC adapter driver can misreport, making a good charger look dead.
- **Port problems masquerade as charger problems.** A damaged jack or lint-filled USB-C port blocks power the charger is delivering.

## How to Fix It

Work through these in order, from glance to measurement.

### Fix 1: The Quick Settings and Icon Check

Ten seconds, no tools. Catches the obvious.

1. Note the battery percentage, then plug the charger into a wall outlet you have verified with another device.
2. Click the taskbar system tray (or just watch the battery icon): a plug symbol should appear within seconds.
3. Hover the icon — it should read like "72% available (plugged in, charging)".
4. Open **Settings** > **System** > **Power & battery** and confirm the top status line agrees.
5. No change? Unplug, firmly replug, and try a second outlet before concluding anything.
6. If the icon responds intermittently when you wiggle the plug, the fault is the port or cable — not the brick. The [charger-not-detected guide](/articles/troubleshoot-laptop-charger-not-detected/) covers port diagnosis in depth.

### Fix 2: Measure the Charge Rate With powercfg

Windows 11 logs charge rates. A weak charger confesses here.

1. Press **Win + X** > **Terminal (Admin)**.
2. Run `powercfg /batteryreport` and open the HTML file.
3. In **Recent usage**, find plugged-in periods and read the charge rate (mW).
4. Compare against your charger's rating: a 90W charger delivering 8W to an idle laptop is failing or being throttled.
5. Also compare plugged-in-off vs plugged-in-on rates. Healthy charger: strong charging while off. If it barely charges even while off, the adapter is dying.
6. Check **Battery capacity history** too — if the battery is healthy but charge rates are anemic, the charger is the bottleneck, full stop.
7. For extra precision, run the report twice: once with the laptop idle on the desktop, once while charging powered-off. The gap between the two readings tells you how much of the charger's output the running system consumes. A charger that can only barely exceed the system's idle draw will never meaningfully charge the battery during use — the classic underpowered-adapter signature.

### Fix 3: Test With USB-C Power Meter (USB-C Laptops)

The right tool for modern charging — shows the negotiation, not just the result.

1. Get a USB-C power meter dongle (widely available, $15-20). Plug it between the charger and the laptop.
2. Read the live display: voltage (should match a standard PD profile like 20V), current, and computed wattage.
3. Watch during plug-in: you should see the negotiation settle within seconds to your charger's rated profile.
4. **No reading at all:** dead charger, dead cable, or dead port — swap the cable first (cheapest).
5. **Reading far below rating** (e.g., 15W on a 65W charger): try another cable; if it persists, the charger's PD controller is failing.
6. **Correct reading but no charging:** the laptop is refusing the power — charge limit, EC issue, or battery problem. The charger is exonerated.

### Fix 4: The Multimeter Test (Barrel-Plug Chargers)

Definitive for traditional chargers. Fifteen dollars of hardware, zero ambiguity.

1. Set a digital multimeter to **DC volts** at a range above the charger's rated output (check the label — usually 19-20V).
2. Plug the charger into the wall. Touch red probe to the plug's inner contact, black probe to the outer barrel.
3. Compare the reading to the label: within ±5% is good.
4. Zero or near-zero: dead charger. Replace with matching voltage and equal-or-higher wattage.
5. Correct voltage but laptop will not charge: charger is fine — suspect the laptop's jack, EC, drivers, or battery.
6. While testing, flex the cable near both ends and watch the reading. Voltage that drops out with movement means broken internal wires — replace the charger even if it "sometimes works."
7. Also test under load if your meter supports it: some failing chargers show correct voltage with no load but collapse the moment the laptop draws current. If you can, measure while the laptop is plugged in and running — a voltage that sags more than about 10% under load means the brick's internals are failing even though it looks fine idle.

### Fix 5: The Swap Test and Final Verdict

When measurement is inconclusive, substitution decides.

1. Borrow a charger with identical voltage and equal-or-higher wattage (never higher voltage).
2. Known-good charger works on your laptop: yours is bad. Buy an exact-spec replacement — genuine or manufacturer-certified.
3. Known-good charger also fails: your laptop's port or charging circuit is at fault. Stop buying chargers.
4. Your charger works on another laptop: your laptop is at fault, same conclusion.
5. No spare hardware available: most repair shops test chargers free in under a minute. Cheaper than a wrong guess.
6. When replacing, match the connector, voltage exactly, and wattage at least equally. Document the purchase — the [Windows support site](https://support.microsoft.com/en-us/windows) and manufacturer pages both stress using correct-spec adapters, because wrong ones cause the subtle failures (slow charging, battery errors) that mimic dying batteries.

### Fix 6: Confirm With BIOS Detection and the Power Troubleshooter

Two independent checks that catch what the other methods miss.

1. Reboot into BIOS/UEFI (**F2**, **Del**, or **F10** during the logo screen) and look for an **AC Adapter** or **Power** page showing detected wattage.
2. **BIOS detects the adapter but Windows 11 does not:** the charger is fine — the fault is Windows-side (AC adapter driver or EC state). Reinstall the battery drivers per the [charger detection guide](/articles/troubleshoot-laptop-charger-not-detected/).
3. **BIOS shows Unknown or nothing:** the firmware rejects the adapter — check for a damaged ID pin, wrong wattage, or non-genuine charger, especially on Dell and Lenovo business models.
4. Back in Windows 11, run **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Power** > **Run** and apply its recommendations.
5. Re-test after the troubleshooter. It occasionally clears stuck power configurations that mimic charger failure.
6. Triple confirmation rule: if the multimeter, the USB-C meter, and the BIOS all disagree with Windows, trust the hardware readings — Windows' reporting layer is the liar, not the charger.

## Closing

Charger testing is elimination in the right order: glance, measure in software, measure in hardware, substitute. Most chargers condemn themselves by Fix 2 — the powercfg numbers do not lie. And when the charger passes every test, you have done something valuable: ruled out the cheapest part, so whatever comes next (port, EC, battery) gets your full attention instead of your wallet's first guess.
