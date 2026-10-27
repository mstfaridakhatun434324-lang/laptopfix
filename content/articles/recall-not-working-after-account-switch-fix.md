---
title: "How to Fix Recall Not Working After an Account Switch on Your AI PC"
slug: recall-not-working-after-account-switch-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["recall", "account switch", "user account", "copilot plus pc", "snapshots", "troubleshooting"]
description: "Fix Recall not working after switching accounts on your Copilot+ PC by checking per-account snapshot stores, permissions, and Windows Hello setup in detail."
thumbnail: "/images/thumbs/recall-not-working-after-account-switch-fix.webp"
faqs:
  - q: "Why does Recall stop working when I switch user accounts?"
    a: "Recall snapshots are stored per user account and encrypted with that account's credentials. Switching accounts gives you a different, possibly empty or unconfigured Recall store, so the previous account's timeline does not carry over."
  - q: "Can I see another account's Recall snapshots?"
    a: "No, by design. Recall snapshots are private to each user account and cannot be viewed from a different account, even on the same PC. This privacy separation is intentional."
  - q: "Do I need to set up Recall separately for each account?"
    a: "Yes. Each account must opt in to Recall, set up Windows Hello, and build its own snapshot history. Settings and snapshots do not transfer between accounts."
  - q: "Will switching back restore my old Recall timeline?"
    a: "Usually, yes — if the original account's snapshot store is intact. Sign back in to the original account with Windows Hello and Recall should show its own timeline again."
---

You switch from one user account to another on your Copilot+ PC — a work account, a family account, or a fresh profile — and Recall is either blank, refuses to open, or shows an error instead of a timeline. The previous account's Recall worked fine, which makes the new account's failure feel like a system fault rather than a setup gap.

In most cases it is a setup gap, with a privacy rule behind it. Recall is deliberately per-account: each account has its own encrypted snapshot store, its own opt-in, and its own Windows Hello unlock.

This guide separates the normal per-account behaviour from a genuine fault: verify the account and its Recall state first, then set up Hello and permissions, then repair the store if the account's own timeline still fails.

## Why this happens

- **Recall not enabled for the new account:** Each account must opt in separately, so switching to an account that never enabled Recall shows a blank or disabled timeline.
- **Windows Hello not set up for this account:** Recall requires Hello sign-in for the account in use, and a Hello setup from another account does not transfer.
- **Per-account snapshot store is empty by design:** Snapshots belong to one account only, so a new account correctly shows no history from the previous account.
- **Snapshot saving paused or blocked by policy:** A work or school account may carry a policy that disables Recall, or the account may have snapshot saving toggled off.
- **Corrupted profile or credential vault for this account:** A damaged profile can prevent Recall from starting even when the account itself signs in normally.
- **Recall component tied to the previous session:** A fast user switch can leave Recall processes from the previous account running, blocking the new account's Recall from starting cleanly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm which account you are in and what Recall expects

Start by establishing the baseline: which account, whether it ever used Recall, and whether its store is empty or broken.

1. Open **Settings > Accounts** and confirm the exact account currently signed in.
2. Open **Settings > Privacy & security > Recall & snapshots** and check whether **Save snapshots** is on or off for this account.
3. Note the storage figure: zero on a brand-new account is normal, while a non-zero figure with a broken timeline is a fault.
4. Switch back to the original account briefly, if you can, and confirm its Recall still works — that proves the system is healthy and the issue is account-specific.

### Fix 2: Enable Recall and set up Windows Hello for this account

A new account needs its own complete Recall setup.

1. In **Settings > Privacy & security > Recall & snapshots**, turn **Save snapshots** **On** and accept the Recall consent prompt for this account.
2. Open **Settings > Accounts > Sign-in options** and set up a **Windows Hello PIN** for this account, completing every prompt.
3. Add fingerprint or face recognition if the device supports it and you want it for this account.
4. Restart the PC and sign in to this account with Hello, not just the password, so the snapshot store unlocks at sign-in.

### Fix 3: Check for policies or settings blocking Recall on this account

Work, school, and family accounts can carry restrictions that a personal account does not.

1. In Recall settings, look for any message stating Recall is managed by your organisation or disabled by policy.
2. Check **Settings > Accounts > Family & other users** if this is a child or managed account, and review its content restrictions.
3. If a policy message appears, you cannot override it from the PC — ask the account administrator whether Recall is permitted for this account.
4. For a personal account with no policy message, confirm no third-party privacy tool is disabling snapshot saving in the background.

### Fix 4: Clear the fast-switch conflict with a full restart

Fast user switching can leave the previous account's Recall processes holding resources the new account needs.

1. Sign out of all accounts completely — do not just switch — using **Start > User > Sign out**.
2. Restart the PC from the sign-in screen to clear every lingering user session.
3. Sign in directly to the affected account, with no prior switch from another account.
4. Open Recall immediately and check whether it loads normally now.

### Fix 5: Repair the account's Recall store without touching other accounts

When the account's own Recall still fails after setup and a clean restart, its snapshot store may be corrupted.

1. Open **Settings > Privacy & security > Recall & snapshots** for the affected account and delete its snapshots.
2. Restart the PC and sign in to the same account with Windows Hello.
3. Re-enable **Save snapshots** and use the account normally for a few hours.
4. Check the guidance on [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) if the settings page itself fails to load or the delete option is unavailable.
5. If new snapshots now appear and survive a restart, the account's store is repaired — the old snapshots for this account are gone, but the account itself works again.

### Fix 6: Test a fresh profile to isolate profile corruption

If nothing above restores Recall for this account, the profile itself may be damaged. A fresh profile test proves it without disturbing the original account's data. A related timeline fault — searching within a single app view — is covered in [Recall timeline search by app not working](/articles/recall-timeline-search-by-app-fix/), and a separate ARM app problem with a similar isolation approach is described in [Zoom app issues on ARM laptops](/articles/zoom-app-arm-laptop-issues-fix/). For a gesture-based Copilot+ fault, see [Click to Do gesture not working](/articles/click-to-do-gesture-not-working/).

1. Create a new local user account in **Settings > Accounts > Other users**.
2. Sign in to the new account, set up Windows Hello, and enable Recall for it.
3. Use the new account briefly and confirm Recall captures snapshots there.
4. If Recall works in the new profile but not the old one, the old profile is corrupted — migrate your files to the new profile rather than continuing to repair the old one.
5. If Recall fails in the brand-new profile too, the fault is system-wide: update Windows fully and contact your PC maker's support with that test result.

## Closing

Recall after an account switch fails most often because the new account was never set up — not because the system broke. Enable Recall for that account, set up its Windows Hello, and sign in cleanly, and its own timeline will build from there; only a fresh-profile test proves the deeper case of a corrupted profile.
