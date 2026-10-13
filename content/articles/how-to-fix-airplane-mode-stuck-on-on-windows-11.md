---
title: "How to Fix Airplane Mode Stuck On in Windows 11"
slug: how-to-fix-airplane-mode-stuck-on-on-windows-11
date: 2026-09-26
categories: ["drivers"]
tags: ["airplane mode stuck", "windows 11", "wifi toggle greyed", "radio management", "network reset"]
description: "Airplane mode stuck on in Windows 11? Fix the greyed-out toggle with seven steps covering services, drivers, BIOS radios, and network resets."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on-on-windows-11.webp"
faqs:
  - q: "Why is the airplane mode button greyed out in Windows 11 Quick Settings?"
    a: "The Quick Settings toggle greys out when the Radio Management Service is not running, when Windows cannot detect a working Wi-Fi/Bluetooth radio (bad or missing driver), or when a hardware switch or BIOS setting has disabled the radios. Start the service and set it to Automatic, then check Device Manager for adapter errors. The Settings > Network & internet toggle sometimes works when Quick Settings is desynced."
  - q: "Did the Windows 11 24H2 update cause my airplane mode problem?"
    a: "It is a plausible trigger. 24H2 changed network-stack behavior and shipped Wi-Fi drivers that, on some Intel and MediaTek cards, misreport radio state — which locks the airplane toggle. If the problem started right after 24H2, reinstall the Wi-Fi driver from the laptop maker's site (not Windows Update's version), reset the network stack, and block driver updates until the channel stabilizes."
  - q: "Can I turn off airplane mode from the command line?"
    a: "There is no supported direct command — airplane mode is managed through the Radio Management Service and the Settings APIs, not a simple toggle command. What you can do from an elevated prompt is restart the underlying pieces: `netsh winsock reset` / `netsh int ip reset` for the stack, and `sc stop RmSvc` / `sc start RmSvc` to bounce the Radio Management Service (service name RmSvc). Then use the Settings toggle."
  - q: "Will a network reset delete anything important?"
    a: "A network reset removes saved Wi-Fi passwords, VPN configurations, virtual switches, and custom DNS/static-IP settings, then reinstalls all network adapters. It does not touch personal files, installed apps, or Windows settings outside networking. Export VPN profiles and note static IP configurations before resetting, then re-enter Wi-Fi passwords afterward."
---

Windows 11 moved the airplane mode toggle into Quick Settings, but the stuck-on failure is the same old beast: the toggle is greyed out or snaps back, Wi-Fi and Bluetooth stay dead, and the taskbar shows the airplane icon indefinitely. Underneath, the Radio Management Service owns this state — when it cannot control the radios, everything locks.

Windows 11-specific triggers include the 24H2 update's network-stack changes, Wi-Fi drivers that report the radio as unavailable after an update, and the new Quick Settings UI desyncing from the actual radio state (the toggle lies). The fix order below starts with the service and works outward to drivers, firmware, and full resets.

If the underlying Wi-Fi adapter has vanished rather than being switched off, start with [missing Wi-Fi diagnostics](/articles/wifi-disappeared-windows-11-no-wifi-option/); for wired-side issues, [Ethernet troubleshooting](/articles/how-to-fix-ethernet-not-working-on-laptop-in-windows-11-24h2/) covers the LAN side. Otherwise, proceed in order.

## Why this happens

- **Radio Management Service stopped** — The service that owns airplane state fails to start — the top cause, unchanged from Windows 10.
- **Wi-Fi driver reporting radio unavailable** — A bad driver makes Windows think no radio exists, so it locks the toggle.
- **Quick Settings UI desync** — The toggle display and the actual radio state disagree after updates or crashes.
- **Hardware radio switch / Fn key off** — Physical switches and Fn-key toggles override software on many laptops.
- **BIOS wireless disabled** — Firmware-level radio disable greys out every Windows toggle permanently.
- **Corrupt network stack (24H2)** — The 24H2 network changes can wedge radio management until reset.
- **Power policy parking the radio** — Modern Standby power policies can leave the radio in a pseudo-off state.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the Radio Management Service

Still the number-one fix on Windows 11. The service must be running.

If the service stops again after a reboot, look for third-party 'network optimizer' or debloat tools reverting it — some aggressively disable services Windows needs. Check Task Scheduler for scripts touching RmSvc, and review anything installed around the time the problem started. A service that will not stay running is being told to stop by something.

1. Press Win + R > `services.msc` > Enter.
2. Find **Radio Management Service** > double-click.
3. Set Startup type to **Automatic**, click **Start** (or Restart if already running).
4. Open Quick Settings (Win + A) and test the airplane toggle.

### Fix 2: Toggle via Settings instead of Quick Settings

Bypasses the Quick Settings UI desync — the Settings page talks to the radio service more directly.

1. Open Settings > Network & internet.
2. Use the **Airplane mode** toggle here instead of the Quick Settings panel.
3. If it works here but not in Quick Settings, the panel UI is desynced: restart Windows Explorer (Task Manager > Windows Explorer > Restart).
4. Retest both toggles after the Explorer restart.

### Fix 3: Reinstall the Wi-Fi and Bluetooth drivers

Drivers that misreport radio state lock the toggle. Refresh both radios' drivers.

Do the Wi-Fi and Bluetooth drivers as a pair even if only one radio seems affected: they often share a combo chip and a single driver package (Intel, MediaTek, Realtek), so a fault in one side's driver state can wedge the shared radio management. Reinstalling both guarantees the combo stack is coherent.

1. In Device Manager, uninstall the Wi-Fi adapter under Network adapters (do not delete the driver yet).
2. Uninstall the Bluetooth adapter under Bluetooth similarly.
3. Action > Scan for hardware changes, then update both drivers from the laptop maker's support site.
4. Restart and test the toggle. For Intel Wi-Fi, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) provides current drivers.

### Fix 4: Reset the network stack

Clears wedged radio-management and TCP/IP state in one pass.

Prefer the Settings-page network reset over the command line if you are unsure about syntax — both do the same job. Either way, screenshot your VPN configurations and static IP settings first; the reset wipes them and 'I forgot my VPN settings' is a painful second problem to have on top of the first.

1. Open Terminal/Command Prompt as administrator.
2. Run: `netsh winsock reset` and `netsh int ip reset`, then `ipconfig /flushdns`.
3. Restart the PC.
4. Alternatively: Settings > Network & internet > Advanced network settings > **Network reset**. Re-enter Wi-Fi passwords afterward.

### Fix 5: Check the hardware switch and BIOS

Firmware and hardware overrides beat every software fix. Rule them out.

1. Check for a physical wireless switch on the chassis and the Fn-key radio toggle (often Fn+F2).
2. Enter BIOS/UEFI and verify WLAN/Bluetooth are **Enabled** under wireless settings.
3. On some laptops, 'Wireless Switch' behavior in BIOS determines whether the OS can control radios — set it to OS control.
4. Save, boot, and test.

### Fix 6: Disable radio power management

Modern Standby aggressively parks radios; a stuck park looks identical to airplane mode.

1. In Device Manager > Wi-Fi adapter > Properties > Power Management: uncheck power-saving.
2. Settings > System > Power & battery > set power mode to **Best performance** while testing.
3. For Modern Standby machines, also check Settings > Bluetooth & devices for device-level power toggles.
4. Restart and verify the toggle stays responsive across sleep/wake.

### Fix 7: Use System Restore or repair install

When the toggle broke at a known update and nothing else helps, roll the system back.

1. Search Start for **Recovery** > Open System Restore > choose a restore point from before the problem.
2. If no restore point exists, consider an in-place repair install using the [Windows 11 download](https://www.microsoft.com/en-us/software-download/windows11) (keeps files and apps).
3. After recovery, immediately verify the toggle, then pause updates while you stabilize drivers.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents both procedures.

## Closing

On Windows 11 the stuck airplane toggle is still, at its core, a radio-management failure: the service, the drivers reporting radio state, or a hardware/firmware override. The service restart and the Settings-page toggle bypass fix most cases in minutes; the driver reinstall and network reset catch the update-triggered remainder.
