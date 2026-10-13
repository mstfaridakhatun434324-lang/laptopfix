---
title: "How to Disable Driver Signature Enforcement (Safely)"
slug: how-to-disable-driver-signature-enforcement
date: 2026-09-24
categories: ["windows-errors"]
tags: ["driver signature enforcement", "unsigned driver", "test mode", "driver install", "windows 11"]
description: "Need to install an unsigned driver? Learn the safe ways to disable driver signature enforcement — temporary, test mode, and when not to."
thumbnail: "/images/thumbs/how-to-disable-driver-signature-enforcement.webp"
faqs:
  - q: "What is driver signature enforcement?"
    a: "It's a Windows security feature requiring all kernel-mode drivers to carry a valid digital signature from Microsoft or a trusted publisher. It blocks malware from installing malicious drivers. Disabling it removes that protection, so it should only be done temporarily to install a trusted unsigned driver."
  - q: "Is it safe to disable driver signature enforcement?"
    a: "Temporarily, for installing a specific trusted driver — reasonably. Permanently — no. Unsigned drivers bypass a key malware defense, and some malware specifically instructs victims to disable enforcement. Re-enable it immediately after installing what you need."
  - q: "What's the difference between disabling enforcement and Test Mode?"
    a: "Disabling via startup settings lasts one boot — enforcement returns on the next restart. Test Mode (bcdedit /set testsigning on) persists across reboots and shows a watermark, meant for developers testing drivers. Use the temporary method unless you're actively developing a driver."
  - q: "Can I sign the driver myself instead?"
    a: "For personal use, you can self-sign a driver and add your certificate to the machine's Trusted Publishers store — this keeps enforcement on while allowing your driver. It's more work but far safer than disabling enforcement system-wide."
---

Driver Signature Enforcement is the bouncer at Windows' kernel door: no valid signature, no entry. Most of the time that's exactly what you want. But occasionally you need to install a legitimate unsigned driver — an old device with no signed driver, a developer's test build, or specialized hardware — and Windows refuses.

There are three ways to get past it, ranging from safest to riskiest. Use the lightest one that works, and always re-enable enforcement afterward.

## Why this happens

- **Old hardware with no signed driver.** Manufacturers abandon products without ever signing newer drivers.
- **Developer or custom drivers.** Test builds and hobbyist drivers aren't submitted for signing.
- **Modified drivers.** Tweaked drivers (e.g., modded GPU drivers) invalidate their signatures.
- **Corporate or specialized hardware.** Niche devices ship unsigned drivers with manual install instructions.
- **Corrupted driver signature catalog.** Rarely, a damaged signature store rejects valid drivers.
- **Secure Boot interactions.** Some unsigned drivers also conflict with Secure Boot policies.

## How to fix it

Work through these in order — start with Fix 1 and stop when the driver installs.

### Fix 1: Disable enforcement for one boot (safest method)

This is the method to use in almost every case.

1. Hold **Shift** while clicking **Restart** (from the Start menu power button).
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press **7** (or **F7**) for **Disable driver signature enforcement**.
4. Windows boots with enforcement off — install your unsigned driver now.
5. Restart normally afterward; enforcement is automatically back on. The driver you installed stays installed.

### Fix 2: Enable Test Mode for driver development

For developers who need persistence across reboots.

1. Open **Terminal (Admin)**.
2. Run `bcdedit /set testsigning on`.
3. Restart — you'll see a **Test Mode** watermark on the desktop.
4. Install and test your unsigned driver across as many reboots as needed.
5. When done, run `bcdedit /set testsigning off` in **Terminal (Admin)** and restart to leave Test Mode.

### Fix 3: Disable integrity checks (advanced, not recommended)

A deeper override for stubborn cases.

1. Open **Terminal (Admin)**.
2. Run `bcdedit /set nointegritychecks on`.
3. Restart and install the driver.
4. Re-enable afterward with `bcdedit /set nointegritychecks off` and restart.
5. Warning: this disables more protection than Fix 1 or 2 — use it only if the temporary method fails, and revert immediately. For the Windows 11 24H2-specific procedure, see [disabling driver signature enforcement in Windows 11 24H2](/articles/how-to-disable-driver-signature-enforcement-in-windows-11-24h2/).

### Fix 4: Self-sign the driver (safest permanent solution)

Keep enforcement on while allowing your specific driver.

1. Use the Windows SDK's `makecert` or PowerShell's `New-SelfSignedCertificate` to create a code-signing certificate.
2. Sign the driver package with `signtool sign` using your certificate.
3. Install your certificate into the **Trusted Publishers** (and **Trusted Root**) certificate store on the machine via `certmgr.msc`.
4. Install the driver normally — enforcement stays on and your signed driver is accepted.
5. This is the correct approach for IT admins deploying custom drivers to multiple machines.

### Fix 5: Check for a signed alternative first

Often the unsigned driver isn't actually necessary.

1. Check the hardware manufacturer's website for a newer signed driver — many "unsigned" problems are just outdated downloads.
2. Let Windows Update try: **Device Manager > Update driver > Search automatically**.
3. Check the Microsoft Update Catalog for signed driver packages for your exact hardware ID.
4. For GPUs, [NVIDIA](https://www.nvidia.com/Download/index.aspx) and [AMD](https://www.amd.com/en/support/download/drivers.html) always ship signed drivers — you should never need to disable enforcement for them.
5. Only proceed with unsigned installation when no signed option exists.

### Fix 6: Verify the unsigned driver's trustworthiness

Don't disable security for malware.

1. Download the driver only from the hardware manufacturer's official site or a source you personally trust.
2. Scan the files with Windows Defender before installing.
3. Check community reputation — forums and Reddit threads about that specific driver.
4. Be extremely suspicious of any "driver" that arrives via email, pop-up ads, or "driver updater" tools — those are malware vectors.
5. If anything feels off, don't install it. No device is worth a kernel-level compromise. (Driver verification tools like Driver Verifier serve a different purpose — catching buggy signed drivers, covered in our [Driver Verifier violation guide](/articles/fix-driver-verifier-detected-violation-after-windows-11-update/) — but the trust principle is the same: know what you're loading into the kernel.)

### Fix 7: Re-enable everything and verify

Close the security hole you opened.

1. After installation, restart normally (Fix 1) or run the revert commands (Fixes 2–3).
2. Confirm enforcement is back: run `bcdedit` in **Terminal (Admin)** and check that `testsigning` and `nointegritychecks` are off/absent.
3. Verify the device works in **Device Manager** with no warning icons.
4. If Windows flags the driver on subsequent boots, you may need Test Mode permanently — reconsider whether the device is worth it.
5. Microsoft's [driver signing documentation](https://support.microsoft.com/en-us/windows) explains the policy in depth.

### Fix 8: Re-verify after every major Windows update

Feature updates can silently undo your unsigned-driver setup.

1. After any Windows feature update, check **Device Manager** for warning icons on the device using the unsigned driver.
2. Feature updates often re-enable enforcement flags and can replace your driver with an older signed version — or break the unsigned one.
3. If the device stops working post-update, repeat Fix 1 (temporary disable) and reinstall the unsigned driver.
4. If you used Test Mode, confirm it's still on with `bcdedit` in **Terminal (Admin)** — updates sometimes reset it.
5. Consider this maintenance cost when deciding whether to keep the unsigned device long-term; hardware with proper signed drivers never needs this attention.

## Closing

Disabling Driver Signature Enforcement is a legitimate tool, not a hack — Microsoft built the temporary-disable path for exactly this situation. Use Fix 1, install your trusted driver, reboot, and you're protected again. What you should never do is leave enforcement off "because it's easier" — that bouncer is stopping real malware, and the inconvenience of one extra reboot is nothing compared to a kernel-level infection. Keep a note of which method you used and why; six months from now, you won't remember, and the next driver update will thank you for the documentation.
