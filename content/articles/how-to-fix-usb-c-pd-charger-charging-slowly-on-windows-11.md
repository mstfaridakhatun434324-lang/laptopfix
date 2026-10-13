---
title: "USB-C PD Charger Charging Slowly on Windows 11? Fix the Slow Charge"
slug: how-to-fix-usb-c-pd-charger-charging-slowly-on-windows-11
date: 2026-09-01
categories: ["battery"]
tags: ["usb-c", "pd charger", "slow charging", "power delivery"]
description: "Your USB-C PD charger should charge fast on Windows 11 but doesn't. Here are the real reasons — wrong wattage, bad cable, port limits — and how to fix each."
thumbnail: "/images/thumbs/how-to-fix-usb-c-pd-charger-charging-slowly-on-windows-11.webp"
faqs:
  - q: "Why does my laptop say 'plugged in' but charge very slowly over USB-C?"
    a: "The charger is delivering less wattage than the laptop needs, so Windows throttles the charge rate. Common causes: a phone charger (18-25W) on a laptop that needs 65W, a cable rated for only 60W or data-only USB 2.0 speeds, or charging through a dock that splits power. Match the charger wattage to your laptop's original adapter."
  - q: "Does the USB-C cable matter for charging speed?"
    a: "Absolutely. USB-C cables are not all equal — many cheap cables only carry 60W or lack the e-marker chip needed for 100W+ negotiation. For a 65W laptop you need a cable rated 100W (20V/5A) with an e-marker chip; for 100W+ laptops, a 240W-rated USB-C cable. A 3-foot quality cable from a known brand beats a long no-name one."
  - q: "Can Windows 11 settings slow down USB-C charging?"
    a: "Yes. Battery charge thresholds (like Lenovo Conservation Mode or ASUS Battery Health Charging capped at 60-80%), the 'Best power efficiency' power mode combined with heavy load, and USB selective suspend can all reduce the effective charge rate. Windows also slows charging when the battery is hot to protect the cells."
  - q: "How can I see how fast my laptop is actually charging?"
    a: "Open an admin Command Prompt and run powercfg /batteryreport, then check the recent usage rows for charge rate in mW. Some laptops show 'Slow charger' in Settings > System > Power & battery. Third-party tools like HWiNFO64 show live charge/discharge wattage under the battery sensor section."
---

You plugged in your USB-C charger, the little plug icon appeared, and... the battery percentage barely moves. An hour later you've gained 8%. USB-C Power Delivery is supposed to be the universal fast-charging standard, so when it crawls, something specific is wrong — and it's almost always fixable without buying a new laptop.

Windows 11 won't tell you much beyond "plugged in," which makes this frustrating to diagnose. But slow USB-C charging comes down to a short list: the charger, the cable, the port, or a setting.

## Why this happens

- **Underpowered charger:** A 65W laptop fed by a 30W phone charger will charge at a trickle — or slowly discharge while you work. The charger must meet or exceed the laptop's rated wattage.
- **Low-rated cable:** Many USB-C cables top out at 60W or lack the e-marker chip required for 100W negotiation. The charger and laptop then settle on a low power contract.
- **Wrong port:** On many laptops only one USB-C port supports charging; the other is data-only. Plugging into the wrong one gives you nothing or a token trickle.
- **Hub or dock in the middle:** USB-C hubs and docks reserve 10-15W for themselves. A 65W charger through a hub may deliver only 45-50W to the laptop.
- **Battery charge threshold active:** Lenovo Conservation Mode, ASUS Battery Health Charging, or Dell's charge limits intentionally slow or cap charging to protect battery lifespan.
- **Heat throttling:** Lithium batteries charge slower when hot. Gaming or heavy work while charging raises cell temperature, and the controller dials the charge current down.
- **Worn battery:** A battery with high wear level has higher internal resistance, so it accepts charge more slowly and the controller limits current to stay safe.

## How to fix it

Work through these in order — most slow-charge cases are solved by the first three.

### Fix 1: Match the charger to your laptop's wattage

The single most common cause of slow USB-C charging is a charger that's simply too weak.

1. Flip your laptop over or check the original barrel/AC adapter — note its wattage (usually 45W, 65W, 90W, or 100W+).
2. Read the fine print on your USB-C charger. Phone chargers are typically 18W, 25W, or 30W — far too weak for most laptops.
3. Buy or borrow a USB-C PD charger rated **at or above** your laptop's original wattage. For a 65W laptop, a 65W or 100W PD charger is ideal.
4. Avoid no-name chargers that lie about wattage. Look for USB-IF certification or reputable brands.
5. Plug the charger directly into the wall, not a power strip shared with heaters or monitors, and retest for 15 minutes.

### Fix 2: Use a proper 100W-rated USB-C cable

The cable is the silent killer of fast charging. Even with a 100W brick, a weak cable caps you at 60W or less.

1. Check your cable for printed markings — quality cables print "100W", "5A", or "20V⎓5A" on the jacket.
2. If the cable came with a phone, assume it's limited (most phone cables are 60W max, many are 25W).
3. Get a USB-C to USB-C cable rated **100W (20V/5A) with an e-marker chip**. For laptops needing 100W+, use a 240W-rated cable.
4. Keep it short if you can — 3 feet (1m) cables have less voltage drop than 6-foot ones.
5. Test again and watch the battery percentage over 10 minutes. A proper setup should add roughly 1% every 1-2 minutes on a 50Wh battery.

### Fix 3: Plug into the correct USB-C port

Not every USB-C port on your laptop can take power.

1. Look for a small **plug/battery icon or "PD" marking** next to one of the USB-C ports — that's the charging port.
2. Check your laptop manual (search "[model] which USB-C port charges") — on many ultrabooks only the left-side port supports PD input.
3. If you're charging through a dock or hub, unplug it and connect the charger **directly to the laptop's charging port** as a test.
4. Thunderbolt ports (lightning symbol) generally accept charging; plain USB-C ports with only a "SS" or DisplayPort symbol may not.
5. If your laptop also has a barrel jack, note that some models charge faster from the original barrel adapter than over USB-C — that's by design, not a fault.

### Fix 4: Check for active charge limits

Your laptop might be deliberately slowing charging to protect the battery.

1. **Lenovo:** Open **Lenovo Vantage > Device > Power** and check **Conservation Mode** — turn it off if you need a full fast charge.
2. **ASUS:** Open **MyASUS > Battery Health Charging** — if set to 60% or 80% maximum lifespan mode, charging slows near the cap. Switch to **Full capacity mode** temporarily.
3. **Dell:** Open **Dell Power Manager > Battery Settings** and check for **Standard** vs **Adaptive** vs **Primarily AC Use** — Adaptive can throttle charging.
4. **HP:** Open **HP BIOS** (tap **F10** at boot) or **HP Power Manager** and check **Battery Health Manager** settings.
5. Also check **Settings > System > Power & battery** — if Windows shows a "Slow charger" warning, it confirms the wattage problem from Fix 1.

### Fix 5: Measure the real charge rate with a battery report

Stop guessing — get the actual wattage numbers.

1. Open an admin terminal: right-click **Start > Terminal (Admin)**.
2. Run `powercfg /batteryreport` and open the HTML file from your user folder.
3. Scroll to the recent usage history and look at the **charge rate** column during plugged-in periods.
4. Compare against your charger's rating: a 65W charger should show roughly 40-60W going in while the laptop idles (the rest runs the system).
5. If the report shows charge rates under 15W with a 65W+ charger and proper cable, the issue is the port, a hub, or a failing charger — replace one variable at a time.
6. For live readings, **HWiNFO64** (Sensors-only mode) shows **Charge Rate** under the battery section in real time. Our guide to [generating a battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/) walks through reading every section.

### Fix 6: Cool the laptop down

Heat forces the battery controller to reduce charge current — sometimes dramatically.

1. While charging slowly, check temperatures: open **Task Manager** (**Ctrl + Shift + Esc**) and look at CPU load; idle should be under 15%.
2. Close heavy apps during a test charge — games, video renders, and Chrome with 40 tabs all generate heat and consume most of the charger's output.
3. Lift the rear of the laptop slightly or use a cooling stand so air flows under the chassis.
4. In **Settings > System > Power & battery > Power mode**, select **Best power efficiency** while testing — this reduces heat from the CPU.
5. Retest: a laptop that was thermal-throttling its charge can double its charge rate once it cools. If overheating is a pattern, see [fixing laptop battery overheating](/articles/how-to-fix-laptop-overheating-while-charging-in-windows-11-24h2/).

### Fix 7: Update BIOS and chipset drivers

The USB-C PD negotiation is handled partly in firmware. Old firmware can fail to negotiate the right power contract.

1. Note your model and current BIOS version from **System Information** (`msinfo32`).
2. Download the latest BIOS and chipset drivers from your manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
3. Install chipset drivers first, reboot, then apply the BIOS update with the charger plugged in.
4. After updating, test charging with your known-good charger and cable combo.
5. As a final check, try a different high-wattage PD charger — if two good chargers both charge slowly but the barrel adapter is fast, the USB-C PD controller hardware may be at fault and needs service.

## Closing

Slow USB-C charging is a chain: charger wattage, cable rating, correct port, and no interfering settings. Nine times out of ten it's a phone charger or a phone cable doing a laptop's job — fix those two and your battery percentage will climb the way it should.

*Related reading: [USB-C charging not working at all](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2/), [laptop battery not charging when plugged in](/articles/troubleshoot-laptop-battery-not-charging-when-plugged-in/)*
