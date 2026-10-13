---
title: "How to Install Chipset Drivers on Windows 10"
slug: how-to-install-chipset-drivers-on-windows-10
date: 2026-09-02
categories: ["drivers"]
tags: ["chipset drivers windows 10", "install chipset driver", "intel chipset driver", "amd chipset driver", "sm bus controller driver"]
description: "Missing chipset drivers cause unknown devices and flaky USB, storage, and power behavior. Here's how to identify your chipset and install the right driver on Windows 10."
thumbnail: "/images/thumbs/how-to-install-chipset-drivers-on-windows-10.webp"
faqs:
  - q: "What are chipset drivers and why do they matter?"
    a: "Chipset drivers are the software interface between Windows and your motherboard's chipset — the silicon managing USB controllers, SATA storage, PCI Express lanes, power management, and the SMBus. Without the right chipset driver, Windows falls back to generic drivers that work but miss optimizations, or leaves devices as 'Unknown' in Device Manager. Symptoms of missing chipset drivers include flaky USB ports, missing power management features, and unrecognized system devices."
  - q: "How do I know which chipset my laptop has?"
    a: "The chipset follows the CPU: Intel CPUs use Intel chipsets, AMD CPUs use AMD chipsets. For the exact model, check Device Manager under System devices for entries like 'Intel Chipset' or 'AMD SMBus', or run msinfo32 and look at the processor line — then match it to the chipset family on the manufacturer's site. Your laptop maker's support page is the easiest path: enter your model and download their chipset package without needing to identify the silicon yourself."
  - q: "Should I get chipset drivers from Intel/AMD or my laptop maker?"
    a: "For laptops, start with your laptop maker's support site — their chipset package is validated for your specific board, power configuration, and custom devices. Intel and AMD's generic chipset drivers work on most hardware and are sometimes newer, making them a good second choice if the maker's package is ancient. Avoid mixing: install one source's package cleanly rather than layering both."
  - q: "Do I need to update chipset drivers regularly?"
    a: "No — chipset drivers are 'install once, update rarely' software. Unlike graphics drivers, they don't get meaningful monthly improvements. Update them when you're troubleshooting USB, storage, or power issues, after a clean Windows install, or when the manufacturer releases a version fixing a specific bug affecting you. If everything works, leave them alone; unnecessary chipset updates are a classic source of new problems."
---

Chipset drivers are the unglamorous foundation Windows 10 stands on: they tell the OS how to talk to the USB controllers, storage interfaces, power management circuitry, and system buses built into your motherboard's chipset. When they're missing or wrong, the symptoms are vague and scattered — unknown devices in Device Manager, USB ports that misbehave, sleep that doesn't quite work — which is why chipset drivers are worth understanding even though you'll rarely think about them.

This guide covers identifying your chipset, choosing the right driver source, installing it correctly, and verifying the result. It's written for Windows 10, where driver management behaves slightly differently than Windows 11.

One thing that confuses people: the "chipset driver" is not really a single driver but a bundle of INF files — text files that tell Windows the names, capabilities, and registry settings for dozens of motherboard devices at once. Installing it rarely adds a visible program; instead, unknown devices in Device Manager quietly get proper names and the OS learns how to manage power states, bus speeds, and interrupt routing for your specific board. If you install it and "nothing seems to happen," that is normal — check Device Manager, not the desktop, for the evidence.

## Why this happens

Chipset driver problems typically surface as:

- **Unknown devices** in Device Manager (especially "SM Bus Controller" and "PCI Device").
- **USB ports misbehaving** — the chipset owns the USB host controllers.
- **Missing power management features** — sleep states and CPU power tuning need chipset support.
- **Windows Update installed a generic driver** that lacks board-specific optimizations.
- **Clean Windows install** with no manufacturer drivers yet applied.
- **Wrong chipset package installed** (desktop package on a laptop, or Intel on AMD).
- **Corrupted chipset INF** after a failed update leaving devices half-configured.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify your chipset and current driver state

Know what you're working with before downloading anything.

1. Press **Win + X**, open **Device Manager**, and expand **System devices**.
2. Look for entries naming Intel or AMD chipset components, and note any **Unknown devices** or **SM Bus Controller** entries with warning icons.
3. Press **Win + R**, type `msinfo32`, and note the **Processor** line — the chipset family follows the CPU brand and generation.
4. The easiest path: go to your laptop maker's support site, enter your exact model, and download their **chipset** driver — no silicon identification needed.

### Fix 2: Download the correct chipset package

Source matters more than version for chipset drivers.

1. **First choice:** your laptop maker's support site — model-specific and validated. For example, [HP's support site](https://support.hp.com/us-en) lists chipset drivers per model.
2. **Second choice:** the chip maker's own package — Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel systems, or [AMD's driver page](https://www.amd.com/en/support/download/drivers.html) for AMD systems.
3. Match the package to **Windows 10** and your architecture (64-bit for virtually all modern laptops).
4. If the maker's package is several years old but everything works, that's fine — chipset drivers don't need to be new to be correct.

### Fix 3: Back up before installing

Two minutes of insurance.

1. [Back up your current drivers](/articles/how-to-backup-drivers-before-update-on-laptop/) with DISM: `dism /online /export-driver /destination:C:\DriverBackup`
2. Create a system restore point named "Before chipset driver install."
3. Chipset installs touch many devices at once, so the safety net matters more here than for single-device drivers.

### Fix 4: Install the chipset driver package

The main event — straightforward but order-sensitive.

1. Close all applications. Disconnect unnecessary USB devices (keep keyboard/mouse).
2. Run the chipset installer **as administrator**.
3. Let it complete without interruption — it updates many device entries in sequence, and the screen may flicker as display-related components refresh.
4. **Restart when prompted**, even if everything looks fine. Many chipset changes only take effect after reboot.
5. After rebooting, open Device Manager and confirm the Unknown devices / SM Bus Controller entries are gone.

### Fix 5: Verify the installation took effect

Don't assume — check.

1. In Device Manager > **System devices**, right-click chipset entries > **Properties** > **Driver tab** and confirm the date/version match the package you installed. (See [how to check driver versions](/articles/how-to-check-driver-version-in-device-manager/) for the full method.)
2. Confirm no Unknown devices remain anywhere in Device Manager.
3. Test the subsystems the chipset owns: plug devices into USB ports, test sleep/wake, check that battery/power readings look sane.

### Fix 6: Handle a bad chipset install

If the new package made things worse.

1. Use **System Restore** to roll back to the restore point from Fix 3 — the fastest recovery.
2. Alternatively, reinstall your backed-up drivers with `pnputil /add-driver "C:\DriverBackup\*.inf" /subdirs /install`.
3. Then install the *other* source's package (if Intel's generic broke things, try the laptop maker's, or vice versa).
4. Report the bad version combination on the manufacturer's forum — chipset regressions get fixed when they're reported with exact model numbers.

### Fix 7: Set the update policy going forward

Keep chipset drivers stable long-term.

1. After a working install, use the show/hide updates troubleshooter to block Windows Update from replacing your chipset driver with its generic version.
2. Revisit chipset drivers only when troubleshooting related symptoms or after a clean Windows install.
3. Document the working version (screenshot the Driver tab) in your maintenance notes for next time.

## Closing

Chipset drivers are infrastructure: install the right package once from the right source, verify it, then leave it alone. Most "mysterious" laptop behaviors — flaky USB, odd power states, unknown devices — trace back to this layer, and a correct chipset install quietly fixes problems you didn't even associate with it. If USB issues persist after the chipset is correct, our [USB selective suspend guide](/articles/how-to-turn-off-usb-selective-suspend-on-windows-11/) addresses the power-management layer that sits on top. And if you're doing a broader driver refresh, pair this with [backing up your drivers first](/articles/how-to-backup-drivers-before-update-on-laptop/) — the habit that makes every driver change reversible.
