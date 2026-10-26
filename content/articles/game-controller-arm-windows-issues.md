---
title: "Game Controller Not Working on Your ARM Laptop? How to Fix It"
slug: game-controller-arm-windows-issues
date: 2026-10-26
categories: ["ai-pc"]
tags: [game-controller, xbox-controller, arm-laptop, windows-gaming, bluetooth, troubleshooting]
description: "Game controller not working on your ARM laptop? Fix pairing, input lag, and unrecognized controller issues on Snapdragon Windows 11 PCs with these steps."
thumbnail: "/images/thumbs/game-controller-arm-windows-issues.webp"
faqs:
  - q: "Why is my Xbox controller not recognized on a Snapdragon laptop?"
    a: >
      The usual causes are a stale Bluetooth pairing, a missing controller driver, or a game that only accepts XInput through an emulation layer. Re-pair the controller, update its firmware, and test it in the Xbox Accessories app to narrow it down.
  - q: "Do PlayStation controllers work on Windows on ARM?"
    a: >
      Yes, DualSense and DualShock controllers generally work over USB and Bluetooth, though some games only show Xbox button prompts. Steam Input can remap PlayStation controllers for games that expect an Xbox layout.
  - q: "Why does my controller lag only on my ARM laptop?"
    a: >
      Bluetooth interference, Wi-Fi congestion, and power-saving settings are the main culprits. Use a wired USB connection to test, and if lag disappears, the problem is wireless, not the controller or the game.
  - q: "Can a failed BIOS update break controller support?"
    a: >
      A failed BIOS or firmware update can disable USB ports or Bluetooth radios, which breaks controllers. If problems started right after a firmware update, check the manufacturer's recovery steps first.
---
You plug in a controller, or pair it over Bluetooth, and your ARM laptop acts like nothing happened. The game shows keyboard prompts, Steam says no controller detected, or the controller connects and then drops out mid-match. On a Snapdragon laptop this is doubly annoying, because the machine handles everyday work beautifully — it is only when you try to play that the controller refuses to join in.

Most controller problems on Windows on ARM are not about the controller at all. They come from the layers between the hardware and the game: Bluetooth pairing state, USB drivers, the Xbox controller firmware, and the way older games talk to controllers through emulation. Each layer can fail independently, which is why a controller can work in one game and vanish in another.

The fixes below go layer by layer, starting with the connection itself and ending with game-specific settings. If your trouble began right after a firmware update, check [AI PC BIOS update failed](/articles/ai-pc-bios-update-failed/) first, since a bad firmware flash can knock out USB and Bluetooth together. And if your laptop's wireless is part of the problem, [Wi-Fi 7 router compatibility](/articles/wifi-7-router-compatibility-ai-laptop/) covers the networking side.

## Why this happens

- **Stale Bluetooth pairing:** A pairing saved before a Windows update can become corrupt, so the controller appears connected but sends no input.
- **Outdated controller firmware:** Old firmware may not negotiate correctly with the newer Bluetooth stack on ARM laptops.
- **USB driver or port fault:** A failed USB enumeration leaves wired controllers unrecognized even though the port charges other devices.
- **XInput versus DirectInput mismatch:** Older games expect one input API and ignore controllers that present the other.
- **Bluetooth interference:** Wi-Fi, wireless mice, and nearby devices crowd the 2.4 GHz band and cause dropouts and lag.
- **Power management suspending the radio:** Windows may power down the Bluetooth radio or USB hub during play to save battery.
- **Game or launcher overlay conflict:** Steam Input, Discord overlays, and other tools can claim the controller exclusively and hide it from the game.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test the controller wired first
A USB cable removes Bluetooth, wireless interference, and pairing state from the equation in one move. If the controller works wired, the hardware and drivers are fine and the problem lives in the wireless layer. If it fails wired too, you know to focus on drivers and game settings instead of chasing Bluetooth ghosts.
1. Connect the controller to the laptop with a USB-C or micro-USB cable, depending on the model.
2. Wait for Windows to play the device-connected sound and check Device Manager for the controller.
3. Open the Xbox Accessories app or a browser gamepad tester to confirm inputs register.
4. If wired works, skip to the Bluetooth fixes below — the controller itself is healthy.
5. If wired fails too, try a different cable and a different USB port before continuing.

### Fix 2: Remove and re-pair the Bluetooth connection
Bluetooth pairings go stale after Windows updates, and a corrupt pairing is the single most common cause of "connected but not working" controllers. Removing the device completely and pairing fresh clears the saved keys and forces a clean handshake, including a firmware capability exchange that a stale pairing skips.
1. Open Settings, go to Bluetooth and devices, and remove the controller from the device list.
2. On the controller, hold the pairing button until the light flashes rapidly.
3. In Settings, choose Add device, then Bluetooth, and select the controller when it appears.
4. Wait for the pairing to finish, then confirm the controller shows as Connected, not just Paired.
5. Test inputs immediately in the Xbox Accessories app before launching any game.
6. If pairing fails repeatedly, restart Bluetooth Support Service from the Services app and retry.

### Fix 3: Update the controller firmware
Controller firmware controls how the device identifies itself over USB and Bluetooth, and old firmware can mismatch the Windows on ARM Bluetooth stack. The Xbox Accessories app updates Xbox controllers over USB, and this one update fixes a surprising number of recognition and dropout problems that look like laptop faults.
1. Connect the controller to the laptop with a USB cable.
2. Open the Xbox Accessories app from the Microsoft Store and select the controller.
3. If an update is offered, install it and do not disconnect the controller until it finishes.
4. For PlayStation controllers, use the manufacturer's firmware updater on a PC if one is available.
5. After updating, re-pair over Bluetooth and test in a game that previously failed.
6. If your laptop's own firmware is suspect, the recovery steps in [AI PC BIOS update failed](/articles/ai-pc-bios-update-failed/) apply.

### Fix 4: Fix USB drivers and disable power saving
When wired controllers are not detected, the USB host driver or power management is usually at fault. Windows may also suspend USB hubs aggressively on ARM laptops to stretch battery life, which disconnects controllers mid-session. Reinstalling the USB controllers and disabling hub power saving stabilizes the connection without hurting battery life noticeably.
1. Open Device Manager and expand Universal Serial Bus controllers.
2. Right-click each USB Root Hub and choose Uninstall device, then restart the laptop.
3. Windows reinstalls the hubs on boot; reconnect the controller and check for recognition.
4. For each hub, open Properties, go to Power Management, and untick power saving.
5. In Device Manager, check Human Interface Devices for warning icons on the controller entry.
6. If the controller shows an error code, uninstall it from Device Manager and reconnect it to force a fresh driver install.

### Fix 5: Configure Steam Input and game controller settings
Steam Input is powerful, but it can also hide a controller from games by remapping it into a virtual device the game does not expect. Some games want the raw XInput device, others want Steam Input handling, and the wrong choice produces a controller that works in the Steam overlay but not in gameplay. Setting the per-game input mode explicitly ends that confusion.
1. In Steam, open Settings, Controller, and confirm your controller type is enabled.
2. Right-click the problem game, choose Properties, Controller, and try Enable Steam Input.
3. If that fails, switch the same setting to Disable Steam Input and relaunch the game.
4. For non-Steam games, check the game's own settings menu for controller type options.
5. Disable other controller tools, such as DS4Windows or reWASD, while testing to avoid conflicts.
6. Note that on-screen helper features can also misbehave after updates — see [Click to Do not showing](/articles/click-to-do-not-showing/) for a similar overlay-debugging pattern.

### Fix 6: Reduce Bluetooth interference and lag
Wireless lag and dropouts are usually environmental, not hardware faults. Bluetooth and Wi-Fi share the 2.4 GHz band, and a crowded room full of wireless devices can starve the controller's link. Moving the controller closer, switching the laptop's Wi-Fi to 5 GHz or 6 GHz, and removing competing devices often transforms a stuttering connection into a stable one.
1. Move closer to the laptop and remove objects between the controller and the machine.
2. Switch the laptop's Wi-Fi to a 5 GHz or 6 GHz network to free the 2.4 GHz band.
3. Turn off unused Bluetooth devices nearby, especially wireless headsets and mice.
4. If lag persists, play wired for competitive games and keep Bluetooth for casual play.
5. For persistent Wi-Fi trouble on AI laptops, see [Wi-Fi 7 router compatibility](/articles/wifi-7-router-compatibility-ai-laptop/) for router-side fixes.
6. Check for Windows updates, since Bluetooth stack improvements ship regularly for ARM devices.

## Closing

Controller trouble on an ARM laptop almost always traces back to pairing state, firmware, or a settings conflict rather than a broken controller. Test wired first to split the problem in half, then work through pairing, firmware, and input settings in order. Once you find the layer that was failing, the fix tends to stick — and you can get back to playing instead of troubleshooting. Microsoft's controller support pages are available at the [Windows support hub](https://support.microsoft.com/en-us/windows).
