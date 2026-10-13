---
title: "Airplane Mode Stuck On? Turn It Off for Good"
slug: how-to-fix-airplane-mode-stuck-on
date: 2026-09-22
categories: ["drivers"]
tags: ["airplane mode", "stuck", "wifi", "bluetooth", "wireless"]
description: "Airplane mode won't turn off on your Windows laptop? Fix the greyed-out toggle with driver, service, and BIOS-level repairs."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on.webp"
faqs:
  - q: "Why is airplane mode stuck on in Windows 11?"
    a: "The most common causes are a physical wireless switch or function key holding the radio off, the Radio Management Service being disabled, or a corrupted network adapter driver that Windows can't reinitialize. Less commonly, a BIOS-level wireless disable or a stuck embedded-controller state keeps the radio off regardless of what Windows tries. Work from the physical switch inward."
  - q: "Airplane mode toggle is greyed out. How do I enable Wi-Fi?"
    a: "A greyed-out toggle means something below Windows is forcing the radio off. Check for a physical wireless switch on the laptop's edge and the Fn wireless key combo first. Then check Device Manager for disabled network adapters (View > Show hidden devices, right-click > Enable). If those are fine, restart the Radio Management Service and check BIOS for a wireless disable option."
  - q: "Can I turn off airplane mode from the command line?"
    a: "Partially. You can restart the relevant services and reset the network stack from an elevated terminal (netsh winsock reset, for example), but there's no single command that overrides a stuck airplane mode when the cause is a physical switch or disabled driver. The command line is useful for the service and stack repairs, not as a magic toggle."
  - q: "Will a network reset fix stuck airplane mode?"
    a: "Sometimes — Network reset (Settings > Network & internet > Advanced network settings > Network reset) reinstalls all network adapters and resets their configuration, which clears driver-level stuck states. It wipes saved Wi-Fi networks and VPNs, so it's a later step, not a first one. Try the physical switch, services, and driver fixes before resetting."
---

Airplane mode stuck on is uniquely maddening: one toggle kills Wi-Fi, Bluetooth, and cellular at once, and when the toggle itself refuses to move — greyed out, instantly snapping back on — the laptop is effectively offline with no obvious recourse. The key insight is that airplane mode is a *command* to the radios, not just a setting. When it sticks, something between Windows and the radio hardware is refusing the command: a physical switch, a dead service, a broken driver, or firmware.

Work from the outside in: physical controls first, then Windows services, then drivers, then firmware. If your whole wireless stack vanished rather than just being toggled, see [Wi-Fi disappeared](/articles/wifi-disappeared-windows-11-no-wifi-option/); for Bluetooth-specific fallout, [Bluetooth not working](/articles/how-do-i-fix-bluetooth-not-working/).

## Why this happens

- **Physical wireless switch or Fn key engaged**: A hardware switch on the laptop's edge (or Fn+F-key combo) forces radios off below the OS level.
- **Radio Management Service disabled**: The Windows service that executes radio on/off commands is stopped or disabled.
- **Corrupted network adapter drivers**: The Wi-Fi/Bluetooth drivers can't reinitialize when Windows commands the radio back on.
- **Stuck embedded controller state**: The firmware-level controller remembers "radios off" across reboots.
- **BIOS wireless disable**: A BIOS option disabling wireless, sometimes toggled by updates resetting BIOS settings.
- **Third-party VPN/security software**: Network filter drivers from VPNs or security suites interfering with adapter state changes.
- **Corrupt network stack**: Winsock/TCP-IP corruption preventing adapters from coming back online.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check physical switches and function keys

The outside-in start — this solves more cases than you'd expect.

1. Inspect the laptop's edges (front edge and sides) for a physical wireless switch — a tiny slider, increasingly rare but still present on business laptops (ThinkPads, Latitudes).
2. Look for a wireless/airplane icon on your function keys — press it, trying both with and without **Fn** held.
3. Watch the on-screen indicator or the taskbar network icon after each press — you're looking for the airplane icon to clear.
4. If you use a docking station, check it too — some docks have their own wireless toggles.
5. After toggling any physical control, wait 10 seconds before judging — radio hardware takes a moment to reinitialize.

### Fix 2: Restart the Radio Management Service

The service that actually executes the toggle.

1. Press **Win + R**, type `services.msc`, and find **Radio Management Service**.
2. If it's not running, right-click > **Start**. Set **Startup type** to **Manual** (its default) — not Disabled.
3. Also verify **WLAN AutoConfig** and **Bluetooth Support Service** are running — airplane mode recovery depends on them.
4. Try the airplane mode toggle again in Quick Settings (**Win + A**) or **Settings** > **Network & internet** > **Airplane mode**.
5. If the service was disabled by a debloat script or "privacy" tool, consider what else that tool changed — they frequently break more than they fix.

### Fix 3: Re-enable adapters in Device Manager

When Windows turned the adapters off and can't turn them back on.

1. Press **Win + X** > **Device Manager**, click **View** > **Show hidden devices**.
2. Expand **Network adapters** — look for greyed-out Wi-Fi and Bluetooth entries. Right-click each > **Enable device**.
3. If an adapter shows a warning icon instead, right-click > **Properties** and read the error — then update or roll back its driver as appropriate.
4. After enabling, click **Action** > **Scan for hardware changes**.
5. Try the airplane toggle again. If adapters enable but immediately disable, a driver or service is fighting you — continue.

### Fix 4: Power-drain the embedded controller

Clear the firmware-level "radios off" memory.

1. Shut down completely, unplug AC and all peripherals.
2. Hold the power button for 30 seconds (remove the battery first if it's removable).
3. Reconnect AC only, power on, and immediately check the airplane toggle before Windows loads extra software.
4. This resets the embedded controller that manages radio power at firmware level — stuck EC states survive normal reboots and cause exactly this symptom.
5. If the toggle works right after the drain but sticks again later, something in software is re-breaking it — suspect third-party network tools (Fix 6).

### Fix 5: Reinstall the wireless drivers

Driver-level stuck states need driver-level repair.

1. In **Device Manager** > **Network adapters**, right-click the Wi-Fi adapter > **Uninstall device**, checking **Attempt to remove the driver** if offered.
2. Do the same for the Bluetooth adapter (internal Bluetooth usually shares the wireless card).
3. Restart — Windows reinstalls inbox drivers for both.
4. For the lasting fix, install the proper driver: Intel cards via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), others from your manufacturer's support page (Dell, HP, or Lenovo).
5. After the driver reinstall, toggle airplane mode off and confirm both Wi-Fi and Bluetooth return. See our [Wi-Fi driver reinstall guide](/articles/best-way-to-reinstall-wifi-driver/) for the full controlled procedure.

### Fix 6: Remove interfering third-party network software

VPNs and security suites that hijack the adapters.

1. Temporarily uninstall VPN clients, third-party firewalls, and "network optimizer" utilities — their filter drivers sit between Windows and the adapter and can block state changes.
2. Restart after each uninstall and test the airplane toggle.
3. If the toggle works after removing something, that's your culprit — reinstall only a current version, or switch to Windows' built-in VPN client for standard protocols.
4. Also check for manufacturer "connection manager" utilities that duplicate Windows' radio controls — disable their radio management features.
5. Re-enable Windows Defender Firewall after removing third-party firewalls so you're not left unprotected.

### Fix 7: Check BIOS and reset the network stack

The deepest software layers.

1. Restart into BIOS/UEFI and look for **Wireless**, **WLAN**, **Bluetooth**, or **Radio** options under Advanced/Security/Devices — ensure they're all **Enabled**.
2. If a BIOS update preceded the problem, **Load Optimized Defaults**, save, and cold-boot.
3. Back in Windows, open an elevated terminal and run `netsh winsock reset` and `netsh int ip reset`, then restart.
4. As the last software step: **Settings** > **Network & internet** > **Advanced network settings** > **Network reset** > **Reset now**. This reinstalls every network adapter — you'll re-enter Wi-Fi passwords afterward. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents this process officially.
5. If airplane mode is still stuck after a network reset with BIOS wireless enabled, the wireless card's firmware or the card itself is likely failed — a USB Wi-Fi adapter is the pragmatic workaround, and internal card replacement is a cheap shop repair.

## Closing

Stuck airplane mode is a chain-of-command problem: Windows issues the order, but a physical switch, a dead service, a broken driver, or firmware can each refuse it. Work the chain from the outside in — switch, service, driver, firmware — and you'll find the link that's refusing. Most of the time it's the physical switch nobody remembered existed.
