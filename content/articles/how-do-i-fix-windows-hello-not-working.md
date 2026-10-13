---
title: "How Do I Fix Windows Hello Not Working on My Laptop?"
slug: how-do-i-fix-windows-hello-not-working
date: 2026-09-18
categories: ["windows-errors"]
tags: ["windows hello fix", "fingerprint not working", "face sign-in", "pin reset", "biometric driver"]
description: "Windows Hello not working on your laptop? Follow this direct fix sequence — driver refresh, PIN reset, biometric rebuild — to restore sign-in."
thumbnail: "/images/thumbs/how-do-i-fix-windows-hello-not-working.webp"
faqs:
  - q: "How do I fix Windows Hello quickly?"
    a: "The two fastest fixes: refresh the biometric driver in Device Manager (uninstall the sensor, restart, let Windows reinstall), and remove then re-add your PIN in Settings, Accounts, Sign-in options. One of those resolves most Hello failures because the causes are almost always driver or credential related."
  - q: "Why is Windows Hello unavailable after a Windows update?"
    a: "Updates replace manufacturer biometric drivers with generic ones that may not support your sensor, or they corrupt the PIN credential store during migration. Roll back the biometric driver to the manufacturer's version, or remove and re-add your PIN — both directly undo the common update damage."
  - q: "Do I need my password to fix Windows Hello?"
    a: "Yes — keep your Microsoft account password handy. Removing the PIN requires password confirmation, and re-enrolling biometrics requires signing in. If you've forgotten it, reset it at account.microsoft.com before starting, or you'll get stuck halfway through the repair."
  - q: "What if my fingerprint sensor is missing from Device Manager?"
    a: "First check for a physical privacy shutter or a BIOS toggle disabling the sensor — both are common gotchas. If it is genuinely absent with no unknown devices, try the manufacturer's hardware diagnostics. A sensor that no scan can see is likely a hardware failure needing service."
---

Your fingerprint reader was working yesterday and today Windows Hello acts like the hardware doesn't exist. Or face recognition fails every attempt. Or the sign-in options page shows "Windows Hello isn't available." Before you assume the sensor died, know this: the overwhelming majority of Hello failures are software — a driver Windows Update replaced, a PIN credential that corrupted, a biometric database that needs rebuilding. This is the direct fix sequence, shortest path first.

For the full technical background, see our [Windows Hello troubleshooting guide](/articles/troubleshoot-windows-hello-not-working/) — this article is the action-focused version.

## Why this happens

- **Windows Update replaced the biometric driver.** The most common cause — a generic driver that doesn't support your sensor.
- **Corrupted PIN credential.** Hello's anchor credential breaks, taking all Hello methods down with it.
- **Damaged biometric database.** Stored fingerprint/face templates become unreadable.
- **Biometric services stopped.** Required services disabled by updates or "tuning" tools.
- **Privacy settings blocking the sensor.** Camera access off (face) or device toggles off (fingerprint).
- **TPM problems.** Hello keys live in the TPM; TPM errors break the chain.
- **Dead sensor hardware.** Least common — verify everything else first.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Refresh the biometric driver

Two minutes, highest success rate.

1. **Device Manager** → **Biometric devices** (or **Cameras** for IR) → right-click sensor → **Uninstall device** (check "delete driver").
2. Restart — Windows reinstalls a driver automatically.
3. Test Hello. If it works, you're done.
4. If not, download the sensor driver from your laptop maker's support page and install it manually.
5. If Windows Update keeps breaking it, pause driver updates until the maker ships a compatible build.

The general driver-update method is detailed in [how to update drivers on a Windows 11 laptop](/articles/how-to-update-drivers-on-windows-11-laptop/).

### Fix 2: Remove and re-add your PIN

Rebuild Hello's credential anchor.

1. Have your **Microsoft account password** ready — you'll need it.
2. **Settings > Accounts > Sign-in options** → **PIN (Windows Hello)** → **Remove** (confirm with password).
3. Restart the laptop fully.
4. Return and click **Add** under PIN — create a fresh one.
5. Re-enroll fingerprint/face under their sections. Test each method.

The 24H2-specific walkthrough: [how to fix Windows Hello not working in Windows 11 24H2](/articles/how-to-fix-windows-hello-not-working-in-windows-11-24h2/).

### Fix 3: Rebuild the biometric database

When the stored templates are the problem.

1. `services.msc` → stop **Windows Biometric Service**.
2. Go to `C:\Windows\System32\WinBioDatabase` — rename the `.DAT` files (keep a backup copy elsewhere).
3. Restart the **Windows Biometric Service**.
4. Re-enroll fingerprint/face in **Sign-in options**.
5. Delete the backup DATs after a week of stable use.

### Fix 4: Check the physical and BIOS gotchas

The embarrassing causes — check before deeper surgery.

1. Look for a **physical camera privacy shutter** — if it's closed, face recognition can't work. (This fixes more "dead" Hello cameras than any driver.)
2. Check for a fingerprint-sensor toggle in your manufacturer's utility app.
3. Enter BIOS/UEFI and verify the biometric device / TPM isn't disabled.
4. Clean the fingerprint sensor surface — skin oils degrade reads gradually, then suddenly.
5. Improve lighting for face enrollment — IR works in the dark, but enrollment needs a clear initial capture.
6. For face recognition specifically, verify the **IR camera** has its own working driver in Device Manager > Cameras — it's separate from the regular webcam driver, and Windows Update sometimes breaks one while leaving the other fine. Reinstall the manufacturer's camera driver package if the IR entry shows a warning.

### Fix 5: Verify services and account state

The supporting infrastructure.

1. `services.msc`: **Windows Biometric Service** and **Credential Manager** → Running, Automatic.
2. **Settings > Privacy & security > Camera** → camera access on (for face).
3. **Settings > Accounts** → confirm you're signed in with your Microsoft account; sign out/in if Hello shows account errors.
4. Disconnect VPN temporarily — region/account mismatches can block Hello provisioning.
5. Ensure **Password** sign-in is enabled as a fallback so you're never locked out mid-repair.
6. When re-enrolling a fingerprint, register the same finger twice at slightly different angles if the option allows — it dramatically improves recognition reliability, especially for fingers with worn prints from manual work.

### Fix 6: Repair system files

For framework-level corruption.

1. **Terminal (Admin)**: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, restart.
2. Re-run Fix 3 (database rebuild) after repairs.
3. Install pending Windows updates — Hello fixes ship in cumulative updates; check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if you're stuck on an old build.
4. In-place upgrade from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) (keep files and apps) for deep corruption.
5. Re-enroll biometrics only after the repair verifies clean, and test each Hello method (face, fingerprint, PIN) separately so you know exactly which ones recovered.

### Fix 7: Confirm hardware failure (or work around it)

The final verdict.

1. If the sensor is absent from Device Manager entirely and diagnostics can't see it, it's likely hardware.
2. Run manufacturer diagnostics and save the result codes.
3. In-warranty → manufacturer repair; bring your troubleshooting notes.
4. Out-of-warranty → a USB Windows Hello fingerprint reader costs little and works fine.
5. Keep using PIN + password meanwhile — Hello is convenience, not a requirement.

## Closing

"How do I fix Windows Hello" has a short answer: refresh the driver, reset the PIN, rebuild the biometric database — in that order, checking the privacy shutter before you touch anything. That's the whole repair for the vast majority of cases, and it works because it follows the actual dependency chain: the driver lets Windows see the sensor, the PIN rebuilds the credential anchor, and the database rebuild gives Hello fresh templates to match against. The sensor is probably fine; Windows just forgot how to talk to it, or forgot the credentials that prove it's you. Remind it, in the right order, and the laptop recognizes you again by tonight.
