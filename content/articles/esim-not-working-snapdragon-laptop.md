---
title: "eSIM Not Working on Snapdragon Laptops: How to Fix It"
slug: esim-not-working-snapdragon-laptop
date: 2026-10-23
categories: ["ai-pc"]
tags: ["esim", "snapdragon laptop", "cellular", "wwan", "windows 11", "troubleshooting"]
description: "Fix eSIM not working on Snapdragon laptops: add your eSIM profile correctly, repair the cellular driver, and reset network settings step by step."
thumbnail: "/images/thumbs/esim-not-working-snapdragon-laptop.webp"
faqs:
  - q: "Why won't my Snapdragon laptop detect the eSIM profile?"
    a: "The eSIM profile may not have downloaded correctly, the cellular modem driver may be broken, or the laptop's eSIM may be locked to a different carrier. Re-adding the profile after a network reset fixes most download failures."
  - q: "Does my carrier need to support eSIM for laptops?"
    a: "Yes. Not every carrier supports eSIM on Windows devices, and some only support phones. Check with your carrier that they offer eSIM activation for Windows laptops specifically before troubleshooting further."
  - q: "Can I use eSIM and Wi-Fi at the same time?"
    a: "Yes — Windows 11 can keep both active, using cellular as a fallback or primary connection. In Settings > Network & internet > Cellular you can choose which connection Windows prefers."
  - q: "Will a Windows reset delete my eSIM profile?"
    a: "A standard 'keep my files' reset preserves eSIM profiles, but a full clean install removes them. Always note down your carrier's activation details or QR code before reinstalling Windows."
---

Your Snapdragon laptop has an eSIM, your carrier sent you a QR code, but Settings > Network & internet > Cellular shows no profile — or the profile is there and stubbornly refuses to connect. Cellular on Windows laptops is a three-way handshake between the eSIM chip, the modem driver, and your carrier's provisioning, and any one of them can stall.

Snapdragon laptops (Surface Pro, ThinkPad, and other Copilot+ machines with 5G) integrate the modem into the platform, which means cellular depends on Qualcomm's modem driver stack working perfectly. The good news is that eSIM problems are almost always configuration or driver issues, not broken hardware.

This guide walks you through six fixes in order: profile and carrier checks first, then driver repair, then full network resets. Have your carrier's activation details or QR code ready before you start.

## Why this happens

- **eSIM profile download failed or is incomplete:** The profile download needs a stable internet connection (Wi-Fi) during setup. An interrupted download leaves a corrupt or missing profile that cannot connect.
- **Carrier does not support Windows eSIM:** Some carriers only provision eSIM for phones. If your carrier has no Windows laptop eSIM support, activation fails no matter what you do on the laptop.
- **Cellular modem driver missing or broken:** The Snapdragon modem needs its driver to expose the eSIM to Windows. A generic or corrupted modem driver makes the entire Cellular page misbehave.
- **Airplane mode or cellular data toggle off:** The obvious one — Windows has separate toggles for airplane mode, cellular, and data roaming, and any of them can silently block the connection.
- **APN settings wrong or missing:** Some carriers need manual APN configuration. An empty or incorrect APN lets the eSIM register on the network but never pass data.
- **Windows package or servicing corruption:** Cellular provisioning touches deep OS components. Corruption in the underlying servicing stack can break eSIM management — the same class of breakage that stops [winget packages from installing](/articles/winget-arm-packages-not-installing/).
- **eSIM locked or profile limit reached:** The eSIM chip holds a limited number of profiles, and carrier locks can block other carriers' profiles entirely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify carrier support and the profile basics

Half of all eSIM failures are provisioning problems, not laptop problems. Confirm the carrier side is correct before touching the machine.

1. Contact your carrier (or check their support pages) and confirm they support eSIM activation on Windows laptops — not just phones.
2. Ask whether your eSIM is already activated on their side and whether your plan includes data on a laptop device type.
3. In **Settings > Network & internet > Cellular**, check whether any eSIM profile is listed at all — "No eSIM profiles" versus a profile that will not connect are different problems with different fixes.
4. Confirm the laptop is not in **Airplane mode** and that **Cellular data** is toggled on in the Cellular settings page.
5. If the carrier confirms everything on their side but no profile appears, delete any partial profile shown and prepare to re-add it cleanly in Fix 3.

### Fix 2: Re-add the eSIM profile on stable Wi-Fi

Profile downloads fail silently on flaky connections. Deleting the broken profile and re-adding it over a solid Wi-Fi connection resolves most provisioning failures.

1. Connect to a stable Wi-Fi network — do not attempt profile downloads over a weak or captive-portal connection.
2. In **Settings > Network & internet > Cellular**, select the broken or partial profile and choose **Delete** (or **Remove**).
3. Restart the laptop so the eSIM chip clears its cached provisioning state.
4. Go back to **Cellular** and choose **Add eSIM** (or **Add a profile**), then scan your carrier's QR code or enter the activation code manually.
5. Wait for the download to complete without letting the laptop sleep, then confirm the profile shows as active. If the download fails twice, ask the carrier for a fresh QR code — codes can expire or be single-use.

### Fix 3: Check APN settings and data roaming

A profile that registers on the network but shows "No internet" or connects without data is usually an APN problem. The carrier's access point name tells the modem how to route data.

1. In **Settings > Network & internet > Cellular > Advanced options** (select your profile), find the **APN settings** section.
2. Compare the APN against the one your carrier publishes for Windows devices — carriers sometimes use a different APN for laptops than for phones.
3. If the APN is empty or wrong, choose **Add an APN** (or Edit) and enter the carrier's APN exactly, including any username, password, or authentication type they specify.
4. Toggle **Data roaming** on if you are outside your carrier's home network — some eSIM profiles require it even in borderline coverage areas.
5. Toggle **Cellular data** off and on, then test with the browser. Data flowing now means the APN was the whole problem.

### Fix 4: Repair the cellular modem driver

If the Cellular page itself is broken — missing options, greyed-out toggles, or no modem detected — the Qualcomm modem driver is the suspect. Corrupt driver stacks tend to fail in clusters — the same class of breakage that hides the NPU from [AI toolkit integrations in VS Code](/articles/ai-toolkit-vscode-npu-not-detected/). This is a driver repair like any other, and Windows documents the general approach on [Windows support](https://support.microsoft.com/en-us/windows).

1. Open **Device Manager** and expand **Network adapters** — look for the Qualcomm cellular/modem device (often "Qualcomm Snapdragon X" modem or similar).
2. If it shows a yellow warning, right-click, open **Properties**, and note the error code.
3. Download the cellular/WWAN driver for your exact model from [Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en), or [Dell](https://www.dell.com/support/) — it is usually bundled under Network or Chipset drivers.
4. Right-click the modem in Device Manager, choose **Uninstall device** with **"Attempt to remove the driver for this device"** checked, restart, then run the OEM installer as administrator.
5. After the restart, recheck **Settings > Network & internet > Cellular** — the modem and eSIM options should now appear correctly.

### Fix 5: Reset network settings and re-provision

When individual fixes fail, a full network reset clears corrupted cellular state across the whole stack — profiles, APNs, and cached modem configuration — so you can start clean.

1. In **Settings > Network & internet > Advanced network settings > Network reset**, click **Reset now** and confirm. The laptop will restart.
2. After the restart, reconnect to Wi-Fi first — you need internet to re-download the eSIM profile.
3. Re-add the eSIM profile using your carrier's QR code or activation code, exactly as in Fix 2.
4. Re-enter the APN settings from Fix 3 if your carrier requires a manual APN.
5. Test the connection. A network reset also clears saved Wi-Fi networks and VPN settings, so expect to reconfigure those afterward.

### Fix 6: Check profile limits, carrier lock, and privacy settings

A few remaining blockers live outside the normal troubleshooting path: a full eSIM chip, a carrier lock, or privacy settings that gate cellular provisioning.

1. In **Cellular** settings, count stored eSIM profiles — the chip typically holds only a handful. Delete profiles you no longer use to free space.
2. If your laptop was bought through a carrier, check whether it is carrier-locked: try (or ask the carrier about) a profile from a different carrier. A locked device rejects foreign profiles.
3. Review **Settings > Privacy & security** for anything restricting cellular or location services your carrier's provisioning app might need.
4. The same privacy-settings hygiene that fixes [AI feature blocks](/articles/click-to-do-privacy-settings-fix/) applies here — overly aggressive privacy toggles can silently break provisioning flows.
5. If the modem is healthy, the profile downloads, the APN is right, and data still will not flow, the modem hardware or SIM circuitry may have failed — contact your laptop maker's support, and keep your carrier's ticket open in parallel since the fault could be on their provisioning side.

## Closing

eSIM failures on Snapdragon laptops are provisioning puzzles more often than hardware failures: carrier support, a clean profile download, the right APN, and a healthy modem driver. Work the carrier side and the laptop side in parallel, re-add the profile over stable Wi-Fi, and repair the modem driver before assuming anything is broken.
