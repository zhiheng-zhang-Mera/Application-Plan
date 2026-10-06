# One-Page Research Statement

## Reliable Multi-Device Edge Execution for Agent Workloads

My research interest is in the systems layer that allows an AI-assisted workload to move from a single application into a heterogeneous set of personal and edge devices. I am particularly interested in placement, recovery and observability: where should a task run, what should happen when the selected device or network path becomes unavailable, and what evidence should remain so that the decision can be reproduced and audited?

I have been building Utopia/Digital City as a concrete multi-device substrate for these questions. Its current accepted product boundary includes Android and Web control surfaces, authenticated device/control paths, and a three-end mesh across two real Windows workers and an Android control surface with strict target-device routing. The system is not yet the Personal Compute Fabric I ultimately want to study; heterogeneous placement/offloading is a planned research extension rather than a completed claim.

For PhD research, I would like to investigate a resource-aware runtime for agent workloads across personal and edge devices. A useful experimental setup would expose device capability, availability, latency and workload pressure to a placement policy, then evaluate the policy under controlled failures and topology changes. Important outcomes would include task completion, placement stability, recovery time, resource cost, and whether the resulting execution path can be independently reconstructed from provenance.

I am also interested in the interaction between policy intelligence and systems guarantees. An LLM or learned component may recommend a device or service, but the runtime should enforce hard eligibility constraints, prevent unsafe or stale routing, and expose why a fallback occurred. This creates a natural boundary between AI-assisted decision making and dependable distributed execution.

My broader goal is to build experimentally useful infrastructure for studying multi-device AI systems, not only a new scheduler. The same substrate should support repeated scenarios, fault injection, replay and ablation so that claims about scheduling or edge intelligence can be tested rather than inferred from demonstrations.
