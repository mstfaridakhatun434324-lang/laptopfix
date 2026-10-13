---
title: "ELAN Touchpad Not Working on a Laptop? What to Do"
slug: what-to-do-if-elan-touchpad-not-working
date: 2026-09-28
categories: ["drivers"]
tags: ["elan touchpad", "touchpad not working", "elantech", "precision touchpad", "cursor frozen"]
description: "ELAN touchpad dead on your laptop? Fix driver conflicts, re-enable the device, and resolve the ELAN vs precision touchpad battle."
thumbnail: "/images/thumbs/what-to-do-if-elan-touchpad-not-working.webp"
faqs:
  - q: "What is the difference between ELAN and precision touchpads?"
    a: "ELAN (Elantech) touchpads use the manufacturer's proprietary driver with its own control panel and gesture engine. Precision touchpads use Microsoft's standardized driver built into Windows, with settings in the Windows Settings app. Many laptops can run either, and conflicts between the two driver models are a leading cause of touchpad failures."
  - q: "Why did my ELAN touchpad stop working after a Windows update?"
    a: "Windows Update frequently replaces the ELAN driver with Microsoft's precision touchpad driver or a generic PS/2 mouse driver. The ELAN hardware may not fully cooperate with the replacement, leaving you with a dead or half-functional touchpad. Reinstalling the OEM ELAN driver for your exact model restores full function."
  - q: "My touchpad works but gestures don't. Is that a driver issue?"
    a: "Almost certainly. Basic cursor movement can work through the generic PS/2 fallback driver while multi-finger gestures need the full ELAN driver. If movement works but two-finger scroll, pinch zoom, and three-finger gestures don't, the ELAN driver isn't properly installed — reinstall the OEM package."
  - q: "Can I switch from ELAN to precision touchpad drivers?"
    a: "On some laptops, yes — if the hardware supports Microsoft's precision driver model, you can sometimes force it. But it's model-dependent and can be fiddly. Unless you have a specific reason to switch, the reliable path is keeping the OEM ELAN driver that the laptop was designed and validated with."
---

ELAN touchpads occupy a special place in Windows laptop frustration. The hardware is fine — Elantech makes perfectly good touchpads — but the driver situation is a tug-of-war between ELAN's proprietary driver and Microsoft's precision touchpad standard. Windows Update loves to "upgrade" you from one to the other, and the touchpad is what suffers.

The symptoms vary: completely dead touchpad, cursor moves but no gestures, touchpad works until sleep then dies, or the touchpad vanishes from Device Manager. All of them trace back to driver state. Fix the driver state and the touchpad comes back.

## Why this happens

- **Windows Update replaced the ELAN driver:** The top cause — Microsoft's driver doesn't fully drive ELAN hardware.
- **ELAN driver corrupted:** Partial updates leave the driver in a broken state with no gestures or no function.
- **Touchpad disabled via Fn key:** Most laptops have an Fn key toggle (often F6/F7/F9) that disables the touchpad with no obvious indicator.
- **Disabled in BIOS or Windows settings:** The touchpad can be switched off in BIOS or in Settings → Bluetooth & devices → Touchpad.
- **"Disable touchpad when mouse connected" setting:** USB mouse insertion auto-disables the touchpad on many laptops.
- **ELAN service not running:** The ELAN background service (ETDService) must run for full functionality.
- **Conflicting precision driver remnants:** Leftover files from driver-model switches cause conflicts.
- **Hardware failure:** Worn touchpad cable or failed controller, usually after liquid damage.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the Fn key toggle and Windows setting

1. Press the touchpad **Fn key** (look for the touchpad icon, commonly F5–F9) — press it once and test, since there's often no on-screen feedback.
2. Go to **Settings → Bluetooth & devices → Touchpad** and confirm the Touchpad toggle is **On**.
3. Uncheck **"Leave touchpad on when a mouse is connected"** confusion: if it's enabled to disable with mouse, unplug your USB mouse and test.
4. This resolves an embarrassing share of "dead touchpad" reports — always check before doing driver surgery.

### Fix 2: Verify the touchpad in Device Manager

1. Open **Device Manager** and expand **Human Interface Devices** and **Mice and other pointing devices**.
2. Look for **ELAN Input Device**, **ELAN Touchpad**, or similar. Note whether it's present, disabled (down arrow), or warning-flagged.
3. If disabled, right-click → **Enable device**. If missing entirely, click **View → Show hidden devices** and look again.
4. A touchpad appearing only as "PS/2 Compatible Mouse" means the ELAN driver isn't loaded — the generic fallback gives basic movement but no gestures.

### Fix 3: Restart the ELAN service

1. Press **Win + R**, type `services.msc`, and find **ELAN Service** or **ETDService**.
2. Set **Startup type** to **Automatic** and click **Start** (or Restart).
3. Also check Task Manager → Startup apps for disabled ELAN entries and re-enable them.
4. Test gestures immediately — the service handles the advanced features, so its absence specifically kills multi-finger input.

### Fix 4: Reinstall the OEM ELAN driver

1. Download the touchpad driver for your exact model from the manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) — look for "Elantech" or "Touchpad" under Input.
2. In Device Manager, uninstall the touchpad/ELAN device, checking "delete the driver software."
3. Install the downloaded package as Administrator and reboot.
4. Verify in Settings → Bluetooth & devices → Touchpad that full gesture options appear — their presence confirms the ELAN driver loaded. The [Synaptics touchpad guide](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/) covers the rival driver with the same methodology.

### Fix 5: Block Windows from replacing the driver again

1. After the OEM driver works, open **Device Installation Settings** (System → About → Advanced system settings → Hardware) and set it to **No**.
2. On Pro editions, enable **"Do not include drivers with Windows Updates"** in Group Policy.
3. Without this, the next update can reinstall Microsoft's driver and you'll repeat this entire process — the ELAN/Windows Update war is perennial.
4. Check the driver version monthly against the OEM page instead, updating manually when a genuinely new version appears.

### Fix 6: Check BIOS and test in a clean environment

1. Enter **BIOS/UEFI** and look for a **Touchpad** or **Internal Pointing Device** option — ensure it's Enabled.
2. Boot into **Safe Mode**: if the touchpad works there, a third-party driver or startup app is interfering.
3. Test with a Linux live USB — working touchpad in Linux proves hardware health and isolates the problem to Windows drivers.
4. If the touchpad is dead in BIOS diagnostics too (many makers include a touchpad test), it's hardware.

### Fix 7: Clean out driver-model conflict remnants

1. If the laptop previously ran precision drivers, uninstall all touchpad drivers in Device Manager with "delete driver software" checked.
2. In **Settings → Apps**, remove any ELAN or precision touchpad utilities.
3. Run the Fix 4 OEM install on the clean slate — mixed remnants are what cause the "installed the driver five times" loop.
4. After reinstalling, avoid third-party "driver updater" tools entirely; they're a leading cause of ELAN breakage, as seen with [other driver conflicts](/articles/how-to-fix-synaptics-touchpad-not-working-on-lenovo-laptop/).

### Fix 8: Diagnose hardware failure

1. Press firmly (not hard) around the touchpad while testing — intermittent function indicates a loose ribbon cable.
2. Check for physical damage: swelling battery underneath can press against the touchpad and kill it — a swollen battery is also a safety issue, stop using the laptop if you suspect this.
3. Liquid spills near the palm rest frequently kill touchpads while leaving everything else working.
4. Touchpad replacement parts are model-specific but usually affordable; under warranty, it's a standard repair.

## Closing

ELAN touchpad failures are driver-model wars, not hardware deaths. Check the Fn toggle, reinstall the OEM ELAN driver, block Windows Update from "fixing" it, and the touchpad stays working. The hardware is almost never the problem. The one habit that prevents recurrence: after every major Windows feature update, open Device Manager and glance at the touchpad entry — catching a driver swap early, before it fully breaks, means a two-minute rollback instead of another full troubleshooting session.
