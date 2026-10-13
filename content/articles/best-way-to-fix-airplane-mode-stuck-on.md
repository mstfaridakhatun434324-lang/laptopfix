---
title: "The Best Way to Fix Airplane Mode Stuck On"
slug: "best-way-to-fix-airplane-mode-stuck-on"
date: "2026-10-03"
categories: ["drivers"]
tags: ["airplane mode", "stuck", "wifi", "windows 11", "troubleshooting"]
description: "Airplane mode won't turn off on your laptop? Fix the stuck toggle with radio management, driver repairs, and BIOS checks."
thumbnail: "/images/thumbs/best-way-to-fix-airplane-mode-stuck-on.webp"
faqs:
  - q: "Why is airplane mode stuck on my laptop?"
    a: "The usual causes are a physical wireless switch in the off position, a stuck Fn-key radio toggle, a corrupted wireless driver, or the Radio Management Service failing. Check for a physical switch first, then try the Settings toggle. If the toggle is greyed out, the driver or service needs repair."
  - q: "How do I turn off airplane mode when the button is greyed out?"
    a: "A greyed-out toggle usually means Windows cannot control the radio because of a driver problem or a hardware switch. Restart the Radio Management Service, reinstall the Wi-Fi driver, and check for a physical wireless switch on the laptop. The [post-update airplane mode guide](/articles/how-to-fix-airplane-mode-stuck-on-after-windows-11-update/) covers the update-triggered case."
  - q: "Can a BIOS setting lock airplane mode on?"
    a: "Yes. Some laptops have a BIOS option for wireless control that can force the radio off. Additionally, the physical wireless switch on some models is wired to report its state to the BIOS. If software fixes fail, check the BIOS wireless settings and the position of any physical switch."
  - q: "Will a network reset fix stuck airplane mode?"
    a: "It often helps when the problem is corrupted network configuration. Network reset reinstalls all network adapters and returns their settings to defaults, which can unstick the airplane mode state. You will need to re-enter Wi-Fi passwords afterward, so note them down first."
---

You flip the airplane mode toggle off, and it flips itself right back on. Or the toggle is greyed out entirely, mocking you while your Wi-Fi sits dead. Airplane mode is supposed to be a convenience; when it sticks, it feels like the laptop has been grounded.

Stuck airplane mode is a radio-control problem. Something in the chain between the toggle and the wireless hardware is broken: a physical switch, the Fn-key radio control, the Radio Management Service, or the wireless driver. Each has a distinct fix. A related symptom is [Wi-Fi disappearing entirely](/articles/wifi-disappeared-windows-11-no-wifi-option/).

Work through these fixes in order, starting with the physical checks that take seconds.

## Why this happens

- **A physical wireless switch is off:** Many business laptops have a side switch that overrides all software toggles.
- **The Fn-key radio toggle is stuck:** The wireless function key can leave the radio in a state the Settings toggle cannot change.
- **The Radio Management Service failed:** This Windows service brokers radio control; when it stops, the toggle breaks.
- **A corrupted wireless driver:** The driver reports the radio state to Windows; a broken driver reports it wrong.
- **BIOS wireless control:** Some BIOS versions manage the radio independently of Windows.
- **Corrupted network configuration:** Tangled adapter settings can lock the airplane mode state.
- **A stuck state from Fast Startup:** The hibernated kernel can preserve a stuck radio state across reboots.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical wireless switch

This is the classic gotcha. A physical switch in the off position overrides every software toggle on the laptop, and the switch is easy to bump in a bag.

1. Inspect the sides and front edge of the laptop for a wireless switch or slider.
2. If you find one, slide it to the on position.
3. Watch for the Wi-Fi indicator light to change.
4. Try the airplane mode toggle in Settings again.
5. On some models the switch is a tiny recessed slider; check the manual if unsure.

### Fix 2: Toggle the radio with the Fn key

The function-row wireless key controls the radio at a lower level than the Settings toggle. Cycling it can unstick a radio that software toggles cannot reach.

1. Find the wireless or airplane icon on your function keys.
2. Press Fn plus that key and wait a few seconds.
3. Press it again to toggle back, watching the on-screen indicator.
4. Try the Settings airplane mode toggle after each Fn press.
5. If the key does nothing, the hotkey driver may need reinstalling from the maker.

### Fix 3: Restart the Radio Management Service

This service is the middleman between the airplane mode toggle and the radios. When it stops or wedges, the toggle loses its connection to the hardware.

1. Press Windows + R, type services.msc, and press Enter.
2. Find Radio Management Service in the list.
3. If it is stopped, right-click and start it; if running, restart it.
4. Set its startup type to Manual or Automatic.
5. Try the airplane mode toggle immediately afterward.

### Fix 4: Reinstall the Wi-Fi driver

The wireless driver reports radio state to Windows. A corrupted driver can report the radio as off permanently, which manifests as airplane mode stuck on.

1. Open Device Manager and expand Network adapters.
2. Uninstall the Wi-Fi adapter, deleting the driver software.
3. Restart the laptop.
4. Install the latest Wi-Fi driver from the manufacturer's support page.
5. Test the airplane mode toggle after the fresh driver loads.

### Fix 5: Perform a network reset

When the adapter configuration itself is tangled, resetting the entire network stack clears the stuck state along with every adapter and profile.

1. Note down your Wi-Fi passwords first; they will be erased.
2. Open Settings, then Network and internet, then Advanced network settings.
3. Choose Network reset and confirm; the laptop restarts.
4. After reboot, toggle airplane mode off.
5. Reconnect to your Wi-Fi network and verify the toggle stays off.

### Fix 6: Disable Fast Startup to clear the stuck state

Fast Startup preserves the kernel state across shutdowns, including a wedged radio state. A true cold boot is the only way to clear it.

1. Open Power Options and click Choose what the power buttons do.
2. Click Change settings that are currently unavailable.
3. Uncheck Turn on fast startup and save.
4. Shut down completely, wait ten seconds, and power on.
5. Check whether airplane mode now toggles normally.

### Fix 7: Check the BIOS wireless settings

As a final software step, verify the BIOS is not forcing the radio off. Some enterprise BIOS configurations manage wireless independently.

1. Restart and enter the BIOS setup.
2. Look for Wireless, WLAN, or Radio settings.
3. Ensure wireless is enabled and not locked by an administrator policy.
4. Load BIOS defaults if the settings look inconsistent.
5. Save, exit, and test the toggle in Windows.

### Fix 8: Update the BIOS for radio firmware fixes

Radio control runs partly in firmware below Windows, and BIOS updates regularly fix stuck airplane mode states that survive every operating-system repair. Manufacturers document these in update notes mentioning wireless, radio, or airplane mode behavior.

1. Check your current BIOS version in System Information.
2. Look for BIOS updates mentioning wireless, radio, or airplane mode fixes.
3. Apply the update exactly as the manufacturer instructs; do not interrupt it.
4. Load BIOS defaults afterward and confirm wireless is enabled.
5. Boot Windows and test the airplane mode toggle thoroughly.

## Closing

Stuck airplane mode is almost always a control problem, not a broken radio: a physical switch, a wedged service, or a tired driver. The physical checks and the service restart resolve most cases in minutes. When the toggle stays stuck through all of these, or the [Wi-Fi adapter has vanished too](/articles/how-to-fix-wifi-disappeared-from-laptop-in-windows-11-24h2/), the wireless card itself deserves a closer look and possibly a professional replacement at a service center.
