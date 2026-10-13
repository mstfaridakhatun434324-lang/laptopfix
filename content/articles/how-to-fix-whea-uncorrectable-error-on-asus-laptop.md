---
title: "How to Fix WHEA_UNCORRECTABLE_ERROR on an ASUS Laptop"
slug: how-to-fix-whea-uncorrectable-error-on-asus-laptop
date: 2026-09-02
categories: ["windows-errors"]
tags: ["bsod", "whea-error", "asus"]
description: "WHEA_UNCORRECTABLE_ERROR crashing your ASUS laptop? From BIOS updates to MyASUS diagnostics, here's the complete fix path."
thumbnail: "/images/thumbs/how-to-fix-whea-uncorrectable-error-on-asus-laptop.webp"
faqs:
  - q: "What triggers WHEA_UNCORRECTABLE_ERROR on ASUS laptops?"
    a: "The same hardware-class causes as other brands — CPU, RAM, NVMe SSD, or board-level faults — plus ASUS-specific angles: Armoury Crate performance profiles pushing unstable settings, outdated BIOS on new Intel/AMD platforms, and MyASUS-updated drivers conflicting with Windows Update versions."
  - q: "How do I run diagnostics on an ASUS laptop for WHEA errors?"
    a: "Use the MyASUS app: open it, go to Customer Support > System Diagnostics, and run the hardware checks for CPU, memory, and storage. For pre-boot testing, power on and tap F2 for BIOS, or use the MyASUS UEFI diagnostics available on many models via the boot menu."
  - q: "Can Armoury Crate cause WHEA_UNCORRECTABLE_ERROR?"
    a: "It can contribute. Armoury Crate's performance modes, manual fan curves, and CPU/GPU tuning can push hardware into instability, especially combined with heat. If crashes started after changing Armoury Crate settings, reset everything to default (or uninstall it temporarily) and retest."
  - q: "Is WHEA_UNCORRECTABLE_ERROR covered by ASUS warranty?"
    a: "If diagnostics confirm a hardware fault (CPU, RAM, SSD, motherboard) and the laptop is within warranty with no physical damage, yes — ASUS warranty covers component failure. Run MyASUS diagnostics first and save any error codes; support will ask for them."
---
WHEA_UNCORRECTABLE_ERROR on an ASUS laptop — whether it's a VivoBook, Zenbook, TUF, or ROG — means Windows' hardware error system caught a fault it couldn't correct. On ASUS machines, the story usually involves one of three things: firmware that's behind, a component (often the SSD or RAM) starting to fail, or performance software pushing the hardware too hard.

Here's the full fix path, ASUS-specific where it matters.

One reassuring note before you start: despite the alarming name, WHEA errors on ASUS laptops resolve to software or firmware causes more often than dead hardware. The BIOS update and diagnostics steps below settle the question quickly — if MyASUS diagnostics pass and a BIOS update stops the crashes, you never needed to worry about the CPU at all. Work the list in order and let the evidence guide you rather than assuming the worst.

## Why this happens

- **Outdated BIOS** — ASUS releases BIOS updates with CPU microcode and stability fixes; old BIOS on new platforms trips WHEA faults.
- **Failing NVMe SSD** — storage controller errors are a leading real-world WHEA trigger.
- **Unstable RAM** — bad cells or mismatched aftermarket upgrades.
- **Overheating** — dust-clogged cooling on thin Zenbooks/VivoBooks, or dried paste on older gaming models.
- **Armoury Crate / MyASUS performance tuning** — aggressive profiles destabilizing CPU/GPU under load.
- **Corrupt chipset or storage drivers** — mismatched Intel/AMD chipset or NVMe drivers.
- **Genuine CPU or board fault** — the rare but real last resort.

## How to fix it

Work through these in order, testing stability for a day between major steps.

### Fix 1: Update the BIOS from ASUS support

The highest-yield single step for WHEA on ASUS.

1. Find your exact model: press **Windows + R**, type `msinfo32`, note **System Model** and **BIOS Version/Date** (or check the sticker on the bottom).
2. Go to ASUS support, search your model, open **Driver & Utility**, select your Windows version, and download the latest **BIOS** file.
3. ASUS BIOS updates come as a renamed file for EZ Flash or a Windows installer — follow the model's instructions exactly. Plug in the AC adapter and don't interrupt the process for any reason.
4. Alternatively, use **MyASUS** > **Customer Support** > **Live Update** to pull the BIOS — it handles model-matching for you.
5. After the update, use the laptop normally for a day and watch for crashes.

### Fix 2: Run MyASUS system diagnostics

Let ASUS's own tools check the hardware.

1. Open the **MyASUS** app (preinstalled; or install it from the Microsoft Store).
2. Go to **Customer Support** > **System Diagnostics**.
3. Run the checks for **CPU**, **Memory**, and **Storage** — the full set if time allows.
4. Note any failure codes. You can also access a pre-boot version: restart, tap **F2** for BIOS, and look for diagnostics options on supported models.
5. Clean passes move you to software fixes with confidence; failures tell you exactly which part to address.

### Fix 3: Reset Armoury Crate and performance settings

Undo any tuning that could destabilize hardware.

1. Open **Armoury Crate** (gaming models) and set the operating mode to **Silent** or **Performance** default — remove any **Manual** mode customizations (custom fan curves, CPU/GPU overclocks, undervolts).
2. On non-gaming models, open **MyASUS** > **Customization** and reset power/performance profiles to defaults.
3. If you used ThrottleStop, Intel XTU, or MSI Afterburner, reset or uninstall them.
4. Retest for a day at stock settings — stability here confirms tuning was the trigger.

### Fix 4: Update chipset and storage drivers

Refresh the drivers between Windows and the hardware.

1. In MyASUS > **Customer Support** > **Live Update**, install all offered **Chipset** and storage-related updates.
2. Supplement from ASUS's support site for your model if Live Update shows nothing — download the chipset package manually.
3. In **Device Manager** (**Windows + X**), check **Storage controllers** and **Firmware** for your SSD — update anything offered.
4. For Intel models, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) catches chipset and wireless drivers ASUS hasn't packaged.

### Fix 5: Test the memory

RAM faults are a classic WHEA source.

1. Press **Windows + R**, type `mdsched.exe` > **Restart now and check for problems**.
2. For a deeper test, run MemTest86 from a bootable USB for at least one full pass.
3. If your ASUS has upgradeable RAM and you added a stick yourself, test with only the original stick installed — mismatched pairs cause exactly these crashes.
4. Reseat removable modules (power off, unplug, remove bottom panel, reseat firmly) before replacing.

### Fix 6: Address cooling

Heat-induced CPU errors are common on thin ASUS models.

1. Monitor temps with HWMonitor during your normal workload — sustained CPU above ~95°C is problem territory.
2. Blow compressed air through the vents with the laptop off and cool.
3. On gaming models, verify fans actually spin up under load in Armoury Crate's manual fan view — a dead fan on a TUF/ROG causes rapid thermal crashes.
4. Persistent overheating after cleaning suggests dried thermal paste — a repaste at a service center is the fix.

### Fix 7: Reset Windows or pursue hardware service

The final fork in the road.

1. If all diagnostics pass but crashes continue, do **Settings** > **System** > **Recovery** > **Reset PC** > **Keep my files** > **Cloud download** — this rules out deep software corruption.
2. Install ASUS chipset and BIOS drivers first after the reset, then test before reinstalling apps.
3. If crashes survive a reset with clean drivers, or diagnostics flagged hardware: contact ASUS support with your diagnostic error codes. In-warranty component failure (SSD, RAM, board) is a warranty claim — don't open the laptop for board-level issues while covered.

## Closing

WHEA_UNCORRECTABLE_ERROR on ASUS laptops most often yields to a BIOS update, a settings reset in Armoury Crate, or identifying a failing SSD/RAM stick via MyASUS diagnostics. Run the diagnostics early — they turn a scary hardware-class error into a specific, actionable finding. For the Dell counterpart to this guide, see [WHEA_UNCORRECTABLE_ERROR on Dell](/articles/how-to-fix-whea-uncorrectable-error-on-dell-laptop/), and for WHEA crashes that only happen under gaming load, [blue screen while gaming on Acer](/articles/how-to-fix-blue-screen-while-gaming-on-acer-laptop/) covers the thermal angle. Community threads like [the WHEA Reddit discussions](/articles/how-to-fix-whea-uncorrectable-error-reddit/) also collect real-world fix reports worth browsing.
