---
title: "How to Turn Off Fast Startup to Fix Battery Drain"
slug: how-to-disable-fast-startup-to-fix-battery-drain
date: 2026-09-27
categories: ["battery"]
tags: ["fast startup", "battery drain", "shutdown"]
description: "Fast Startup can keep hardware powered after shutdown and drain your battery overnight. Here's how to turn it off properly."
thumbnail: "/images/thumbs/how-to-disable-fast-startup-to-fix-battery-drain.webp"
faqs:
  - q: "What is Fast Startup and why does it drain the battery?"
    a: "Fast Startup is a Windows feature that hibernates the kernel session instead of fully shutting down, so the next boot is faster. Because the shutdown is not complete, some hardware and drivers stay partially powered, which can drain the battery overnight — especially on laptops with buggy drivers."
  - q: "Will disabling Fast Startup make my laptop slower to boot?"
    a: "Slightly, on older machines with spinning hard drives. On modern laptops with SSDs, the difference is usually just a few seconds and barely noticeable. The battery savings and the cleaner hardware initialization are worth the trade for most users."
  - q: "How do I know if Fast Startup is causing my drain?"
    a: "Test it: charge to a known percentage, shut down fully with Fast Startup on, and check the level in the morning. Then disable Fast Startup, repeat the test, and compare. If the overnight loss shrinks dramatically, Fast Startup was the culprit."
  - q: "Does Fast Startup affect restart too?"
    a: "No. Restart always performs a full kernel reload regardless of the Fast Startup setting. That is why some problems temporarily vanish after a restart but return after a shutdown — the restart bypassed the hibernated kernel state that Fast Startup preserves."
---

Fast Startup sounds like pure benefit: faster boots, no downside. But "shutdown" with Fast Startup enabled is not really a shutdown — Windows saves the kernel session to disk and hibernates instead of powering fully off. On a desktop that distinction barely matters. On a laptop, it means components can remain in a half-powered state all night, sipping battery while you assume the machine is off.

If your laptop loses charge overnight while "shut down," Fast Startup belongs high on the suspect list. Disabling it is safe, reversible, and takes two minutes. This guide shows the proper way to do it and what to check afterward.

## Why this happens

- **Hybrid shutdown:** Fast Startup hibernates the kernel instead of fully powering off, leaving hardware in low-power rather than off states.
- **Buggy drivers:** Some drivers fail to enter their deepest sleep state during hybrid shutdown and keep drawing power.
- **USB power:** Ports can remain powered during hybrid shutdown, feeding connected devices all night.
- **Wake from hybrid state:** The hibernated kernel can be woken more easily than a fully-off machine, restarting drain.
- **Masked issues:** Because restart bypasses Fast Startup, problems appear intermittent — fine after restart, draining after shutdown.
- **Dual-boot conflicts:** Fast Startup's locked disk state causes issues with other operating systems and can keep drives spun up.

## How to fix it

Work through these in order — disable the feature, verify the fix, then handle edge cases.

### Fix 1: Disable Fast Startup in Control Panel

The primary fix, done properly.

1. Press **Win + R**, type `powercfg.cpl`, and press Enter.
2. Click **Choose what the power buttons do** in the left sidebar.
3. Click **Change settings that are currently unavailable** (requires administrator).
4. Under **Shutdown settings**, uncheck **Turn on fast startup (recommended)**.
5. Click **Save changes**. The next shutdown will be a true full shutdown.

### Fix 2: Disable it via Command Prompt (alternative method)

Useful if the Control Panel option is missing or greyed out.

1. Press **Win + X** and open **Terminal (Admin)**.
2. Run `powercfg /h off` — this disables hibernation entirely, which also disables Fast Startup (it depends on the hibernation file).
3. Note: this also removes the **Hibernate** option from power menus. If you want hibernate but not Fast Startup, use Fix 1 instead and leave hibernation on.
4. To re-enable hibernation later without Fast Startup, run `powercfg /h on` and then uncheck Fast Startup via Fix 1.
5. Restart the laptop after making the change so the new shutdown behavior takes effect cleanly.

### Fix 3: Verify with an overnight drain test

Prove the fix worked with a controlled experiment.

1. Charge the battery to a round number like **80 percent**.
2. Shut down the laptop (not sleep, not hibernate) and unplug all peripherals.
3. Leave it overnight — 8 hours minimum.
4. Power on in the morning and note the percentage immediately.
5. A loss of 0–2 percent is normal; anything much higher means another drain source remains — see [overnight drain fixes](/articles/best-way-to-fix-battery-drains-overnight-when-laptop-is-off/) for the full hunt.

### Fix 4: Check hibernation settings as an alternative

If you liked fast resumes, hibernate properly instead.

1. With Fast Startup off, enable true hibernation: run `powercfg /h on` in **Terminal (Admin)** if needed.
2. In `powercfg.cpl`, click **Choose what the power buttons do** and check **Hibernate** so it appears in the power menu.
3. Set the power button or lid-close action to **Hibernate** — this writes the full session to disk and powers off completely, using zero battery.
4. Hibernate gives you the fast resume without the half-powered hardware state that caused the drain.
5. For the Windows 11-specific walkthrough, see [disabling Fast Startup on Windows 11](/articles/how-to-disable-fast-startup-to-fix-battery-drain-on-windows-11/).

### Fix 5: Update drivers that misbehave during hybrid shutdown

Fix the underlying driver bugs too.

1. Even with Fast Startup off, update **chipset**, **USB**, and **network** drivers from your manufacturer's support site.
2. Old drivers that mishandle hybrid shutdown often mishandle sleep as well.
3. In **Device Manager**, check **Universal Serial Bus controllers** for devices with power-management issues.
4. Under each USB Root Hub's **Properties → Power Management**, ensure **Allow the computer to turn off this device to save power** is checked.
5. Retest the overnight drain after updating — the combination of disabled Fast Startup and fixed drivers should eliminate it.

### Fix 6: Address the greyed-out Fast Startup checkbox

When the option will not let you change it.

1. The checkbox requires administrator rights — make sure you clicked **Change settings that are currently unavailable** first.
2. On company-managed laptops, a group policy may enforce Fast Startup; check with your IT administrator.
3. If hibernation is disabled (`powercfg /h off` was run), the Fast Startup option disappears entirely — re-enable hibernation first, then uncheck Fast Startup.
4. Corrupted system files can also hide the option: run `sfc /scannow` in an admin Terminal.
5. As a last resort, the registry-free command-line method in Fix 2 achieves the same result without the checkbox.

### Fix 7: Confirm boot time is still acceptable

Make sure the trade-off is worth it for your machine.

1. Time a cold boot before and after disabling Fast Startup — on SSD laptops the difference is typically 3 to 8 seconds.
2. If boot feels sluggish, trim **Startup apps** in **Task Manager** — that speeds up every boot regardless of Fast Startup.
3. Keep Windows updated; boot optimizations in cumulative updates help.
4. If you dual-boot Linux or another OS, disabling Fast Startup also fixes disk-lock issues — a welcome side benefit.
5. Microsoft documents startup behavior on the [Windows support site](https://support.microsoft.com/en-us/windows). The 24H2-specific steps are in [disabling Fast Startup in Windows 11 24H2](/articles/how-to-disable-fast-startup-to-fix-battery-drain-in-windows-11-24h2/).

## Closing

Fast Startup trades a few seconds of boot time for a shutdown that is not quite a shutdown — and on laptops, that half-awake state can drain the battery overnight. Turning it off is a two-minute change with an easy overnight test to prove it worked. If your "shut down" laptop was losing charge by morning, this is very likely the fix you have been looking for.
