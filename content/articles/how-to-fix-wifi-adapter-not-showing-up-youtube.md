---
title: "How to Fix a Wi-Fi Adapter Not Showing Up (Step-by-Step)"
slug: how-to-fix-wifi-adapter-not-showing-up-youtube
date: 2026-09-17
categories: ["drivers"]
tags: ["wifi adapter missing", "wifi not showing", "network adapter", "wireless driver", "device manager"]
description: "Wi-Fi adapter missing from Device Manager and Settings? Work through BIOS checks, driver reinstalls, and hardware resets to bring wireless back."
thumbnail: "/images/thumbs/how-to-fix-wifi-adapter-not-showing-up-youtube.webp"
faqs:
  - q: "Why is my Wi-Fi adapter completely missing from Device Manager?"
    a: "A completely missing adapter means Windows cannot see the hardware at all, which points to a BIOS-level disable, airplane mode locking the radio, a failed WLAN card, or the card not being enumerated on the PCIe bus. It is different from a driver problem, where the adapter appears with a warning. Start with BIOS and physical switch checks before touching drivers."
  - q: "Can a Windows update make my Wi-Fi adapter disappear?"
    a: "Yes, this is a well-documented pattern. Feature updates can install an incompatible driver that fails to initialize the card, or flip power management settings that shut the adapter down. If wireless vanished right after an update, reinstall the manufacturer's WLAN driver and check the BIOS wireless setting, since updates occasionally reset it."
  - q: "My Wi-Fi shows as hidden in Device Manager — what now?"
    a: "A greyed-out hidden adapter means Windows remembers the driver but believes the hardware is absent. Uninstall the hidden entry with driver software deletion, then scan for hardware changes. If it still will not appear, the card is likely disabled in BIOS, switched off physically, or has failed electrically."
  - q: "Is the WLAN card replaceable if it has failed?"
    a: "On most laptops the WLAN card is a small M.2 module that is replaceable, though some ultrabooks solder it. Replacement cards cost little, but check your laptop's BIOS whitelist and antenna connections first. If the laptop is under warranty, let the manufacturer handle it rather than opening the machine yourself."
---

When the Wi-Fi adapter vanishes entirely — no wireless icon, no Wi-Fi section in Settings, nothing under Network adapters in Device Manager — the instinct is to reinstall drivers. But a missing adapter is fundamentally different from a broken driver. A broken driver shows up with a warning; a missing adapter means Windows cannot see the hardware at all, and no driver install will fix hardware Windows cannot find.

The correct order matters here: verify the hardware is visible to the system first (BIOS, switches, hidden devices), then fix the driver layer. Jumping straight to driver downloads wastes time when the card is disabled at a lower level.

## Why this happens

- **Wireless disabled in BIOS/UEFI:** Many laptops have a BIOS wireless toggle. If it is off, the card is invisible to Windows — no driver can help.
- **Airplane mode or physical Wi-Fi switch engaged:** A stuck airplane mode or a physical switch/keyboard toggle powers down the radio, and some models hide the adapter when the radio is off.
- **Windows update replaced the WLAN driver:** An incompatible driver from Windows Update can fail to initialize the card, making it drop out of Device Manager after reboot.
- **Card not enumerated on the bus:** Power events and failed sleep/wake cycles can leave the PCIe/USB bus in a state where the card is never enumerated.
- **Hidden ghost entry blocking detection:** A greyed-out ghost of the adapter can hold a broken configuration that prevents the real hardware from being detected fresh.
- **Power management shutting the card down:** Aggressive link-state power management can power-gate the WLAN card so thoroughly that it stops responding to enumeration.
- **Failed WLAN card:** Cards do die — heat, age, and power surges kill them, and the symptom is exactly this: total disappearance.
- **Loose M.2 card or antenna:** On machines that have been opened, a partially seated WLAN module may enumerate intermittently or not at all.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out airplane mode and physical switches

1. Press **Win + A** to open Quick Settings and confirm **Airplane mode** is off. If it is stuck on, the radio may be locked at a lower level.
2. Check the laptop's edges for a physical Wi-Fi switch — some business laptops still have one.
3. Try the wireless function key (often **Fn + F2** or a radio-tower icon key) and watch for an on-screen indicator.
4. Open **Settings → Network & internet** — if there is no Wi-Fi section at all, the adapter is truly missing rather than just disconnected.
5. A stuck airplane mode needs its own treatment; the [airplane mode troubleshooting guide](/articles/best-way-to-fix-airplane-mode-stuck-on/) covers the registry and service fixes for radios that refuse to turn on.

### Fix 2: Check the BIOS wireless setting

1. Restart and enter BIOS/UEFI (usually **F2** or **Del** during boot).
2. Look under **Advanced**, **System Configuration**, or **Security** for **Wireless**, **WLAN**, or **Wireless LAN**.
3. Make sure it is **Enabled**. On some BIOS versions there are separate toggles for WLAN and Bluetooth — enable WLAN at minimum.
4. Save and exit, then boot into Windows and check Device Manager's Network adapters section.
5. If Windows Update preceded the disappearance, double-check this setting — updates have been known to flip BIOS-adjacent wireless settings on certain models.

### Fix 3: Reveal hidden devices and clear ghosts

1. Open Device Manager, click **View → Show hidden devices**.
2. Expand **Network adapters** and look for a greyed-out Wi-Fi entry (Intel Wireless, Realtek, MediaTek, or Qualcomm).
3. If you find one, right-click → **Uninstall device**, checking **Attempt to remove the driver for this device**.
4. Click **Action → Scan for hardware changes** and watch whether the adapter reappears as a live device.
5. A ghost that refuses to clear points to deeper trouble — the [hidden devices walkthrough](/articles/best-way-to-enable-hidden-devices-in-device-manager/) covers the environment-variable method for stubborn non-present entries.

### Fix 4: Reinstall the WLAN driver from the manufacturer

1. Identify your adapter model from the ghost entry, the laptop's spec sheet, or the manufacturer's support page.
2. On another device if needed, download the WLAN driver from your laptop maker's support site ([Dell](https://www.dell.com/support) or [HP](https://support.hp.com/us-en)) for your exact model — or from [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel cards.
3. In Device Manager, uninstall any trace of the old adapter including driver software, then install the downloaded driver.
4. Restart and check whether the Wi-Fi section returns to Settings.
5. Avoid the generic Windows Update driver for now — install the manufacturer's package first, since it includes the correct initialization firmware. The [Wi-Fi driver reinstall guide](/articles/best-way-to-reinstall-wifi-driver/) details the clean-install sequence.

### Fix 5: Reset the network stack

1. Open an elevated Command Prompt (**Win + R** → `cmd` → **Ctrl + Shift + Enter**).
2. Run these in order: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
3. Restart the laptop.
4. This fixes cases where the adapter is present but the stack above it is corrupted — worth trying before assuming hardware failure.
5. After reboot, check **Settings → Network & internet → Advanced network settings → Network reset** as a heavier option if the commands did not help.

### Fix 6: Disable power management on the adapter

1. In Device Manager, open the Wi-Fi adapter's **Properties → Power Management** tab.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. Go to **Control Panel → Power Options → Change plan settings → Change advanced power settings**.
4. Under **Wireless Adapter Settings → Power Saving Mode**, set both battery and plugged-in to **Maximum Performance**.
5. Restart and test. Power-gated cards that vanish after sleep are the classic beneficiaries of this fix.

### Fix 7: Power-drain the hardware to force re-enumeration

1. Shut down fully, unplug the charger, and remove the battery if it is removable.
2. Hold the power button for **30 seconds** to drain residual charge from the board.
3. Reconnect power and boot. The cold start forces the BIOS to re-enumerate every PCIe device, including the WLAN card.
4. Check Device Manager immediately after boot.
5. If the adapter appears briefly then vanishes, suspect a failing card or a heat-related intermittent fault rather than software.

### Fix 8: Test with a USB Wi-Fi adapter to isolate hardware failure

1. Plug in any USB Wi-Fi adapter. If it works, your OS network stack is fine and the internal card is the problem.
2. If the internal card never appears in BIOS, Device Manager (even hidden), or after a power drain, it has likely failed electrically.
3. On laptops with a socketed M.2 WLAN card, reseating or replacing the module is a cheap fix — check the service manual for your model first.
4. If the laptop is under warranty, stop here and contact the manufacturer — opening the machine can void coverage.
5. As a permanent workaround, a nano USB Wi-Fi adapter costs very little and restores wireless without any disassembly.

## Closing

A missing Wi-Fi adapter is a visibility problem before it is a driver problem: BIOS toggles, airplane mode locks, ghost entries, and power gating all hide the card from Windows. Work the list from hardware visibility down to drivers, and you will find the layer where the card drops out. If it never appears anywhere — not in BIOS, not hidden, not after a power drain — the card itself has failed, and a replacement module or USB adapter is the practical answer.
