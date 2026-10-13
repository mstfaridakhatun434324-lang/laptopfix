---
title: "Driver Verifier Detected Violation: How to Fix This Blue Screen Error"
slug: driver-verifier-detected-violation-blue-screen-error-fix
date: 2026-09-16
categories: ["windows-errors"]
tags: ["driver verifier", "bsod", "stop code", "driver issue", "windows 11"]
description: "Seeing DRIVER_VERIFIER_DETECTED_VIOLATION on a blue screen? Learn what triggers it and how to turn off Driver Verifier and fix the faulty driver."
thumbnail: "/images/thumbs/driver-verifier-detected-violation-blue-screen-error-fix.webp"
faqs:
  - q: "What is Driver Verifier?"
    a: "Driver Verifier is a built-in Windows diagnostic tool that stress-tests drivers to catch bugs. When it finds a driver breaking the rules, it deliberately crashes the system with a blue screen so developers can identify the faulty driver. Most home users never turn it on intentionally — it is often enabled accidentally or left on after someone ran a diagnostic."
  - q: "Can Driver Verifier damage my computer?"
    a: "No, it cannot damage hardware. It only forces blue screens when a driver misbehaves, which is annoying but harmless. The crash dumps it produces actually help identify the bad driver. The real risk is leaving it running permanently, because it slows the system and keeps crashing it until you turn it off."
  - q: "How do I turn off Driver Verifier if Windows won't boot?"
    a: "Boot into the Windows Recovery Environment, open Command Prompt from Troubleshoot, Advanced options, and run verifier /reset followed by verifier /bootmode resetonbootfail. This disables Verifier on the next boot. If that fails, you can delete the verifier settings from the registry offline."
  - q: "Which driver usually causes this error?"
    a: "There is no single culprit — Verifier flags whichever driver violates the rules. Graphics drivers, network adapter drivers, and third-party antivirus filter drivers are the most common offenders. Check the minidump file with BlueScreenView or WinDbg to see the exact driver name, which points you to what needs updating or rolling back."
---
DRIVER_VERIFIER_DETECTED_VIOLATION is a blue screen that confuses a lot of people, because it is not really a normal crash — it is Windows catching a driver red-handed and pulling the emergency brake on purpose. If Driver Verifier is running on your laptop, even a slightly misbehaving driver will blue-screen the machine every time it steps out of line.

The fix has two parts: turn off Driver Verifier so the crashing stops, then deal with the underlying driver problem so the system is actually stable. Here is how to do both.

## Why this happens

- **Driver Verifier is enabled and doing its job:** Someone ran `verifier.exe` — deliberately or by accident — and it is now stress-testing drivers and crashing on the first violation it finds.
- **An outdated or buggy driver violates memory rules:** The flagged driver accesses memory it should not touch, and under Verifier's scrutiny that becomes an instant blue screen.
- **A recent driver update introduced a bug:** New GPU, Wi-Fi, or chipset drivers sometimes ship with defects that only Verifier's strict checks expose.
- **Third-party antivirus or VPN filter drivers:** These hook deep into the system, and older versions frequently trip Verifier's checks.
- **Verifier was left on after troubleshooting:** A technician or a forum guide had you enable it to diagnose an older crash, and it was never switched back off.
- **Overclocking or unstable RAM amplifies violations:** Marginal hardware makes drivers behave erratically, which Verifier interprets as driver bugs.
- **Corrupted driver files:** A partially installed or disk-corrupted driver binary can fail Verifier's integrity checks.

## How to fix it

Work through these in order, starting at Fix 1. If you cannot boot normally, start Windows in Safe Mode (hold Shift while clicking Restart, or interrupt boot three times to reach recovery).

### Fix 1: Turn off Driver Verifier

This stops the deliberate crashing immediately.

1. Press **Win + R**, type `verifier`, and press Enter. If Windows boots normally, the Driver Verifier Manager opens.
2. Select **Delete existing settings** and click **Finish**, then restart the laptop.
3. If Windows will not boot, open a recovery **Command Prompt** (**Troubleshoot > Advanced options > Command Prompt**) and run:
   `verifier /reset`
   then `verifier /bootmode resetonbootfail`
4. Restart. The blue screens caused by Verifier itself should stop now.

For a deeper look at Verifier-specific crashes on newer builds, see our guide on [fixing Driver Verifier violations in Windows 11 24H2](/articles/how-to-fix-driver-verifier-detected-violation-in-windows-11-24h2/).

### Fix 2: Identify the offending driver from the crash dump

Once Verifier is off, find out which driver was actually misbehaving.

1. Press **Win + R**, type `%SystemRoot%\Minidump`, and press Enter to open the minidump folder.
2. Look for the most recent `.dmp` file dated around your crashes.
3. Download BlueScreenView (free, from NirSoft) and open the dump with it — the red-highlighted driver name in the lower pane is your culprit.
4. Note the driver file name (for example, `rtwlanu.sys` for a Realtek Wi-Fi driver or `nvlddmkm.sys` for NVIDIA graphics).

If you get other driver-related crashes while investigating, our [IRQL_NOT_LESS_OR_EQUAL fix guide](/articles/irql-not-less-or-equal-windows-11-fix/) covers the most common driver crash in Windows.

### Fix 3: Update the flagged driver

Most Verifier violations disappear once the buggy driver is replaced with a current version.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Find the device matching the culprit driver — expand **Display adapters** for GPU drivers, **Network adapters** for Wi-Fi/Ethernet.
3. Right-click it, choose **Update driver > Search automatically for drivers**.
4. If Windows finds nothing, go to your laptop manufacturer's support page (or the chip maker's site, such as [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel hardware) and download the latest driver manually.
5. Restart and use the laptop normally for a day to confirm stability.

### Fix 4: Roll back the driver if the problem started with an update

If the crashes began right after a driver update, the new version is the problem.

1. In **Device Manager**, right-click the device and choose **Properties**.
2. Go to the **Driver** tab and click **Roll Back Driver** if the button is active.
3. Choose a reason and click **Yes**, then restart.
4. To stop Windows Update from reinstalling the bad driver, go to **Settings > Windows Update > Advanced options > Optional updates** and avoid that driver version, or use the "Show or hide updates" troubleshooter.

### Fix 5: Clean-reinstall the graphics driver

GPU drivers are the single most common Verifier trigger, and a standard reinstall often leaves broken pieces behind.

1. Download Display Driver Uninstaller (DDU) and the latest driver for your GPU from the manufacturer's site ([NVIDIA driver downloads](https://www.nvidia.com/Download/index.aspx) or [AMD driver downloads](https://www.amd.com/en/support/download/drivers.html)).
2. Boot into **Safe Mode** (Settings > System > Recovery > Advanced startup, then Troubleshoot > Startup Settings).
3. Run DDU, choose **Clean and restart** — it fully removes the old driver.
4. After reboot, install the freshly downloaded driver and restart again.

### Fix 6: Remove or update third-party antivirus and VPN software

Filter drivers from security and VPN products trip Verifier more than almost anything else.

1. Go to **Settings > Apps > Installed apps** and uninstall any third-party antivirus or VPN client temporarily.
2. Restart and test for a day. Windows Defender protects you in the meantime.
3. If the crashes stop, reinstall the latest version of that software from the vendor's official site — never from a third-party download mirror.

### Fix 7: Check memory and system file integrity

Rule out hardware and corruption that make good drivers look bad.

1. Press **Win + R**, type `mdsched.exe`, press Enter, and choose **Restart now and check for problems**.
2. After the memory test completes and Windows boots, open an elevated **Command Prompt** (**Win + X > Terminal (Admin)**) and run `sfc /scannow`.
3. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` if SFC reports unfixable damage.

## Closing

Driver Verifier crashes look alarming, but they are actually Windows doing diagnostics out loud — the tool is working as designed, it just should not be running on a daily-use laptop. Turn it off with `verifier /reset`, identify the flagged driver from the minidump, and update or roll back that one driver. In the large majority of cases, that sequence ends the blue screens for good, and your system is left more stable than before Verifier ever got involved.
