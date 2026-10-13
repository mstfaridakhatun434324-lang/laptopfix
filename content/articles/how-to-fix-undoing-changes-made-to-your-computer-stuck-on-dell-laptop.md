---
title: "'Undoing Changes Made to Your Computer' Stuck on a Dell Laptop? How to Fix It"
slug: how-to-fix-undoing-changes-made-to-your-computer-stuck-on-dell-laptop
date: 2026-09-01
categories: ["windows-update"]
tags: ["undoing changes", "dell laptop", "update rollback", "supportassist", "windows 11"]
description: "Your Dell laptop is stuck on 'Undoing changes made to your computer'? Dell-specific recovery with SupportAssist, F12 diagnostics, and BIOS recovery options."
thumbnail: "/images/thumbs/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-dell-laptop.webp"
faqs:
  - q: "How long should 'Undoing changes' take on a Dell laptop?"
    a: "Allow two hours on Dell models with SSDs and three hours on older models with hard drives. Dell's business lines (Latitude, Precision) often run full-disk encryption, which slows rollbacks noticeably — don't mistake encryption overhead for a freeze. Intervene only after the deadline with zero disk activity."
  - q: "What is Dell SupportAssist OS Recovery?"
    a: "It's a recovery environment built into modern Dell laptops, launched by pressing F12 during boot and selecting SupportAssist OS Recovery. It offers automated repair, system restore, and cloud-based OS reinstallation without needing separate recovery media — your best last resort when Windows won't boot after a failed rollback."
  - q: "Can BitLocker complicate the rollback on my Dell?"
    a: "Yes. Many Dell business laptops ship with BitLocker enabled, and recovery operations may prompt for the 48-digit BitLocker recovery key. Find your key in advance at account.microsoft.com/devices/recoverykey while signed into your Microsoft account — without it, you can't access recovery tools on an encrypted drive."
  - q: "Should I update the Dell BIOS before retrying the Windows update?"
    a: "Absolutely. Dell BIOS updates fix hardware compatibility issues that cause update rollbacks, and Dell releases them frequently. Use SupportAssist or Dell's support site to install the latest BIOS for your service tag before retrying — this single step resolves a large share of repeat rollback cases on Dell hardware."
---

Dell laptops bring two distinctive wrinkles to the "Undoing changes" scenario: SupportAssist OS Recovery, which is genuinely one of the better built-in recovery environments in the industry, and the prevalence of BitLocker encryption on business models, which can turn a simple recovery into a key-hunt if you're unprepared. Add Dell's frequent BIOS updates — Dell is aggressive about firmware fixes — and the Dell-specific playbook differs meaningfully from the generic one.

The fundamentals don't change: the rollback screen means a failed update is being reversed, your files are safe, and patience is the first fix. But on a Dell, the diagnostic and recovery tools at your disposal (F12 diagnostics, SupportAssist OS Recovery, Dell's driver packs) give you a cleaner path when patience runs out. Our general [rollback guide](/articles/what-to-do-if-windows-update-says-undoing-changes-made-to-your-computer/) covers the universal steps; this is the Dell layer.

## Why this happens

- **Failed update triggering automatic rollback**: The core cause — an update failed integrity checks mid-install.
- **Outdated Dell BIOS**: Dell's rapid firmware cadence means a year-old BIOS can conflict with new Windows builds.
- **BitLocker + update interaction**: Encryption overhead and recovery-key prompts complicating the rollback and recovery.
- **Dell Data Protection / encryption tools**: Third-party Dell security software interfering with system file replacement.
- **Corrupt Dell driver packages**: Stale Dell OEM drivers in the DriverStore conflicting with the new build.
- **Nearly full drive**: Dell's smaller SSD configurations filling up, starving the update's staging space.
- **SupportAssist driver conflicts**: SupportAssist and Windows Update managing the same drivers inconsistently.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait with Dell realistic timing

Business Dells with encryption need the longest leash. Don't mistake slow for stuck.

1. Connect AC power — Dell laptops can be picky about battery-only operation during recovery.
2. Deadline: **2 hours** (SSD), **3 hours** (HDD or BitLocker-encrypted drives).
3. On Latitudes/Precisions with encryption, add 30 minutes to your expectations — decryption overhead is real.
4. Signs of life: drive activity LED (many Dells have one), fan cycling, spinner animation.
5. If it completes, go to Fix 2. If dead past the deadline, go to Fix 4.

### Fix 2: Locate your BitLocker recovery key BEFORE you need it

Do this now, while Windows is accessible. Every Dell recovery path below may demand the key.

1. On any device, sign into **account.microsoft.com/devices/recoverykey** with your Microsoft account.
2. Find your Dell laptop and copy the 48-digit recovery key — save it on your phone or printed paper.
3. If the key isn't there, check whether your organization manages it (work laptops) or whether BitLocker was never enabled (**Control Panel > BitLocker Drive Encryption**).
4. Without this key, SupportAssist OS Recovery and startup repair can't touch an encrypted drive.
5. This two-minute step prevents the most stressful Dell recovery scenario.

### Fix 3: Update BIOS and drivers via SupportAssist before retrying

Dell's update tooling is the preventive fix. Outdated Dell firmware is behind most repeat rollbacks.

1. Open **Dell SupportAssist** (preinstalled on most Dells; download from the Microsoft Store if missing).
2. Run **Check for updates** and install all **BIOS**, **firmware**, and **driver** updates.
3. BIOS updates require AC power — the installer enforces this.
4. Alternatively, enter your **service tag** on [Dell support](https://www.dell.com/support) for the exact driver pack.
5. After SupportAssist is fully green, check **Settings > Windows Update > Update history** for the failed KB, then retry.
6. For Dell-specific driver failures, our [driver update guidance](/articles/how-to-update-drivers-on-windows-11-laptop/) complements this.

### Fix 4: Force-restart a confirmed-frozen rollback

Past your deadline, spinner frozen, no disk activity: intervene.

1. Hold **power** 10 seconds until fully off.
2. Disconnect docks (Dell WD-series docks especially), USB devices, and external monitors.
3. Power on — the rollback typically resumes and completes within 30 minutes.
4. If BitLocker prompts for the recovery key during boot, enter the key from Fix 2.
5. If it reaches the desktop, continue to Fix 5.
6. If it returns to the frozen screen, power off and go to Fix 6.

### Fix 5: Diagnose the failure from Update history

With the system back, identify what failed so the retry doesn't repeat it.

1. **Settings > Windows Update > Update history** — note the failed KB and error code.
2. **0xC1900101** (driver) → see our [0xC1900101 guide](/articles/how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update/); **0x80070070** → space; **0x800F0922** → .NET/secure boot.
3. Check free space on C: — Dell's 256 GB models need active management; keep 20 GB free.
4. Clear the update cache: elevated Command Prompt, `net stop wuauserv` + `net stop bits`, empty `C:\Windows\SoftwareDistribution\Download`, restart services.
5. Pause updates for 2 weeks while you complete Fixes 3 and 6.

### Fix 6: Run Dell's F12 pre-boot diagnostics

Rule out hardware before deeper software surgery. Dell's diagnostics run outside Windows.

1. Power off completely.
2. Power on and press **F12** repeatedly to reach the boot menu.
3. Select **Diagnostics** — the full system scan tests drive, memory, and board.
4. Pay attention to drive results: Dell's diagnostics report specific error codes (e.g., 2000-0142 for drive failure).
5. If the drive fails, back up immediately and replace it — record the error code for warranty claims.
6. If hardware passes, the rollback cause is software — continue to Fix 7.

### Fix 7: Use SupportAssist OS Recovery as the last resort

When Windows won't boot after the forced restart, Dell's recovery environment handles it without external media.

1. Power off, power on, press **F12**, and select **SupportAssist OS Recovery**.
2. Have your BitLocker key ready (Fix 2) — you'll likely need it.
3. Try **Repair** first — automated startup and system file repair.
4. Then **Restore** — system restore points or Dell's factory image options.
5. **Cloud restore** downloads a fresh Dell factory image — needs internet and wipes data, so it's truly last.
6. After any recovery, install SupportAssist updates first, then Windows Update — Dell's prescribed order. Microsoft documents recovery options generally on the [Windows support site](https://support.microsoft.com/en-us/windows).

## Closing

Dell's recovery story is better than most: F12 diagnostics catch hardware faults early, SupportAssist OS Recovery handles the worst cases without USB media, and Dell's aggressive BIOS cadence means firmware fixes actually exist for most conflicts. The two Dell-specific disciplines — keep the BitLocker key accessible and keep the BIOS current via SupportAssist — prevent the vast majority of "undoing changes" recurrences on Dell hardware.
