---
title: "Battery Only Charges When the Laptop Is Off: How to Fix It"
slug: how-to-fix-battery-only-charges-when-laptop-is-off-youtube
date: 2026-10-11
categories: ["battery"]
tags: ["charging issue", "power adapter", "battery"]
description: "Charger works when the laptop is off but not while you're using it? That's a classic power-delivery problem. Diagnose and fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-battery-only-charges-when-laptop-is-off-youtube.webp"
faqs:
  - q: "Why does my laptop only charge when it's turned off?"
    a: "The charger can supply enough power to charge the battery only when the laptop isn't also consuming power. When the machine is on, the CPU, screen, and other components eat the charger's entire output, leaving nothing for the battery. This points to a weak, wrong, or failing charger — or a laptop drawing unusually high power."
  - q: "Is my charger broken if the laptop charges while off?"
    a: "Possibly, but not necessarily. An underpowered third-party charger behaves exactly this way while still being 'functional.' Before replacing it, verify the wattage matches your laptop's requirement and test the original adapter. If the original also fails, the issue is in the laptop."
  - q: "Can a Windows setting cause this?"
    a: "Rarely, but high-performance power plans and background processes that max out the CPU can push power draw high enough to stall charging. Switching to Balanced mode and closing heavy apps is a quick test. The far more common cause is the adapter itself."
  - q: "Should I keep using an underpowered charger?"
    a: "Only as a temporary measure. Running on a charger that can't keep up stresses the charging circuit and can cause instability, throttling, and extra heat. Get an adapter with the correct wattage from the manufacturer as soon as practical."
---

Here's the strange pattern: shut the laptop down, plug it in, and the battery charges fine. Boot into Windows, keep it plugged in, and the percentage flatlines — or even drops. The charger clearly works, so what's going on?

Think of it like a water pipe with two taps. When the laptop is off, all the power flows to the battery. When it's on, the system drinks first and the battery gets whatever is left. If the charger can't supply both, the battery gets nothing.

## Why this happens

- **Underpowered or wrong charger:** The most common cause. A 45W adapter on a laptop that needs 90W can charge a sleeping machine but can't feed a running one.
- **Failing charger losing capacity:** An aging brick may still output some power but no longer its rated wattage, producing exactly this symptom.
- **Laptop drawing excessive power:** Malware, a stuck Windows Update, or a runaway process can pin the CPU at 100%, consuming everything the charger provides.
- **Power plan set to maximum performance:** Best performance mode lets components draw peak power continuously, leaving no headroom for charging.
- **Faulty charging circuit or DC jack:** A loose or damaged power jack can deliver reduced current — enough to trickle-charge when off, not enough under load.
- **USB-C PD negotiation failure:** With USB-C chargers, the laptop and adapter negotiate wattage. A bad cable can cause negotiation to settle at a low wattage like 15W.

## How to fix it

Work through these in order, testing whether the battery percentage climbs while the laptop is on after each step.

### Fix 1: Verify the charger wattage matches your laptop

Start with the simplest explanation.

1. Read the wattage printed on your charger brick (for example, **65W**) and compare it with the requirement in your laptop's manual or on the manufacturer's site.
2. If you're using a third-party or borrowed charger with lower wattage, that's almost certainly the cause — borrow or buy the correct one.
3. Check that you're using the original cable; thin or damaged USB-C cables throttle power delivery.
4. Retest: with the correct charger connected, the battery should charge whether the laptop is on or off.

### Fix 2: Reduce the laptop's power draw

If the charger is correct, find out what's eating all the power.

1. Open **Task Manager** with **Ctrl+Shift+Esc**, sort by **CPU**, and look for processes pinned near 100% — especially updaters, antivirus scans, or unknown apps.
2. End unnecessary heavy tasks, then go to **Settings > System > Power & battery > Power mode** and select **Balanced** or **Best power efficiency**.
3. In **Settings > Windows Update**, check for a stuck update downloading in a loop — pause updates for a week as a test.
4. Run a full scan with **Windows Security > Virus & threat protection** to rule out crypto-miners or other malware hogging the CPU. If background drain is also an issue, see how to stop a [laptop battery draining while plugged in](/articles/how-to-fix-laptop-battery-drains-while-plugged-in-in-windows-11-24h2/).

### Fix 3: Test the charger hardware properly

A charger can be half-dead rather than fully dead.

1. Feel the brick after 15 minutes of use — a failing adapter often runs unusually hot or makes a faint buzzing sound.
2. Wiggle the connector gently at the laptop end; if the charging light flickers, the DC jack or cable is loose.
3. Try a different wall outlet directly (no power strip) to rule out poor mains power.
4. If possible, test your charger on an identical laptop, or a known-good correct-wattage charger on yours — this isolates the fault definitively. For USB-C specific checks, see our [USB-C charging troubleshooting guide](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2/).

### Fix 4: Reset the battery driver and EC

Stale driver or controller state can misreport and mishandle charge current.

1. Open **Device Manager**, expand **Batteries**, and uninstall **Microsoft ACPI-Compliant Control Method Battery**.
2. Shut down, unplug everything, and hold the power button for 30 seconds to drain residual charge and reset the embedded controller.
3. Reconnect the charger (laptop still off) and confirm the charging light behaves normally.
4. Power on and check whether the percentage now climbs while in Windows.

### Fix 5: Check for a manufacturer charge limit

Some utilities pause charging under load by design.

1. Open your manufacturer's app (**Lenovo Vantage**, **MyASUS**, **Dell Power Manager**) and inspect the battery settings.
2. Look for options like **Conservation Mode**, **Battery Health Charging**, or adaptive charging that might restrict charging behavior.
3. Set the battery to standard/full-charge mode temporarily and retest.
4. If a firmware update is available for your model, install it — [Microsoft's support site](https://support.microsoft.com/en-us/windows) and your manufacturer's page both document power-related fixes.

### Fix 6: Inspect the battery's health

A worn battery charges inefficiently and can appear to stall.

1. Run `powercfg /batteryreport` in **Terminal (Admin)** and open the report.
2. Compare **Full Charge Capacity** to **Design Capacity**; heavy wear means the battery accepts charge poorly under load.
3. Look at the usage history for erratic jumps, which suggest failing cells.
4. If wear is severe, a replacement battery resolves the symptom where software cannot.

### Fix 7: Get the DC jack and charging circuit checked

If every charger behaves the same way, the laptop itself is the problem.

1. Note whether the charging LED flickers or changes color when you move the cable — that indicates a loose jack.
2. Check for a burning smell or discoloration around the charging port.
3. Don't attempt to resolder a DC jack yourself unless you're experienced; take it to an authorized service center.
4. Describe the exact symptom — "charges when off, not when on" — since it points the technician straight at power delivery rather than the battery.

## Closing

"Charges only when off" is your charger's way of saying it can't keep up with a running laptop. Nine times out of ten, the correct-wattage adapter — or replacing a dying one — fixes it outright. If the right charger still can't do the job, excessive power draw or a tired charging circuit is next on the suspect list.
