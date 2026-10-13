---
title: "Windows Hello Not Working? A Step-by-Step Fix Guide"
slug: how-to-fix-windows-hello-not-working-step-by-step
date: 2026-09-12
categories: ["windows-errors"]
tags: ["windows hello", "biometrics", "sign-in"]
description: "Windows Hello face, fingerprint, or PIN broken? Follow this step-by-step guide to diagnose and repair Hello on any Windows 11 laptop."
thumbnail: "/images/thumbs/how-to-fix-windows-hello-not-working-step-by-step.webp"
faqs:
  - q: "Why does Windows Hello say 'something went wrong' with no details?"
    a: "That generic message usually means the PIN infrastructure or TPM state broke underneath the biometrics. Work the PIN fixes (Fixes 4-5) first — face and fingerprint depend on the PIN, so a broken PIN produces vague errors for everything above it."
  - q: "Do I need a Microsoft account for Windows Hello?"
    a: "No. Fingerprint, face, and PIN all work with local accounts. A Microsoft account adds conveniences like syncing some settings, but Hello itself is fully functional offline with a local account."
  - q: "Why did my fingerprint stop working after a Windows update?"
    a: "Updates frequently replace the biometric driver with a generic version that lacks the vendor's Hello integration. Reinstalling the driver from your laptop maker's support site (Fix 2) restores it — this is the single most common post-update Hello failure."
  - q: "Is Windows Hello actually secure?"
    a: "Yes — it's more secure than passwords. Biometric data never leaves your device; it's stored in the TPM-backed secure store and used to unlock a cryptographic key. Even Microsoft never receives your fingerprint or face data."
---

Windows Hello is wonderful until it isn't: the camera doesn't recognize you, the fingerprint reader vanished, or the PIN option throws an error. Rather than random fixes, this guide works like a technician would — checking each layer of the Hello stack in order until the broken one is found.

Hello depends on a chain: sensor hardware, drivers, the biometric service, the TPM, and your enrolled data. Any link can break. For HP-specific issues see our [HP Hello guide](/articles/how-to-fix-windows-hello-not-working-on-hp-laptop/); below is the universal step-by-step for any laptop. Start at Fix 1. Each step ends with a quick test, so you'll know immediately when you've found the broken layer — there's no need to complete the whole chain once Hello works.

## Why this happens

- Biometric drivers corrupted or replaced by a Windows update.

- Enrolled face/fingerprint data corrupted in Hello's secure database.

- The TPM holding Hello's keys being in a confused state.

- Windows Biometric Service disabled or crashing.

- Camera privacy shutters, kill switches, or BIOS-disabled sensors.

- PIN infrastructure broken, which also breaks face/fingerprint (they depend on the PIN).

- A pending Windows update holding biometric components in a half-updated state, where the sensor driver and the Hello service disagree with each other.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Check the hardware basics

Two minutes of physical checks eliminate the embarrassing causes before you touch software.

1. Slide open any **camera privacy shutter** and check for a **camera kill-switch** key.

2. Open the **Camera** app — if video works, the sensor is fine.

3. For fingerprint: check **Device Manager > Biometric devices** for the sensor's presence.

4. Check the BIOS for disabled cameras or biometric devices and re-enable them.

### Fix 2: Reinstall biometric and camera drivers

Driver corruption is the top software cause. Clean-reinstall the drivers Hello depends on.

1. In **Device Manager**, expand **Biometric devices** and **Cameras**.

2. Uninstall the fingerprint sensor and IR camera, ticking **Attempt to remove the driver**.

3. Restart — Windows installs base drivers.

4. Then install the latest drivers from your laptop maker's support site (HP users: [HP support](https://support.hp.com/us-en); Lenovo: [Lenovo support](https://support.lenovo.com/us/en/)).

### Fix 3: Remove and re-enroll your biometrics

Corrupted enrollment data fails even with perfect drivers. Wiping and re-enrolling is quick.

1. Go to **Settings > Accounts > Sign-in options**.

2. Under **Facial recognition** and **Fingerprint recognition**, click **Remove** on each.

3. Restart the laptop.

4. Re-enroll in good lighting (face) with clean, dry fingers (fingerprint), then test sign-in immediately.

### Fix 4: Fix the PIN first

Face and fingerprint both depend on the Windows Hello PIN infrastructure. A broken PIN breaks everything above it.

1. In **Settings > Accounts > Sign-in options**, under **PIN**, click **Remove**, then **Add** to create a fresh PIN.

2. If PIN setup errors with **0x80090016**, the NGC folder is corrupted — see Fix 5.

3. Test PIN sign-in before re-enrolling biometrics.

4. Only move on once the PIN works reliably.

### Fix 5: Reset the NGC folder (PIN error 0x80090016)

This specific error means the PIN credential store is corrupted. Deleting it forces Windows to rebuild it cleanly.

1. Open **File Explorer** and navigate to `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc`.

2. Take ownership if prompted (you'll need admin rights), then delete the folder's contents.

3. Restart the laptop.

4. Go to **Settings > Accounts > Sign-in options > PIN > Add** and create a new PIN. Microsoft documents Hello recovery on [their Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 6: Clear the TPM

Hello's encryption keys live in the TPM. When the TPM state corrupts, Hello fails cryptically.

1. Save BitLocker recovery keys first if BitLocker is on.

2. Open **Windows Security > Device security > Security processor details > Security processor troubleshooting**.

3. Click **Clear TPM** and restart when prompted.

4. Re-create your PIN and re-enroll biometrics afterward.

### Fix 7: Verify the biometric service and system files

The last layer: the Windows Biometric Service itself and the system files around it.

1. Press **Win + R**, type `services.msc`, find **Windows Biometric Service** — set to **Automatic** and start it.

2. In an admin Terminal, run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth`.

3. Restart and re-enroll.

4. If it still fails on all accounts, test in a new user profile to rule out profile corruption.

### Fix 8: Check the biometrics Group Policy and registry

On Pro editions — and on any machine touched by a 'privacy' script — the policy that allows biometrics can be disabled. Everything else can be perfect and Hello still won't work until this is re-enabled.

1. Press **Win + R**, type `gpedit.msc`, and press **Enter** (Pro/Enterprise).

2. Go to **Computer Configuration > Administrative Templates > Windows Components > Biometrics**.

3. Set **Allow the use of biometrics** to **Enabled**.

4. Also enable **Allow users to log on using biometrics** and **Allow domain users to log on using biometrics**.

5. On Home edition, open an admin Terminal and run: `reg add "HKLM\SOFTWARE\Policies\Microsoft\Biometrics" /v Enabled /t REG_DWORD /d 1 /f`.

6. Restart and re-enroll your biometrics.

## Closing

Windows Hello troubleshooting is really just walking the chain: hardware, drivers, enrollment data, PIN, TPM, service. Fix them in that order and you'll find the broken link instead of guessing — and in practice, it's the drivers or the enrollment data about eighty percent of the time. Once Hello works again, resist the urge to 'optimize' biometric drivers with third-party updaters; the manufacturer's versions are the ones tested against Hello, and that's what keeps it working through the next update. On work or school laptops, also check with your IT admin — organizations can disable biometrics by policy, and no local fix overrides that. For the PIN side specifically, our [PIN troubleshooting guide](/articles/best-way-to-fix-pin-not-working-on-windows-11/) goes deeper on the errors that cascade upward into face and fingerprint failures. Work through any new symptoms the same way: hardware, drivers, enrollment data, PIN, TPM, service. The chain rarely changes, so this diagnostic order stays useful long after today's problem is fixed — it's genuinely reusable troubleshooting skill.
