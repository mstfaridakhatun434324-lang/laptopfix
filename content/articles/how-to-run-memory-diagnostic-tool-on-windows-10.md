---
title: "How to Run the Memory Diagnostic Tool on Windows 10"
slug: how-to-run-memory-diagnostic-tool-on-windows-10
date: 2026-09-08
categories: ["windows-errors"]
tags: ["memory diagnostic", "ram test", "windows 10", "mdsched"]
description: "Test your RAM for errors on Windows 10 with the built-in Memory Diagnostic tool — launch it, read the results, and know exactly what to do next."
thumbnail: "/images/thumbs/how-to-run-memory-diagnostic-tool-on-windows-10.webp"
faqs:
  - q: "How long does the Windows Memory Diagnostic take?"
    a: "The default standard test takes 10–30 minutes depending on how much RAM you have. The extended test can take several hours. Run the standard test first — it catches the vast majority of bad-RAM problems."
  - q: "Do I need to install anything to test my RAM?"
    a: "No. Windows Memory Diagnostic (mdsched.exe) ships with every copy of Windows 10. You can run it in under a minute with no downloads, no USB stick, and no third-party software."
  - q: "What should I do if the test finds errors?"
    a: "Back up your data first, then identify the bad stick: if you have two sticks, test with one removed at a time and rerun the diagnostic. Replace the faulty stick with matching RAM. Running Windows on failing memory corrupts files silently, so do not ignore it."
  - q: "Is the built-in test as good as MemTest86?"
    a: "For obvious, crash-causing RAM faults, yes — it finds them reliably. MemTest86 is more thorough for subtle, intermittent faults and is worth running overnight if Windows Memory Diagnostic passes but you still suspect the RAM."
---

Random blue screens, corrupted files, programs crashing for no reason — bad RAM produces a grab-bag of symptoms that look like everything except the actual problem. Before you reinstall Windows or buy a new SSD, it is worth spending 20 minutes testing your memory with the tool Microsoft already put on your machine: **Windows Memory Diagnostic** (`mdsched.exe`).

This guide covers Windows 10 specifically. If you have moved to Windows 11, the steps are nearly identical and we have a dedicated [Memory Diagnostic walkthrough for Windows 11](/articles/how-to-run-memory-diagnostic-tool-on-windows-11/). And if your crashes name a specific file, like the classic [MEMORY_MANAGEMENT stop code](/articles/memory-management-bsod-windows-11-fix/), that is another sign the RAM deserves a look.

## Why this happens

Bad RAM is not always dramatic. Here is what failing memory actually does:

- **Random, changing blue screens.** Different stop codes each time — MEMORY_MANAGEMENT one day, IRQL_NOT_LESS_OR_EQUAL the next — is the textbook signature of bad RAM.
- **Silent file corruption.** Data gets scrambled as it passes through faulty memory, so downloads fail checksums and documents come out garbled.
- **Crashes under load, fine when idle.** Memory faults often only show up when the system actually uses the damaged addresses — gaming, video editing, or having 40 browser tabs open.
- **Failed Windows updates.** Update installers verify file integrity aggressively, so a bad stick often first announces itself as updates that refuse to install.
- **One bad stick in a pair.** Most laptops with two RAM slots fail one stick at a time, which is why testing sticks individually matters.

## How to fix it

Work through these in order — test first, then interpret, then act.

### Fix 1: Launch Windows Memory Diagnostic

The fastest way in.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**. Save your work first — the laptop reboots immediately.
3. The test starts automatically on a blue screen with a progress bar. Do not interrupt it.
4. When it finishes, the laptop reboots back into Windows and shows a notification with the result.

### Fix 2: Launch it from the Control Panel instead

If you prefer menus over the Run box, or want to schedule the test for the next restart:

1. Open **Control Panel** and go to **System and Security > Administrative Tools**.
2. Double-click **Windows Memory Diagnostic**.
3. Choose **Restart now and check for problems** or **Check for problems the next time I start my computer**.

### Fix 3: Choose the right test options

The default test is fine for a first pass, but you can make it more thorough.

1. When the blue diagnostic screen appears, press **F1** to open **Options**.
2. Under **Test mix**, choose **Standard** for the first run (fast), or **Extended** if you have time — extended runs more patterns and catches subtler faults.
3. Set **Cache** to **On** (default) and **Pass count** to **2** for a good balance of speed and confidence.
4. Press **F10** to apply and start. Two passes of the standard test is the sweet spot for most people.

### Fix 4: Read the results properly

The result notification is easy to miss — here is how to find it for certain.

1. After rebooting, look for a toast notification saying "Your computer has a memory problem" or "No memory errors were detected."
2. If you missed the notification, press **Win + X**, choose **Event Viewer**, and navigate to **Windows Logs > System**.
3. Click **Find** in the right panel and search for `MemoryDiagnostics-Results`.
4. Double-click the entry to read the full report — it will say plainly whether errors were found.

### Fix 5: Isolate the bad stick

The diagnostic tells you *that* memory failed, not *which* stick. Here is how to find it.

1. Back up your important files now — bad RAM corrupts data silently.
2. Power off, unplug, and (on laptops with removable RAM) take out one stick. Consult your laptop manual for the access panel location; many thin laptops have soldered RAM and cannot do this step.
3. Boot with the remaining stick and rerun `mdsched.exe`.
4. If it passes, swap sticks and test the other one. The stick that fails is the one to replace.
5. Replace with RAM matching the original specs (DDR generation, speed, and voltage) — mismatched sticks cause their own problems.

### Fix 6: Reseat the RAM and check for dust

Sometimes "bad RAM" is just a poor connection.

1. Power off completely, unplug, and remove the battery if it is removable. Hold the power button for 10 seconds to discharge residual power.
2. Remove each RAM stick, blow out the slot with compressed air, and reseat the stick firmly until the clips snap.
3. Rerun the diagnostic. A surprising number of "failures" disappear after a proper reseat — especially on laptops that travel a lot.

### Fix 7: Run MemTest86 for a deeper check

If Windows Memory Diagnostic passes but the symptoms scream bad RAM, go deeper.

1. Download MemTest86 from its official site and create a bootable USB stick with its included tool.
2. Boot from the USB (use the boot menu key — **F12** on Dell, **F9** on HP, **F2/F12** on Lenovo, **Esc** on ASUS) and let it run overnight.
3. Any red error line means bad RAM, full stop — replace the stick even if the Windows tool said it was fine.

### Fix 8: Replace the faulty RAM

1. Buy replacement RAM matching your laptop's specs — check the manual or the existing stick's label for DDR type, speed (e.g., DDR4-3200), and capacity.
2. Install it in the same slot, boot up, and rerun `mdsched.exe` to confirm the errors are gone.
3. If your laptop has soldered RAM that cannot be replaced, the motherboard needs professional repair — get a quote before deciding whether the machine is worth fixing.

## Closing

Testing your RAM on Windows 10 takes about a minute to start and twenty minutes to run, and it rules out one of the sneakiest causes of random crashes. Run `mdsched.exe`, read the result in Event Viewer if you miss the notification, and isolate the bad stick if errors show up. Bad memory only gets worse with time — and unlike a software bug, it will happily corrupt your files while you ignore it. For broader context on update-related memory errors, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) is a solid reference.
