---
title: "5G WWAN Not Working on Snapdragon Laptops: How to Fix It"
slug: 5g-wwan-not-working-snapdragon-laptop
date: 2026-10-23
categories: ["ai-pc"]
tags: ["5g", "wwan", "snapdragon laptop", "cellular data", "modem driver", "troubleshooting"]
description: "Fix 5G WWAN not working on Snapdragon laptops: diagnose signal vs. driver issues, repair the modem driver, fix APN settings, and reset the network stack."
thumbnail: "/images/thumbs/5g-wwan-not-working-snapdragon-laptop.webp"
faqs:
  - q: "Why does my Snapdragon laptop show 5G but have no internet?"
    a: "The modem can register on the 5G network without a working data path. The usual causes are a wrong or missing APN, a carrier plan that doesn't include laptop data, or a modem driver problem. Check the APN first, then the driver."
  - q: "How do I know if the problem is signal or software?"
    a: "Open Settings > Network & internet > Cellular and look at the signal indicator. Strong signal with no data points to APN, plan, or driver issues. No signal at all points to antenna, SIM/eSIM, or modem hardware problems."
  - q: "Does 5G drain the laptop battery faster?"
    a: "Yes, measurably — the 5G modem is one of the hungrier components. If battery life matters more than speed on a given day, dropping to 4G/LTE in the cellular settings noticeably reduces drain."
  - q: "Can a Windows update break the 5G modem?"
    a: "Yes. Windows Update can replace the OEM Qualcomm modem driver with a generic version that breaks 5G bands or drops the connection. Reinstalling the modem driver from your laptop maker fixes it."
---

Your Snapdragon laptop shows a 5G icon — or worse, shows nothing at all — but pages will not load over cellular. WWAN (wireless wide area network) on these machines runs through the integrated Snapdragon modem, and the failure can sit anywhere from the cell tower to the driver to your data plan.

The tricky part of WWAN troubleshooting is separating signal problems from software problems. A laptop with no signal in a basement is not broken; a laptop with full bars and no internet has a configuration or driver issue. This guide helps you tell the difference, then fixes each case in order.

You will work through six fixes: signal and plan checks first, then APN and driver repair, then full resets. Keep your carrier's support number handy — half of WWAN issues need something changed on their side.

## Why this happens

- **No 5G coverage at your location:** The modem can only use what the tower offers. Indoors or in rural areas, the laptop may cling to a weak 5G signal or drop to LTE — or show nothing if coverage is absent.
- **Wrong or missing APN:** The access point name routes your data through the carrier's network. A wrong APN gives you signal bars with zero internet — the classic "connected, no internet" on cellular.
- **Data plan does not include the laptop:** Some plans are phone-only, data-capped, or suspended. The modem registers fine, but the carrier refuses data sessions.
- **Corrupted or outdated modem driver:** The Qualcomm modem driver translates between Windows and the cellular hardware. A generic or corrupted driver breaks bands, drops connections, or hides the Cellular page entirely.
- **eSIM profile problem:** A failed or expired eSIM profile leaves the modem with nothing to authenticate against — the same provisioning class of failure that affects [eSIM setup on Snapdragon laptops](/articles/esim-not-working-snapdragon-laptop/).
- **Antenna or modem hardware fault:** The cellular antennas run through the display lid and hinges. Physical damage or a loose antenna cable produces weak or absent signal regardless of software.
- **Aggressive power saving killing the modem:** Windows can power-gate the modem during sleep or on battery, and a modem that never wakes properly shows as connected-but-dead after resume.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check signal, location, and the data plan

Start with the physical layer: signal and account. No amount of driver surgery fixes a dead zone or a suspended plan.

1. Open **Settings > Network & internet > Cellular** and note the signal strength indicator and the network type shown (5G, LTE, or nothing).
2. Move near a window or step outside and watch whether the signal improves — a big change means coverage, not the laptop, is the problem.
3. Confirm **Cellular data** is toggled on and **Airplane mode** is off; also check the physical airplane-mode key on the keyboard.
4. Log in to your carrier's account portal (over Wi-Fi) and confirm the plan is active, has data remaining, and includes laptop/tablet data — not phone-only.
5. If the carrier shows the line suspended, capped, or provisioned for the wrong device type, nothing on the laptop will help until they fix the account side.

### Fix 2: Force the right network mode and reset the data session

A modem stuck on the wrong network mode — clinging to a dying 5G signal instead of usable LTE — looks like a total failure. Forcing the mode breaks the deadlock.

1. In **Cellular > Advanced options** (select your profile), look for **Network type** or **Preferred network** settings if your driver exposes them.
2. If 5G is unusable at your location, try forcing **4G/LTE only** — a stable LTE connection beats a flapping 5G one every time.
3. Toggle **Cellular data** off, wait 30 seconds, and toggle it back on to force a fresh data session with the tower.
4. Toggle **Airplane mode** on for 30 seconds, then off — this re-registers the modem on the network from scratch, clearing stuck sessions.
5. Test with a browser. If data flows on LTE but not 5G, your location's 5G is the problem; leave the mode on LTE until coverage improves.

### Fix 3: Verify and correct the APN

Signal with no internet is the APN's signature. Carriers occasionally change APNs, and Windows sometimes provisions the wrong one automatically.

1. In **Cellular > Advanced options**, open the **APN settings** for your active profile.
2. Get the current Windows-laptop APN from your carrier's support site or support line — do not guess, and do not reuse a phone APN unless they confirm it.
3. If the APN field is empty or wrong, add or edit it with the exact APN, username, password, and authentication type the carrier specifies.
4. Save, then toggle cellular data off and on to force the modem to re-establish the data bearer with the new APN.
5. Browse to confirm. If data works now, the APN was the entire issue — a five-minute fix for what felt like a hardware failure.

### Fix 4: Reinstall the Qualcomm modem driver

When the Cellular page misbehaves, options are greyed out, or connections drop constantly, the modem driver is suspect. Windows Update is a frequent culprit, replacing the OEM's validated Qualcomm driver with a generic one.

1. Open **Device Manager > Network adapters** and find the Qualcomm modem/WWAN device; check for yellow warnings and note any error codes.
2. Download the WWAN/cellular driver package for your exact model from [Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en), or [Dell](https://www.dell.com/support/).
3. Right-click the modem, choose **Uninstall device** with **"Attempt to remove the driver for this device"** checked, then restart.
4. Run the OEM modem installer as administrator and restart again when prompted.
5. Recheck the Cellular settings page — all options should be present — and test the connection. The same driver-hygiene principle that keeps [local AI runtimes using the right accelerator](/articles/pytorch-directml-npu-not-used/) applies here: the correct vendor driver matters more than the newest generic one.

### Fix 5: Disable modem power management and test after sleep

A modem that works after boot but dies after sleep is being power-gated and never waking. This is especially common on battery, where Windows is aggressive about suspending radios.

1. In Device Manager, find the modem under **Network adapters**, open **Properties > Power Management**, and uncheck **"Allow the computer to turn off this device to save power"**.
2. In **Settings > System > Power & battery**, set **Power mode** to **Best performance** temporarily for testing.
3. Put the laptop to sleep for a minute, wake it, and immediately test cellular data — if it is dead until a reboot, power management is confirmed as the cause.
4. Check your maker's control app (Lenovo Vantage, MyASUS, etc.) for its own radio power-saving settings and disable aggressive modem sleeping there too.
5. Once confirmed working, you can return the power mode to Balanced — the Device Manager power-management change is the one that matters.

### Fix 6: Full network reset and carrier-side reprovisioning

When everything above fails, reset the entire network stack and have the carrier reprovision the line — this clears corruption on both sides at once.

1. Go to **Settings > Network & internet > Advanced network settings > Network reset**, click **Reset now**, and let the laptop restart.
2. Reconnect to Wi-Fi, then re-add your eSIM profile or reinsert the physical SIM, and re-enter the APN from Fix 3.
3. Call your carrier and ask them to reprovision the line and confirm the IMEI/ICCID they have on file matches your laptop — mismatches silently break data.
4. While on the call, ask them to check for tower-side issues or maintenance in your area.
5. As a last hardware check, compare signal with another cellular device in the same spot — and note that unrelated startup features like [auto-starting captions at boot](/articles/live-captions-auto-start-boot/) have no bearing on WWAN; likewise, [Java JDK install issues on ARM](/articles/java-jdk-arm-windows-install/) are a separate developer-tools track, not a modem symptom. If your laptop alone shows no signal where a phone shows full bars, the antenna or modem hardware needs professional service.

## Closing

5G WWAN failures on Snapdragon laptops split cleanly into signal problems and software problems — diagnose which one you have before touching anything. Check coverage and the data plan first, fix the APN second, reinstall the OEM modem driver third, and get the carrier to reprovision the line before concluding the hardware is at fault.
