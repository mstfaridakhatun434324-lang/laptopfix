---
title: "Windows Update Stuck on the Restarting Screen on a Lenovo Laptop? Fix It"
slug: how-to-fix-windows-update-stuck-on-restarting-screen-on-lenovo-laptop
date: 2026-09-08
categories: ["windows-update"]
tags: ["stuck on restarting", "lenovo laptop", "windows update", "thinkpad", "ideapad"]
description: "Your Lenovo is frozen on 'Restarting' after a Windows update? Lenovo-specific causes — Vantage drivers, BIOS, Novo button recovery — and safe recovery steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-screen-on-lenovo-laptop.webp"
faqs:
  - q: "How long should I let my Lenovo sit on 'Restarting'?"
    a: "Ninety minutes on SSD models, two hours on hard-drive models. Lenovo's business laptops with encryption take longer — BitLocker overhead during the restart phase is real. Only force a shutdown after an hour of zero disk activity with a frozen spinner, and keep the AC adapter connected the entire time."
  - q: "Why does my ThinkPad hang on restart after every update?"
    a: "The classic ThinkPad pattern is a driver that won't unload — commonly the Intel storage driver, the trackpad driver, or Lenovo's power management driver. Updating these through Vantage rather than Windows Update, and disabling Fast Startup, breaks the cycle for most repeat cases."
  - q: "Can I use the Novo button if the restart hang broke Windows?"
    a: "Yes. The Novo button (small pinhole button beside the power button) boots into the Novo menu outside Windows, offering BIOS setup, boot menu, and system recovery. If a forced restart leaves Windows unbootable, the Novo menu's recovery options are your path back."
  - q: "Should I unplug my Lenovo dock during update restarts?"
    a: "Yes — disconnect ThinkPad docks, USB-C hubs, and external drives before restarting for updates. Docks are a leading cause of restart hangs because the shutdown sequence waits on dock-connected devices that don't respond promptly. Reconnect everything after Windows is fully back up and the update is confirmed installed."
---

Lenovo's restart hangs have a recognizable signature: the ThinkPad or Ideapad sits on "Restarting" far past any reasonable time, and the usual suspects are Lenovo-flavored — the Intel RST storage driver in RAID mode (Lenovo's BIOS default), Lenovo's power management and trackpad drivers that hook shutdown, and the ThinkPad docks that half the business world uses. The generic [24H2 Restarting screen guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/) covers the universal mechanics; this is the Lenovo-specific playbook.

Two Lenovo facts shape everything below. First, Lenovo BIOS defaults to RAID/RST storage mode, which makes the Intel storage driver a participant in every restart — and a hanging participant when it's outdated. Second, Lenovo Vantage manages drivers Windows Update doesn't understand, so the "update your drivers" advice means Vantage specifically, not just Device Manager. Get those two right and most Lenovo restart hangs disappear.

## Why this happens

- **Outdated Intel RST/storage driver**: Lenovo's RAID-mode default makes this driver critical to every restart.
- **Lenovo power/trackpad drivers hanging shutdown**: Model-specific drivers that won't unload cleanly.
- **ThinkPad dock connected**: USB-C/Thunderbolt docks stalling the shutdown sequence.
- **Fast Startup collision**: Hybrid shutdown state conflicting with the update restart.
- **Outdated Lenovo BIOS**: Firmware-level restart handling bugs fixed in newer BIOS.
- **Vantage-managed driver outdated**: Drivers Windows Update can't see or update.
- **BitLocker overhead**: Encryption adding significant time to the restart phase on business models.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's stuck, Lenovo-adjusted timing

Business Lenovos with encryption legitimately take longer. Don't force what isn't stuck.

1. Timer from the Restarting screen: **90 minutes** (SSD), **2 hours** (HDD or BitLocker-encrypted).
2. Listen for drive activity; watch the drive LED if your model has one.
3. Frozen spinner + silent drive for 60+ minutes = stuck. Anything else = wait.
4. Keep AC connected — Lenovo firmware updates and restarts assume wall power.
5. Only continue past this point on a confirmed hang.

### Fix 2: Force off, undock, and restart clean

The dock is suspect number one on ThinkPads. Remove it from the equation.

1. Hold **power** 10 seconds until fully off.
2. **Disconnect the dock**, all USB devices, external monitors, and Ethernet.
3. If BitLocker prompts at boot, enter your recovery key (find it at account.microsoft.com/devices/recoverykey).
4. Power on with only AC connected.
5. Windows typically resumes with "Working on updates" and finishes in 10–30 minutes.
6. Reconnect the dock only after fully booted to the desktop.

### Fix 3: Update storage and chipset drivers via Vantage

The highest-value Lenovo-specific fix. The RST driver in RAID mode is the repeat-hang champion.

1. Open **Lenovo Vantage > System Update** and install all **BIOS**, **chipset**, **storage**, and **Management Engine** updates.
2. Restart as prompted (BIOS updates need AC power).
3. In BIOS (F1 at boot, or Novo button > BIOS Setup), note whether storage mode is **RAID/RST** or **AHCI** — if you're not using RAID features, switching to AHCI uses Microsoft's inbox driver and eliminates RST hangs. (Research your model's procedure; wrong switching can prevent booting — back up first.)
4. Also update **trackpad** and **power management** drivers in Vantage — both hook shutdown.
5. Test with a manual restart before the next update round.

### Fix 4: Disable Fast Startup

The hybrid shutdown collision hits Lenovos as hard as anyone.

1. **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. **Change settings that are currently unavailable**, uncheck **Turn on fast startup**.
3. Save and test a full restart.
4. On BitLocker models, also run `powercfg /hibernate off` then `powercfg /hibernate on` in elevated Command Prompt to rebuild hiberfil.sys.
5. Leave Fast Startup off — the few seconds of boot time aren't worth monthly hangs.

### Fix 5: Update the Lenovo BIOS

Lenovo's BIOS updates routinely fix restart and power-state handling. A year-old ThinkPad BIOS is a hang risk.

1. Check your BIOS version in Vantage or with `wmic bios get smbiosbiosversion`.
2. Compare against the latest for your model on [Lenovo support](https://support.lenovo.com/us/en/).
3. Install via Vantage (preferred) — AC power, don't interrupt, allow auto-restarts.
4. After the BIOS update, re-verify storage/chipset drivers are current — BIOS and drivers interact.
5. The BIOS + driver combination from Fixes 3 and 5 resolves the large majority of repeat Lenovo restart hangs.

### Fix 6: Clean-boot to identify the hanging component

If hangs persist with current BIOS and drivers, isolate the culprit.

1. `msconfig` > hide Microsoft services > **Disable all**; disable all Task Manager startup items.
2. Restart — if fast, a third-party component was hanging shutdown.
3. Re-enable in halves. Lenovo-specific suspects: old **hotkey utilities**, **fingerprint software**, VPN clients, docking station utilities.
4. Update or remove the identified component.
5. If a Lenovo utility is the culprit, check Vantage for its update before uninstalling — Vantage often has the fixed version.

### Fix 7: Novo button recovery for unbootable systems

If a forced restart corrupted the boot, Lenovo's hardware-level recovery bypasses Windows entirely.

1. Power off completely.
2. Press the **Novo button** (pinhole beside the power button; use a paperclip) — or F12/F1 on ThinkPads.
3. Select **System Recovery** > **Troubleshoot**.
4. Try **Startup Repair**, then **System Restore** to a pre-update point.
5. **Reset this PC > Keep my files** as the deeper repair.
6. After recovery: Vantage BIOS + drivers first, then Windows Update — Lenovo's prescribed order prevents recurrence. For the broader recovery context, our [Lenovo rollback guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-lenovo-laptop/) covers sibling scenarios, and Microsoft documents recovery on the [Windows support site](https://support.microsoft.com/en-us/windows).

## Closing

Lenovo restart hangs are dominated by two fixable things: the RST storage driver in Lenovo's default RAID mode, and docks holding the shutdown sequence hostage. Keep Vantage's storage/chipset/BIOS stack current, undock before update restarts, and disable Fast Startup. The "Restarting" screen will still take its normal 20–40 minutes on big updates — but it will finish, every time.
