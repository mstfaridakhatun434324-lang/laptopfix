---
title: "How to Fix Airplane Mode Stuck On an HP Laptop"
slug: how-to-fix-airplane-mode-stuck-on-on-hp-laptop
date: 2026-09-29
categories: ["drivers"]
tags: ["airplane mode", "hp laptop", "wifi stuck", "airplane mode stuck", "wireless"]
description: "Airplane mode stuck on your HP laptop? Fix the stuck toggle with registry edits, service restarts, and driver reinstalls to restore Wi-Fi."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on-on-hp-laptop.webp"
faqs:
  - q: "Why is airplane mode greyed out on my HP laptop?"
    a: "A greyed-out airplane mode toggle usually means the Radio Management Service is stuck or the wireless adapter driver has failed, leaving Windows unable to change the radio state. Restarting the Radio Management Service and reinstalling the Wi-Fi driver resolves most greyed-out cases. A physical wireless switch in the off position can also grey out the toggle."
  - q: "Can the BIOS cause airplane mode to stick?"
    a: "Yes. Some HP BIOS versions have wireless toggles, and if WLAN is disabled there, Windows may show airplane mode as stuck on with no way to clear it in software. Enter the BIOS setup and verify the wireless LAN setting is enabled. BIOS updates can also flip this setting unexpectedly."
  - q: "What is the Radio Management Service?"
    a: "RmSvc, the Radio Management Service, is the Windows service that controls airplane mode and radio states. When it hangs — often after sleep/wake cycles or updates — the airplane mode toggle freezes in its current position. Restarting the service from services.msc usually unfreezes the toggle immediately."
  - q: "Will a network reset fix stuck airplane mode?"
    a: "Often yes. Windows' Network Reset reinstalls all network adapters and resets networking components to defaults, which clears the corrupted radio state keeping airplane mode stuck. It's a heavier step that removes saved Wi-Fi passwords, so try the service restart and driver fixes first, but it's highly effective for stubborn cases."
---

Airplane mode stuck ON is one of the most maddening Windows failures: the toggle won't move, it's greyed out, or it flips back on instantly — and your Wi-Fi and Bluetooth are dead with it. On HP laptops, this usually traces to the Radio Management Service hanging, a wireless driver failure, or a BIOS-level wireless disable that Windows can't override.

The fixes run from instant (service restart) to structural (registry and network reset). Don't skip the physical checks at the start — HP's wireless function keys and BIOS toggles cause a real share of these.

## Why this happens

- **Radio Management Service hung:** The service controlling radio state freezes, usually after sleep/wake or updates, locking the toggle.
- **Wi-Fi driver failed:** If the wireless adapter driver crashes, Windows can't change radio state and the toggle greys out.
- **BIOS wireless disabled:** A BIOS-level WLAN disable overrides Windows entirely — the toggle stays stuck because the hardware is off below the OS.
- **Physical wireless key/switch:** HP's Fn wireless key or a side switch can hard-disable radios in a way the software toggle can't reverse.
- **Corrupted radio state in registry:** The software radio state can desync from hardware reality, and the toggle reflects the corrupted value.
- **Fast Startup preserving the stuck state:** The hung service state survives restarts via Fast Startup's kernel hibernation.
- **Third-party VPN/security software:** Network filter drivers from VPNs can interfere with radio state management.
- **Failing wireless card:** A dying WLAN card that won't initialize leaves the radio permanently "off" from Windows' perspective.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical wireless controls

1. Look for HP's wireless function key (usually **F12** with a radio tower icon and LED — amber means radios off, white/blue means on).
2. Press **Fn + F12** (or F12 alone if Fn-lock is inverted) and watch the LED and the airplane mode toggle.
3. Check the laptop's sides for a physical wireless switch — some HP business models still have one.
4. If the LED won't change from amber, the radio is hard-disabled — continue to the BIOS check (Fix 5).
5. This hardware-level disable overrides everything in Windows, which is why software toggles appear "stuck." The same radio-lock logic affects [general airplane mode issues](/articles/best-way-to-fix-airplane-mode-stuck-on/).

### Fix 2: Restart the Radio Management Service

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Radio Management Service** (RmSvc) in the list.
3. Right-click → **Restart**. If it's stopped, right-click → **Start**, and set **Startup type** to **Manual** or **Automatic**.
4. Immediately check the airplane mode toggle in Quick Settings (**Win + A**).
5. This single restart unfreezes the toggle in a large share of cases — the service hang is the classic cause, especially after the laptop wakes from sleep.

### Fix 3: Toggle via Settings instead of Quick Settings

1. Open **Settings → Network & internet → Airplane mode**.
2. Try the toggle here rather than in Quick Settings — the two sometimes desync, and the Settings page can succeed where the quick toggle fails.
3. Turn airplane mode **On**, wait ten seconds, then turn it **Off**.
4. If the Settings toggle is also greyed out, the problem is deeper (service, driver, or BIOS) — continue below.
5. After successfully turning it off here, verify Wi-Fi and Bluetooth both return in Quick Settings.

### Fix 4: Reinstall the wireless adapter driver

1. In Device Manager, expand **Network adapters** and note your Wi-Fi adapter (Intel, Realtek, MediaTek, or Qualcomm).
2. Right-click → **Uninstall device**, checking **Attempt to remove the driver for this device**.
3. Download the wireless driver for your exact HP model from [HP Support](https://support.hp.com/us-en) and install it.
4. Restart and check the airplane mode toggle.
5. A crashed wireless driver leaves Windows unable to manage radio state — the toggle greys out because there's no working radio to toggle. Fresh HP drivers restore the management path. If the adapter is missing entirely, the [missing adapter guide](/articles/how-to-fix-wifi-adapter-not-showing-up-youtube/) applies.

### Fix 5: Verify wireless is enabled in BIOS

1. Restart and press **F10** (HP's BIOS key) or **Esc** → BIOS Setup.
2. Look for **Wireless** or **WLAN** under Advanced or System Configuration and ensure it's enabled.
3. Save and exit, then test the toggle in Windows.
4. If a BIOS update preceded the stuck airplane mode, check every wireless-related setting — updates reset them more often than HP admits.
5. BIOS-disabled wireless is invisible to Windows' toggle; no software fix can override it.

### Fix 6: Disable Fast Startup and cold boot

1. Open **Control Panel → Power Options → Choose what the power buttons do** → **Change settings that are currently unavailable**.
2. Uncheck **Turn on fast startup** and save.
3. **Shut down** fully (not Restart), wait ten seconds, and power on.
4. Test the airplane mode toggle on the cold boot.
5. Fast Startup hibernates the kernel, preserving the hung Radio Management Service state across "shutdowns" indefinitely — a true cold boot is the only way to clear it.

### Fix 7: Fix the radio state in the registry

1. Press **Win + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\RadioManagement\SystemRadioState`.
2. If the value is **1** (radios off), set it to **0** — back up the key first (right-click → Export).
3. Also check `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ActionCenter\Quick Actions` for stuck toggle state (advanced users only).
4. Restart and test the toggle.
5. Registry desync between the stored radio state and hardware reality is a real, documented cause of permanently stuck toggles — but edit carefully and only as directed.

### Fix 8: Perform a network reset

1. Open **Settings → Network & internet → Advanced network settings → Network reset**.
2. Click **Reset now** and confirm. This reinstalls all network adapters and resets networking components to defaults.
3. The laptop will restart. Reconnect to Wi-Fi afterward (saved networks are forgotten).
4. Test airplane mode toggling. Network reset clears corrupted adapter and radio state that survives driver reinstalls.
5. If airplane mode is STILL stuck after a network reset, cold boot, BIOS check, and driver reinstall, the wireless card hardware is likely failing — [airplane mode troubleshooting](/articles/airplane-mode-stuck-on-troubleshooting/) covers the final hardware isolation steps.

## Closing

Stuck airplane mode on HP laptops is a radio-state problem, and radio state lives in layers: physical key, BIOS toggle, Radio Management Service, wireless driver, registry. Work from the physical layer down and you'll find the layer holding the lock — usually the hung service or a BIOS toggle flipped by an update. The network reset is your heavy artillery for corrupted states that resist everything else.
