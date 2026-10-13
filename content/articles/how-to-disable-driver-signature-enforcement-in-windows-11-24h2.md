---
title: "How to Disable Driver Signature Enforcement in Windows 11 24H2"
slug: how-to-disable-driver-signature-enforcement-in-windows-11-24h2
date: 2026-09-18
categories: ["windows-errors"]
tags: ["driver signature enforcement", "windows 11 24h2", "unsigned drivers", "advanced startup"]
description: "Disable driver signature enforcement in Windows 11 24H2 safely — temporary method, Test Mode, and when you actually need it."
thumbnail: "/images/thumbs/how-to-disable-driver-signature-enforcement-in-windows-11-24h2.webp"
faqs:
  - q: "What is driver signature enforcement?"
    a: "It's a Windows security feature that blocks installation of drivers not digitally signed by Microsoft or a trusted publisher. It protects against malicious kernel drivers. Disabling it lets unsigned drivers load — useful for old hardware or development, but it removes a real layer of protection."
  - q: "Is it safe to disable driver signature enforcement?"
    a: "Temporarily, for a specific trusted driver, the risk is manageable — that's what the one-boot disable method is for. Leaving it permanently off (Test Mode) exposes the kernel to any unsigned driver, including malicious ones. Use the temporary method unless you have a specific ongoing need."
  - q: "Does this work on Windows 11 24H2 with Secure Boot on?"
    a: "The temporary Startup Settings method works regardless. But permanent Test Mode (bcdedit /set testsigning on) requires Secure Boot to be OFF in the BIOS — 24H2 enforces this strictly. If the bcdedit command fails, Secure Boot is the reason."
  - q: "Will disabling it fix my driver error?"
    a: "Only if the error is specifically about an unsigned driver being blocked (error 52 in Device Manager: 'Windows cannot verify the digital signature'). It won't fix buggy signed drivers, blue screens from driver bugs, or hardware problems — those need actual driver fixes."
---
Driver signature enforcement is the bouncer at Windows' kernel door: no valid digital signature, no entry. Most of the time that's exactly what you want — it's a meaningful defense against malicious drivers. But sometimes you have a legitimate reason to get past it: an old printer, scanner, or specialty device whose manufacturer never signed a Windows 11 driver, or you're developing and testing your own driver. On Windows 11 24H2, the methods still work, but Secure Boot and the tightened security posture add wrinkles worth knowing.

This guide covers the two legitimate methods — the temporary one-boot disable (what most people need) and the persistent Test Mode (for ongoing needs) — plus when you shouldn't bother at all.

## Why this happens

- **Old hardware with unsigned drivers.** Manufacturers abandoning devices before signing drivers for modern Windows.
- **Error 52 in Device Manager.** "Windows cannot verify the digital signature for the drivers required for this device" — the specific symptom this fixes.
- **Driver development and testing.** Developers iterating on drivers can't sign every test build.
- **Specialty/industrial hardware.** Niche devices (lab equipment, legacy controllers) with community or vendor drivers that were never submitted for signing.
- **Misunderstood blue screens.** People disable enforcement hoping to fix driver crashes — it doesn't help those, and this guide says so clearly.
- **Secure Boot conflicts.** 24H2 strictly ties Test Mode to Secure Boot state, confusing people whose bcdedit commands fail silently.

## How to fix it

Work through these in order. Method 1 is the right answer for most people — read Method 3 before deciding you need Method 2.

### Fix 1: Check whether you actually need this

Don't disable a security feature for the wrong problem.

1. Open **Device Manager** (`devmgmt.msc`) and find the problematic device. Open **Properties** > **General** tab.
2. If the **Device status** says **"Windows cannot verify the digital signature for the drivers required for this device. (Code 52)"** — yes, you need this guide.
3. If it shows any other error code, or the device works but crashes, signature enforcement isn't your problem. A Code 52 is the specific signature-block symptom; everything else needs a different fix.
4. Also check the manufacturer's site once more for a signed driver — many "unsigned" problems are actually "outdated download page" problems. Our [driver update guidance](/articles/driver-power-state-failure-windows-11-fix/) covers finding proper signed drivers first.

### Fix 2: Temporarily disable via Startup Settings (recommended)

Disables enforcement for one boot only — the safe way.

1. Go to **Settings** > **System** > **Recovery** > **Advanced startup** > **Restart now**.
2. **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. Press **7** (or **F7**) for **Disable driver signature enforcement**.
4. Windows boots with enforcement off for this session only. Install your unsigned driver now via Device Manager (**Update driver** > **Browse my computer**).
5. Next reboot, enforcement is back on automatically. The installed unsigned driver may fail to load on subsequent boots — that's expected; this method is for one-time installations or testing, not permanent use.

### Fix 3: Understand the risks before going permanent

Read this before touching bcdedit.

1. Permanent disable (Test Mode) means **every** unsigned driver can load, every boot, with no warning. Malicious kernel drivers are the most privileged malware possible.
2. Some games with kernel anti-cheat (and some enterprise security tools) refuse to run in Test Mode — you'll trade one problem for another.
3. Windows shows a **"Test Mode" watermark** on the desktop — cosmetic, but a constant reminder of the reduced protection.
4. If your need is one old device, consider instead: running it on an older offline PC, finding a community-signed driver, or replacing the device. Permanent disable is the last resort, not the first.

### Fix 4: Enable Test Mode for persistent needs

If you've read Fix 3 and still need it permanently:

1. First, disable **Secure Boot** in BIOS/UEFI (required — 24H2 blocks Test Mode with Secure Boot on). Find it under the **Security** or **Boot** tab; set to **Disabled**, save, exit.
2. In **Terminal (Admin)**, run: `bcdedit /set testsigning on`.
3. Confirm with `bcdedit` — look for `testsigning Yes` in the Windows Boot Loader section.
4. Reboot. The desktop shows the Test Mode watermark, and unsigned drivers now load every boot.
5. Install your driver. Keep a note of what you did — future-you troubleshooting a strange issue needs to know Test Mode is on.

### Fix 5: Re-enable enforcement when done

Don't leave the door open longer than necessary.

1. In **Terminal (Admin)**, run: `bcdedit /set testsigning off`.
2. Re-enable **Secure Boot** in BIOS/UEFI.
3. Reboot and confirm the watermark is gone and `bcdedit` shows `testsigning No` (or the line absent).
4. If the unsigned driver was the goal and it's now blocked again, you didn't actually need it permanently — revisit Fix 2's temporary method for the occasions you use the device.

### Fix 6: Alternative — self-sign the driver

The proper long-term answer for developers and persistent needs.

1. Create a test certificate: in an elevated **Developer Command Prompt**, `makecert -r -pe -ss PrivateCertStore -n "CN=TestCert" testcert.cer`.
2. Sign the driver with **SignTool**: `signtool sign /s PrivateCertStore /n TestCert /t http://timestamp.digicert.com driver.sys`.
3. Install the certificate to **Trusted Root Certification Authorities** and **Trusted Publishers** on the target machine (`certmgr.msc`).
4. The driver now loads with enforcement ON — no Test Mode needed. This is how driver developers are supposed to test, and Microsoft documents the process on [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 7: Fix the actual underlying driver problem

If you arrived here chasing a blue screen rather than a Code 52:

1. Disabling enforcement doesn't fix buggy drivers — signed or not. Identify the crashing driver from the minidump instead.
2. The [driver IRQL fix guide](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/) and the [Driver Verifier guide](/articles/how-to-fix-driver-verifier-detected-violation-in-windows-11-24h2/) address actual driver bugs.
3. Re-enable enforcement (`bcdedit /set testsigning off`, Secure Boot on) and fix the real problem. Security features disabled for no benefit is the worst of both worlds.

## Closing

Driver signature enforcement in 24H2 is straightforward once you know the two methods and their constraints: Startup Settings for the one-boot disable (works always, reverts automatically), Test Mode via bcdedit for the permanent route (needs Secure Boot off, carries real risk). Most people need the temporary method exactly once — to install one old device's driver — and should never think about it again. If you're here because of a blue screen rather than a Code 52, close this tab and fix the driver; the bouncer wasn't your problem.
