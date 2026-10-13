---
title: "How to Install a Driver in Compatibility Mode in Windows 11 24H2"
slug: how-to-install-driver-in-compatibility-mode-in-windows-11-24h2
date: 2026-09-11
categories: ["drivers"]
tags: ["compatibility mode", "old driver install", "windows 11 24h2", "legacy driver"]
description: "Need to install a Windows 10 or older driver on Windows 11 24H2? How compatibility mode works, when to use it, and the exact steps for setup-based and INF-based drivers."
thumbnail: "/images/thumbs/how-to-install-driver-in-compatibility-mode-in-windows-11-24h2.webp"
faqs:
  - q: "What does compatibility mode actually do to a driver installer?"
    a: "Compatibility mode lies to the installer about the Windows version, reporting Windows 8 or 7 instead of 11, so version checks that would abort the install pass. It can also apply shims for old API behavior. It does not change the driver itself — a driver that is fundamentally incompatible with the 24H2 kernel will still fail or misbehave. Think of it as getting past the bouncer, not rewriting the guest list."
  - q: "Is it safe to install old drivers in compatibility mode?"
    a: "Generally yes for device drivers from reputable vendors, with two caveats: old drivers can be less stable on the 24H2 kernel and may lack security fixes, and unsigned old drivers require disabling driver signature enforcement, which weakens a real protection. Create a system restore point first, prefer the newest driver that supports your hardware, and treat compatibility mode as a bridge — not a permanent home."
  - q: "Compatibility mode didn't work — the installer still refuses. What now?"
    a: "If the version lie wasn't enough, the driver itself is likely incompatible with 24H2's driver model. Next options: install via Device Manager by pointing at the extracted .inf files (which skips the installer's checks), look for a community or vendor-updated driver package, or check whether Windows' built-in driver already supports the device adequately. For devices showing as unknown, the [unknown device guide](/articles/how-to-fix-unknown-device-in-device-manager-in-windows-11-24h2/) covers identification tricks."
  - q: "Can I use compatibility mode for NVIDIA or AMD graphics drivers?"
    a: "You shouldn't need to — both vendors publish native Windows 11 drivers, and forcing an old graphics driver through compatibility mode is a reliable way to get crashes. Compatibility mode is for orphaned hardware: old printers, scanners, specialty USB devices, and laptop utilities whose vendors never released Windows 11 packages. Graphics drivers should always be the current native build, installed with the [clean install method](/articles/how-to-update-nvidia-drivers-clean-install-in-windows-11-24h2/)."
---

Your laptop has a perfectly good printer, scanner, or specialty USB device, and the vendor's last driver package says "Windows 10" or even "Windows 7" on it. Windows 11 24H2 refuses to run the installer — or the installer runs and the device still doesn't work. Before you retire working hardware, there's a legitimate bridge: compatibility mode, which lets older installer programs run under the version identity they expect.

A word of honest framing first. Compatibility mode is a shim for the *installer*, not a time machine for the *driver*. It convinces setup programs that they're running on Windows 8 or 7 so their OS version checks pass. If the underlying driver was built for the old driver model, it may still fail on 24H2's kernel — but a surprising amount of "Windows 10" era hardware works fine once the installer is allowed to proceed, because the driver model didn't actually change that much between 10 and 11. This guide covers when compatibility mode is appropriate, the exact steps for both setup.exe and manual INF installs, and what to do when it isn't enough.

## Why this happens

- **The installer has a hardcoded OS version check.** Old setup programs compare the Windows version against a whitelist and abort on anything newer, even when the driver itself would work.
- **The vendor never released a Windows 11 package.** Orphaned hardware — old printers, scanners, MIDI devices — is frozen at its last supported OS, usually Windows 10 or 8.1.
- **24H2's installer blocking is stricter.** SmartScreen and the 24H2 application compatibility layer are more aggressive about refusing to launch very old installers than Windows 10 was.
- **The driver needs an older runtime the installer bundles.** Some installers check for .NET or Visual C++ versions by OS rather than by actual presence, and fail the check on 11.
- **Unsigned driver components get blocked.** Old packages often include unsigned kernel components that 24H2's driver signature enforcement rejects outright.
- **The installer is 16-bit or uses deprecated APIs.** Truly ancient installers (pre-XP era helpers bundled with old hardware) can't run on 64-bit Windows 11 at all — compatibility mode can't fix that.
- **Windows Update keeps "fixing" your manual install.** You get the old driver working, and Windows Update replaces it with a newer generic one that doesn't support your device's features.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the installer in compatibility mode

The core technique — start here.

1. Right-click the driver's `setup.exe` (or installer file) and choose **Properties**.
2. Open the **Compatibility** tab and check **Run this program in compatibility mode for:**.
3. Select **Windows 8** from the dropdown first (closest to 11); if that fails, try **Windows 7**.
4. Check **Run this program as an administrator**, click **Apply**, then double-click the installer to run it.
5. Create a system restore point before installing (**Create a restore point** in Start search) — old drivers deserve a safety net.

### Fix 2: Use the Program Compatibility Troubleshooter

Let Windows pick the settings when manual selection fails.

1. Right-click the installer > **Troubleshoot compatibility**.
2. Choose **Try recommended settings** and run the installer through the troubleshooter's launch.
3. If it works, save those settings when the troubleshooter asks.
4. If not, choose **Troubleshoot program** and answer the questions — the wizard tries different mode/shim combinations automatically.

### Fix 3: Install via Device Manager with the extracted INF

Bypass the installer program entirely.

1. Extract the driver package (many .exe installers are self-extracting archives — try 7-Zip, or run the installer until it extracts and grab files from the temp folder).
2. Find the `.inf` files in the extracted folders (there may be separate ones for 32/64-bit — use the 64-bit).
3. In Device Manager, right-click the device > **Update driver** > **Browse my computer for drivers** > point at the folder containing the .inf.
4. This skips every installer-side check — OS version, bundled runtimes, all of it — and installs the driver directly. If Device Manager can't even name the hardware, identify it first with the [unknown device identification guide](/articles/how-to-fix-unknown-device-in-device-manager-in-windows-11-24h2/).

### Fix 4: Temporarily disable driver signature enforcement

For old drivers with unsigned components.

1. Go to **Settings** > **System** > **Recovery** > **Advanced startup** > **Restart now**.
2. **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **7** for **Disable driver signature enforcement**.
3. Install the driver in this session. Note this is per-boot — the enforcement returns on the next restart.
4. Only do this for drivers you trust from known vendors; unsigned kernel code is a genuine security risk, which is why [Microsoft documents the driver signing requirements](https://support.microsoft.com/en-us/windows) rather than recommending bypasses.

### Fix 5: Block Windows Update from replacing the working driver

Protect the old driver once it's installed.

1. After the device works, note the driver version in Device Manager.
2. Set the registry DWORD `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\ExcludeWUDriversInQualityUpdate` to **1** to stop driver updates via Windows Update.
3. Alternatively, use the vendor's utility to manage that device's driver instead of Windows Update.
4. If Windows already replaced it, roll back via the **Driver** tab in Device Manager first.

### Fix 6: Verify the device actually works under the old driver

Don't assume success — test the full feature set.

1. Test every function of the device (printing *and* scanning, all buttons on the peripheral), not just basic detection.
2. Check Device Manager for warning icons after a full restart — some old drivers load initially then fail on the second boot.
3. Run the device through a sleep/wake cycle; old power-management code is the most common late failure.
4. If features are missing or unstable, accept the verdict: check for a community-updated driver package, or confirm the exact device identity with the [driver version check guide](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/) and search vendor forums for a 24H2-specific build.

## Closing

Compatibility mode is a practical, legitimate tool — not a hack — for keeping working hardware alive on Windows 11 24H2. Set the version identity, run as admin, fall back to manual INF installation when the setup program won't cooperate, and protect the result from Windows Update. Just keep the honest framing in mind: it's a bridge for orphaned hardware, and the day a native driver exists for your device, cross back to it.
