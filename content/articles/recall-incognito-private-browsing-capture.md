---
title: "Recall and Private Browsing: What Gets Captured and How to Control It"
slug: recall-incognito-private-browsing-capture
date: 2026-10-22
categories: ["ai-pc"]
tags: ["recall incognito", "recall private browsing", "windows recall privacy", "recall capture control", "copilot plus pc", "windows 11"]
description: "Worried Recall captures private browsing? Learn exactly what Recall records in incognito mode, how its filters work, and how to keep private activity private."
thumbnail: "/images/thumbs/recall-incognito-private-browsing-capture.webp"
faqs:
  - q: "Does Recall capture Chrome incognito windows?"
    a: >
      No. Recall skips private windows in all major browsers, including Chrome incognito, Edge InPrivate, and Firefox private windows. The exclusion is automatic — there is no toggle to turn it off or on.
  - q: "Can websites opt out of Recall capture?"
    a: >
      Websites cannot opt out directly, but you can add any site to Recall's website exclusion list in Settings, and Recall will never snapshot those pages in Edge. For other browsers, use private windows for sensitive sites.
  - q: "Does Recall capture my passwords?"
    a: >
      Recall tries to filter snapshots containing sensitive information like passwords and card numbers, and password-manager apps can be excluded entirely. Still, avoid typing highly sensitive data into non-excluded apps while capture is on.
  - q: "How do I know Recall isn't secretly recording private tabs?"
    a: >
      Run the verification test in Fix 1: browse a unique word in a private window, wait, and search for it in Recall. No result means no capture. The test takes minutes and settles the question definitively.
---

One of the first questions Copilot+ PC owners ask is whether Recall captures incognito or InPrivate browsing. It is a fair worry: a feature that screenshots everything you do sounds like the opposite of private browsing — unless the boundaries are clearly enforced.

The short answer is reassuring: Recall does not capture InPrivate windows in Edge, incognito windows in Chrome, or private windows in other major browsers. Private browsing sessions are excluded from snapshots by design, not by a setting you have to remember to enable. That said, the boundary has edges worth understanding — which is also true of [Studio Effects with external webcams](/articles/studio-effects-external-webcam-issues/), where knowing exactly what the camera pipeline does and does not process matters.

This guide explains precisely what Recall captures and skips in private browsing, how to verify it on your own PC, and the settings that tighten control further. No speculation — just what the feature actually does and how to check it.

## Why this happens

- **Confusion between browser privacy and Recall capture:** Private browsing stops the browser from saving history — a separate question from whether Recall snapshots the window. Users conflate the two, which is why [Recall not filtering sensitive information](/articles/recall-not-filtering-sensitive-info/) worries persist even when the boundary works.
- **Non-private windows captured during the same session:** Recall captures your normal windows normally. If you had a regular window open beside the incognito one, that regular window's snapshots exist — which can look like private activity was captured.
- **Browser not recognized as private:** Recall relies on browsers correctly flagging private windows. An obscure browser that does not use the standard private-window APIs might not be excluded automatically.
- **Website exclusion list gaps:** Recall lets you exclude specific websites from capture. Sites you visit in normal mode but never excluded will be snapshotted — private mode is not a substitute for the exclusion list.
- **Screen-sharing a private window:** If you share your screen in a meeting while a private window is visible, the meeting app — not Recall — is what records it. Recall still skips the private window itself.
- **Misreading the timeline:** Text from a private session can appear in snapshots of adjacent normal windows — a search result page, a copied link — creating the false impression that the private window was captured.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify private windows are excluded on your PC

Trust, then verify. A two-minute test proves the boundary works on your specific browser and build.

1. Open an InPrivate window in Edge (or incognito in Chrome) and browse a distinctive test site, like a page with an unusual word.
2. Also open a normal window and visit a different distinctive page for contrast.
3. Wait 10–15 minutes, then search Recall for the unusual word from the private session — it should return nothing.
4. Search for the word from the normal session — it should appear. That contrast confirms the boundary.

### Fix 2: Use the website exclusion list for normal-mode privacy

For sites you visit in normal windows but never want snapshotted — banking, health portals — the exclusion list is the right tool.

1. Go to **Settings > Privacy & security > Recall & snapshots** and open website exclusions.
2. Add the domains you want permanently excluded from capture.
3. Remember this applies to Edge; other browsers are handled through their own private modes and app exclusions.
4. Test by visiting an excluded site normally, waiting, and confirming no snapshot appears.

### Fix 3: Exclude sensitive apps entirely

Password managers, banking apps, and similar tools can be excluded as whole apps, so nothing they display is ever captured.

1. In the same Recall settings page, open the app exclusion list.
2. Add your password manager, banking apps, and any other sensitive tools.
3. Note that DRM-protected content (like some streaming video) is already skipped automatically.
4. For background on how Windows distinguishes app architectures when applying these rules, [ARM64EC apps explained](/articles/arm64ec-apps-explained-fix/) is a helpful explainer.

### Fix 4: Turn on sensitive-information filtering

Recall can automatically filter snapshots that appear to contain sensitive data like passwords and credit card numbers.

1. In Recall settings, confirm **Filter sensitive information** is enabled.
2. Understand its limits: it is a best-effort filter, not a guarantee — treat it as a safety net, not a vault.
3. Combine it with app exclusions for anything truly sensitive rather than relying on the filter alone.
4. Review the filter's behavior after enabling by checking that test snapshots with obvious sensitive content are handled.

### Fix 5: Delete snapshots after a private-adjacent session

If you are ever unsure what got captured — say you forgot which window was private — you can surgically remove recent history.

1. Open Recall and find the time range you are unsure about in the timeline.
2. Delete snapshots from that range; deletion is immediate and permanent.
3. For a stronger reset, delete all snapshots from **Settings > Privacy & security > Recall & snapshots**.
4. Going forward, make private browsing a habit for sensitive tasks instead of cleaning up afterward.

### Fix 6: Lock down Recall access itself

Snapshots are encrypted and require Windows Hello to open Recall — but that protection only matters if your sign-in is strong.

1. Ensure Windows Hello (face, fingerprint, or PIN) is set up — Recall requires it.
2. Lock your PC (**Win + L**) whenever you step away; snapshots cannot be viewed without authentication.
3. Keep BitLocker/device encryption on — it is a Recall requirement and protects the snapshot store if the laptop is stolen.
4. Review these settings at [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) if anything about the requirements is unclear.

## Closing

Recall's private-browsing boundary is automatic and reliable across major browsers: private windows are simply not captured. Verify it once with the test above, use website and app exclusions for sensitive normal-mode activity, keep the sensitive-information filter on, and secure Recall behind Windows Hello. With those layers in place, private browsing stays private — even on a PC that remembers everything else.
