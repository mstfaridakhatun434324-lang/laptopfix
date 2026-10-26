---

title: "Photos Erase Object Not Working? How to Fix It on Windows 11"

slug: "photos-erase-object-not-working"

date: 2026-10-26

categories: ["ai-pc"]

tags: ["windows-11", "microsoft-photos", "ai-features", "copilot-plus-pc", "troubleshooting"]

description: "How to fix the Erase Object tool in Photos on your Windows 11 AI PC: check drivers, app updates and settings with this step-by-step troubleshooting guide."

thumbnail: "/images/thumbs/photos-erase-object-not-working.webp"

faqs:

  - q: "Why is the Erase Object tool in Photos not working on my AI laptop?"

    a: >

      Most often the cause is an outdated driver, an outdated app or a requirement that is not met, such as a Copilot+ PC, a signed-in account or a pending Windows update. Work through the driver and app checks in this guide before assuming the hardware is faulty, because software causes are far more common.

  - q: "Do I need a Copilot+ PC for the Erase Object tool in Photos?"

    a: >

      Many on-device AI features do need a Copilot+ PC with a qualifying NPU, while others run on any modern Windows 11 laptop using the CPU or GPU. Check the feature's requirements in the app and in Task Manager to see whether your NPU is present and active.

  - q: "Will reinstalling fix the Erase Object tool in Photos?"

    a: >

      Reinstalling helps when the app or driver installation itself is damaged, but it will not fix a missing requirement, an unsupported device or a driver problem. Try updating and repairing first, and keep a clean reinstall as a later step in this guide.

  - q: "When should I contact support about the Erase Object tool in Photos?"

    a: >

      Contact the laptop maker or app vendor if the NPU is missing from Device Manager after a clean driver reinstall, if a firmware update failed, or if the problem affects every AI feature at once. Note your driver versions and error messages first, since support will ask for them.

---



If the Erase Object tool in Photos has stopped working on your Windows 11 AI laptop, you are not alone, and the problem is usually fixable without replacing hardware or reinstalling Windows. Erase Object is meant to remove a passer-by, a sign or a stray cable with one brush stroke, so a greyed-out tool or an edit that never applies is immediately obvious. The good news is that most failures come from a short list of causes — drivers, app versions, settings and requirements — and each one has a straightforward check.

This feature is one of the reasons many people bought an AI laptop in the first place, because it promises to do in seconds work that used to take minutes of manual effort. When it fails, it is tempting to assume the laptop is faulty or the feature was marketing hype, but in practice the underlying hardware is rarely the problem. More often, a single update, driver or setting has drifted out of step with the rest of the system, and restoring that alignment brings the feature back.

This guide walks through the likely causes first, then works through fixes in order, from the quickest checks to a clean reinstall. Along the way you will also find related fixes, such as [ai laptop usb ports not working](/articles/ai-laptop-usb-ports-not-working/) and [ai pc factory reset stuck](/articles/ai-pc-factory-reset-stuck/), which cover neighbouring AI features that share the same drivers and settings. Follow the steps in order, testing after each one, so you know exactly which fix solved it.

## Why this happens

- **Outdated app version:** AI features in Microsoft Photos arrive through Store updates, so an older build may simply not contain the Erase Object tool in Photos yet, or may contain a buggy early version of it.

- **NPU or graphics driver problem:** the Erase Object tool in Photos often runs on the NPU or GPU, so a missing, outdated or corrupted driver can make the feature fail silently or grey out entirely.

- **Hardware or account requirement not met:** Many AI features need a Copilot+ PC with a qualifying NPU, a signed-in Microsoft account and sometimes a specific region or language setting.

- **Corrupted app cache or settings:** A damaged cache, a stuck background process or a bad settings file can break one feature while the rest of Microsoft Photos keeps working normally.

- **Unsupported image or file:** Very large images, unusual formats or files stored in a restricted location can stop the Erase Object tool in Photos from processing even when the feature itself is healthy.

- **Pending Windows update:** AI features depend on Windows components that ship with feature updates, so a laptop behind on updates may lack the runtime the feature needs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Update the app from the Microsoft Store

Start with the simplest cause: an outdated Microsoft Photos. Store updates deliver AI features and their fixes, and a laptop that has not updated the app in weeks is a common culprit.

1. Open the Microsoft Store and go to Downloads and updates.

2. Check for updates and install any available update for Microsoft Photos.

3. Restart Microsoft Photos and try the Erase Object tool in Photos again.

4. If no update appears, confirm you are signed in with your usual Microsoft account.

5. Retry the feature on a small test image to rule out file problems.

### Fix 2: Update your NPU and graphics drivers

Because the Erase Object tool in Photos leans on accelerated hardware, stale drivers are the next thing to rule out. Use the laptop maker's support page or Windows Update rather than a random driver site. Microsoft's own guidance at [Microsoft Windows support](https://support.microsoft.com/en-us/windows) is a good cross-check for the steps below.

1. Open Device Manager and expand Neural processors and Display adapters.

2. Right-click each device and choose Update driver, then Search automatically.

3. Also check Windows Update for optional driver updates.

4. Restart the laptop after any driver change.

5. Test the Erase Object tool in Photos again and note whether the error changed.

### Fix 3: Repair or reset the app

When the app itself is damaged, repair keeps your files while fixing broken components, and reset goes further by clearing its settings. Try repair first.

1. Open Settings, then Apps, then Installed apps.

2. Find Microsoft Photos, open its advanced options and choose Repair.

3. Test the Erase Object tool in Photos; if it still fails, return and choose Reset.

4. Reopen Microsoft Photos and sign in again if prompted.

5. Try the feature on a fresh photo to confirm the fix.

### Fix 4: Check requirements, account and region

Some AI features are gated by hardware, account or region, and no amount of reinstalling will unlock a feature your laptop or account is not eligible for yet.

1. Confirm your laptop is a Copilot+ PC with a qualifying NPU in Task Manager.

2. Sign in to Microsoft Photos with your Microsoft account.

3. Check Settings, then Time and language, and confirm your region and language are supported.

4. Install any pending Windows feature update.

5. Reopen Microsoft Photos and check whether the feature is now available.

### Fix 5: Clear the cache and test with a clean file

A single corrupted image or a bloated cache can masquerade as a broken feature, so isolating the file from the feature saves a lot of wasted reinstalling. For driver downloads, stick to the official vendor or laptop-maker pages linked in this guide rather than third-party driver sites.

1. Close Microsoft Photos completely from Task Manager.

2. Copy a small JPG photo to your Desktop as a test file.

3. Open the test photo in Microsoft Photos and try the Erase Object tool in Photos on it.

4. If it works, the original file or location was the problem.

5. If it fails too, move on to a full reinstall of the app.

### Fix 6: Reinstall the app and update Windows

If nothing else worked, a clean reinstall removes damaged components that repair cannot reach, and a current Windows build supplies the runtimes AI features need.

1. Uninstall Microsoft Photos from Settings, then Apps.

2. Restart the laptop before reinstalling.

3. Reinstall Microsoft Photos from the Microsoft Store.

4. Install all pending Windows updates and restart again.

5. Open Microsoft Photos and verify the Erase Object tool in Photos works end to end.

## Closing

Once the Erase Object tool in Photos is working again, keep it that way by installing app and driver updates promptly, staying on a current Windows build and checking Task Manager if performance ever slips. If a future update breaks it again, you now know which checks to repeat first. For a related older fix, see [live captions netflix app not working](/articles/live-captions-netflix-app-not-working/), and if the problem persists across every AI feature, treat that as a sign to check drivers and firmware as a whole rather than one app at a time.
