---
title: "USB-C PD Charger Charging Slowly on Windows 10? Fix the Slow Charge"
slug: how-to-fix-usb-c-pd-charger-charging-slowly-on-windows-10
date: 2026-09-02
categories: ["battery"]
tags: ["usb-c", "pd charger", "slow charging", "windows 10"]
description: "Slow USB-C charging on a Windows 10 laptop is usually a charger, cable, or port problem. Follow this step-by-step diagnosis to get full-speed charging back."
thumbnail: "/images/thumbs/how-to-fix-usb-c-pd-charger-charging-slowly-on-windows-10.webp"
faqs:
  - q: "Why does Windows 10 show my laptop as plugged in but not really charging?"
    a: "Windows 10 reports 'plugged in' whenever any power source is detected, even a weak 15W phone charger. If the charger can't cover the laptop's power draw plus charge the battery, you'll see the percentage stall or creep up very slowly. Check the charger's wattage rating against your laptop's original adapter — they should match or the charger should be higher."
  - q: "Can a Windows update cause slow USB-C charging?"
    a: "Yes, occasionally. Updates can replace the USB-C/Thunderbolt controller driver or reset power management settings, which may break the PD power negotiation. If slow charging started right after an update, check Device Manager for the USB-C controller, roll back its driver, and make sure BIOS is current."
  - q: "Is it safe to use a higher-wattage USB-C charger than my laptop needs?"
    a: "Yes. USB-C Power Delivery negotiates — the laptop only draws what it needs. A 100W charger on a 65W laptop is perfectly safe and often charges slightly faster under load because there's headroom. What's unsafe are counterfeit chargers that don't actually implement PD negotiation properly."
  - q: "How do I know if my USB-C cable supports fast charging?"
    a: "Look for printed ratings on the cable jacket like '5A' or '100W'. Cables bundled with phones are usually limited to 60W or less. For reliable laptop charging, use a cable explicitly rated 100W (20V/5A) with an e-marker chip from a reputable brand, and keep it under 2 meters."
---

Your Windows 10 laptop says it's plugged in, the charging light is on, but the battery percentage refuses to climb. With USB-C Power Delivery, "plugged in" and "charging properly" are two very different things — and Windows 10 doesn't do a great job of telling you which one you're getting.

The mechanics of PD charging are identical on Windows 10 and 11; what differs is where you click to check settings. This guide walks you through the hardware checks first (charger, cable, port), then the Windows 10 settings that can quietly strangle your charge rate.

## Why this happens

- **Charger wattage too low:** The most common cause. A laptop that shipped with a 90W adapter will barely charge from a 45W USB-C brick, and a 65W machine crawls on a 30W phone charger.
- **Cable bottleneck:** USB-C cables negotiate power through an e-marker chip. Cheap or phone-bundled cables cap negotiation at 60W, 30W, or even 15W regardless of the brick.
- **Charging through a dock:** USB-C hubs consume 10-15W for themselves and sometimes negotiate a lower contract with the laptop than a direct connection would.
- **Wrong port:** Many laptops designate a single USB-C port for power input. The others are data/display only and won't charge at all, or deliver a token trickle.
- **Manufacturer charge limits:** Lenovo Conservation Mode, ASUS Battery Health Charging, and Dell Adaptive charging intentionally slow charging near their caps to extend battery lifespan.
- **Driver or firmware regression:** A Windows 10 update or an outdated Thunderbolt/USB-C controller driver can break PD negotiation, leaving you stuck on a 15W fallback contract.
- **Hot battery:** The charge controller reduces current when cell temperature is high. A laptop baking on a bed while gaming will charge slowly no matter how good the charger is.

## How to fix it

Work through these in order — the first three solve the vast majority of cases.

### Fix 1: Verify the charger actually meets your laptop's needs

Don't trust the marketing — read the label.

1. Find your laptop's original adapter wattage: it's printed on the old brick (e.g., "Output: 20V ⎓ 3.25A" = 65W) or in the manual.
2. Read the USB-C charger's label the same way. Multiply volts × amps on the highest PD profile to get real wattage.
3. The charger should be **equal to or higher** than the original adapter. A 100W PD charger safely powers any 45W/65W/90W laptop.
4. Be suspicious of ultra-cheap "100W" chargers from unknown brands — many deliver half their claimed rating. USB-IF certified chargers from established brands are worth the premium.
5. Plug the charger straight into a wall outlet for testing, bypassing power strips, and watch the battery percentage for 10 minutes.

### Fix 2: Swap to a proper 100W-rated cable

Even a great charger is useless through a weak cable.

1. Inspect your current cable for printed text. No printing usually means a basic cable — assume 60W max.
2. Phone-box cables are the usual culprit. They're built for 25W phones, not 65W laptops.
3. Replace it with a USB-C to USB-C cable rated **100W / 20V / 5A with e-marker chip**. The packaging will say so explicitly.
4. Avoid cables longer than 2 meters for charging — voltage drop over long cables can cause the laptop to negotiate down.
5. Retest. If the charge rate jumps, you've found it. Keep the good cable as your dedicated laptop cable and label it.

### Fix 3: Use the right port, directly

Port choice matters more than people expect.

1. Examine each USB-C port for a **battery/plug icon** or lightning bolt — the marked port is the charging input on most models.
2. Unplug any dock, hub, or dongle and connect the charger **directly** to the laptop's charging port.
3. On some Dell and HP models, USB-C charging only works when the laptop is asleep or off with certain docks — direct connection avoids all of this.
4. Check the manual if unsure: search the web for "[your model] USB-C charging port location".
5. Give it 15 minutes on the correct port with no hub. If charging is now fast, your dock was eating the wattage — consider a dock with a higher passthrough rating or a dedicated higher-wattage brick for the dock.

### Fix 4: Disable manufacturer charge-limit features temporarily

These features are good for battery longevity but they slow charging by design.

1. **Lenovo:** Open **Lenovo Vantage > Hardware Settings > Power** and turn off **Conservation Mode**.
2. **ASUS:** Open **MyASUS > Customization > Battery Health Charging** and set it to **Full capacity mode**.
3. **Dell:** Open **Dell Power Manager > Battery Information > Settings** and choose **Standard**.
4. **Acer:** Open **Acer Care Center > Battery > Battery Health** and check the charge limit setting.
5. Retest charging speed. You can re-enable these limits later — they're genuinely good for the battery — but confirm they're the cause first. If your battery seems stuck at a limit, our guide on [fixing ASUS battery health charging stuck at 80](/articles/best-way-to-fix-asus-battery-health-charging-stuck-at-80/) goes deeper.

### Fix 5: Check Windows 10 power settings and battery drivers

Windows-side settings can quietly limit charging behavior.

1. Open **Control Panel > Hardware and Sound > Power Options** and select the **Balanced** plan (not Power saver) while testing.
2. Click **Change plan settings > Change advanced power settings**, expand **USB settings > USB selective suspend setting**, and set it to **Disabled** for both battery and plugged in.
3. Open **Device Manager** (right-click **Start**), expand **Batteries**, and uninstall **Microsoft ACPI-Compliant Control Method Battery**, then restart — Windows reinstalls it fresh.
4. In **Device Manager**, expand **Universal Serial Bus controllers** and look for the USB-C/Thunderbolt controller. If it has a yellow warning, update or roll back its driver.
5. Run `powercfg /batteryreport` from an admin Command Prompt and check the charge-rate history to confirm the improvement in numbers, not just feel. Our [battery report walkthrough](/articles/how-to-generate-battery-report-windows-11-powercfg/) explains how to read the charge rate column.

### Fix 6: Rule out heat throttling

A hot battery charges slowly on purpose — it's a safety feature, not a bug.

1. While charging, open **Task Manager** (**Ctrl + Shift + Esc**) and check CPU usage at idle. Anything over 20% sustained means background load is generating heat and consuming charger output.
2. Close heavy applications during a test charge, especially games, video editors, and browsers with dozens of tabs.
3. Make sure vents are unobstructed — lift the laptop on a book or cooling stand, never charge on a pillow or duvet.
4. Blow dust from vents with compressed air (short bursts, can upright).
5. In **Power Options > Advanced settings**, expand **Processor power management > Maximum processor state** and temporarily set **On battery** to 90% — this caps heat generation significantly.
6. If the chassis is consistently hot even at idle, the cooling system may need repasting or fan replacement — a shop job, but worth it for both speed and battery life.

### Fix 7: Update BIOS, chipset, and Thunderbolt drivers

PD negotiation involves firmware. Outdated firmware negotiates badly.

1. Get your exact model and current BIOS version: press **Windows key + R**, type `msinfo32`, press Enter.
2. Download the latest **BIOS**, **chipset driver**, and **Thunderbolt/USB-C driver** from the manufacturer support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
3. Install in this order: chipset → Thunderbolt/USB-C → BIOS. Keep the charger plugged in throughout.
4. During the BIOS update, don't touch anything until the laptop reboots itself.
5. After updating, test with your verified charger + cable + correct port combination.
6. If slow charging persists across two known-good chargers but the original barrel adapter charges fast, the USB-C PD controller may have a hardware fault — contact manufacturer support while under warranty.

## Closing

On Windows 10, slow USB-C charging is a hardware-chain problem far more often than a software one: weak brick, weak cable, wrong port, or a hub skimming wattage. Work the chain from wall to laptop, verify with a battery report, and you'll find the weak link — usually a $20 cable, not a $200 repair.

*Related reading: [generate a battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/), [battery drains while plugged in](/articles/how-to-fix-laptop-battery-drains-while-plugged-in-in-windows-11-24h2/)*
