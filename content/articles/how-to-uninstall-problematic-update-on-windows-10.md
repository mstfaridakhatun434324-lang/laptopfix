---
title: "How to Uninstall a Problematic Update on Windows 10"
slug: how-to-uninstall-problematic-update-on-windows-10
date: 2026-10-13
categories: ["windows-update"]
tags: ["uninstall update", "problematic update", "windows 10", "rollback"]
description: "A Windows 10 update broke something? Here's how to uninstall it safely — via Settings, Control Panel, or recovery — and stop it reinstalling."
thumbnail: "/images/thumbs/how-to-uninstall-problematic-update-on-windows-10.webp"
faqs:
  - q: "Is it safe to uninstall a Windows 10 update?"
    a: "Yes, for quality updates — uninstalling one simply removes that month's patches and returns those components to their previous state. Your files and apps are untouched. The trade-off is losing that update's security fixes, so treat uninstalling as a temporary measure while you wait for a revised patch, not a permanent solution. Feature updates can also be rolled back within ten days."
  - q: "How do I stop the bad update from reinstalling itself?"
    a: "After uninstalling, pause updates for one to two weeks in Settings > Update & Security > Windows Update > Pause updates. For longer-term blocking of a specific KB, Microsoft offers the Show or Hide Updates troubleshooter, which lets you hide that update so Windows Update skips it. Pausing alone is enough in most cases since Microsoft usually ships a fixed version quickly."
  - q: "What if the Uninstall button is grayed out?"
    a: "Some updates can't be uninstalled because they're required by newer updates already installed on top of them, or because the servicing stack marks them permanent. In that case, uninstall the newer updates first (newest to oldest) until the target becomes removable. If it's a feature update past the ten-day window, rollback is no longer offered and you'd need a clean install to go back."
  - q: "Can I uninstall an update if Windows won't boot?"
    a: "Yes. Boot into the Windows Recovery Environment by interrupting startup three times or using installation media, then go to Troubleshoot > Advanced options > Uninstall Updates. You can remove the latest quality update or the latest feature update from there. This is the rescue path when a bad update leaves the laptop unbootable."
---

It installed overnight, and now something's broken — Wi-Fi drops, an app crashes, the laptop crawls. When the timeline points squarely at a Windows 10 update, the fastest relief is to remove that update and confirm the problem disappears. Uninstalling a quality update is safe, quick, and reversible: if removing it doesn't help, you can reinstall it just as easily.

The trick is doing it properly: identifying the right KB, removing it through the right interface, and then preventing Windows from helpfully reinstalling the same broken patch tonight. If the update broke things so badly the laptop won't start, skip ahead to the recovery-environment method. And if you'd rather diagnose first, our [Windows 10 troubleshooter guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-windows-10/) helps confirm the update is truly the culprit.

## Why this happens

- **A buggy patch shipped** — It happens: a quality update with a regression that breaks specific hardware or software.
- **A driver rode along** — The "problematic update" is often a driver Windows Update bundled in, not the KB itself.
- **Software incompatibility** — Older applications can break when system components change underneath them.
- **You need to confirm the cause** — Uninstalling is also a diagnostic: if the problem vanishes, you've found it.
- **The update won't reinstall cleanly** — Sometimes removing and reinstalling the same update fixes a bad first install.
- **You're buying time** — Removing a bad patch while waiting for Microsoft's revised version is legitimate triage.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the exact update to remove

Don't guess — match the problem's start date to the install date.

1. Go to Settings > Update & Security > Windows Update > **View update history**.
2. Note which quality update installed just before the problem started — write down its KB number and date.
3. Check the **Driver Updates** section too; a driver delivered alongside the KB is a frequent real culprit.
4. Search the KB number online to see if others report the same issue — confirmation you're not chasing a coincidence.
5. If the timeline doesn't implicate any update, stop here and troubleshoot the symptom directly instead.

### Fix 2: Uninstall via Settings

The simplest path for recent quality updates.

1. On the View update history page, click **Uninstall updates** at the top.
2. In the installed-updates list, click the **Installed On** column to sort newest first.
3. Select the suspect KB, click **Uninstall**, and confirm.
4. Reboot when prompted and test whether the problem is gone.
5. If it is, pause updates for 7–14 days (Settings > Windows Update > Pause updates) so the same patch doesn't return tonight.
6. Take a screenshot of the installed-updates list before uninstalling — if the problem turns out to be unrelated, the screenshot makes reinstalling the exact KB trivial.

### Fix 3: Uninstall via Control Panel

The classic interface — same list, sometimes more reliable when Settings misbehaves.

1. Open Control Panel > **Programs** > **Programs and Features**.
2. Click **View installed updates** in the left sidebar.
3. Sort by **Installed On** to find the most recent updates at a glance.
4. Right-click the target update and choose **Uninstall**, then reboot.
5. Verify the fix held for a full day of normal use before declaring victory.

### Fix 4: Uninstall from the Recovery Environment

For updates that broke booting — the rescue path when Windows won't start.

1. Interrupt the boot process three times in a row (hold power during the Windows logo) to reach Automatic Repair, then **Advanced options**.
2. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
3. Choose **Uninstall the latest quality update** (or feature update, if that's what broke it).
4. Let the rollback complete and reboot normally.
5. Once you're back in Windows, immediately pause updates so the bad patch doesn't reinstall before you've stabilized things. Microsoft documents this recovery flow on their [Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 5: Block the update from reinstalling

Removing the update is half the job — stopping its return is the other half.

1. After uninstalling, go to Settings > Windows Update and **Pause updates for 7 days** (extendable to 35).
2. For a specific KB you want gone longer, use Microsoft's Show or Hide Updates troubleshooter to hide it from Windows Update.
3. If a driver was the real problem, roll it back in Device Manager and consider disabling driver updates via Group Policy or the registry.
4. Watch for the revised patch — Microsoft typically reissues fixed updates within weeks; unpause then.
5. If Windows is stuck in a loop of [undoing a failed install](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-windows-10/) rather than a bad-but-installed update, that needs the undoing-changes recovery path instead.
6. As a final sanity check, run Windows Update once more after unpausing and confirm the replacement patch installs cleanly — a smooth install closes the incident for good.

### Fix 6: Reinstall cleanly or wait for the fixed version

Uninstalling is triage, not a cure — close the loop properly.

1. Once you've confirmed the problem is gone, decide: was it a corrupt install or a genuinely bad patch?
2. If others report the same breakage, wait — install the re-released version when it appears in Windows Update.
3. If yours was an isolated bad install, try reinstalling the same KB manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
4. A clean reinstall of the same update succeeding proves the first attempt was just corrupted.
5. Keep a note of the KB number and date somewhere — if the issue ever recurs, you'll identify it in seconds next time.

## Closing

Uninstalling a problematic Windows 10 update is one of the safest troubleshooting moves you can make: it's quick, it doesn't touch your files, and it immediately answers the question "was the update the problem?" Identify the right KB, remove it through Settings or recovery, block its return while you wait for the fixed version, and you're back to a working laptop — with a clear conscience about the temporary security trade-off.
