---
title: "Display Adapter Missing on Windows 11? Get Your GPU Back"
slug: how-to-fix-display-adapter-missing-on-windows-11
date: 2026-09-27
categories: ["drivers"]
tags: ["display adapter", "gpu", "device manager", "windows 11", "drivers"]
description: "GPU missing from Device Manager on Windows 11? Restore a missing display adapter with driver, BIOS, and hardware checks — step by step."
thumbnail: "/images/thumbs/how-to-fix-display-adapter-missing-on-windows-11.webp"
faqs:
  - q: "Why did my graphics card disappear from Device Manager?"
    a: "The GPU usually disappears because its driver failed to load — after a bad driver update, a Windows update conflict, or driver corruption. Less commonly, the GPU is disabled in BIOS, the card isn't seated properly, or the hardware has failed. If the screen still works through integrated graphics, the discrete GPU's driver binding is the prime suspect."
  - q: "How do I know if my GPU is dead or just a driver problem?"
    a: "Check BIOS first: if the GPU appears in BIOS or the boot screen, the hardware is alive and it's a Windows driver issue. Try the GPU in another machine or check whether it appears with hidden devices shown. A GPU invisible in BIOS, with fans not spinning and no detection anywhere, points at hardware failure."
  - q: "Can Windows Update remove my display adapter?"
    a: "It can effectively do so by installing an incompatible driver or corrupting the existing one during the update process. This is especially common with major Windows 11 feature updates. Rolling back the driver or reinstalling the vendor driver usually restores the adapter immediately."
  - q: "Why does only Microsoft Basic Display Adapter show up?"
    a: "That means Windows sees display hardware but couldn't load the proper GPU driver, so it fell back to the generic basic driver. The GPU is present — it just needs its real driver. Install the vendor driver for your exact GPU model and the proper adapter entry will replace the basic one."
---

Opening Device Manager to find your graphics card simply gone is alarming — especially when the "Display adapters" section shows only "Microsoft Basic Display Adapter" or nothing at all. Games won't launch, external monitors misbehave, and everything feels sluggish. But a missing display adapter is usually a driver problem, not a dead GPU, and the distinction matters because one is a twenty-minute fix and the other is a repair bill.

Windows loads the GPU driver at boot; if that load fails — corrupt driver, bad update, conflict — Windows may show nothing at all rather than an error. The recovery path is methodical: confirm the hardware exists, clear the broken driver state, and reinstall cleanly. Here's the order that works.

## Why this happens

- **Corrupt GPU driver:** the driver files are damaged and fail to load at boot.
- **Bad driver update:** a new version is incompatible or installed incompletely.
- **Windows update conflict:** a feature update broke the driver binding.
- **GPU disabled in BIOS:** integrated/discrete graphics settings hide the adapter.
- **Driver signature issue:** Windows refused to load an unsigned or tampered driver.
- **Hardware not seated:** the GPU lost proper PCIe contact (desktops, some laptops).
- **Failed GPU hardware:** the card itself died — least common but possible.
- **Display driver cleanup gone wrong:** DDU or a utility removed too much.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Show hidden devices and scan for hardware

1. Open Device Manager and click **View > Show hidden devices** — the GPU often sits there grayed out.
2. Click **Action > Scan for hardware changes** to force re-enumeration.
3. If the GPU appears (even grayed), right-click it, check Properties > General for the error code, then **Enable device** or **Uninstall device** followed by a rescan.
4. Error Code 43 means Windows stopped the device for reporting problems — continue to the driver fixes.
5. If nothing appears even as hidden, the driver state is thoroughly broken or the hardware isn't detected — keep going.

### Fix 2: Check BIOS for the GPU

1. Restart and enter BIOS/UEFI setup.
2. Look for graphics settings — often under **Advanced** — controlling integrated vs. discrete GPU, or "dGPU" enable/disable.
3. Ensure the discrete GPU is **Enabled**, not forced to integrated-only mode.
4. On desktops, confirm the primary display output is set to PCIe/PEG rather than iGPU.
5. Check whether BIOS itself lists the GPU in its hardware information — visible in BIOS means the hardware is alive.
6. Save and boot to Windows, then recheck Device Manager.

### Fix 3: Clean-reinstall the GPU driver

1. Download the correct driver for your exact GPU: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or Intel via the [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. Boot into Safe Mode and run Display Driver Uninstaller (DDU) to remove all GPU driver remnants.
3. Reboot normally and install the downloaded driver with the clean-install option.
4. Check Device Manager — the proper adapter name should now appear under Display adapters.
5. If the installer says no compatible hardware found, that's significant: it suggests Windows truly can't see the GPU (hardware or BIOS level).

### Fix 4: Roll back a bad update

1. If the adapter vanished right after a driver or Windows update, roll back: Device Manager > Display adapters > (hidden GPU) > Properties > Driver > **Roll Back Driver**.
2. For Windows updates: **Settings > Windows Update > Update history > Uninstall updates**, and remove the suspect update.
3. After rollback, pause driver updates temporarily so Windows doesn't immediately reinstall the bad version.
4. Report the bad driver to the vendor — TDR-style timeouts after updates are covered in [fixing display driver crashes](/articles/best-way-to-fix-display-driver-stopped-responding/) if the GPU appears but keeps resetting.

### Fix 5: Check driver signature and Windows integrity

1. Unsigned or modified drivers get blocked: run `sigverif` to check for unsigned system drivers.
2. If you disabled driver signature enforcement for some other install, re-enable it — a half-disabled state causes bizarre detection failures.
3. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an admin Command Prompt to repair system driver infrastructure.
4. Corrupted system files can prevent *any* GPU driver from loading, mimicking a missing adapter.
5. Reboot after repairs and recheck Device Manager.

### Fix 6: Reseat the hardware (desktops and serviceable laptops)

1. Power off completely, unplug, and (on desktops) open the case.
2. Remove the GPU and reseat it firmly in the PCIe slot until the latch clicks.
3. Reconnect all PCIe power cables — they must click fully into place.
4. Check for dust in the slot and on the card's contacts; clean gently with compressed air.
5. On laptops with removable GPUs (rare, mostly older models), reseating is a service-center job — don't force it.
6. If the GPU has power LEDs or spinning fans, note whether they activate — dead fans plus no detection means hardware failure.

### Fix 7: Test to confirm hardware vs. software

1. Boot from a Linux live USB — if the GPU shows up there (`lspci`), the hardware is fine and Windows is the problem.
2. On desktops, test the GPU in another PCIe slot or another machine if available.
3. Check warranty status before concluding hardware failure — GPU death is usually covered.
4. If the GPU is detected but unstable rather than missing, the [unknown device in Device Manager](/articles/best-way-to-fix-unknown-device-in-device-manager/) guide covers the halfway-detected case.
5. Document every test result; warranty claims go much faster with a clear diagnostic trail.

## Closing

A missing display adapter is frightening but fixable in most cases — the GPU is usually sitting there waiting for a driver that loads correctly. The critical fork in this guide is Fix 2's BIOS check: hardware visible in BIOS means a Windows/driver problem you can solve; invisible everywhere means hardware. Don't skip straight to "my GPU died" without the driver cleanup steps, because clean-reinstalling the driver resurrects more "dead" GPUs than any other single action. Work the list, and you'll know exactly which one you're dealing with.
