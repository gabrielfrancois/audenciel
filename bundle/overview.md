# Overview

Welcome to the **AUDENSIEL - REFIT** Data Challenge!

This dataset has been set up with the help of AUDENSIEL, using part of the REFIT electricity consumption database. The REFIT database is a two-year study of the consumption of British households.

**Aim of the Challenge**

Predictive maintenance of household appliances represents a major lever for reducing energy costs and improving system reliability. In this challenge, we focus on detecting operating anomalies in refrigerator/freezer appliances in residential environments, within a realistic instrumentation framework: the only measurement assumed to be available under operational conditions is the household's total electrical consumption from a smart meter.

Measurements are acquired at a fixed time step of 8 seconds. No direct measurement of the refrigerator/freezer consumption is assumed to be accessible for production inference. The problem thus falls under non-intrusive anomaly detection from an aggregated signal, complemented by a quantification of the energy impact associated with the abnormal state.

The REFIT dataset has been adapted: a household has been annotated to indicate anomalies relating to refrigerator/freezer appliances.

**Challenge Program**

**Phase 1: Anomaly Detection and Classification**
- **Objective**: Detect anomalies in the signal and predict their type among the defined classes (normal, elongated, frequent)
- **Dataset**: Multi-home normal-only data + one annotated dataset
- **Expected Output**: For each timestamp, the model must produce:
  - A "normal / abnormal" decision for the refrigerator/freezer
  - A prediction of the anomaly type among the defined classes (normal, elongated, frequent), when possible given the chosen approach

The model should be designed to learn primarily from multi-home "normal-only" data. The annotated data will be used for supervised or semi-supervised training.

**Phase 2: Energy Overconsumption Estimation** *(TBC)*
- **Objective**: Same dataset as Phase 1. In addition to detection, estimate the energy impact of the abnormal state
- **Expected Output**:
  - **Instantaneous level**: Estimated overconsumption in power (W) or energy per time step
  - **Aggregated level**: Total overconsumption per anomaly episode and per home, and average overconsumption during abnormal periods

The expected methodology relies on building a "normal expected" baseline from nominal periods, then estimating the observed deviation during abnormal periods.

**Getting Started**

Check out our YouTube tutorial playlist to help you with your first steps on Codabench:

<iframe width="840" height="630" style="border:none;" allowfullscreen=""
src="https://www.youtube.com/embed/lvWF-ruQlvw?list=PLU1mBHFYvdQoq74OkE2nIuGv6BpsHv7jj">
</iframe> 


Enjoy the challenge!