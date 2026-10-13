---
title: "Intel Wi-Fi 6 AX201 Not Working? Here's How to Fix It"
slug: "how-do-i-fix-intel-wifi-6-ax201-not-working"
date: "2026-09-22"
categories: ["drivers"]
tags: ["intel ax201", "wifi 6", "wireless driver", "intel wifi"]
description: "Intel Wi-Fi 6 AX201 dropping connections, not detected, or slow on your laptop? Fix it with the right driver, correct settings, and proven troubleshooting steps."
thumbnail: "/images/thumbs/how-do-i-fix-intel-wifi-6-ax201-not-working.webp"
faqs:
  - q: "Which Intel driver version is best for the AX201?"
    a: "It varies over time because Intel's release quality for the AX201 has been uneven. As a rule, prefer the latest version unless community reports flag regressions — in which case step back one release. Avoid letting Windows Update choose the version; install Intel's package directly and block driver replacements."
  - q: "Why does my AX201 disconnect every few minutes?"
    a: "Frequent periodic drops usually come from roaming aggressiveness set too high (the card keeps hunting for better access points), power management suspending the adapter, or a router with buggy Wi-Fi 6 handling. Lower roaming aggressiveness, disable adapter power saving, and update the router firmware."
  - q: "Why does my AX201 stop working after sleep?"
    a: "The AX201's power-state handling is its weakest area: it enters a low-power state on sleep that some driver versions cannot exit. Disable 'allow the computer to turn off this device' in Device Manager, set wireless power saving to Maximum Performance, and test sleep-wake cycles after each driver change."
  - q: "Should I replace my AX201 with a newer card?"
    a: "If the card drops on every network with known-good drivers and secure antennas, replacement is reasonable — the AX210 is a popular, inexpensive upgrade that fits the same M.2 slot. But rule out drivers, power settings, and router issues first; most AX201 problems are software, not silicon."
---

The Intel Wi-Fi 6 AX201 is one of the most common wireless cards in Windows laptops — and one of the most complained about. Its failure modes are distinctive: the adapter vanishes from Device Manager, connections drop every few minutes, speeds collapse on 5 GHz, or the card dies after sleep. Each symptom points at a different layer.

The AX201 has a sensitive driver history: one version is rock solid while the next is a disaster, so 'update to the latest' is not always right — sometimes a specific known-good version is. Check Intel's release notes for acknowledged regressions.

This guide covers the full AX201 playbook: identifying your failure mode, picking the right driver version, and tuning the settings this card is picky about. For the deeper diagnostic sequence, see our [AX201 step-by-step guide](/articles/troubleshoot-intel-wifi-6-ax201-not-working/); if the adapter is missing entirely, our [vanished-adapter guide](/articles/best-way-to-fix-wifi-adapter-not-showing-up/) applies.

## Why this happens

- ****Buggy Intel driver version**:** The AX201's driver history includes several bad releases that cause drops, disappearance, or blue screens. The installed version matters enormously with this card.
- ****Windows Update driver replacement**:** Windows Update pushes its own Intel Wi-Fi driver builds, which may be older or less stable than Intel's current release — and may overwrite a working version.
- ****Aggressive power management**:** The AX201 is sensitive to power-saving states. PCIe power management and the adapter's own power-saving mode can disconnect it or prevent wake from sleep.
- ****802.11ax mode incompatibility with the router**:** Some router firmware handles Wi-Fi 6 negotiation poorly with the AX201, causing drops or failure to connect on the 5 GHz band.
- ****Roaming aggressiveness misconfiguration**:** In offices or homes with multiple access points, the AX201's roaming settings can cause constant disconnect-reconnect cycling.
- ****Antenna or M.2 seating issues**:** The AX201 uses two tiny antenna leads. If one pops off — common after repairs — range collapses and the 5 GHz band may fail entirely.
- ****Bluetooth coexistence interference**:** The AX201 shares radio resources with Bluetooth. Heavy Bluetooth use (audio streaming) can degrade Wi-Fi on congested bands.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install a Known-Good Intel Driver Version

Download Intel's Wi-Fi driver package via Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html). But check community feedback first: if the newest release has drop complaints, install the previous stable. Uninstall the current driver with driver deletion in Device Manager, restart, then install your chosen version.

After installing, block Windows Update from replacing it (decline driver offerings under Optional updates). Version churn from Windows Update is how many AX201 owners end up on a bad driver without ever choosing it.

1. 1. Identify your current AX201 driver version in Device Manager.
2. 2. Download Intel's Wi-Fi driver package for the AX201.
3. 3. Uninstall the current driver with driver deletion and restart.
4. 4. Install the chosen known-good version.
5. 5. Block Windows Update driver replacements afterward.

### Fix 2: Disable Power Saving on the Adapter

In Device Manager, open the AX201's properties: uncheck power-saving on the Power Management tab, and on the Advanced tab set Power Saving Mode to Maximum Performance and Transmit Power to Highest. Mirror this in your power plan's advanced wireless settings.

The AX201's sleep/wake behavior is its weakest area, and these settings directly address the 'works until sleep' failure mode. Test through several sleep-wake cycles after changing them.

1. 1. In Device Manager, open the AX201 properties.
2. 2. Uncheck power-saving on the Power Management tab.
3. 3. Set Power Saving Mode to Maximum Performance on the Advanced tab.
4. 4. Set wireless power saving to Maximum Performance in the power plan.
5. 5. Test multiple sleep and wake cycles.

### Fix 3: Tune the 802.11ax and Band Settings

In the AX201's Advanced tab, disable '802.11ax' mode temporarily as a diagnostic — if drops stop, your router's Wi-Fi 6 implementation is the problem and a router firmware update is the real fix. Also set 'Preferred Band' explicitly instead of automatic.

On the router side, ensure its firmware is current and try disabling features like 'Smart Connect' band steering temporarily. The AX201 negotiates best with straightforward, separate SSIDs for 2.4 and 5 GHz on some routers.

1. 1. Open the AX201 Advanced tab in Device Manager.
2. 2. Disable 802.11ax mode temporarily as a diagnostic.
3. 3. Set Preferred Band explicitly instead of automatic.
4. 4. Update the router's firmware.
5. 5. Test with separate 2.4 GHz and 5 GHz SSIDs if drops persist.

### Fix 4: Adjust Roaming Aggressiveness

In the adapter's Advanced tab, set 'Roaming Aggressiveness' to 'Lowest' if you stay near one access point — high aggressiveness makes the card hunt for better APs and drop the current connection. Use 'Medium' where you genuinely roam.

This setting is the fix for the maddening pattern of disconnecting every few minutes in offices, dorms, and mesh-network homes. Pair it with disabling 'Allow the computer to turn off this device' since the two issues often coexist.

1. 1. Open the AX201 Advanced tab in Device Manager.
2. 2. Set Roaming Aggressiveness to Lowest for single-AP environments.
3. 3. Use Medium if you genuinely move between access points.
4. 4. Apply and test for at least an hour.
5. 5. Adjust one step at a time if drops continue.

### Fix 5: Reset the Network Stack

If the AX201 is detected but connections fail or drop constantly, reset the network stack: run netsh winsock reset, netsh int ip reset, and ipconfig /flushdns in an elevated Command Prompt, then restart. Follow with a Settings network reset if needed.

These resets clear corrupted socket catalogs, IP configurations, and adapter bindings without touching your files. Microsoft documents the procedure in its [Windows support hub](https://support.microsoft.com/en-us/windows).

1. 1. Open Command Prompt as administrator.
2. 2. Run netsh winsock reset and netsh int ip reset.
3. 3. Run ipconfig /flushdns.
4. 4. Restart the laptop.
5. 5. Use Settings network reset if problems persist.

### Fix 6: Check the Antenna Connections

If range is terrible — full speed next to the router, nothing ten feet away — suspect the antenna leads. Power off, remove the bottom panel, and find the AX201's M.2 card with its two tiny coaxial connectors (MAIN and AUX). Press each gently to confirm it is snapped on.

A popped antenna lead is common after any repair involving the bottom panel. The connectors are fragile — press straight down, never at an angle. If both are secure and range is still awful, the card itself may be failing.

1. 1. Power off completely and remove the bottom panel.
2. 2. Locate the AX201 M.2 card and its two antenna leads.
3. 3. Gently press each connector to confirm it is seated.
4. 4. Reassemble and test range on both bands.
5. 5. Replace the card if antennas are fine but range is still bad.

### Fix 7: Test on a Different Network

Connect to a phone hotspot or different router. Stable there means your router (firmware, settings, band steering) is the problem, not the card. Dropping everywhere means the card, driver, or antennas.

Do this before buying replacement hardware: stable-on-hotspot plus broken-on-router means updating or replacing the router, or tuning its Wi-Fi 6 settings.

1. 1. Connect to a phone hotspot and use it for an hour.
2. 2. Try a second Wi-Fi network if available.
3. 3. Stable elsewhere means your router is the problem.
4. 4. Broken everywhere means the card, driver, or antennas.
5. 5. Act on the verdict instead of guessing.

## Closing

The AX201 rewards specific attention: the right driver version (not just the newest), power management disabled, and router settings it negotiates cleanly. Work the list in order and you will fix the card or get a clean diagnosis — vanishing adapter, bad driver, router incompatibility, or loose antenna.
