---
title: "Windows Hello Not Working on Your HP Laptop? How to Fix It"
slug: how-to-fix-windows-hello-not-working-on-hp-laptop
date: 2026-09-01
categories: ["windows-errors"]
tags: ["windows hello", "hp laptop", "biometrics"]
description: "Windows Hello face or fingerprint sign-in broken on your HP laptop? These HP-specific fixes get biometric sign-in working again."
thumbnail: "/images/thumbs/how-to-fix-windows-hello-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why does Windows Hello say my camera isn't compatible?"
    a: "Usually the IR camera driver is missing or generic. Windows Hello face sign-in needs an infrared camera with a proper driver — HP's driver from their support site includes the IR components. Also check the BIOS: some HP models let you disable the IR camera there."
  - q: "Can I use Windows Hello without a Microsoft account?"
    a: "Facial recognition and fingerprint sign-in work with local accounts too. But the PIN — which Hello requires as a fallback — and some features like Hello for Business need a Microsoft account or domain setup. For a personal HP laptop, a local account plus PIN plus fingerprint works fine."
  - q: "Is it safe to clear the TPM?"
    a: "Generally yes, but with one caution: if BitLocker encrypts your drive, have the recovery key handy before clearing, because the TPM change can trigger BitLocker recovery on next boot. Your Hello enrollments will need to be redone afterward, which is the point."
  - q: "My fingerprint worked yesterday and stopped today — what happened?"
    a: "The most common overnight cause is a Windows update replacing the biometric driver, or fast startup resuming the sensor in a bad state. Reinstalling the driver from HP's site and disabling fast startup (Fixes 2 and 6) resolve the large majority of sudden failures."
---

You lift the lid expecting the camera to recognize you, and instead Windows Hello just... doesn't. Maybe it says the camera couldn't be found, or the fingerprint reader vanished from settings. On HP laptops this is usually a driver or HP software issue, not broken hardware.

HP's fingerprint readers and IR cameras depend on specific drivers plus HP's own utilities, which gives failures a few extra places to hide. Our [general Hello repair guide](/articles/best-way-to-fix-windows-hello-not-working/) covers all PCs; the steps below are tuned for HP. Start at Fix 1.

## Why this happens

- The biometric driver (Synaptics, ELAN, or Goodix fingerprint; Intel/Realtek camera) being outdated or corrupted.

- Windows Hello's biometric database corrupting after a Windows update.

- HP Client Security or HP Wolf Security interfering with the biometric pipeline.

- The IR camera being disabled in BIOS or by a privacy shutter / kill switch.

- Fast startup leaving the biometric device in a bad state across reboots.

- A Windows update breaking the handshake between Hello and the sensor driver.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Check for a physical privacy shutter or kill switch

Many HP laptops have a camera shutter slider or a keyboard kill switch. If it's closed, no software fix will help — check the hardware first.

1. Look for a small slider over the webcam and slide it open.

2. Check for a camera kill-switch key (often **Fn** + a function key with a camera icon).

3. Open the **Camera** app from the Start menu to confirm video works at all.

4. If the Camera app works but Hello doesn't, continue — the sensor is fine and it's a software problem.

### Fix 2: Reinstall the biometric drivers

Corrupted fingerprint or IR camera drivers are the top software cause. A clean reinstall fixes most Hello failures on HP machines.

1. Open **Device Manager** and expand **Biometric devices** (and **Cameras** for face sign-in).

2. Right-click the fingerprint sensor or IR camera and choose **Uninstall device**, ticking **Attempt to remove the driver**.

3. Restart the laptop so Windows reinstalls a base driver.

4. Then install the latest driver from [HP's support site](https://support.hp.com/us-en) for your exact model — HP's versions include the Hello integration pieces generic drivers lack.

### Fix 3: Reset Windows Hello's biometric data

Hello stores your face/fingerprint templates in a protected database. When that database corrupts, Hello fails even with perfect drivers.

1. Go to **Settings > Accounts > Sign-in options**.

2. Under **Facial recognition** or **Fingerprint recognition**, click **Remove** for each enrolled method.

3. Restart the laptop.

4. Return to **Sign-in options** and set up your face or fingerprint fresh. Test sign-in immediately.

### Fix 4: Clear the TPM

Windows Hello keys live in the Trusted Platform Module. A confused TPM breaks Hello in ways that look like sensor failures.

1. Back up BitLocker recovery keys first if you use BitLocker — clearing the TPM can trigger recovery.

2. Open **Windows Security > Device security > Security processor details > Security processor troubleshooting**.

3. Click **Clear TPM** and restart when prompted.

4. Re-enroll your Hello biometrics afterward in **Settings > Accounts > Sign-in options**.

### Fix 5: Update HP Client Security and BIOS

HP's security software and BIOS both participate in biometric authentication. Old versions break Hello after Windows updates.

1. Open **HP Support Assistant** and install all recommended updates.

2. Check your model's page on [HP's support site](https://support.hp.com/us-en) for a newer **BIOS** — biometric fixes appear in BIOS changelogs regularly.

3. Apply the BIOS update on AC power without interruption.

4. Re-test Hello after the update completes.

### Fix 6: Disable fast startup

Fast startup can leave the biometric sensor in a half-initialized state. A true cold boot often brings it back.

1. Open **Control Panel > Power Options > Choose what the power buttons do**.

2. Click **Change settings that are currently unavailable**.

3. Untick **Turn on fast startup** and save.

4. Shut down completely, wait 10 seconds, and power on — then test Hello.

### Fix 7: Check the biometric service

Windows Biometric Service must be running for any of this to work. HP utilities sometimes disable it.

1. Press **Win + R**, type `services.msc`, and press **Enter**.

2. Find **Windows Biometric Service**.

3. Set **Startup type** to **Automatic** and click **Start** if it's stopped.

4. Restart and test Hello. If the service won't stay running, run `sfc /scannow` from an admin Terminal — system file damage can break it.

### Fix 8: Enable biometrics in the BIOS

Many HP laptops have BIOS-level toggles for the fingerprint reader and camera. If a BIOS update or reset disabled them, Windows can't see the hardware no matter what drivers you install.

1. Restart and press **F10** to enter the HP BIOS setup.

2. Go to **Advanced > Built-in Device Options** (exact naming varies by model).

3. Ensure the **fingerprint reader** and **camera** are enabled — not hidden or disabled.

4. Press **F10** to save and exit.

5. Back in Windows, check **Device Manager** for the devices reappearing, then re-enroll in **Settings > Accounts > Sign-in options**.

## Closing

Windows Hello on HP laptops fails for boring reasons far more often than broken sensors: a privacy shutter, a corrupted driver, or a stale biometric database. Check the hardware shutter first (it's embarrassing how often that's it), then reinstall HP's drivers and re-enroll. Once it's working, keep HP Support Assistant updating in the background — HP ships Hello compatibility fixes through it regularly, and staying current prevents the next Windows update from breaking things again. If Hello works but is slow or fussy, re-enroll in the lighting you actually use — face recognition trained in a dark room struggles in daylight and vice versa. For the general, non-HP-specific side of Hello repair, our [main Windows Hello guide](/articles/best-way-to-fix-windows-hello-not-working/) covers the PIN and TPM layers in more depth. Dell owners hitting the same wall can use our [Dell-specific Windows Hello guide](/articles/how-to-fix-windows-hello-not-working-on-dell-laptop/) — same biometric pipeline, Dell's own driver and BIOS quirks.
