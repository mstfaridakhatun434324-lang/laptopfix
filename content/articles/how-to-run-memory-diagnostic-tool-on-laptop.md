---
title: "How to Run the Windows Memory Diagnostic Tool on Your Laptop"
slug: how-to-run-memory-diagnostic-tool-on-laptop
date: 2026-09-02
categories: ["windows-errors"]
tags: ["Memory Diagnostic", "RAM testing", "Windows tools"]
description: "Run Windows Memory Diagnostic on your laptop the right way: choose the correct test mode, read the results in Event Viewer, and know when to use MemTest86."
thumbnail: "/images/thumbs/how-to-run-memory-diagnostic-tool-on-laptop.webp"
faqs:
  - q: "How do I open Windows Memory Diagnostic?"
    a: "Press Win + R, type mdsched.exe, and press Enter. Choose 'Restart now and check for problems' to test immediately, or 'Check for problems the next time I start my computer' to schedule it for your next boot. The tool runs before Windows loads, so it can test memory regions Windows itself would otherwise be using."
  - q: "How long does Windows Memory Diagnostic take?"
    a: "The default Standard test takes 15–30 minutes depending on how much RAM you have. The Extended test can take several hours — it's thorough but slow. For most troubleshooting, run Standard first; only move to Extended (or MemTest86) if Standard passes but you still suspect the RAM."
  - q: "Where do I find the Memory Diagnostic results?"
    a: "Results don't pop up on screen — they're logged to Event Viewer. After rebooting, open Event Viewer, go to Windows Logs > System, and look for an event from source MemoryDiagnostics-Results. It plainly states whether hardware problems were detected or the test passed with no errors."
  - q: "Is Windows Memory Diagnostic as good as MemTest86?"
    a: "It's good enough for obvious failures but less thorough than MemTest86. Memory Diagnostic is convenient and catches clearly bad RAM; MemTest86 (booted from USB, 4+ passes) is the gold standard that catches intermittent faults. Use Memory Diagnostic for the quick check and MemTest86 for the definitive verdict."
---

Windows Memory Diagnostic (`mdsched.exe`) is the built-in RAM tester most people have never opened. It runs before Windows loads, hammering your memory with test patterns to catch faulty sticks, bad slots, and intermittent errors. When blue screens like [MEMORY_MANAGEMENT](/articles/memory-management-bsod-blue-screen-error-fix/) or [FAULTY_HARDWARE_CORRUPTED_PAGE](/articles/what-to-do-if-faulty-hardware-corrupted-page/) point at RAM, this tool gives you the answer.

Running it is easy; running it *right* — choosing the correct mode, finding the results, and knowing its limits — is what this guide covers. Ten minutes here can save you from buying RAM you don't need, and from chasing driver ghosts when the hardware is genuinely at fault. Make it your first move whenever crashes smell like memory — it's faster than every alternative.

## Why this happens (why RAM testing matters)

- Faulty RAM causes random, inconsistent crashes that mimic driver and software problems.
- Windows can't fully test memory while it's running — the test must happen pre-boot.
- Intermittent RAM faults only surface under specific test patterns, not during normal use.
- A single bad stick in a two-stick kit causes crashes that look like everything else.
- Loose or poorly seated modules produce faults that reseating fixes for free.
- Memory Diagnostic's results hide in Event Viewer, so people run the test and never see the verdict.
- Overclocked RAM (XMP profiles) failing only under the test's specific patterns while seeming fine in daily use.

## How to fix it (run the test properly)

Work through these in order — from the quick built-in test to the definitive one.

### Fix 1: Launch Memory Diagnostic the easy way

The fastest path to a running memory test.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems (recommended)**.
3. Your laptop restarts into the blue Memory Diagnostic screen automatically.
4. The **Standard** test begins immediately — don't interrupt it.
5. The PC reboots into Windows when the test completes.

### Fix 2: Choose the right test mode

Standard is the default, but the options matter for tricky faults.

1. On the blue test screen, press **F1** to open **Options**.
2. **Test mix**: **Standard** covers the common patterns; **Extended** adds cache and stress tests.
3. **Cache**: leave **Default** unless you're chasing an L2/L3 cache suspect.
4. **Pass count**: set to **2** for a more thorough Standard run without Extended's hours-long wait.
5. Press **F10** to apply and start — remember, Extended can take several hours on 32 GB+ systems.

### Fix 3: Schedule the test for next boot

If you can't restart right now, queue the test for later.

1. Run `mdsched.exe` and choose **Check for problems the next time I start my computer**.
2. The test runs automatically at your next restart or shutdown-boot cycle.
3. This is handy for overnight testing: schedule it, shut down, and boot in the morning.
4. Combine with **Pass count 2** for an unattended thorough check.
5. Don't forget it's scheduled — an unexpected long boot tomorrow morning is just the test running.

### Fix 4: Find your results in Event Viewer

The test doesn't show results on screen — you have to look them up.

1. After rebooting, press **Win + X** and open **Event Viewer**.
2. Navigate to **Windows Logs > System**.
3. Click **Find** (or filter) and search for **MemoryDiagnostics-Results**.
4. Open the event: it states clearly whether **hardware problems were detected**.
5. No event at all usually means the test didn't run — check that it was actually scheduled.

### Fix 5: Interpret the results correctly

What the verdict means for your next step.

1. **"No memory errors detected"**: RAM is likely fine — focus on drivers and software.
2. **"Hardware problems were detected"**: at least one stick or slot is faulty — continue below.
3. A clean Standard test with ongoing crashes warrants the Extended test or MemTest86.
4. Errors that appear only on pass 2+ suggest heat-related or intermittent faults.
5. Note which test and pass found errors — it helps if you contact support.

### Fix 6: Isolate the faulty stick

A positive result doesn't tell you *which* stick — find it before buying replacements.

1. Power off, unplug, and remove the bottom panel.
2. If you have two sticks, remove one and run Memory Diagnostic on the remaining stick.
3. Swap and test the other stick alone in the same slot.
4. Test the suspect stick in the *other* slot to rule out a bad slot versus bad stick.
5. Replace only the confirmed-faulty stick with matching DDR generation, speed, and timings.

### Fix 7: Reseat before you replace

Loose contacts cause a surprising share of "faulty RAM" diagnoses.

1. Release the clips and fully remove each stick.
2. Blow out the slots with compressed air — dust causes contact issues.
3. Reinsert firmly until both clips snap shut on their own.
4. Re-run Memory Diagnostic to confirm the errors are gone.
5. If reseating fixes it, the RAM was never bad — just poorly connected.

### Fix 8: Escalate to MemTest86 for the final word

When Memory Diagnostic passes but crashes scream "RAM," bring out the gold standard.

1. Download **MemTest86** on another PC and create a bootable USB with its installer.
2. Boot your laptop from the USB and let it run **4 full passes** (several hours).
3. Any red error line is definitive: that RAM is faulty, no ambiguity.
4. Test sticks individually to identify the culprit, as in Fix 6.
5. Microsoft documents Memory Diagnostic basics on its [Windows support hub](https://support.microsoft.com/en-us/windows) if you want the official reference.

## Closing

Windows Memory Diagnostic is the fastest way to answer the biggest question in crash troubleshooting — "is my RAM actually bad?" Run it in Standard mode first, read the results in Event Viewer, isolate the stick if it fails, and escalate to MemTest86 only when you need certainty. Done right, it turns RAM from a scary unknown into a checked box — and it costs nothing but a little patience.
