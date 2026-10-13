---
title: "Disable Fast Startup to Stop Battery Drain on Windows 11"
slug: how-to-disable-fast-startup-to-fix-battery-drain-on-windows-11
date: 2026-09-12
categories: ["battery"]
tags: ["fast startup", "battery drain", "windows 11"]
description: "Laptop losing charge overnight while shut down? Fast Startup is the likely culprit. Disable it correctly with these steps."
thumbnail: "/images/thumbs/how-to-disable-fast-startup-to-fix-battery-drain-on-windows-11.webp"
faqs:
  - q: "What is Fast Startup and why does it drain the battery?"
    a: "Fast Startup is a hybrid shutdown: Windows saves the kernel session to disk instead of fully powering off. The laptop never truly powers down, so components stay partially energized and USB ports may keep supplying power — draining the battery overnight while you think the machine is off."
  - q: "Will disabling Fast Startup make my laptop boot slower?"
    a: "Slightly — typically a few extra seconds on machines with SSDs. On modern NVMe drives the difference is barely noticeable, and it's a small price for a laptop that doesn't lose 10 to 20 percent overnight."
  - q: "Does disabling Fast Startup affect hibernate or sleep?"
    a: "No. Sleep and hibernate work exactly as before. Fast Startup only changes what happens when you click Shut down — with it off, shutdown becomes a true full power-off."
  - q: "Windows keeps re-enabling Fast Startup after updates. What can I do?"
    a: "Major Windows updates sometimes reset the setting. Check it after each feature update via Control Panel, Power Options, Choose what the power buttons do. Alternatively, disable hibernation entirely with powercfg /hibernate off, which removes Fast Startup as a side effect."
---
You shut the laptop down at 80% before bed. In the morning it's at 62% — and it was "off" the whole time. This is the signature symptom of Fast Startup drain. Your laptop wasn't actually off; Windows 11's hybrid shutdown left it in a half-powered state, sipping battery all night while looking completely dead.

Disabling Fast Startup is a two-minute change with an outsized payoff. Here's how to do it properly and verify it worked.

## Why this happens

- **Hybrid shutdown isn't a real shutdown.** Fast Startup saves the kernel to hiberfil.sys and leaves hardware in a low-power state instead of cutting power.
- **USB ports stay powered.** Many laptops keep USB ports energized during hybrid shutdown, powering connected mice, drives, and docks all night.
- **Wake timers can fire.** Scheduled tasks can partially wake the machine from hybrid shutdown, burning significant power.
- **Drivers never fully unload.** A misbehaving driver can keep a device powered through the hybrid state.
- **Updates re-enable it silently.** Feature updates frequently turn Fast Startup back on without telling you.
- **The battery gauge drifts.** Without true power-offs, the fuel gauge rarely recalibrates, compounding the apparent drain.
- **Modern Standby interaction.** On Modern Standby machines, hybrid shutdown can leave the system in network-connected idle rather than off.

## How to fix it

Work through these in order.

### Fix 1: Turn off Fast Startup in Control Panel

The setting lives in the classic Control Panel, not the Settings app:

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do** in the left sidebar.
3. Click **Change settings that are currently unavailable** (requires admin).
4. Uncheck **Turn on fast startup (recommended)**.
5. Click **Save changes**.

If the checkbox is missing entirely, hibernation is disabled on your system — run `powercfg /hibernate on` in an elevated Command Prompt, then repeat these steps.

### Fix 2: Verify shutdown is now a true shutdown

Don't just trust the checkbox — confirm the behavior changed.

1. Shut down the laptop (not restart).
2. Watch the power LED and listen: with Fast Startup off, the machine powers down completely within 15–30 seconds and stays dark.
3. Unplug all USB devices, note the battery percentage, and leave it overnight.
4. Check the percentage in the morning.

A drop of 0–2% overnight is normal (self-discharge). Anything more means something else is still drawing power — continue below. For a deeper overnight-drain investigation, see [fixing overnight drain when the laptop is off](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-on-windows-11/).

### Fix 3: Disable USB selective suspend's evil twin — USB power in shutdown

Some laptops power USB ports even in true shutdown (a BIOS feature for phone charging). If peripherals stay lit after shutdown:

1. Enter BIOS setup (tap **F2**, **F10**, or **Del** at boot depending on brand).
2. Look for **USB PowerShare**, **USB charging in sleep/off**, or **Always On USB** and disable it.
3. Save and exit.

This stops the laptop from acting as an overnight phone charger at its own battery's expense.

### Fix 4: Kill wake timers

Wake timers can pull the machine out of shutdown-adjacent states.

1. Open **Control Panel > Hardware and Sound > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **Sleep > Allow wake timers** and set both **On battery** and **Plugged in** to **Disable**.
3. In an elevated Command Prompt, check what's armed:

```
powercfg /waketimers
```

4. For any task you don't need waking the machine, open **Task Scheduler**, find it, open **Properties > Conditions**, and uncheck **Wake the computer to run this task**.

### Fix 5: Check for the Modern Standby drain

If your laptop supports Modern Standby (S0), "shutdown" behavior gets murky. Check with:

```
powercfg /a
```

If **Standby (S0 Low Power Idle)** is listed as available, your machine may be entering connected idle instead of shutting down. Generate a sleep study to see what's happening:

```
powercfg /sleepstudy /output %USERPROFILE%\Desktop\sleepstudy.html
```

The report shows exactly which components drew power and when. Our guide on [sleep-mode battery drain](/articles/how-to-fix-laptop-battery-drains-in-sleep-mode-after-windows-11-update/) goes deeper on taming S0 drain.

### Fix 6: Update BIOS and chipset drivers

Ancient firmware can mishandle the S4/S5 power states that true shutdown uses.

1. Visit your manufacturer's support site and install the latest **BIOS** and **chipset** drivers.
2. Check for an **Intel Management Engine** update too.

Firmware updates frequently include "improve power consumption in shutdown state" fixes. After updating, re-verify Fix 1's checkbox — BIOS updates don't touch it, but Windows updates sometimes do.

### Fix 7: Consider disabling hibernation entirely

If you never use hibernate and want Fast Startup permanently gone:

```
powercfg /hibernate off
```

This deletes hiberfil.sys (freeing gigabytes of disk space) and removes Fast Startup as a side effect — the checkbox disappears because the underlying mechanism is gone. The tradeoff: no hibernate option and slightly slower shutdowns. For desktop-replacement laptops that live on AC power, it's a clean, permanent fix. Microsoft documents these power options at [support.microsoft.com](https://support.microsoft.com/en-us/windows).

### Fix 8: Audit scheduled tasks that wake or churn the machine

Beyond Windows' own maintenance, manufacturer updaters love to schedule overnight work. Open **Task Scheduler** (`taskschd.msc` via **Win + R**) and browse the **Task Scheduler Library** for entries from Dell, HP, Lenovo, ASUS, or Acer — updaters, telemetry, and "optimization" tasks. For each one you don't need running overnight, open **Properties > Conditions** and uncheck **Wake the computer to run this task**, or disable the task outright if it's pure telemetry. Also check the **Microsoft > Windows > UpdateOrchestrator** tasks — **Reboot** and **Schedule Scan** are notorious wakers. After cleaning house, rerun `powercfg /waketimers` in an elevated Command Prompt to confirm nothing remains armed, then repeat the overnight percentage test from Fix 2.

## Closing

Fast Startup is a boot-time optimization with a battery-life cost, and on laptops the cost usually outweighs the benefit. Turn it off, confirm with an overnight test, then mop up the stragglers — USB power, wake timers, Modern Standby. A laptop that's truly off should lose essentially nothing overnight, and now yours will.
