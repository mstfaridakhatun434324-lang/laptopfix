---
title: "Windows Update Stuck on 'Restarting' on HP Laptop — Break the Freeze"
slug: how-to-fix-windows-update-stuck-on-restarting-on-hp-laptop
date: 2026-10-05
categories: ["windows-update"]
tags: ["update stuck", "restarting", "hp laptop", "frozen update", "windows 11"]
description: "HP laptop frozen on the 'Restarting' screen during a Windows update? Learn the safe way to break the freeze, finish the install, and prevent it next time."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-on-hp-laptop.webp"
faqs:
  - q: "How long should I wait on the Restarting screen before forcing it?"
    a: "Wait at least 45 to 60 minutes with the charger plugged in before doing anything drastic. Large feature updates genuinely sit on 'Restarting' for a long time while servicing the image. But if the spinner is frozen, the hard drive light shows zero activity, and two hours have passed, the update is hung — not slow — and it's safe to move to the fixes below."
  - q: "Is it safe to force-shutdown during a stuck update?"
    a: "It's a last resort, but Windows is designed to roll back gracefully: hold the power button for 10 seconds, wait 30 seconds, and power on. In most cases the update either resumes or automatically rolls back to the previous state. Forcing shutdown is far safer than leaving a hung machine baking for a full day."
  - q: "Why does this happen specifically on HP laptops?"
    a: "HP's Fast Boot firmware setting, HP BIOS update utilities running alongside Windows Update, and older HP storage or chipset drivers are common contributors. The restart phase hands control between Windows and firmware, and HP firmware quirks can stall that handoff."
  - q: "Will I lose files if I interrupt the stuck restart?"
    a: "Your personal files are almost never at risk — the update works on system files, and the rollback mechanism restores the previous system state automatically. Your documents and photos aren't touched during this phase at all. Still, keeping a current backup before major updates is always wise practice."
---

There is a special kind of dread reserved for the blue "Restarting" screen that does not restart. The spinning dots are frozen, the fan may be quiet or roaring, and your HP laptop has been sitting there for an hour. Maybe two. Touching it feels wrong — every instinct says never interrupt an update — but at some point waiting becomes the worse option. Here is how a technician handles it: a disciplined waiting period first, then a safe forced recovery, then the fixes that stop it happening again.

HP laptops hit this more than average because of how their firmware interacts with the Windows restart handoff: Fast Boot settings, HP's own update agents, and chipset drivers that do not fully support the restart signaling Windows expects. None of that means your laptop is broken. Follow the order below and do not skip the waiting step — roughly half of "stuck" updates are just slow ones. For the general step-by-step version of this fix, see our [comprehensive restarting-fix guide](/articles/how-to-fix-windows-update-stuck-on-restarting-step-by-step/).

One more thing before you start: note exactly what the screen shows. A spinning circle of dots that still animates means Windows is alive and possibly working; a completely frozen frame with no animation for over an hour means it is truly hung. Also check whether the Caps Lock key still toggles its light — if it does, the system is responsive underneath and patience is the right call. These two observations take ten seconds and prevent the most common mistake: force-restarting a healthy update mid-install.

## Why this happens

- **Genuinely slow servicing**: Large updates can sit on "Restarting" for 45+ minutes while the servicing stack works — this looks stuck but isn't.
- **HP Fast Boot firmware setting**: Aggressive fast-boot skips initialization steps the update's restart sequence expects, stalling the handoff.
- **Conflicting HP update agents**: HP Support Assistant or HP BIOS Update utility running during the Windows restart competes for firmware access.
- **Outdated chipset/storage drivers**: Old drivers mishandle the power-state transitions during restart.
- **Stuck pending operations**: A previous failed install left `PendingFileRenameOperations` or reboot flags that deadlock the restart.
- **USB peripherals interfering**: Docking stations, external drives, and USB hubs can block the restart handshake on HP firmware.
- **Corrupt update payload**: A partially downloaded update that passed verification can hang when it tries to apply.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: The disciplined wait — confirm it is really stuck

Do not touch anything for the first hour. Seriously.

1. Plug in the charger — a battery dying mid-restart is the one thing that can turn this into a real disaster.
2. Watch the hard drive activity light (if your HP has one) or listen for disk sounds. Activity means it is working.
3. Wait a full **60 minutes** on first occurrence. Feature updates legitimately take this long on spinning disks and older SSDs.
4. If the spinner is completely frozen and there has been zero activity for over an hour, it is hung — proceed to Fix 2.

### Fix 2: Force the shutdown safely

The last resort that is safer than it sounds.

1. Press and hold the **power button for 10 full seconds** until the laptop powers off completely.
2. Unplug the charger, wait **30 seconds** (this drains residual power and clears the hung state), then plug back in and power on.
3. Windows will either resume the update, roll it back automatically ("Undoing changes made to your computer"), or boot normally.
4. If it rolls back, that is a success — the system protected itself. Now fix the cause before retrying (Fixes 3–6).

### Fix 3: Disconnect everything and retry

Peripherals are a top HP-specific cause of restart hangs.

1. Shut down fully, then unplug **all USB devices**: docks, hubs, external drives, printers, even the mouse if you can spare it.
2. If you use an HP docking station, connect the charger directly to the laptop instead.
3. Power on, go to **Settings > Windows Update**, and retry the update with only the charger attached.

### Fix 4: Update HP drivers and BIOS before retrying

HP publishes driver updates that specifically fix restart-handoff issues.

1. Open **HP Support Assistant** or visit [HP Support](https://support.hp.com/us-en), enter your model, and install all **BIOS**, **chipset**, and **storage** updates.
2. Restart after each BIOS update (HP's installer will guide you — never interrupt a BIOS flash).
3. With firmware current, retry the Windows update. Updated firmware handles the restart signaling correctly.

### Fix 5: Clear the stuck update state in WinRE

If Windows boots to the desktop but the update immediately tries and hangs again, clear the deck first.

1. Hold **Shift** while clicking **Restart** to enter the Windows Recovery Environment.
2. Go to **Troubleshoot > Advanced options > Command Prompt**.
3. Run: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` (use `dir C:` to confirm the drive letter in WinRE).
4. Select **Continue** to boot normally, then check for updates fresh. Guidance for recovery-environment repairs is also documented at the [Windows update support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Disable Fast Boot in BIOS/UEFI

HP's Fast Boot can stall the update restart handoff.

1. Restart and press **F10** repeatedly to enter BIOS Setup.
2. Navigate to **Advanced > Boot Options** and disable **Fast Boot**.
3. Save and exit (F10), boot to Windows, and retry the update.
4. You can re-enable Fast Boot afterward if boot times matter to you — but leave it off during update days.

### Fix 7: Run the update manually from the Microsoft Update Catalog

Bypass the flaky automatic path entirely.

1. Note the KB number from **Settings > Windows Update > Update history**.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. With peripherals disconnected and HP utilities closed, run the installer and let it handle the restart itself.

## Closing

A stuck "Restarting" screen on an HP laptop is scary but survivable: wait the hour, force the shutdown if it is truly hung, then fix the underlying cause — usually peripherals, firmware, or a poisoned cache — before retrying. The one rule that never changes: charger plugged in, always. A power loss during the restart phase is the only version of this problem that can genuinely brick a machine. And if the forced recovery lands you in the "undoing changes" loop instead of a clean boot, our [undoing-changes recovery guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update/) covers that next step.
