---
title: "How to Fix a Missing Network Adapter on an Acer Laptop"
slug: how-to-fix-network-adapter-missing-on-acer-laptop
date: 2026-10-03
categories: ["drivers"]
tags: ["network adapter missing", "acer laptop", "wifi missing", "ethernet adapter"]
description: "Fix a missing network adapter on an Acer laptop: restore the vanished Wi-Fi or Ethernet adapter in Device Manager and get back online."
thumbnail: "/images/thumbs/how-to-fix-network-adapter-missing-on-acer-laptop.webp"
faqs:
  - q: "Why did my Wi-Fi adapter disappear from Device Manager?"
    a: "The adapter is usually hidden because its driver failed to load, or it was disabled. Windows updates, corrupted drivers, BIOS wireless settings, and power-management faults are the common causes. Enabling Show hidden devices in Device Manager reveals it in most cases, and the fix is driver repair rather than hardware replacement."
  - q: "The network icon is gone from the taskbar too. Is that the same problem?"
    a: "Yes — when the adapter vanishes, Windows removes the network flyout options that depend on it. Restoring the adapter in Device Manager brings the taskbar icon back automatically. Do not chase taskbar settings; fix the adapter and the UI follows."
  - q: "Can airplane mode make the adapter disappear?"
    a: "Airplane mode disables the radio but should not remove the adapter from Device Manager. However, a stuck airplane mode state combined with a driver fault can look like a missing adapter. Toggle airplane mode off, check the physical wireless switch, and then investigate the driver if the adapter is still absent."
  - q: "What if neither Wi-Fi nor Ethernet adapters appear?"
    a: "Both missing simultaneously points to a system-level cause: a corrupted network stack, a bad Windows update, BIOS settings disabling onboard devices, or a failed chipset driver. Run a network reset, check BIOS, and reinstall chipset drivers before suspecting two simultaneous hardware failures — which is very unlikely."
---

A network adapter that vanishes from an Acer laptop takes all connectivity with it — no Wi-Fi networks listed, no Ethernet, and the taskbar network icon reduced to a globe or gone entirely. It feels like the networking hardware died, but adapters rarely die; what happens far more often is that Windows stops loading the driver, hides the device, and leaves you offline with no obvious explanation.

This guide restores the adapter systematically: reveal hidden devices, repair the driver, check the BIOS and physical switches that can suppress the radio, reset the network stack, and determine definitively whether hardware is involved.

Network adapters live or die by their NDIS miniport drivers — the Windows driver model for network interfaces — and the failure modes are distinctive. When the miniport driver fails to load, Windows does not show you a broken adapter with an error; it hides the adapter entirely and tears down everything built on top of it, including the taskbar network icon and the Wi-Fi settings page. This cascade is why a missing adapter feels so total: it is not just the hardware entry that disappears, but the entire networking UI that depended on it. The recovery therefore has to rebuild from the bottom — the driver itself — before anything above it can come back. There is a useful corollary: if both Wi-Fi and Ethernet vanish simultaneously, suspect something they share (the network stack, a Windows update, BIOS settings) rather than two independent hardware failures, because two adapters dying at once is extraordinarily unlikely.

## Why this happens

- **Driver failed to load:** Windows hides the adapter instead of showing a broken one.
- **Windows Update damage:** Updates corrupt or replace the network driver.
- **Device disabled:** Disabled adapters vanish from the default view.
- **BIOS wireless disabled:** Acer BIOS can disable WLAN/LAN devices at hardware level.
- **Physical wireless switch:** Some Acer models have a hardware switch or Fn-key toggle that kills the radio.
- **Power management fault:** The adapter fails to resume and drops out of enumeration.
- **Corrupted network stack:** Winsock/TCP-IP damage can cascade into adapter presentation issues.
- **Hardware failure:** Dead wireless card or Ethernet controller — uncommon, verified last.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Show hidden devices and rescan

1. Open **Device Manager → View → Show hidden devices → Network adapters**.
2. If the adapter appears greyed out, right-click → **Enable device** and restart.
3. Check **Other devices** for **Network Controller** — the adapter awaiting its driver.
4. Click **Action → Scan for hardware changes** and watch for the adapter to reappear.

### Fix 2: Check wireless switches and airplane mode

1. Look for a physical wireless switch on the laptop's sides or front edge and ensure it is on.
2. Press the **Fn + wireless key** (often F3 on Acer) to toggle the radio.
3. Open **Settings → Network & internet** and make sure **Airplane mode** is off.
4. These hardware-level kills override every software fix, so rule them out before touching drivers.

### Fix 3: Reinstall the network driver

1. If the adapter is visible (even hidden), right-click → **Uninstall device**, checking driver removal if offered.
2. Restart — Windows will attempt to reinstall.
3. Download the **Wireless LAN** and/or **LAN** driver for your exact model from Acer's support site using another device, transfer via USB, and install.
4. Prefer Acer's package — wireless behavior is tuned per model, the same reason [MediaTek Wi-Fi issues](/articles/how-to-fix-mediatek-wifi-not-working-step-by-step/) respond best to OEM drivers.

### Fix 4: Reset the network stack

1. Open **Settings → Network & internet → Advanced network settings → Network reset → Reset now**, then restart.
2. Alternatively, in an elevated Command Prompt: **netsh winsock reset**, **netsh int ip reset**, then restart.
3. After the reset, check Device Manager — Windows reinstalls adapters fresh, clearing corrupted enumeration.
4. Reconnect to Wi-Fi afterward; saved networks are cleared by the reset.

### Fix 5: Check BIOS settings

1. Restart and press **F2** to enter Acer BIOS setup.
2. Look for **Wireless**, **WLAN**, **LAN**, or **Onboard Devices** settings and ensure they are **Enabled**.
3. Choose **Load Setup Defaults** to clear any misconfiguration, save, and exit.
4. A BIOS-disabled radio produces a missing adapter regardless of drivers — this check is mandatory before concluding hardware failure.

### Fix 6: Reinstall the chipset driver

1. Download the **chipset driver** for your model from Acer's support site and install as administrator.
2. Restart and rescan for hardware changes in Device Manager.
3. The chipset driver owns PCI bus enumeration — a missing network adapter after a clean install is often just a missing chipset driver, exactly as with [missing display adapters](/articles/how-to-fix-display-adapter-missing-on-acer-laptop/).
4. Verify **System devices** in Device Manager shows no warnings after installation.

### Fix 7: Power management and selective suspend

1. If the adapter appears, open its **Properties → Power Management** and uncheck power-saving.
2. Disable **USB selective suspend** if you use a USB network adapter.
3. Test specifically across sleep/wake cycles — adapters that vanish after sleep point here.
4. Disable **Fast Startup** to stop broken resume states from persisting across reboots.

### Fix 8: Hardware determination

1. Boot a **Linux live USB** — network adapters visible and working there means Windows is the problem.
2. Run Acer's hardware diagnostics on the network devices.
3. If the wireless card never appears anywhere, it may have failed — on many Acer laptops it is a replaceable M.2 module.
4. For built-in Ethernet that never links, a USB Ethernet adapter is the practical workaround. Microsoft's network recovery guidance is at [Microsoft support](https://support.microsoft.com/en-us/windows), and [Code 10 diagnostics](/articles/wifi-driver-code-10-error-troubleshooting/) apply if the adapter reappears with an error.

## Closing

A missing network adapter on an Acer laptop is an enumeration or driver problem in nearly every case — not dead hardware. Reveal hidden devices, rule out the physical switches, reinstall Acer's network and chipset drivers, reset the network stack, and verify BIOS has the radio enabled. The Linux live-USB test at the end gives you a definitive hardware verdict for the rare cases that resist everything else.
