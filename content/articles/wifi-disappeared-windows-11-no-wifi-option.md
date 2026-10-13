---
title: "Wi-Fi Disappeared in Windows 11: No Wi-Fi Option? Restore It Now"
slug: wifi-disappeared-windows-11-no-wifi-option
date: 2026-09-22
categories: ["drivers"]
tags: ["wifi disappeared", "no wifi option", "windows 11", "network adapter", "wifi driver"]
description: "Wi-Fi option missing in Windows 11? Restore your wireless connection with 7 fixes — from quick toggles to full network stack resets."
thumbnail: "/images/thumbs/wifi-disappeared-windows-11-no-wifi-option.webp"
faqs:
  - q: "Why is there no Wi-Fi option in Windows 11 settings?"
    a: "Windows hides the Wi-Fi toggle when it can't see a working wireless adapter — the driver failed to load, the device is disabled, or the adapter is missing from Device Manager. In almost all cases the hardware is fine; the driver or the adapter's enabled state is the problem, and both are fixable in minutes."
  - q: "Why did my Wi-Fi disappear after a Windows update?"
    a: "Updates frequently replace the manufacturer's wireless driver with a generic or incompatible build, or the update process leaves the driver half-installed. Reinstalling the wireless driver package from your laptop maker's support page is the standard fix — it restores the exact build tested for your hardware."
  - q: "What if the network adapter is missing from Device Manager?"
    a: "First enable Show hidden devices in the View menu — a grayed-out adapter with an error code is a driver problem, not missing hardware. If it's truly absent, check the BIOS for a wireless toggle and try a network reset. A card invisible everywhere may have failed or (on some models) worked loose."
  - q: "Will network reset delete my files?"
    a: "No. Network reset only removes network adapters and their settings — saved Wi-Fi passwords, VPN configurations, and virtual switches. Your files, apps, and accounts are untouched. You'll need to re-enter Wi-Fi passwords afterward, so have them handy before you reset."
---

You open Settings or the Quick Settings panel and the Wi-Fi toggle is simply gone — no available networks, no Wi-Fi section, sometimes not even a network icon that makes sense. Ethernet may still work, Bluetooth may be fine, but wireless has vanished as if the laptop never had it. This is one of Windows 11's most common driver failures, and it's almost never dead hardware: Windows hides Wi-Fi controls when the wireless adapter's driver isn't loading, and drivers stop loading for very fixable reasons.

The repair sequence below goes from instant checks (airplane mode, function keys) through driver reinstallation to the full network reset, ending with the hardware checks for the rare cases that need them.

## Why this happens

- **Wireless driver corrupted or replaced by an update.** The runaway leader — Windows Update swapping in a bad wireless build.
- **Adapter disabled.** Via function key, Windows device disable, airplane mode stuck on, or BIOS toggle.
- **Failed driver migration during a feature update.** The 24H2 upgrade path is notorious for stranding wireless drivers.
- **Corrupted network stack.** Winsock/TCP-IP corruption hiding alongside the driver failure.
- **Power management disabling the adapter.** Aggressive power settings turning the radio off and failing to restore it.
- **BIOS wireless toggle off.** Especially after BIOS updates that reset settings.
- **Failed wireless card.** Rare — but the final check when software is exhausted.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check airplane mode, function keys, and quick settings

The 30-second sweep.

1. **Quick Settings** (Win+A): ensure **Airplane mode** is off — toggle it on and off once to reset radio state.
2. Press your laptop's **wireless function key** (often Fn+F2/F5 or a dedicated key) — these can disable the radio at firmware level.
3. **Settings > Network & internet**: if Wi-Fi is absent here but Ethernet shows, the adapter driver isn't loading — continue below.
4. Restart the laptop fully (not sleep) — stuck radio states often clear on a real reboot.
5. If Wi-Fi appears after reboot but vanishes later, suspect power management (Fix 5) or a flaky driver (Fix 3).

### Fix 2: Inspect Device Manager

See what Windows thinks about the adapter.

1. Open **Device Manager** → **View > Show hidden devices** → expand **Network adapters**.
2. A present adapter with a **yellow warning** = driver problem → Fix 3.
3. A **grayed-out** adapter = disabled → right-click → **Enable device**.
4. An adapter with **error Code 10/43/45** = driver/firmware failure → Fix 3, then Fix 6.
5. **Truly absent** (not even hidden) → check BIOS wireless toggle (Fix 7), then suspect hardware.

The 24H2-specific disappearance guide: [how to fix Wi-Fi disappeared from laptop in Windows 11 24H2](/articles/how-to-fix-wifi-disappeared-from-laptop-in-windows-11-24h2/).

### Fix 3: Reinstall the wireless driver from the manufacturer

The core fix — the right driver build.

1. On another device (or via Ethernet/USB tethering), download the **wireless/WLAN driver** for your exact model from the maker's support page.
2. In Device Manager, right-click the wireless adapter → **Uninstall device**, checking **Attempt to remove the driver software**.
3. Restart — Windows loads a basic driver or none at all.
4. Install the downloaded manufacturer package, restart again.
5. For Intel wireless cards, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) is the reliable alternative source.

The adapter-not-showing variant: [how to fix Wi-Fi adapter not showing up in Windows 11 24H2](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/).

### Fix 4: Run the network troubleshooter and reset the stack

Repair the software around the driver.

1. **Settings > System > Troubleshoot > Other troubleshooters > Network and Internet > Run**.
2. If it doesn't fix it, reset the stack in **Terminal (Admin)**: `netsh winsock reset` then `netsh int ip reset`, then restart.
3. Release and renew: `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
4. If the adapter appears but won't connect, **forget the network** (Settings > Network & internet > Wi-Fi > Manage known networks) and rejoin fresh.
5. Have your Wi-Fi password ready before forgetting anything.

### Fix 5: Disable power management on the adapter

The "Wi-Fi vanishes after sleep" fix.

1. **Device Manager** → wireless adapter → **Properties > Power Management** → **uncheck** "Allow the computer to turn off this device to save power."
2. **Settings > System > Power & battery** → Power mode **Best performance** while plugged in (test).
3. Advanced power plan settings → **Wireless Adapter Settings > Power Saving Mode** → **Maximum Performance**.
4. Test sleep/wake cycles — if Wi-Fi survives them now, power management was the culprit.
5. Update the BIOS from the maker's support page; radio power-state fixes are common in firmware changelogs.

### Fix 6: Network reset — the full rebuild

When the stack is tangled beyond targeted repair.

1. Have your **Wi-Fi passwords** written down — this erases them.
2. **Settings > Network & internet > Advanced network settings > Network reset > Reset now**.
3. The laptop restarts; all adapters reinstall fresh and all network settings return to defaults.
4. Reinstall the manufacturer's wireless driver (Fix 3) after the reset if Windows loads a generic one.
5. Rejoin your Wi-Fi networks. If Wi-Fi now works, the old stack was corrupt — don't try to diagnose further, just enjoy it.

### Fix 7: BIOS toggles and the hardware verdict

The last checks before concluding hardware failure.

1. Enter BIOS/UEFI → verify **Wireless/WLAN** is **Enabled** (updates sometimes reset this).
2. Load **Optimized Defaults** if wireless settings look odd, then re-enable wireless explicitly.
3. Boot a Linux USB live session — Wi-Fi working there + dead in Windows = software (return to Fix 3/6); dead in both = hardware.
4. On models with a socketed M.2 wireless card (Intel AX200/AX210), reseating or replacing the card is a 10-minute, low-cost repair.
5. Soldered wireless that fails everywhere = manufacturer service; document your software steps so support doesn't repeat them.

## Closing

A missing Wi-Fi option in Windows 11 is a driver problem wearing an invisibility cloak — the adapter is usually right there, just not loading. Check the toggles, look at Device Manager with hidden devices shown, reinstall the manufacturer's wireless package, and reset the network stack if needed. That sequence restores Wi-Fi in the overwhelming majority of cases, usually within half an hour. Save the hardware worry for last: it's the least likely explanation, and the Linux-USB test will tell you definitively before you spend a cent.
