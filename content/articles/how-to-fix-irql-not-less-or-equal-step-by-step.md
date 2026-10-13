---
title: "IRQL Not Less or Equal: A Step-by-Step Fix Guide"
slug: how-to-fix-irql-not-less-or-equal-step-by-step
date: 2026-10-01
categories: ["windows-errors"]
tags: ["blue screen", "IRQL", "step by step"]
description: "IRQL Not Less or Equal blue screen? Follow this exact step-by-step sequence to find the faulty driver and fix it."
thumbnail: "/images/thumbs/how-to-fix-irql-not-less-or-equal-step-by-step.webp"
faqs:
  - q: "What does IRQL Not Less or Equal mean in plain English?"
    a: "Stop code 0x0000000A: a driver tried to access a region of memory it wasn't allowed to touch at that moment — specifically, it touched paged memory while running at a high interrupt level where only non-paged memory is safe. Windows halted the system to prevent corruption."
  - q: "Which drivers cause IRQL Not Less or Equal most often?"
    a: "Network drivers (Wi-Fi and Ethernet), graphics drivers, and storage drivers lead the list, because they operate at the elevated interrupt levels where this violation happens. Antivirus filter drivers are another frequent offender."
  - q: "Can bad RAM cause IRQL Not Less or Equal?"
    a: "Yes. Faulty memory can corrupt the pointers drivers use, making a healthy driver access the wrong address — which looks exactly like a driver bug. If driver updates don't help, or crashes name different drivers each time, test your RAM."
  - q: "How do I stop this error from coming back?"
    a: "Keep the specific driver that caused it updated from the manufacturer's site (not just Windows Update), avoid beta drivers on a daily-use laptop, and don't run two security products simultaneously. Most recurrences trace to one of those three."
---
IRQL_NOT_LESS_OR_EQUAL is the most common driver-caused blue screen in Windows, and the fix is a proper detective sequence: identify the driver, deal with that driver, verify the hardware underneath. This guide gives you that sequence as numbered steps to follow exactly — no branching decisions until the evidence tells you to branch.

Set aside about an hour. You'll need administrator access, an internet connection for driver downloads, and ideally the ability to reboot several times. Pen and paper (or a notes app) for writing down driver names — you'll need them.

## Why this happens

The thirty-second background so each step makes sense:

- **A driver accesses invalid memory.** The classic cause: a buggy or mismatched driver reads or writes memory at an elevated interrupt request level (IRQL) where that memory isn't available. Network, graphics, and storage drivers do this most.
- **Two drivers conflict.** Antivirus plus another antivirus, or old driver remnants conflicting with a new install, create the invalid-access conditions.
- **Corrupted system files** make valid drivers behave invalidly — the driver is fine, but the memory map it relies on is damaged.
- **Failing RAM** corrupts driver pointers, producing crashes that blame different drivers each time — the signature of hardware, not software.
- **Overclocking instability** causes the CPU to miscalculate addresses under load, which surfaces as IRQL violations during heavy use.
- **A Windows update replaced a working driver** with a generic or newer-but-buggy one, and the crashes started within days of the update.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Capture the evidence

Step one of any driver hunt: find out *which* driver.

1. Press **Win + R**, type `eventvwr.msc`, press Enter. Go to **Windows Logs > System**.
2. Find the **Error** entries with source **BugCheck** at your crash times. Double-click the most recent one and read the details — write down any `.sys` filename mentioned (for example `Netwtw10.sys`, `nvlddmkm.sys`, `rt640x64.sys`).
3. If Event Viewer names nothing useful, check `C:\Windows\Minidump` for `.dmp` files and open the newest with a dump-viewer tool — the faulting driver is at the top of the stack.
4. Google the filename plus the word "driver." Within two minutes you'll know the hardware and the vendor. Write down: driver name, device, vendor. This note drives every step below.

### Fix 2: Update that specific driver from the manufacturer

Don't update all drivers — update the guilty one, from the best source.

1. Identify your laptop's exact model (`msinfo32` → **System Model**).
2. Go to the manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or Lenovo's support site), find your model, and download the driver for the device from Fix 1.
3. Install it and restart. For network drivers, also check the chip vendor (Intel, Realtek, MediaTek) for a newer release if the manufacturer's is old.
4. Use the laptop through the scenario that crashed before. One clean day of the trigger scenario = fixed. If it crashes again within a day, proceed — the new driver didn't solve it.

### Fix 3: Roll back if the crashes started with an update

If your notes say crashes began right after a driver or Windows update, undo it.

1. Open **Device Manager** (**Win + X**), find the device, right-click → **Properties → Driver → Roll Back Driver**.
2. If rollback is unavailable, **Uninstall device** (tick **Attempt to remove the driver for this device**), restart, and let Windows install its inbox driver.
3. Test for a day. Inbox drivers are boring but exceptionally well-behaved — if the crashes stop, the updated driver was the problem.
4. Prevent Windows from reinstalling the bad version: use the **Show or hide updates** troubleshooter from [Microsoft support](https://support.microsoft.com/en-us/windows) to hide that driver update.

### Fix 4: Remove conflicting security software

Two kernel-level security products will eventually produce exactly this crash.

1. Check **Settings > Apps > Installed apps** for more than one antivirus/antimalware product (including "free trials" that came with the laptop).
2. Uninstall all but one — keep either your preferred product or **Microsoft Defender** (built in, free, conflict-free).
3. Use each vendor's dedicated removal tool if offered — filter drivers survive normal uninstalls and keep causing IRQL crashes.
4. Restart and test. If you kept a third-party product and crashes continue, trial a week on Defender alone to isolate whether the product itself is the offender. (If Driver Verifier is enabled on your machine, also read our [Driver Verifier IOManager Violation guide](/articles/how-to-fix-driver-verifier-iomanager-violation/) — the two errors share the same filter-driver suspects.)

### Fix 5: Run SFC and DISM

Eliminate corrupted system files as the hidden cause.

1. **Terminal (Admin)** via **Win + X**. Run `sfc /scannow` — wait for full completion.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` with internet connected.
3. Restart, then retest the trigger scenario.
4. If SFC found and fixed corruption, that may have been the entire problem — corrupted memory-management files make good drivers crash. Give it two days of testing before moving on.

### Fix 6: Test the RAM

The hardware check — essential when dumps blame different drivers each time.

1. Save work. **Win + R** → `mdsched.exe` → **Restart now and check for problems**.
2. At the test screen, press **F1**, select **Extended**, let it complete.
3. Check results: **Event Viewer > Windows Logs > System**, filter **MemoryDiagnostics-Results**.
4. Any errors → reseat or replace the RAM. Clean Extended pass → memory is innocent. Note which outcome you got; it determines whether Fix 7 is driver forensics or hardware replacement. RAM-caused crashes overlap with the [memory corruption blue screens](/articles/how-to-fix-pfn-list-corrupt-in-windows-11-24h2/) — compare your symptoms if the pattern is random.

### Fix 7: Reset overclocks and do a final driver sweep

Close out the remaining variables.

1. Reset BIOS to **Optimized Defaults**; disable XMP; remove any undervolt/overclock utilities' settings.
2. In **Device Manager**, check for any device with a warning icon and resolve it — an unknown or errored device with a half-installed driver is a quiet IRQL risk.
3. Update the **chipset** driver from the manufacturer if you haven't — it's the foundation the other drivers stand on.
4. Final test: a full day of normal use plus the original trigger scenario. If IRQL crashes persist after all seven fixes with clean RAM, you're looking at a motherboard-level fault — document your sequence and contact support or a repair shop.

## Closing

The step that most people skip — Fix 1, writing down the actual driver name — is the step that makes everything else fast. IRQL crashes feel random, but they're nearly always one specific driver doing one specific wrong thing, and the dump tells you which. Follow the evidence, fix that driver, verify the RAM underneath, and this most-common of blue screens becomes a solved problem instead of a recurring mystery. Keep the driver note somewhere; if it ever recurs, you'll know in thirty seconds whether it's the same offender or a new one.
