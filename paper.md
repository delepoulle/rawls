---
title: 'Rawls: A Python package for managing .rawls image files'
tags:
  - Python
  - Computer Graphics
  - Statistics
  - Global illumination
authors:
  - name: Jérôme BUISINE
    orcid: 0000-0001-6071-744X
    affiliation: 1 # (Multiple affiliations must be quoted)
affiliations:
 - name: Univ. Littoral Côte d’Opale, LISIC Calais, France, F-62100
   index: 1
date: 2 June 2020
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
#aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
#aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

![Scheme of global illumination rendering of 3D scene.\label{fig:path-tracing}](docs/source/_static/path-tracing.png){ width=60% }

Global illumination methods based on stochastic techniques provide photo-realistic images. These methods are generally based on path tracing theory in which stochastic paths are generated from the camera point of view through each pixel toward the 3D scene (see \autoref{fig:path-tracing}). The Monte Carlo theory based on the rendering equation [@kajiya1986rendering] ensures that this process will converge to the correct image when the number of paths grows [@kollig2002efficient]. However, they are prone to stochastic perceptual noise that can be reduced by increasing the number of paths (see \autoref{fig:noise-overview}) as proved by Monte Carlo theory but requires a lot of time to generate such image. 

![Overview of noise evolution during rendering.\label{fig:noise-overview}](docs/source/_static/noise-overview.png)

# `.rawls` extension

In order to tackle this perceptual noise problem, some methods have been implemented in order to reduce variance and improve the rendered image [@delbracio2014boosting; @boughida2017bayesian]. Unlike online rendering statisticals methods, `.rawls` (for RAW Light Simulation) extension files can be used offline into a post-processing task in order to prepare huge dataset.

A `.rawls` file is a custom image file obtained as output of renderer. These files keep fully information about generated images such as rendering parameters (number of samples, integrator, sampler, camera...) and store all RGB spectrum values before gamma correction as float (32 bits).

`.rawls` contains 3 blocks and specific lines information within each block:

- **IHDR:**
    - __First line:__ next line size information (into bytes)
    - __Second line:__ `{width}` `{height}` `{nbChannels}`
- **COMMENTS:**
    - __All lines:__ information from the renderer as comment
- **DATA:**
    - __First line:__ data block size
    - __Next lines:__ all pixels values as bytes code at each line

# Motivation

`Rawls` Python package have been developed to manage `.rawls` files format. Files with `.rawls` extension can be generated using custom pbrt-v3 [@pharr2016physically] renderer which enables to generate `k` images of `n` samples per pixels [@pbrtp3d] of the same `.pbrt` file 3D scene. `Rawls` Python package can load `.rawls` file, save it into `.png`, can also merge few `.rawls` images in order to extracts statisticals information from samples for each pixels distribution (such as Mean, Variance, Skewness, Kurtosis). As the distributions of pixels when rendering an image do not seem to follow a Gaussian law, paying attention to their distribution seems interesting.

# Application

If we have a pool $10000$ images of $1$ sample per pixel, we can generate $\binom{10000}{k}$ of $k$ samples from pool of $10000$ samples. In this way, deep learning techniques such as Autoencoder [@xie2012image; @chaitanya2017interactive] can be used for noise reduction as it's possible to have a huge image database.

# Acknowledgements

ANR support : project ANR-17-CE38-0009

# References