---
title: "Fix Intune Enrollment Failures on Copilot+ PCs"
slug: intune-copilot-plus-pc-enrollment-issues
date: 2026-10-23
categories: ["ai-pc"]
tags: ["intune", "copilot+ pc", "enrollment", "mdm", "autopilot", "troubleshooting"]
description: "Fix Intune enrollment failures on Copilot+ PCs: verify TPM attestation, update Windows, re-run MDM enrollment, and troubleshoot Autopilot step by step."
thumbnail: "/images/thumbs/intune-copilot-plus-pc-enrollment-issues.webp"
faqs:
  - q: "Are Copilot+ PCs supported by Microsoft Intune?"
    a: "Yes. Intune fully supports Windows 11 on ARM, including Snapdragon-powered Copilot+ PCs, for MDM enrollment, Autopilot, and app deployment. Enrollment failures on these machines are configuration or device-state issues, not a platform gap — the fixes below resolve the common ones."
  - q: "Why does enrollment fail with an attestation error on my Copilot+ PC?"
    a: "Attestation errors mean Intune could not verify the device's TPM identity. The usual causes are a TPM that is not ready or cleared, outdated firmware, or a device record mismatch in Entra ID. Checking tpm.msc and updating the BIOS/UEFI firmware resolves most attestation failures."
  - q: "Can I enroll a Copilot+ PC in Intune after initial setup?"
    a: "Yes. Go to Settings > Accounts > Access work or school > Connect and sign in with your work or school account. The device enrolls in MDM without a reset. For a fully managed Autopilot experience, though, the device should go through Autopilot Reset or be reimaged with the Autopilot profile."
  - q: "Does Intune enrollment require a specific Windows edition on ARM?"
    a: "The device needs Windows 11 Pro, Enterprise, or Education — Windows 11 Home cannot enroll in Intune MDM. Many consumer Copilot+ PCs ship with Home, so upgrading to Pro through the Microsoft Store is a common prerequisite step."
---

Your new Copilot+ PC should have joined Intune during setup — instead you got an enrollment error, an Autopilot profile that never applied, or a device that shows as non-compliant no matter what you try. The hardware is fine; something in the identity chain between the TPM, Entra ID, and Intune disagreed.

On Snapdragon machines the usual suspects are familiar to any Intune admin: TPM attestation hiccups, stale device records, Windows edition mismatches, and Autopilot hashes registered to the wrong tenant. ARM adds no new failure modes here — Intune treats these PCs like any other Windows 11 device — but the fixes are worth doing in the right order because attestation problems mask everything behind them.

This guide gives you six fixes in technician order: device readiness first, then enrollment mechanics, then the deeper identity repairs. Some steps need your IT admin; the guide marks those clearly.

## Why this happens

- **TPM not ready or attestation failing:** Intune verifies device identity through TPM attestation. A cleared, disabled, or outdated TPM breaks the chain and enrollment fails at the first hurdle.
- **Windows 11 Home edition:** Home cannot do MDM enrollment at all. Consumer Copilot+ PCs commonly ship with Home, and no amount of troubleshooting enrolls a Home device.
- **Stale or duplicate device record:** A previous enrollment, a wiped-and-reused machine, or a renamed device leaves a conflicting record in Entra ID that blocks the new enrollment.
- **Autopilot hash issues:** The hardware hash was never uploaded, was uploaded to the wrong tenant, or the Autopilot profile assignment has not synced yet.
- **Outdated Windows build or firmware:** Enrollment components and TPM firmware both evolve; a machine months behind on updates can fail checks its own admin console demands.
- **License or assignment gap:** The user lacks an Intune license, or the enrollment targets a group the user or device is not in — an admin-side problem that looks like a device problem.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the TPM is ready and healthy

Everything in Intune enrollment builds on TPM attestation. If the TPM is not ready, every later step fails — so verify it first with the built-in console before touching accounts or profiles.

1. Press **Win + R**, type **tpm.msc**, and press Enter.
2. Confirm the Status reads **"The TPM is ready for use"** with a specification version listed — anything else (not found, not ready) is your problem.
3. If the TPM shows as not ready, check the BIOS/UEFI: reboot into firmware settings and make sure the TPM / security processor is **enabled**, not hidden or disabled.
4. As a last resort in the console, use **Clear TPM** — then reboot and re-run any firmware updates from your manufacturer ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/)) before retesting enrollment.
5. Only proceed to Fix 2 once tpm.msc reports ready; attestation cannot succeed without it.

### Fix 2: Verify the Windows edition and update fully

Two boring prerequisites cause a large share of Copilot+ enrollment failures: the Home edition, which cannot enroll, and an outdated build, whose enrollment components predate what Intune expects.

1. Open **Settings > System > About** and check the **Edition** line — it must say **Pro**, **Enterprise**, or **Education**. If it says Home, upgrade to Pro via the Microsoft Store before anything else.
2. Open **Settings > Windows Update**, install every pending update, and restart — enrollment uses system components that ship with the OS.
3. Confirm the build is a recent Windows 11 release; Intune's newest enrollment flows assume reasonably current builds.
4. Update the BIOS/UEFI firmware from your manufacturer's support page — TPM attestation behavior is firmware-dependent on Snapdragon platforms.
5. After updating, retry enrollment once before moving on; updates alone resolve a meaningful fraction of these failures.

### Fix 3: Re-run MDM enrollment from Settings

If the TPM is ready and the edition is correct, the enrollment attempt itself may just have failed transiently — a network blip during OOBE, a mistyped account, or a token that expired. A clean manual enrollment often succeeds where the setup-time attempt failed.

1. Open **Settings > Accounts > Access work or school** and check what is already listed — remove any stale or half-connected work account first.
2. Click **Connect**, enter your **work or school** email (not a personal Microsoft account), and follow the sign-in prompts.
3. Watch for the "your organization" confirmation screens; if enrollment succeeds you will see the account listed with a **Managed by** note.
4. Open the **Company Portal** app (install it from the Store if missing) and check the device status there.
5. If it fails again, note the exact error code shown — codes like 80180018 (already enrolled elsewhere) point directly at Fix 4's stale-record cleanup. General account and sign-in mechanics are covered in [Microsoft's Windows support documentation](https://support.microsoft.com/en-us/windows).

### Fix 4: Clear stale enrollment state and device records

Error codes about existing enrollments, or a device that enrolls and immediately shows non-compliant, usually mean a ghost record: the device object in Entra ID or Intune still references an old enrollment. This step often needs your IT admin.

1. On the PC, open an elevated Terminal and run `dsregcmd /leave`, then restart — this detaches the device from its current Entra registration.
2. Ask your IT admin to check **Entra ID > Devices** and **Intune > Devices** for duplicate or stale records for this machine and delete them.
3. Confirm with the admin that your user account has an **Intune license** assigned (Microsoft 365 E3/E5, EMS, or standalone Intune) — unlicensed users fail enrollment silently.
4. Verify the device or user is in the groups targeted by the enrollment and compliance policies.
5. Re-run Fix 3's manual enrollment against the now-clean directory state.

### Fix 5: Troubleshoot the Autopilot path

If this machine is supposed to enroll via Autopilot — zero-touch setup with your organization's apps and policies — the failure is usually in the hash registration or profile assignment, both admin-side.

1. Ask your IT admin to confirm the device's **hardware hash** is uploaded in **Intune > Devices > Autopilot** and assigned to the correct deployment profile.
2. Confirm the Autopilot profile itself has synced — newly created profiles can take time to become available to devices.
3. On the device, if you reach the OOBE sign-in screen, the Autopilot profile should apply automatically after the work-account sign-in; if it does not, the hash/profile link is broken.
4. As a remediation, the admin can trigger **Autopilot Reset** from Intune (a clean, profile-driven reset — distinct from the consumer reset flow documented in [resetting an ARM laptop](/articles/rufus-arm-bootable-usb-windows-11/) guides for boot media, which is the manual alternative).
5. After the reset, go through OOBE on a reliable network and do not skip the account sign-in step — that is what triggers profile download.

### Fix 6: Check the logs and escalate with evidence

When the structured fixes fail, stop guessing and read what the enrollment engine actually reported. Precise log evidence turns a vague ticket into a solvable one for your admin or Microsoft support.

1. Open **Event Viewer > Applications and Services Logs > Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider > Admin** and look for error events timestamped at your enrollment attempts.
2. Note the exact error codes and messages — search them verbatim; Intune error codes are well documented and specific.
3. Run the **MDM Diagnostics**: **Settings > Accounts > Access work or school**, select the account, **Info > Create report**, and save the HTML report.
4. Send your admin the report plus the Event Viewer errors and the steps you already tried — "I did Fixes 1–5, TPM ready, Pro edition, error 0x80180014 at 10:32" gets action; "enrollment doesn't work" gets a queue.
5. If local app installs are also misbehaving on the machine, rule out broader installer corruption with the [ComfyUI install troubleshooting approach](/articles/comfyui-arm-windows-install-issues/) mindset — isolate whether the problem is Intune-specific or system-wide before escalating.

## Closing

Intune enrollment on Copilot+ PCs fails for the same reasons it fails on any Windows 11 device: TPM attestation, edition, stale records, or Autopilot registration. Work the chain from the hardware up — TPM ready, Pro edition, clean directory records, correct Autopilot hash — and collect the exact error codes before escalating. The platform is fully supported; the enrollment just needs every link in its identity chain to agree. For Click to Do quirks on these same machines, the [bulleted-list rewrite fix](/articles/click-to-do-bulleted-list-rewrite/) covers that corner.
