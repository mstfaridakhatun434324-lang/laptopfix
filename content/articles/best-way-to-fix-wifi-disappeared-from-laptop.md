---
title: "WiFi Disappeared From Your Laptop? Best Fixes That Work"
slug: best-way-to-fix-wifi-disappeared-from-laptop
date: 2026-09-25
categories: ["drivers"]
tags: ["wifi disappeared", "no wifi option", "wifi missing", "wireless adapter gone"]
description: "WiFi option completely gone from Windows? These are the best fixes that bring back disappeared WiFi, from airplane mode to driver and BIOS repairs."
thumbnail: "/images/thumbs/best-way-to-fix-wifi-disappeared-from-laptop.webp"
faqs:
  - q: "Why did the WiFi option disappear from my laptop?"
    a: "The WiFi option vanishes when Windows cannot see a working wireless adapter: the driver failed (often after an update), the adapter is disabled in Device Manager or the BIOS, airplane mode is stuck on, or the wireless card itself stopped enumerating. Because the causes range from a stuck toggle to hardware, the best approach is the ordered checklist — toggles first, drivers second, firmware and hardware last."
  - q: "How is disappeared WiFi different from WiFi not connecting?"
    a: "Not connecting means the adapter works but cannot join a network — a network or authentication problem. Disappeared means there is no WiFi adapter for Windows to use at all: no icon, no networks list, no WiFi section in Settings. The former is fixed in network settings; the latter is fixed in Device Manager, drivers, and the BIOS. Different layers, different fixes."
  - q: "Can airplane mode get stuck and hide WiFi?"
    a: "Yes. The airplane-mode state can wedge so the toggle shows off while the radio stays disabled at the driver level — Quick Settings then shows no WiFi option at all. Toggling airplane mode on and off, or clearing it via Settings > Network & internet, releases the stuck state. This is one of the most common and most embarrassing causes of vanished WiFi."
  - q: "What if the wireless adapter is missing from Device Manager?"
    a: "A missing adapter (even with hidden devices shown) means the card is not enumerating: check the BIOS wireless toggle, do a cold boot with the power drained, and test with a Linux live USB. If it is absent everywhere, the card or its slot connection has failed. If it appears flagged rather than missing, that is a driver problem — reinstall the wireless driver."
---

There is no WiFi icon. No networks list. The WiFi section is simply gone from Settings, as if the laptop never had wireless. This is different from WiFi that will not connect — there, the adapter exists and struggles; here, Windows has no adapter to work with at all. The fault sits below the network layer: in a stuck radio state, a failed driver, a BIOS toggle, or the card itself.

The best fixes run the stack bottom-up in order of effort: the toggles and airplane mode first (seconds), the driver second (minutes), the BIOS and hardware last. Each step has a clear pass/fail, so you always know where the adapter went.

## Why this happens

- **Airplane mode stuck on** at the driver level despite the toggle showing off.
- **Wireless adapter disabled** in Device Manager.
- **WiFi driver corrupted or replaced** by an incompatible update.
- **WLAN AutoConfig service stopped**, so no wireless UI appears.
- **Wireless disabled in the BIOS** or by a physical switch.
- **Power management** cutting the adapter so it never enumerates.
- **Wireless card not enumerating** — loose module or failed hardware.
- **Corrupted network stack** hiding the adapter from Settings.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear airplane mode and the radio state

Toggle airplane mode on, wait ten seconds, and toggle it off — in Quick Settings and in Settings > Network & internet > Airplane mode. Check for a physical wireless switch on the laptop's edge and any Fn-key radio toggle, flipping each. A radio stuck in the off state hides the entire WiFi UI, and this toggle dance is the release. If the WiFi icon returns, the state was wedged — the most common single cause. The [no-WiFi-option guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) covers stuck-radio variants.

1. Toggle airplane mode on, wait, then off.
2. Check the physical wireless switch and Fn radio toggle.
3. Verify in Settings > Network & internet.
4. Confirm the WiFi icon and networks list return.

### Fix 2: Enable the adapter in Device Manager

Open Device Manager > Network adapters: if the wireless adapter shows a down arrow, right-click and enable it. Choose View > Show hidden devices — a greyed-out adapter can also be enabled from there. If the adapter appears with a warning icon instead, skip to the driver fix; a flagged adapter is a driver problem, not a disabled one. If the adapter is absent entirely, note that and continue — the BIOS and hardware checks later address enumeration failure. The [adapter-not-showing guide](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/) continues that branch.

1. Open Device Manager > Network adapters.
2. Enable any disabled (down-arrow) wireless adapter.
3. Show hidden devices and enable greyed-out entries.
4. Note warning icons vs total absence for the next steps.

### Fix 3: Restart WLAN AutoConfig and reinstall the driver

The WLAN AutoConfig service builds the WiFi UI — if it is stopped, there is no WiFi section in Settings. Open services.msc, set WLAN AutoConfig to Automatic, and start it. Then reinstall the wireless driver: download it from the laptop maker's support page for your exact model, uninstall the adapter in Device Manager (deleting the driver software), install fresh, and reboot. This pair — service plus driver — resolves the large majority of disappeared-WiFi cases. Microsoft's wireless steps are in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Set WLAN AutoConfig to Automatic and start it.
2. Download the WiFi driver from the laptop maker's support page.
3. Uninstall the adapter, deleting the driver software.
4. Install the fresh driver and reboot.

### Fix 4: Roll back the update that broke it

If WiFi vanished within a day of a Windows update, roll back: Device Manager > adapter Properties > Driver > Roll Back Driver. Check Update history to name the culprit, and consider pausing updates while you stabilize. For Intel cards, Intel's [detection tool](https://www.intel.com/content/www/us/en/support/detect.html) can install the newest known-good wireless build when the OEM package is the problem. If Windows keeps reinstalling the bad driver, block it by hardware ID using the procedure in the driver-update control guide.

1. Roll back the wireless driver in Device Manager.
2. Identify the breaking update in Update history.
3. Install the newest good build from the maker or Intel.
4. Block the bad driver if Windows reinstalls it.

### Fix 5: Check the BIOS wireless toggle

Reboot into the BIOS and verify the wireless/WLAN device is enabled — firmware updates and resets flip this toggle, and a BIOS-disabled radio never enumerates in Windows. Check whether the BIOS device inventory lists the wireless card at all; absent there means the hardware is not announcing itself. Save, boot, and recheck Device Manager. This step catches the cases where every Windows fix fails because the device was switched off below the OS.

1. Enter the BIOS setup on boot.
2. Enable the wireless/WLAN device.
3. Check the BIOS inventory for the card.
4. Save, boot, and recheck Device Manager.

### Fix 6: Cold-boot to reset the embedded controller

Shut down fully (not sleep, not hybrid restart — hold Shift while clicking Shut down to bypass fast startup), unplug AC, and if the battery is removable, remove it. Hold the power button 30 seconds to drain residual power, then reconnect and boot. This cold reset forces the embedded controller to re-enumerate every device, which revives wireless cards stuck in a wedged power state. Cards that reappear after this were never broken — their power state was. Retest WiFi immediately after boot.

1. Shift+Shut down to fully power off.
2. Unplug AC and remove the battery if possible.
3. Hold power 30 seconds, reconnect, and boot.
4. Check whether the adapter reappears.

### Fix 7: Reseat or replace the wireless module

If the adapter is absent in Device Manager (hidden shown), absent in the BIOS inventory, and absent in a Linux live USB, the card or its connection failed. On many laptops it is a user-replaceable M.2 2230 module: open the service hatch, reseat the card and its two antenna leads, and test. Still absent means a dead card — replacements are cheap, just match the form factor and CNVi type for Intel platforms. Soldered-down cards make this a board-level repair. Either way, the triad of absences is the definitive hardware verdict.

1. Confirm absence in Device Manager, BIOS, and Linux.
2. Open the hatch and reseat the M.2 card and antennas.
3. Replace the card with a compatible module if still absent.
4. Get a board repair quote for soldered cards.

## Closing

Disappeared WiFi is an adapter-visibility problem, and visibility has a fixed hierarchy: radio state, OS enablement, driver, service, firmware, hardware. The best fixes walk that hierarchy without skipping, because each layer's test is definitive — the toggle either brings the icon back or it does not, the driver either enumerates the card or it does not. Most cases end at the stuck airplane mode or the driver reinstall, which is why those come first. And the preventive lesson is the familiar one: wireless drivers are the most update-fragile in the machine, so once WiFi is back, keep the working installer and keep automatic driver updates from silently swapping it again.
