---
title: "Fingerprint Reader Not Working on Windows 10: A Technician's Fix Guide"
slug: how-to-fix-fingerprint-reader-not-working-on-windows-10
date: 2026-09-05
categories: ["drivers"]
tags: ["fingerprint reader", "windows hello", "windows 10", "biometric driver"]
description: "Windows Hello says your fingerprint isn't available on Windows 10? This guide covers every fix — biometric driver repair, service restarts, and clean re-enrollment."
thumbnail: "/images/thumbs/how-to-fix-fingerprint-reader-not-working-on-windows-10.webp"
faqs:
  - q: "Why does Windows 10 say my fingerprint reader isn't available?"
    a: "That message means Windows Hello cannot communicate with the biometric sensor. The usual causes are a broken or outdated biometric driver, the Windows Biometric Service being stopped, or corrupted enrollment data. Reinstalling the driver and restarting the biometric service resolves it in most cases without touching your PIN or password."
  - q: "Will fixing the fingerprint reader delete my PIN?"
    a: "No. Your PIN is stored separately in the TPM and credential manager, and driver-level fixes do not touch it. Only removing and re-adding the fingerprint itself deletes the old scans — you will simply scan your finger again. Your PIN and password sign-in options remain exactly as they were."
  - q: "Do I need a special driver for the fingerprint reader?"
    a: "Yes — fingerprint readers need the vendor's biometric driver, not the generic Windows one. Get it from your laptop manufacturer's support site for your exact model. The generic driver often enumerates the device but cannot perform enrollment or recognition, which produces the classic works-in-Device-Manager but not in Windows Hello symptom."
  - q: "Can a Windows update break the fingerprint reader?"
    a: "Regularly. Updates replace biometric drivers with incompatible versions, reset biometric service settings, or invalidate enrollment data when the underlying driver changes. If the reader died right after an update, rolling back the biometric driver or reinstalling the vendor package is the first fix to try."
---

You lift the lid, rest your finger on the reader — and nothing happens. Windows 10 says "this option is currently unavailable" under fingerprint sign-in, or the reader light never comes on, or enrollment fails with a vague error. The sensor worked last month, and now Windows Hello acts like the hardware does not exist.

Fingerprint readers live at the intersection of three systems: the biometric driver, the Windows Biometric Service, and Windows Hello's enrollment database. When one breaks — usually the driver after an update — the whole chain goes silent. The repair order matters: verify the hardware is seen, fix the driver, restart the services, then re-enroll. If you are on Windows 11 instead, the same concepts apply — see our [Windows 11 fingerprint repair guide](/articles/how-to-fix-fingerprint-reader-not-working-on-windows-11/) for the version-specific screens.

## Why this happens

- **Biometric driver broken by a Windows update.** The update replaced the vendor driver with an incompatible generic one.
- **Windows Biometric Service stopped or disabled.** The service that brokers between Hello and the sensor is not running.
- **Corrupted enrollment data.** Stored fingerprint templates no longer match the current driver version.
- **Fingerprint reader disabled in Device Manager.** The update disables the biometric device rather than removing it.
- **Vendor control software conflicting.** Old fingerprint utility apps block the new driver from binding.
- **TPM or security setting changed.** BIOS updates can reset TPM or biometric authentication settings.
- **Power management cutting the sensor.** USB power saving suspends the reader before Hello can use it.
- **Dirty or worn sensor surface.** Physical contamination prevents reliable reads and failed enrollments.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean the sensor and check the basics

Wipe the fingerprint reader with a dry microfiber cloth — skin oils and dust are a genuine cause of failed reads. Then open **Settings > Accounts > Sign-in options** and look at the Fingerprint section. If it says the reader is unavailable, note the exact wording; if it offers setup, try enrolling again before doing driver work. Also confirm you have a **PIN** set up — Windows Hello fingerprint requires a PIN as a fallback, and a corrupted PIN blocks fingerprint setup entirely. If the PIN itself errors, remove and re-add it in Sign-in options before continuing.

### Fix 2: Check Device Manager for the biometric device

Open **Device Manager** and expand **Biometric devices** — you should see your fingerprint reader (Synaptics, ELAN, Goodix, or similar). If it has a down arrow, right-click and choose **Enable device**. If it shows a yellow warning, the driver is broken — continue to the next fixes. If the Biometric devices section is missing entirely, click **Action > Scan for hardware changes**, and check whether the reader appears under **Unknown devices**. A completely absent reader after scanning points to a BIOS-level disable or a hardware fault.

### Fix 3: Restart the Windows Biometric Service

Press **Windows + R**, type `services.msc`, and press Enter. Find **Windows Biometric Service**, double-click it, set **Startup type** to **Automatic**, and click **Start** (or **Restart** if already running). This service is the broker between Windows Hello and the sensor — when an update leaves it stopped or set to manual, Hello reports the reader as unavailable even with a perfect driver. Restart the laptop after starting the service and retest sign-in.

### Fix 4: Reinstall the biometric driver

In Device Manager, right-click the fingerprint reader under Biometric devices and choose **Uninstall device**, checking **Attempt to remove the driver for this device** if offered. Restart. Windows will install a driver on boot — test Windows Hello. The generic driver sometimes restores basic function, but for reliable enrollment and recognition you want the vendor package: download the **fingerprint / biometric driver** for your exact model from [Lenovo support](https://support.lenovo.com/us/en/), [Dell support](https://www.dell.com/support), or [HP support](https://support.hp.com/us-en), install it, and restart again.

### Fix 5: Remove and re-enroll your fingerprints

Corrupted enrollment templates survive driver fixes and keep failing silently. Go to **Settings > Accounts > Sign-in options > Fingerprint**, choose **Remove** to delete the stored prints, and restart. Then enroll fresh — scan the same finger from several angles, slowly, as the wizard instructs. Enroll the finger you actually use to unlock the laptop daily, and consider adding a second finger as backup. Fresh enrollment against the fixed driver resolves the "reader works but never recognizes me" class of problems.

### Fix 6: Disable USB power management for the reader

Many fingerprint readers connect over internal USB, and Windows 10's power saving can suspend them. In Device Manager, expand **Universal Serial Bus controllers**, and for each **USB Root Hub**, open **Properties > Power Management** and uncheck **Allow the computer to turn off this device to save power**. Then go to **Settings > System > Power & sleep > Additional power settings**, open your plan's advanced settings, and set **USB settings > USB selective suspend** to **Disabled**. This fixes readers that work after a restart but die after the laptop sleeps.

### Fix 7: Check BIOS biometric settings and update firmware

Restart into the BIOS (F2, Del, or your brand's key) and look for fingerprint, biometric, or security-device toggles — ensure the reader is enabled. Check that the **TPM** is enabled and active, since Windows Hello depends on it. While you are on the manufacturer's support site, check for a **BIOS update** — firmware updates regularly include fixes for biometric device initialization. Flash with the charger connected. If the reader is enabled in BIOS, has the vendor driver, the service is running, and Hello still reports it unavailable, the sensor hardware itself has likely failed and needs service. Driver signature problems can also block biometric drivers in rare cases — our guide on [disabling driver signature enforcement](/articles/how-to-disable-driver-signature-enforcement-in-windows-11-24h2/) explains when that step is appropriate.

## Closing

Fingerprint reader failures on Windows 10 are a chain problem — driver, service, enrollment — and the fix is to repair the chain in order. Start with the sensor and Device Manager, reinstall the vendor biometric driver, restart the Windows Biometric Service, and finish with a fresh enrollment. Once it works, keep the vendor driver pinned and be wary of letting Windows Update swap biometric drivers automatically.
