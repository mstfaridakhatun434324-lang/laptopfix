---
title: "How to Fix USB-C PD Charging Not Working on Your AI Laptop"
slug: usb-c-pd-charging-not-working-ai-laptop
date: 2026-10-23
categories: ["ai-pc"]
tags: ["usb-c", "pd charging", "ai laptop", "battery", "charger", "troubleshooting"]
description: "Fix USB-C PD charging failures on AI laptops — wattage and cable checks, port and dock isolation, EC firmware updates, and battery driver resets that work."
thumbnail: "/images/thumbs/usb-c-pd-charging-not-working-ai-laptop.webp"
faqs:
  - q: "Why does my AI laptop say 'plugged in' but the battery keeps draining?"
    a: "The charger is delivering power, but less than the laptop is consuming. This happens with underpowered chargers, weak pass-through docks, or heavy workloads like video rendering that outpace a 45W adapter. Use the OEM wattage or higher and connect directly to the wall to confirm."
  - q: "Can I charge my Copilot+ laptop with a phone charger?"
    a: "A phone charger will usually be recognized but charges extremely slowly or not at all, because Snapdragon laptops negotiate specific USB Power Delivery profiles (typically 65W at 20V). For daily use, get a PD charger rated at or above your laptop's specified wattage."
  - q: "Does it matter which USB-C port I use for charging?"
    a: "Yes. On many AI laptops only one or two USB-C ports support PD input; the others are data-only or DisplayPort-out. Check the small charging icon next to the port in your manual, and test every port before assuming the charger is dead."
  - q: "Charging worked yesterday and stopped after an update — what broke?"
    a: "Firmware and embedded-controller updates can reset PD negotiation tables or re-enable battery protection modes. Reinstall the OEM chipset and EC firmware, then do a full EC reset (unplug, hold the power button 30 seconds) to force a fresh PD handshake."
---

You plug in the USB-C charger and nothing happens — no LED, no charging icon, or Windows reports "plugged in" while the battery percentage keeps falling. The charger works on your phone and the port works for a flash drive, but the power refuses to flow.

On AI laptops and Copilot+ PCs, USB-C PD charging is a negotiation, not a dumb power feed. The charger and the laptop's embedded controller handshake over the USB Power Delivery protocol to agree on voltage and wattage, and Snapdragon boards are pickier about that handshake than older Intel machines — they expect specific PD profiles (usually 20V rails), and a charger that "worked on the last laptop" can fail negotiation here. Docks and hubs complicate it further by skimming watts off the top.

This guide gives you six fixes in technician order: matching the wattage and cable first, then isolating ports and docks, then testing whether the problem lives in Windows or the hardware, and finally fixing the firmware and drivers that run the PD handshake. Check the charging icon after each step.

## Why this happens

- **Underpowered or non-PD charger:** AI laptops typically need 65W or more over USB PD. A 30W phone brick or an old barrel-charger-with-adapter cannot satisfy the negotiation, so the laptop refuses the charge entirely.
- **Cable not rated for the wattage:** USB-C cables are not all equal — pushing more than 60W requires an e-marker chip in the cable. A cheap data cable silently caps the handshake at a wattage the laptop rejects.
- **Dock or hub skimming power:** Pass-through charging on docks loses 10–15W to the dock itself. A 65W adapter through a hungry dock may deliver only 45W to the laptop — below its minimum.
- **Wrong USB-C port:** Many Copilot+ laptops have one charging-capable port and one or two data/display-only ports. Plugging into the wrong one gives you data and zero watts.
- **Stale EC or PD-controller firmware:** The embedded controller runs the PD handshake. Old firmware mis-negotiates with newer GaN chargers, and the failure looks exactly like a dead charger.
- **Battery protection or driver state:** After overheating or deep discharge, the battery controller can latch into a protective state and refuse charge until reset; a corrupted Windows battery driver produces the same symptom.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Match the wattage with a real PD charger

Before suspecting the laptop, confirm the charger can actually feed it. Underpowered charging drops Windows into battery saver and throttles background AI work — which is also when [Copilot in Excel starts misbehaving](/articles/copilot-in-excel-not-working/) on battery.

1. Check the wattage printed on your OEM charger or in the laptop's specs — most AI laptops want 65W minimum, some 90W or 100W.
2. Read the fine print on your USB-C charger: it must list **USB Power Delivery** and a 20V output at enough amps to reach your laptop's wattage.
3. Test with the original OEM charger first, even if you prefer a third-party one — this isolates the charger variable completely.
4. Watch for the charging LED and the battery icon change within 10 seconds of plugging in; note exactly what happens for the next steps.
5. If the OEM brick charges but your travel charger does not, the travel charger fails PD negotiation — replace it with a PD-rated unit at the right wattage.

### Fix 2: Swap the cable and try every port

Cables and ports are the next cheapest variables. A cable that charges a phone at 25W can still be the reason a laptop gets nothing, because the laptop demands a higher PD profile the cable cannot signal.

1. Use a USB-C cable explicitly rated for 100W (5A) with an e-marker chip — if yours is unmarked or came with a phone, assume it is the problem.
2. Try every USB-C port on the laptop, waiting 10 seconds on each; look for the small battery/plug icon printed next to the charging-capable port.
3. Wiggle the connector gently while watching the icon — a port that only charges at an angle is a hardware issue.
4. If one port charges and another does not, you have found your charging port; mark it mentally and stop blaming the charger.
5. Retest the original charger-and-cable combo on the good port, so you carry a known-working baseline into the firmware steps.

### Fix 3: Bypass the dock and check the real power budget

Docks are the classic invisible thief. Test the raw wall-to-laptop path, and while you are at it, sanity-check whether your workload simply outruns the charger.

1. Unplug every dock, hub, and adapter — connect the charger directly to the laptop's charging port and a wall outlet, not a power strip.
2. If direct charging works, the dock's pass-through is the bottleneck: check its rated wattage and subtract 10–15W for the dock's own draw.
3. With the direct connection, open **Settings > System > Power & battery** and confirm the status reads "Plugged in, charging" with a rising percentage.
4. Now consider the workload budget: heavy sustained loads can outpace a weak adapter. Video editing is the worst case — [CapCut on ARM Windows laptops](/articles/capcut-arm-windows-laptop-issues/) can pull more than a 45W adapter delivers.
5. The NPU adds its own draw during calls — [Studio Effects in Discord calls](/articles/studio-effects-discord-calls/) measurably increases consumption, so test charging with the camera off.

### Fix 4: Test charging outside Windows (BIOS check)

This is the great divider: if the laptop charges in the BIOS/UEFI screen, the hardware and PD handshake are fine and Windows is the problem. If it does not charge there either, the issue is hardware or firmware.

1. Shut down fully, then power on into the BIOS/UEFI (usually **F2**, **F12**, or **Del**).
2. Plug in the charger while in the BIOS and watch the charging LED and any battery status shown on the BIOS screen.
3. Leave it for five minutes: if the reported battery percentage climbs, the PD handshake and charging circuit are healthy.
4. If it charges in BIOS but not in Windows, skip to Fix 6 — the Windows battery driver is your target, and firmware is innocent.
5. If it does not charge even in BIOS, continue to Fix 5; no Windows setting can fix a handshake that fails before the OS loads.

### Fix 5: Update the EC, PD-controller, and chipset firmware

When the handshake itself fails — no charge in BIOS, or charging that worked until a firmware update — the embedded controller and PD-controller firmware need attention. Snapdragon boards get PD negotiation fixes in platform firmware more often than people expect.

1. On your maker's support page ([Dell](https://www.dell.com/support), HP, or Lenovo), download the latest BIOS/UEFI, embedded-controller, and chipset driver packages for your exact model.
2. Install the BIOS/EC update first on AC power if possible, and do not interrupt it.
3. Install the Qualcomm chipset driver package next, then run Windows Update to catch any newer PD-related drivers.
4. After updating, unplug the charger, hold the power button for a full 30 seconds (EC reset), then plug back in — this forces a fresh PD handshake with the new firmware.
5. Test with the direct wall connection before reintroducing docks, so a dock problem cannot masquerade as a firmware failure.

### Fix 6: Reset the Windows battery driver and read the battery report

If the hardware charges fine in BIOS, the Windows side is lying to you — usually a wedged battery driver or a protection latch. Reset the driver stack and let Windows rediscover the battery.

1. Open **Device Manager > Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device** (do not uninstall the AC adapter entry).
2. Shut down, unplug the charger, hold the power button 30 seconds, then boot with the charger connected — Windows reinstalls a clean battery driver.
3. Run `powercfg /batteryreport` in an elevated Command Prompt and compare design capacity against full charge capacity.
4. If full charge capacity is far below design capacity, the battery is worn and may refuse charge as a safety measure — see the [Windows support pages](https://support.microsoft.com/en-us/windows) for next steps.
5. If the report looks healthy and charging now works, reintroduce your dock one device at a time; the moment charging breaks again, you have found the power thief.

## Closing

USB-C PD charging failures are a negotiation problem far more often than a dead battery: the wrong wattage, the wrong cable, a power-hungry dock, or stale EC firmware. Match the wattage, test the direct wall path, divide BIOS from Windows, and reset the driver.
