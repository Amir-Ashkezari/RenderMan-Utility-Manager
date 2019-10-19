# RenderMan Utility Manager

A utility that can speeds up pre-converting tex files, ACEScg colorspace conversion, building RenderManAsset out of PBR Metallic/Roughness texture sets, denoising rendered images via Hyperion Denoise Filtering or Intel Open Image Denoise.

[Introduction Tex](https://vimeo.com/364862427)
[Introduction HyperionDenoise](https://vimeo.com/367336236)

## Features

### Tex: Export PBR texture sets to PxrSurface-based material

The asset will use the incoming textures to create the shading network. It supports Albedo/BaseColor, Roughness, Metallic, Emissive, Displacement/Height. The limitation are:

* Require keywords for each texture, e.g. *albedo*.tiff or *basecolor*.tiff, *roughness*.tiff,...