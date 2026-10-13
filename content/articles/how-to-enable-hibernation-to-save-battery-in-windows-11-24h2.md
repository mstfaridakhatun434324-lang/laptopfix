---
title: "How to Enable Hibernation on Windows 11 to Save Battery"
slug: how-to-enable-hibernation-to-save-battery-in-windows-11-24h2
date: 2026-09-11
categories: ["battery"]
tags: ["hibernation", "save battery", "power settings", "windows 11 24h2"]
description: "Hibernation saves your session to disk and uses zero battery. Learn how to enable it on Windows 11 24H2 and make it your default lid-close action."
thumbnail: "/images/thumbs/how-to-enable-hibernation-to-save-battery-in-windows-11-24h2.webp"
faqs:
  - q: "What is the difference between sleep and hibernation?"
    a: "Sleep keeps your session in RAM, which still draws a small amount of battery — typically one to three percent per hour. Hibernation writes the entire session to disk and powers the machine fully off, using zero battery. Hibernation is slower to resume but your laptop can sit for weeks without losing charge."
  - q: "Why is hibernate missing from my Windows 11 power menu?"
    a: "Microsoft hides the hibernate option by default on many new laptops in favor of Modern Standby. You can bring it back with a single command (powercfg /hibernate on) or by enabling it in the classic Power Options dialog."
  - q: "Does hibernation wear out an SSD?"
    a: "Not meaningfully. Each hibernation writes a few gigabytes once, which is trivial compared to an SSD's total write endurance rating — typically hundreds of terabytes. Daily hibernation for years still uses only a small fraction of a modern SSD's lifespan."
  - q: "Can I make my laptop hibernate when I close the lid?"
    a: "Yes. In Control Panel > Power Options > Choose what closing the lid does, set the On battery action to Hibernate. Your open apps and documents are saved to disk and restored exactly when you reopen the lid."
---
Sleep mode is convenient, but it is not free. A sleeping laptop keeps its RAM powered, which quietly sips one to three percent of battery every hour. Leave it in a bag over a long weekend and you can come back to a dead machine — or worse, a battery drained so deep it takes a while to revive. Hibernation solves this completely: it snapshots everything to disk and shuts the machine fully off, drawing zero power.

On Windows 11 24H2, hibernation is often hidden rather than missing. Microsoft pushes Modern Standby on new hardware and tucks the hibernate option out of sight. This guide brings it back, wires it into your power menu and lid, and tunes it so your battery stops leaking overnight.

## Why this happens

- **Hibernate is disabled by default:** many 24H2 installations ship with hibernation turned off, especially on laptops with Modern Standby.
- **The hiberfil.sys file is missing or too small:** without the hibernation file on the system drive, the option cannot appear.
- **Fast Startup confusion:** Fast Startup uses a partial hibernation, and its settings interact with full hibernation in ways that hide the option.
- **Group Policy or OEM configuration:** some business laptops and OEM images disable hibernation via policy.
- **Low disk space:** Windows needs free space roughly equal to your RAM size for the hibernation file, and hides the option when space is tight.
- **Outdated chipset drivers:** on some platforms the hibernate path depends on chipset drivers that Windows Update did not install.
- **Modern Standby (S0) replacing S3 sleep:** on S0 systems the classic sleep states behave differently, which changes how hibernation is exposed.

## How to fix it

Work through these in order. Most people only need the first two.

### Fix 1: Turn hibernation on with powercfg

The single command that enables the whole feature.

1. Open **Terminal (Admin)** — right-click the Start button and choose it.
2. Run `powercfg /hibernate on` and press Enter. There is no confirmation message; silence means success.
3. Verify with `powercfg /availablesleepstates` — **Hibernate** should now be listed.
4. If you get an error about the hibernation file, free up disk space first (see Fix 5).

### Fix 2: Add Hibernate to the power menu and lid actions

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do**, then **Change settings that are currently unavailable**.
3. Check **Hibernate** under shutdown settings so it appears in the Start menu power options.
4. On the same page, set **When I close the lid** to **Hibernate** for the **On battery** column. Keep **Plugged in** on Sleep if you prefer faster resumes at your desk.
5. Click **Save changes**.

### Fix 3: Make hibernation automatic at low battery

This is the real battery saver: the laptop hibernates itself before the battery dies.

1. In **Power Options**, click **Change plan settings** next to your active plan, then **Change advanced power settings**.
2. Expand **Battery > Critical battery action** and set **On battery** to **Hibernate**.
3. Expand **Battery > Low battery level** and set it to around 15 percent, and **Critical battery level** to 7 percent.
4. Click **OK**. Now the machine protects itself even if you forget it in a bag.

### Fix 4: Fix hibernation when the command fails

1. If `powercfg /hibernate on` reports that the system firmware does not support hibernation, update your BIOS from the manufacturer's support site first.
2. Run `sfc /scannow` in an elevated terminal to repair corrupted power components.
3. Check **Device Manager** for warning icons under **System devices** — a broken chipset driver can block the hibernate path. Install the chipset driver from your maker's support page.

### Fix 5: Free space for the hibernation file

1. Windows needs contiguous free space roughly equal to 40–100 percent of installed RAM for hiberfil.sys.
2. Open **Settings > System > Storage** and run **Cleanup recommendations** to reclaim space.
3. You can shrink the file with `powercfg /hibernate /size 50` in an elevated terminal, which sets it to 50 percent of RAM — enough for most systems.
4. Re-run `powercfg /hibernate on` after cleanup.

### Fix 6: Handle hibernation on Modern Standby laptops

1. On S0 Modern Standby systems, closing the lid may use "connected standby" instead of your hibernate setting.
2. Go to **Settings > System > Power & battery > Screen, sleep, & hibernate timeouts** and set the sleep timeouts short, so the machine reaches hibernate faster.
3. In the advanced power settings, look for **Sleep > Allow hybrid sleep** and turn it **Off** on battery — hybrid sleep can interfere with clean hibernation.
4. Test by closing the lid for a minute: the power light should go fully dark, not pulse.

### Fix 7: Verify zero drain with a battery report

1. Before relying on hibernation for a trip, test it: note the battery percentage, hibernate for a few hours, then resume.
2. The percentage should be identical. If it dropped, the machine slept instead of hibernating — recheck Fix 2's lid settings.
3. For deeper analysis, run `powercfg /batteryreport` in **Terminal (Admin)** and check the recent usage section for unexpected drain during the hibernate window. Our [battery report guide](/articles/how-to-generate-battery-report-windows-11-powercfg/) explains how to read it.

## Closing

Hibernation is the closest thing to a free lunch in battery management: everything saved, zero drain, no downside beyond a slightly slower wake. Two minutes in the terminal and the Power Options dialog turn it on, and the automatic low-battery hibernate means you never come back to a dead laptop again. Set it once and forget it — it's the most reliable battery insurance Windows offers. Your laptop will thank you every morning with a full charge.

Pair it with [disabling Fast Startup to cut idle drain](/articles/how-to-disable-fast-startup-to-fix-battery-drain-in-windows-11-24h2/) and our guide to [finding battery-draining apps](/articles/how-to-find-which-app-is-draining-battery-in-windows-11-24h2/) for a complete battery-saving setup. Microsoft documents the powercfg options at [Microsoft support](https://support.microsoft.com/en-us/windows).
