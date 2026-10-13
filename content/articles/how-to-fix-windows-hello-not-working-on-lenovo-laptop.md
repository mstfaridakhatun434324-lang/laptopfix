---
title: "Windows Hello Not Working on Your Lenovo Laptop? Here's How to Fix It"
slug: how-to-fix-windows-hello-not-working-on-lenovo-laptop
date: 2026-09-30
categories: ["windows-errors"]
tags: ["windows hello", "fingerprint", "face recognition", "lenovo", "login"]
description: "Windows Hello fingerprint or face login broken on your Lenovo? These 7 fixes cover drivers, PIN reset, biometrics service, and camera issues."
thumbnail: "/images/thumbs/how-to-fix-windows-hello-not-working-on-lenovo-laptop.webp"
faqs:
  - q: "Why does Windows Hello say 'something went wrong' on Lenovo laptops?"
    a: "This usually means the biometric driver crashed or the PIN credential store is corrupted. Reinstalling the fingerprint driver from Lenovo's site and removing/re-adding your PIN fixes it in most cases. Camera privacy settings blocking the IR camera are the other common cause."
  - q: "Can I use Windows Hello without a PIN?"
    a: "No. Windows Hello requires a PIN as a fallback credential — it's part of the setup by design. If PIN setup fails with an error, fix the PIN first (remove it, restart, re-add it), and fingerprint or face recognition will usually start working again."
  - q: "Why is the fingerprint option missing from sign-in settings?"
    a: "The fingerprint reader driver isn't installed or isn't being detected. Check Device Manager under Biometric devices — if it's missing or has a warning icon, download the fingerprint driver from Lenovo support and reinstall it, then restart."
  - q: "Does a Windows update break Windows Hello on Lenovo?"
    a: "Yes, it's a known pattern: major Windows updates sometimes replace Lenovo's biometric drivers with generic ones that don't work, or corrupt the PIN. Reinstalling Lenovo's drivers and re-adding your PIN resolves it almost every time."
---

Nothing is more annoying than a fingerprint reader that worked yesterday and refuses you today. On Lenovo laptops — ThinkPads, IdeaPads, and Yogas alike — Windows Hello breaks for a handful of predictable reasons: a driver Windows Update replaced, a corrupted PIN, a privacy setting blocking the IR camera, or the biometric service getting stuck. The good news is it's almost never broken hardware.

The fixes below are ordered by how often they work. Most people are back to one-touch login by Fix 3 or 4, so you probably won't need the whole list.

## Why this happens

- **Windows Update replaced your biometric driver.** Lenovo ships custom fingerprint and IR camera drivers; a generic Microsoft driver pushed by Windows Update often breaks Hello silently.
- **The PIN credential store is corrupted.** Hello depends on the PIN as its root credential. If the PIN breaks, fingerprint and face login break with it.
- **Camera privacy settings block the IR camera.** Windows 11's camera privacy toggle can disable the infrared camera that face recognition needs.
- **The Windows Biometric Service is stuck or disabled.** If this service isn't running, Hello options grey out or fail with vague errors.
- **Fast Startup causes driver initialization issues.** On some Lenovo models, Fast Startup leaves the fingerprint reader in a half-awake state after every boot.
- **TPM or Secure Boot state changed.** A BIOS update or reset can clear the TPM, which invalidates stored Hello credentials.

## How to fix it

Work through these in order — start with Fix 1 and stop when Hello works again.

### Fix 1: Remove and re-add your PIN

The PIN is the foundation of Windows Hello. Rebuilding it fixes a huge share of cases.

1. Open **Settings > Accounts > Sign-in options**.
2. Under **PIN (Windows Hello)**, click **Remove** and confirm. You may need your Microsoft account password.
3. Restart the laptop.
4. Go back to **Settings > Accounts > Sign-in options** and click **Set up** under PIN.
5. Create a new PIN, then try adding your fingerprint or face again.

If PIN setup itself fails with an error like 0x8009002d, continue to Fix 4 — that error means the credential store needs a deeper repair. PIN problems often travel with other sign-in weirdness; if you're also getting stuck at startup, see our guide on [fixing a PC that ran into a problem](/articles/how-to-fix-your-pc-ran-into-a-problem-after-windows-11-update/).

### Fix 2: Reinstall the fingerprint and IR camera drivers

This is the fix for "it broke right after an update."

1. Go to [Lenovo Support](https://support.lenovo.com/us/en/) and enter your exact model or serial number.
2. Download the latest **fingerprint reader** driver and, if you use face login, the **camera/IR camera** driver for your Windows version.
3. Open **Device Manager**, expand **Biometric devices**, right-click the fingerprint sensor, and choose **Uninstall device**. Tick **Attempt to remove the driver for this device** if offered.
4. Do the same under **Cameras** or **Imaging devices** for the IR camera if you're fixing face recognition.
5. Install the drivers you downloaded from Lenovo, then restart.

Do not let Windows Update substitute its own drivers here — Lenovo's packages include firmware for the sensor that generic drivers lack. For a broader walkthrough of driver-caused sign-in issues, our [black screen after update fix guide](/articles/how-to-fix-black-screen-after-windows-update-on-lenovo-laptop/) covers similar territory on Lenovo hardware.

### Fix 3: Check camera privacy settings (face login)

Face recognition silently fails when the camera is blocked at the OS level.

1. Open **Settings > Privacy & security > Camera**.
2. Make sure **Camera access** is turned on.
3. Scroll down and confirm **Let desktop apps access your camera** is on if you use face login with third-party software.
4. Also check the physical camera shutter — many ThinkPads have a sliding privacy cover or a **Fn** key camera kill switch. If the shutter is closed, Hello can't see you.
5. Try face setup again in **Settings > Accounts > Sign-in options**.

### Fix 4: Repair the NGC credential folder

Error 0x8009002d or repeated PIN failures mean the credential store is damaged.

1. Open **File Explorer** and navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft`.
2. Right-click the **Ngc** folder and rename it to `Ngc.old` (you'll need administrator permission).
3. Restart the laptop.
4. Go to **Settings > Accounts > Sign-in options** and set up a new PIN from scratch.
5. Re-enroll your fingerprint or face.

Windows rebuilds the credential store cleanly. This is safe — the old folder is just a backup you can delete later.

### Fix 5: Restart the Windows Biometric Service

If Hello options are greyed out, the service behind them may have died.

1. Press **Windows + R**, type `services.msc`, and press Enter.
2. Find **Windows Biometric Service** in the list.
3. Double-click it, set **Startup type** to **Automatic**, and click **Start** if it's stopped.
4. Click **OK** and restart the laptop.
5. If the service stops again on its own, run `sfc /scannow` in an admin Command Prompt — a corrupted system file is likely killing it.

### Fix 6: Turn off Fast Startup

Fast Startup can leave Lenovo's fingerprint reader in a broken state between boots.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do** in the left sidebar.
3. Click **Change settings that are currently unavailable**.
4. Untick **Turn on fast startup (recommended)** and click **Save changes**.
5. Shut down fully (not restart), wait 10 seconds, and power on.

Boots take a few seconds longer, but the fingerprint reader initializes cleanly every time. This is a well-known fix on IdeaPad and Yoga models specifically.

### Fix 7: Reset the TPM and re-enroll

If a BIOS update or settings change cleared the TPM, Hello credentials are invalid.

1. Back up BitLocker recovery keys first if you use BitLocker (**Settings > Privacy & security > Device encryption** or manage-bde).
2. Restart and enter the BIOS (**F2** or **Fn + F2** on most Lenovos at the logo screen).
3. Go to the **Security** tab and find **TPM** / **Security Chip** — choose **Clear TPM** or reset it to defaults.
4. Save and exit, then boot into Windows.
5. Remove and re-add your PIN and biometrics as in Fix 1.

Microsoft documents TPM-related Hello failures on the [Windows support site](https://support.microsoft.com/en-us/windows), which is worth checking if your model has additional firmware steps.

## Closing

Windows Hello on Lenovo laptops is fragile in exactly the ways you'd expect — driver swaps, PIN corruption, and privacy toggles — but each of those has a clean fix, and the list above covers all of them. Work through it once, properly, and you'll have one-touch login back. If nothing here helps, test the fingerprint reader in the BIOS diagnostics (most Lenovos have one under the boot menu) to rule out a dead sensor before assuming the worst.
