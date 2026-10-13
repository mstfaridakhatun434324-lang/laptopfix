---
title: "How to Fix Intel Wi-Fi 6 AX201 Not Working in Windows 11 24H2"
slug: how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2
date: 2026-09-27
categories: ["drivers"]
tags: ["intel ax201", "wifi 6 not working", "wireless driver", "windows 11 24h2"]
description: "Intel Wi-Fi 6 AX201 not working on Windows 11 24H2? Six fixes for the Code 10/43 errors, from Intel's standalone driver to BIOS and power settings."
thumbnail: "/images/thumbs/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "What do Code 10 and Code 43 mean on the Intel AX201?"
    a: "Code 10 means the device can't start — the driver loaded but the hardware won't initialize, usually a driver/firmware mismatch or a power-state problem. Code 43 means Windows stopped the device because it reported problems, often after a failed initialization. On the AX201 both codes overwhelmingly trace to the driver build: the wrong version for your 24H2 build, a corrupted install, or the CNVi firmware interface misbehaving. The driver fixes in this guide resolve both codes in most cases."
  - q: "Why is the AX201 special compared to other Wi-Fi cards?"
    a: "The AX201 is a CNVi (Connectivity Integration) card: unlike traditional cards, it offloads baseband logic to the Intel chipset, and the M.2 module holds only the radio. This means the AX201 depends on chipset firmware and the Intel chipset driver in ways normal Wi-Fi cards don't — and it only works in systems designed for CNVi. Driver problems therefore involve the chipset side too, which is why this guide covers chipset drivers and BIOS alongside the Wi-Fi driver."
  - q: "Should I use Intel's driver or my laptop maker's driver for the AX201?"
    a: "Intel's standalone Wi-Fi driver (from the Intel download site or the Driver & Support Assistant) is usually the better choice for the AX201 — Intel updates it frequently with bug fixes, and the card is standardized enough that vendor customization is minimal. The exception: if Intel's latest breaks something the vendor's older build handled, roll back to the vendor's. Start with Intel's latest; fall back to the vendor's if needed."
  - q: "Can the AX201's Bluetooth also break when Wi-Fi fails?"
    a: "Yes — the AX201 is a combo card, so Wi-Fi and Bluetooth share the module and parts of the driver package. A corrupted install or wedged power state often kills both simultaneously. If your Bluetooth also vanished, that's confirmation the problem is at the card/driver level rather than the Wi-Fi network side. The [Bluetooth disappeared guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-youtube/) covers the Bluetooth-specific recovery steps."
---

No Wi-Fi networks listed. Or the Intel Wi-Fi 6 AX201 shows a yellow warning in Device Manager with Code 10 or Code 43. Or Wi-Fi works until the laptop sleeps, then never comes back. The AX201 is Intel's most widely deployed Wi-Fi 6 card — it's in millions of laptops — and on Windows 11 24H2 it has a well-documented rough patch: driver builds that don't initialize the card, power management that wedges it, and the card's special CNVi architecture adding failure modes that standard Wi-Fi cards don't have.

Understanding the CNVi detail matters for troubleshooting: the AX201 isn't a self-contained Wi-Fi card. Its intelligence lives partly in your Intel chipset, so "the Wi-Fi driver" is only half the story — the chipset driver and BIOS firmware participate in every initialization. That's why this guide goes beyond the usual "update the driver" into chipset, BIOS, and power-state territory. If Wi-Fi is fine but Bluetooth (same card) vanished, the [Bluetooth disappeared guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-youtube/) is the companion fix.

## Why this happens

- **The 24H2 update installed an incompatible Wi-Fi driver build.** Intel's rapid driver releases mean Windows Update sometimes lands a build with an AX201 initialization bug.
- **The driver install corrupted.** A partial or interrupted driver update leaves the AX201 in the Code 10/43 state — driver present, hardware unstartable.
- **CNVi chipset interface misbehaving.** The chipset-side driver or firmware that the AX201 depends on is outdated or mismatched, so the card can't initialize.
- **Power management wedges the card.** PCIe power saving puts the AX201 to sleep (especially across modern standby) and it fails to wake.
- **The card is stuck from Fast Startup.** Hibernation-style shutdowns preserve the failed hardware state across "reboots."
- **BIOS/UEFI firmware too old for the driver.** Newer Intel Wi-Fi drivers expect chipset firmware behaviors that old BIOS versions don't provide.
- **Antenna or card hardware failure.** Least common: the M.2 card unseated or the radio portion failed — but rule out software first, since software causes dominate.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install Intel's latest standalone Wi-Fi driver

Get the authoritative build, not Windows Update's pick.

1. Go to Intel's driver download site or run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) and install the latest **Intel Wi-Fi 6 AX201** driver (the package is usually named "Wi-Fi-22.x.x-Driver64").
2. In Device Manager > **Network adapters**, right-click **Intel(R) Wi-Fi 6 AX201 160MHz** > **Uninstall device** (check **Attempt to remove the driver**) before installing Intel's package — this clears the broken build.
3. Install Intel's downloaded driver, restart, and check that the warning icon is gone.
4. Verify the driver version in the **Driver** tab matches Intel's published version.

### Fix 2: Update the Intel chipset driver

Fix the CNVi side the AX201 depends on.

1. Download the **Intel Chipset Device Software** (INF utility) for your platform from Intel or your laptop vendor.
2. Install it and restart — this updates the chipset-side interfaces the AX201's CNVi architecture requires.
3. Re-check Device Manager: Code 10 errors that survive a Wi-Fi driver update but clear after the chipset update were CNVi-side problems.
4. If your vendor offers a newer BIOS mentioning connectivity or Intel firmware, note it for Fix 5.

### Fix 3: Disable power management on the AX201

Stop the sleep-that-kills-Wi-Fi cycle.

1. Device Manager > **Network adapters** > right-click the AX201 > **Properties** > **Power Management** tab — uncheck **Allow the computer to turn off this device to save power**.
2. **Advanced** tab: set **Power Saving Mode** / **Transmit Power** to **Maximum Performance**, and disable any **802.11a/b/g Wireless Mode** power-saving entries if present.
3. **Control Panel** > **Power Options** > **Wireless Adapter Settings** > **Power Saving Mode** > **Maximum Performance** (both battery and plugged in).
4. Test sleep/wake cycles — Wi-Fi that dies after sleep and needs a reboot was almost certainly this.

### Fix 4: Disable Fast Startup and drain residual power

Clear the preserved failed state.

1. **Control Panel** > **Power Options** > **Choose what the power buttons do** > uncheck **Turn on fast startup**.
2. Shut down fully (Shift + Shut down), unplug the charger, hold the power button 30 seconds.
3. Boot and check the AX201 in Device Manager.
4. If it was Code 43 before and enumerates cleanly now, the card was wedged — keep Fast Startup off to prevent recurrence.

### Fix 5: Update the BIOS

Bring the firmware up to the driver's expectations.

1. Check your vendor's support page for a BIOS update: [Dell Support](https://www.dell.com/support), HP's support site, or [Lenovo Support](https://support.lenovo.com/us/en/).
2. Read the release notes — proceed if they mention Wi-Fi, connectivity, Intel firmware, or CNVi.
3. Flash with the charger connected and nothing else running; do not interrupt.
4. After the BIOS update, reinstall Intel's Wi-Fi driver (Fix 1) once more — firmware changes can require driver re-initialization.

### Fix 6: Roll back to a known-good driver version

When the latest driver is the problem.

1. Device Manager > AX201 > **Properties** > **Driver** tab — note the current version, then click **Roll Back Driver** if available.
2. If rollback isn't available, download an older Intel Wi-Fi driver (Intel archives previous releases) — try one version back first.
3. Uninstall the current driver (**Attempt to remove the driver** checked), install the older build, restart.
4. Once stable, pause driver updates for Wi-Fi via the `ExcludeWUDriversInQualityUpdate` registry policy so Windows Update can't re-break it. Document the working version using the [driver version check method](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/) — with the AX201's rapid release cadence, knowing your good build saves hours next time.

## Closing

The AX201's CNVi architecture means its failures are never just "the Wi-Fi driver" — they're the Wi-Fi driver plus the chipset driver plus BIOS firmware plus power policy, all of which have to agree. Work all four layers: Intel's latest Wi-Fi build, the chipset INF, a firmware check, and power management tamed. The card that "stopped working" on 24H2 is in millions of laptops working fine — yours just needs its stack realigned.
