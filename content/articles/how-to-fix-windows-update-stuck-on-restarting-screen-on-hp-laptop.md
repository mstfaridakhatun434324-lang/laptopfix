---
title: "Windows Update Stuck on Restarting Screen on HP Laptop (Fix)"
slug: how-to-fix-windows-update-stuck-on-restarting-screen-on-hp-laptop
date: 2026-10-07
categories: ["windows-update"]
tags:
  - windows update
  - restarting screen
  - hp laptop
  - update stuck
  - winre
description: "HP laptop stuck on the Restarting screen after Windows Update? Learn when to wait, how to force a safe shutdown, and HP-specific recovery steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-screen-on-hp-laptop.webp"
faqs:
  - q: "How long is too long on the Restarting screen?"
    a: >
      On SSD-based HP laptops, 30 to 60 minutes for a major update is the upper end of normal; hard-drive models can legitimately need 90 minutes. It becomes too long when the spinning dots freeze completely and there is no drive light, fan, or heat activity for 30 straight minutes — that combination means stuck, not slow.
  - q: "Will force-shutting down during Restarting corrupt Windows?"
    a: >
      Usually not. Windows applies updates in transactional phases with journaling, so an interrupted phase rolls back cleanly on the next boot — you will typically see Undoing changes, which is the safety net working. The risk is small but nonzero, which is why the guide insists on the waiting deadline before you force it.
  - q: "Why does this keep happening on my HP but not my desktop?"
    a: >
      Laptops — especially HP models with Sure Start firmware verification, custom drivers, and power-saving storage — have more phases in the reboot sequence than desktops, giving updates more places to stall. Keeping HP BIOS and drivers current via HP Support Assistant and disabling Fast Startup closes most of the gap.
  - q: "What if the laptop is stuck in a Restarting loop after I forced the shutdown?"
    a: >
      Boot into WinRE with three interrupted startups, run Startup Repair, and if that fails, uninstall the latest quality update from WinRE. The loop is almost always one bad update phase repeating; removing the update breaks the cycle. Your files remain untouched through both operations.
---

The HP logo appears, the spinning dots circle, the word Restarting sits underneath — and an hour later nothing has changed. A Windows Update that gets stuck on the Restarting screen is especially common on HP laptops, where HP's firmware, Sure Start protection, and custom drivers add extra phases to the reboot sequence that updates must navigate.

The critical skill here is triage: a Restarting screen that is still working looks identical to one that is wedged. Forcing a shutdown during genuine update work risks corruption; waiting forever on a wedged machine wastes your evening. This guide teaches you to tell the difference and gives you the HP-specific recovery ladder.

Your files are almost certainly safe throughout — Windows updates transactionally and rolls back interrupted phases. Follow the steps in order.

## Why this happens

- **Large update finalizing on slow storage:** the Restarting phase includes driver and component finalization that can legitimately take 60+ minutes on HDD-based HP models.
- **HP driver hanging the reboot:** display, audio, or chipset drivers that do not unload cleanly block the restart transition.
- **Fast Startup hybrid boot conflicting:** the hibernated kernel state can clash with the update's expectation of a cold reboot.
- **Corrupted update payload retrying silently:** a damaged download makes the installer loop on one operation behind the static screen.
- **Peripheral blocking the reboot:** USB devices and docks can stall the hardware re-enumeration during restart.
- **HP BIOS/Sure Start extended verification:** firmware-level checks add time and can interact badly with an interrupted update.
- **Nearly full system drive:** the restart phase needs staging room; a cramped C: drive stalls it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait with a deadline and check for signs of life

Do not touch the power button yet. Most Restarting hangs on HP laptops are slow rather than stuck, and patience is the safest tool you own. Interrupting a working update is the one action that can turn a boring wait into genuine corruption, so the deadline matters: it gives legitimate finalization every fair chance while still catching a truly wedged machine before your whole evening disappears.

1. Give it 60 minutes on SSD models, 90 on hard-drive models, from the moment it appeared stuck.
2. Watch the drive activity light and listen for disk or fan activity — steady activity means work is happening.
3. Check the Caps Lock light: if it toggles, Windows is responsive behind the screen.
4. Only when the dots are frozen and all activity has been dead for 30 minutes should you intervene.

### Fix 2: Force a shutdown safely and strip peripherals

When the deadline passes with a truly idle machine, a forced shutdown is correct. Windows will roll back or resume the update on next boot.

1. Unplug all USB devices, docks, external monitors, and SD cards.
2. Hold the power button for 10 seconds until the HP laptop powers off fully.
3. Wait 30 seconds, then power on with only the charger connected.
4. If Windows shows Working on updates or Undoing changes, let it finish uninterrupted.

### Fix 3: Boot to WinRE and run Startup Repair

If the HP laptop loops back to the stuck Restarting screen or will not boot, the Recovery Environment can repair the boot sequence.

1. Interrupt startup three times at the HP logo to reach Automatic Repair.
2. Click Advanced options, then Troubleshoot > Advanced options > Startup Repair.
3. Let it diagnose and repair, rebooting as needed.
4. If Windows boots normally afterward, pause updates for a week before retrying.

### Fix 4: Uninstall the latest update from WinRE

When the stuck restart began with a specific update, removing that update from outside Windows is the cleanest fix.

1. In WinRE go to Troubleshoot > Advanced options > Uninstall Updates.
2. Choose Uninstall latest quality update and wait for completion.
3. Reboot and confirm normal startup.
4. Research the KB number before allowing it again — a [manual catalog install](https://www.catalog.update.microsoft.com/) later may succeed where the automatic one wedged.

### Fix 5: Run HP PC Hardware Diagnostics

Rule out coincidental hardware failure — storage problems love to surface during update-heavy reboots.

1. Power on tapping Esc, then F2 for HP PC Hardware Diagnostics.
2. Run System Tests > Fast Test on storage and memory.
3. Passing hardware means this is purely a software/update issue — continue.
4. A failure ID means contacting HP support; no software fix overcomes bad hardware.

### Fix 6: Disable Fast Startup to prevent recurrences

Fast Startup is a repeat offender in HP restart hangs. Disabling it makes every shutdown a true cold boot that updates handle reliably.

1. Boot into Windows, open Control Panel > Power Options > Choose what the power buttons do.
2. Click Change settings that are currently unavailable.
3. Untick Turn on fast startup and save changes.
4. Restart once normally to confirm clean behavior.

### Fix 7: Reset update components and repair the image

The final software cleanup: clear the cache the interrupted update poisoned, and repair any half-written system files.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv, net stop bits, then ren C:\Windows\SoftwareDistribution SoftwareDistribution.old, then net start wuauserv, net start bits.
3. Run: DISM /Online /Cleanup-Image /RestoreHealth followed by sfc /scannow.
4. Reboot, run Windows Update, and confirm restarts are clean. If the screen goes black instead of showing Restarting, see [black screen after Windows update on HP](/articles/how-to-fix-black-screen-after-windows-update-on-hp-laptop/) and our [step-by-step restarting-screen guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-step-by-step/).

## Closing

An HP laptop stuck on Restarting after an update needs triage first — wait out the legitimate finalization, force the shutdown only when truly idle — then the HP recovery ladder: WinRE repairs, update removal, and Fast Startup disabled for prevention. The pattern rarely repeats once the underlying cause is addressed, and each Patch Tuesday becomes uneventful instead of another evening lost to spinning dots.
