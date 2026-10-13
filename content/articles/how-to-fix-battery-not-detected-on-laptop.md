---
title: "Battery Not Detected on Laptop? How to Fix It"
slug: how-to-fix-battery-not-detected-on-laptop
date: 2026-09-02
categories: ["battery"]
tags: ["battery not detected", "no battery", "device manager", "troubleshooting"]
description: "Windows says no battery is detected? Work through the driver, firmware, and hardware fixes that bring a missing battery back."
thumbnail: "/images/thumbs/how-to-fix-battery-not-detected-on-laptop.webp"
faqs:
  - q: "Why does my laptop say no battery is detected?"
    a: "Windows can't communicate with the battery: the battery driver is corrupted, the embedded controller glitched, the battery connector is loose, the battery's controller board failed, or the battery itself is dead. Driver and EC resets fix the software causes; the rest need physical inspection or replacement."
  - q: "How do I fix 'no battery detected' in Device Manager?"
    a: "Open Device Manager, expand Batteries, right-click Microsoft ACPI-Compliant Control Method Battery, choose Uninstall device, then restart — Windows reinstalls it automatically. If the battery still isn't detected, follow with an EC reset (power off, unplug, hold power 60 seconds) and a BIOS update."
  - q: "Can a dead battery show as 'not detected'?"
    a: "Yes. A battery with a failed controller board or completely dead cells may not respond to the system's queries at all, so Windows reports it as missing rather than dead. If software fixes fail and the battery is old, assume the battery itself is the problem."
  - q: "Will my laptop work if no battery is detected?"
    a: "Yes, on AC power — the laptop runs fine off the charger with no battery involved. You just lose the built-in backup: any power interruption means an instant shutdown, so avoid critical unsaved work until it's fixed."
---
"No battery is detected." Your laptop is sitting there with a battery physically inside it, and Windows insists there isn't one. It's a strange message, but it actually narrows things down well: somewhere between the battery's controller chip and Windows, communication has broken.

The causes split cleanly into software (drivers, EC, BIOS) and hardware (connector, controller board, dead battery). We'll clear the software side first — it fixes most cases — then move to hardware.

## Why this happens

- **Corrupted battery driver.** The Microsoft ACPI-Compliant Control Method Battery driver is the translator between Windows and the battery; when it corrupts (often after updates), the battery "disappears."
- **Embedded controller glitch.** The EC manages battery communication at the firmware level; a glitch or protection trip can silence the battery entirely.
- **Loose or corroded connector.** Physical connection problems — common after drops or on aging machines — break the data lines the system uses to detect the battery.
- **Failed battery controller board.** Each battery pack has its own little circuit board; when it dies, the pack can't identify itself to the laptop.
- **Completely dead cells.** A battery degraded past all usefulness may not power its own controller, making it invisible to the system.
- **BIOS/firmware issue.** Outdated or glitched BIOS can fail to enumerate the battery, especially after updates.

## How to fix it

Work through these in order — software before hardware.

### Fix 1: Reinstall the battery driver

The most common fix, taking about two minutes.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
3. Confirm, then **restart** — Windows reinstalls the driver during boot.
4. Check the taskbar battery icon after restart.

### Fix 2: Reset the embedded controller

Clear firmware-level glitches that hide the battery.

1. **Shut down** completely and **unplug** the charger and all peripherals.
2. If the battery is **removable**: take it out, hold the **power button for 30 seconds**, reinsert the battery, plug in, and boot.
3. If the battery is **internal**: with everything unplugged, hold the **power button for 60 seconds**, then plug in and boot.
4. Check **Device Manager > Batteries** for the battery's return.

### Fix 3: Check for the battery in BIOS

Determine whether it's Windows or the hardware that's blind.

1. Restart and enter **BIOS/UEFI** (**F2**, **Del**, or brand-specific key).
2. Look for **battery information** — most Dell, HP, and Lenovo BIOS setups show it.
3. If the **BIOS sees the battery** but Windows doesn't, it's a Windows/driver problem — continue with software fixes.
4. If the **BIOS doesn't see it either**, it's hardware — skip to Fix 5.

### Fix 4: Update BIOS and chipset drivers

Firmware updates repair battery enumeration bugs.

1. Download the latest **BIOS** and **chipset drivers** from your maker's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
2. Install while **plugged into AC power**; don't interrupt the BIOS update.
3. After restarting, check detection in both BIOS and Windows.

### Fix 5: Reseat the battery

For when the connection is the problem.

1. Power off, unplug, and remove the battery if **removable** — inspect contacts for **corrosion, dirt, or bent pins**, clean gently, and reseat firmly.
2. For **internal** batteries: only open the laptop if you're comfortable — verify the battery cable is firmly seated on the motherboard.
3. Check for **swelling** while you're in there — a swollen battery needs replacement per our [safety guide](/articles/how-to-fix-laptop-battery-swelling-reddit/), not reseating.
4. Boot and check detection.

### Fix 6: Test with a known-good battery

The definitive isolation test.

1. If you can borrow a **compatible battery**, install it and check detection.
2. Detected → your battery's controller or cells have failed; replace it.
3. Still not detected → the **motherboard's battery circuitry** is faulty; professional repair is needed.

### Fix 7: Replace the battery

When the evidence points at the pack, act on it.

1. Buy a **genuine replacement** for your exact model — batteries with failed controllers are exactly where cheap knockoffs cause repeat problems.
2. After installing, run a full **calibration cycle** so the gauge learns the new pack.
3. If Windows detects the new battery but it won't hold charge, see our guide on [batteries that won't hold charge](/articles/how-to-fix-laptop-battery-won-t-hold-charge-after-windows-11-update/).

## Closing

"No battery detected" feels dramatic, but the fix is usually mundane — a driver reinstall or EC reset brings the battery back in most cases. The BIOS check (Fix 3) is the key diagnostic fork: BIOS sees it, it's Windows' problem; BIOS doesn't, it's hardware's problem. That one test saves hours of fixing the wrong layer.

There's one scenario worth calling out specifically: the battery that vanishes after a Windows feature update. Updates sometimes install a generic battery driver that doesn't play well with your specific hardware, or they reset firmware-level settings. If your timeline matches an update, prioritize the driver reinstall and BIOS update steps — they're the ones that address update-caused breakage directly, and checking Windows Update for a follow-up driver fix costs nothing. And if the laptop only runs plugged in even after detection is restored, our [AC-only troubleshooting](/articles/how-do-i-fix-laptop-only-works-on-ac-power/) picks up the trail.

One last check that costs nothing: boot into the BIOS setup and leave the laptop there for a few minutes, then check whether the BIOS battery indicator changes or the battery warms slightly. The BIOS talks to the battery without any Windows drivers involved, so any sign of life there confirms the hardware path works and the problem is purely in Windows' driver stack. No sign of life in the BIOS either means the hardware side needs attention — reseat, swap-test, or replace, per the steps above.

And one practical tip for the driver reinstall step: do it with the charger plugged in and the laptop on AC power throughout. The uninstall-and-restart cycle briefly leaves Windows without battery communication, and if the machine is on battery during that window, an already-flaky battery connection can cause a surprise shutdown mid-reinstall. On AC power, the process is completely safe regardless of what the battery is doing.
