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
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
affiliations:
 - name: Lyman Spitzer, Jr. Fellow, Princeton University
   index: 1
date: 30 May 2020
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
#aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
#aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

Global illumination methods based on stochastic techniques provide photo-realistic images. These methods are generally based on path tracing theory in which stochastic paths are generated from the camera point of view through each pixel toward the 3D scene. The Monte Carlo theory based on the rendering equation (TODO: citation) ensures that this process will converge to the correct image when the number of paths grows (TODO: citation). However, they are prone to stochastic perceptual noise that can be reduced by increasing the number of paths as proved by Monte Carlo theory.

# `.rawls` extension

In order to tackle this perceptual noise problem, some methods have been implemented in order to variance and improve the rendered image. Unlike online rendering statisticals methods, `.rawls` (for RAW Light Simulation) extension files can be used offline into a post-processing task in order to prepare huge dataset.

A `.rawls` file stores all RGB spectrum values before gamma correction as float (32 bits) and keeps also information about generated image (renderer used).

`.rawls` contains 3 blocks and specific lines information within each block:

- IHDR:
    - __First line:__ next information line size into byte
    - __Second line:__ `{width}` `{height}` `{nbChannels}`
- COMMENTS
    - __All lines:__ information from the renderer as comment
- DATA
    - __First line:__ data block size
    - __Next lines:__ all pixels values as byte code at each line

# Why this package ?

`Rawls` Python package have been developed to manage `.rawls` files format. Files with `.rawls` extension can be generated format implemented into custom pbrt-v3 [@pharr2016physically] renderer which enables to generate `k` images of `n` samples per pixels [@pbrtp3d]. These files store fully information about generated images such as rendering parameters (number of samples, integrator, sampler, camera...) and all samples based values obtained. `Rawls` Python package can load `.rawls` file and save it into `.png`, can also merge few `.rawls` images in order to extracts statisticals information from samples for each pixels distribution (such as Mean, Variance, Skewness, Kurtosis).

As example, if we have a pool $10000$ images of $1$ sample per pixel, we can generate $\binom{10000}{k}$ of $k$ samples from pool of $10000$ samples. In this way, deep learning techniques such as Autoencoder can be used for noise reduction as it's possible to have a huge image database.

Example of comments data kept for a `.rawls` file using Python package:
```sh
--------------------------------------------------------
Shape: 
        (1080, 1920, 3)
Details: 
        Samples 20
        Filter: default
        Resolution: 1920 x 1080
        Sampler: `halton` 
                - samples: 100
        Accelerator: default
        Integrator: `path` 
                - maxdepth: 10
        Camera: `perspective` 
                - fov: 28.0
        LookAt: 
                - eye: (32.5772, -11.5177, 5.28233) 
                - point: (32.1838, -10.6715, 4.92289) 
                - up: (0.0, 0.0, 1.0)
Gamma converted: 
        False
--------------------------------------------------------
```

# Acknowledgements

ANR support : project ANR-17-CE38-0009

# References