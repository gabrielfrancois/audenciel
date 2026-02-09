# Overview                 
                           
Welcome to the *AUDENSIEL - REFIT* data challenge. 

The *Health Data Challenge (HADACA)* is a series of data challenges aimed at benchmarking deconvolution methods through crowdsourcing. The primary goal is to develop and improve deconvolution methods for biological data.

- The **first edition** took place in 2018, in collaboration with the Data Institute at University Grenoble-Alpes.
- The **second edition** was held in 2019, in partnership with the Ligue contre le Cancer and sponsored by EIT Health.
- The **third edition** will be in December 2024, in collaboration with the M4DI project, part of the PEPR Santé Numérique. Visit the official website for details: http://hadaca3.sciencesconf.org.
    
                           
**Aim of the challenge**     
                           
Cellular heterogeneity in tumors is a key factor that determines disease progression and influences biomedical analysis of samples and patient classification.

At the molecular level, the cellular composition of tissues is difficult to assess and quantify, as it is hidden within the bulk molecular profiles of samples (average profile of millions of cells), with all cells present in the tissue contributing to the recorded signal. Despite great promise, conventional computational approaches to quantifying cellular heterogeneity from mixtures of cells have encountered difficulties in providing robust and biologically relevant estimates.

Here, our focus will be on reference-based approaches, which are gaining increasing popularity. While each method presents its own advantages and limitations, all are inherently constrained by the quality of the reference data employed. Our hypothesis is that integrating multimodal data can improve the quality of the reference data and, in turn, enhance the performance of deconvolution algorithms.

The *HADACA3* challenge aims to improve existing cell-type deconvolution models by integrating multimodal datasets as reference data.

**Program**

**Phase 1**: 

- Objective: Detect anomalies in the signal and predict its type among the defined classes (normal, elongated, frequent)

- Dataset: the normal-only data and one of the annotated dataset.

For each timestamp, the model must produce:
- a "normal / abnormal" decision for the refrigerator/freezer;
- a prediction of the anomaly type among the defined classes (normal, elongated, frequent), when possible given the chosen approach.

The model should be designed to learn primarily from multi-home "normal-only" data.
  
    
**Phase 2 - TBC**:

- Objective: Same dataset than in Phase 1. In addition to detection, participants are asked to estimate the energy impact of the abnormal state of the refrigerator/freezer.
- Results should be provided:
- at the instantaneous level: estimated overconsumption in power (W) or energy per time step;
at the aggregated level: total overconsumption per anomaly episode and per home, and average overconsumption during abnormal periods.

The expected methodology relies on building a "normal expected" baseline from nominal periods, then estimating the observed deviation during abnormal periods.



**Tutorial**

There is a playlist of YouTube videos to help you with your first steps on Codabench. 

 <iframe width="840" height="630" style="border:none;" allowfullscreen=""
src="https://www.youtube.com/embed/lvWF-ruQlvw?list=PLU1mBHFYvdQoq74OkE2nIuGv6BpsHv7jj">
</iframe> 

Enjoy the challenge!                           
