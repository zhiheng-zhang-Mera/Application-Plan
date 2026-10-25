# Uncertainty-aware clarification for audio-driven assistants

Research-fit statement | Mirco Ravanelli

zhiheng0mera@gmail.com | Melbourne, Australia | Fall 2027

Concordia application/student ID: 20814667 | Doctor of Philosophy - Computer Science

International applicant; neither a Canadian citizen nor a permanent resident.

## Motivation and fit

Your current work on conversational AI and efficient, interpretable representations, together with SpeechBrain, offers a practical path from systems experimentation to audio research. LMAC-TD motivates an additional question about the evidence a user receives when deciding whether to trust a prediction. I would keep the initial study at the audio-component level before generalizing to a conversational assistant.

## Proposed research question

Under controlled audio distribution shift, can calibrated abstention and clarification reduce incorrect downstream actions at a useful coverage and latency cost, and when do listenable explanations help users recognize an incorrect classification?

## Preparation I can bring

I led architecture, AI-assisted integration and evidence-backed acceptance of Utopia, a completed and frozen multi-device system. Its bounded records cover two Windows execution workers, Android/Web control, fault/replay histories and independently inspectable results. My Android privacy-evidence research provides additional experience in separating observed signals from stronger claims. These artifacts are a starting point for research, not substitutes for a controlled scientific evaluation.

## Initial method

First reproduce a suitable existing SpeechBrain or lab recipe on a public dataset. Introduce predefined noise/overlap and held-out conditions, keeping calibration and evaluation splits separate. Compare unconditional prediction, confidence thresholds and calibrated fallback, then evaluate whether evidence features add value beyond confidence alone. A separate, appropriately reviewed interface pilot could compare labels, confidence displays, raw audio and listenable explanation clips. An environmental-audio pilot would test a component-level mechanism, not establish the reliability of a whole conversational agent.

# Evaluation and feasible starting scope

Mirco Ravanelli | Uncertainty-aware clarification for audio-driven assistants

## 1. Calibration and shift

Measure risk-coverage curves, Brier score/calibration error and false downstream actions under clean and shifted inputs. Tune thresholds on validation data and preserve a held-out test set.

## 2. Fallback costs

Compare abstain, request clarification and unconditional execution on error rate, useful coverage, clarification frequency and latency. Report the conditions in which asking the user too often erases the benefit.

## 3. Evidence usefulness

If the technical results justify a user study, compare raw audio, confidence and listenable explanations on error detection, decision time and appropriate acceptance/rejection. Assess faithfulness separately from listener preference.

## First 12 weeks after project agreement

Weeks 1-3: reproduce an agreed audio baseline and identify gaps in my ML preparation. Weeks 4-7: construct controlled corruption/shift conditions and calibration baselines. Weeks 8-12: evaluate fallback trade-offs and decide whether an explanation-assisted interaction study is warranted.

## Scope and evidence boundaries

I have not trained a validated speech foundation model or deployed a smart-glasses assistant. My existing platforms offer integration experience, not evidence of speech-model performance. An audio explanation is not the same as denoising, source separation or an explanation of an entire agent. This proposal is conditional on a suitable current opening.

## Selected sources and artifacts

Current official research and contact

SpeechBrain

LMAC-TD

Utopia implementation and bounded acceptance evidence

Prepared 25 October 2026. Proposed experiments are not completed results. Topic and supervision arrangements remain open for discussion.

## Source and project links

- <https://www.concordia.ca/faculty/mirco-ravanelli.html>

- <https://speechbrain.github.io/>

- <https://francescopaissan.it/lmac-td/>

- <https://github.com/zhiheng-zhang-Mera/utopia>
