---
title: "Change the Power Plan to Best Performance on Windows 10"
slug: how-to-change-power-plan-to-best-performance-on-windows-10
date: 2026-10-11
categories: ["performance"]
tags: ["power plan", "best performance", "windows 10", "power settings", "cpu performance"]
description: "Switch your Windows 10 laptop to the Best Performance power plan correctly: unlock hidden plans, set per-scenario defaults, and avoid battery pitfalls."
thumbnail: "/images/thumbs/how-to-change-power-plan-to-best-performance-on-windows-10.webp"
faqs:
  - q: "What does the Best Performance power plan actually change?"
    a: "It raises the minimum processor state so the CPU doesn't park at low clocks, disables aggressive USB and PCIe link-state power saving, keeps the hard disk from spinning down quickly, and prevents the display and system from sleeping aggressively. The net effect is higher sustained clocks and snappier response, at the cost of more heat, fan noise, and battery drain."
  - q: "Will Best Performance damage my laptop or battery?"
    a: "No. It doesn't overclock anything — it only allows the CPU and GPU to use their factory-rated speeds instead of holding them back. Thermals stay within the manufacturer's design limits because built-in throttling still protects the hardware. The real costs are shorter battery life and more fan noise, which is why most people use it plugged in and switch to Balanced on battery."
  - q: "Why don't I see the High Performance plan in Windows 10?"
    a: "On many modern laptops, especially with Modern Standby, Windows 10 hides the classic High Performance plan and shows only Balanced, sometimes with a slider instead. You can restore it with a single command (powercfg -duplicatescheme) or create an equivalent custom plan. The slider's 'Best performance' end achieves the same practical result on most machines."
  - q: "Should I use Best Performance all the time?"
    a: "Not necessarily. Use it when plugged in and doing demanding work — gaming, video editing, compiling — where sustained clocks matter. On battery, Balanced usually gives a better experience because Best Performance can drain the battery 20 to 40 percent faster for little perceptible gain in light tasks. Set per-power-source defaults so Windows switches automatically."
---

Windows 10 decides how aggressively your laptop chases performance versus battery life, and its default choice — Balanced — is a compromise that doesn't suit everyone. If your CPU feels hesitant to boost, if games stutter until the system "wakes up," or if you simply want the machine running at its rated speed when plugged in, switching to a Best Performance configuration is the fix. It takes two minutes, it's reversible, and it changes nothing about your files or apps.

But there's a right way to do it: restore the proper plan (it's hidden on many laptops), configure it sensibly per power source, and understand the tradeoffs so you get speed without pointless battery drain. Here's the complete walkthrough.

## Why this happens

- **Balanced throttles boost behavior:** The default plan parks the CPU at low clocks and ramps slowly, adding latency to bursty workloads.
- **The High Performance plan is hidden:** Modern Standby laptops hide the classic plan, leaving users stuck with Balanced and a slider.
- **Per-source settings confusion:** Windows can use different plans on battery vs. plugged in; a plan set only for one source surprises users on the other.
- **OEM power utilities override Windows:** Manufacturer tools (Dell Power Manager, Lenovo Vantage, Armoury Crate) can silently override the Windows plan.
- **Minimum processor state too low:** Balanced sets minimum CPU to 5%, causing the "wake-up stutter" in games and heavy apps.
- **Aggressive link-state power management:** PCIe and USB power saving add latency to GPUs and peripherals under Balanced.
- **Sleep and disk timeouts interrupting work:** Short idle timeouts spin down disks and sleep the system during pauses in long tasks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check your current plan and the slider

Before changing anything, know where you stand. Click the battery icon in the taskbar — Windows 10 shows a performance slider on many laptops. Note its position for both battery and plugged-in states (unplug to check the battery position). Then open **Control Panel → Power Options** to see the underlying plan. This baseline tells you whether you're actually on Balanced or whether an OEM utility has already customized things.

1. Click the taskbar battery icon; note the slider position (plugged in).
2. Unplug; note the slider position on battery.
3. Open **Control Panel → Hardware and Sound → Power Options**; note the selected plan.
4. If an OEM power tool is installed, check its profile too — it may override Windows.

### Fix 2: Restore the hidden High Performance plan

If Power Options shows only Balanced (and maybe Power Saver), restore the classic High Performance scheme with one command. Open **Command Prompt as administrator** and run `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61`. The High Performance plan appears immediately in Power Options. This is Microsoft's own documented scheme GUID — safe and reversible.

1. Open **Command Prompt as administrator**.
2. Run `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61`.
3. Open **Power Options**; select **High Performance**.
4. Verify the slider (if present) reflects the change.

### Fix 3: Create a custom plan if you prefer control

If you want Best Performance behavior with your own timeouts, create a custom plan instead: **Power Options → Create a power plan → High performance** as the base, name it (e.g., "Plugged-in Performance"), and adjust display/disk/sleep timeouts to taste. A custom plan survives Windows updates better than modified built-ins and documents your intent.

1. **Power Options → Create a power plan**.
2. Base it on **High performance**; name it clearly.
3. Set display, sleep, and disk timeouts for your use.
4. Save and select it. For the Windows 11 24H2 equivalent path, see [best performance in Windows 11 24H2](/articles/how-to-change-power-plan-to-best-performance-in-windows-11-24h2/).

### Fix 4: Set per-power-source behavior

The plan should differ by power source. In **Power Options → Change plan settings → Change advanced power settings**, configure: **Processor power management → Minimum processor state** to 100% on plugged in (5% on battery), and review **PCI Express → Link State Power Management** (Off plugged in, Moderate on battery). This gives full speed at the desk and sane battery life on the go — automatically.

1. **Change advanced power settings** for your performance plan.
2. **Processor power management → Minimum processor state**: 100% plugged in, 5% on battery.
3. **PCI Express → Link State Power Management**: Off plugged in.
4. Apply; test both plugged in and on battery.

### Fix 5: Reconcile OEM power utilities

Manufacturer tools can override Windows plans silently. Open yours (Dell Power Manager, Lenovo Vantage, HP, ASUS Armoury Crate, Acer) and set its thermal/power profile to match your intent — e.g., Dell's "Ultra Performance" or Lenovo's "Best Performance" mode. If the OEM tool fights your Windows plan, pick one authority: either drive everything from the OEM tool or set the OEM tool to a neutral profile and manage via Windows.

1. Open the OEM power/thermal utility.
2. Set its profile to the performance equivalent.
3. Verify in Task Manager that CPU boosts as expected under load.
4. If conflicts persist, choose one control point and neutralize the other.

### Fix 6: Verify the change with real measurements

Don't trust the setting — verify the behavior. Plug in, open Task Manager → **Performance → CPU**, and run a heavy task (a game, a render, a benchmark). Watch the clock speed: on Best Performance it should jump to boost clocks immediately and hold them. Compare against Balanced behavior from Fix 1. If clocks still won't rise, the limiter is elsewhere — thermals, BIOS settings, or a charger issue — not the power plan.

1. Plug in; open Task Manager → **Performance → CPU**.
2. Run a sustained heavy workload.
3. Confirm immediate boost to high clocks and sustained speeds.
4. If capped, investigate thermals/BIOS/charger rather than the plan. Microsoft's power guidance: [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 7: Build the battery-friendly counterpart

Best Performance on battery is usually wasteful. Create (or keep) a Balanced plan for battery use and let Windows switch automatically — it does this by default when you configure per-source settings in Fix 4. Additionally, in **Settings → System → Battery**, configure **Battery saver** to engage at 20–30% so the laptop protects itself. The result: full speed at the desk, sensible endurance away from it, zero manual toggling.

1. Keep a Balanced plan configured for **On battery**.
2. Verify automatic switching: unplug and check Power Options.
3. Set **Battery saver** threshold in Settings → System → Battery.
4. Confirm the step-by-step idle-RAM angle too if battery life is the goal: [idle RAM step by step](/articles/how-to-fix-windows-11-using-too-much-ram-idle-step-by-step/).

## Closing

Switching Windows 10 to Best Performance is a two-minute change with real consequences: snappier boosts, sustained clocks, and the end of wake-up stutter — paid for in battery life and fan noise. Do it deliberately: restore the real plan, configure per power source, reconcile the OEM utility, and verify with actual clock speeds. Set up once, and the laptop simply behaves the way its hardware was built to behave.
