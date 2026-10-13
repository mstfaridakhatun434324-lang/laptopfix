---
title: "Battery Drains Overnight When the Laptop Is Off? What to Do"
slug: what-to-do-if-battery-drains-overnight-when-laptop-is-off
date: 2026-10-02
categories: ["battery"]
tags: ["battery drain", "overnight drain", "powered off"]
description: "Laptop loses charge overnight while completely off? That's not normal. Find the hidden power draw and stop it with these 7 fixes."
thumbnail: "/images/thumbs/what-to-do-if-battery-drains-overnight-when-laptop-is-off.webp"
faqs:
  - q: "Is it normal for a laptop battery to drain when the laptop is off?"
    a: "A tiny drain — 1 to 2% overnight — is normal, since the embedded controller and USB ports can sip power. Losing 10%, 20%, or more overnight while fully shut down is not normal and points to USB PowerShare, Wake-on-LAN, a stuck power state, or a failing battery."
  - q: "What's the difference between sleep drain and off drain?"
    a: "Sleep drain happens in Modern Standby, where the system is semi-awake — that's a software configuration issue. Off drain happens during a full shutdown (S5 state), where almost nothing should be drawing power. Off drain is more likely hardware settings like USB charging ports or a battery that self-discharges."
  - q: "Can a bad battery drain itself when the laptop is off?"
    a: "Yes. Aging lithium-ion cells self-discharge faster, and a damaged battery with internal micro-shorts can lose significant charge sitting idle. If the drain persists with all power-sharing features disabled and the battery is old, self-discharge is the likely cause — a battery report will confirm the wear level."
  - q: "Does Fast Startup cause overnight drain when off?"
    a: "It can contribute. Fast Startup uses a hybrid shutdown that leaves some hardware initialized, and certain devices don't fully power down. Disabling Fast Startup forces a true cold shutdown, which eliminates this as a variable. It's a quick test worth running."
---

Sleep drain is annoying. Off drain is unsettling. You shut the laptop down completely — not sleep, not hibernate, full shutdown — and the next morning 20% of your battery has vanished into thin air. Nothing was running. The screen was black. Where did the power go?

When a laptop is truly off, only a few things can legally draw power: the embedded controller, USB ports configured for device charging, and network adapters listening for wake signals. Plus the battery's own self-discharge. Overnight off-drain means one of those is misbehaving — or the shutdown wasn't as complete as you thought. Let's find it.

## Why this happens

- **USB PowerShare / always-on USB** — ports that charge phones while the laptop is off keep drawing power all night.
- **Wake-on-LAN enabled** — the network adapter stays powered listening for wake packets.
- **Fast Startup hybrid shutdown** — the "shutdown" isn't fully off; devices stay partially initialized.
- **Battery self-discharge** — old or damaged cells lose charge faster sitting idle.
- **Stuck embedded controller** — the EC can fail to enter its lowest power state.
- **Peripherals left connected** — docks and external drives can keep negotiating power with a "sleeping" port.

## How to fix it

Work through these in order.

### Fix 1: Confirm the laptop is actually shutting down

This sounds obvious, but many "off drain" cases turn out to be sleep or hybrid shutdown in disguise.

1. Click **Start** > **Power** > **Shut down** — don't just close the lid. Closing the lid usually sleeps; it doesn't shut down.
2. Wait for all lights and fans to stop completely, which can take 30 seconds with Fast Startup.
3. For one test night, shut down by holding **Shift** while clicking **Shut down** — this forces a full cold shutdown bypassing Fast Startup.
4. If the Shift-shutdown night shows no drain, Fast Startup was your culprit — disable it permanently in Fix 4.

### Fix 2: Disable USB PowerShare and always-on USB

This is the most common real cause of off drain. Many laptops ship with USB ports that stay powered to charge phones — convenient, and a constant overnight leak.

1. Enter the BIOS (usually **F2** or **Del** during boot).
2. Look under **Power**, **Advanced**, or **USB Configuration** for **USB PowerShare**, **Always On USB**, or **USB Charging in S5**.
3. Disable it. The ports will no longer deliver power when the laptop is off.
4. Save, exit, and test overnight. If you actually use the phone-charging feature, you can re-enable it later knowing exactly what it costs — but test with it off first.

### Fix 3: Disable Wake-on-LAN

A network adapter listening for wake signals draws power all night, every night.

1. Open **Device Manager**, expand **Network adapters**.
2. Right-click your Ethernet and Wi-Fi adapters, choose **Properties**, and go to the **Power Management** tab.
3. Uncheck **Allow this device to wake the computer**.
4. On the **Advanced** tab, disable **Wake on Magic Packet**, **Wake on Pattern Match**, and **Shutdown Wake-On-LAN** if present. Unless you remotely wake this laptop on purpose, you lose nothing.

### Fix 4: Turn off Fast Startup

Fast Startup's hybrid shutdown keeps the kernel session hibernated and leaves hardware in a semi-initialized state — not a true power-off.

1. Go to **Control Panel** > **Hardware and Sound** > **Power Options** > **Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and save.
4. Shut down fully and test overnight. The boot will be a few seconds slower, but the shutdown will be real. Our guide to [disable Fast Startup for battery drain](/articles/how-to-disable-fast-startup-to-fix-battery-drain-in-windows-11-24h2/) covers the details.

### Fix 5: Unplug everything and test in isolation

Docks, external drives, and even some chargers can keep power negotiation alive with a shut-down laptop.

1. Shut down, then unplug every peripheral: dock, external drives, USB hubs, HDMI, Ethernet, and the charger itself.
2. Note the battery percentage, leave the laptop alone overnight.
3. Check in the morning. If the drain is gone, reconnect things one at a time across subsequent nights to identify the leech.
4. Pay special attention to USB-C docks — they're the most common peripheral cause because they actively negotiate power delivery even with the host "off."

### Fix 6: Reset the embedded controller

The EC manages power states, and if it fails to drop into its deepest sleep, the laptop sips power all night while appearing off.

1. Shut down and unplug everything, including the charger.
2. Remove the battery if removable, or press the pinhole reset button for 10 seconds.
3. Hold the power button for 30 seconds.
4. Reconnect the charger, boot, then shut down normally and test overnight. A controller that was stuck in a high-power idle state will now shut down cleanly.

### Fix 7: Check for battery self-discharge

If every setting is correct and the drain persists in total isolation, the battery is draining itself — chemistry, not configuration.

1. Charge to 100%, shut down fully, unplug everything.
2. Note the percentage, wait 12+ hours, and check again without booting into Windows if possible (many BIOS screens show battery level).
3. Losing more than 3–4% in this state points to cell self-discharge.
4. Run `powercfg /batteryreport` and check the wear level. A worn battery self-discharges faster, and if wear is high, replacement is the fix. See how to [check your battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/) for the full interpretation. If the drain also happens while the machine is merely asleep rather than off, the [sleep-drain guide](/articles/how-to-fix-laptop-battery-drains-in-sleep-mode-after-windows-11-update/) addresses that separate scenario.

## Closing

Overnight drain while off is never "just how laptops are" — something is drawing power that shouldn't be. USB PowerShare, Wake-on-LAN, and Fast Startup cover the vast majority of cases; the battery itself covers most of the rest. Work the list, test one variable per night, and you'll find your leak.
