---
title: "Fix ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on an ASUS Laptop"
slug: how-to-fix-attempted-execute-of-noexecute-memory-on-asus-laptop
date: 2026-09-14
categories: ["windows-errors"]
tags: ["bsod", "stop code 0xfc", "asus", "myasus"]
description: "Fix ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on your ASUS laptop — MyASUS driver updates, dump analysis, and memory testing."
thumbnail: "/images/thumbs/how-to-fix-attempted-execute-of-noexecute-memory-on-asus-laptop.webp"
faqs:
  - q: "What does this stop code mean on an ASUS laptop?"
    a: "Stop code 0x000000FC means a driver tried to execute code from memory marked non-executable. On ASUS laptops the typical causes are outdated graphics/chipset drivers, Armoury Crate or MyASUS component drivers misbehaving, a Windows update swapping in a generic driver, or faulty RAM."
  - q: "Should I use MyASUS or Armoury Crate to update drivers?"
    a: "MyASUS is the right tool for drivers and BIOS updates — it's ASUS's validated channel. Armoury Crate is for performance profiles and RGB; its updates are less critical for stability. For this blue screen, update via MyASUS first, and treat Armoury Crate's driver offers as secondary."
  - q: "My ASUS is a ROG gaming laptop. Anything different?"
    a: "Yes: disable overclocking profiles in Armoury Crate early in your troubleshooting, check thermals (gaming ASUS laptops run hot and heat causes memory errors), and prioritize the NVIDIA/AMD graphics driver — it's the prime suspect on ROG and TUF models."
  - q: "How do I stop Windows Update from replacing my ASUS drivers?"
    a: "After installing ASUS's drivers, open Device Installation Settings (search it in Start) and choose 'No' to block automatic driver updates, or use the show/hide updates troubleshooter to hide the specific bad driver version. Keep Windows security updates flowing — only block the driver swaps."
---
ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY (0x000000FC) on your ASUS means a driver tried to run code from a memory region Windows had fenced off as data-only. Windows treats that as a possible exploit attempt and pulls the plug. On ASUS machines — especially ROG and TUF gaming laptops — the script is familiar: a graphics or chipset driver misbehaving, sometimes with Armoury Crate's tuning profiles or heat as accomplices.

ASUS gives you MyASUS as the validated driver channel, which simplifies the fix considerably. This guide follows the technician's order: test RAM, identify the driver from the dump, replace it via ASUS's channels, and clean up the damage.

## Why this happens

- **A buggy graphics or chipset driver.** The top cause across all ASUS lines, gaming models especially.
- **Armoury Crate overclocking profiles.** Unstable CPU/GPU/memory tuning corrupts memory bookkeeping and triggers this exact stop code.
- **Windows Update replacing ASUS-validated drivers.** Generic drivers that haven't been tested on your ASUS hardware.
- **MyASUS/Armoury Crate component drivers.** The background services install kernel drivers; outdated versions misbehave.
- **Faulty RAM.** Less common than drivers, but bad cells produce identical symptoms.
- **Overheating.** Thermal memory errors on thin ASUS gaming laptops under sustained load.

## How to fix it

Work through these in order. Don't skip the RAM test — it's fast and rules out hardware.

### Fix 1: Disable Armoury Crate tuning profiles

On ROG/TUF models, do this first — it's a two-minute test.

1. Open **Armoury Crate** and set the operating mode to **Silent** or **Windows** (not Turbo/Performance with manual tuning).
2. Go to any **manual overclocking** or **GPU tuning** sections and reset everything to default.
3. Reboot and test under normal load. If crashes stop, your tuning profile was unstable — the "stable" overclock wasn't.
4. Non-gaming ASUS (VivoBook, ZenBook): skip to Fix 2, but keep thermals in mind for Fix 5.

### Fix 2: Test the RAM

Rule out hardware before the driver hunt.

1. **Win + R** > `mdsched.exe` > **Restart now and check for problems** > **F1** > **Extended** > two passes.
2. Errors? Power off, unplug, open the bottom panel (screws vary by model — check your manual), reseat the sticks, retest.
3. Persistent errors on a soldered-RAM ZenBook mean a warranty claim — document the error codes from the test.
4. Clean result? The driver hunt begins. RAM faults also feature in the [memory management BSOD guide](/articles/memory-management-bsod-windows-11-fix/) if you want a second testing method.

### Fix 3: Identify the driver from the minidump

Get the name; don't guess.

1. Open `C:\Windows\Minidump`, install **WinDbg Preview** from the Microsoft Store.
2. Load the newest dump, run `!analyze -v`, read **IMAGE_NAME**.
3. Common ASUS results: `nvlddmkm.sys` (NVIDIA), `amdkmdag.sys` (AMD), `igdkmd64.sys` (Intel), `AsusWmiAcpi.sys` or similar ASUS WMI drivers.
4. Our [WinDbg guide](/articles/best-way-to-read-dump-files-with-windbg/) walks through the analysis if you haven't done it before.

### Fix 4: Update via MyASUS

ASUS's validated driver channel — use it before anything else.

1. Open **MyASUS** > **Customer Support** > **LiveUpdate** and install all recommended **BIOS**, **chipset**, **graphics**, and **driver** updates.
2. BIOS updates: charger plugged in, close everything, don't interrupt the flash.
3. Reboot between major updates and test. MyASUS drivers are validated against your exact model's firmware, which is why they beat Windows Update's generic versions.
4. For anything MyASUS misses, ASUS's support site by exact model number is the fallback.

### Fix 5: Clean-replace the graphics driver

When the dump names the GPU driver, do the full clean replacement.

1. Boot to Safe Mode with Networking (interrupt boot 3x > **Automatic Repair** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > **5**).
2. Run **Display Driver Uninstaller (DDU)** from Wagnardsoft's official site: select GPU brand > **Clean and restart**.
3. Install the graphics driver from MyASUS (preferred) or the vendor: [NVIDIA](https://www.nvidia.com/Download/index.aspx) **Custom** > **Perform a clean installation**, or [AMD](https://www.amd.com/en/support/download/drivers.html) with **Factory Reset**.
4. Test with the crashing workload: gaming, video, external monitor, sleep/wake cycles.

### Fix 6: Check thermals

Heat-induced memory errors are the great impersonator on gaming ASUS laptops.

1. Monitor with **HWiNFO** during load. Sustained CPU/GPU temps above 95°C need attention.
2. Blow compressed air through the vents, elevate the rear, and try a cooling pad.
3. In Armoury Crate, create a manual fan curve that's aggressive earlier — prevention beats throttling.
4. If max fans stop the crashes, thermals were the cause. Consider a repaste at a service center for older machines.

### Fix 7: Repair system files and scan for malware

Cover the remaining bases.

1. In **Terminal (Admin)**: `sfc /scannow`, `DISM /Online /Cleanup-Image /RestoreHealth`, `sfc /scannow` again.
2. **Windows Security** > **Virus & threat protection** > **Scan options** > **Microsoft Defender Offline scan** > **Scan now** — this stop code exists partly to catch injected code, so rule it out.
3. Microsoft documents these tools on [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 8: Clean-boot to isolate software conflicts

When crashes only happen in normal use, bisect the software stack.

1. **Win + R** > `msconfig` > **Services** tab > tick **Hide all Microsoft services** > **Disable all**.
2. **Task Manager** > **Startup apps** > disable everything, including Armoury Crate and MyASUS entries. Reboot.
3. Stable in clean boot? Re-enable services in halves until crashes return — the last batch holds the culprit.
4. Frequent winners on ASUS machines: RGB control software, game overlays (Discord, GeForce Experience), old VPN clients, and "system optimizer" utilities. Update the offender or remove it — software that corrupts kernel memory doesn't deserve a second chance.

## Closing

On an ASUS, ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY follows a predictable path: calm Armoury Crate's tuning down, test the RAM, read the dump, and let MyASUS deliver the validated drivers. Gaming models add the thermal check — heat lies convincingly as a driver bug. Work the list in order and you'll find the one component that was spoiling the party, with the dump file to prove it. And once it's stable, keep MyASUS updating drivers on its schedule rather than letting Windows Update freelance — that's what keeps this particular blue screen from making a return appearance.
