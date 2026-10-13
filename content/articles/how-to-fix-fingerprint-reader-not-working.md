---
title: "Fingerprint Reader Not Working? Fix Windows Hello Sign-In"
slug: how-to-fix-fingerprint-reader-not-working
date: 2026-09-17
categories: ["drivers"]
tags: ["fingerprint", "windows hello", "biometric", "sign-in", "troubleshooting"]
description: "Fingerprint reader not recognized or Windows Hello fingerprint setup fails? Fix biometric sign-in with driver, service, and enrollment steps."
thumbnail: "/images/thumbs/how-to-fix-fingerprint-reader-not-working.webp"
faqs:
  - q: "Why does Windows say my fingerprint reader isn't available?"
    a: "Windows Hello needs three things: a compatible reader, its biometric driver, and the Windows Biometric Service running. 'Not available' means one is missing — usually the driver after a Windows update, or the biometric service stopped. Device Manager and services.msc tell you which in under a minute."
  - q: "My fingerprint worked yesterday and stopped today. What happened?"
    a: "Overnight Windows updates are the prime suspect — they replace biometric drivers or reset the biometric service. Less commonly, a dirty or wet sensor, or a changed fingerprint (cut, dry skin), causes recognition failures that look like hardware problems. Check Windows Update history first: a driver update listed overnight is near-confirmation, and rolling it back is the fastest fix."
  - q: "Can I re-enroll my fingerprints to fix recognition issues?"
    a: "Yes — deleting all enrolled fingerprints and re-enrolling is the standard fix for recognition degradation. Enroll the same finger twice (it lets you add multiple prints) at different angles, with clean dry hands, for the most reliable recognition. If fresh enrollments still fail, reset the biometric database as described in Fix 6 — the template store itself may be corrupt."
  - q: "Is the fingerprint reader a separate device in Device Manager?"
    a: "Usually yes — look under Biometric devices, or sometimes under Human Interface Devices or System devices, depending on the maker. If it's missing entirely, check BIOS for a biometric toggle and scan for hardware changes before assuming it's dead."
---

The fingerprint reader is one of those features you don't appreciate until it's gone — suddenly you're typing a PIN like it's 2015. When Windows Hello fingerprint stops working, the failure sits in one of four places: the sensor hardware, the biometric driver, the Windows Biometric Service, or the enrolled fingerprint data itself. Each has a distinct fix, and the order matters.

Start with the recognition basics (dirty sensor, re-enrollment) only if the reader is detected but not recognizing. If Windows says no reader exists, that's a driver/service problem — different track entirely.

## Why this happens

- **The biometric driver was replaced or corrupted.** Windows Update is the usual culprit — the fingerprint driver is a frequent downgrade victim.
- **Windows Biometric Service isn't running.** Without this service, Hello can't talk to any biometric hardware.
- **Enrolled fingerprint data degraded.** Cuts, dry skin, or sensor wear change what the reader sees versus what's enrolled.
- **Dirty or wet sensor.** The most mundane cause — and the first to rule out.
- **BIOS-level biometric disable.** Business laptops especially have firmware toggles for biometrics.
- **Corrupted biometric database.** The stored templates can corrupt, producing failures that re-enrollment alone doesn't fix.
- **Hardware failure.** Dead sensor — rare, but it happens; usually total absence rather than flaky recognition.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean the sensor and test recognition basics

Thirty seconds, fixes the mundane cases.

1. Wipe the fingerprint sensor with a clean, dry microfiber cloth. Even invisible skin oil degrades reads.
2. Make sure your finger is **clean and dry** — wet fingers are the number-one false-failure cause.
3. Try the enrolled finger at slightly different angles and pressures. Try other enrolled fingers.
4. If recognition is flaky rather than totally dead, skip to Fix 5 (re-enrollment) — the hardware and driver are fine.

### Fix 2: Verify Windows sees the reader

Determines whether you're on the driver track or the enrollment track.

1. Open **Device Manager** and look under **Biometric devices** for the fingerprint reader. Also check **Human Interface Devices** and **System devices** — makers file them inconsistently.
2. If present without warnings → driver is loaded; the problem is service or enrollment (Fixes 3–5).
3. If present with a **yellow warning** → driver problem (Fix 4).
4. If **missing entirely** → check **View** > **Show hidden devices**, then **Action** > **Scan for hardware changes**. Still missing → check BIOS (Fix 6).

### Fix 3: Restart the Windows Biometric Service

The service Hello depends on.

1. Press **Win + R**, type `services.msc`, find **Windows Biometric Service**.
2. Make sure it's **Running** with startup type **Automatic**. If stopped, start it; if disabled, set to Automatic and start it.
3. Restart the service even if it appears running — a hung service reports "running" while doing nothing.
4. Go to **Settings** > **Accounts** > **Sign-in options** > **Fingerprint recognition (Windows Hello)** and check whether setup is now offered.
5. If the service won't stay running, continue to Fix 4 — a broken driver can crash it.

### Fix 4: Reinstall the biometric driver

The core repair for driver-track failures.

1. In Device Manager, right-click the fingerprint device > **Uninstall device**, checking "Attempt to remove the driver" if offered.
2. Restart the laptop.
3. Download the **biometric/fingerprint driver** for your exact model from the manufacturer's support page — for Lenovo systems, [Lenovo support](https://support.lenovo.com/us/en/) — and install as administrator.
4. Restart, verify the device appears without warnings, and recheck the Biometric Service (Fix 3).
5. Then re-enroll fingerprints (Fix 5) — driver changes can invalidate old templates.

### Fix 5: Delete and re-enroll fingerprints

For recognition failures with a healthy driver.

1. Go to **Settings** > **Accounts** > **Sign-in options** > **Fingerprint recognition (Windows Hello)** > **Remove** — delete all enrolled fingerprints.
2. Click **Set up** and enroll fresh: use clean, dry hands, and cover different angles and edges of the finger.
3. Enroll the same finger **twice** as two separate entries (different angles) — this dramatically improves reliability.
4. Enroll at least two different fingers in case of cuts.
5. Test lock/unlock several times. If recognition is still flaky with fresh enrollments and a clean sensor, suspect sensor wear (Fix 7). Additional enrollment edge cases are covered in our [Windows 11 fingerprint guide](/articles/how-to-fix-fingerprint-reader-not-working-in-windows-11-24h2/).

### Fix 6: Check BIOS and reset the biometric database

For missing readers and corrupted template stores.

1. Reboot into **BIOS/UEFI** and find the **fingerprint**, **biometric**, or **FPR** setting — set it to **Enabled**.
2. For corrupted databases: stop the Windows Biometric Service, then navigate to `C:\Windows\System32\WinBioDatabase` and rename the `.DAT` files (don't delete — rename, so you can restore). Restart the service and re-enroll.
3. This database reset fixes the stubborn cases where re-enrollment alone fails because the template store itself is corrupt.
4. Our related [fingerprint variant guide](/articles/how-to-fix-fingerprint-reader-not-working-on-windows-11/) covers additional enrollment edge cases.

### Fix 7: Confirm hardware as the final step

Only after the software track is exhausted.

1. If the reader is **missing from Device Manager** across driver reinstalls, BIOS toggles, and a Linux live USB test, the sensor hardware has likely failed.
2. Fingerprint readers are usually part of the palmrest or power-button assembly — replacement difficulty varies hugely by model; check the service manual.
3. Practical alternative: **Windows Hello face** (if your laptop has an IR camera) or **PIN** — both are first-class Hello methods and arguably more convenient.
4. Don't sink money into a fingerprint sensor repair on an old laptop when Hello face or PIN gives you the same passwordless sign-in.

Microsoft documents Windows Hello setup on the official [Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

Fingerprint failures split cleanly: reader detected but not recognizing means clean the sensor and re-enroll; reader missing or erroring means driver and Biometric Service. Work that split — sensor hygiene, Device Manager check, service restart, driver reinstall, fresh enrollment, BIOS toggle — and Hello fingerprint comes back. It's a convenience feature with a simple stack, and simple stacks are fixable.
