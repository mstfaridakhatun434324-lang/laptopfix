---
title: "How to Make Live Captions Start Automatically at Boot on Windows 11"
slug: live-captions-auto-start-boot
date: 2026-10-22
categories: ["ai-pc"]
tags: ["live-captions", "auto-start", "startup", "windows-11", "copilot-plus-pc", "task-scheduler"]
description: "Want Live Captions to auto-start at every boot? Set it up on your Copilot+ laptop with the Startup folder or Task Scheduler, and fix silent launch failures."
thumbnail: "/images/thumbs/live-captions-auto-start-boot.webp"
faqs:
  - q: "Is there a built-in setting to auto-start Live Captions?"
    a: "No. Windows 11 does not offer a native 'start Live Captions at boot' toggle. You set it up yourself with a Startup-folder shortcut or a Task Scheduler task at logon — both methods are covered step by step below."
  - q: "Will auto-starting Live Captions slow down my boot?"
    a: "Slightly. Live Captions loads its NPU models at launch, which adds a few seconds of background work. If boot feels slower after enabling it, our [Copilot+ slow boot fix](/articles/copilot-plus-pc-slow-boot-fix/) helps trim startup overall."
  - q: "Why does my auto-start entry launch Live Captions but show a blank window?"
    a: "The caption service launched before the NPU driver or audio stack was ready. Add a 30–60 second delay to the Task Scheduler trigger, or use the Startup folder (which launches later in the boot sequence) so drivers finish initializing first."
  - q: "How do I stop Live Captions from starting at boot?"
    a: "Delete the shortcut from the Startup folder (Win+R, shell:startup) or disable the scheduled task in Task Scheduler. Either method takes effect on the next sign-in."
---

If you rely on Live Captions for every call, class, or video, opening it manually after each boot gets old fast. Windows 11 has no built-in "launch at startup" switch for captions — but the standard Windows startup machinery handles it fine once you wire it up.

The setup itself is straightforward; the headaches come after. Auto-started captions sometimes open to a blank window, appear before the NPU driver is ready, or never launch at all because Fast Startup skipped a real initialization. On Arm-based Copilot+ PCs, startup quirks can also come from the [x64 emulation cache](/articles/x64-emulation-cache-clear-arm/) — worth knowing if other apps misbehave at boot too.

This guide gives you two reliable auto-start methods and repairs each failure mode, so captions are simply there when your desktop appears.

## Why this happens

- **No native auto-start toggle:** Microsoft did not ship a startup option, so manual setup is required.
- **Race with driver initialization:** Captions can launch before the NPU driver or audio service is ready, showing a blank window.
- **Fast Startup skips full init:** Hybrid shutdown can leave the caption service in a half-initialized state.
- **Task misconfiguration:** Wrong trigger, missing "run only when logged on," or a bad program path silently breaks scheduled tasks.
- **Startup folder item disabled:** Task Manager's Startup apps list can disable the shortcut without telling you.
- **NPU driver not loading at boot:** A damaged driver install means captions auto-start into a broken pipeline every time.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Add Live Captions to the Startup folder

The Startup folder is the simplest method — anything in it launches after you sign in, late enough that drivers are usually ready.

1. Press Win+R, type shell:startup, and press Enter to open your Startup folder.
2. Open the Start menu, find Live Captions in the app list, and drag it into the Startup folder to create a shortcut (or right-click > Open file location, then copy the shortcut).
3. Restart the laptop and sign in; Live Captions should open on its own.
4. If nothing appears, open Task Manager > Startup apps and make sure the Live Captions entry is Enabled.
5. Reposition the caption window once — Windows remembers its last position for future launches.

### Fix 2: Use Task Scheduler with a logon delay

Task Scheduler gives you a delay option, which fixes the blank-window race where captions start before the NPU driver.

1. Open Task Scheduler from the Start menu and choose Create Task (not Basic Task).
2. On the General tab, name it "Live Captions Auto-Start" and select "Run only when user is logged on."
3. On the Triggers tab, add a trigger "At log on" for your user, with "Delay task for" set to 1 minute.
4. On the Actions tab, set the action to Start a program and point it at the Live Captions app executable.
5. Save, restart, and sign in — captions should appear about a minute after the desktop, fully working.

### Fix 3: Repair the blank-window race condition

If auto-started captions open but show nothing, the app beat the driver to the punch. Delaying or re-sequencing the launch fixes it.

1. Confirm the symptom: manually launched captions work fine, only auto-started ones are blank.
2. If using the Startup folder method, switch to the Task Scheduler method with a 1–2 minute delay.
3. If already using Task Scheduler, increase the delay to 2 minutes.
4. Check Device Manager after boot — the NPU should show no warning icon before captions launch.
5. If the NPU driver looks broken at boot, a clean reinstall following our [Intel NPU clean install guide](/articles/intel-npu-driver-clean-install-ddu/) fixes the underlying driver load.

### Fix 4: Find and fix a silently failing scheduled task

A task that never fires usually has a configuration mistake. Task Scheduler's own history tells you exactly what happened.

1. Open Task Scheduler, find your Live Captions task, and open its History tab (enable history in the right pane if it is off).
2. Look for the last run result — "0x1" or "file not found" means the program path is wrong; fix the action path.
3. Make sure the trigger is "At log on" for the correct user, not "At startup" (which runs too early, before logon).
4. On the Conditions tab, uncheck "Start the task only if the computer is on AC power" if you boot on battery.
5. Run the task manually from Task Scheduler to confirm it launches captions, then reboot to test the real trigger.

### Fix 5: Stop Fast Startup from breaking the launch

Fast Startup's hybrid shutdown can leave services half-initialized, which confuses auto-started apps that depend on driver state.

1. Open Control Panel > Power Options > "Choose what the power buttons do."
2. Click "Change settings that are currently unavailable."
3. Uncheck "Turn on fast startup" and save changes.
4. Shut down fully (not restart), power on, and check whether captions now auto-start correctly.
5. If boot got noticeably slower overall from your changes, run through our [slow boot fix for Copilot+ PCs](/articles/copilot-plus-pc-slow-boot-fix/) to keep startup lean. Microsoft's [support hub](https://support.microsoft.com/en-us/windows) also documents startup troubleshooting for apps that misbehave at logon.

### Fix 6: Remove auto-start cleanly when you no longer want it

Auto-start you cannot turn off is just bloat. Removing it cleanly avoids leftover tasks and shortcuts.

1. For the Startup folder method: press Win+R, type shell:startup, and delete the Live Captions shortcut.
2. For Task Scheduler: open Task Scheduler, right-click the task, and choose Delete.
3. Check Task Manager > Startup apps for any leftover Live Captions entry and disable it.
4. Restart and confirm captions no longer appear — launch them manually when needed.

## Closing

Auto-starting Live Captions is a small quality-of-life win that Windows makes you assemble yourself — a Startup-folder shortcut for simplicity, or a delayed Task Scheduler task when the blank-window race bites. The key insight is timing: captions depend on the NPU driver and audio stack, so launching a minute after logon beats launching instantly. Set it up once, verify it survives a real shutdown-and-power-on cycle, and captions become part of your desktop instead of another thing to remember.
