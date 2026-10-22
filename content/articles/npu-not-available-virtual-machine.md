---
title: "NPU Not Available in Virtual Machine? Why It Happens and Workarounds"
slug: npu-not-available-virtual-machine
date: 2026-10-22
categories: ["ai-pc"]
tags: ["npu","virtual-machine","hyper-v","wsl2","windows-11","troubleshooting"]
description: "Your NPU does not appear inside Hyper-V, VMware, or WSL2 virtual machines. Learn why NPU passthrough is not supported and the workarounds that actually work."
thumbnail: "/images/thumbs/npu-not-available-virtual-machine.webp"
faqs:
  - q: "Can I pass the NPU through to a Hyper-V virtual machine?"
    a: >
      No. Hyper-V's Discrete Device Assignment supports only certain PCIe GPUs;
      NPUs are not on the supported list, and vendors do not provide the
      firmware hooks passthrough needs. The NPU stays visible only to the host
      Windows installation.
  - q: "Does WSL2 support the NPU?"
    a: >
      Not currently. WSL2 exposes the GPU to Linux through GPU paravirtualization,
      but no equivalent path exists for the NPU. AI workloads in WSL2 run on the
      CPU or the paravirtualized GPU instead.
  - q: "Will this change in a future Windows update?"
    a: >
      Possibly, but nothing is announced. GPU passthrough took years to mature in
      Hyper-V and WSL2; NPU virtualization would need new vendor firmware and
      hypervisor support. Treat host-side execution as the plan for now.
  - q: "Can the VM at least use the CPU for AI tasks?"
    a: >
      Yes. Frameworks like ONNX Runtime and OpenVINO fall back to CPU execution
      inside the VM automatically. It is slower than the NPU but works without any
      special configuration.
---

You installed Windows 11 in Hyper-V, fired up Device Manager inside the guest, and the Neural processors category is simply gone. The NPU that works fine on the host is invisible to every virtual machine on the system — Hyper-V, VMware, VirtualBox, and WSL2 alike. This is not a driver bug and not something a guest-side install can fix.

The reason is architectural: NPUs were designed as host-only accelerators, and neither the hypervisors nor the NPU firmware support handing the device to a guest. If you set up virtualization expecting the NPU to follow, our [Hyper-V setup guide for ARM laptops](/articles/hyper-v-setup-arm-laptop/) covers what virtualization can actually do on these machines — NPU access is not on the list.

The practical answer is to run NPU workloads on the host and use the VM for everything else. The sections below explain exactly why passthrough fails for each platform and lay out the workarounds that genuinely work, including one you may not have considered: keeping AI inference on the host while the VM handles the surrounding application. And if the host side itself is flaky — say you need to [save a Live Captions transcript](/articles/save-live-captions-transcript/) from an AI feature that keeps failing, or the [Copilot app will not work offline](/articles/copilot-app-offline-mode-not-working/) — fix the host first, because the VM inherits nothing from a broken host.

## Why this happens

- **NPUs lack passthrough firmware support:** Unlike server GPUs, NPUs ship without the SR-IOV or DDA hooks a hypervisor needs to assign them to a guest.
- **Hyper-V DDA supports only certain GPUs:** Discrete Device Assignment has a narrow hardware compatibility list, and no shipping NPU qualifies for it.
- **WSL2 has GPU-PV but no NPU-PV:** Microsoft built GPU paravirtualization for WSL2; no equivalent virtualization path exists for neural processors.
- **Vendors target the host OS only:** Intel, AMD, and Qualcomm validate their NPU drivers against bare-metal Windows — guest drivers do not exist.
- **The NPU is tied to host power management:** NPU sleep/wake behavior is coordinated with the host firmware, which a guest cannot participate in.
- **Security model keeps AI local:** Copilot+ features are architected around on-device processing for the signed-in host user, not for sharing with guests.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the NPU is healthy on the host first

Before working around anything, verify the NPU actually works outside the VM. A surprising number of "NPU missing in VM" reports turn out to be "NPU missing everywhere" — and that is a host problem with a host fix.

1. On the host, open Device Manager and confirm the NPU appears under Neural processors.
2. Open Task Manager, Performance tab, and check that the NPU graph shows activity when you run an AI feature.
3. If the host cannot see the NPU either, troubleshoot the host — the VM question is moot until then.
4. Run one AI feature on the host (Live Captions is the quickest) to confirm end-to-end function.
5. Only once the host is proven healthy should you treat the VM's missing NPU as expected behavior rather than a bug.

### Fix 2: Run NPU workloads on the host, orchestrate from the VM

The most practical architecture: keep inference on the host where the NPU lives, and let the VM call it over the local network. This sounds complex but is often just a small service on the host plus an HTTP call from the guest.

1. On the host, set up your AI workload (for example, an ONNX Runtime or OpenVINO inference script) using the NPU.
2. Wrap it in a minimal local HTTP API — a few lines in Python's http.server or Flask is enough.
3. From the VM, verify network connectivity to the host (the default Hyper-V switch gives the host a reachable address).
4. Send inference requests from the VM application to the host API and measure end-to-end latency.
5. For many workloads the network hop adds single-digit milliseconds — far less than losing NPU acceleration entirely.
6. Document the setup; this host-service pattern is reusable for every VM you run.

### Fix 3: Use CPU or GPU fallback inside the VM

When re-architecting is overkill, accept the slower path: AI frameworks automatically fall back to CPU inside the VM, and WSL2 guests can use the paravirtualized GPU. For light or occasional inference, this is genuinely sufficient.

1. Inside the VM, install your AI framework (ONNX Runtime, OpenVINO, or PyTorch) normally.
2. Run your model and note which execution provider it selects — it will be CPU by default.
3. In WSL2, install the CUDA-enabled framework build to use the paravirtualized GPU instead.
4. Benchmark the fallback path: if it meets your latency needs, you are done — no heroics required.
5. Only invest in host-side serving (Fix 2) if the fallback is measurably too slow for your use case.
6. Keep the VM's framework updated; CPU fallback performance improves steadily with new releases.

### Fix 4: Use Hyper-V enlightenments and check for GPU-PV confusion

Some users expect the NPU to appear because the GPU appears in enhanced guests. Understanding the difference prevents wasted hours chasing a device that was never going to show up — and points you at what Hyper-V can actually accelerate.

1. In Hyper-V Manager, confirm the VM uses the default switch or an external virtual switch with host connectivity.
2. Verify GPU-PV is working if you need it (dxdiag in the guest should show the paravirtualized GPU).
3. Accept that no equivalent "NPU-PV" exists — this is a platform limitation, not a configuration error.
4. Check the [Microsoft support hub](https://support.microsoft.com/en-us/windows) for the current Hyper-V feature list so your expectations match reality.
5. Design your VM workload around CPU and GPU and reserve NPU tasks for the host.

### Fix 5: Consider dual-boot for bare-metal NPU access

When the workload truly needs the NPU and cannot be split across host and guest, dual-booting gives the second OS direct hardware access. It is heavier operationally than a VM, but it is the only way to put the NPU in front of another full OS.

1. Shrink the Windows partition from Disk Management to free space for the second OS.
2. Install the second OS (another Windows instance or a Linux distribution with NPU driver support).
3. Install the vendor's NPU driver stack in the second OS — Intel OpenVINO, for example, supports Linux NPU access on Core Ultra.
4. Verify NPU visibility with the vendor's tools before migrating any workload.
5. Weigh the reboot cost against Fix 2's host-service pattern; dual-boot wins only for sustained, interactive NPU work.

### Fix 6: Track vendor and Microsoft roadmaps for future support

NPU virtualization may arrive eventually — GPU-PV did, after years. Positioning yourself to adopt it early costs nothing and keeps you from building permanent workarounds for a temporary limitation.

1. Watch Intel, AMD, and Qualcomm developer blogs for NPU virtualization announcements.
2. Follow Windows Insider release notes for Hyper-V and WSL2 feature additions.
3. Keep host and guest systems updated so you receive support the moment it ships.
4. Revisit this decision yearly: the workaround you build today should be easy to retire.
5. Until an announcement lands, treat host-side NPU execution as the durable architecture.

## Closing

The NPU stays with the host — no hypervisor setting changes that, and no guest driver will conjure it into existence. The winning pattern is simple: prove the host healthy, run inference where the silicon lives, and let the VM use CPU or GPU fallback for everything else. If your virtualization experiments led you here from [Android emulator trouble on ARM](/articles/android-emulator-not-working-arm-laptop/) or [Docker Desktop on ARM](/articles/docker-desktop-arm-windows/), the same principle applies — match the workload to the layer that owns the hardware.
