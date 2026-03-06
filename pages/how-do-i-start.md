{
  "cells": [
    {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"text-align: center;\">\n",
    "    <a href=\"https://www.hi-paris.fr/\">\n",
    "        <img border=\"0\" src=\"https://www.hi-paris.fr/wp-content/uploads/2020/09/logo-hi-paris-retina.png\" width=\"25%\"></a>\n",
    "    <a href=\"https://www.dataia.eu/\">\n",
    "        <img border=\"0\" src=\"https://github.com/ramp-kits/template-kit/raw/main/img/DATAIA-h.png\" width=\"70%\"></a>\n",
    "</div>\n",
    "\n",
    "# Audensiel - REFIT challenge\n",
    "\n",
    "<i> Team 27 </i><br/>\n",
    "<i> Ruben BUENO </i><br/>\n",
    "<i> Toscane CARRO </i><br/>\n",
    "<i> Gabriel FRANCOIS </i><br/>\n",
    "<i> Clément GAUBERT </i><br/>\n",
    "<i> Alice LATASTE </i><br/>\n",
    "<i> Soline MIGNOT </i>"
    ]
  },
      {
      "cell_type": "markdown",
      "metadata": {
        "id": "9gqbYkfiK-TE"
      },
      "source": [
        "## Introduction\n",
        "\n",
        "This challenge is based on the [REFIT](http://dx.doi.org/10.1038/sdata.2016.122) dataset, which contains electricity consumption data (both global and individual appliances) for different houses :\n",
        "\n",
        "- The R&D department of AUDENSIEL has modified these datasets for the purpose of their EcoSmartGrid project and graciously provided them for use on this challenge.\n",
        "- This challenge is an anomaly detection task applied to time series.  \n",
        "- The goal of this task is to be able to detect consumption anomalies which indicate an individual equipment is malfunctioning, via the monitoring of the house's electricity meter.\n",
        "\n",
        "\n",
        "### Anomaly Detection:\n",
        "\n",
        "Anomaly detection refers to the task of identifying observations that significantly deviate from the majority of the data. These anomalies (or outliers) are usually:\n",
        "\n",
        "- Rare\n",
        "- Difficult to label\n",
        "- Different in nature from normal patterns\n",
        "\n",
        "Most anomaly detection methods follow a common modeling principle: first learn a representation of normal data, then compute a score that quantifies how much each observation deviates from this normal behavior.\n",
        "\n",
        "### Baseline selected for the starting kit : Isolation Forest\n",
        "\n",
        "Isolation Forest is an unsupervised anomaly detection method that identifies anomalies by isolating observations rather than modeling normal behavior.  \n",
        "It builds random trees and measures how quickly a point is isolated:  \n",
        "**anomalies require fewer splits**, while normal points lie deeper in the trees.\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "C9xMBnYtK-TF"
      },
      "source": [
        "# Exploratory data analysis\n",
        "\n",
        "The data comes from four homes (H2, H3, H9, H15) from the REFIT database. The datasets have been adapted to annotate instances showing abnormal consumption related to the refrigerator/freezer. The recordings are synchronized to an 8-second time step.\n",
        "### Data Description\n",
        "The files include the following column families:   \n",
        "- `unix (int64)`: timestamp in Unix format (seconds since 1970-01-01).  \n",
        "- `time (string)`: date-time in readable format (e.g., 2014-03-21 00:00:00).  \n",
        "- `Global signal` (variable usable in production)  \n",
        "- `aggregate (float64)`: total household consumption (instantaneous power, in Watts).  \n",
        "- `Sub-measurements per appliance` (reference data)  \n",
        "Some columns may correspond to consumption per appliance (float64), including: fridge freezer, washing machine, microwave, dishwasher, washer dryer, electric space heater, television, audio system, kettle.  \n",
        "These columns are provided for reference and analysis purposes and must not be used as input variables for the model in the context of this challenge.  \n",
        "- Partial aggregate (reference data)  \n",
        "- `agg_4p (float64)`: exact aggregate of four appliances (washing machine, microwave, dishwasher, kettle).  \n",
        "- Annotations (targets)  \n",
        "- `anomaly (int64)`: label indicating the state of the refrigerator/freezer (normal or abnormal) according to the coding used in the annotated files.  \n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fffw6ooXK-TF",
        "outputId": "8f083d97-fe4a-4ca7-9ece-abdd8e0a9573",
        "colab": {
          "base_uri": "https://localhost:8080
