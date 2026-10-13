---
title: "'Undoing Changes Made to Your Computer' Stuck on an ASUS Laptop? How to Fix It"
slug: how-to-fix-undoing-changes-made-to-your-computer-stuck-on-asus-laptop
date: 2026-09-02
categories: ["windows-update"]
tags: ["undoing changes", "asus laptop", "update rollback", "myasus", "windows 11"]
description: "Your ASUS laptop is frozen on 'Undoing changes made to your computer'? ASUS-specific fixes using MyASUS, F9 recovery, and ROG/consumer model guidance."
thumbnail: "/images/thumbs/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-asus-laptop.webp"
faqs:
  - q: "How long should I wait on 'Undoing changes' on my ASUS?"
    a: "Two hours for SSD models, three for HDD models. ASUS ROG gaming laptops with large game libraries often have nearly full drives, which slows rollbacks — check that space isn't the underlying issue while you wait. Only force a restart after the deadline with a frozen spinner and no disk activity."
  - q: "What does pressing F9 during ASUS boot do?"
    a: "On many ASUS consumer laptops, F9 launches the ASUS recovery partition, offering Windows recovery options including refresh and reset. It's the fallback when Windows won't boot after a failed rollback. Note that some newer models replaced F9 with the standard Windows recovery environment — try both."
  - q: "Can MyASUS help prevent update rollbacks?"
    a: "Yes. MyASUS delivers ASUS-validated BIOS, firmware, and driver updates — including ROG-specific components Windows Update doesn't handle. Keeping MyASUS updates current eliminates the outdated-firmware cause of most repeat rollbacks on ASUS hardware, particularly on ROG and TUF gaming models."
  - q: "Do Armoury Crate or ASUS utilities interfere with updates?"
    a: "They can. Armoury Crate and some ASUS system utilities install kernel-level components for fan control, lighting, and performance profiles that occasionally conflict with build upgrades. If rollbacks recur, try updating Armoury Crate first, and as a test, uninstall it before the next feature update attempt."
---

ASUS laptops span two worlds — the VivoBook/Zenbook ultrabooks and the ROG/TUF gaming machines — and the "Undoing changes" experience differs slightly between them. Gaming models tend to have nearly full drives (games are enormous), aggressive performance utilities (Armoury Crate) with kernel components, and users who tweak BIOS settings — all of which raise rollback risk. Ultrabooks are closer to the generic case but still benefit from ASUS-specific tools: MyASUS for validated updates and the F9 recovery partition for worst cases.

The core truth is unchanged: the rollback screen means Windows caught a failed update and is reversing it. Your files are safe. But ASUS users should pay special attention to three things: free space (gaming drives fill fast), Armoury Crate (update it or temporarily remove it), and the BIOS (MyASUS makes this painless). Our general [rollback guide](/articles/what-to-do-if-windows-update-says-undoing-changes-made-to-your-computer/) covers the universal steps; here is the ASUS-specific path.

## Why this happens

- **Drive nearly full from games**: ROG/TUF models with 512 GB drives packed with 100 GB games starve the update's staging space.
- **Armoury Crate kernel components**: ASUS's control software hooks deep enough to conflict with build upgrades.
- **Outdated ASUS BIOS**: BIOS updates via MyASUS fix hardware quirks new Windows builds trip over.
- **Custom BIOS settings**: Overclocking, XMP, or disabled secure boot on gaming models conflicting with update requirements.
- **Corrupt update download**: Damaged packages failing verification mid-install.
- **Preinstalled McAfee trial**: ASUS bundles trial antivirus whose filter drivers fight system file replacement.
- **Interrupted previous update**: A force-restarted earlier update leaving the component store inconsistent.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait it out on AC power

Standard patience protocol, with ASUS-specific notes.

1. Plug into AC power — ASUS gaming laptops can throttle or sleep aggressively on battery.
2. Deadline: **2 hours** (SSD), **3 hours** (HDD).
3. On ROG models, the keyboard backlight may stay lit during rollback — that's normal, not a sign of a freeze.
4. Listen for drive activity; watch the spinner for smooth animation.
5. If it completes, go to Fix 2. If frozen past the deadline, go to Fix 4.

### Fix 2: Check space and identify the failure

Gaming laptops fail updates on space more than any other single cause.

1. Once back in Windows, check free space on C: — you need **25+ GB** for feature updates on game-loaded systems.
2. **Settings > Windows Update > Update history** — note the failed KB and error code.
3. **0x80070070** explicitly means out of space. **0xC1900101** means driver conflict (see our [0xC1900101 guide](/articles/how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update/)).
4. Move games to a secondary drive or uninstall what you don't play — space pressure causes repeat failures.
5. Run **Storage Sense** (**Settings > System > Storage**) to automate future cleanup.

### Fix 3: Update everything through MyASUS first

MyASUS is the ASUS equivalent of Lenovo Vantage — validated BIOS, firmware, and drivers for your exact model.

1. Open **MyASUS** (preinstalled; available in the Microsoft Store).
2. Go to **System Update** or **Live Update** and install all **BIOS**, **firmware**, and **driver** updates.
3. BIOS updates need AC power and take several minutes — don't interrupt.
4. Update **Armoury Crate** itself via the Microsoft Store or ASUS's site — an outdated Crate is a rollback risk.
5. After MyASUS is fully current, retry the Windows update.
6. On ROG models, also check for **firmware updates for the GPU** (VBIOS) in MyASUS — these occasionally gate Windows updates.

### Fix 4: Force-restart a confirmed-frozen rollback

Past deadline, frozen spinner, silent drive: intervene.

1. Hold **power** 10 seconds until off.
2. Unplug all USB peripherals — gaming peripherals with custom drivers are suspects.
3. Power on and let the rollback resume (usually completes within 30 minutes).
4. If it boots to desktop, continue to Fix 5.
5. If it loops to the frozen screen, power off and go to Fix 7.

### Fix 5: Neutralize Armoury Crate and the trial antivirus

The two most common ASUS software culprits. Address both before the retry.

1. **Settings > Apps** — uninstall the **McAfee/Norton trial**; run the vendor's removal tool for leftover filter drivers.
2. Confirm **Windows Security** shows Defender active.
3. For Armoury Crate: first try updating it fully. If rollbacks recur, **uninstall Armoury Crate** temporarily before the next feature update — you can reinstall afterward.
4. Also check for other ASUS utilities with kernel components (GameVisual, Sonic Studio) and update them.
5. Pause Windows Update for 1–2 weeks while stabilizing the software stack.

### Fix 6: Reset custom BIOS settings to defaults

ROG users who tweaked BIOS settings may have created update blockers unknowingly.

1. Enter BIOS: power on and press **F2** (or **Del** on some models).
2. Note your current settings (photo with your phone) if you've customized.
3. Choose **Load Optimized Defaults** (usually F5 or in the Exit menu).
4. Ensure **Secure Boot** is enabled — some updates require it.
5. Save and exit, then retry the Windows update.
6. If the update succeeds, reapply customizations one at a time to find the conflicting setting.
7. For related boot issues, our [stuck on Restarting guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/) covers recovery.

### Fix 7: Use ASUS recovery (F9) as the last resort

When Windows won't boot after the forced restart.

1. Power off completely.
2. Power on and press **F9** repeatedly (on supported models) to launch ASUS recovery.
3. If F9 doesn't work, interrupt boot three times to reach standard **Windows Recovery > Troubleshoot**.
4. Try **Startup Repair**, then **System Restore** to a pre-update point.
5. **Refresh/reset keeping files** before full factory restore.
6. After recovery: MyASUS updates first, then Windows Update — in that order.
7. Microsoft documents the general recovery options on the [Windows support site](https://support.microsoft.com/en-us/windows).

## Closing

ASUS rollbacks cluster around three fixable things: full drives on gaming models, Armoury Crate's deep hooks, and outdated BIOS. Free the space, keep MyASUS (and Crate) current, and reset aggressive BIOS tweaks before major updates. The rollback screen is Windows protecting your system — with the ASUS-specific causes handled, the next update should install instead of reversing.
