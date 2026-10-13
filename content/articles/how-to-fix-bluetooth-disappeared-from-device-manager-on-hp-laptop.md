---
title: "Bluetooth Disappeared on an HP Laptop: Device Manager Fix"
slug: "how-to-fix-bluetooth-disappeared-from-device-manager-on-hp-laptop"
date: "2026-10-10"
categories: ["drivers"]
tags: ["bluetooth disappeared", "hp laptop", "device manager", "pavilion", "omen"]
description: "Bluetooth missing from Device Manager on your HP Pavilion, Envy, or Omen? Use HP Support Assistant, hardware diagnostics, and these HP-specific fixes."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-disappeared-from-device-manager-on-hp-laptop.webp"
faqs:
  - q: "Why does Bluetooth disappear on HP laptops?"
    a: "HP Pavilion, Envy, and Omen models use Intel, Realtek, or MediaTek wireless cards, and Bluetooth vanishes when Windows Update replaces HP's validated driver with a generic one. HP's BIOS also includes wireless device toggles, and the HP Support Assistant driver updates — while usually correct — can occasionally leave the Bluetooth half of a combo driver broken."
  - q: "Can HP Support Assistant fix missing Bluetooth?"
    a: "Yes, it is the best starting point on HP hardware. HP Support Assistant's updates section installs drivers validated for your exact product number, including the correct wireless combo driver. Run it, install all recommended wireless and Bluetooth updates, restart with a full shutdown, and check Device Manager."
  - q: "Does HP have built-in hardware diagnostics for Bluetooth?"
    a: "Yes. HP PC Hardware Diagnostics (press Esc during boot, then F2) tests wireless modules at firmware level, independent of Windows. If the diagnostic passes but Windows cannot see Bluetooth, the problem is software. If it fails, the wireless card itself is faulty — a definitive answer without guesswork."
  - q: "What about Bluetooth on HP Omen gaming laptops?"
    a: "Omen laptops add Omen Gaming Hub, whose power and network settings can affect radios. Check Gaming Hub for any disabled wireless devices or aggressive power profiles, update the Gaming Hub app itself, and ensure the correct wireless driver for your Omen model is installed from HP support."
---

HP's laptop families — Pavilion, Envy, Spectre, EliteBook, ProBook, and Omen — share a support ecosystem that makes Bluetooth troubleshooting more deterministic than on many brands: HP Support Assistant for validated drivers, HP PC Hardware Diagnostics for firmware-level testing, and a BIOS with explicit wireless-device controls. When Bluetooth disappears from Device Manager on an HP, these tools answer the hardware-versus-software question faster than generic Windows steps can.

HP-specific wrinkles include the Esc/F2 diagnostics menu, BIOS wireless toggles on business models, Omen Gaming Hub's radio management, and the product-number driver model (HP drivers are matched to product numbers like "Pavilion 15-eg2000," not just series names). Work the HP layer first, then fall back to Windows repair. Check Device Manager for the Bluetooth category after each step.

## Why this happens

- **Generic driver replacing HP's validated package**: Windows Update installs a non-HP Bluetooth driver that fails against HP's firmware customizations.
- **HP Support Assistant partial updates**: an interrupted update can leave the Bluetooth half of the wireless combo driver broken.
- **BIOS wireless device toggles**: HP BIOS menus (Advanced > Built-in Device Options) can disable Bluetooth independently of Windows.
- **Omen Gaming Hub interference**: outdated Gaming Hub versions and power profiles can disable or hide wireless radios on Omen and Victus models.
- **Function-key radio toggle**: **Fn + F12** or airplane-mode keys on many HP models can leave Bluetooth off while Wi-Fi recovers.
- **Fast Startup caching**: a failed Bluetooth initialization preserved across hybrid shutdowns looks like a permanent failure.
- **USB power management**: HP's power plans can sleep the internal USB bus where the Bluetooth radio lives.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run HP Support Assistant updates

HP Support Assistant knows your exact product number and delivers HP-validated drivers — the single most reliable first step for Bluetooth loss on HP hardware.

1. Open **HP Support Assistant** (preinstalled; otherwise install from HP's site) and go to updates.
2. Install all recommended updates, prioritizing wireless, Bluetooth, network, and BIOS categories.
3. Verify it detected your correct product number — driver matching depends on the full model identifier.
4. Restart with a full shutdown (hold **Shift** while clicking **Shut down**).
5. Check Device Manager for the Bluetooth category — HP-validated combo drivers fix the generic-driver mismatch behind most cases.

### Fix 2: Run HP PC Hardware Diagnostics on the wireless module

Before spending time on drivers, answer the hardware question definitively. HP's pre-boot diagnostics test the wireless card at firmware level, completely independent of Windows.

1. Restart and press **Esc** repeatedly during the HP logo, then press **F2** for System Diagnostics.
2. Run the **Component Tests > Wireless** (or Network) tests.
3. If the wireless module passes, the radio hardware is alive — the fault is Windows-side, so continue with driver fixes.
4. If it fails, note the failure ID — the wireless card needs replacement, and you have HP's own diagnostic as evidence.
5. This firmware-level answer saves hours: passing diagnostics mean every subsequent step is software, a diagnostic approach also useful in [our Dell Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-dell-laptop/).

### Fix 3: Check the function key, airplane mode, and Gaming Hub

HP's radio toggles operate below Device Manager. Rule them out — including Omen Gaming Hub on gaming models — before touching drivers.

1. Press the wireless function key (**Fn + F12** on many models, or the dedicated airplane-mode key) and toggle it off and on.
2. Open **Settings > Network & internet** and confirm Airplane mode is off.
3. On Omen/Victus models, open **Omen Gaming Hub**, check for disabled wireless devices, and switch to a Balanced profile.
4. Update the Gaming Hub app itself if an update is available — old versions have hidden radios before.
5. Open Device Manager — a returned Bluetooth category means the radio was switched off at the HP layer.

### Fix 4: Verify Bluetooth in the BIOS

HP business and consumer BIOS menus include built-in device options that can disable Bluetooth at firmware level. A firmware-disabled radio never appears in Device Manager.

1. Restart and press **F10** during the HP logo to enter BIOS Setup.
2. Navigate to **Advanced > Built-in Device Options** (or **Configuration**) and verify Bluetooth/wireless devices are enabled.
3. Choose **Load Defaults** to clear any stale device configuration, then save and exit.
4. Boot into Windows and rescan Device Manager (**Action > Scan for hardware changes**).
5. Firmware-level blocks clear instantly once enabled — no driver reinstall can substitute for this check.

### Fix 5: Clean-reinstall HP's wireless combo driver

When the Bluetooth half of the combo driver is broken, remove both halves and install HP's validated package for your exact product number.

1. In Device Manager (**View > Show hidden devices**), uninstall all grayed-out Bluetooth entries, ticking driver removal.
2. Uninstall the Wi-Fi adapter entry the same way.
3. Download the wireless/Bluetooth driver for your product number from [HP's official support site](https://support.hp.com/us-en).
4. Disconnect from the internet, install the HP package, then full shutdown and cold boot.
5. Confirm both Wi-Fi and Bluetooth enumerate and pair a device — and for Intel-based cards, [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) can verify the package contents.

### Fix 6: Tame power management and block driver replacement

Two maintenance steps that prevent recurrence: stop power policy from sleeping the radio, and stop Windows Update from replacing HP's validated driver with a generic one.

1. In Device Manager, uncheck "Allow the computer to turn off this device to save power" on the Bluetooth adapter and all **USB Root Hubs**.
2. Set **USB selective suspend** to **Disabled** in Power Options > Advanced settings.
3. Set **Device Installation Settings** to **No** so Windows Update stops managing the Bluetooth driver.
4. Verify the adapter's **Driver tab** shows HP as the provider with an HP date.
5. Create a system restore point while Bluetooth works — the same lockdown in [our post-update Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-after-windows-11-update/).

### Fix 7: Final isolation with a live USB

If HP diagnostics passed but Windows still cannot enumerate the adapter after every fix, confirm with an independent OS before concluding the Windows installation is unrepairable.

1. Boot an Ubuntu live USB and check Settings > Bluetooth.
2. If Linux sees the adapter, perform an in-place Windows repair from Microsoft's Windows 11 download page, keeping files and apps.
3. Check [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for known Bluetooth issues with your build first.
4. If Linux cannot see it either — despite passing HP diagnostics — re-run the diagnostics; intermittent card failures can pass once and fail later.
5. A consistently invisible radio across HP diagnostics, Linux, and Windows means the M.2 wireless card has failed and needs replacement.

## Closing

HP gives you unusually good tools for this problem: Support Assistant for validated drivers, pre-boot diagnostics for the hardware question, and BIOS toggles for the firmware layer. Use them in that order — updates first, diagnostics to settle hardware-versus-software, BIOS for firmware blocks, then the combo-driver reinstall and the power/update lockdown. Most HP Bluetooth disappearances resolve in the first two steps; the rest of the guide exists so the stubborn cases get a definitive answer instead of an endless driver-reinstall loop.
