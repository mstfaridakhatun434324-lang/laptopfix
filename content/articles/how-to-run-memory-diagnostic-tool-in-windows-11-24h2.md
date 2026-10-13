---
title: "How to Run the Memory Diagnostic Tool in Windows 11 24H2"
slug: how-to-run-memory-diagnostic-tool-in-windows-11-24h2
date: 2026-10-05
categories: ["windows-errors"]
tags: ["memory-diagnostic", "windows-11-24h2", "ram-test"]
description: "Learn how to run Windows Memory Diagnostic in Windows 11 24H2, read the results, and know when your RAM needs replacing."
thumbnail: "/images/thumbs/how-to-run-memory-diagnostic-tool-in-windows-11-24h2.webp"
faqs:
  - q: "What does the Windows Memory Diagnostic tool actually test?"
    a: "It writes test patterns to every addressable byte of your RAM and reads them back, checking for bits that flip, addresses that alias each other, and cells that fail under different access patterns. It runs outside Windows (before boot) so it can test memory Windows itself would be using. The standard test covers the common failure modes; extended mode adds deeper pattern and cache tests."
  - q: "How long does the memory test take in 24H2?"
    a: "The standard test takes 10–20 minutes on most laptops. Extended mode with 2 passes takes 1–3 hours depending on RAM size and speed; overnight runs with more passes catch intermittent faults. Plan accordingly — the laptop is unusable during the test, so run long tests when you don't need the machine."
  - q: "Where do I find the results after the test finishes?"
    a: "Windows doesn't show results on screen for long — it boots normally and logs them. Open Event Viewer (Win + X > Event Viewer), go to Windows Logs > System, and filter for source 'MemoryDiagnostics-Results'. The entry says whether errors were detected. If you miss it, the result stays in the log permanently."
  - q: "Is Windows Memory Diagnostic as good as MemTest86?"
    a: "For most purposes, yes — it catches the same common RAM failures. MemTest86 (booted from USB) is more thorough for elusive intermittent faults and gives per-address error details, which helps when deciding which stick to replace. Start with the built-in tool; reach for MemTest86 if crashes continue after a clean built-in result."
---
If your laptop crashes with ever-changing blue screens, freezes randomly, or corrupts files for no apparent reason, bad RAM is a prime suspect — and Windows ships a free tool to test it. Windows Memory Diagnostic runs before Windows boots, giving it full access to test every byte of your memory. It's the first thing technicians run when hardware is suspected, and on Windows 11 24H2 it works exactly as it always has.

This guide covers running the test, choosing the right test depth, reading the results, and what to do when errors appear. If you're here because of a specific stop code, our [Memory Management on Windows 10](/articles/how-to-fix-stop-code-memory-management-on-windows-10/) guide covers the software side of memory crashes, and the [Windows 11 version of this tool guide](/articles/how-to-run-memory-diagnostic-tool-on-windows-11/) applies if you're not on 24H2.

## Why this happens

- **Failing RAM cells.** Memory chips degrade; individual cells start flipping bits, causing random crashes and corruption.
- **Mismatched RAM sticks.** Different brands, speeds, or timings in the same laptop create instability the test will reveal.
- **Loose or poorly seated RAM.** A stick that's worked slightly out of its slot produces intermittent errors.
- **Overclocked memory (XMP/EXPO).** Aggressive timings the RAM can't sustain show up as test failures.
- **Overheating memory.** Poor case airflow lets RAM overheat under sustained load, causing errors only when hot.
- **Motherboard slot faults.** Rare, but a bad slot produces errors that follow the slot, not the stick.

## How to fix it

Work through these in order — test, interpret, then act.

### Fix 1: Run the standard Memory Diagnostic test

Start with the quick test to catch obvious failures.

1. Save all work and close applications — the test requires a restart.
2. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
3. Choose **Restart now and check for problems**. (Choose **Check for problems the next time I start my computer** if you want to schedule it for later.)
4. The laptop restarts into the blue Memory Diagnostic screen and runs the standard test automatically.
5. Wait 10–20 minutes for it to complete. The system then boots into Windows normally.

### Fix 2: Run the extended test for intermittent problems

The standard test misses faults that only appear under specific patterns or when hot.

1. Start the test as in Fix 1, and when the blue test screen appears, press **F1** to open **Options**.
2. Use the arrow keys to select **Extended** test mix (instead of Standard).
3. Set **Pass count** to at least **2** — more passes catch more intermittent faults.
4. Press **F10** to apply and start. The extended test takes 1–3 hours; overnight runs are ideal for elusive problems.
5. Leave the laptop plugged in and don't interrupt the test.

### Fix 3: Find and read the results in Event Viewer

The results don't stay on screen — they're logged.

1. After the test completes and Windows boots, press **Win + X** and choose **Event Viewer**.
2. In the left pane, go to **Windows Logs > System**.
3. In the right **Actions** pane, click **Filter Current Log**, and in the **Event sources** dropdown check **MemoryDiagnostics-Results**, then click **OK**.
4. Click the resulting entry to read it: it states clearly whether hardware errors were detected.
5. If no MemoryDiagnostics-Results entry exists, the test may not have completed — rerun it.

### Fix 4: Interpret the results correctly

Know what the outcome means before acting.

1. **No errors detected (standard test):** RAM is probably fine for common faults, but intermittent issues may need the extended test.
2. **No errors detected (extended, 2+ passes):** RAM is very likely healthy — look at drivers, thermals, or the SSD instead.
3. **Errors detected:** At least one RAM stick is faulty. Note that the built-in tool doesn't tell you which stick — Fix 5 does.
4. **Test freezes or crashes mid-run:** Also indicates bad RAM (or a severe fault) — the test itself crashing is a result.

### Fix 5: Isolate the faulty stick

Find which stick is bad so you replace the right one.

1. Shut down, unplug, and remove the bottom panel (check your model's manual for the procedure).
2. If you have two sticks, remove one and run the standard test with the remaining stick.
3. Swap and test the other stick alone in the same slot.
4. The stick that errors is the bad one. If both error in the same slot but pass in the other slot, the slot itself is faulty.
5. Ground yourself before handling RAM (touch unpainted metal on the chassis), and handle sticks by the edges.

### Fix 6: Reseat RAM and disable XMP before replacing

Some "failures" are seating or settings, not dead chips.

1. Remove each stick and firmly reseat it — press evenly until both retention clips click.
2. Blow any dust out of the slots with compressed air.
3. Enter BIOS (**F2**/**Del** at boot) and disable **XMP / EXPO** profiles, returning RAM to stock speeds.
4. Rerun the standard test. If errors vanish, the RAM was fine but the overclock or seating wasn't.
5. If errors persist at stock speeds with firm seating, the stick is genuinely faulty.

### Fix 7: Replace the faulty RAM

Buy right, install carefully.

1. Note your RAM specs: type (DDR4/DDR5), speed, and capacity — check with **Task Manager > Performance > Memory** or the existing stick's label.
2. Buy a **matched kit** (both sticks in one package) rather than a single stick — matched pairs avoid the mismatch instability that causes these errors.
3. Install with the laptop powered off and unplugged, pressing firmly until clips engage.
4. Boot and rerun the standard Memory Diagnostic to confirm the new RAM passes.
5. Keep the receipt — RAM has long warranties, and a stick that fails early may be a warranty claim.

### Fix 8: When the test passes but crashes continue

A clean memory test redirects the investigation.

1. Update drivers — graphics, chipset, and storage first. Many "RAM-like" crashes are driver memory corruption.
2. Check thermals: overheating CPUs and SSDs cause crashes that mimic RAM faults.
3. Run `chkdsk C: /f /r` to rule out disk errors.
4. Try **MemTest86** from a USB drive for a second opinion — it's more thorough for borderline faults.
5. Microsoft documents memory-related blue screen troubleshooting on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Windows Memory Diagnostic is the fastest way to answer the "is it the RAM?" question — free, built in, and definitive for common faults. Run the standard test first, go extended for intermittent issues, read the results in Event Viewer, and isolate the bad stick before spending money. And remember the golden rule this tool teaches: a clean extended test means the RAM is innocent, so stop suspecting it and chase the real culprit.
