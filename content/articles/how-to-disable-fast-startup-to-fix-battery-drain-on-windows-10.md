---
title: "Turn Off Fast Startup to Fix Battery Drain on Windows 10"
slug: how-to-disable-fast-startup-to-fix-battery-drain-on-windows-10
date: 2026-09-15
categories: ["battery"]
tags: ["fast startup", "battery drain", "windows 10"]
description: "Windows 10 laptop draining overnight while powered off? Turn off Fast Startup the right way and verify the drain is gone."
thumbnail: "/images/thumbs/how-to-disable-fast-startup-to-fix-battery-drain-on-windows-10.webp"
faqs:
  - q: "Where is the Fast Startup setting in Windows 10?"
    a: "In Control Panel under Hardware and Sound, then Power Options, then Choose what the power buttons do. Click Change settings that are currently unavailable, then uncheck Turn on fast startup. It's not in the Settings app."
  - q: "Why does my Windows 10 laptop lose battery when shut down?"
    a: "Fast Startup performs a hybrid shutdown that leaves hardware partially powered instead of fully off. USB devices stay energized, wake timers can fire, and drivers never fully unload — all of which sip battery overnight while the laptop appears dead."
  - q: "Is it safe to disable Fast Startup on Windows 10?"
    a: "Completely safe. It only changes shutdown behavior from hybrid to full. Sleep, hibernate, and restart work identically. The only cost is a few extra seconds of boot time on SSD-equipped machines."
  - q: "Fast Startup keeps turning itself back on. How do I stop that?"
    a: "Feature updates are the usual culprit — recheck the setting after each one. For a permanent solution, disable hibernation with powercfg /hibernate off in an elevated Command Prompt, which removes Fast Startup entirely."
---
The math doesn't add up: you shut down at 75%, the laptop sat untouched for ten hours, and now it's at 58%. Nothing was running — except something was. Windows 10's Fast Startup means "Shut down" doesn't actually shut the machine down. It performs a hybrid shutdown that leaves the hardware in a powered twilight state, and that state drinks battery all night.

The fix is quick, but doing it right means verifying the behavior actually changed. Here's the complete procedure.

## Why this happens

- **Hybrid shutdown keeps hardware energized.** The kernel session is saved to disk while devices stay in low-power states rather than off.
- **USB ports remain powered.** Connected peripherals, docks, and even phone-charging ports draw current all night.
- **Wake timers fire in the hybrid state.** Scheduled maintenance can partially wake the system.
- **Driver bugs persist across hybrid shutdowns.** A driver holding a device awake never gets the full reset a true shutdown provides.
- **Feature updates re-enable the setting.** Every major Windows 10 update is a chance for Fast Startup to switch itself back on.
- **Hiberfil.sys grows stale.** Corruption in the hibernation file can cause odd power behavior on the next boot.
- **Dual-boot complications.** Fast Startup locks the NTFS partitions, which also affects Linux dual-boot setups.

## How to fix it

Work through these in order.

### Fix 1: Disable Fast Startup properly

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do**.
3. Click **Change settings that are currently unavailable** — this needs administrator rights.
4. Uncheck **Turn on fast startup (recommended)**.
5. Click **Save changes**.

If the option isn't listed, hibernation is off: run `powercfg /hibernate on` from an elevated Command Prompt and come back. Note that on some corporate-managed machines, group policy controls this setting and the checkbox will be grayed out — that's an IT department conversation.

### Fix 2: Prove the drain is gone with an overnight test

1. Charge to a round number like 80%, unplug everything including USB devices.
2. Shut down via **Start > Power > Shut down**.
3. Leave it overnight — 8+ hours.
4. Power on and check the percentage before opening anything.

Losing 0–2% is normal self-discharge. If you previously lost 10–20% and now lose almost nothing, Fast Startup was the culprit and you're done. If significant drain persists, keep going — something else is awake.

### Fix 3: Disable wake timers

1. Go to **Control Panel > Hardware and Sound > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **Sleep > Allow wake timers** → set **On battery** to **Disable**.
3. Open an elevated Command Prompt and list armed timers:

```
powercfg /waketimers
```

4. For offenders, open **Task Scheduler** (**Win + R** → `taskschd.msc`), find the task, open **Properties > Conditions**, and clear **Wake the computer to run this task**.

Windows 10's automatic maintenance is a frequent overnight waker — reschedule it to daytime hours in **Control Panel > Security and Maintenance > Maintenance**.

### Fix 4: Stop USB devices from sipping power

1. In **Device Manager**, expand **Universal Serial Bus controllers**.
2. For each **USB Root Hub**, open **Properties > Power Management** and check **Allow the computer to turn off this device to save power**.
3. Check your BIOS for **USB PowerShare** / **Always On USB** / **USB charging in off state** and disable it.

That glowing mouse or dock left plugged in overnight is a small but real load multiplied across hours.

### Fix 5: Refresh the hibernation file

A corrupt hiberfil.sys can cause strange hybrid-shutdown behavior even with the setting on — and cleaning it up is good hygiene when disabling:

1. Elevated Command Prompt:

```
powercfg /hibernate off
```

2. Restart the computer.
3. If you use hibernate and want it back:

```
powercfg /hibernate on
```

4. Then repeat Fix 1 to ensure Fast Startup stays off.

Toggling hibernation off deletes and recreates hiberfil.sys cleanly, which also recovers disk space equal to a chunk of your RAM.

### Fix 6: Update chipset and BIOS

Old firmware can mishandle the S5 (soft-off) power state:

1. Get the latest **chipset** and **BIOS** from your manufacturer's support site.
2. Install with AC power connected.

Firmware updates often include fixes for excessive power draw in shutdown states. After updating, recheck the Fix 1 checkbox — Windows updates bundled with driver updates can flip it back.

### Fix 7: Audit what's actually running at shutdown

If drain persists with Fast Startup off and timers disabled, something is genuinely not shutting down:

1. Before shutting down, open **Task Manager > Startup** and disable everything non-essential as a test.
2. Check **Settings > Privacy > Background apps** and turn off the ones you don't need.
3. Run a sleep study for data:

```
powercfg /sleepstudy
```

Even though it's named for sleep, the report reveals power draw in low-power states. For persistent overnight losses, our guide on [overnight drain while off](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-step-by-step/) continues the hunt. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document these powercfg tools as the standard diagnostic set.

### Fix 8: Enable the BIOS deep-power-off option

Many BIOS implementations have a setting that forces the deepest shutdown state regardless of what Windows requests — look for **ErP Ready**, **Deep Sleep Control**, or similar under **Power Management** in BIOS setup, and disable **Power On by PCI-E** / **Wake on LAN** while you're there. Enabling **ErP** (the EU energy regulation mode) forces the machine to cut nearly all standby power in the S5 shutdown state, which overrides any residual hybrid-shutdown behavior Windows might still attempt. The tradeoff: USB wake and wake-on-LAN stop working, and boot takes a couple of seconds longer — acceptable for a laptop that travels. After enabling it, shut down and confirm no LEDs stay lit and no USB devices receive power. Combine this with Fix 1 and overnight drain should be effectively zero. If you still see losses above 2–3%, the remaining draw is almost certainly battery self-discharge — verify with a [battery health check](/articles/how-to-check-battery-health-on-windows-11-laptop/).

## Closing

On Windows 10, overnight drain while "off" is Fast Startup's signature move — the laptop was never truly off. Disable it, verify with the overnight test, then clear out wake timers and USB power. When a shut-down laptop starts acting like it's actually shut down, the mystery is solved.
