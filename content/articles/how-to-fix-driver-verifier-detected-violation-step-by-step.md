---
title: "Driver Verifier Detected Violation: A Step-by-Step Fix"
slug: how-to-fix-driver-verifier-detected-violation-step-by-step
date: 2026-09-14
categories: ["windows-errors"]
tags: ["windows 11", "driver verifier", "bsod"]
description: "Hit DRIVER_VERIFIER_DETECTED_VIOLATION? Learn what Driver Verifier is, why it is crashing your PC, and how to turn it off and fix the bad driver."
thumbnail: "/images/thumbs/how-to-fix-driver-verifier-detected-violation-step-by-step.webp"
faqs:
  - q: "What is Driver Verifier actually for?"
    a: "It is a developer tool built into Windows for stress-testing drivers. Developers enable it to catch bugs in drivers they are writing — illegal memory access, improper IRQL usage, deadlocks. It was never meant to run permanently on a daily-use PC, which is why a forgotten enabled Verifier causes so much grief."
  - q: "Is it safe to just turn Driver Verifier off?"
    a: "Yes, for normal use. Disabling it returns Windows to its default behavior of trusting drivers without the extra stress checks. You lose nothing as an everyday user — Verifier provides no protection or performance benefit outside active driver debugging. Just also update the driver it was flagging, so the underlying bug does not cause ordinary crashes later."
  - q: "The dump names ntoskrnl.exe. Which driver do I fix?"
    a: "ntoskrnl.exe is the Windows kernel itself — it is almost never the real culprit, just the victim that crashed. Look deeper in the WinDbg output for the MODULE_NAME or the stack trace entries above the kernel; the third-party .sys file listed there is your target."
  - q: "Can Driver Verifier damage my hardware?"
    a: "No. It only monitors driver behavior and crashes Windows deliberately when a driver breaks the rules. The crashes are intentional and controlled — annoying, but not harmful to the hardware. The underlying driver bug it caught is the thing worth fixing."
---

DRIVER_VERIFIER_DETECTED_VIOLATION is a special kind of blue screen: it means Windows caught a driver misbehaving because you — or some software — asked it to watch. Driver Verifier is a built-in stress-test tool that monitors drivers for illegal operations. When it catches one, it deliberately crashes the system with this stop code and names the offending driver in the dump.

Most people encountering this never turned Verifier on themselves. Debugging tools, some antivirus products, and certain driver installers enable it silently, and then every boot crashes. The fix has two halves: first stop the crashing by disabling Verifier, then deal with the driver it was complaining about. Do them in that order.

## Why this happens

- **Driver Verifier was left enabled:** the tool is meant for temporary testing. Left on, it keeps stress-testing drivers on every boot until one trips it — which can be a perfectly ordinary driver under artificial stress.
- **A genuinely buggy driver:** Verifier sometimes catches real bugs — a driver writing to memory it does not own or mishandling power states. The crash is doing its job.
- **An outdated driver under a new Windows build:** drivers that passed Verifier on the old build can fail its checks after a Windows update tightens the rules.
- **Third-party software enabled it silently:** some debugging, virtualization, or security tools turn Verifier on during installation and never turn it off.
- **Corrupted driver files:** a half-installed or corrupted driver can fail Verifier checks that the intact version would pass.
- **Overclocking or unstable hardware:** Verifier's stress tests push drivers harder than normal use, so marginal RAM or an unstable overclock can produce violations that look like driver bugs.

## How to fix it

Work through these in order, from the quickest checks to the deeper repairs. Most people are back up and running by Fix 4 or 5.

### Fix 1: Disable Driver Verifier from Safe Mode

First, stop the bleeding. Disabling Verifier stops the deliberate crashes so you can work on the actual driver problem.

1. Boot into Safe Mode: interrupt the boot three times to reach **Automatic Repair**, then **Advanced options > Troubleshoot > Advanced options > Startup Settings > Restart**, press **4**. See [this Safe Mode walkthrough](/articles/how-to-boot-windows-11-in-safe-mode/) if the menu will not appear.
2. Press **Win + R**, type `verifier`, and press Enter to open Driver Verifier Manager.
3. Select **Delete existing settings** and click **Finish**, then restart normally.
4. If the GUI will not open, run `verifier /reset` from an elevated Command Prompt instead — it does the same thing silently.
5. After rebooting, confirm Verifier is off by running `verifier /query` — it should report that no settings are configured.

### Fix 2: Disable Verifier from the recovery command prompt

If Windows will not stay up long enough to reach Safe Mode, disable Verifier offline from recovery.

1. Boot to **Automatic Repair** (three interrupted boots), then **Troubleshoot > Advanced options > Command Prompt**.
2. Type `verifier /reset` and press Enter.
3. For good measure, also run `bcdedit /deletevalue {default} nointegritychecks` in case integrity checks were forced on alongside Verifier.
4. Type `exit`, choose **Continue**, and let Windows boot. The deliberate crashes should be gone.
5. If crashes continue with a different stop code, Verifier was masking a real driver bug — continue with Fix 3.

### Fix 3: Identify the guilty driver from the dump

Verifier names the offender. Reading the dump tells you exactly which driver to update, roll back, or remove.

1. Once booted, open **File Explorer** and go to `C:\Windows\Minidump`. Sort by date and find the dump from the Verifier crash.
2. The quick way to read it: install **WinDbg Preview** from the Microsoft Store, open the dump, and run `!analyze -v` in the command box.
3. Look for the **IMAGE_NAME** or **MODULE_NAME** line — it names the crashing driver file, e.g. `nvlddmkm.sys` (NVIDIA) or `Netwtw10.sys` (Intel Wi-Fi).
4. No WinDbg patience? The free **BlueScreenView** tool lists the crashing driver in a simple table — good enough for this job.
5. Write the driver name down. Fix 4 targets it directly. This same dump-reading approach helps with any stubborn [blue screen](/articles/how-to-fix-blue-screen-of-death-windows-11/).

### Fix 4: Update or roll back the offending driver

With the culprit identified, replace it. Update if it is old, roll back if the trouble started with a recent update.

1. Open **Device Manager** (right-click **Start**), find the device matching the driver name, right-click it, and open **Properties**.
2. If the crashes started after a driver update, use the **Driver** tab's **Roll Back Driver** button.
3. Otherwise click **Update driver > Search automatically**, then check **Settings > Windows Update > Advanced options > Optional updates** for a newer version.
4. For the best results, get it from the source: [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel drivers, the [NVIDIA download page](https://www.nvidia.com/Download/index.aspx) for GeForce, or [AMD's driver page](https://www.amd.com/en/support/download/drivers.html).
5. Restart and use the PC normally for a day. Only re-enable Verifier deliberately if you are actually debugging a driver.

### Fix 5: Remove the software that enabled Verifier

If you never turned Verifier on, find what did — otherwise it may get re-enabled on the next install or update.

1. Think back: did the crashes start after installing a debugging tool, a VPN, virtualization software, or a new antivirus? Those are the usual suspects.
2. Open **Settings > Apps > Installed apps**, sort by install date, and look at what arrived just before the crashes began.
3. Uninstall the suspect, reboot, and run `verifier /query` to confirm Verifier stays off.
4. Check the program's settings for any driver verification or kernel debugging option and leave it disabled if you reinstall.
5. Some motherboard utilities (RGB control, fan tools) also enable it — check those too if the timeline fits.

### Fix 6: Repair system files and check memory

Corrupted system files or bad RAM can make innocent drivers fail Verifier's checks. Rule both out.

1. Open an elevated Command Prompt and run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store.
3. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems** to run Windows Memory Diagnostic.
4. If the memory test reports errors, reseat the RAM sticks (laptops: power off, remove battery if possible, reseat) or test one stick at a time.
5. Unstable RAM under Verifier's stress is a classic false positive — the driver was fine, the hardware was not.

### Fix 7: Reset the driver stack as a last resort

If one bad driver keeps resisting every targeted fix, refresh the whole driver stack rather than fighting it individually.

1. In **Device Manager**, systematically update the chipset, storage controller, network, and graphics drivers from the manufacturer's sources (Fix 4's links).
2. Run **Settings > Windows Update > Advanced options > Optional updates** and install every driver update offered.
3. If the machine still crashes, use **Settings > System > Recovery > Reset this PC > Keep my files** — this reinstalls Windows and all inbox drivers cleanly.
4. After the reset, install drivers one category at a time and test between each, so a returning Verifier crash points straight at the culprit.
5. Document which driver failed — Microsoft's Windows support hub has per-driver troubleshooting if it is a Microsoft-provided one.

## Closing

DRIVER_VERIFIER_DETECTED_VIOLATION looks intimidating, but it is actually Windows handing you the answer: a driver misbehaved under observation. Turn Verifier off to stop the deliberate crashes, read the dump to name the driver, and fix that driver properly. And if you ever intentionally enable Verifier for testing, set a reminder to turn it off — future you will be grateful.
