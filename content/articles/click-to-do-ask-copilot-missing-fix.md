---
title: "How to Fix the Missing Ask Copilot Action in Click to Do"
slug: click-to-do-ask-copilot-missing-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["click to do", "ask copilot", "copilot", "copilot+ pc", "windows 11", "troubleshooting"]
description: "Restore the missing Ask Copilot action in Click to Do with fixes for the Copilot app, account sign-in, feature settings, and Windows AI component repair."
thumbnail: "/images/thumbs/click-to-do-ask-copilot-missing-fix.webp"
faqs:
  - q: "Why is Ask Copilot missing when other Click to Do actions work?"
    a: "Ask Copilot is the only Click to Do action that hands your selection to the Copilot app. If Copilot is not installed, not signed in, or blocked by a setting, that one action disappears while Rewrite and Summarize, which run on-device, keep working."
  - q: "Does Ask Copilot need an internet connection?"
    a: "Yes. Unlike on-device text actions, Ask Copilot sends your selection to Copilot's cloud service, so it needs a working internet connection and a signed-in Microsoft account. Without either, the action may not appear at all."
  - q: "Is Ask Copilot available on work or school accounts?"
    a: "It depends on your organisation's policy. Some work and school accounts disable Copilot or restrict it, which removes Ask Copilot from Click to Do even on a fully capable Copilot+ PC. Your IT admin can confirm whether it is allowed."
  - q: "Will reinstalling Copilot delete my chat history?"
    a: "No, your Copilot chat history is tied to your Microsoft account, not to the local app install. Reinstalling the app and signing back in restores access to your previous chats."
---

Every other Click to Do action is present — Rewrite, Summarize, even Create image — but Ask Copilot is nowhere to be seen. The menu opens, the text actions work, yet the bridge to Copilot is missing. That pattern is actually good news: it narrows the fault to one link in the chain.

Ask Copilot is different from the other actions because it does not run on your PC alone. It passes your selected text to the Copilot app and its cloud service, which means it needs the app installed, the account signed in, the connection working, and the organisation policy allowing it. Any one of those can remove the action silently.

This guide checks that bridge link by link: the Copilot app, your account, the feature settings, and finally the Windows components that connect them. Test the Click to Do menu after each fix.

## Why this happens

- **Copilot app missing or outdated:** If the Copilot app was uninstalled, never installed, or is badly out of date, Click to Do has nowhere to send the selection, so it hides Ask Copilot.
- **Not signed in to Copilot:** Ask Copilot requires a signed-in Microsoft account; a signed-out app, or a Windows sign-in that drifted from the Copilot sign-in, removes the action.
- **Copilot disabled by policy or setting:** Work, school, or privacy settings can disable Copilot, and Click to Do respects that by hiding the action rather than showing an error.
- **No internet connection at menu time:** Because Ask Copilot is cloud-based, a dead connection, VPN problem, or proxy block can keep the action from loading.
- **Click to Do feature state stale:** A crashed or half-updated Click to Do service can show on-device actions while failing to register the Copilot handoff.
- **Windows AI components damaged:** Corrupted system files can break the link between Click to Do and Copilot without affecting either app on its own.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Open Copilot directly and sign in

Start with the simplest explanation: the Copilot app itself. If Copilot does not open or is not signed in, Ask Copilot cannot exist in Click to Do, and fixing the app fixes the menu action as a side effect.

1. Open the Copilot app from the Start menu. If it is missing, install it from the Microsoft Store and open it.
2. Check the top of the Copilot window for your account name or avatar — if you see a sign-in prompt, sign in with your personal Microsoft account.
3. Send Copilot a test question, such as "What is 2 + 2?", and confirm you get an answer — this proves the app, account, and connection all work.
4. Without closing Copilot, open Notepad, select a sentence, and open Click to Do to look for Ask Copilot.
5. If the action appears while Copilot is running but vanishes when Copilot is closed, the handoff is working but fragile — keep Copilot pinned and move to Fix 3 to stabilise it. A similar one-action-missing pattern appears in [Copilot taskbar icon missing](/articles/copilot-taskbar-icon-missing/), where the Copilot surface itself is the fault.

### Fix 2: Check your connection and account type

Ask Copilot is cloud-based, so a connection or account problem hides it in a way on-device actions never show. Ruling these out early stops you from reinstalling Windows for what is really a VPN or account issue.

1. Open Edge and load a normal website to confirm the internet connection works, then disconnect any VPN temporarily and test again.
2. If you are on a work or school network, try a personal hotspot briefly — a corporate proxy that blocks Copilot will hide the action only on that network.
3. Confirm you are signed in to Windows with a Microsoft account, not only a local account, at **Settings > Accounts**.
4. If your device is managed by work or school, ask your IT admin whether Copilot is enabled for your account — a policy block cannot be fixed from the PC alone.
5. After any account or network change, restart the PC and test Click to Do again, since the action registers at sign-in time.

### Fix 3: Re-register Click to Do and the Copilot handoff

Sometimes both apps are healthy but the link between them has gone stale — after an update, a crash, or a sign-in change. Toggling the feature and restarting forces Windows to rebuild that link from scratch.

1. Open **Settings > System > Click to Do** and switch the feature **Off**.
2. Close all apps, restart the PC, and sign in again with your Microsoft account.
3. Return to **Settings > System > Click to Do** and switch the feature back **On**.
4. Open Copilot once, confirm you are signed in, then open Notepad, select text, and check for Ask Copilot.
5. If the action appears now, the link was simply stale — no deeper repair is needed. If it is still missing, the Copilot app install itself is suspect, so continue to Fix 4. The neighbouring action in this chain, [Click to Do with a stylus pen](/articles/click-to-do-stylus-pen-not-working-fix/), also depends on a fragile handoff, and its fixes show the same toggle-and-retest pattern.

### Fix 4: Repair or reinstall the Copilot app

A damaged Copilot app can open and answer questions yet fail to register itself as a Click to Do target. Repairing, then reinstalling if needed, rebuilds that registration cleanly.

1. Open **Settings > Apps > Installed apps**, find **Copilot**, click the three dots, and choose **Advanced options**.
2. Click **Repair**, wait for it to finish, then open Copilot, confirm sign-in, and test Click to Do.
3. If Repair does not help, return to the same screen and click **Reset**, then open Copilot and sign in again before testing.
4. If Reset also fails, uninstall Copilot from **Installed apps**, restart, reinstall it from the Microsoft Store, sign in, and test again.
5. After reinstalling, do not skip the sign-in test in Fix 1 — an unsigned-in Copilot looks installed but still cannot provide Ask Copilot.

### Fix 5: Update Windows and the Copilot app together

The Click to Do-to-Copilot handoff depends on matching versions: a new Click to Do menu talking to an old Copilot app, or the reverse, can drop the action. Updating both sides together removes version mismatch as a cause.

1. Open the Microsoft Store, go to **Library**, click **Get updates**, and install any Copilot update offered.
2. Open **Settings > Windows Update** and install all pending updates, including optional updates.
3. Restart the PC after both updates, then open Copilot and confirm sign-in before testing anything else.
4. Open Notepad, select a sentence, and check the Click to Do menu for Ask Copilot.
5. If Windows Update fails, check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for current update troubleshooting before trying the system repair below. Version-sensitive AI failures on other tools follow the same rule, as in [Stable Diffusion DirectML NPU issues](/articles/stable-diffusion-directml-npu-fix/), where mismatched components break one workload while others survive.

### Fix 6: Repair Windows AI components

When Copilot works, the account is right, the connection is fine, and the action is still missing, the Windows side of the handoff is damaged. System repair rebuilds it without touching your files or apps.

1. Right-click **Start**, choose **Terminal (Admin)**, and run `DISM /Online /Cleanup-Image /RestoreHealth`, waiting for it to finish.
2. When DISM completes, run `sfc /scannow` in the same window, then restart the PC.
3. After the restart, open Copilot, confirm sign-in, then test Click to Do in Notepad.
4. If the action is still missing, perform an in-place repair install of Windows 11 from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), choosing **Keep personal files and apps**.
5. After the repair install, sign in, open Copilot once, and test Click to Do — the handoff should now register cleanly.

## Closing

Ask Copilot disappears when the bridge between Click to Do and the Copilot app breaks — a missing app, a signed-out account, a policy block, or a stale registration. Fix the app and account first, re-register the feature, and only repair Windows when both sides are proven healthy.
