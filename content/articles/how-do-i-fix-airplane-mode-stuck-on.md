---
title: "How Do I Fix Airplane Mode Stuck On? 7 Proven Fixes"
slug: how-do-i-fix-airplane-mode-stuck-on
date: 2026-10-05
categories: ["drivers"]
tags: ["airplane mode", "stuck", "wifi", "bluetooth", "wireless switch"]
description: "Airplane mode stuck on and won't turn off? Fix it with toggle resets, driver repair, service restarts, and BIOS checks — step by step."
thumbnail: "/images/thumbs/how-do-i-fix-airplane-mode-stuck-on.webp"
faqs:
  - q: "Why won't airplane mode turn off on my laptop?"
    a: "The usual causes are a stuck software toggle, a disabled Radio Management Service, a corrupted network adapter driver, or a physical wireless switch in the off position. Windows thinks the radios should stay off and keeps re-enabling airplane mode. The fixes in this guide address each cause in order of likelihood."
  - q: "Can a Windows update cause airplane mode to get stuck?"
    a: "Yes, this is a well-known pattern. Updates can corrupt the network adapter driver or reset the Radio Management Service to a disabled state, which locks airplane mode on. Reinstalling the Wi-Fi driver and setting the service back to manual or automatic resolves most post-update cases."
  - q: "My laptop has no physical wireless switch. What else could lock it?"
    a: "Check the Fn-key wireless toggle, the BIOS wireless setting, and the Radio Management Service. Some laptops also have airplane mode tied to a BIOS-level radio control. If none of those apply, the network adapter driver itself is the prime suspect and should be reinstalled cleanly."
  - q: "Will resetting network settings fix stuck airplane mode?"
    a: "Often, yes. A network reset reinstalls all network adapters and returns networking components to defaults, which clears the corrupted state that holds airplane mode on. You will lose saved Wi-Fi passwords, so note them first. It is one of the most reliable fixes when simpler toggles fail."
---

Airplane mode stuck on is one of those problems that makes you feel like the laptop is mocking you. You click the toggle, it flips back. You turn it off in Settings, it turns itself on again. Meanwhile Wi-Fi and Bluetooth are dead and nothing you click seems to matter. The underlying story is simple: something — a service, a driver, a switch — keeps telling Windows the radios must stay off, and the toggle is just the messenger.

Fixing it means finding that something. The causes form a short list: physical switch, stuck toggle state, disabled radio service, corrupted adapter driver, or BIOS-level control. Work the list in order and the toggle starts obeying again.

## Why this happens

- **Physical wireless switch off:** Many laptops have a side switch or Fn-key toggle that cuts radios at the hardware level; Windows cannot override it.
- **Radio Management Service disabled:** This service mediates airplane mode; when disabled by updates or utilities, the mode locks on.
- **Corrupted Wi-Fi driver:** A bad wireless driver can report the radio as unavailable, which Windows interprets as "stay in airplane mode."
- **Stuck toggle state in the OS:** The software flag for airplane mode can desync from the actual radio state after crashes or updates.
- **BIOS-level radio disable:** Some firmware disables radios independently; Windows then shows airplane mode as permanently on.
- **Third-party network utilities:** VPN clients and "optimizer" tools can hook the radio controls and refuse to release them.
- **Fast Startup hibernation state:** A corrupted hibernation file can restore the stuck radio state on every boot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical switch and Fn-key toggle

Inspect the sides and front edge of the laptop for a physical wireless switch — slide it to the on position. Then try the Fn-key wireless combination (commonly Fn + F2, Fn + F3, or a key with an antenna icon). Watch for an on-screen indicator. On some models the switch is tiny and gets bumped in a bag, which explains "it worked yesterday." If your laptop has no switch, move on — but be thorough here, because no software fix can beat a hardware switch in the off position. This is the single most common cause on business laptops that have the switch.

### Fix 2: Toggle airplane mode from every available control

Try each toggle point in sequence: the Quick Settings panel (Win + A), Settings under Network & internet, and the physical switch from Fix 1. Sometimes one control path is stuck while another works — toggling from Settings can unstick what Quick Settings cannot. After each attempt, wait ten seconds before judging; the radio hardware needs a moment to respond. If the toggle flips itself back on within seconds every time, the lock is being enforced by something deeper — continue to the service and driver fixes rather than clicking the toggle harder.

### Fix 3: Restart the Radio Management Service

Press Win + R, type `services.msc`, and locate Radio Management Service. If it is stopped, start it; set Startup type to Manual or Automatic. This service is the broker between the airplane mode toggle and the actual radios — when it is disabled, Windows defaults to keeping airplane mode on and the toggle becomes decorative. VPN clients and system "debloating" scripts are frequent culprits for disabling it. Restart the laptop after changing the service and test the toggle again. This fix alone resolves a large share of stuck-airplane-mode cases.

### Fix 4: Reinstall the Wi-Fi adapter driver

A corrupted wireless driver reports the radio as unavailable, which pins airplane mode on. Open Device Manager (Win + X), expand Network adapters, right-click the Wi-Fi adapter, choose Uninstall device, and check "delete the driver software" if offered. Restart and let Windows redetect it. Then install the manufacturer's Wi-Fi driver from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) for your exact model — the OEM driver handles radio state transitions far more reliably than the generic one. If the adapter is missing from Device Manager entirely, see our guide on [fixing a missing network adapter](/articles/how-to-fix-network-adapter-missing/). For Wi-Fi-specific disappearance cases, also see [fixing Wi-Fi that vanished from the laptop](/articles/how-to-fix-wifi-disappeared-from-laptop-in-windows-11-24h2/).

### Fix 5: Disable Fast Startup and do a full shutdown

Fast Startup saves a hibernation file that can preserve the stuck radio state across "shutdowns." Open Control Panel, Power Options, "Choose what the power buttons do," click "Change settings that are currently unavailable," and uncheck "Turn on fast startup." Then do a full shutdown (hold Shift while clicking Shut down), wait 30 seconds, and power on. This forces Windows to initialize the radio hardware from scratch instead of restoring the corrupted state. If airplane mode now toggles normally, you can re-enable Fast Startup later — but many technicians leave it off permanently on troublesome machines.

### Fix 6: Perform a network reset

Go to Settings, Network & internet, Advanced network settings, Network reset. Click Reset now and confirm. This reinstalls every network adapter and returns all networking components — including the radio management pieces — to their defaults. The laptop will restart. You will need to re-enter Wi-Fi passwords, so collect them beforehand. A network reset is the heavy artillery for this problem: it clears corrupted adapter configurations, broken bindings, and stuck states in one pass. After the restart, test airplane mode before reinstalling any VPN client, so you can tell whether the VPN was contributing.

### Fix 7: Check the BIOS and test the hardware

Restart into BIOS/UEFI setup and look for wireless, WLAN, or radio controls — confirm they are enabled. Some laptops expose an "airplane mode control" or wireless enable at the firmware level. Save and exit. Then run the manufacturer's hardware diagnostics wireless test. If the radio fails diagnostics, the Wi-Fi card itself may be faulty or its antenna leads loose — a hardware fault that presents exactly like stuck airplane mode. Microsoft's Windows support hub documents additional radio troubleshooting, and a USB Wi-Fi adapter makes a fine stopgap while you arrange a card replacement.

## Closing

Stuck airplane mode is never really about the toggle — it is about whatever is holding the radios off underneath it. Physical switch, radio service, driver, hibernation state, firmware: check them in that order and the toggle comes back to life. Once it is working, note which fix did it, because the same cause tends to recur after the next big Windows update.
