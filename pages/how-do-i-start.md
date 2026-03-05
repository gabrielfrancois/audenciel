# How do I start?           
                           

This section will give you a description of the dataset and baseline methods suggested by the organizers.

                           
## Data   


### Provided energy consumption reference data


The data comes from four homes (H2, H3, H9, H15) from the REFIT database. The datasets have been adapted to annotate instances showing abnormal consumption related to the refrigerator/freezer. The recordings are synchronized to an 8-second time step.
Data Description
The files include the following column families:
Temporal columns

- `unix (int64)`: timestamp in Unix format (seconds since 1970-01-01).
- `time (string)`: date-time in readable format (e.g., 2014-03-21 00:00:00).
- `Global signal` (variable usable in production)
- `aggregate (float64)`: total household consumption (instantaneous power, in Watts).
- `Sub-measurements per appliance` (reference data)

Some columns may correspond to consumption per appliance (float64), including:
fridge freezer, washing machine, microwave, dishwasher, washer dryer, electric space heater, television, audio system, kettle.

These columns are provided for reference and analysis purposes and must not be used as input variables for the model in the context of this challenge.

- Partial aggregate (reference data)

- `agg_4p (float64)`: exact aggregate of four appliances (washing machine, microwave, dishwasher, kettle).

- Annotations (targets)

- `anomaly (int64)`: label indicating the state of the refrigerator/freezer (normal or abnormal) according to the coding used in the annotated files.
type_defaut_fridge_freezzer (int64): associated anomaly type (observed values: 0, 1, 2).

To avoid any ambiguity, the convention adopted in this challenge is as follows:

type_defaut_fridge_freezzer = 0: normal state, no anomaly;
type_defaut_fridge_freezzer = 1: prolonged duration fault (Elongated);
type_defaut_fridge_freezzer = 2: frequency fault (Frequent).

Dataset Availability

H2: "normal-only" file (all observations are normal).
H15: "normal-only" file (all observations are normal).
H3: one "normal-only" file and one annotated file (presence of anomaly variable and type).

The "normal-only" files are intended for learning nominal behavior. The annotated files (H3) allow training on abnormal behaviors, depending on the chosen strategy (supervised, semi-supervised, or unsupervised approaches).
Fault Type Definitions
Two types of anomalies are considered:

Prolonged duration fault (Elongated): the compressor remains active longer than usual, resulting in overconsumption and abnormal stability of the consumption pattern.
Frequency fault (Frequent): the compressor switches abnormally frequently between active/inactive states, inducing atypical switching cycles that may reveal a malfunction.


### PHASE 1
  
The provided dataset allows for training of a ML model that should output :
- **an anomaly status** for each timestamp
- **the type of anomaly** 



### PHASE 2 (TBC)

In Phase 2, the same dataset shall be used in order to evaluate the estimated overconsumption in power (W) per time step, both instantaneous and at the Aggregated level.


## Baselines                 

A baseline is a simple approach designed to address the problem raised by the challenge, in this case multi-omic deconvolution. It serves as a straightforward method that is easy to understand and provides a foundation for further improvements.
The starting kit contains 1 baseline.

**submission_script.py** - This file uses a common anomaly detection algorithm
