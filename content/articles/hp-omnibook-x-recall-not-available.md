---
title: "How to Fix HP OmniBook X Recall Not Available on Your AI Laptop"
slug: hp-omnibook-x-recall-not-available
date: 2026-10-28
categories: ["ai-pc"]
tags: ["HP OmniBook X", "Recall", "Copilot+ PC", "AI laptop", "Windows 11"]
description: "Recall should be built into your HP OmniBook X, but sometimes it simply is not there. Learn why Recall is missing and how to bring it back. Do it now."
thumbnail: "/images/thumbs/hp-omnibook-x-recall-not-available.webp"
faqs:
  - q: "Why is Recall not available on my OmniBook X?"
    a: >
      Recall requires a Copilot+ PC with a qualifying NPU, the right Windows build, and opt-in setup. A missing requirement, a disabled feature, or an outdated build can all make Recall unavailable.
  - q: "Is the OmniBook X a Copilot+ PC?"
    a: >
      Yes, the HP OmniBook X is sold as a Copilot+ PC with a Snapdragon X Elite chip and a qualifying NPU, so Recall should be available once the software requirements are met.
  - q: "Can I install Recall separately?"
    a: >
      No. Recall is a Windows system feature, not a standalone app. It appears only when the hardware, Windows build, and settings all qualify, and it cannot be downloaded on its own.
  - q: "Do I have to use Recall if it becomes available?"
    a: >
      No. Recall is strictly opt-in. Even when it is available, it does nothing until you choose to enable it, and you can turn it off again at any time.
---

Recall is the flagship Copilot+ feature: a photographic memory for your PC that lets you search back through what you were doing, find a document you glimpsed hours ago, and pick up exactly where you left off. On the HP OmniBook X, which is sold as a Copilot+ PC, Recall should simply be there — so when it is not available at all, the gap is confusing. You check Settings, search the Start menu, and find nothing, while other Copilot+ features work fine.

The explanation is usually a checklist problem rather than a hardware failure. Recall has more requirements than most Windows features: a qualifying NPU, a specific Windows build, a supported region and language, enough storage, and an explicit opt-in. If any single requirement is unmet, Windows hides Recall entirely instead of showing a greyed-out option, which makes the problem look mysterious when it is actually specific.

This guide runs that checklist in order: confirming your hardware and build, checking region and storage, enabling the feature, and fixing the driver and update issues that hide Recall.

## Why this happens

- **Windows build too old:** Recall requires a recent Windows 11 build, and an OmniBook X that has not installed the right feature update will not show it.
- **NPU driver problem:** If the NPU driver is missing or erroring, Windows may not recognize the laptop as a qualifying Copilot+ PC for Recall.
- **Region or language not supported:** Recall rolls out by region and language, and an unsupported setting can hide the feature even on qualifying hardware.
- **Recall disabled by policy:** A work, school, or management policy can disable Recall, hiding it from Settings entirely.
- **Insufficient storage:** Recall needs free disk space for its snapshot database, and Windows may hide the feature when storage is critically low.
- **Feature not yet opted in:** Recall is opt-in, and until you complete its first-run setup, it may not appear as an active feature in some Settings views.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your Windows build and Copilot+ status

Start by verifying the foundation: the right Windows build on qualifying hardware.

1. Open Settings, go to System, then About, and note your Windows edition, version, and build number.
2. Check that the laptop reports a Snapdragon X Elite processor and an NPU in Device Manager.
3. Open Windows Update and install all available updates, including the latest feature update.
4. After updating, restart and search Settings for "Recall" to see whether it appears.
5. If your build is current and Recall is still missing, the blocker is a setting, driver, or policy rather than the build.

### Fix 2: Check region, language, and storage

Recall's availability depends on these three factors, and each is quick to check.

1. Open Settings, go to Time and language, then Language and region, and confirm your region is one where Recall is supported.
2. Confirm your Windows display language is a supported language for Recall.
3. Open Settings, go to System, then Storage, and make sure you have at least 50 GB free, since Recall needs room for snapshots.
4. Free space if needed by removing large unused apps or files, then restart.
5. Search Settings for Recall again after correcting region, language, or storage.

A similar availability-checklist fix resolves [Copilot key remapping problems](/articles/copilot-key-opens-wrong-app-remap/) when the assigned action is unavailable, and the same requirements logic applies when [VS Code Copilot Chat shows blank](/articles/vscode-github-copilot-chat-blank-arm/) because a component is missing. For a related app check, see [Notion AI problems on ARM](/articles/notion-ai-arm-laptop-issues-fix/).

### Fix 3: Fix the NPU driver

Windows only offers Recall when it can see a healthy qualifying NPU.

1. Open Device Manager, expand Neural processors, and check the NPU for warnings or errors.
2. Visit the official HP support site for the OmniBook X and download the latest chipset and NPU drivers.
3. Install the chipset driver first, restart, then install the NPU driver.
4. Check Task Manager's Performance tab to confirm the NPU appears as a working device.
5. Search Settings for Recall again after the NPU is healthy.

### Fix 4: Enable Recall in Settings

Once the requirements are met, Recall still needs its explicit opt-in.

1. Open Settings, go to Privacy and security, then Recall and snapshots.
2. Turn on "Save snapshots" and complete the first-run setup, including Windows Hello verification.
3. Choose which apps and websites Recall should exclude if you want to limit its scope.
4. Wait for the first snapshots to be captured, then open Recall from the taskbar or Start menu.
5. If the Recall page is still missing, restart once more, since feature visibility can lag behind driver and update changes.

### Fix 5: Check for management policies

A managed device can hide Recall even when everything else qualifies.

1. Check whether your OmniBook X is managed by a work or school account in Settings, under Accounts, then Access work or school.
2. Ask your IT administrator whether Recall is disabled by policy, since managed devices often block it deliberately.
3. On a personal device, check the Group Policy or registry only if you are comfortable doing so, and only to confirm no Recall policy is set.
4. If a policy is the blocker on a personal device, removing the management account may restore Recall, but back up your data first.
5. If the device is intentionally managed, Recall may be unavailable by design, and that is a policy decision rather than a fault.

### Fix 6: Repair Windows and check for known rollout delays

If everything qualifies and Recall is still missing, Windows itself may need repair or the rollout may not have reached you.

1. Open Settings, go to System, then Recovery, and run a repair install using Windows Update if the option is available.
2. Check Microsoft's official Recall requirements at [Microsoft Support](https://support.microsoft.com/en-us/windows) to confirm your configuration qualifies.
3. Search HP's support forum for OmniBook X Recall reports, since rollout timing can vary by model.
4. Keep Windows Update current and check for Recall monthly, since availability expands with new builds.
5. If Recall remains unavailable after all checks, contact HP support with your build number and NPU status for model-specific guidance.

## Closing

Recall missing from the OmniBook X feels like a broken promise, but it is usually a checklist item — a build, a driver, a region setting, or a policy — that hides the feature instead of a hardware defect. Work through the requirements in order, and Recall typically appears once the last blocker clears. And remember: even when it appears, Recall stays off until you choose to turn it on, so you remain in control of what it remembers.
