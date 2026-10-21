---
title: "How to Fix the Windows Recall Welcome Screen Loop on Copilot+ PCs"
slug: recall-welcome-screen-loop
date: 2026-10-21
categories: ["ai-pc"]
tags: ["recall welcome screen loop", "windows recall", "recall onboarding", "copilot+ pc", "recall setup", "windows 11"]
description: "Fix the Recall welcome screen loop on your Copilot+ PC with six step-by-step methods covering the onboarding flag, snapshots, Group Policy, and driver repair."
thumbnail: "/images/thumbs/recall-welcome-screen-loop.webp"
faqs:
  - q: "Why does the Recall welcome screen keep appearing after setup?"
    a: "Windows stores an onboarding-completion flag for Recall. If the wizard is closed instead of finished, a policy blocks snapshots, or the snapshot database fails validation, the flag never gets written and the welcome screen returns on every boot."
  - q: "Will fixing the welcome loop delete my Recall snapshots?"
    a: "Not necessarily. Re-completing the wizard or correcting a policy setting preserves existing snapshots. Only the fixes that explicitly clear the snapshot store remove them, and the guide says so before each such step."
  - q: "Can Group Policy cause the Recall welcome screen loop?"
    a: "Yes. If an administrator policy disables Recall snapshotting, the welcome wizard can never complete its final step, so it reappears each sign-in. Checking the Recall-related policies is one of the core fixes below."
  - q: "Is the welcome loop a sign my NPU is broken?"
    a: "No. The loop is a software and configuration issue — onboarding state, policies, or a corrupt snapshot database. NPU hardware faults show up as device errors in Device Manager, not as a repeating setup screen."
---

Finishing the Windows Recall welcome screen, restarting your laptop, and being greeted by the same welcome screen again is maddening. The onboarding wizard is supposed to record that you completed it and never show itself again — when that completion flag never gets written, the wizard treats every sign-in like your first.

Recall is the flagship AI feature of Copilot+ PCs, so a looping welcome screen blocks the entire experience: no snapshots, no timeline search, no semantic recall of your past activity. The laptop feels broken even though everything underneath is probably fine.

This guide walks through six fixes in order, starting with the simplest explanation — the wizard was dismissed instead of completed — and moving through policy settings, a corrupt snapshot store, and driver repair. Most loops clear by Fix 3.

## Why this happens

- **The wizard was closed instead of completed:** Clicking the X or pressing Escape dismisses the welcome screen without writing the onboarding-completion flag, so Windows shows it again next sign-in.
- **Snapshot saving gets blocked by policy:** The welcome flow finishes only when snapshotting is enabled. If a Group Policy or registry setting disables snapshots, the final step can never succeed and the wizard loops. The same policy family is known for [disabling Recall outright](/articles/recall-group-policy-keeps-disabling/).
- **Corrupt snapshot database fails validation:** Onboarding checks the snapshot store before marking setup complete. A database corrupted by a crash or interrupted update fails that check, and the wizard restarts.
- **User profile or permissions problem:** If your profile lacks write access to the Recall data folder, or the profile itself is damaged, the completion flag cannot be saved.
- **NPU or display driver instability:** The welcome screen uses the same AI and display stack as [Studio Effects creative filters](/articles/studio-effects-creative-filters-missing/). A crashing driver can kill the wizard mid-flow, which looks like a dismissal.
- **Scaling misfires on ARM laptops:** On Snapdragon machines with aggressive display scaling, the wizard's final button can render off-screen. See the [display scaling guide](/articles/display-scaling-issues-snapdragon-laptop/) if the wizard looks oversized or cut off.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Complete the wizard end-to-end instead of dismissing it

The most common cause is also the simplest: the welcome screen was closed with the X button or Escape, which never records completion. Only clicking the final confirmation button writes the flag.

1. When the welcome screen appears, do not press Escape or click the X — work through every page.
2. On the snapshots page, toggle **Save snapshots** on and choose your snapshot storage limit.
3. On the final page, click **Finish** or **Start using Recall** and wait for the wizard to close itself.
4. Restart the laptop and confirm the welcome screen does not return.
5. If it returns anyway, the flag is being blocked or reset — continue to Fix 2.

### Fix 2: Toggle Recall snapshotting off and back on in Settings

The onboarding flag lives alongside the snapshot setting in **Settings > Privacy & security > Recall & snapshots**. Toggling it forces Windows to re-evaluate Recall's state and rewrite its configuration, clearing stale onboarding data.

1. Open **Settings > Privacy & security > Recall & snapshots** (see the [official support page](https://support.microsoft.com/en-us/windows) for navigation help).
2. Turn **Save snapshots** off, wait 30 seconds, then turn it back on.
3. Re-run the welcome wizard when prompted and complete every page through the final button.
4. Restart and verify the welcome screen stays gone for two consecutive boots.

### Fix 3: Check the Group Policy and registry settings that block Recall

If a policy disables Recall, the wizard can never finish — it loops because its last step is forbidden. This hits managed laptops and machines that once ran a debloat script. The policies live under Computer Configuration > Administrative Templates > Windows Components > WindowsAI.

1. Press **Win + R**, type **gpedit.msc** (Pro/Enterprise), and go to **Computer Configuration > Administrative Templates > Windows Components > WindowsAI**.
2. Set **"Turn off saving snapshots for Windows"** and **"Turn off Windows Recall"** to **Not configured** or **Disabled**.
3. On Home edition, open **regedit** and check `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsAI` for `TurnOffSavingSnapshots` — delete it or set it to 0.
4. Restart and complete the wizard; with the block removed, the final step can succeed.
5. If a script or MDM keeps re-applying the policy, look for third-party privacy tools running at startup.

### Fix 4: Clear the corrupt snapshot store and re-onboard

When the snapshot database is corrupt, onboarding's validation step fails silently and the wizard starts over. Deleting the store lets Recall rebuild it cleanly. **This removes existing snapshots**, so use it only if you have none worth keeping.

1. In **Settings > Privacy & security > Recall & snapshots**, click **Delete snapshots** and confirm.
2. Restart the laptop, then complete the welcome wizard from the first page.
3. Verify Recall captures a snapshot: open an app, wait a few minutes, and check the Recall timeline.
4. If snapshots still do not save, see the [Recall not working guide](/articles/windows-recall-not-working/) for deeper snapshot failures.

### Fix 5: Repair the NPU and display drivers the wizard depends on

A driver crash during onboarding looks exactly like a dismissal — the wizard vanishes, no completion flag is written, and it returns next boot. If the welcome screen ever flickered, froze, or vanished on its own, suspect the driver stack.

1. Download the latest chipset/NPU and graphics drivers for your exact model from Dell, HP, or Lenovo support.
2. Install both packages as administrator and restart when prompted.
3. On Intel Core Ultra machines, also run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch missed NPU updates.
4. Re-run the wizard and watch whether it still vanishes mid-flow.
5. If it now completes, confirm an NPU feature like live captions works to prove the stack is healthy.

### Fix 6: Test in a new local user profile and repair system files

If the loop survives every fix, your user profile may be unable to persist Recall's settings. A fresh local profile isolates that in minutes, and system-file repair fixes corrupt Windows components that block the flag.

1. Go to **Settings > Accounts > Other users** and add a new local administrator account.
2. Sign into the new account and complete the Recall welcome wizard there.
3. If the wizard completes and stays gone, your main profile is damaged — migrate to the new one.
4. On the original profile, run `sfc /scannow` then `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated Command Prompt.
5. Restart, sign into your main profile, and complete the wizard one final time.

## Closing

The Recall welcome screen loop is a bookkeeping failure: something keeps the onboarding flag from sticking. Usually the answer is completing the wizard properly, removing a snapshot-blocking policy, or clearing a corrupt snapshot store. Verify across two restarts.
