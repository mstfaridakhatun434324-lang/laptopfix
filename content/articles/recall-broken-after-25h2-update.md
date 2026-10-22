---
title: "Recall Broke After the 25H2 Update? Restore It Step by Step"
slug: recall-broken-after-25h2-update
date: 2026-10-22
categories: ["ai-pc"]
tags: ["recall", "windows-11", "25h2", "ai-pc", "update", "troubleshooting"]
description: "Did the Windows 11 25H2 feature update break Recall on your Copilot+ laptop? Follow these ordered steps to re-enable snapshots and get the timeline working."
thumbnail: "/images/thumbs/recall-broken-after-25h2-update.webp"
faqs:
  - q: "Why do feature updates break Recall so often?"
    a: >
      Feature updates replace core system components that Recall depends on,
      including the AI model runtime, the snapshot service, and Hello's credential
      plumbing. Settings can reset and component versions can mismatch, which is
      why Recall usually needs a deliberate re-enable after a big update.
  - q: "Will I lose my old snapshots after fixing Recall post-update?"
    a: >
      Usually not. Most post-update failures are settings or binding problems, and
      the existing snapshot store survives the repairs in this guide. Only the
      explicit Delete snapshots step removes history, so avoid that unless nothing
      else works.
  - q: "Recall says my device no longer meets requirements after 25H2. Is that real?"
    a: >
      Sometimes yes and sometimes no. Updates can misreport the NPU or memory
      check until drivers catch up. Update your chipset and NPU drivers first; if
      the warning persists after that, then take the requirements message at face
      value.
  - q: "How long should I wait before assuming Recall is broken after an update?"
    a: >
      Give it at least a few hours of plugged-in idle time. Post-update, Windows
      re-indexes and reprocesses in the background, and Recall can look dead while
      that backlog clears. Only start the repairs below after that window.
---

Feature updates are supposed to make Windows better, but on Copilot+ laptops the 25H2 update has a habit of breaking Recall on the way through. The symptoms vary: Recall is suddenly toggled off, the timeline is empty, the setup wizard hangs on "Setting up" forever, or every snapshot demands Hello verification in a loop. The update itself usually installed fine, which makes the whole thing feel random. It is not random; it follows a pattern.

During a feature update, Windows replaces the system components Recall depends on: the on-device AI model runtime, the snapshot capture service, and the Hello credential plumbing that protects the store. Any one of those can come back in a mismatched state, and Recall's own toggle in Settings sometimes flips off as collateral. Before diving into repairs, confirm this is actually update damage and not a general failure. Our guide to [Recall not working after updates](/articles/recall-not-working-after-update/) covers the generic post-update checklist.

It is also worth distinguishing a stalled setup from a dead feature. If Recall is stuck mid-setup, the fix path differs from a Recall that opens but shows nothing. Our walkthrough for [Recall stuck on setting up](/articles/recall-stuck-on-setting-up/) handles that specific hang. Below, we assume the common 25H2 case: Recall worked before the update and broke after it, and we restore it in dependency order.

## Why this happens

- **Recall toggle reset by the update:** feature updates can flip the Recall setting off during migration. Everything underneath is healthy, but no new snapshots are captured until you re-enable it.
- **AI model runtime version mismatch:** 25H2 ships a new model runtime, but the Recall service may still reference the old one until servicing completes, leaving capture and search half-functional.
- **Hello credential container recreated:** the update can rebuild the TPM-backed Hello container, orphaning Recall's encryption binding so snapshots fail to open or the PIN prompt loops.
- **NPU or chipset drivers outdated:** Recall's on-device processing needs current NPU drivers. After 25H2, old drivers can fail the hardware check, and Recall reports the device as unsupported.
- **Corrupted system files from the upgrade:** interrupted or partial upgrades leave damaged system files that Recall's service depends on, producing crashes or a perpetually "setting up" state.
- **Third-party software conflicts:** security tools and utilities that hook into the display pipeline can break against 25H2's changed internals, silently blocking snapshot capture.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Re-enable Recall and confirm it is actually on

The most common 25H2 outcome is also the simplest: the update turned Recall off. Re-enabling it and confirming the toggle sticks resolves a large share of reports without any deeper repair.

1. Open Settings, Privacy and security, then Recall and snapshots.
2. If Recall is off, turn it on and complete any Hello verification prompt.
3. Restart the laptop, then return to the same page and confirm the toggle is still on.
4. Use the laptop normally for thirty minutes, then open Recall and check for fresh snapshots.
5. If the toggle turns itself back off, skip ahead to Fix 5, since something is actively disabling it.

### Fix 2: Repair the Hello binding the update disturbed

When Recall opens but every snapshot triggers a PIN loop or a decryption error after 25H2, the update almost certainly recreated your Hello container. Re-enrolling the PIN and re-binding Recall fixes the identity mismatch.

1. Go to Settings, Accounts, Sign-in options, then PIN (Windows Hello), and click Remove.
2. Restart the laptop so the TPM clears the old container left behind by the update.
3. Return to Sign-in options, add a new PIN, and sign out and back in once.
4. In Recall settings, toggle Recall off and on, completing Hello verification when asked.
5. Test snapshots from before the update; if they open, the binding is healed.

### Fix 3: Update NPU, chipset, and graphics drivers

Recall's hardware check runs against your NPU and chipset drivers, and 25H2 frequently outpaces the drivers that shipped with the laptop. Updating them clears false "device not supported" states and restores the processing pipeline.

1. Open Device Manager and expand System devices and Neural processors, if listed.
2. Right-click the NPU and chipset entries and choose Update driver, then Search automatically.
3. Visit your laptop maker's support site for 25H2-ready drivers. [Lenovo's support portal](https://support.lenovo.com/us/en/) publishes them by model, for example.
4. Intel-based Copilot+ laptops can also use the [Intel Driver and Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch everything at once.
5. Restart after driver updates, then confirm Recall's requirements page no longer shows a hardware warning.

### Fix 4: Repair system files with DISM and SFC

If Recall crashes, hangs on setup, or throws generic errors after 25H2, the upgrade may have left damaged system files. The built-in repair tools fix this without touching your data or settings.

1. Open Terminal as administrator from the Start menu.
2. Run DISM /Online /Cleanup-Image /RestoreHealth and wait for it to finish; this can take fifteen minutes.
3. When DISM completes, run sfc /scannow in the same window.
4. Restart the laptop after both tools report no remaining corruption.
5. Open Recall and test capture and search; if the service was crashing, it should now start cleanly.

### Fix 5: Check for software that is disabling Recall

Some security suites and system utilities disable Recall deliberately, and their 25H2 updates can start doing so where they did not before. If the toggle will not stay on, an outside program is usually responsible.

1. Temporarily disable third-party antivirus or endpoint protection and check whether Recall stays enabled.
2. Look through recently updated utilities for any "privacy" feature that mentions Recall, screenshots, or screen capture, and turn it off.
3. Check Task Scheduler for vendor tasks that modify Recall's registry settings and disable them.
4. Re-enable Recall in Settings and restart to confirm the toggle now persists.
5. If a specific program is the cause, check its vendor site for a 25H2-compatible version rather than leaving protection off.

### Fix 6: Reset Recall's store as a last resort

When every repair above fails and Recall remains broken, the snapshot store or its configuration may be damaged beyond binding repairs. Resetting gives Recall a clean slate on the new OS build.

1. In Settings, Privacy and security, Recall and snapshots, click Delete snapshots and confirm.
2. Toggle Recall off, restart the laptop, then toggle it back on.
3. Complete Hello verification to establish a fresh binding on 25H2.
4. Grab the latest Windows 11 image from the [official download page](https://www.microsoft.com/en-us/software-download/windows11) only if you suspect the installed update itself is damaged beyond DISM's ability to repair.
5. Use the laptop for a few hours and confirm new snapshots capture, open, and search correctly.

## Closing

Post-update Recall failures look chaotic, but they follow the update's own footprint: a flipped toggle, a disturbed Hello binding, outdated drivers, or damaged system files. Work the list in dependency order and resist the urge to delete snapshots until the repairs have had their chance; the history usually survives. Once Recall is capturing again on 25H2, leave Windows Update on so the AI components stay matched to the OS. Two other things that commonly misbehave after big updates on the same machine: [Studio Effects clashing with virtual cameras](/articles/studio-effects-obs-virtual-camera-conflict/) and [Slack running slowly under ARM emulation](/articles/slack-arm-windows-slow/); both have dedicated fixes.
