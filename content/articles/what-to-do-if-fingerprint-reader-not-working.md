---
title: "Fingerprint Reader Not Working? What to Do Next"
slug: what-to-do-if-fingerprint-reader-not-working
date: 2026-09-12
categories: ["drivers"]
tags: ["fingerprint reader", "windows hello", "biometric not working", "fingerprint sensor"]
description: "Fingerprint login failing on your laptop? Learn what to do when the fingerprint reader stops working, from driver fixes to re-enrolling prints."
thumbnail: "/images/thumbs/what-to-do-if-fingerprint-reader-not-working.webp"
faqs:
  - q: "Why did my fingerprint reader suddenly stop working?"
    a: "The most common sudden cause is a Windows update replacing the biometric driver with an incompatible version, which breaks the secure link between the sensor and Windows Hello. The next most common is corrupted enrolled fingerprint data. Both are software states — the sensor hardware rarely fails — which is why driver reinstalls and re-enrollment fix the large majority of cases."
  - q: "Should I remove my PIN before fixing the fingerprint reader?"
    a: "No — keep your PIN. Windows Hello requires a PIN as the fallback credential, and removing it can lock you out of Hello entirely. The PIN is also how you sign in while the fingerprint reader is broken. Fix the reader with the PIN in place; once fingerprints work again, the PIN simply stays as your backup sign-in method."
  - q: "Why does my fingerprint reader work sometimes but not others?"
    a: "Intermittent recognition is usually the sensor or the finger, not the driver: moisture, lotion, cuts, or a dirty sensor all degrade reads. Clean the sensor with a dry cloth and make sure your finger is clean and dry. If recognition fails consistently regardless of conditions, then suspect the driver or corrupted enrollment data rather than the sensor surface."
  - q: "Do I need to re-enroll fingerprints after reinstalling the driver?"
    a: "Often yes. Fingerprint templates are stored in a secure enclave tied to the driver stack, and a driver reinstall can invalidate them. If Hello reports that the fingerprint data is corrupted or simply never recognizes you after the driver fix, remove the existing fingerprints in Settings and enroll fresh ones — enrollment takes about a minute per finger."
---

Fingerprint sign-in is the kind of feature you stop thinking about until it breaks — then every login becomes a password hunt. When the fingerprint reader stops working, Windows Hello usually says something unhelpful like 'couldn't recognize you' or the fingerprint option vanishes from sign-in settings entirely. The two presentations point at different layers: recognition failures are sensor or enrollment problems, while a missing option is a driver problem.

The fix order follows that split. Clean the sensor and re-enroll first for recognition issues; reinstall the biometric driver first for a missing Hello option. Both paths are short, and the sensor hardware itself is almost never the fault.

## Why this happens

- **Biometric driver replaced or corrupted** by a Windows update.
- **Enrolled fingerprint data corrupted**, so no print ever matches.
- **Dirty or wet sensor surface** degrading every read.
- **Windows Hello fingerprint option disabled** by policy or a failed setup.
- **PIN removed or broken**, which Hello requires as the base credential.
- **Sensor disabled in Device Manager** or the BIOS.
- **Third-party security software** intercepting the biometric pipeline.
- **Failed sensor hardware**, rare and usually after liquid damage.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean the sensor and re-enroll your fingerprints

Start with the physical layer: wipe the sensor with a dry, lint-free cloth, and make sure your finger is clean and dry. Then go to Settings > Accounts > Sign-in options > Fingerprint recognition and remove the existing fingerprints — corrupted templates are a leading cause of total recognition failure. Re-enroll, lifting and placing your finger at slightly different angles so the template captures the full print. Test sign-in immediately. This resolves the 'never recognizes me' cases without touching any driver.

1. Clean the sensor with a dry, lint-free cloth.
2. Remove existing fingerprints in Sign-in options.
3. Re-enroll with varied finger angles and good coverage.
4. Test sign-in right away.

### Fix 2: Confirm your PIN is set up

Windows Hello fingerprint is built on top of the PIN — without a working PIN, the fingerprint option cannot function and may disappear from settings. Go to Settings > Accounts > Sign-in options and verify a PIN is set; if Hello complains about the PIN, remove it and create a fresh one. Never remove the PIN as a 'fix' for fingerprint trouble — it is the fallback that keeps you signed in while you repair the reader. Microsoft's Hello setup guidance is in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open Settings > Accounts > Sign-in options.
2. Verify a PIN is set up and working.
3. Remove and recreate the PIN if Hello reports PIN errors.
4. Keep the PIN as your backup sign-in method.

### Fix 3: Reinstall the biometric driver

If the fingerprint option is missing from sign-in options, or Device Manager shows the biometric device flagged, reinstall the driver. Find the fingerprint sensor under 'Biometric devices' in Device Manager, uninstall it (deleting the driver software), then install the biometric driver from the laptop maker's support page for your exact model and reboot. Maker drivers include the firmware interface Windows Hello needs; generic drivers often expose the sensor without the secure pipeline. The [in-depth fingerprint guide](/articles/how-to-fix-fingerprint-reader-not-working-in-windows-11-24h2/) covers brand-specific driver packages.

1. Uninstall the biometric device in Device Manager, deleting the driver.
2. Install the biometric driver from the laptop maker's support page.
3. Reboot and check Biometric devices for a clean entry.
4. Verify the fingerprint option returns in Sign-in options.

### Fix 4: Check Device Manager and BIOS for a disabled sensor

A sensor that vanished entirely may simply be disabled. In Device Manager, choose View > Show hidden devices and look for a greyed-out biometric device — right-click and enable it. Then reboot into the BIOS and confirm the fingerprint reader is enabled; some BIOS versions expose it under Security. If the sensor is absent from both Device Manager (even hidden) and the BIOS, note that for the hardware check at the end. Lenovo's biometric troubleshooting notes are on [Lenovo support](https://support.lenovo.com/us/en/).

1. Show hidden devices in Device Manager and enable any greyed-out sensor.
2. Enter the BIOS and confirm the fingerprint reader is enabled.
3. Save, boot, and re-check Device Manager.
4. Reinstall the driver if the sensor reappears flagged.

### Fix 5: Remove interfering security software temporarily

Some third-party security suites hook the biometric pipeline and break Hello's secure channel to the sensor. If the reader broke around the time security software updated, temporarily disable its identity-protection or biometric-guard features and retest. If fingerprint sign-in returns, add an exclusion or check the vendor's documentation for Hello compatibility — do not leave the protection off permanently. Windows' built-in protections handle Hello natively, which is why the built-in stack rarely conflicts.

1. Identify recently updated third-party security software.
2. Temporarily disable its biometric/identity protection features.
3. Retest fingerprint sign-in.
4. Configure an exclusion rather than leaving protection off.

### Fix 6: Reset Windows Hello's biometric data store

When re-enrollment fails or Hello insists the data is corrupted, the template store itself may be damaged. Remove all fingerprints and the PIN, then delete the contents of the NGC folder (C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC) after taking ownership — this clears Hello's credential store. Reboot, set up the PIN fresh, then enroll fingerprints. This is the deep reset for Hello; it fixes the cases where surface-level re-enrollment keeps failing. The [Windows 11 fingerprint walkthrough](/articles/how-to-fix-fingerprint-reader-not-working-on-windows-11/) details the NGC reset.

1. Remove all fingerprints and the PIN in Sign-in options.
2. Take ownership of the NGC folder and clear its contents.
3. Reboot and set up a fresh PIN.
4. Enroll fingerprints and test sign-in.

### Fix 7: Test for sensor hardware failure

If the sensor is invisible in the BIOS and Device Manager (hidden devices shown) and a Linux live USB shows no biometric device either, the sensor or its cable has failed. Fingerprint sensors connect via a small ribbon cable that liquid spills love to destroy — check for any history of spills near the palm rest. The sensor is usually part of the palm-rest assembly or a small separate module; replacement means the palm-rest assembly on most models, so get a repair quote before ordering parts.

1. Confirm the sensor is absent in BIOS, Device Manager, and Linux.
2. Consider any liquid-spill history near the palm rest.
3. Inspect the sensor cable if the palm rest is already open.
4. Get a repair quote — sensors are usually palm-rest-assembly parts.

## Closing

Fingerprint reader failures are enrollment and driver problems far more often than sensor problems. The sensor is a simple, robust device; what breaks is the software around it — the corrupted template, the replaced driver, the missing PIN that Hello silently requires. Work the layers in order and the reader comes back quickly: clean and re-enroll for recognition failures, reinstall the maker's biometric driver for a missing Hello option, and reset the NGC store when enrollment itself is corrupted. Keep the PIN set and treat it as the real credential — the fingerprint is a convenience on top of it, and a working PIN means a broken reader is ever only an inconvenience, never a lockout.
