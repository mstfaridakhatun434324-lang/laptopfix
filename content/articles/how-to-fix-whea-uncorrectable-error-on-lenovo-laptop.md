---
title: "How to Fix the WHEA Uncorrectable Error on a Lenovo Laptop"
slug: how-to-fix-whea-uncorrectable-error-on-lenovo-laptop
date: 2026-10-03
categories: ["windows-errors"]
tags: ["whea-uncorrectable-error", "lenovo", "hardware-error"]
description: "WHEA Uncorrectable Error on your Lenovo laptop? Diagnose the hardware fault — CPU, RAM, SSD, or thermals — and fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-whea-uncorrectable-error-on-lenovo-laptop.webp"
faqs:
  - q: "What does WHEA Uncorrectable Error mean?"
    a: "WHEA is the Windows Hardware Error Architecture — the system Windows uses to report hardware faults. 'Uncorrectable' means the hardware reported an error that couldn't be fixed automatically: typically a CPU, RAM, SSD, or PCIe bus fault. Unlike most blue screens, this one points at hardware first, software second."
  - q: "Is WHEA Uncorrectable Error always a hardware failure?"
    a: "Not always, but usually. Overclocking, unstable undervolting, outdated BIOS, and overheating can all trigger WHEA errors on healthy hardware. Rule those out first — they're free to fix. If the error persists at stock settings with current BIOS and good thermals, suspect a genuine hardware fault."
  - q: "Can a Windows update cause WHEA Uncorrectable Error?"
    a: "Indirectly. Updates can install drivers that stress hardware differently, and BIOS updates change hardware behavior. But an update doesn't damage hardware — if WHEA errors start after an update, it's usually exposing a marginal component (often RAM or thermals) rather than causing the fault."
  - q: "Should I keep using the laptop if I get this error occasionally?"
    a: "Back up your data immediately, then diagnose. Occasional WHEA errors can precede total component failure — especially SSD or RAM faults. Don't ignore it: run the diagnostics in this guide, and if hardware fails, replace the component before it takes your data with it."
---
WHEA Uncorrectable Error (0x124) is the blue screen that means business: Windows' hardware error reporting caught a fault in the CPU, memory, storage, or bus that couldn't be corrected automatically. On Lenovo laptops — ThinkPads, Legions, and IdeaPads alike — this error demands a hardware-first mindset, though overclocking, thermals, and BIOS issues can trigger it on perfectly healthy components.

The strategy: eliminate the fixable causes (overclocks, heat, BIOS, drivers), then test each hardware component until the faulty one confesses. For the general Windows 11 version see [WHEA Uncorrectable Error in Windows 11 24H2](/articles/how-to-fix-whea-uncorrectable-error-in-windows-11-24h2/), and for post-update cases [the after-update variant](/articles/how-to-fix-whea-uncorrectable-error-after-windows-11-update/).

## Why this happens

- **Failing CPU, RAM, or SSD.** The classic cause — a component developing faults under load or heat.
- **Overheating.** Thermal stress causes transient hardware errors that WHEA reports as uncorrectable.
- **Overclocking or unstable undervolt.** Pushing components past stable limits generates hardware errors.
- **Outdated BIOS.** Firmware bugs in power management or memory training cause false or real hardware errors.
- **Loose or corroded connections.** Poorly seated RAM or SSD on models with accessible components.
- **Failing power delivery.** An aging battery or charger causing voltage instability under load.

## How to fix it

Work through these in order — free fixes first, component testing second.

### Fix 1: Back up your data immediately

Do this before anything else. WHEA errors can precede sudden component death.

1. Copy critical files to an external drive or cloud storage right now — don't wait until after diagnostics.
2. If the laptop crashes too often to back up normally, boot into Safe Mode (which stresses hardware less) and copy from there.
3. Verify the backup opens correctly on another device before continuing.

### Fix 2: Reset all overclocks and undervolts to stock

Eliminate the most common false alarm.

1. Enter BIOS/UEFI setup (**F2** or Novo button at boot).
2. Load **Optimized Defaults** (usually **F9** in the BIOS) to clear any overclocking.
3. Disable **XMP / EXPO** memory profiles.
4. If you use ThrottleStop, Intel XTU, or Ryzen Master, reset everything to stock and uninstall the tool temporarily.
5. Save (**F10**), exit, and test under the workload that crashed before.

### Fix 3: Check thermals and clean the cooling system

Heat-induced hardware errors are common and fixable.

1. Install **HWMonitor** and check idle and load temperatures for CPU, GPU, and SSD.
2. CPU consistently above 95°C or SSD above 70°C under load indicates a cooling problem.
3. Power off, unplug, and blow compressed air through all vents.
4. In **Lenovo Vantage**, set thermal mode to **Performance** for maximum fan speed during testing.
5. Retest. If errors stop after cleaning, heat was the trigger — consider a cooling pad for sustained workloads.

### Fix 4: Update the BIOS and chipset drivers

Firmware fixes resolve a meaningful share of WHEA errors.

1. Visit [Lenovo Support](https://support.lenovo.com/us/en/), enter your model, and check for a newer BIOS.
2. Install it with AC power connected, all apps closed — never interrupt a BIOS update.
3. Install the latest chipset driver from the same page.
4. Restart and test. BIOS updates frequently fix memory-training and power-management bugs that generate WHEA errors.

### Fix 5: Run Lenovo's hardware diagnostics

Let Lenovo's tools test each component.

1. Restart and press **F10** (or use the Novo button) to enter **Lenovo Diagnostics**.
2. Run the **CPU**, **Memory**, and **Storage** tests — start with quick tests, then run extended tests on any component that looks suspicious.
3. Note exactly which test fails and the error code.
4. A failing component needs replacement — contact Lenovo support if under warranty, with the error code ready.

### Fix 6: Test RAM thoroughly with Windows Memory Diagnostic

Memory is the most common failing component behind WHEA errors.

1. Press **Win + R**, type `mdsched.exe`, press **Enter**, choose **Restart now and check for problems**.
2. Press **F1** during the test, choose **Extended**, and run at least 2 passes (overnight for intermittent errors).
3. With two sticks, test each alone in the same slot to isolate the bad one.
4. Our detailed walkthrough is in [running the Memory Diagnostic tool in Windows 11 24H2](/articles/how-to-run-memory-diagnostic-tool-in-windows-11-24h2/).
5. Replace faulty RAM with a matched kit — mismatched sticks cause WHEA errors on their own.

### Fix 7: Check the SSD health

Storage faults are the second most common hardware cause.

1. Identify your SSD in **Device Manager > Disk drives**.
2. Install the manufacturer's toolbox (**Samsung Magician**, **Crucial Storage Executive**, **WD Dashboard**, **Intel MAS**).
3. Check SMART health — look for reallocated sectors, media errors, or any "failing" status.
4. Update the SSD firmware while you're there; firmware bugs cause WHEA-reportable errors.
5. Run `chkdsk C: /f /r` from an admin prompt to catch file-system damage.
6. A failing SSD needs immediate replacement — clone it before it dies completely.

### Fix 8: Reseat components and test with minimal hardware

For models with accessible panels, rule out connection issues.

1. Power off, unplug, and remove the bottom panel (check your model's hardware manual on [Lenovo Support](https://support.lenovo.com/us/en/) first).
2. Reseat the RAM sticks and the M.2 SSD — remove and firmly reinstall each.
3. Check for visible corrosion or damage on contacts.
4. If you have two RAM sticks, try booting with each one alone.
5. Reassemble, boot, and test. If errors persist with known-good seating, the component itself is faulty.
6. Microsoft's hardware error documentation is on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

WHEA Uncorrectable Error is hardware's way of asking for attention — back up first, then work the list: stock settings, thermals, BIOS, then component-by-component testing. Many cases end at the overclock reset or the vent cleaning; the ones that don't have a genuinely failing part that diagnostics will identify. Either way, you'll know exactly what's wrong instead of guessing, and that's what gets the laptop reliable again.
