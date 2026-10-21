---
title: "Fix Windows Recall Not Working on Microsoft Surface Pro 11"
slug: microsoft-surface-pro-11-recall-issues
date: 2026-10-21
categories: ["ai-pc"]
tags: ["surface pro 11", "windows recall", "recall not working", "snapdragon x", "copilot+ pc", "recall snapshots"]
description: "Fix Windows Recall on your Surface Pro 11 — won't enable, no snapshots, or stuck screens — with six ordered step-by-step fixes for Snapdragon X models."
thumbnail: "/images/thumbs/microsoft-surface-pro-11-recall-issues.webp"
faqs:
  - q: "Why is Recall missing from Settings on my Surface Pro 11?"
    a: "Recall only appears on Copilot+ PCs with 40+ TOPS NPUs, and the Snapdragon X Plus and Elite in the Surface Pro 11 qualify. If the page is missing, a prerequisite failed — usually BitLocker, Secure Boot, Microsoft account sign-in, or Windows Hello enrollment."
  - q: "Does Recall work on the Surface Pro 11 for Business?"
    a: "Business SKUs managed by an organization often have Recall disabled by IT policy. On personally owned devices, removing a work or school account from Settings > Accounts usually restores the option."
  - q: "Will enabling Recall slow down my Surface Pro 11?"
    a: "Noticeably little — Recall runs on the Snapdragon X NPU, not the CPU, so snapshots process in the background efficiently. The main cost is disk space, which you control through snapshot frequency and retention settings."
  - q: "Can I use Recall without a Microsoft account?"
    a: "No. Recall requires signing in with a Microsoft account plus Windows Hello enrollment — this is a security design decision by Microsoft, since snapshots are encrypted per user identity."
---

The Surface Pro 11 is Microsoft's own Copilot+ flagship — a Snapdragon X Plus or Elite machine that was practically designed around Windows Recall. So it is especially frustrating when Recall refuses to enable, saves no snapshots, or gets stuck on its welcome screens. The hardware qualifies without question, which means every Recall failure on this machine is a software, policy, or prerequisite problem — and those are fixable.

Recall's requirements are strict and its error messages are vague. It needs BitLocker device encryption, Secure Boot, a Microsoft account, Windows Hello enrollment, and a healthy NPU driver — and it must not be blocked by organization policy, which happens more often than owners expect. This guide walks the full checklist in technician order so you find the actual blocker instead of guessing.

Work through the six fixes below in sequence, testing Recall after each. Most Surface Pro 11 machines are fixed by the third step.

## Why this happens

- **BitLocker or Secure Boot not active:** Recall's security model requires device encryption and Secure Boot. Either one off — or merely reporting incorrectly — blocks Recall silently.
- **Microsoft account or Windows Hello missing:** Recall encrypts snapshots against your identity. A local account, or a Microsoft account without Hello enrollment, fails the check.
- **Organization policy blocking Recall:** A work or school account on the device, or MDM leftovers, can disable Recall. Personally owned devices hit this after enrolling in a workplace account even once.
- **NPU driver unhealthy on Snapdragon X:** Recall's snapshot processing runs on the Hexagon NPU. A corrupt Qualcomm NPU driver breaks Recall while everything else looks normal.
- **Stuck welcome or setup screens:** Recall's first-run flow can loop or freeze, usually after an interrupted update or a corrupted snapshot database.
- **Snapshot storage misconfigured:** If snapshots never appear, the storage location may be full, excluded, or pointed somewhere Recall cannot write.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify every Recall prerequisite explicitly

Do not assume the requirements are met — check each one, because Recall fails silently on the first missing item and never tells you which.

1. Open **Settings > Privacy & security > Device encryption** and confirm it shows encryption is on.
2. Run `msinfo32` and verify **Secure Boot State** reads **On**.
3. Go to **Settings > Accounts** and confirm you are signed in with a Microsoft account, then enroll in Windows Hello under **Sign-in options**.
4. Open **Settings > Privacy & security > Recall & snapshots** — if the page now appears, toggle **Save snapshots** on. If the NPU itself looks wrong in Device Manager, the [Surface Pro NPU detection guide](/articles/microsoft-surface-pro-npu-not-detected/) covers the driver side.

### Fix 2: Remove organization policy blocks

This is the most common surprise blocker on personally owned Surface Pro 11s. Any work or school account — even a removed one — can leave policies that disable Recall.

1. Go to **Settings > Accounts > Access work or school** and disconnect any listed organization account.
2. Check **Settings > Privacy & security > Recall & snapshots** again after signing out and back in.
3. If Recall still reports being managed by your organization, review the [Recall disabled by organization](/articles/recall-disabled-by-organization/) walkthrough for registry and policy cleanup steps.
4. On a true business-managed device, the fix is your IT admin — no local workaround will (or should) override their policy.

### Fix 3: Repair the Snapdragon X NPU driver

Recall processes snapshots on the NPU, so a broken Qualcomm NPU driver kills Recall while the rest of Windows seems fine. Surface drivers come from Windows Update and the Surface support channel.

1. In Device Manager, expand **Neural processors**, right-click the Qualcomm NPU, choose **Uninstall device**, and check **"Attempt to remove the driver for this device"**.
2. Restart — Windows will reinstall the driver from its driver store or Windows Update during boot.
3. Check **Settings > Windows Update** and install everything pending, including optional driver updates.
4. For the full Surface driver pack, see Microsoft's [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and the Surface support site for your exact model. If you suspect the driver is leaking rather than broken, the [NPU driver memory leak fix](/articles/npu-driver-memory-leak-fix/) covers that adjacent failure.

### Fix 4: Break out of the Recall welcome screen loop

If Recall opens its welcome or setup screens and never finishes — looping back or freezing — the first-run state is corrupted. Resetting it lets the flow start clean.

1. Open **Settings > Privacy & security > Recall & snapshots** and toggle **Save snapshots** off, then restart the Surface.
2. Toggle it back on and walk through the welcome screens again without skipping.
3. If the loop persists, delete the snapshot data: in the Recall settings page, use the option to delete snapshots, restart, and re-enable.
4. The dedicated [Recall welcome screen loop](/articles/recall-welcome-screen-loop/) guide has deeper steps if this does not break the cycle.

### Fix 5: Fix snapshot storage and frequency

When Recall is enabled but the timeline stays empty, snapshots are not being saved — usually a storage or scheduling problem rather than a Recall failure.

1. In **Recall & snapshots** settings, check the storage allocation and increase the maximum if it is set very low.
2. Confirm the snapshot location has free disk space — Recall pauses silently when the drive fills.
3. Review which apps and websites are excluded from snapshots; an over-broad exclusion list (or an inprivate-only browsing habit) leaves the timeline empty.
4. Tune how often snapshots are taken with the [Recall snapshot frequency settings](/articles/recall-snapshot-frequency-settings/) guide to balance history depth against disk usage.

### Fix 6: Reset Recall with a clean feature reinstall

When nothing else works, reinstalling the Recall experience itself clears corrupted components that toggles cannot reach.

1. Open **Settings > System > Optional features** (or Windows Features) and remove the Recall component if listed, then restart.
2. Re-add it, restart again, and re-enable snapshots in **Recall & snapshots** settings.
3. Walk the welcome flow completely — do not close it early this time.
4. Search the timeline for something you did an hour ago to confirm snapshots are actually landing. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents current Recall known issues if a Windows bug is the cause.

## Closing

Recall on the Surface Pro 11 fails on prerequisites, not hardware — the Snapdragon X NPU qualifies easily. Walk the checklist: BitLocker, Secure Boot, Microsoft account with Hello, no organization policy, healthy NPU driver, then the welcome flow and storage settings. Test the timeline after each fix so you know which one did it. If Recall still refuses after all six steps on a personally owned device, a Windows in-place repair install is the last resort before calling Microsoft support with your symptom log.
