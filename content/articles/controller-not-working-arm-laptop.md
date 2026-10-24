---
title: "How to Fix Controller Not Working on ARM Laptops"
slug: controller-not-working-arm-laptop
date: 2026-10-24
categories: ["ai-pc"]
tags: ["controller", "gamepad", "arm laptop", "bluetooth", "gaming"]
description: "Xbox or PlayStation controller not connecting to your Snapdragon laptop? Fix controller issues on ARM Windows with these pairing, driver, and USB steps."
thumbnail: "/images/thumbs/controller-not-working-arm-laptop.webp"
faqs:
  - q: "Do Xbox controllers work on Windows on ARM laptops?"
    a: >
      Yes. Xbox Wireless Controllers connect via Bluetooth or USB and work normally on Snapdragon laptops — controller support is architecture-independent. Pairing and input issues are Bluetooth-stack or driver problems, not ARM limitations.
  - q: "Why does my controller pair but not work in games?"
    a: >
      Paired-but-dead usually means the game is reading a different input API (XInput vs. DirectInput), Steam Input is interfering, or another device claimed the controller first. Testing in the Xbox Accessories app or Steam's controller settings isolates which layer is failing.
  - q: "Why does my controller keep disconnecting over Bluetooth?"
    a: >
      Bluetooth dropouts are typically power management (Windows turning off the radio to save power), interference from Wi-Fi/USB 3 devices, or low controller batteries. Disabling Bluetooth power saving and using fresh batteries fix most cases.
  - q: "Should I use Bluetooth or USB for my controller?"
    a: >
      USB is more reliable — lower latency, no pairing issues, no battery concerns. Use Bluetooth for convenience, USB for competitive play or when Bluetooth misbehaves. A USB cable also updates Xbox controller firmware through the Xbox Accessories app.
---

Your controller paired yesterday. Today the laptop does not see it, or it connects and then does nothing in games, or it disconnects every ten minutes mid-match. Controllers are supposed to be plug-and-play — when they are not, the frustration is disproportionate because the fix should be simple.

Controller support on Windows on ARM is architecture-independent — the input stack does not care about your CPU. So controller problems on Snapdragon laptops are the same Bluetooth, USB, driver, and game-configuration issues as anywhere else, with ARM-specific wrinkles only in Bluetooth driver maturity and power management aggressiveness.

This guide gives you six fixes in order: fix Bluetooth pairing, fix USB connections, update controller firmware and drivers, configure Steam/Xbox input layers, fix in-game detection, and stop the dropouts. If voice typing also misbehaves on the machine, the Bluetooth stack is a shared suspect: [voice typing not working on ARM](/articles/voice-typing-not-working-arm-laptop/).

## Why this happens

- **Bluetooth pairing corruption:** Stale pairings, especially after Windows updates, cause "pairs but won't connect" loops.
- **Bluetooth power management:** Windows aggressively powers down the Bluetooth radio on laptops to save battery — disconnecting idle controllers.
- **Controller firmware outdated:** Old firmware has pairing and input bugs fixed in updates delivered via USB.
- **Steam Input conflicts:** Steam's controller remapping layer can fight the game's native input or double-map buttons.
- **Game reading the wrong API:** XInput vs. DirectInput mismatches make controllers invisible to specific games.
- **USB port/power issues:** Underpowered ports or hubs cause wired controllers to drop.
- **Interference:** Wi-Fi, USB 3.0 devices, and microwaves share the 2.4GHz band with Bluetooth.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean up Bluetooth pairing and re-pair

Most "was working, now isn't" Bluetooth controller issues are stale pairing data. Removing the device everywhere and pairing fresh resolves the corrupted-state cases.

1. Go to **Settings > Bluetooth & devices**, find the controller, click **...** > **Remove device**.
2. Put the controller in pairing mode (Xbox: hold the pair button until the light flashes rapidly; DualSense/DualShock: hold PS + Share/Create).
3. Click **Add device > Bluetooth** and select the controller when it appears.
4. Test immediately in a game or the Xbox Accessories app — confirm inputs register.
5. If pairing fails repeatedly, restart the laptop's Bluetooth: toggle Bluetooth off/on in Quick Settings, or restart the **Bluetooth Support Service** in `services.msc`. ASUS ProArt owners report similar Bluetooth flakiness: [ASUS ProArt PX13 AI issues](/articles/asus-proart-px13-ai-issues/).

### Fix 2: Disable Bluetooth power management

The classic "disconnects when idle, or randomly" cause on laptops. Windows' power saver turns off the Bluetooth radio — great for battery, terrible for controllers.

1. Open **Device Manager > Bluetooth**, right-click your Bluetooth adapter > **Properties > Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. Do the same under **Universal Serial Bus controllers** for USB root hubs if you use USB Bluetooth dongles.
4. In **Settings > System > Power & battery**, check that battery saver is not aggressively managing Bluetooth.
5. Test a full gaming session. If dropouts stop, power management was the culprit — this single checkbox fixes a remarkable number of cases.

### Fix 3: Update controller firmware and drivers

Controller firmware updates fix pairing bugs, input lag, and disconnect issues — and they require USB. Outdated firmware is invisible until it causes exactly your symptom.

1. Connect the controller via USB cable to the laptop.
2. Open the **Xbox Accessories** app (Microsoft Store) — it detects the controller and offers firmware updates.
3. Install any available firmware update and do not disconnect during the process.
4. For PlayStation controllers, use the manufacturer's firmware updater on a PC (or check for updates via the console).
5. In **Device Manager**, check for warning icons on Bluetooth and USB controllers — update those drivers via Windows Update optional drivers. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document driver update procedures.

### Fix 4: Configure Steam Input correctly

Steam's controller layer is powerful and frequently the problem: it remaps inputs, creates virtual controllers, and confuses games. When a controller works in some games but not others, Steam Input is the prime suspect.

1. In Steam, go to **Settings > Controller** and check the detected controllers — confirm yours appears.
2. Per-game: right-click the game > **Properties > Controller** — try **Enable Steam Input**, **Disable Steam Input**, and **Use default** to find which the game prefers.
3. If buttons are double-mapped or wrong, open the game's **Controller Configuration** and reset to the official layout.
4. For non-Steam games added to Steam, Steam Input can hijack the controller — disable it for those shortcuts.
5. Test with Steam fully closed (not just minimized) — if the controller works with Steam closed, Steam Input was interfering.

### Fix 5: Fix in-game controller detection

The controller pairs, Windows sees it, but the game ignores it. This is the input-API layer: the game expects XInput and gets something else, or another device is player one.

1. Confirm the controller works in Windows: **Settings > Bluetooth & devices** shows it connected, or test at gamepad-tester.com in Edge.
2. Disconnect other input devices (flight sticks, racing wheels, extra controllers) — some games only read "controller 1."
3. For older games, check whether they need DirectInput mode — Xbox controllers are XInput; tools like Steam Input can translate.
4. Check the game's settings for a controller enable toggle — some games default to keyboard/mouse and need the toggle flipped.
5. Try launching the game with the controller already connected and turned on — hot-plugging mid-game fails in some titles. Copilot's VPN conflicts show the same "order of operations matters" pattern: [Copilot not working with VPN](/articles/copilot-not-working-with-vpn/).

### Fix 6: Reduce interference and stabilize the connection

The remaining dropouts are environmental: 2.4GHz congestion, distance, low batteries, or USB power issues for wired play.

1. Replace or recharge the controller batteries — low batteries cause exactly the "random disconnect" pattern, and the indicator lies.
2. Move the laptop away from USB 3.0 hubs/docks and Wi-Fi routers — both spray 2.4GHz interference.
3. Sit within a few meters with line-of-sight — Bluetooth range collapses through desks and walls.
4. For wired: use a direct laptop USB port, not a hub — and try a different cable (charge-only cables lack data wires).
5. If Bluetooth remains flaky after all this, a quality USB Bluetooth 5.x dongle (with its own antenna) often outperforms the laptop's internal radio — $15 ends the fight.

## Closing

Controllers on Snapdragon laptops work fine — the input stack is architecture-independent, so every fix here is the same one that works on Intel. Bluetooth pairing hygiene, the power-management checkbox, firmware updates, and Steam Input configuration cover nearly every case. Do them in order, and the controller goes back to being invisible: you press buttons, the game responds, and nobody thinks about Bluetooth at all.
