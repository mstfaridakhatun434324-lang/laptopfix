---
title: "Recall Group Policy Keeps Disabling It? How to Stop That on Windows 11"
slug: recall-group-policy-keeps-disabling
date: 2026-10-20
categories: ["ai-pc"]
tags: ["recall group policy", "recall keeps turning off", "troubleshooting", "ai pc", "windows 11 policy"]
description: "Recall turns itself off after every reboot? A Group Policy or MDM rule is likely forcing it off. Learn to find the policy and stop it disabling Recall."
thumbnail: "/images/thumbs/recall-group-policy-keeps-disabling.webp"
faqs:
  - q: "Why does Recall keep turning itself off?"
    a: "In almost every case, a Group Policy object or mobile-device-management rule is configured to disable Recall, and Windows re-applies it at every sign-in or policy refresh. Manual toggles in Settings get overridden within minutes or at the next reboot."
  - q: "Can I override the policy on a work laptop?"
    a: "No, not legitimately. On organization-managed PCs, IT administrators control these policies centrally, and local changes get reverted. Contact your IT department and ask whether Recall can be allowed for your device instead of fighting the policy."
  - q: "Does this affect Windows 11 Home?"
    a: "Windows 11 Home has no Group Policy editor, so a true Group Policy cannot be the cause there. On Home, the equivalent culprit is usually a registry value set by a debloating tool, a third-party privacy app, or a startup script."
  - q: "Will changing the policy delete my Recall snapshots?"
    a: "Changing the policy itself does not touch your snapshots. However, if the policy also disables snapshot saving, Recall may purge stored data depending on configuration. Re-enable promptly and check your timeline once the policy is corrected."
---

Few things are more frustrating than a setting that refuses to stay on. You enable Recall, everything works, and then — after a reboot, or sometimes within the hour — it's off again. When this happens, you're almost certainly not dealing with a bug. You're dealing with a policy: a Group Policy object, an MDM rule, or a registry value that tells Windows to keep Recall disabled, and Windows dutifully re-applies it on every refresh cycle.

This is most common on work or school laptops, where IT departments disable Recall deliberately. But it also strikes personal PCs, usually because a "privacy hardening" script, a debloating tool, or a third-party security suite set the policy value without making it obvious. This guide shows you how to find the exact policy responsible and stop it. Once Recall stays on, you may notice it using more memory than expected — the guide on [Recall using too much RAM](/articles/recall-high-ram-usage-fix/) covers that next.

If Recall isn't being disabled but is failing for security-prerequisite reasons, the guide on [Recall's Secure Boot requirement error](/articles/recall-secure-boot-requirement-error/) covers that family of problems.

## Why this happens

- **Domain Group Policy:** An Active Directory GPO targeting your PC or user account disables Recall, re-applied at every logon and policy refresh.
- **MDM enrollment:** Intune or another device-management service pushes a configuration profile that turns Recall off.
- **Local Group Policy:** Someone (or some tool) set the policy in the local Group Policy editor on a Pro-edition PC.
- **Registry values from debloat tools:** Privacy scripts write the policy registry keys directly, which works even on Windows 11 Home.
- **Third-party security suites:** Some security or "anti-spy" tools disable Recall as part of their privacy hardening and re-apply it on a schedule.
- **Startup scripts:** A logon script or scheduled task re-disables Recall each boot, mimicking policy behavior.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm a policy is actually the cause

Before changing anything, verify that a policy — not a crash or a failed service — is what's turning Recall off. When a policy controls a feature, Windows usually shows a "managed by your organization" notice on the Settings page.

1. Open Settings, go to Privacy & security, then the Recall & snapshots page.
2. Look for text like "Some of these settings are managed by your organization."
3. Re-enable Recall manually, reboot, and check whether it switched itself off again — a repeat offender confirms policy control.
4. If you see the managed-by-organization notice, a policy is confirmed — continue with the fixes below.

### Fix 2: Check the local Group Policy editor

On Windows 11 Pro, Education, or Enterprise, the local Group Policy editor may hold the disabling rule. This is the easiest policy to find and reverse on a PC you administer. Microsoft documents the available Recall policies in its [Windows support documentation](https://support.microsoft.com/en-us/windows).

1. Press Win + R, type `gpedit.msc`, and press Enter.
2. Navigate to Computer Configuration, Administrative Templates, Windows Components, Windows AI or the Recall-related node.
3. Look for a policy such as "Allow Recall to be enabled" or "Turn off Recall" and check its state.
4. Double-click it: if it is set to Disabled (or Enabled for a "turn off" policy), change it to Not Configured.
5. Run `gpupdate /force` in an elevated Command Prompt, restart, and test whether Recall stays on.

### Fix 3: Inspect the registry policy keys

Policies ultimately land in the registry, and tools that bypass the Group Policy editor write them directly. Checking these keys catches culprits that `gpedit.msc` never shows — especially on Windows 11 Home.

1. Press Win + R, type `regedit`, and press Enter (back up the registry first via File, Export).
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows` and look for Recall or WindowsAI subkeys.
3. Check `HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows` for the same keys.
4. If you find values like DisableRecall or similar set to 1, note their exact paths before touching them.
5. Delete or reset only the Recall-related policy values you can positively identify.
6. Restart the PC and verify Recall remains enabled after a full reboot cycle.

### Fix 4: Check MDM enrollment and Intune profiles

If your PC is enrolled in mobile device management — common with work accounts added under Accounts, Access work or school — policies arrive from the cloud and local edits get overwritten within hours. Identifying enrollment tells you whether local fixes can ever stick.

1. Open Settings, go to Accounts, then Access work or school.
2. Check whether a work or school account is connected and whether MDM enrollment is mentioned.
3. Look for any configuration profile mentioning Recall, Windows AI, or snapshot features set to disabled.
5. You cannot remove an organization's profile yourself — contact your IT administrator to request an exception.
6. If the enrollment is stale (old job or school), disconnect the account, restart, and re-test Recall.

### Fix 5: Remove or reconfigure third-party privacy tools

"Anti-spy" utilities, debloaters, and some security suites disable Recall as part of privacy hardening, then re-apply their settings on a schedule or at boot.

1. Review installed apps for privacy tools or debloaters you may have run.
2. Open each tool and look for a Recall, snapshot, or "Windows AI" toggle in its settings.
3. Change the tool's Recall setting to allow or neutral rather than block.
4. Disable any task whose action re-disables Recall, or uninstall the tool if you no longer want it.
5. Restart and confirm Recall stays enabled for at least 24 hours before declaring victory.

### Fix 6: Audit startup scripts and scheduled tasks

A logon script or scheduled task that runs a disabling command at every boot produces exactly this symptom. Don't confuse this with app-level Copilot problems such as the [Designer image creator error](/articles/copilot-designer-image-creator-error/) — those are unrelated to policy.

1. Open Task Scheduler and browse the Task Scheduler Library for tasks referencing Recall, snapshots, or privacy.
2. Check the Actions tab of any suspicious task for commands or scripts touching Recall settings.
3. Disable tasks you can identify as the culprit; do not delete system tasks you don't recognize.
4. Press Win + R, type `shell:startup`, and check the Startup folder for scripts.
5. Restart twice — once to test, once to be sure — and confirm Recall remains on.

## Closing

A Recall that keeps disabling itself is Windows following orders, not malfunctioning — your job is to find who gave the order. Work from the Settings notice to the policy editor, the registry, MDM enrollment, third-party tools, and scheduled tasks to find the source. On personal PCs the fix is yours to make; on managed PCs the honest answer is a conversation with IT. If you suspect the hardware side of your Copilot+ PC needs attention too, the guide on [NPU high power usage draining the battery](/articles/npu-high-power-usage-draining-battery/) covers keeping the AI hardware stack healthy.
