---
title: "Laptop Slow to Wake from Sleep on 24H2? Speed It Up"
slug: how-to-fix-laptop-slow-to-wake-from-sleep-in-windows-11-24h2
date: 2026-09-05
categories: ["performance"]
tags: ["slow wake", "sleep", "windows 11 24h2", "resume", "power management"]
description: "Laptop taking forever to wake from sleep after 24H2? Fix slow resume with power, driver, and sleep-state tuning that actually works."
thumbnail: "/images/thumbs/how-to-fix-laptop-slow-to-wake-from-sleep-in-windows-11-24h2.webp"
faqs:
  - q: "Why does my laptop wake slowly after the 24H2 update?"
    a: "The 24H2 update changes power management defaults, reinstalls chipset and graphics drivers with different sleep behavior, and enables deeper sleep states (like Modern Standby refinements) that take longer to exit. It can also re-enable wake timers and background maintenance that run during sleep, so the machine wakes into a backlog of deferred work. Slow resume is the system paying off sleep-related debt plus re-initializing hardware with new drivers."
  - q: "Is slow wake from sleep bad for my laptop?"
    a: "It is not harmful to hardware, but it signals misconfiguration worth fixing: excessive wake timers drain battery during sleep, driver issues during resume can cause instability or black screens, and a machine that takes 30 seconds to wake defeats the purpose of sleep. Fixing slow wake also typically fixes related issues like battery drain during sleep and occasional failure to wake at all."
  - q: "Should I use Hibernate instead of Sleep to avoid slow wake?"
    a: "Hibernate is slower to resume than healthy sleep by design — it reloads the entire RAM image from disk — so it is not a fix for slow wake, it is a different tradeoff. Hibernate shines for multi-day suspension with zero battery drain. If your sleep resume is broken (30+ seconds, black screens), hibernate may feel more reliable, but the right move is fixing sleep itself; a healthy Modern Standby or S3 resume takes 2–5 seconds."
  - q: "Can outdated drivers really cause slow wake?"
    a: "Absolutely — drivers are the most common cause. During resume, Windows re-initializes every device driver in sequence, and a single misbehaving driver (often graphics, network, or chipset) can stall the whole chain for 10–30 seconds. The 24H2 update frequently replaces these drivers with builds that have different resume behavior. Updating chipset, graphics, and network drivers from your laptop maker's site resolves the majority of slow-wake cases."
---

You close the lid, open it later, and... wait. And wait. The screen stays black for ten, twenty, thirty seconds before the lock screen finally appears — if it appears at all. After the Windows 11 24H2 update, slow wake from sleep became one of the most reported laptop annoyances, turning sleep from an instant-on convenience into a coin flip. The machine is not broken; its resume sequence is tangled.

Resume speed is a chain: firmware hands off to Windows, Windows re-initializes every driver in order, and deferred maintenance wakes up demanding attention. 24H2 changed links throughout that chain — new power defaults, new drivers, new sleep-state behavior. This guide works the chain from fastest wins to deepest fixes: wake timers, driver re-initialization, sleep states, and the nuclear options. If sleep is also eating your battery, see [fixing 24H2 battery drain on HP laptops](/articles/how-to-fix-windows-11-24h2-battery-drain-on-hp-laptop/) for the power side; charging quirks are covered in [laptop battery not charging after the 24H2 update](/articles/how-to-fix-laptop-battery-not-charging-after-windows-11-24h2-update/).

## Why this happens

- **Wake timers firing during sleep**: Scheduled tasks and devices with wake permission interrupt sleep constantly, so the machine wakes into a backlog of work.
- **Graphics driver slow to re-initialize**: The 24H2-supplied GPU driver may take 10–30 seconds to bring the display back — the classic black-screen-then-wake symptom.
- **Network adapter resume stall**: Wi-Fi drivers that struggle to reassociate after sleep block the resume chain until they time out.
- **Deep sleep states (Modern Standby) misbehaving**: Refined low-power states in 24H2 save battery but exit slowly when firmware and drivers disagree on the state.
- **Fast Startup interfering with clean resume**: The hybrid shutdown/fast-startup path can leave driver state tangled, slowing the next wake cycle.
- **Deferred Windows maintenance backlog**: Update orchestration, indexing, and telemetry deferred during the day all fire at wake, saturating the just-woken system.
- **USB devices delaying resume**: External drives and hubs must re-enumerate at wake; a slow or failing device stalls everything behind it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable rogue wake timers

The fastest win: stop the machine from doing work during sleep so wake is instant.

1. Open an elevated Command Prompt and run `powercfg /waketimers` to list everything scheduled to wake the PC.
2. Go to **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings** > **Sleep** > **Allow wake timers** and set it to **Disable** (both battery and plugged in).
3. In **Device Manager**, check network adapters and USB devices: **Properties** > **Power Management** > uncheck **Allow this device to wake the computer** except for the one input device you wake with.
4. Run `powercfg /devicequery wake_armed` to see which devices can currently wake the machine — the list should be short.
5. Test sleep/wake twice; wake-timer fixes show results immediately.

### Fix 2: Update chipset, graphics, and network drivers

Resume is a driver parade — one slow marcher delays everyone. Update the three that matter most.

1. Install the latest **chipset driver** from your laptop maker's support site — it governs the sleep/wake power sequencing.
2. Clean-install the current **graphics driver** from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or Intel via the [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
3. Update the **Wi-Fi driver** from the laptop maker or chipmaker — resume stalls on reassociation are extremely common after 24H2.
4. Reboot fully (not fast-startup) after the driver installs so the new drivers initialize from a clean state.
5. Time three wake cycles with a stopwatch; you are aiming for lock screen in under 5 seconds.

### Fix 3: Turn off Fast Startup

Fast Startup's hybrid shutdown saves boot time but leaves driver state half-persistent, which tangles the next resume.

1. Open **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable**.
2. Uncheck **Turn on fast startup (recommended)** and save changes.
3. Shut down fully (not restart), wait 10 seconds, power on, then test a sleep/wake cycle.
4. If wake improves, leave Fast Startup off — on SSD machines the boot-time cost is a second or two.
5. If nothing changes, you can re-enable it; the test costs nothing.

### Fix 4: Tune which sleep states the machine uses

When firmware and Windows disagree about deep sleep, resume suffers. Simplify the negotiation.

1. Run `powercfg /a` in an elevated terminal to see which sleep states your hardware supports (S3, Modern Standby, Hibernate).
2. If **Modern Standby** (S0 low-power idle) is active and wake is slow, try disabling hibernate-based hybrid sleep: `powercfg /h off` as a diagnostic.
3. In advanced power settings > **Sleep** > **Allow hybrid sleep**, set it to **Off** to test pure sleep behavior.
4. Some BIOS setups offer **Sleep state** or **ACPI Suspend Type** options — S3 (if available) resumes faster than Modern Standby on many laptops.
5. Change one variable at a time and time each wake; keep the combination that resumes fastest on your hardware.

### Fix 5: Clear the deferred maintenance backlog

A machine that wakes into an hour of catch-up work feels slow even when resume itself is fine.

1. Open **Control Panel** > **Security and Maintenance** > **Maintenance** > **Change maintenance settings** and schedule **Automatic Maintenance** for a time the laptop is on but idle.
2. Run maintenance manually once: same panel > **Start maintenance** — let it complete fully while plugged in.
3. In **Settings** > **Windows Update** > **Advanced options**, ensure updates are not all pending; install them so post-update tasks stop queuing.
4. Check **Task Scheduler** for third-party tasks set to run at wake or logon and stagger the aggressive ones.
5. After the backlog clears, wake should land on an idle system instead of a busy one.

### Fix 6: Isolate USB devices from the resume path

External devices re-enumerate at wake, and one slow device holds the door for everyone.

1. Unplug all USB devices and test wake speed bare — if it is suddenly fast, a peripheral is the bottleneck.
2. Reconnect one at a time, testing wake after each, to identify the slow enumerator (often older external HDDs or hubs).
3. In **Device Manager** > **USB Root Hub** > **Properties** > **Power Management**, uncheck **Allow the computer to turn off this device to save power** for hubs in the resume path.
4. Update firmware for docks and hubs from their makers — dock firmware is a notorious resume delayer.
5. Consider leaving the worst offender unplugged during travel; use it only at the desk.

### Fix 7: Reset the power plan and check firmware

The deepest layer: corrupted power schemes and old firmware both sabotage resume.

1. Run `powercfg /restoredefaultschemes` in an elevated terminal to wipe any corrupted custom power plans, then re-select **Balanced** or **Best power efficiency**.
2. Check your BIOS version against the laptop maker's support site — 24H2-era BIOS updates frequently include Modern Standby and resume fixes.
3. Update the BIOS on AC power with all apps closed if you are behind; firmware resume fixes are common in the 24H2 timeframe.
4. In BIOS setup, look for **Wake on LAN**, **USB Wake**, or **PowerShare** options and disable the ones you never use.
5. As a final diagnostic, test wake with a clean boot (`msconfig` > **Selective startup**) to rule out third-party interference — if clean-boot wake is fast, re-enable services in halves to find the offender.

## Closing

Slow wake is never one thing — it is a chain of firmware handoff, driver re-initialization, and deferred work, and 24H2 rattled every link. Work from wake timers through drivers to sleep states, timing each change, and the 30-second black screen becomes the 3-second resume sleep was always supposed to be. Your lid is a power button again, not a prayer.
