---
title: "Best Way to Fix Windows Update Stuck on the Restarting Screen"
slug: "best-way-to-fix-windows-update-stuck-on-restarting-screen"
date: 2026-10-13
categories: ["windows-update"]
tags: ["windows update", "stuck on restarting", "frozen update", "troubleshooting", "laptop"]
description: "Windows Update stuck on the ‘Restarting’ screen? Learn the safest order: when to wait, when to force a restart, and how to repair the update."
thumbnail: "/images/thumbs/best-way-to-fix-windows-update-stuck-on-restarting-screen.webp"
faqs:
  - q: "How long should I wait on the Restarting screen?"
    a: >
      For monthly updates, 30 to 45 minutes; for feature updates, 60 to 90
      minutes — longer on hard drives or nearly full SSDs. Only consider
      it stuck if the dots freeze or nothing changes for over two hours.
      These phases do heavy work — migrating drivers, finalizing file
      operations — that simply takes time on slower storage. Impatience is
      the main cause of interrupted updates, so set a timer and walk away.
  - q: "Will force-restarting damage Windows?"
    a: >
      A single forced restart during a stuck update is generally safe —
      Windows is designed to resume or roll back. The risk comes from
      repeated forced shutdowns, which is why you wait first and intervene
      once, deliberately. Each forced shutdown during active disk writes
      carries a small corruption risk; doing it once after a proper wait
      is the accepted procedure, while doing it five times in a panic is
      how systems get damaged.
  - q: "Why do the dots keep spinning if it’s stuck?"
    a: >
      Spinning dots mean the UI thread is alive, not that the install is
      progressing. A hung driver or stalled phase can leave the animation
      running indefinitely while nothing advances underneath. The
      animation is rendered by a separate lightweight process that keeps
      looping regardless of install state. Judge stuck-ness by elapsed
      time and disk activity — not by the dots, which will happily spin
      for hours on a deadlocked system.
  - q: "Should I unplug USB devices during updates?"
    a: >
      Yes — disconnect everything non-essential before starting an update.
      USB docks, drives, and peripherals are disproportionately
      represented in stuck-restart cases because their drivers stall the
      restart handoff. The update must stop and restart every device
      driver during the reboot; one misbehaving USB driver can deadlock
      the whole sequence. Keep only the charger connected, and reattach
      everything after the update completes.
---

Few sights are as nerve-wracking as a laptop sitting on the ‘Restarting’ screen with the spinning dots for an hour or more during Windows Update. The instinct is to hold the power button — and sometimes that is eventually the right move — but doing it too early can interrupt a legitimate install phase and create the very corruption you are trying to avoid. The best approach is a disciplined sequence: verify it is truly stuck, wait the right amount of time, then intervene safely.

Here is the key fact most guides bury: the ‘Restarting’ screen covers several distinct phases, and some of them are legitimately slow. A feature update can sit at this screen for 30 to 90 minutes on a spinning hard drive or a nearly full SSD while it migrates drivers and finalizes the install. The dots spinning means the system is alive; frozen dots or a completely static screen for a very long time means it is not.

This guide gives you the best-practice order used by technicians: how long to wait, how to tell stuck from slow, the safe way to force a restart when waiting fails, and the repairs that prevent it from happening again. If you are dealing with a related symptom instead, see [troubleshooting a Windows 11 stuck-on-restarting screen](/articles/windows-11-stuck-on-restarting-screen-fix/) and [fixing a Windows update undoing-changes loop](/articles/how-to-fix-windows-update-undoing-changes-stuck-on-dell-laptop/).

The instinct when a laptop sits on ‘Restarting’ for an hour is to hold the power button, and eventually that may be the right move — but timing matters enormously. Interrupting a healthy install phase creates the corruption you are trying to avoid, while waiting forever on a truly deadlocked machine wastes your evening. The discipline is simple: verify it is actually stuck using the checks below, wait the appropriate window, and only then intervene — once, deliberately.

## Why this happens

- **Slow legitimate install phase** driver migration and finalization can take over an hour on slow storage.

- **Driver hanging during restart** a misbehaving driver stalls the shutdown/startup handoff.

- **Corrupt update payload** the installer cannot complete a phase and retries silently.

- **Peripheral blocking restart** USB devices can stall the restart sequence.

- **Insufficient disk space** finalization needs working room that is not there.

- **Fast Startup interfering** hybrid shutdown state confuses the update restart.

- **Antivirus hooking shutdown** security drivers delay or block the restart phases.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether it is actually stuck

Do not intervene in a healthy install. When in doubt, err toward waiting: an interrupted healthy install causes far more damage than an extra hour spent watching a stuck one.

1. Watch the spinning dots for 5 minutes: moving dots mean activity.

2. Listen for disk activity or check the drive light if your laptop has one.

3. Give feature updates at least 60–90 minutes; monthly updates 30–45 minutes.

4. Only proceed to force a restart if the dots are frozen or nothing has changed for over 2 hours.

### Fix 2: Force a restart — the safe way

When it is genuinely stuck, a forced restart is the correct next step. Do this exactly once and then let the machine work — repeated forced shutdowns compound the risk instead of resolving anything.

1. Hold the power button for 10 seconds until the laptop powers off.

2. Unplug all USB devices except the charger.

3. Wait 30 seconds, then power on.

4. Windows will usually resume or roll back the update automatically.

### Fix 3: Boot into Safe Mode if it loops

Safe Mode bypasses the drivers that stall restarts. If Safe Mode boots fine, the culprit is almost certainly a third-party driver, which narrows your next steps enormously.

1. If the laptop returns to the stuck screen, force-power-off twice more to trigger Automatic Repair.

2. Choose Troubleshoot > Advanced options > Startup Settings > Restart, then press 4 for Safe Mode.

3. In Safe Mode, open Settings > Windows Update and check the status.

### Fix 4: Run the Windows Update troubleshooter

Cleans up the failed attempt’s state. Run this before manually clearing caches; the troubleshooter’s automated resets are gentler than deleting folders by hand.

1. In normal or Safe Mode, go to Settings > System > Troubleshoot > Other troubleshooters.

2. Run the Windows Update troubleshooter and apply its fixes.

3. Restart normally.

### Fix 5: Clear the update cache

Removes the payload that stalled the restart. Clearing the cache also removes the half-downloaded payload that stalled the restart, so the next attempt starts from a genuinely clean state.

1. Elevated Command Prompt: net stop wuauserv, net stop bits.

2. Delete contents of C:\Windows\SoftwareDistribution\Download.

3. net start wuauserv, net start bits.

4. Retry the update.

### Fix 6: Disable Fast Startup

Hybrid shutdown is a known contributor to stuck restarts. Fast Startup skips the full shutdown servicing pass that updates rely on, which is why disabling it prevents a whole class of restart hangs.

1. Open Control Panel > Power Options > ‘Choose what the power buttons do’.

2. Click ‘Change settings that are currently unavailable’.

3. Uncheck ‘Turn on fast startup’ and save.

4. Retry the update with full shutdowns.

### Fix 7: Update drivers and free disk space

Prevents the next stuck restart. Do this maintenance before the next Patch Tuesday rather than during it — calm preparation beats frantic repair every time.

1. Update chipset, storage, and graphics drivers from your laptop maker’s support site.

2. Free at least 25–30 GB on C: with Disk Cleanup.

3. Disconnect USB peripherals before starting the next update.

## Closing

The best way through a stuck ‘Restarting’ screen is patience first, then a deliberate forced restart — never panic, never yank power repeatedly. Most of these resolve with one clean reboot and a cache clear, and the prevention steps keep the next update moving. For official guidance, see [Microsoft’s Windows update support hub](https://support.microsoft.com/en-us/windows).
