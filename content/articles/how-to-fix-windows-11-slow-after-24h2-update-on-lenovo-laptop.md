---
title: "Windows 11 Slow After the 24H2 Update on a Lenovo Laptop? Fix It"
slug: how-to-fix-windows-11-slow-after-24h2-update-on-lenovo-laptop
date: 2026-10-10
categories: ["performance"]
tags: ["slow after update", "24h2", "lenovo laptop", "windows 11 slow"]
description: "Lenovo laptop sluggish since the Windows 11 24H2 update? The complete recovery sequence — drivers, settings, services, and Lenovo-specific steps."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-after-24h2-update-on-lenovo-laptop.webp"
faqs:
  - q: "Why is my Lenovo slow after the 24H2 update?"
    a: "Feature updates are major surgery: they replace drivers (sometimes with older versions), reset power plans and privacy/gaming settings to defaults, invalidate the search index (forcing a rebuild), trigger Defender rescans, and leave gigabytes of setup leftovers. On Lenovos specifically, the update can also desync Lenovo Vantage's profiles and replace Lenovo-tuned drivers with generic ones. The slowness is the sum of these — not one bug, but a dozen small regressions stacking up."
  - q: "How long should I wait before trying to fix post-24H2 slowness?"
    a: "Give it 24–48 hours of plugged-in use first. The heaviest post-update work — search re-indexing, .NET optimization, Defender rescans, and setup finalization — legitimately consumes resources during this window and then stops on its own. If the laptop is still slow after two days of normal plugged-in use, the remaining slowness is a real configuration problem, not settling-in, and the fixes in this guide apply."
  - q: "Should I roll back the 24H2 update on my Lenovo?"
    a: "Only as a last resort. Rollback (available for 10 days post-update via Settings > System > Recovery) removes security improvements and is meant for broken updates, not slow ones — and post-update slowness is fixable in place 95% of the time. Work through drivers, settings, and services first. Consider rollback only if the update broke something specific and documented (like a Lenovo forum full of identical reports for your model)."
  - q: "Will updating Lenovo Vantage fix 24H2 slowness?"
    a: "Partially — it's one piece. An outdated Vantage can misapply power/thermal profiles after the OS changes underneath it, and old Lenovo drivers (chipset, power management, hotkeys) can conflict with 24H2's expectations. Update Vantage from the Microsoft Store and run its System Update for drivers. But Vantage alone won't fix the Windows-side regressions (power plans, indexing, services) — you need both halves, which this guide covers."
---

The 24H2 update landed on your Lenovo, and now everything is slower: boots drag, apps hesitate, the fans work harder for less. It's tempting to blame the update as a whole — but post-update slowness is rarely one thing. It's a pile-up: replaced drivers, reset settings, background maintenance storms, and Lenovo's own software desynced from the new OS. Each piece is fixable, and together they restore the machine.

This guide is the complete recovery sequence for Lenovos: let legitimate settling finish, then fix drivers (Lenovo's, not just Microsoft's), restore reset settings, calm the background storm, and trim Lenovo's own load. For the brand-neutral version, see [Windows 11 slow after update](/articles/windows-11-slow-after-update-how-to-fix/); for ongoing speed, [how to speed up Windows 11](/articles/how-to-speed-up-windows-11-laptop/).

## Why this happens

- **Drivers replaced with older/generic versions**: 24H2 swaps Lenovo-tuned drivers for Microsoft's inbox versions.
- **Power plans and settings reset**: Power mode, gaming toggles, and privacy settings revert to defaults.
- **Search index invalidated**: Full rebuild consuming CPU/disk for a day or more.
- **Defender post-update rescans**: Re-baselining scans hammer CPU and disk.
- **Setup leftovers**: Gigabytes of $Windows.~BT and old-install files lingering.
- **Lenovo Vantage desync**: Old Vantage/driver combos misbehaving under the new OS build.
- **Re-enabled background services**: SysMain, telemetry, and suggestions toggled back on.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let legitimate settling finish

Don't fix what time fixes free.

1. Confirm the update is fully done: **Settings** > **Windows Update** — no pending installs or restarts.
2. Give the laptop 24–48 hours of plugged-in use — indexing, .NET optimization, and Defender rescans need this window.
3. During the window, leave the laptop idle and plugged in overnight at least once — maintenance tasks defer until idle.
4. After 48 hours, assess honestly: if it's 80% better, the rest is configuration (continue); if unchanged, skip the waiting and dig in.
5. Check Task Manager for the settling signature: `SearchIndexer`, `TiWorker`, `MsMpEng` active now but trending down = settling; constant and flat = stuck.

### Fix 2: Update Lenovo drivers and Vantage

Restore the Lenovo-tuned driver stack.

1. Open the **Microsoft Store**, check for **Lenovo Vantage** updates, and install.
2. In Vantage, run **System Update** — install all critical/recommended driver updates (chipset, storage, power management, BIOS if offered).
3. Then run **Settings** > **Windows Update** including **Optional updates** for anything Vantage missed.
4. Reboot and test — driver restoration alone fixes a large share of post-24H2 Lenovo slowness.
5. In Vantage, verify the thermal/power profile is set to **Performance** or **Balanced**, not Quiet — updates sometimes flip it.

### Fix 3: Restore reset Windows settings

Reclaim what 24H2 flipped back.

1. **Settings** > **System** > **Power & battery** — set **Power mode** to **Best performance** (plugged in).
2. **Settings** > **Gaming** > **Game Mode** On; **Xbox Game Bar** Off (unless used).
3. **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings** — re-enable **Hardware-accelerated GPU scheduling**.
4. **Settings** > **Privacy & security** > **Searching Windows** — set back to **Classic**, re-trim indexed folders, turn off **Search highlights**.
5. Revisit notification suggestions and tips toggles if you had them off — 24H2 commonly re-enables them.

### Fix 4: Clean up setup leftovers

Reclaim disk and remove setup debris.

1. **Settings** > **System** > **Storage** > **Temporary files** — check **Previous Windows installations**, **Temporary Windows installation files**, **Windows Update Cleanup**, **DirectX Shader Cache** — then **Remove files**.
2. This can free 10–30GB and removes the debris that keeps setup-related processes lingering.
3. After cleanup, verify `$Windows.~BT` is gone from C: (show hidden items).
4. A cleaner disk also helps SSD performance — keep at least 15–20% free.
5. Reboot after the cleanup completes.

### Fix 5: Calm the background service storm

Address the services 24H2 woke up.

1. **Task Manager** > **Startup apps** — disable everything non-essential (the update often re-enables entries you'd turned off).
2. If on an HDD: disable **SysMain** (`services.msc`) — 24H2 re-enables it.
3. Scope and rebuild the search index if `SearchIndexer.exe` is still heavy after 48 hours (Settings > Privacy & security > Searching Windows > Advanced indexing options > Rebuild, overnight).
4. For Defender CPU: schedule scans to idle hours and exclude high-churn folders rather than fighting it — see [taming Defender's CPU](/articles/antimalware-service-executable-high-cpu-windows-11/).
5. Re-measure after each change — the storm has multiple sources, so fix them one at a time.

### Fix 6: Trim Lenovo's background load

Lighten the vendor footprint.

1. In Vantage settings, disable features you don't use (keep battery charge threshold if you set one).
2. **Task Manager** > **Startup apps**: disable Lenovo entries not needed at boot.
3. `services.msc`: set Lenovo update/imcontroller services to **Manual** if you update on your own schedule.
4. **Settings** > **Apps**: remove Lenovo apps you never open and any trial antivirus — let Defender handle protection cleanly.
5. Reboot and compare — the Lenovo trim typically recovers a few hundred MB of RAM and measurable idle CPU.

### Fix 7: Repair install or rollback (last resorts)

When the update is genuinely broken for your model.

1. First, search your exact Lenovo model + "24H2 slow" — if forums show a widespread, model-specific issue (e.g., a bad BIOS/driver combo), check Lenovo's support page for a model-specific fix or BIOS update before anything drastic.
2. Try the in-place repair: download Windows 11 from the [official download page](https://www.microsoft.com/en-us/software-download/windows11), run setup, **Keep personal files and apps** — this rebuilds the OS cleanly while preserving data.
3. Only then consider rollback: **Settings** > **System** > **Recovery** > **Go back** (available 10 days post-update) — it restores the previous build.
4. If you roll back, pause updates for a few weeks while Lenovo/Microsoft ship fixes, then retry the update with fresh drivers pre-installed via Vantage.
5. Report via **Feedback Hub** with your model and symptoms — model-specific regressions get fixed when they're reported with data.

## Closing

Post-24H2 slowness on a Lenovo is a stack of small regressions, not a single failure: replaced drivers, reset settings, background maintenance, and desynced Lenovo software. Give settling its 48 hours, then work the sequence — Lenovo drivers via Vantage, restore reset settings, clean setup leftovers, calm background services, trim the vendor load. That order restores the machine in nearly every case, with repair-install and rollback held in reserve for the genuinely broken few.
