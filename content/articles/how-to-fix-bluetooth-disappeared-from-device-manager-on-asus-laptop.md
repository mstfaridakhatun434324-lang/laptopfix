---
title: "Bluetooth Disappeared on an ASUS Laptop: Restore It in Device Manager"
slug: "how-to-fix-bluetooth-disappeared-from-device-manager-on-asus-laptop"
date: "2026-10-02"
categories: ["drivers"]
tags: ["bluetooth disappeared", "asus laptop", "device manager", "myasus", "vivobook"]
description: "Bluetooth gone from Device Manager on your ASUS VivoBook, ZenBook, or ROG laptop? Use MyASUS and these ASUS-specific fixes to bring the adapter back."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-disappeared-from-device-manager-on-asus-laptop.webp"
faqs:
  - q: "Why does Bluetooth disappear on ASUS laptops?"
    a: "ASUS models commonly use MediaTek, Realtek, or Intel wireless cards, and the Bluetooth function can fail when MyASUS or Windows Update installs a mismatched driver. ASUS Wireless Radio Control can also disable the radio at a software layer Device Manager cannot see. ROG gaming models add Armoury Crate power profiles that can keep the radio asleep."
  - q: "Can the MyASUS app fix missing Bluetooth?"
    a: "Yes, frequently. MyASUS > System Diagnostics and its driver-update section deliver ASUS-validated wireless drivers matched to your exact model. Running MyASUS diagnostics first identifies whether the issue is driver, software-switch, or hardware, which saves time compared to guessing with generic Windows fixes."
  - q: "What is ASUS Wireless Radio Control and does it affect Bluetooth?"
    a: "ASUS Wireless Radio Control is a utility that manages the on/off state of Wi-Fi and Bluetooth radios. If it has switched Bluetooth off, the adapter may vanish from Device Manager entirely. Check its status in the system tray or in MyASUS, and make sure Bluetooth radio control is set to on."
  - q: "Do ROG laptops have different Bluetooth problems?"
    a: "ROG models share the same driver architecture but add Armoury Crate, whose power profiles and device-management features can disable radios. If Bluetooth disappeared on a ROG laptop, check Armoury Crate's settings for any disabled wireless devices before reinstalling drivers, and update Armoury Crate itself — old versions are a known culprit."
---

ASUS laptops — VivoBook, ZenBook, ExpertBook, TUF, and ROG — use a wider mix of wireless chips than most brands: MediaTek (very common in recent VivoBooks), Realtek, and Intel all appear across the lineup. That variety matters, because Bluetooth disappearance on an ASUS is frequently a wrong-driver problem: Windows Update installs a driver for a chip you do not have, or MyASUS pushes a package built for a sibling model.

ASUS also layers its own radio management on top of Windows: Wireless Radio Control and MyASUS can switch the Bluetooth radio off below Device Manager, and on ROG machines Armoury Crate adds power profiles that do the same. This guide starts with those ASUS-specific layers — the ones generic guides miss — then moves to driver repair.

Check Device Manager for the Bluetooth category after each step.

## Why this happens

- **Wrong-chip driver installed**: with MediaTek, Realtek, and Intel all in ASUS's lineup, an update can install a driver for the wrong radio, which fails silently and hides the adapter.
- **ASUS Wireless Radio Control switched off**: this utility can disable the Bluetooth radio at a software layer that removes it from Device Manager.
- **MyASUS driver updates**: MyASUS system updates occasionally deliver a wireless package whose Bluetooth component does not match the installed card's firmware.
- **Armoury Crate interference (ROG/TUF)**: outdated Armoury Crate versions and aggressive power profiles can disable or hide wireless radios.
- **Windows Update generic drivers**: Windows replaces the ASUS-validated driver with a generic one that cannot initialize the specific radio chip.
- **Airplane-mode hotkey**: **Fn + F2** on many ASUS models toggles airplane mode, which can stick in a half-state where Wi-Fi returns but Bluetooth does not.
- **Fast Startup caching**: ASUS's fast-boot firmware combined with Windows Fast Startup can preserve a failed Bluetooth initialization across restarts.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the airplane-mode key and Wireless Radio Control

ASUS's **Fn + F2** airplane-mode toggle and the Wireless Radio Control utility both operate beneath Device Manager. A radio switched off here is invisible to every Windows-level fix, so rule this layer out first.

1. Press **Fn + F2** and watch the on-screen indicator; toggle airplane mode on and then off again, waiting 15 seconds.
2. Open **Settings > Network & internet** and confirm Airplane mode is off and Bluetooth's toggle area is checked.
3. Look for the ASUS Wireless Radio Control icon in the system tray; open it and verify the Bluetooth radio is switched on.
4. In **MyASUS**, check the device/radio status panel for any disabled wireless device and re-enable it.
5. Open Device Manager — if the Bluetooth category appeared, the radio was simply switched off at the ASUS layer.

### Fix 2: Run MyASUS diagnostics and updates

MyASUS is ASUS's equivalent of a service technician's first step: its diagnostics can distinguish a driver problem from a hardware one, and its update section delivers drivers validated for your exact model.

1. Open **MyASUS** (install it from the Microsoft Store if it is missing) and run **System Diagnostics > Bluetooth** if available.
2. Go to the update/driver section and install any recommended wireless or Bluetooth driver updates.
3. Also install any MyASUS app updates — the app itself must be current to manage radios correctly.
4. Restart with a full shutdown (Shift + Shut down) after updates complete.
5. Check Device Manager; MyASUS-validated drivers resolve the wrong-chip driver problem that causes most ASUS Bluetooth disappearances.

### Fix 3: Identify your actual wireless chip and install its driver

Because ASUS ships three different radio vendors, installing the right driver means knowing which chip you have. The Hardware IDs in Device Manager reveal the truth even when the Bluetooth entry is hidden.

1. In Device Manager, click **View > Show hidden devices** and look under **Network adapters** for your Wi-Fi card (e.g., "MediaTek Wi-Fi," "Realtek 8852BE," or "Intel Wireless").
2. Right-click it > **Properties > Details > Hardware Ids** and note the VEN (vendor) code: 14C3 = MediaTek, 10EC = Realtek, 8086 = Intel.
3. Download the matching Bluetooth driver from your laptop manufacturer's official support page for your exact model — or from [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel cards.
4. Uninstall any grayed-out Bluetooth entries first, ticking driver removal, then install the correct package.
5. Full shutdown, cold boot, and verify.

### Fix 4: Update or reset Armoury Crate (ROG/TUF models)

On ROG and TUF laptops, Armoury Crate manages device power states and can disable the Bluetooth radio; older Crate versions have documented bugs that hide wireless devices.

1. Open Armoury Crate and check for app updates; install them and restart the laptop.
2. Look through Crate's device and power-profile settings for any disabled wireless or Bluetooth device and re-enable it.
3. Switch to the **Balanced** or **Performance** profile temporarily — aggressive silent/eco profiles can suppress the radio.
4. If Crate itself seems broken, uninstall it, restart, check Device Manager for Bluetooth, then reinstall the latest Crate from ASUS support.
5. Test Bluetooth with Crate fully uninstalled before reinstalling — if the adapter returns, Crate was the culprit, a pattern also seen with vendor utilities in [our Lenovo Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-lenovo-laptop/).

### Fix 5: Block Windows Update from replacing the working driver

ASUS's multi-vendor lineup makes Windows Update's generic driver habit especially destructive: the "newer" driver Windows offers is often for the wrong chip. Lock the working driver down once Bluetooth returns.

1. In **System > About > Advanced system settings > Hardware > Device Installation Settings**, choose **No**.
2. In Device Manager, verify the Bluetooth adapter's **Driver tab** shows the ASUS/Intel/MediaTek/Realtek provider and date — not a Microsoft-dated generic.
3. Create a system restore point while Bluetooth is functional.
4. If Windows already replaced the driver, roll it back (**Properties > Driver > Roll Back Driver**) before locking updates.
5. Re-check the driver version after the next Patch Tuesday to confirm the policy held.

### Fix 6: Power-cycle the embedded controller

ASUS firmware keeps radio state in the embedded controller, and a full power drain resets it — clearing stuck states that survive driver reinstalls and restarts.

1. Shut down fully, unplug the charger, and disconnect all peripherals.
2. Hold the power button for 40 seconds (ASUS recommends a long press for EC reset on many models).
3. If the battery is removable, take it out during the drain; if internal, the long press suffices.
4. Reconnect only the charger, power on, and check Device Manager.
5. EC resets often restore radios that vanished after firmware or driver updates.

### Fix 7: Test hardware with a live USB and check the BIOS

If no software step has revived the adapter, determine whether the radio hardware itself is alive. A Linux live USB uses an independent Bluetooth stack — the definitive test.

1. Boot from an Ubuntu live USB and check Settings > Bluetooth for the adapter.
2. If Linux sees it, the fault is Windows-side: perform an in-place Windows repair install from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
3. If Linux cannot see it either, enter the ASUS BIOS (**F2** or **Del** during boot) and check **Advanced** settings for wireless/Bluetooth device options.
4. Load BIOS optimized defaults, save, and retest in both Windows and Linux.
5. A radio invisible everywhere points to a failed wireless card — on most ASUS models it is a replaceable M.2 module, as outlined in [our step-by-step Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-step-by-step/).

## Closing

Bluetooth disappearance on ASUS laptops is usually a vendor-layer problem, not a Windows mystery: the wrong chip's driver, a radio switched off in Wireless Radio Control or Armoury Crate, or a MyASUS update that missed. Once the adapter is back, keep its correct driver locked against Windows Update, and treat MyASUS as your first stop the next time a radio misbehaves.
