---
title: "How to Update Drivers on Windows 11: The Complete Safe Method"
slug: how-to-update-drivers-on-windows-11
date: 2026-09-30
categories: ["drivers"]
tags: ["update drivers", "windows 11", "device manager", "driver update", "oem drivers"]
description: "Update drivers on Windows 11 the safe way: the correct order, the right sources, and how to recover if a new driver misbehaves."
thumbnail: "/images/thumbs/how-to-update-drivers-on-windows-11.webp"
faqs:
  - q: "Is it safe to update all my drivers at once?"
    a: "No. Update one driver at a time and reboot between critical ones like chipset, graphics, and network. Updating everything at once makes it impossible to identify which new driver caused a problem. Create a system restore point first, so any bad update can be rolled back in minutes."
  - q: "Should I use Windows Update or the manufacturer's website for drivers?"
    a: "Use the manufacturer's website first for chipset, graphics, Wi-Fi, and audio drivers, because OEM packages include laptop-specific tuning. Use Windows Update as a supplement for anything the manufacturer does not provide. Never use third-party driver updater tools, which are a common source of wrong or bundled drivers."
  - q: "How often should I update my laptop's drivers?"
    a: "Check quarterly for most drivers, and update graphics drivers when a game or creative app you use recommends it. Do not chase every new release — if the laptop works well, a driver update is optional. Update promptly only when you are fixing a specific problem or a security bulletin names your hardware."
  - q: "What do I do if a new driver makes things worse?"
    a: "Open Device Manager, right-click the device, choose Properties, go to the Driver tab, and click Roll Back Driver. If that option is greyed out, use System Restore to return to the restore point you made before updating. Then report the bad version and stay on the previous one until a fixed release appears."
---

Updating drivers on Windows 11 sounds like routine maintenance, and it is — but the difference between a smooth update and a broken laptop comes down to order, source, and having a way back. Windows will happily install drivers on its own through Windows Update, yet those are generic, months-old versions. The manufacturer's drivers are tuned for your exact machine. Knowing which source to use for each component, and in what sequence, is the whole skill.

This guide gives you the technician's method: prepare a restore point, work in the right order, use the right source for each driver, and verify each step. Done this way, driver updates fix problems instead of creating them.

## Why this happens

- **Windows Update drivers are generic:** Microsoft's catalog favors broad compatibility over your laptop's specific thermal and power tuning.
- **Drivers go stale silently:** Unlike apps, drivers rarely notify you of updates, so machines run years-old graphics and Wi-Fi drivers without anyone noticing.
- **Wrong source, wrong behavior:** A generic Intel or NVIDIA package can lack the OEM customizations your laptop's cooling and power profiles depend on.
- **Update order matters:** Installing graphics before the chipset, or audio before the chipset, can leave devices misconfigured or invisible.
- **Third-party updaters cause damage:** "Driver booster" style tools routinely install wrong, mismatched, or bundled drivers that create the problems they claim to fix.
- **Skipped reboots corrupt installs:** Many driver installers need a reboot to finish registering; stacking installs without rebooting leaves half-configured devices.
- **No rollback plan:** Updating without a restore point turns a ten-minute fix into a multi-hour recovery when a new driver misbehaves.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Create a system restore point first

Before touching any driver, press Win + S, type "Create a restore point," open it, select your system drive, and click Create. Name it something like "Before driver updates" with today's date. This takes about a minute and is your escape hatch: if any update goes wrong, System Restore returns the drivers and system files to this exact state without touching your documents. Skip this step and a bad graphics driver can cost you an afternoon; keep it and the same failure costs ten minutes. Make restore-point creation a reflex before every driver session, not just this one.

### Fix 2: Inventory what you have and what needs updating

Open Device Manager (Win + X) and expand each category, looking for yellow warning icons — those are your priority targets. For the big four — chipset, graphics, Wi-Fi, audio — note the current driver version and date via Properties, Driver tab. Then check your manufacturer's support page for your exact model and compare versions. You only need to update drivers where the manufacturer offers something meaningfully newer, or where you have a symptom. "Update everything because updates exist" is how working laptops get broken. Learn to [check driver versions in Device Manager](/articles/how-to-check-driver-version-in-device-manager-on-windows-11/) precisely so your comparisons are accurate.

### Fix 3: Download from the manufacturer, in the right order

Go to your laptop maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — enter your exact model or service tag, and download drivers in this order: chipset first, then graphics, then network (Wi-Fi/Ethernet), then audio, then everything else (touchpad, card reader, Bluetooth). The chipset defines how Windows sees the motherboard, so it must go first; everything else registers against it. Save each installer to a clearly named folder. If the manufacturer has no package for a component, note it — those gaps get filled by Windows Update later. Never substitute a desktop driver package for a laptop component.

### Fix 4: Install one driver at a time with reboots

Run the chipset installer as administrator, reboot when asked, and confirm the machine comes back cleanly before touching the next driver. Repeat for graphics, network, and audio. This feels slow, but it is the only way to know which update caused a problem if one appears. If an installer offers "clean install" (NVIDIA's does), take it for graphics drivers — it removes old profiles that cause conflicts. Between installs, do a quick smoke test: Wi-Fi connects, sound plays, the display looks right. For NVIDIA cards specifically, our guide to [clean-installing NVIDIA drivers](/articles/how-to-update-nvidia-drivers-clean-install-on-windows-11/) walks through the options that prevent leftover-file conflicts.

### Fix 5: Use Device Manager for components with no installer

Some drivers arrive as INF files or have no setup program. In Device Manager, right-click the device, choose Update driver, then "Browse my computer for drivers," and point at the extracted folder. Alternatively, choose "Search automatically for drivers" to let Windows check its catalog. The automatic search is fine for minor components like card readers and sensors — save the manufacturer-first rule for the big four. After each manual install, confirm the version changed on the Driver tab. If Windows insists the best driver is already installed but you know a newer one exists, the manual browse method overrides that verdict.

### Fix 6: Let Windows Update fill the remaining gaps

Once the manufacturer's drivers are in, open Settings, Windows Update, and check for updates, including the "Optional updates" section where driver updates hide. Install what it offers for components you skipped — these are safe precisely because the critical drivers are already handled. Then go to Device Manager one final time and confirm no yellow warnings remain anywhere. If an unknown device persists, right-click it, check its hardware ID, and search it — or follow our guide for [fixing unknown devices in Device Manager](/articles/how-to-fix-unknown-device-in-device-manager-on-windows-11/). Microsoft's Windows support hub documents the optional-updates flow if you want the official reference.

### Fix 7: Verify stability and know how to roll back

Use the laptop normally for a day: sleep and wake it a few times, run a video call, play something with sound, connect to Wi-Fi from cold boot. Driver problems often surface at power transitions, not during the install. If something regressed, open Device Manager, find the device, open Properties, Driver tab, and click Roll Back Driver. If rollback is unavailable, run System Restore and pick the restore point from Fix 1. Then note which version failed and stay on the working one. A driver update that breaks something is not a personal failure — it is exactly what the restore point was for.

## Closing

Safe driver updating is a discipline, not a chore: restore point first, inventory second, manufacturer packages in chipset-to-peripherals order, one at a time with reboots, Windows Update for the leftovers, and a day of stability testing. Follow that sequence and driver updates become what they should be — quiet improvements instead of surprises. Your future self, facing a misbehaving update, will be grateful for the ten minutes you spent on step one.
