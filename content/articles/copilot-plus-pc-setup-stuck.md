---
title: "How to Fix Copilot+ PC Setup Stuck During Initial Setup"
slug: copilot-plus-pc-setup-stuck
date: 2026-10-26
categories: ["ai-pc"]
tags:
  - copilot-plus-pc
  - setup
  - windows-11
  - troubleshooting
  - oobe
description: "Copilot+ PC setup stuck on a loading screen? Learn the safe ways to unstick out-of-box setup without losing data and finish configuring your new PC safely."
thumbnail: "/images/thumbs/copilot-plus-pc-setup-stuck.webp"
faqs:
  - q: "Is it safe to restart a PC stuck in setup?"
    a: >
      Usually, yes. Out-of-box setup is designed to resume after a restart, and Windows keeps your
      progress through most stages. Avoid a forced shutdown only during an actual firmware update
      or while the screen explicitly says an update is installing.
  - q: "How long should Copilot+ PC setup normally take?"
    a: >
      Most setups finish in 15 to 45 minutes depending on your internet speed and update size. If a
      single screen has not changed for over an hour with no disk or network activity, the setup is
      genuinely stuck rather than merely slow.
  - q: "Will I lose anything if setup restarts from the beginning?"
    a: >
      No files are at risk, because no personal data exists on a brand-new PC yet. At worst you
      repeat the language, region, and account steps, which only takes a few minutes.
  - q: "What if setup keeps freezing at the same step every time?"
    a: >
      A repeat freeze at the same step usually points to a network problem, a bad update, or faulty
      hardware. Try setup without Wi-Fi, skip optional updates, or test with different installation
      media before suspecting the machine itself.
---

Unboxing a new Copilot+ PC should be the fun part: power on, answer a few questions, sign in, and start using a fast new machine. When setup freezes instead, the excitement turns to worry very quickly. The screen sits on "Hi there," "Checking for updates," or "Setting up your device" for an hour or more, the spinner keeps turning, and nothing you press seems to help. Because the machine is brand new, the fear is that something is already broken — but in most cases, setup is simply waiting on something that will never arrive.

Setup can stall for surprisingly ordinary reasons. A slow or captive Wi-Fi network can leave the update check hanging forever. A Microsoft account sign-in can fail silently behind the scenes. A Windows update can download but never finish applying. On some machines, a driver for a built-in device stalls the whole sequence — a pattern familiar from other first-boot headaches, such as a [printer driver missing on ARM Windows](/articles/printer-driver-arm-windows-missing/) blocking an otherwise healthy install. Setup is a chain of steps, and any single slow link freezes the entire chain.

The fixes below are ordered by safety. First you confirm whether setup is truly stuck or just slow, then you try the least disruptive escapes, and only then do you consider restarting setup or reinstalling. The same patient, step-by-step approach untangles other new-PC problems too, including [Asus Zenbook S14 AI quirks](/articles/asus-zenbook-s14-ai-issues/) that appear during first configuration. A related lesson applies to bundled creative apps: when [Clipchamp's AI features fail to work](/articles/clipchamp-ai-features-not-working/) on a fresh machine, the cause is often the same unfinished update or incomplete driver set that stalls setup itself.

## Why this happens

- **Slow or captive Wi-Fi:** Setup waits on network steps, and a hotel-style login page or a weak signal can leave it waiting indefinitely with no error shown.
- **Windows update stuck mid-download:** A large update that downloads slowly or fails to verify can hold the "Checking for updates" screen for hours.
- **Microsoft account sign-in failure:** If sign-in cannot complete — bad password, two-factor delay, or a service hiccup — setup may spin instead of showing a clear error.
- **Driver installation stall:** A driver for the NPU, camera, or another Copilot+ component can hang during first boot, blocking every step behind it.
- **Corrupted setup files or interrupted first boot:** A power cut or forced shutdown during the first boot can leave setup in a half-finished state that loops on restart.
- **Faulty storage or memory:** Rarely, a genuine hardware fault — a failing drive or bad memory — makes setup freeze at the same point every time.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm setup is truly stuck, not just slow

Patience is a real fix here, because interrupting a healthy setup creates the very corruption you are trying to avoid. Checking for signs of life first saves you from an unnecessary restart.

1. Wait at least 30 minutes on the stuck screen before doing anything.
2. Watch for disk activity lights or fan changes that show work is happening.
3. Move the mouse and press a key to confirm the screen is not simply frozen.
4. If progress text, percentages, or the spinner animation still change, keep waiting.
5. Only proceed to the next fixes if nothing has changed for a full hour.

### Fix 2: Fix the network connection setup is waiting on

Network stalls are the most common cause, and they are also the easiest to eliminate. Giving setup a clean connection — or none at all — often unsticks it within minutes.

1. If you are on Wi-Fi, move closer to the router or switch to a wired connection.
2. On a captive network, such as hotel Wi-Fi, switch to a phone hotspot instead.
3. If the network asks for a browser login, complete it on another device first.
4. Restart your router, then wait for setup to detect the restored connection.
5. As a test, disconnect from Wi-Fi entirely and see if setup offers an offline path.

### Fix 3: Restart setup safely with a power cycle

When setup is genuinely frozen with no activity, a restart is the correct move. Out-of-box setup is built to resume, so this is far less risky than it feels.

1. Hold the power button for 10 seconds until the laptop fully powers off.
2. Wait 30 seconds, then power the laptop back on.
3. Let setup resume and watch whether it passes the previously stuck step.
4. If it returns to the same screen, let it sit for 15 minutes before judging.
5. Repeat the power cycle once more if the second attempt also freezes.

### Fix 4: Skip optional updates and finish setup offline

Optional updates and feature downloads are the usual stall points. Skipping them lets you reach the desktop, where updates can run properly with full tools available.

1. When setup offers a network connection, choose the option to skip or continue without internet.
2. If an update screen offers "Skip" or "Remind me later," take it.
3. Complete the remaining steps — region, keyboard, account — without updates.
4. Once on the desktop, open Settings, then Windows Update, and install updates there.
5. Restart after updates finish and confirm the PC is fully up to date.

### Fix 5: Use a clean restart with peripherals removed

USB devices and docks can stall driver installation during setup. Stripping the machine back to basics removes those variables in one move.

1. Power off the laptop and unplug every USB device, dock, and external monitor.
2. Power on and let setup run with only the charger connected.
3. If setup completes, reconnect devices one at a time, testing after each.
4. If one device freezes setup again, leave it unplugged and update its driver later.
5. Check [Windows 11 download and recovery options](https://www.microsoft.com/en-us/software-download/windows11) if you need fresh installation media.

### Fix 6: Reset the PC and run setup again

When setup loops at the same step across restarts, a reset gives you a clean slate. This erases nothing personal, since a new PC holds no user files yet.

1. From the setup screen, press Shift + F10 to open a command prompt if available.
2. If recovery options are reachable, choose Troubleshoot, then Reset this PC.
3. Select "Keep my files" if offered, or a full reset on a brand-new machine.
4. Let the reset complete, then run through setup from the beginning.
5. If the same step freezes again after a reset, contact the manufacturer's support — the fault is likely hardware.

## Closing

A Copilot+ PC stuck in setup feels alarming on a brand-new machine, but the cause is usually a network stall, a slow update, or a driver hiccup — not a broken laptop. Confirm it is truly stuck, fix the connection, restart safely, and skip optional updates to reach the desktop, where the remaining updates can finish properly. If a reset still freezes at the same step, that repeatability is valuable evidence for a warranty claim, and you will have ruled out every software cause first.
