---
title: "Windows Copilot Runtime Components Missing? How to Restore Them"
slug: windows-copilot-runtime-components-missing
date: 2026-10-21
categories: ["ai-pc"]
tags: ["windows copilot runtime", "copilot runtime missing", "copilot components", "recall not working", "ai pc", "windows 11"]
description: "Windows Copilot Runtime components missing? Learn six step-by-step fixes to restore the runtime, repair AI system components, and get Copilot+ features running."
thumbnail: "/images/thumbs/windows-copilot-runtime-components-missing.webp"
faqs:
  - q: "What is Windows Copilot Runtime?"
    a: "Windows Copilot Runtime is the shared system layer that powers on-device AI features on Copilot+ PCs — Recall, Click to Do, live captions, Studio Effects, and Phi Silica local models. When its components go missing or corrupt, every app built on top of it stops working."
  - q: "How do I know the Copilot Runtime is missing?"
    a: "You will see errors like 'Windows Copilot Runtime components are missing' when opening Recall or Click to Do, Settings > System > System components will show gaps, and AI features such as live captions or Studio Effects silently stop running."
  - q: "Will restoring the runtime delete my files?"
    a: "No. Repairing the component store with SFC and DISM, reinstalling updates, and even an in-place upgrade repair install all keep your files, apps, and settings. Only the damaged system components get rebuilt."
  - q: "Can third-party debloat tools cause this?"
    a: "Yes. Aggressive debloating scripts and registry cleaners sometimes remove Copilot Runtime system packages, thinking they are bloat. If you ran one before the error appeared, the fixes below — especially the repair install — rebuild what was stripped out."
---

Open Recall or Click to Do and you're greeted with an error: Windows Copilot Runtime components are missing. Suddenly every on-device AI feature stops dead — no Recall timeline, no live captions, no Studio Effects.

Everything breaks at once because the Copilot Runtime is the shared system layer under all Windows 11 on-device AI — local Phi Silica models, OCR engines, and the glue to your NPU. Damage that layer and every feature on top collapses.

This guide gives you six fixes in order: confirm what's missing, repair the component store, reinstall packages through Windows Update, and rebuild the runtime with an in-place upgrade if needed. Test Recall or live captions after each step.

## Why this happens

- **Interrupted Windows update:** A cumulative or feature update that stalls, gets force-cancelled, or reboots mid-install can leave Copilot Runtime system packages half-registered — present enough to be expected, broken enough to fail.
- **Debloating scripts and registry cleaners:** Aggressive "debloater" tools sometimes strip Copilot Runtime packages or disable its services, mistaking the AI system layer for removable bloatware.
- **Corrupt component store:** The Windows component store (WinSxS) holds the master copies of every system package. If it corrupts, DISM-based repairs are the only way to rebuild it, and the runtime is often the first victim to show symptoms.
- **Missing or failed NPU driver:** The Copilot Runtime expects a working NPU driver. If the driver was never installed or failed — showing as [code 28 in Device Manager](/articles/npu-error-code-28-drivers-not-installed/) — the runtime components that depend on it fail to initialize and report themselves missing.
- **Version mismatch after a feature update:** Major Windows updates sometimes leave the runtime's user-mode components at the old build while the system core moves on. Apps then look for package versions that no longer exist.
- **Copilot features disabled by policy or settings:** Group Policy or registry tweaks that disable Windows Copilot can also block its runtime packages from installing, making the components appear missing on every dependent app.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm which runtime components are actually missing

Before repairing anything, find out what's missing versus merely turned off — the fix for a disabled Recall differs from the fix for a damaged component.

1. Open **Settings > System > System components** and look for Copilot-related entries and Recall. Missing entries confirm damaged or removed packages.
2. Open **Settings > Privacy & security > Recall & snapshots** and check whether the feature toggles exist at all — absent toggles point to a missing runtime rather than a settings issue.
3. If the error appears in a loop on one specific app — for example Recall stuck on its welcome screen — check the [Recall welcome screen loop fix](/articles/recall-welcome-screen-loop/) before assuming the runtime itself is broken.
4. Note what you find: missing system components need repair (Fix 2–3); missing features on an otherwise healthy list may be disabled (Fix 4).

### Fix 2: Repair the component store with SFC and DISM

Corrupt system files are the most common cause. SFC and DISM rebuild them from known-good sources and fix most missing-component errors.

1. Open **Terminal (Admin)** — right-click Start and choose it — or Command Prompt as administrator.
2. Run `sfc /scannow` and wait for it to finish; restart when it completes, even if it finds nothing.
3. Back in an elevated terminal, run `DISM /Online /Cleanup-Image /RestoreHealth` to rebuild the component store from Windows Update sources.
4. Restart again and test Recall or Click to Do. If the error persists, continue — the packages likely need reinstalling, not just repair.

### Fix 3: Reinstall the latest Windows 11 cumulative update

The runtime ships with Windows, so reinstalling the current cumulative update re-registers all its packages — often succeeding where SFC/DISM alone falls short.

1. Go to **Settings > Windows Update** and install any pending updates, then restart.
2. If none are pending, open the update history, note the latest cumulative update (KB) number, and download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Run the downloaded update package — reinstalling the same cumulative update is supported and re-registers its payload, runtime components included.
4. Restart and recheck Settings > System > System components. Newly appearing Copilot entries confirm the reinstall worked.

### Fix 4: Re-enable the AI features and their system packages

Sometimes the runtime is intact but its features were disabled, so apps report missing components. Re-enabling lets Windows reinstall the packages it needs.

1. Open **Settings > Privacy & security > Recall & snapshots** and make sure **Save snapshots** is available and switched on.
2. Go to **Settings > Apps > Optional features**, click **View features**, and search for any Recall or AI-related features to install.
3. If your Copilot key also stopped responding while features were off, the [Copilot key driver reinstall guide](/articles/copilot-key-driver-reinstall/) covers the hardware side of the same problem.
4. Restart after enabling anything, then launch Recall or Click to Do to confirm the error is gone.

### Fix 5: Update the NPU driver so the runtime can initialize

Copilot Runtime components that accelerate on the neural processor fail to initialize — and report as missing — if the NPU driver is absent or broken. This is especially common after motherboard firmware updates or clean Windows installs.

1. Open Device Manager and check the NPU entry. A yellow warning or an "unknown device" means the driver layer is the real problem.
2. Download the chipset/NPU package for your exact model from your laptop maker — [Dell](https://www.dell.com/support), HP, or Lenovo support — or use Intel's and AMD's official driver tools.
3. Install as administrator, restart, and verify the NPU starts cleanly in Device Manager.
4. Relaunch the failing AI app. If the runtime error clears, the components were never truly missing — the driver just kept them from starting.

### Fix 6: Run an in-place upgrade repair install

When individual repairs fail, an in-place upgrade reinstalls Windows 11 over itself, rebuilding every system package including the full Copilot Runtime, while keeping your files, apps, and settings.

1. Download the Windows 11 installer from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and run setup.exe from inside Windows.
2. Choose **Keep personal files and apps** when asked — this is what makes it a repair install rather than a reset.
3. Let the upgrade complete; it takes 30–90 minutes with several restarts. Do not interrupt it.
4. After signing in, verify System components, test Recall and Click to Do, and confirm the missing-components error is gone for good.

## Closing

A missing Copilot Runtime looks like every AI feature died at once — because architecturally, they did. Start with SFC and DISM, reinstall the cumulative update, verify the NPU driver, and keep the in-place upgrade as your safety net.
