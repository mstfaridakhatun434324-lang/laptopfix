---
title: "How to Enable NPU in BIOS: Step-by-Step for All Brands"
slug: how-to-enable-npu-in-bios
date: 2026-10-19
categories: ["ai-pc"]
tags: ["npu", "bios", "uefi", "enable npu", "windows 11"]
description: "How to enable NPU in BIOS? Step-by-step instructions for Dell, HP, Lenovo, and Asus laptops to turn on the AI accelerator in firmware settings."
thumbnail: "/images/thumbs/how-to-enable-npu-in-bios.webp"
faqs:
  - q: "What is the NPU setting called in BIOS?"
    a: "Names vary: NPU, AI Boost, AI Accelerator, Neural Processing Unit, XDNA, or IPU. It usually lives under Advanced, Integrated Peripherals, or Advanced CPU Configuration. Check your maker's manual for the exact label."
  - q: "Can enabling the NPU in BIOS cause problems?"
    a: "No — enabling simply makes the hardware visible to Windows. It does not overclock anything or change voltages. The only 'risk' is none; a disabled NPU just sits idle."
  - q: "I don't see any NPU option in my BIOS. Why?"
    a: "Three possibilities: your processor has no NPU, your BIOS version hides the option (check for updates), or the vendor enables it permanently with no toggle. Confirm your chip model first."
  - q: "Do I need to reinstall drivers after enabling in BIOS?"
    a: "Usually Windows detects the newly visible hardware and installs a driver automatically. If Device Manager shows an unknown device afterward, install your OEM's NPU driver package manually."
---

Windows cannot use hardware that firmware hides. On many AI laptops the NPU ships disabled in BIOS/UEFI — sometimes by default, sometimes flipped off by a firmware update — and no amount of driver reinstalling in Windows will help until the firmware toggle is set. This guide walks through finding and enabling it on all major brands.

If you have confirmed your processor actually includes an NPU but Device Manager shows no [Neural processors section](/articles/neural-processors-missing-device-manager/), the BIOS toggle is the most likely culprit. Enable it here first.

## Why this happens (why it is disabled)

- **Factory default off:** Some vendors ship with the NPU disabled to simplify validation, expecting users or IT to enable it.
- **BIOS update reset:** Firmware updates commonly reset custom settings — including an NPU you previously enabled.
- **Corporate IT policy:** Enterprise-imaged machines may have the NPU disabled by policy for security review.
- **Power-saving presets:** "Battery saver" BIOS profiles on some laptops disable the NPU along with other accelerators.
- **Mislabeled options:** The toggle exists but under an unfamiliar name, so users assume there is no option.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enter BIOS/UEFI setup

Get into firmware settings safely.

1. Save all work, then restart the laptop.
2. During boot, repeatedly press the BIOS key: F2 (Dell, Asus, Acer), F10 (HP), F1 or Fn+F1 (Lenovo), Del (many others).
3. Alternative: Settings, System, Recovery, Advanced startup, Restart now, Troubleshoot, UEFI Firmware Settings, Restart.
4. If BitLocker prompts for a recovery key, have it ready — firmware changes can trigger it.
5. Do not change anything yet — just get comfortable navigating the menus.

### Fix 2: Find the NPU toggle (Dell, HP, Lenovo, Asus)

Locations differ by vendor.

1. **Dell:** Advanced or Integrated Devices — look for "NPU," "AI Accelerator," or under Processor settings.
2. **HP:** Advanced, Device Options or Built-in Device Options — "Neural Processing Unit" or "AI" entries.
3. **Lenovo:** Advanced, or Devices menu — "Intel AI Boost," "AMD XDNA," or "NPU."
4. **Asus/Acer:** Advanced, CPU Configuration or NB Configuration — "NPU," "IPU," or "AI Engine."
5. Use the BIOS search function if your firmware has one — type "NPU" or "AI" directly.

### Fix 3: Enable it and save properly

The critical step — and the save matters as much as the toggle.

1. Change the NPU/AI entry from Disabled to Enabled (avoid "Auto" if a full Enabled option exists).
2. Check for related sub-options (NPU power modes) and leave them at defaults for now.
3. Save and exit — usually F10, then confirm "Yes."
4. Let Windows boot fully; do not interrupt the first boot after a firmware change.
5. Open Device Manager and verify the Neural processors section appears.

### Fix 4: Update BIOS if no toggle exists

Old firmware may lack the option entirely.

1. Check your BIOS version: Win + R, `msinfo32`, BIOS Version/Date.
2. Visit your maker's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) and compare.
3. If newer, install the BIOS update exactly per instructions — charger plugged in, no interruptions, no forced shutdowns.
4. Re-enter BIOS after updating and look for the NPU toggle again — vendors add it in updates.
5. If still absent and your chip has an NPU, the vendor may enable it permanently — check Device Manager in Windows instead.

### Fix 5: Install the driver after enabling

Firmware visibility is half the job; Windows still needs the driver.

1. After enabling in BIOS and booting, check Device Manager for Neural processors or an Unknown device.
2. If Unknown device appears, let Windows search automatically first.
3. If that fails, install the OEM NPU/chipset driver package manually.
4. Reboot and confirm the NPU entry is clean with no warnings.
5. Test with Task Manager's NPU graph or an AI feature to confirm it is not just visible but working.

### Fix 6: Lock it against future resets

Prevent the next BIOS update from undoing your work.

1. Note your BIOS version and the exact menu path of the toggle for future reference.
2. After any future BIOS update, re-enter setup and verify the NPU is still enabled — updates reset settings routinely.
3. If your IT department manages the machine, ask them to include the NPU setting in their firmware baseline.
4. Some vendors offer a BIOS settings backup/export — use it if available.
5. If the toggle keeps reverting on its own (without updates), report it to the maker — that indicates a firmware bug, and newer BIOS releases often fix it.

## Closing

Enabling the NPU in BIOS is a five-minute job once you know the menu label your vendor uses — the hard part is only finding it. After enabling, Windows still needs its driver, so treat firmware and software as two halves of one fix. On Snapdragon machines, the firmware side pairs with the [Qualcomm Hexagon driver](/articles/qualcomm-hexagon-npu-driver-windows/) specifically. And remember to recheck the toggle after every BIOS update; firmware has a habit of quietly resetting exactly the setting you just fixed. If the machine then runs hot under AI loads, our [NPU overheating guide](/articles/npu-overheating-laptop/) is the natural next read.
