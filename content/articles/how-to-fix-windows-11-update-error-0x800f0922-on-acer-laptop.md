---
title: "How to Fix Windows 11 Update Error 0x800f0922 on an Acer Laptop"
slug: how-to-fix-windows-11-update-error-0x800f0922-on-acer-laptop
date: 2026-09-09
categories: ["windows-update"]
tags: ["0x800f0922 fix", "acer windows update error", "net framework 3.5 update error", "windows 11 update failed"]
description: "Error 0x800f0922 blocking updates on your Acer laptop? The .NET Framework 3.5 step is failing — repair the feature, clear the pending state, and retry."
thumbnail: "/images/thumbs/how-to-fix-windows-11-update-error-0x800f0922-on-acer-laptop.webp"
faqs:
  - q: "Why does the update fail at the same point every time?"
    a: "Because the failure is deterministic: the installer reaches the .NET 3.5 configuration step, finds the broken feature state, and fails the same way on every attempt. Retrying without changing the feature state will never succeed — you have to fix or remove the broken piece first."
  - q: "Is it safe to disable Secure Boot to test?"
    a: "Temporarily, yes, as long as you re-enable it afterward. Secure Boot protects against boot-level malware, so do not leave it off. The test is only worthwhile on Acer firmware where the .NET installer shim is known to clash with Secure Boot validation."
  - q: "Will a manual Catalog install really bypass the error?"
    a: "Often, yes. The standalone .msu installer handles feature configuration differently from the Windows Update engine path, and many users report the manual install succeeding where automatic updates failed repeatedly with 0x800f0922. It is one of the highest-success fixes for this code."
  - q: "Should I just reinstall Windows to fix 0x800f0922?"
    a: "Only as a last resort. The .NET feature repair, pending.xml cleanup, and manual Catalog install resolve the large majority of cases without a reinstall. An in-place upgrade that keeps your files and apps is the sensible final step if everything else fails."
---

If Windows Update on your Acer laptop keeps dying with 0x800f0922, the update engine is telling you that one of its sub-installers failed — and nine times out of ten that sub-installer is .NET Framework 3.5. Windows features like .NET 3.5 are installed from side-by-side payloads, and if those payloads are missing or corrupt, every update that touches the feature fails with this exact code. [0x800f0922 appearing in Windows 11 24H2](/articles/how-to-fix-error-0x800f0922-in-windows-11-24h2/)

Acer-specific note: Acer Care Center sometimes toggles Windows features during driver installs, and I have seen Acer laptops where .NET 3.5 was left in a half-enabled state after an Acer Care Center session. The Features dialog (optionalfeatures.exe) will show you the truth in seconds, and that is where the diagnosis starts.

## Why this happens

- **App Readiness service disabled.** Updates that configure features depend on this service; tuners often disable it. Debloat tools target this service aggressively; check its state in services.msc.
- **Corrupted CBS store.** The component-based servicing store fails the transaction the .NET installer needs. DISM /Online /Cleanup-Image /ScanHealth reports store corruption quickly.
- **Acer Care Center feature toggling.** Acer's utility can leave Windows features in inconsistent states after driver operations. Review Acer Care Center's history for feature changes made around the time updates started failing.
- **Pending restart from a previous update.** A stuck pending.xml makes every new update attempt fail at the same installer step. Clear C:\Windows\WinSxS\pending.xml only after a clean reboot fails to clear it.
- **Third-party .NET or developer tools.** SDKs and targeting packs can conflict with the inbox .NET 3.5 feature install. Visual Studio-era targeting packs are the usual suspects in this category.
- **Corrupted update payload.** The downloaded cumulative update itself is damaged and fails when it reaches the .NET step. Re-download from the Catalog rather than trusting a cached copy.
- **Insufficient EFI partition quirks.** Rare, but Secure Boot validation failures during feature configuration produce this code. This is the rarest cause on the list; investigate it last.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable the App Readiness service

Feature configuration during updates depends on App Readiness. Debloat tools love to disable it. [the same error on Windows 10](/articles/how-to-fix-error-0x800f0922-on-windows-10/) If .NET 3.5 was enabled only because an old application demanded it, consider whether that application is still needed before repairing the feature.

1. Press Win + R, type services.msc, and press Enter.
2. Find 'App Readiness' and set its Startup type to Manual.
3. Do the same for 'AppX Deployment Service (AppXSVC)'.
4. Restart and retry the update.
5. If a tuner keeps disabling it, remove or reconfigure the tuner.
6. If the update still fails, note whether it fails at the same percentage — a different failure point means progress.

### Fix 2: Check Secure Boot settings

On some Acer firmware, Secure Boot interferes with the .NET installer shim. This is a diagnosis step, not a permanent change. On Acer systems, Acer Care Center driver installs occasionally toggle Windows features as a side effect, so check the feature state after any Acer Care Center session.

1. Restart and enter the BIOS/UEFI setup (F2 on most Acer laptops).
2. Find the Secure Boot option under the Security or Boot tab.
3. Temporarily disable it, save, and boot into Windows.
4. Retry the update. If it succeeds, re-enable Secure Boot afterward.
5. If it still fails, re-enable Secure Boot immediately and continue.
6. Restart once more and run a second update check to catch any follow-on updates the first pass unblocked.

### Fix 3: Reset the Windows Update cache

A damaged download can fail at the .NET step even when the feature state is fine. The SxS payload for .NET 3.5 is about 300 MB; if Disk Cleanup removed it, DISM needs a source, which is why the ISO method exists.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv, net stop bits, net stop cryptsvc.
3. Rename C:\Windows\SoftwareDistribution to SoftwareDistribution.old.
4. Restart the services with net start wuauserv, net start bits, net start cryptsvc.
5. Check for updates to pull a fresh copy of the payload.
6. Confirm your applications that need .NET 3.5 still launch correctly after the feature state change.

### Fix 4: Run SFC and DISM

CBS store corruption breaks the transaction the .NET installer needs. Error 0x800f0922 specifically means a CBS installer failed, which distinguishes it from download errors (0x800700xx) and servicing corruption (0x80073712).

1. Open Command Prompt as administrator and run: sfc /scannow.
2. Then run: DISM /Online /Cleanup-Image /RestoreHealth.
3. Restart the laptop.
4. Retry the update after both complete.
5. If DISM cannot repair the store, continue to the manual install.
6. Delete any mounted ISO afterward and store it for future use rather than leaving it attached.

### Fix 5: Install the update manually from the Catalog

Bypass the failing installer path entirely by installing the cumulative update by hand. After fixing the feature state, install one small update first to prove the pipeline works before attempting the large cumulative update.

1. Find the KB number in Settings > Windows Update > Update history.
2. Go to [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for that KB number.
3. Download the .msu for your architecture (x64 for most Acer laptops).
4. Double-click the .msu to install it and restart when prompted.
5. Manual installs often succeed where the automatic path fails at 0x800f0922.
6. If you disabled .NET 3.5 to bypass the error, document which apps need it before you forget.

### Fix 6: Uninstall conflicting .NET SDKs temporarily

Developer targeting packs and SDKs occasionally fight the inbox .NET 3.5 feature. If the machine was upgraded from Windows 10, the .NET feature state sometimes carries over broken; a clean feature reset resolves those legacy states.

1. Open Settings > Apps > Installed apps and look for .NET SDKs or targeting packs.
2. Uninstall ones you do not actively need (you can reinstall them later).
3. Restart and retry the update.
4. Reinstall your SDKs after the update succeeds.
5. This is rare, but worth trying before a repair install.
6. Run sfc /scannow once after the successful update to confirm the servicing operations left the system consistent.

### Fix 7: Do an in-place upgrade repair

The last resort: reinstall Windows over itself, keeping files and apps, which rebuilds the feature and servicing state. Keep a Windows 11 ISO handy on a USB stick — it doubles as the DISM source and as repair media for future problems.

1. Back up important files first.
2. Download the Windows 11 media creation tool from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Run setup.exe and choose 'Keep personal files and apps'.
4. Complete the repair install (30 to 90 minutes).
5. The 0x800f0922 failure state does not survive a fresh servicing stack.
6. Keep the KB number noted; if the error ever returns, you will know exactly which update to investigate.

## Closing

Once the .NET feature state is clean, this error rarely returns — which is why the feature check comes first and generic cache-clearing comes later. Work the list in order and verify after each step rather than stacking fixes blindly. Related update-failure patterns are covered in [a broader Windows 11 update failure](/articles/how-to-fix-windows-update-error-0x800f0922-in-windows-11-24h2/).
