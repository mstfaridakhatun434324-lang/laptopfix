---
title: "WiFi Driver Code 10 Error? How to Get Wireless Working Again"
slug: how-to-fix-wifi-driver-code-10-error-youtube
date: 2026-09-04
categories: ["drivers"]
tags: ["wifi driver code 10", "device cannot start", "wifi not working", "wireless adapter"]
description: "Seeing 'This device cannot start (Code 10)' on your WiFi adapter? Learn what causes the Code 10 error and the exact steps to bring wireless back."
thumbnail: "/images/thumbs/how-to-fix-wifi-driver-code-10-error-youtube.webp"
faqs:
  - q: "What does Code 10 mean on a WiFi adapter?"
    a: "Code 10 means the driver told Windows it cannot start the device. For WiFi adapters this is almost always a driver problem: a corrupted install, a driver written for the wrong adapter revision, or a power-management conflict. It rarely means the wireless card itself is dead. Reinstalling the correct driver from the laptop or chip maker resolves most Code 10 cases."
  - q: "Can a Windows update cause a WiFi Code 10 error?"
    a: "Yes, and it is one of the most common triggers. Windows Update sometimes installs a newer WiFi driver that is incompatible with the laptop's firmware, or a partial update leaves mismatched driver files. The adapter then fails to start with Code 10. Rolling back the driver or installing the laptop maker's validated version restores the matching driver-firmware pair."
  - q: "Will resetting the network fix a Code 10 WiFi error?"
    a: "A network reset fixes TCP/IP and adapter configuration problems, but Code 10 is a driver-start failure that happens before networking even loads. The reset is harmless and worth trying after the driver is healthy, but it cannot make a failed driver start. Fix the driver first, then reset the network stack if connections still misbehave."
  - q: "Is Code 10 ever a hardware failure?"
    a: "Occasionally. If the correct driver from the chip maker still produces Code 10 across Windows reinstalls, and the card is invisible in the BIOS or a Linux live USB, the wireless module or its slot connection may have failed. Loose M.2 WiFi cards after drops are a real cause. But always exhaust driver fixes first — hardware failure is the minority outcome."
---

The Code 10 error — "This device cannot start" — is Device Manager's way of telling you the WiFi driver tried to initialize the wireless adapter and failed. Your laptop can see the card, but the driver cannot bring it to life, so there is no WiFi icon, no networks list, and no wireless of any kind. It feels like broken hardware, but in the overwhelming majority of cases it is a driver mismatch that you can fix in under half an hour.

Code 10 sits at the boundary between software and hardware, which is why the fix order matters. You start with the cheap, reversible driver repairs — rollback, clean reinstall, the chip maker's package — and only move to BIOS, power, and hardware checks when the driver itself is proven healthy. Work the list in order and you will know exactly which layer failed.

## Why this happens

- **Corrupted WiFi driver files** after a failed or partial update.
- **Windows Update installed an incompatible driver** for the adapter revision.
- **Driver–firmware mismatch**: the driver expects firmware the card does not have.
- **Power management cutting the adapter**, blocking driver initialization.
- **Airplane mode or the wireless kill state** stuck at the driver level.
- **Conflicting old driver remnants** from a previous adapter or OS upgrade.
- **BIOS wireless setting disabled**, so the driver finds no radio to start.
- **Loose or failed wireless module** in its M.2 slot, usually after a drop.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Roll back the WiFi driver

If the Code 10 appeared right after an update, the previous driver was working — so go back to it. In Device Manager, open the WiFi adapter's properties and use Roll Back Driver. This restores the exact driver version that was running before, including its settings. Reboot and check whether the adapter starts cleanly. If the rollback button is greyed out, Windows has no older driver stored, and you move to the clean reinstall.

1. Open Device Manager and find the flagged WiFi adapter.
2. Open Properties > Driver tab and click Roll Back Driver.
3. Choose a reason and confirm, then reboot.
4. Check Device Manager for a clean, unflagged adapter.

### Fix 2: Clean-reinstall the driver from the laptop maker

A rollback cannot fix corruption, so the next step is a full clean install of the laptop maker's validated WiFi driver. Download it from the maker's support page for your exact model (you will need another device or a wired connection), then uninstall the adapter in Device Manager with 'Delete the driver software' ticked. Install the fresh package and reboot. This removes every corrupted remnant and installs the driver-firmware pair the maker tested. Intel's official [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) can also identify the right wireless driver automatically.

1. Download the WiFi driver from the laptop maker's support page.
2. Uninstall the adapter in Device Manager, deleting the driver software.
3. Install the downloaded package and reboot.
4. Confirm the adapter starts with no warning icon.

### Fix 3: Install the chip maker's reference driver

If the laptop maker's driver is outdated or itself broken, go straight to the source: Intel, MediaTek, Realtek, or Qualcomm, depending on your adapter. The chip maker's reference driver is newer and sometimes fixes Code 10 cases where the OEM package lags behind. Match the adapter model exactly (AX201 vs AX211 matters) and the Windows version. A variant-specific walkthrough for this error class is in the [Code 10 in-depth guide](/articles/how-to-fix-wifi-driver-code-10-error-in-windows-11-24h2/).

1. Identify your adapter's exact model in Device Manager.
2. Download the reference driver from the chip maker's site.
3. Uninstall the old driver completely, then install the new one.
4. Reboot and verify the adapter starts.

### Fix 4: Disable power management on the adapter

Some Code 10 failures are power problems wearing a driver disguise: the driver cannot start the card because Windows has powered the radio down. In the adapter's Properties > Power Management, untick 'Allow the computer to turn off this device to save power'. Also open the advanced power plan settings and set Wireless Adapter Settings to Maximum Performance. Then shut the laptop down fully (not sleep) and power it back on, which forces a clean power cycle of the radio. Microsoft's wireless troubleshooting steps are in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Untick power saving on the adapter's Power Management tab.
2. Set Wireless Adapter Settings to Maximum Performance in the power plan.
3. Shut down fully, wait 30 seconds, and power on.
4. Check whether the adapter now starts.

### Fix 5: Clear the stuck airplane-mode / radio state

A radio stuck in the off state can produce Code 10 because the driver cannot initialize a disabled radio. Toggle airplane mode on and off in Quick Settings, then check Settings > Network & internet > Airplane mode. Some laptops also have a physical wireless switch or an Fn-key radio toggle — flip it. Finally, run the built-in Network troubleshooter, which can clear stuck radio states that manual toggles miss.

1. Toggle airplane mode on, wait 10 seconds, toggle it off.
2. Check any physical wireless switch or Fn-key radio toggle.
3. Run Settings > System > Troubleshoot > Network troubleshooter.
4. Re-check the adapter status in Device Manager.

### Fix 6: Check the BIOS wireless setting

Reboot into the BIOS and verify that the wireless/WLAN device is enabled. Some BIOS versions also expose a 'wireless switch' behavior setting — set it so the OS controls the radio. While you are there, check whether the BIOS even lists the wireless card; a card missing from the BIOS inventory points at hardware rather than software. If the adapter is missing from Device Manager entirely rather than flagged, the [adapter-not-showing guide](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/) covers that sibling symptom.

1. Enter the BIOS setup on boot.
2. Confirm the wireless/WLAN device is enabled.
3. Set wireless control to OS control if the option exists.
4. Save, boot into Windows, and re-check Device Manager.

### Fix 7: Reseat or replace the wireless module

If the correct driver still yields Code 10 and the card is invisible in the BIOS and in a Linux live USB, the module or its connection is the problem. On many laptops the WiFi card is a user-replaceable M.2 2230 module under a service hatch: power down, remove the battery if possible, reseat the card and its two antenna leads, and test. Replacement cards are inexpensive — just match the form factor and, for Intel cards, the CNVi/non-CNVi type. If the card is soldered, this becomes a board-level repair job.

1. Power down and open the service hatch or bottom cover.
2. Reseat the M.2 WiFi card and both antenna connectors.
3. Boot and check whether the adapter now appears and starts.
4. If not, replace the module with a compatible part.

## Closing

Code 10 on a WiFi adapter is a driver-start failure, and the fix ladder reflects that: roll back the last change, clean-install the maker's validated driver, escalate to the chip maker's reference build, then clear power and radio states before ever suspecting hardware. Most cases resolve at step two or three — the corrupted or mismatched driver is the overwhelming favorite. Keep the working driver installer somewhere safe once wireless is back, and if Windows Update caused this once, consider deferring automatic driver updates so a background update cannot silently re-break the radio overnight. A WiFi card that works today with a known driver will work tomorrow as long as nothing swaps that driver out from under it.
