---
title: "Windows Recall System Requirements: Does Your Laptop Qualify?"
slug: windows-recall-system-requirements
date: 2026-10-19
categories: ["ai-pc"]
tags: [windows-recall, system-requirements, copilot-plus-pc, npu, windows-11, hardware]
description: "Windows Recall system requirements explained: the NPU, 16GB RAM, storage space, and Windows 11 version your laptop needs to run Recall smoothly in 2026."
thumbnail: "/images/thumbs/windows-recall-system-requirements.webp"
faqs:
  - q: "What NPU does Windows Recall require?"
    a: >
      A 40+ TOPS neural processing unit — found in Snapdragon X series, Intel Core Ultra 200V series, and AMD Ryzen AI 300 series chips. Older NPUs below 40 TOPS do not qualify.
  - q: "Can I run Recall with 8GB of RAM?"
    a: >
      No. Copilot+ certification requires 16GB minimum, and Recall enforces it. The snapshot pipeline needs the headroom.
  - q: "Does Recall work on Windows 11 23H2?"
    a: >
      No. Recall requires Windows 11 version 24H2 or later, where its components and AI models exist.
  - q: "Why is Recall unavailable in my country?"
    a: >
      Microsoft has rolled Recall out unevenly across regions. Check current availability for your region, and avoid bypass tools — they break with updates.
---
Before troubleshooting Recall, it pays to answer the foundational question: does this laptop even qualify? Recall has the strictest hardware requirements of any Windows feature to date, and Microsoft enforces them — no check, no Recall. A surprising number of 'Recall not working' cases end right here, with a laptop that was never eligible.

The requirements are specific and non-negotiable: a neural processor of a certain class, minimum RAM and storage, the right Windows build, and a few setup prerequisites. Miss any one and Recall stays unavailable, no matter how many settings you toggle.

This guide lays out each requirement plainly, shows how to check your laptop against them, and explains what to do at each failure point. If the timeline will not render on qualifying hardware, see [Recall timeline not loading](/articles/recall-timeline-not-loading/). For the next Copilot+ feature to verify, see [Click to Do not working](/articles/click-to-do-not-working-windows-11/). And to verify Copilot+ status directly, read [how to check if your laptop is a Copilot+ PC](/articles/how-to-check-if-laptop-is-copilot-plus-pc/).

## Why this happens

- **No qualifying NPU:** The headline requirement: a 40+ TOPS neural processing unit. Most laptops sold before 2024 simply do not have one.
- **Less than 16GB RAM:** Copilot+ certification — and therefore Recall — requires 16GB of memory minimum.
- **Storage below 256GB:** The snapshot store needs room to live; 256GB total storage is the floor.
- **Windows 11 older than 24H2:** Recall's components only exist in Windows 11 version 24H2 and later.
- **Windows Hello not configured:** Recall needs Hello for snapshot encryption. Without it, the feature cannot initialize.
- **Region or edition exclusions:** Recall availability has varied by region and Windows edition during rollout.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check for a 40+ TOPS NPU
This is the gatekeeper requirement and the one that ends most eligibility questions. The NPU entry in Task Manager's Performance tab is the ground truth — present and 40+ TOPS means you pass, absent means the laptop predates the AI PC wave entirely. Everything else on the requirements list is moot without it, so check here first and save yourself the rest of the list when the answer is no.
1. Open Task Manager (Ctrl + Shift + Esc) > Performance and look for an NPU entry.
2. If present, check the specs — Copilot+ needs 40+ TOPS (Snapdragon X series, Intel Core Ultra 200V+, AMD Ryzen AI 300+).
3. No NPU entry means the laptop predates the AI PC wave.
4. For the full Copilot+ picture, see [how to check if your laptop is a Copilot+ PC](/articles/how-to-check-if-laptop-is-copilot-plus-pc/).

### Fix 2: Verify RAM and storage
The supporting requirements are just as hard-edged as the NPU: 16GB RAM and 256GB storage are certification floors, not recommendations. The snapshot pipeline genuinely needs the headroom — an 8GB machine would thrash. The small consolation is that RAM and storage are the only requirements you can fix with an upgrade, unlike a missing NPU.
1. In Settings > System > About, confirm at least 16GB of installed RAM.
2. Check that total storage is 256GB or more, with healthy free space.
3. Falling short on either means Recall stays unavailable — these are certification floors.
4. Upgrading RAM/storage on a qualifying NPU machine can bring it into compliance.

### Fix 3: Confirm Windows 11 24H2 or later
Software is the easiest requirement to satisfy and the most commonly missed. Recall's components only exist in Windows 11 24H2 and later — no 24H2, no Recall, regardless of how new the hardware is. The fix is a straight update path, and Microsoft's official installer covers machines where Windows Update is being coy about offering the new build.
1. Go to Settings > System > About and read the Version number.
2. If you are on 23H2 or older, run Windows Update until 24H2+ is installed.
3. Use the official installer at the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) if Update does not offer it.
4. Re-check Recall availability after updating and restarting.

### Fix 4: Set up Windows Hello
Windows Hello feels like a mere convenience until Recall refuses to initialize without it. The snapshot store's encryption is architecturally tied to Hello enrollment, so this 'requirement' is really a security design decision. Enrolling a PIN takes two minutes and unblocks not just Recall but the whole encrypted-storage story on the device.
1. Go to Settings > Accounts > Sign-in options.
2. Enroll face, fingerprint, or at minimum a PIN.
3. Sign out and back in to activate Hello fully.
4. Recall setup should now proceed past the encryption step.

### Fix 5: Confirm region and edition support
After the big four — NPU, RAM, storage, build — region and edition are the last mile. Recall's rollout has been uneven geographically, and some Windows editions need additional feature packs. This is the requirement most likely to resolve itself with time, which makes waiting the rational play rather than reaching for bypass tools that break with updates.
1. Check Microsoft's current availability notes at [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for your region.
2. Recall needs a full Windows 11 edition — some N editions need the media feature pack.
3. If everything else qualifies and only region blocks you, waiting for rollout beats hacking.
4. Do not use bypass tools; see why in our [unsupported PC](/articles/enable-recall-on-unsupported-pc/) article.

### Fix 6: Check the fine print: SSD and Hello
Two quieter requirements catch people who pass the headline checks: Recall wants its store on a fast system SSD rather than a spinning drive, and it leans on device encryption beneath Hello. Both are quick to verify and quick to fix, and they explain a meaningful slice of 'meets all requirements but still unavailable' cases.
1. Confirm Windows is installed on an SSD, not a spinning drive — check Task Manager > Performance > Disk.
2. Complete Windows Hello setup under Settings > Accounts > Sign-in options.
3. Verify BitLocker or device encryption status, since snapshot encryption builds on it.
4. Recheck Recall availability after satisfying these secondary requirements.

### Fix 7: Run Microsoft's PC Health Check
When manual spec-checking feels error-prone, Microsoft's own PC Health Check renders an authoritative verdict, naming exactly which requirement fails. It removes all guesswork and all forum-speculation from the process. Fix the specific failure it names instead of shotgun-troubleshooting the whole list.
1. Download PC Health Check from Microsoft's website.
2. Run it and review the Windows 11 and Copilot+ eligibility sections.
3. Note exactly which requirement fails — the tool names it plainly.
4. Address that specific failure rather than guessing at the whole list.

## Closing

Recall's requirements are strict because the feature genuinely needs the hardware — on-device AI at 40+ TOPS is not marketing fluff. Check NPU, RAM, storage, Windows version, and Hello in that order. If your laptop clears all five and Recall still will not run, you have a software problem worth troubleshooting; if it fails any of them, you have a hardware answer, and no amount of settings-toggling will change it.
