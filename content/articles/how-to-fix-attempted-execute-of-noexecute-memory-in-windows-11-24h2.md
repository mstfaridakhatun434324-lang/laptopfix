---
title: "Attempted Execute of Noexecute Memory on Windows 11 24H2: Fix Guide"
slug: how-to-fix-attempted-execute-of-noexecute-memory-in-windows-11-24h2
date: 2026-09-28
categories: ["windows-errors"]
tags: ["bsod", "noexecute-memory", "windows-11-24h2"]
description: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on Windows 11 24H2? A driver is tripping memory protection. Here's the fix sequence."
thumbnail: "/images/thumbs/how-to-fix-attempted-execute-of-noexecute-memory-in-windows-11-24h2.webp"
faqs:
  - q: "What changed in 24H2 to cause this error?"
    a: "The 24H2 build hardened memory protections (DEP/NX enforcement) and changed kernel memory layout. Drivers with latent bugs — especially older network, audio, and peripheral drivers carried over from 23H2 — can now trip the no-execute protection that previous builds didn't enforce as strictly."
  - q: "Does this mean my RAM is bad?"
    a: "Not necessarily. On 24H2, a driver incompatibility is the more common cause. But because bad RAM corrupts the addresses drivers execute, it produces the identical stop code. Test the RAM if driver updates don't help, or if crashes name different files each time."
  - q: "Can I turn off DEP to stop the crashes?"
    a: "You can, but you shouldn't. Disabling Data Execution Prevention removes a critical security protection against malware, and it only hides the symptom — the buggy driver or bad RAM is still there. Fix the root cause instead; it's usually a single driver update."
  - q: "The crash mentions a specific .sys file. Is that reliable?"
    a: "Very. For this stop code, the named file is the driver that attempted the illegal execution in the large majority of cases. Update or roll back exactly that driver first — it's the fastest fix available for this error."
---
ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY (stop code 0x000000FC) appears more often on Windows 11 24H2 than on earlier builds, and the reason is architectural: 24H2 enforces the CPU's no-execute memory protection more aggressively. Memory regions marked non-executable are meant for data only — when a driver tries to run code from one, the processor blocks it and Windows crashes.

On 24H2, the trigger is usually a driver that was carried over from 23H2 and never updated for the new build's stricter rules. The good news: the crash frequently names the driver, making this one of the more solvable blue screens.

## Why this happens

- **Pre-24H2 drivers tripping stricter enforcement.** Older graphics, network, and audio drivers that worked on 23H2 now hit the hardened no-execute protection.
- **The 24H2 upgrade installed a buggy driver.** The upgrade process pushes driver updates that may themselves contain the bug.
- **Failing RAM.** Bad memory corrupts execution addresses, sending drivers into non-executable regions — identical symptoms, different cause.
- **Corrupted driver files from the upgrade.** The 24H2 installation can damage driver files in the driver store.
- **Malware exploiting execution tricks.** Malicious code running from data regions trips this exact protection — worth ruling out.
- **Unstable memory overclocks.** XMP profiles or manual RAM tuning that isn't fully stable corrupts execution flow, especially under load.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Stop once the crashes stop.

### Fix 1: Capture the driver name from the crash

Don't troubleshoot blind — one filename can save you an hour of guessing.

1. Press **Win + X** and open **Event Viewer**, then go to **Windows Logs > System**.
2. Open the **BugCheck** error from the crash time — the details or the blue screen's **"What failed:"** line usually names the `.sys` file.
3. Note it exactly. On 24H2, common names include older Intel Wi-Fi drivers, Realtek audio drivers, and third-party USB/peripheral drivers.
4. With the name, jump to Fix 3. Without one, continue in order.

### Fix 2: Boot into Safe Mode to stabilize

Break the crash cycle so you can work.

1. Interrupt the boot three times (hold the power button at the logo screen) to reach the **Windows Recovery Environment**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **5** for **Safe Mode with Networking**.
3. If the system is stable here, a third-party driver is confirmed — Safe Mode skips them.

### Fix 3: Update to a 24H2-compatible driver version

The core fix for this build.

1. Press **Win + X** and open **Device Manager**.
2. Find the device matching your suspect driver (**Display adapters**, **Network adapters**, **Sound, video and game controllers**).
3. Right-click and choose **Update driver > Search automatically for drivers**.
4. Better: visit your laptop maker's support site ([Dell](https://www.dell.com/support), HP, Lenovo) and install the latest driver explicitly listed for **Windows 11 24H2** and your exact model.
5. For Intel wireless or Bluetooth, [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) detects and installs 24H2-ready versions.
6. Restart and test. The general [post-update version of this error](/articles/how-to-fix-attempted-execute-of-noexecute-memory-after-windows-11-update/) uses the same approach for other builds.

### Fix 4: Roll back the driver if the update broke it

When the 24H2 upgrade itself installed the bad driver.

1. In **Device Manager**, right-click the suspect device and choose **Properties > Driver tab**.
2. Click **Roll Back Driver** and pick the reason, then confirm.
3. Restart and test stability.
4. Then install the manufacturer's 24H2 driver (Fix 3) rather than leaving the old one indefinitely — rolled-back drivers miss security fixes.

### Fix 5: Scan for malware and repair system files

Rule out the security and corruption angles together.

1. Open **Windows Security > Virus & threat protection > Scan options**, select **Microsoft Defender Offline scan**, and click **Scan now**. Remove anything found.
2. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
3. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart. The [Lenovo-specific guide for this stop code](/articles/how-to-fix-attempted-execute-of-noexecute-memory-on-lenovo-laptop/) covers the same scans with brand-specific driver pointers.

### Fix 6: Test your RAM and memory settings

Essential when crashes are random, happen under load, or name a different file every time — those patterns point away from a single driver and toward memory.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. If errors appear, power off, reseat the RAM sticks firmly, and retest. Replace sticks that consistently fail with matching specs.
3. Enter the BIOS and disable **XMP** or any memory overclock — 24H2's memory layout changes can expose marginal RAM tuning that was perfectly stable on 23H2.
4. For a definitive test, run MemTest86 from a USB drive for two full passes and treat any red error as a failed stick.

### Fix 7: Clean-install 24H2 as the final step

When drivers are current, RAM passes, and it still crashes.

1. Back up everything.
2. Create fresh 24H2 media from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and clean-install, or use **Settings > System > Recovery > Reset PC** with **Remove everything** and **Cloud download**.
3. Install the manufacturer's 24H2 drivers first, verify stability, then restore files.
4. Crashes on a clean install with healthy RAM indicate a CPU or motherboard fault — professional diagnosis is next.

## Closing

On Windows 11 24H2, ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY is the build's stricter memory protection catching drivers that 23H2 let slide. Get the driver name from the crash, install the 24H2-compatible version from your laptop maker, and test your RAM if the crashes are erratic. Don't disable DEP to make it go away — that's trading a fixable driver problem for a real security hole. The fix is methodical, not mysterious: identify, update, verify, and move on with confidence.
