---
title: "How to Manually Install Windows Updates on Windows 10"
slug: how-to-manually-install-windows-update-on-windows-10
date: 2026-09-26
categories: ["windows-update"]
tags: ["manual install", "windows 10", "update catalog", "msu", "offline"]
description: "Skip the broken update pipeline: download any Windows 10 update manually from the Catalog and install it yourself, step by step."
thumbnail: "/images/thumbs/how-to-manually-install-windows-update-on-windows-10.webp"
faqs:
  - q: "Where do I safely download Windows 10 updates manually?"
    a: "Only from the official Microsoft Update Catalog at catalog.update.microsoft.com. Never download .msu files from third-party sites, forums, or file hosts — tampered update packages are a classic malware vector. The Catalog is Microsoft's own repository and every package is signed; Windows verifies the signature at install."
  - q: "How do I know which update file matches my system?"
    a: "Check Settings → System → About for your architecture (almost always x64 now) and your Windows 10 version/build (e.g., 22H2, build 19045). On the Catalog, pick the entry matching your KB number, architecture (x64), and Windows 10 version. Installing the wrong architecture's package just fails harmlessly; the wrong version may report 'not applicable.'"
  - q: "Do manually installed updates show in Update history?"
    a: "Yes. Once installed, a manual .msu appears in Settings → Update & Security → Windows Update → View update history like any other update. Windows tracks it identically — future cumulative updates build on it normally. Manual installation is a first-class path, not a hack."
  - q: "Should I manually install every update instead of using Windows Update?"
    a: "No — manual installation is a fallback for specific stuck or failing updates, not a replacement routine. Windows Update handles dependencies, ordering, and superseded updates automatically; doing everything by hand is error-prone tedium. Use the Catalog surgically: for the one KB that won't come down the normal pipe."
---

There's a special satisfaction in bypassing a broken pipeline entirely. When Windows 10's updater refuses to download or install a specific update — stuck at 0%, failing with the same code for the third time — you don't have to keep fighting it. Microsoft publishes every update as a standalone installer on the Update Catalog, and installing it by hand takes five minutes. Same bits, same signature, zero downloader drama.

Manual installation is also a diagnostic tool: if the .msu installs cleanly, your problem was the delivery pipeline (now bypassed); if it fails identically, the problem is systemic (servicing store, drivers, disk). Either way you learn something. This guide covers finding the right package, installing it correctly, and handling the edge cases. For the broader repair context, see [resetting Windows Update components on Windows 10](/articles/how-to-reset-windows-update-components-on-windows-10/).

You'll need your KB number (from Update history) and your build number (Settings → System → About). That's the entire prerequisite list.

## Why this happens

- **Pipeline-specific failures**: Corrupt cache, wedged BITS, or orchestrator loops that do not affect standalone installers. If the .msu installs cleanly, the pipeline was the problem — now bypassed.
- **Metered-connection blocks**: Manual .msu installs ignore metered flags entirely. Download on any unmetered connection and carry the file over on USB.
- **WSUS/targeting issues**: Managed machines not receiving a needed update can install it directly, with IT approval. On unmanaged machines this is simply the fastest path to a specific KB.
- **Single-KB urgency**: A security patch you need today, not after the pipeline gets fixed. Security updates are the highest-value use of the manual path.
- **Diagnostic isolation**: Separating bad package from bad pipeline in one test. Identical failure from the .msu means the cause is systemic — investigate the store and drivers.
- **Offline/air-gapped installs**: Machines without direct update access can be patched via USB. Install in dependency order: servicing stack first, then cumulative.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the exact KB and your build

Precision here prevents 'not applicable' errors later. Precision here prevents not applicable errors later.

1. Settings → Update & Security → Windows Update → **View update history** → note the failing KB number.
2. Settings → System → About → note Edition, Version (e.g., 22H2), OS build, and System type (x64).
3. Write both down — you'll match all three on the Catalog (KB + version + architecture).
4. If you don't have a specific KB (just 'updates won't install'), start with the latest cumulative update for your version.
5. If Update history shows no KB at all, use the Settings, System, About build number to pick the latest cumulative for your version.

### Fix 2: Find and download the package on the Update Catalog

The only safe source. Bookmark it. The only safe source. Bookmark it.

1. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and search your KB number.
2. In the results, find the row matching **Windows 10 Version 22H2** (your version), **x64**.
3. Click **Download**, then click the file link in the popup to save the .msu.
4. Verify the file size looks sane (cumulative updates are hundreds of MB — a 2 KB file means the download failed).
5. Use the Catalog's advanced search filters — KB number alone can return dozens of architecture variants.

### Fix 3: Install the .msu correctly

The installation itself is simple; the preparation is what matters. The installation itself is simple; the preparation is what matters.

1. Close other applications; plug in the charger.
2. Temporarily disable third-party antivirus real-time protection (re-enable right after).
3. Double-click the .msu (or right-click → run as administrator via an elevated prompt with `wusa path\file.msu`).
4. Follow the installer; reboot when prompted — don't postpone the reboot.
5. If the installer seems to hang at initializing, give it 15 minutes — large .msu files verify slowly on older disks.

### Fix 4: Verify the installation

Confirm it actually landed before moving on. Confirm it actually landed before moving on.

1. After reboot: Settings → Update & Security → Windows Update → **View update history** → the KB should be listed as successful.
2. Check Settings → System → About → OS build incremented as expected.
3. Run **Check for updates** — it should now offer only subsequent updates, not the one you just installed.
4. If the KB still shows as needed, the install didn't take — note any new error and continue to Fix 5.
5. Also confirm in the registry under HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\Packages if you want belt-and-suspenders proof.

### Fix 5: Handle 'not applicable' and failure cases

The two common manual-install errors, decoded. The two common manual-install errors, decoded.

1. 'Not applicable to your computer' → wrong KB variant: recheck version/architecture in Fix 1, or the update is already superseded (check history).
2. Install fails with an error code → the problem is systemic: run DISM/SFC, check disk space, update drivers.
3. Servicing stack prerequisite missing → install the latest SSU for your build from the Catalog first, then retry.
4. Persistent failure across manual attempts = escalate with the exact code and CBS logs.
5. Document the exact error text — manual-install failures have distinct codes that map to distinct causes.

### Fix 6: Install driver updates manually the same way

The Catalog technique works for drivers too — useful when Windows Update withholds one. The Catalog technique works for drivers too — useful when Windows Update withholds one.

1. Search the Catalog for the driver KB or hardware ID.
2. Prefer the laptop manufacturer's support site for drivers when possible (better-tested bundles).
3. Install via the .msu/.cab as appropriate; reboot.
4. Verify in Device Manager → device → Driver → version/date updated.
5. For network drivers especially, manual installation rescues machines whose updater cannot even reach the internet.

### Fix 7: Use manual installs for offline patching

The air-gap pattern for machines without update access. The air-gap pattern for machines without update access.

1. On an internet-connected PC, download needed KBs from the Catalog (cumulative + servicing stack + critical).
2. Transfer via USB to the target machine.
3. Install in dependency order: servicing stack first, then cumulative, then others; reboot between.
4. Verify via Update history on the target. This is also how you patch a fresh install quickly — see [update errors after a clean install](/articles/how-do-i-fix-windows-update-error-after-clean-install/).
5. Label the USB with KB numbers and dates — future-you will not remember which stick holds which patch.

## Closing

Manual installation is Windows Update's pressure valve: same Microsoft-signed packages, installed on your terms, immune to pipeline corruption and metered flags. Learn the Catalog workflow once — match KB, version, and architecture — and no single stuck update can ever hold your patching hostage again. Related guides: [resetting Windows Update components on Windows 10](/articles/how-to-reset-windows-update-components-on-windows-10/) and [update errors after a clean install](/articles/how-do-i-fix-windows-update-error-after-clean-install/).
