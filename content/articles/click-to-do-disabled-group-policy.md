---
title: "How to Fix Click to Do Disabled by Group Policy on Windows 11"
slug: click-to-do-disabled-group-policy
date: 2026-10-21
categories: ["ai-pc"]
tags: ["click to do disabled", "group policy", "click to do greyed out", "copilot+ pc", "windows 11", "registry fix"]
description: "Fix Click to Do disabled by Group Policy on your AI PC with six step-by-step methods covering policy editor, registry keys, MDM blocks, and debloat scripts."
thumbnail: "/images/thumbs/click-to-do-disabled-group-policy.webp"
faqs:
  - q: "Why does Click to Do say it is disabled by Group Policy?"
    a: "An administrator policy — or a registry value written by a debloat script, MDM enrollment, or enterprise baseline — explicitly turns Click to Do off. Windows then greys out the toggle even on personal laptops."
  - q: "I own this laptop — why is there a Group Policy on it?"
    a: "Group Policy settings can be written by more than domain admins: MDM enrollment, third-party privacy tools, and Windows debloat scripts all write the same registry keys, and Windows reports them as policy."
  - q: "Will editing the registry to re-enable Click to Do break anything?"
    a: "Removing the specific Click to Do policy values is safe and only affects that feature. Back up the registry key first and change only the named values."
  - q: "Can my employer re-disable Click to Do after I fix it?"
    a: "Yes. If the laptop is managed by Intune or another MDM, the policy will be re-applied at the next sync. On a managed device, ask your IT admin instead of fighting the policy locally."
---

Opening **Settings > Privacy & security > Click to Do** and finding the toggle greyed out with "disabled by Group Policy" is confusing on a laptop you own outright. The message is technically accurate but misleading: Windows calls several policy sources "Group Policy," including registry keys written by debloat scripts, school or work account enrollments, and privacy tools.

Click to Do is a Copilot+ headline feature, so a policy block kills text actions, image actions, and the whole Win + Q experience in one stroke. The fix is finding which source wrote the block and removing it — then making sure it does not come back.

This guide gives you six fixes in order: identifying the policy source, clearing it in the Group Policy editor, clearing it in the registry, handling MDM re-application, undoing debloat scripts, and verifying the feature unlocks.

## Why this happens

- **A debloat or privacy script disabled it:** "Windows 11 debloat" scripts aggressively turn off AI features by writing policy registry values — and Recall too, which shares the same policy family (see [Recall policy blocks](/articles/recall-group-policy-keeps-disabling/)).
- **Work or school account enrollment:** Signing in with an organizational account can enroll the device in MDM (Intune), which pushes a baseline disabling Click to Do. The block returns after every sync.
- **Enterprise baseline on a secondhand laptop:** A used Copilot+ PC may still carry policies from its previous corporate life, including a Click to Do block that survives a reset.
- **Registry value set directly:** Tools write `DisableClickToDo` (or related AI-experience values) straight into the Policies registry hive. Windows honors them exactly like Group Policy.
- **Feature prerequisites unmet:** Click to Do also disables itself — with a similar-looking message — when the NPU requirement is not met. If policies are clean, check the [NPU requirement error guide](/articles/studio-effects-npu-required-error/).
- **Fast Startup caching a stale policy state:** On ARM laptops, Fast Startup can preserve a policy state across "shutdowns," so a fix appears to do nothing. [Fast Startup quirks](/articles/fast-startup-issues-arm-laptop/) are worth knowing when policy changes do not apply.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify which policy is actually blocking Click to Do

Do not start deleting things blindly. First confirm the block is real and find its source — a domain policy, an MDM push, or a local registry value each needs a different fix.

1. Open **Settings > Privacy & security > Click to Do** and note the exact message.
2. Press **Win + R**, type `rsop.msc`, and check for Click to Do or Windows AI entries (Pro/Enterprise).
3. Open **regedit** and check `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsAI` for values like `DisableClickToDo` or `TurnOffAIDataAnalysis`.
4. Also check `HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\WindowsAI` for user-level blocks.
5. If the laptop is signed into a work/school account, assume MDM until proven otherwise.

### Fix 2: Clear the block in the Group Policy editor (Pro/Enterprise)

If the value came from real Group Policy, the editor is the clean way to remove it. Setting the policy to "Not configured" removes the registry value it was enforcing, which un-greys the Settings toggle after a policy refresh.

1. Press **Win + R**, type **gpedit.msc**, and go to **Computer Configuration > Administrative Templates > Windows Components > WindowsAI**.
2. Find the Click to Do policy (e.g., "Turn off Click to Do") and set it to **Not configured**.
3. Check **User Configuration > Administrative Templates > Windows Components > WindowsAI** and clear it there too.
4. In an elevated Command Prompt, run `gpupdate /force`, then restart.
5. Reopen **Settings > Privacy & security > Click to Do** and confirm the toggle is clickable.

### Fix 3: Remove the registry values directly (all editions)

Windows 11 Home has no gpedit, and scripts often write raw registry values anyway. Deleting the specific values under the Policies hives removes the block at its source. Export a backup first.

1. Press **Win + R**, type **regedit**, right-click `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows` and choose **Export** as a backup.
2. Go to `...\Windows\WindowsAI` and delete values such as `DisableClickToDo` or `TurnOffAIDataAnalysis` (only these named values).
3. Repeat under `HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\WindowsAI` if that key exists.
4. Do a full restart (not Fast Startup's hybrid shutdown) so the policy cache rebuilds.
5. Check the Click to Do Settings page; the toggle should now be enabled. Microsoft documents current policy names in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 4: Stop MDM or work-account re-application

If the block returns within hours or after a restart, something is re-applying it — almost always MDM from a work or school account. Fighting it locally is futile; the policy sync wins every time.

1. Go to **Settings > Accounts > Access work or school** and see if an organization is connected.
2. If you no longer need it, select the account and click **Disconnect** (this unenrolls MDM on personally owned devices).
3. Repeat Fix 3 to clear leftover registry values, then restart.
4. If the device must stay enrolled (employer-owned), ask your IT admin to allow Click to Do, citing the exact policy name.
5. Verify across two restarts that the toggle stays enabled.

### Fix 5: Undo debloat and privacy scripts

Debloat scripts are the most common source of this block on personally owned laptops. They write dozens of policy values at once, so removing just the Click to Do one may leave related AI features broken.

1. Check your downloads or script history for Windows debloaters or "privacy" scripts run after setup.
2. Re-run the script and look for an **undo**, **revert**, or **restore defaults** option covering AI features.
3. If no undo exists, manually review the `WindowsAI` and `WindowsCopilot` policy keys for disabled-AI values and reset them.
4. Check Task Scheduler for a task that re-applies settings at logon, and disable it.
5. Restart, clear any re-created values once more, then confirm Click to Do enables.

### Fix 6: Verify the feature actually works after unlocking

With every policy source cleared, confirm Click to Do works rather than just un-greys. A toggle that enables but a feature that still does nothing points at the NPU or a corrupted install.

1. In **Settings > Privacy & security > Click to Do**, turn the toggle on.
2. Press **Win + Q** on the desktop — the Click to Do overlay should appear.
3. Select text in Notepad and **Win + click** it to confirm actions show up.
4. Check Device Manager for a healthy NPU; without it, Click to Do cannot function regardless of policy.
5. If the toggle enables but nothing happens, run Windows Update — Click to Do components ship with feature updates.

## Closing

"Disabled by Group Policy" on a personal laptop is almost never a real administrator — it is a debloat script, an old MDM enrollment, or a leftover baseline. Find the source, clear it there, and confirm the toggle survives two restarts.
