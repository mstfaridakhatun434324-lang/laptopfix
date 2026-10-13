---
title: "Fingerprint Reader Not Working on Windows 11? Here's How to Fix It"
slug: how-to-fix-fingerprint-reader-not-working-on-windows-11
date: 2026-09-19
categories: ["drivers"]
tags: ["fingerprint reader", "windows hello", "windows 11", "biometric driver"]
description: "Windows Hello fingerprint unavailable on Windows 11? Repair the biometric driver, restart the biometric service, and re-enroll with this step-by-step guide."
thumbnail: "/images/thumbs/how-to-fix-fingerprint-reader-not-working-on-windows-11.webp"
faqs:
  - q: "Why does Windows 11 say my fingerprint option is unavailable?"
    a: "Windows Hello cannot reach the biometric sensor. On Windows 11 the usual causes are a driver replaced by a feature update, the Windows Biometric Service stopped, or enrollment data invalidated by the driver change. The sensor hardware is rarely at fault — driver and service repairs restore it in most cases."
  - q: "Do I need to set up a PIN before fixing the fingerprint?"
    a: "Windows Hello requires a PIN as the fallback credential, and fingerprint setup will not proceed without one. If your PIN is also broken, fix it first in Settings, then Accounts, then Sign-in options. The fingerprint repair itself does not touch your PIN — it stays exactly as configured."
  - q: "Where do I get the correct fingerprint driver?"
    a: "From your laptop manufacturer's support site, for your exact model — Lenovo, Dell, HP, ASUS, or Acer. The vendor's biometric driver is matched to the sensor (Synaptics, ELAN, Goodix) in your machine. Generic Windows drivers often enumerate the reader without enabling enrollment, which is the classic looks-fine-but-does-nothing symptom."
  - q: "Will I lose my saved fingerprints during the fix?"
    a: "Only if you explicitly remove them, which this guide recommends as one step — corrupted enrollment templates can survive a driver fix and keep failing. Removing and re-scanning your finger takes two minutes and ensures the templates match the repaired driver. Your PIN and password are unaffected."
---

You press your finger to the reader and Windows 11 shrugs: "This option is currently unavailable," or the reader never lights up, or enrollment fails halfway. It worked before the update. Now Windows Hello pretends the sensor does not exist.

On Windows 11 the fingerprint chain has four links: the biometric driver, the Windows Biometric Service, the TPM-backed Hello credential store, and your enrollment data. Feature updates — 24H2 especially — love breaking the first link by swapping in an incompatible driver, which silently invalidates the fourth. Repair in chain order and the reader comes back. (Windows 10 owners: the same chain applies with older menus — see our [Windows 10 fingerprint guide](/articles/how-to-fix-fingerprint-reader-not-working-on-windows-10/).)

## Why this happens

- **Feature update replaced the biometric driver.** 24H2 installed a generic driver that cannot drive the sensor.
- **Windows Biometric Service stopped.** The broker service is disabled or crashed after the update.
- **Enrollment data invalidated.** Stored templates no longer match the new driver version.
- **Reader disabled in Device Manager.** The update disabled the biometric device instead of removing it.
- **PIN credential corrupted.** A broken Hello PIN blocks fingerprint setup and recognition.
- **TPM or Secure Boot state changed.** Firmware updates reset the security foundation Hello needs.
- **Power management suspending the reader.** USB power saving kills the sensor between uses.
- **Sensor surface contaminated.** Oils and grime prevent reliable reads and enrollments.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean the sensor and verify the PIN

Wipe the reader with a dry microfiber cloth. Then open **Settings > Accounts > Sign-in options** and confirm your **PIN** works — remove and re-add the PIN if it errors, since Hello fingerprint depends on a healthy PIN. Note the exact fingerprint status message: "unavailable" points at driver/service, while failed recognition with a working setup points at enrollment data. This two-minute triage tells you which fixes matter most.

### Fix 2: Check Device Manager

Open **Device Manager** and expand **Biometric devices**. Your reader (Synaptics, ELAN, Goodix, or similar) should be listed without warnings. A down arrow means disabled — right-click and **Enable device**. A yellow warning means driver failure — continue below. If the whole Biometric devices category is missing, click **Action > Scan for hardware changes** and watch for new unknown devices. A reader absent after scanning, with no unknown devices, suggests a BIOS-level disable or hardware fault.

### Fix 3: Restart the Windows Biometric Service

Press **Windows + R**, type `services.msc`, and press Enter. Locate **Windows Biometric Service**, set its **Startup type** to **Automatic**, and click **Start** or **Restart**. Then restart the laptop and test. This service brokers every Hello biometric transaction — when 24H2 leaves it stopped or set to Manual, the reader is invisible to Windows Hello regardless of driver health. It is a thirty-second fix that resolves a real share of cases.

### Fix 4: Reinstall the vendor biometric driver

In Device Manager, right-click the reader under Biometric devices, choose **Uninstall device**, and check **Attempt to remove the driver for this device**. Restart. Then download the **fingerprint/biometric driver** for your exact model from [Lenovo support](https://support.lenovo.com/us/en/), [Dell support](https://www.dell.com/support), or [HP support](https://support.hp.com/us-en), install it, and restart again. The vendor driver is matched to your sensor hardware — generic drivers enumerate without functioning. Verify in Device Manager that the provider shows the vendor or sensor maker, not Microsoft. In rare cases a driver signature problem blocks the biometric driver from loading; our guide on [driver signature enforcement](/articles/how-to-disable-driver-signature-enforcement-in-windows-11-24h2/) explains that scenario. After the vendor driver is installed, confirm Device Manager shows the vendor's driver version — Windows Update sometimes swaps it back within hours, so verify before you celebrate.

### Fix 5: Remove and re-enroll fingerprints

Go to **Settings > Accounts > Sign-in options > Fingerprint recognition**, choose **Remove**, and restart. Then enroll fresh: follow the wizard, scanning slowly from multiple angles, and add a second finger as backup. Old templates calibrated to the broken driver keep failing against the fixed one — this is the "reader lights up but never recognizes me" pattern. Fresh enrollment against the repaired driver resolves it. Test unlock from a cold boot, not just from sleep, and enroll in a well-lit room with clean, dry hands — moisture and dirt are the most common reasons enrollment fails repeatedly even with a perfectly healthy driver and sensor. If one finger consistently fails, try another; some fingers simply scan better than others.

### Fix 6: Disable USB power saving for the reader

Many readers sit on an internal USB bus. In Device Manager, expand **Universal Serial Bus controllers**, open each **USB Root Hub > Properties > Power Management**, and uncheck **Allow the computer to turn off this device to save power**. In **Settings > System > Power & battery**, open the advanced power settings and set **USB selective suspend** to **Disabled**. This fixes readers that work after a restart but go dead after sleep — the sensor suspends and the driver cannot wake it. Retest across a full sleep/wake cycle.

### Fix 7: Check BIOS, TPM, and firmware

Restart into the BIOS/UEFI (F2, Del, or your brand's key) and confirm the fingerprint/biometric device is enabled and the **TPM** is on and active — Windows Hello needs both. Check the manufacturer's site for a **BIOS update** and flash it with the charger connected, since biometric initialization fixes ship in firmware. If the reader is enabled in BIOS, carries the vendor driver, the service runs, enrollment is fresh, and Hello still reports it unavailable, the sensor module itself has likely failed — a service-center repair.

## Closing

Windows 11 fingerprint failures are chain failures: driver, service, enrollment. Work the chain in order — vendor driver, biometric service on Automatic, fresh enrollment — and the reader comes back in the large majority of cases. Pin the working driver against future updates, because the next feature update is the most likely thing to break it again.
