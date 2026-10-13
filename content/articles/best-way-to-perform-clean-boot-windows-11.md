---
title: "Best Way to Perform a Clean Boot on Windows 11"
slug: best-way-to-perform-clean-boot-windows-11
date: 2026-10-08
categories: ["windows-errors"]
tags: ["clean-boot", "windows-11", "troubleshooting"]
description: "Learn the right way to clean-boot Windows 11 to isolate crashing apps, slow startups, and mystery errors."
thumbnail: "/images/thumbs/best-way-to-perform-clean-boot-windows-11.webp"
faqs:
  - q: "What is a clean boot?"
    a: "A clean boot starts Windows with only Microsoft services and no third-party startup programs. It doesn't delete anything — it temporarily disables non-essential software so you can tell whether a problem is caused by Windows itself or by something installed on top of it."
  - q: "Is a clean boot the same as Safe Mode?"
    a: "No. Safe Mode loads a minimal set of drivers and a basic display, while a clean boot loads your normal drivers but disables third-party services and startup apps. Clean boot is better for isolating software conflicts; Safe Mode is better when Windows barely runs."
  - q: "Will a clean boot delete my programs?"
    a: "No. It only disables them temporarily. When you re-enable normal startup afterward, everything comes back exactly as it was. Nothing is uninstalled at any point."
  - q: "How do I find which program is causing the problem?"
    a: "After clean-booting, re-enable services and startup apps in halves: enable half, restart, test. If the problem returns, the culprit is in that half — keep halving until one program remains. It's methodical but it always works."
---
# Best Way to Perform a Clean Boot on Windows 11

A **clean boot** is the single most useful diagnostic technique in Windows troubleshooting, and most people do it wrong — they disable a few startup apps and call it done. Done properly, a clean boot strips Windows down to Microsoft-only services plus your normal drivers, giving you a clean room to test whether a crash, slowdown, or error comes from Windows itself or from something you installed.

Use it whenever a problem might be software conflict: random crashes, apps that won't launch, login loops, or performance issues with no obvious cause. Don't use it for hardware symptoms — a clean boot won't fix overheating, bad RAM, or a failing drive, and testing those first saves you a wasted hour.

A lighter version of this technique helps with [Windows stuck on the restarting screen](/articles/windows-11-stuck-on-restarting-screen-fix/).

## Why this happens (when you need a clean boot)

- **Conflicting startup programs:** Two apps fighting over the same system hooks at boot.
- **Buggy third-party services:** A service that crashes or hangs, dragging the system down with it.
- **Shell extensions:** Context-menu and Explorer add-ons that destabilize the desktop.
- **Driver-adjacent software:** RGB controllers, fan tools, and "optimizers" that install kernel-adjacent components.
- **Antivirus conflicts:** Overly aggressive real-time scanning breaking legitimate apps.
- **Mystery slowdowns:** Boot taking minutes with no clear cause — a clean boot tells you in one restart whether software is to blame.

## How to fix it (perform the clean boot)

Work through these in order. The process has three phases: set up, test, and identify.

### Fix 1: Open System Configuration

The clean boot is configured in the classic `msconfig` tool.

1. Press **Win + R**, type `msconfig`, and press **Enter**.
2. Go to the **Services** tab.
3. Tick **Hide all Microsoft services** at the bottom — this is the critical step that protects Windows' own services from being disabled. Skipping it can leave Windows unable to boot properly, so double-check the box is ticked before touching anything.
4. Click **Disable all**. Every remaining (third-party) service is now unchecked.
5. Don't click OK yet — first handle startup apps in Fix 2.

### Fix 2: Disable startup apps in Task Manager

Startup apps live in a different place and must be disabled separately.

1. In the System Configuration window, go to the **Startup** tab and click **Open Task Manager**.
2. In Task Manager's **Startup apps** tab, right-click each **Enabled** app and choose **Disable**.
3. Don't skip "harmless" ones — the point is to disable everything for a true clean baseline.
4. Close Task Manager, back in System Configuration click **OK**, and restart when prompted. The restart takes you into the clean-boot state — your desktop will look the same, but none of your third-party apps will be running in the background.

### Fix 3: Test in the clean-boot state

Now determine whether the problem is third-party software at all.

1. After restarting, confirm the clean boot is active: Task Manager's **Startup apps** should show everything disabled.
2. Reproduce the problem — run the crashing app, wait for the error, or time the boot.
3. If the problem is **gone**, it's caused by third-party software — continue to Fix 4 to find which one.
4. If the problem **persists**, third-party startup software is innocent — look at drivers, Windows components, or hardware instead. Re-enable normal startup (Fix 6) and investigate elsewhere, such as our [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

### Fix 4: Re-enable in halves to find the culprit

The binary search: enable half, test, narrow down.

1. Open `msconfig` again, go to **Services** (with Microsoft services hidden), and re-enable the **top half** of the disabled services.
2. In Task Manager, re-enable the **top half** of startup apps.
3. Restart and test. Problem back? The culprit is in this half. Still fine? It's in the other half.
4. Keep halving the suspect group — enable or disable halves, restart, test — until one service or app remains.
5. This takes several restarts, but each one eliminates half the suspects. Be patient; it converges fast. Keep notes on paper or your phone — after four or five reboots it's easy to forget which half you're testing.

### Fix 5: Deal with the culprit

Once identified, decide what to do with the offending software.

1. Check for an updated version — the vendor may have fixed the conflict already.
2. If no update helps, change its settings (disable its startup entry, turn off overlapping features like a second antivirus's real-time shield).
3. If it's non-essential, uninstall it. "System optimizers," duplicate cloud-sync clients, and old VPN clients are frequent offenders.
4. If it's essential (your antivirus, for example), contact the vendor's support with your findings — "clean boot isolates the crash to your service" gets their attention fast.

### Fix 6: Return to normal startup

Don't stay in clean-boot state — it's a diagnostic mode, not a way of life.

1. Open `msconfig`, go to the **Services** tab, and click **Enable all** (Microsoft services were never disabled thanks to the hide checkbox).
2. In Task Manager's **Startup apps**, re-enable everything except the identified culprit.
3. On the **General** tab of System Configuration, ensure **Normal startup** is selected.
4. Click **OK**, restart, and verify the problem stays gone.
5. Document what you found — if the culprit updates itself back into a broken state later, you'll recognize the symptoms immediately instead of starting the diagnosis from zero. Microsoft documents the official clean-boot procedure on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

A proper clean boot — Microsoft services protected, everything else disabled, then a methodical halving search — identifies the conflicting software behind crashes, loops, and slowdowns every time. It costs a few restarts, but it replaces hours of guessing with certainty. Learn this technique once and you'll use it for every mysterious Windows problem from here on, and you'll diagnose faster than most shop technicians.
