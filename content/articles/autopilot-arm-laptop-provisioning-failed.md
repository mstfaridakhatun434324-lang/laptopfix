---
title: "How to Fix Autopilot Provisioning Failures on ARM Laptops"
slug: autopilot-arm-laptop-provisioning-failed
date: 2026-10-23
categories: ["ai-pc"]
tags: ["autopilot", "provisioning", "arm laptop", "intune", "esp timeout", "copilot+"]
description: "Fix Autopilot provisioning failures on ARM laptops: ESP timeouts, Intune app install hangs, TPM attestation errors, and white-glove blocks — step-by-step."
thumbnail: "/images/thumbs/autopilot-arm-laptop-provisioning-failed.webp"
faqs:
  - q: "Why does Autopilot get stuck at the Enrollment Status Page on my Snapdragon laptop?"
    a: >
      The most common cause is a Win32 or ARM64 app failing to install within the ESP timeout window, often a legacy x86 installer running under emulation that hangs silently. Review the Intune app install status and ESP timeout settings, and consider excluding non-ARM-native installers from the provisioning phase.
  - q: "Does Windows Autopilot support Windows on ARM devices?"
    a: >
      Yes, Autopilot fully supports ARM64 devices running Windows 11, including Copilot+ PCs. The failure points are rarely ARM-specific — they are usually driver or app packages that were validated only on x64, plus TPM attestation timing that runs slower on first boot.
  - q: "Can I bypass a failed provisioning step without reimaging?"
    a: >
      In most cases yes: rebooting into audit-safe states lets you fix the offending app or policy, then the ESP resumes or can be skipped with a registry override for technician access. A full wipe should be the last resort, not the first.
  - q: "Why does Autopilot fail only on some of my ARM laptops?"
    a: >
      Mixed hardware revisions and firmware versions behave differently during provisioning — one batch may ship with a TPM firmware that attests slower, or a driver that enumerates later in boot. Verify the exact build and firmware revision of failing units before changing the deployment profile.
---

You unboxed the new Snapdragon Copilot+ fleet, started Autopilot, and watched the Enrollment Status Page crawl — then fail at "Installing apps" or stall on "Joining your organization's network" until it times out. The hardware is fine; the provisioning sequence is tripping over x64-era apps and policies.

ARM64 devices use the same Autopilot pipeline as Intel laptops, but x86-only installers run slowly under emulation and exceed ESP timeouts, and driver packages often assume x64-only hardware IDs. Neither surfaces in a two-machine pilot — both surface at scale.

This guide walks the failure points in technician order: reading ESP logs to find the real blocker, fixing app and driver packages for ARM64, adjusting timeouts and TPM behavior, and recovering a stuck machine without reimaging.

## Why this happens

- **x86-only apps exceeding ESP timeouts under emulation:** Legacy x64 installers run through Prism emulation, often 2-3x slower. The ESP timeout expires while the installer is still legitimately working, and Autopilot records a failure.
- **Driver packages with x64-only INF assumptions:** A driver uploaded to Intune that targets only x64 hardware IDs silently fails to match on ARM64 devices, leaving devices without a driver the ESP step was waiting on.
- **TPM attestation running slow on first boot:** ARM firmware initializes the TPM and attestation chain differently; on some Snapdragon platforms the first attestation takes long enough to collide with Autopilot's expected timing, producing intermittent "something went wrong" errors.
- **Win32 detection rules that never resolve on ARM:** Detection scripts checking x86 Program Files paths or x64 registry hives return "not installed" forever, so Intune retries the install in a loop until the ESP fails.
- **Network-dependent steps on a slow first connection:** Wi-Fi-only ARM laptops sometimes associate slowly on first boot; steps assuming instant connectivity (domain join, certificate enrollment) time out before the link is stable.
- **White-glove flows hitting the same blocks:** Pre-provisioning failures look identical to user-driven ones; the same fixes apply to both.
- **Mismatched firmware revisions:** Some units ship older UEFI firmware that enumerates devices differently, shifting which step fails. Compare firmware versions before assuming randomness.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the ESP logs and identify the actual failing step

Autopilot's error screen is vague by design. The real diagnosis lives in the local provisioning logs, which name the exact app, policy, or script that failed. Never change the deployment profile until you have read them.

1. On the failed machine, press **Shift + F10** at the error screen to open a command prompt (this works during OOBE on most Autopilot profiles).
2. Run `mdmdiagnosticstool.exe -area Autopilot;TPM -cab c:\autopilot.cab` to collect provisioning diagnostics.
3. Extract the CAB on a technician machine and open the Autopilot logs — find the first step marked failed, not the timeout message that follows.
4. Note the exact app GUID or policy name; cross-check it under **Devices > the device > Managed apps** in Intune. If the machine will not reach the command prompt, a [safe-mode boot on your ARM laptop](/articles/safe-mode-arm-laptop-boot/) can get you to a recovery shell.
5. Classify the failure: app install hang, detection rule loop, TPM attestation error, or policy conflict — the remaining fixes each target one class.

### Fix 2: Rebuild failing apps as ARM64-native packages

Once you know which app fails, the fix is almost always packaging: replace the x86 installer with an ARM64-native build, or fix detection so it resolves on ARM64. Emulated installs are the number one ESP killer on Snapdragon fleets.

1. In Intune, open the failing app's properties and check whether an ARM64 installer exists from the vendor — most major enterprise apps now ship one.
2. If only x86 exists, extend the install timeout in the assignment — raise the restart grace period and the Win32 install timeout so emulation has room to finish.
3. Fix the detection rule: point file/registry checks at ARM64 paths (`C:\Program Files`, not `C:\Program Files (x86)`) or use a custom detection script that handles both architectures.
4. Move long or emulation-heavy installs out of the ESP blocking phase — assign them as required but non-blocking, so provisioning completes while the app installs in the background.
5. Re-run provisioning on one test device with the fixed package before touching the fleet profile.

### Fix 3: Correct the driver and firmware layer for ARM64

Driver steps fail on ARM when the uploaded package only matches x64 hardware IDs, or when firmware is too old to enumerate a component the policy expects. Validate both against the failing hardware.

1. Confirm the failing units' model and firmware in **Intune > Devices > Hardware** and compare against units that provisioned successfully.
2. Update UEFI firmware from the OEM (Dell, HP, Lenovo support pages) — firmware fixes for TPM attestation timing on Snapdragon platforms ship regularly.
3. Re-upload driver packages with ARM64-capable INFs; remove x64-only driver assignments from the ARM group so they cannot block matching.
4. If a driver step hangs, check whether Windows Update already delivered a working driver — if so, delete the Intune driver assignment for the ARM group and let WU handle it.
5. After firmware updates, reset the device and re-run Autopilot; do not judge the fix on a machine still holding the old TPM attestation state.

### Fix 4: Adjust ESP timeouts and blocking behavior for ARM reality

Default ESP timeouts were tuned for fast x64 installs. ARM emulation and first-boot attestation legitimately take longer — without headroom, healthy installs get marked failed.

1. In **Intune > Devices > Windows enrollment > Enrollment Status Page**, open the ESP profile and raise the error timeout to 120 minutes for the ARM group.
2. Reduce ESP-blocking apps to the true minimum (security agent, VPN client); move everything else to non-blocking required assignments.
3. Enable **"Allow users to collect logs"** so failures produce diagnostics instead of a dead end.
4. For white-glove flows, verify the technician ESP profile has the same relaxed timeouts — it is a separate profile, often left at defaults.
5. Re-test on the slowest unit; if it passes, the timeouts suit the whole group.

### Fix 5: Stabilize first-boot networking and TPM attestation

Intermittent failures that move between steps are usually timing: Wi-Fi association, TPM attestation, and app installs racing on first boot. Slow the race down.

1. For Wi-Fi-only provisioning, use a wired USB-C Ethernet adapter during initial provisioning where possible — it removes association timing from the equation entirely.
2. In the ESP profile, confirm **"Block device use until all apps and profiles are installed"** matches your intent; for troubleshooting, temporarily allow blocking-apps-only and observe.
3. Clear stale TPM state on repeatedly failing units: `tpm.msc` → **Clear TPM** (or `Clear-Tpm` in PowerShell from the Shift+F10 prompt), then reboot and re-run enrollment.
4. Check the date and time in UEFI — attestation fails outright on a wrong clock, common on devices that sat in a warehouse.
5. After a clean attestation, provisioning usually completes in one pass; if it still fails, the blocker is back in the app layer (Fix 2).

### Fix 6: Recover a stuck device without reimaging

A machine parked at a failed ESP screen is not bricked. You can usually reach a working desktop, fix the offending item, and complete enrollment — reimaging is the last resort.

1. At the failure screen, press **Shift + F10** — or simpler, reboot and let Autopilot retry; most profiles allow a retry without wiping.
2. To bypass the ESP for technician access: in the Shift+F10 prompt, create the registry value `HKLM\SOFTWARE\Microsoft\Enrollments\Status\SkipUserStatusPage` (DWORD = 1) on test machines only — never in production profiles.
3. Once at the desktop, open **Settings > Accounts > Access work or school**, verify the Intune enrollment state, and manually install or remove the app that failed.
4. Run `dsregcmd /status` to confirm Azure AD join state and re-run `mdmdiagnosticstool` to confirm the failing step now passes.
5. For units that repeatedly need rescue, check whether a background workload is starving the installer — runaway [live captions transcription](/articles/save-live-captions-transcript/) or an NPU workload like [AnythingLLM failing to detect the NPU](/articles/anythingllm-npu-not-detected/) can consume CPU during provisioning. Disable such startup items in the image.

## Closing

Autopilot failures on ARM laptops are almost never ARM problems — they are x86-era packages, tight timeouts, and slow first-boot timing colliding with a strict sequence. Read the logs, fix packaging for ARM64, give the ESP realistic timeouts, and most fleets go green without touching hardware.
