---
title: "SYSTEM_LICENSE_VIOLATION Blue Screen: Causes and Fixes"
slug: how-to-fix-system-license-violation-bsod-youtube
date: 2026-09-23
categories: ["windows-errors"]
tags: ["blue screen", "licensing", "windows 11"]
description: "Hit with a SYSTEM_LICENSE_VIOLATION blue screen? It's usually a licensing or driver conflict — here's how to diagnose and fix it for good."
thumbnail: "/images/thumbs/how-to-fix-system-license-violation-bsod-youtube.webp"
faqs:
  - q: "What is the SYSTEM_LICENSE_VIOLATION blue screen?"
    a: "It's stop code 0x0000009A, triggered when Windows detects a licensing integrity problem or a driver violates licensing checks. In practice on modern systems, it's more often a corrupt licensing store or a misbehaving driver than actual piracy detection."
  - q: "Does this error mean my Windows is not genuine?"
    a: "Not necessarily. Genuine, activated systems get this error too — usually from corrupted licensing files or driver conflicts. Check Settings > System > Activation first; if it says activated, the cause is technical, not legal."
  - q: "Can a driver really cause a license violation crash?"
    a: "Yes. Certain drivers — particularly storage and security drivers — interact with Windows licensing components. A buggy or incompatible driver can trip the license check and crash the system even on fully genuine installations."
  - q: "Will I need to buy Windows again to fix this?"
    a: "Almost certainly not. Rebuilding the licensing store and repairing system files resolves it without a new purchase. Only if your license is genuinely invalid would you need to address activation separately."
---
SYSTEM_LICENSE_VIOLATION (stop code 0x0000009A) sounds like Microsoft accusing you of piracy, but don't take it personally. On a genuine Windows installation, this blue screen almost always means the licensing store got corrupted or a driver tripped over the license-checking machinery. Either way, it's fixable without buying anything.

Work through these fixes in order. First, quickly verify your activation status — it takes ten seconds and rules out the obvious. For crashes with other stop codes, see our [general blue screen repair guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

## Why this happens

- **Corrupted licensing store.** The files Windows uses to verify activation get damaged.
- **Driver conflicts with licensing components.** Storage and security drivers are frequent triggers.
- **Failed Windows update.** Updates that touch activation components can leave them inconsistent.
- **Corrupted system files.** Damage to licensing-related system files trips the check.
- **Hardware changes.** Major hardware swaps (especially motherboards) can invalidate the license binding.
- **Third-party activation tools.** Cracks and KMS activators corrupt the licensing store.
- **BIOS/UEFI issues.** The embedded OEM key can become unreadable after firmware problems.

## How to fix it

Work through these in order — stop when the crashes stop.

### Fix 1: Verify your activation status

Rule out the simple explanation first.

1. Open **Settings > System > Activation**.
2. Check the status. If it says **Active** or **Windows is activated**, your license is fine and the crash is technical — continue with Fix 2.
3. If it shows an error, click **Troubleshoot** and follow the activation troubleshooter.
4. Note your product key type: **digital license** (tied to your Microsoft account/hardware) or **product key**.
5. If you recently changed major hardware, use the troubleshooter's **I changed hardware on this device recently** option.
6. Microsoft's activation help on [support.microsoft.com](https://support.microsoft.com/en-us/windows) covers the error codes if the troubleshooter stalls.

### Fix 2: Rebuild the licensing store

The core fix for corrupted licensing data.

1. Open an elevated Command Prompt: right-click **Start > Terminal (Admin)**.
2. Stop the Software Protection service:
   `net stop sppsvc`
3. Rename the corrupted licensing store (Windows rebuilds it automatically):
   `ren C:\Windows\System32\spp\store\2.0\tokens.dat tokens.old`
   If the path differs slightly on your build, check `C:\Windows\System32\spp\store\` for the version folder first.
4. Restart the service:
   `net start sppsvc`
5. Then re-register the license:
   `slmgr.vbs /rilc`
6. Restart the laptop and check **Settings > System > Activation** again.

### Fix 3: Repair system files with SFC and DISM

Licensing components depend on intact system files.

1. Open an elevated terminal.
2. Repair the component store:
   `DISM /Online /Cleanup-Image /RestoreHealth`
3. When it finishes, run:
   `sfc /scannow`
4. Restart the laptop.
5. Re-check activation status — SFC often repairs the exact files the license check needs.
6. If crashes continue, note whether they happen at specific times (startup, during updates) — that pattern helps isolate driver causes.

### Fix 4: Identify and update the offending driver

If licensing is healthy, a driver is tripping the check.

1. Boot into Safe Mode (forced-restart 2-3 times to reach WinRE, then **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4**).
2. If crashes stop in Safe Mode, a third-party driver is the cause.
3. Open **Device Manager** and look at **Storage controllers**, **Network adapters**, and any security devices.
4. Update each via **Update driver > Search automatically for drivers**, or download from your laptop maker's support site.
5. If crashes began after a specific driver update, use **Properties > Driver > Roll Back Driver** instead.
6. Pay special attention to disk-encryption and endpoint-security drivers — they interact most with licensing. If your crashes resemble [DRIVER_POWER_STATE_FAILURE](/articles/driver-power-state-failure-blue-screen-error-fix/) patterns (crashes on sleep/wake), the power-related driver is suspect.

### Fix 5: Remove third-party activation tools

If any crack or activator was ever used, it poisoned the store.

1. Uninstall any KMS activators or "loader" tools from **Settings > Apps > Installed apps**.
2. Open an elevated Command Prompt and clear any KMS configuration:
   `slmgr.vbs /upk`
   `slmgr.vbs /cpky`
3. Rebuild the store as in Fix 2.
4. Activate properly: enter your genuine product key via **Settings > System > Activation > Change product key**, or link your digital license to your Microsoft account.
5. Run a full antivirus scan — activator tools are a notorious malware vector.
6. Restart and verify activation shows as genuine.

### Fix 6: Check the BIOS for the embedded key

OEM laptops store the Windows key in firmware.

1. Open an elevated Command Prompt and read the firmware key:
   `wmic path softwarelicensingservice get OA3xOriginalProductKey`
2. If it returns a key, your firmware is fine — the problem is software-side.
3. If it returns nothing on an OEM laptop (HP, Dell, Lenovo, Asus, Acer), enter BIOS/UEFI and check for firmware issues or reset to defaults.
4. A BIOS update from your manufacturer's support site can restore a corrupted firmware key table — install with the charger connected.
5. After any BIOS change, re-check activation in Settings.
6. If the firmware key is genuinely gone (rare), contact the laptop manufacturer's support with your serial number.

### Fix 7: Perform an in-place upgrade

The final software repair — fresh system files, kept data.

1. Download the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) on a working PC, or directly if your laptop boots between crashes.
2. Mount the ISO (double-click it) and run `setup.exe`.
3. Choose **Keep personal files and apps**.
4. Complete the upgrade — it replaces every system file including licensing components.
5. Afterward, verify activation and rebuild the licensing store once more (Fix 2) for a clean state.
6. Monitor for several days. If SYSTEM_LICENSE_VIOLATION persists after all of this on verified-genuine Windows, document the minidumps and contact Microsoft support — you're in rare territory.

## Closing

SYSTEM_LICENSE_VIOLATION is intimidating by name but mundane in practice: rebuild the licensing store, repair system files, and chase down the driver if those don't do it. Genuine Windows users should never need to pay again to fix this. Keep your drivers from the laptop manufacturer's site rather than random driver updaters, and the licensing machinery tends to stay quiet.
