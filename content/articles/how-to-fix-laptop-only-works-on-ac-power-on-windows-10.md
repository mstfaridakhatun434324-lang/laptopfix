---
title: "Windows 10 Laptop Dies When Unplugged? How to Fix It"
slug: how-to-fix-laptop-only-works-on-ac-power-on-windows-10
date: 2026-09-25
categories: ["battery"]
tags: ["windows 10", "dies when unplugged", "ac power only", "dead battery", "battery not detected"]
description: "Unplug your Windows 10 laptop and it dies instantly. Here's how to tell a dead battery from a software problem — and fix it."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-on-ac-power-on-windows-10.webp"
faqs:
  - q: "Why does my Windows 10 laptop shut off the moment I unplug it?"
    a: "Because the battery isn't delivering any power — it's either fully worn out, not detected by Windows, or physically disconnected. The laptop runs fine on AC because the adapter powers it directly. A battery report and a BIOS check will tell you which situation you're in."
  - q: "My battery shows 100% but the laptop dies when unplugged. How?"
    a: "The percentage can lie. A worn battery's voltage collapses the instant a real load hits it, so Windows shows a full charge right up until the machine dies. This is classic end-of-life behavior — the battery report's full charge capacity will confirm it."
  - q: "Can I replace the battery myself on an older Windows 10 laptop?"
    a: "Many Windows 10-era laptops have removable batteries with a simple latch — those take seconds to swap. For internal batteries, you'll need to open the bottom panel. Check a teardown guide for your exact model and disconnect AC power first."
  - q: "Will a factory reset fix a laptop that only works plugged in?"
    a: "Almost certainly not. This is a hardware-level symptom — the battery delivers zero power. A reset only helps in the rare case where driver corruption hides a healthy battery, and reinstalling the battery drivers in Device Manager achieves the same thing in two minutes."
---

There's a special kind of disappointment in a laptop that works perfectly — as long as you never move it. Unplug the charger to walk to the couch and it's dead before you take three steps. On Windows 10 machines, which tend to be a few years old now, this is usually simple battery old age. But "usually" isn't "always," and replacing a battery only to discover it was a driver problem is an expensive mistake.

So let's do this properly: quick checks to rule out the free fixes, then an honest assessment of the battery, then the replacement decision with real numbers behind it.

## Why this happens

- **Normal battery aging.** Most Windows 10 laptops are 4+ years old — right in the window where batteries give up.
- **Voltage collapse under load.** Worn cells show a fake full charge, then the voltage craters the moment the charger disconnects.
- **Driver corruption hiding a good battery.** Less common, but Windows updates can break battery detection.
- **Loose internal connector.** Years of heat cycles and the odd drop work connectors loose.
- **Deep discharge from storage.** A laptop left in a drawer at 0% for a year may never wake its battery again.
- **Swollen battery disconnected by protection circuits.** The system cuts off a swelling battery for safety.
- **Wrong power plan masking the issue.** High Performance on AC hides how little the battery can actually do.

## How to fix it

Work through these in order — the free checks first, the verdict second, the wallet last.

### Fix 1: Read the battery report

This is the single most informative step. Do it before anything else.

1. Right-click **Start** and open **Windows PowerShell (Admin)**.
2. Run `powercfg /batteryreport` and open the HTML file it creates.
3. Find **Design Capacity** and **Full Charge Capacity**. If full charge capacity is a small fraction of design — or the report fails to generate battery data at all — you're looking at dead cells.
4. Check **Cycle Count** if shown. Anything over 500–800 cycles on a consumer battery is well into borrowed time.
5. Look at recent history: a long gradual decline means natural aging; an abrupt cliff means cell failure. Either way, the fix is the same — but it helps to know.
6. If the report shows healthy capacity yet the laptop still dies unplugged, keep going — you've got one of the interesting cases.

### Fix 2: Check whether Windows even sees the battery

A battery Windows can't see can't power anything, even if the cells are fine.

1. Press **Win + X**, open **Device Manager**, and expand **Batteries**.
2. Missing entries, or a battery icon with a red X in the taskbar, means detection failure.
3. Right-click each battery entry and uninstall it, then shut down fully, unplug for 30 seconds, reconnect, and boot. Windows reinstalls the drivers.
4. If the battery appears after this and holds a charge, you just saved yourself the cost of a replacement.
5. If Device Manager shows the battery fine but unplugging still kills the machine instantly, the cells can't sustain a load — back to the report in Fix 1 for confirmation. For the broader detection problem, see our [battery not detected guide](/articles/laptop-battery-not-detected-windows-11/).

### Fix 3: Look in the BIOS

The BIOS sees hardware without Windows' opinions getting in the way.

1. Reboot and press **F2**, **Del**, or **F10** (brand-dependent) to enter setup.
2. Find the battery information page — most BIOS versions show charge level and health status.
3. Battery present and healthy in BIOS but dead in Windows? Driver or OS issue — revisit Fix 2 and consider a BIOS update.
4. Battery missing or flagged as failed in BIOS? Hardware problem, full stop. No Windows reinstall will fix it.
5. Some BIOS versions also show a **Battery Health** percentage — under 40% here means replacement time regardless of what Windows claims.

### Fix 4: Try the long trickle charge

Batteries stored at zero for months can enter a protection lockout. Sometimes patience revives them.

1. With the laptop powered off, plug in the original adapter.
2. Leave it completely alone for 6–8 hours — overnight is perfect. Don't boot it to "check"; some controllers only trickle-charge while off.
3. In the morning, boot on AC, then unplug and see what happens.
4. Even if it revives, treat the battery as suspect — run the Fix 1 report again and expect reduced capacity. A revived battery is a borrowed-time battery.

### Fix 5: Reseat the battery

For removable batteries this takes ten seconds; for internal ones, only attempt if you're comfortable with a screwdriver.

1. Power off, unplug everything.
2. **Removable:** slide the latches, pull the battery, check the contacts for corrosion, and click it firmly back in.
3. **Internal:** open the bottom panel, unplug the battery connector from the motherboard, inspect it, and reconnect firmly.
4. Check for swelling while you're in there — a puffy battery is a replace-immediately situation, not a reseat situation.
5. Boot on AC and check detection. A loose connector that now reads properly may just need a calibration cycle to behave.

### Fix 6: Rule out the charger as a contributor

A weak adapter can mask battery problems by never actually charging the battery properly.

1. Confirm you're using the original wattage adapter — the rating is on the brick.
2. If the battery never really charged because the adapter was underpowered, the "dead battery" might partly be a "never-charged battery."
3. Test with the correct adapter for a full charge cycle before declaring the battery dead.
4. Watch the charging LED: if it never indicates a full charge after hours, that corroborates the battery report.

### Fix 7: Replace the battery with the right part

When the report shows dead cells and nothing above helped, it's time.

1. Get the exact battery part number — it's printed on the battery itself, and it's more reliable than the laptop model name.
2. Buy genuine or from a reputable third-party brand. Ultra-cheap batteries are a safety gamble and often lie about capacity.
3. **Removable:** swap it in seconds, charge to 100%, done.
4. **Internal:** follow a teardown guide for your exact model, disconnect AC first, and be gentle with ribbon cables.
5. After installing, do a full calibration: charge to 100%, drain to hibernate, rest a few hours, recharge uninterrupted.
6. For the bigger picture on detection issues, our [battery health check guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) and [Microsoft's Windows support](https://support.microsoft.com/en-us/windows) cover the diagnostic tools in more depth.

## Closing

On a Windows 10 laptop, "dies when unplugged" is usually the battery's retirement announcement — but the report, the BIOS check, and the driver reinstall exist to catch the exceptions before you spend money. Five minutes of diagnosis beats a wrongly ordered battery every time.
