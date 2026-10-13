---
title: "How to Fix Thunderbolt Not Working on a Laptop in Windows 11 24H2"
slug: how-to-fix-thunderbolt-not-working-on-laptop-in-windows-11-24h2
date: 2026-09-09
categories: ["drivers"]
tags: ["thunderbolt not working", "thunderbolt driver", "usb4", "windows 11 24h2"]
description: "Thunderbolt dock, eGPU, or drive not recognized on Windows 11 24H2? Six fixes covering drivers, BIOS settings, cable issues, and Thunderbolt security levels."
thumbnail: "/images/thumbs/how-to-fix-thunderbolt-not-working-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why did Thunderbolt stop working after the Windows 11 24H2 update?"
    a: "The 24H2 upgrade reinstalls the Thunderbolt driver and firmware stack, and the Thunderbolt controller driver or the Intel Thunderbolt Control Center app can come out mismatched or missing. Additionally, 24H2 tightened default DMA protection and device approval behavior, so previously auto-approved devices may now need explicit authorization. Reinstalling the Thunderbolt driver package from your laptop vendor and re-approving the device fixes the great majority of post-update failures."
  - q: "How do I know if the problem is the cable and not the driver?"
    a: "Thunderbolt requires a genuine Thunderbolt-rated cable — a regular USB-C cable fits the same port but cannot carry Thunderbolt signals, and many docks fail silently with the wrong cable. Test with the short cable that came with your dock or a certified Thunderbolt 3/4 cable, and try a different port. If Device Manager shows the Thunderbolt controller healthy but the device never enumerates, the cable is the prime suspect."
  - q: "Should Thunderbolt work if I plug the device in before booting?"
    a: "On many laptops, yes — pre-boot enumeration bypasses Windows driver quirks and is a useful diagnostic. If the dock works when connected before power-on but not when hot-plugged, the issue is almost certainly the Windows Thunderbolt driver or the approval/security setting rather than hardware. Use that result to focus on Fix 2 and Fix 4 rather than replacing cables."
  - q: "Is it safe to lower the Thunderbolt security level in BIOS?"
    a: "Lowering the security level (for example from User Authorization to No Security) does remove the DMA-attack protection that Thunderbolt security provides, so only do it on a laptop you physically control and don't leave unattended in untrusted places. For most home and office users the practical risk is low, but prefer fixing the driver and approval flow first and treat the security setting as a diagnostic step, not a permanent configuration."
---

Your Thunderbolt dock was working fine, the 24H2 update landed, and now the external monitors are dark, the eGPU is invisible, and the dock might as well be a paperweight. Thunderbolt failures after a Windows update are a special kind of frustrating because the chain has so many links: the physical cable, the Thunderbolt controller firmware, the Windows driver, the approval/security layer, and the BIOS. A break at any link looks the same from your desk.

The good news is that the failure signature narrows it down fast. Device never appears at all? Driver or enumeration problem. Appears but needs approval every time? Security-level issue. Worked before the update and nothing else changed? Driver stack, almost certainly. We'll walk the chain in the order a technician would, from the cheapest checks to the deeper ones. Thunderbolt shares plumbing with USB4 and docks, so if USB devices are also misbehaving, check the [USB device not recognized guide](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/) in parallel.

## Why this happens

- **The Thunderbolt driver didn't survive the 24H2 upgrade.** The controller driver or the Thunderbolt Control Center app was removed or left version-mismatched by the feature update.
- **The device needs re-approval.** 24H2's security defaults can require explicit authorization for Thunderbolt devices that were previously auto-approved, silently blocking them.
- **You're using a USB-C cable, not a Thunderbolt cable.** The connectors are identical; a non-Thunderbolt USB-C cable cannot negotiate Thunderbolt at all, and docks fail without any useful error.
- **The Thunderbolt firmware is out of sync with the driver.** Controller firmware (NVM) and the Windows driver are version-paired; an update that moves one without the other breaks enumeration.
- **BIOS Thunderbolt settings changed or reset.** The 24H2 update process (or a companion firmware update) can reset BIOS options like Thunderbolt pre-boot support or security level.
- **DMA protection is blocking the device.** Kernel DMA Protection, now more strictly enforced, can block Thunderbolt PCIe tunneling for devices it doesn't trust.
- **The controller is stuck in a bad power state.** Modern standby transitions can wedge the Thunderbolt controller so it stops enumerating until fully reset.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the cable and port

Eliminate the physical layer before touching software.

1. Use a certified Thunderbolt 3 or 4 cable — look for the lightning-bolt logo on the connector. The short cable bundled with your dock is the best test cable.
2. Try every USB-C/Thunderbolt port on the laptop; on some models only specific ports are Thunderbolt-capable.
3. Connect the dock's power adapter — many docks won't enumerate devices when running on bus power alone.
4. If possible, test the dock on another Thunderbolt laptop to confirm the dock itself is healthy.

### Fix 2: Reinstall the Thunderbolt driver package

Get the vendor-matched driver stack back in place.

1. Open Device Manager > **System devices** and look for **Thunderbolt(TM) Controller**.
2. Right-click > **Uninstall device**, checking **Attempt to remove the driver for this device**.
3. Download the Thunderbolt driver package from your laptop vendor's support page (not Intel's generic page — the vendor package includes the firmware and control app pairing): [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
4. Install, restart, and reconnect the device. Also reinstall the **Intel Thunderbolt Control Center** from the Microsoft Store if it's missing.

### Fix 3: Approve the device in Thunderbolt Control Center

The device may be blocked at the security layer.

1. Open **Intel Thunderbolt Control Center** (or **Thunderbolt Control Center**) from the Start menu.
2. With the device connected, it should appear under **Attached Thunderbolt Devices** awaiting approval.
3. Approve it and choose **Always Connect** so it doesn't ask again.
4. If the app says no devices are attached while the dock is plugged in, the problem is below the approval layer — return to Fix 2 or continue to Fix 5.

### Fix 4: Adjust the Thunderbolt security level in BIOS

For devices blocked by authorization policy.

1. Restart into BIOS/UEFI setup (F2/Del/F12 depending on vendor).
2. Find the **Thunderbolt** settings — often under **Advanced**, **Security**, or **System Configuration**.
3. Note the current **Thunderbolt Security Level**. For diagnosis, you can temporarily set it to **No Security** to see if the device enumerates.
4. If it works with security off, the driver/approval flow is the issue — set it back to **User Authorization** and fix approval via Fix 3, keeping the lower level only if you accept the tradeoff.

### Fix 5: Update Thunderbolt firmware (NVM)

When the driver is right but enumeration still fails, the controller firmware is suspect.

1. Check your vendor's support page for a **Thunderbolt firmware** or **NVM** update for your exact model — install only the one matching your machine.
2. Close all apps, keep the charger connected, and do not interrupt the flash.
3. Restart and reconnect the Thunderbolt device.
4. Verify in Thunderbolt Control Center > **Settings** > **Details** that the NVM version matches the update.

### Fix 6: Reset the controller with a full power drain

Clear a wedged controller state.

1. Shut down the laptop completely (not sleep, not hibernate).
2. Unplug the charger and all Thunderbolt/USB-C devices.
3. Hold the power button for 30 seconds to drain residual power (on removable-battery models, remove the battery too).
4. Reconnect the charger, boot, then attach the Thunderbolt device. If monitors on the dock still don't appear, the [second monitor detection guide](/articles/how-to-fix-second-monitor-not-detected-windows-11-on-hp-laptop/) covers the display side of dock setups.

## Closing

Thunderbolt troubleshooting is chain diagnosis: cable, driver, approval, firmware, BIOS, power state. Work it in that order and you'll find the broken link instead of replacing parts at random. Once it's working, keep the vendor's Thunderbolt package installed and let the vendor's update utility — not Windows Update alone — manage it, because version pairing between driver, firmware, and control app is exactly what the next feature update will try to break.
