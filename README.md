# Solar-Resilience-PIML-Sylhet
**Physics-Informed Machine Learning for Solar PV Stability in Sylhet, Bangladesh.**

## 1. Research Objective
This project aims to model solar energy reliability specifically for surgical and critical care facilities in the Sylhet region. By utilizing **Physics-Informed Machine Learning (PIML)**, we constrain standard Neural Networks with the physical laws of photovoltaics to ensure high-accuracy forecasting even with sparse local data.

## 2. Methodology
* **Data Source:** NASA POWER API (Long-term solar irradiance & temperature).
* **Physics Constraints:** Incorporating the Beer-Lambert law and temperature-coefficient efficiency drops.
* **Optimization:** Reducing Levelized Cost of Energy (LCOE) for local microgrids.

## 3. Structure
* `src/piml`: Physics-informed neural network architectures.
* `src/economics`: Solar ROI and resilience metrics.
* `data/`: (Not tracked in Git) Local meteorological time-series.