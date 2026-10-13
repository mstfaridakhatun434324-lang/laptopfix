---
title: "How to Fix Optional Updates Not Installing on Windows 11, Step by Step"
slug: "how-to-fix-optional-updates-not-installing-windows-11-step-by-step"
date: 2026-09-14
categories: ["windows-update"]
tags: ["optional updates", "windows 11", "step by step", "windows update"]
description: "Optional updates not installing on Windows 11? A careful step-by-step walkthrough — unblock, isolate, verify, and install optional updates correctly."
thumbnail: "/images/thumbs/how-to-fix-optional-updates-not-installing-windows-11-step-by-step.webp"
faqs:
  - q: "What is the right order to troubleshoot optional updates?"
    a: "Work in this order: first clear the global pause and metered flags, then refresh the update components, then install optional packages one at a time starting with the most important. Compare each driver’s version against what you already have before installing, and hide any that fail repeatedly with the wushowhide tool. This sequence isolates the real problem instead of letting one bad package mask everything else."
  - q: "Which optional update should I try first?"
    a: "Pick the single most important one — usually a driver for misbehaving hardware — and install it alone. Watch whether it succeeds. If it does, continue one at a time; if it fails, you have isolated the problem package without contaminating the diagnosis. Batch-installing a dozen optionals is the fastest way to learn nothing about which one is broken."
  - q: "How do I know if an optional driver is worth installing?"
    a: "Compare versions first: in Device Manager, check the device’s current driver version against the optional offer. If the optional is older, hide it — installing it would downgrade your hardware support. If it is newer or the device lacks a working driver, install it. For graphics and network hardware, the manufacturer’s package is usually better than the optional WHQL version anyway."
  - q: "Can I permanently remove a bad optional update?"
    a: "Yes, with the wushowhide (“Show or hide updates”) troubleshooter from Microsoft Support. Run it, choose Hide updates, and tick the failing optional package. It disappears from the Optional updates list permanently (until you unhide it). This is the supported resolution for optional offers that are wrong for your hardware — it stops the retry noise without affecting security or quality updates."
---

“Step by step” is exactly what optional-update troubleshooting needs, because the failure is usually a stack of small blockers rather than one big break: a pause here, a metered flag there, a bad package hiding in a batch of twelve. Attack them out of order and you will chase your tail; attack them in order and each step visibly narrows the problem.

This guide is the ordered walkthrough. The conceptual background — what optional updates are and why they fail — is in the [optional-updates overview](/articles/how-to-fix-optional-updates-not-installing-after-windows-11-update/); what follows is the sequence to run, top to bottom, without skipping.

## Why this happens

- **Updates paused globally:** The main pause switch also freezes the optional list; users check optionals without noticing the pause banner.
- **Metered connection suppressing optionals:** Optional downloads are the first sacrificed on metered networks, so the list never progresses.
- **Selecting too many optionals at once:** Batch-installing lets one bad package jam the queue with no indication of which one failed.
- **Version conflicts with installed drivers:** Optional offers older than current drivers fail as downgrades (0x80070103).
- **Corrupted optional metadata:** Desynced catalog metadata lists phantom packages that can never install.
- **Stuck update services:** A hung wuauserv or BITS blocks the optional queue behind the main queue.
- **No staging space:** Nearly full drives fail optional staging silently.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Step 1 — Confirm updates are not paused

Step one is always the same: make sure updates are actually allowed to run. The pause banner is easy to miss, and no optional package can install while the global pause is active. This thirty-second check eliminates the most embarrassing cause first.

1. Open Settings > Windows Update.
2. Look for any “Updates paused” banner — click Resume updates if present.
3. Go to Advanced options and confirm no pause duration is set.
4. Proceed only with the queue unpaused.

### Fix 2: Step 2 — Remove the metered block

Step two: remove the connection-level block. Optional updates are the lowest-priority downloads in Windows, so metering suppresses them first and most completely. Either unflag the network or explicitly permit updates over it.

1. Go to Settings > Network & internet > Wi-Fi and open your connected network.
2. Set Metered connection to Off.
3. For genuinely capped connections, instead enable “Download updates over metered connections” under Windows Update > Advanced options.
4. Return to the Optional updates list.

### Fix 3: Step 3 — Reset the update components

Step three: give the list a clean foundation. The component reset clears stuck services, corrupted caches, and phantom metadata in one pass — the same repair the built-in troubleshooter attempts, done with full visibility.

1. Elevated Command Prompt: net stop wuauserv, net stop bits, net stop cryptSvc.
2. Rename: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
3. Restart the services: net start wuauserv, net start bits, net start cryptSvc.
4. Open Optional updates — entries repopulate with fresh metadata.

### Fix 4: Step 4 — Install one optional at a time

Step four: install individually. One package at a time is slower but diagnostic — a success confirms the pipeline works, a failure isolates the exact offending package instead of smearing blame across a batch.

1. In Optional updates, tick exactly one package — the most important driver.
2. Click Download and install and watch it complete.
3. If it succeeds, continue with the next single package.
4. If it fails, note the error and move to Step 5 before retrying.

### Fix 5: Step 5 — Verify versions on any failure

Step five: adjudicate the failure. Not every failed optional deserves a retry — version comparison tells you whether the package was ever appropriate. Manufacturer packages resolve the legitimate cases; hiding resolves the illegitimate ones.

1. For a failed driver: compare versions in Device Manager versus the offer.
2. If the offer is older, hide it with wushowhide (next step) — it is a downgrade.
3. If the offer is newer, install the manufacturer’s package directly from [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or your laptop maker.
4. Retry the optional afterward if appropriate.

### Fix 6: Step 6 — Hide the optionals that will never install

Step six: curate the list. Hiding wrong-for-your-hardware optionals is the supported end state, not a workaround — it leaves a clean list containing only packages worth installing, and ends the failure notifications permanently.

1. Download wushowhide.diagcab from [Microsoft Support](https://support.microsoft.com/en-us/windows).
2. Choose Hide updates and tick every optional that failed legitimately (older versions, wrong hardware).
3. Confirm the Optional updates list is now clean.
4. For brand-specific wrinkles, see the [HP optional-updates guide](/articles/how-to-fix-optional-updates-not-installing-windows-11-on-hp-laptop/).

### Fix 7: Step 7 — Verify success and set a maintenance routine

The final step is confirming the fix holds and preventing recurrence. After the optional list is clean, run one full update cycle — Check for updates, install everything offered, restart — and verify Update history shows no failures. Then set a light maintenance routine: check Optional updates monthly rather than daily, keep 15 GB free on C:, and revisit hidden updates (wushowhide > Show hidden updates) after each Windows feature update, since new builds can bring corrected driver packages worth unhiding. Ten minutes a month keeps the optional list a useful tool instead of a source of red failure badges.

1. Run Check for updates and install everything currently offered.
2. Restart and confirm Update history shows all successes.
3. Note which updates you hid and why (a simple text note suffices).
4. Monthly: glance at Optional updates, install only what you need, one at a time.
5. After each Windows feature update, review hidden updates for newly valid packages.

## Closing

Optional updates reward methodical work: unblock the queue, install one package at a time, verify versions, and hide what will never install. Follow the sequence above in order and the optional list transforms from a graveyard of failed entries into a short, manageable set of genuinely useful drivers.
