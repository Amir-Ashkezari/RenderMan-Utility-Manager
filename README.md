# RenderMan Utility Manager

A utility that can speeds up pre-converting tex files, ACEScg colorspace conversion, building RenderManAsset out of PBR Metallic/Roughness texture sets, denoising rendered images via Hyperion Denoise Filtering or Intel Open Image Denoise.

[Introduction Tex](https://vimeo.com/364862427)

[Introduction HyperionDenoise](https://vimeo.com/367336236)

## Features

### Tex: Building RenderManAsset out of PBR Metallic/Roughness texture sets

It will use the incoming texture files to create the PxrSurface-based material. It supports Albedo/BaseColor, Roughness, Metallic, Emissive, Displacement/Height. It will lookup for these keywords in the texture filename to construct the asset.
* UDIM supported.

### Tex: ACEScg colorspace conversion

It will use ocioconvert utility for converting incoming texture files to ACEScg colorspace. 

### HyperionDenoise

It uses Hyperion Denoise Filtering (RenderMan denoise tool) to filter incoming rendered images.

### OIDenoise

It uses Intel Open Image Denoise example to filter incoming rendered images.

## Requirements

This utility require the following software to operate:

* RenderMan Pro Server 21.0+
* [OpenColorIO-tools](https://opencolorio.org/userguide/tool_overview.html#ocioconvert)
* [Intel Open Image Denoise example](https://openimagedenoise.github.io/downloads.html)
* [ImageMagick](https://imagemagick.org/script/download.php)

## Known Issues

* No progress indication during process.

## Release notes

### 0.6

* Added
  * Hyperion Denoise Filtering
  * Intel Open Image Denoise
  
* Fixed
  * Open IT context menu no longer freezes the gui

### 0.2.1

* Added
  * PxrManifold2D to shading graph

* Updates
  * Albedo or basecolor keyword can be recognized for PBR Metallic/Roughness mode
  * Metallic map is no longer mandatory for PBR Metallic/Roughness mode

### 0.2

* Added

  * Displacement/height to PBR Metallic/Roughness mode
  * OpenGL and DirectX normal orientation to PBR Metallic/Roughness mode
  
* Fixed
  * An issue when trying to open images in the selection dailog via openIT context menu
  
### 0.1

* Added
  * Pre converting tex files
  * ACEScg colorspace conversion
  * Buidling RenderManAsset out of PBR Metallic/Roughness texture sets
