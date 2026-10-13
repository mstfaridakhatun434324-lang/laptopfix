---
title: "Wi-Fi Dead After the Windows 11 24H2 Update? Bring It Back"
slug: how-to-fix-windows-11-24h2-wifi-not-working-youtube
date: 2026-09-14
categories: ["windows-update"]
tags: ["wifi not working", "windows 11 24h2", "wireless", "network"]
description: "Fix Wi-Fi not working after the Windows 11 24H2 update: roll back the bad driver, reset the network stack, and get wireless back online."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-wifi-not-working-youtube.webp"
faqs:
  - q: "Why do Windows updates break Wi-Fi so often?"
    a: "Wi-Fi drivers sit at a complex intersection of power management, security protocols, and hardware firmware. An OS update can invalidate the driver's assumptions about any of those, or replace a working manufacturer driver with a generic one. The driver worked yesterday and the hardware is fine — the interface between them changed."
  - q: "Should I download the Wi-Fi driver on another device?"
    a: "If your laptop has no working network at all, yes — that is the practical move. Download the Wi-Fi driver package from the manufacturer's support site on your phone or another computer, transfer it via USB, and install it. Keep that USB stick; it is your lifeline for future update mishaps."
  - q: "Will a network reset delete my saved Wi-Fi passwords?"
    a: "Yes. The network reset removes all network adapters and returns networking to factory defaults, which includes forgetting saved Wi-Fi networks and passwords. Have your Wi-Fi password handy before you run it. It is a last-resort step precisely because of this inconvenience."
  - q: "Can I stop Windows from replacing my working Wi-Fi driver?"
    a: "Yes. After installing the manufacturer's driver, you can hide the Windows Update driver offering with the show/hide troubleshooter, or use the device installation settings to block driver updates for that device. This is one of the few cases where blocking a driver update is genuinely the right call."
---

You install the Windows 11 24H2 update, reboot, and the Wi-Fi is gone — no networks listed, or networks listed but no connection, or a connection that drops every ninety seconds. The hardware did not break during a software update. What broke is the relationship between the new OS build and your Wi-Fi driver.

This is one of the most common 24H2 complaints, and it has a well-worn fix path: confirm the driver state, roll back or replace the driver, reset the network stack if needed, and stop Windows from "fixing" your working driver again. Work it in order and you will be back online within the hour.

## Why this happens

- **Driver replaced by generic:** 24H2 swaps the manufacturer's Wi-Fi driver for a generic one that lacks your card's quirks.
- **Power management conflicts:** The new build's power policies clash with the driver's sleep/wake handling, causing drops.
- **Security protocol changes:** Updated WPA3 and authentication stacks expose bugs in older drivers.
- **Corrupted driver migration:** The update's driver migration step partially completes, leaving a broken hybrid.
- **Third-party VPN/filter leftovers:** Old VPN clients install filters the new stack rejects, killing connectivity.
- **Band steering confusion:** Driver bugs in 5 GHz/6 GHz band selection after the update's wireless stack changes.
- **Fast Startup stale state:** Hibernated driver state from before the update conflicting with the new build.
- **Safeguard-held driver versions:** Microsoft knowingly blocking on your driver — the same hold logic behind [24H2 update errors](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/) on affected hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Diagnose the exact symptom

1. Click the network icon: note whether Wi-Fi is missing entirely, networks show but will not connect, or connections drop repeatedly.
2. Open **Device Manager → Network adapters** and check your Wi-Fi card's status — yellow warning, disabled, or missing entirely each mean different things.
3. Try Ethernet or USB tethering from your phone to confirm the rest of networking works.
4. Record the driver version and date in **Properties → Driver** — you will compare after fixes.
5. Precise symptoms prevent wasted effort: a missing adapter is a driver problem, drops are usually power management.

### Fix 2: Roll back the Wi-Fi driver

1. In **Device Manager**, right-click the Wi-Fi adapter → **Properties → Driver → Roll Back Driver** (if available).
2. Choose the reason, roll back, and reboot.
3. Test connectivity for ten minutes, including a sleep/wake cycle.
4. Rollback restores the pre-24H2 driver that was working — the fastest fix when available.
5. If the button is greyed out, the old driver was purged; continue to Fix 3.

### Fix 3: Install the manufacturer's Wi-Fi driver

1. On another device, download the latest Wi-Fi driver for your exact model from the maker's support site (or [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel cards).
2. Transfer via USB, then in Device Manager uninstall the current Wi-Fi driver (check **remove driver**).
3. Install the manufacturer's package fresh and reboot.
4. Verify the version in Driver properties matches what you downloaded.
5. Manufacturer drivers contain the card-specific fixes that generic Windows drivers lack — this resolves most non-rollback cases.

### Fix 4: Disable Wi-Fi power saving

1. **Device Manager → Wi-Fi adapter → Properties → Power Management**: uncheck **Allow the computer to turn off this device to save power**.
2. **Settings → System → Power & battery**: set the wireless adapter to **Maximum Performance** on both battery and plugged in.
3. In the driver's **Advanced** tab, disable power-saving features like "Power Saving Mode" or set roaming aggressiveness to moderate.
4. Test with several sleep/wake cycles — drops that only happen after sleep are power management, full stop.
5. This single setting fixes the majority of "connects then drops" cases after 24H2.

### Fix 5: Remove VPN clients and stale filters

1. Uninstall third-party VPN clients via **Settings → Apps** — their network filters frequently break across build upgrades.
2. In an elevated prompt, run `netsh winsock reset` to clear filter damage, then reboot.
3. Reinstall only a current-version VPN client afterward if you need one.
4. Test Wi-Fi before reinstalling anything — confirm the filter was the cause.
5. Old VPN filters are a top-three cause of "adapter present, no connectivity" after feature updates.

### Fix 6: Forget the network and reset the stack

1. **Settings → Network & internet → Wi-Fi → Manage known networks**: forget your network and reconnect fresh with the password.
2. If that fails, run the full network reset: **Settings → Network & internet → Advanced network settings → Network reset**.
3. Reboot when prompted and reconnect to Wi-Fi from scratch.
4. Have your Wi-Fi password ready — the reset forgets all saved networks.
5. The reset reinstalls all network adapters to factory state, clearing migration corruption. Microsoft documents the reset and its effects on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Block Windows from replacing your working driver

1. With Wi-Fi working on the manufacturer's driver, download the show/hide updates troubleshooter.
2. Hide any Wi-Fi driver offerings so Windows Update stops "updating" your working driver into a broken one.
3. Alternatively, set **Device installation settings** to not automatically download manufacturer apps/drivers for the device.
4. Verify after the next Patch Tuesday that the driver version is unchanged.
5. For MediaTek-based cards, the [MediaTek-specific guide](/articles/how-to-fix-mediatek-wifi-not-working-in-windows-11-24h2/) covers card-specific quirks worth knowing.

### Fix 8: Test hardware as the last resort

1. Boot a Linux live USB: if Wi-Fi works there, your hardware is fine and the issue is purely Windows-side.
2. If it fails in Linux too, reseat the Wi-Fi card (if accessible) and check the antenna wires.
3. A USB Wi-Fi adapter ($15–25) is a pragmatic permanent fix for an aging laptop with a dying card.
4. Document the card model and working driver version for the future.
5. Hardware failure is rare after updates — but "rare" is not "never," so verify rather than assume.

## Closing

Wi-Fi dying after the 24H2 update is a driver-interface problem, not a hardware problem: the update replaced, migrated, or confused the driver your card needs. Roll back when you can, install the manufacturer's driver when you cannot, kill power-saving and stale VPN filters, and reset the network stack as the heavy option. Then protect the fix by blocking Windows from replacing your working driver. Wireless is too essential to leave to the generic driver lottery — ten minutes of driver discipline after each feature update keeps you online.
