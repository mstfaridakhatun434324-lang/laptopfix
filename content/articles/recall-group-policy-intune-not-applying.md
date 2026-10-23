---
title: "Fix Recall Group Policy and Intune Settings Not Applying on Copilot+ PCs"
slug: recall-group-policy-intune-not-applying
date: 2026-10-23
categories: ["ai-pc"]
tags: ["recall", "group policy", "intune", "copilot+", "policy not applying", "windows 11"]
description: "Recall Group Policy and Intune settings not applying on your Copilot+ PC? Diagnose policy conflicts, sync failures, and snapshot controls step by step."
thumbnail: "/images/thumbs/recall-group-policy-intune-not-applying.webp"
faqs:
  - q: "Why is my Recall disable policy not taking effect?"
    a: >
      The usual cause is a conflicting policy winning the precedence battle — a less-restrictive Intune setting profile overriding your Group Policy, or the device not having synced since the policy was assigned. Check the winning policy source in Settings > Accounts > Access work or school > Info before changing anything.
  - q: "Does disabling Recall via policy delete existing snapshots?"
    a: >
      Disabling the Recall feature through policy stops new snapshots, but previously captured snapshots remain until the retention window expires or you clear them manually in Settings > Privacy & security > Recall & snapshots. Verify deletion on a test device if your compliance regime requires proof.
  - q: "Can Group Policy and Intune both manage Recall at once?"
    a: >
      They can coexist, but MDM (Intune) wins over Group Policy when both configure the same setting. If your Recall policy seems ignored, check Intune first — an old or default settings catalog profile is likely overriding your GPO.
  - q: "How long does an Intune Recall policy take to apply?"
    a: >
      After a manual sync, most settings apply within 5-15 minutes, but a full policy refresh cycle can take up to 8 hours on its own. If nothing changes after a manual sync plus a reboot, the problem is conflict or targeting, not timing.
---

You pushed a policy to disable Recall — or lock down its snapshot storage — and the Copilot+ PCs are ignoring it. Intune shows it assigned, the GPO is linked, yet Recall keeps capturing snapshots. The engine did not break; something with higher precedence is overriding your setting, or the device never received it.

Recall is governed by a layered stack: Group Policy, MDM/Intune settings catalog, provisioning defaults, and per-user toggles. On Copilot+ PCs the winning layer is not always the one you configured — and the UI never says which policy is in force.

This guide diagnoses in the right order: verifying what the device received, finding the winning policy source, resolving GPO-versus-Intune conflicts, and confirming with evidence instead of assumptions.

## Why this happens

- **MDM wins over Group Policy on the same setting:** When Intune and a GPO both configure Recall, the MDM value silently wins. Admins who set the GPO first and added Intune later often chase a policy that was never going to apply.
- **A stale Intune profile overriding your intent:** Recall options live in more than one settings-catalog location; an older profile or inherited default can neutralize the profile you meant to enforce.
- **The device has not synced since assignment:** Intune checks in on its own schedule. A policy assigned an hour ago may simply not have reached the device yet, especially on machines that sleep aggressively — a Copilot+ battery trait.
- **Targeting misses the device:** The policy targets a group the device is not in, targets users while the setting is device-scoped (or vice versa), or an exclusion group quietly removes the machines you are testing on.
- **Co-management confusion:** Devices with both ConfigMgr and Intune agents, or hybrid-joined machines, can receive conflicting Recall settings from two authorities.
- **Build mismatch: the policy CSP does not exist on that build:** Some Recall policy settings only exist on newer Windows 11 builds. Pushing them to a 23H2-era machine does nothing, with no error surfaced in the console.
- **Per-user Settings toggle appearing to override policy:** When policy partially applies, the Settings UI can show a toggle that looks user-controllable but is actually greyed by policy — or vice versa, creating false reports of "policy not working."

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify what the device actually received

Before changing any policy, establish ground truth on the device itself. The Intune console shows intent; the device shows reality. Half of all "policy not applying" tickets end here.

1. On the affected Copilot+ PC, open **Settings > Accounts > Access work or school**, click the work account, then **Info** — this shows sync status and the last successful check-in time.
2. Click **Sync** and wait for it to complete, then check whether Recall behavior changes within 15 minutes.
3. Run `gpresult /h c:\gpreport.html` elevated and open the report — it shows exactly which GPOs applied and which Recall settings they set.
4. Open **Settings > Privacy & security > Recall & snapshots** and note whether the toggles are greyed (policy-managed) or active (no effective policy) — this is the fastest single indicator of whether any policy won.
5. If the toggles are active after a successful sync, the policy genuinely is not reaching the device — continue to Fix 2. If they changed after sync, it was only timing, and you are done.

### Fix 2: Find the winning policy source and resolve the conflict

When both Group Policy and Intune touch Recall, one wins and the loser is silent. Identify the winner, then consolidate control into a single authority instead of fighting precedence.

1. Compare the `gpresult` output with the Intune device's **Device configuration** blade — list every profile that mentions Recall or snapshots.
2. Remember the rule: **MDM beats GPO** on the same setting. If Intune has any Recall setting configured (even "Allow"), it overrides your GPO.
3. Decide on one authority: for cloud-managed fleets, configure Recall only in Intune and set the GPO to **Not Configured**; for on-prem fleets, do the reverse and exclude the devices from the Intune profile.
4. Search all Intune profiles for "Recall" — a forgotten baseline profile is the classic hidden override.
5. After consolidating, sync the device and re-check the Recall toggles; the greyed-out state should now reflect your single source of truth.

### Fix 3: Fix targeting, scope, and assignment mistakes

A perfectly configured policy assigned to the wrong group applies to nobody. Targeting errors are the second most common cause and the easiest to overlook because the console shows the policy as healthy.

1. In Intune, open the policy's **Assignments** and verify the target group actually contains the affected devices — check group membership dynamically, not from memory.
2. Confirm scope: Recall snapshot controls are device-scoped in most CSP paths — a user-targeted assignment will not apply them.
3. Check **Exclude** groups and filters: an exclusion added for a pilot can silently swallow the production fleet if the filter is too broad.
4. For GPOs, verify link order and that the OU with the Copilot+ computer objects is in scope — `gpresult /r` shows which GPOs were denied and why.
5. After fixing assignments, force a sync and allow up to 15 minutes; then verify in the Recall settings page rather than trusting the console's "Succeeded" status alone.

### Fix 4: Handle build and edition requirements

Recall policies depend on OS build and edition. Pushing a 24H2-era CSP to an older build fails silently, and Recall itself behaves differently across builds — the policy cannot manage what the OS does not expose.

1. Check the device build in **Settings > System > About** — Recall management policies need Windows 11 24H2 or later on Copilot+ hardware.
2. If devices are behind, update via [Windows Update](https://support.microsoft.com/en-us/windows) or deploy the enablement package through Intune before expecting policy control.
3. Verify edition: Recall and its policies are a Windows 11 Pro/Enterprise story — Home edition devices in a fleet will not honor enterprise Recall policies.
4. Confirm the Recall feature state: on builds where Recall ships disabled by default, a "disable" policy looks broken when there was simply nothing to disable.
5. Standardize the fleet on one build before finalizing Recall policy — mixed builds produce exactly the "works on some machines" pattern.

### Fix 5: Confirm snapshots actually stop and clean up existing data

Disabling Recall going forward does not erase the past. Compliance usually requires proof that capture stopped and old snapshots are gone — verify both, do not assume.

1. After the policy applies (toggles greyed, showing your enforced state), open **Settings > Privacy & security > Recall & snapshots** and confirm the storage indicator shows no new snapshot growth over 24 hours.
2. Delete existing snapshots (**Delete snapshots**) on a sample of devices and confirm the storage figure drops to zero.
3. Check Event Viewer under **Applications and Services Logs > Microsoft > Windows > Recall** for capture errors or policy events as your audit trail.
4. For Intune-managed proof, use a proactive remediation script that reports snapshot folder size per device — this gives you fleet-wide evidence without touching each machine.
5. Heavy background AI workloads can mask verification — if a device shows odd NPU/CPU behavior, rule out unrelated loads like [GPT4All NPU acceleration issues](/articles/gpt4all-npu-acceleration-not-working/) or [live captions burning CPU](/articles/live-captions-high-cpu-usage-fix/) before blaming the policy.

### Fix 6: Reset policy state on stubborn devices

When a device has received conflicting policies over its lifetime, its local policy cache can hold stale values that survive syncs. A clean reset of the management state resolves the "everything looks right but nothing changes" cases.

1. Start gentle: delete the local Group Policy cache (`C:\Windows\System32\GroupPolicy` contents) and run `gpupdate /force`.
2. In Intune, use **Sync** then **Restart** from the device blade — some Recall settings only apply at boot.
3. If MDM enrollment itself is suspect, retire and re-enroll the device, then re-apply only the consolidated Recall profile from Fix 2.
4. As a last resort for lab machines, a fresh Autopilot reset gives a known-clean policy state — on dual-boot setups this can disturb the second OS, so check our [dual-boot Linux on Snapdragon guide](/articles/dual-boot-linux-snapdragon-laptop/) first.
5. Re-verify with Fix 1's checks; a passing device is genuinely compliant, not just console-green.

## Closing

Recall policy failures are precedence and targeting problems, not Recall problems. Establish what the device received, consolidate to one authority, fix the assignment scope, verify on-device — and the snapshots stop where you told them to.
