---
title: "How to Fix Image Creator Not Working in Windows 11"
slug: image-creator-not-working-windows-11
date: 2026-10-20
categories: ["ai-pc"]
tags: ["image creator", "windows 11", "ai image generation", "troubleshooting", "ai pc", "copilot+"]
description: "Image Creator not working in Windows 11? Discover why AI image generation fails on your PC and follow proven step-by-step fixes to create images again."
thumbnail: "/images/thumbs/image-creator-not-working-windows-11.webp"
faqs:
  - q: "Where is Image Creator in Windows 11?"
    a: "Image Creator appears in Paint as part of Cocreator, in the Photos app editing tools, and in Copilot experiences. The on-device version needs a Copilot+ PC, while the cloud version works on any PC with a Microsoft account and internet."
  - q: "Does Image Creator need a Copilot+ PC?"
    a: "Only the on-device version does. Image Creator in Paint's Cocreator needs a 40+ TOPS NPU. The cloud version in Copilot generates on Microsoft's servers and works on any Windows 11 PC with a Microsoft account and internet connection."
  - q: "Why does Image Creator say I am out of boosts or credits?"
    a: "Microsoft rations generation with credits or boosts to manage demand. An empty balance slows or stops new images until refresh. Check your balance in the app and avoid bulk-generating dozens of images in one sitting."
  - q: "Image Creator worked yesterday but fails today. What changed?"
    a: "Overnight changes are usually a Store app update, a Windows update touching the NPU driver, exhausted credits, or a Microsoft service outage. Check credits first, verify the NPU in Task Manager, then look for app updates."
---

Image Creator brings text-to-image generation into Windows 11 — in Paint, Photos, and Copilot — and its error messages are rarely helpful. Sometimes the button is missing, sometimes generations spin forever, and sometimes a vague failure appears after a full minute of waiting.

The key is that Image Creator ships in on-device and cloud flavors with different requirements. On-device generation needs Copilot+ hardware with a healthy NPU; cloud generation needs an account, credits, and internet. A failure in either path looks identical to the user. For the Paint version specifically, our [Cocreator troubleshooting guide](/articles/cocreator-paint-not-working/) covers that path in depth, and [generative erase issues in Photos](/articles/generative-erase-photos-not-working/) share several NPU and account root causes.

This guide covers both flavors: identifying which version you use, checking hardware and account requirements, and repairing the app and driver layers underneath.

## Why this happens

- **Wrong flavor expectations:** On-device creation needs a 40+ TOPS NPU, while cloud features need an account instead.
- **NPU driver failure:** Local generation runs on the neural processor, so a broken driver silently disables it.
- **Microsoft account missing:** Both flavors need Microsoft sign-in; local accounts get greyed-out controls.
- **Credits exhausted:** The boosts system rations generation, and an empty balance stops new images quietly.
- **App is outdated:** Image Creator arrives through Store updates to Paint, Photos, or Copilot, so stale apps predate it.
- **Network or service outage:** Cloud generation needs Microsoft's servers, and outages defeat every local fix.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify which Image Creator you are using

Image Creator is several features sharing a name, and the fix depends on which one fails. The Paint version generates on-device and needs Copilot+ hardware. The Photos version mixes local and cloud processing. The Copilot version is fully cloud-based and works on any PC. Note exactly where the failing button lives — that identifies the broken pipeline. On a Copilot+ PC, check Task Manager's Performance tab for a healthy NPU, since on-device generation dies without it, like an [NPU that Windows fails to detect](/articles/npu-not-detected-windows-11/).

1. Note which app fails: Paint, Photos, or Copilot.
2. For Paint or Photos, check Task Manager's Performance tab for an NPU.
3. Confirm 40+ TOPS if on-device generation is expected.
4. For Copilot's cloud version, verify the internet connection works.

### Fix 2: Sign in and check your credit balance

Nearly every Image Creator path needs a Microsoft account, and credits are the most common silent failure. Find the profile icon in the app — unsigned-in or local-only accounts get no working controls. Sign in, then locate the credits or boosts indicator near the generation button. An empty balance means waiting for Microsoft's scheduled refresh; smaller batches stretch each refresh further. If sign-in loops, repair the account under Windows Settings, then Accounts.

1. Open the app and find its account or profile icon.
2. Sign in with your Microsoft account.
3. Locate the credits or boosts balance near the controls.
4. Generate a simple test image to confirm it works.

### Fix 3: Update the host app from the Microsoft Store

Image Creator ships inside Paint, Photos, and Copilot app updates — not Windows updates — so a patched system can run an outdated app missing the feature. Open the Store, go to your library, and force an update check. Install pending updates for Paint, Photos, and Copilot, then relaunch the failing app. Microsoft has fixed several generation bugs this way. If the Store claims all is current but versions look old, restart and recheck. [Microsoft's support documentation](https://support.microsoft.com/en-us/windows) covers Store troubleshooting.

1. Open the Microsoft Store and go to your Library.
2. Click Get updates and wait for the check.
3. Install updates for Paint, Photos, and Copilot.
4. Relaunch the failing app and test image generation.

### Fix 4: Repair the NPU driver for on-device generation

On a Copilot+ PC, a broken NPU driver is a prime suspect for Paint or Photos failures — on-device models cannot run without it. In Device Manager, inspect Neural processors or System devices for warnings or unknown-device labels. A generic driver swapped in by Windows Update is a classic post-update cause. Download the latest package from your laptop maker's support page, since OEM releases match your exact chip — an [AMD XDNA driver that refuses to install](/articles/amd-xdna-npu-driver-not-installing/) shows how finicky these can be. Reinstall, reboot, and confirm full TOPS in Task Manager.

1. Open Device Manager and find the NPU under Neural processors.
2. If flagged, uninstall it with driver removal checked.
3. Download the newest NPU driver from the manufacturer's support page.
4. Install, restart, verify Task Manager health, and test.

### Fix 5: Check network, region, and service status

Cloud Image Creator needs Microsoft's servers, so network blocks defeat local fixes. Confirm the internet works in a browser, then check for VPNs, firewalls, or DNS filtering blocking Microsoft's AI endpoints — briefly disabling the VPN is a quick test. Region gating applies too: set a supported region under Time and language settings if suspected. Finally, Microsoft's services do have outages; if everything local checks out, waiting a few hours is legitimate troubleshooting.

1. Confirm general internet access in your browser.
2. Temporarily disable any VPN and retry generation.
3. Check Windows region settings if gating is suspected.
4. Search the web for a Microsoft image-generation outage and retry later if confirmed.

### Fix 6: Reset the app to clear corrupted data

When everything checks out — hardware, sign-in, credits, current app, healthy network — corrupted app data remains. Paint, Photos, and Copilot are Store apps Windows can repair or reset safely. Go to Settings, then Apps, then Installed apps, find the host app, and open Advanced options. Try Repair first since it preserves data. If generation still fails, use Reset to wipe cached state, then sign in fresh.

1. Open Settings, then Apps, then Installed apps.
2. Find Paint, Photos, or Copilot — whichever hosts Image Creator.
3. Open Advanced options and click Repair, then test.
4. If still broken, click Reset, sign in fresh, and retest.

## Closing

Image Creator failures split into two camps: on-device problems rooted in NPU hardware and drivers, and cloud problems rooted in accounts, credits, and connectivity. Identify your flavor first, then work its chain — sign-in and credits, app updates, NPU health, network and region. Keep host apps and NPU drivers current, since Microsoft ships improvements through both.
