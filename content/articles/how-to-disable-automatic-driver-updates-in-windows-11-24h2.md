---
title: "How to Disable Automatic Driver Updates on Windows 11 24H2"
slug: how-to-disable-automatic-driver-updates-in-windows-11-24h2
date: 2026-09-29
categories: ["drivers"]
tags: ["driver updates", "windows update", "windows 11 24h2", "group policy"]
description: "Disable automatic driver updates on Windows 11 24H2: block driver delivery via Windows Update settings, Group Policy, and registry — without stopping security updates."
thumbnail: "/images/thumbs/how-to-disable-automatic-driver-updates-in-windows-11-24h2.webp"
faqs:
  - q: "Will disabling driver updates stop Windows security updates?"
    a: "No, when done correctly. The methods in this guide target only the driver-delivery channel of Windows Update. Security patches, cumulative updates, and feature updates continue normally. You are telling Windows to stop swapping your drivers, not to stop patching the operating system."
  - q: "Why would I want to stop automatic driver updates?"
    a: "Because a working driver is worth more than a newer one. Automatic updates routinely replace stable vendor-tuned drivers — graphics, Wi-Fi, audio — with generic or mismatched versions that break things that worked yesterday. Users with a known-good driver set disable the automatic channel and update drivers manually on their own schedule."
  - q: "Is it safe to leave driver updates disabled permanently?"
    a: "It is a trade-off. You gain stability and lose automatic fixes for driver-level security issues. The balanced approach is to review driver updates manually every few months from your laptop vendor's support page, installing only what you need. For most home users, that cadence is perfectly safe."
  - q: "Do these methods work on Windows 11 Home?"
    a: "The Settings and registry methods work on Home. The Group Policy method needs Pro, Education, or Enterprise — Home has no Local Group Policy Editor. The registry method achieves the same result on Home, so no edition is left without an option."
---

Windows 11 24H2 is enthusiastic about updating your drivers — so enthusiastic that it will replace a perfectly working graphics or Wi-Fi driver with a different version while you are in the middle of using it, then act surprised when something breaks. For anyone who has found a stable driver set through careful manual installation, automatic driver updates are not a feature; they are a recurring threat to a working system.

The good news is that driver delivery is a separable channel inside Windows Update. You can shut off the driver pipeline while security patches and cumulative updates continue flowing normally. Windows offers several switches for this at different levels — a Settings toggle, a Group Policy, and a registry value — and they vary in strength and in which Windows editions support them.

This guide covers all three methods in order of simplicity, explains what each one actually blocks, and shows how to verify the block is working and how to update drivers manually afterward. Nothing here stops security updates; that boundary is respected throughout.

## Why this happens

- **Windows Update bundles drivers with OS updates:** On 24H2, driver updates arrive through the same Windows Update channel as patches, and declining them individually every time is impractical.
- **Generic drivers replace vendor-tuned ones:** Microsoft's driver catalog often carries generic versions that lack the laptop vendor's customizations for power, thermals, and hybrid graphics.
- **Background installs interrupt work:** Driver installations can briefly disrupt displays, audio, or networking mid-session, and they sometimes demand reboots at bad moments.
- **Version regressions break working hardware:** A newer driver is not a better driver. Regressions in Wi-Fi stability, GPU performance, and audio quality after automatic updates are well documented.
- **No per-driver approval in the consumer UI:** Windows 11 Home and Pro offer no built-in way to approve drivers one by one — the choice is all-or-nothing at the UI level.
- **Enterprise and stability requirements:** Managed and mission-critical machines need driver changes on a tested schedule, not on Microsoft's release cadence.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the Settings toggle (simplest, all editions)

Windows includes a device installation setting that stops automatic driver downloads. It is the gentlest method and the right starting point.

1. Search for Change device installation settings and open it.
1. Select No, let me choose what to do, then Never install driver software from Windows Update.
1. Click Save Changes. This reduces automatic driver installs, though determined updates can occasionally bypass it — verify with the methods below if a driver still sneaks through.

### Fix 2: Block driver updates with Group Policy (Pro and higher)

The Group Policy setting is the authoritative switch on Pro, Education, and Enterprise editions. It is what IT departments use.

1. Press Win+R, type gpedit.msc, and press Enter.
1. Navigate to Computer Configuration, then Administrative Templates, then Windows Components, then Windows Update, then Manage updates offered from Windows Update.
1. Open Do not include drivers with Windows Updates, set it to Enabled, and click OK.
1. Run gpupdate /force in an elevated Command Prompt, or restart, to apply it.

### Fix 3: Set the registry value (works on Home)

The registry method achieves the Group Policy result on editions without gpedit, including Windows 11 Home.

1. Press Win+R, type regedit, and press Enter.
1. Navigate to HKEY_LOCAL_MACHINE, then SOFTWARE, Policies, Microsoft, Windows, WindowsUpdate.
1. Create a DWORD value named ExcludeWUDriversInQualityUpdate and set it to 1.
1. Restart the laptop. This is the same underlying switch the Group Policy flips.

### Fix 4: Verify the block is actually working

Trust but verify. A quick check confirms Windows honors the setting before the next Patch Tuesday tests it for you.

1. Open Settings, then Windows Update, and check optional updates — driver offerings should stop appearing.
1. Note your current driver versions via [checking driver versions](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/) so you can confirm nothing changes after the next update cycle.
1. After the next cumulative update, recheck one driver version to confirm it held.

### Fix 5: Update drivers manually on your own schedule

With the automatic channel off, you become the update mechanism. That is the point — do it deliberately.

1. Every few months, check your laptop vendor's support page for driver updates for your exact model.
1. Prioritize graphics, Wi-Fi, chipset, and BIOS; skip the rest unless you have a symptom.
1. Follow the [manual driver update process](/articles/how-to-update-drivers-on-windows-11-laptop/) for each one, installing from the vendor's packages.

### Fix 6: Re-enable selectively if needed

The block is reversible. If a future problem is fixed by a newer driver, you can temporarily reopen the channel.

1. Reverse the setting you changed — set the policy to Not Configured or the registry value to 0.
1. Run Windows Update to pull the driver you want, then reapply the block.
1. Alternatively, install just that driver manually from the vendor and leave the block in place. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the Windows Update settings if you need a refresher on the surrounding options.

### Fix 7: Block individual drivers with the show-or-hide updates tool

Sometimes you want to block one bad driver while allowing others through, and the all-or-nothing switches are too blunt for that. Microsoft's show-or-hide updates troubleshooter lets you hide specific driver updates so Windows Update skips them while continuing everything else. It is the surgical option for the one driver that keeps breaking your system.

1. Download the show-or-hide updates troubleshooter package from Microsoft's support site.
1. Run it, choose Hide updates, and select the specific driver version causing trouble.
1. Confirm on the next update cycle that the hidden driver no longer appears while other updates proceed.

## Closing

Disabling automatic driver updates on 24H2 is about choosing stability on your own terms: security patches keep flowing, but your working graphics, Wi-Fi, and audio drivers stay exactly as you left them. Pick the method that matches your Windows edition, verify it held through an update cycle, and adopt a calm manual review cadence. The driver that works is the driver you keep.
