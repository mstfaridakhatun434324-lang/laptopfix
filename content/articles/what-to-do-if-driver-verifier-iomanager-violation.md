---
title: "DRIVER_VERIFIER_IOMANAGER_VIOLATION: What to Do Next"
slug: what-to-do-if-driver-verifier-iomanager-violation
date: 2026-09-03
categories: ["windows-errors"]
tags: ["blue screen", "driver verifier", "driver error"]
description: "Got DRIVER_VERIFIER_IOMANAGER_VIOLATION? It means Driver Verifier caught a bad driver. Here's how to identify it and turn Verifier off safely."
thumbnail: "/images/thumbs/what-to-do-if-driver-verifier-iomanager-violation.webp"
faqs:
  - q: "What is Driver Verifier and why is it crashing my PC?"
    a: "Driver Verifier is a built-in Windows tool that stress-tests drivers by enforcing strict rules. When a driver breaks a rule, Verifier deliberately blue-screens so the bug gets caught during testing instead of corrupting data silently. The crash is intentional — it's how the tool reports its findings."
  - q: "How do I turn off Driver Verifier?"
    a: "Boot into Safe Mode (Verifier doesn't run there), press Win + R, type verifier, choose Delete existing settings, and restart. Or run verifier /reset from an elevated Command Prompt. Either way, restart afterward — the setting only takes effect on reboot."
  - q: "Should I leave Driver Verifier running all the time?"
    a: "No. Verifier slows the system and will keep crashing on any driver bug it finds, including minor ones that never affect real usage. Enable it only when hunting a specific suspected driver, verify just that driver, then turn Verifier off."
  - q: "The dump doesn't name a driver — what now?"
    a: "Run !verifier in WinDbg against the dump; it lists exactly which drivers were being verified and the violation details. If dumps aren't being created at all, check your Startup and Recovery settings to make sure minidumps are enabled, then reproduce the crash once more."
---

Seeing DRIVER_VERIFIER_IOMANAGER_VIOLATION means Driver Verifier — Windows' driver stress-test tool — caught a driver breaking I/O rules and crashed the system on purpose. That's actually good news: instead of a mystery crash, you have a tool pointing directly at a misbehaving driver.

The catch: Verifier stays on until you turn it off, and it'll keep crashing your laptop until you do. So the order here matters: identify the driver, disable Verifier, then fix the driver. Our [Verifier reference](/articles/best-way-to-fix-driver-verifier-iomanager-violation/) has more detail if you need it.

## Why this happens

- Driver Verifier was enabled (by you, a technician, or a troubleshooting guide) and is now doing its job — crashing on the bad driver it found.

- A third-party driver violating I/O manager rules: improper IRP handling, bad buffer usage, or illegal calls.

- The offending driver is often storage, network, or USB-related, since those live in the I/O path.

- Verifier was left on after a previous troubleshooting session and forgotten.

- An outdated driver that was always buggy, now exposed by Verifier's strict checks.

- Running Verifier on all drivers at once, which makes the system unstable and the culprit harder to isolate.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Boot into Safe Mode

Driver Verifier doesn't run in Safe Mode, so this gets you to a stable desktop where you can turn it off and investigate.

1. Force-power-off twice during boot to reach the recovery environment.

2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **4** for Safe Mode.

3. Confirm the laptop is stable in Safe Mode.

4. Everything below happens from here.

### Fix 2: Turn off Driver Verifier

This is the urgent step — with Verifier off, the intentional crashes stop and you can work normally while fixing the real driver.

1. In Safe Mode, press **Win + R**, type `verifier`, and press **Enter**.

2. Choose **Delete existing settings** and click **Finish**.

3. Alternatively, open an admin Command Prompt and run `verifier /reset`.

4. Restart normally and confirm the blue screens stop. (The underlying driver bug remains — keep going.)

### Fix 3: Identify the caught driver from the dump

Verifier's crash dump names the driver that broke the rules. Reading it tells you exactly what to fix.

1. Open **Event Viewer > Windows Logs > System** and find the **BugCheck** entry — it often names the driver.

2. For the full picture, open the minidump in **WinDbg** (our [dump analysis guide](/articles/best-way-to-read-dump-files-with-windbg/) shows how) and run `!verifier` and `!analyze -v`.

3. Note the driver file name — that's your target.

4. If no dump was saved, check **Settings > System > About > Advanced system settings > Startup and Recovery** settings to enable dumps for next time.

### Fix 4: Replace the offending driver

The driver Verifier caught is buggy — update it, roll it back, or remove it, depending on what changed recently.

1. Open **Device Manager** and find the device tied to the named driver.

2. If the driver updated recently, use **Properties > Driver > Roll Back Driver**.

3. Otherwise **Uninstall device** (tick **Attempt to remove the driver**), restart, and install the manufacturer's latest version.

4. For Intel components, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the right one automatically.

### Fix 5: Re-run Verifier narrowly to confirm the fix

Before declaring victory, verify the replacement driver actually passes Verifier's checks — narrowly, so a different bug doesn't crash you again.

1. Press **Win + R**, type `verifier`, and choose **Create standard settings**.

2. Select **Select driver names from a list** and tick ONLY the replacement driver.

3. Restart and use the laptop normally for several hours.

4. If no crash occurs, run `verifier /reset` from an admin prompt and restart — leave Verifier off for daily use.

### Fix 6: Check for firmware updates

Sometimes the 'driver bug' is really the driver working around buggy firmware. A BIOS or device firmware update resolves the underlying issue.

1. Check your laptop maker's support site for **BIOS** and firmware updates for your exact model.

2. Also check the device maker's site (SSD, Wi-Fi card, dock) for firmware updates.

3. Apply on AC power without interruption.

4. Re-test stability after updating. Microsoft's guidance on driver troubleshooting is on [their Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 7: Recover with System Restore if you can't reach Safe Mode

If Verifier crashes the boot too early for Safe Mode, System Restore from the recovery environment rolls back to before Verifier was enabled. And for next time, there's a flag that makes Verifier disable itself after a boot failure.

1. Boot into the recovery environment (force-power-off twice during the Windows logo).

2. Go to **Troubleshoot > Advanced options > System Restore**.

3. Pick a restore point from before you enabled Driver Verifier and complete the wizard.

4. Once you're back in Windows, open an admin Command Prompt.

5. For future Verifier sessions, first run `verifier /bootmode resetonbootfail` — this makes Verifier automatically disable itself if the next boot fails.

6. Then configure Verifier as before, knowing a bad session can never lock you out again.

## Closing

DRIVER_VERIFIER_IOMANAGER_VIOLATION looks alarming, but it's Verifier doing exactly what you asked: catching a bad driver in the act. Turn Verifier off first so you can think straight, read the dump to name the driver, replace that driver, and confirm with a narrow re-run. And when you're done, leave Verifier off — it's a diagnostic tool, not a bodyguard, and running it permanently just manufactures crashes. The resetonbootfail flag is the seatbelt for Driver Verifier: set it before every session and a bad run can never lock you out again. Verifier is a power tool — respect it the way you'd respect any tool that deliberately crashes your PC, and it keeps handing you driver names instead of headaches.
