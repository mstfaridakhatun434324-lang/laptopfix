---
title: "The Best Way to Fix BAD_SYSTEM_CONFIG_INFO on Windows 11"
slug: best-way-to-fix-bad-system-config-info
date: 2026-10-12
categories: ["windows-errors"]
tags: ["bad system config info", "bsod", "boot error", "bcd", "windows 11"]
description: "BAD_SYSTEM_CONFIG_INFO stopping Windows 11 from booting? Here is the most reliable fix order, from BCD repair to registry restoration."
thumbnail: "/images/thumbs/best-way-to-fix-bad-system-config-info.webp"
faqs:
  - q: "What causes BAD_SYSTEM_CONFIG_INFO?"
    a: "Almost always a corrupted Boot Configuration Data (BCD) store or damaged registry hives — typically after a failed Windows update, an interrupted driver install, or a power cut during a system change. It means the loader cannot assemble a valid system configuration, so Windows stops at boot with stop code 0x74."
  - q: "Can I fix BAD_SYSTEM_CONFIG_INFO without losing my files?"
    a: "Yes. The BCD rebuild, registry restore, and startup repair steps all preserve your personal files. Your documents, photos, and installed programs survive these repairs untouched. Only a full reset or clean install would remove them, and those are last resorts, not first steps."
  - q: "Why did this happen right after a Windows update?"
    a: "Updates rewrite boot files and registry entries. If the update is interrupted — by a power loss, forced shutdown, or disk error — the BCD or registry can be left half-written. The next boot then fails with BAD_SYSTEM_CONFIG_INFO. This is also why you should never force-power-off a laptop mid-update."
  - q: "How do I get into recovery if Windows won't boot?"
    a: "Let the laptop fail to boot three times in a row — Windows automatically opens the Recovery Environment (WinRE). Alternatively, hold Shift while clicking Restart from the login screen. From WinRE you get Startup Repair, Command Prompt, and System Restore, which is everything this guide needs."
---

BAD_SYSTEM_CONFIG_INFO (stop code 0x74) is Windows telling you it can't assemble the instructions for starting itself. The boot loader reads the Boot Configuration Data store and the system registry hives to learn where everything lives and how to initialize it; if those are corrupted, the boot process has nothing trustworthy to work with, and Windows crashes before the login screen ever appears. The good news: this is one of the most fixable blue screens, because the damage is usually confined to boot metadata, not your files.

The "best way" to fix it isn't a single magic command — it's an order. Each step below is less destructive and more likely than the next, so you repair the boot data before you ever think about resetting Windows. You'll need the Windows Recovery Environment (WinRE); if Windows can't reach it on its own, boot from Windows 11 installation media created on another PC via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

## Why this happens

- **Corrupted BCD store.** The Boot Configuration Data tells the loader where Windows lives; damage here is the number-one cause of 0x74.
- **Damaged system registry hives.** The SYSTEM hive in particular is read at boot; corruption blocks configuration assembly.
- **Interrupted Windows updates.** A power cut or forced shutdown mid-update leaves boot files half-written.
- **Failed driver installations.** Drivers that hook the boot process (storage, encryption) can corrupt boot data when they install badly.
- **Disk errors or a failing drive.** Bad sectors in the boot partition corrupt the BCD or registry hives silently over time.
- **Dual-boot or partition changes.** Resizing, cloning, or third-party boot managers can desync the BCD from the actual partition layout.
- **Malware targeting boot components.** Bootkits and aggressive "system cleaners" damage the same files the loader depends on.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run Startup Repair from WinRE

Let Windows attempt the automatic fix before you touch anything manually.

1. Boot into the **Recovery Environment** (three failed boots, or boot from installation media and choose **Repair your computer**).
2. Go to **Troubleshoot > Advanced options > Startup Repair**.
3. Select your Windows installation and let it run — it can take 10–20 minutes.
4. If it reports it couldn't repair, note any log path it mentions and move on; you haven't lost anything.
5. Try booting normally. If it still fails, continue — the manual BCD rebuild below succeeds where Startup Repair often can't.

Startup Repair fixes simple BCD issues reliably, but registry-hive damage usually needs the manual steps. The update-triggered variant of this error has its own walkthrough in [how to fix BAD_SYSTEM_CONFIG_INFO after a Windows 11 update](/articles/how-to-fix-bad-system-config-info-after-windows-11-update/).

### Fix 2: Rebuild the BCD from the command prompt

This is the core fix for most 0x74 cases.

1. In WinRE, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Run `bootrec /scanos` to confirm Windows is detected.
3. Run `bootrec /fixmbr` to repair the master boot record.
4. Run `bootrec /fixboot` — if you get "Access is denied," that's a known quirk on UEFI systems; proceed to the next command.
5. Run `bootrec /rebuildbcd`, type **Y** when it asks to add the installation, and restart.
6. If rebuildbcd finds nothing, run these instead: `bcdedit /export C:\BCD_Backup`, then `attrib c:\boot\bcd -h -r -s`, then `ren c:\boot\bcd bcd.old`, then `bootrec /rebuildbcd`.

After a successful rebuild, Windows should boot normally. For the broader stop-code reference, see [BAD_SYSTEM_CONFIG_INFO blue screen error fix](/articles/bad-system-config-info-blue-screen-error-fix/).

### Fix 3: Restore the registry hives

When the BCD is fine but the registry is damaged, restore the hives.

1. From the WinRE **Command Prompt**, first identify your Windows drive letter — it may not be C: here. Run `diskpart`, then `list volume`, then `exit`.
2. Navigate to the config folder: `cd /d D:\Windows\System32\config` (replace D: with your actual drive).
3. Rename the current hives as backup: `ren SYSTEM SYSTEM.bad`, `ren SOFTWARE SOFTWARE.bad`, and so on for SAM, SECURITY, DEFAULT.
4. Copy the repair backups: `copy D:\Windows\System32\config\RegBack\* D:\Windows\System32\config\` — note that on modern Windows 11, RegBack may be empty (Microsoft disabled automatic registry backup); if so, skip to Fix 4.
5. Type `exit`, remove any media, and restart.

If RegBack is empty, don't panic — System Restore points contain registry snapshots, which is what Fix 4 uses.

### Fix 4: Use System Restore

A restore point rolls back the registry, drivers, and system files together.

1. In WinRE, go to **Troubleshoot > Advanced options > System Restore**.
2. Choose a restore point dated **before** the crashes began.
3. Confirm and let it complete — the laptop will restart.
4. Your personal files are untouched; only system state rolls back.
5. After booting, immediately check **Settings > Windows Update** and install updates cleanly — then create a fresh restore point.

If no restore points exist, consider enabling System Protection afterward so you have this safety net next time.

### Fix 5: Run CHKDSK and SFC offline

Fix underlying disk damage that keeps re-corrupting boot data.

1. From the WinRE **Command Prompt**, run `chkdsk C: /f /r` (use the correct drive letter from Fix 3).
2. Let the full scan finish — on large drives this can take an hour or more.
3. Then run the offline SFC: `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.
4. Restart and test. If chkdsk reports bad sectors in the boot area, plan a drive replacement even if the boot works now.
5. Persistent disk errors after a clean chkdsk point at a failing SSD — clone your data while the drive still reads.

### Fix 6: Uninstall the last update or driver

If the crash started immediately after an update, roll it back.

1. In WinRE, go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Try **Uninstall the latest quality update** first, then test booting.
3. If that fails, try **Uninstall the latest feature update** (this takes longer).
4. Once booted, open **Device Manager** and roll back any driver updated on the same day the crashes began.
5. Pause Windows updates for a week (**Settings > Windows Update > Pause updates**) so the bad update doesn't reinstall instantly — then check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for a fixed revision before unpausing.

### Fix 7: Reset Windows as a last resort

When boot data is damaged beyond repair, a reset preserves the most.

1. In WinRE, go to **Troubleshoot > Reset this PC**.
2. Choose **Keep my files** first — this reinstalls Windows while preserving personal data.
3. If that fails or crashes return, repeat with **Remove everything** after backing up via the Command Prompt (`xcopy` your user folder to a USB drive).
4. Prefer **Cloud download** over **Local reinstall** when your connection allows — it fetches undamaged source files.
5. After the reset, install drivers only from your manufacturer's support page and create a restore point immediately.

## Closing

BAD_SYSTEM_CONFIG_INFO looks catastrophic — a laptop that won't boot always feels like the end — but it's usually a ten-minute BCD rebuild away from normal. The order matters: automatic repair first, then the manual BCD rebuild, then registry restoration, and only then the heavier options. Resist the urge to jump straight to a reset; every step before it preserves more of your setup. And once you're booted again, turn on System Protection and make a restore point — the five minutes it takes is the cheapest insurance against ever seeing stop code 0x74 again.
