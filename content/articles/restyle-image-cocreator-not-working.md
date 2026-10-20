---
title: "How to Fix Restyle Image in Cocreator Not Working on Windows 11"
slug: restyle-image-cocreator-not-working
date: 2026-10-20
categories: ["ai-pc"]
tags: ["restyle image", "cocreator paint", "troubleshooting", "ai pc", "image creator", "copilot+ pc"]
description: "Restyle Image in Cocreator not working in Paint? Discover why the AI restyle button fails on Copilot+ PCs and the exact steps to get it working again."
thumbnail: "/images/thumbs/restyle-image-cocreator-not-working.webp"
faqs:
  - q: "Why is the Restyle Image button greyed out in Cocreator?"
    a: "The Restyle Image button is usually greyed out because your PC does not meet the Copilot+ requirements, you are not signed in with a Microsoft account, or the NPU driver is not working. Paint's AI features need a 40+ TOPS NPU and the latest Paint update from the Microsoft Store."
  - q: "Does Restyle Image need an internet connection?"
    a: "Yes, for most styles Restyle Image sends a request to Microsoft's cloud image service, so a stable internet connection and a signed-in Microsoft account are required. Some Cocreator generation runs on the NPU locally, but restyling still relies on cloud models."
  - q: "Which PCs support Restyle Image in Cocreator?"
    a: "Restyle Image requires a Copilot+ PC with a neural processing unit rated at 40 TOPS or higher, running Windows 11 version 24H2 or later. This includes Snapdragon X, Intel Lunar Lake, and AMD Ryzen AI 300 series laptops."
  - q: "How do I reset Paint if Cocreator features stop working?"
    a: "Open Settings, go to Apps, then Installed apps, find Microsoft Paint, click the three dots, choose Advanced options, and use Repair first. If the problem persists, use Reset, which clears Paint's data and restores Cocreator and Restyle Image to a clean state."
---

Paint's Cocreator panel turns rough sketches into finished illustrations, and the Restyle Image button applies an artistic style to any picture with a single click. So when Restyle Image does nothing, stays greyed out, or throws a vague error — especially on a brand-new Copilot+ PC sold on these features — it is frustrating. The good news: it is rarely a hardware failure. It is almost always a settings, sign-in, or update problem.

Restyle Image depends on a small chain of things working together: a Copilot+ capable NPU, the current version of Paint from the Microsoft Store, a signed-in Microsoft account, and a working connection to Microsoft's cloud image service. If any link in that chain breaks, the button either disappears or silently refuses to work. Understanding that chain is the key to a fast fix, because each failure mode points at a different link.

In this guide you will learn why Restyle Image in Cocreator stops working and how to fix it step by step — starting with the quick checks that solve it for most people, then driver and update repairs, then deeper resets for stubborn cases. If you are sorting out [Lenovo ThinkPad T14s Snapdragon issues](/articles/lenovo-thinkpad-t14s-snapdragon-issues/) or [Recall secure boot requirement errors](/articles/recall-secure-boot-requirement-error/) on the same machine, many of the same NPU and update checks apply there too.

## Why this happens

- **PC is not a Copilot+ PC:** Restyle Image needs an NPU rated at 40 TOPS or more. Older laptops, even fast ones, show Cocreator without the restyle option because the hardware requirement is not met.
- **Not signed in with a Microsoft account:** Cocreator and Restyle Image require a Microsoft account sign-in. A local-only Windows account will leave the features disabled or greyed out.
- **Outdated Paint app:** The restyle feature only exists in recent Paint versions. If the Microsoft Store has not updated Paint, the button may be missing or broken.
- **NPU driver problems:** A missing, outdated, or crashed NPU driver stops the on-device part of Cocreator from initializing, which can also break Restyle Image. See our guide on [NPU not detected in Windows 11](/articles/npu-not-detected-windows-11/) if Device Manager shows no neural processor.
- **Cloud service or network blocked:** Restyle requests go to Microsoft's servers. A firewall, VPN, metered connection, or regional restriction can silently block them.
- **Corrupted Paint data or cache:** A damaged app cache after a Windows update can leave Cocreator half-functional, with generation working but restyle failing.
- **Content policy rejection:** Restyle Image refuses certain images and prompts for safety reasons. If only some pictures fail, the content filter — not a bug — is the cause.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your PC actually supports Restyle Image

Restyle Image is a Copilot+ exclusive with no workaround for non-qualifying hardware, so verify your machine first. Check Settings, System, About for a Snapdragon X, Intel Core Ultra 200V, or AMD Ryzen AI 300 chip, then confirm an NPU entry in Task Manager's Performance tab. No NPU means Restyle Image will never appear — focus on features your hardware supports.

1. Press Windows + I to open Settings, then go to System and click About.
2. Note your processor name and confirm it is a Copilot+ class chip (Snapdragon X, Intel Core Ultra 200V, or AMD Ryzen AI 300).
3. Press Ctrl + Shift + Esc to open Task Manager and click the Performance tab.
4. Look for an NPU tile on the left; click it to confirm it shows activity and driver details.

### Fix 2: Sign in with a Microsoft account

Cocreator's cloud features check your sign-in state before they enable the Restyle button. A local account, a work or school account with restrictions, or a stale sign-in token will keep it greyed out. Signing in with a personal Microsoft account and refreshing the account token fixes this in seconds.

1. Open Settings, go to Accounts, then click Your info.
2. If it says Local Account, click "Sign in with a Microsoft account instead" and complete the sign-in.
3. After signing in, restart Paint completely (close it from Task Manager if needed).
4. Open Paint, click the Cocreator icon, and check whether Restyle Image is now active.

### Fix 3: Update Paint and Windows to the latest versions

An old Paint build is one of the most common causes of a missing or broken Restyle button. Microsoft ships Cocreator improvements through Store updates, and Restyle Image also needs Windows 11 version 24H2 or newer. Update both before trying anything deeper.

1. Open the Microsoft Store and click Library in the bottom-left corner.
2. Click "Get updates" and wait for Microsoft Paint to update if an update is listed.
3. Open Settings, go to Windows Update, and click "Check for updates".
4. Install all available updates, including any optional driver updates shown.

### Fix 4: Repair or reset the Paint app

If Paint is current but Restyle Image still fails, the app's local data may be corrupted — a frequent side effect of major Windows updates. Windows includes built-in Repair and Reset options that fix this without reinstalling anything. Repair keeps your data; Reset wipes it, so try Repair first. For detailed background on Windows app troubleshooting, the [official Windows support hub](https://support.microsoft.com/en-us/windows) documents these steps.

1. Open Settings, go to Apps, then click Installed apps.
2. Scroll to Microsoft Paint (or search for "Paint"), click the three dots, and choose Advanced options.
3. Click the Repair button and wait for the checkmark to appear.
4. Open Paint and test Restyle Image in the Cocreator panel.

### Fix 5: Fix the NPU driver

Cocreator initializes against the NPU at startup, and a broken NPU driver can leave Restyle Image dead even when the rest of Paint looks fine. Device Manager will usually show the problem as a warning icon on the neural processor or an unknown device. Reinstalling the correct driver from your laptop maker restores the handshake Paint expects.

1. Press Windows + X and open Device Manager.
2. Expand System devices (or Neural processors) and look for your NPU entry.
3. If it shows a yellow warning, right-click it and choose Uninstall device, ticking "delete driver" if offered.
4. Restart the laptop so Windows attempts a fresh driver install.

## Closing

Restyle Image usually fails for a fixable reason: unsupported hardware, missing Microsoft account sign-in, outdated Paint, a broken NPU driver, or a blocked cloud connection. Work through the fixes in order, then keep Paint and NPU drivers updated.
