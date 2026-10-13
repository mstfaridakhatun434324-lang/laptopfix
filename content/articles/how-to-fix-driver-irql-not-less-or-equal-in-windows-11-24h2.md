---
title: "DRIVER_IRQL_NOT_LESS_OR_EQUAL in Windows 11 24H2: 7 Proven Fixes"
slug: how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2
date: 2026-09-22
categories: ["windows-errors"]
tags: ["windows-11", "bsod", "driver-irql"]
description: "DRIVER_IRQL_NOT_LESS_OR_EQUAL crashing Windows 11 24H2? A driver touched memory it should not have. Find it and fix it with these 7 steps."
thumbnail: "/images/thumbs/how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2.webp"
faqs:
  - q: "What does DRIVER_IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "A driver tried to access a memory address at an incorrect interrupt request level (IRQL) — essentially, it reached for memory it had no business touching at that moment. Windows treats this as a serious violation and crashes immediately. The cause is almost always a buggy, outdated, or corrupted device driver, most commonly network, graphics, or storage drivers."
  - q: "The blue screen names a file like ndis.sys or nvlddmkm.sys. What now?"
    a: "That file is the prime suspect. Ndis.sys points to the network stack (update your Wi-Fi/Ethernet driver), nvlddmkm.sys is NVIDIA graphics (clean-reinstall it), and storport.sys or stornvme.sys point at storage drivers. Update or clean-reinstall the driver that owns the named file first — targeted fixes beat updating everything blindly."
  - q: "Can bad RAM cause DRIVER_IRQL_NOT_LESS_OR_EQUAL?"
    a: "Yes. Faulty memory corrupts the addresses drivers work with, producing this exact stop code with no driver visibly at fault. If driver updates do not help, run Windows Memory Diagnostic (mdsched.exe). I have seen plenty of these cases resolve with a RAM reseat or replacement after the driver trail went cold."
  - q: "Can my Wi-Fi driver really cause DRIVER_IRQL_NOT_LESS_OR_EQUAL?"
    a: "Absolutely — network drivers are among the most common triggers, and the dump usually names ndis.sys or your adapter's driver file. Update the Wi-Fi driver from your laptop maker's support page, not from Windows Update. If the crashes persist, try an older driver version from the maker's archive, since brand-new network drivers sometimes ship with bugs on 24H2."
---

DRIVER_IRQL_NOT_LESS_OR_EQUAL is one of the most common blue screens on Windows 11 24H2, and its translation is simple: a driver tried to access memory improperly, and Windows pulled the plug. The name is jargon; the fix is familiar — find the bad driver, fix the bad driver, and check the memory if drivers do not explain it.

Here is the full sequence.

## Why this happens

- **A buggy network driver.** The number one cause on 24H2 — Wi-Fi and Ethernet drivers (Intel, Realtek, Killer) mishandling memory at the wrong IRQL.
- **A corrupted graphics driver.** NVIDIA, Intel, and AMD GPU drivers are the next most common names in these dumps.
- **Outdated storage drivers.** NVMe and AHCI drivers that predate 24H2's kernel changes.
- **Faulty RAM.** Bad memory corrupts addresses, making innocent drivers look guilty.
- **Overclocking or unstable XMP.** Pushing hardware past stable limits corrupts in-flight memory operations.
- **Corrupted driver files.** Partial updates leave mismatched binaries that misbehave at the kernel level.
- **Third-party antivirus filter drivers.** Kernel-level security hooks operating at elevated IRQL are frequent offenders.

## How to fix it

Work through these in order. Boot into Safe Mode if crashes prevent normal operation.

### Fix 1: Read the blue screen and identify the driver

The crash usually hands you the answer — capture it.

1. The next time it blue-screens, look for a file name under the stop code and photograph it.
2. Quick decoder: `ndis.sys` / `Netwtw10.sys` = network, `nvlddmkm.sys` = NVIDIA graphics, `igdkmdnd64.sys` = Intel graphics, `rtkvhd64.sys` = Realtek audio, `storport.sys` = storage.
3. Boot into Safe Mode (**Shift** + **Restart** → **Troubleshoot** → **Advanced options** → **Startup Settings** → **Restart** → **4**) to work safely.
4. If no file was shown, start with the network driver — it is the most common offender on 24H2.

### Fix 2: Update or clean-reinstall the network driver

Since network drivers lead the statistics, start here.

1. In **Device Manager** (**Win + X** → **Device Manager**), expand **Network adapters**.
2. Right-click your Wi-Fi adapter → **Uninstall device**, checking **Attempt to remove the driver for this device** for a truly clean removal.
3. Restart — Windows installs a basic driver. Then install the latest driver from your laptop manufacturer's support site (or Intel/Realtek/Killer directly).
4. Do the same for the Ethernet adapter if you have one.
5. Test with heavy network activity (large downloads, video calls) — IRQL bugs often surface under network load.

### Fix 3: Clean-reinstall the graphics driver

The second most common culprit deserves the full DDU treatment.

1. Download Display Driver Uninstaller and the latest GPU driver.
2. Disconnect from the internet, boot into Safe Mode, run DDU → **Clean and restart**.
3. Install the fresh driver — from the [NVIDIA download page](https://www.nvidia.com/Download/index.aspx), the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), or AMD's driver site as appropriate.
4. Reconnect, restart, and test with the workload that crashed.

### Fix 4: Run Windows Memory Diagnostic

When drivers do not explain it, test the memory — this stop code is a classic RAM symptom.

1. Press **Win + R**, type `mdsched.exe`, press **Enter** → **Restart now and check for problems**.
2. Let the test complete. Errors mean bad RAM: reseat the modules, test sticks individually, replace the faulty one.
3. Also enter the BIOS and disable XMP/EXPO or any overclocking — unstable memory timings cause IRQL violations even on healthy RAM.
4. Retest the crashing workload after any memory change.

### Fix 5: Update chipset and storage drivers

Complete the driver stack so no outdated driver remains.

1. Install the latest **chipset** driver from your laptop manufacturer's support site, then the **storage/AHCI/NVMe** driver, restarting between each. Chipset drivers govern how every other driver talks to the hardware, so an outdated chipset package can make innocent drivers throw IRQL errors.
2. In **Device Manager**, verify no yellow warnings under **Storage controllers**, **IDE ATA/ATAPI controllers**, or **System devices**.
3. If a specific device shows a warning, right-click → **Properties** → **Events** tab to see its driver history — a recent automatic driver update listed there is a strong hint about what changed.
4. Microsoft's [Windows support documentation](https://support.microsoft.com/en-us/windows) covers the built-in driver update and rollback tools if you need the official walkthrough.

### Fix 6: Run SFC, DISM, and chkdsk

Repair the system files and disk underneath the drivers.

1. In **Terminal (Admin)**: `sfc /scannow` → `DISM /Online /Cleanup-Image /RestoreHealth` → `sfc /scannow` again.
2. Run `chkdsk C: /f` (type `Y`, restart, let it run).
3. If SFC reports corruption it could not fix even after DISM, note which files — that points at deeper damage addressed by Fix 7.

### Fix 7: Uninstall the triggering update or do an in-place repair

If the crashes started with a specific 24H2 update, act on that.

1. Go to **Settings** → **Windows Update** → **Update history** → **Uninstall updates** → remove the most recent cumulative update → restart and test for 48 hours.
2. If stable, pause updates for a week or two while the driver vendor catches up.
3. If crashes persist regardless, do an in-place repair: run Windows 11 setup → **Upgrade this PC now** → **Keep personal files and apps**.
4. After the repair, install manufacturer drivers before Windows Update, keeping the validated driver set in place.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL on 24H2 is a driver detective case where the blue screen usually names the suspect — read the `.sys` file, clean-reinstall that driver, and test the RAM if the trail goes cold. The network driver deserves first attention on this build; it causes more of these crashes than any other single component. Work the list in order, give each fix a day of real use before moving on, and you will find it — these crashes always have a cause, and it is almost always fixable without new hardware. For the earlier-build variant, see [DRIVER_IRQL_NOT_LESS_OR_EQUAL after a Windows 11 update](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/); for the general guide, [IRQL_NOT_LESS_OR_EQUAL on Windows 11](/articles/irql-not-less-or-equal-windows-11-fix/).
