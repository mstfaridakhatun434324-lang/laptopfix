---
title: "Unstick Airplane Mode on an ASUS Laptop"
slug: how-to-fix-airplane-mode-stuck-on-on-asus-laptop
date: 2026-09-02
categories: ["drivers"]
tags: ["airplane mode", "asus laptop", "wifi", "wireless", "troubleshooting"]
description: "Airplane mode stuck on your ASUS laptop? Unlock Wi-Fi and Bluetooth again with these targeted fixes for the greyed-out toggle."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on-on-asus-laptop.webp"
faqs:
  - q: "Why is airplane mode greyed out on my ASUS laptop?"
    a: "The toggle greys out when Windows believes the wireless radio is controlled by hardware. This happens with a stuck function-key state, a corrupted network adapter driver, or the Radio Management Service being disabled. Re-enabling that service usually restores the toggle."
  - q: "Can a BIOS setting lock airplane mode on?"
    a: "Yes. Some ASUS models have a wireless control setting in the BIOS that can disable the radio at firmware level. If Windows cannot override it, enter the BIOS and confirm the wireless device is enabled, which hands control back to the operating system."
  - q: "Why does airplane mode turn itself back on after restart?"
    a: "A scheduled task, a third-party power manager, or a corrupted network profile can re-enable it at boot. Check the Radio Management Service startup type and remove any ASUS or third-party utilities that manage wireless power. Also inspect Task Scheduler for wireless-related tasks that run at logon and reapply the radio state."
  - q: "Does the physical wireless switch still exist on ASUS laptops?"
    a: "Most modern ASUS laptops replaced the physical switch with an Fn key combination, typically Fn plus F2. If the key is stuck or its driver is missing, Windows may read the radio as permanently off, which is why reinstalling ATK drivers helps."
---

Airplane mode stuck on is one of the most maddening Windows failures because it cuts everything at once: no Wi-Fi, no Bluetooth, and a toggle that either does nothing or is greyed out entirely. On ASUS laptops the problem has a few brand-specific twists — the Fn-key wireless toggle, the ATK package that drives it, and MyASUS power profiles that can lock the radio state.

The root cause is almost always a disagreement between Windows and the wireless hardware about who controls the radio. Windows thinks a hardware switch has the radio off; the hardware thinks Windows has it off. Neither side yields. The fix is to identify which side is actually wrong, then force the correct state through services, drivers, or the BIOS.

These fixes are ordered from the least invasive to the deepest. The first three resolve the issue for most people without touching drivers at all.

There is one more ASUS-specific wrinkle worth understanding: MyASUS and the ATK hotkey package both claim some authority over the wireless radio, and after major Windows updates they can disagree about its state. When that happens, neither the Windows toggle nor the Fn key works because each one thinks the other is in charge. The service and driver fixes below break that deadlock by re-establishing a single source of truth.

## Why this happens

- **Radio Management Service disabled:** This Windows service arbitrates airplane mode. When it is stopped or disabled, the toggle locks and the radios stay off.
- **Stuck Fn-key wireless state:** The ASUS ATK hotkey driver can leave the wireless toggle in a phantom off state that survives reboots.
- **Corrupted wireless adapter driver:** A broken Wi-Fi or Bluetooth driver makes Windows treat the radio as unavailable, which greys out airplane mode controls.
- **MyASUS or power manager locking the radio:** Battery-saving profiles in ASUS utilities can force the radio off and reapply the setting at every boot.
- **BIOS wireless device disabled:** Firmware-level wireless control overrides Windows entirely, making every software toggle meaningless.
- **Network adapter disabled in Device Manager:** A manually or accidentally disabled adapter reads as no radio hardware, freezing the airplane mode UI.
- **Corrupted network stack:** Damaged Winsock or TCP/IP state can cascade into the radio management layer and jam the toggle.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle airplane mode with the hardware key

The Fn wireless key bypasses the Windows UI entirely and can break the deadlock between hardware and software state.

1. Press **Fn + F2** (the wireless icon key) and watch the on-screen indicator.
2. Press it again after five seconds to toggle the state back.
3. If nothing happens, the ATK hotkey driver may be missing — note this and continue to the driver fix.
4. Check whether the Windows airplane mode toggle responds after the key press. If Wi-Fi itself has vanished rather than just being toggled, see the [missing Wi-Fi guide](/articles/wifi-disappeared-windows-11-no-wifi-option/).

### Fix 2: Restart the Radio Management Service

This service is the referee for airplane mode. Restarting it unsticks the toggle in a large share of cases.

1. Press **Win + R**, type **services.msc**, and press Enter.
2. Find **Radio Management Service**, right-click it, and choose **Restart**.
3. Double-click it and set **Startup type** to **Manual** or **Automatic**.
4. Try the airplane mode toggle in **Settings > Network & internet** again.

### Fix 3: Enable the wireless adapter in Device Manager

A disabled adapter makes Windows believe no radio exists. Re-enabling it hands the radio back to the operating system.

1. Open **Device Manager** and expand **Network adapters**.
2. If the Wi-Fi adapter shows a down arrow, right-click it and choose **Enable device**.
3. Also check for any adapter with a yellow warning and update its driver.
4. Restart and test the airplane mode toggle. Related adapter disappearances are covered in the [missing network adapter guide](/articles/how-to-fix-network-adapter-missing-on-windows-10/).

### Fix 4: Reinstall the ASUS ATK and wireless drivers

The ATK package drives the Fn keys; the wireless driver drives the radio. Both must be healthy for the toggle to work.

1. On another device, visit the ASUS support site — or use the [Intel Driver Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel wireless cards — and download the ATK package and Wi-Fi driver for your exact model.
2. In Device Manager, uninstall the Wi-Fi adapter, checking **Delete the driver software**.
3. Install the ATK package first, restart, then install the Wi-Fi driver and restart again.
4. Test Fn + F2 and the Windows toggle.

### Fix 5: Reset the network stack

When the network stack is corrupt, resetting it clears the jammed state that the radio service reads.

1. Open an elevated Command Prompt.
2. Run **netsh winsock reset** and press Enter, then run **netsh int ip reset**.
3. Run **ipconfig /release**, **ipconfig /renew**, and **ipconfig /flushdns** in sequence.
4. Restart the laptop and check airplane mode.

### Fix 6: Check the BIOS wireless setting

Firmware-level control overrides everything in Windows. If the BIOS has the radio off, no software fix can help.

1. Restart and tap **F2** or **Del** to enter the BIOS.
2. Look under **Advanced** or **Onboard Devices** for a wireless or WLAN toggle.
3. Ensure it is **Enabled**, save with **F10**, and boot into Windows.
4. The airplane mode toggle should now respond normally.

### Fix 7: Remove radio-locking utilities

Third-party power and network managers can re-enable airplane mode at every boot, undoing your fixes.

1. Open **Settings > Apps** and look for third-party Wi-Fi managers or aggressive battery utilities.
2. Uninstall them one at a time, restarting after each.
3. In MyASUS, check power profiles for any setting that disables wireless on battery and turn it off.
4. Confirm the toggle survives a full shutdown and cold boot.

### Fix 8: Reset the BIOS to factory defaults

When firmware settings for the radio are corrupt, resetting the BIOS clears them and hands clean control back to Windows.

1. Restart and enter the BIOS with **F2** or **Del**.
2. Find **Load Optimized Defaults** or **Restore Defaults** — usually on the Exit tab.
3. Confirm, then verify the wireless device is still **Enabled** before saving.
4. Boot into Windows and test the airplane mode toggle.

## Closing

A stuck airplane mode toggle is a control dispute, not a dead radio. The Radio Management Service, the Fn-key driver, and the BIOS setting are the three authorities involved — get them agreeing and the toggle frees up. Only if the adapter is missing from Device Manager entirely should you suspect the wireless card itself.
