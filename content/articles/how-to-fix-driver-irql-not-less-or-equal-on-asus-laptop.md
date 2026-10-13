---
title: "How to Fix DRIVER_IRQL_NOT_LESS_OR_EQUAL on an ASUS Laptop"
slug: how-to-fix-driver-irql-not-less-or-equal-on-asus-laptop
date: 2026-10-05
categories: ["windows-errors"]
tags: ["driver irql not less or equal", "bsod", "asus laptop", "0xd1", "ndis.sys"]
description: "DRIVER_IRQL_NOT_LESS_OR_EQUAL blue screen on your ASUS laptop? Fix the faulty driver behind stop code 0xD1 with this step-by-step guide."
thumbnail: "/images/thumbs/how-to-fix-driver-irql-not-less-or-equal-on-asus-laptop.webp"
faqs:
  - q: "What does DRIVER_IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "It is stop code 0x000000D1: a driver tried to access memory at an invalid address while running at a high interrupt priority level (IRQL). Drivers at high IRQL may only touch non-paged memory; touching paged-out or invalid memory crashes the system. It is one of the most common driver bug signatures in Windows."
  - q: "Why does the blue screen mention ndis.sys or netio.sys?"
    a: "Those are Windows' own network stack files. They appear on the crash screen because the faulty network adapter driver called into them with bad data — they are the victim, not the culprit. The real offender is usually your Wi-Fi or Ethernet adapter's driver (like rtwlane.sys or Netwtw10.sys), which the minidump will name."
  - q: "Can this error damage my hardware?"
    a: "No. It is a software crash — Windows halting to prevent a driver bug from causing real damage. Your hardware is fine. The urgency is about stability and data loss from unexpected reboots (unsaved work), not about physical harm to the laptop."
  - q: "Why does it only crash during gaming or video calls?"
    a: "Those workloads hammer the network and graphics drivers at high interrupt priority — exactly the conditions where an IRQL bug triggers. A driver that is fine during light browsing can crash under sustained high-throughput load. Load-dependent crashing strongly suggests updating the network and GPU drivers first."
---
DRIVER_IRQL_NOT_LESS_OR_EQUAL (0xD1) is the most classic driver crash in Windows. A driver tried to touch memory it had no business touching while running at elevated interrupt priority, and Windows pulled the plug. On ASUS laptops, nine times out of ten the offender is the network adapter driver — which is why the crash screen so often mentions ndis.sys.

Let's find the actual culprit and fix it properly.

## Why this happens

- **Faulty network adapter driver:** Wi-Fi/Ethernet drivers running at high IRQL with bad memory accesses — the number one cause.
- **Graphics driver bugs:** GPU drivers under gaming or video-call load trigger 0xD1 regularly.
- **Outdated or corrupted driver binaries:** Old drivers, or new ones damaged during install.
- **Third-party antivirus/VPN filter drivers:** These operate at high IRQL and are frequent offenders.
- **USB device drivers:** Faulty USB controller or peripheral drivers, especially with docks and external drives.
- **Overclocking or unstable RAM:** Marginal hardware makes drivers misbehave at high IRQL.
- **Recent Windows update changing driver behavior:** Updates can expose latent bugs in older drivers.

## How to fix it

Work through these in order, starting at Fix 1.

### Fix 1: Read the minidump — name the driver

1. Press **Win + R**, type `%SystemRoot%\Minidump`, press Enter; open the newest `.dmp` in BlueScreenView (free, NirSoft).
2. Look past `ndis.sys`/`ntoskrnl.exe` to the third-party `.sys` file in the stack — that is your culprit.
3. Common ASUS-laptop offenders: `rtwlane.sys`/`rtwlanu.sys` (Realtek Wi-Fi), `Netwtw10.sys` (Intel Wi-Fi), `nvlddmkm.sys` (NVIDIA).

The general Windows 11 version of this crash is covered in our [IRQL_NOT_LESS_OR_EQUAL fix guide](/articles/irql-not-less-or-equal-windows-11-fix/).

### Fix 2: Update the network adapter driver

Since network drivers cause most 0xD1 crashes, start here even if the dump was ambiguous.

1. **Device Manager** (**Win + X > Device Manager**) → **Network adapters**.
2. Right-click your Wi-Fi adapter → **Update driver > Search automatically for drivers**.
3. Then get the vendor-validated version: ASUS's official support downloads for your model, or the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel wireless.
4. Update the Ethernet adapter too if you use wired connections.
5. Restart and test under network load.

### Fix 3: Update the graphics driver cleanly

The second most common offender, especially for gaming crashes.

1. Download the latest driver for your GPU: [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx) or [AMD drivers](https://www.amd.com/en/support/download/drivers.html).
2. For a truly clean install, use Display Driver Uninstaller (DDU) in Safe Mode: run DDU → **Clean and restart** → install the fresh driver.
3. Restart and stress-test with the game or app that used to crash.

### Fix 4: Roll back if the crashes started with an update

1. **Device Manager** → culprit device → **Properties** → **Driver** → **Roll Back Driver**.
2. Or **Settings > Windows Update > Update history > Uninstall updates** for update-triggered cases — our [0xD1 after Windows 11 update guide](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/) covers that path specifically.
3. Restart, verify stability for a few days.

### Fix 5: Remove antivirus/VPN filter drivers temporarily

1. **Settings > Apps > Installed apps** → uninstall third-party antivirus and VPN clients.
2. Restart — Windows Security protects you meanwhile.
3. Test for 24-48 hours under the crashing workload. If stable, the filter driver was guilty; reinstall only the latest vendor version if desired.

### Fix 6: Check USB devices and update chipset drivers

1. Disconnect USB docks, external drives, and hubs — test without them.
2. In **Device Manager**, update **Universal Serial Bus controllers** and **System devices** (chipset).
3. Install the latest ASUS chipset driver package from ASUS's support page for your model.
4. Reconnect USB devices one at a time to identify a faulty peripheral or its driver.

### Fix 7: Test memory and reset overclocks

1. **Win + R** → `mdsched.exe` → **Restart now and check for problems**; check results in Event Viewer under **MemoryDiagnostics-Results**.
2. Return any overclocking, XMP, or Armoury Crate performance profiles to stock.
3. In **Terminal (Admin)**, run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` for completeness.
4. Microsoft's driver-crash reference is on the [Windows support page](https://support.microsoft.com/en-us/windows).

### Fix 8: Use Driver Verifier to force the culprit into the open

When dumps are inconclusive, Verifier makes the buggy driver crash immediately and identifiably instead of intermittently.

1. Press **Win + R**, type `verifier`, and press Enter.
2. Choose **Create standard settings**, then **Select driver names from a list**.
3. Tick only third-party drivers: network adapters, GPU, USB controllers, antivirus/VPN filters. Leave Microsoft drivers alone.
4. Click **Finish** and restart. Use the laptop normally — Verifier stresses the selected drivers, and the violator will blue-screen quickly with its name in the dump.
5. Read the new minidump in BlueScreenView to confirm the driver name, then boot into Safe Mode and run `verifier /reset` to disable Verifier.
6. Never leave Driver Verifier running day-to-day: it slows the system and deliberately crashes on violations. It is a diagnostic instrument, not a setting.

### Fix 9: Update the ASUS BIOS and reset network stack

The final firmware-and-network pass for stubborn 0xD1 crashes.

1. Check your BIOS version with `msinfo32` and compare against ASUS's support downloads for your model — install any update mentioning stability or device compatibility, following ASUS's flashing instructions precisely.
2. Reset the network stack, since network drivers dominate this stop code. In **Terminal (Admin)**, run:
   `netsh winsock reset`
   `netsh int ip reset`
   `ipconfig /flushdns`
3. Restart. These commands clear corrupted network configuration that can make even a good driver misbehave.
4. Reinstall the ASUS wireless driver package fresh after the reset so the driver and the stack start from the same clean state.
5. If crashes continue with a named driver fully updated, current BIOS, and clean network stack, test the RAM with `mdsched.exe` — at this point marginal memory is the most likely remaining explanation, and our [MEMORY_MANAGEMENT guide](/articles/memory-management-bsod-windows-11-fix/) walks through that diagnosis.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL is the bread-and-butter of blue screens: a driver touched memory it should not have, Windows said no. Read the dump, update the network and graphics drivers from proper vendor sources, and clear out old filter drivers — that resolves the overwhelming majority of 0xD1 crashes on ASUS laptops. When the crash only happens under load, treat that as a clue pointing straight at the network or GPU driver, not as a mystery.
