---
title: "How to Fix KERNEL_SECURITY_CHECK_FAILURE BSOD in Windows 11"
slug: kernel-security-check-failure-bsod-windows-11
date: 2026-09-14
categories: ["windows-errors"]
tags: ["kernel security check failure", "blue screen", "windows 11", "driver", "bsod fix"]
description: "KERNEL_SECURITY_CHECK_FAILURE BSOD on Windows 11? Fix it step by step: update drivers, remove bad software, test RAM, repair Windows."
thumbnail: "/images/thumbs/kernel-security-check-failure-bsod-windows-11.webp"
faqs:
  - q: "What triggers KERNEL_SECURITY_CHECK_FAILURE on Windows 11?"
    a: "A driver corrupting kernel memory — the kernel's integrity checks catch the damage and crash deliberately. On Windows 11 the usual triggers are graphics driver bugs after major updates, antivirus filter drivers, and overclocked RAM. Faulty RAM itself is a less common but real cause."
  - q: "How do I find which driver is causing it?"
    a: "Analyze the minidump at C:\\Windows\\Minidump with WinDbg Preview (free from the Microsoft Store) — !analyze -v names the faulting module. For stubborn cases, Driver Verifier (verifier.exe) stresses third-party drivers until the guilty one crashes with its name attached."
  - q: "Can I fix this without Safe Mode?"
    a: "Often yes, if the crashes are intermittent — update drivers and uninstall suspect software from normal Windows. But if crashes happen at boot or every few minutes, you'll need Safe Mode (via WinRE's Startup Settings) to work without interruption."
  - q: "Does overclocking cause KERNEL_SECURITY_CHECK_FAILURE?"
    a: "Yes — unstable CPU overclocks and especially XMP/EXPO RAM profiles are a documented cause. If crashes happen under load, reset BIOS to optimized defaults and disable XMP as one of your first steps."
---

**KERNEL_SECURITY_CHECK_FAILURE** on Windows 11 means the kernel caught something corrupting its memory and pulled the plug. In plain terms: a driver is misbehaving at the deepest level of the system. This is the practical, step-by-step fix sequence — no dump-analysis degree required, though we'll use the dumps to aim our efforts.

For the full diagnostic methodology (reading dumps, deploying Driver Verifier strategically), see our [troubleshooting guide](/articles/kernel-security-check-failure-troubleshooting/). What follows is the fix order that resolves most cases.

The single most useful thing you can do before touching anything: check whether the crashes correlate with something. Open Reliability Monitor (just search for it in Start) — it shows crashes, driver installs, and Windows updates on one timeline. If every KERNEL_SECURITY_CHECK_FAILURE started the day after a graphics driver update, you've already found your culprit before running a single command.

## Why this happens

- **Buggy graphics driver:** The leading cause on Windows 11, especially after feature updates or major NVIDIA/AMD/Intel driver releases.
- **Antivirus/VPN kernel drivers:** Security and network filter drivers corrupting kernel structures.
- **Corrupted driver installation:** Half-updated or mismatched driver files.
- **Unstable RAM overclock (XMP/EXPO):** Memory pushed past stability, corrupting kernel data under load.
- **Bad RAM:** Faulty modules flipping bits in kernel memory.
- **Corrupted Windows system files:** Damaged kernel components failing their own integrity checks.
- **HVCI/driver conflicts:** Virtualization-based security (Core isolation / Memory integrity) clashing with older drivers that aren't compatible.
- **Stale manufacturer utilities:** Old OEM tools with kernel drivers predating Windows 11's integrity requirements.

## How to fix it

Work through these in order.

### Fix 1: Clean-install the graphics driver

Start with the most likely offender. Don't just update over the old driver — a true clean install with DDU removes the corrupted remnants, registry entries, and conflicting files that a regular update leaves behind. This matters more than people think.

1. Download **DDU (Display Driver Uninstaller)** and the latest graphics driver recommended for your laptop (manufacturer's site first choice).
2. Boot into **Safe Mode**: hold **Shift** while clicking **Restart**, then **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4**.
3. Run DDU, choose **Clean and restart**.
4. Install the fresh graphics driver, restart normally, and test with your usual workload.

### Fix 2: Update chipset, storage, and network drivers

1. From your laptop maker's support site, install the latest **chipset**, **storage controller**, and **Wi-Fi/Ethernet** drivers for your exact model — one at a time, restarting between each.
2. Update the **BIOS/UEFI firmware** as well; firmware updates include fixes for memory-controller and CPU behavior that affect kernel stability.
3. Test for a day of normal use. If the crashes started with a Windows update, see our [kernel security check failure after update guide](/articles/how-to-fix-kernel-security-check-failure-after-windows-11-update/).

### Fix 3: Remove third-party security and utility software

Kernel-mode third-party drivers are the second most common trigger. These drivers run at the same privilege level as the kernel itself, so when they corrupt memory, the kernel's integrity checks catch it — that's literally what this stop code is. Removing them is both a fix and a diagnostic.

1. Uninstall third-party antivirus suites, VPN clients, firewalls, and "PC optimizer"/"driver updater" tools.
2. Restart. Windows Security provides solid protection on its own.
3. If crashes stop, you've found the category — reinstall only what you truly need, one at a time.

### Fix 4: Disable overclocks and XMP

If crashes happen under load (gaming, rendering, video calls):

1. Enter BIOS/UEFI setup and **load optimized defaults**.
2. Specifically disable **XMP/EXPO** memory profiles — run RAM at stock JEDEC speed.
3. Reset any tuning in Intel XTU, Ryzen Master, MSI Afterburner, or manufacturer utilities (OMEN Gaming Hub, Armoury Crate, etc.).
4. Retest under the same load. Stability now = the overclock was the cause.

### Fix 5: Check the minidump for the culprit

If crashes continue, get the evidence. Five minutes with WinDbg often names the exact driver, turning a week of guesswork into a single targeted fix. The learning curve looks steep; the actual procedure is three clicks and one command.

1. Install **WinDbg Preview** from the Microsoft Store.
2. Open the newest `.dmp` from `C:\Windows\Minidump`, run `!analyze -v`.
3. Note the faulting module. If it's the same `.sys` file every time, update, roll back, or uninstall that specific driver.
4. Check **Reliability Monitor** (search Start) for what changed just before crashes began.

### Fix 6: Run Driver Verifier on third-party drivers

The definitive trap for an elusive driver bug.

1. Create a restore point first.
2. **Win + R** > `verifier.exe` > **Create custom settings** > enable **Standard settings** + **Special pool**.
3. **Select driver names from a list** > check non-Microsoft drivers > **Finish** > restart.
4. Use the PC until it crashes — Verifier will name the guilty driver.
5. Boot to Safe Mode, run `verifier /reset` in an admin terminal, then fix the named driver.

### Fix 7: Test the RAM

Software leads exhausted? Verify the hardware. At this point you've eliminated the likely software causes, so a definitive RAM test either confirms the hardware verdict or sends you back to drivers with certainty — both outcomes are progress.

1. **Win + R** > `mdsched.exe` > **Restart now and check for problems**.
2. Then **MemTest86** from a bootable USB — one full pass, zero errors required.
3. Reseat modules before replacing; test sticks individually to isolate.

### Fix 8: Repair Windows with SFC/DISM and in-place upgrade

1. Admin terminal: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Install all pending Windows updates — Microsoft ships kernel fixes in cumulative updates (grab them from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update is broken).
3. Still crashing? Do an in-place upgrade: mount the Windows 11 ISO from the [download page](https://www.microsoft.com/en-us/software-download/windows11), run **setup.exe**, choose **Keep personal files and apps**.

## Closing

On Windows 11, KERNEL_SECURITY_CHECK_FAILURE is a driver problem until proven otherwise — and the proof comes from the fix order above: graphics driver clean install, third-party kernel software removal, overclock reset, then dump analysis and Verifier for the stubborn ones. RAM testing is the backstop, not the starting point. Work it in order and you'll either fix it or have the evidence (a named driver or a failed MemTest86) that tells you exactly what's next. Keep a note of what fixed it — this stop code has a habit of returning after the next big driver update if the underlying habit, like letting Windows Update install GPU drivers or running an overclocked XMP profile, hasn't changed.
