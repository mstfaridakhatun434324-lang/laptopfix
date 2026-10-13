---
title: "How to Manually Install a Windows Update in Windows 11 24H2"
slug: how-to-manually-install-windows-update-in-windows-11-24h2
date: 2026-09-06
categories: ["windows-update"]
tags: ["manual update install", "microsoft update catalog", "windows 11 24h2", "msu installer"]
description: "Windows Update failing on 24H2? Learn how to manually download and install any update from the Microsoft Update Catalog, step by step."
thumbnail: "/images/thumbs/how-to-manually-install-windows-update-in-windows-11-24h2.webp"
faqs:
  - q: "Is manually installing Windows updates safe?"
    a: "Yes, when you download from the official Microsoft Update Catalog. The packages are byte-identical to what Windows Update delivers automatically — same signatures, same contents. Manual installation is a documented, supported procedure that Microsoft itself recommends as a fallback when automatic installation fails."
  - q: "How do I know which update file to download for my laptop?"
    a: "Match two things: the KB number from your Update history, and your system architecture — x64 for nearly all modern laptops, ARM64 for Snapdragon-based machines. Check Settings, then System, then About, then System type if you are unsure. Downloading the wrong architecture simply will not install, so the main risk is wasted time."
  - q: "Can manual installation fix updates that keep failing automatically?"
    a: "Very often, yes. Manual installation skips the download manager, the BITS transfer service, and the staging cache — the three phases where most automatic failures occur. If the failure is in the install phase itself, the manual installer will fail too, but it usually shows a clearer error message that points at the real problem."
  - q: "Do manually installed updates still appear in Update history?"
    a: "Yes. Once installed, the update registers in the system exactly like an automatically installed one and appears in Update history. Future cumulative updates will supersede it normally, and Windows Update continues working as before. There is no lasting difference between a manual and an automatic install of the same KB."
---

When Windows Update refuses to install something on 24H2 — failing downloads, cryptic errors, endless retries — the manual route cuts through all of it. You download the exact update package yourself from Microsoft's official catalog and run the installer by hand. It is the same update, the same code, delivered without the machinery that keeps breaking.

This is a skill worth learning once, because it applies to every future update failure. The whole process has four parts: identify the KB number, confirm your system type, download the right file, and install it. Total time is usually under fifteen minutes plus the install itself.

Manual installation used to be an IT-department procedure; today it is a mainstream troubleshooting skill, and this guide treats it that way. The Microsoft Update Catalog is a public library of every update Microsoft has shipped, each package signed and hash-verified, and installing from it is no more dangerous than letting Windows Update do the same download. The only real skill involved is matching the KB number and architecture correctly — everything else is double-clicking.

## Why this happens

- **Automatic download or staging failures** that manual installation bypasses entirely — the most common reason to go manual.
- **BITS or Delivery Optimization problems** breaking the transfer phase while the install phase would work fine.
- **Corrupted local update cache** that keeps poisoning automatic attempts but does not affect a hand-delivered package.
- **A specific update pulled from automatic distribution** but still available in the catalog for manual installation.
- **Metered or restricted networks** where the automatic client will not download but a manual download on another connection works.
- **Need for an out-of-band or preview update** that Windows Update is not offering your machine yet.
- **Troubleshooting requirement** — support technicians routinely ask for a manual install to isolate whether the failure is in delivery or installation.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find the exact KB number of the update

1. Open **Settings** > **Windows Update** > **Update history**.
2. Find the failed or missing update and note its **KB number** (for example, KB5037771).
3. If the update was never offered, search Microsoft's release notes for the current month's cumulative KB for Windows 11 24H2.
4. Write the KB number down — everything else keys off it. If you are chasing a monthly failure pattern, also read [fixing cumulative update failures](/articles/how-to-fix-monthly-cumulative-update-failed-on-windows-11/).

### Fix 2: Confirm your system architecture

1. Open **Settings** > **System** > **About**.
2. Look at **System type**: it will say 64-bit operating system, x64-based processor on nearly all Intel/AMD laptops, or ARM64 on Snapdragon machines.
3. Note your Windows build too (same page, under **Windows specifications**) — 24H2 packages differ from 23H2 ones.
4. Downloading the wrong architecture will not harm anything — the installer simply refuses — but checking first saves a wasted download.

### Fix 3: Download the package from the Microsoft Update Catalog

1. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for the KB number.
2. You will see multiple entries — pick the one matching your architecture (x64 or ARM64) and Windows 11 version.
3. Click **Download**, then click the file link in the popup window to save the `.msu` file.
4. Save it somewhere easy to find, like your Desktop or Downloads folder. Never download update packages from third-party sites — only the official catalog.

### Fix 4: Prepare the system before installing

1. Close all running programs and save your work.
2. Connect the charger — do not install updates on battery.
3. Temporarily disable third-party antivirus real-time protection (re-enable afterward).
4. If a previous automatic attempt is stuck, clear it first: stop the Windows Update service and empty `C:\Windows\SoftwareDistribution\Download`, as covered in [resolving stuck downloads](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/).

### Fix 5: Run the manual installer

1. Double-click the downloaded `.msu` file.
2. Click **Yes** when Windows Update Standalone Installer asks to proceed.
3. Wait — the installer verifies the package, checks applicability, and installs. This takes several minutes for cumulative updates.
4. Do not interrupt it. If it reports the update is "not applicable to your computer," you downloaded the wrong KB or architecture — recheck Fix 1 and Fix 2.

### Fix 6: Handle installer errors with the command line

1. If double-clicking fails silently, open an elevated Command Prompt.
2. Run:
   `wusa C:\path\to\update.msu /quiet /norestart`
   (replace with your actual file path; the quotes matter if the path has spaces)
3. Check `%windir%\Logs\CBS\CBS.log` for detailed error lines if it fails.
4. The `/quiet` switch suppresses dialogs and `/norestart` lets you control the reboot — useful when the GUI installer hangs. Microsoft's [Windows Update support page](https://support.microsoft.com/en-us/windows) documents additional standalone installer options.

### Fix 7: Verify the installation and re-enable automatic updates

1. Restart the laptop when the installer asks (or run your delayed restart now).
2. After booting, go to **Settings** > **Windows Update** > **Update history** and confirm the KB appears as successfully installed.
3. Re-enable your antivirus real-time protection.
4. Click **Check for updates** to confirm the automatic pipeline still works — the manual install should not have disturbed it, and any superseding updates will now be offered normally.

### Fix 8: Install a .cab package directly with DISM

Some updates (especially servicing stack and cumulative packages) are also distributed as `.cab` files, which DISM can install directly — useful when the `.msu` wrapper itself misbehaves.

1. If you have the `.msu`, extract the cab: run `expand -F:* C:\path\update.msu C:\temp\cab` in an elevated prompt.
2. Install it with:
   `DISM /Online /Add-Package /PackagePath:C:\temp\cab\update.cab`
3. Wait for the operation to complete, then restart when prompted.
4. Verify in **Update history**. DISM package installation bypasses the standalone installer entirely, succeeding in cases where even the manual `.msu` fails.

## Closing

Manual installation is the technician's bypass around broken update delivery: same official package, none of the fragile automation. Learn the KB-to-catalog routine once and every future "update won't install" becomes a fifteen-minute errand instead of an afternoon of retry loops. Keep the `.msu` files for a week in case you need to reference them, then delete them to reclaim the space. Keep this skill in your back pocket: the next time an update fails at 2 AM before a deadline, you will go straight to the catalog instead of watching a progress bar loop. Fifteen minutes, same official package, problem solved.
