---
title: "Airplane Mode Stuck On? Fix It on Your Acer Laptop"
slug: how-to-fix-airplane-mode-stuck-on-on-acer-laptop
date: 2026-09-25
categories: ["drivers"]
tags: ["airplane mode", "acer laptop", "wifi fix", "wireless", "windows 11"]
description: "Airplane mode stuck on your Acer laptop and won't turn off? Diagnose the stuck toggle, radio drivers, and physical switch with this step-by-step technician's guide."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on-on-acer-laptop.webp"
faqs:
  - q: "Why is airplane mode greyed out on my Acer laptop?"
    a: "A greyed-out airplane mode toggle almost always means Windows cannot reach the wireless radio driver. The Wi-Fi adapter driver is missing, disabled, or crashed, so the Settings page has no radio to command. Check Device Manager under Network adapters first — if the Wi-Fi device is absent or flagged with a warning icon, reinstall or re-enable its driver and the toggle will unlock."
  - q: "Can a BIOS setting lock airplane mode on?"
    a: "Yes. Some Acer BIOS versions include a wireless device control option that can disable the radio at firmware level, which Windows then cannot override. Enter the BIOS with F2 during boot, look for a wireless or radio setting under the Advanced or Main tab, and make sure WLAN is enabled. This is rare on consumer models but worth checking when nothing else works."
  - q: "Does the Acer keyboard shortcut override Windows airplane mode?"
    a: "On many Acer laptops, the Fn+F3 (or Fn with a wireless icon key) toggles the radio independently of the Windows setting. If that key combination was pressed, Windows may show airplane mode as on with no clickable fix. Pressing Fn+F3 again often clears it immediately. Try this before any deeper troubleshooting."
  - q: "Will reinstalling Windows fix a stuck airplane mode?"
    a: "Reinstalling Windows can fix it if the cause is a corrupt driver or broken settings database, but it will not fix a faulty physical switch, a dead Wi-Fi card, or a disabled radio in BIOS. Treat reinstallation as a last resort. Work through driver resets, the radio management service, and the registry fix in this guide first — they resolve the vast majority of cases."
---

Airplane mode that refuses to turn off is one of the most disorienting Windows problems: everything looks fine, the toggle just snaps back on, and your laptop behaves like it's sealed in a metal box. On Acer laptops this complaint comes up again and again, and the root cause is rarely the toggle itself — it's the wireless radio, its driver, or a service underneath it that has stopped responding.

The good news is that the fix is almost never expensive. In the field, roughly nine out of ten stuck airplane mode cases on Acer machines trace back to a driver state issue, a stuck Radio Management service, or an accidentally pressed function key. The remaining cases are hardware — a dead Wi-Fi card or a failed keyboard switch. This guide walks you through the diagnosis in the right order so you find out which camp you're in within about thirty minutes.

## Why this happens

- **Wireless driver in a bad state:** The Wi-Fi adapter driver can crash or partially load so that Windows sees the radio as permanently off. The airplane mode toggle then has nothing to switch, and it stays stuck.
- **Radio Management service stopped:** Windows uses the Radio Management service (RmSvc) to handle airplane mode. If it's disabled or hung, the toggle becomes cosmetic — it moves but changes nothing.
- **Function key pressed accidentally:** Acer laptops map wireless control to Fn+F3 on many models. One stray press puts the radio in a state the Windows toggle can't reverse without pressing the key again.
- **Airplane mode stuck in the registry:** A corrupted value under the Windows radio settings registry key can pin the state to "on" across reboots, surviving even driver reinstalls.
- **BIOS-level radio disable:** Some Acer BIOS builds include a wireless device switch. If WLAN is disabled there, Windows 11 will report airplane mode as permanently on.
- **Failed Windows update:** Feature updates to Windows 11 24H2 occasionally leave the old radio driver half-migrated, producing a [stuck toggle after an update](/articles/how-to-fix-airplane-mode-stuck-on-after-windows-11-update/) until the driver is refreshed.
- **Power management turning the radio off:** Windows' power saver can be allowed to switch off the Wi-Fi adapter, and on some Acer models the radio never comes back up, leaving airplane mode locked on.
- **Failing Wi-Fi card:** A Wi-Fi module with a cracked solder joint or a dying radio can report itself as perpetually disabled. If nothing software-side changes the state, suspect hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Try the Acer function key first

1. Press **Fn+F3** on your Acer keyboard (on some models the wireless icon is on F3; on newer models it may be a dedicated key — check the icon).
2. Wait five seconds and watch the Wi-Fi icon in the taskbar.
3. Open **Settings > Network & internet** and check whether the airplane mode toggle now responds.
4. If nothing changed, try the key combination with the laptop plugged in and on battery — power state occasionally affects the key's behavior.

### Fix 2: Restart the Radio Management service

1. Press **Win+R**, type `services.msc`, and press Enter.
2. Scroll to **Radio Management service**.
3. Right-click it and choose **Restart**. If it's not running, choose **Start**.
4. Double-click it and set **Startup type** to **Automatic**.
5. Go back to Settings and try the airplane mode toggle again. If the toggle now moves, the stuck service was your whole problem — a situation the [24H2-specific guide](/articles/how-to-fix-airplane-mode-stuck-on-in-windows-11-24h2/) covers in more depth for the latest Windows build.

### Fix 3: Re-enable the Wi-Fi adapter in Device Manager

1. Press **Win+X** and open **Device Manager**.
2. Expand **Network adapters** and find your Wi-Fi device (Intel, Realtek, MediaTek, or Qualcomm).
3. If it shows a down arrow, right-click it and choose **Enable device**.
4. If it's missing entirely, click **Action > Scan for hardware changes** and watch for it to appear.
5. Right-click the adapter, choose **Properties > Power Management**, and uncheck **Allow the computer to turn off this device to save power**.

### Fix 4: Reinstall the wireless driver cleanly

1. In Device Manager, right-click the Wi-Fi adapter and choose **Uninstall device**.
2. Tick **Attempt to remove the driver for this device** if the checkbox appears, then confirm.
3. Restart the laptop. Windows will attempt to reinstall a driver automatically.
4. If the adapter is still broken, visit the [official Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) for guided driver recovery steps, then install the latest wireless driver from Acer's support site for your exact model.
5. Restart once more and test the airplane mode toggle.

### Fix 5: Reset the network stack

1. Open **Settings > Network & internet > Advanced network settings**.
2. Click **Network reset**, then **Reset now**, and confirm.
3. The laptop will restart. This clears saved Wi-Fi networks, VPN adapters, and virtual switches, rebuilding the network stack from scratch.
4. After the reboot, set up your Wi-Fi connection again and confirm airplane mode stays off.

### Fix 6: Clear the stuck registry value

1. Press **Win+R**, type `regedit`, and press Enter. Confirm the UAC prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\RadioManagement\SystemRadioState`.
3. Double-click the value on the right. If its data is `1`, change it to `0` and click OK.
4. Also check the same path for a `Default` or user-profile subkey with a stuck state and correct it the same way.
5. Restart the laptop and test. Back up the registry key first (File > Export) in case you need to restore it.

### Fix 7: Check the BIOS wireless setting

1. Restart the laptop and press **F2** repeatedly during the Acer logo to enter the BIOS.
2. Look under **Advanced** or **Main** for a **WLAN**, **Wireless**, or **Radio** option.
3. Make sure it is set to **Enabled**, then save and exit (usually F10).
4. If the setting was already enabled, the BIOS is innocent — move on. While you're here, note that a [pending BIOS update](/articles/how-to-update-bios-on-laptop-in-windows-11-24h2/) can also resolve radio control bugs on some Acer boards.

## Closing

A stuck airplane mode on an Acer laptop is frustrating precisely because the fix is usually trivial — a function key, a stalled service, or a driver that needs a clean reinstall. Work the list top to bottom, and in most cases you'll have your wireless back before you reach the BIOS step. If every software fix fails and the adapter is invisible in Device Manager even after a scan, the Wi-Fi card itself is the likely culprit, and a replacement module or USB Wi-Fi adapter is the practical next step.
