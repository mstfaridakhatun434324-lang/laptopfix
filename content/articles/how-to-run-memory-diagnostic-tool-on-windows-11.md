---
title: "How to Run the Memory Diagnostic Tool on Windows 11"
slug: how-to-run-memory-diagnostic-tool-on-windows-11
date: 2026-09-19
categories: ["windows-errors"]
tags: ["memory diagnostic", "ram test", "windows 11", "mdsched"]
description: "Test your RAM on Windows 11 with the built-in Memory Diagnostic — launch options, extended tests, reading results in Event Viewer, and next steps."
thumbnail: "/images/thumbs/how-to-run-memory-diagnostic-tool-on-windows-11.webp"
faqs:
  - q: "How do I open Windows Memory Diagnostic on Windows 11?"
    a: "Press Win + R, type mdsched.exe, and press Enter — then choose Restart now and check for problems. It is built into every Windows 11 installation, so there is nothing to download or install."
  - q: "Where do I find the Memory Diagnostic results?"
    a: "Windows shows a notification after rebooting, but it is easy to miss. Open Event Viewer, go to Windows Logs > System, and search for MemoryDiagnostics-Results. The entry states plainly whether errors were detected."
  - q: "How long does the test take on Windows 11?"
    a: "The standard test with two passes takes roughly 15–45 minutes depending on your RAM size and speed. The extended test can take several hours — run it overnight if you need that level of confidence."
  - q: "What does it mean if the test finds hardware problems?"
    a: "At least one RAM stick is failing. Back up your data immediately, then isolate the bad stick by testing them one at a time (on laptops with removable RAM). Replace the faulty stick — failing memory corrupts files silently and will only get worse."
---

Faulty RAM is the great impersonator of PC problems. It causes blue screens with a different stop code every time, corrupts files at random, crashes programs that were fine yesterday, and makes Windows updates fail for no apparent reason. Before you go down any of those rabbit holes, spend half an hour testing the memory itself with the tool Microsoft ships in every copy of Windows 11: **Windows Memory Diagnostic**.

This is the Windows 11 edition of the guide — the tool works the same as on Windows 10 (covered [here](/articles/how-to-run-memory-diagnostic-tool-on-windows-10/)), but the surrounding steps reflect Windows 11's Settings and Terminal. If your crashes already name a memory-related stop code like [MEMORY_MANAGEMENT](/articles/memory-management-bsod-windows-11-fix/), consider this test mandatory rather than optional.

Timing matters with memory testing, and here is the practical advice: run the standard test as soon as you suspect RAM, because every hour you run on failing memory is another hour of potential silent file corruption. But run the extended test when you can afford to leave the machine alone — overnight is perfect. The standard test is a screening; the extended test is the diagnosis. People who skip the extended test after a passing standard test and keep chasing software causes lose days. If the symptoms point at RAM and the quick test is clean, the overnight test is always worth it.

## Why this happens

RAM fails for unglamorous reasons, and the symptoms rarely point at it directly:

- **Age and heat.** Memory cells degrade over years of thermal cycling — laptops that run hot age their RAM faster.
- **The "different BSOD every time" pattern.** MEMORY_MANAGEMENT today, IRQL_NOT_LESS_OR_EQUAL tomorrow, SYSTEM_SERVICE_EXCEPTION next week. When the stop codes keep changing, suspect the RAM.
- **Crashes only under load.** Bad addresses may sit unused until you actually fill the memory — gaming, video work, or heavy multitasking.
- **Silent data corruption.** Faulty RAM scrambles data passing through it, so files save corrupted and downloads fail verification.
- **New RAM that was never quite right.** Even fresh sticks can be marginal — always test new memory after installation.

## How to fix it

"Fix" here means test, interpret, and act. Work through these in order.

### Fix 1: Run the standard test

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Click **Restart now and check for problems**. Save everything first — the reboot is immediate.
3. The laptop restarts into a blue diagnostic screen and the test runs automatically. Leave it alone until it finishes and reboots into Windows.
4. After reboot, watch for the result notification in the bottom-right corner.

### Fix 2: Run it from Windows Tools

If you prefer navigating menus:

1. Press **Win + S**, type **Windows Tools**, and open it.
2. Double-click **Windows Memory Diagnostic**.
3. Choose **Restart now and check for problems** — or schedule it for the next restart if you are in the middle of something.

### Fix 3: Use the extended test for stubborn cases

The standard test catches obvious faults. For intermittent crashes that smell like RAM but pass the standard test:

1. Launch `mdsched.exe` and restart into the diagnostic screen.
2. Press **F1** to open options.
3. Set **Test mix** to **Extended**, **Cache** to **On**, and **Pass count** to **2**.
4. Press **F10** to start. Budget several hours — overnight is ideal.
5. Extended mode runs many more test patterns (including the brutal MATS+ and stride tests) that catch marginal cells.

### Fix 4: Find the result in Event Viewer

The toast notification disappears quickly. The permanent record lives in Event Viewer.

1. Press **Win + X** and choose **Event Viewer**.
2. Navigate to **Windows Logs > System**.
3. Click **Find** in the right-hand Actions panel and search for `MemoryDiagnostics-Results`.
4. Double-click the entry. It will say either "The Windows Memory Diagnostic tested the computer's memory and detected no errors" or describe the hardware problems found.

### Fix 5: Isolate the faulty stick

1. **Back up your important data now.** Bad RAM corrupts files silently — do this before anything else.
2. If your laptop has removable RAM (check the manual — many ultrabooks have soldered memory), power off, unplug, and remove one stick.
3. Boot with the single remaining stick and rerun `mdsched.exe`.
4. Repeat with the other stick alone. The one that fails is the one to replace.
5. Buy a replacement matching the original's DDR generation, speed, and voltage — mixing specs causes its own instability.

### Fix 6: Reseat the memory modules

A surprising number of "bad RAM" diagnoses are just poor contact.

1. Power off fully, unplug, and hold the power button for 10 seconds to discharge.
2. Remove each stick, clean the slot with compressed air, and reseat firmly until both clips snap shut.
3. Rerun the diagnostic. Laptops that get carried around daily are the most prone to slowly loosening modules.

### Fix 7: Confirm with MemTest86 if results are ambiguous

1. If Windows Memory Diagnostic passes but you still strongly suspect RAM, create a MemTest86 bootable USB and run it overnight.
2. Boot from USB via your laptop's boot menu key and let all passes complete.
3. Any error — even one — means the RAM is bad. Replace it regardless of what the Windows tool said.

### Fix 8: Replace and verify

1. Install the new stick(s), boot up, and rerun `mdsched.exe` to confirm zero errors.
2. If your laptop has soldered RAM, replacement means board-level repair — get a quote from a reputable shop and weigh it against the machine's value.
3. After replacing, re-run any workload that used to crash to confirm stability before calling it done.

## Closing

The Windows 11 Memory Diagnostic is one of the most underused tools in the operating system — free, built in, and decisive. Run it at the *start* of any random-crash investigation, not after you have already reinstalled Windows twice. Read the result in Event Viewer, isolate the bad stick if there is one, and replace it. RAM problems never fix themselves, but they are among the cheapest hardware problems to solve once you have identified them. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has additional memory troubleshooting background if you want to go deeper.
