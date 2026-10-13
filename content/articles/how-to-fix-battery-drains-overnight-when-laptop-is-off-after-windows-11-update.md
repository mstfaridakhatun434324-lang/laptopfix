---
title: "How to Stop Your Laptop Battery Draining Overnight When It's Off"
slug: how-to-fix-battery-drains-overnight-when-laptop-is-off-after-windows-11-update
date: 2026-09-07
categories: ["battery"]
tags: ["overnight drain", "windows 11", "fast startup"]
description: "Laptop loses charge overnight while fully shut down? The usual culprits are Fast Startup, Modern Standby, and USB charging — here's how to stop each one."
thumbnail: "/images/thumbs/how-to-fix-battery-drains-overnight-when-laptop-is-off-after-windows-11-update.webp"
faqs:
  - q: "Should a laptop lose battery when completely shut down?"
    a: "A tiny amount — 1-2% overnight — is normal, since the battery self-discharges and the embedded controller sips power. Losing 10% or more overnight while shut down means something is drawing power that shouldn't be."
  - q: "Does Fast Startup drain the battery?"
    a: "Yes, indirectly. Fast Startup puts the laptop into a deep hibernation-like state rather than a true shutdown, and some hardware keeps drawing power in that state. Disabling it gives you a real shutdown with near-zero drain."
  - q: "Can USB ports drain the battery when the laptop is off?"
    a: "Yes. Many laptops keep USB ports powered when off to charge phones — check BIOS for USB PowerShare, Always-On USB, or similar settings and disable them if you don't use that feature."
  - q: "Why did overnight drain start after a Windows update?"
    a: "Updates can re-enable Fast Startup, reset power plans, or change sleep behavior. They can also update the BIOS, which sometimes resets USB charging and wake settings to their defaults."
---
You shut the laptop down at 80% before bed. In the morning it's at 61% — and it was off the entire time. Off should mean off. But on modern Windows laptops, "shut down" often isn't what it used to be, and a Windows 11 update can quietly change the rules underneath you.

The good news: overnight drain while shut down is almost never a bad battery. It's a setting — usually Fast Startup, a powered USB port, or a sleep state masquerading as a shutdown. Each one is a five-minute fix once you know where to look.

## Why this happens

- **Fast Startup isn't a real shutdown.** It logs you out and hibernates the kernel, leaving hardware in a low-power state that still draws current. Updates frequently re-enable it.
- **Modern Standby replaces classic sleep.** Instead of the old S3 sleep, many laptops use S0 Modern Standby, which keeps the system semi-awake — and an update can switch a machine to it.
- **USB ports stay powered when off.** USB PowerShare / Always-On USB keeps charging your phone overnight — from your laptop's battery.
- **Wake timers fire during the night.** Scheduled tasks and updates can wake the machine from sleep states, and a half-awake laptop burns far more than a sleeping one.
- **The battery gauge is lying.** Sometimes the "drain" is just the gauge recalibrating after an update — the charge didn't go anywhere, the estimate changed.
- **A device refuses to suspend.** A USB dongle or peripheral that won't enter low-power mode keeps the whole system from resting properly.

## How to fix it

Work through these in order. Test one night between changes so you know which one worked.

### Fix 1: Turn off Fast Startup for a true shutdown

This is the fix in roughly half of all overnight-drain cases.

1. Open **Control Panel** > **Hardware and Sound** > **Power Options**.
2. Click **Choose what the power buttons do** in the left sidebar.
3. Click **Change settings that are currently unavailable** (admin prompt).
4. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
5. Shut down tonight with **Start** > **Power** > **Shut down** and compare the morning percentage. If Fast Startup was the cause, there's a dedicated [Fast Startup drain walkthrough](/articles/how-to-disable-fast-startup-to-fix-battery-drain-in-windows-11-24h2/) with screenshots.

### Fix 2: Disable USB charging while off

1. Restart into BIOS setup (**F2**/**Del**/**F10** during boot, varies by brand).
2. Look under **Power**, **Advanced**, or **USB** for **USB PowerShare**, **Always On USB**, **USB Charging in S4/S5**, or similar.
3. Disable it. Save and exit.
4. Alternatively, unplug all USB devices before shutting down for the night as a quick test — if drain stops, a powered port was the culprit.

### Fix 3: Check whether it's really shutting down or "modern sleeping"

1. Shut down the laptop, wait 10 seconds, then listen and feel: fans spinning or warmth means it didn't fully shut down.
2. Open **Terminal (Admin)** and run: `powercfg /a` — this lists available sleep states. If **Standby (S0 Low Power Idle)** is listed but S3 isn't, your laptop uses Modern Standby.
3. To force hibernate instead of sleep when you close the lid: **Control Panel** > **Power Options** > **Choose what closing the lid does** > set **On battery** to **Hibernate**.

### Fix 4: Disable wake timers

1. Open **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings**.
2. Expand **Sleep** > **Allow wake timers** and set both **On battery** and **Plugged in** to **Disable**.
3. This stops scheduled tasks and Windows Update from waking the machine at 3 AM. Note this only affects sleep/hibernate states, but combined with Fix 1 it covers the "wasn't really off" scenario.

### Fix 5: Generate a sleep study to catch the thief

If drain persists, get evidence of what's awake.

1. Open **Terminal (Admin)** and run: `powercfg /sleepstudy /output "C:\sleepstudy.html"`.
2. Open the report and look at the overnight hours. Sessions labeled with high drain and an active component (network, USB device, audio) name the culprit.
3. Common finds: a USB receiver that never suspends (unplug it at night), or "Unknown" drain pointing to Modern Standby — in which case hibernate (Fix 3) is the practical answer. Overnight drain on the plain Windows 11 build has its own [step-by-step variant](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-on-windows-11/) if yours isn't update-related.

### Fix 6: Recalibrate to rule out a lying gauge

1. If the "drain" appeared immediately after a Windows 11 update, the gauge may have reset rather than the battery draining.
2. Run one full calibration cycle: 100% charge, drain to auto-shutdown, rest 3-5 hours, recharge uninterrupted to 100%.
3. After calibration, do the overnight test again. If the morning number is now stable, it was the gauge all along.

### Fix 7: Update the BIOS

1. Check your manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) for a BIOS newer than yours.
2. Power-management firmware bugs — especially around S5 shutdown current — are a real thing, and BIOS updates fix them.
3. Install with the charger connected, don't interrupt it, and retest overnight drain after.

### Fix 8: Test with a true shutdown command

Isolate whether Fast Startup is really the culprit with a one-time true shutdown.

1. Instead of the Start menu, press **Windows key + R**, type `shutdown /s /t 0`, and press Enter. This forces a full S5 shutdown, bypassing Fast Startup for that one shutdown.
2. Note the battery percentage, leave the laptop overnight, and check in the morning.
3. If the drain is gone after the `shutdown /s` night but returns with normal Start-menu shutdowns, you've proven Fast Startup is the cause — leave it disabled (Fix 1) permanently.
4. If it drains even after the true shutdown, the draw is happening at the firmware level (USB power, embedded controller) — focus on Fixes 2, 6, and 7 instead of Windows settings.

## Closing

Overnight drain while shut down is a settings problem wearing a battery problem's clothes. Kill Fast Startup, cut power to USB ports, make sure "off" really means off — and one quiet morning you'll find the percentage exactly where you left it. The `shutdown /s` test takes ten seconds and tells you definitively which half of the problem you're fighting.
