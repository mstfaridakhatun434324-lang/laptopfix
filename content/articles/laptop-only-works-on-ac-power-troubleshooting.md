---
title: "Diagnose a Laptop That Dies the Moment You Unplug It"
slug: laptop-only-works-on-ac-power-troubleshooting
date: 2026-09-22
categories: ["battery"]
tags: ["ac power only", "diagnostics", "battery failure", "troubleshooting"]
description: "A diagnostic walkthrough for AC-only laptops: test whether the battery, connector, driver, or motherboard is keeping you tethered to the wall."
thumbnail: "/images/thumbs/laptop-only-works-on-ac-power-troubleshooting.webp"
faqs:
  - q: "How do I diagnose a laptop that only works plugged in?"
    a: "Start with Windows' view (Device Manager, battery report), then check BIOS for a disabled battery, then the drivers, then the physical connector. Each layer you clear narrows it to the next. The battery report's wear numbers and the manufacturer's hardware diagnostic give the final verdict."
  - q: "What's the difference between a dead battery and a disconnected one?"
    a: "A dead battery is usually still detected by Windows (showing 0% or very low capacity) but holds no charge. A disconnected or disabled battery doesn't appear at all — no icon, no entry in Device Manager, and the battery report shows nothing. The fix differs completely."
  - q: "Can a software issue really make the battery disappear?"
    a: "Yes. A corrupted ACPI battery driver, a BIOS setting that disables the battery, or a failed Windows update can all make a healthy battery invisible. That's why the diagnostic order goes software first — driver and BIOS checks are free and fix many cases."
  - q: "When should I stop diagnosing and replace the battery?"
    a: "When the battery is detected but shows severe wear (under 60% of design capacity), fails the manufacturer's hardware diagnostic, or shows physical swelling. At that point further software troubleshooting is wasted effort — the chemistry is done."
---
When a laptop dies the instant the charger comes out, you're dealing with a battery contributing exactly zero — but "zero" has several distinct causes, and the treatment for each is completely different. A disconnected battery needs a reseat. A driver-hidden battery needs a reinstall. A chemically dead battery needs a replacement. Guessing wrong costs either time or money.

This is the diagnostic companion to the fix guide: a structured process that isolates the faulty layer — OS, driver, firmware, connector, or cell chemistry — with a test at each step and a clear interpretation of the results.

## Why this happens

- **Chemical end of life:** The pack's protection circuit cuts off a battery that can no longer safely hold charge. Detected, but useless.
- **Loose internal connector:** Physical disconnection from drops, heat cycling, or swelling. The battery is fine but electrically absent.
- **BIOS-level disable:** A firmware setting disconnects the battery for servicing. Invisible to Windows until re-enabled.
- **Driver failure:** The ACPI battery driver fails to load or corrupts, hiding a healthy battery from the OS.
- **Deep-discharge lockout:** A pack drained to absolute zero enters protection mode and won't wake without extended charging.
- **Swollen pack safety cutoff:** Physical swelling triggers the pack's safety systems, electrically isolating it.
- **Motherboard power circuit fault:** The battery power path on the board fails while the AC path survives. Rare, but it's the diagnosis of exclusion.

## How to fix it

Work through these in order — each test eliminates a layer.

### Fix 1: Establish the detection baseline

The single most informative minute of this whole process: is the battery detected at all?

1. **Check the taskbar:** Battery icon present? Red X? Missing entirely? Note exactly what you see.
2. **Device Manager > Batteries:** List every entry. Missing entries = detection failure. Present entries = the OS sees hardware.
3. **Run** `powercfg /batteryreport` in an admin Terminal. Success with battery data = detected. Errors or empty output = not detected.
4. **Classify your case:** **Detected but dead** (shows 0%/low capacity) vs. **Not detected at all**. The rest of the diagnosis branches on this.

Detected-but-dead points toward chemistry or deep discharge (Fixes 5–7). Not-detected points toward driver, BIOS, or connector (Fixes 2–4). Write down your classification.

### Fix 2: Test the driver layer

Drivers are free to fix and a common hiding place for healthy batteries.

1. **Uninstall all battery devices:** Device Manager > Batteries — right-click each entry, **Uninstall device**.
2. **Full shutdown** (**Shift + Shut down**), unplug 30 seconds, reconnect, boot.
3. **Recheck detection:** If the battery appears now, the driver was corrupt. Done — monitor for recurrence.
4. **Check for warning symbols:** A yellow triangle with an error code (e.g., Code 10, Code 43) points to a driver-hardware communication fault. Note the code.
5. **Update the chipset driver** from your manufacturer's support site — the chipset driver is the bridge between Windows and the battery hardware.

If the battery remains undetected after a clean driver reinstall, the problem is below the OS: firmware or physical. For the fix-oriented version of these steps, see [fix a laptop that only works on AC power](/articles/best-way-to-fix-laptop-only-works-on-ac-power/). If the battery shows up but won't hold charge, check [laptop battery not detected in Windows 11](/articles/laptop-battery-not-detected-windows-11/) for the detection-specific deep dive.

### Fix 3: Test the firmware layer

BIOS settings and firmware state sit between the hardware and Windows.

1. **Enter BIOS/UEFI setup** and look for battery options — **Disable Built-in Battery**, battery health readings, or power settings.
2. **Ensure the battery is enabled.** If a disable option is on, turn it off, save, and boot to Windows.
3. **Note the BIOS battery reading:** If the BIOS itself shows no battery, Windows never will — the issue is physical (connector or pack), not software.
4. **Reset BIOS to defaults** if settings look odd — a corrupted power setting can hide the battery. (Note your custom settings first if you changed boot order or similar.)
5. **Check for a BIOS update** mentioning battery or power fixes — but only flash with the charger connected.

BIOS shows battery + Windows doesn't = driver/OS problem (back to Fix 2, deeper). BIOS doesn't show it either = physical problem (Fix 4).

### Fix 4: Test the physical layer

If firmware can't see the battery, it's the connector, the pack, or the board.

1. **Safety check first:** Power off and inspect for swelling — base wobble on a flat surface, lifting trackpad, visible bulge. If swollen, stop and go to Fix 6.
2. **Reseat the connector:** Open the bottom cover, disconnect and firmly reconnect the battery's motherboard plug. Reassemble enough to test.
3. **Test detection:** Boot to BIOS first — if the battery appears in BIOS now, the connector was the fault.
4. **Inspect the connector and cable:** Bent pins, corrosion, or a cracked housing mean the connection was never reliable. Clean gently or replace the cable if it's a separate part.
5. **Try the long charge:** With the connector reseated, charge 4+ hours undisturbed in case the pack was also deeply discharged.

A battery that appears after reseating had a connection problem, full stop. If it never appears, the pack or board is the fault.

### Fix 5: Run the manufacturer's hardware diagnostic

Get an authoritative verdict from the people who built the machine.

1. **Dell:** **F12** at boot → **Diagnostics**. **Lenovo:** Vantage battery test or UEFI diagnostics. **HP:** **Esc**/**F2** at boot → diagnostics. **ASUS/Acer:** Check the support apps or UEFI.
2. **Run the battery-specific test** and record the exact result and any failure code.
3. **Interpret:** A clear battery failure code = replace the pack. A pass with the battery still undetected in Windows = driver/OS issue (return to Fix 2 with the chipset driver). Adapter failures flagged here explain charging-side problems.

The diagnostic result plus your detection classification from Fix 1 gives you a near-certain diagnosis. Microsoft's troubleshooting guidance at [support.microsoft.com](https://support.microsoft.com/en-us/windows) covers the OS-side complements.

### Fix 6: Assess swelling and safety

Physical inspection is a diagnostic step with safety implications — do it deliberately.

1. **The flat-surface test:** Power off, unplug, place on a flat table. Any rocking means the base is deformed.
2. **The trackpad test:** A trackpad that's lifting, clicking oddly, or hard to press often sits above a swelling pack.
3. **Look and smell:** Remove the bottom cover (if you're comfortable) and look for a pillowy pack, plus any sweet/chemical smell.
4. **If swollen:** Don't puncture, bend, or compress it. Don't charge it. Back up data with the battery removed if the model allows, and get the pack replaced promptly — a shop can handle removal safely.

Swelling explains every AC-only symptom by itself: the protection circuit isolates a dangerous pack. No further diagnosis needed.

### Fix 7: Assemble the final verdict

Combine all test results into one conclusion.

1. **Not detected anywhere + reseat didn't help + no swelling:** Dead pack electronics or board power circuit. Try a known-good battery if you can borrow one — if it detects, buy a replacement; if not, it's board-level repair.
2. **Detected with severe wear:** Replace the pack. The chemistry is done.
3. **Detected after driver/BIOS work:** Fixed — but watch for recurrence, which suggests a flaky driver update cycle.
4. **Diagnostic failure code:** Follow the manufacturer's recommended action; attach the code to any warranty claim.
5. **Document everything:** Detection status, wear numbers, diagnostic codes, and what you tried. This is gold for a repair shop or support ticket — it skips their entire first hour.

## Closing

AC-only diagnosis is a layer cake: OS detection, driver, firmware, connector, chemistry. Test each layer in order and the faulty one reveals itself — usually by step three or four. The key discipline is classifying "detected but dead" versus "not detected at all" right at the start, because those two cases go down completely different paths. With the tests above, you reach a certain verdict instead of a guess — and whether the answer is a free driver reinstall or a new battery, you'll know why.
