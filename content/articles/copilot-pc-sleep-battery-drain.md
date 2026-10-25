---
title: "Copilot+ PC Losing Battery in Sleep? Fix the Drain"
slug: "copilot-pc-sleep-battery-drain"
date: 2026-10-25
categories: ["ai-pc"]
tags: ["copilot plus pc", "sleep", "battery drain", "windows 11", "modern standby", "ai pc"]
description: "Does your Copilot+ PC lose 20 percent overnight in sleep? Learn why sleep battery drain happens and how to stop it with proven settings fixes."
thumbnail: "/images/thumbs/copilot-pc-sleep-battery-drain.webp"
faqs:
  - q: "How much battery should a Copilot+ PC lose in sleep?"
    a: >
      A healthy Copilot+ laptop should lose only 1 to 3 percent overnight in Modern Standby. Losing 10 percent or more means something is waking the machine or keeping it active while the lid is closed.
  - q: "Is Modern Standby worse than old sleep mode?"
    a: >
      Modern Standby keeps the PC semi-awake so it can fetch mail and updates, which uses slightly more power than classic sleep. When it works properly the drain is small, but a misbehaving app or device can keep it fully awake.
  - q: "Does turning off Wi-Fi in sleep help?"
    a: >
      Yes, disconnecting Wi-Fi during standby often cuts drain dramatically, because it stops background sync, updates, and wake timers from running all night. Windows has a dedicated setting for this.
  - q: "Can a USB device drain battery in sleep?"
    a: >
      Absolutely. Mice, dongles, and docks can wake the PC repeatedly or draw power through the port. Unplugging peripherals before closing the lid is a quick test that often reveals the culprit.
---

You close the lid at night with 60 percent battery and wake up to 30 percent, or worse, a dead laptop. Sleep battery drain is one of the most common complaints on Copilot+ PCs, and it is especially annoying because the machine is supposed to be doing nothing. The drain is real, measurable, and usually fixable without new hardware.

Copilot+ laptops use Modern Standby, a sleep state that keeps the system lightly connected so it can wake instantly and fetch updates. That design is convenient, but it gives every app, driver, and peripheral a chance to wake the machine. When one of them misbehaves, the laptop spends the night half-awake, burning battery as if it were in use. Finding that one wake source is the whole game.

Some drains come from apps you would not suspect. Design tools running under emulation, for example, can keep background processes alive in sleep, so check how [Figma on ARM Windows](/articles/figma-arm-windows-issues/) behaves on your machine. A [Copilot key remapping that does not work](/articles/copilot-key-remapping-not-working/) can also signal configuration drift that affects power behavior. For related sleep behavior in other apps, our guide to [Click to Do in the Edge PDF reader](/articles/click-to-do-edge-pdf-reader/) shows how background features interact with standby.

## Why this happens

- **Wake timers:** Scheduled tasks, updates, and apps can wake the PC from sleep repeatedly through the night.
- **Connected standby networking:** Wi-Fi stays active in Modern Standby, letting mail, cloud sync, and updates run while closed.
- **Misbehaving devices:** USB mice, dongles, and docks can wake the machine or draw power continuously.
- **Background apps:** Cloud storage, chat apps, and AI features like Recall may keep working during standby.
- **Outdated drivers:** Old network, chipset, or BIOS drivers can fail to enter low-power states properly.
- **Fast Startup interaction:** Hybrid shutdown states can confuse sleep behavior after updates.
- **Battery calibration drift:** Windows may report battery inaccurately after months without a full charge cycle.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find what woke your PC

1. Open Command Prompt as administrator.
2. Run `powercfg /sleepstudy` to generate a sleep report.
3. Open the HTML report it creates and look for sessions with high drain.
4. Run `powercfg /lastwake` to see the most recent wake source.
5. Note the device or app named, since the rest of the fixes target it directly.

### Fix 2: Disconnect Wi-Fi during standby

1. Open Settings, then System, then Power & battery.
2. Find the option for network connectivity in standby and set it to Disconnect.
3. Alternatively, turn on Airplane mode before closing the lid for a night as a test.
4. Compare overnight drain with Wi-Fi disconnected versus connected.
5. If drain drops sharply, leave the disconnect setting on permanently.

### Fix 3: Stop devices from waking the PC

1. Open Device Manager and expand Network adapters, Mice, and USB controllers.
2. Right-click each device, choose Properties, then the Power Management tab.
3. Uncheck "Allow this device to wake the computer" for mice and dongles.
4. Unplug USB peripherals before sleep for one night to confirm the effect.
5. Keep wake permission only for devices you genuinely need, like the power button.

### Fix 4: Disable wake timers and background apps

1. Open Settings, then System, then Power & battery, and turn off background apps you do not need.
2. Open Task Scheduler and disable non-essential wake timers under Microsoft, then Windows, then UpdateOrchestrator.
3. In Power Options, set "Allow wake timers" to Disable for both battery and plugged-in states.
4. Pause Windows Update overnight by setting active hours to cover the night.
5. Test one full night of sleep and measure the percentage lost.

### Fix 5: Update BIOS and drivers

1. Visit your manufacturer's support site for your exact model.
2. Install the latest BIOS, chipset, and network drivers.
3. Open Windows Update and install any optional driver updates.
4. Restart the laptop and let it complete one full sleep and wake cycle.
5. Run `powercfg /sleepstudy` again to confirm drain sessions have shrunk.

### Fix 6: Use hibernate instead of sleep for long breaks

1. Open Settings, then System, then Power & battery.
2. Set the laptop to hibernate after 60 minutes of sleep on battery.
3. Or enable hibernate as the lid-close action for overnight use.
4. Test overnight drain with hibernate; it should be near zero.
5. If sleep still drains fast but hibernate works, keep hibernate as your overnight default.

For official Windows power guidance, see [Microsoft Support for Windows](https://support.microsoft.com/en-us/windows) and the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) for reinstall or repair options.

### Fix 7: Audit scheduled tasks and Store app updates

Beyond devices and network settings, scheduled tasks are a hidden source of overnight wake-ups that many users never check. Windows maintenance, application updaters, antivirus scans, and cloud tools can all schedule themselves to run at night, and each one wakes the machine from standby, runs for a while, and sometimes fails to let it return to deep sleep. Store apps are a particular culprit because they can update silently overnight and hold the system awake while downloading. Auditing these schedules takes a few minutes and often reveals a task you did not know existed, set to run at exactly the time your battery starts draining.

1. Open Task Scheduler and browse the task library for tasks scheduled between midnight and morning.
2. Look for updater, maintenance, and scan tasks from third-party apps and disable their wake permission.
3. Open the Microsoft Store, go to Settings, and turn off automatic app updates temporarily for one test night.
4. Check your antivirus settings for a scheduled full scan and move it to a daytime hour.
5. Review cloud storage apps for scheduled sync or backup jobs and set them to manual overnight.
6. After changing schedules, run a fresh sleep study for one night and confirm the number of wake events has dropped.

## Closing

Overnight battery drain feels like a hardware flaw, but it is usually one wake source or one setting. Run the sleep study, cut standby networking, tame wake-capable devices, and update drivers, and most Copilot+ laptops go from losing a quarter of their battery overnight to losing almost nothing. If drain persists after all of that, a battery health report is worth running before you assume the battery itself is worn out.
