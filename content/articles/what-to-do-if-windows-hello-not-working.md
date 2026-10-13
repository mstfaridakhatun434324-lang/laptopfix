---
title: "Windows Hello Not Working? Here's What to Do"
slug: what-to-do-if-windows-hello-not-working
date: 2026-09-22
categories: ["windows-errors"]
tags: ["windows hello", "face recognition", "fingerprint", "biometric", "windows 11"]
description: "Windows Hello face or fingerprint sign-in suddenly stops working? Here's what to do — from re-enrolling biometrics to fixing the underlying driver."
thumbnail: "/images/thumbs/what-to-do-if-windows-hello-not-working.webp"
faqs:
  - q: "Why did Windows Hello suddenly stop working?"
    a: "The most common triggers are a Windows update that broke the biometric driver, a corrupted biometric enrollment database, disabled related services, or a BIOS update that changed how the fingerprint reader or IR camera is exposed to Windows. Physical causes matter too: a dirty fingerprint sensor or a camera blocked by a privacy shutter produces the exact same 'couldn't recognize you' errors as software failures."
  - q: "Will removing my PIN break Windows Hello?"
    a: "Yes — Windows Hello biometrics require a PIN as the fallback credential, and removing the PIN disables face and fingerprint sign-in with it. If your biometrics vanished after you removed the PIN, that's expected behavior, not a bug. Re-add a PIN under Settings > Accounts > Sign-in options, and the biometric options will become available again."
  - q: "Windows Hello says it's not available on this device. What now?"
    a: "That message means Windows can't see compatible biometric hardware. Check Device Manager for the biometric device — if it's missing or shows a warning icon, the driver is the problem. On some laptops a BIOS setting controls the fingerprint reader; a BIOS reset can silently disable it. Re-enable it in BIOS and reinstall the driver from your manufacturer's support page."
  - q: "Can I still sign in if Windows Hello is broken?"
    a: "Absolutely. Your PIN and password always work independently of biometrics — Hello is a convenience layer on top of them, not a replacement. If face or fingerprint fails, click Sign-in options on the login screen and choose the PIN or password icon. Fix Hello at your leisure; you're never locked out by a biometric failure alone."
---

Windows Hello is the kind of feature you take for granted until it breaks — then every login becomes a small annoyance. Whether it's face recognition that suddenly "can't recognize you," a fingerprint reader that stopped responding, or the sign-in options page declaring Hello "not available on this device," the failure always feels abrupt. It worked yesterday; today it doesn't.

In most cases the hardware is fine. Windows Hello depends on a chain: the biometric sensor, its driver, the Windows Biometric Service, your enrollment data, and the PIN that underpins it all. Break any link and Hello fails. Updates are the usual culprit — a Windows update replaces the biometric driver with a broken one, or a BIOS update changes how the sensor appears to the OS. The fixes below walk that chain from the simplest checks to driver surgery. And remember: your PIN and password always work regardless, so there's no emergency — fix it methodically.

## Why this happens

- **Broken biometric driver after a Windows update**: Updates frequently replace working fingerprint or IR camera drivers with generic or buggy versions.
- **Corrupted biometric enrollment data**: The stored face/fingerprint templates can corrupt, especially after a failed update or sudden shutdown during enrollment.
- **PIN removed or reset**: Hello biometrics require a PIN. Removing it disables face and fingerprint sign-in by design.
- **Windows Biometric Service disabled**: "Privacy" tweaking tools sometimes disable this service, killing Hello silently.
- **BIOS update changed sensor visibility**: Some laptops expose the fingerprint reader via a BIOS toggle; updates or resets can flip it off.
- **Dirty sensor or blocked camera**: Fingerprint readers fouled with grime, or IR cameras blocked by privacy shutters and stickers, fail exactly like software problems.
- **Conflicting security software**: Some third-party security suites hook the credential pipeline and break Hello enrollment or recognition.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical basics first

Rule out the embarrassingly simple causes before touching software.

1. Clean the fingerprint reader with a soft, dry cloth — skin oils and grime are a top cause of "sudden" failures.
2. For face recognition, check for a physical privacy shutter over the webcam (common on Lenovo ThinkPads) and remove any stickers covering the IR sensors beside the main camera lens.
3. Improve lighting — face recognition struggles in very dark rooms, though the IR camera should compensate.
4. Try enrolling the same finger at a slightly different angle, or reposition your face during recognition. If physical checks don't help, the problem is software — continue.

### Fix 2: Verify your PIN is set

No PIN means no Hello, by design.

1. Go to **Settings** > **Accounts** > **Sign-in options**.
2. Under **PIN (Windows Hello)**, confirm a PIN is set. If it says you need to add one, add it now.
3. Once the PIN exists, the **Facial recognition** and **Fingerprint recognition** sections should offer **Set up** buttons.
4. If the biometric sections still say "not available," continue — the hardware isn't being detected properly.

### Fix 3: Remove and re-enroll your biometrics

Corrupted enrollment data is fixed by starting over.

1. In **Settings** > **Accounts** > **Sign-in options**, expand **Facial recognition** or **Fingerprint recognition** and click **Remove**.
2. Restart the laptop — this clears any cached biometric state.
3. Return to the same page and click **Set up**, then follow the enrollment wizard carefully. For fingerprints, enroll the same finger twice at different angles if the wizard allows it.
4. Test sign-in by locking (**Windows + L**) and unlocking with the biometric. If enrollment itself fails with an error, the driver is the problem — continue to Fix 4.

### Fix 4: Reinstall the biometric driver

The driver is the most common real culprit, especially after updates.

1. Open **Device Manager** (**Windows + X** > **Device Manager**).
2. Look under **Biometric devices** for your fingerprint reader, and under **Cameras** or **Imaging devices** for the IR camera. If either shows a yellow warning icon — or is missing entirely — you've found it.
3. Right-click the device > **Uninstall device**, tick **Attempt to remove the driver for this device** if offered, then restart. Windows will attempt to reinstall on boot.
4. If Windows installs a generic driver that doesn't work, download the proper driver from your manufacturer's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or Lenovo — searching for your exact model plus "fingerprint" or "biometric."

### Fix 5: Check the Windows Biometric Service

A disabled service kills Hello without any obvious error.

1. Press **Windows + R**, type `services.msc`, and press Enter.
2. Find **Windows Biometric Service**. It should be **Running** with startup type **Automatic**.
3. If it's stopped or disabled, double-click it, set **Automatic**, click **Start**, and apply.
4. If a privacy or "debloater" tool disabled it, whitelist the service in that tool — otherwise it'll be disabled again on the next run. Microsoft documents Hello's requirements on their [support site](https://support.microsoft.com/en-us/windows).

### Fix 6: Check BIOS settings for the sensor

Some laptops gate the fingerprint reader behind a firmware toggle.

1. Restart and enter BIOS/UEFI setup (usually **F2**, **Del**, or **F1** depending on brand).
2. Look under **Security** for **Fingerprint**, **Biometric device**, or similar options and make sure they're **Enabled**.
3. While there, check that you haven't accidentally disabled the integrated camera if face recognition is the problem.
4. Save and exit. If the device appears in Device Manager after this but still doesn't work, reinstall its driver (Fix 4).

### Fix 7: Run the hardware troubleshooter and system repair

Rule out broader system damage.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** and run anything hardware-related your build offers.
2. Open **Windows Terminal (Admin)** and run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`.
3. Check **Settings** > **Windows Update** > **Update history** — if Hello broke the same day as an update, that update is suspect. You can uninstall recent quality updates from **Update history** > **Uninstall updates** as a test.
4. For driver-level blue screens involving biometric devices, our [driver troubleshooting guide](/articles/driver-power-state-failure-windows-11-fix/) covers the deeper driver diagnostics.

### Fix 8: Reset the biometric database manually (advanced)

When re-enrollment fails because the database itself is corrupt, clear it at the file level.

1. Stop the **Windows Biometric Service** in `services.msc`.
2. Navigate to `C:\Windows\System32\WinBioDatabase\` and rename or move the `.DAT` files there (don't delete them outright until you've confirmed the fix).
3. Restart the **Windows Biometric Service** — Windows creates a fresh, empty database.
4. Re-enroll your biometrics from scratch in **Settings** > **Accounts** > **Sign-in options**. If this still fails, the sensor hardware itself may have failed — contact manufacturer support, especially if under warranty.

## Closing

Windows Hello failures are rarely hardware death — they're usually a driver replaced by an update, a corrupted enrollment, a missing PIN, or a disabled service. Work the chain in order: physical checks, PIN, re-enrollment, driver reinstall, service check, BIOS toggle. One of those resolves the overwhelming majority of cases without spending anything. And keep perspective: biometrics are a convenience, and your PIN always works underneath. For the deeper driver-level investigation when Device Manager shows the biometric device misbehaving, our [companion fix guide](/articles/how-to-fix-windows-hello-not-working-in-windows-11-24h2/) walks the driver angle step by step.
