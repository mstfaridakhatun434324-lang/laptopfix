---
title: "How to Fix Passkeys Not Working on Windows 11 ARM Laptops"
slug: passkeys-not-working-windows-11-arm
date: 2026-10-23
categories: ["ai-pc"]
tags: ["passkeys", "windows hello", "arm laptop", "sign-in", "copilot+ pc", "troubleshooting"]
description: "Fix passkeys not working on Windows 11 ARM laptops — repair Windows Hello and TPM state, configure browser passkey sync properly, and restore fast sign-in."
thumbnail: "/images/thumbs/passkeys-not-working-windows-11-arm.webp"
faqs:
  - q: "Why do passkeys fail on my ARM laptop but work on my phone?"
    a: "The phone and the laptop store passkeys in different places. On the laptop, passkeys depend on Windows Hello backed by the Pluton TPM — if Hello or the TPM is broken, the browser cannot create or use passkeys even though the same account works on your phone."
  - q: "Does Chrome support passkeys on Windows on ARM?"
    a: "Yes. Both Chrome and Edge support WebAuthn passkeys on Windows 11 ARM natively — there is no x86 emulation involved in the browser path. Failures are almost always in Windows Hello or the TPM layer, not the browser."
  - q: "My PIN works but passkey sign-in says 'something went wrong' — why?"
    a: "A working PIN proves Hello is partially alive, but passkeys need the full WebAuthn stack: a provisioned TPM, an intact credential store, and a browser allowed to call the platform authenticator. Work through the TPM and browser fixes below."
  - q: "Can I use a phone as a security key for passkeys on my laptop?"
    a: "Yes, via Bluetooth cross-device authentication — the laptop shows a QR code and your phone approves the sign-in. This is a good workaround while you repair the laptop's own platform authenticator."
---

You try to sign in with a passkey and Edge or Chrome throws "Something went wrong," the Windows Hello prompt never appears, or creating a new passkey spins forever and fails. Your phone handles the same passkeys fine, so the account is not the problem — your laptop is.

On Windows 11 ARM machines — Snapdragon Copilot+ PCs included — passkeys live in the platform authenticator: Windows Hello backed by the Pluton TPM. The browser is just a messenger; the actual cryptography happens in Hello's key store. When that layer breaks, every passkey on every site breaks with it, which is why the failure looks so total.

This guide repairs the stack bottom-up: verifying Hello and the TPM, fixing the browser's authenticator path, handling sync and Bluetooth cross-device issues, and rebuilding Hello when the credential store is corrupt.

## Why this happens

- **Windows Hello PIN or biometrics broken:** Passkeys are sealed by Hello credentials — if the PIN was reset, corrupted, or never set up, passkey creation and use both fail.
- **TPM unprovisioned or cleared:** The platform authenticator needs a working Pluton TPM; after a reset, firmware update, or failed provisioning, Hello cannot mint passkey keys.
- **Browser not using the platform authenticator:** Extensions, enterprise policies, or a misconfigured default can push the browser toward a different authenticator path that fails on ARM builds.
- **Passkey created on another device with no sync path:** A passkey saved only on your phone is invisible to the laptop unless the site supports cross-device sign-in or the credential is synced.
- **Bluetooth blocked for cross-device sign-in:** Phone-as-authenticator flows need Bluetooth; on some ARM laptops the radio is off or the pairing handshake fails.
- **Corrupt WebAuthn credential store:** Partial writes from a crashed browser session can poison the stored credentials, breaking sign-in while leaving the PIN working.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify Windows Hello is fully working first

Since every laptop passkey flows through Hello, a five-minute Hello health check resolves or rules out the most common cause before you touch anything else.

1. Go to **Settings > Accounts > Sign-in options** and confirm a **PIN (Windows Hello)** is set — passkeys cannot exist without one.
2. Lock the PC (**Win + L**) and sign back in with the PIN to prove it works end to end.
3. If the PIN fails or is missing, remove and re-add it here; do not skip this even if you "never use" the PIN.
4. If Hello itself refuses to set up, the TPM layer underneath is likely broken — the same [Pluton TPM checks used for attestation failures](/articles/pluton-tpm-attestation-failed/) apply here.
5. Only after Hello signs you in cleanly should you retry the passkey — retest on the site that failed before changing anything else.

### Fix 2: Confirm the TPM is ready for the platform authenticator

Hello's passkey keys are generated inside the TPM. A TPM that is present but unprovisioned lets the PIN work while silently breaking passkey creation — a confusing split that this check resolves.

1. Press **Win + R**, type `tpm.msc`, and confirm the status reads "The TPM is ready for use."
2. If it does not, use **Action > Prepare the TPM** and restart — Pluton completes provisioning during boot.
3. In elevated PowerShell, run `Get-Tpm` and verify `TpmReady` is True.
4. Retry creating a test passkey — [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) document the supported Hello recovery steps if provisioning keeps failing.
5. For a deeper system-level view of what hardware Windows actually sees, the same diagnostic approach as [checking whether hardware appears in msinfo32](/articles/msinfo32-npu-not-listed/) applies: confirm the security devices are listed, not just assumed present.

### Fix 3: Fix the browser's passkey and WebAuthn path

With Hello healthy, the browser is the next suspect. Both Edge and Chrome call the same Windows WebAuthn API on ARM, so a browser-side misconfiguration breaks both identically.

1. In Edge, open **Settings > Privacy, search, and services** and make sure **Offer to save passwords** and passkey-related prompts are enabled, not blocked.
2. In Chrome, check **Settings > Privacy and security > Third-party cookies** — some sites' passkey flows fail when cross-site storage needed by the ceremony is blocked; test with a temporary allow.
3. Disable password-manager extensions (1Password, Bitwarden, Dashlane) temporarily — they can intercept the WebAuthn ceremony and fail on ARM builds.
4. Test passkey creation in an InPrivate/Incognito window to rule out extensions and cached state.
5. Try the other browser: if Edge fails but Chrome works (or vice versa), reset the failing browser's settings and retest — the platform layer is fine and the browser profile was the problem.

### Fix 4: Use your phone as a cross-device authenticator

If the laptop's own authenticator still will not cooperate, your phone can approve sign-ins over Bluetooth — and this also tells you whether the site's passkey flow is healthy at all.

1. On the sign-in page, choose the passkey option and look for **"Use a different device"** or a QR code.
2. Make sure Bluetooth is **on** on both the laptop and the phone, and that the devices are near each other.
3. Scan the QR code with the phone's camera and approve the sign-in with the phone's biometrics.
4. If the QR code never appears, the site may not support cross-device sign-in — test on a known-good site like a Microsoft or Google account page.
5. Success here proves the site and your account are fine; the remaining problem is strictly the laptop's platform authenticator, so continue to Fix 5.

### Fix 5: Rebuild Windows Hello and the credential store

When Hello partially works but passkeys fail everywhere, the credential store itself is corrupt. Rebuilding it is destructive to stored credentials but reliable — and your site accounts can re-register passkeys afterward.

1. Go to **Settings > Accounts > Sign-in options** and remove the Hello PIN, facial recognition, and fingerprint — all of them.
2. Restart the laptop so the TPM-backed containers are released cleanly.
3. Re-add the PIN first, then biometrics — set them up fresh, not from any backup.
4. Visit one site that failed, delete its old passkey entry in your account security settings, and create a new passkey from the laptop.
5. If creation succeeds, re-register passkeys on your other important sites; keep your phone's passkeys as backup until the laptop proves stable. If the index of stored credentials seems damaged beyond Hello itself, the same rebuild logic used when [Recall's search index corrupts](/articles/rebuild-recall-search-index/) applies: remove, restart, recreate, verify.

### Fix 6: Update the platform and check for ARM-specific fixes

Passkey and WebAuthn bugs do get fixed in Windows updates — and on ARM laptops, the relevant fixes sometimes arrive in the SoC vendor's driver packages rather than Windows Update itself.

1. Run **Settings > Windows Update** and install everything pending, then restart.
2. Check your maker's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) for chipset, TPM/Pluton, or security-processor driver updates newer than what Windows installed.
3. Install the [Windows 11 download](https://www.microsoft.com/en-us/software-download/windows11) repair path only if updates fail repeatedly — an in-place upgrade preserves files while refreshing the WebAuthn stack.
4. After updating, retest passkey creation on a single site before re-registering everywhere.
5. If one specific site still fails while others work, the problem is that site's ARM/WebAuthn handling — report it to them with your Windows build number (`winver`) rather than rebuilding your laptop again. For diagnosing odd platform behavior generally, tools like [Process Explorer for ARM64](/articles/process-explorer-arm64-download/) help confirm which component is actually hanging during the ceremony, and if the hang happens during on-device AI work, [CPU vs GPU vs NPU for image generation](/articles/cpu-vs-gpu-vs-npu-image-generation/) explains which engine Windows actually uses.

## Closing

Passkeys on ARM laptops fail at the Hello-and-TPM layer, not in the browser — verify the PIN works, confirm the TPM is provisioned, clear the browser's path, and rebuild Hello if the credential store is corrupt. Once the platform authenticator is green, passkeys work on every site at once.
