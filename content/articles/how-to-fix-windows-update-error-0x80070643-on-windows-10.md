---
title: "Fix Windows Update Error 0x80070643 on Windows 10: Step-by-Step"
slug: how-to-fix-windows-update-error-0x80070643-on-windows-10
date: 2026-09-22
categories: ["windows-update"]
tags: ["windows update", "0x80070643", ".net framework", "defender", "windows 11"]
description: "Windows 10 error 0x80070643 signals a fatal error during installation. Identify which update failed and apply the right repair."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070643-on-windows-10.webp"
faqs:
  - q: "Why does 0x80070643 happen mostly with .NET updates?"
    a: "Because .NET cumulative updates install through the Windows Installer engine on top of the existing .NET runtime. If that runtime has corrupted registrations or damaged assemblies — common after interrupted updates or aggressive cleaners — the installer detects the broken baseline and aborts with ERROR_INSTALL_FAILURE. Repairing .NET with Microsoft's repair tool fixes the baseline so the update can proceed."
  - q: "Is error 0x80070643 dangerous for my system?"
    a: "Not by itself. It means an update failed to install — your Windows 10 system keeps running on the previous, working state. The risk is indirect: the longer the failed update stays uninstalled, the longer you miss its security fixes. Repair the failing component promptly, but there is no emergency beyond staying current."
  - q: "Can I just hide the failing update?"
    a: "You can, but treat hiding as a last resort, not a fix — especially for .NET and Defender updates, which carry security content. Hiding is reasonable only as a temporary measure while you arrange the real repair, or when Microsoft has acknowledged a bad update and you are waiting for the revised package."
  - q: "Why does the .NET update fail but everything else installs?"
    a: "Because only the .NET update exercises the damaged .NET runtime. Other updates touch different components and install fine, which is actually useful diagnostically: selective failure points squarely at the .NET installation rather than at Windows Update itself. Run the .NET Repair Tool before touching any servicing-wide settings."
---
On Windows 10, 0x80070643 means an update's installation died with a fatal error partway through. The usual offenders are the .NET Framework rollups and Defender intelligence updates, both of which install through the Windows Installer engine — and both of which fail in well-documented, fixable ways. The code is generic, so the update's name in your history is the real diagnostic.

Treat this as a per-update problem first and a system problem second: fix the specific failing component, and the error typically vanishes without touching anything else. Only escalate to servicing-wide repairs if multiple unrelated updates fail the same way.

The [Windows 11 guide](/articles/how-to-fix-windows-update-error-0x80070643-on-windows-11/) is the Windows 11 edition of this guide, and the [companion guide for 0x8024200d](/articles/how-to-fix-windows-update-error-0x8024200d-on-windows-10/) covers installer hangs — the close cousin of this error. Identify, then repair.

## Why this happens

- **The .NET Framework installation is damaged:** 0x80070643 is the signature failure of .NET cumulative updates installing over a corrupted .NET runtime. The installer detects the broken baseline and aborts rather than layering a patch on damage.
- **A Defender definition update collided with a scan:** Defender intelligence updates fail with this code when a full scan is running, definitions are mid-download, or a third-party AV conflicts with Defender's update path.
- **A previous install left the engine in a bad state:** An interrupted MSI installation can leave the Windows Installer service wedged, so the next update that uses the engine fails immediately with a fatal error.
- **Permissions on installer folders are wrong:** If SYSTEM or TrustedInstaller lost write access to servicing folders — often after aggressive permission-tweaking tools — installers cannot stage their files and die fatally.
- **The update cache holds a corrupted package:** A damaged .msu or payload in SoftwareDistribution fails at apply time rather than download time, producing 0x80070643 instead of a download error.
- **Third-party antivirus blocks the installer:** Security suites that intercept MSI operations can kill an update's installer mid-flight, which Windows reports as a fatal installation error.
- **Pending reboots block new installations:** Some updates refuse to install while another operation awaits a restart; the installer exits fatally instead of queuing politely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the exact failing update

Check both the update history and the reliability monitor; the failing package is usually named plainly.

1. Open Settings > Update & Security > Windows Update > Update history and find the entry marked Failed with 0x80070643.
2. Note whether it is a .NET Framework update, a Defender intelligence update, or something else.
3. Press Win + R, type `perfmon /rel`, and check Reliability Monitor for the matching critical event and its details.
4. Write down the KB number — you will need it for the manual-install fallback.
5. Proceed to the fix matching your culprit below.

### Fix 2: Repair the .NET Framework installation

This is the highest-yield fix for the .NET flavor of 0x80070643 and takes about ten minutes.

1. Download the Microsoft .NET Framework Repair Tool from the [Windows support hub](https://support.microsoft.com/en-us/windows) guidance pages.
2. Run it, accept the license, and let it diagnose the installed .NET versions.
3. Apply all recommended repairs and restart when prompted.
4. Return to Settings > Update & Security > Windows Update and retry — install only the .NET update first to confirm.
5. If it still fails, uninstall the newest .NET update in Update history, restart, and retry once more.

### Fix 3: Update Defender definitions manually

This also immediately restores protection currency, which matters more than the error code itself.

1. Open Windows Security > Virus & threat protection > Protection updates and click Check for updates.
2. If that fails, open Command Prompt as administrator.
3. Run `"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -SignatureUpdate`.
4. Wait for it to report a successful update, then restart.
5. Verify in Protection updates that the intelligence version is current.

### Fix 4: Clear pending operations and the update cache

Reboot first — a surprising number of pending operations resolve themselves across a restart and never needed manual clearing.

1. Restart the laptop (Start > Power > Restart) to flush simple pending operations.
2. Open Command Prompt as administrator.
3. Run `net stop wuauserv` and `net stop bits`.
4. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`, then restart both services.
5. Retry the failed update from Settings > Update & Security > Windows Update.

### Fix 5: Install the update in a clean boot

If the update succeeds here, the permanent fix is an exclusion in the interfering program — not perpetual clean-booting.

1. Press Win + R, type `msconfig`, and press Enter.
2. On the Services tab, check Hide all Microsoft services, then Disable all.
3. Disable all startup items in Task Manager's Startup tab.
4. Restart and install the update from Settings > Update & Security > Windows Update.
5. Restore normal startup with `msconfig` afterward and restart again.

### Fix 6: Install the failing update manually

Use the KB number you noted in Fix 1 to get precisely the right package — close is not good enough with servicing updates.

1. Search your KB number on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Download the package matching your architecture and OS version.
3. Close other programs, then double-click the .msu to install.
4. Restart when prompted.
5. Run a normal update check to confirm the failure is cleared from history.

### Fix 7: Re-register the Windows Installer engine

On Windows 10, the Windows Installer service handles .NET rollups and many cumulative updates. When its registration corrupts — after a crashed install or a bad uninstall — the engine fails every MSI operation with the same fatal error. The unregister/re-register pair restores it in under a minute.

1. Open Command Prompt as administrator.
2. Run `msiexec /unregister` and wait for the silent return.
3. Run `msiexec /regserver` to rebuild the registration.
4. Restart the laptop so the fresh registration takes effect.
5. Retry the failed update from Settings > Update & Security > Windows Update.

## Closing

On Windows 10, 0x80070643 is rarely the system crying for help — it is one component's installer failing and taking the error code with it. Fix the .NET runtime, refresh Defender definitions by hand, or clear the servicing debris, and the failure clears. Work per-update rather than per-system and you will spend minutes on this, not hours.
