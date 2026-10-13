---
title: "How to Fix Airplane Mode Stuck On After a Windows 11 Update"
slug: how-to-fix-airplane-mode-stuck-on-after-windows-11-update
date: 2026-10-10
categories: ["drivers"]
tags: ["airplane mode stuck", "windows 11 wifi fix", "wireless driver update"]
description: "Airplane mode stuck on after a Windows 11 update? Fix the grayed-out toggle, dead Wi-Fi and Bluetooth with these driver and service repairs."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on-after-windows-11-update.webp"
faqs:
  - q: "Why is airplane mode stuck on after updating Windows 11?"
    a: "Updates sometimes replace your wireless driver with a generic version that misreports the radio state, leaving the airplane mode toggle grayed out or stuck. The radio management service can also fail to start. Reinstalling the manufacturer's wireless driver fixes the stuck toggle in most cases."
  - q: "The airplane mode toggle is grayed out. What does that mean?"
    a: "A grayed-out toggle means Windows cannot communicate with the wireless radio at all — usually a driver problem, not a settings issue. It can also indicate the radio management service is stopped or the adapter is disabled in Device Manager. Work through the driver fixes below."
  - q: "Will resetting network settings fix stuck airplane mode?"
    a: "It can help when the problem is corrupted network configuration rather than a driver fault. A network reset reinstalls all adapters and returns settings to defaults. You will need to re-enter Wi-Fi passwords afterward, so have them handy before you reset."
  - q: "Could a physical wireless switch cause this?"
    a: "Yes, though it is rare on modern laptops. Some business laptops still have a physical wireless switch or a Fn-key radio toggle. If the switch is off, Windows shows airplane mode as stuck. Check your keyboard for a wireless icon key and your laptop's edges for a slider switch."
---

You install a Windows 11 update, reboot, and suddenly there is no Wi-Fi, no Bluetooth, and the airplane mode toggle is either stuck on or completely grayed out. Clicking it does nothing. Restarting does nothing. This is one of the most disorienting post-update problems because it cuts off your internet — the very thing you need to research the fix.

The good news: this is almost never broken hardware. Updates frequently swap your wireless driver for a generic one that misreads the radio state, or they leave the radio management service in a failed state. The fixes below restore the toggle and your wireless radios, starting with the quick checks and moving to driver repairs.

## Why this happens

- **Generic wireless driver installed by the update:** The update replaces your Intel, MediaTek, or Realtek wireless driver with a basic one that cannot control the radio properly.
- **Radio Management Service failed:** The service that coordinates airplane mode can get stuck in a stopped or failed state after the update.
- **Airplane mode registry state corrupted:** The update can leave the system-wide radio state flag set to "on" with no working path to clear it.
- **Adapter disabled in Device Manager:** Post-update driver migrations occasionally leave the Wi-Fi adapter in a disabled state that the toggle cannot override.
- **Physical wireless switch or Fn key:** A hardware radio kill switch engaged during the update (or a stuck Fn toggle) locks airplane mode on at the firmware level.
- **Power management cutting the adapter:** Aggressive power settings can keep the wireless adapter powered down, which Windows interprets as airplane mode.
- **Corrupted network stack:** The update can damage Winsock or TCP/IP configuration, which cascades into radio management failures.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical switch and Fn-key toggle

Rule out hardware before touching software — it takes ten seconds.

1. Look along the sides and front edge of your laptop for a small wireless slider switch. If you find one, slide it to the on position.
2. Check your function keys for a wireless/airplane icon (often **F2**, **F7**, or **F12**). Press **Fn + that key** to toggle the radio.
3. Watch the taskbar network icon as you do this — if it flickers or changes, the hardware switch was the issue.

Business laptops from Dell and Lenovo are the most likely to have these switches. If nothing changes, the problem is software, and the toggle should respond to the fixes below.

### Fix 2: Restart the Radio Management Service

This service owns the airplane mode state, and restarting it clears many stuck toggles.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **Radio Management Service** in the list.
3. If it is not running, right-click it and choose **Start**. If it is running, choose **Restart**.
4. Double-click it, set **Startup type** to **Manual** (its normal setting), and click **OK**.
5. Try the airplane mode toggle again in **Settings > Network & internet > Airplane mode**.

If the service refuses to start or immediately stops, note any error message — it usually points at the underlying driver problem that Fix 3 addresses.

### Fix 3: Reinstall the wireless driver from the manufacturer

This is the fix that resolves most post-update stuck airplane mode cases.

1. Open **Device Manager** and expand **Network adapters**. Note whether your Wi-Fi adapter appears, shows a warning, or is missing entirely.
2. Visit [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/) for your exact model and download the wireless/WLAN driver.
3. If you have no internet on the laptop, download it on your phone and transfer it via USB.
4. In Device Manager, right-click the wireless adapter, choose **Uninstall device**, and check **Attempt to remove the driver for this device**.
5. Run the manufacturer's installer and restart.

The vendor driver restores proper radio control, and the airplane mode toggle starts working again. If your adapter was missing from Device Manager entirely, see our guide on [fixing Wi-Fi that disappeared from the laptop](/articles/best-way-to-fix-wifi-disappeared-from-laptop/), which covers the deeper detection problem.

### Fix 4: Clear the stuck radio state in the registry

When the toggle is grayed out because Windows thinks airplane mode is permanently on, you can reset the flag directly.

1. Press **Win + R**, type `regedit`, and press **Enter**. Click **Yes** on the UAC prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\RadioManagement\SystemRadioState`.
3. Double-click the default value and set it to **0** (off).
4. Also check `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ActionCenter\Quick Actions` — but the first key is the critical one.
5. Restart the laptop and test the toggle.

Back up the registry key first (right-click > **Export**). This fix is specifically for the corrupted-state scenario where everything else looks fine but the toggle will not budge.

### Fix 5: Run the network reset

A network reset reinstalls every network adapter and returns all network settings to factory defaults.

1. Go to **Settings > Network & internet > Advanced network settings**.
2. Click **Network reset**, then **Reset now**, and confirm.
3. The laptop will restart. After booting, rejoin your Wi-Fi network with your password.

You will lose saved Wi-Fi passwords, VPN profiles, and custom DNS settings, so have your Wi-Fi password ready. This is the broad hammer that fixes corrupted-stack variants of the problem — and our [airplane mode troubleshooting hub](/articles/best-way-to-fix-airplane-mode-stuck-on/) covers related toggle issues in more depth.

### Fix 6: Disable power management on the wireless adapter

If the adapter keeps getting powered down, Windows reads that as "radio off" and locks airplane mode on.

1. In Device Manager, expand **Network adapters** and double-click your Wi-Fi adapter.
2. Open the **Power Management** tab and uncheck **Allow the computer to turn off this device to save power**.
3. Click **OK** and restart.

While you are here, check the **Advanced** tab for any vendor-specific power or radio properties set to aggressive values and return them to defaults.

### Fix 7: Reset Winsock and the TCP/IP stack

When the network stack itself is damaged, radio management can fail as a side effect.

1. Open **Terminal** or **Command Prompt** as administrator.
2. Run these commands one at a time, pressing Enter after each:
   - `netsh winsock reset`
   - `netsh int ip reset`
   - `ipconfig /release`
   - `ipconfig /renew`
   - `ipconfig /flushdns`
3. Restart the laptop.

These commands rebuild the core networking components from scratch. Microsoft's official guidance on network repair lives on the Windows support site if you want to read more about what each command does.

## Closing

Airplane mode stuck on after a Windows 11 update feels catastrophic because it kills your connectivity, but the cause is almost always a driver swap or a stuck service rather than dead hardware. Check the physical switch, restart the Radio Management Service, and reinstall the manufacturer's wireless driver — that sequence brings the toggle (and your Wi-Fi) back to life in the overwhelming majority of cases.
