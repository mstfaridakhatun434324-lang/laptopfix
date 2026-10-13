---
title: "How to Disable Fast Startup to Fix Battery Drain on a Laptop"
slug: how-to-disable-fast-startup-to-fix-battery-drain-on-laptop
date: 2026-09-23
categories: ["battery"]
tags: ["fast startup", "battery drain", "power options"]
description: "Fast Startup secretly drains laptop batteries. Learn how to disable it properly and stop overnight power loss on Windows 10 and 11."
thumbnail: "/images/thumbs/how-to-disable-fast-startup-to-fix-battery-drain-on-laptop.webp"
faqs:
  - q: "What is Fast Startup and why does it drain the battery?"
    a: "Fast Startup is a hybrid shutdown: it logs you out, then hibernates the Windows kernel instead of fully powering off. Because the system is in a hibernate-like state rather than truly off, hardware and drivers can keep drawing power — and failed hibernation writes can leave the laptop secretly awake."
  - q: "Will disabling Fast Startup make my laptop boot slower?"
    a: "Slightly — expect a few extra seconds on boot, since Windows does a full cold start. On modern laptops with SSDs the difference is usually 5-10 seconds. Most people never notice it in daily use."
  - q: "Does Fast Startup affect hibernate too?"
    a: "Yes. Fast Startup uses the same hiberfil.sys mechanism as hibernate, and the two can interfere — a common symptom is the laptop failing to hibernate properly or waking from what should be a full shutdown. Disabling Fast Startup makes hibernate more reliable."
  - q: "Should I disable Fast Startup on a desktop too?"
    a: "It matters less on desktops since they are always plugged in, but Fast Startup causes its own headaches there: it can lock the disk (blocking dual-boot access) and prevent Windows Update from fully applying. Many technicians disable it everywhere as a matter of habit."
---

Fast Startup sounds like a pure win — faster boots, no downside. But on laptops it has a dirty secret: "shutting down" with Fast Startup on is not really shutting down. Windows hibernates its core instead of powering off, and that half-asleep state is behind a huge share of overnight battery drain complaints on both Windows 10 and 11.

If your laptop loses 5-15% overnight while "off," Fast Startup is suspect number one. Disabling it takes two minutes, costs you a few seconds of boot time, and fixes an entire category of power weirdness. Here is exactly how.

## Why this happens

- **Shutdown is actually hybrid hibernate.** Fast Startup saves the kernel session to hiberfil.sys and powers down — but drivers and firmware do not always settle cleanly.
- **Failed hibernation leaves the laptop awake.** If the hibernate write fails partway, the machine can sit with the screen off but the system running — maximum drain, zero indication.
- **Wake timers fire during the hybrid state.** Scheduled tasks can wake the "shutdown" laptop just like they wake sleep.
- **Drivers keep polling hardware.** Some drivers do not handle the hybrid shutdown correctly and keep devices powered.
- **Dual-boot and update conflicts.** Fast Startup locks the system drive, which can also stall updates that then retry all night.
- **The hibernate file itself can corrupt.** A damaged hiberfil.sys makes every Fast Startup shutdown unreliable.
- **Peripheral firmware keeps USB ports powered.** Docks, external drives, and some USB-C hubs draw power through the night even when the laptop appears off, and Fast Startup's half-awake state makes this worse than a true shutdown.

## How to fix it

Work through these in order — the main toggle first, then the deeper cleanup.

### Fix 1: Disable Fast Startup in Power Options

The core fix. Two minutes, reversible.

1. Open **Control Panel** > **Hardware and Sound** > **Power Options**.
2. Click **Choose what the power buttons do** in the left sidebar.
3. Click **Change settings that are currently unavailable** (requires admin).
4. Under **Shutdown settings**, uncheck **Turn on fast startup (recommended)**.
5. Click **Save changes**.
6. Restart the laptop (not shut down — restart always does a full boot, which clears the old hybrid state).
7. From now on, **Shut down** performs a true full shutdown.

### Fix 2: Verify it actually turned off

The checkbox sometimes lies, especially on managed machines. Confirm with the registry-free method.

1. Open **Terminal (Admin)**.
2. Run `powercfg /a` and check the output.
3. If you see "The hiberfile type does not support hibernation" or hibernate listed as unavailable, something else disabled hibernation entirely — run `powercfg /hibernate on` if you want hibernate available (Fast Startup needs hiberfil.sys to exist, but disabling Fast Startup does not require disabling hibernate).
4. Do a full **Shut down**, wait 30 seconds, then power on and time the boot. A slightly longer boot with the manufacturer's logo confirms a true cold boot.
5. Leave the laptop "off" overnight and check the battery in the morning — this is the real test.

### Fix 3: Do a true full shutdown going forward

Old habits can reintroduce the hybrid state.

1. Remember: with Fast Startup off, **Shut down** is now a real shutdown. No special steps needed.
2. If you ever need to force a full shutdown on someone else's machine (or before this fix), hold **Shift** while clicking **Shut down** — this bypasses Fast Startup for that one shutdown.
3. The command `shutdown /s /t 0` in Terminal also forces a full shutdown regardless of the setting.
4. **Restart** was always a full reboot even with Fast Startup on — useful to know when troubleshooting.

### Fix 4: Clean up the hibernate file

Since Fast Startup used hiberfil.sys, a corrupted file can keep causing trouble.

1. Open **Terminal (Admin)**.
2. Run `powercfg /hibernate off` to delete hiberfil.sys.
3. Restart the laptop.
4. Run `powercfg /hibernate on` to recreate a clean hibernate file (only if you use hibernate — if you never hibernate, leave it off and reclaim the disk space).
5. Test shutdown drain overnight again.

### Fix 5: Fix wake timers and sleep settings too

Fast Startup is often only part of the overnight drain story.

1. Go to **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings**.
2. Expand **Sleep** > **Allow wake timers** and set **On battery** to **Disable**.
3. In **Device Manager**, check **Network adapters** > your Wi-Fi adapter > **Properties** > **Power Management** — uncheck **Allow this device to wake the computer**.
4. These two changes stop the 3 AM wake-ups that drain batteries whether Fast Startup is on or off. Our [hibernate drain guide](/articles/how-to-fix-laptop-battery-drains-in-hibernate-on-windows-11/) covers the full wake-hunting process.

### Fix 6: Check for the deeper drain causes

If disabling Fast Startup helped but drain continues, keep digging.

1. Run `powercfg /sleepstudy` in an admin Terminal after a night of drain and read the report — it names the processes and devices responsible.
2. Run `powercfg /batteryreport` to check whether the battery itself is worn — a dying battery self-discharges faster, and no setting fixes chemistry. See our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/).
3. Disable **USB selective suspend** quirks and unplug peripherals overnight as a test — some docks and dongles keep the USB bus powered.
4. Update the BIOS — manufacturers do fix power management bugs, and the update process is documented on [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) alongside general power troubleshooting.
5. As a final comparison test, shut the laptop down with Fast Startup off for three nights in a row and log the morning percentage each day. Consistent near-zero loss confirms the hybrid shutdown was the culprit; erratic loss points to a remaining wake source or a worn battery.

## Closing

Disabling Fast Startup is one of those fixes that sounds too simple to matter, but it resolves overnight drain for a remarkable number of laptops. You trade a few seconds of boot time for a laptop that is actually off when you shut it off — which is all most people ever wanted from a shutdown button.
