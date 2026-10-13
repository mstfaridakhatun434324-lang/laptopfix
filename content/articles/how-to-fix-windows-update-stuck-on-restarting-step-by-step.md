---
title: "Update Stuck on 'Restarting'? The Full Step-by-Step Rescue"
slug: how-to-fix-windows-update-stuck-on-restarting-step-by-step
date: 2026-10-10
categories: ["windows-update"]
tags: ["update stuck", "restarting screen", "frozen", "step by step", "windows 11"]
description: "Windows update frozen on the Restarting screen? This step-by-step rescue walks you from safe waiting through forced recovery to a clean retry."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-step-by-step.webp"
faqs:
  - q: "How long is too long on the Restarting screen?"
    a: "On an SSD with a normal cumulative update, 15 to 30 minutes is typical; large feature updates can legitimately take 60 to 90 minutes. The screen becomes suspicious after 90 minutes with zero disk activity and a frozen spinner. At the two-hour mark with no activity, treat it as hung and start the recovery steps."
  - q: "Will force-shutting down corrupt my Windows?"
    a: "Windows is built to survive this: the update is transactional, so an interrupted install rolls back to the previous working state automatically. The real risk isn't corruption — it's impatience. Wait the full diagnostic period first, keep the charger connected, and the forced shutdown is safe."
  - q: "What if it gets stuck on Restarting again after I fix it?"
    a: "A repeat hang means you haven't found the trigger yet — usually a USB peripheral, an outdated storage driver, or a poisoned update cache. The steps below address each in turn; if the second attempt also hangs at the same point, the manual-install step bypasses the automatic path entirely."
  - q: "Does Safe Mode help with a stuck restarting update?"
    a: "Yes — if the system boots, Safe Mode loads a minimal driver set that often lets a wedged update service reset itself. It's also the cleanest environment for clearing the update cache, which is why it appears as a dedicated step below."
---

The blue "Restarting" screen with its frozen spinning dots is the most stressful sight in Windows Update troubleshooting — because every instinct screams "don't touch it" while the clock screams "it's been two hours." Both instincts have a point. Some updates genuinely take 90 minutes on this screen; others are deadlocked and will sit there until the heat death of the universe. This guide tells you how to tell the difference and what to do about each.

The method is: verify it is actually stuck (not just slow), recover safely, remove the trigger, then retry cleanly. Do not skip the verification — about half of all "stuck" reports turn out to be slow-but-working updates that would have finished if left alone. For the HP-specific variant of this problem, see our [HP restarting-freeze guide](/articles/how-to-fix-windows-update-stuck-on-restarting-on-hp-laptop/).

Two quick diagnostic checks before anything else: does the Caps Lock light still toggle? If yes, the kernel is alive and the update may be working — wait longer. Is there any disk activity at all — drive light flickering, faint seeking sounds? Any activity means progress, even if the percentage display hasn't moved. A truly dead system shows none of these: frozen spinner, dark drive light, unresponsive Caps Lock. Only that combination justifies the forced shutdown in Fix 2.

## Why this happens

- **Slow servicing mistaken for a hang**: Big updates can take over an hour on this screen legitimately.
- **USB peripheral deadlock**: Docks, external drives, and hubs blocking the restart handshake.
- **Outdated storage/chipset drivers**: Mishandled power transitions during restart.
- **Corrupt update payload**: A damaged package hanging at the apply phase.
- **Stuck reboot flags**: Leftover pending-operation flags from a previous failed install.
- **Fast Boot / firmware quirks**: Firmware skipping initialization the update expects.
- **Antivirus locking files**: Real-time protection interfering with the restart-phase file operations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the hang — the 90-minute rule

Patience with a purpose.

1. Plug in the charger immediately — this is non-negotiable.
2. Note the time. Watch for disk activity (drive light, sounds) for the next stretch.
3. If there is **any** activity, it is working — leave it alone, even past an hour.
4. If the spinner is frozen and there is zero activity for **90+ minutes**, it is hung. Proceed to Fix 2.

### Fix 2: Forced shutdown and automatic recovery

Safe when done correctly.

1. Hold the **power button 10 seconds** until fully off.
2. Disconnect the charger, wait **30 seconds**, reconnect, power on.
3. Windows will resume, roll back ("Undoing changes"), or boot normally — all three are acceptable outcomes. A rollback means the system protected itself; if it loops on undoing changes, see our [undoing-changes guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update/).

### Fix 3: Boot into Safe Mode and clear the cache

The clean-room retry preparation.

1. Hold **Shift** + click **Restart** → **Troubleshoot > Advanced options > Startup Settings > Restart** → press **4** for Safe Mode.
2. In Safe Mode, open elevated Terminal: `net stop wuauserv`, `net stop bits`.
3. Rename `C:\Windows\SoftwareDistribution` → `SoftwareDistribution.old`.
4. Restart normally — the cache rebuilds clean on next check.

### Fix 4: Strip peripherals and retry

The most common real trigger.

1. Power off fully. Unplug **everything USB** — docks, hubs, drives, printers.
2. Connect the charger directly to the laptop (no dock passthrough).
3. Boot, go to **Settings > Windows Update**, and retry with only the charger attached.

### Fix 5: Update storage and chipset drivers first

Old drivers mishandle the restart handoff.

1. Get the latest **chipset** and **storage (IRST/NVMe)** drivers from your laptop maker's support site — or use Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel-based machines.
2. Install, restart, then retry the Windows update. Pay special attention to the storage driver: the restart phase hands disk control between Windows and firmware, and an outdated Intel RST or NVMe driver is the single most common driver-level cause of restart hangs.
3. Also check for a BIOS update from the manufacturer; firmware fixes for restart hangs are common. Apply BIOS updates with the charger connected and never interrupt the flash — a failed BIOS update is far worse than a stuck Windows update.

### Fix 6: Disable Fast Startup temporarily

Hybrid shutdown state can wedge the restart sequence.

1. Go to **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Shut down fully (not restart), power on, and retry the update. Re-enable afterward if you like.

### Fix 7: Manual install from the Update Catalog

When the automatic restart path keeps hanging, sidestep it.

1. Note the KB number from **Update history**.
2. Download the package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. With peripherals disconnected and AV temporarily uninstalled, run the `.msu` and let it manage its own restart.

## Closing

The stuck-Restarting rescue is really two skills: knowing when to wait (90 minutes, charger in, watch for activity) and knowing what to remove before retrying (peripherals, stale cache, old drivers). Master those and this screen loses its terror — it becomes a 20-minute detour instead of a lost evening. The single best prevention: keep chipset and storage drivers current, and never update through a docking station.

One last piece of advice for the aftermath: after you recover and successfully install the update, restart the laptop one more time and use it normally for an hour before declaring victory. Occasionally a recovered system hides a secondary issue — a driver that installed half-configured, a service that didn't restart — that only shows up under normal use. An hour of ordinary browsing and work is the real test, and it's much easier to fix a small leftover glitch now than to discover it during your next important video call. File this whole experience under hard-won knowledge: the next time an update lingers on "Restarting," you'll know the drill — verify, wait, recover, remove the trigger — instead of staring at the screen in dread.
