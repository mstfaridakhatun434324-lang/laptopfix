---
title: "How to Fix SYSTEM_SERVICE_EXCEPTION on Windows 10"
slug: how-to-fix-system-service-exception-on-windows-10
date: 2026-10-12
categories: ["windows-errors"]
tags: ["blue screen", "windows 10", "driver error"]
description: "SYSTEM_SERVICE_EXCEPTION blue screen on Windows 10? Identify the faulty driver or system file and fix it with these proven steps."
thumbnail: "/images/thumbs/how-to-fix-system-service-exception-on-windows-10.webp"
faqs:
  - q: "What causes SYSTEM_SERVICE_EXCEPTION on Windows 10?"
    a: "Usually a faulty third-party driver, most often graphics, webcam, or storage drivers. Windows 10 feature updates are a common trigger because they replace drivers wholesale. Corrupted system files, bad RAM, and disk errors can produce the same stop code less frequently."
  - q: "How do I find which driver caused it?"
    a: "Look for a .sys file name on the blue screen itself, then confirm it in Event Viewer's BugCheck entry. For certainty, analyze the memory dump with WinDbg — our [dump file guide](/articles/best-way-to-read-dump-files-with-windbg/) walks through it step by step."
  - q: "Can antivirus software cause SYSTEM_SERVICE_EXCEPTION?"
    a: "Yes. Third-party antivirus installs kernel-level drivers that hook system services, and a buggy or outdated one crashes exactly this way. If crashes started after an antivirus update, remove it with the vendor's official removal tool and test with Windows Security for a few days."
  - q: "Is this blue screen a sign of a failing hard drive?"
    a: "It can be. If chkdsk finds bad sectors or the crashes happen during disk-heavy operations, back up your data first and check the drive's SMART health. But rule out drivers first — they're the cause far more often than the drive."
---

SYSTEM_SERVICE_EXCEPTION is the blue screen equivalent of a shrug — it means something went wrong while Windows was running a system service, but the message alone doesn't say what. The good news is that the fix pattern is well understood, and the blue screen often drops a hint in the form of a file name.

That file name is your starting point: it usually points at a driver. Our [SYSTEM_SERVICE_EXCEPTION reference](/articles/best-way-to-fix-system-service-exception/) has the background; the steps below turn the hint into a fix. Start at Fix 1.

## Why this happens

- An outdated or corrupted third-party driver — graphics and webcam drivers are frequent offenders on Windows 10.

- A Windows 10 feature update replacing a working driver with a broken one.

- Corrupted system files that a system service depends on.

- Third-party antivirus or firewall drivers conflicting with Windows services.

- Failing RAM corrupting data as services use it.

- Disk errors damaging the system files that services load at boot.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Read the file name on the blue screen

The stop code line sometimes includes a file like asmtxhci.sys or ks.sys. That file identifies the driver or component to fix first.

1. Photograph the blue screen before it disappears, or find the **BugCheck** entry in **Event Viewer > Windows Logs > System** after rebooting.

2. Search the file name online to identify its device — most **.sys** files belong to a specific driver.

3. If the file belongs to a third-party driver, skip to Fix 3 and target that driver directly.

4. If no file is named, work the list in order — the general fixes still apply.

### Fix 2: Boot into Safe Mode and observe

Safe Mode loads a minimal driver set. If the crashes stop there, a third-party driver or startup item is the cause.

1. Hold **Shift** while clicking **Restart** from the Start menu.

2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4**.

3. Use the laptop in Safe Mode for a while — browse, open apps, let it sit.

4. Stable in Safe Mode means the problem is loadable software, not Windows itself. Continue below.

### Fix 3: Update or roll back the suspect driver

Whether it's the named file's driver or just the usual suspects, getting the right driver version installed resolves most of these crashes.

1. Open **Device Manager** and locate the device tied to the named file (or start with **Display adapters** and imaging devices).

2. Try **Properties > Driver > Roll Back Driver** if the crashes began after an update.

3. Otherwise **Uninstall device** (tick **Attempt to remove the driver**), restart, and install the manufacturer's latest driver.

4. Intel hardware users can find theirs via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 4: Run SFC and DISM

When a system service itself is crashing, corrupted Windows files are a strong possibility. Repair them before blaming drivers further.

1. Open **Command Prompt (Admin)** from the **Win + X** menu.

2. Run `sfc /scannow` and wait for it to finish.

3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.

4. Restart and test. These two in sequence fix most file-corruption causes.

### Fix 5: Check the disk

System services load from disk at boot; bad sectors in the wrong place crash them with exactly this stop code.

1. Open **Command Prompt (Admin)** and run `chkdsk C: /f /r`.

2. Type **Y** to schedule the scan and restart — it can take over an hour.

3. Check the outcome in **Event Viewer > Windows Logs > Application** under the **Wininit** source.

4. Widespread bad sectors mean the drive is failing: back up immediately.

### Fix 6: Do a clean boot

If crashes only happen in normal mode, some startup program's driver is the trigger. A clean boot finds it systematically.

1. Press **Win + R**, type `msconfig`, and on the **Services** tab tick **Hide all Microsoft services**, then **Disable all**.

2. In **Task Manager > Startup**, disable all non-Microsoft entries.

3. Restart and test. Re-enable in halves until the crash returns to isolate the culprit.

4. Full instructions are in our [clean boot guide](/articles/best-way-to-perform-clean-boot-windows-11/) — the steps are identical on Windows 10.

### Fix 7: Reset Windows 10 while keeping files

When the crashes survive every targeted fix, the system installation itself is damaged. A keep-my-files reset rebuilds it.

1. Open **Settings > Update & Security > Recovery**.

2. Under **Reset this PC**, click **Get started**.

3. Choose **Keep my files** and follow the prompts.

4. Reinstall your desktop applications afterward. Your documents and photos are preserved.

### Fix 8: Turn off fast startup

Fast startup resumes drivers from a saved hibernation state instead of loading them fresh. When that saved state corrupts, system services crash on every boot with this exact stop code — and a true cold boot clears it.

1. Open **Control Panel > Power Options > Choose what the power buttons do**.

2. Click **Change settings that are currently unavailable**.

3. Untick **Turn on fast startup (recommended)** and click **Save changes**.

4. Shut the laptop down fully — don't just restart — then power it back on.

5. Use it for a few days. If the crashes stop, leave fast startup off permanently.

## Closing

SYSTEM_SERVICE_EXCEPTION is vague by design, but the investigation pattern isn't: read the file name, test in Safe Mode, fix the driver, repair the files. Most cases resolve at the driver step — especially on Windows 10, where feature updates love to replace working drivers. If you've reached the reset step, take it as a fresh start rather than a defeat; a clean system with current drivers is the most stable thing you can run. Fast startup is one of those features that works perfectly until it doesn't — and when it corrupts, the symptoms look like everything except fast startup. Modern SSDs boot fast enough without it, and a true cold boot every time is one less variable in your troubleshooting life.
