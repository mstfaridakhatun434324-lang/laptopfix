---
title: "PIN Not Working on Windows 11: Complete Troubleshooting"
slug: pin-not-working-on-windows-11-troubleshooting
date: 2026-10-09
categories: ["windows-errors"]
tags: ["pin", "troubleshooting", "windows-hello"]
description: "Troubleshoot any Windows 11 PIN failure: diagnose Ngc corruption, TPM problems, Hello issues, and account sync faults with this systematic guide."
thumbnail: "/images/thumbs/pin-not-working-on-windows-11-troubleshooting.webp"
faqs:
  - q: "How do I diagnose which PIN problem I have?"
    a: "Match the symptom: 'PIN isn't available' or wrong-PIN-rejected means Ngc store corruption. Missing PIN option means TPM or credential-provider trouble. 'Something happened' errors during setup mean account sync or service issues. Each points to a different fix, which is why diagnosing first saves time."
  - q: "What is the Ngc folder and why does deleting it fix PIN issues?"
    a: "Ngc (at C:\\Windows\\ServiceProfiles\\LocalService\\AppData\\Local\\Microsoft\\Ngc) is where Windows stores your encrypted PIN credential. When its contents corrupt, Windows can't verify any PIN you enter. Deleting the contents forces Windows to rebuild the store cleanly when you set up a new PIN."
  - q: "Does fingerprint or face unlock break when the PIN breaks?"
    a: "Often yes — Windows Hello biometrics depend on the same PIN-backed credential infrastructure and TPM. Fixing the PIN (Ngc reset, TPM check) usually restores fingerprint and face unlock too. If biometrics fail but PIN works, the issue is the biometric driver, not the credential store."
  - q: "Can domain or work policies disable my PIN?"
    a: "Yes. Work or school accounts can apply policies that disable Windows Hello PIN, require different sign-in methods, or enforce complexity rules. If your laptop is managed, check with IT before troubleshooting — and check Settings, then Accounts, then Sign-in options for policy notices."
---
PIN troubleshooting goes wrong when people treat every failure the same way. "PIN isn't available," "PIN incorrect" (when it isn't), the PIN option vanishing entirely, and setup failing halfway are four different problems with four different fixes. This guide is organized as a diagnostic: match your symptom, apply the matching repair, and only escalate if it doesn't fit.

Start by reading the symptom list below and jumping to your section. If you'd rather skip the diagnosis and go straight to the highest-success fix, our [best PIN fix guide](/articles/best-way-to-fix-pin-not-working-on-windows-11/) leads with the Ngc reset. The order within each section goes from least to most invasive, and nothing here touches your files.

## Why this happens

- **Ngc store corruption** — damaged encrypted PIN data; symptom: PIN rejected or "isn't available."
- **TPM disabled, cleared, or faulty** — symptom: PIN/Hello options missing or failing to set up.
- **Microsoft account desync** — symptom: setup errors, "something happened," failures after password changes.
- **Stopped credential services** — symptom: PIN worked, then mysteriously stopped after "optimization."
- **Windows Hello driver issues** — symptom: biometrics fail while PIN works, or vice versa.
- **Corrupted user profile** — symptom: PIN works on a new account but not yours.
- **TPM firmware bugs** — symptom: Hello worked, then broke after a firmware or BIOS update.
- **Conflicting credential providers** from third-party security software — symptom: multiple sign-in options misbehave at once.

## How to fix it

Work through these in order, from quickest to most involved.

### Fix 1: Diagnose your symptom first

Thirty seconds of diagnosis picks the right fix.

1. **"Your PIN isn't available" / correct PIN rejected** → Ngc corruption. Go to Fix 2.
2. **PIN option missing from sign-in options** → TPM or provider issue. Go to Fix 3.
3. **"Something happened" during PIN setup** → account or service issue. Go to Fix 4.
4. **PIN broke right after an update or "tune-up"** → services or files. Go to Fix 5, then Fix 6.

### Fix 2: Rebuild the Ngc credential store

The fix for symptom 1 — corrupted PIN data.

1. On the login screen, click **Sign-in options** and sign in with your **password**.
2. Take ownership of `C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc` (**Properties** → **Security** → **Advanced** → change owner, grant full control).
3. Delete everything **inside** the Ngc folder.
4. Go to **Settings** → **Accounts** → **Sign-in options** → **PIN (Windows Hello)** → **Set up** and create a new PIN.

### Fix 3: Verify TPM and the Hello infrastructure

The fix for symptom 2 — missing PIN/Hello options.

1. Run `tpm.msc` — you want **"The TPM is ready for use."** Anything else means a TPM problem.
2. If the TPM is missing or erroring, reboot into BIOS/UEFI and enable **TPM** / **PTT** (Intel) / **fTPM** (AMD).
3. Check **Device Manager** → **Security devices** for the TPM — a yellow warning means a driver issue; update the chipset driver.
4. Re-add the PIN via **Sign-in options** once the TPM reports healthy.

### Fix 4: Repair account sync and credential services

The fix for symptom 3 — setup failures and "something happened."

1. Go to **Settings** → **Accounts** → **Your info**; confirm the right Microsoft account is signed in.
2. If you changed your account password recently, switch to a local account and back (**Your info** → **Sign in with a local account instead**, restart, reverse) to resync credentials.
3. Open `services.msc` and ensure **Credential Manager**, **CNG Key Isolation**, and **TPM Base Services** are running and set to **Automatic**.
4. Retry PIN setup. If it still fails with a hex error, note the code — 0x8009002d, for example, specifically means TPM/credential provider trouble. Searching the exact code plus your laptop model often surfaces maker-specific fixes that generic guides miss.

Our best-practice [PIN repair guide](/articles/best-way-to-fix-pin-not-working-on-windows-11/) covers the Ngc reset with extra detail if Fix 2's permission steps give you trouble.

### Fix 5: Repair system files

The fix for symptom 4 — PIN died after an update or tune-up.

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart and test the PIN — or re-add it if you cleared Ngc earlier.
4. If you ran a "debloat"/"privacy" tool, review what it changed — these tools commonly disable Hello components and credential services.

### Fix 6: Update biometric and chipset drivers

When Hello biometrics are involved, drivers matter.

1. In **Device Manager**, expand **Biometric devices** and update the fingerprint sensor driver.
2. Update the chipset driver from your laptop maker's support site — it carries TPM and security-device drivers.
3. Check for a TPM firmware update for your model; several laptop lines have shipped TPM firmware bugs that broke Hello.
4. Remove and re-add fingerprint/face data under **Sign-in options** after driver updates.

### Fix 7: Isolate with a new user profile

Determines whether the damage is profile-level or system-level.

1. Create a new local account (**Settings** → **Accounts** → **Other users** → **Add account**).
2. Sign in, link your Microsoft account, and set up a PIN.
3. **Works on new profile:** your profile's credential store is damaged — migrate files to the new account.
4. **Fails on new profile too:** system-level issue — continue to Fix 8.

### Fix 8: In-place repair install

The final step for system-level PIN breakage.

1. Back up your files.
2. Run Windows 11 setup from [official media](https://www.microsoft.com/en-us/software-download/windows11) inside Windows, keeping files and apps.
3. Sign in with your password first, verify `tpm.msc` is healthy, then add a fresh PIN.
4. Afterward, leave TPM, Hello, and credential services alone — and keep "optimizer" tools away from them.

## Closing

PIN failures are diagnostic problems, not guessing problems: the symptom tells you the cause, and the cause tells you the fix. Ngc corruption, TPM trouble, account desync, broken services — four symptoms, four repairs, and a profile test to settle arguments. Work it like a flowchart instead of a grab bag, and the PIN will be working again before you've finished your coffee. Probably. And if Hello itself (fingerprint or face) stays broken after the PIN is fixed, our [Windows Hello repair guide](/articles/how-to-fix-windows-hello-not-working-on-windows-11/) covers the biometric side of the same credential stack.
