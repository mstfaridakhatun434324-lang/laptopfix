---
title: "Fix PC Game Pass Installs Failing on Your ARM Laptop"
slug: game-pass-arm-laptop-install-failed
date: 2026-10-23
categories: ["ai-pc"]
tags: ["game pass", "xbox app", "arm laptop", "install failed", "gaming services", "troubleshooting"]
description: "Fix PC Game Pass install failures on ARM laptops: repair Gaming Services and the Xbox app, check drive requirements, and clear the store cache step by step."
thumbnail: "/images/thumbs/game-pass-arm-laptop-install-failed.webp"
faqs:
  - q: "Why does PC Game Pass fail to install games on my ARM laptop?"
    a: "The usual culprits are a corrupted Gaming Services package, a damaged Xbox app installation, or a Microsoft Store cache problem. On ARM machines the Gaming Services component also runs through the x64 emulation layer, which makes it more sensitive to corruption. Repairing Gaming Services and resetting the Xbox app fixes most cases."
  - q: "Does Game Pass work on Copilot+ PCs and Windows on ARM?"
    a: "Yes, the Xbox app and PC Game Pass run on Windows 11 on ARM, with x64 emulation handling the parts that have no native ARM64 build. Game downloads, cloud saves, and achievements all work normally once the install pipeline is healthy. Individual games may vary, but the Game Pass service itself is fully supported."
  - q: "Can I install Game Pass games to an external drive or SD card?"
    a: "No. The Xbox app only installs games to internal drives formatted as NTFS. External USB drives, SD cards, and drives formatted as exFAT or FAT32 are rejected by the installer. Point the install location at your internal NVMe SSD in the Xbox app settings before downloading."
  - q: "What does error 0x80070005 mean when installing a Game Pass game?"
    a: "That is an access-denied error, and it usually points to broken permissions on the WindowsApps folder or a corrupted Gaming Services install. Running the Gaming Services repair, resetting the Xbox app, and making sure you are signed in with the account that owns the Game Pass subscription resolves it in most cases."
---

You picked a game in the Xbox app, hit Install, and instead of a download bar you got an error — or the progress froze at 0% and the game quietly vanished from the queue. On your Snapdragon-powered laptop this feels like an ARM problem, and in a way it is: the install pipeline involves more moving parts than a normal download, and each one can break.

On Copilot+ PCs the Xbox app itself is fine, but Gaming Services — the system component that actually stages and verifies Game Pass downloads — still relies on x64 code running through emulation. That makes it unusually fragile: one bad update or one corrupted cache file and the whole pipeline stalls, even though the rest of Windows runs perfectly.

This guide walks you through six repairs in technician order: quick service and app repairs first, then the drive and system checks, then a full Gaming Services reinstall. Do them in sequence and test an install after each step.

## Why this happens

- **Corrupted Gaming Services package:** The background service that manages Game Pass installs is the single most common failure point — a bad update or interrupted install leaves it half-registered and every new download fails.
- **Damaged Xbox app installation:** The Xbox app is a Store app like any other, and its local state can corrupt. When its sign-in tokens or download queue go stale, installs fail even though the app looks normal.
- **Stale Microsoft Store cache:** The Xbox app shares download infrastructure with the Store. A corrupted Store cache blocks licensing checks and aborts installs with vague errors.
- **Install drive rejected by the app:** Game Pass games must go to an internal NTFS drive. An external drive, an SD card, or an exFAT-formatted volume is refused, sometimes with no clear explanation.
- **Windows build out of date:** Gaming Services updates ship through Windows Update. An ARM laptop that has missed updates can run a Gaming Services version too old for the current Xbox app.
- **Account or subscription mismatch:** If you are signed into the Xbox app with a different account than the one holding the Game Pass subscription, the licensing check fails and the install is blocked.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Repair Gaming Services in Settings

Gaming Services is a separate system component, and Windows gives you a one-click repair for it. This takes under a minute and is the fix more often than anything else — start here before touching the app or the store.

1. Open **Settings > Apps > Installed apps** and search for **Gaming Services**.
2. Click the **...** menu next to it and choose **Advanced options**.
3. Click **Repair** and wait for the checkmark, then try your game install again.
4. If it still fails, return to the same page and click **Reset** — this clears its local state without removing the component.
5. Restart the laptop after the reset, then open the Xbox app and retry the download. Do not skip the restart: the service re-registers itself during boot.

### Fix 2: Reset the Xbox app and clear the Store cache

If Gaming Services is healthy, the problem is usually the Xbox app's own state or the shared Store cache. Resetting both clears stale sign-in tokens and broken download queues — the same app-state hygiene that helps when [Copilot in OneNote stops responding](/articles/onenote-copilot-not-working/) after an update.

1. In **Settings > Apps > Installed apps**, find **Xbox**, open **Advanced options**, and click **Repair** first, then **Reset** if the repair changes nothing.
2. Press **Win + R**, type **wsreset.exe**, and press Enter — a blank command window opens and closes on its own, clearing the Store cache.
3. Open the Xbox app again and sign out, then sign back in with the Microsoft account that owns the Game Pass subscription.
4. Check **Settings > General** in the Xbox app to confirm the right profile is active before installing.
5. Retry the install. If the download starts but stalls, let it sit for five minutes — the first chunks sometimes take a while to negotiate on a fresh cache.

### Fix 3: Point installs at a proper internal NTFS drive

The Xbox app silently refuses install locations it cannot use. External drives, SD cards, and non-NTFS volumes all get rejected, and the error message rarely says the drive is the problem — a frustrating trap that also affects people connecting storage through a [USB4 dock that misbehaves](/articles/usb4-dock-display-not-working-arm/).

1. In the Xbox app, open **Settings > General** and look at the **Game install options** / install drive dropdown.
2. Make sure the selected drive is an **internal** drive — the install will not proceed to USB-attached storage.
3. Verify the drive is formatted **NTFS**: open File Explorer, right-click the drive, choose **Properties**, and check the file system line.
4. If it shows exFAT or FAT32, back up its contents and reformat it as NTFS — Game Pass games cannot install to any other file system.
5. Confirm the drive has enough free space for the full game plus a few gigabytes of headroom, then start the install again from the corrected location.

### Fix 4: Update Windows and restart cleanly

Gaming Services is serviced through Windows Update, and the Xbox app expects a minimum build. ARM laptops that sit on an old build — or that downloaded an update but never restarted — run mismatched components that fail installs in odd ways.

1. Open **Settings > Windows Update** and click **Check for updates**; install everything offered, including optional driver updates.
2. Restart when prompted — do not just close the lid. A full restart lets pending Gaming Services updates register.
3. After rebooting, open the Xbox app and check for app updates in the Microsoft Store library as well.
4. If an update was pending for a long time, run Fix 1 (Gaming Services repair) once more after the update lands.
5. Retry the install. For the general process of keeping the update stack healthy, [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) document the supported troubleshooting path.

### Fix 5: Reinstall Gaming Services with PowerShell

When the Settings repair does nothing, the component is usually too damaged for an in-place repair. Removing it completely and letting the Store pull a fresh copy clears corruption that survives resets — the heavy hammer, but a reliable one.

1. Right-click Start and open **Windows Terminal (Admin)** or **PowerShell as administrator**.
2. Run `Get-AppxPackage Microsoft.GamingServices -AllUsers | Remove-AppxPackage -AllUsers` to remove the component. (Type it exactly; a typo here removes the wrong package.)
3. Restart the laptop.
4. Open the Microsoft Store, search for **Gaming Services**, and install it fresh — or simply launch the Xbox app, which prompts you to install the missing component.
5. Once installed, open the Xbox app, sign in, and attempt the game download again from scratch.

### Fix 6: Verify the account, region, and subscription

If every repair above checks out, the block is licensing, not software. The install pipeline verifies three things before writing a single byte: the signed-in account, the subscription attached to it, and the region match.

1. In the Xbox app, click your profile picture and confirm the email matches the account that pays for Game Pass — family sharing does not extend PC Game Pass installs to every profile.
2. Visit account.microsoft.com in a browser and confirm the Game Pass subscription is active and not expired or past-due.
3. Check **Settings > Time & language > Language & region** in Windows — a region mismatch between the account and the PC can block Store licensing.
4. If you recently changed region or payment method, sign out of the Xbox app and Store, restart, and sign back in to refresh the license tokens.
5. As a last resort, create a fresh local Windows user, sign into the Xbox app there, and test — if installs work on the new profile, your main profile's Store identity is corrupted and a profile rebuild is the clean fix.

## Closing

Game Pass install failures on ARM laptops are almost never about the games or the hardware — they are about Gaming Services, the Xbox app's state, or the install drive. Repair Gaming Services first, reset the app and Store cache second, and confirm the target drive is internal NTFS before anything drastic. When the pipeline is healthy, installs behave exactly like they do on any other Windows 11 PC. If a different subsystem starts acting up instead — for example an [NPU stuck in the wrong power state](/articles/npu-power-state-stuck-fix/) — the same diagnose-first discipline applies.
