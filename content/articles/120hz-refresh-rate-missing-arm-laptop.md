---
title: "How to Get Back the Missing 120Hz Refresh Rate on Your ARM Laptop"
slug: 120hz-refresh-rate-missing-arm-laptop
date: 2026-10-21
categories: ["ai-pc"]
tags: ["120hz", "refresh rate", "arm laptop", "display settings", "snapdragon", "troubleshooting"]
description: "Restore the missing 120Hz refresh rate on your ARM laptop with step-by-step fixes covering display settings, drivers, cables, HDR conflicts, and power modes."
thumbnail: "/images/thumbs/120hz-refresh-rate-missing-arm-laptop.webp"
faqs:
  - q: "Why is 120Hz missing from my display settings?"
    a: "The most common reasons are an outdated or generic ARM display driver, the laptop running in a battery-saver mode that caps the refresh rate, or an external monitor connected through a cable or dock that cannot carry 120Hz. Check the driver and power mode first."
  - q: "Can a Windows Update remove the 120Hz option?"
    a: "Yes. Windows Update sometimes replaces your laptop maker's validated Adreno driver with a generic one that only exposes 60Hz. Reinstalling the OEM graphics driver from your manufacturer's support page restores the full refresh-rate list."
  - q: "Does HDR block 120Hz on ARM laptops?"
    a: "On some panels and external monitors, enabling HDR at full resolution consumes enough bandwidth that the display drops to 60Hz. If 120Hz vanishes when you toggle HDR on, try a lower resolution or disable HDR to get the higher rate back."
  - q: "Will a USB-C dock limit my refresh rate?"
    a: "Often. Many docks and adapters only pass DisplayPort 1.2 bandwidth, which cannot do 120Hz at high resolutions. Connect the monitor directly with a certified cable to rule out the dock before blaming the laptop."
---

Your Snapdragon laptop's box promised a silky 120Hz panel, but Settings > System > Display > Advanced display shows only 60Hz — or the 120Hz option was there yesterday and vanished after an update. The panel did not downgrade itself; something in the chain between the GPU, the driver, and the display is negotiating a lower rate.

On Windows 11 on ARM Copilot+ PCs, the refresh-rate list is built live from what the driver reports the display can do. A generic driver, a power policy, an HDR setting, or a bandwidth-limited cable can each silently shrink that list — and the fix depends on which link broke.

This guide gives you six fixes in technician order: settings and power checks first, then driver repair, then the cable and monitor layer. Work through them in sequence and recheck Advanced display settings after each step.

## Why this happens

- **Generic or outdated Adreno display driver:** Windows Update can replace your laptop maker's validated ARM graphics driver with a generic one that only exposes 60Hz — the single most common cause of a vanished 120Hz option.
- **Battery saver or power mode capping the rate:** Many Copilot+ laptops drop to 60Hz in battery-saver or "best power efficiency" modes to extend runtime, and the setting that did it is not always obvious.
- **HDR consuming display bandwidth:** Enabling HDR at the panel's full resolution can exceed what the display pipeline supports at 120Hz, so Windows quietly offers only 60Hz while HDR is on.
- **Cable, dock, or adapter bottleneck:** External monitors depend on the whole signal path — a USB-C dock, an old HDMI cable, or a DisplayPort 1.2 adapter caps the rate long before the laptop does.
- **Dynamic refresh rate overriding the manual choice:** Windows 11's Dynamic refresh rate (DRR) feature switches between 60 and 120Hz automatically; when it misreads the situation it can park the display at 60Hz and hide the manual option.
- **Wrong resolution selected:** Some panels only offer 120Hz at their native resolution. A scaled-down resolution picked by mistake can remove the high rate from the list entirely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check power mode and disable battery saver

Before touching drivers, rule out the simplest cause: Windows throttles the panel to 60Hz to save battery. This takes thirty seconds and is the fix more often than people expect — especially if 120Hz vanished while unplugged.

1. Plug in the charger — battery saver never engages on AC power, which isolates the variable instantly.
2. Open **Settings > System > Power & battery** and set **Power mode** to **Best performance** (or Balanced), not Best power efficiency.
3. Turn off **Battery saver** if it is active, including its automatic threshold.
4. Open **Settings > System > Display > Advanced display** and check whether 120Hz reappeared in the **Choose a refresh rate** dropdown.
5. If it did, you are done — the driver and panel were fine all along. Keep the charger handy or accept 60Hz on battery as the tradeoff.

### Fix 2: Pick the right resolution and toggle Dynamic refresh rate

The refresh-rate list depends on the selected resolution, and Dynamic refresh rate can fight your manual choice. Set both deliberately and watch the dropdown repopulate.

1. In **Settings > System > Display**, set **Display resolution** to the panel's native value — the one marked **(Recommended)**.
2. Open **Advanced display** and look at **Choose a refresh rate**: if 120Hz now appears, select it and stop here.
3. If you see **Dynamic** as an option, try selecting **120Hz** explicitly instead of Dynamic — DRR sometimes parks the panel at 60Hz when it misjudges workload.
4. Conversely, if only Dynamic and 60Hz show, disable DRR temporarily and recheck; a stuck DRR state clears on the next step's driver work. Similar display-stack confusion shows up in [Surface Pro 11 recall-related display reports](/articles/microsoft-surface-pro-11-recall-issues/), where firmware and driver interplay decides what the panel offers.
5. Test scrolling and window dragging at 120Hz to confirm the change actually applied, not just that the option appeared.

### Fix 3: Reinstall the OEM Adreno display driver

If 120Hz is still missing at native resolution on AC power, the driver is almost certainly the problem — a generic Microsoft Basic Display Adapter driver or a half-updated Adreno package. This is the same driver hygiene that fixes [missing drivers on Windows on ARM](/articles/drivers-missing-windows-arm/) across the platform.

1. Open **Device Manager > Display adapters** and confirm what is listed — "Microsoft Basic Display Adapter" means no real driver is loaded at all.
2. Find your exact model in **Settings > System > About**, then download the latest graphics/display driver for Windows 11 on ARM from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support.
3. Run the installer as administrator and let it complete without interruption or sleep.
4. Restart when prompted, then recheck **Advanced display** — the full refresh-rate list, including 120Hz, should be back.
5. If Windows Update later swaps the driver again, check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for the supported way to block that specific driver update.

### Fix 4: Disable HDR and test again

HDR is a bandwidth hog. On several Copilot+ panels and many external monitors, the display pipeline cannot sustain full-resolution HDR at 120Hz, so Windows simply removes 120Hz from the options while HDR is enabled.

1. Open **Settings > System > Display > HDR** (or **Use HDR**) and toggle it **Off**.
2. Return to **Advanced display** and check the refresh-rate dropdown immediately — on affected panels 120Hz reappears the moment HDR is off.
3. If it returns, decide which matters more for your use: HDR color or 120Hz motion. There is no way to have both on a bandwidth-limited panel.
4. As a middle ground, try lowering the resolution one step with HDR on and see if 120Hz becomes available — some panels allow the tradeoff.
5. Re-enable HDR only after confirming which combination your panel actually supports.

### Fix 5: Rule out the cable, dock, and monitor (external displays)

For an external monitor stuck at 60Hz, the laptop is rarely the bottleneck — the signal path is. USB-C docks are the usual suspect: many only pass enough bandwidth for 4K60, not 4K120 or 1440p120.

1. Bypass everything: connect the monitor directly to the laptop with a single certified cable (USB-C to DisplayPort, or HDMI 2.1) and recheck the refresh-rate list.
2. If 120Hz appears with the direct connection, your dock or adapter is the limiter — check its specs for the maximum refresh rate per resolution.
3. In the monitor's own on-screen menu, confirm the input is set to the right port version (some monitors default HDMI ports to 1.4 mode, which caps at 60Hz — switch the port to 2.0/2.1 mode).
4. Try a different port on the laptop; on some ARM machines only one USB-C port carries full DisplayPort bandwidth.
5. If the monitor still shows 60Hz direct-connected, the monitor itself may not support 120Hz at that resolution — check its manual before going further.

### Fix 6: Reset the display stack with a clean driver sweep

When nothing above restores 120Hz, the display stack may hold stale EDID or driver state that survives normal reinstalls. A full sweep with a cold boot clears it.

1. Disconnect external monitors, then in Device Manager uninstall the display adapter with **"Attempt to remove the driver for this device"** checked.
2. Hold **Shift** and click **Shut down** for a true cold boot — this forces the firmware to re-enumerate the panel and its EDID from scratch.
3. Power on, reinstall the OEM display driver from Fix 3, and restart again.
4. Reconnect monitors one at a time, checking the refresh-rate list after each. If the panel's capabilities report inconsistently at this point, the same firmware-first approach used for [missing Copilot runtime components](/articles/windows-copilot-runtime-components-missing/) applies — a BIOS update from your maker is the next step.

## Closing

A missing 120Hz option on an ARM laptop is a negotiation failure, not a panel failure — the negotiators are the power mode, the driver, HDR, and the cable. Check power first, reinstall the OEM Adreno driver second, and suspect the dock or HDR setting before anything exotic.
