---
title: "Windows 11 23H2 Not Showing in Update? Force It to Appear"
slug: windows-11-23h2-not-showing-in-update-troubleshooting
date: 2026-09-30
categories: ["windows-update"]
tags: ["23h2", "not showing", "feature update", "windows 11"]
description: "Windows 11 23H2 not appearing in Windows Update? Understand why Microsoft withholds it and the legitimate ways to make the update appear."
thumbnail: "/images/thumbs/windows-11-23h2-not-showing-in-update-troubleshooting.webp"
faqs:
  - q: "Why isn't Windows 11 23H2 showing in Windows Update?"
    a: "Microsoft rolls out feature updates in phases and withholds them from PCs with known compatibility holds — specific drivers, software, or hardware combinations with reported problems. If your PC has a safeguard hold, 23H2 won't appear until the blocking issue is resolved, which is actually protecting you from a bad upgrade."
  - q: "How can I check if my PC has a safeguard hold?"
    a: "There's no direct 'hold' indicator in Settings, but clues include: 23H2 missing while other updates install fine, and no error messages. The most reliable check is attempting the update via the Installation Assistant — it will tell you if your PC isn't ready and sometimes names the blocking component."
  - q: "Is it safe to force the 23H2 update with the Installation Assistant?"
    a: "Generally yes, but with a caveat: the Assistant bypasses safeguard holds that exist for a reason. If your PC was held back due to a driver conflict, forcing the update can bring the very problem the hold was preventing. Update your drivers and BIOS first, then force it — don't force it blindly."
  - q: "Do I need TPM 2.0 and Secure Boot for 23H2?"
    a: "Yes — 23H2 enforces the same hardware requirements as Windows 11 generally: TPM 2.0, Secure Boot capability, and a supported CPU. If any requirement isn't met, 23H2 won't be offered. Check with Microsoft's PC Health Check app to confirm your hardware qualifies before troubleshooting further."
---

# Windows 11 23H2 Not Showing in Update? Force It to Appear

You know 23H2 exists. Other people have it. But your Windows Update insists you're "up to date" on 22H2, and no amount of clicking "Check for updates" changes that. It's not a bug in the button — Microsoft is deliberately not offering it to your PC, and understanding *why* determines whether you should coax it out or leave it alone.

This guide covers both paths: the legitimate reasons 23H2 hides (safeguard holds, requirements, rollout phases), how to clear the blockers properly, and how to install it manually when you're confident your PC is ready. No registry hacks to fake eligibility — just the methods that don't create bigger problems.

## Why this happens

- **A safeguard hold on your hardware.** Microsoft blocks 23H2 for specific driver/software combinations with known upgrade problems.
- **Phased rollout.** Microsoft releases feature updates gradually; your PC may simply not be in the current wave yet.
- **Unmet hardware requirements.** TPM 2.0, Secure Boot, or CPU requirements not satisfied means no offer, ever.
- **Outdated drivers triggering a hold.** Specific old driver versions (storage, display, audio) place automatic holds until updated.
- **Insufficient disk space.** Feature updates need ~20GB free; low space can suppress the offer silently.
- **Managed or metered update policies.** Group Policy, MDM enrollment, or metered connections can defer or hide feature updates.
- **Corrupted update metadata.** A damaged local update database can fail to evaluate the 23H2 offer correctly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify Your PC Actually Qualifies for 23H2

Before fighting the rollout, confirm eligibility — ineligible PCs will never be offered 23H2 through normal channels.

1. Download and run Microsoft's **PC Health Check** app to verify TPM 2.0, Secure Boot, CPU, and RAM requirements.
2. Check **Settings > System > About** to confirm you're on Windows 11 22H2 (or 21H2) — 23H2 upgrades from these builds.
3. Verify you have at least 20GB free on the system drive.
4. If PC Health Check reports a failure, that's your answer — address the hardware requirement first (often just enabling TPM/Secure Boot in BIOS).
5. If everything passes, your PC is eligible and something else is hiding the update — continue.

### Fix 2: Update Drivers to Clear Safeguard Holds

Most safeguard holds trace to specific old drivers — updating them lifts the hold automatically.

1. Open **Device Manager** and update these critical drivers: display adapter, storage controllers, network adapters, audio.
2. Visit your manufacturer's support page — [Dell](https://www.dell.com/support), HP, or [Lenovo](https://support.lenovo.com/us/en/) — and install the latest chipset and BIOS for your model.
3. For Intel systems, run Intel's Driver & Support Assistant to catch chipset and wireless updates the manufacturer page misses.
4. Remove or update old VPN clients, disk utilities, and antivirus — these are frequent hold triggers.
5. After updating, run **Check for updates** daily for a few days — holds lift asynchronously as Microsoft re-evaluates your hardware.

### Fix 3: Check for Policies Hiding Feature Updates

Your PC might be configured — by you, past you, or your organization — to defer feature updates.

1. Open `gpedit.msc` (Windows Pro) and go to **Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update**.
2. Check **Select the target Feature Update version** — if it's set to 22H2, that's your blocker; clear it or set it to 23H2.
3. In **Settings > Windows Update > Advanced options**, check whether updates are paused or deferred.
4. If the PC is work-managed (MDM), feature update timing may be controlled by IT — check with your admin.
5. On metered connections, Windows may defer feature updates — temporarily unmeter or use the manual method in Fix 5.

### Fix 4: Reset Update Components and Re-scan

Corrupted metadata can prevent the 23H2 offer from evaluating — a clean rebuild fixes it.

1. Open an elevated Command Prompt.
2. Stop services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Rename: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Restart services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Click **Check for updates** and let the full fresh scan complete — the rebuilt metadata re-evaluates feature update eligibility from scratch.

### Fix 5: Install 23H2 via the Installation Assistant

When your PC is eligible and prepared but Windows Update still won't offer 23H2, the Assistant is the sanctioned manual path.

1. Confirm Fixes 1–2 are done — drivers current, requirements met, 20GB+ free.
2. Back up important files (external drive or cloud).
3. Download the Windows 11 Installation Assistant from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11).
4. Run it and follow the prompts — it downloads 23H2 directly and upgrades in place, bypassing the phased rollout.
5. The Assistant will warn you if your PC genuinely isn't ready — heed that warning rather than forcing past it. For related rollout quirks on newer builds, see [24H2 rollout troubleshooting](/articles/how-to-fix-windows-11-24h2-rollout-issues-step-by-step/).

### Fix 6: Use the "Get the Latest Updates" Toggle

Windows 11 has a built-in fast lane for feature updates that many people overlook.

1. Go to **Settings > Windows Update**.
2. Turn ON **Get the latest updates as soon as they're available**.
3. Click **Check for updates** — this toggle prioritizes your PC for current releases including 23H2.
4. Leave it on for several days; the offer can take time to propagate after enabling.
5. If 23H2 appears, install it while plugged in and idle — feature updates deserve your laptop's full attention.

### Fix 7: Wait Strategically (When Waiting Is Correct)

Sometimes the right move is patience — but informed patience, not helpless waiting.

1. If you suspect a safeguard hold and your drivers are now current, give it 1–2 weeks — Microsoft lifts holds in waves as telemetry confirms fixes.
2. During the wait, keep installing monthly quality updates normally — they don't interfere with the eventual 23H2 offer.
3. Don't attempt registry hacks to spoof eligibility — they bypass the protections holds provide and can produce unbootable systems.
4. Set a calendar reminder to recheck; if 23H2 hasn't appeared after a month with current drivers, use the Installation Assistant from Fix 5.
5. Remember what the hold is for: it exists because PCs like yours had problems. The [23H2-not-showing checklist](/articles/what-to-do-if-windows-11-23h2-not-showing-in-update/) covers the same ground from a different angle if you want a second opinion on your specific situation.

## Closing

23H2 hiding from Windows Update is usually Microsoft protecting you — a safeguard hold, a phased rollout, or an unmet requirement. Verify eligibility, update your drivers to lift holds, check for deferral policies, and then either wait for the offer or take the Installation Assistant's manual path. Forced the right way, after preparation, 23H2 installs cleanly.
