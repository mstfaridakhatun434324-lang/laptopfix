---
title: "Fix Windows 11 23H2 Not Showing in Update: Step by Step"
slug: how-to-fix-windows-11-23h2-not-showing-in-update-step-by-step
date: 2026-09-27
categories: ["windows-update"]
tags: ["windows 11 23h2", "feature update missing", "step by step"]
description: "Windows 11 23H2 not appearing in Windows Update? Follow this exact step-by-step checklist to find the block and get the update offered."
thumbnail: "/images/thumbs/how-to-fix-windows-11-23h2-not-showing-in-update-step-by-step.webp"
faqs:
  - q: "How do I know if a safeguard hold is blocking my update?"
    a: "There is no direct notification, which is what makes holds confusing. The indirect signs: your PC meets all requirements, drivers are current, months have passed, and similar hardware already has the update. Updating all drivers and waiting 48 hours for re-evaluation is the practical test — if the update appears, a hold was the cause."
  - q: "Can I check which safeguard hold applies to my PC?"
    a: "Microsoft documents known safeguard holds publicly, and IT admins can query them, but there is no consumer-facing tool that names your specific hold. The actionable approach is the same regardless: update every driver, especially storage, chipset, and graphics, then recheck."
  - q: "Does the Installation Assistant bypass safeguard holds?"
    a: "Yes, and that is both its power and its risk. The assistant does not honor the holds that Windows Update respects. Use it only after updating drivers and confirming requirements — bypassing a hold that exists for your hardware configuration can install a build with known issues on your machine."
  - q: "What if none of these steps make the update appear?"
    a: "Then either a hold persists (keep drivers current and wait), your hardware genuinely does not qualify, or update detection is broken (try the repair install in the final step). In rare cases the update simply is not needed — if you are already on a newer build like 24H2, 23H2 will never be offered."
---

This is the checklist version: no theory, just the exact steps in the exact order to make Windows 11 23H2 appear in Windows Update. Work top to bottom, stop when the update shows up. Most people resolve it by step 3. If you want the explanations behind these steps, the [HP-focused guide](/articles/how-to-fix-windows-11-23h2-not-showing-in-update-on-hp-laptop/) covers the same territory with full context.

Before starting: confirm you actually need 23H2. Open **Settings → System → About** and check your Windows version — if you are already on 24H2 or later, 23H2 will never be offered, and everything is working correctly.

The single most misunderstood step in this whole process is step 2 of Fix 1 — confirming which build you are on. People skip it, run the entire checklist, force the update with the Installation Assistant, and then discover they were already on 24H2 and the "missing" 23H2 was never going to appear. Thirty seconds in Settings → System → About prevents that entire wasted afternoon. Diagnostics always starts with establishing the current state; with feature updates, the current state is the build number.

## Why this happens

- **Safeguard hold:** Microsoft deliberately withholding the update from your hardware configuration due to a known issue. Holds are the most common reason a healthy, eligible PC never sees the offer — and the most misunderstood, because Windows never tells you a hold exists.
- **Outdated drivers triggering the hold:** The flagged component is usually a storage, chipset, or graphics driver.
- **Paused updates or metered connection:** Simple settings blocks.
- **Corrupted update detection:** Windows Update cannot scan properly. Symptoms include the update page spinning forever, erroring on every check, or showing a last-checked date from weeks ago despite manual refreshes.
- **Failing requirement checks:** TPM, Secure Boot, or disk space silently unmet.
- **Deferred by policy:** Group policy or MDM deferral settings.
- **Already on a newer build:** 23H2 is not offered to PCs running 24H2+.
- **Staggered rollout:** The update genuinely has not reached you yet (only valid for the first weeks after release).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm you need 23H2 and clear simple blocks

1. **Settings → System → About** — note your current build. If it is 24H2 or newer, stop here; nothing is wrong.
2. **Settings → Windows Update** — ensure updates are not paused.
3. **Settings → Network & internet** — turn off **Metered connection** if enabled.
4. Ensure **20+ GB free** on C:, then click **Check for updates** and let the scan finish. If the scan itself errors out or hangs indefinitely, skip ahead to Fix 4 — broken detection needs repair before any offer can appear.

### Fix 2: Update all drivers

1. Open your manufacturer's driver tool (SupportAssist, HP Support Assistant, Lenovo Vantage, MyASUS) and install every offered driver, BIOS, and firmware update.
2. Prioritize **BIOS**, **chipset**, **storage**, and **graphics** — these are the hold-triggering components.
3. Reboot fully after BIOS updates.
4. Wait **24–48 hours**, then check for updates again — Microsoft re-evaluates holds on its own schedule. Do not check every hour; the re-evaluation is server-side and impatience does not accelerate it. Set a reminder and move on with your day.

### Fix 3: Verify requirements in BIOS

1. Run **PC Health Check** and note any failing requirement.
2. Reboot into BIOS and confirm **TPM 2.0** and **Secure Boot** are enabled.
3. Correct any failures, boot back into Windows, and check for updates. If TPM shows as unavailable in BIOS despite a compatible CPU, a BIOS update from your manufacturer often exposes the setting — check their support site.

### Fix 4: Reset Windows Update detection

1. Elevated Terminal: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename `C:\Windows\SoftwareDistribution` and `C:\Windows\System32\catroot2` with `.old` suffixes.
3. Restart the three services, reboot, and **Check for updates**. If the scan now completes but still shows no feature update, return to Fix 2 — the hold is the remaining suspect, and another driver pass is the answer.

### Fix 5: Inspect deferral policies

1. **Win + R** → `gpedit.msc` → Computer Configuration → Administrative Templates → Windows Components → Windows Update → Manage updates offered from Windows Update.
2. If "Select the target Feature Update version" is configured, note what it pins — change or clear it only if you are authorized to. On home PCs this policy is sometimes set by long-forgotten tweaking tools — clearing it is safe if the PC is yours.
3. On work/school devices, confirm with IT whether the deferral is intentional.

### Fix 6: Force the offer with the Installation Assistant

1. Only after steps 1–5: download the **Installation Assistant** from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Back up important files first — this bypasses safeguard holds.
3. Run it and follow the prompts. If it refuses with a compatibility message, believe it: your PC has a genuine blocker. The [24H2 update repair sequence](/articles/how-to-fix-windows-update-fails-to-install-in-windows-11-24h2/) covers the component resets that fix unhealthy update pipelines in more depth.

### Fix 7: Repair-install to fix broken detection

1. If Windows Update shows errors or the page malfunctions, download the Windows 11 ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount it, run setup, choose **Keep personal files and apps**.
3. After the repair, check for updates — detection is rebuilt and eligible feature updates are offered.

## Closing

Run the checklist in order and the 23H2 offer appears as soon as its actual blocker is gone — usually an outdated driver holding a safeguard in place. Resist the urge to jump straight to forcing it: the hold system exists to keep problematic builds off your exact hardware, and the driver update that lifts the hold also makes the install safer. Methodical beats forceful with feature updates every time. Print this page or bookmark it — the same checklist works for every future feature update that goes missing. The checklist does not expire — only the build numbers change.
