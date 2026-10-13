---
title: "How to Fix the 'Your PC Ran Into a Problem' Error on an ASUS Laptop"
slug: how-to-fix-your-pc-ran-into-a-problem-on-asus-laptop
date: 2026-09-21
categories: ["windows-errors"]
tags: ["your-pc-ran-into-a-problem", "asus", "blue-screen"]
description: "Stuck in the 'Your PC ran into a problem' loop on your ASUS laptop? Diagnose the stop code and repair startup with these proven steps."
thumbnail: "/images/thumbs/how-to-fix-your-pc-ran-into-a-problem-on-asus-laptop.webp"
faqs:
  - q: "What does 'Your PC ran into a problem and needs to restart' actually mean?"
    a: "It's Windows' generic crash screen — the blue screen of death with friendly wording. The important detail is the stop code printed near the bottom (like MEMORY_MANAGEMENT or DRIVER_IRQL_NOT_LESS_OR_EQUAL), which tells you what actually failed. Always note that code before the laptop restarts; it determines which fix applies."
  - q: "Why does my ASUS laptop show this screen on every boot?"
    a: "A crash loop at boot means something in the startup path is broken: a bad driver loading early, corrupted boot records, or failing hardware. ASUS laptops commonly hit this after Armoury Crate or BIOS updates. Boot into Safe Mode or WinRE to break the loop, then work through driver and boot repairs."
  - q: "Can I lose files from this error?"
    a: "The crash itself doesn't delete files, and the repair steps here are non-destructive. Files are only at risk if the underlying cause is a dying drive — which is why checking disk health is part of the process. If you can reach WinRE, you can copy important files to USB before attempting riskier fixes."
  - q: "How do I stop the automatic restart loop to read the error?"
    a: "From WinRE, go to Troubleshoot > Advanced options > Startup Settings > Restart, then press 9 or F9 to disable automatic restart after failure. Windows will then halt on the blue screen instead of rebooting, giving you time to photograph the stop code and any named driver file."
---
"Your PC ran into a problem and needs to restart" is the message nobody wants to see twice — let alone on every boot. This is the modern blue screen, and on ASUS laptops it most often appears after a driver update, an Armoury Crate change, or a Windows feature update that didn't land cleanly. The screen usually shows a stop code near the bottom; that code is your biggest clue.

Don't panic, and don't reach for the reset button yet. Most of these crashes are fixed with driver repairs and boot fixes that leave your files alone. Work through the steps below in order. For the Dell-side version of this exact screen, see [Your PC Ran Into a Problem on Dell](/articles/how-to-fix-your-pc-ran-into-a-problem-on-dell-laptop/), and if the loop started after an update, [the after-update variant](/articles/how-to-fix-your-pc-ran-into-a-problem-after-windows-11-update/) is the better starting point.

## Why this happens

- **A faulty driver.** Graphics, chipset, and network drivers are the top triggers — a bad one crashes Windows during normal use or at boot.
- **Corrupted system files.** Interrupted updates leave Windows components half-written, causing crashes under load or at startup.
- **Failing RAM or SSD.** Hardware faults produce crashes that move between different stop codes, which is the telltale sign.
- **ASUS software conflicts.** Armoury Crate, MyASUS background services, and the bundled antivirus trial occasionally clash with new Windows builds.
- **Overheating.** A dust-clogged ASUS cooling system can crash the laptop under load, mimicking driver errors.
- **Recent Windows update.** Feature updates replace dozens of drivers at once; one bad replacement starts the crashing.

## How to fix it

Work through these in order. Start by capturing the stop code — it focuses everything that follows.

### Fix 1: Capture the stop code and disable auto-restart

You can't fix what you can't identify, so make the error stay on screen.

1. If Windows boots at all, press **Win + R**, type `sysdm.cpl`, and press **Enter**.
2. Go to the **Advanced** tab, click **Settings** under **Startup and Recovery**.
3. Uncheck **Automatically restart** and click **OK**.
4. If you can't boot, force WinRE (interrupt the boot twice at the ASUS logo), go to **Troubleshoot > Advanced options > Startup Settings > Restart**, and press **9** to disable automatic restart after failure.
5. The next crash will hold on the blue screen — photograph the stop code and any driver filename shown.

### Fix 2: Boot into Safe Mode

Safe Mode loads only essential drivers, which usually breaks the crash loop.

1. From WinRE go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
2. Press **4** for Safe Mode, or **5** for Safe Mode with Networking if you need internet access.
3. If the laptop runs stably in Safe Mode, the problem is almost certainly a third-party driver or startup program — the next fixes target exactly those.
4. If it crashes even in Safe Mode, skip to the hardware and system-file checks (Fixes 5–7).

### Fix 3: Roll back or update the suspect driver

In Safe Mode, deal with the driver the stop code implicates.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Check **Display adapters**, **Network adapters**, and **System devices** for yellow warning icons.
3. Right-click any suspect, open **Properties**, and on the **Driver** tab click **Roll Back Driver** if available.
4. If rollback isn't available, choose **Update driver > Search automatically for drivers**, or download the latest from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html).
5. Restart normally and test.

### Fix 4: Uninstall conflicting ASUS utilities temporarily

If crashes started after an Armoury Crate or MyASUS update, isolate it.

1. In Safe Mode, open **Settings > Apps > Installed apps**.
2. Uninstall **Armoury Crate** (and its associated services like Armoury Crate Service) temporarily — you can reinstall later from the Microsoft Store.
3. Also consider removing the bundled antivirus trial; Windows Defender activates automatically.
4. Restart normally. If crashes stop, reinstall Armoury Crate fresh from the Store rather than restoring the old install.

### Fix 5: Repair system files with SFC and DISM

Fix Windows components damaged by the interrupted update or crash.

1. Open an admin **Terminal** (right-click **Start > Terminal (Admin)**) — in Safe Mode if necessary.
2. Run: `sfc /scannow`
3. Then run: `DISM /Online /Cleanup-Image /RestoreHealth`
4. Restart and use the laptop normally for a while to confirm stability.

### Fix 6: Test RAM and disk health

Rule out the hardware causes that produce wandering stop codes.

1. Press **Win + R**, type `mdsched.exe`, press **Enter**, and choose **Restart now and check for problems**.
2. For the disk, open an admin **Terminal** and run `chkdsk C: /f` (schedule it if prompted, then restart).
3. If memory errors appear, reseat or replace the RAM. Our full walkthrough for [running the Memory Diagnostic tool in Windows 11 24H2](/articles/how-to-run-memory-diagnostic-tool-in-windows-11-24h2/) covers extended testing.
4. If the SSD reports SMART warnings, back up immediately — a failing drive explains everything.

### Fix 7: Check temperatures and clean the cooling system

Overheating crashes often masquerade as driver errors on gaming-oriented ASUS laptops.

1. Install a monitoring tool like HWMonitor and watch CPU/GPU temperatures under load — sustained readings above 95°C are a red flag.
2. With the laptop off and unplugged, blow compressed air through the rear vents to clear dust.
3. Make sure the laptop sits on a hard flat surface, not bedding or a couch that blocks intakes.
4. If temperatures stay high after cleaning, the thermal paste may need replacement — a repair shop job on most models.

### Fix 8: System Restore or Reset as the final step

When drivers, files, and hardware all check out, restore Windows itself.

1. From WinRE go to **Troubleshoot > Advanced options > System Restore** and pick a point from before the crashes.
2. With no restore point, use **Troubleshoot > Reset this PC > Keep my files**.
3. Microsoft's official recovery documentation covers these options in detail.

## Closing

The "Your PC ran into a problem" screen is scary but highly fixable: capture the stop code, get into Safe Mode, and deal with the driver or software that started the trouble. Most ASUS cases end at Fix 3 or Fix 4. If the stop codes keep changing between crashes, think hardware — run the memory and disk checks before anything else, because no driver update fixes a dying stick of RAM.
