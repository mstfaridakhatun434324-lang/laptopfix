---
title: "How to Fix USB-C Charging Not Working on Your Laptop"
slug: how-to-fix-usb-c-charging-not-working-on-laptop-reddit
date: 2026-09-06
categories: ["battery"]
tags: ["usb-c charging", "power delivery", "charging problems", "battery"]
description: "USB-C plugged in but your laptop won't charge? Learn the real causes — weak chargers, bad cables, dead ports — and fix USB-C charging step by step."
thumbnail: "/images/thumbs/how-to-fix-usb-c-charging-not-working-on-laptop-reddit.webp"
faqs:
  - q: "Why does my laptop say plugged in but not charge over USB-C?"
    a: "The most common reason is a charger that delivers too little wattage or a cable that cannot carry USB Power Delivery. A 45W phone charger, for example, may be detected by a laptop that needs 65W, so Windows shows the charger as connected but refuses to draw power. A damaged cable, a data-only USB-C port, or a failed PD handshake after a firmware glitch can cause the same symptom."
  - q: "Can any USB-C cable charge a laptop?"
    a: "No. Many USB-C cables are wired only for data and low-power charging (phones), and some cheap cables lack the e-marker chip required for currents above 3A. For a laptop, you need a cable rated for USB Power Delivery at your laptop's wattage — typically marked 60W, 100W, or 240W. If your cable came with a phone, assume it is not suitable until you check its rating printed on the connector or packaging."
  - q: "Do all USB-C ports on a laptop support charging?"
    a: "No, and this trips up a lot of people. Some laptops have multiple USB-C ports where only one supports Power Delivery input; the others are data-only. Check the small icons next to each port — a lightning bolt or battery symbol usually marks the charging-capable port — or look in your laptop's manual. Testing every USB-C port with the charger takes thirty seconds and often solves the problem."
  - q: "Can a BIOS update fix USB-C charging?"
    a: "Yes, surprisingly often. USB-C charging depends on Power Delivery negotiation between the charger and the laptop's embedded controller, and manufacturers fix PD handshake bugs in BIOS/EC firmware updates. If charging over USB-C broke right after a Windows or BIOS update, or works with the barrel charger but not USB-C, check your manufacturer's support site for a newer BIOS and install it with the laptop plugged into its original charger."
---

You plug the USB-C cable into your laptop, the little LED lights up or Windows chimes — and then nothing. The battery percentage keeps falling, or Windows says "plugged in" while the charge level never moves. Sometimes the port works fine for a mouse or a dock but flatly refuses to charge.

This is one of the most reported laptop problems because USB-C charging has more moving parts than people expect: the charger, the cable, the port, and the laptop's firmware all have to agree on voltage and wattage before a single watt flows. The good news is that most USB-C charging failures are caused by the first two items on that list, which are easy to test.

## Why this happens

- **Underpowered charger.** A charger that outputs less wattage than your laptop needs (a 45W phone brick on a 90W laptop) may be detected but rejected for charging.
- **Wrong or damaged cable.** Many USB-C cables can't carry laptop-level power. A frayed cable or one missing its e-marker chip will fail PD negotiation.
- **Data-only USB-C port.** On some laptops only one USB-C port accepts charge; the others are data/display only.
- **Dirty or damaged port.** Lint, dust, or a bent pin inside the USB-C port can break the PD negotiation lines while data still passes through fine.
- **PD handshake glitch.** The embedded controller can get stuck after a sleep/wake cycle or firmware update and stop negotiating with chargers.
- **BIOS setting disabled.** Some laptops have a "USB-C Power Delivery" or "Type-C charging" option in BIOS that can be switched off.
- **Failing charging circuitry.** Rare, but a damaged PD controller on the motherboard means no USB-C charger will ever work, even while the barrel jack charges fine.

## How to fix it

Work through these in order, starting with the easiest. Stop when your issue is resolved.

### Fix 1: Match the charger to your laptop's wattage

USB-C chargers are not interchangeable the way old barrel chargers were. Check the wattage printed on your laptop's original charger (usually 65W, 90W, 100W, or higher) and compare it to the charger you're using now.

1. Flip your laptop's original charger over and read the **Output** wattage.
2. Read the wattage printed on the USB-C charger you're trying to use.
3. If it's lower than the original, borrow or buy a charger that meets or exceeds the original wattage.
4. Plug it in and watch the taskbar battery icon for the charging bolt — give it a full 60 seconds.

### Fix 2: Swap in a proper PD-rated cable

The cable matters as much as the brick. Phone cables and bargain cables are the number one cause of "works with data, won't charge" complaints.

1. Look for a wattage rating printed on the cable's connector housing or packaging (60W / 100W / 240W).
2. Use a cable that explicitly mentions **USB Power Delivery (USB PD)** — not just "fast charging".
3. Try a short, thick cable first; long thin cables drop too much voltage for laptop charging.
4. If the laptop charges with a different cable, throw the old one away — intermittent cables can damage ports over time.

### Fix 3: Try every USB-C port on the laptop

Don't assume all ports are equal.

1. Inspect the symbols next to each USB-C port — a **battery or lightning-bolt icon** marks the charging port on many models.
2. Plug the charger into each USB-C port in turn, waiting 30 seconds each time.
3. Note which port (if any) starts charging and use that one going forward.
4. If your manual lists a specific charging port, mark it with a small sticker so you don't forget.

### Fix 4: Clean the USB-C port

Pocket lint is the silent killer of USB-C charging. The port can look fine and still have compressed debris blocking the pins.

1. Power the laptop off completely and unplug everything.
2. Shine a phone flashlight into the port and look for lint or bent contacts.
3. Gently pick out debris with a **wooden or plastic toothpick** — never metal.
4. Blow out loose dust with short bursts from a can of compressed air.
5. Reconnect the charger and test.

### Fix 5: Reset the embedded controller

When PD negotiation gets stuck, a full power drain forces the charging controller to re-initialize.

1. Shut down the laptop and unplug the charger and all USB devices.
2. If the battery is removable, take it out; if not, leave it in.
3. Press and hold the **power button for 30 seconds** to drain residual power.
4. Reconnect only the USB-C charger and power on.
5. Check whether the battery icon now shows charging.

### Fix 6: Update the BIOS and chipset drivers

Manufacturers regularly fix USB-C Power Delivery bugs in firmware updates — especially after major Windows updates.

1. Find your exact model number (on the bottom sticker or via **Settings > System > About**).
2. Go to your manufacturer's support site and download the latest **BIOS** and **chipset** drivers.
3. Install the chipset driver first, then the BIOS, with the original barrel charger connected if you have one.
4. Let the laptop restart fully, then test USB-C charging again.

### Fix 7: Check USB power settings in Windows

Windows can suspend USB ports to save power, which sometimes interferes with charging negotiation.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Change plan settings** next to your active plan, then **Change advanced power settings**.
3. Expand **USB settings > USB selective suspend setting** and set it to **Disabled** for both battery and plugged in.
4. Click **OK**, restart the laptop, and test the charger.

### Fix 8: Generate a battery report and test with the laptop off

This tells you whether the problem is Windows or the hardware.

1. Open **Terminal (Admin)** and run `powercfg /batteryreport`, then open the generated HTML report.
2. Check **Design Capacity** vs **Full Charge Capacity** — a badly worn battery can confuse charging logic.
3. Now shut the laptop down completely and plug in the USB-C charger while it's off.
4. If the charging LED comes on while off but not in Windows, the hardware is fine — focus on drivers and firmware. If it won't charge even when off, the charger, cable, port, or charging circuit is at fault.

If you've worked through all of this and the laptop still won't take a charge over USB-C — but charges fine through its barrel jack — the USB-C PD controller on the motherboard may have failed, and that's a repair-shop job. Also worth reading: our walkthrough for a [laptop battery not charging when plugged in](/articles/how-to-fix-laptop-battery-not-charging-when-plugged-in-step-by-step/) covers the driver and Windows-side fixes in more depth, and our guide to [generating a battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/) shows how to check whether the battery itself is worn out.

For official help, Microsoft's [Windows charging and battery support page](https://support.microsoft.com/en-us/windows) covers the built-in troubleshooters, and if you suspect a firmware issue, [Intel's driver update tool](https://www.intel.com/content/www/us/en/support/detect.html) can catch outdated chipset drivers that affect USB-C negotiation.

## Closing

Nine times out of ten, USB-C charging failure comes down to a weak charger, a data-only cable, or the wrong port — all things you can test in a few minutes without opening the laptop. Work from the wall inward (charger, cable, port, firmware) and you'll usually find the weak link quickly.
