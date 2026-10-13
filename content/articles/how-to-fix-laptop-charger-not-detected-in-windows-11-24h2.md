---
title: "Laptop Charger Not Detected in Windows 11 24H2: How to Fix It"
slug: how-to-fix-laptop-charger-not-detected-in-windows-11-24h2
date: 2026-09-26
categories: ["battery"]
tags: ["charger not detected", "windows 11 24h2", "ac adapter"]
description: "Windows 11 24H2 not detecting your laptop charger? Fix the AC adapter detection problem with these 7 steps, from driver resets to BIOS updates."
thumbnail: "/images/thumbs/how-to-fix-laptop-charger-not-detected-in-windows-11-24h2.webp"
faqs:
  - q: "Why does Windows 11 24H2 say my charger is not detected?"
    a: "The 24H2 update can corrupt the Microsoft AC Adapter driver or break its handshake with the laptop's firmware. Physical causes matter too: a damaged adapter cable, a worn charging port, or an underpowered third-party charger. Start with the driver reset below, then check the hardware."
  - q: "How do I know if the problem is Windows or the charger?"
    a: "Check the charger's LED and the laptop's charging LED — if neither lights up, suspect the hardware. Also try charging while the laptop is powered off or in the BIOS screen. If it charges there but not in Windows, the problem is in Windows. If it doesn't charge anywhere, it's the adapter, cable, or port."
  - q: "Will reinstalling Windows fix a charger detection problem?"
    a: "It can, if the cause is deep driver or system corruption that SFC and DISM can't repair. But try the driver reset, BIOS update, and hardware tests first — a reinstall is a last resort that costs hours. Most charger detection issues resolve without one."
  - q: "Does Windows 11 24H2 have known charging bugs?"
    a: "Major Windows updates sometimes ship with power management regressions affecting specific hardware combinations. If your charger worked fine before 24H2 and broke immediately after, check your manufacturer's support site for a BIOS or chipset update that addresses 24H2 compatibility — these usually appear within weeks."
---

You plug in the charger and... nothing. No charging LED, no plug icon on the battery, no "plugged in" message. Windows 11 24H2 behaves as if the charger doesn't exist, and the battery just keeps draining. If this started right after the 24H2 update, you're probably dealing with a driver or firmware handshake problem rather than dead hardware — but you have to rule out the hardware first, because the symptoms look identical.

This guide is ordered the way a repair tech would work: quick physical checks, then the Windows-side fixes that address 24H2 specifically, then firmware, then the deeper repairs.

## Why this happens

- **Corrupted AC adapter driver** — the 24H2 update can break the Microsoft AC Adapter driver entry in Device Manager.
- **Damaged adapter or cable** — a severed wire inside the cable or a failed brick means no power reaches the laptop at all.
- **Worn charging port** — a loose DC jack or dirty USB-C port breaks the physical connection.
- **Firmware mismatch** — the embedded controller's charging handshake can break after a major Windows update until the BIOS is updated.
- **Third-party charger rejection** — some laptops refuse unrecognized adapters more aggressively after firmware updates.
- **Power state corruption** — a stuck power state in the controller can make the system blind to the adapter until reset.

## How to fix it

Work through these in order.

### Fix 1: Verify the charger hardware is alive

Before blaming Windows, confirm the charger itself works. This takes two minutes and prevents hours of wasted software troubleshooting.

1. Check the adapter brick for an LED — if it has one, it should light when plugged into the wall. No light means no power, so try a different outlet first.
2. Inspect the full cable length for damage, and check the laptop's charging port for debris or bent pins.
3. For USB-C charging, try a different USB-C cable — cables fail far more often than bricks, and many only support data, not full-wattage charging.
4. If possible, test your charger on another compatible laptop. If it's dead there too, replace it and you're done.

### Fix 2: Reset the embedded controller

A stuck power state can make the laptop ignore a perfectly good charger. This reset is harmless and surprisingly effective.

1. Shut the laptop down completely and unplug the charger.
2. Remove the battery if it's removable. Otherwise, press the pinhole reset button on the bottom cover with a paperclip for 10 seconds if your model has one.
3. Hold the power button for 30 seconds.
4. Plug the charger back in before powering on, and watch for the charging LED. If it lights now, the controller was stuck.

### Fix 3: Reinstall the AC adapter and battery drivers

This is the core 24H2 fix. The update is known to corrupt the driver entries that tell Windows an adapter is connected.

1. Right-click **Start** and open **Device Manager**.
2. Expand **Batteries**. Right-click **Microsoft AC Adapter** and choose **Uninstall device**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and uninstall it too.
4. Click **Action** > **Scan for hardware changes**. Windows reinstalls both drivers fresh.
5. Restart with the charger connected. In most 24H2 cases, detection returns immediately after this reset.

### Fix 4: Check for a 24H2-specific chipset or BIOS update

When a major Windows version breaks hardware detection, manufacturers respond with firmware updates. Yours may already be waiting.

1. Open `msinfo32` and note your **BIOS Version/Date**.
2. Visit your manufacturer's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/), or [Microsoft's Windows support](https://support.microsoft.com/en-us/windows) for Surface devices — and search your exact model.
3. Install any **BIOS**, **chipset**, or **power management** updates marked as 24H2-compatible, with the AC adapter connected.
4. Restart and test charger detection from a cold boot, not just a restart.

### Fix 5: Run the hardware troubleshooter and system file checks

If the driver reset didn't stick, underlying system corruption may be breaking redetection.

1. Open **Command Prompt** as administrator and run `sfc /scannow`.
2. If it reports unfixable damage, run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
3. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** and run the **Power** troubleshooter.
4. Restart and check whether Windows now sees the adapter. Related detection problems, like a [battery not detected at all](/articles/laptop-battery-not-detected-windows-11/), follow a similar repair path — and if the battery vanished after an update specifically, see [no battery detected after a Windows update](/articles/how-to-fix-no-battery-detected-after-windows-update-in-windows-11-24h2/).

### Fix 6: Test charging outside of Windows

This step tells you definitively whether Windows is the problem.

1. Power the laptop off completely and plug in the charger. Watch the charging LED for 5 minutes.
2. If the LED lights and the battery charges while off, the hardware is fine — the fault is in Windows. Revisit Fixes 3–5, and consider updating or reinstalling the chipset driver from the manufacturer.
3. Enter the BIOS setup (usually **F2** or **Del**) and leave the laptop there on AC power. Many BIOS screens show adapter wattage — check that it reads correctly.
4. If there's no charging in BIOS or while powered off either, the adapter, port, or motherboard charging circuit is at fault — that's hardware service, not software.

### Fix 7: Refresh Windows as a last resort

If the charger works on other machines, charges while powered off, but Windows 11 still won't detect it after every fix above, the OS installation itself is damaged.

1. Back up your files to an external drive or cloud storage.
2. Go to **Settings** > **System** > **Recovery** and choose **Reset this PC**, keeping your files.
3. After the reset, install the manufacturer's chipset and power drivers before anything else, then test the charger.
4. A clean driver stack resolves the stubborn cases where corruption survived SFC and DISM. It's a big step, but it's definitive.

## Closing

A charger that Windows 11 24H2 can't see is usually a driver casualty of the update, not a hardware failure — but always verify the hardware first so you don't chase a software ghost. Reset the drivers, update the firmware, and test outside Windows; that sequence will tell you exactly where the break is.
