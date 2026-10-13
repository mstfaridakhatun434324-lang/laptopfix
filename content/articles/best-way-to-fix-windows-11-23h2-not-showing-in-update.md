---
title: "Best Way to Make Windows 11 23H2 Appear in Windows Update"
slug: best-way-to-fix-windows-11-23h2-not-showing-in-update
date: 2026-10-09
categories: ["windows-update"]
tags: ["23h2", "not showing", "best way", "feature update"]
description: "The most reliable methods to get Windows 11 23H2 offered in Windows Update — ranked by safety, from lifting safeguard holds to the manual install path."
thumbnail: "/images/thumbs/best-way-to-fix-windows-11-23h2-not-showing-in-update.webp"
faqs:
  - q: "What is the single best way to get 23H2 to show up?"
    a: "Update all your drivers and BIOS first, then enable 'Get the latest updates as soon as they're available' and check daily. This resolves the most common blocker (a safeguard hold from outdated drivers) through the official channel. If it's still missing after two weeks, the Installation Assistant is the sanctioned manual route."
  - q: "How long does it take for a safeguard hold to lift?"
    a: "Holds lift in waves as Microsoft's telemetry confirms the blocking issue is resolved — typically days to a few weeks after you update the offending driver. There's no notification when a hold lifts; 23H2 simply appears in Windows Update one day. Checking every few days is the practical approach."
  - q: "Is using the Installation Assistant as good as Windows Update?"
    a: "The end result is identical — the same 23H2 build installed the same way. The Assistant just bypasses the phased rollout queue. The one thing it doesn't do is respect safeguard holds, so only use it after updating drivers and confirming your PC meets requirements."
  - q: "Can I still get 23H2 if my PC is a few years old?"
    a: "Age alone doesn't block it — meeting the requirements does. If TPM 2.0, Secure Boot, and CPU requirements are met (check with PC Health Check), a 4–5 year old laptop gets 23H2 fine. What's more likely on older hardware is a safeguard hold from an outdated driver, which updating resolves."
---

# Best Way to Make Windows 11 23H2 Appear in Windows Update

When 23H2 won't show up, the internet offers a dozen "tricks" of wildly varying wisdom — registry edits, scripts, forced installs. Most are unnecessary; some are actively harmful. There is a best way, and it's boring: clear the legitimate blockers through official channels, in the right order, and escalate to the manual install only when the automatic path is exhausted.

This guide ranks the methods by what actually works and what's actually safe. No hacks, no eligibility spoofing — just the sequence that gets 23H2 offered to the maximum number of PCs with the minimum risk.

## Why this happens

- **Safeguard holds from outdated drivers.** The top reason — Microsoft withholds 23H2 until known-bad driver versions are updated.
- **Phased rollout queue.** Your PC simply hasn't been selected in the current rollout wave.
- **The "latest updates" toggle is off.** Without it, your PC sits in the slower standard rollout lane.
- **Deferred feature updates via policy.** Group Policy or MDM settings pushing feature updates months out.
- **Corrupted update metadata.** The local database failing to evaluate the 23H2 offer.
- **Unmet requirements.** TPM, Secure Boot, or CPU gates silently blocking the offer.
- **Low disk space.** Insufficient room suppressing the feature update offer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Eligibility with PC Health Check

The best method starts with knowing you're actually in the game.

1. Run Microsoft's **PC Health Check** app and verify every Windows 11 requirement passes.
2. If TPM or Secure Boot fails, reboot into BIOS/UEFI and enable them — this alone unblocks many "missing" 23H2 offers.
3. Confirm 20GB+ free space on the system drive.
4. Verify you're on 22H2 or 21H2 in **Settings > System > About**.
5. Everything green means the block is a hold, a queue, or metadata — all fixable below. Anything red means fix the requirement first; nothing else will work.

### Fix 2: Update Drivers and BIOS — The Hold-Lifter

This single step resolves more missing-23H2 cases than everything else combined.

1. Update in **Device Manager**: display, storage controllers, network, audio — right-click each, **Update driver**.
2. Get the full driver pack from your manufacturer — [Dell](https://www.dell.com/support), HP, or [Lenovo](https://support.lenovo.com/us/en/) — chipset and BIOS especially.
3. Run Intel's Driver & Support Assistant for Intel-based systems to catch what the manufacturer page misses.
4. Update or remove old VPN clients, disk utilities, and third-party antivirus — classic hold triggers.
5. After updating, check Windows Update every few days for two weeks — holds lift asynchronously, and patience here beats every hack.

### Fix 3: Enable the Fast Lane Toggle

The official "offer it to me sooner" switch — use it.

1. **Settings > Windows Update** — turn ON **Get the latest updates as soon as they're available**.
2. Click **Check for updates** immediately after enabling.
3. Leave the toggle on permanently — it also speeds future feature updates.
4. Combine with Fix 2's driver updates: toggle + current drivers is the highest-probability automatic path.
5. If 23H2 appears, install it while plugged in with peripherals disconnected — feature updates deserve a clean environment.

### Fix 4: Clear Deferral Policies

Your PC might be told to wait — find out and change the instruction.

1. `gpedit.msc` > **Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update**.
2. Check **Select the target Feature Update version** — clear it or set it to 23H2 if it's pinning you to an older build.
3. **Settings > Windows Update > Advanced options** — ensure updates aren't paused and no deferral days are set.
4. Work-managed PCs: ask IT about feature update rings — the policy may be intentional.
5. After clearing policies, run `gpupdate /force` in an elevated prompt and check for updates again.

### Fix 5: Rebuild Update Metadata

When eligibility is fine and policies are clear but the offer still won't evaluate, rebuild the local database.

1. Elevated Command Prompt: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
3. `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. **Check for updates** — the fresh metadata re-evaluates 23H2 eligibility from zero.
5. Let the scan complete fully; the first post-rebuild scan is slow and the offer evaluation happens at the end of it.

### Fix 6: Use the Installation Assistant — The Sanctioned Manual Path

When the automatic path is exhausted but your PC is prepared, this is the best manual method.

1. Confirm Fixes 1–2 are complete: eligible, drivers current, 20GB free, backup done.
2. Download the Installation Assistant from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Run it — it fetches 23H2 directly and upgrades in place, ignoring the rollout queue.
4. Heed any "your PC isn't ready" warning from the Assistant — it sees holds that Settings doesn't show.
5. Post-install, verify in **Settings > System > About** that you're on 23H2, then run Windows Update to catch up on patches. For the full troubleshooting angle on this scenario, see [23H2 not showing — troubleshooting edition](/articles/windows-11-23h2-not-showing-in-update-troubleshooting/).

### Fix 7: Know When Waiting Is the Best Move

The best method sometimes isn't a method — it's informed patience plus a deadline.

1. If drivers are current and everything checks out, waiting 2–4 weeks for the rollout wave is legitimate — Microsoft staggers releases deliberately.
2. Keep installing monthly quality updates during the wait — they don't block the 23H2 offer.
3. Set a personal deadline: if 23H2 hasn't appeared after a month, use the Installation Assistant (Fix 6) rather than waiting indefinitely.
4. Never use registry hacks or third-party "enablers" to force eligibility — they bypass safety holds and can leave systems unbootable.
5. The rollout eventually reaches every eligible PC — the [24H2 rollout guide](/articles/how-to-fix-windows-11-24h2-rollout-issues-on-lenovo-laptop/) shows the same pattern on newer builds, where patience plus preparation wins.

## Closing

The best way to get 23H2 isn't a trick — it's preparation plus the official channels: verify eligibility, update drivers to lift holds, enable the fast-lane toggle, clear deferrals, rebuild metadata if needed, and use the Installation Assistant as the sanctioned fallback. Ranked by safety and reliability, that sequence gets 23H2 onto more PCs than every hack combined, with none of the risk.
