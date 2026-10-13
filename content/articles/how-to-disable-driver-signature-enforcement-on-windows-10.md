---
title: "How to Disable Driver Signature Enforcement on Windows 10"
slug: how-to-disable-driver-signature-enforcement-on-windows-10
date: 2026-09-24
categories: ["windows-errors"]
tags: ["windows 10", "driver signature", "drivers"]
description: "Need to install an unsigned driver on Windows 10? Here are the safe, reversible ways to disable driver signature enforcement — temporarily or longer."
thumbnail: "/images/thumbs/how-to-disable-driver-signature-enforcement-on-windows-10.webp"
faqs:
  - q: "Will disabling driver signature enforcement harm my computer?"
    a: "Temporarily disabling it to install a trusted driver is low-risk — the exposure lasts one boot or until you re-enable it. Leaving it permanently disabled is genuinely risky: it removes a layer that blocks rootkits and malicious drivers. Always re-enable after installing, and never disable it to run software you do not fully trust."
  - q: "Why does the driver stop working after a Windows update?"
    a: "Major Windows updates can invalidate previously installed unsigned drivers or re-tighten enforcement. If your unsigned device breaks after Patch Tuesday or a feature update, repeat Fix 1's one-boot method and reinstall the driver — it usually takes five minutes once you know the drill."
  - q: "What's the difference between test mode and the F7 method?"
    a: "The F7 Startup Settings method disables enforcement for one boot only and leaves no trace — ideal for a single install. Test mode (bcdedit /set testsigning on) persists across reboots until you turn it off, showing a desktop watermark — better for developers who install unsigned builds repeatedly."
  - q: "Can I permanently disable it on Windows 10 Home?"
    a: "Technically yes via the bcdedit methods, but you should not. There is no legitimate ongoing need for most users, and the security cost is real. Every scenario in this guide — old hardware, development, vendor drivers — is served by the temporary methods. Permanent disabling is for specialized lab machines, not daily drivers."
---

Driver signature enforcement is the Windows 10 feature that refuses to load drivers without a valid Microsoft signature. It exists for good reason — it blocks a huge class of rootkits and unstable drivers — but it also blocks legitimate unsigned drivers: old hardware whose vendor never signed a Windows 10 driver, development drivers you built yourself, and some niche equipment drivers.

Disabling it is not a single toggle; Windows 10 offers several methods with different durations and risk levels. This guide covers them from the safest (one boot only) to the most persistent, with honest notes on when each is appropriate. A word of caution first: only disable enforcement to install drivers you trust from sources you trust.

## Why this happens

- **You have hardware with no signed driver:** perfectly good older printers, scanners, lab equipment, and industrial hardware whose vendors stopped updating drivers before signing became mandatory.
- **You are developing or testing a driver:** driver developers need to load unsigned test builds constantly — enforcement would make development impossible.
- **A vendor's installer ships an unsigned driver:** some smaller hardware vendors never completed Microsoft's signing process but ship working drivers.
- **Windows blocks the install outright:** the symptom is usually Windows cannot verify the digital signature (error 52 in Device Manager) or the installer failing with a signature error.
- **You need it temporarily, not permanently:** most people need enforcement off for exactly one install — and Windows has a method designed for precisely that.
- **Understanding the risk matters:** with enforcement off, Windows will load any driver, including malicious ones. The temporary methods limit your exposure window; the permanent ones do not.

## How to fix it

Work through these in order, from the quickest checks to the deeper repairs. Most people are back up and running by Fix 4 or 5.

### Fix 1: Use the Startup Settings method (one boot only)

The safest method: enforcement is disabled for a single boot, then automatically re-enables. Perfect for installing one unsigned driver.

1. Open **Settings > Update & Security > Recovery**. Under **Advanced startup**, click **Restart now**.
2. When the blue menu appears, choose **Troubleshoot > Advanced options > Startup Settings**, then click **Restart**.
3. After the restart, press **7** (or **F7**) for **Disable driver signature enforcement**.
4. Windows boots with enforcement off. Install your unsigned driver now — Device Manager will accept it this session.
5. Restart normally afterward: enforcement is automatically back on, while your installed driver keeps working (it was already loaded and registered).

### Fix 2: Disable it from an elevated command (test mode)

For developers and repeat testers: test mode visibly watermarks the desktop and allows unsigned drivers until you turn it off.

1. Right-click **Start** and open **Windows PowerShell (Admin)** or **Command Prompt (Admin)**.
2. Run `bcdedit /set testsigning on` and press Enter — you should see **The operation completed successfully**.
3. Restart. The desktop now shows a **Test Mode** watermark in the corner — that is your reminder that enforcement is off.
4. Install and test your unsigned drivers freely across reboots.
5. When done, run `bcdedit /set testsigning off` from the elevated prompt and restart. The watermark disappears and enforcement returns.
6. Note: some games with anti-cheat refuse to run in test mode — another reason to treat it as temporary.

### Fix 3: Disable integrity checks (advanced, use carefully)

A deeper switch that disables signature verification more thoroughly. Only for cases where test mode is insufficient.

1. Open an elevated Command Prompt.
2. Run `bcdedit /set nointegritychecks on`.
3. Restart and install the driver.
4. Re-enable afterward with `bcdedit /set nointegritychecks off` and restart.
5. Warning: this disables more protections than test mode. Do not browse the web or run untrusted software while it is off, and do not leave it off permanently.
6. If Windows will not boot after this change, use recovery (**Troubleshoot > Advanced options > Command Prompt**) and run the off command from there.

### Fix 4: Install the unsigned driver correctly while enforcement is off

Disabling enforcement is only half the job — the install itself has a right way that avoids future breakage.

1. With enforcement disabled (any method above), open **Device Manager**, right-click the device, and choose **Update driver > Browse my computer for drivers**.
2. Point it at the folder containing the `.inf` file. When Windows warns the driver is unsigned, choose **Install this driver software anyway**.
3. Verify in **Device Manager** that the device shows no yellow warning and reports **This device is working properly**.
4. If the vendor provides an installer `.exe`, run it as administrator during the enforcement-off session instead.
5. After reinstalling, reboot normally (enforcement back on) and confirm the device still works — properly installed unsigned drivers continue loading once registered.

### Fix 5: Handle Secure Boot conflicts

On machines with Secure Boot enabled, some enforcement bypasses behave differently. Know the interaction.

1. The Startup Settings method (Fix 1) works fine with Secure Boot on — it is the recommended path for Secure Boot machines.
2. The `testsigning` bcdedit method may be blocked or behave unexpectedly with Secure Boot enabled on some firmware.
3. Do not disable Secure Boot in BIOS just to install a driver — that trades a major security protection for convenience, and most unsigned-driver needs do not require it.
4. If a driver absolutely will not load even with enforcement disabled, check whether it is a 32-bit driver on 64-bit Windows or vice versa — architecture mismatch produces similar errors.
5. When in doubt, Fix 1's one-boot method is the answer that keeps every other protection intact.

### Fix 6: Re-enable everything and verify

Disabling enforcement should be a round trip. Verify you actually came back.

1. After installing, restart normally (not into Startup Settings).
2. Check for the Test Mode watermark — its absence confirms testsigning is off.
3. Run `bcdedit` in an elevated prompt and confirm `testsigning` shows **No** (or is absent) and `nointegritychecks` is off.
4. Confirm the device still works in Device Manager.
5. If you used Fix 1 only, there is nothing to undo — it was already automatic. This verification step is mainly for the bcdedit methods.

### Fix 7: When you should NOT disable enforcement

Honest guidance on when the right answer is to leave it alone — this saves more machines than any bypass method.

1. Do not disable it to install drivers from random download sites — unsigned drivers from untrusted sources are a classic malware vector.
2. Do not disable it permanently as a workaround for a single old device — use Fix 1's one-boot install instead.
3. If the hardware vendor has a signed driver you have not tried, try it first — check [Microsoft's Update Catalog](https://www.catalog.update.microsoft.com/) by searching the hardware ID; signed drivers are often listed there.
4. For Windows 10 machines, also check Windows Update's **Optional updates** — Microsoft signs and distributes many vendor drivers itself.
5. If no signed driver exists anywhere and the device is non-essential, weigh a $20 modern replacement against the ongoing security tradeoff. If driver experiments lead to crashes, the [Driver Verifier violation guide](/articles/how-to-fix-driver-verifier-detected-violation-step-by-step/) and the general [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) will get you unstuck.

## Closing

Driver signature enforcement is a guardrail, not a wall — Windows 10 gives you legitimate ways past it for legitimate reasons. Use the one-boot Startup Settings method for single installs, test mode for development, and always come back. The goal is getting your hardware working without leaving the gate open behind you.
