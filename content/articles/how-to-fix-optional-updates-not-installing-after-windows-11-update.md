---
title: "How to Fix Optional Updates Not Installing After a Windows 11 Update"
slug: "how-to-fix-optional-updates-not-installing-after-windows-11-update"
date: 2026-10-11
categories: ["windows-update"]
tags: ["optional updates", "windows update", "windows 11", "drivers"]
description: "Optional updates not installing after a Windows 11 update? Six fixes for stuck optional drivers and feature packs, from unpausing to metadata resets."
thumbnail: "/images/thumbs/how-to-fix-optional-updates-not-installing-after-windows-11-update.webp"
faqs:
  - q: "Where do I find optional updates on Windows 11?"
    a: "Open Settings, then Windows Update, then Advanced options, and expand Optional updates. Drivers, firmware, and feature experience packs appear there. Select the ones you want and click Download and install. Note that some optional drivers only appear when Windows detects the hardware needs them — an empty list usually means nothing optional is currently applicable, not that the feature is broken."
  - q: "Should I install all optional updates?"
    a: "Generally no, with one exception: install optional driver updates only when you have a specific reason, such as fixing a misbehaving device or filling in for a missing manufacturer driver. Optional drivers are older WHQL packages, and installing them over a newer manufacturer driver can downgrade your hardware support. Security and quality updates are never optional in this sense — those install through the main channel automatically."
  - q: "An optional driver keeps failing — hide it or force it?"
    a: "If the offered driver is older than your installed one, hiding it with the wushowhide tool is the correct outcome — forcing an older driver in is a downgrade. But if the optional package is genuinely newer or fills a missing driver, work through the fixes: clear pauses and metered flags, reset the update components, and install the manufacturer’s package directly if Windows Update keeps failing on it."
  - q: "Is it safe to ignore optional updates completely?"
    a: "No. Optional updates are, by definition, not required for security or stability — that is why they sit in a separate list. Skipping them entirely is safe. The one nuance: if a device is misbehaving and its driver appears under optional updates, installing that specific package (or the manufacturer’s equivalent) is worth doing as a targeted fix rather than ignoring it."
---

After a Windows 11 update, you open the Optional updates list expecting new drivers or feature packs — and nothing installs. The entries sit there, you click Download and install, and they either fail quietly or never start at all. Because these updates are “optional,” Windows gives you almost no error detail, which makes the problem feel vague.

It is not vague once you know the mechanics: optional updates are the lowest-priority downloads in the system, so every upstream condition — pauses, metered flags, stuck services, version conflicts — hits them first and hardest. On HP hardware the same symptom has machine-specific twists covered in the [HP optional-updates guide](/articles/how-to-fix-optional-updates-not-installing-windows-11-on-hp-laptop/).

## Why this happens

- **Optional updates paused by the main update toggle:** Pausing all updates also pauses the optional section; users forget the pause is active and blame the optional list.
- **Driver already at a newer version:** If the manufacturer driver installed is newer than the optional offer, Windows may list it but fail or skip the install silently.
- **Corrupted optional-update metadata:** The metadata describing optional packages can desync from the actual catalog, leaving entries that can never install.
- **Metered connection filtering optionals first:** Optional updates are the first downloads Windows sacrifices on metered connections, producing endless “not installing” behavior.
- **Stuck Windows Update service state:** A hung wuauserv or BITS session blocks the optional queue behind the main queue without any visible error.
- **Third-party driver tools holding locks:** OEM or third-party driver utilities can lock the target drivers, so the optional install fails at the file-replacement step.
- **Insufficient disk space for staging:** Optional driver and feature-experience packages still need staging space; a full drive fails them quietly.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Clear pauses and metered flags blocking the optional queue

Two silent blockers sit above the optional list: the global pause and the metered connection flag. Both suppress optional downloads without marking the individual entries as blocked, so the list just sits there, inert. Clear both before touching anything else.

1. Open Settings > Windows Update and check for any “Updates paused” message; click Resume updates if present.
2. Go to Advanced options and confirm the pause toggle is off.
3. Check the metered setting on your connection (Settings > Network & internet > Wi-Fi > your network).
4. Return to Optional updates and retry the specific package.

### Fix 2: Install optional updates one at a time

Selecting a dozen optional updates at once lets one bad package jam the whole batch with no indication of which one failed. Installing them individually isolates the offender in a single pass and is the fastest way to identify a package worth hiding.

1. Open Settings > Windows Update > Advanced options > Optional updates.
2. Untick everything except the one package you actually want.
3. Click Download and install and watch that single package.
4. If it succeeds, the queue was the problem; add others back one at a time.

### Fix 3: Compare versions before installing optional drivers

An optional driver offer is not a recommendation — it is just availability. Comparing versions first prevents the classic mistake of downgrading a working manufacturer driver to an older WHQL package and then wondering why performance dropped.

1. Open Device Manager and check the device’s current driver version versus the optional offer.
2. If your installed driver is newer, do not install the optional — hide it with wushowhide instead.
3. If the optional is newer or the device has no working driver, proceed with the install.
4. For graphics and Wi-Fi, prefer the manufacturer package from [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html).

### Fix 4: Reset update components to refresh optional metadata

When optional entries are stale or phantom — listed but uninstallable — the metadata describing them is corrupt. Resetting the update components forces Windows to re-query the catalog, which clears phantom entries and refreshes real ones.

1. Run Command Prompt as administrator.
2. Stop the services: net stop wuauserv, net stop bits, net stop cryptSvc.
3. Rename the caches: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Restart the services, then revisit the Optional updates list — the entries will repopulate with fresh metadata.

### Fix 5: Hide optional packages that will never install

Some optional packages are simply wrong for your hardware and will never install. Hiding them is the supported resolution — it stops the retry noise without affecting anything else, and you can unhide later if a corrected package appears.

1. Download wushowhide.diagcab from [Microsoft Support](https://support.microsoft.com/en-us/windows).
2. Run it, choose Hide updates, and tick the persistently failing optional package.
3. Confirm it vanishes from the Optional updates list.
4. Re-check after the next Windows feature update, which may bring a valid newer package.

### Fix 6: Free staging space and install drivers directly

Optional packages still stage hundreds of megabytes before installing. On drives hovering near full, the staging silently fails and the optional entry just sits there. Freeing space is the unglamorous fix that resolves a surprising share of these cases.

1. Check free space: Settings > System > Storage — keep at least 10–15 GB free.
2. Run Disk Cleanup as administrator and remove “Windows Update Cleanup” and temporary files.
3. If a specific driver is the goal, install it from the manufacturer’s site directly.
4. Retry the optional install once space is freed.

### Fix 7: Fetch needed optional drivers from the Update Catalog directly

When the Optional updates list will not cooperate but you genuinely need one of its drivers — say, for a device with no working driver — the Microsoft Update Catalog hosts the same driver packages as standalone downloads. Searching the driver name plus “windows 11” usually surfaces the exact package Windows Update was failing to deliver. This bypasses the optional-queue machinery entirely, and the [step-by-step optional-updates walkthrough](/articles/how-to-fix-optional-updates-not-installing-windows-11-step-by-step/) shows where this fits in the ordered troubleshooting sequence.

1. In Device Manager, identify the device and its hardware ID (Properties > Details > Hardware Ids).
2. Search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for the device or driver name.
3. Download the matching x64 driver package.
4. Install it via Device Manager > Update driver > Browse my computer, pointing at the downloaded files.
5. Confirm the device works, then hide the stale optional offer with wushowhide.

## Closing

Optional updates that will not install are usually being blocked by something upstream — a pause, a metered flag, a stuck service, or a version conflict — rather than broken in themselves. Clear the upstream blockage, retry the specific optional package, and treat any that persistently fail as candidates for hiding rather than forcing.
