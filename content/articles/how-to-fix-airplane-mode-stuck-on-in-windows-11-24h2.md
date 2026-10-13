---
title: "Airplane Mode Stuck On in Windows 11 24H2? Turn It Off for Good"
slug: "how-to-fix-airplane-mode-stuck-on-in-windows-11-24h2"
date: "2026-10-02"
categories: ["drivers"]
tags: ["airplane mode", "windows 11 24h2", "wifi stuck", "wireless", "radio"]
description: "Airplane mode won't turn off on Windows 11 24H2? Learn why the toggle gets stuck and follow proven fixes to restore WiFi and Bluetooth."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on-in-windows-11-24h2.webp"
faqs:
  - q: "Why is airplane mode stuck on and greyed out in Windows 11?"
    a: "A greyed-out toggle means Windows believes a hardware radio switch is engaged — a physical slider, a function-key toggle, or a BIOS setting holding the radios off. When the hardware reports radios disabled, Windows locks the software toggle. It can also happen when the radio management driver corrupts after the 24H2 update, making Windows misread the hardware state."
  - q: "Can a Windows update cause airplane mode to stick?"
    a: "Yes, particularly the 24H2 update. It can replace the radio management or chipset driver with a version that misreports the radio state, or reset BIOS-adjacent settings that control the wireless radios. If airplane mode stuck immediately after updating, driver reinstallation and a BIOS check are the highest-yield fixes."
  - q: "Will resetting network settings fix stuck airplane mode?"
    a: "It helps when the cause is corrupted radio state in the network stack, which a reset clears along with all adapters and profiles. But it cannot override a hardware switch or a BIOS-disabled radio — if the toggle is greyed out due to hardware state, reset changes nothing. Use network reset after ruling out physical switches and BIOS settings."
  - q: "Does airplane mode stuck on mean my WiFi card is dead?"
    a: "Very unlikely. A dead WiFi card removes the adapter from Device Manager; stuck airplane mode with the adapter still listed is a state-management problem, not hardware death. The radios are almost certainly fine — Windows is just refusing to turn them on. Work through the switch, driver, and service fixes before even considering hardware."
---

The toggle is on, it's greyed out, and nothing you click changes it. WiFi and Bluetooth are both dead, and the laptop behaves as if it's on an actual airplane with no way to land. Airplane mode stuck on — especially after the Windows 11 24H2 update — is one of those problems that feels like a hardware failure but is almost always a disagreement between Windows and the radio hardware about who's in charge.

The key distinction that drives the whole fix sequence: is the toggle clickable but ineffective, or greyed out entirely? A greyed-out toggle means Windows thinks a hardware switch is engaged. A clickable-but-stuck toggle means the software radio management is confused. The steps below handle both, in the order that unsticks the most laptops fastest.

## Why this happens

- **Physical radio switch engaged:** A side slider or function-key toggle holds radios off at hardware level.
- **Radio management driver corrupted:** 24H2 replaces the driver that reports radio state to Windows.
- **Stuck radio state in the network stack:** Corrupted state persists across reboots and ignores the toggle.
- **BIOS wireless disabled:** Firmware-level radio off makes Windows lock the toggle.
- **Fast startup preserving bad state:** Hybrid boot carries the stuck radio state from session to session.
- **Airplane mode service misconfiguration:** The radio management service fails to process toggle commands.
- **Keyboard driver misreporting the Fn key:** A stuck key event keeps re-engaging airplane mode.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Check every physical radio control
Inspect the laptop for a physical wireless slider (common on business laptops) and ensure it's in the on position. Press the airplane-mode function key (often Fn + F2 or a dedicated key with an airplane icon) several times, watching the on-screen indicator. Some laptops also have the toggle in BIOS. If the Windows toggle is greyed out, a hardware control is almost certainly the cause — Windows locks the software toggle when hardware reports radios off. Our [step-by-step airplane mode guide](/articles/how-to-fix-airplane-mode-stuck-on-step-by-step/) has model-specific switch locations.

### Fix 2: Toggle via Settings and kill fast startup
Go to Settings > Network & internet and try the airplane mode toggle there rather than quick settings. Then disable fast startup (Power Options > "Choose what the power buttons do" > uncheck fast startup), shut down fully, unplug, hold power 30 seconds, and boot. Fast startup preserves the stuck radio state across "reboots" — only a true cold boot clears it. This combination unsticks a large share of software-level cases.

### Fix 3: Enable radios in BIOS and check Device Manager
Reboot into BIOS/UEFI and confirm wireless/WLAN and Bluetooth are Enabled. Back in Windows, open Device Manager with hidden devices shown: if the wireless adapter is disabled, enable it; if it's missing, rescan for hardware changes. A BIOS-disabled radio is invisible to every Windows fix, so this check belongs early. After re-enabling, the airplane toggle usually unlocks immediately.

### Fix 4: Reinstall wireless and chipset drivers
Download the WiFi and chipset drivers for your model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). Uninstall the wireless adapter with driver deletion, install the fresh packages, and reboot. The 24H2 update's generic radio-management drivers misreport hardware state on many models; the OEM drivers restore correct communication between the radio hardware and Windows' airplane mode logic.

### Fix 5: Restart the radio management services
Open `services.msc` and restart "Radio Management Service" (set to Manual or Automatic), plus "WLAN AutoConfig." Then open an elevated Command Prompt and run `netsh winsock reset` and `netsh int ip reset`, followed by a restart. These services translate toggle clicks into hardware commands — when they hang, the toggle animates but nothing happens. If the toggle was clickable-but-dead, this is frequently the fix.

### Fix 6: Check for a stuck keyboard key event
If airplane mode re-engages seconds after you turn it off, a stuck Fn-key event or faulty keyboard driver is re-triggering it. Test with an external USB keyboard while the internal one is disabled in Device Manager, and update the keyboard/ATK driver from your manufacturer's site. Also inspect for physically stuck keys. This pattern — off, then mysteriously back on — is the signature of a hardware key event, not a Windows bug. Related radio issues are covered in our [airplane mode troubleshooting reference](/articles/airplane-mode-stuck-on-troubleshooting/).

### Fix 7: Network reset and system repair
As a final software step, do Settings > Network & internet > Advanced network settings > Network reset, then restart. If the toggle remains stuck, run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` to repair system corruption. Persistent failure across all of this — with the adapter present in Device Manager — is rare and points to embedded-controller firmware trouble; check for a BIOS update mentioning radio or airplane mode. Microsoft's radio diagnostics at Windows support round out the official checks.

## Closing
Stuck airplane mode is Windows and the radio hardware arguing about state, and the argument almost always ends when you find who's actually holding the radios off — a physical switch, a BIOS toggle, a corrupted driver, or a stuck service. Check the hardware controls first, then work the software stack, and the toggle surrenders in nearly every case. Once the toggle obeys again, prevent the next stuck episode: memorize your laptop's physical radio controls, because a bumped switch in a bag remains the most common cause and the fastest to check. After each Windows update, glance at quick settings to confirm the radios respond — catching a stuck state early keeps it a curiosity instead of a crisis. If your machine was fixed by a driver reinstall, save that driver installer; 24H2's servicing may attempt the same replacement again. For laptops where a flaky keyboard kept re-triggering airplane mode, consider remapping or disabling the airplane-mode key in the manufacturer's utility if it offers that option. And remember the diagnostic split that guided this whole repair: a greyed-out toggle means hardware is holding the radios off, while a clickable-but-dead toggle means software confusion — knowing which you are looking at cuts every future radio problem in half.
