---
title: "CompatTelRunner.exe High CPU on a Lenovo Laptop? Fix It"
slug: how-to-fix-compattelrunner-high-cpu-on-lenovo-laptop
date: 2026-09-04
categories: ["performance"]
tags: ["compattelrunner", "telemetry", "high cpu", "lenovo laptop", "windows 11"]
description: "CompatTelRunner.exe (Windows Compatibility Telemetry) spiking CPU on your Lenovo laptop? Tame or disable the telemetry runner safely."
thumbnail: "/images/thumbs/how-to-fix-compattelrunner-high-cpu-on-lenovo-laptop.webp"
faqs:
  - q: "What is CompatTelRunner.exe?"
    a: "CompatTelRunner.exe is the Microsoft Compatibility Telemetry runner — it collects system compatibility data (installed apps, drivers, device info) that Microsoft uses to assess upgrade readiness and reliability. It runs periodically via scheduled tasks. It is a legitimate Microsoft process, not malware, but its scans can spike CPU and disk usage for extended periods, especially on laptops."
  - q: "Is it safe to disable CompatTelRunner.exe?"
    a: "Yes, for individual users. Disabling its scheduled tasks stops the telemetry collection without affecting Windows updates, security, or stability — Microsoft just gets less diagnostic data from your machine. Enterprises managed by IT may have policies requiring it, but on a personal Lenovo laptop, disabling it is a common and safe optimization."
  - q: "Why does CompatTelRunner use so much CPU on Lenovo laptops?"
    a: "Lenovo machines often carry large factory software loads, and CompatTelRunner inventories all of it — more installed apps and drivers means longer, heavier scans. It also tends to run at inconvenient times (right after boot or during active use) rather than when idle, making its CPU usage far more noticeable than on cleaner systems."
  - q: "Will disabling telemetry break Windows Update?"
    a: "No. Windows Update functions independently of compatibility telemetry. Disabling CompatTelRunner's tasks doesn't block security patches, driver updates, or feature updates. At most, Microsoft has slightly less data about your specific configuration when assessing update rollouts — which doesn't affect what updates you receive."
---

`CompatTelRunner.exe` — Microsoft Compatibility Telemetry — periodically wakes up on your Lenovo laptop and hammers the CPU and disk for twenty minutes, an hour, sometimes longer. You're not installing anything, you're not updating; the machine is just busy... reporting on itself.

The telemetry scans your installed software, drivers, and system configuration to feed Microsoft's compatibility analytics. Legitimate, but badly timed and occasionally stuck in loops. On Lenovo machines with heavy factory software loads, the scans are longer and more intrusive. Here's how to calm it down — from polite rescheduling to full disable — without breaking anything.

## Why this happens

- **Scheduled telemetry tasks firing at bad times**: The tasks run on Microsoft's schedule, not when you're idle.
- **Large factory software inventory**: Lenovo's preinstalled apps mean longer, heavier scans.
- **Stuck or looping scan**: A corrupted telemetry state causing repeated full scans instead of quick deltas.
- **Post-update assessment runs**: Feature updates trigger intensive compatibility data collection.
- **Multiple telemetry tasks overlapping**: Appraiser, telemetry runner, and related tasks stacking up.
- **Disk-heavy inventory on HDDs**: Spinning-disk Lenovos suffer disproportionately during scans.
- **Lenovo telemetry adding on top**: Lenovo's own telemetry services running concurrently with Microsoft's.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's actually CompatTelRunner

Verify before you disable anything.

1. Open Task Manager > **Details** tab, find **CompatTelRunner.exe** — note its CPU and disk numbers.
2. Right-click > **Open file location** — genuine file lives in `C:\Windows\System32`. Anything else: scan immediately.
3. Check **Task Scheduler** > **Task Scheduler Library** > **Microsoft** > **Windows** > **Application Experience** — you'll see tasks like **Microsoft Compatibility Appraiser**. Check their **Last Run Time** — does it match when your CPU spikes?
4. Note the pattern: does it run for 15 minutes and finish (normal, just badly timed), or run for hours/constantly (stuck)?
5. Normal-but-annoying → reschedule (Fix 2). Stuck → disable and reset (Fixes 3–4).

### Fix 2: Reschedule telemetry to idle hours

The polite fix — keep the data flowing, move it out of your way.

1. Open **Task Scheduler** (`taskschd.msc`) > **Microsoft** > **Windows** > **Application Experience**.
2. Right-click **Microsoft Compatibility Appraiser** > **Properties** > **Triggers** tab.
3. Change the trigger to a time you're asleep (e.g., 3 AM), and on the **Conditions** tab check **Start the task only if the computer is idle for** 30 minutes, plus **Stop if the computer ceases to be idle**.
4. Uncheck **Wake the computer to run this task** if you don't want 3 AM wake-ups.
5. Do the same for related tasks in **Customer Experience Improvement Program** folder.
6. This preserves Microsoft's telemetry (harmless to you) while ending the mid-workday CPU spikes. If background load is high in general, our [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) helps trim the rest of the auto-starting crowd.

### Fix 3: Disable the telemetry tasks

The common fix — safe on personal machines.

1. In **Task Scheduler**, navigate to **Microsoft** > **Windows** > **Application Experience**.
2. Right-click **Microsoft Compatibility Appraiser** > **Disable**.
3. Also disable telemetry tasks under **Customer Experience Improvement Program** (consolidator, kernel CEIP tasks).
4. Check **Microsoft** > **Windows** > **Autochk** — no, leave that one; it's disk checking, not telemetry. Only disable the clearly telemetry-named tasks.
5. Reboot and monitor for a few days — CompatTelRunner.exe should never appear in Task Manager again.
6. Revisit after major feature updates — they occasionally re-enable these tasks. A quick Task Scheduler check post-update keeps them off.

### Fix 4: Reduce diagnostic data and telemetry via Settings

Lower the telemetry level so less runs.

1. **Settings** > **Privacy & security** > **Diagnostics & feedback** > **Diagnostic data** — set to the minimum available (**Required** only, toggle off optional).
2. Turn off **Improve inking and typing**, **Tailored experiences**, and **View diagnostic data** options on the same page.
3. Less diagnostic data = less for CompatTelRunner to collect and upload = shorter runs if you kept the tasks enabled.
4. In **Settings** > **Privacy & security** > **General**, turn off advertising ID and suggestion options — unrelated to CPU, but part of the same data-minimization hygiene.
5. Note: on some builds the "Required only" option needs no further action; the scheduled tasks respect the reduced scope automatically.

### Fix 5: Quiet Lenovo's own telemetry

Lenovo adds its telemetry on top of Microsoft's.

1. Open **Lenovo Vantage** > **Settings** (gear icon) — find **participation** or **data collection** options and opt out.
2. In **Task Scheduler**, look for Lenovo-named tasks (telemetry, "experience improvement," data collection) — disable the aggressive ones, keep update-related tasks.
3. Task Manager > **Startup apps** — disable Lenovo telemetry/analytics startup entries.
4. In **Services** (`services.msc`), Lenovo telemetry services can usually be set to **Manual** safely — keep the ones tied to drivers and updates on Automatic.
5. Don't gut everything Lenovo — Vantage handles driver/BIOS updates well. Just silence the data-collection extras. Lenovo's support site ([Lenovo Support](https://support.lenovo.com/us/en/)) documents which services are essential.

### Fix 6: Clear a stuck telemetry state

When the runner loops instead of finishing.

1. Disable the tasks first (Fix 3) — stop the bleeding.
2. Open an elevated terminal and clear the telemetry data store: the appraiser cache lives under `C:\Windows\System32\CompatTel` and related data in `C:\ProgramData\Microsoft\Diagnosis` — rather than deleting manually, run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` to repair the components.
3. Check **Settings** > **System** > **Storage** > **Temporary files** — clear **Delivery Optimization Files** and temp data that can wedge telemetry uploads.
4. Re-enable the tasks temporarily as a test: if the runner now completes in 15 minutes and goes quiet, the stuck state is cleared — then disable again if you prefer it off.
5. If it immediately loops again, keep it disabled and move on — some configurations just don't get along with the appraiser.

### Fix 7: The Group Policy / registry route (Pro)

A more durable disable for Windows 11 Pro.

1. `Win + R` > `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Data Collection and Preview Builds**.
2. Set **Allow Telemetry** (or **Allow Diagnostic Data**) to **Enabled** with the lowest option (0/Security or 1/Basic depending on build).
3. This policy-level setting survives feature updates better than Task Scheduler disables.
4. On Home edition (no gpedit), the Task Scheduler method (Fix 3) plus Settings (Fix 4) achieves the same practical result.
5. Verify after the next cumulative update — check Task Scheduler to confirm the tasks stayed disabled, and Task Manager to confirm the runner stays quiet.
6. For broader background-process hygiene, our [clean boot guide](/articles/how-to-perform-clean-boot-windows-11-on-laptop/) helps identify any other telemetry-adjacent CPU consumers. Microsoft documents diagnostic data controls at [Windows support](https://support.microsoft.com/en-us/windows).

## Closing

CompatTelRunner high CPU is Microsoft's telemetry running at the worst possible times on a software-heavy Lenovo. Reschedule it to the night, or disable the tasks entirely — both are safe on a personal machine and neither affects updates or stability. Your laptop's CPU is yours; telemetry doesn't get to spend it during your workday.
