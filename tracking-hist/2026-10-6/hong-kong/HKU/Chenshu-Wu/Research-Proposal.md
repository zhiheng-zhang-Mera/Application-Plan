# Research Proposal Draft

## Reliable Personal Compute Fabric for Context-Aware AIoT Systems

### Motivation

Personal AI systems are increasingly expected to act across phones, PCs, wearables and nearby edge devices rather than remain inside one application. The difficult systems problem is not only how to run an AI model on an edge device, but how to decide where an action should execute, how sensing context should influence that decision, and how a user can still understand what happened when devices disappear, degrade or disagree.

My current Utopia/Digital City project provides a concrete substrate for this question. Its accepted product evidence includes Android and Web control surfaces, authenticated device paths, and a three-end mesh across two real Windows workers plus an Android control surface with strict target-device routing. This gives me a working environment in which placement, recovery and user-visible control can be studied on real heterogeneous endpoints.

### Research question

I would like to investigate how a **personal compute fabric** can combine AIoT sensing/context with resource-aware agent execution while preserving reliability and user control.

Three questions are especially interesting:

1. **Context-aware placement.** How should location, sensing context, device capability, latency and availability jointly affect where an agent action runs?
2. **Failure-aware continuity.** When a device becomes unavailable or sensing context changes, how should work migrate or degrade without silently changing the semantics of the action?
3. **Inspectable decisions.** Can the runtime expose enough provenance for a user or evaluator to understand why a particular device and execution path were chosen?

### Proposed method

I would extend the existing multi-device substrate with a measurement layer for device resources and contextual signals. Placement policies would be compared under controlled workloads rather than evaluated only by end-to-end task success.

The evaluation could include:

- heterogeneous Android/PC/edge-device configurations;
- controlled changes in device availability, network conditions and sensing context;
- latency, energy/resource use, task success and recovery time;
- user-visible correctness of placement/fallback explanations;
- replay and ablation to isolate whether context-aware scheduling actually improves outcomes.

Where relevant, ubiquitous localization or wireless sensing could provide contextual inputs to the runtime. I am particularly interested in doing this without making the scheduler a black box: sensing should inform placement, but policy and provenance should remain testable.

### Expected contribution

The intended contribution is a systems framework and empirical methodology for **context-aware, reliable personal AIoT execution**, rather than a single application. The same fabric could later support wearable assistants, health terminals or embodied devices, but those would be evaluation verticals over a shared runtime.

This direction connects my existing multi-device systems work with the AIoT, localization and edge-systems research of your group while leaving room to refine the sensing modality and application domain around the lab's current projects.
