---
title: "How to Perform a Clean Boot in Windows 11 on a Laptop"
slug: how-to-perform-clean-boot-windows-11-on-laptop
date: 2026-09-25
categories: ["windows-errors"]
tags: ["clean boot", "troubleshooting", "startup"]
description: "Suspect a program is crashing your laptop? Learn how to clean boot Windows 11 and hunt down the conflicting software."
thumbnail: "/images/thumbs/how-to-perform-clean-boot-windows-11-on-laptop.webp"
faqs:
  - q: "What is a clean boot, exactly?"
    a: "It's starting Windows with only Microsoft's own services and drivers, disabling all third-party startup programs and non-Microsoft services. If your problem disappears in a clean boot, a third-party program is the cause — you've cut the suspect list from hundreds to a manageable few."
  - q: "Is a clean boot the same as Safe Mode?"
    a: "No. Safe Mode loads a minimal Windows with generic drivers and a stripped-down interface. A clean boot loads your full, normal Windows — your drivers, your resolution, your desktop — just without third-party software. Clean boot is better for hunting software conflicts you can actually use the machine during."
  - q: "Will a clean boot delete anything?"
    a: "No. It only temporarily disables startup items and services — nothing is uninstalled or deleted. When you re-enable everything afterward, your laptop returns to exactly how it was. It's one of the safest diagnostic procedures in Windows."
  - q: "How do I undo a clean boot when I'm done?"
    a: "Reopen System Configuration (msconfig), select Normal startup on the General tab, re-enable your startup items in Task Manager, and restart. Your laptop boots normally with everything restored. Never leave a laptop in clean-boot state permanently — you'd be running without your antivirus and utilities."
---
When your laptop crashes, freezes, or misbehaves and you suspect *some program* is behind it — but you have no idea which one — a clean boot is the detective's magnifying glass. It starts Windows with everything third-party switched off: no antivirus, no Discord, no printer utilities, no RGB software. If the problem vanishes, you've proven it's software, not hardware or Windows itself. Then you switch things back on in groups until the culprit reveals itself.

Technicians use this constantly because it turns "something is wrong and I don't know what" into a systematic hunt. It takes ten minutes to set up, it's completely reversible, and it works for crashes, slowdowns, error messages, and weird behavior alike.

## Why this happens

A clean boot is a diagnostic technique, so "why this happens" here means why third-party software causes the problems a clean boot exposes:

- **Programs fighting over the same resources.** Two programs hooking the same system function — two antivirus products, or an antivirus plus a "system optimizer" — create conflicts that crash processes or freeze the system.
- **Buggy startup programs.** Software that launches at boot runs with high privilege and early timing. A bug there affects everything that starts after it, producing crashes that look like Windows problems.
- **Driver-adjacent software.** VPN clients, virtual-machine software, and disk tools install kernel-level components. When those misbehave, you get blue screens — our [blue screen troubleshooting guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) pairs well with clean-boot diagnosis for exactly these cases.
- **Outdated software on a new Windows build.** A program written for Windows 10 can misbehave on 24H2 in subtle ways — not crashing itself, but destabilizing the programs around it.
- **Too many startup items.** Even without bugs, dozens of startup programs compete for disk and CPU during boot, causing timeouts, hangs, and services that fail to start properly.
- **Malware masquerading as utilities.** Sketchy "driver updaters" and "PC cleaners" install themselves to start at boot and cause exactly the instability they claim to fix.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Perform the clean boot

The core procedure — disable everything third-party, restart, test.

1. Press **Win + R**, type `msconfig`, and press Enter to open **System Configuration**.
2. Go to the **Services** tab. Tick **Hide all Microsoft services** at the bottom — this is the critical step; it protects Windows' own services from being disabled.
3. Click **Disable all**. Every remaining (third-party) service is now unchecked.
4. Switch to the **Startup** tab and click **Open Task Manager**. In Task Manager's **Startup apps**, select each **Enabled** item and click **Disable**. Close Task Manager.
5. Back in System Configuration, click **OK** and choose **Restart**.
6. When the laptop reboots, test the exact scenario that was failing. If the problem is gone, a third-party program was responsible — proceed to Fix 2 to find which one.

### Fix 2: Hunt the culprit by halves

Re-enable in groups to isolate the offender efficiently — binary search beats one-by-one.

1. Open **msconfig** again, go to the **Services** tab (with **Hide all Microsoft services** still ticked), and re-enable the **top half** of the disabled services. Restart and test.
2. If the problem returns, the culprit is in that half — disable half of *those* and retest. If the problem stays away, the culprit is in the other half — enable half of the remaining and retest.
3. Repeat the halving until you've narrowed it to a single service. Each round cuts the suspects in half, so even 60 services take only about six rounds.
4. Do the same for **Startup apps** in Task Manager if the services all check out clean — enable half, test, narrow down.
5. This methodical halving feels slow but it's dramatically faster than enabling one item per reboot, and it never misses.

### Fix 3: Deal with the culprit

Once you've named the offender, decide its fate.

1. If it's non-essential (game launchers, RGB software, updaters), uninstall it via **Settings > Apps > Installed apps** — or just leave it disabled in Task Manager's **Startup apps** if you use it occasionally.
2. If it's something you need (antivirus, VPN, printer software), check the vendor's site for an update — the conflict may be a known bug fixed in a newer version.
3. If it's your antivirus conflicting, consider switching to **Microsoft Defender** (built into Windows, free, and conflict-free by design) rather than fighting a third-party product.
4. After removing or updating the culprit, restore normal boot (Fix 4) and verify the original problem is gone with everything else enabled.

### Fix 4: Return to normal startup

Don't leave the laptop in diagnostic mode — restore everything except the culprit.

1. Open **msconfig**, go to the **General** tab, and select **Normal startup**. Click **OK**.
2. Open **Task Manager > Startup apps** and re-enable everything you disabled, *except* the culprit you identified (leave that one disabled or uninstalled).
3. Restart. The laptop now boots normally with all your software — minus the troublemaker.
4. Use the laptop for a full day of normal work to confirm the problem is truly gone and nothing else was depending on the disabled item.

### Fix 5: Use clean boot to diagnose update failures

Clean boot isn't just for crashes — it's excellent for updates that won't install.

1. Perform the clean boot as in Fix 1.
2. While in the clean-boot state, run **Settings > Windows Update > Check for updates** and install the failing update.
3. Third-party interference (especially antivirus file filters) is a leading cause of update failures, and updates often sail through in a clean-boot state that they couldn't touch normally.
4. Restore normal startup afterward with Fix 4. If the same update fails again next month with the specific [error 0x800f0922](/articles/how-to-fix-error-0x800f0922-in-windows-11-24h2/), that guide covers the partition-space cause behind it — otherwise, consider replacing the culprit program.

### Fix 6: Document what you found

Future you will thank present you.

1. Write down the culprit program's name and what it was breaking. A note in your phone or a text file on the desktop is enough.
2. If it was a driver-adjacent program (VPN, virtualization, disk tool), note the version — when the vendor releases a fixed version, you'll know it's safe to try again.
3. Check whether the vendor has a support article about the conflict; reporting it helps them fix it, and their workaround might be better than yours.
4. Consider whether you even need the program. The most stable software is software you don't run — every clean-boot hunt that ends in "I uninstalled it and never missed it" is a win. Microsoft's [official clean-boot documentation](https://support.microsoft.com/en-us/windows) has additional background if you want the full technical picture.

## Closing

The clean boot is the closest thing Windows troubleshooting has to a universal solvent: whenever the question is "is it Windows, hardware, or some program I installed," a clean boot answers it in one reboot. Learn the msconfig dance — hide Microsoft services, disable all, Task Manager startup items, restart — and keep the halving technique in your back pocket. Most software conflicts aren't mysterious once you can turn the suspects off in groups; they're just tedious. And tedium, unlike mystery, always yields to method.
