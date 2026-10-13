---
title: "How to Fix IRQL_NOT_LESS_OR_EQUAL on a Lenovo Laptop"
slug: fix-irql-not-less-or-equal-on-lenovo-laptop
date: 2026-09-03
categories: ["windows-errors"]
tags: ["IRQL_NOT_LESS_OR_EQUAL", "Lenovo", "driver errors"]
description: "Fix IRQL_NOT_LESS_OR_EQUAL on your Lenovo laptop: update drivers via Lenovo Vantage, read the crash dump, test RAM, and end the 0xA blue screens."
thumbnail: "/images/thumbs/fix-irql-not-less-or-equal-on-lenovo-laptop.webp"
faqs:
  - q: "Why does my Lenovo keep crashing with IRQL_NOT_LESS_OR_EQUAL?"
    a: "On Lenovos, the usual triggers are outdated Intel Wi-Fi or chipset drivers, Lenovo-specific system drivers (like the ACPI or power management drivers) lagging behind Windows updates, and third-party antivirus filters. The stop code 0xA means a driver touched memory it shouldn't have — updating the right driver almost always fixes it."
  - q: "Should I use Lenovo Vantage or Windows Update for drivers?"
    a: "Use Lenovo Vantage first. Lenovo validates driver packages against your exact model, including the power-management and chipset drivers Windows Update often gets wrong. Windows Update is fine as a supplement, but Vantage's model-specific drivers are the safer bet for fixing IRQL crashes on ThinkPads, IdeaPads, and Legions."
  - q: "Can Lenovo's preinstalled software cause this blue screen?"
    a: "Occasionally. Older versions of Lenovo Vantage components, Lenovo System Update drivers, and bundled McAfee trials have all been implicated in IRQL crashes. If crashes started after a Lenovo software update, try updating (not removing) Vantage first, and uninstall the McAfee trial in favor of Windows Security."
  - q: "How do I find which driver is crashing my Lenovo?"
    a: "Read the crash dump: open the newest .dmp file in C:\\Windows\\Minidump with WinDbg Preview (free from the Microsoft Store), configure symbols, and run !analyze -v. The IMAGE_NAME line names the faulting driver. On Lenovos it's frequently Netwtw10.sys (Intel Wi-Fi) or a Lenovo system driver."
---

IRQL_NOT_LESS_OR_EQUAL (stop code `0xA`) on a Lenovo laptop follows the same rules as everywhere else — a driver broke Windows' memory-access rules — but the fix has a Lenovo-specific fast lane: Lenovo Vantage delivers model-validated drivers that Windows Update doesn't. Start there before anything else.

This guide blends the general IRQL playbook (see our [complete IRQL fix guide](/articles/irql-not-less-or-equal-blue-screen-error-fix/)) with the Lenovo-specific steps that resolve most cases on ThinkPads, IdeaPads, and Legions. The order matters: Lenovo-validated drivers first, because they fix the cause; dump analysis second, because it confirms the target. If you're seeing [APC_INDEX_MISMATCH](/articles/how-to-fix-apc-index-mismatch-on-asus-laptop/) instead, the driver-hunting approach is similar.

## Why this happens

- Outdated Intel Wi-Fi drivers (Netwtw10/12.sys) — the top Lenovo-specific offender.
- Lenovo chipset and power-management drivers lagging behind Windows updates.
- Third-party antivirus (especially bundled McAfee trials) installing faulty filter drivers.
- Corrupt graphics drivers on Legion and IdeaPad gaming models.
- Faulty RAM producing inconsistent crash blame across dumps.
- A Windows feature update exposing latent bugs in older Lenovo drivers.

## How to fix it

Work through these in order — Vantage first, dumps second, hardware last.

### Fix 1: Update everything through Lenovo Vantage

The single highest-value step on any Lenovo.

1. Open **Lenovo Vantage** from the Start menu (install it from the Microsoft Store if missing).
2. Go to **Device > System Update** and click **Check for Updates**.
3. Install all **Critical** and **Recommended** updates — prioritize **Wi-Fi**, **chipset**, **BIOS**, and **power management**.
4. Restart when prompted, even if it seems optional.
5. Lenovo's [official support site](https://support.lenovo.com/us/en/) has manual downloads if Vantage misses a driver.

### Fix 2: Read the dump to confirm the driver

Don't update blindly — let the crash name its culprit.

1. Open the newest `.dmp` in `C:\Windows\Minidump` with **WinDbg Preview**.
2. Set symbols once, then run `!analyze -v`.
3. Read **IMAGE_NAME**: `Netwtw10.sys` = Intel Wi-Fi, `rtwlanu.sys` = Realtek, `nvlddmkm.sys` = NVIDIA.
4. Run `lmvm <name>` to check the driver's date — old timestamps confirm staleness.
5. Target that specific driver in the remaining fixes.

### Fix 3: Replace the Intel Wi-Fi driver properly

Intel Wi-Fi drivers are the most common IRQL trigger on Lenovos — update them from Intel directly.

1. In **Device Manager > Network adapters**, note your exact Intel Wi-Fi model.
2. Download the latest **Intel Wireless** driver from Intel's official site or use their driver detection tool.
3. In Device Manager, right-click the Wi-Fi adapter, choose **Uninstall device**, and check **Delete the driver software**.
4. Install the freshly downloaded driver and restart.
5. Test with heavy network use (video calls, large downloads) that previously triggered crashes.

### Fix 4: Remove the McAfee trial and other filter drivers

Bundled antivirus trials are a notorious IRQL source on new Lenovos.

1. Open **Settings > Apps > Installed apps** and uninstall **McAfee** (or any bundled trial antivirus).
2. Use the vendor's official **removal tool** afterwards — standard uninstalls leave filter drivers behind.
3. Restart; **Windows Security** activates automatically.
4. Also uninstall any VPN clients you don't actively use.
5. Test for several days before installing any replacement security software.

### Fix 5: Update or reinstall the graphics driver

Legion and IdeaPad gaming models crash on GPU drivers that Vantage sometimes lags on.

1. Identify your GPU in **Device Manager > Display adapters**.
2. For NVIDIA, download from [NVIDIA's official page](https://www.nvidia.com/Download/index.aspx); for AMD integrated graphics, use Lenovo Vantage or AMD's site.
3. For a truly clean install, use **DDU** in Safe Mode first, then install fresh.
4. Avoid "Game Ready" bleeding-edge drivers if stability matters more than day-one game support.
5. Restart and test with the games or apps that crashed before.

### Fix 6: Test RAM when dumps blame different drivers

Consistent blame = driver. Inconsistent blame = test the memory.

1. Press **Win + R**, type `mdsched.exe`, and run **Windows Memory Diagnostic**.
2. Check **Event Viewer > Windows Logs > System** for the **MemoryDiagnostics-Results** entry.
3. For certainty, run **MemTest86** from USB for 4 passes.
4. Reseat sticks before replacing; test one at a time.
5. Replace confirmed-faulty RAM with the specs your Lenovo model requires.

### Fix 7: Repair system files and roll back bad updates

Clean up OS-level damage and update-triggered regressions.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
2. If crashes began after a Windows update, uninstall it via **Settings > Windows Update > Update history > Uninstall updates**.
3. Restart and monitor for a few days.
4. Microsoft tracks known issues on its [Windows support hub](https://support.microsoft.com/en-us/windows).
5. Re-enable updates gradually once stable.

### Fix 8: Update the BIOS as the final driver-side step

Lenovo BIOS updates frequently fix IRQL crashes via new firmware and microcode.

1. Check your current BIOS version with `msinfo32` (**BIOS Version/Date**).
2. Compare against the latest for your exact model on Lenovo's official support site.
3. Read the release notes for stability or crash fixes.
4. Install with the charger plugged in and don't interrupt the process.
5. After updating, load BIOS defaults once, then retest under your normal workload.

## Closing

IRQL_NOT_LESS_OR_EQUAL on a Lenovo is a driver problem with a Lenovo-shaped solution: Vantage first for validated drivers, the dump to name the exact culprit, Intel's own Wi-Fi driver when Vantage lags, and the bundled antivirus trial shown the door. Follow that order and the 0xA crashes end — no reinstall required, and no guesswork either. Keep Vantage updating drivers on its schedule afterwards; staying current is what prevents the next round of crashes. And if a future update breaks things again, you'll know exactly where to look first instead of starting from scratch like you did the last time. That hard-won familiarity turns the next crash from a crisis into a routine.
