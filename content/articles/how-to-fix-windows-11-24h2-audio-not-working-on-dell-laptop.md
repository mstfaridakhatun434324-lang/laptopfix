---
title: "No Sound After Windows 11 24H2 on a Dell Laptop: Getting Audio Back"
slug: how-to-fix-windows-11-24h2-audio-not-working-on-dell-laptop
date: 2026-09-06
categories: ["windows-update"]
tags: ["24h2", "audio not working", "dell laptop", "sound fix"]
description: "Windows 11 24H2 broke audio on your Dell laptop? Restore sound with the correct Realtek and Waves MaxxAudio driver sequence plus Windows audio repairs."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-audio-not-working-on-dell-laptop.webp"
faqs:
  - q: "Why does 24H2 break audio on Dell laptops specifically?"
    a: "Dell uses a customized Realtek audio stack with Waves MaxxAudio processing. The 24H2 update replaces that stack with a generic driver that lacks the MaxxAudio components, so the device loads but produces silence. Installing Dell's own audio package — which includes the MaxxAudio integration — restores the full chain and brings sound back."
  - q: "Should I use Dell SupportAssist or install drivers manually?"
    a: "Use SupportAssist first; it is the fastest path and picks the right package for your exact service tag. If SupportAssist itself is broken after the update, download the audio driver manually from the Dell support site. Manual installation gives you more control, but SupportAssist handles the driver order correctly on its own."
  - q: "My Dell shows no audio device at all after 24H2. Is it hardware?"
    a: "Almost certainly not. A missing audio device after a feature update points to a failed driver enumeration, not dead hardware. The device usually reappears after reinstalling the Dell audio driver or after Windows falls back to the basic High Definition Audio driver. Only suspect hardware if no driver version makes the device appear."
  - q: "Can I stop 24H2 from replacing my Dell audio driver again?"
    a: "Yes. After restoring Dell's driver, you can pause optional driver updates or use the show/hide updates tool to block the specific generic driver. Some users also disable driver updates via group policy on Pro editions. Blocking just the audio driver update keeps your sound stable while letting security updates flow normally."
---

Silence after Windows 11 24H2 is a signature Dell problem, and it has a signature cause: Dell's audio stack pairs Realtek hardware with Waves MaxxAudio processing, and the 24H2 update replaces that carefully matched combination with a generic driver. The generic driver loads, looks healthy in Device Manager, and produces absolutely nothing from the speakers.

The fix is almost always driver-layer, and it follows a specific order. Dell's packages expect the MaxxAudio components to be present, so installing things in the wrong sequence can leave you with sound that crackles or cuts out. Work through the steps below exactly as written — most Dell owners get sound back at Fix 3. If Windows Update is [failing to deliver driver updates](/articles/how-to-fix-driver-updates-failing-in-windows-update-after-windows-11-update/) at all, address that first, since a broken driver pipeline underlies many of these cases.

## Why this happens

- **Generic driver replaced the Dell stack:** 24H2 swapped Dell's Realtek plus MaxxAudio combination for a plain driver missing the processing components.
- **MaxxAudio service broken:** The Waves audio service that sits between the driver and the speakers failed to start under the new driver.
- **Audio endpoint mapping lost:** The update re-registered audio devices and the speaker endpoint ended up misconfigured.
- **SupportAssist audio check skipped:** The post-update driver reconciliation did not run, leaving the old MaxxAudio components orphaned.
- **Enhancement settings conflict:** Old enhancement profiles now point at components that no longer exist.
- **Default output switched:** The default playback device silently moved to an external monitor or disconnected output.
- **Audio service startup failure:** Windows Audio or the Endpoint Builder service did not start cleanly after the feature update.
- **BIOS audio setting reset:** Rare, but some Dell firmware resets the onboard audio controller state during major updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the basics

Rule out the simple causes before touching drivers.

1. Check the volume mixer — make sure the output is not muted and the level is up.
2. Right-click the speaker icon, open **Sound settings**, and confirm the internal speakers are the default output.
3. Press the test tone button — a working tone means the problem is application-level.
4. Plug in wired headphones: if they work but speakers do not, the speaker path specifically is broken.
5. Try a different program to confirm the silence is system-wide.

### Fix 2: Restart the audio services

Post-update service failures are quick to rule out.

1. Press Win + R, type `services.msc`, and press Enter.
2. Start **Windows Audio** and **Windows Audio Endpoint Builder** if they are stopped.
3. Set both services' startup type to **Automatic**.
4. Also check the **Waves Audio Services** entry — start it if present.
5. Restart the laptop and test.

### Fix 3: Install the Dell audio driver via SupportAssist

This is the fix that works for most Dell owners, because it installs the matched Realtek plus MaxxAudio package. Get the right package for your service tag from [Dell support](https://www.dell.com/support) if SupportAssist is unavailable.

1. Open **Dell SupportAssist** from the Start menu.
2. Run a full system scan and install all recommended driver updates, especially anything audio-related.
3. If SupportAssist is broken, go to the Dell support site, enter your service tag, and download the audio driver manually.
4. Install the driver package and restart when prompted.
5. Open the MaxxAudio app afterward and confirm it loads without errors.

### Fix 4: Reinstall MaxxAudio separately

Sometimes the Realtek driver is fine but the MaxxAudio layer is orphaned.

1. Open **Settings > Apps > Installed apps** and uninstall anything labeled MaxxAudio or Waves.
2. In Device Manager, uninstall the audio device under **Sound, video and game controllers** without deleting the driver.
3. Restart — Windows will reload the Dell audio driver.
4. Reinstall the MaxxAudio component from the Dell support site package.
5. Restart again and test the speakers.

### Fix 5: Disable enhancements and exclusive mode

Leftover enhancement hooks from the pre-24H2 stack can silence the new driver.

1. Open **Sound settings**, select your speakers, and open the device properties.
2. Disable all audio enhancements on the **Enhancements** tab.
3. On the **Advanced** tab, uncheck exclusive-mode access.
4. Set the default format to **24-bit, 48000 Hz** — a safe, widely supported setting.
5. Apply and test with the built-in tone.

### Fix 6: Run the Windows audio troubleshooter

Microsoft's tool handles endpoint registration failures well, as documented on the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Audio** troubleshooter.
3. Apply its recommended fixes.
4. Restart the laptop.
5. Test sound before reinstalling anything else.

### Fix 7: Clean-slate reinstall of the audio stack

For cases where every driver version stays silent, wipe the stack and rebuild it. If [driver updates keep failing in Windows Update](/articles/how-to-fix-driver-updates-keep-failing-windows-update-in-windows-11-24h2/), clear that problem before reinstalling, or the fresh driver will fail the same way.

1. In Device Manager, uninstall every device under **Sound, video and game controllers** and **Audio inputs and outputs**, deleting driver software each time.
2. Restart — Windows installs the basic High Definition Audio driver.
3. Test: if the basic driver produces sound, the hardware and bus are fine.
4. Install the Dell audio package from Fix 3 on top of the working basic driver.
5. Restart once more and confirm both speakers and MaxxAudio work.

## Closing

Dell's audio stack is a matched set — Realtek driver plus MaxxAudio processing — and 24H2 breaks it by replacing only half the equation with a generic part. The matched Dell package restores the whole chain, which is why SupportAssist or the Dell support site's driver page succeeds where generic driver updates fail. Work the list in order, test after each step, and remember that silence after a feature update is a software problem until proven otherwise — the speakers did not break overnight.
