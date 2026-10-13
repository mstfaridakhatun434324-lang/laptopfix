---
title: "Laptop Battery Won't Hold a Charge: What to Do"
slug: how-to-fix-laptop-battery-won-t-hold-charge-reddit
date: 2026-10-10
categories: ["battery"]
tags: ["battery won't hold charge", "battery wear", "battery replacement"]
description: "Battery dies minutes after unplugging? Find out if it's worn cells, a lying gauge, or hidden drain — and what to do next."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-won-t-hold-charge-reddit.webp"
faqs:
  - q: "What does it mean when a battery won't hold a charge?"
    a: "It means the battery can't store usable energy anymore — it may show 100% then die in minutes, or drain absurdly fast under any load. The usual cause is worn-out lithium cells that have lost most of their capacity, though a badly miscalibrated gauge or extreme background drain can mimic the symptom."
  - q: "Can a battery that won't hold charge be fixed?"
    a: "If the cause is gauge miscalibration, yes — a proper calibration cycle can restore accurate reporting and sometimes reveals the battery is healthier than it looked. If the cells are chemically worn (confirmed by a battery report showing very low full charge capacity), no software fix helps; replacement is the only real solution."
  - q: "How long should a laptop battery hold a charge?"
    a: "It depends on the model and workload, but most modern laptops are rated for 6-12 hours of light use when new. If yours delivered 8 hours new and now gives 90 minutes doing the same tasks, that's roughly 20% health remaining. Compare against your own history, not just the spec sheet."
  - q: "Is it worth replacing the battery or buying a new laptop?"
    a: "If the laptop is under 4 years old, meets your performance needs, and a genuine battery costs well under a third of a replacement machine, replacing usually wins. If the laptop is slow, has other failing parts, or the battery costs nearly as much as its resale value, put the money toward a new machine."
---

"Won't hold a charge" is the end-stage battery complaint: you charge it up, unplug, and minutes later it's gasping. Sometimes it even shows a healthy percentage right up until it dies. Before you spend money on a replacement, it's worth confirming the battery is truly done — because a lying gauge or a ravenous background process can fake this exact symptom, and both are free to fix.

Here's how to tell which one you have and what to do about each.

## Why this happens

- **Chemically exhausted cells.** The most common cause: after hundreds of cycles and years of heat, the cells store only a fraction of their original energy.
- **Severe gauge miscalibration.** The controller thinks the battery is full when it's nearly empty (or vice versa), making a mediocre battery look completely dead.
- **Extreme background drain.** Malware, stuck updaters, or runaway processes can burn through even a healthy battery in an hour.
- **One failed cell group.** In series-wired packs, a single dead group collapses the whole pack's usable capacity while the others are fine.
- **Chronic heat damage.** Years of hot operation permanently reduce capacity far faster than cycle count alone would suggest.
- **Deep-discharge damage.** Batteries left at zero for months can lose the ability to ever hold a meaningful charge again.

## How to fix it

Work through these in order — measure first, fix the free things, then make the replacement decision with data.

### Fix 1: Measure true capacity with a battery report

Stop guessing; get the number.

1. Open **Terminal (Admin)** (**Win + X**) and run `powercfg /batteryreport`.
2. Compute health: **Full Charge Capacity ÷ Design Capacity × 100**.
3. Above 70% with terrible runtime: the battery is probably fine — your problem is drain or gauge. Continue with Fix 2.
4. Below 50%: the cells are genuinely exhausted. You can still try calibration (Fix 4), but plan on replacement.
5. Our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) walks through reading the whole report if the numbers confuse you.

### Fix 2: Rule out runaway background drain

A healthy battery can look dead if something's eating it alive.

1. Unplug, wait 5 minutes, open **Task Manager** (**Ctrl + Shift + Esc**), enable **Power usage** and **Power usage trend** columns, and sort.
2. Anything stuck on **Very high** — especially updaters, sync tools, or unknown processes — is suspect. End the task and watch the drain rate.
3. Check **Settings → System → Power & battery → Battery usage** for the 24-hour per-app breakdown.
4. Run a full antivirus scan — crypto miners and malware are classic "battery won't hold charge" mimics.
5. If the drain is mostly during sleep, our [sleep drain guide](/articles/how-to-fix-laptop-battery-drains-in-sleep-mode-after-windows-11-update/) covers Modern Standby culprits.

### Fix 3: Do a controlled runtime test

Measure reality under known conditions.

1. Charge to 100%, unplug, set brightness to 50%, close everything but one browser tab.
2. Time exactly how long until the laptop shuts off. Note the percentage curve — steady decline versus sudden death.
3. Compare to the laptop's original rated life for light use. Under 25% of original = exhausted. 50%+ = worn but the "won't hold charge" feeling may be drain-related.
4. A sudden death from a high percentage (e.g., 40% to dead in minutes) points to cell collapse or gauge error rather than simple wear — our [fast drain troubleshooting](/articles/laptop-battery-drains-fast-windows-11/) covers that pattern.
### Fix 4: Calibrate to reveal the battery's true state

Before declaring it dead, make sure the gauge isn't lying.

1. Charge to 100% and keep it plugged in for 2 hours.
2. Unplug and use the laptop until it shuts itself off completely.
3. Leave it off and unplugged overnight (5+ hours).
4. Charge to 100% in one uninterrupted session without using it.
5. Repeat the cycle once more, then run a fresh `powercfg /batteryreport`.
6. If capacity numbers improved notably or runtime increased, the gauge was the problem — keep a monthly calibration habit. Full details in our [calibration guide](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 5: Check for swelling and heat damage

Physical inspection matters for old packs.

1. Power off and check whether the bottom panel bulges, the trackpad sits raised, or the case rocks on a flat desk.
2. Any swelling means the battery is done — power down, unplug, do not charge it, and arrange a professional replacement. Never puncture or press a swollen pack, and recycle it through e-waste channels, never household trash.
3. Even without swelling, years of hot running permanently cut capacity. If the laptop idles hot, clean the vents with compressed air (powered off) and use it on hard flat surfaces going forward.
### Fix 6: Reduce the load to stretch what remains

If replacement isn't immediate, make the remaining capacity go further.

1. Switch to **Best power efficiency** mode in **Settings → System → Power & battery**.
2. Lower brightness to 40-50%, shorten display timeouts, and disable keyboard backlighting on battery.
3. In **Settings → Apps**, restrict background permissions for apps you don't need mobile.
4. Unplug USB peripherals on battery — external drives and phone charging drain the pack directly.
5. These measures won't fix dead cells, but they can turn 25 unusable minutes into 60 useful ones while you arrange a replacement.

### Fix 7: Replace the battery — or the laptop

Make the call with your data in hand.

1. **Replace the battery** if: health is under 50%, calibration didn't help, the laptop is under 4 years old, and a genuine pack costs well under a third of a new machine.
2. Buy genuine or manufacturer-approved packs — cheap third-party batteries often arrive with worse real capacity than the worn one you're replacing. Check [Dell Support](https://www.dell.com/support) or [Lenovo Support](https://support.lenovo.com/us/en/) for a pack matched to your exact model.
3. Check warranty status with your manufacturer first; premature failure is sometimes covered.
4. **Replace the laptop** if: it's slow, has other failing components, or the battery price approaches the machine's resale value.
5. After installing a new pack, protect it: enable an 80% charge limit if you mostly stay docked ([charge limit guide](/articles/how-to-limit-battery-charge-to-80/)), keep vents clear, and avoid storing it at 100% in heat.

## Closing

A battery that won't hold a charge is usually telling the truth about worn cells — but verify first with a battery report, rule out drain, and calibrate the gauge before spending money. If the numbers confirm exhaustion, replace the pack (or the laptop) with confidence instead of doubt. And treat the new battery better than the old one: cooler, calmer charging habits pay off for years.
