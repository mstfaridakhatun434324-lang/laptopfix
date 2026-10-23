---
title: "How to Fix OneNote Copilot Not Working on Windows 11"
slug: onenote-copilot-not-working
date: 2026-10-23
categories: ["ai-pc"]
tags: ["onenote", "copilot", "microsoft 365", "windows 11", "notes", "troubleshooting"]
description: "Fix OneNote Copilot not working on Windows 11 with step-by-step checks for licensing, app version, notebook location, admin policies, and sync issues."
thumbnail: "/images/thumbs/onenote-copilot-not-working.webp"
faqs:
  - q: "Why is Copilot not showing up in my OneNote?"
    a: "The usual causes are a missing Microsoft 365 Copilot license, using an outdated OneNote app, or notebooks stored locally instead of on OneDrive or SharePoint. Copilot in OneNote only works with cloud-hosted notebooks and a licensed account."
  - q: "Does Copilot work in OneNote for Windows 10?"
    a: "Copilot features are rolling out in the unified OneNote app on Windows 11 and OneNote on the web. The legacy OneNote for Windows 10 app is in maintenance mode and does not receive new Copilot features — switch to the current OneNote app."
  - q: "Do my notebooks need to be on OneDrive for Copilot to work?"
    a: "Yes. Copilot in OneNote reads and summarizes your notes through the Microsoft 365 cloud, so notebooks stored only on your local drive are invisible to it. Move them to OneDrive or SharePoint to unlock Copilot."
  - q: "Is OneNote Copilot an NPU feature on Copilot+ PCs?"
    a: "No. Like the rest of Microsoft 365 Copilot, it runs in Microsoft's cloud rather than on your laptop's NPU. A Copilot+ PC does not change the requirements — licensing, the app version, and cloud notebooks are what matter."
---

You open OneNote on your new AI laptop, select a page of meeting notes, and look for the Copilot button that should summarize, rewrite, or answer questions about your notes — but it is grayed out, missing, or throws an error when you click it. Your Microsoft 365 subscription is paid up, Copilot works in Word, yet OneNote refuses to cooperate.

On Windows 11 Copilot+ PCs this is doubly frustrating because OneNote feels like the natural home for AI assistance. But Copilot in OneNote is a cloud service with strict prerequisites: the right license, the current unified OneNote app, notebooks stored in the cloud, and an admin policy that allows it. Miss any one of those and the feature silently fails.

This guide gives you six fixes in technician order: license and account first, then the app itself, then notebook location and sync, then policies. Work through them in sequence and test Copilot after each step.

## Why this happens

- **No Copilot license on the signed-in account:** Copilot in OneNote requires a Microsoft 365 Copilot (work/school) or Copilot Pro (personal) license. Without it, the button never appears.
- **Legacy OneNote for Windows 10 app:** The old OneNote for Windows 10 is in maintenance mode and never received Copilot. Only the unified OneNote app (formerly "OneNote for Microsoft 365") gets the feature.
- **Notebooks stored locally:** Copilot processes your notes in the Microsoft 365 cloud. Notebooks that live only on your hard drive are invisible to it, so Copilot stays disabled on those pages.
- **Outdated OneNote build:** Copilot in OneNote rolled out progressively. An outdated build may predate the feature entirely or carry a broken early implementation.
- **Admin policy blocking Copilot:** Microsoft 365 admins can disable Copilot per app, and OneNote is commonly included in those restrictions in regulated industries.
- **Sync or sign-in corruption:** A half-signed-in state or stuck sync can leave OneNote thinking you are unlicensed. The UI shows no license error — Copilot just does nothing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the license on the account OneNote is using

Copilot in OneNote checks your license every time it loads, and it checks the account signed into OneNote — not the account you think you are using. Confirm both before touching anything else.

1. In OneNote, go to **File > Account** and note exactly which Microsoft account is signed in.
2. Sign into account.microsoft.com with that same account and confirm an active **Microsoft 365 Copilot** or **Copilot Pro** subscription under Subscriptions.
3. For work accounts, ask your IT admin to confirm the Copilot license is **assigned** to you in the Microsoft 365 admin center — assigned, not merely purchased.
4. If the signed-in account is wrong, use **File > Account > Sign out**, then sign back in with the licensed account and restart OneNote.
5. Allow up to 24 hours after any license change for Microsoft's provisioning to reach the OneNote client before concluding it failed.

### Fix 2: Make sure you are on the unified OneNote app

Two different OneNote apps still exist on many PCs, and only one of them gets Copilot. Running the legacy app is a dead end — no update will ever add the feature there.

1. Open OneNote and go to **File > Account > About OneNote** to identify which app you have.
2. If it says **OneNote for Windows 10**, you are on the legacy app — install the current **OneNote** from the Microsoft Store instead.
3. After installing, open the new OneNote, sign in with your licensed account, and let your cloud notebooks sync down.
4. You can uninstall the legacy app afterward from **Settings > Apps > Installed apps** to avoid opening the wrong one by habit.
5. Pin the correct OneNote to your taskbar and remove the old pin. Version confusion causes the same class of problem elsewhere on ARM, as with [Minecraft Java performance on ARM laptops](/articles/minecraft-java-arm-laptop-performance/), where running the wrong build decides which features work.

### Fix 3: Move your notebooks to OneDrive or SharePoint

This is the OneNote-specific gotcha that catches almost everyone: Copilot cannot see notebooks stored on your local drive. If your notes live in a local folder, the Copilot button will stay dead on those pages no matter what your license says.

1. In OneNote, go to **File > Info** and look at each notebook's location — anything pointing to a local path like `C:\Users\...` is invisible to Copilot.
2. Right-click the local notebook and choose **Share** or **Move**, then select your OneDrive or a SharePoint library as the destination.
3. Wait for the move and the subsequent sync to finish — check the sync status icon on each notebook and resolve any conflicts first.
4. Open a page in the now-cloud notebook, select some text, and check whether the Copilot option appears in the ribbon or right-click menu.
5. For notebooks you cannot move (shared local archives, for example), accept that Copilot will not work there — copy the pages you need AI help with into a cloud notebook instead.

### Fix 4: Update OneNote and repair the installation

An outdated or half-broken OneNote install can carry a Copilot implementation that never activates. Update first, repair second — both are quick and non-destructive.

1. In OneNote, go to **File > Account > Update Options > Update Now** to pull the latest Microsoft 365 Apps build.
2. Restart OneNote after the update and test Copilot on a cloud-notebook page.
3. If it still fails, open **Settings > Apps > Installed apps**, find **Microsoft 365** or **OneNote**, choose **Modify**, and run an **Online Repair**.
4. Let the repair complete without opening Office apps, then restart the PC and sign back into OneNote.
5. After major repairs, re-verify the signed-in account under **File > Account** — repairs sometimes drop you to a different identity, which silently unlicenses Copilot again.

### Fix 5: Check admin policies and connected experiences

In managed environments, Copilot in OneNote is frequently disabled by policy even when Word's Copilot works — admins can scope the restriction per app. There is also a local privacy setting that can suppress it.

1. In OneNote, open **File > Options > Trust Center > Privacy Options** and confirm optional connected experiences are enabled.
2. Ask your Microsoft 365 admin to check whether Copilot is restricted for OneNote specifically under the organization's Copilot policies.
3. Have the admin confirm the Copilot service plan is enabled on your license — individual service plans can be switched off per user.
4. After any policy change, sign out of OneNote and back in so the new policy downloads to the client.
5. If your laptop aggressively conserves power during these checks, remember that some AI-adjacent features behave oddly under power limits — the [battery limiter behavior on AI laptops](/articles/battery-limiter-80-percent-ai-laptop/) is a useful reference for separating power quirks from real Copilot failures.

### Fix 6: Clear OneNote's cache and reset its local state

When everything above checks out but Copilot still refuses to engage, stale cached credentials or corrupted local state is usually the culprit. A cache clear forces OneNote to re-authenticate and re-download its feature configuration.

1. Close OneNote completely, then open **File Explorer** and navigate to `%localappdata%\Microsoft\OneNote`.
2. Rename the version-numbered cache folder (for example, add `.old` to its name) rather than deleting it, so you can restore it if needed.
3. Reopen OneNote, sign in with your licensed account, and let notebooks resync from the cloud — this can take a while on large notebooks.
4. Test Copilot on a synced cloud page; the fresh sign-in usually restores the license check that was silently failing.
5. If the problem persists only on this PC while Copilot works in OneNote on the web, the issue is local to your Windows install — on-device AI features like [Click to Do on touchscreens](/articles/click-to-do-touchscreen-not-working/) failing at the same time would point to a broader system problem worth investigating through [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

Copilot in OneNote fails for boring, checkable reasons: the wrong account, the legacy app, local notebooks, or a policy. Confirm the license on the signed-in account, run the unified OneNote app, keep your notebooks in the cloud, and the AI features light up.
